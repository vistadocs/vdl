---
title: HL7 HL*1.6 HLO VMS Developer Manual
doc_type: API
doc_label: API Manual
doc_layer: anchor
doc_subject: HLO VMS Developer Manual
app_code: HL7
app_name: HL7 (VistA Messaging)
section: INF
app_status: active
pkg_ns: 
patch_ver: 1.6
patch_id: 
group_key: "HL7::1.6"
file_numbers: 
  - 777
  - 778
  - 7870
security_keys: []
menu_options: 11
description: "HLO provides the developer with a set of APIs for building messaging applications. The following is an outline of the development process:"
audience: 
keywords: 
  - message
  - application
  - class
  - segment
  - table
  - style
  - messages
  - colspan
  - width
  - contents
page_count: 0
word_count: 40615
section_count: 43
table_count: 53
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Health_Level_7_(HL7)/vms_hlo_developer_manual.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Health_Level_7_(HL7)/vms_hlo_developer_manual.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=8"
---

VistA Messaging Services

Health Level Seven Optimized (HLO)

Developer Manual

![](hl7-hl-1-6-hlo-vms-developer-manual/001.png)

Software HL\*1.6

Document Revision 1.3

VA Office of Information and Technology (OI&T)

Veterans Health Information Technology (VHIT)

VistA Messaging Services

(*This page left blank for two sided printing*)

Revision History

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 40%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date</td>
<td>Revision</td>
<td>Description</td>
<td>Author</td>
</tr>
<tr class="even">
<td>5/20/09</td>
<td>1</td>
<td>Created document (VMS_CR1261)</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>8/4/09</td>
<td>1.1</td>
<td>Technical Edit (VMS_CR1261)</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>9/28/09</td>
<td>1.2</td>
<td>Technical Edit (VMS_CR1261)</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/5/16</td>
<td>1.3</td>
<td><p>VistA Maintenance patch HL*1.6*166 –</p>
<p>Updated description of Count Messages on Outgoing Queues, pg. 91</p></td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

(*This page left blank for two sided printing*)

Contents

1.0 Introduction [1](#introduction)

1.1 Scope of this Manual [1](#scope-of-this-manual)

1.2 The HL7 Standard [2](#the-hl7-standard)

1.2.1 HL7 Version [2](#hl7-version)

1.2.2 Supported Communication Protocols [2](#supported-communication-protocols)

1.2.3 HL7 Messages [2](#hl7-messages)

1.2.3.1 Individual Messages [2](#individual-messages)

1.2.3.2 Batch Messages [4](#batch-messages)

1.2.4 Local Customizations [4](#local-customizations)

1.2.5 Data Types and Tables [4](#data-types-and-tables)

1.2.6 Message Acknowledgments [5](#message-acknowledgments)

1.2.7 Message Delimiters [5](#message-delimiters)

1.2.8 Escape Sequences [5](#escape-sequences)

1.3 Application’s Responsibilities Versus HLO’s Responsibilities [6](#applications-responsibilities-versus-hlos-responsibilities)

1.3.1 HLO [6](#hlo)

1.3.2 Application [6](#application)

1.4 HLO Client-Server Behavior [7](#hlo-client-server-behavior)

1.4.1 HLO Client Behavior [7](#hlo-client-behavior)

1.4.1.1 The Outgoing Queue Structure [7](#the-outgoing-queue-structure)

1.4.1.2 The Client Algorithm [7](#the-client-algorithm)

1.4.2 HLO Server Behavior [8](#hlo-server-behavior)

1.4.2.1 The Server Algorithm [8](#the-server-algorithm)

1.4.2.2 The Incoming Queue Structure [9](#the-incoming-queue-structure)

1.5 Features Not Supported by HLO [9](#features-not-supported-by-hlo)

1.6 Special Considerations for Interfacing HLO to COTS, Middleware, or Other Messaging Applications [9](#special-considerations-for-interfacing-hlo-to-cots-middleware-or-other-messaging-applications)

2.0 Building and Sending HL7 Messages [10](#building-and-sending-hl7-messages)

2.1 Overview [10](#overview)

2.2 Create an Entry in the HLO Application Registry File for the Sending Application [12](#create-an-entry-in-the-hlo-application-registry-file-for-the-sending-application)

2.3 Create Entries in the HL Logical Link File for Each Destination [13](#create-entries-in-the-hl-logical-link-file-for-each-destination)

2.4 The MSH, BHS, and BTS Segments [14](#the-msh-bhs-and-bts-segments)

2.4.1 HLO’s MSH Segment [14](#hlos-msh-segment)

2.4.2 HLO’s BHS Segment [15](#hlos-bhs-segment)

2.4.3 HLO’s BTS Segment [16](#hlos-bts-segment)

2.5 List of Message Building APIs [17](#list-of-message-building-apis)

2.6 The HLO Framework for Message Building [18](#the-hlo-framework-for-message-building)

2.6.1 New-Style Message Building [19](#new-style-message-building)

2.6.1.1 Pattern 1 – Building a Segment [19](#pattern-1-building-a-segment)

2.6.1.2 Pattern 2 – Building an Individual Message [20](#pattern-2-building-an-individual-message)

2.6.1.3 Pattern 3 – Building a Batch Message [20](#pattern-3-building-a-batch-message)

2.6.2 Traditional Style Message Building [21](#traditional-style-message-building)

2.6.2.1 Pattern 4 Building an Individual Message in the Traditional Style [21](#pattern-4-building-an-individual-message-in-the-traditional-style)

2.6.3 Hybrid Style Message Building [21](#hybrid-style-message-building)

2.6.3.1 Pattern 5 – Mixing Traditional Style and New Style Segment Builders [21](#pattern-5-mixing-traditional-style-and-new-style-segment-builders)

2.6.3.2 Pattern 6 – Traditional Message Building without Protocols [22](#pattern-6-traditional-message-building-without-protocols)

2.7 Application Callbacks [22](#_Toc241910354)

2.7.1 Callback for Application Acknowledgments [22](#callback-for-application-acknowledgments)

2.7.2 Callback for Commit Acknowledgments [22](#_Toc241910356)

2.7.3 Callbacks for Messages that Fail to Transmit [23](#callbacks-for-messages-that-fail-to-transmit)

2.8 Sequence Queues [23](#_Toc241910358)

2.8.1 The Algorithm [23](#the-algorithm)

2.8.1.1 Client Role: [23](#client-role)

2.8.1.2 Server Role: [24](#server-role)

2.8.2 Using Sequence Queues [24](#using-sequence-queues)

2.9 HLO Subscription Registry [24](#hlo-subscription-registry)

2.9.1 The User Interface for Creating Subscription Lists [25](#_Toc241910364)

2.9.2 The Programming Interface for Creating Subscription Lists [26](#_Toc241910365)

2.10 Turning Messaging On/Off [27](#_Toc241910366)

3.0 Receiving Messages [28](#receiving-messages)

3.1 Setting up the Receiving Application in the HLO Application Registry [28](#setting-up-the-receiving-application-in-the-hlo-application-registry)

3.2 List of Message Parsing APIs [30](#list-of-message-parsing-apis)

3.3 HLO Parses the Message Header [31](#_Toc241910370)

3.3.1 Parsing the MSH Segment [31](#_Toc241910371)

3.3.2 Parsing the BHS Segment [32](#parsing-the-bhs-segment)

3.4 Stepping Through an Individual Message [33](#stepping-through-an-individual-message)

3.4.1 Method 1 – Using \$\$NEXTSEG^HLOPRS [34](#method-1-using-nextseghloprs)

3.4.2 Method 2 – Using \$\$HLNEXT^HLOMSG [35](#method-2-using-hlnexthlomsg)

3.4.3 Examples of Message Parsing [35](#examples-of-message-parsing)

3.5 Stepping through a Batch of Messages [36](#stepping-through-a-batch-of-messages)

4.0 Acknowledgement Messages [38](#acknowledgement-messages)

4.1 Requesting Acknowledgments [38](#requesting-acknowledgments)

4.2 Returning Acknowledgments [40](#returning-acknowledgments)

4.2.1 Commit Acknowledgments [40](#commit-acknowledgments)

4.2.2 Application Acknowledgments [40](#application-acknowledgments)

4.2.3 Determining the Return Destination [42](#determining-the-return-destination)

5.0 API Reference Guide [43](#_Toc241910384)

5.1 Sending Messages [45](#sending-messages)

5.1.1 Start Building a New Message [45](#start-building-a-new-message)

5.1.2 Start Building a New Batch of Messages [46](#start-building-a-new-batch-of-messages)

5.1.3 Add a New Message to a Batch [47](#_Toc241910388)

5.1.4 Add a Segment to a Message [48](#add-a-segment-to-a-message)

5.1.5 Move Traditional-Style Message Array into an HLO Message [48](#move-traditional-style-message-array-into-an-hlo-message)

5.1.6 Move Traditional-Style Segment Array into HLO [50](#move-traditional-style-segment-array-into-hlo)

5.1.7 Setting Data Types into a Segment [51](#setting-data-types-into-a-segment)

5.1.7.1 Set Value (Unspecified Data Type) [51](#set-value-unspecified-data-type)

5.1.7.2 Set Address [52](#set-address)

5.1.7.3 Set Coded Element [53](#set-coded-element)

5.1.7.4 Set Coded Element with No Exceptions [54](#set-coded-element-with-no-exceptions)

5.1.7.5 Set Coded Value with Exceptions [56](#set-coded-value-with-exceptions)

5.1.7.6 Set Date [56](#set-date)

5.1.7.7 Set Hierarchic Designator [57](#set-hierarchic-designator)

5.1.7.8 Set Timestamp [59](#set-timestamp)

5.1.7.9 Set Extended Person Name [59](#set-extended-person-name)

5.1.8 Completing and Sending Messages [61](#_Toc241910402)

5.1.8.1 Send a Single Message [62](#send-a-single-message)

5.1.8.2 Send Messages to a List of Destinations [63](#_Toc241910404)

5.1.8.3 Send Messages via the HLO Subscription Registry to a List of Subscribers [65](#_Toc241910405)

5.1.8.4 Send Messages via HL7 1.6 Protocol Setup [66](#send-messages-via-hl7-1.6-protocol-setup)

5.2 Parsing Messages [68](#parsing-messages)

5.2.1 Start Parsing a Message [68](#start-parsing-a-message)

5.2.2 Advance to the Next Message within a Batch [70](#advance-to-the-next-message-within-a-batch)

5.2.3 Advance to and Parse the Next Segment [70](#advance-to-and-parse-the-next-segment)

5.2.4 Get Next Segment [71](#get-next-segment)

5.2.5 Get Message ID [72](#get-message-id)

5.2.6 Parsing Data Types [72](#parsing-data-types)

5.2.6.1 Get Value (Unspecified Data Type) [72](#get-value-unspecified-data-type)

5.2.6.2 Get Address [73](#get-address)

5.2.6.3 Get Coded Element [74](#get-coded-element)

5.2.6.4 Get Coded Element with No Exceptions [75](#get-coded-element-with-no-exceptions)

5.2.6.5 Get Coded Element with Exceptions [75](#get-coded-element-with-exceptions)

5.2.6.6 Get Date [76](#get-date)

5.2.6.7 Get Hierarchic Designator [77](#get-hierarchic-designator)

5.2.6.8 Get Timestamp [78](#get-timestamp)

5.2.6.9 Get Extended Person Name [78](#get-extended-person-name)

5.3 Returning Application Acknowledgments [79](#returning-application-acknowledgments)

5.3.1 Begin Application Acknowledgment for an Individual Message [79](#begin-application-acknowledgment-for-an-individual-message)

5.3.2 Begin Batch Application Acknowledgement [81](#begin-batch-application-acknowledgement)

5.3.3 Add an Application Acknowledgement to a Batch [82](#add-an-application-acknowledgement-to-a-batch)

5.3.4 Send the Application Acknowledgement. [82](#send-the-application-acknowledgement.)

5.4 Subscription Registry [83](#subscription-registry)

5.4.1 Create an Entry in the Subscription Registry [83](#create-an-entry-in-the-subscription-registry)

5.4.2 Add a New Recipient to a Subscription Registry Entry [84](#add-a-new-recipient-to-a-subscription-registry-entry)

5.4.3 Terminate a Recipient from a Subscription Registry Entry [85](#terminate-a-recipient-from-a-subscription-registry-entry)

5.4.4 Check Subscription Registry Entry for a Recipient [86](#check-subscription-registry-entry-for-a-recipient)

5.4.5 Retrieve Next Recipient from a Subscription Registry Entry [86](#retrieve-next-recipient-from-a-subscription-registry-entry)

5.4.6 Build a Subscription Registry Index [87](#build-a-subscription-registry-index)

5.4.7 Find a Subscription Registry Entry [87](#find-a-subscription-registry-entry)

5.5 Miscellaneous APIs [88](#miscellaneous-apis)

5.5.1 Resend a Message [88](#resend-a-message)

5.5.2 Reprocess a Message [88](#reprocess-a-message)

5.5.3 Reprocess a Message Immediately [88](#reprocess-a-message-immediately)

5.5.4 Reset the Purge Date and Time for a Message [90](#reset-the-purge-date-and-time-for-a-message)

5.5.5 Count Messages on All Queues [91](#count-messages-on-all-queues)

5.5.6 Count Messages on Outgoing Queues [91](#count-messages-on-outgoing-queues)

5.5.7 Count of Messages on Incoming Queues [92](#count-of-messages-on-incoming-queues)

5.5.8 Count of the number of messages on the sequence queues. [92](#count-of-the-number-of-messages-on-the-sequence-queues.)

6.0 Code Examples [93](#code-examples)

6.1 HLODEM1 [93](#hlodem1)

6.2 HLODEM2 [97](#hlodem2)

6.3 HLODEM3 [101](#hlodem3)

6.4 HLODEM4 [103](#hlodem4)

6.5 HLODEM5 [104](#hlodem5)

6.6 HLODEM6 [107](#hlodem6)

6.7 HLODEM7 [110](#hlodem7)

6.8 HLODEM8 [111](#hlodem8)

6.9 HLODEM9 [112](#hlodem9)

6.10 HLODEM10 [113](#hlodem10)

7.0 Quick Overview of the HLO User Interface [116](#quick-overview-of-the-hlo-user-interface)

7.1 HLO Main Menu [116](#hlo-main-menu)

7.2 HLO System Monitor [117](#hlo-system-monitor)

8.0 Troubleshooting for the Developer [121](#troubleshooting-for-the-developer)

8.1 The Client Trace Tool [121](#the-client-trace-tool)

8.2 The Server Trace Tool [123](#the-server-trace-tool)

(*This page left blank for two sided printing*)

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
  - [## Scope of this Manual](#scope-of-this-manual)
  - [## The HL7 Standard](#the-hl7-standard)
    - [### HL7 Version](#hl7-version)
    - [### Supported Communication Protocols](#supported-communication-protocols)
    - [### HL7 Messages](#hl7-messages)
    - [Local Customizations](#local-customizations)
    - [Data Types and Tables](#data-types-and-tables)
    - [Message Acknowledgments](#message-acknowledgments)
    - [Message Delimiters](#message-delimiters)
    - [Escape Sequences](#escape-sequences)
  - [Application’s Responsibilities Versus HLO’s Responsibilities](#applications-responsibilities-versus-hlos-responsibilities)
    - [HLO](#hlo)
    - [Application](#application)
  - [HLO Client-Server Behavior](#hlo-client-server-behavior)
    - [HLO Client Behavior](#hlo-client-behavior)
    - [HLO Server Behavior](#hlo-server-behavior)
  - [Features Not Supported by HLO](#features-not-supported-by-hlo)
  - [Special Considerations for Interfacing HLO to COTS, Middleware, or Other Messaging Applications](#special-considerations-for-interfacing-hlo-to-cots-middleware-or-other-messaging-applications)
- [Building and Sending HL7 Messages](#building-and-sending-hl7-messages)
  - [Overview](#overview)
  - [Create an Entry in the HLO Application Registry File for the Sending Application](#create-an-entry-in-the-hlo-application-registry-file-for-the-sending-application)
  - [Create Entries in the HL Logical Link File for Each Destination](#create-entries-in-the-hl-logical-link-file-for-each-destination)
  - [The MSH, BHS, and BTS Segments](#the-msh-bhs-and-bts-segments)
    - [HLO’s MSH Segment](#hlos-msh-segment)
    - [HLO’s BHS Segment](#hlos-bhs-segment)
    - [HLO’s BTS Segment](#hlos-bts-segment)
  - [List of Message Building APIs](#list-of-message-building-apis)
  - [The HLO Framework for Message Building](#the-hlo-framework-for-message-building)
    - [New-Style Message Building](#new-style-message-building)
    - [Traditional Style Message Building](#traditional-style-message-building)
    - [Hybrid Style Message Building](#hybrid-style-message-building)
  - [Application Callbacks](#application-callbacks)
    - [Callback for Application Acknowledgments](#callback-for-application-acknowledgments)
    - [Callback for Commit Acknowledgments](#callback-for-commit-acknowledgments)
    - [Callbacks for Messages that Fail to Transmit](#callbacks-for-messages-that-fail-to-transmit)
  - [Sequence Queues](#sequence-queues)
    - [The Algorithm](#the-algorithm)
    - [Using Sequence Queues](#using-sequence-queues)
  - [HLO Subscription Registry](#hlo-subscription-registry)
    - [The User Interface for Creating Subscription Lists](#the-user-interface-for-creating-subscription-lists)
    - [The Programming Interface for Creating Subscription Lists](#the-programming-interface-for-creating-subscription-lists)
  - [Turning Messaging On/Off](#turning-messaging-onoff)
- [Receiving Messages](#receiving-messages)
  - [Setting up the Receiving Application in the HLO Application Registry](#setting-up-the-receiving-application-in-the-hlo-application-registry)
  - [## ## List of Message Parsing APIs](#list-of-message-parsing-apis)
  - [HLO Parses the Message Header](#hlo-parses-the-message-header)
    - [Parsing the MSH Segment](#parsing-the-msh-segment)
    - [Parsing the BHS Segment](#parsing-the-bhs-segment)
  - [Stepping Through an Individual Message](#stepping-through-an-individual-message)
    - [Method 1 – Using \$\$NEXTSEG^HLOPRS](#method-1-using-nextseghloprs)
    - [Method 2 – Using \$\$HLNEXT^HLOMSG](#method-2-using-hlnexthlomsg)
    - [Examples of Message Parsing](#examples-of-message-parsing)
  - [Stepping through a Batch of Messages](#stepping-through-a-batch-of-messages)
- [Acknowledgement Messages](#acknowledgement-messages)
  - [Requesting Acknowledgments](#requesting-acknowledgments)
  - [Returning Acknowledgments](#returning-acknowledgments)
    - [Commit Acknowledgments](#commit-acknowledgments)
    - [Application Acknowledgments](#application-acknowledgments)
    - [Determining the Return Destination](#determining-the-return-destination)
- [API Reference Guide](#api-reference-guide)
  - [Sending Messages](#sending-messages)
    - [Start Building a New Message](#start-building-a-new-message)
    - [Start Building a New Batch of Messages](#start-building-a-new-batch-of-messages)
    - [Add a New Message to a Batch](#add-a-new-message-to-a-batch)
    - [Add a Segment to a Message](#add-a-segment-to-a-message)
    - [Move Traditional-Style Message Array into an HLO Message](#move-traditional-style-message-array-into-an-hlo-message)
    - [Move Traditional-Style Segment Array into HLO](#move-traditional-style-segment-array-into-hlo)
    - [Setting Data Types into a Segment](#setting-data-types-into-a-segment)
    - [Completing and Sending Messages](#completing-and-sending-messages)
  - [Parsing Messages](#parsing-messages)
    - [Start Parsing a Message](#start-parsing-a-message)
    - [Advance to the Next Message within a Batch](#advance-to-the-next-message-within-a-batch)
    - [Advance to and Parse the Next Segment](#advance-to-and-parse-the-next-segment)
    - [Get Next Segment](#get-next-segment)
    - [Get Message ID](#get-message-id)
    - [Parsing Data Types](#parsing-data-types)
  - [Returning Application Acknowledgments](#returning-application-acknowledgments)
    - [Begin Application Acknowledgment for an Individual Message](#begin-application-acknowledgment-for-an-individual-message)
    - [Begin Batch Application Acknowledgement](#begin-batch-application-acknowledgement)
    - [Add an Application Acknowledgement to a Batch](#add-an-application-acknowledgement-to-a-batch)
    - [Send the Application Acknowledgement.](#send-the-application-acknowledgement)
  - [Subscription Registry](#subscription-registry)
    - [Create an Entry in the Subscription Registry](#create-an-entry-in-the-subscription-registry)
    - [Add a New Recipient to a Subscription Registry Entry](#add-a-new-recipient-to-a-subscription-registry-entry)
    - [Terminate a Recipient from a Subscription Registry Entry](#terminate-a-recipient-from-a-subscription-registry-entry)
    - [Check Subscription Registry Entry for a Recipient](#check-subscription-registry-entry-for-a-recipient)
    - [Retrieve Next Recipient from a Subscription Registry Entry](#retrieve-next-recipient-from-a-subscription-registry-entry)
    - [Build a Subscription Registry Index](#build-a-subscription-registry-index)
    - [Find a Subscription Registry Entry](#find-a-subscription-registry-entry)
  - [Miscellaneous APIs](#miscellaneous-apis)
    - [Resend a Message](#resend-a-message)
    - [Reprocess a Message](#reprocess-a-message)
    - [Reprocess a Message Immediately](#reprocess-a-message-immediately)
    - [Reset the Purge Date and Time for a Message](#reset-the-purge-date-and-time-for-a-message)
    - [Count Messages on All Queues](#count-messages-on-all-queues)
    - [Count Messages on Outgoing Queues](#count-messages-on-outgoing-queues)
    - [Count of Messages on Incoming Queues](#count-of-messages-on-incoming-queues)
    - [Count of the number of messages on the sequence queues.](#count-of-the-number-of-messages-on-the-sequence-queues)
- [Code Examples](#code-examples)
  - [HLODEM1](#hlodem1)
  - [HLODEM2](#hlodem2)
  - [HLODEM3](#hlodem3)
  - [HLODEM4](#hlodem4)
  - [HLODEM5](#hlodem5)
  - [HLODEM6](#hlodem6)
  - [HLODEM7](#hlodem7)
  - [HLODEM8](#hlodem8)
  - [HLODEM9](#hlodem9)
  - [HLODEM10](#hlodem10)
- [Quick Overview of the HLO User Interface](#quick-overview-of-the-hlo-user-interface)
  - [HLO Main Menu](#hlo-main-menu)
  - [HLO System Monitor](#hlo-system-monitor)
- [Troubleshooting for the Developer](#troubleshooting-for-the-developer)
  - [The Client Trace Tool](#the-client-trace-tool)
  - [The Server Trace Tool](#the-server-trace-tool)
VistA’s Health Level Seven Optimized (HLO) software is VistA’s newest software that supports Health Level Seven (HL7) messaging for VistA MUMPS (M) applications. It was released in patch HL\*1.6\*126. It consists of:
1.  A set of Application Programming Interfaces (APIs) that VistA M developers use to build and transmit HL7 messages, and receive and parse HL7 messages.
2.  A messaging engine, consisting of a client and a server, that sends and receives HL7 messages between systems.
3.  A user interface that sites use to control and monitor the HL7 messaging, and view messages, message errors, and message statistics.
This manual is a guide to those who are developing HL7 interfaces using HLO, either between two VistA systems, or between a VistA system and a Commercial Off-the-Shelf (COTS) or other non-VistA system. It assumes familiarity with the HL7 standard.
HLO coexists with the earlier HL7 software. *In this document the older software will be referred to as’HL7 1.6’.* Messaging applications that were developed prior to HLO will continue to use HL7 1.6, though it is recommended that new applications use HLO.
> **NOTE:** In this document the older software will be referred to as’HL7 1.6’.

## ## Scope of this Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual is concerned with the technical aspects of using HLO to build a messaging application. Among the steps involved in interfacing systems that are not discussed are:

- Analysis of the data that needs to be exchanged. This requires individuals with in-depth knowledge of the information domain and the functions of the systems being interfaced.
- Determining the HL7 messages that are needed to exchange the information.
- Detailed analysis of the data and compatibility issues between the two systems. For example, if the two systems use different code systems to record lab tests, then conversion of the data from one code system to another may be a factor to consider.
- Negotiation, documentation, and approval of the interface specification.
- Determination of the trigger events that must be responded to by the messaging. For example, in a patient appointment scheduling system, is a message needed when an appointment is cancelled? The HL7 standard provides a wide variety of event types that may be implemented.
- Detailed analysis of the sending application software to determine how to insert hooks to implement the desired trigger events. For example, if an interface is to include notification of an appointment cancellation then that requires a detailed analysis of the scheduling system software to determine at which point, or points, the hooks need to be inserted. It may be within a routine, an option, protocol, or other components that make up software within VistA. When those points are determined, the interface developer needs to insert a call to a routine that uses the HLO APIs to build and send the appropriate HL7 message – that IS a topic within the scope of this manual.

## ## The HL7 Standard

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL7 is an application protocol for the electronic exchange of data between information systems in the healthcare environment. It facilitates the exchange of data by specifying a standard set of messages, including the content and format of the messages and the encoding of the data fields within the message. The HL7 standard provides flexibility by allowing the standard set of messages to be extended for specific needs, subject to negotiation between the systems being interfaced to one another.

HL7 does not specify the particular communication protocol or technology to use for the exchange of data.

### ### HL7 Version

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLO was designed to support version 2.4 of the HL7 standard, using the traditional delimited format for HL7 messages. The application may designate other versions of the standard in the message header, but that won’t otherwise affect how HLO formats the message.

### ### Supported Communication Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLO currently supports messaging only via TCP, using the set of APIs provided by Cache to read and write data over TCP communication channels. HLO implements the HL7 Standard’s Minimal Lower Layer Protocol (MLLP) to package messages for transmission via TCP.

### ### HL7 Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLO implements both individual messages and batch messages.

#### #### Individual Messages

An individual HL7 message is the atomic unit for transferring data between systems in the HL7 standard. The HL7 standard defines numerous types of messages. The type of message is identified by the *message type* and *event type,* each of which is a three-letter code. For example, for the ADT~A01 message, the message type is ADT (admission, discharge, transfer) and the event type is A01 (admission/visit notification). The HL7 standard defines the content and format of each type of message. Since the HL7 standard is evolving, there are different versions of the messages.

A message is composed of groups of segments. A *group* is an ordered set of related segments.

A *segment* is an ordered set of related fields. The first three characters of a segment is a code that identifies the *segment type*. For example, the PID segment is the patient identification segment and contains information that identifies the patient.

The first segment in a message is always the MSH segment, the *message header*. It contains information about the message, such as the type of message, the version, the sending application, the receiving application, and the date/time of the message. It also contains the *Message Control ID*, which is used to uniquely identify each message.

A *field* is an item of information, such as a person’s name or address or weight. Fields may repeat within a segment. For example, the NAME field within the PID segment may be repeating since a person may have more than one name. On the other hand, the SEX field is not allowed to repeat.

A field can have multiple parts called *components*. For example, the Patient Address field of the PID segment contains the street, state, city, zip code, etc., which are components of the field. In turn, components can have multiple parts called *subcomponents*.

Special characters called *message delimiters* are used to mark the boundaries between the segments, fields, components, and subcomponents. They are:

- The segment terminator marks the boundaries between segments. The segment terminator is always the carriage return character.
- The field separator marks the boundary between fields.
- The component separator marks the boundary between the components of a field.
- The repetition separator marks the boundary between repetitions of a field.
- The escape character marks the start and end of escape sequences within a field. An escape sequence is an instruction for special handling of the data.
- The subcomponent separator marks the boundary between the subcomponents within a subcomponent.

Here is an example of an HL7 message:

MSH\|^~\\\|ORDER\|REDACTED\|RESULTS\|500\|19900314130405\|\|ORU^R01\|523123\|D\|2.3\|

PID\|\|7777790^2^M10\|\|HL7Patient^One\|\|\|\|\|\|\|\|123456789\|

OBR\|\|2930423.08^1^L\|\|199304230800\|\|\|\|\|\|\|DERMATOLOGY\|

OBX\|CE\|10040\|OV\|1^0^0^0^0\|

OBX\|CE\|11041\|PR\|

OBX\|CE\|216.6\|P\|

OBX\|ST\|VW^WEIGHT^L\|\|120\|KG

OBX\|ST\|VB^BLOOD PRESSURE^L\|\|120/80\|MM HG

OBX\|ST\|VT^TEMPERATURE^L\|\|99\|C

OBX\|ST\|VP^PULSE^L\|\|75\|/MIN

The following is a partial analysis of the message:

- The first line of the message is the message header (MSH) segment. Within the MSH segment, we see that:
  - The field separator is ‘\|’, the component separator is ‘^’, the repetition separator is ‘~’, the escape character is ‘\\ and the subcomponent separator is ‘&’. This is the recommended set.
  - The sending application is ORDER and the receiving application is RESULTS.
  - The sending facility is REDACTED and the receiving facility is 500. (HLO uses the domain name and station number to identify the facilities. The standard often leaves such choices to the applications to negotiate.)
  - The message type is Observation Result/Unsolicited (ORU) and the event type is an unsolicited transmission of an observation message (R01).
- The second line of the message is the second segment, Patient Identification (PID).
- The third line of the message is the third segment, an Observation Request (OBR).
- The subsequent lines of the message are multiple Observation/Results (OBX) segments.

The HL7 standard provides a variety of message types and event types relevant to many areas in health care, including:

- Patient Administration
- Order Entry
- General Queries
- Financial Management
- Observation Reporting
- Master Files
- Medical Records/Information
- Scheduling
- Patient Referral
- Patient Care

Note on Notation: The n<sup>th</sup> field in a segment will be referenced by the three- letter code and the field number as follows:’MSH-1’ is the first field in the MSH segment.

#### Batch Messages

A batch message is a message that contains individual messages. The batch message itself doesn’t convey much information; rather, it is the individual messages within the batch that contain the information.

A batch message starts with the *batch header segment* (BHS). Instead of containing a Message Control ID as in the MSH segment, it contains the *Batch Control ID* that serves the same purpose of uniquely identifying the message. The batch message ends with the *batch trailer segment* (BTS).

The individual messages within the batch are exactly the same as when they don’t appear within a batch. A batch message may contain different types of messages, though generally batch messages contain messages of all the same type.

### Local Customizations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The standard also permits organizational-specific customizations to messages through a number of mechanisms including:

- Locally defined message types. Their three-letter code must begin with a’Z’.
- Locally defined event types. Their three-letter code must begin with a’Z’.
- Locally defined segment types. Their three-letter code must begin with a’Z’.
- Optional fields, components, subcomponents, and repeating fields.
- User-defined tables.

### Data Types and Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One of the issues involved in exchanging data between disparate systems is the format of the data and units of measurement. The HL7 standard provides a wide variety of data types to specify data as divergent as address, time, lab results, lab test results, etc. HLO supports some of the most common of the specialized data types, but not all of them. The support provided is in the form of specialized APIs for setting data types into a message under construction, or parsing the data types from a segment while reading the message.

Many of the data types reference tables, both tables defined within the HL7 standard as well as external tables and user-defined tables. The HLO software does not keep a database of those tables. It is the application’s responsibility to insure that the codes it uses within its messages conform to the tables. An exception pertains to the codes used within the message header, for example, the acknowledgment type codes, for which HLO is responsible.

### Message Acknowledgments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an application initiates the exchange of messages, the return of a message called an *acknowledgement message* from the receiving system may be required as part of the defined transaction. The HL7 standard defines two different acknowledgment protocols, *original mode* and *enhanced mode*. HLO supports only enhanced mode acknowledgments, which have two-phases, both of which are optional:

- An accept acknowledgement (also called a commit acknowledgement) confirms that the receiving system has received the message and has committed it to safe storage.
- An application acknowledgement confirms that the receiving application processed the sender’s message and may include additional information, for example, the reply to a query message.

The type of acknowledgement returned for any given message depends on the negotiated interface between the sending and receiving applications.

> **NOTE:** Commit acknowledgments are recommended to guarantee message delivery.

### Message Delimiters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The choice of characters to use as the message delimiters is left to the application. However, HL7 recommends this set:

> Field Separator: \|

> Component Separator: ^

> Repetition Separator: ~

> Escape Character: \\

> Subcomponent Separator: &

HLO allows the application to specify the set of delimiters to use, but defaults to the recommended set. When HLO generates accept acknowledgments, it always uses the recommended set of delimiters. When an application calls the HLO APIs to generate an application acknowledgment, the application must specify the delimiters to use if it wants other than the recommended set – i.e., HLO does not default to the same set as the original message.

### Escape Sequences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Suppose a data value contains one of the message delimiters, for example, the component separator is “^” and a data value is “a^39”. If the value were simply inserted into a field, *it would be impossible to correctly parse it back out from the message* because the parsing application would instead interpret it as two components, the first with value “a” and the second with value “39”. To provide for this the HL7 standard requires that message delimiters that appear within a value be replaced by the escape sequence for that delimiter. When parsing the value out of the message, the escape sequence must then be replaced by the original character.

The escape sequences for the message delimiters are:

> \F\\ field separator

> \S\\ component separator

> \T\\ subcomponent separator

> \R\\ repetition separator

> \E\\ escape character

In the example above, to set the field value of “a^39” into the message, the “^” would be replaced with the escape sequence “\S\\, and instead of “a^39” the value would appear within the segment as “a\S\39”.

HLO supports these escape sequences, fully automating the process provided that the application uses the message building and parsing APIs.

The standard also provides these escape sequences which HLO does NOT support:

> \H\\ start highlighting

> \N\\ normal text (end highlighting)

> \Xdddd…\\ hexadecimal data

> \Zdddd…\\ locally defined escape sequence

## Application’s Responsibilities Versus HLO’s Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### HLO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- HLO is responsible for message delivery. It accepts messages from the sending application for transmission to remote destinations. It receives messages from remote destinations and passes them to the receiving application for processing.
- HLO provides the application with tools for message construction and parsing.
- HLO builds the message header for the sending application.
- HLO parses the message header for the receiving application.
- When an application builds an HL7 message with the HLO APIs, HLO will automatically replace message delimiters that occur within the data with the appropriate escape sequence. When an application parses a message with the HLO APIs, HLO will automatically replace the escape sequence with the original character.
- HLO purges completed messages after a time period specified by the system administrator.
- HLO handles the exchange of commit acknowledgments if requested by the sending application.

### Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The application is responsible for the content of the messages, for building and parsing the content of its messages, and for processing them.
- HLO is only responsible for building the MSH and BHS header segments. The application is responsible for the building of the other segments, and for insuring that its segments conform to the HL7 standard.
- The application may choose to hard-code its message building or parsing rather than using the HLO APIs. However, in that case, the application is responsible for handling escape sequences.
- It is the application’s responsibility to determine whether or not to utilize commit acknowledgments and/or application acknowledgments. Commit acknowledgments are recommended to guarantee message delivery.
- The application is responsible for insuring that when it references tables that it uses valid codes. HLO does not maintain a database of tables referenced by HL7 messages.

## HLO Client-Server Behavior

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a messaging transaction occurs between two systems, one system always acts as the server and the other system acts as the client. The client initiates the transaction. The server passively monitors the communication channel, waiting for a remote client to initiate a message exchange.

### HLO Client Behavior 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA applications generate messages and place them on outgoing queues. Each queue contains messages meant for a particular destination. There are always HLO client processes running in the background, looking for queued outgoing messages. The client process’s job is to transmit those messages to a server at the remote destination.

#### The Outgoing Queue Structure

The outgoing queue is a special cross-reference on the HLO MESSAGES file (#778) with the following format. It has one more level than the queues of HL7 1.6 because it allows multiple queues to be associated with a specific HL Logical Link.

^HLB(“QUEUE”,”OUT”,\<name of HL Logical Link\>:\<destination port number\>,\<\*queue name\>,\<list of messages IENS, file \#778, pending on this queue\>)

\*Sending applications may designate their own private queues. The name should be name-spaced. There is a default queue named “DEFAULT’ for messages not assigned to a private queue.

#### The Client Algorithm

For each outgoing queue that has pending messages:

- The client locks the queue to insure that it has exclusive access.
- The client attempts to establish a connection to the remote server. The client will timeout after 30 seconds if the server does not accept the connection request, in which case the client will put this link on the list of down links, unlock the queue, and look for another queue with pending messages. A down queue is ignored for 30 seconds before another client process will again attempt to process it.
- For each message on the queue, up to a limit of 1,000 messages at a time for a particular queue, the client process:
  - Reads the message from the HLO files where it is stored.
  - Writes the message over the open communications channel to the remote HL7 server.
  - Updates the message status, removes the message from the queue, and moves on to sending the next message on the queue if a commit acknowledgment is not required.
  - Attempts to read from the open communications channel if a commit acknowledgment is required.
- The client will timeout after 20+ seconds if the remote server fails to return the requested commit acknowledgment. If a timeout does occur, the client will close the connection, and will attempt once to re-open the connection and send the message again, and again try to read the return commit acknowledgment. If that fails, the client will mark the link as down for 30 seconds and move on to the next queue with pending messages. That queue will NOT advance until the message is transmitted and a commit ack is returned.
- If the commit acknowledgment is received, the client will update the status of the message and remove the message from the queue. If the sending application requested notification of the commit acknowledgment via a callback (section 2.7.2) the message is placed on an incoming queue to be passed to the application.
- The closes the connection, unlocks the queue, and moves on to the next queue that has messages pending transmission when the client finishes processing a queue, or reaches the limit of 1,000 messages.

### HLO Server Behavior

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The server’s job is to monitor a communications channel, waiting for a remote client to initiate the exchange of messages.

#### The Server Algorithm

- The server monitors the communications channel until it receives a connection request from a client. When it receives a connection request, it spawns another process to handle the messaging with that client and then continues to monitor for more connection requests. This means the server is multi-threaded, allowing it to handle multiple concurrent clients. The following steps apply to the newly spawned child process.
- The server reads messages over the open communication channel until the client terminates the session, at which point this server process terminates. For each message:
  - The server reads from the communication channel looking for the delimiter marking the beginning of an HL7 message. It continues to read until either it reaches the delimiter marking the end of the message or a read timeout occurs after 20 seconds. If a read timeout occurs, the child server process terminates.
  - The server parses the individual fields from the message header.
  - Based on the message header, the server will determine an error if:
- There is no Message Control ID specified.
- The message is an application acknowledgment and the original message is not found in the HLO MESSAGES FILE (#778).
- The message is an application acknowledgment and the original message was already acknowledged.
- The Receiving Facility in the message header does not match the server’s system.
- The Processing ID in the message header doesn’t match the system.
- The Receiving Application is not found in the HLO APPLICATION REGISTRY file (#779.2) file. The HLO Application Registry is used to lookup what application routine should be executed to process the message.
  - If the server determines an error, and a commit acknowledgement was requested, a commit acknowledgement is returned with the CE code in the MSA segment. The message status is set to ERROR and the message is not passed to the application.
  - Also, based on the message header, the server determines if the message is a duplicate.
- Messages are frequently received multiple times due to communication failures. For example, if communication fails after the client sends a message, but before the client receives a return commit acknowledgement, then the client would generally resend the message. So the HLO server does a lookup based on the Sending Facility, Sending Application, and Message ID to determine if the message was previously received. If a match is found, the server determines that the message was previously received, and so it is not processed a second time. If a commit acknowledgement was requested, the server will return a commit acknowledgement based on the commit acknowledgement that was returned for the original message.
- If the message is not a duplicate nor an error:
  - The server returns a commit acknowledgement if one was requested. The MSA segment will have the CA code.
  - The server sets the message onto the incoming queue. The server determines the application routine by doing a lookup on the HLO APPLICATION REGISTRY file (#779.2). Another HLO process is responsible for taking the messages off the incoming queue one-by-one and passing them to the application routine to process.

#### The Incoming Queue Structure

The incoming queue is a special cross-reference on the HLO MESSAGES file (#778) with the following format. It has one more level than the queues of HL7 1.6, because it allows multiple queues to be associated with a sending facility.

^HLB(“QUEUE”,”IN”,\<HL Logical Link\>ORSending Facility\>,\<\queue name*\>,\<list of messages IENS, file \#778, pending on this queue\>)

\*Receiving applications may designate their own private queues. The name should be name-spaced. There is a default queue named “DEFAULT’ for messages not assigned to a private queue.

## Features Not Supported by HLO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Original Mode Acknowledgments
2.  Synchronous (real-time) communication between the sending and receiving application.
3.  Sequence Number Protocol
4.  Transfer of messages via files using the FHS and FTS segments.

## Special Considerations for Interfacing HLO to COTS, Middleware, or Other Messaging Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The Message Control ID and Batch Control ID must be unique.

The Control ID that appears in the message header must be unique within the domain of {sending facility, sending application}. HLO insures that its Control ID’s are unique by incorporating the station number. A common mistake is to base the Control ID on a timestamp, which may not insure a unique Control ID.

5.  Acknowledgment types are not interchangeable

HLO will not accept an application acknowledgement in lieu of a commit acknowledgement. For example, if the remote server returns the AA code in the MSA segment instead of the CA code, the status of the message will be set to error.

6.  Commit acknowledgments are synchronous.

The HLO client expects that the commit acknowledgement be returned synchronously over the same open connection as the original message, and the HLO Server expects to return the commit acknowledgment in the same manner. A commit acknowledgment returned asynchronously over another connection will not be accepted.

7.  Batch messaging is not standard.

Batch message processing under HLO incorporates several non-standard features that may prevent batch messaging with COTS systems without customization. These features include:

1.  The standard does not provide for a Processing ID in the batch header (BHS segment) as it does in the MSH segment. HLO requires that the Processing ID be in the Batch Name/ID/Type field, sequence 9, of the BHS segment.
2.  The standard does not provide for a commit ack to be requested via the batch header. HLO also uses the Batch Name/ID/Type field, sequence 9, of the BHS segment for that purpose.
3.  The HL7 standard provides several different methods for returning application acknowledgments in response to a batch of messages. For example, the standard allows the application to return an acknowledgment for every individual message, or to return acknowledgments for only the messages that encountered an error. HLO leaves that to the application to decide, but if the sending application requests acknowledgments for a batch of messages then the receiving application must return the acknowledgments within a single batch of messages and not in multiple batches or as individual messages. The Reference Batch Control ID field (Sequence 12) is used to cross-reference a batch of application acknowledgments to the original batch of messages.
8.  Guaranteeing the sequence of message delivery.

When messaging occurs between two applications using HLO with no middleware involved, HLO will insure that messages are delivered to the receiving application in the same order that they were generated by the sending application. However, when other configurations are employed, such as the use of an interface engine, the sequence of the messages cannot be guaranteed by HLO without special handling. HLO provides Sequence Queues that applications may use to guarantee the order of their messages. Sequence Queues use application acknowledgments to insure that a message placed on a Sequence Queue is not delivered until the preceding message is received by the remote Receiving Application. The throughput of a single Sequence Queue, because of its reliance on the exchange of application acknowledgments, is quite slow, so Sequence Queues may not be appropriate for high-volume messaging applications.

# Building and Sending HL7 Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLO provides the developer with a set of APIs for building messaging applications. The following is an outline of the development process:

<u>Step 0:</u> HLO needs to be installed, configured, and running on the sending system. An HL7 server, either HLO or other, needs to be running on the receiving system, with TCP connectivity between the two systems.

<u>Step 1:</u> Create the necessary table entries:

- An entry is needed in the HL LOGICAL LINK file (#870) file for each destination.
- An entry is needed in the HLO APPLICATION REGISTRY file (#779.2) for the sending application.
- HLO does not require the use of protocols, but does support their use. If used, entries are needed for the event and subscriber protocols in the PROTOCOL file (#101), and the HL7 APPLICATION PARAMETER file (#771). Instructions for that setup can be found in the *VistA Health Level Seven (HL7) Site Manager & Developer Manual, Version 1.6\*56*.

<u>  
</u>

<u>Step 2:</u> Using the HLO APIs, write a routine to build and send the message.

- The developer needs to build the body of the HL7 message segment-by-segment, excluding message headers. The developer is responsible for insuring the content and format of the message.
- After completing the body of the message, the developer calls an HLO API to send the message. HLO will:
  - Build a header segment for the message based on the input parameters provided by the developer and various configuration tables.
  - Store the body of the message in the HLO MESSAGE BODY file (#777) and store the message header and administrative information in the HLO MESSAGES file (#778).
  - Place the message on an outgoing queue for an HLO client process to transmit to the remote server.

<u>Step 3:</u> The developer needs to implement the necessary event triggers in the application software. That entails inserting one or more hooks into the application that will execute the routine developed in Step 2 when the event occurs. In a typical VistA application, the hooks may be inserted directly into an application routine, option, protocol, M-style cross-reference, or other software component. How best to implement the event triggers requires careful technical analysis of the application software.

The HLO APIs support two styles of message building, which we’ll refer to as “traditional style” and “new style.”

*Traditional style* – This is the original style provided by the HL7 package prior to the development of HLO. Its characteristics are:

- Messages are built by the application outside of the HL7 package as an array of lines of text. The application typically builds each segment by concatenating the individual fields together or by setting the fields into the segment using the M \$PIECE function. The completed message array is then passed to the HL7 package.
- Event protocols and subscriber protocols are created during development. These protocols define various message parameters, such as message type, event type, sending and receiving application, and receiving facility. When an application’s trigger event occurs, the application passes the event protocol to the HL7 package, along with the message array described above.

*New style* – HLO provides applications with a new style of generating their messages. Its characteristics are:

- The application uses the HLO APIs within a framework to both build and deliver the message. The overview of the framework is:
1.  Start the process of generating a message by calling either \$\$NEWMSG^HLOAPI for an individual message or \$\$NEWBATCH^HLOAPI for a batch message.
2.  Build the message segment-by-segment and field-by-field using special HLO APIs.
3.  Once the message is complete, send it via one of the HLO SEND APIs.
- The application developer isn’t required to set up protocols in advance to define various message parameters. Instead, the application can pass HLO those parameters through the formal parameter list to the HLO API.

*Why support two styles of building messages?*

There are many existing applications that have invested considerable effort in developing hard-coded segment builders, message builders, and protocols in the traditional style. To protect that investment, HLO supports the traditional style of message building.

On the other hand, there are distinct advantages to the new style:

- HLO relieves the developer of considerable overhead:
  - HL7 message delimiters that occur within the data are automatically replaced with their corresponding escape sequences.
  - HLO automatically keeps track of how long a segment is and prevents nodes from exceeding the maximum size allowed.
  - HLO automatically caches the message being built in memory, moving it to disk when it is complete or it grows too large for the symbol table.
- The message building APIs are also designed to make message building self-documenting and resistant to the types of errors that tend to occur in hard-coding complex segments via piecing together individual fields.
- The setup without the use of protocols can be simpler and more flexible.

> So while HLO supports both styles, the downside is that HLO has more APIs than otherwise.

## Create an Entry in the HLO Application Registry File for the Sending Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The application must specify a name for the sending application when generating messages to send. The application name is required to be unique within the enterprise, so it should be namespaced by the sending package. The sending application appears in the message header segments MSH-4 or BHS-4.

HLO requires that a sending application have an entry in the HLO APPLICATION REGISTRY file (#779.2), but the information required is minimal.

Using the ADD/EDIT SENDING APPLICATION option \[HLO EDIT SENDING APPLICATION\] on the APPLICATION REGISTRY MENU option \[HLO APPLICATION REGISTRY MENU\], which in turn is under the HL7 (Optimized) MAIN MENU option \[HLO MAIN MENU\], create an entry for the sending application. Only the name and package are required for the sending application.

Example: Adding a sending application to the HLO Application Registry. In this example the sending application will not use sequence queues.

Select HLO APPLICATION REGISTRY APPLICATION NAME: HLO DEMO SENDING APPLICATION

Are you adding ’HLO DEMO SENDING APPLICATION' as

a new HLO APPLICATION REGISTRY (the 69TH)? No// Y (Yes)

APPLICATION NAME: HLO DEMO SENDING APPLICATION Replace

Package File Link: HLO HL7 OPTIMIZED (HLO) HLO

Do you want to edit the setup for sequence queues? NO//

Example: Adding a sending application to the HLO Application Registry. In this example, the sending application will use sequence queues (see section 2.7).

Select HLO APPLICATION REGISTRY APPLICATION NAME: HLO DEMO SENDING APPLICATION

Are you adding ’HLO DEMO SENDING APPLICATION' as

a new HLO APPLICATION REGISTRY (the 69TH)? No// Y (Yes)

APPLICATION NAME: HLO DEMO SENDING APPLICATION Replace

Package File Link: HLO HL7 OPTIMIZED (HLO) HLO

Do you want to edit the setup for sequence queues? NO// YES

SEQUENCE EXCEPTION ROUTINE: HLOSEQ

SEQUENCE EXCEPTION TAG: LATE

SEQUENCING TIMEOUT: 10

As of patch XU\*8.0\*399, KIDS supports the inclusion of entries in the HLO Application Registry in software distributions by allowing the developer to include them in a build in the same way as other components such as options and protocols.

## Create Entries in the HL Logical Link File for Each Destination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An outgoing message must be associated with an entry in the HL LOGICAL LINK file (#870) in order to be transmitted. The HL Logical Link provides the IP internet address, port number, domain, and if applicable, the VHA station number.

An HLO server can coexist with other servers at the same IP address, but it must have its own port reserved exclusively for HLO. The VHA DBA has assigned standard ports for HLO as follows:

Production Systems: Port 5001

Development and Test Systems: Port 5026

The field that identifies the HLO port is the TCP/IP PORT (OPTIMIZED) (#400.08). If not valued, HLO will default to the standard port shown above. HLO determines whether it’s a production system via the HLO SYSTEM PARAMETERS file (#779.1).

The majority of fields defined for the HL LOGICAL LINK file (#870) are defined for the use of the HL7 1.6 and are not used by HLO. The following fields *are* used by HLO:

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>Fields Used by HLO in the HL Logical Link file.</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NODE (#.01)</td>
<td>The name of the HL LOGICAL LINK entry, file #7870.</td>
</tr>
<tr class="even">
<td>INSTITUTION (#.02)</td>
<td>If there is an entry in the INSTITUTION file (#4) for the remote facility then set this field. It will be used to obtain the station number.</td>
</tr>
<tr class="odd">
<td>LLP TYPE (#2)</td>
<td>Set this to “TCP”.</td>
</tr>
<tr class="even">
<td>TCP/IP SERVICE TYPE (#400.03)</td>
<td>Set this to “CLIENT”.</td>
</tr>
<tr class="odd">
<td>MAILMAN DOMAIN (#.03)</td>
<td><p>Not used if the DNS DOMAIN field (below) is defined.</p>
<p>Otherwise, set this to an entry in the MailMan’s DOMAIN file (#4.2).</p></td>
</tr>
<tr class="even">
<td>DNS DOMAIN (#.08)</td>
<td>Set this to the TCP/IP domain name of the remote server.</td>
</tr>
<tr class="odd">
<td>TCP/IP ADDRESS (#400.01)</td>
<td>Set this to the TCP/IP address of the remote server.</td>
</tr>
<tr class="even">
<td>TCP/IP PORT (OPTIMIZED) (#400.08)</td>
<td>Set to the port number used by the remote server.</td>
</tr>
</tbody>
</table>

Every system on the network should have an official domain name assigned. Using the domain name in conjunction with the Dynamic Name Service (DNS) protocol, HLO can find the TCP/IP address of the remote server – which is important in case the TCP/IP address changes. It allows HLO to automatically recover without disruption. When VHA’s DNS service was created it was initially populated with domains taken from the MailMan’s DOMAIN file (#4.2). HLO also uses domain names in the HL7 message headers to identify the sending and receiving facilities.

Use the Link Edit \[HL EDIT LOGICAL LINKS\] option to create or edit an HL Logical Link entry, setting only the fields listed above.

> **WARNING:** If modifying an existing HL Logical Link entry for use with HLO, do NOT modify or delete any field not specific to HLO. Though HLO does not use those other fields, HL7 1.6 does.

## The MSH, BHS, and BTS Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLO automatically builds the MSH and BHS message header segments and the BTS batch trailer segment. The following sections provide a description of those segments.

### HLO’s MSH Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 22%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Sequence</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Assigned Value</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Field Separator</td>
<td>Required. Defaults to “|”, but another value may be provided by the application.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Encoding Characters</td>
<td>Required. Defaults to “^~\&amp;”, but another value may be provided by the application.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Sending Application</td>
<td>Required. Provided by the application.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Sending Facility</td>
<td><p>Component 1: the station number</p>
<p>Component 2: the domain name</p>
<p>Component 3: “DNS”</p>
<p>These values are determined from the HLO SYSTEM PARAMETERS file (#779.1).</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td>Receiving Application</td>
<td>Required. Provided by the application.</td>
</tr>
<tr class="even">
<td>6</td>
<td>Receiving Facility</td>
<td><p>Component 1: the station number</p>
<p>Component 2: the domain name</p>
<p>Component 3: “DNS”</p>
<p>These values are determined from the HL LOGICAL LINK file (#870).</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td>Date/Time Of Message</td>
<td>Required. Set by HLO at the point the message is generated by the application.</td>
</tr>
<tr class="even">
<td>8</td>
<td>Security</td>
<td>Optional. Provided by the application.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>Message Type</td>
<td>Required. A three-letter code provided by the application.</td>
</tr>
<tr class="even">
<td>10</td>
<td>Message Control ID</td>
<td>Required. The value is based on a counter and is prefixed with the station number to insure its uniqueness within VHA.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>Processing ID</td>
<td>Required. The value is determined by the HLO SYSTEM PARAMETERS file (#779.1)</td>
</tr>
<tr class="even">
<td>12</td>
<td>Version ID</td>
<td>Required. Defaults to 2.4, but the application may provide another value.</td>
</tr>
<tr class="odd">
<td>13</td>
<td>Sequence Number</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>14</td>
<td>Continuation Pointer</td>
<td>Optional. Provided by the application.</td>
</tr>
<tr class="odd">
<td>15</td>
<td>Accept Acknowledgment Type</td>
<td>Required. “NE” or “AL” as specified by the application.</td>
</tr>
<tr class="even">
<td>16</td>
<td>Application Acknowledgment Type</td>
<td>Required. “NE” or “AL” as specified by the application.</td>
</tr>
<tr class="odd">
<td>17</td>
<td>Country Code</td>
<td>Optional. Three-character code provided by the application.</td>
</tr>
<tr class="even">
<td>18</td>
<td>Character Set</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>19</td>
<td>Principal Language Of Message</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>20</td>
<td>Alternate Character Set Handling Scheme</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>21</td>
<td>Message Profile Identifier</td>
<td>Not used.</td>
</tr>
</tbody>
</table>

### HLO’s BHS Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 22%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Sequence</strong></th>
<th><strong>Field Name</strong></th>
<th><strong>Assigned Value</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Batch Field Separator</td>
<td><p>Required. Defaults to “|”, but another value may be provided by the</p>
<p>application.</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>Batch Encoding Characters</td>
<td>Required. Defaults to “^~\&amp;”, but another value may be provided by the application.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Batch Sending Application</td>
<td>Required. Provided by the application.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Batch Sending Facility</td>
<td><p>Component 1: the station number</p>
<p>Component 2: the domain name</p>
<p>Component 3: “DNS”</p>
<p>The values are determined from the HLO SYSTEM PARAMETERS file (#779.1).</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td>Batch Receiving Application</td>
<td>Required. Provided by the application.</td>
</tr>
<tr class="even">
<td>6</td>
<td>Batch Receiving Facility</td>
<td><p>Component 1: the station number</p>
<p>Component 2: the domain name</p>
<p>Component 3: “DNS”</p>
<p>The values are determined from the HL LOGICAL LINK file (#870).</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td>Batch Creation Date/Time</td>
<td>Required. Set by HLO at the point the message is generated by the application.</td>
</tr>
<tr class="even">
<td>8</td>
<td>Batch Security</td>
<td>Optional. Provided by the application.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>Batch Name/ID/Type</td>
<td><p>This field is used by HLO for a non-standard purpose. It is used to store three items of information, the Processing ID, determined from the HLO SYSTEM PARAMETERS file (#779.1), the Accept Acknowledgment Type , provided by the application, and the Application Acknowledgment Type, provided by the application.</p>
<p>The format of the field is:</p>
<p>“PROCESSING ID=”&lt;Processing ID code is “P” or “D”&gt;</p>
<p>“ACCEPT ACK TYPE=”&lt;Accept Acknowledgment Type is “NE” or “AL”&gt;</p>
<p>“APP ACK TYPE=”&lt;Application Acknowledgment Type is “NE” or “AL”&gt;</p></td>
</tr>
<tr class="even">
<td>10</td>
<td>Batch Comment</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>Batch Control ID</td>
<td>Required. The value is based on a counter and is prefixed with the station number to insure its uniqueness within VHA.</td>
</tr>
<tr class="even">
<td>12</td>
<td>Reference Batch Control ID</td>
<td>This is used only for a batch that contains application acknowledgments to another batch. It is set to the Batch Control ID of the original batch.</td>
</tr>
</tbody>
</table>

### HLO’s BTS Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Sequence | Field Name      | Assigned Value                                                      |
|--------------|---------------------|-------------------------------------------------------------------------|
| 1            | Batch Message Count | Required. The value is set to a count of the messages within the batch. |
| 2            | Batch Comment       | Not used.                                                               |
| 3            | Batch Totals        | Not Used.                                                               |

## List of Message Building APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 36%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="19"></th>
<th colspan="4"><p>New Style Message Building</p>
<p>Group 1</p></th>
</tr>
<tr class="odd">
<th rowspan="13"></th>
<th colspan="3"><p>Building a Segment</p>
<p>Group 1.1</p></th>
</tr>
<tr class="header">
<th rowspan="9"></th>
<th colspan="2"><p>Inserting Data into a Segment</p>
<p>Group 1.1.1</p>
<ul>
<li><p>Not all data types in the HL7 standard are supported by a specific API.</p></li>
<li><p>These APIs automatically replaces message delimiters with escape sequences.</p></li>
</ul></th>
</tr>
<tr class="odd">
<th>SET^HLOAPI</th>
<th>Sets a single atomic value of unspecified data type into the segment.</th>
</tr>
<tr class="header">
<th>SETAD^HLOAI4</th>
<th>Sets an address into a segment</th>
</tr>
<tr class="odd">
<th>SETCE^HLOAPI4</th>
<th>Sets a coded element into a segment.</th>
</tr>
<tr class="header">
<th>SETCNE^HLOPAI4</th>
<th>Sets a coded value with no exceptions into a segment.</th>
</tr>
<tr class="odd">
<th>SETCWE^HLOAPI4</th>
<th>Sets a coded value with exceptions into a segment.</th>
</tr>
<tr class="header">
<th>SETDT^HLOAPI4</th>
<th>Sets a date into the segment.</th>
</tr>
<tr class="odd">
<th>SETHD^HLOAPI4</th>
<th>Sets a hierarchic designator into a segment.</th>
</tr>
<tr class="header">
<th>SETTS^HLOAPI4</th>
<th>Sets a timestamp into the segment.</th>
</tr>
<tr class="odd">
<th></th>
<th>SETXPN^HLOAPI4</th>
<th>Sets an extended person name into a segment.</th>
</tr>
<tr class="header">
<th colspan="3"><p>Inserting the Completed Segment Into the Message</p>
<p>Group 1.1.2</p></th>
</tr>
<tr class="odd">
<th></th>
<th>ADDSEG^HLOAPI</th>
<th>Adds the completed segment to the end of the message.</th>
</tr>
<tr class="header">
<th rowspan="5"></th>
<th colspan="3"><p>Building an Individual Message</p>
<p>Group 1.2</p></th>
</tr>
<tr class="odd">
<th></th>
<th>NEWMSG^HLOAPI</th>
<th>Begins a new message.</th>
</tr>
<tr class="header">
<th colspan="3"><p>Building a Batch Message</p>
<p>Group 1.3</p></th>
</tr>
<tr class="odd">
<th rowspan="2"></th>
<th>NEWBATCH^HLOAPI</th>
<th>Begins a new batch of messages.</th>
</tr>
<tr class="header">
<th>ADDMSG^HLOAPI</th>
<th>Adds another message into the batch.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="4"></td>
<td rowspan="4"></td>
<td colspan="3"><p>Sending a Batch Message or Individual Message whose Construction is Complete</p>
<p>Group 1.4</p>
<ul>
<li><p>Stores the body of the message in the HLO MESSAGE BODY (#777)</p></li>
<li><p>For each recipient, creates an entry in the HLO MESSAGES (#778)</p></li>
</ul>
<ul>
<li><p>The message is placed on an outgoing queue for transmission for each recipient.</p></li>
</ul></td>
</tr>
<tr class="even">
<td></td>
<td>SENDONE^HLOAPI1</td>
<td>Sends a message to a single destination.</td>
</tr>
<tr class="odd">
<td></td>
<td>SENDMANY^HLOAPI1</td>
<td>Sends a message to a list of destinations, passed in as a parameter.</td>
</tr>
<tr class="even">
<td></td>
<td>SENDSUB^HLOAPI1</td>
<td>Sends a message to a list of destinations. The list is based on an entry in the HLO Subscription Registry.</td>
</tr>
<tr class="odd">
<td colspan="5"><p>Traditional Style Message Building</p>
<p>Group 2</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>EN^HLOCNRT</td>
<td>Allows the use of traditional-style hardcoded message builders and protocol setup as in HL7 1.6, but the messages are sent via HLO. It is similar to HL7 1.6’s EN^HLMA. However, it does not support the sending of batch messages, the use of the ROUTING LOGIC field of a protocol, and other features of EN^HLMA.</td>
</tr>
<tr class="odd">
<td colspan="5"><p>Hybrid Style Message Building</p>
<p>Group 3</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>MOVEMSG^HLOAPI</td>
<td>Moves a message array built in the traditional way into HLO. It does not require the use of protocols or other traditional setup.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>MOVESEG^HLOAPI</td>
<td>Moves a single segment built in the traditional way into HLO. This preserves the investment in the library of message builders that were already developed prior to HLO.</td>
</tr>
</tbody>
</table>

## The HLO Framework for Message Building

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following set of patterns defines the framework under which applications may use the HLO APIs to generate their messages.

Message building within HLO always requires the following steps, so they won’t be included when discussing the individual patterns:

1.  Setting up entries in the HL LOGICAL LINK file (#870) for the network destinations for the messages
2.  Setting up entries in the HLO APPLICATION REGISTRY file (#779.2) for the sending application
3.  Using the M NEW command to set up the required variables used for calls to the various APIs

Also, the technical details for using each API are not presented here. For that, please refer to the API Reference Guide.

### New-Style Message Building

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Pattern 1 – Building a Segment

The APIs in group 1.1.1 are used iteratively to build a segment, field by field.

- The fields may be set in any order, though left to right is recommended.
- The particular SET-type API used depends on the data type of the field, component, or subcomponent. HLO does not provide specialized APIs for all of the HL7 standard’s complex data types, but the generic SET^HLOAPI can always be used to set a single atomic value into a segment at the field, repetition, component, or subcomponent level.

Pattern:

- Start building the segment by setting the three-character segment type into your workspace (SEG):
  - DO SET^HLOAPI(.SEG,\<3 character segment type\>)

    or equivalently:
  - DO SET^HLOAPI(.SEG,\<3 character segment type\>,0)
- For each field in the segment that is to contain a data value:
  - Call the APIs from group 1.1.1 to set the data into the field. If the field is repeating, or has multiple components or subcomponents, you may need to make multiple calls.

> **NOTE:** In the following pages, the numbered examples refer to the code examples in the section on Code Examples. The un-numbered examples are self contained.

Example 1: Building a PID segment using the HLO APIs. See PID^HLODEM1 in the section on Code Examples. Segments built this way are added to the message by calling ADDSEG^HLOAPI.

Example 2: For the sake of comparison, this example builds the same PID segment *without* using the HLO APIs. See PID^HLODEM2 in the section on Code Examples. Segments built this way are added to the message by calling MOVESEG^HLOAPI.

Example 3: Builds a NK1 segment using the HLO APIs. See NK1^HLODEM1 in the section on Code Examples.

Example 4: This example builds the same NK1 segment *without* using the HLO APIs.

#### Pattern 2 – Building an Individual Message

This builds a complete individual message, as opposed to a batch message, and places it on an outgoing queue for transmission. The message header segment MSH is automatically added to the message.

<u>Pattern:</u>

- Call NEWMSG^HLOAPI to start building the message.
- For each segment to appear in the message, other than the MSH segment, in the correct order defined for its message structure based on the message type and event:
  - Build the segment using pattern 1.
  - Call ADDSEG^HLOAPI to add the completed segment to the message.
- Call one of the APIs in group 1.4 to complete the message and queue it for transmission.

  Example 5: Builds an ADT~A08 message and queues it for transmission. See A08^HLODEM1 in the section on Code Examples.

#### Pattern 3 – Building a Batch Message

This builds batch message, and places it on an outgoing queue for transmission. The batch header segment BHS and individual message header segments MSH are automatically added to the message.

Pattern:

- Call NEWBATCH^HLOAPI to start the batch.
- For each message to be placed in the batch:
  - Call ADDMSG^HLOAPI to start the message.
  - For each segment to appear in the message, other than the MSH segment, in the correct order defined for its message structure based on the message type and event:
- Build the segment using pattern 1.
- Call ADDSEG^HLOAPI to add the completed segment to the message.
- Call one of the APIs in group 1.4 to send the message.

Example 6: Builds a batch of ADT~A08 message and queues it for transmission. See BATCHA08^HLODEM1 in the section on Code Examples.

### Traditional Style Message Building

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Pattern 4 Building an Individual Message in the Traditional Style

So that existing applications might easily convert from HL7 1.6 to HLO, HLO supports traditional style hard-coded message builders and the use of protocols as found in HL7 1.6. HLO does NOT support sending batch messages built with HL7 1.6 tools.

<u>Pattern:</u>

- Set up entries in the HL7 APPLICATION PARAMETER file (#771) for the sending and receiving applications.
- Set up an event protocol and its subscriber protocols.
- Create the body of the message in either the HLA(“HLS”) local array or the ^TMP(“HLS”,\$J) global array in the traditional way.
- Call EN^HLOCNRT.

Example 7: Builds an ADT~A08 using a hardcoded message builder and a protocol setup. The resultant message is identical to that of example 4. See A08^HLODEM2 in the section on Code Examples.

### Hybrid Style Message Building

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several combinations in which elements of the traditional style message building may be mixed with the new style message building.

#### Pattern 5 – Mixing Traditional Style and New Style Segment Builders

A message can be built using a mix of the new segment building APIs and the traditional style segment builders.

Pattern:

- Follows new style Patterns 2 or 3, except for each segment:
  - If the segment was built via a traditional segment builder as an array of lines, add it to the message by calling MOVESEG^HLOAPI.
  - If the segment was built using the HLO segment building APIs, add it to the message by calling ADDSET^HLOAPI.

Example 8: Builds an ADT~A08 using a the HLO segment building APIs for the PID segment and a traditional hardcoded segment builder for the NK1 segment. The resultant message is identical to that of example 4. See A08^HLODEM3 in the appendix of code examples.

#### Pattern 6 – Traditional Message Building without Protocols

Messages built using a traditional hardcoded message builder can be sent via HLO without using protocols.

<u>Pattern:</u>

- Create an entry in the HLO Application Registry for the sending application.
- Create the individual message in either the HLA (“HLS”) local array or the ^TMP(“HLS”,\$J) global array in the traditional way.
- Call NEWMSG^HLOAPI to start building the message.
- Call MOVEMSG^HLOAPI to move the body of the message, built in the tradition style as an array of segments, into the message started by the call to NEWMSG^HLOAPI.
- Call one of the APIs in group 1.4 to complete the message and queue it for transmission.

Example 9: Builds an ADT~A08 using with a hardcoded message builder but sends it without the protocol setup. See A08^HLODEM3 in the appendix of code examples.

## Application Callbacks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A callback is an application routine that is executed upon the occurrence of some future event. With HLO, when an application sends a message, it may set three different callbacks as parameters.

### Callback for Application Acknowledgments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The application may set a callback that will be executed when the application acknowledgment message is returned. To do so, set this parameter before calling one of the send APIs listed in group 1.4 of section 2.5:

S PARMS(“APP ACK RESPONSE”) = \<tag\>^\<routine\>

At the point the routine is executed by HLO, the only variable defined is HLMSGIEN equal to the IEN of the application acknowledgment. As always, the application should start by calling \$\$STARTMSG^HLOPRS(.MSG,HLMSGIEN,.HDR). The array MSG is returned with information about the application acknowledgment, but to refer back to the original message the variable MSG(“ACK TO”) is returned with the Message Control ID of the original message and MSG(“ACK TO IEN”) is returned with the IEN of the original message in the HLO MESSAGES file (#778).

### Callback for Commit Acknowledgments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The application may set a callback that will be executed when the commit acknowledgment message is returned. To do so, set this parameter before calling one of the send APIs listed in group 1.4 of section 2.5:

S PARMS(“ACCEPT ACK RESPONSE”) = \<tag\>^\<routine\>

At the point the routine is executed by HLO, the only variable defined is HLMSGIEN set equal to the IEN of the *original* message. That is because the commit acknowledgment is not stored separately. Instead, when the commit acknowledgment is returned, HLO does the following:

- If the commit acknowledgment returns an error or reject, the status of the original message is set to error.
- The MSA segment of the commit acknowledgment is stored with the original message.

As with the callback for the application acknowledgment, the application callback should start off by calling \$\$STARTMSG^HLOPRS(.MSG,.HLMSGIEN,.HDR), but in this case the MSG array is returned with information pertaining to the *original* message. Two items of information that are of particular importance when processing a commit acknowledgment in a callback:

- MSG(“STATUS”) will be “ER” if the commit acknowledgment indicated an error or reject.
- MSG("STATUS","ACCEPT ACK ID") is the message id of the commit acknowledgment that was returned.
- MSG(“MSG("STATUS","ACCEPT ACK MSA") will be the MSA segment of the commit acknowledgment that was returned.

### Callbacks for Messages that Fail to Transmit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLO will repeatedly attempt to transmit a message until its either successful or a negative acknowledgment is returned. But eventually, after a very long period determined by the site, HLO will cease its attempts to transmit a message and set its status to “error.” The sending application can set a callback to be executed in this eventuality by setting this parameter:

PARMS(“FAILURE RESPONSE”)=\<tag\>^\<routine\>

At the point, the callback is executed; the only variable defined is HLMSGIEN equal to the IEN in the HLO MESSAGES file (#778) of the message.

## Sequence Queues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sequence queues are a mechanism for ensuring that messages are received by the remote application in the same order that the sending application generates them. When sending messages between two VistA systems with no middleware involved, sequence queues are NOT necessary. But when the sending application uses the services of the VIE or other middleware, or when sending messages to a non-VistA system, sequence queues *may* be necessary to insure the sequence of message delivery.

### The Algorithm

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sequence queues work in conjunction with the use of application acknowledgments to insure the correct sequence of message delivery. The algorithm has two parts, with roles for both the client and the server.

#### Client Role:

- At the point when a sending application generates a message, it requests:
  1.  That an application acknowledgement be returned.
  2.  That the message be placed on its private sequence queue.
- If the sequence queue is NOT currently pending the return of an application acknowledgment for a preceding message, then HLO places the new message on the outgoing queue and marks the sequence queue as pending the return of an application acknowledgment for this new message.
- However, if the sequence queue IS currently pending the return of an application acknowledgment for the preceding message, then HLO does NOT place the new message on the outgoing queue. Instead, the new message is placed on the sequence queue, pending the application acknowledgment for the preceding message.

#### Server Role:

- The server receives the return of an application acknowledgment.
- It looks up the original message to determine whether or not the sending application had used a sequence queue.
- If so, it goes to that sequence queue and moves the next message on it into the outgoing queue for transmission, and marks the sequence queue as pending an application acknowledgment for that message.

### Using Sequence Queues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To use a sequence queue, an application developer needs to take these additional steps in building their messaging application:

1.  The sending application must request both an accept acknowledgment and an application acknowledgement.
2.  The sending application must specify the name of a sequence queue on which to place the message. The queue is created dynamically as needed, and disappears once it is empty. The name of the queue can be up to 30 characters and must be namespaced by the application. It is passed as an input parameter to any of the HLO message sending APIs by specifying PARMS("SEQUENCE QUEUE"). The input parameter must be passed-by-reference.
3.  The application must provide an exception handler for HLO to invoke if a sequence queue waits too long for an application acknowledgment to be returned. Typically, the exception handler will serve to notify the operations staff to investigate why the remote application has not returned the application acknowledgement. The queue may be manually advanced if it is determined to be the appropriate action.
4.  There are new parameters that must be entered for the sending application in the HLO Application Register file (#779.2).
    1.  SEQUENCE TIMEOUT field (#.12) - The number of minutes to wait for an application acknowledgment before calling the application's sequence exception routine.
    2.  SEQUENCE EXCEPTION ROUTINE field (#.10) and SEQUENCE EXCEPTION TAG field (#.11) - Together these two fields specify an M \<tag\>^\<routine\> to call when a the timeout period expires while waiting for an application acknowledgment.

Example 10: This is identical to example 5, A08^HLODEM1, except that the message is placed on a sequence queue. See A08^HLODEM4 in the section on Code Examples.

## HLO Subscription Registry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HLO Subscription Registry (file \#779.4) is used to store lists of subscribers to an application’s messages. Conceptually, it’s the same as the subscriber list stored in the PROTOCOL file (#101) used by HL7 1.6, or distribution lists used by email. An application may address a message to a subscription list, and HLO will send the message to each subscriber on that list.

HLO has two interfaces to the subscription registry. It has a user interface which is used to create a subscription list at design time. Subscription lists created that way are distributed along with the other system components of the messaging application via KIDS.

The other interface is via a set of APIs used to create subscriptions on-the-fly on the system where they will be used. For example, if a new patient is registered at a site, an application may create a subscription specifically related to that patient to keep informed of that patient’s activities via HL7 messages.

### The User Interface for Creating Subscription Lists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ADD/EDIT SUBSCRIPTIONS option is used to create a subscription list and to add subscribers to it. The option is under the Developer Menu, which in turn is under the HLO MAIN MENU.

These fields should be entered to create an entry in the HLO Subscription Registry (file \#779.4).

| \# | Field Name    | Description                                                                                 |
|--------|-------------------|-------------------------------------------------------------------------------------------------|
| .01    | NAME              | Then name of the entry. It must be unique, so it should be namespaced.                          |
| .02    | OWNER APPLICATION | Could be the package, the sending application, or other meaningful designation for the creator. |
| .03    | DESCRIPTION       | Optional. A brief one-line description.                                                         |

For each subscriber to be added, these fields should be entered to the RECIPIENTS sub-file (#794.41).

| \# | Field Name          | Description                                                                                                                                                                                                                                                                                                                     |
|--------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .01    | RECEIVING APPLICATION   | The name of the receiving application, exactly as it should appear in the message header.                                                                                                                                                                                                                                           |
| .02    | MIDDLEWARE LOGICAL LINK | Enter this field ONLY IF the message should be transmitted through middleware, such as an interface engine. It is the HL Logical Link file (#870) that has the IP address and port \# of the middleware.                                                                                                                            |
| .021   | FACILITY LOGICAL LINK   | This field is ALWAYS needed. It is the HL Logical Link of the facility that the message is being sent to. It is used to obtain values for the Receiving Facility field of the message header. If a MIDDLEWARE LOGICAL INK is not specified, it is also used to obtain the IP address and port \# for where to transmit the message. |

Example: Adding a new entry to the HLO Subscription Registry using the ADD/EDIT SUBSCRIPTIONS option. One subscriber is added to the new subscriber list.

Select HLO DEVELOPER MENU Option: ADD/EDIT SUBSCRIPTIONS

Select HLO SUBSCRIPTION REGISTRY NAME: HLO DEMONSTRATION APPLICATION

Are you adding ’HLO DEMONSTRATION APPLICATION' as a new HLO SUBSCRIPTION REGISTRY (the 21ST)? No// Y (Yes)

NAME: HLO DEMONSTRATION APPLICATION Replace

OWNER APPLICATION: HLO

DESCRIPTION: SUBSCRIPTION LIST FOR HLO’S DEMONSTRATION APPLICATION

Select RECEIVING APPLICATION: HLO DEMO RECEIVING APPLICATION

Are you adding ’HLO DEMO RECEIVING APPLICATION' as

a new RECEIVING APPLICATION (the 1ST for this HLO SUBSCRIPTION REGISTRY)? No// YES

MIDDLEWARE LOGICAL LINK:

RECEIVING FACILITY LOGICAL LINK: VAALB

DATE/TIME TERMINATED:

Select RECEIVING APPLICATION:

In the example above, since the messages won’t be routed through middleware such as an interface engine, the MIDDLEWARE LOGICAL LINK was not entered.

Entering a DATE/TIME TERMINATED indicates that the subscription is terminated and would cause messages to that particular subscriber to stop.

### The Programming Interface for Creating Subscription Lists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An application may create a subscription list programmatically. For example, it could be used to send a patient’s health data to a special registry if an indicator is present. The following framework explains how to use the subscription API’s to do that.

<u>Step 1:</u> Create an entry in the HLO SUBSCRIPTION REGISTRY file (#779.4).

This is accomplished by calling \$\$CREATE^HLOASUB(OWNER,DESCRIPTION,.ERROR). The function returns the IEN of the newly created entry. The NAME field (#.01) is automatically set to the IEN.

Example: Creating a new subscription list.

S IEN=\$\$CREATE^HLOASUB(“HLO DEMO APPLICATION”,”PATIENTS IN SPECIAL REGISTRY”)

<u>Step 2:</u> (Optional) Add lookup values for the new entry.

In step 1, an IEN is returned for the new subscription list. An application may store that IEN, in which case lookup values are not necessary, though still useful. However, if the IEN is *not* stored by the application, then it *must* add lookup values to uniquely identify the subscription list, because otherwise it would be unable to find the subscription.

Lookup values are added by calling \$\$INDEX^HLOASUB1(IEN,.LOOKUP)

If used, the application may add up to five lookup values. They will be used to create an index that will enable the application to find the subscription. If the owner name is not sufficiently unique, then at least one of the lookup values must be namespaced to insure its uniqueness. If the subscription is patient specific, at least one of the lookup values must contain a unique patient identifier, such as the DFN or ICN.

Example: Adding lookup values for the subscription list, where IEN=the IEN of the entry just created, and DFN is the patient DFN.

N LOOKUP

S LOOKUP(1)=”HLO PATIENT REGISTRY”

S LOOKUP(2)=DFN

I \$\$INDEX^HLOASUB(IEN,.LOOKUP) ;then success

After doing this, the application can find the subscription list by using \$\$FIND^HLOSUB1(OWNER,.LOOKUP).

Example: Finding the subscription using the lookup values.

N LOOKUP,IEN

S LOOKUP(1)=”HLO PATIENT REGISTRY”

S LOOKUP(2)=DFN

S IEN=\$\$FIND^HLOASUB1(“HLO DEMO APPLICATION”,.LOOKUP)

<u>Step 3:</u> Adding subscribers to the subscriber list.

For each destination where these messages should be sent, call \$\$ADD^HLOASUB(IEN,.WHO,.ERROR) to add that destination as a subscriber. The WHO parameter is an array that is used to identify the name of the receiving application and the receiving facility, and a link over which to send the message.

Example: Adding a subscriber to the list, where IEN is the IEN of the list.

N WHO

S WHO(“RECEIVING APPLICATION”)=”HLO DEMO RECEIVING APPLICATION”

S WHO(“STATION NUMBER”)=500

S WHO(“MIDDLEWARE LINK NAME”)=”VAVIE”

I \$\$ADD^HLOASUB(IEN,.WHO,.ERROR) ;then the subscriber was successfully added, else ERROR would contain an error message.

The identification of a link for middleware in the WHO parameter array is optional and only necessary if the messages will go through middleware such as an interface engine. Also, there are several choices for how to identify the receiving facility, either by station number, IEN of an entry in the INSTITUTION file (#4), or an entry in the HL LOGICAL LINK file (#870).

## Turning Messaging On/Off

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An application may need to build in the capability of turning its message generation on or off. HLO provides some support for that via the HLO Application Registry and the INACTIVATE SENDING APPLICATION option, which is on the APPLICATION REGISTRY MENU \[HLO APPLICATION REGISTRY MENU\] under the DEVELOPER MENU \[HLO DEVELOPER MENU\]. Using the INACTIVATE SENDING APPLICATION option \[HLO TERMINATE OUTGOING MESSAGE\] a user may turn on or off a sending application’s messages.

Example: Using the INACTIVATE SENDING APPLICATION option to set the ADT~A08 messages inactive flag.

Select APPLICATION REGISTRY MENU Option: INACTIVATE SENDING APPLICATION

Select HLO APPLICATION REGISTRY APPLICATION NAME: HLO DEMO SENDING APPLICATION

APPLICATION NAME: HLO DEMO SENDING APPLICATION Replace

Select HL7 MESSAGE TYPE: ADT

Are you adding ’ADT' as a new HL7 MESSAGE TYPE (the 1ST for this HLO APPLICATION REGISTRY)? No// Y (Yes)

HL7 MESSAGE TYPE HL7 EVENT: A08

HL7 MESSAGE TYPE HL7 VERSION:

HL7 EVENT: A01//

HL7 VERSION:

INACTIVE: INACTIVE

> **NOTE:** The application must be designed to honor the inactive flag - otherwise it will have no effect!

To enable this ability, the application must check the flag within its event trigger code. If the flag is set to INACTIVE, the application should quit without generating the message. The flag is checked by calling \$\$ACTIVE^HLOAPP(APP,MSGTYPE,EVENT,VERSION)

Example: Designing the sending application to honor the INACTIVE flag.

This example refers to A08^HLODEM1 in the section on Code Examples. To build in an ON/OFF switch for the ADT~A08 message, the application could insert the following line of code at the A08^HLODEM1.

A08 ;

Q:‘\$\$ACTIVE^HLOAPP(“HLO DEMO SENDING APPLICATION”,”ADT”,”A01”)

# Receiving Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Applications receive their messages by following these steps:

1.  The receiving application must be registered in the HLO Application Registry (file \# 779.2).
2.  The HLO server process follows the algorithm described in section 1.4.2 Server Behavior. It reads the message and parses the header.
3.  Using the name of the receiving application, type of message (BHS or MSH), message type, event type, and version, it does a lookup on the HLO Application Registry (file 779.2) to determine the application routine that should be executed to process the message.
4.  If the lookup fails, and a commit acknowledgment was requested, the HLO server will return an error to the sending system. The message status is set to error and appears in HLO’s log of message errors.
5.  If the lookup succeeds, the server places the message on an incoming queue, with information about the application routine to execute.
6.  Another HLO process operates continuously in the background, looking for new messages on the incoming queue. For each new message, it executes the application routine that was specified in the HLO Application Registry for the receiving application.
7.  The application routine is responsible for parsing the message and taking appropriate actions. HLO provides a set of APIs for parsing the message and for returning application acknowledgments.

## Setting up the Receiving Application in the HLO Application Registry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order for an application to receive messages, it must be entered in the HLO APPLICATION REGISTRY file (#779.2) at the site. The primary purpose is to designate which application routine should be executed to process which incoming message. The application may designate a default message handler, a message handler for batch messages, and specific message handlers for specific messages. The application may also designate private queues to place the messages, the alternative is that the messages are by default placed on an incoming queue named ’DEFAULT’.

Using the ADD/EDIT RECEIVING APPLICATION option \[HLO EDIT RECEIVING APPLICATION\] on the APPLICATION REGISTRY MENU \[HLO APPLICATION REGISTRY MENU\], which in turn is under the HL7 (Optimized) MAIN MENU option \[HLO MAIN MENU\], create an entry for the receiving application.

Applications in the HLO Application Registry (file 779.4) can be included in a KIDS build as other components such as protocols, and included in software distributions.

> **NOTE:** The name of the receiving application must be unique within the enterprise. Wherever possible, the name should be namespaced.

Example: Adding a receiving application to the HLO Application Registry.

Select APPLICATION REGISTRY MENU Option: ADD/EDIT RECEIVING APPLICATION

Select HLO APPLICATION REGISTRY APPLICATION NAME: HLO DEMO RECEIVING APPLICATION

Are you adding ’HLO DEMO RECEIVING APPLICATIONS' as a new HLO APPLICATION REGISTRY (the 70TH)? No// Y (Yes)

APPLICATION NAME: HLO DEMO RECEIVING APPLICATIONS

Replace

Package File Link: HLO HL7 OPTIMIZED (HLO) HLO

Do you want to edit the setup for receiving batch messages? NO// YES

BATCH ACTION ROUTINE: HLODEM7

BATCH ACTION TAG: BATCH

If a private queue is used for batches its name must be namespaced!

BATCH PRIVATE IN-QUEUE: HLO DEM BATCH

Select HL7 MESSAGE TYPE: ADT

Are you adding ’ADT' as a new HL7 MESSAGE TYPE (the 1ST for this HLO APPLICATION REGISTRY)? No// Y (Yes)

HL7 MESSAGE TYPE HL7 EVENT: A08

HL7 MESSAGE TYPE HL7 VERSION:

ACTION ROUTINE: HLODEM5

ACTION TAG: PARSEA08

If a private queue is used the name must be namespaced!

PRIVATE QUEUE (optional): HLO DEMO A08

Select HL7 MESSAGE TYPE:

Do you want to edit the default action for non-specified messages types? NO// YES

DEFAULT ACTION ROUTINE: HLODEM5

DEFAULT ACTION TAG: PARSEMSG

If you specify a private queue for the default action then its name must be namespaced!

DEFAULT PRIVATE QUEUE (optional):

If application acknowledgments are returned, and they must go through a specific link, enter it here. This applies if an interface engine or other middleware is used.

RETURN LINK FOR APPLICATION ACKNOWLEDGMENTS:

## ## ## List of Message Parsing APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 28%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">STARTMSG^HLOPRS</th>
<th><p>Begin parsing the message.</p>
<p>Parsing a message always starts with a call to this API.</p>
<p>The message header fields are returned to the application.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2">NEXTMSG^HLOPRS</td>
<td><p>Moves the parser to the next message within the batch.</p>
<p>Applies only to batch messages.</p></td>
</tr>
<tr class="even">
<td colspan="2">NEXTSEG^HLOPRS</td>
<td><p>Moves the parser to the next segment within the individual message.</p>
<p>Applies to parsing both individual messages and batch messages.</p>
<p>The individual values are parsed out from the segment, and escape sequences are automatically replaced with the original characters.</p></td>
</tr>
<tr class="odd">
<td colspan="3"><p><strong>APIs for Parsing HL7 Data Types from a Segment</strong></p>
<p>These APIs are always invoked after a call to NEXTSEG^HLOPRS to obtain data from the returned segment. The application specifies the field, component, subcomponent, and repetition.</p></td>
</tr>
<tr class="even">
<td></td>
<td>GET^HLOPRS</td>
<td><p>Parses an individual value from a segment.</p>
<p>Use this if HLO does not provide a special API to parse the data type. If the data type contains multiple parts, call this API multiple times, once for each part.</p></td>
</tr>
<tr class="odd">
<td></td>
<td>GETAD^HLOPRS2</td>
<td>Parses an address, data type AD, from a segment.</td>
</tr>
<tr class="even">
<td></td>
<td>GETCE^HLOPRS2</td>
<td>Parses a coded element, data type CE.</td>
</tr>
<tr class="odd">
<td></td>
<td>GETCNE^HLOPRS2</td>
<td>Parses a coded value with no exceptions, data type CNE.</td>
</tr>
<tr class="even">
<td></td>
<td>GETCWE^HLOPRS2</td>
<td>Parses a coded value with exceptions, data type CWE.</td>
</tr>
<tr class="odd">
<td></td>
<td>GETDT^HLOPRS2</td>
<td>Parses a date, data type DT.</td>
</tr>
<tr class="even">
<td></td>
<td>GETHD^HLOPRS2</td>
<td>Parses an HL7 hierarchic designator, data type HD.</td>
</tr>
<tr class="odd">
<td></td>
<td>GETXPN^HLOPRS2</td>
<td>Parses an extended person’s name, data type XPN.</td>
</tr>
<tr class="even">
<td colspan="3"><strong>Miscellaneous APIs</strong></td>
</tr>
<tr class="odd">
<td colspan="2">HLNEXT^HLOMSG</td>
<td><p>Returns the segment as an array of lines. Example: SEGMENT(1),</p>
<p>SEGMENT(2), etc.</p>
<p>This is different from NEXTSEG^HLOPRS in that HLNEXT^HLOMSG does not parse the segment into its individual pieces.</p>
<p>If using this API, it is totally up to the application to parse the data from the segment. There are no HLO APIs to assist.</p>
<p>Applications are responsible for replacing escape sequences with the original characters.</p>
<p>If the segment fits within a single node, the array returned will have only</p>
<p>one subscript=1. <strong>Example</strong>: SEGMENT(1)</p></td>
</tr>
<tr class="even">
<td colspan="2">MSGID^HLOPRS</td>
<td>Given the IEN of the message, in the HLO MESSAGES file (#778), this API returns the Control ID found in the message header.</td>
</tr>
</tbody>
</table>

## HLO Parses the Message Header

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An application always begins parsing a message by calling STARTMSG^HLOPRS. A call to \$\$STARTMSG^HLOPRS(.MSG,\<message ien, file \#778\>,.HDR) returns administrative information about the message, the header segment, and the header segment’s parsed fields.

The following is a partial list of the MSG array subscripts returned. See section 5.2.1 for a complete list of the subscripts returned and available to the developer. (Start Parsing a Message)

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th>MSG(“BATCH”)</th>
<th>If the segment type is BHS, it returns 1. If it is NOT a batch message, it returns 0.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MSG("ID")</td>
<td>If the header type is MSH, it returns the Message Control ID. If the header type is BHS, it returns the Batch Control ID.</td>
</tr>
<tr class="even">
<td>MSG("EVENT")</td>
<td>The HL7 event, only returned if the segment type is MSH.</td>
</tr>
<tr class="odd">
<td>MSG("MESSAGE TYPE")</td>
<td><p>The HL7 message type. It is returned if the segment types is MSH, but NOT if</p>
<p>it is BHS.</p></td>
</tr>
<tr class="even">
<td>MSG(“HDR”,1)</td>
<td>The unparsed message header, field sequence1 through 6.</td>
</tr>
<tr class="odd">
<td>MSG(“HDR”,2)</td>
<td>The unparsed message header, field sequence 7 to the end.</td>
</tr>
</tbody>
</table>

In addition, HLO will return all the fields from the header segment and return them in an array, passed-by-reference in the third parameter. The next two sections specify what subscripts are returned in the case of a BHS segment and in the case of an MSH segment.

### Parsing the MSH Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For an individual message, as opposed to a batch message, a call to \$\$STARTMSG^HLOPRS (.MSG,\<message IEN, HLO MESSAGES file ( \#778)\>,.HDR) will return the HDR array with the following subscripts. Any escape sequences found within the returned value will be replaced with the original character.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 44%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Sequence</strong></th>
<th><strong>Subscript</strong></th>
<th><strong>Description/Comment</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0</td>
<td>“SEGMENT TYPE”</td>
<td>“MSH”</td>
</tr>
<tr class="even">
<td>1</td>
<td>“FIELD SEPARATOR”</td>
<td>The field separator</td>
</tr>
<tr class="odd">
<td>2</td>
<td><p>“COMPONENT SEPARATOR”</p>
<p>“SUBCOMPONENT SEPARATOR”</p>
<p>“REPETITION SEPARATOR”</p>
<p>“ESCAPE CHARACTER”</p></td>
<td>The message delimiters</td>
</tr>
<tr class="even">
<td>3</td>
<td>“SENDING APPLICATION”</td>
<td>The name of the sending application</td>
</tr>
<tr class="odd">
<td>4</td>
<td><p>“SENDING FACILITY”,1</p>
<p>“SENDING FACILITY”,2</p>
<p>“SENDING FACILITY”,3</p></td>
<td><p>First Component</p>
<p>Second Component</p>
<p>Third Component</p></td>
</tr>
<tr class="even">
<td>5</td>
<td>“RECEIVING APPLICATION”</td>
<td>The name of the receiving application</td>
</tr>
<tr class="odd">
<td>6</td>
<td><p>“RECEIVING FACILITY”,1</p>
<p>“RECEIVING FACILITY”,2</p>
<p>“RECEIVING FACILITY”,3</p></td>
<td><p>First Component</p>
<p>Second Component</p>
<p>Third Component</p></td>
</tr>
<tr class="even">
<td>7</td>
<td>“DT/TM OF MESSAGE”</td>
<td>Converted to FileMan format</td>
</tr>
<tr class="odd">
<td>8</td>
<td>“SECURITY”</td>
<td><p>The security field, which is specific to the</p>
<p>application.</p></td>
</tr>
<tr class="even">
<td>9</td>
<td><p>“MESSAGE TYPE”</p>
<p>“EVENT”</p>
<p>“MESSAGE STRUCTURE”</p></td>
<td><p>First Component</p>
<p>Second Component</p>
<p>Third Component</p></td>
</tr>
<tr class="odd">
<td>10</td>
<td>“MESSAGE CONTROL ID”</td>
<td>A unique ID for the message</td>
</tr>
<tr class="even">
<td>11</td>
<td><p>“PROCESSING ID”</p>
<p>“PROCESSING MODE”</p></td>
<td><p>First Component</p>
<p>Second Component</p></td>
</tr>
<tr class="odd">
<td>12</td>
<td>“VERSION”</td>
<td><p>The version of the HL7 standard on which</p>
<p>the message was based</p></td>
</tr>
<tr class="even">
<td>14</td>
<td>“CONTINUATION POINTER”</td>
<td><p>MESSAGE CONTROL ID of the message</p>
<p>that this one continues.</p></td>
</tr>
<tr class="odd">
<td>15</td>
<td>“ACCEPT ACK TYPE”</td>
<td><p>ACCEPT ACKNOWLEDGMENT TYPE,</p>
<p>&lt;AL or NE&gt;</p></td>
</tr>
<tr class="even">
<td>16</td>
<td>“APP ACK TYPE”</td>
<td><p>APPLICATION ACKNOWLEDGMENT</p>
<p>TYPE = &lt;AL or NE&gt;</p></td>
</tr>
<tr class="odd">
<td>17</td>
<td>“COUNTRY”</td>
<td>COUNTRY CODE</td>
</tr>
</tbody>
</table>

### Parsing the BHS Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A call to \$\$STARTMSG^HLOPRS(.MSG,\<message IEN, HLO MESSAGES file ( \#778)\>,.HDR) will return the HDR array with the following subscripts. Any escape sequences found within the returned value will be replaced with the original character.

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 40%" />
<col style="width: 3%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Sequence</strong></th>
<th colspan="2"><strong>Subscript</strong></th>
<th><strong>Description/Comment</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0</td>
<td colspan="2">“SEGMENT TYPE”</td>
<td>“BHS”</td>
</tr>
<tr class="even">
<td>1</td>
<td colspan="2">“FIELD SEPARATOR”</td>
<td>The field separator</td>
</tr>
<tr class="odd">
<td>2</td>
<td colspan="2"><p>“COMPONENT SEPARATOR”</p>
<p>“SUBCOMPONENT SEPARATOR”</p>
<p>“REPETITION SEPARATOR”</p>
<p>“ESCAPE CHARACTER”</p></td>
<td>The message delimiters</td>
</tr>
<tr class="even">
<td>3</td>
<td colspan="2">“SENDING APPLICATION”</td>
<td>The name of the sending application</td>
</tr>
<tr class="odd">
<td>4 See Note</td>
<td colspan="2"><p>“SENDING FACILITY”,1</p>
<p>“SENDING FACILITY”,2</p>
<p>“SENDING FACILITY”,3</p></td>
<td><p>First Component</p>
<p>Second Component</p>
<p>Third Component</p></td>
</tr>
<tr class="even">
<td>5</td>
<td colspan="2">“RECEIVING APPLICATION”</td>
<td>The name of the receiving application</td>
</tr>
<tr class="odd">
<td>6 See Note</td>
<td colspan="2"><p>“RECEIVING FACILITY”,1</p>
<p>HEAD “RECEIVING FACILITY”,2</p>
<p>“RECEIVING FACILITY”,3</p></td>
<td><p>First Component</p>
<p>Second Component</p>
<p>Third Component</p></td>
</tr>
<tr class="even">
<td>SEQ-7</td>
<td colspan="2">“DT/TM OF MESSAGE”</td>
<td>Converted to FileMan Format</td>
</tr>
<tr class="odd">
<td>SEQ-8</td>
<td colspan="2">“SECURITY”</td>
<td>Specific to the application</td>
</tr>
<tr class="even">
<td>SEQ-9</td>
<td colspan="3"><p>“BATCH NAME/ID/TYPE”</p>
<p>These fields are not defined by the standard within the BHS segment, but they</p>
<p>are needed and are encoded in BHS-9 by the VistA HLO software:</p>
<blockquote>
<p>“PROCESSING ID”</p>
<p>“ACCEPT ACK TYPE”</p>
<p>“APP ACK TYPE”</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SEQ-10</td>
<td colspan="3">“BATCH COMMENT”</td>
</tr>
<tr class="even">
<td>SEQ-11</td>
<td>“BATCH CONTROL ID”</td>
<td colspan="2">A unique ID for the message</td>
</tr>
<tr class="odd">
<td>SEQ-12</td>
<td>“REFERENCE BATCH CONTROL ID”</td>
<td colspan="2"><p>If this batch message contains application</p>
<p>acknowledgments from another batch, this will</p>
<p>be the BATCH CONROL ID of the original</p>
<p>batch.</p></td>
</tr>
</tbody>
</table>

> **NOTE:** BHS-4 & BHS-6 The HL7 Version 2.4 Standards Manual does not document this, but components 2 & 3

were added in an erratum to be compatible with the MSH segment. It is documented in version 2.5 of the

standard.

## Stepping Through an Individual Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Message parsing always starts with these steps:

- When a message is received, HLO executes the application’s message handler routine in the background.
- At that point, the ONLY variables defined are:
  - HLMSGIEN set to the IEN of the message in the HLO MESSAGES file, \#778.
  - The variables are defined by calling DUZ^XUP with DUZ set to .5, which is a proxy for the Postmaster.
- The application must call \$\$STARTMSG^HLOPRS to start parsing the message. The API will return information about the message and the fields parsed from the header. (see section 3.3)

At this point, the application steps through the message segment by segment, parsing each for its data. But there are two different methods for parsing the individual segment.

### Method 1 – Using \$\$NEXTSEG^HLOPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the preferred method for parsing segments within HLO because it automatically parses the segment into all its parts and automatically replaces escape sequences for delimiters with the original characters. Another advantage is that using this method results in routines that are self-documenting and less prone to the type of errors that occur with hard-coded parsing.

Calling \$\$NEXTSEG^HLOPRS accomplishes the following:

- The parser is moved forward one segment and the segment is returned. The function returns 1 if a segment is returned, and 0 if there are no more segments in the message. If called within a batch, 0 is returned if the end of the individual message is reached, even if there are more messages within the batch.
- The segment is totally parsed into its individual parts.
- If the segment contained any escape sequences for message delimiters, they are automatically replaced by the original characters.

After calling \$\$NEXTSEG^HLOPRS, the application then calls the data type parsing APIs (see section 3.2) to retrieve the field values.

### Method 2 – Using \$\$HLNEXT^HLOMSG

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This method is modeled after HL7 1.6 message parsing and is provided so that older applications may use their existing HL7 1.6 message parsers for messaging with HLO. Its use is discouraged for new applications.

Calling \$\$HLNEXT ^HLOMSG accomplishes the following:

- The parser is moved forward one segment and the segment is returned. The function returns 1 if a segment is returned, and 0 if there are no more messages in the segment. If called within a batch, 0 is returned if the end of the individual message is reached, even if there are more messages within the batch.
- The segment is NOT parsed. The application is responsible for parsing out the data. If the data contains escape sequences, the application is responsible for replacing them with the original characters.

There are differences between using \$\$HLNEXT^HLOMSG and parsing in HL7 1.6:

- In HL7 1.6, the variable HLNEXT is executed with the M EXECUTE command to move the parser to the next segment, rather than calling it as a function: X HLNEXT.
- If parsing a batch message, \$\$HLNEXT will NOT move the parser to the next message within the batch when the current message’s end is reached.

### Examples of Message Parsing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: A simple message parser.

N MSG,HDR,SEG

I ’\$\$STARTMSG^HLOPRS(.MSG,HLMSGIEN,.HDR) {report error} QUIT

F Q:’\$\$NEXTSEG^HLOPRS(.MSG,.SEG) D

.I SEG(“SEGMENT TYPE”)={3 character segment type} D

..{use HLO’s data type parsing routines to retrieve the data from the segment}

In this example:

- HLMSGIEN is the internal entry number of the message record in the HLO MESSAGES file (#778). If HLO is executing the application’s routine in the background, then HLO will set that variable for the application’s use.
- MSG stores information about the message, including the parser’s current position in the message.
- HDR will contain the fields that were parsed from the message header.
- SEG will contain the fields that were parsed from the current segment.
- Parsing always starts off with a call to \$\$STARTMSG^HLOPRS. It returns both the MSG array and the HDR array. If the function returns 0, then something is wrong – the message record has been deleted or is corrupted!
- After calling \$\$STARTMSG^HLOPRS, the HLO parser is pointing to the message header. Calling \$\$NEXTSEG^HLOPRS iteratively will step the parser through the message’s other segments.
- After each call to \$\$NEXTSEG^HLOPRS, the HLO parser will return with the segment, parsed into its fields, components, and subcomponents, with any escape sequences replaced with the original characters.
- At that point, the application uses the HLO data type parsing APIs to extract the needed data.
- If \$\$NEXTSEG^HLOPRS returns 0, it means that there are no more segments left in the message.

Example 11: In this example, the set up for the receiving application in the HLO APPPLICATION REGISRY file (#779.2) does not include a specific handler for the ADT~A08 message, but does specify a default message handler. When an ADT~A08 message is received, HLO will execute the default handler and it is up to the application to determine what specific action to take based on the message type and event.

Note that the HLO APPLICATION REGISTRY specifies that HLO should place this application’s messages on a private queue named ’HLO DEMO CLIENT’. That is an optional feature. If a private queue was not specified, then the application’s messages would be placed on a generic queue named “DEFAULT.”

See PARSEMSG^HLODEM5 in the section on Code Examples.

Example 12: In this example, the set up for the receiving application in the HLO APPPLICATION REGISRY file (#779.2) does specify a message handler for the ADT~A08 message. That means that at the point when the applications message handler is executed by HLO, the routine already knows that the message is an ADT~A08. See PARSEA08^HLODEM5 in the section on Code Examples.

Example 13: In this example, the PID segment built in example 1 is parsed using the HLO segment parsing APIs. Note that each of the segment building APIs that inserts a data type into a segment has a corresponding API that parses the data type from the segment. See PID^HLODEM5 in the section on Code Examples.

Example 14: In this example, the NK1 segment built in example 3 is parsed using the HLO segment parsing APIs. See NK1^HLODEM5 in the section on Code Examples.

Example 15: In this example, the ADT~A08 message is parsed using hard-coded segment parsers. See PARSEA08^HLODEM6 in the section on Code Examples.

This example makes two WRONG assumptions:

1.  That escape sequences do not appear in the message.
2.  That the entire segment is stored on one node.

> **WARNING:** With hardcoded segment parsers, the application is responsible for replacing escape sequences with the original characters. The application should NOT assume that the entire segment is contained in a single node.

## Stepping through a Batch of Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A batch of messages is processed in a nearly identical manner to an individual message with these differences:

1.  As with an individual message, the receiving application needs to be entered to the HLO APPLICATION REGISTRY, file \# 779.2. However, the application needs to specify an application routine to execute when a batch of messages is received. It is up to that application routine to step through the batch of messages and determine each message’s type and to process it accordingly.
2.  The parsing of a batch starts off with a call to \$\$STARTMSG^HLOPRS, just as it does when parsing an individual message, but in addition the \$\$NEXTMSG^HLOPRS API is used to step through the batch of messages. Calling \$\$NEXTMSG^HLOPRS moves the parser to the next message within the batch.
3.  If an application acknowledgment is required, the receiving application should return a batch of acknowledgments rather than an individual acknowledgment for each message within the original batch.

Example: Here is the general form for parsing a batch of messages. For simplicity, the steps needed to return application acknowledgments is not included here, but will be covered in a later section.

;{Create your workspace.}

N MSG,BHS,MSH,SEG

;

;{Start the parsing.}

I ’\$\$STARTMSG^HLOPRS(.MSG,HLMSGIEN,.BHS) D Q

.{The message is lost or corrupted! Call an exception handler}

;

;{Step through the individual messages that are in the batch.}

F Q:’\$\$NEXTMSG^HLOPRS(.MSG,.MSH) D

.;

.:{If its not known in advance what type of messages the batch contains, then determine that from the message header.}

.I MSH(“MESSGE TYPE”)=”ADT”,MSH(“EVENT”)=”A08” D

..;

..;{Now step through the segments of the message.}

..F Q:’\$\$NEXTSEG^HLOPRS(.MSG,.SEG) D

…;

…;{Look at the segment type, then parse the needed data for that segment.}

…I SEG(“SEGMENT TYPE”)={3 character segment type} D

….;

….;{Use HLO’s data type parsing routines to retrieve the data from the segment.}

..;

..;{Now that all the data has been retrieved from the message, process it.}

In this example:

- HLMSGIEN is the internal entry number of the message record in the HLO MESSAGES file (#778). If HLO is executing the application’s routine in the background, then HLO will set that variable for the application’s use.
- MSG is used by the HLO parser to keep track of the current message and segment.
- BHS will contain the fields that were parsed from the batch message header.
- Parsing always starts off with a call to \$\$STARTMSG^HLOPRS. It returns both the MSG array and the BHS array. If the function returns 0 then something is wrong – the message record has been deleted or is corrupted!
- To verify that this is a batch message rather than an individual message, the application may check MSG(“BATCH”)=1.
- After calling \$\$STARTMSG^HLOPRS, the HLO parser is pointing to the batch message header. Calling \$\$NEXTMSG^HLOPRS iteratively will step the parser through the messages within the batch.
- \$\$NEXTMSG^HLOPRS returns 1 if the parser has advanced to the next message. In that case, MSH will contain the individual fields parsed from the individual message header. The application can check the values of MSH(“MESSAGE TYPE”) and MSH(“EVENT”) to determine the type of message. HLO allows a batch of messages to contain mixed message types, though that is rarely done in practice.
- \$\$NEXTMSG^HLOPRS returns 0 if there are no more messages within the batch.
- After calling \$\$NEXTMSG^HLOPRS, the application then steps through that individual message’s segments by calling \$\$NEXTSEG^HLOPRS, and parses that message in an identical manner to a message that is not contained within a batch.

Example 16

This is an example of parsing a batch of messages. The batch of messages consists of the ADT~A08 messages created in example 5. See BATCH^HLODEM7 in the appendix of code examples.

# Acknowledgement Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLO supports the two-phase enhanced acknowledgment protocol of the HL7 standard. The first phase is the exchange of a commit acknowledgment, also known as the accept acknowledgment. The second phase is the exchange of an application acknowledgment.

The sending application controls which acknowledgments to request. The information is encoded in the message header. For individual messages, the MSH-15 controls the Accept Acknowledgment Type and MSH-16 controls the Application Acknowledgment Type. *For batch messages, the standard does not provide a specific mechanism for requesting acknowledgments within the batch header. HLO encodes the information in a non-standard way using BHS-9.* As a result, batch messages cannot be exchanged between HLO and other messaging systems without customization.

The return of a commit acknowledgment signifies that the receiving system received the message and committed it to safe storage, and furthermore promises to deliver it to the receiving application.

> **NOTE:** It is highly recommended that applications request the return of commit acknowledgments because otherwise there can be no reasonable certainty that a message will actually be delivered. Electronic communications can fail without warning!

The return of an application acknowledgment signifies that the receiving application processed the message. The distinguishing feature of an application acknowledgment is that it contains an MSA segment, not the message type or event. The MSA segment contains the message id of the original message and an acknowledgment code. The application acknowledgment message may contain segments with information related to the original message, such as the response to a query message. There is no general rule as to whether or not an application should use application acknowledgments, as its use is dictated by the specific requirements of the application.

## Requesting Acknowledgments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The sending application indicates which acknowledgments to request at the point of calling one of the SEND API’s listed in section 2.5, group 1.4. These parameters control which acknowledgments are requested:

PARMS(“ACCEPT ACK TYPE”) = “NE” means DO NOT request the commit ack.

= “AL” means DO request a commit ack.

= “” or left undefined – defaults to “AL”

If the application does request a commit acknowledgment, it may optionally indicate a callback routine as described in section 2.7.2. The routine will be executed by HLO when the commit acknowledgment is returned.

PARM(“ACCEPT ACK RESPONSE”) = \<routine tag\>^\<routine\>

Similarly, whether to request an application acknowledgment is controlled by this parameter:

PARMS(“APP ACK TYPE”) = “NE” means DO NOT request an application acknowledgment.

= “AL” means DO request an application acknowledgment.

= “” or undefined - defaults to “NE”

If the application does request an application acknowledgment, it may optionally indicate a callback routine as described in section 2.7.1. The routine will be executed by HLO when the application acknowledgment is returned. Although the use of a callback is optional, there is generally little point to requesting an application acknowledgment unless the application plans on taking some action upon its receipt.

PARMS(“APP ACK RESPONSE”) = \<routine tag\>^\<routine\>

Example: In this code snippet the application requests both a commit acknowledgment and an application acknowledgment. The application routine APPACK^HLODEM8 will be executed upon receipt of the application acknowledgment.

S PARMS(“ACCEPT ACK TYPE”)=”AL”

S PARMS(“APP ACK TYPE”)=”AL”

S PARMS(“APP ACK RESPONSE”)=”APPACK^HLODEM8”

I ’\$\$SENDONE^HLOAPI1(.MSG,.PARMS,.WHOTO,.ERROR) ;{perform exception processing on failure}

For application acknowledgments an alternative to setting up a callback routine as an input parameter is to register the application acknowledgment’s message type and event in the HLO Application Registry (file \#779.2). In either case, the result is identical – HLO will execute the application’s routine when an application acknowledgment is received. At the point the application’s routine is executed, the variable HLMSGIEN is set to the IEN of the application acknowledgment message. As always, the application should start processing the message by calling \$\$STARTMSG^HLOPRS(.MSG,HLMSGIEN,.HDR), which in addition to returning the usual information will also return the identity of the original message as follows:

MSG(“ACK TO”) = the message id of the original message

MSG(“ACK TO IEN”) = the IEN of the original message in the HLO MESSAGES file (#778)

Example: As an alternative to adding a callback routine via an input parameter, as in the example above, the application could instead use the HLO Application Registry (file \#779.2) to indicate what action to execute when an application acknowledgment is received. Here is how that could be accomplished:

APPLICATION NAME: HLO DEMO CLIENT

HL7 MESSAGE TYPE: ACK HL7 EVENT: A01

ACTION TAG: APPACK ACTION ROUTINE: HLODEM8

Package File Link: HL7 OPTIMIZED (HLO)

Example: This is an example of processing a returned application acknowledgment. In the case of an error, the application generates an alert to the support staff and reschedules the purge date of the original message so that there is plenty of time to correct the error. No action is taken if the acknowledgment does not return an error, but if this were, for example, a query result the application would process it. See APPACK^HLODEM8 in the appendix of code examples.

## Returning Acknowledgments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Commit Acknowledgments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Commit acknowledgments are returned automatically by HLO with no action needed on the part of the receiving application. The commit acknowledgment consists of only two segments, the MSH and MSA. The message header is an MSH segment with message type of ACK with no event. The MSA segment contains these fields:

MSA-1 Acknowledgment Code = CA, CR, or CE.

MSA-2 Message ID of the original message

MSA-3 if applicable, a text message describing the error

The CA code (commit accept) indicates that the message was accepted by the receiving system and it will be passed to the receiving application. The CR (commit reject) and CE (commit error) codes indicate that some error condition was encountered and as a result the message will NOT be passed to the application.

### Application Acknowledgments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is the receiving application’s responsibility to return an application acknowledgment if requested.

Individual Messages:

For an individual message, the receiving application may return an acknowledgment by following these steps:

1.  As usual, \$\$STARTMSG^HLOPRS(.MSG,HLMSGIEN,.HDR) is called to begin processing the original message.
2.  If HDR(“APPLICATION ACK TYPE”)=”AL” then the application must return an acknowledgment. If it is known in advance from the negotiated interface specification that an acknowledgment is required, then the test may be skipped.
3.  Call \$\$ACK^HLOAPI2(.MSG,.PARMS,.ACK,.ERROR) to begin the process of creating the return message, where:
    1.  MSG contains information about the original message, obtained in step 1.
    2.  The PARMS array may contain these input parameters:

> PARMS(“ACK CODE”) - AA, AE, or AR (required)

> PARMS(“ERROR MESSAGE”) - text describing the error (optional)

> PARMS(“MESSAGE TYPE”) - message type of return message, defaults to “ACK”

> PARMS(“EVENT”) - event type of return message, defaults to the

> event of the original message.

> PARMS(“FIELD SEPARATOR”) - defaults to “\|”

> PARMS(“ENCODING CHARACTERS”) – defaults to “^~\\”

3.  ACK is an array where the acknowledgment message is being constructed.
4.  Optionally, the application may add segments to ACK in the usually manner. The application should not add a message header segment as that is always done automatically. The application may add an MSA segment, but if it does not, then one will be added automatically.
5.  Call \$\$SENDACK^HLOAPI2 to complete the message and queue it for delivery.

Example: In this example, an application acknowledgment is returned. The message type defaults to ACK, the event defaults to the event of the original message, and the message delimiters default to the standard ones. The application chose to add an ERR segment to the acknowledgment message. The MSA segment with the AA code in MSA-1 and the message id of the original message in MSA-2 is automatically included in the message, since the application did not specifically add an MSA segment.

N MSH,HDR,ACK,SEG,PARMS

;

;start parsing the message

I ’\$\$STARTMSG^HLOPRS(MSG,HLMSGIEN,.MSH) {report error} QUIT

;

;{finish parsing the message and process it}

;

;now test if an application acknowledgment was requested

I MSH(“APP ACK TYPE”)=”AL” D

.;

.;an acknowledgment was requested – so build one

. S PARMS(“ACK CODE”)=”AA”

. I ’\$\$ACK^HLOAPI2(.MSG,.PARMS,.ACK,.ERROR) {report error} QUIT

.;

. ;add an ERR segment

. D SET^HLOAPI(.SEG,”ERR”,0)

. D SET^HLOAPI(.SEG,”0”,3)

. D SET^HLOAPI(.SEG,”I”,4)

. I ’\$\$ADDSEG^HLOAPI(.ACK,.SEG) {report error} QUIT

.;

.;send the acknowledgment message – the MSA segment is automatically added

. I ’\$\$SENDACK^HLOAPI2(.ACK,.ERROR) { report error}

Example 17: This example is an extension of example 11. As in that example, this routine also receives and parses an ADT~A08 message, but in addition it returns an application acknowledgment. See PARSEA08^HLODEM10 in the appendix of code examples.

Batch Messages:

For a batch message, application acknowledgments for messages within the original batch are returned via a batch of messages by following these steps:

1.  As usual, \$\$STARTMSG^HLOPRS(.MSG,HLMSGIEN,.BHS) is called to begin processing the original message.
2.  If MSG(“BATCH”)= 1 and HDR(“APPLICATION ACK TYPE”)=”AL” then the application must return a batch of acknowledgments in response to this batch.
3.  Call \$\$BATCHACK^HLOAPI2(.MSG,.PARMS,.ACK,.ERROR) to begin the process of creating the return batch, where:
    1.  MSG contains information about the original message, obtained in step 1.
    2.  The PARMS array may contain input parameters, including these:

> PARMS(“FIELD SEPARATOR”) - defaults to “\|”

> PARMS(“ENCODING CHARACTERS”) – defaults to “^~\\”

3.  ACK is an array where the acknowledgment message is being constructed.
1.  The receiving application should iteratively call \$\$NEXTMSG^HLOPRS to step through the messages of the original batch. After processing each message, the application may add an application acknowledgment to the return batch by calling \$\$ADDACK^HLOAPI3. Optionally, the application may also add other segments prior to calling \$\$ADDACK^HLOAPI3.
2.  Call \$\$SENDACK^HLOAPI2 to complete the return batch of message acknowledgments and queue it for delivery.

Example: Returning a batch of acknowledgment in response to a batch.

N MSG,BHS,ACK,SEG,.ERROR

;{Start the parsing.}

I ’\$\$STARTMSG^HLOPRS(.MSG,HLMSGIEN,.BHS) {report error} QUIT

.;

.;if not known in advance, check whether this is a batch message and if acknowledgments are requested

.;if yes, then start building the return batch in ACK

.I MSG(“BATCH”),BHS(“APP ACK TYPE”)=”AL” I ’\$\$BATCHACK^HLOAPI3(.MSG,,.ACK,.ERROR) D {report error} QUIT

.

;{Step through the individual messages that are in the batch.}

F Q:’\$\$NEXTMSG^HLOPRS(.MSG,.MSH) D

. ;

.{process each message}

.;

.if a return batch is being built, then add an application acknowledgment to the return batch

.S PARMS(“APP ACK CODE”)={”AA”, “AE”, or “AR”}

.I ’\$\$ADDACK^HLOAPI3(.ACK,.PARMS,.ERROR) {report error} QUIT

.;

;now send the return batch

I ’\$\$SENDACK^HLOAPI2(.ACK,.ERROR) {report error}

Example 18: This example is an extension of example 16. As in that example, this routine receives and parses a batch of messages, but in addition it returns a batch of application acknowledgments. See BATCH^HLODEM10 in the section on Code Examples.

### Determining the Return Destination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Commit acknowledgments are always returned immediately over the same open connection as the original messages, so *where* to return the commit acknowledgment is never an issue.

But application acknowledgments are always returned at a later time over a different connection, so *where* to return the application acknowledgment message *is* an issue that needs to be addressed. HLO uses three methods to determine the return link in the HL LOGICAL LINK file (#870) in this order:

1.  The application may optionally specify the return link as an input parameter to \$\$ACK^HLOAPI2 and \$\$BATCHACK^HLOAPI2. This method is recommended only if methods 2 and 3 are not applicable.
2.  The entry for the receiving application in the HLO Application Registry (file \#779.2) can specify a return link. This method is particularly valuable if the message needs to be returned via middleware, such as an interface engine, rather than directly.
3.  If steps 1 and 2 don’t provide the return link, HLO will try to determine it based on the message header of the original message. If the sending facility field contains a TCP/IP domain, or a VHA station number, HLO will perform a lookup on the HL LOGICAL LINK file (#779.2) using those values. If the sending facility of the original message is a VHA medical facility or national database with no middleware involvement, such as an interface engine, this is a reliable method for determining the return link.

> **NOTE:** The Receiving Application and Receiving Facility for the application acknowledgment message header is always based on the Sending Application and Sending Facility of the original message header. The issue discussed above is slightly different – it concerns the determination of the IP address and port to connect with to return the application acknowledgment.

# API Reference Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                           |                                                  |     | Name         | Brief Description                                                                                    | Section |
|-------------------------------------------|--------------------------------------------------|-----|------------------|----------------------------------------------------------------------------------------------------------|-------------|
| Sending Messages                      |                                                  |     |                  |                                                                                                          |             |
|                                           |                                                  |     | NEWMSG^HLOAPI    | Begins a new individual message.                                                                         | 5.1.1       |
|                                           |                                                  |     | NEWBATCH^HLOAPI  | Begins a new batch of messages.                                                                          | 5.1.2       |
|                                           |                                                  |     | ADDMSG^HLOAPI    | Begins a new message within a batch of messages.                                                         | 5.1.3       |
|                                           |                                                  |     | ADDSEG^HLOAPI    | Adds a segment to a message.                                                                             | 5.1.4       |
|                                           |                                                  |     | MOVEMSG^HLOAPI   | Moves a message built in the traditional style as an array of segments into an HLO message.              | 5.1.5       |
|                                           |                                                  |     | MOVESEG^HLOAPI   | Moves a segment built in the traditional style into the HLO message under construction.                  | 5.1.6       |
|                                           | Setting Data into Segments                   |     |                  |                                                                                                          |             |
|                                           |                                                  |     | SET^HLOAPI       | Sets a single atomic value into the segment. Use this if there is no specific API for the HL7 data type. | 5.1.7.1     |
|                                           |                                                  |     | SETAD^HLOAPI4    | Sets an address.                                                                                         | 5.1.7.2     |
|                                           |                                                  |     | SETCE^HLOAPI4    | Sets the CE data type (Coded Element).                                                                   | 5.1.7.3     |
|                                           |                                                  |     | SETCNE^HLOAPI4   | Sets the CNE data type (Coded Element with No Exceptions).                                               | 5.1.7.4     |
|                                           |                                                  |     | SETCWE^HLOAPI4   | Sets the CWE data type (Coded Value with Exceptions)                                                     | 5.1.7.5     |
|                                           |                                                  |     | SETDT^HLOAPI4    | Sets a DT data type (Date).                                                                              | 5.1.7.6     |
|                                           |                                                  |     | SETHD^HLOAPI4    | Sets the HD data type (Hierarchic Designator)                                                            | 5.1.7.7     |
|                                           |                                                  |     | SETTS^HLOAPI4    | Sets the TS data type (Timestamp)                                                                        | 5.1.7.8     |
|                                           |                                                  |     | SETXPN^HLOAPI4   | Sets the XPN data type (Extended Person Name)                                                            | 5.1.7.9     |
|                                           | Addressing and Sending the Completed Message |     |                  |                                                                                                          |             |
|                                           |                                                  |     | SENDONE^HLOAPI1  | Sends a message to a single recipient.                                                                   | 5.1.8.1     |
|                                           |                                                  |     | SENDMANY^HLOAPI1 | Sends a message to a list of recipients.                                                                 | 5.1.8.2     |
|                                           |                                                  |     | SENDSUB^HLOAPI1  | Sends a message to a list of recipients based on the HLO Subscription Registry.                          | 5.1.8.3     |
|                                           |                                                  |     | EN^HLOCNRT       | Sends a message based on an Event/Subscriber Protocol setup.                                             | 5.1.8.4     |
| Parsing Messages                      |                                                  |     |                  |                                                                                                          |             |
|                                           |                                                  |     | STARTMSG^HLOPRS  | Retrieves the message.                                                                                   | 5.2.1       |
|                                           |                                                  |     | NEXTMSG^HLOPRS   | Advance to the next message within a batch                                                               | 5.2.2       |
|                                           |                                                  |     | NEXTSEG^HLOPRS   | Advance to and parse the next segment                                                                    | 5.2.3       |
|                                           |                                                  |     | HLNEXT^HLOMSG    | Advances to the next segment without parsing it.                                                         | 5.2.4       |
|                                           |                                                  |     | MSGID^HLOPRS     | Returns the message id from the message header.                                                          | 5.2.5       |
|                                           | Parsing Data Types                           |     |                  |                                                                                                          |             |
|                                           |                                                  |     | GET^HLOPRS       | Gets a value of unspecified data type.                                                                   | 5.2.6.1     |
|                                           |                                                  |     | GETAD^HLOPRS2    | Gets an AD data type (Address).                                                                          | 5.2.6.2     |
|                                           |                                                  |     | GETCE^HLOPRS2    | Gets a CE data type (Coded Element).                                                                     | 5.2.6.3     |
|                                           |                                                  |     | GETCNE HLOPRS2   | Gets a CNE data type (Coded Element With No Exceptions).                                                 | 5.2.6.4     |
|                                           |                                                  |     | GETCWE^HLOPRS2   | Gets an CWE data type (Coded Element With Exceptions).                                                   | 5.2.6.5     |
|                                           |                                                  |     | GETDT^HLOPRS2    | Gets a date.                                                                                             | 5.2.6.6     |
|                                           |                                                  |     | GETHD^HLOPRS2    | Gets an HD data type (Hierarchic Designator)                                                             | 5.2.6.7     |
|                                           |                                                  |     | GETTS^HLOPRS2    | Gets a timestamp.                                                                                        | 5.2.6.8     |
|                                           |                                                  |     | GETXPN^HLOPRS2   | Gets an XPN data type (Extended Person Name)                                                             | 5.2.6.9     |
| Returning Application Acknowledgments |                                                  |     |                  |                                                                                                          |             |
|                                           |                                                  |     | ACK^HLOAPI2      | Begins an application acknowledgment for an individual message.                                          | 5.3.1       |
|                                           |                                                  |     | BATCHACK^HLOAPI3 | Begins an application acknowledgment for a batch of messages.                                            | 5.3.2       |
|                                           |                                                  |     | ADDACK^HLOAPI3   | Adds an acknowledgment message to a batch of acknowledgment messages.                                    | 5.3.3       |
|                                           |                                                  |     | SENDACK^HLOAPI2  | Sends the acknowledgment message.                                                                        | 5.3.4       |
| Subscription Registry                 |                                                  |     |                  |                                                                                                          |             |
|                                           |                                                  |     | CREATE^HLOASUB   | Creates a new entry in the HLO SUBSCRIPTION REGISTRY file (#779.4).                                      | 5.4.1       |
|                                           |                                                  |     | ADD^HLOASUB      | Adds a new subscriber.                                                                                   | 5.4.2       |
|                                           |                                                  |     | END^HLOASUB      | Terminates a subscriber.                                                                                 | 5.4.3       |
|                                           |                                                  |     | ONLIST^HLOASUB   | Validates a subscriber.                                                                                  | 5.4.4       |
|                                           |                                                  |     | NEXT^HLOASUB     | Loops through a subscriber list.                                                                         | 5.4.5       |
|                                           |                                                  |     | INDEX^HLOASUB1   | Creates a lookup value for an entry.                                                                     | 5.4.6       |
|                                           |                                                  |     | FIND^HLOASUB1    | Looks up an entry.                                                                                       | 5.4.7       |
| Miscellaneous APIs                    |                                                  |     |                  |                                                                                                          |             |
|                                           |                                                  |     | RESEND^HLOAPI3   | Queues a message for retransmission.                                                                     | 5.5.1       |
|                                           |                                                  |     | REPROC^HLOAPI3   | Queues a message for reprocessing.                                                                       | 5.5.2       |
|                                           |                                                  |     | PROCNOW^HLOAPI3  | Reprocesses a message immediately.                                                                       | 5.5.3       |
|                                           |                                                  |     | SETPURGE^HLOAPI3 | Resets the scheduled purge time for a message.                                                           | 5.5.4       |
|                                           |                                                  |     | QUECNT^HLOQUE    | Returns a count of messages pending on each queue of all types.                                          | 5.5.5       |
|                                           |                                                  |     | OUT^HLOQUE       | Returns a count of messages pending on each outgoing queue.                                              | 5.5.6       |
|                                           |                                                  |     | IN^HLOQUE        | Returns a count of messages pending on each incoming queue.                                              | 5.5.7       |
|                                           |                                                  |     | SEQ^HLOQUE       | Returns a count of messages pending on each sequence queue.                                              | 5.5.8       |

## Sending Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Start Building a New Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$NEWMSG^HLOAPI(.PARMS,.MSG,.ERROR)

<u>Description:</u> Starts the process of building an individual messag.

<u>Input:</u>

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 31%" />
<col style="width: 20%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>PARMS</p>
<p>These subscripts are used:</p></th>
<th>Required</th>
<th>Used to pass in various parameters.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="9"></td>
<td>“COUNTRY”</td>
<td>Optional</td>
<td>A three-character country code.</td>
</tr>
<tr class="even">
<td>“CONTINUATION POINTER”</td>
<td>Optional</td>
<td>Indicates a fragmented message.</td>
</tr>
<tr class="odd">
<td>“EVENT”</td>
<td>Required</td>
<td>A three-character event type.</td>
</tr>
<tr class="even">
<td>“FIELD SEPARATOR”</td>
<td>Optional</td>
<td>Field separator that defaults to "|".</td>
</tr>
<tr class="odd">
<td>“ENCODING CHARACTERS”</td>
<td>Optional</td>
<td>Four HL7 encoding characters that defaults to "^~\&amp;".</td>
</tr>
<tr class="even">
<td>“MESSAGE STRUCTURE”</td>
<td>Optional</td>
<td>MSH-9, component 3 - a code from the standard HL7 table.</td>
</tr>
<tr class="odd">
<td>“MESSAGE TYPE”</td>
<td>Required</td>
<td>A three-character message type (required).</td>
</tr>
<tr class="even">
<td>“PROCESSING MODE”</td>
<td>Optional</td>
<td>MSH-11, component 2 – A one character code.</td>
</tr>
<tr class="odd">
<td>“VERSION”</td>
<td>Optional</td>
<td>The HL7 Version ID, for example, "2.4", defaults to 2.4.</td>
</tr>
</tbody>
</table>

Output: Function call - Returns 1 on success, 0 on failure.

| MSG   | Required | Pass-by-Reference | Used by the HLO as a workspace to build the message. |
|-------|----------|-------------------|------------------------------------------------------|
| ERROR | Optional | Pass-by-Reference | Returns an error message on failure.                 |

### Start Building a New Batch of Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$NEWBATCH^HLOAPI(.PARMS,.MSG,.ERROR)

<u>Description:</u> Starts the process of building a batch of messages.

<u>Input:</u>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 30%" />
<col style="width: 11%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>PARMS</p>
<p>These subscripts are used:</p></th>
<th>Optional</th>
<th>Used to pass in various parameters.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="4"></td>
<td>“COUNTRY”</td>
<td>Optional</td>
<td>A three-character country code.</td>
</tr>
<tr class="even">
<td>“FIELD SEPARATOR”</td>
<td>Optional</td>
<td>Field separator that defaults to "|".</td>
</tr>
<tr class="odd">
<td>“ENCODING CHARACTERS”</td>
<td>Optional</td>
<td>Four HL7 encoding characters that defaults to "^~\&amp;".</td>
</tr>
<tr class="even">
<td>“VERSION”</td>
<td>Optional</td>
<td>HL7 Version ID, for example, "2.4" that defaults to 2.4.</td>
</tr>
</tbody>
</table>

<u>  
</u>

<u>Output:</u> Function call - returns 1 on success, 0 on failure.

| MSG   | Required | Pass-by-Reference | Used by HLO as a workspace for building the message. |
|-------|----------|-------------------|------------------------------------------------------|
| ERROR | Optional | Pass-by-Reference | Returns an error message on failure.                 |

### Add a New Message to a Batch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$ADDMSG^HLOAPI(.MSG,.PARMS,.ERROR)

<u>Description:</u> Add a message to a batch that is in the process of being built.

<u>Input:</u>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 23%" />
<col style="width: 19%" />
<col style="width: 15%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">MSG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>Used by HLO as a workspace for building the message.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p>PARMS</p>
<p>These subscripts are used:</p></td>
<td>Required</td>
<td>Pass-by-Reference</td>
<td>Used to pass in various parameters.</td>
</tr>
<tr class="even">
<td rowspan="2"></td>
<td>“EVENT”</td>
<td>Required</td>
<td colspan="2">A three-character event type for the message being added.</td>
</tr>
<tr class="odd">
<td>“MESSAGE TYPE”</td>
<td>Required</td>
<td colspan="2">A three-character message type for the message being added.</td>
</tr>
</tbody>
</table>

<u>Output:</u> Function Call - Returns 1 on success, 0 on failure.

| MSG   | Required |                   | Pass-by-Reference | Used by HLO as a workspace for building the message. |
|-------|----------|-------------------|-------------------|------------------------------------------------------|
| ERROR | Optional | Pass-by-Reference |                   | Returns an error message on failure.                 |

### Add a Segment to a Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$ADDSEG^HLOAPI(.MSG,.SEG,.ERROR,TOARY)

<u>Description:</u> Used to add a segment to a message that is being built.

<u>Input:</u>

| MSG | Required | Pass-by-Reference | Used by HLO as a workspace for building the message.                                                                                    |
|-----|----------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| SEG | Required | Pass-by-Reference | Contains the segment’s data. It must be built calling the APIs in [section 5.1.7](#_Setting_Data_Types) prior to calling ADDSEG^HLOAPI. |

<u>Note#1:</u> The message control segments, including the MSH and BHS segments, are added automatically.

<u>Note#2:</u> Prior to calling ADDSET^HLOAPI, at a minimum the three- character segment type must have been set into SEG.

<u>Note#3:</u> SEG is killed upon successfully adding the segment.

<u>Output:</u> Function call, returns 1 on success, 0 on failure.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th>MSG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>Used by HLO as a workspace for building the message.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ERROR</td>
<td>Optional</td>
<td>Pass-by-Reference</td>
<td>Returns an error message on failure.</td>
</tr>
<tr class="even">
<td>TOARY</td>
<td>Optional</td>
<td>Pass-by-Reference</td>
<td><p>Returns the built segment as a set of lines in the format:</p>
<p>TOARY(1)</p>
<p>TOARY(2)</p>
<p>TOARY(3), etc.</p>
<p>If the segment fits on a single node then the entire segment is returned in TOARY(1).</p></td>
</tr>
</tbody>
</table>

### Move Traditional-Style Message Array into an HLO Message 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> MOVEMSG^HLOAPI(.MSG,.ARY)

<u>Description:</u> If a message is built as an array of segments as done in HL7 1.6 , this API can be used to

> move the message array into the MSG workspace. This API allows message builders that

> were created prior to HLO to be used within HLO.

<u>Input:</u>

| MSG | Required | Pass-by-Reference | Used by HLO as a workspace for building the message.               |
|-----|----------|-------------------|--------------------------------------------------------------------|
| ARY | Required | Pass-by-Value     | The name of the local or global array where the message was built. |

<u>  
</u>

<u>Output:</u>

| MSG | Required | Pass-by-Reference | Used by HLO as a workspace for building the message. MSG() is updated with the contents of @ARY@(). |
|-----|----------|-------------------|-----------------------------------------------------------------------------------------------------|

> **NOTE:** When using this API, it is the application’s responsibility to insure that message delimiters that may occur within the data have been replaced with the corresponding escape sequence.

Example: If a message (excluding the header) was built as an array of segments stored in ARRAY(1), ARRAY(2), etc., then call MOVEMSG^HLOAPI:

> S ARY=”ARRAY”

> D MOVEMSG^HLOAPI(.MSG,ARY)

### Move Traditional-Style Segment Array into HLO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$MOVESEG^HLOAPI(.MSG,.SEG,.ERROR)

<u>Description:</u> Used to add a segment built in the old-style of HL7 1.6 into an HLO message that is

> being built. Its main use is to allow segment builders that were designed for use with

> HL7 1.6 messages to be used with HLO.

<u>Input:</u>

| MSG | Required | Pass-by-Reference | Used by HLO as a workspace for building the message.                                                                                                                          |
|-----|----------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SEG | Required | Pass-by-Reference | Contains the segment. If the segment fits on a single node then SEG is the entire segment. If it does not fit on a single node then the annex nodes are (SEG(1), SEG(2), etc. |

<u>Output:</u> Function call, returns 1 on success, 0 on failure.

| MSG   | Required | Pass-by-Reference | Used by HLO as a workspace for building the message. After calling \$\$MOVESEG^HLOAPI the segment stored in SEG is appended to the message being built in MSG. |
|-------|----------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERROR | Optional | Pass-by-Reference | Returns an error message on failure.                                                                                                                           |

> **NOTE:** When using this API, it is the application’s responsibility to insure that message delimiters that may occur within the data have been replaced with the corresponding escape sequence.

<span id="_Setting_Data_Types" class="anchor"></span>

### Setting Data Types into a Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 standard includes numerous data types, such as for dates, addresses, and coded values. HLO provides specialized APIs for setting some of the most common data types into a segment, but not all of them. If

HLO lacks a specialized API for the data type at hand, the application should use SET^HLOAPI to set the data directly into the segment. If the data type has multiple parts, then call SET^HLOAPI multiple times to set each part into the segment.

HLO will automatically replace message delimiters found within the data with the corresponding escape sequence.

Implementation Note: Calling these APIs sets the data into the SEG array, which a workspace used by HLO for building the segment. The format of this internal workspace is:

SEG(\<field sequence \#\>,\<occurrence \# of repetition\>,\<component \#\>,\<sub-component \#\>)=\<sub-component value\>

When \$\$ADDSEG^HLOAPI is called HLO will concatenate all the values together and insert the message delimiters to create the completed segment. The segment is then appended to the message array that is being built.

Both the segment array and the message array are internal to HLO and should not be written to directly by the application.

#### Set Value (Unspecified Data Type)

<u>Routine:</u> SET^HLOAPI(.SEG,VALUE,FIELD,COMP,SUBCOMP,REP)

<u>Description:</u> Sets a single atomic value of unspecified data type into a segment at a specified location. It is used where HLO lacks a specific API for the data type at hand.

<u>Input:</u>

| SEG     | Required | Pass-by-Reference | The segment being built.                                                                                                                   |
|---------|----------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| VALUE   | Required | Pass-by-Value     | The individual value to be set into the segment.                                                                                           |
| FIELD   | Optional | Pass-by-Value     | The sequence number of the field (optional, defaults to 0). Note: FIELD=0 is used to denote the segment type.                          |
| COMP    | Optional | Pass-by-Value     | The number of the component (optional, defaults to 1).                                                                                     |
| SUBCOMP | Optional | Pass-by-Value     | The number of the subcomponent that defaults to 1.                                                                                         |
| REP     | Optional | Pass-by-Value     | The occurrence number , which defaults to 1. For a non-repeating field, the occurrence number need not be provided, because it would be 1. |

<u>Output:</u>

| SEG | Required | Pass-by-Reference | An array that HLO uses as its private workspace while building a segment. |
|-----|----------|-------------------|---------------------------------------------------------------------------|

Example: Sets the segment type to MSA.

| D SET^HLOAPI(.SEG,"MSA",0) |     |
|----------------------------|-----|

Example: Sets the value “AE” into the first field. It defaults to the first occurrence of the field, first component, and first sub-component.

D SET^HLOAPI(.SEG,"AE",1)

Example: Sets the value “ALBANY” into the first field, fourth occurrence of a repeating field, second component, third sub-component.

D SET^HLOAPI(.SEG,"ALABANY",1,2,3,4)

#### Set Address

<u>Routine:</u> SETAD^HLOAPI4(.SEG,.VALUE,FIELD,COMP,REP)

<u>Description:</u> Sets an AD data type (Address) into the segment at the specified location. It can also be used to

> set the 1st 8 components of the XAD (Extended Address) data type.

> **NOTE:** The XAD (extended address) data type replaced the AD data type as of version 2.3 of the HL7 standard. The XAD data type has additional components not included in the AD data type. If the additional components of the XAD data type are needed, SETAD^HLOAPI can be called, then the additional parts set into the segment by calling SET^HLOAPI4.

<u>Input:</u>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th>SEG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>The segment being built.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VALUE</td>
<td>Required</td>
<td>Pass-by- Reference</td>
<td><p>These subscripts may be passed:</p>
<ul>
<li><p>"STREET1" - street address</p></li>
<li><p>"STREET2" - other designation</p></li>
<li><p>"CITY"</p></li>
<li><p>"STATE" - state or province</p></li>
<li><p>"ZIP" - zip or postal code</p></li>
<li><p>"COUNTRY"</p></li>
<li><p>"TYPE" - address type</p></li>
</ul></td>
</tr>
<tr class="even">
<td>FIELD</td>
<td>Required</td>
<td>Pass-by-Value</td>
<td>The sequence number of the field.</td>
</tr>
<tr class="odd">
<td>COMP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td><p>If specified, the address is presumed to be a component value with the parts as subcomponents.</p>
<p>If not specified, the parts are presumed to be components of the field.</p></td>
</tr>
<tr class="even">
<td>REP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td>The occurrence number, which defaults to 1. For non-repeating fields, this parameter is not necessary.</td>
</tr>
</tbody>
</table>

<u>Output:</u>

| SEG | Required | Pass-by-Reference | The segment being built. |
|-----|----------|-------------------|--------------------------|

Example: Sets an address into the second field of the segment. Since a component is not

specified, its parts are at the component level.

S VALUE(“STREET1”)=”13 MOCKING BIRD LANE”

S VALUE(“CITY”)=”ALBANY”

S VALUE(“STATE”)=”NY”

S VALUE(“ZIP”)=”12506”

S VALUE(“TYPE”)=”H”

D SETAD^HLOAPI4(.SEG,.VALUE,2)

Example: Sets an address into the second field of the segment. Since a component is specified, the address is demoted to the component level, and its parts are at the subcomponent level.

S VALUE(“STREET1”)=”13 MOCKING BIRD LANE”

S VALUE(“CITY”)=”ALBANY”

S VALUE(“STATE”)=”NY”

S VALUE(“ZIP”)=”12506”

S VALUE(“TYPE”)=”H”

D SETAD^HLOAPI4(.SEG,.VALUE,2,1)

#### Set Coded Element

<u>Routine:</u> SETCE^HLOAPI4(.SEG,.VALUE,FIELD,COMP,REP)

<u>Description:</u> Sets the CE data type (Coded Element) into the segment at the specified location.

<u>Input:</u>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 18%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th>SEG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>The segment being built.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VALUE</td>
<td>Required</td>
<td>Pass-by- Reference</td>
<td><p>These subscripts may be passed:</p>
<p>"ID" - the identifier</p>
<p>"TEXT" -</p>
<p>"SYSTEM" - name of the code system</p>
<p>"ALTERNATE ID" - alternate identifier</p>
<p>"ALTERNATE TEXT"</p>
<p>"ALTERNATE SYSTEM" - name of the alternate coding system</p></td>
</tr>
<tr class="even">
<td>FIELD</td>
<td>Required</td>
<td>Pass-by-Value</td>
<td>The sequence number of the field.</td>
</tr>
<tr class="odd">
<td>COMP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td><p>If specified, the coded element is presumed to be a component value with the parts as subcomponents.</p>
<p>If not specified, the parts are presumed to be components of the field.</p></td>
</tr>
<tr class="even">
<td>REP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td>The occurrence number, defaults to 1. For non-repeating fields, this parameter is not necessary.</td>
</tr>
</tbody>
</table>

<u>Output:</u>

| SEG | Required | Pass-by-Reference | The segment being built. |
|-----|----------|-------------------|--------------------------|

#### Set Coded Element with No Exceptions

<u>Routine:</u> SETCNE^HLOAPI4(.SEG,.VALUE,FIELD,COMP,REP)

<u>Description:</u> Sets the CNE data type (Coded Element with No Exceptions) into the segment at the

> specified location.

<u>Input:</u>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 18%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th>SEG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>The segment being built.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VALUE</td>
<td>Required</td>
<td>Pass-by- Reference</td>
<td><p>These subscripts may be passed:</p>
<ul>
<li><blockquote>
<p>"ID" - the identifier</p>
</blockquote></li>
<li><blockquote>
<p>"TEXT"</p>
</blockquote></li>
<li><blockquote>
<p>"SYSTEM" - name of the code system</p>
</blockquote></li>
<li><blockquote>
<p>"ALTERNATE ID" - alternate identifier</p>
</blockquote></li>
<li><blockquote>
<p>"ALTERNATE TEXT"</p>
</blockquote></li>
<li><blockquote>
<p>"ALTERNATE SYSTEM" - name of the alternate coding system</p>
</blockquote></li>
<li><blockquote>
<p>"ORIGINAL TEXT"</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>FIELD</td>
<td>Required</td>
<td>Pass-by-Value</td>
<td>The sequence number of the field.</td>
</tr>
<tr class="odd">
<td>COMP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td><p>If specified, the coded element is presumed to be a component value with the parts as subcomponents.</p>
<p>If not specified, the parts are presumed to be components of the field.</p></td>
</tr>
<tr class="even">
<td>REP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td>The occurrence number, which defaults to 1. For non-repeating fields, this parameter is not necessary.</td>
</tr>
</tbody>
</table>

Output:

| SEG | Required | Pass-by-Reference | The segment being built. |
|-----|----------|-------------------|--------------------------|

#### Set Coded Value with Exceptions

<u>Routine:</u> SETCWE^HLOAPI4(.SEG,.VALUE,FIELD,COMP,REP)

<u>Description:</u> Sets the CWE data type (Coded Value with Exceptions) into a segment at the specified

> location.

<u>Input:</u>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>SEG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>The segment being built.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VALUE</td>
<td>Required</td>
<td>Pass-by- Reference</td>
<td><p>These subscripts may be passed:</p>
<ul>
<li><blockquote>
<p>"ID" - the identifier</p>
</blockquote></li>
<li><blockquote>
<p>"TEXT"</p>
</blockquote></li>
<li><blockquote>
<p>"SYSTEM" - name of the code system</p>
</blockquote></li>
<li><blockquote>
<p>"ALTERNATE ID" - alternate identifier</p>
</blockquote></li>
<li><blockquote>
<p>"ALTERNATE TEXT"</p>
</blockquote></li>
<li><blockquote>
<p>"ALTERNATE SYSTEM" - name of the alternate coding system</p>
</blockquote></li>
<li><blockquote>
<p>"ORIGINAL TEXT"</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>FIELD</td>
<td>Required</td>
<td>Pass-by-Value</td>
<td>The sequence number of the field.</td>
</tr>
<tr class="odd">
<td>COMP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td><p>If specified, the coded value is presumed to be a component value with the parts as subcomponents.</p>
<p>If not specified, the parts are presumed to be components of the field.</p></td>
</tr>
<tr class="even">
<td>REP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td>The occurrence number, which defaults to 1. For non-repeating fields, this parameter is not necessary.</td>
</tr>
</tbody>
</table>

Output:

| SEG | Required | Pass-by-Reference | The segment being built. |
|-----|----------|-------------------|--------------------------|

#### Set Date

<u>Routine:</u> SETDT^HLOAPI4(.SEG,.VALUE,FIELD,COMP,REP)

<u>Description:</u> Sets a DT data type (Date) in FileMan format into the segment at the specified location.

> The date is converted to HL7 format. The degree of precision may be optionally

> specified.

<u>  
</u>

<u>Input:</u>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th>SEG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>The segment being built.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VALUE</td>
<td>Required</td>
<td>Pass-by-Reference</td>
<td><p>The date to be set into the segment. Optionally, you may specify that the value should be rounded down to a particular precision by specifying this subscript:</p>
<p>"PRECISION" (If needed, VALUE must be passed by reference.)</p>
<p>Allowed values are:</p>
<ul>
<li><blockquote>
<p>"D" - day (default value)</p>
</blockquote></li>
<li><blockquote>
<p>"L" - month</p>
</blockquote></li>
<li><blockquote>
<p>"Y" - year</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>FIELD</td>
<td>Required</td>
<td>Pass-by-Value</td>
<td>The sequence # of the field.</td>
</tr>
<tr class="odd">
<td>COMP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td><p>If specified, the date is presumed to be a component value with the parts as subcomponents.</p>
<p>If not specified, the parts are presumed to be components of the field.</p></td>
</tr>
<tr class="even">
<td>REP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td>The occurrence #, defaults to 1. For non-repeating fields, this parameter is not necessary.</td>
</tr>
</tbody>
</table>

<u>Output:</u>

| SEG | Required | Pass-by-Reference | The segment being built. |
|-----|----------|-------------------|--------------------------|

#### Set Hierarchic Designator

<u>Routine</u> SETHD^HLOAPI4(.SEG,.VALUE,FIELD,COMP,REP)

<u>Description:</u> Sets the HD data type (Hierarchic Designator) into the segment at the specified location.

<u>Input:</u>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th>SEG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>The segment being built.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VALUE</td>
<td>Required</td>
<td>Pass-by- Reference</td>
<td><p>These subscripts may be passed:</p>
<ul>
<li><p>"NAMESPACE ID"</p></li>
<li><p>"UNIVERSAL ID"</p></li>
<li><p>"UNIVERSAL ID TYPE"</p></li>
</ul></td>
</tr>
<tr class="even">
<td>FIELD</td>
<td>Required</td>
<td>Pass-by-Value</td>
<td>The sequence # of the field.</td>
</tr>
<tr class="odd">
<td>COMP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td><p>If specified, the hierarchic designator is presumed to be a component value with the parts as subcomponents.</p>
<p>If not specified, the parts are presumed to be components of the field.</p></td>
</tr>
<tr class="even">
<td>REP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td>The occurrence number, which defaults to 1. For non-repeating fields, this parameter is not necessary.</td>
</tr>
</tbody>
</table>

Output:

| SEG | Required | Pass-by-Reference | The segment being built. |
|-----|----------|-------------------|--------------------------|

#### Set Timestamp

<u>Routine:</u> SETTS^HLOAPI4(.SEG,.VALUE,FIELD,COMP,REP)

<u>Description:</u> Sets the TS data type (Timestamp) in FM format into a segment at the specified location.

> The time stamp is converted to HL7 format. The degree of precision may be optionally specified. The inserted value will include the time zone if the input included the time

<u>Input:</u>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 20%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th>SEG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>The segment being built.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VALUE</td>
<td>Required</td>
<td><p>If the precision is not needed, then Pass-by-Value may be used.</p>
<p>If the precision is specified, then Pass-by-Reference.</p></td>
<td><p>The date/time in FileMan format. You can <em>optionally</em> specify that the value is to be rounded down to a particular precision by specifying this subscript:</p>
<p>"PRECISION" - Allowed values are:</p>
<ul>
<li><p>"S" - second</p></li>
<li><p>"M" - minute</p></li>
<li><p>"H" - hour</p></li>
<li><p>"D" - day</p></li>
<li><p>"L" - month</p></li>
<li><p>"Y" - year</p></li>
<li><p>"" - precision not specified</p></li>
</ul></td>
</tr>
<tr class="even">
<td>FIELD</td>
<td>Required</td>
<td>Pass-by-Value</td>
<td>The sequence number of the field.</td>
</tr>
<tr class="odd">
<td>COMP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td><p>If specified, the timestamp is presumed to be a component value with the parts as subcomponents.</p>
<p>If not specified, the parts are presumed to be components of the field.</p></td>
</tr>
<tr class="even">
<td>REP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td>The occurrence number, which defaults to 1. For non-repeating fields, this parameter is not necessary.</td>
</tr>
</tbody>
</table>

Output:

| SEG | Required | Pass-by-Reference | The segment being built. |
|-----|----------|-------------------|--------------------------|

#### Set Extended Person Name

<u>Routine:</u> SETXPN^HLOAPI4(.SEG,.VALUE,FIELD,COMP,REP)

<u>Description:</u> Sets the XPN data type (Extended Person Name) into the segment at the specified

> location.

> **NOTE:** The XPN data type has additional components not included in this API. If needed, the additional components can be set into the segment by calling SET^HLOAPI after calling SETXPN^HLOAPI4.

This API can also be used to set the Person Name (PN) data type into a segment. The PN data type was made obsolete in version 2.5 of the HL7 standard.

<u>Input:</u>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th>SEG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>The segment that is being built.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VALUE</td>
<td>Required</td>
<td></td>
<td><p>These subscripts may be passed:</p>
<ul>
<li><p>"FAMILY"</p></li>
<li><p>"GIVEN" first name</p></li>
<li><p>"SECOND" second and further names or initials</p></li>
<li><p>"SUFFIX" (e.g., JR)</p></li>
<li><p>"PREFIX" (e.g., DR)</p></li>
<li><p>"DEGREE" (e.g., MD)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>FIELD</td>
<td>Required</td>
<td>Pass-by-Value</td>
<td>The sequence number of the field.</td>
</tr>
<tr class="odd">
<td>COMP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td><p>If specified, the extended person name is presumed to be a component value with the parts as subcomponents.</p>
<p>If not specified, the parts are presumed to be components of the field.</p></td>
</tr>
<tr class="even">
<td>REP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td>The occurrence number, defaults to 1. For non-repeating fields, this parameter is not necessary.</td>
</tr>
</tbody>
</table>

<u>Output:</u>

| SEG | Required | Pass-by-Reference | The segment being built. |
|-----|----------|-------------------|--------------------------|

### Completing and Sending Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the building of the message has been completed with all its segments, it must be addressed and sent. HLO supports several APIs for doing that. They are:

SENDONE^HLOAPI1 Sends a single copy of the message to a single destination.

SENDMANY^HLOAPI1 Sends one or many copies of the message to a list of destinations. The

list of destinations is provided as an input parameter to the API. This

API is suited to static lists of recipients because the list is created within

the routine and cannot be modified without a patch.

SENDSUB^HLOAPI1 Sends one or many copies of the message to a list of subscribers. The

list of subscribers is maintained in an entry in the HLO Subscription

> Registry. This API is suited to applications that need to provide for a dynamic list of subscribers. Subscribers can be added, modified, or deleted via the table-based HLO Subscription Registry.

EN^HLOCNRT This API is supports existing applications based on HL7 1.6 that need to

convert to HLO. It is not recommended for new applications. It

> supports many of the features of GENERATE^HLMA, though not all of

> them. It requires that the message be passed in as an array of segments,

> and uses the traditional-style Event/Subscriber protocol setup.

#### Send a Single Message

<u>Routine:</u> \$\$SENDONE^HLOAPI1(.MSG,.PARMS,.WHOTO,.ERROR)

<u>Description:</u> Used to send a message to a single recipient. The recipient is identified in the message

> header by the Receiving Facility and the Receiving Application. The message

> may optionally be routed through middleware.

<u>Input:</u>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 19%" />
<col style="width: 7%" />
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 0%" />
<col style="width: 4%" />
<col style="width: 13%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">MSG</th>
<th colspan="3">Required</th>
<th colspan="2">Pass-by-Reference</th>
<th>The workspace where the message was built.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><p>PARMS</p>
<p>These subscripts are allowed:</p></td>
<td colspan="3">Required</td>
<td colspan="2">Pass-by-Reference</td>
<td>Various parameters.</td>
</tr>
<tr class="even">
<td rowspan="9"></td>
<td colspan="2">"APP ACK RESPONSE"</td>
<td colspan="2">Optional</td>
<td colspan="4">&lt;tag^routine&gt; to call in response to app ack. (see Callbacks section 2.7)</td>
</tr>
<tr class="odd">
<td colspan="2">"APP ACK TYPE"</td>
<td colspan="2">Optional</td>
<td colspan="4">&lt;AL,NE&gt; defaults to NE.</td>
</tr>
<tr class="even">
<td colspan="2">"ACCEPT ACK RESPONSE"</td>
<td colspan="2">Optional</td>
<td colspan="4">&lt;tag^routine&gt; to call in response to a commit ack. (See Callbacks section 2.7.)</td>
</tr>
<tr class="odd">
<td colspan="2">"ACCEPT ACK TYPE"</td>
<td colspan="2">Optional</td>
<td colspan="4">&lt;AL,NE&gt; defaults to AL.</td>
</tr>
<tr class="even">
<td colspan="2">"FAILURE RESPONSE"</td>
<td colspan="2">Optional</td>
<td colspan="4">&lt;tag^routine&gt; The sending application routine to execute when the transmission of the message fails, i.e., the message cannot be sent or no commit ack is received. (See Callbacks section 2.7.)</td>
</tr>
<tr class="odd">
<td colspan="2">"QUEUE"</td>
<td colspan="2">Optional</td>
<td colspan="4">An application can name its own private queue by entering a string under 20 characters. The queue name should be namespaced.</td>
</tr>
<tr class="even">
<td colspan="2">"SECURITY”</td>
<td colspan="2">Optional</td>
<td colspan="4">Security information to include in the header segment, MSH-8.</td>
</tr>
<tr class="odd">
<td colspan="2">"SENDING APPLICATION"</td>
<td colspan="2">Required</td>
<td colspan="4">The name of the sending application (60 characters max-length).</td>
</tr>
<tr class="even">
<td colspan="2">“SEQUENCE QUEUE”</td>
<td colspan="2">Optional</td>
<td colspan="4">A sequence queue to place the message on, name up to 30 characters and must be namespaced. See section 2.8 Sequence Queues.</td>
</tr>
<tr class="odd">
<td colspan="2"><p>WHOTO</p>
<p>These subscripts are allowed:</p></td>
<td colspan="2">Required</td>
<td colspan="3">Pass-by-Reference</td>
<td colspan="2">Used to specify the receiving application, receiving facility, and HL Logical Link over which to transmit.</td>
</tr>
<tr class="even">
<td rowspan="9"></td>
<td colspan="2">"RECEIVING APPLICATION"</td>
<td colspan="2">Required</td>
<td colspan="4">The name of the application that should receive the message (60 characters max-length).</td>
</tr>
<tr class="odd">
<td colspan="8">One of the following four parameters is required to identify the Receiving Facility.</td>
</tr>
<tr class="even">
<td colspan="2">"FACILITY LINK IEN"</td>
<td colspan="2">Optional</td>
<td colspan="4">IEN of the logical link.</td>
</tr>
<tr class="odd">
<td colspan="2">"FACILITY LINK NAME"</td>
<td colspan="2">Optional</td>
<td colspan="4">Name of the logical link.</td>
</tr>
<tr class="even">
<td colspan="2">"INSTITUTION IEN"</td>
<td colspan="2">Optional</td>
<td colspan="4">Pointer to the INSTITUTION File (#4).</td>
</tr>
<tr class="odd">
<td colspan="2">"STATION NUMBER"</td>
<td colspan="2">Optional</td>
<td colspan="4">Station number with suffix.</td>
</tr>
<tr class="even">
<td colspan="8">One of the following two parameters MAY be provided, optionally, to identify the interface engine or other middleware to route the message through.</td>
</tr>
<tr class="odd">
<td colspan="2">MIDDLEWARE LINK IEN"</td>
<td colspan="2">Optional</td>
<td colspan="4">Pointer to a logical link for the interface engine or other middleware.</td>
</tr>
<tr class="even">
<td colspan="2">"MIDDLEWARE LINK NAME"</td>
<td colspan="2">Optional</td>
<td colspan="4">Name of the logical link for the interface engine or other middleware.</td>
</tr>
</tbody>
</table>

<u>Output:</u> Function call - returns the IEN of the message in HLO MESSAGES file (#778) on success, 0 on failure.

| MSG   | Required | Pass-by-Reference | The workspace where the message was built. |
|-------|----------|-------------------|--------------------------------------------|
| ERROR | Optional | Pass-by-Reference | On failure, will contain an error message. |
| PARMS |          | Pass-by-Reference | Killed when the function returns.          |
| WHOTO |          | Pass-by-Reference | Killed when the function returns.          |

#### Send Messages to a List of Destinations

<u>Routine:</u> \$\$SENDMANY^HLOAPI1(.MSG,.PARMS,.WHOTO)

<u>Description:</u> Used to send a message to a list of recipients. The list is passed in as an array.

<u>Input:</u> Similar to \$\$SENDONE^HLOAPI1. In \$\$SENDMANY^HLOAPI1, the WHOTO()

array is a list of recipients.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>MSG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>The workspace where the message was built.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PARMS</td>
<td>Required</td>
<td>Pass-by-Reference</td>
<td>See PARMS definition in the $$SENDONE^HLOAPI1 API.</td>
</tr>
<tr class="even">
<td>WHOTO</td>
<td>Required</td>
<td>Pass-by-Reference</td>
<td><p>Specifies a list of recipients. Each recipient should be listed individually in array WHOTO(i), where i=a recipient. For each recipient, the same subscripts may be defined as in the $$SENDONE API. For example:</p>
<p>WHOTO(1,"FACILITY LINK NAME")="VAALB"</p>
<p>WHOTO(1,"RECEIVING APPLICATION")="MPI"</p>
<p>WHOTO(2,"STATION NUMBER")=500</p>
<p>WHOTO(2,"RECEIVING APPLICATION")="MPI"</p></td>
</tr>
</tbody>
</table>

<u>  
</u>

<u>Output:</u> Function call- returns 1 if a message is queued to be sent to each intended recipient; 0 otherwise.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 14%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>MSG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>The workspace where the message was built.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PARMS</td>
<td>Required</td>
<td>Pass-by-Reference</td>
<td>Killed when the function returns.</td>
</tr>
<tr class="even">
<td>WHOTO</td>
<td>Required</td>
<td>Pass-by-Reference</td>
<td><p>Returns the status of each message to be sent in the format:</p>
<p>(&lt;i&gt;,"QUEUED") - 1 if queued to be sent, 0 otherwise.</p>
<p>(&lt;i&gt;,"IEN") – IEN from HLO MESSAGES file (#778) if queued to be sent, null otherwise.</p>
<p>(&lt;i&gt;,"ERROR") - Error message if an error was encountered (status=0), and null otherwise.</p></td>
</tr>
</tbody>
</table>

#### Send Messages via the HLO Subscription Registry to a List of Subscribers

<u>Routine:</u> \$\$SENDSUB^HLOAPI1(.MSG,.PARMS,.MESSAGES)

<u>Description:</u> Used to send a message to a list of recipients. It differs from \$\$SENDMANY^HLOAPI1

> in that the list, instead of being passed in as an array, is contained in the HLO

> SUBSCRIPTION REGISTRY file (#779.4). In other words, the list of recipients is maintained by the application in a table rather than being created dynamically.

<u>Input:</u>

| MSG                       | Required | Pass-by-Reference | The workspace where the message was built.                                                                             |
|---------------------------|----------|-------------------|------------------------------------------------------------------------------------------------------------------------|
| PARMS                     | Required | Pass-by-Reference | See PARMS definition in the \$\$SENDONE^HLOAPI1 API. It has one additional subscript, PARMS(“SUBSCRIPTION IEN”).       |
| PARMS("SUBSCRIPTION IEN") | Required | Pass-by-Reference | The IEN of an entry in the HLO. SUBSCRIPTION REGISTRY File (#779.4), defining the intended recipients of this message. |

<u>Output:</u> Function call - returns 1 if a message is queued to be sent to each intended recipient, 0 otherwise.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th>MSG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>The workspace where the message was built.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PARMS</td>
<td></td>
<td></td>
<td>Killed when the function returns.</td>
</tr>
<tr class="even">
<td>MESSAGES</td>
<td>Required</td>
<td>Pass-by-Reference</td>
<td><p>Returns the status of each message to be sent in this format, where the sub-IEN is the IEN of the recipient in the RECIPIENTS sub-file of the HLO SUBSCRIPTION REGISTRY File (#779.4).</p>
<p>(&lt;subien&gt;,"QUEUED") - 1 if queued to be sent, 0 otherwise.</p>
<p>(&lt;subien&gt;,"IEN") – IEN from HLO MESSAGES file (#778) if queued to be sent, or null otherwise.</p>
<p>(&lt;subien&gt;,"ERROR") - Error message if an error was encountered (status=0), and null otherwise.</p></td>
</tr>
</tbody>
</table>

#### Send Messages via HL7 1.6 Protocol Setup

<u>Routine:</u> \$\$EN^HLOCNRT(HLOPRTCL,.ARYTYP,.HLP,.HLL, .RESULT)

<u>Description:</u> Used to send a message that was built in the traditional-style of HL 1.6 and send it via an

> Event/Subscriber protocol setup as used in HL7 1.6. It is similar to

> GENERATE^HLMA, though it does not implement all of its features.

Protocol Fields Not Supported:

- Entry Action
- Exit Action
- Processing ID
- Response Processing Routine
- Sending Facility Required
- Receiving Facility Required
- Processing Routine
- Routing Logic

<u>Input:</u>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 2%" />
<col style="width: 15%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">HLOPRTCL</th>
<th colspan="3">Required</th>
<th>Pass-by-Value</th>
<th>Protocol IEN or Protocol Name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2">ARYTYP</td>
<td colspan="3">Required</td>
<td>Pass-by-Value</td>
<td>An array type: “GM” is used for a global array and “LM” is used for a local array.</td>
</tr>
<tr class="even">
<td colspan="2"><p>HLP</p>
<p>These subscripts are allowed:</p></td>
<td colspan="3">Optional</td>
<td>Pass-by-Reference</td>
<td>Used to pass in various parameters.</td>
</tr>
<tr class="odd">
<td rowspan="5"></td>
<td>“SECURITY”</td>
<td>Optional</td>
<td colspan="4">Security information to include in the header segment, SEQ-8</td>
</tr>
<tr class="even">
<td>“CONTPTR”</td>
<td>Optional</td>
<td colspan="4">Value to place in MSH-14, the Continuation Pointer field used to link long messages that have been broken into fragments. Its use is application-specific and not defined by the standard.</td>
</tr>
<tr class="odd">
<td>“QUEUE”</td>
<td>Optional</td>
<td colspan="4">An application can name its own private queue by entering a string under 20 characters. The queue name should be namespaced.</td>
</tr>
<tr class="even">
<td>“SEQUENCE QUEUE”</td>
<td>Optional</td>
<td colspan="4">A sequence queue to place the message on, name up to 30 characters and must be namespaced. See section 2.8, Sequence Queues.</td>
</tr>
<tr class="odd">
<td>“EXCLUDE SUBSCRIBER”</td>
<td>Optional</td>
<td colspan="4">Used to specify subscriber protocols that should be skipped when sending the HL7 message.</td>
</tr>
<tr class="even">
<td colspan="2">HLL</td>
<td>Optional</td>
<td>Pass-by-Reference</td>
<td colspan="3"><p>The HLL array is used by some applications to dynamically address messages by passing in a list of recipients. The format of the list is:</p>
<p>HLL(“LINKS”,&lt;i=1,2,3,etc.&gt;)=&lt;destination protocol, name or IEN&gt;^&lt;destination link, name or IEN&gt;</p></td>
</tr>
</tbody>
</table>

<u>  
</u>

<u>Output:</u> Function Call - returns 1 on success, 0^error code^error description on failure.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th>RESULT</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th><p><strong>Note:</strong> If more than one message was sent, the RESULT applies to the first. Status information of the additional messages located at RESULT(1), Result(2), etc.</p>
<p><strong>On success:</strong> &lt;subscriber protocol IEN&gt;^&lt;link IEN&gt;^&lt;message id&gt;^0</p>
<p><strong>On failure:</strong> &lt;subscriber protocol IEN&gt;^&lt;link IEN&gt;^&lt;message id&gt;^&lt;error code&gt;^&lt;optional error message&gt;</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>RESULT(“IEN”)</td>
<td>Optional</td>
<td>Pass-by-reference</td>
<td>The IEN, file 778, of the first message sent.</td>
</tr>
<tr class="even">
<td>RESULT(&lt;1,2,…&gt;)</td>
<td>Optional</td>
<td>Pass-by-Reference</td>
<td>Status information for additional messages sent. The returned status information is in the same format as for RESULT above.</td>
</tr>
<tr class="odd">
<td>RESULT(&lt;1,2,…&gt;,”IEN”)</td>
<td>Optional</td>
<td>Pass-by-Reference</td>
<td>The IENs, file 778, of additional messages sent.</td>
</tr>
</tbody>
</table>

## Parsing Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Start Parsing a Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$STARTMSG^HLOPRS(.MSG,.HLMSGIEN,.HDR)

<u>Description:</u> This API is always called as the first step in parsing a message. It retrieves the message

> header and parses it. It also returns administrative information about the message.

> The application will most often parse a message while it is executing in the context of the

> background HLO process that passes newly-received messages that are pending on the

> incoming queue to the application. At that point, the variable HLMSGIEN is guaranteed to be defined and its value set to the IEN of the newly received message.

<u>Input:</u>

| HLMSGIEN | Required | Pass-by-Value | The IEN of the message in HLO MESSAGES file (#778). |
|----------|----------|---------------|-----------------------------------------------------|

<u>Output:</u> Function returns 1 on success, 0 on failure. Failure would indicate that the message was

> not found.

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 1%" />
<col style="width: 8%" />
<col style="width: 2%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 3%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">MSG</th>
<th colspan="2">Required</th>
<th colspan="3">Pass-by-Reference</th>
<th colspan="2">This array is used by HLO as a workspace to retrieve the message. The application MUST NOT write to this array.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="10"><strong>The following subscripts are returned and may be referenced by the application:</strong></td>
</tr>
<tr class="even">
<td colspan="3">“ACK BY"</td>
<td colspan="7">The message ID of the message that acknowledges this one.</td>
</tr>
<tr class="odd">
<td colspan="3">* "ACK BY IEN"</td>
<td colspan="7"></td>
</tr>
<tr class="even">
<td colspan="3">"ACK TO"</td>
<td colspan="7">The message ID of the message that this message acknowledges.</td>
</tr>
<tr class="odd">
<td colspan="3">* "ACK TO IEN"</td>
<td colspan="7">The message IEN (file #778) of message that this one acknowledges. If the message is an individual message within a batch, the value is &lt;IEN&gt;^&lt;sub-IEN&gt;, where sub-IEN is the IEN of the message within the sub-file #778.03.</td>
</tr>
<tr class="even">
<td colspan="3">"BATCH"</td>
<td colspan="7">A flag that is set to 1 if the message is a batch message and 0 if it is not a batch message.</td>
</tr>
<tr class="odd">
<td colspan="3">"BODY"</td>
<td colspan="7">The IEN of the entry in file #777 that contains the body of the message.</td>
</tr>
<tr class="even">
<td colspan="3">"DIRECTION"</td>
<td colspan="7">Indicates the direction of the message transmission, "IN" if incoming, "OUT" if outgoing.</td>
</tr>
<tr class="odd">
<td colspan="3">"DT/TM"</td>
<td colspan="7">The date/time that the message was sent or received.</td>
</tr>
<tr class="even">
<td colspan="3"><p>"DT/TM</p>
<p>CREATED"</p></td>
<td colspan="7">The date/time the message record was created.</td>
</tr>
<tr class="odd">
<td colspan="3">* "EVENT"</td>
<td colspan="7">The HL7 event, only defined if not a batch message.</td>
</tr>
<tr class="even">
<td colspan="3">"HDR"</td>
<td colspan="7">The message header segment, NOT parsed. MSG(“HDR”,1) contains fields sequence 1-6, and MSG(“HDR”,2) contains fields sequence 7-end.</td>
</tr>
<tr class="odd">
<td colspan="3">"ID"</td>
<td colspan="7">The id from within the message header. It is the Message Control ID field for an individual message and the Batch Control ID field for a batch message</td>
</tr>
<tr class="even">
<td colspan="3">"IEN"</td>
<td colspan="7">The IEN of the message in the HLO MESSAGES file ( #778).</td>
</tr>
<tr class="odd">
<td colspan="3">*"MESSAGE TYPE"</td>
<td colspan="7">The HL7 message type, only defined if not a batch message.</td>
</tr>
<tr class="even">
<td colspan="3">"STATUS"</td>
<td colspan="7">The message’s completion status. It is NULL if the message transaction has not yet been completed, “SU” if the message was completed without an error returned, “ER” if transmission failed or an error was returned.</td>
</tr>
<tr class="odd">
<td colspan="3"></td>
<td colspan="7">These subscripts are stored at a lower level under “STATUS”:</td>
</tr>
<tr class="even">
<td></td>
<td colspan="6">"ACCEPT ACK'D"</td>
<td colspan="3">Indicates whether an accept acknowledgment, aka commit acknowledgment, was sent or received. Its value is 1 yes, 0 if no.</td>
</tr>
<tr class="odd">
<td></td>
<td colspan="6"><p>* ”ACCEPT ACK</p>
<p>DT/TM”</p></td>
<td colspan="3">If a commit acknowledgment was sent or received, this is the date/time.</td>
</tr>
<tr class="even">
<td></td>
<td colspan="6"><p>* ”ACCEPT ACK</p>
<p>ID”</p></td>
<td colspan="3">If a commit acknowledgment was sent or received, this is its message id.</td>
</tr>
<tr class="odd">
<td></td>
<td colspan="6"><p>* “ACCEPT ACK</p>
<p>MSA”</p></td>
<td colspan="3">If a commit acknowledgment was sent or received, this is the entire MSA segment that it contained.</td>
</tr>
<tr class="even">
<td></td>
<td colspan="6">"APP ACK'D"</td>
<td colspan="3">Indicates whether an application acknowledgment was sent or received. Its value is 1 yes, 0 if no.</td>
</tr>
<tr class="odd">
<td></td>
<td colspan="6">“ERROR TEXT"</td>
<td colspan="3">If the completion status is “ER”, this is any text that is associated with that status. If the status is an error because of an acknowledgment that was returned, it’s the text that was returned in the MSA segment.</td>
</tr>
<tr class="even">
<td></td>
<td colspan="6">"LINK NAME"</td>
<td colspan="3">The name of the link in the HL LOGICAL LINK file (#870) over which the message was transmitted or will be transmitted.</td>
</tr>
<tr class="odd">
<td></td>
<td colspan="6">"PURGE"</td>
<td colspan="3">If the message has been scheduled for purging, this is the date/time of the scheduled purge.</td>
</tr>
<tr class="even">
<td></td>
<td colspan="6"><p>* "SEQUENCE</p>
<p>QUEUE"</p></td>
<td colspan="3">If this is an outgoing message that was initially placed on a sequence queue, this is the name of the sequence queue.</td>
</tr>
<tr class="odd">
<td colspan="10">* Indicates that the subscript is not always defined. Some subscripts are defined only if they are valued, ergo, for a batch message the subscript “MESSAGE TYPE” is not defined.</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td colspan="8"></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="2">HDR</td>
<td colspan="2">Optional</td>
<td colspan="3">Pass-by-Reference</td>
<td>This array contains the results of parsing the message header. Escape sequences are replaced by the original characters. See section 3.3 for the subscripts returned (HLO Parses the Message Header).</td>
</tr>
</tbody>
</table>

### Advance to the Next Message within a Batch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$NEXTMSG^HLOPRS(.MSG,.MSH)

<u>Description:</u> Used to advance to the next message within a batch and return the MSH segment for that

> message.

<u>Input:</u>

| MSG | Required | Pass-by-Reference | This array is used to track the current position within the message. |
|-----|----------|-------------------|----------------------------------------------------------------------|

<u>Output:</u> Function returns 1 on success, 0 if there are no more messages.

| MSG | Required | Passed by Reference | Updated with the new position within the message.                                                          |
|-----|----------|---------------------|------------------------------------------------------------------------------------------------------------|
| MSH | Required | Pass-by-Reference   | Returns the parsed message header. See section 3.3.1 for the subscripts returned (Parsing the MSH Segment) |

### Advance to and Parse the Next Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$NEXTSEG^HLOPRS(.MSG,.SEG)

<u>Description:</u> Used to advance parsing to the next segment and parses it.

<u>Input:</u>

| MSG | Required | Pass-by-Reference | This array is used to track the current position in the message. |
|-----|----------|-------------------|------------------------------------------------------------------|

<u>Output:</u> Function Call- returns 1 on success, 0 if there are no more segments in this message. For batch messages, a return value of 0 does not preclude the possibility that there are additional individual messages within the batch.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th>MSG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>Updated with the new position within the message.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SEG</td>
<td>Required</td>
<td>Pass-by-Reference</td>
<td><p>Contains all the individual values parsed from the segment. The application should not reference this array directly. Instead, the APIs listed in section 5.2.4 below should be used.</p>
<p>Additionally, SEG(“SEGMENT TYPE”) will return the 3 character segment type that starts every segment. SEG(0) is also returned and is shorthand for SEG(“SEGMENT TYPE”) with the same return value.</p></td>
</tr>
</tbody>
</table>

### Get Next Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$HLNEXT^HLOMSG(.MSG,.SEG)

<u>Description:</u>

This API returns the next segment in the current message, but unlike

\$\$NEXTSEG^HLOPRS, it does not parse it. If the message is within a batch, it will NOT

jump to the next message when reaching the last segment in the current message.

> Its use is principally for messaging applications that were developed prior to HLO that need to convert to HLO. It steps through messages in a similar fashion to HL7 1.6’s ‘XECUTE HLNEXT’, with two differences:

1.  For batch messages, \$\$HLNEXT does not traverse to the next message in the batch as ‘X HLNEXT’ does. Instead, too step to the next message within a batch the application must call \$\$NEXTMSG^HLOPRS.
2.  \$\$HLNEXT^HLOMSG always returns the data in an array in the format SEG(1), SEG(2), etc. The number of subscripts used depends on how large the segment is. ‘XECUTE HLNEXT’ instead returns the variable SEG containing the segment, with SEG(1), SEG(2), etc. defined only if the segment doesn’t fit entirely in SEG.

<u>Input:</u>

| MSG | Required | Pass-by-Reference | Contains the message and tracks the current position within the message. |
|-----|----------|-------------------|--------------------------------------------------------------------------|

<u>Output:</u> Function returns 1 on success, 0 if there are no more segments in this message. For batch messages, a return value of 0 does not preclude the possibility that there are additional individual messages within the batch.

| MSG | Required | Pass-by-Reference | Updated with the current position within the message.                                                                                   |
|-----|----------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| SEG | Required | Pass-by-Reference | The segment is returned in this array in the format SEG(1), SEG(2), etc. If the segment fits on a single node, only SEG(1) is returned. |

> **NOTE:** After calling this API, it is the applications responsibility to correctly parse the individual fields, including:

- Converting data types
- Replacing escape sequences with the original characters
- Where the segment is returned in more than one node with fields broken in parts, correctly putting together the pieces.

### Get Message ID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$MSGID^HLOPRS(HLMSGIEN)

<u>Description:</u> Given the message IEN (file \#778) this function returns the message ID from the

message header.

<u>Input:</u>

| HLMSGIEN | Required | Pass-by-Value | The message IEN, from the HLO MESSAGES file (#778). |
|----------|----------|---------------|-----------------------------------------------------|

<u>Output:</u> The function returns the message ID from the message header.

### Parsing Data Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After calling \$\$NEXTSEG^HLOPRS, the segment has been totally parsed and all its data returned in an array. The following APIs are used to fetch the specific data that is needed from that array.

The HLO standard defines numerous data types, such as for person names, addresses, and coded values. HLO provides specialized APIs to get some of the HL7 data types, but not all of them. Where a specialized API is not available, the generic \$\$GET^HLOPRS should be used to get the needed data. It returns a single atomic value, so if the data has more than one part, then \$\$GET^HLOPRS should be called multiple time to obtain the entire data type.

The following APIs are used to obtain the specific data that is needed after the segment has been parsed by \$\$NEXTSEG^HLOPRS.

#### Get Value (Unspecified Data Type)

<u>Routine:</u> \$\$GET^HLOPRS(.SEG,FIELD,COMP,SUBCOMP,REP)

<u>Description:</u> Gets a single atomic value from a segment. It is used when HLO lacks an

> API specific to the data type at hand.

Example: \$\$GET^HLOPRS(.SEG,1) specifies to return a value of the first field. Since the other

> parameters aren’t specified it defaults to the first component, first subcomponent, first occurrence.

<u>Input:</u>

| SEG     | Required | Pass-by-Reference | The parsed segment.                                                                                                         |
|---------|----------|-------------------|-----------------------------------------------------------------------------------------------------------------------------|
| FIELD   | Optional | Pass-by-Value     | The sequence number of the field which defaults to 1. If 0 (zero) is specified, then the function returns the segment type. |
| COMP    | Optional | Pass-by-Value     | The number of the component which defaults to 1.                                                                            |
| SUBCOMP | Optional | Pass-by-Value     | The number of the subcomponent which defaults to 1.                                                                         |
| REP     | Optional | Pass-by-Value     | The occurrence number which defaults to 1. For a non-repeating field, the occurrence number will always be 1.               |

<u>Output:</u> Function returns the requested value on success, null if not valued.

#### Get Address

<u>Routine:</u> GETAD^HLOPRS2(.SEG,.VALUE,FIELD,COMP,REP)

<u>Description:</u> Gets an AD data type (Address) from the segment at the specified location. It can also be

> used to get the 1st 8 components of the XAD (Extended Address) data type.

> **NOTE:** The XAD (extended address) data type replaced the AD data type as of version 2.3 of the HL7 standard. The XAD data type has additional components not included in the AD data type. If the additional components of the XAD data type are needed, GETAD^HLOPRS can be called, then the additional parts can be obtained by calling GET^HLOPRS.

<u>Input:</u>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th>SEG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>The parsed segment.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FIELD</td>
<td>Required</td>
<td>Pass-by-Value</td>
<td>The sequence # of the field.</td>
</tr>
<tr class="even">
<td>COMP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td><p>If specified, the address is presumed to be a component value with the parts as subcomponents.</p>
<p>If not specified, the parts are presumed to be components of the field.</p></td>
</tr>
<tr class="odd">
<td>REP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td>The occurrence number, which defaults to 1. For non-repeating fields, this parameter is not necessary.</td>
</tr>
</tbody>
</table>

<u>  
</u>

<u>Output:</u>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th>VALUE</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th><p>These subscripts are returned:</p>
<ul>
<li><blockquote>
<p>"STREET1" -street address</p>
</blockquote></li>
<li><blockquote>
<p>"STREET2" - other designation</p>
</blockquote></li>
<li><blockquote>
<p>"CITY"</p>
</blockquote></li>
<li><blockquote>
<p>"STATE" - state or province</p>
</blockquote></li>
<li><blockquote>
<p>"ZIP" - zip or postal code</p>
</blockquote></li>
<li><blockquote>
<p>"COUNTRY"</p>
</blockquote></li>
<li><blockquote>
<p>"TYPE" - address type</p>
</blockquote></li>
<li><blockquote>
<p>"OTHER" - other geographic designation</p>
</blockquote></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Get Coded Element

<u>Routine:</u> GETCE^HLOPRS2(.SEG,.VALUE,FIELD,COMP,REP)

<u>Description:</u> Gets a CE data type (Coded Element) from the parsed segment at the specified location.

<u>Input:</u>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>SEG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>The parsed segment.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FIELD</td>
<td>Required</td>
<td>Pass-by-Value</td>
<td>The sequence number of the field.</td>
</tr>
<tr class="even">
<td>COMP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td><p>If specified, the coded element is presumed to be a component value with the parts as subcomponents.</p>
<p>If not specified, the parts are presumed to be components of the field.</p></td>
</tr>
<tr class="odd">
<td>REP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td>The occurrence number, which defaults to 1. For non-repeating fields, this parameter is not necessary.</td>
</tr>
</tbody>
</table>

Output:

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th>VALUE</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th><p>These subscripts are returned:</p>
<ul>
<li><p>"ID" - the identifier</p></li>
<li><p>"TEXT" -</p></li>
<li><p>"SYSTEM" - name of the code system</p></li>
<li><p>"ALTERNATE ID" - alternate identifier</p></li>
<li><p>"ALTERNATE TEXT"</p></li>
<li><p>ALTERNATE SYSTEM" - name of the alternate coding system</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Get Coded Element with No Exceptions

<u>Routine:</u> GETCNE HLOPRS2(.SEG,.VALUE,FIELD,COMP,REP)

<u>Description:</u> Gets a CNE data type (Coded Element with No Exceptions) from the parsed segment at

> the specified location.

<u>Input:</u>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>SEG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>The parsed segment.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FIELD</td>
<td>Required</td>
<td>Pass-by-Value</td>
<td>The sequence number of the field.</td>
</tr>
<tr class="even">
<td>COMP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td><p>If specified, the coded element is presumed to be a component value with the parts as subcomponents.</p>
<p>If not specified, the parts are presumed to be components of the field.</p></td>
</tr>
<tr class="odd">
<td>REP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td>The occurrence number, which defaults to 1. For non-repeating fields, this parameter is not necessary.</td>
</tr>
</tbody>
</table>

<u>Output:</u>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>VALUE</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th><p>These subscripts are returned:</p>
<ul>
<li><p>"ID" - the identifier</p></li>
<li><p>"TEXT" -</p></li>
<li><p>"SYSTEM" - name of the code system</p></li>
<li><p>"ALTERNATE ID" - alternate identifier</p></li>
<li><p>"ALTERNATE TEXT"</p></li>
<li><p>ALTERNATE SYSTEM" - name of the alternate coding system</p></li>
<li><p>"SYSTEM VERSION" - version ID of the coding system</p></li>
<li><p>"ALTERNATE SYSTEM VERSION" - version ID of the alternate coding system</p></li>
<li><p>"ORIGINAL TEXT"</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Get Coded Element with Exceptions

<u>Routine:</u> GETCWE^HLOPRS2(.SEG,.VALUE,FIELD,COMP,REP)

<u>Description:</u> Gets an CWE data type (Coded Element with Exceptions) from the parsed segment at the

> specified location.

<u>Input:</u>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>SEG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>The parsed segment..</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FIELD</td>
<td>Required</td>
<td>Pass-by-Value</td>
<td>The sequence number of the field.</td>
</tr>
<tr class="even">
<td>COMP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td><p>If specified, the coded element is presumed to be a component value with the parts as subcomponents.</p>
<p>If not specified, the parts are presumed to be components of the field.</p></td>
</tr>
<tr class="odd">
<td>REP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td>The occurrence number, which defaults to 1. For non-repeating fields, this parameter is not necessary.</td>
</tr>
</tbody>
</table>

<u>Output:</u>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>VALUE</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th><p>These subscripts are returned:</p>
<ul>
<li><p>"ID" - the identifier</p></li>
<li><p>"TEXT" -</p></li>
<li><p>"SYSTEM" - name of the code system</p></li>
<li><p>"ALTERNATE ID" - alternate identifier</p></li>
<li><p>"ALTERNATE TEXT"</p></li>
<li><p>ALTERNATE SYSTEM" - name of the alternate coding system</p></li>
<li><p>"SYSTEM VERSION" - version ID of the coding system</p></li>
<li><p>"ALTERNATE SYSTEM VERSION" - version ID of the alternate coding system</p></li>
<li><p>"ORIGINAL TEXT"</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Get Date

<u>Routine:</u> GETDT^HLOPRS2(.SEG,.VALUE,FIELD,COMP,REP)

<u>Description:</u> Gets a date from the parsed array at the specified location and converts it to FileMan

> format. The degree of precision is optionally returned.

<u>Input:</u>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th>SEG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>The parsed segment.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FIELD</td>
<td>Required</td>
<td>Pass-by-Value</td>
<td>The sequence number of the field.</td>
</tr>
<tr class="even">
<td>COMP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td><p>If specified, the date is presumed to be a component value with the parts as subcomponents.</p>
<p>If not specified, the parts are presumed to be components of the field.</p></td>
</tr>
<tr class="odd">
<td>REP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td>The occurrence number, which defaults to 1. For non-repeating fields, this parameter is not necessary.</td>
</tr>
</tbody>
</table>

Output:

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 24%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>VALUE</th>
<th>Required</th>
<th>Pass-by-Reference Pass-by-Reference if the precision is needed</th>
<th>The date/time in FileMan format. The "PRECISION" subscript is also returned:</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><p>“PRECISION” – VALUE must be passed-by-reference if this subscript is needed</p>
<p>Expected values are:</p>
<ul>
<li><p>"S" – second (not valid for DT)</p></li>
<li><p>"M" – minute (not valid for DT)</p></li>
<li><p>"H" – hour (not valid for DT)</p></li>
<li><p>"D" - day</p></li>
<li><p>"L" - month</p></li>
<li><p>"Y" - year</p></li>
<li><p>"" - precision not specified</p></li>
</ul></td>
</tr>
</tbody>
</table>

#### Get Hierarchic Designator

<u>Routine:</u> GETHD^HLOPRS2(.SEG,.VALUE,FIELD,COMP,REP)

<u>Description:</u> Gets an HD data type (Hierarchic Designator) from the parsed segment at the specified

> location.

<u>Input:</u>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th>SEG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>The parsed segment..</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FIELD</td>
<td>Required</td>
<td>Pass-by-Value</td>
<td>The sequence number of the field.</td>
</tr>
<tr class="even">
<td>COMP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td><p>If specified, the hierarchic designator is presumed to be a component value with the parts as subcomponents.</p>
<p>If not specified, the parts are presumed to be components of the field.</p></td>
</tr>
<tr class="odd">
<td>REP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td>The occurrence number. For non-repeating fields, this parameter is not necessary.</td>
</tr>
</tbody>
</table>

<u>Output:</u>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 15%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th>VALUE</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th><p>These subscripts are returned:</p>
<ul>
<li><p>"NAMESPACE ID"</p></li>
<li><p>"UNIVERSAL ID"</p></li>
<li><p>"UNIVERSAL ID TYPE"</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Get Timestamp

<u>Routine:</u> GETTS^HLOPRS2(.SEG,.VALUE,FIELD,COMP,REP)

<u>Description:</u> Gets a timestamp in HL7 format from the segment at the specified location and converts

> it to FileMan format. If the data type value includes the time zone, then the time is

> converted to local time. The degree of precision is optionally returned.

<u>Input:</u>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th>SEG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>The parsed segment.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FIELD</td>
<td>Required</td>
<td>Pass-by-Value</td>
<td>The sequence # of the field.</td>
</tr>
<tr class="even">
<td>COMP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td><p>If specified, the time stamp is presumed to be a component value with the parts as subcomponents.</p>
<p>If not specified, the parts are presumed to be components of the field.</p></td>
</tr>
<tr class="odd">
<td>REP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td>The occurrence #, defaults to 1. For non-repeating fields, this parameter is not necessary.</td>
</tr>
</tbody>
</table>

Output:

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 15%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th>VALUE</th>
<th>Required</th>
<th>Pass-by-Reference IF subscripts are used</th>
<th>The date/time in FileMan format. The PRECISION subscript is optional, if provided the time stamp's precision will be determined.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><p>“PRECISION” - Value should be Passed-by-Reference if the precision is needed.</p>
<p>Expected values are:</p>
<ul>
<li><p>"S" - second</p></li>
<li><p>"M" - minute</p></li>
<li><p>"H" - hour</p></li>
<li><p>"D" - day</p></li>
<li><p>"L" - month</p></li>
<li><p>"Y" - year</p></li>
<li><p>"" - precision not specified</p></li>
</ul>
<p><strong>Note:</strong> FM does not allow greater precision than seconds, so greater precision will be rounded down to the second.</p></td>
</tr>
</tbody>
</table>

#### Get Extended Person Name

<u>Routine:</u> GETXPN^HLOPRS2(.SEG,.VALUE,FIELD,COMP,REP)

<u>Description:</u> Gets an XPN data type (Extended Person Name) from the parsed array at the specified

> location.

> **NOTE:** The XPN data type has additional components not included in this API. If needed, the additional components can be obtained by calling GET^HLOPRS after calling GETXPN^HLOPRS2.

This API can also be used to get the PN (Person Name) data type. The PN data type was made obsolete in version 2.5 of the HL7 standard.

<u>Input:</u>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 14%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th>SEG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>The parsed segment</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FIELD</td>
<td>Required</td>
<td>Pass-by-Value</td>
<td>The sequence number of the field.</td>
</tr>
<tr class="even">
<td>COMP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td><p>If specified, the extended person name is presumed to be a component value with the parts as subcomponents.</p>
<p>If not specified, the parts are presumed to be components of the field.</p></td>
</tr>
<tr class="odd">
<td>REP</td>
<td>Optional</td>
<td>Pass-by-Value</td>
<td>The occurrence number, which defaults to 1. For non-repeating fields, this parameter is not necessary.</td>
</tr>
</tbody>
</table>

<u>Output:</u>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 14%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th>VALUE</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th><p>These subscripts are returned:</p>
<ul>
<li><p>"FAMILY"</p></li>
<li><p>"GIVEN" first name</p></li>
<li><p>"SECOND" second and further names or initials</p></li>
<li><p>"SUFFIX" (e.g., JR)</p></li>
<li><p>"PREFIX" (e.g., DR)</p></li>
<li><p>"DEGREE" (e.g., MD)</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Returning Application Acknowledgments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Begin Application Acknowledgment for an Individual Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$ACK^HLOAPI2(.MSG,.PARMS,.ACK,.ERROR)

<u>Description:</u> Starts the process of building an application acknowledgement to return in response to an

> Individual mesage. This API should NOT be called for batch messages; instead use

> \$\$BATCHACK^HLOAPI3.

<u>Input:</u>

<table style="width:100%;">
<colgroup>
<col style="width: 3%" />
<col style="width: 36%" />
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">MSG</th>
<th>Required</th>
<th>Pass-by-Reference</th>
<th>Contains the original message. Its obtained by calling $$STARTMSG^HLOPRS.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p>PARMS</p>
<p>Allowed subscripts:</p></td>
<td>Required</td>
<td>Pass-by-Reference</td>
<td>Contains various parameters that may be set to configure the application acknowledgment message.</td>
</tr>
<tr class="even">
<td rowspan="15"></td>
<td>"ACK CODE"</td>
<td>Required</td>
<td colspan="2">The value to return in MSA-1. Possible values are “AA”, “AE”, or “AR”.</td>
</tr>
<tr class="odd">
<td>"ERROR MESSAGE"</td>
<td>Optional</td>
<td colspan="2">An optional error message to return in MSA-3, should be used only if the return code is AE or AR.</td>
</tr>
<tr class="even">
<td>"ACCEPT ACK RESPONSE"</td>
<td>Optional</td>
<td colspan="2">The &lt;tag^routine&gt; to call in response to a commit acknowledgment.</td>
</tr>
<tr class="odd">
<td>"ACCEPT ACK TYPE"</td>
<td>Optional</td>
<td colspan="2">Indicates whether or not to request a commit acknowledgment. Possible values are “AL” or “NE”. Defaults to “AL”.</td>
</tr>
<tr class="even">
<td>"CONTINUATION POINTER"</td>
<td>Optional</td>
<td colspan="2">Indicates a fragmented message.</td>
</tr>
<tr class="odd">
<td>"COUNTRY"</td>
<td>Optional</td>
<td colspan="2">The three-character country code</td>
</tr>
<tr class="even">
<td>"EVENT"</td>
<td>Optional</td>
<td colspan="2">The three-character event type which defaults to the event code of the original message.</td>
</tr>
<tr class="odd">
<td>"ENCODING CHARACTERS"</td>
<td>Optional</td>
<td colspan="2">The four HL7 encoding characters which defaults to "^~\&amp;".</td>
</tr>
<tr class="even">
<td>"FAILURE RESPONSE"</td>
<td>Optional</td>
<td colspan="2">The &lt;tag&gt;^&lt;routine&gt; that the sending application routine should execute if the transmission of the message fails.</td>
</tr>
<tr class="odd">
<td>"FIELD SEPARATOR"</td>
<td>Optional</td>
<td colspan="2">Field separator which defaults to "|".</td>
</tr>
<tr class="even">
<td>"MESSAGE TYPE"</td>
<td>Optional</td>
<td colspan="2">If not defined, ACK is used.</td>
</tr>
<tr class="odd">
<td>"MESSAGE STRUCTURE CODE"</td>
<td>Optional</td>
<td colspan="2">An optional code for the MSH-9 field.</td>
</tr>
<tr class="even">
<td>"QUEUE"</td>
<td>Optional</td>
<td colspan="2">An application can name its own private queue (a string under 20 characters, it should be namespaced). The default is the name of the queue of the original message</td>
</tr>
<tr class="odd">
<td>“SECURITY"</td>
<td>Optional</td>
<td colspan="2">Security information to include in the header segment, SEQ-8.</td>
</tr>
<tr class="even">
<td>"VERSION"</td>
<td>Optional</td>
<td colspan="2">The HL7 Version ID which defaults to 2.4.</td>
</tr>
</tbody>
</table>

<u>Output:</u> Function call returns 1 on success, 0 on failure.

| PARMS |          |                   | Killed when the function returns.                              |
|-------|----------|-------------------|----------------------------------------------------------------|
| ACK   | Required | Pass-by-Reference | The workspace where the acknowledgment message is being built. |
| ERROR | Optional | Pass-by-Reference | On encountering an error, returns a message.                   |

### Begin Batch Application Acknowledgement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$BATCHACK^HLOAPI3(.MSG,.PARMS,.ACK,.ERROR)

<u>Description:</u> Used to initiate a batch application acknowledgement. It will contain individual

> application acknowledgements for each message in the original batch message that was

> received via HLO. Individual acknowledgements are placed in this batch by calling \$\$ADDACK^HLOAPI3, then the batch of acknowledgements is actually sent by calling \$\$SENDACK^HLOAPI2

<u>Input:</u>

<table>
<colgroup>
<col style="width: 2%" />
<col style="width: 23%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">MSG</th>
<th>Required</th>
<th colspan="2">Pass-by-Reference</th>
<th>Obtained by calling $$STARTMSG^HLOPRS when parsing the original message. The application MUST NOT directly modify any values in this array.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p>PARMS</p>
<p>Allowed subscripts:</p></td>
<td>Optional</td>
<td colspan="2">Pass-by-Reference</td>
<td>Used to pass in various parameters.</td>
</tr>
<tr class="even">
<td rowspan="9"></td>
<td>"ACCEPT ACK RESPONSE"</td>
<td colspan="2">Optional</td>
<td colspan="2">&lt;tag^routine&gt; to call in response to a commit ack.</td>
</tr>
<tr class="odd">
<td>"ACCEPT ACK TYPE"</td>
<td colspan="2">Optional</td>
<td colspan="2">&lt;AL,NE&gt; which defaults to AL.</td>
</tr>
<tr class="even">
<td>"COUNTRY"</td>
<td colspan="2">Optional</td>
<td colspan="2">A three-character country code from the HL7 standard table.</td>
</tr>
<tr class="odd">
<td>"ENCODING CHARACTERS"</td>
<td colspan="2">Optional</td>
<td colspan="2">The four HL7 encoding characters; optional, defaults to "^~\&amp;".</td>
</tr>
<tr class="even">
<td>"FAILURE RESPONSE"</td>
<td colspan="2">Optional</td>
<td colspan="2">The &lt;tag&gt;^&lt;routine&gt; that the sending application routine should execute if the transmission of the message fails, i.e., the message cannot be sent or a requested commit ack is not received.</td>
</tr>
<tr class="odd">
<td>"FIELD SEPARATOR"</td>
<td colspan="2">Optional</td>
<td colspan="2">Field separator; optional, defaults to "|".</td>
</tr>
<tr class="even">
<td>"QUEUE"</td>
<td colspan="2">Optional</td>
<td colspan="2">An application can name a private queue (a string under 20 characters, it should be namespaced). The default is the name of the queue of the original message.</td>
</tr>
<tr class="odd">
<td>"SECURITY"</td>
<td colspan="2">Optional</td>
<td colspan="2">Security information to include in the header segment, SEQ-8.</td>
</tr>
<tr class="even">
<td>"VERSION"</td>
<td colspan="2">Optional</td>
<td colspan="2">The HL7 Version ID which defaults to 2.4.</td>
</tr>
</tbody>
</table>

<u>Output:</u> Function call - returns 1 on success, 0 on failure.

| PARMS |          |                   | Killed when the function returns.        |
|-------|----------|-------------------|------------------------------------------|
| ACK   | Required | Pass-by-Reference | The acknowledgement message being built. |
| ERROR | Optional | Pass-by-Reference | An error message.                        |

### Add an Application Acknowledgement to a Batch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$ADDACK^HLOAPI3(.ACK,.PARMS,.ERROR)

<u>Description:</u> Used to add an application acknowledgement to a batch acknowledgement message that

was started by calling \$\$BATCHACK^HLOAPI3.

<u>Input:</u>

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 32%" />
<col style="width: 12%" />
<col style="width: 1%" />
<col style="width: 16%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">ACK</th>
<th colspan="2">Required</th>
<th>Pass-by-Reference</th>
<th>The batch of acknowledgements that is being built.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p>PARMS</p>
<p>Allowed subscripts:</p></td>
<td colspan="2">Required</td>
<td>Pass-by-<br />
Reference</td>
<td>Used to pass in various parameters.</td>
</tr>
<tr class="even">
<td rowspan="7"></td>
<td>“ACK CODE"</td>
<td>Required</td>
<td colspan="3">Allowed values are AA, AE, or AR, and is used to populate MSA-1.</td>
</tr>
<tr class="odd">
<td>“ERROR MESSAGE"</td>
<td>Optional</td>
<td colspan="3">If the “ACK CODE” is AE or AR, then the value passed in this parameter is used to populate MSA-3.</td>
</tr>
<tr class="even">
<td>“EVENT"</td>
<td>Optional</td>
<td colspan="3">A three-character event type (optional, defaults to the event type of the original message).</td>
</tr>
<tr class="odd">
<td>“MESSAGE CONTROL ID"</td>
<td>Required</td>
<td colspan="3">The message control ID of the original individual message within the batch that is being acknowledged.</td>
</tr>
<tr class="even">
<td>“MESSAGE STRUCTURE CODE"</td>
<td>Optional</td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td>“MESSAGE TYPE"</td>
<td>Optional</td>
<td colspan="3">A three-character message type that defaults to ACK.</td>
</tr>
<tr class="even">
<td>“SECURITY"</td>
<td>Optional</td>
<td colspan="3">Security information to include in the header segment SEQ-8.</td>
</tr>
</tbody>
</table>

Output: (Function call returns 1 on success, 0 on failure.)

| PARMS |          |                   | Killed when the function returns.        |
|-------|----------|-------------------|------------------------------------------|
| ACK   | Required | Pass-by-Reference | The acknowledgement message being built. |
| ERROR | Optional | Pass-by-Reference | An error message.                        |

### Send the Application Acknowledgement.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$SENDACK^HLOAPI2(.ACK,.ERROR)

<u>Description:</u> Used to send the acknowledgement message that was initiated by a call to

> \$\$ACK^HLAPI2 or a batch of acknowledgement messages that was initiated by a call to

> \$\$BATCHACK^HLOAPI3.

<u>Input:</u>

| ACK | Required | Pass-by-Reference | An array that contains the acknowledgement message. |
|-----|----------|-------------------|-----------------------------------------------------|

<u>Output:</u> Function Call - Returns 1 on success, 0 on failure.

| ERROR | Optional | Pass-by-Reference | An error message is returned if the function fails. |
|-------|----------|-------------------|-----------------------------------------------------|

## Subscription Registry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An entry in the HLO Subscription Registry is similar to a mailing list in that it can be used to send HL7 messages to multiple recipients. The application that creates the entry is the owner and is responsible for maintaining it.

### Create an Entry in the Subscription Registry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$CREATE^HLOASUB(OWNER,DESCRIPTION,.ERROR)

<u>Description:</u> Used to create a new entry in the HLO SUBSCRIPTION REGISTRY File (#779.4).

<u>Input:</u>

| OWNER       | Required | Pass-by-Value | The name of the owning application. It should be prefixed with the package namespace to ensure uniqueness. |
|-------------|----------|---------------|------------------------------------------------------------------------------------------------------------|
| DESCRIPTION | Required | Pass-by-Value | A brief (1 line) description.                                                                              |

<u>Output:</u> Function call returns the new IEN in the HLO SUBSCRIPTION REGISTRY File (#779.4) if successful, 0 if error.

| ERROR | Optional | Pass-by-Reference | An error message is returned if the function fails. |
|-------|----------|-------------------|-----------------------------------------------------|

### Add a New Recipient to a Subscription Registry Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$ADD^HLOASUB(IEN,.WHO,.ERROR)

<u>Description:</u> Used to add a new recipient to the subscription list.

<u>Input:</u>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 2%" />
<col style="width: 8%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th>IEN</th>
<th colspan="2">Required</th>
<th>Pass-by-Value</th>
<th colspan="2">The IEN of the entry in the HLO SUBSCRIPTION REGISTRY File (#779.4).</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WHO</td>
<td colspan="2">Required</td>
<td>Pass-by-Reference</td>
<td colspan="2">Used to define a new subscriber.</td>
</tr>
<tr class="even">
<td colspan="6"><strong>These subscripts are allowed:</strong></td>
</tr>
<tr class="odd">
<td colspan="2">"RECEIVING APPLICATION"</td>
<td colspan="3">Required</td>
<td>String, 60 char max, required.</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td colspan="4"><p><strong>ONE</strong> of the following four parameters <strong>MUST</strong> be provided to identify the Receiving</p>
<p>Facility:</p></td>
</tr>
<tr class="odd">
<td colspan="2">"FACILITY LINK IEN"</td>
<td colspan="3">Optional</td>
<td>IEN of the logical link.</td>
</tr>
<tr class="even">
<td colspan="2">"FACILITY LINK NAME"</td>
<td colspan="3">Optional</td>
<td>Name of the logical link.</td>
</tr>
<tr class="odd">
<td colspan="2">"INSTITUTION IEN"</td>
<td colspan="3">Optional</td>
<td>Pointer to the INSTITUTION File (#4).</td>
</tr>
<tr class="even">
<td colspan="2">"STATION NUMBER"</td>
<td colspan="3">Optional</td>
<td>Station number with suffix.</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="4"><strong>ONE</strong> of the following two parameters <strong>MAY</strong> be provided - optionally - to identify the middleware to route the message through, such as an interface engine:</td>
</tr>
<tr class="even">
<td colspan="2">“MIDDLEWARE LINK IEN")</td>
<td colspan="3">Optional</td>
<td>Pointer to a logical link for that is setup to communicate with the middleware.</td>
</tr>
<tr class="odd">
<td colspan="2">“MIDDLEWARE LINK NAME"</td>
<td colspan="3">Optional</td>
<td>Name of the link to communicate with the middleware.</td>
</tr>
</tbody>
</table>

<u>Output:</u> Function call returns the IEN of the recipient from the RECIPIENTS multiple, 0 on failure.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th>WHO</th>
<th></th>
<th></th>
<th>Killed when the function returns.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ERROR</td>
<td>Optional</td>
<td>Pass-by-Reference</td>
<td><p>On an error, one of the following error messages may be returned:</p>
<ul>
<li><p>“SUBSCRIPITON REGISTRY ENTRY NOT FOUND”</p></li>
<li><p>“RECEIVING FACILTY LOGICAL LINK NOT FOUND”</p></li>
<li><p>“RECEIVING APPLICATION NOT FOUND”</p></li>
<li><p>“MIDDLEWARE LOGICAL LINK PROVIDED BUT NOT FOUND”</p></li>
<li><p>“FAILED TO ACTIVATE SUBSCRIBER”</p></li>
</ul></td>
</tr>
</tbody>
</table>

### Terminate a Recipient from a Subscription Registry Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$END^HLOASUB(IEN,.WHO)

<u>Description:</u> Used to terminate a recipient from the subscriber list. The recipient is not deleted, but the

> DATE/TIME TERMINATED field is entered with the current date/time.

<u>Input:</u>

| IEN | Required | Pass-by-Value     | The IEN of the HLO SUBSCRIPTION REGISTRY File (#779.4) entry.                                                                                    |
|-----|----------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| WHO | Required | Pass-by-Reference | If WHO("SUBIEN") is defined, then it should be the IEN of the sub-record to be terminated. Otherwise, set the parameters as per \$\$ADD^HLOASUB. |

<u>Output:</u> Function call returns 1 on success, 0 on failure.

| WHO |     |     | Killed when the function returns. |
|-----|-----|-----|-----------------------------------|

### Check Subscription Registry Entry for a Recipient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine :</u> \$\$ONLIST^HLOASUB(IEN,LINKIEN,APPNAME,FAC1,FAC2,FAC3)

<u>Description:</u> Used to locate an individual recipient within a subscription registry entry.

<u>Input:</u>

| IEN     | Required | Pass-by-Value | The IEN of the HLO SUBSCRIPTION REGISTRY File (#779.4) entry. |
|---------|----------|---------------|---------------------------------------------------------------|
| LINKIEN | Required | Pass-by-Value | IEN of the logical link.                                      |
| APPNAME | Required | Pass-by-Value | Name of the receiving application.                            |
| FAC1    | Required | Pass-by-Value | Component 1 of the receiving facility.                        |
| FAC2    | Required | Pass-by-Value | Component 2 of the receiving facility.                        |
| FAC3    | Required | Pass-by-Value | Component 3 of the receiving facility.                        |

Output: Function call returns the IEN of the recipient from the RECIPIENTS multiple, 0 on failure.

### Retrieve Next Recipient from a Subscription Registry Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$NEXT^HLOASUB(IEN,.RECIP)

<u>Description:</u> Used to loop through a subscription list. It ignores recipients that have been terminated

> from the specified subscription registry entry.

<u>Input:</u>

| IEN   | Required | Pass-by-Value     | The IEN of the HLO SUBSCRIPTION REGISTRY File (#779.4) entry.                                                                                                        |
|-------|----------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RECIP | Required | Pass-by-Reference | If empty, the function finds the first recipient in the specified subscription registry entry, else it uses the value of RECIP("SUBIEN") to find the next recipient. |

<u>Output:</u> Function call - Returns the IEN of the recipient from the RECIPIENTS multiple, 0 on

> Failure. If no more recipients are found, then SUBIEN=-1 and all other subscripts are set

> to null.

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 21%" />
<col style="width: 7%" />
<col style="width: 17%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>RECIP</p>
<p>These subscripts are returned:</p></th>
<th colspan="2">Required</th>
<th>Pass-by-Reference</th>
<th>Returns the next recipient in the specified subscription registry entry.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="7"></td>
<td colspan="2">“LINK IEN"</td>
<td colspan="3">IEN of the logical link</td>
</tr>
<tr class="even">
<td colspan="2">"LINK NAME"</td>
<td colspan="3">Name of the logical link</td>
</tr>
<tr class="odd">
<td colspan="2">"RECEIVING APPLICATION”</td>
<td colspan="3">Name of receiving application</td>
</tr>
<tr class="even">
<td colspan="2">("RECEIVING FACILITY",1)</td>
<td colspan="3">Component 1 of receiving facility</td>
</tr>
<tr class="odd">
<td colspan="2">("RECEIVING FACILITY",2)</td>
<td colspan="3">Component 2 of receiving facility</td>
</tr>
<tr class="even">
<td colspan="2">("RECEIVING FACILITY",3)</td>
<td colspan="3">Component 3 of receiving facility</td>
</tr>
<tr class="odd">
<td colspan="2">“SUBIEN"</td>
<td colspan="3">The IEN in the multiple, used to find the next recipient in the specified subscription registry entry</td>
</tr>
</tbody>
</table>

### Build a Subscription Registry Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$INDEX^HLOASUB1(IEN,.PARMS)

<u>Description:</u> Used to build an index of its subscriptions. This is optional, but using this function allows

> the application to find subscriptions without storing the IEN.

<u>Input:</u>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th>IEN</th>
<th>Required</th>
<th>Pass-by-Value</th>
<th>The IEN of the HLO SUBSCRIPTION REGISTRY File (#779.4) entry.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PARMS</td>
<td>Required</td>
<td>Pass-by-Reference</td>
<td><p>An array of parameters with which to build the index. The format is:</p>
<p>PARMS(1)=&lt;first parameter&gt;,</p>
<p>PARMS(2)=&lt;second parameter&gt;</p>
<p>If PARMS(i)=null, the parameter is translated to a single space.</p></td>
</tr>
</tbody>
</table>

<u>Output:</u> Function Call - Returns 1 on success, 0 on failure.

| PARMS |     |     | Killed when the function returns. |
|-------|-----|-----|-----------------------------------|

### Find a Subscription Registry Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$FIND^HLOASUB1(OWNER,.PARMS)

<u>Description:</u> Used to find a subscription registry entry. The application must maintain a private index

> via \$\$INDEX^HLOASUB1 in order to utilize this function,

<u>Input:</u>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 10%" />
<col style="width: 18%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>OWNER</th>
<th>Required</th>
<th>Pass-by-Value</th>
<th>The name of the owning application, as entered in $$CREATE^HLOSUB.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PARMS</td>
<td>Required</td>
<td>Pass-by-Reference</td>
<td><p>An array of parameters with which to build the index. The format is:</p>
<p>PARMS(1)=&lt;first parameter&gt;,</p>
<p>PARMS(2)=&lt;second parameter&gt;</p>
<p>If PARMS(i)=null, the parameter is translated to a single space.</p></td>
</tr>
</tbody>
</table>

<u>Output:</u> Function returns the IEN of the subscription list if found, 0 otherwise.

| PARMS |     |     | Killed when the function returns. |
|-------|-----|-----|-----------------------------------|

## Miscellaneous APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Resend a Message 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$RESEND^HLOAPI3(MSGIEN,.ERROR)

<u>Description:</u> Used to retransmit a message by making a copy of the message, reusing all the original parameters. Then the message is placed in the same outgoing queue as the original message.

<u>Input:</u>

| MSGIEN | Required | Pass-by-Value | The IEN of the HLO MESSAGES file (#778) entry that is to be resent. |
|--------|----------|---------------|---------------------------------------------------------------------|

<u>Output:</u> Function returns the IEN of the new message in HLO MESSAGES file (#778) on

> success, 0 on failure.

| ERROR | Optional | Pass–by-Reference | On failure, will return an error message. |
|-------|----------|-------------------|-------------------------------------------|

### Reprocess a Message 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$REPROC^HLOAPI3(MSGIEN,.ERROR)

<u>Description:</u> Used to place a message back on an incoming queue for reprocessing by the application.

> The HLO in-filer process will execute the applications routine in the background.

<u>Input:</u>

| MSGIEN | Required | Pass-by-Value | The IEN of the HLO MESSAGES file (#778) entry that is to be reprocessed. |
|--------|----------|---------------|--------------------------------------------------------------------------|

<u>Output:</u> Function Call - Rreturns 1 on success, 0 on failure

| ERROR | Optional | Pass-by-Reference | On failure, will contain an error message. |
|-------|----------|-------------------|--------------------------------------------|

### Reprocess a Message Immediately

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$PROCNOW^HLOAPI3(MSGIEN,.ERROR)

<u>Description:</u> Used to pass a message immediately to the application for processing. It differs from

> \$\$REPROC^HLOAPI3 in that it does not put the message on the incoming queue for

> the in-filer to process, instead it executes the application routine immediately.

<u>Input:</u>

| MSGIEN | Required | Pass-by-Value | The IEN of the HLO MESSAGES file (#778) entry that is to be reprocessed. |
|--------|----------|---------------|--------------------------------------------------------------------------|

<u>Output:</u> Function Call - Returns 1 on success, 0 on failure.

| ERROR | Optional | Pass-by-Reference | On failure, will contain an error message. |
|-------|----------|-------------------|--------------------------------------------|

### Reset the Purge Date and Time for a Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$SETPURGE^HLOAPI3(MSGIEN,TIME)

<u>Description:</u> Used to reset the scheduled purge date/time of a message.

<u>Input:</u>

| MSGIEN | Required | Pass-by/Value     | The IEN of the HLO MESSAGES file (#778) entry that is to be modified. |
|--------|----------|-------------------|-----------------------------------------------------------------------|
| TIME   | Optional | Pass-by-Reference | The new scheduled purge date/time. If not defined, defaults to NOW.   |

<u>Output:</u> Function returns 1 on success, 0 on failure.

### Count Messages on All Queues 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$QUECNT^HLOQUE(.ARRAY)

<u>Description:</u> Returns the count of messages pending on all incoming, outgoing, and sequence queues.

<u>Input:</u> None

<u>Output:</u>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 59%" />
</colgroup>
<tbody>
<tr class="odd">
<td>ARRAY</td>
<td>Required</td>
<td>Pass-by-Reference</td>
<td><p>The array will return a list of all queues and the message count on each. The format is:</p>
<p>ARRAY("TOTAL") = Total number of messages on all</p>
<p>queues.</p>
<p>ARRAY("OUT") = Total number of outgoing messages</p>
<p>ARRAY("IN") = Total number of incoming messages.</p>
<p>ARRAY("SEQ")= Total number of messages on sequence</p>
<p>queues.</p>
<p>ARRAY("IN",&lt;link_name&gt;,&lt;queue_name&gt;) = Number of</p>
<p>messages on given link and queue.</p>
<p>ARRAY("OUT",link_name,queue_name) = Number of</p>
<p>messages on given link and queue.</p>
<p>ARRAY("SEQ",&lt;queue_name&gt;) = Number of messages on</p>
<p>the given sequence queue.</p></td>
</tr>
</tbody>
</table>

### Count Messages on Outgoing Queues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$OUT^HLOQUE(.ARRAY)

<u>Description:</u> Returns the count of messages pending on all outgoing queues.

<u>Input:</u> None.

<u>Output:</u>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 59%" />
</colgroup>
<tbody>
<tr class="odd">
<td>ARRAY</td>
<td>Required</td>
<td>Pass-by-Reference</td>
<td><p>ARRAY will return the list of outbound queues and the message count on each. The format is:</p>
<p>ARRAY("OUT") = Total number of outgoing messages.</p>
<p>ARRAY("OUT",&lt;link_name&gt;,&lt;queue_name&gt;) = Number of</p>
<p>messages on the given link and queue. *This array will</p>
<p>only exist if the number of messages in the queue is</p>
<p>greater than 0.</p></td>
</tr>
</tbody>
</table>

### Count of Messages on Incoming Queues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine :</u> \$\$IN^HLOQUE(.ARRAY)

<u>Description:</u> Returns the count of messages pending on all incomming queues.

<u>Input:</u> None

<u>Output:</u>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 59%" />
</colgroup>
<tbody>
<tr class="odd">
<td>ARRAY</td>
<td>Required</td>
<td>Pass-by-Reference</td>
<td><p>ARRAY will return a list of the inbound queues and the message count on each. The format is:</p>
<p>ARRAY("IN") = Total number of outgoing messages.</p>
<p>ARRAY("IN",&lt;sending facility&gt;,&lt;queue_name&gt;) = Number</p>
<p>of messages on the given link and queue.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### Count of the number of messages on the sequence queues. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine:</u> \$\$SEQ^HLOQUE(.ARRAY)

<u>Description :</u> Returns the total number of messages pending on the incoming queues.

<u>Input:</u> None.

<u>Output:</u>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 59%" />
</colgroup>
<tbody>
<tr class="odd">
<td>ARRAY</td>
<td>Required</td>
<td>Pass-by-Reference</td>
<td><p>Array will return a list of all the sequences queues. The format is:</p>
<p>ARRAY("SEQ") = Total number of sequence queue messages.</p>
<p>ARRAY("SEQ",&lt;link_name&gt;,&lt;queue_name&gt;) = Number of messages on given link and queue.</p></td>
</tr>
</tbody>
</table>

# Code Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## HLODEM1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLODEM1 ;ALB/CJM-HL7 - Demonstration Code ;04/20/2009

;;1.6;HEALTH LEVEL SEVEN;\*\*146\*\*;Oct 13, 1995;Build 34

;Per VHA Directive 2004-038, this routine should not be modified.

;

;

PID(DFN,SEQ,SEG) --

;

;Description:

; Builds the PID segment using the HLO segment building APIs.

; PIMS APIs are called to obtain data from PATIENT file (#2).

;

; The fields that are included in the segment are:

; PID-1 Set ID

; PID-3 Patient Identifier List: This is a repeating field.

; The first repetition will be set to the ICN, the second to

; the SSN.

; PID-5 Patient Name

; PID-7 Date/Time of Birth

; PID-11 Patient Address

;

;Input:

; DFN (required) The IEN of the record in the PATIENT file (#2).

; SEQ (optional) Value for PID-1, the Set ID field. For the first

; occurrence of the PID segment it should be set to 1, for the

; second 2, etc.

;

;Output:

; SEG (pass-by-reference) The segment, returned as a list of fields.

;

;

N VA,VADM,VAHOW,VAROOT,VATEST,VAPA,NAME,DOB,SSN,ICN,ADDRESS

K SEG S SEG="" ;The segment should start off blank.

;

;Get the patient data using PIMS utilities.

;

S VAHOW=1

D DEM^VADPT

S NAME=VADM("NM") ;The name returned in non-standard (VHA) format.

;

;Standardize the format of the name using a Kernel utility.

;Returns the subscripts "FAMILY","GIVEN","MIDDLE","SUBSCRIPT".

D STDNAME^XLFNAME(.NAME,"C")

;

S DOB=\$P(VADM("DB"),"^") ;in FileMan format

S SSN=\$P(VADM("SS"),"^")

;

;Get the address.

S VAHOW=""

D ADD^VADPT

;Move address components into ADDRESS.

S ADDRESS("STREET1")=VAPA(1)

S ADDRESS("STREET2")=VAPA(2)

S ADDRESS("CITY")=VAPA(4)

S ADDRESS("STATE")=\$P(VAPA(5),"^",2)

S ADDRESS("ZIP")=VAPA(6)

;

;Call an MPI utility to get the ICN.

S ICN=\$P(\$\$GETICN^MPIF001(DFN),"V")

;

;Use the HLO APIs to set the data into the segment.

;

D SET^HLOAPI(.SEG,"PID",0) ;Set the segment type.

D SET^HLOAPI(.SEG,SEQ,1) ;Set PID-1.

;

;Set ICN into PID-3, repetition 1.

D SET^HLOAPI(.SEG,ICN,3,1,1,1) ;component 1, subcomponent 1

D SET^HLOAPI(.SEG,"USVHA",3,4,1,1) ;component 4, subcomponent 1

D SET^HLOAPI(.SEG,"0363",3,4,3,1) ;component 4, subcomponent 3

D SET^HLOAPI(.SEG,"NI",3,5,1,1) ;component 5

;

;Set SSN into PID-3, repetition 2.

D SET^HLOAPI(.SEG,SSN,3,1,1,2) ;component 1, subcomponent 1

D SET^HLOAPI(.SEG,"USSSA",3,4,1,2) ;component 4, subcomponent 1

D SET^HLOAPI(.SEG,"0363",3,4,3,2) ;component 4, subcomponent 3

D SET^HLOAPI(.SEG,"SS",3,5,1,2) ;component 5

;

;Set the name into PID-5.

D SETXPN^HLOAPI4(.SEG,.NAME,5)

;

;Set DOB into PID-7.

D SETDT^HLOAPI4(.SEG,DOB,7)

;

;Set the address into PID-11.

D SETAD^HLOAPI4(.SEG,.ADDRESS,11)

Q

;

NK1(DFN,SEQ,SEG) --

;

;Description:

; Builds the NK1 segment for the primary emergency contact

; using the HLO segment building APIs. A PIMS API is called to get the

; necesary data from PATIENT file (#2).

;

; The fields included in the segment are:

; NK1-1 Set ID: Set to the SEQ input parameter. For the 1st

; occurrence of the NK1 segment it should be set

; to 1, for the 2nd 2, etc.

; NK1-2 Name

; NK1-3 Relationship

; NK1-4 Address

; NK1-5 Phone Number

; NK1-7 Contact Role

;

;Input:

; DFN (required) The IEN of the record in the PATIENT file (#2).

; SEQ (optional) Value for NK1-1.

;

;Output:

; SEG (pass-by-reference) Will return an array containing the segment.

; The ADDSEG^HLOAPI API must be called to move the segment into

; the message.

;

N VA,VAOA,VAHOW,VAROOT,VATEST,NAME,ADDRESS

K SEG S SEG="" ;The segment should start off blank.

;

;Get the patient's emergency contact using a PIMS utility.

S VAOA("A")=1

D OAD^VADPT

;

S NAME=VAOA(9) ;The name is returned in non-standard (VHA) format.

;

;Standardize the format of the name using a Kernel utility.

;Returns the subscripts "FAMILY","GIVEN","MIDDLE","SUBSCRIPT".

D STDNAME^XLFNAME(.NAME,"C")

;

;Move the address components into ADDRESS.

S ADDRESS("STREET1")=VAOA(1)

S ADDRESS("STREET2")=VAOA(2)

S ADDRESS("CITY")=VAOA(4)

S ADDRESS("STATE")=\$P(VAOA(5),"^",2)

S ADDRESS("ZIP")=VAOA(6)

;

;Now set the data into the segment.

;

D SET^HLOAPI(.SEG,"NK1",0) ;Set the segment type.

D SET^HLOAPI(.SEG,SEQ,1) ;Set NK1-1.

;

;Set the name into NK1-2.

D SETXPN^HLOAPI4(.SEG,.NAME,2)

;

;Set the relationship into NK1-3, component 2.

D SET^HLOAPI(.SEG,VAOA(10),3,2)

;

;Set the address into NK1-4.

D SETAD^HLOAPI4(.SEG,.ADDRESS,4)

;

;Set the phone number into NK1-5.

D SET^HLOAPI(.SEG,VAOA(8),5)

;

;Set the contact role into NK1-7.

D SET^HLOAPI(.SEG,"EP",7,1)

D SET^HLOAPI(.SEG,"EMERGENCY CONTACT PERSON",7,2)

D SET^HLOAPI(.SEG,"0131",7,3)

Q

A08(DFN,ERROR) --

;

;Description:

; Builds an ADT~A08 message and queues it for transmission.

; Included segments are the PID and NK1.

;

;Input:

; DFN (required) ien of a patient record in the PATIENT file (#2)

;Output:

; function:

; On Success: Returns the ien of the messgage in the

; HLO MESSAGES file (#778).

; On Failure: Returns 0.

; ERROR - (optional, pass-by-refernce) On failure returns an

; error message.

;

;Required Setup:

;\<\<HLO APPLICATION PARAMETER - file \#779.2\>\>

; \*\* The sending application. \*\*

; APPLICATION NAME: HLO DEMO SENDING APPLICATION

; \*\* The package that is sending the message. \*\*

; Package File Link: HL7 OPTIMIZED (HLO)

;

;\<\<HL Logical Link, file \#870\>\>

; \*\* The receiving facility. \*\*

;NODE: HLODEMO

; INSTITUTION: \<Institution entered here.\>

; LLP TYPE: TCP

; MAILMAN DOMAIN: \<The use of DNS DOMAIN is preferred for new links.\>

; DNS DOMAIN: \<TCP/IP domain name for DNS entered here.\>

; TCP/IP ADDRESS: \<IP address entered here.\>

; TCP/IP SERVICE TYPE: CLIENT (SENDER)

; TCP/IP PORT (OPTIMIZED): \<Port \# entered here.\>

;

;

N SEG,PARMS,WHOTO

S PARMS("MESSAGE TYPE")="ADT"

S PARMS("EVENT")="AO8"

I '\$\$NEWMSG^HLOAPI(.PARMS,.MSG,.ERROR) Q 0

D PID(DFN,1,.SEG)

I '\$\$ADDSEG^HLOAPI(.MSG,.SEG,.ERROR) Q 0

D NK1(DFN,1,.SEG)

I '\$\$ADDSEG^HLOAPI(.MSG,.SEG,.ERROR) Q 0

S PARMS("SENDING APPLICATION")="HLO DEMO SENDING APPLICATION"

S WHOTO("RECEIVING APPLICATION")="HLO DEMO RECEIVING APPLICATION"

S WHOTO("FACILITY LINK NAME")="HLODEMO"

Q \$\$SENDONE^HLOAPI1(.MSG,.PARMS,.WHOTO,.ERROR)

;

BATCHA08(DFNLIST,ERROR) --

;

;Description:

; Builds a batch of ADT~A08 messages and queues it for transmission.

; The DFNLIST is a list of patients to include messages for.

;

;Input:

; DFNLIST (required, pass-by-reference) A list of patient DFNs in the

; format DFNLIST(\<DFN)="".

;Output:

; Function:

; On Success: Returns the ien of the messgage in the

; HLO MESSAGES file (#778).

; On Failure: Returns 0.

; ERROR (optional, pass-by-refernce) On failure returns an error

; message.

;

;Required Setup: Same as for A08^HLODEM1

;

N MSG,PARMS,SEG,WHOTO,MSG,DFN,QUIT

I '\$\$NEWBATCH^HLOAPI(,.MSG,.ERROR) Q 0

S (DFN,QUIT)=0

F S DFN=\$O(DFNLIST(DFN)) Q:(QUIT!('DFN)) D

.N PARMS

.S PARMS("MESSAGE TYPE")="ADT"

.S PARMS("EVENT")="AO8"

.I '\$\$ADDMSG^HLOAPI(.MSG,.PARMS,.ERROR) S QUIT=1 Q

.D PID(DFN,1,.SEG)

.I '\$\$ADDSEG^HLOAPI(.MSG,.SEG,.ERROR) Q 0

.D NK1(DFN,1,.SEG)

.I '\$\$ADDSEG^HLOAPI(.MSG,.SEG,.ERROR) Q 0

;

S PARMS("SENDING APPLICATION")="HLO DEMO SENDING APPLICATION"

S WHOTO("RECEIVING APPLICATION")="HLO DEMO RECEIVING APPLICATION"

S WHOTO("FACILITY LINK NAME")="HLODEMO"

Q \$\$SENDONE^HLOAPI1(.MSG,.PARMS,.WHOTO,.ERROR)

Q

## HLODEM2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLODEM2 ;ALB/CJM-HL7 - Demonstration Code ;04/20/2009

;;1.6;HEALTH LEVEL SEVEN;\*\*146\*\*;Oct 13, 1995;Build 34

;Per VHA Directive 2004-038, this routine should not be modified.

;

;

PID(DFN,SEQ,SEG) --

;

;Description: Builds the PID segment exactly as in PID^HLODEM1, but

; without using the HLO APIs for setting the values into the segment.

;

;Input:

; DFN (required) The IEN of the record in the PATIENT file (#2).

; SEQ (optional) Value for PID-1, Set ID. For the first occurence

; of the segement it should be set to 1, for the second 2, etc.

;

;Output:

; SEG (pass-by-reference) The PID segment as a single line.

;

;Notes: 1) Assumes that the variables returned from INIT^HLFNC2 are

; defined, specifically, HL("FS") and HL("ECH").

; 2) This segment builder takes the shortcut of not replacing

; delimiters that occur within data fields with their

; escape sequences.

; 3) Also takes the shortcut of assuming the segment will fit

; on a single node.

;

N VA,VADM,VAHOW,VAROOT,VATEST,VAPA,NAME,DOB,SSN,ICN,ADDRESS,FS,CS,RS,SS

K SEG S SEG="" ;The segment should start off blank.

;

;Set the message delimiters for easy reference.

S FS=HL("FS") ;field separator

S CS=\$E(HL("ECH"),1) ;component separator

S RS=\$E(HL("ECH"),2) ;repitition separator

S SS=\$E(HL("ECH"),4) ;subcomponent separator

;

;Get the patient data using a PIMS utility.

S VAHOW=1

D DEM^VADPT

S NAME=VADM("NM") ;The name is returned in non-standard (VHA) format.

;

;Standardize the format of the name using a Kernel utility.

;Returns the subscripts "FAMILY","GIVEN","MIDDLE","SUBSCRIPT".

D STDNAME^XLFNAME(.NAME,"C")

;

S DOB=\$P(VADM("DB"),"^") ;(in FileMan format)

S SSN=\$P(VADM("SS"),"^")

;

;Get the address.

S VAHOW=""

D ADD^VADPT

;Move address components into ADDRESS.

S ADDRESS("STREET1")=VAPA(1)

S ADDRESS("STREET2")=VAPA(2)

S ADDRESS("CITY")=VAPA(4)

S ADDRESS("STATE")=\$P(VAPA(5),"^",2)

S ADDRESS("ZIP")=VAPA(6)

;

;Call an MPI utility to get the ICN.

S ICN=\$P(\$\$GETICN^MPIF001(DFN),"V")

;

;Now concatenate all the fields together that make up the PID segment.

S SEG="PID"\_FS_SEQ_FS_FS_ICN_CS_CS_CS\_"USVHA"\_SS_SS\_"0363"\_CS\_"NI"

S SEG=SEG_RS_SSN_CS_CS_CS\_"USSSA"\_SS_SS\_"0363"\_CS\_"SS"

S SEG=SEG_FS_FS_NAME("FAMILY")\_CS_NAME("GIVEN")\_CS_NAME("MIDDLE")\_CS_NAM

E("SUFFIX")

;

;DOB needs to be converted to HL7 format.

S DOB=\$\$HLDATE^HLFNC(DOB,"DT")

;

S SEG=SEG_FS_FS_DOB_FS_FS_FS_FS_ADDRESS("STREET1")\_CS_ADDRESS("STREET2")

\_CS_ADDRESS("CITY")\_CS_ADDRESS("STATE")\_CS_ADDRESS("ZIP")

;

Q

;

NK1(DFN,SEQ,SEG) --

;

;Description: Builds the NK1 segment for the primary emergency

; contact as in NK1^HLODEM1, but without using the HLO segment building

; APIs. A PIMS API is used to get the necesary data from PATIENT

; file (#2).

;

; The fields included in the segment are:

; NK1-1 Set ID: Set to the SEQ input parameter.

; NK1-2 Name

; NK1-3 Relationship

; NK1-4 Address

; NK1-5 Telephone Number

; NK1-7 Contact Roll

;

;Input:

; DFN (required) The IEN of the record in the PATIENT file (#2).

; SEQ (optional) Value for NK1-1.

;

;Output:

; SEG (pass-by-reference) The NK1 segment as a single line.

;

;Notes: 1) Assumes that the variables returned from INIT^HLFNC2 are

; defined, specifically, HL("FS") and HL("ECH").

; 2) This segment builder takes the shortcut of not replacing

; delimiters that occur within data fields with their

; escape sequences.

; 3) Also takes the shortcut of assuming the segment will fit

; on a single node.

;

;

N VA,VAOA,VAHOW,VAROOT,VATEST,NAME,ADDRESS,FS,CS

K SEG S SEG="" ;The segment should start off blank.

;

;Set the message delimiters for convenience.

S FS=HL("FS") ;Field Separator

S CS=\$E(HL("ECH"),1) ;Component Separator

;

;Get the patient's emergency contact using a PIMS utility.

S VAOA("A")=1

D OAD^VADPT

;

S NAME=VAOA(9) ;(name returned in non-standard (VHA) format)

;

;Standardize the format of the name using a Kernel utility.

;returns the subscripts "FAMILY","GIVEN","MIDDLE","SUBSCRIPT"

D STDNAME^XLFNAME(.NAME,"C")

;

;Move address components into ADDRESS.

S ADDRESS("STREET1")=VAOA(1)

S ADDRESS("STREET2")=VAOA(2)

S ADDRESS("CITY")=VAOA(4)

S ADDRESS("STATE")=\$P(VAOA(5),"^",2)

S ADDRESS("ZIP")=VAOA(6)

;

;Set the data into the segment.

;

;Set segment type,set id, and name.

S SEG="NK1"\_FS_1_FS_NAME("FAMILY")\_CS_NAME("GIVEN")\_CS_NAME("MIDDLE")\_CS

\_NAME("SUFFIX")

;

;Set the relationship into NK1-3, component 2.

S SEG=SEG_FS_CS_VAOA(10)

;

;Set the address into NK1-4.

S SEG=SEG_FS_ADDRESS("STREET1")\_CS_ADDRESS("STREET2")\_CS_ADDRESS("CITY")

\_CS_ADDRESS("STATE")\_CS_ADDRESS("ZIP")

;

;Set the phone number into NK1-5.

S SEG=SEG_FS_VAOA(8)

;

;Set the contact role into NK1-7.

S SEG=SEG_FS\_"EP"\_CS\_"EMERGENCY CONTACT PERSON"\_CS\_"0131"

Q

;

A08(DFN,ERROR) --

;Description: Builds an ADT~A08 message and queues it for transmission.

; The transmission is via HLO, but uses an event protocol setup and

; hardcoded segment builders. Included segments are the PID and NK1.

;

;Input:

; DFN (required) ien of a patient record in the PATIENT file (#2)

;Output:

; Function Return Value:

; On Success: Returns the ien of the messgage in the HLO Messages

; file (#778).

; On Failure: Returns 0.

; ERROR (optional, pass-by-refernce) On failure, returns an error

; message.

;

;Required Setup:

;\<\<Subscriber protocol (file \#101)\>\>

; \*\* The receiving application. \*\*

; NAME: HLO DEMO A08 CLIENT TYPE: subscriber

; RECEIVING APPLICATION: HLO DEMO RECEIVING APPLICATION

; LOGICAL LINK: HLODEMO

;

;\<\<Event protocol (file \#101)\>\>

; \*\* The sending application. \*\*

; NAME: HLO DEMO A08 SERVER TYPE: event driver

; CREATOR: MOORE,JIM SENDING APPLICATION: HLO DEMO SENDING AP

PLICATION

; TRANSACTION MESSAGE TYPE: ADT EVENT TYPE: A08

; ACCEPT ACK CODE: AL APPLICATION ACK TYPE: NE

; VERSION ID: 2.4

; SUBSCRIBERS: HLO DEMO A08 CLIENT

;

;\<\<HL7 Application Parameter (file \#771) for receiving application\>\>

; NAME: HLO DEMO RECEIVING APPLICATION

; ACTIVE/INACTIVE: ACTIVE

;

;\<\<HL7 Application Parameter - file \#771\>\>

; \*\* Represents the sending application. This will be automatically

; created if not already by HLO .\*\*

; NAME: HLO DEMO SENDING APPLICATION

; ACTIVE/INACTIVE: ACTIVE

;

;\<\<HL Logical Link, file 870\>\>

; \*\* The receiving facility. \*\*

; NODE: HLODEMO

; INSTITUTION: \<institution entered here\>

; LLP TYPE: TCP

; MAILMAN DOMAIN: \<use of DNS DOMAIN is preferred for new links\>

; DNS DOMAIN: \<TCP/IP domain name for DNS entered here\>

; TCP/IP ADDRESS: \<ip address entered here\>

; TCP/IP SERVICE TYPE: CLIENT (SENDER)

; TCP/IP PORT (OPTIMIZED): \<port \# entered here\>

;

N SEG,HLA,HL,RESULT,RSLT

D INIT^HLFNC2("HLO DEMO A08 SERVER",.HL)

K ERROR

D PID(DFN,1,.SEG)

S HLA("HLS",1)=SEG

D NK1(DFN,1,.SEG)

S HLA("HLS",2)=SEG

S RSLT=\$\$EN^HLOCNRT("HLO DEMO A08 SERVER","LM",,,.RESULT)

I 'RSLT S ERROR=\$P(RESULT,"^",4,5) Q 0

Q RESULT("IEN")

## HLODEM3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLODEM3 ;ALB/CJM-HL7 - Demonstration Code ;04/20/2009

;;1.6;HEALTH LEVEL SEVEN;\*\*146\*\*;Oct 13, 1995;Build 34

;Per VHA Directive 2004-038, this routine should not be modified.

;

;

A08(DFN,ERROR) --

;

;Description: Demonstrates the use of MOVESEG^HLOAPI to use hardcoded

; segment builders in conjunction with HLO. Builds an ADT~A08

; message and queues it for transmission. Included segments are the PID

; built with the HLO APIs and the NK1 segment built in the traditional

; hardcoded manner. The NK1 segment is moved into the HLO message by

; calling MOVESEG^HLOAPI. Protocols are not used.

;

;Input:

; DFN (required) The IEN of a patient record in the PATIENT file (#2).

;Output:

; Function Return Value:

; On Success: Returns the ien of the messgage in the HLO Messages

; file (#778).

; On Failure: Returns 0.

; ERROR (optional, pass-by-reference) On failure returns an error

; message.

;

;Required Setup: \<\< Same as for A08^HLODEM1. \>\>

;

;

N SEG,PARMS,WHOTO,HLA,HL

S PARMS("MESSAGE TYPE")="ADT"

S PARMS("EVENT")="AO8"

I '\$\$NEWMSG^HLOAPI(.PARMS,.MSG,.ERROR) Q 0

;

;Use the HLO segment building APIs to build the PID segment.

D PID^HLODEM1(DFN,1,.SEG)

;

;Segments build with the HLO APIs are moved into the message by calling

;\$\$ADSEG^HLOAPI.

I '\$\$ADDSEG^HLOAPI(.MSG,.SEG,.ERROR) Q 0

;

;Call the hardcoded NK1 segment builder.

;It requires that message delimiters be defined via HL("FS") and HL("ECH

").

S HL("FS")="\|"

S HL("ECH")="^~\\"

D NK1^HLODEM2(DFN,1,.SEG)

;

;Hardcoded segments are moved into the message by calling

;MOVESEG^HLOAPI.

I '\$\$MOVESEG^HLOAPI(.MSG,.SEG,.ERROR) Q 0

;

S PARMS("SENDING APPLICATION")="HLO DEMO SENDING APPLICATION"

S WHOTO("RECEIVING APPLICATION")="HLO DEMO RECEIVING APPLICATION"

S WHOTO("FACILITY LINK NAME")="HLODEMO"

Q \$\$SENDONE^HLOAPI1(.MSG,.PARMS,.WHOTO,.ERROR)

;

A082(DFN,ERROR) --

;

;Description: Demonstrates the use of the MOVEMSG^HLOAPI to use

;traditional style message builders in conjunction with HLO. Builds an

;ADT~A08 message and queues it for transmission. The message includes

;the PID and NK1 segments and is built in the traditional manner as an

;array of hardcoded segments. The message is then moved to HLO by

;calling MOVEMSG^HLOAPI. Protocols are not used.

;

;Input:

; DFN (required) ien of a patient record in the PATIENT file (#2)

;Output:

; Function Return Value:

; On Success: Returns the IEN of the messgage in the HLO Messages

; file (#778).

; On Failure: Returns 0/

; ERROR (optional, pass-by-reference) On failure returns a message.

;

;Required Setup: \<\< Same as for A08^HLODEM1. \>\>

;

N SEG,PARMS,WHOTO,HLA,HL

K ERROR

;

;Build the message in the tradional manner in the HLA("HS") array.

;It requires that message delimiters be defined via HL("FS") and

;HL("ECH").

S HL("FS")="\|"

S HL("ECH")="^~\\"

D PID^HLODEM2(DFN,1,.SEG)

S HLA("HLS",1)=SEG

D NK1^HLODEM2(DFN,1,.SEG)

S HLA("HLS",2)=SEG

;

;Now use the HLO APIs to send the message.

S PARMS("MESSAGE TYPE")="ADT"

S PARMS("EVENT")="AO8"

I '\$\$NEWMSG^HLOAPI(.PARMS,.MSG,.ERROR) Q 0

;

;Move the message built in HLA("HLS") into MSG.

D MOVEMSG^HLOAPI(.MSG,\$NA(HLA("HLS")))

;

S PARMS("SENDING APPLICATION")="HLO DEMO SENDING APPLICATION"

S WHOTO("RECEIVING APPLICATION")="HLO DEMO RECEIVING APPLICATION"

S WHOTO("FACILITY LINK NAME")="HLODEMO"

Q \$\$SENDONE^HLOAPI1(.MSG,.PARMS,.WHOTO,.ERROR)

## HLODEM4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLODEM4 ;ALB/CJM-HL7 - Demonstration Code ;04/20/2009

;;1.6;HEALTH LEVEL SEVEN;\*\*146\*\*;Oct 13, 1995;Build 34

;Per VHA Directive 2004-038, this routine should not be modified.

;

;\*\* NOTE: The following segment and message builders

;are presented for demonstration purposes and are NOT fully

;developed.

;

A08(DFN,ERROR) --

;

;Description: Builds an ADT~A08 message and queues it for transmission

; using a sequence queue to guarantee the order of delivery. Included

; segments are the PID and NK1.

;

;Input:

; DFN (required) The IEN of a patient record in the PATIENT file (#2)

;Output:

; Function Return Value:

; On Success: Returns the IEN of the messgage in the HLO MESSAGES

; file (#778).

; On Failure: Returns 0.

; ERROR (optional, pass-by-refernce) On failure returns a message.

;

;Required Setup:

;\<\<HLO APPLICATION PARAMETER - file \#779.2\>\>

; \*\* The sending application. \*\*

; APPLICATION NAME: HLO DEMO SENDING APPLICATION

; \*\* Enter the routine to call that will alert folks that the sequence

; queue is not moving. \*\*

; SEQUENCE EXCEPTION TAG: LATE

; SEQUENCE EXCEPTION ROUTINE: HLODEM4

; \*\* Enter how many minutes to wait for an application acknowledgment

; before generating an alert that something is wrong. \*\*

; SEQUENCING TIMEOUT: 5

; \*\* Enter the package that is sending the message. \*\*

; Package File Link: HL7 OPTIMIZED (HLO)

;

;\<\<HL Logical Link, file 870\>\>

; \*\* The receiving facility. \*\*

; NODE: HLODEMO

; INSTITUTION: \<The institution is entered here.\>

; LLP TYPE: TCP

; MAILMAN DOMAIN: \<The use of DNS DOMAIN is preferred for new links.\>

; DNS DOMAIN: \<The TCP/IP domain name for DNS is entered here.\>

; TCP/IP ADDRESS: \<The IP address is entered here.\>

; TCP/IP SERVICE TYPE: CLIENT (SENDER)

; TCP/IP PORT (OPTIMIZED): \<The port \# is entered here.\>

;

;

N SEG,PARMS,WHOTO

S PARMS("MESSAGE TYPE")="ADT"

S PARMS("EVENT")="AO8"

I '\$\$NEWMSG^HLOAPI(.PARMS,.MSG,.ERROR) Q 0

D PID^HLODEM1(DFN,1,.SEG)

I '\$\$ADDSEG^HLOAPI(.MSG,.SEG,.ERROR) Q 0

D NK1^HLODEM1(DFN,1,.SEG)

I '\$\$ADDSEG^HLOAPI(.MSG,.SEG,.ERROR) Q 0

;

;

S PARMS("SENDING APPLICATION")="HLO DEMO SENDING APPLICATION"

;

;\*\* These parameters are mandatory if using a sequence queue. \*\*

;The name of the sequence queue is arbitrary, but should be

;namespaced by the application.

S PARMS("ACCEPT ACK TYPE")="AL"

S PARMS("APP ACK TYPE")="AL"

S PARMS("SEQUENCE QUEUE")="HLO DEMO RECIEVING APPLICATION" ;named sequen

ce queue

;

S WHOTO("RECEIVING APPLICATION")="HLO DEMO RECEIVING APPLICATION"

S WHOTO("FACILITY LINK NAME")="HLODEMO"

Q \$\$SENDONE^HLOAPI1(.MSG,.PARMS,.WHOTO,.ERROR)

;

LATE ;The sending application secified this routine in the entry in the

;HLO APPLICATION REGISTRY file \#779.2 for HLO DEMO SENDING

;APPLICATION. (see above)

;

;Enter code that will alert the operations staff in the event that the

;sequence queue stalls. It could be an email message or other

;communication.

;

Q

## HLODEM5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLODEM5 ;ALB/CJM-HL7 - Demonstration Code ;04/20/2009

;;1.6;HEALTH LEVEL SEVEN;\*\*146\*\*;Oct 13, 1995;Build 34

;Per VHA Directive 2004-038, this routine should not be modified.

;

;

PARSEMSG --

;

;Description: This is the default message handler for the receiving

; application named HLO DEMO RECEIVING APPLICATION.

;

;Input:

; HLMSGIEN: At the point HLO calls this message handler, the variable

; HLMSGIEN is set to the IEN of the message in the HLO

; MESSAGE ADMINISTRATION file, \#779.2.

;

;Output: none

;

;Required Setup:

;\<\<HLO APPLICATION PARAMETER - file \#779.2\>\>

; \*\* The receiving application. \*\*

; APPLICATION NAME: HLO DEMO RECEIVING APPLICATION

; \*\* The application chose to specify a private queue for its incoming

; messages. If not specified, the queue 'DEFAULT' would be used. \*\*

; DEFAULT PRIVATE IN-QUEUE: HLO DEMO RECEIVING APPLICATION

; \*\*The application did not specify a message handler for the ADT~A08

; message, but did specify a default handler. \*\*

; DEFAULT ACTION TAG: PARSEMSG

; DEFAULT ACTION ROUTINE: HLODEM5

; \*\* The package that is receiving the message. \*\*

; Package File Link: HL7 OPTIMIZED (HLO)

;

N MSG,HDR

I '\$\$STARTMSG^HLOPRS(.MSG,HLMSGIEN,.HDR) D ERROR("lost message") QUIT

I 'MSG("BATCH"),HDR("MESSAGE TYPE")="ADT",HDR("EVENT")="A08" D

.D A08(.MSG)

.I HDR("APP ACK TYPE")="AL" ;(Need to respond with an application ack.)

E D ERROR("unexpected message type") QUIT

Q

;

PARSEA08 --

;

;Description:

; This is the ADT~A08 message handler for the receiving application

; named HLO DEMO RECEIVING APPLICATION.

;Input:

; At the point it is called, the variable HLMSGIEN is set to the IEN

; of the message in the HLO MESSAGE ADMINISTRATION file, \#779.2.

;

;Required Setup:

;\<\<HLO APPLICATION PARAMETER - file \#779.2\>\>

; \*\* The receiving application. \*\*

; APPLICATION NAME: HLO DEMO RECEIVING APPLICATION

; \*\*The application specified a specific message handler. \*\*

; HL7 MESSAGE TYPE: ADT

; HL7 EVENT: A08

; ACTION TAG: PARSEA08

; ACTION ROUTINE: HLODEM5

; \*\* The package that is receiving the message. \*\*

; Package File Link: HL7 OPTIMIZED (HLO)

;

;

N MSG,HDR,PID,NK1

I '\$\$STARTMSG^HLOPRS(.MSG,HLMSGIEN,.HDR) D ERROR("lost message") QUIT

;

;The message type and event are already known to be ADT~A08 based on the

;HLO Application Registry, but they could be checked by looking at

;MSG("MESSAGE TYPE") and MSG("EVENT")

;

;Parse the remaining segments of the message.

D A08(.MSG,.PID,.NK1)

;

;

;(At this point the message's data has been retrieved into the PID and

; NK1 arrays. Process it! Then return an application acknowledgment

; if requested.)

;

Q

;

A08(MSG,PID,NK1) --

;

;Description: \$\$STARTMSG^HLOPRS was already called. Parse the remaining

; segments.

;Input:

; MSG (required, pass-by-reference) The message array returned by

; callng \$\$STARTMSG^HLOPRS.

;Output:

; PID (pass-by-reference) The fields from the PID segment are returned

; in this array.

; NK1 (pass-by-reference) The fields parsed from the NK1 segment are

; returned in this array.

;

N SEG

F Q:'\$\$NEXTSEG^HLOPRS(.MSG,.SEG) D

.;Base the parsing on the type of segment.

.;SEG(0) is equivalent to SEG("SEGMENT TYPE")

.I SEG("SEGMENT TYPE")="PID" D PID(.SEG,.PID) Q

.I SEG(0)="NK1" D PID(.SEG,.PID) Q

.;If not a PID or NK1 segment, disregard it.

;

Q

;

PID(SEG,PID) --

;

;Description:

; Put the needed data into the PID array.

;Input:

; SEG (pass-by-reference) The parsed segment.

;Output:

; NK1 (pass-by-reference) Will return the specific data needed by the a

pplication.

;

N I,VALUE

K PID

;Get the patient identifiers from the repeating field.

F I=1:1 S VALUE=\$\$GET^HLOPRS(.SEG,3,4,1,I) Q:VALUE="" D

.I VALUE="USVHA" S PID("ICN")=\$\$GET^HLOPRS(.SEG,3,1,1,I)

.I VALUE="USSSA" S PID("SSN")=\$\$GET^HLOPRS(.SEG,3,1,1,I)

;

;Get the patient name.

D GETXPN^HLOPRS2(.SEG,.VALUE,2)

M PID("NAME")=VALUE

;

;Get the patient DOB.

D GETDT^HLOPRS2(.SEG,.VALUE,7)

S PID("DOB")=VALUE

;

;Get the patient address.

D GETAD^HLOPRS2(.SEG,.VALUE,11)

M PID("ADDRESS")=VALUE

;

Q

NK1(SEG,NK1) --

;

;Description: Returns the needed data from the NK1 segment.

;Input:

; SEG (pass-by-reference) The parsed segment.

;Output:

; NK1 (pass-by-reference) Will return the specific data needed by the

; application.

N VALUE

K NK1

;

;Get the contact's name.

D GETXPN^HLOPRS2(.SEG,.VALUE,2)

M NK1("NAME")=VALUE

;

;Get the contact's relationship.

S NK1("RELATIONSHIP")=\$\$GET^HLOPRS(.SEG,3,2)

;

;Get the contact's address.

D GETAD^HLOPRS2(.SEG,.VALUE,4)

M NK1("ADDRESS")=VALUE

;

;Get the contact's phone number.

S NK1("PHONE")=\$\$GET^HLOPRS(.SEG,5)

;

;get contact's role the contact

S NK1("ROLE")=\$\$GET^HLOPRS(.SEG,7,2)

Q

;

ERROR(ERROR) --

;report error

;{needs to be coded}

Q

## HLODEM6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLODEM6 ;ALB/CJM-HL7 - Demonstration Code ;04/20/2009

;;1.6;HEALTH LEVEL SEVEN;\*\*146\*\*;Oct 13, 1995;Build 34

;Per VHA Directive 2004-038, this routine should not be modified.

;

;

PARSEA08 --

;

;Description: This is the ADT~A08 message handler for the receiving

; application named HLO DEMO RECEIVING APPLICATION. This example uses

; hardcoded segment parsers.

;

;Input:

; At the point it is called, the variable HLMSGIEN is set to the IEN

; of the message in the HLO MESSAGE ADMINISTRATION file, \#779.2.

;

;Required Setup:

;\<\<HLO APPLICATION PARAMETER - file \#779.2\>\>

; \*\* The receiving application. \*\*

; APPLICATION NAME: HLO DEMO RECEIVING APPLICATION

; \*\*The application specified a specific message handler. \*\*

; HL7 MESSAGE TYPE: ADT

; HL7 EVENT: A08

; ACTION TAG: PARSEA08

; ACTION ROUTINE: HLODEM6

; \*\* The package that is receiving the message. \*\*

; Package File Link: HL7 OPTIMIZED (HLO)

;

;

N MSG,HDR,SEG,PID,NK1

I '\$\$STARTMSG^HLOPRS(.MSG,HLMSGIEN,.HDR) D ERROR("lost message") QUIT

;

;The message type and event are already known because of how the

;receving application was setup in the HLO Application Registry.

;

;Set up the delimiters in HL array required by the segment parsers.

N HL

S HL("FS")=HDR("FIELD SEPARATOR")

S HL("ECH")=HDR("ENCODING CHARACTERS")

;

;loop through the segments

F Q:'\$\$HLNEXT^HLOMSG(.MSG,.SEG) D

.I \$E(SEG(1),1,3)="PID" D PID(SEG(1),.PID)

.I \$E(SEG(1),1,3)="NK1" D NK1(SEG(1),.NK1)

.;If not of these segment types, ignore it.

;

;(At this point the message's data has been retrieved into the PID and

; NK1 arrays. Process it! Then return an application acknowledgment

; if requested - not shown here.)

Q

;

PID(SEG,PID) --

;

;Description: A hardcoded parser for the PID segment.

;Input:

; SEG The un-parsed segment.

; HL("FS"),HL("ECH") should be defined.(message delimiters)

;Output:

; NK1 (pass-by-reference) Will return the specific data needed by the a

pplication.

;

; \*\*WARNING\*\*: The following code makes two WRONG assumptions:

; 1) That the data does not include escape sequences for delimiters.

; 2) That the entire segment is contained on a single node.

;

N I,VALUE,FS,CS,RS,SS

K PID

;

;For convenience, set the essage delimiters into variables.

S FS=HL("FS") ;field separator

S CS=\$E(HL("ECH"),1) ;component separator

S RS=\$E(HL("ECH"),2) ;repetition separator

S SS=\$E(HL("ECH"),4) ;subcomponent separator

;

;Get the patient identifiers from the repeating field.

F I=1:1 S VALUE=\$P(\$P(\$P(\$P(SEG,FS,4),RS,I),CS,4),SS,1) Q:VALUE="" D

.I VALUE="USVHA" S PID("ICN")=\$P(\$P(\$P(\$P(SEG,FS,4),RS,I),CS,1),SS,1)

.I VALUE="USSSA" S PID("SSN")=\$P(\$P(\$P(\$P(SEG,FS,4),RS,I),CS,1),SS,1)

;

;Get the patient name.

S PID("NAME","FAMILY")=\$P(\$P(\$P(\$P(SEG,FS,3),RS,1),CS,1),SS,1)

S PID("NAME","GIVEN")=\$P(\$P(\$P(\$P(SEG,FS,3),RS,1),CS,2),SS,1)

S PID("NAME","SECOND")=\$P(\$P(\$P(\$P(SEG,FS,3),RS,1),CS,3),SS,1)

S PID("NAME","SUFFIX")=\$P(\$P(\$P(\$P(SEG,FS,3),RS,1),CS,4),SS,1)

S PID("NAME","PREFIX")=\$P(\$P(\$P(\$P(SEG,FS,3),RS,1),CS,5),SS,1)

S PID("NAME","DEGREE")=\$P(\$P(\$P(\$P(SEG,FS,3),RS,1),CS,6),SS,1)

;

;Get the patient DOB.

S PID("DOB")=\$\$HL7TFM^XLFDT(\$P(\$P(\$P(\$P(SEG,FS,8),RS,1),CS,1),SS,1))

;

;Get the patient address.

S PID("ADDRESS","STREET1")=\$P(\$P(\$P(\$P(SEG,FS,12),RS,1),CS,1),SS,1)

S PID("ADDRESS","STREET2")=\$P(\$P(\$P(\$P(SEG,FS,12),RS,1),CS,2),SS,1)

S PID("ADDRESS","CITY")=\$P(\$P(\$P(\$P(SEG,FS,12),RS,1),CS,3),SS,1)

S PID("ADDRESS","STATE")=\$P(\$P(\$P(\$P(SEG,FS,12),RS,1),CS,4),SS,1)

S PID("ADDRESS","ZIP")=\$P(\$P(\$P(\$P(SEG,FS,12),RS,1),CS,5),SS,1)

S PID("ADDRESS","COUNTRY")=\$P(\$P(\$P(\$P(SEG,FS,12),RS,1),CS,6),SS,1)

S PID("ADDRESS","TYPE")=\$P(\$P(\$P(\$P(SEG,FS,12),RS,1),CS,7),SS,1)

S PID("ADDRESS","OTHER")=\$P(\$P(\$P(\$P(SEG,FS,12),RS,1),CS,8),SS,1)

;

Q

;

NK1(SEG,NK1) --

;

;Description: A hardcoded parser for the NK1 segment.

;Input:

; SEG -the segment

; HL("FS"),HL("ECH") should be defined.(message delimiters)

;Output:

; NK1 (pass-by-reference) Will return the specific data needed by the

; a pplication.

;

; \*\*WARNING\*\*: The following code makes two WRONG assumptions:

; 1) That the data does not include escape sequences for delimiters.

; 2) That the entire segment is contained on a single node.

;

N VALUE,FS,CS,RS,SS

K NK1

;

;For convenience, set the essage delimiters into variables.

S FS=HL("FS") ;field separator

S CS=\$E(HL("ECH"),1) ;component separator

S RS=\$E(HL("ECH"),2) ;repetition separator

S SS=\$E(HL("ECH"),4) ;subcomponent separator

;

;Get contact's name.

S NK1("NAME","FAMILY")=\$P(\$P(\$P(\$P(SEG,FS,3),RS,1),CS,1),SS,1)

S NK1("NAME","GIVEN")=\$P(\$P(\$P(\$P(SEG,FS,3),RS,1),CS,2),SS,1)

S NK1("NAME","SECOND")=\$P(\$P(\$P(\$P(SEG,FS,3),RS,1),CS,3),SS,1)

S NK1("NAME","SUFFIX")=\$P(\$P(\$P(\$P(SEG,FS,3),RS,1),CS,4),SS,1)

S NK1("NAME","PREFIX")=\$P(\$P(\$P(\$P(SEG,FS,3),RS,1),CS,5),SS,1)

S NK1("NAME","DEGREE")=\$P(\$P(\$P(\$P(SEG,FS,3),RS,1),CS,6),SS,1)

;

;Get contact's relationship.

S NK1("RELATIONSHIP")=\$P(\$P(\$P(\$P(SEG,FS,4),RS,1),CS,2),SS,1)

;

;Get contact's address.

S NK1("ADDRESS","STREET1")=\$P(\$P(\$P(\$P(SEG,FS,5),RS,1),CS,1),SS,1)

S NK1("ADDRESS","STREET2")=\$P(\$P(\$P(\$P(SEG,FS,5),RS,1),CS,2),SS,1)

S NK1("ADDRESS","CITY")=\$P(\$P(\$P(\$P(SEG,FS,5),RS,1),CS,3),SS,1)

S NK1("ADDRESS","STATE")=\$P(\$P(\$P(\$P(SEG,FS,5),RS,1),CS,4),SS,1)

S NK1("ADDRESS","ZIP")=\$P(\$P(\$P(\$P(SEG,FS,5),RS,1),CS,5),SS,1)

S NK1("ADDRESS","COUNTRY")=\$P(\$P(\$P(\$P(SEG,FS,5),RS,1),CS,6),SS,1)

S NK1("ADDRESS","TYPE")=\$P(\$P(\$P(\$P(SEG,FS,5),RS,1),CS,7),SS,1)

S NK1("ADDRESS","OTHER")=\$P(\$P(\$P(\$P(SEG,FS,5),RS,1),CS,8),SS,1)

;

;Get contact's phone.

S NK1("PHONE")=\$P(\$P(\$P(\$P(SEG,FS,6),RS,1),CS,2),SS,1)

;

;Get contact's role the contact.

S NK1("ROLE")=\$P(\$P(\$P(\$P(SEG,FS,8),RS,1),CS,2),SS,1)

Q

;

ERROR(ERROR) --

;report error

;(Needs to be coded.)

Q

## HLODEM7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLODEM7 ;ALB/CJM-HL7 - Demonstration Code ;04/20/2009

;;1.6;HEALTH LEVEL SEVEN;\*\*144\*\*;Oct 13, 1995;Build 34

;Per VHA Directive 2004-038, this routine should not be modified.

;

;

BATCH ;

;Description: This is the batch message handler for the receiving

; application named HLO DEMO RECEIVING APPLICATION. It parses

; the ADT~A08 messages created in BATCHA08^HLODEM1, though a batch of

; messages is allowed to contain different types of messages.

;

;Input:

; At the point it is called, the variable HLMSGIEN should be set to

; the IEN of the message in the HLO MESSAGE ADMINISTRATION file,

; \#779.2.

;Output: none

;

;Required Setup:

;\<\<HLO APPLICATION PARAMETER - file \#779.2\>\>

; \*\* The receiving application. \*\*

; APPLICATION NAME: HLO DEMO RECEIVING APPLCATION

; \*\*The application specified a batch message handler. \*\*

; BATCH ACTION TAG: BATCH

; BATCH ACTION ROUTINE: HLODEM7

; \*\* The package that is receiving the message. \*\*

; Package File Link: HL7 OPTIMIZED (HLO)

;

;

;Create the variable workspace.

;

N MSG,BHS,MSH

;

;Start the parsing.

;

I '\$\$STARTMSG^HLOPRS(.MSG,HLMSGIEN,.BHS) D ERROR("lost message") QUIT

;

;The application mayverify that this is indeed a batch of messages by

;checking MSG("BATCH"). The check is not necessary if the

;receiving application setup is correct.

;

I 'MSG("BATCH") D ERROR("not a batch message") QUIT

;

;Step through each message in the batch and process it.

;

F Q:'\$\$NEXTMSG^HLOPRS(.MSG,.MSH) D

.;

.;If it is not known in advance what type of messages the batch

.;contains then determine that from the message header.

.I MSH("MESSGE TYPE")="ADT",MSH("EVENT")="A08" D

..;

..N PID,NK1

..;

..;Step through the segments of the message.

..F Q:'\$\$NEXTSEG^HLOPRS(.MSG,.SEG) D

...;

... ;Look at the segment type, then get its data.

...I SEG("SEGMENT TYPE")="PID" D PID^HLODEM5(.SEG,.PID)

...I SEG("SEGMENT TYPE")="NK1" D NK1^HLODEM5(.SEG,.NK1)

..;

..;(All the data has been parsed from the message. Now process it -

..; not shown.)

Q

;

ERROR(ERROR) --

;reports an exception

;(Needs to be coded.)

Q

## HLODEM8

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLODEM8 ;ALB/CJM-HL7 - Demonstration Code ;04/20/2009

;;1.6;HEALTH LEVEL SEVEN;\*\*144\*\*;Oct 13, 1995;Build 34

;Per VHA Directive 2004-038, this routine should not be modified.

;

;

APPACK ;Description:

; This is for receiving application acknowledgments. In

; this example, it just reports errors to support staff and sets

; the purge date of the original message to one month in the future.

;

;Input:

; At the point it is called, the variable HLMSGIEN is set to the IEN

; of the message in the HLO MESSAGE ADMINISTRATION file, \#779.2.

;

;Required Setup:

; If this routine was designated as the callback routine when

; the original message was generated then no additional setup is

; needed. An alternative to using callbacks is to set up the message

; type & event for the acknowledgment in the HLO Application Registry.

;

N MSG,HDR,SEG

;

;start parsing the acknowledgment.

I \$\$STARTMSG^HLOPRS(.MSG,HLMSGIEN,.HDR) D

.;step through the segments looking for the MSA segment.

.F Q:'\$\$NEXTSEG^HLOPRS(.MSG,.SEG) D

..I SEG("SEGMENT TYPE")="MSA" D

...;Check MSA-1 acknowledgment code. If not AA it is an error.

...I \$\$GET^HLOPRS(.SEG,1)'="AA" D

....;Reset the purge date of the original message to 1 month in future.

....N TIME S TIME=\$\$FMADD^XLFDT(\$\$NOW^XLFDT,30)

....I '\$\$SETPURGE^HLOAPI3(MSG("ACK TO IEN"),TIME)

....;Send the staff an alert.

....;MSA-2 is the message id of the original message

....;MSA-3 is the error text

....D ALERT(\$\$GET^HLOPRS(.SEG,2),\$\$GET^HLOPRS(.SEG,3))

Q

;

ALERT(MSGID,ERROR) --

;alert support staff to the error

;(Needs to be coded.)

Q

## HLODEM9

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLODEM9 ;ALB/CJM-HL7 - Demonstration Code ;04/20/2009

;;1.6;HEALTH LEVEL SEVEN;\*\*144\*\*;Oct 13, 1995;Build 34

;Per VHA Directive 2004-038, this routine should not be modified.

;

;

PARSEA08 --

;

;Description:

; This is the ADT~A08 message handler for the receiving application

; named HLO DEMO CLIENT. It is the same as PARSEA08^HLODEM5 except

; that it has been enhanced to return an application acknowledgment.

;

;Input:

; At the point this is called, the variable HLMSGIEN is set to the IEN

; of the message in the HLO MESSAGE ADMINISTRATION file, \#779.2.

;

;Required Setup:

;\<\<HLO APPLICATION PARAMETER - file \#779.2\>\>

; \*\* The receiving application. \*\*

; APPLICATION NAME: HLO DEMO CLIENT

; \*\*The application specified a specific message handler. \*\*

; HL7 MESSAGE TYPE: ADT

; HL7 EVENT: A08

; ACTION TAG: PARSEA08

; ACTION ROUTINE: HLODEM5

; \*\* the package that is receiving the message. \*\*

; Package File Link: HL7 OPTIMIZED (HLO)

;

;

N MSG,HDR,PID,NK1

I '\$\$STARTMSG^HLOPRS(.MSG,HLMSGIEN,.HDR) D ERROR("lost message") QUIT

;

;The message type and event are already known to be ADT~A08 based

;on the setup. Parse the PID and NK1 segments.

D A08^HLODEM5(.MSG,.PID,.NK1)

;

;Was an application acknowlegment requested?

I HDR("APP ACK TYPE")="AL" D

.;

.;

.;If the PID had a social security number return AA.

.I \$L(PID("SSN"))=9

Q

;

ERROR(ERROR) --

;report error

;(Needs to be coded.)

Q

## HLODEM10

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLODEM10 --

;ALB/CJM-HL7 - Demonstration Code ;04/20/2009

;;1.6;HEALTH LEVEL SEVEN;\*\*144\*\*;Oct 13, 1995;Build 34

;Per VHA Directive 2004-038, this routine should not be modified.

;

;

;

PARSEA08 --

;

;Description:

; This is the ADT~A08 message handler for the receiving application

; named HLO DEMO RECEIVING APPLICATION. It is identical to

; PARSEA08^HLODEM5, except that it additionally returns an applicaiton

; acknowledgment.

;

;Input:

; At the point it is called, the variable HLMSGIEN is set to the IEN

; of the message in the HLO MESSAGE ADMINISTRATION file, \#779.2.

;

;Output: none

;

;Required Setup: see PARSEA08^HLODEM5

;

N MSG,MSH,PID,NK1

I '\$\$STARTMSG^HLOPRS(.MSG,HLMSGIEN,.MSH) D ERROR("lost message") Q

;

;Parse the remaining segments of the message.

D A08^HLODEM5(.MSG,.PID,.NK1)

;

;

;{At this point the message's data has been retrieved into the PID and

; NK1 arrays. Process it - not shown!}

;

;If an application acknowledgment was requested, then return one.

I MSH("APP ACK TYPE")="AL" D

.N ACK,PARMS

.;return AA if the PID had a social security number,or AE=error if not

.I \$L(\$G(PID("SSN")))=9 D

..S PARMS("ACK CODE")="AA"

.E D

..S PARMS("ACK CODE")="AE",PARMS("ERROR MESSAGE")="MISSING SSN"

.I '\$\$ACK^HLOAPI2(.MSG,.PARMS,.ACK,.ERROR) D ERROR("\$\$ACK^HLOAPI2 FAILED

") Q

.;

.;There are no additional segments to add to the acknowledgment, so

.;send it.

.I '\$\$SENDACK^HLOAPI2(.ACK,.ERROR) D ERROR(ERROR)

;

Q

;

BATCH ;Description:

; This is an extension of the batch message handler in BATCH^HLODEM7.

; In addition to parsing a batch of messages as in BATCH^HLODEM7, it

; also returns a batch of application acknowledgments.

;

;Input:

; At the point it is called, the variable HLMSGIEN should be set to

; the IEN of the message in the HLO MESSAGE ADMINISTRATION file,

; \#779.2.

;

;Output: none

;

;Required Setup: see BATCH^HLODEM7

;

N MSG,BHS,MSH,ACK

;

;Start the parsing.

I '\$\$STARTMSG^HLOPRS(.MSG,HLMSGIEN,.BHS) D ERROR("lost message") QUIT

;

;Is a return batch of application acknowledgments requested?

;If so, start the return batch.

I BHS("APP ACK TYPE")="AL",'\$\$BATCHACK^HLOAPI3(.MSG,,.ACK,.ERROR) D ERRO

R(ERROR)

;

;Step through each message in the batch and process it.

F Q:'\$\$NEXTMSG^HLOPRS(.MSG,.MSH) D

.;

.;(If it is not known in advance what type of messages the batch

.;contains then determine that from the message header. But here

.; it is assumed to be an ADT~A08.)

.

.;Parse the remaining segments of the message.

.D A08^HLODEM5(.MSG,.PID,.NK1)

.;

.;(All the data has been parsed from the message. Now process it! Not

.; shown.)

.;

.;Might check the individual message to determine if an acknowledgment

.;was requested. Whether or not this is necessary depends on the

.;negotiated interface specification, but usually it is NOT necessary.

.I MSH("APP ACK TYPE")="AL" D

..N PARMS

..;return AA if the PID had a social security number,or AE=error if not

..I \$L(\$G(PID("SSN")))=9 D

...S PARMS("ACK CODE")="AA"

..E D

...S PARMS("ACK CODE")="AE",PARMS("ERROR MESSAGE")="MISSING SSN"

..;

..;Add a message to the return batch.

..I '\$\$ADDACK^HLOAPI3(.ACK,.PARMS,.ERROR) D ERROR(.ERROR)

.;

.;There are no additional messages to add to the return batch, so

.;send it.

.I '\$\$SENDACK^HLOAPI2(.ACK,.ERROR) D ERROR(ERROR)

Q

;

ERROR(ERROR) --

;report error

;(Needs to be coded.)

Q

# Quick Overview of the HLO User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## HLO Main Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the top-level menu for HLO:

SM HLO SYSTEM MONITOR

MV HLO MESSAGE VIEWER

STAT HLO MESSAGE STATISTICS

ES HLO ERROR STATISTICS

DM HLO DEVELOPER MENU ...

SP EDIT HLO SYSTEM PARAMETERS

Select HL7 (Optimized) MAIN MENU Option:

- The HLO System Monitor is used for controlling and monitoring the operation of HLO. It is described in more detail below.
- The HLO Message Viewer is the main tool for viewing messages. Its features include:
  - The ability to search for messages by date range, application, and message type.
  - Reporting of message errors by date range and application.
  - It displays messages, using the message ID from the message header as the lookup key. It also shows all the administrative data related to the message, such as the status and date/time transmitted. It also links messages to their application acknowledgments and visa versa. Commit acknowledgments are stored with the original message and can only be accessed through the message id of the original message.
- The HLO Message Statistics option provides reporting capability for counts of messages sent and received over any time period. Monthly, daily, and hourly statistics are maintained.
- The HLO Error Statistics option provides reporting capability for counts of message errors over any time period. Monthly, daily, and hourly statistics are maintained.
- The HLO Developer Menu contains options that are needed to develop messaging applications with HLO. They have been described elsewhere in this manual.
- The Edit HLO System Parameters option is used by system managers to configure their system. It contains parameters used by HLO for sending, receiving, and purging messages.

## HLO System Monitor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLO SYSTEM MONITOR Apr 20, 2009@10:01:33 Page: 1 of 1

Brief Operational Overview

SYSTEM STATUS: RUNNING

PROCESS MANAGER: RUNNING

STANDARD LISTENER: OPERATIONAL

TASKMAN: RUNNING

DOWN LINKS: ZZRH OEX:5031

CLIENT LINK PROCESSES: 0

IN-FILER PROCESSES: 0

MESSAGES PENDING ON OUT QUEUES: 504 ON SEQUENCE QUEUES: 3

STOPPED OUTGOING QUEUES:

MESSAGES PENDING ON APPLICATIONS: 1

STOPPED INCOMING QUEUES:

FILE 777 RECORD COUNT: 977 --\> as of Apr 19, 2009@23:57:07

FILE 778 RECORD COUNT: 1011 --\> as of Apr 19, 2009@23:57:07

![](hl7-hl-1-6-hlo-vms-developer-manual/002.png)MESSAGES SENT TODAY: 1

![](hl7-hl-1-6-hlo-vms-developer-manual/003.png)MESSAGES RECEIVED TODAY: 0

MESSAGE ERRORS TODAY: 4

Brief System Status \>\>\>

LP LIST PROCESSES BS BRIEF STATUS TL TEST TCP LINK

DL DOWN LINKS ML MONITOR LINK <span class="mark">RT RealTime MODE</span>

<span class="mark">OQ OUTGOING QUEUES STOP HLO SEQ SEQUENCE QUEUES</span>

<span class="mark">IQ INCOMING QUEUES START HLO SQ START/STOP QUEUE</span>

Select Action:Quit//

Shows whether HLO is running.

> Shows whether the HLO Process Manager is running. The HLO Process Manager is a process that starts and stops other HLO processes as needed, and can respond automatically to changes in the workload. The HLO Process Manager should always be running while HLO is running. If it stops unexpectedly, HLO may continue to run, but no new HLO processes will be started.

> Shows whether the HLO listener is running. In VHA the standard listener is a VMS TCPIP Service running on a standard port.

> Shows whether Taskman is running.

> Shows a list of the links that have recently been failing.

> Shows a count of the number of client proesses that are running. Client processes are responsible for transmitting the messages that are pending on the outgoing queues.

> Shows a count of the in-filer processes that are running. The in-filer processes are responsible for passing newly received messages to the receiving application.

> Shows a count of the messages pending to be transmitted.

> Shows a count of the messages pending on sequence queues. Sequence queues are used to guarantee the order of message delivery.

> Shows a list of outgoing queues that have been stopped via the START/STOP QUEUE action.

> Shows a count of newly received messages that are still waiting to be passed to the application by the in-filer process.

> Shows a list of the incoming queues that have been stopped via the START/STOP QUEUE action.

> Shows the most recent count of the records in the HLO MESSAGE BODY file (#777). Since FileMan is not used to add or delete records to this file, the 0 node of the file is not updated with a count of the records each time a record is added or deleted. Instead, there is a special option that runs several times during the day that counts the records.

> Shows the most recent count of the records in the HLO MESSAGES file (#778). Since FileMan is not used to add or delete records to this file, the 0 node of the file is not updated with a count of the records each time a record is added or deleted. Instead, there is a special option that runs several times during the day that counts the records.

> Shows the count of all messages sent today. Commit acknowledgments aren’t included in the count.

> Shows a count of the messages received today. Commit acknowledgments aren’t included n the count.

> Shows a count of the messages whose status has been set to ERROR today.

> This action will show a list of the HLO processes that are currently running or scheduled to run.

> This action will display a screen that lists the links that recently have been failing. It has actions for manually starting or stopping specific links.

> This action will display a screen that lists all the outgoing queues that have messages pending on them. It has actions for deleting a queue and for deleting messages from queues.

> This action will display a screen that lists all the incoming queues that have messages pending on them. It has actions for deleting a queue and for deleting messages from queues.

> This action takes you to the screen that provides an overview of the current status of the HLO system. It is the same screen that is shown above.

> This screen will show a near real-time display of the count of messages pending for transmission over a specific link.

> This action is used to turn HLO off. It may take several minutes for all the processes to stop.

> This action is used to turn HLO back on. It may take several minutes for all the HLO processes to be started via Taskman.

> This action is used to test whether there is connectivity via TCP/IP over a specific link.

> This action changes how the screen is displayed. In real-time mode the screen is updated every few seconds.

> This action will display a screen that lists counts of messages pending on sequence queues. It has actions for deleting sequence queues and for advancing sequence queues.

> This action is used to manually start or stop specific named queues. Stopping a named queue will cause all queues with that name to suspend transmission of its messages, regardless of the link over which the transmission is to take place.

# Troubleshooting for the Developer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLO provides two tools that are specifically for troubleshooting interface problems - the client trace and server trace tools described below. In addition, there are several general tools that may be useful when troubleshooting problems, including:

- The HLO SYSTEM MONITOR:
  - Has an action to test the connectivity to a remote link.
  - Provides the status of the HLO Client/Server engine.
  - Provides the status of incoming queues, outgoing queues, and sequence queues.
- The HLO MESSAGE VIEWER:
  - Provides message search capability.
  - Provides the ability to view messages and related administrative information.
  - Provides a visual parser for interpreting the content of messages.

## The Client Trace Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The routine ^HLOTRACE is a utility for running the HLO client in the foreground. It asks the user to select a remote server to connect to, and at that point it attempts to transmit pending messages to that server. As it executes, it writes a stream of messages to the screen detailing each step of the process as it occurs.

To use the tool, there must be pending messages waiting for transmission. Furthermore, the tool has to be able to obtain a lock on the queue, so within the HLO System Monitor it is necessary to either:

- Shutdown the link for those messages by using the SHUTDOWN LINK action on the DOWN LINKS screen.
- Shutdown the specific queue by using the START/STOP QUEUE action.
- Shutdown the entire HLO system by using the STOP HLO action.

Example: Using the client trace tool.

First the ^HLOTRACE routine must be obtained and installed on the system. Then shut down either the specific queue, the link, or the entire HLO system. Then at the M prompt enter:

NXT\>D ^HLOTRACE

Select a TCP link: HLODEMO Enter the client link.

What is the name of the queue: DEFAULT// Verify the queue.

Send how many at a time: (1-100): 1// Enter number to trace.

Launching the client process

Trying to connect...

Connected!

Looking for the next message to transmit...

Message IEN=1461582 next on queue, do you want to trace its transmission? YES//

Time: 3090407.085809 Beginning to transmit message....

Time: 3090407.085809 Writing header segment...

MSH\|^~\\\|HLO DEMO SENDING APPLICATION\|998^HL7.REDACTED5011^DNS\|HLO

DEMO RECEIVING APPLICATION\|612BY^TEST.DOMAIN:5031^DNS\|20090407075126-0800\|\|ADT^

AO8^\|998 1461582\|T^\|2.4\|\|\|AL\|NE\|

Time: 3090407.085809 Completed!

Time: 3090407.085809 Writing next segment...

PID\|1\|\|3333^^^USVHA&&0363^NI~517509835^^^USSSA&&0363^SS\|\|HOFFMAN^JOHN^^^^\|\|19470

605\|\|\|\|4876 25TH AVE.^^SAN FRANCISCO^CALIFORNIA^94111^^^

Time: 3090407.085809 Completed!

Time: 3090407.085809 Writing next segment...

NK1\|1\|DOE^JOHN^^^^\|^\|^^^^^^^\|\|\|EP^EMERGENCY CONTACT PERSON^0131

Time: 3090407.085809 Completed!

Time: 3090407.085809 Writing message terminators and flushing buffer...

Time: 3090407.085809 Completed!

Time: 3090407.085809 Message transmitted!

Time: 3090407.085809 Beginning to read commit acknowledgment....

Time: 3090407.085809 Reading header...

Time: 3090407.085809

MSH\|^~\\\|HLO DEMO RECEIVING APPLICATION\|050^OEX.REDACTED^DNS\|HLO DE

MO SENDING APPLICATION\|998^HL7.REDACTED:5011^DNS\|20090407085809-070

0\|\|ACK\|050 100000294967\|T\|2.4\|\|\|NE\|NE

Time: 3090407.085809 Completed!

Time: 3090407.085809 Reading next segment...

Time: 3090407.085809

MSA\|CR\|998 1461582\|RECEIVING APPLICATION NOT DEFINED\|

Time: 3090407.085809 Completed!

Time: 3090407.085809 Reading next segment...

Time: 3090407.085809 No more segments!

Time: 3090407.085809 Commit acknowledgment received!

Looking for the next message to transmit...

No more messages pending on that queue!

Cleaning up....

DONE!

## The Server Trace Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The routine ^HLOSTRAC is a utility that runs the HLO server in the foreground. It asks the user to select a port to receive messages on, and then will attempt to read messages through that port. As the trace tool executes, it writes a stream of messages to the screen detailing each step of the process as it occurs.

The server trace tool must be able to open the port. If a server is already running on that port, that server must be stopped before using the server trace tool. If the server is a VMS TCPIP Service, the service must be stopped by using the VMS TCPIP ‘DISABLE SERVICE’ command.

Example: Using the server trace tool.

NXT\>D ^HLOSTRAC

What port do you want to listen on while in server trace mode?

The port must be free. If a server already has it opened then the

server needs to be stopped before starting in server trace mode.

PORT: (1-65535): 5011// 6666

Starting the server, hit the CTRL-C key to stop the server...

Time: 3090810.121211 Opening the port...

Time: 3090810.121211 Waiting for remote client to connect...

Time: 3090810.121442 Remote client connected...

Beginning to read next message...

Time: 3090810.121442 Reading message header...

Time: 3090810.121442

MSH\|^~\\\|MYTEST\|050^OEX.REDACTED^DNS\|MY_silly_TEST\|^NXT.FO-OA\|

Time: 3090810.121442 Completed!

Time: 3090810.121442 Parsing the message header...

Time: 3090810.121442 Checking if duplicate message...

Time: 3090810.121442 Reading next segment...

Time: 3090810.121442

MSA\|\|1

Time: 3090810.121442 Completed!

Time: 3090810.121442 Reading next segment...

Time: 3090810.121442 No more segments!

Beginning to write the commit acknowledgment...

Time: 3090810.121442 Writing header segment...

MSH\|^~\\\|MY_silly_TEST\|998^NXT.REDACTED^DNS\|MYTEST\|050^OEX.FO-OAKLE

Time: 3090810.121442 Completed!

Time: 3090810.121442 Writing next segment...

MSA\|CR\|050 922237\|RECEIVING APPLICATION NOT DEFINED\|

Time: 3090810.121442 Completed!

Time: 3090810.121442 Writing message terminators and flushing buffer...

Time: 3090810.121442 Completed!

Do you want to trace another message transmission? NO//

Time: 3090810.121511 Error encountered, \$ECODE=ZZHLOSTOP

TCP connection was dropped

Time: 3090810.121512 Closing the port...

NXT\>