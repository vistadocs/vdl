---
title: "LA*5.2*53/LR*5.2*254 Laboratory: Universal Interface HP CareVue Interface Specifications Document"
doc_type: INT
doc_label: Interface Specification
doc_layer: patch
doc_subject: 
app_code: LA
app_name: "Laboratory: Universal Interface"
section: CLI
app_status: active
pkg_ns: LA
patch_ver: 5.2
patch_id: LA*5.2*53
group_key: "LA:LA:5.2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - strong
  - class
  - vista
  - interface
  - table
  - style
  - width
  - even
  - results
  - engine
page_count: 0
word_count: 4152
section_count: 3
table_count: 1
figure_count: 2
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2000
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/la7dis.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/la7dis.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=120"
---

![](la-5-2-53-lr-5-2-254-laboratory-universal-interface-hp-carevue-interface-specifi/001.png)

LABORATORY HEWLET PACKARD (HP)CAREVUE INTERFACEPatch LR\*5.2\*254 and Patch LA\*5.2\*53INTERFACE SPECIFICATIONS

May 2000

Department of Veteran Affairs

V*IST*A Software Service

Clinical Specialties Product Line

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Overview - VISTA Laboratory Interface](#overview-vista-laboratory-interface)
  - [VISTA Filtering of Results](#vista-filtering-of-results)
- [VISTA System Environment](#vista-system-environment)
  - [HLLP Operation - VISTA Results Interface](#hllp-operation-vista-results-interface)
- [VISTA Network Connectivity to Interface Engine](#vista-network-connectivity-to-interface-engine)
- [Detailed Description - VISTA Laboratory Results Interface](#detailed-description-vista-laboratory-results-interface)
- [VISTA Laboratory Results Interface Mapping](#vista-laboratory-results-interface-mapping)
The purpose of this document is to describe the Veterans Health Information Systems and Technology Architecture (V*IST*A) Laboratory Test result system’s use of the HL7 Interface Standard (Version 2.3) and to provide a reference guide for implementing this interface with the CareVue system.
The focus of this document is to describe the HL7 Observation Request Unsolicited (ORU) control message used for sending V*IST*A lab test results to the CareVue system. The interface is designed to generate an ORU message upon verification of lab results for any patient whose reporting location is identified as either a CareVue location.

# Overview - VISTA Laboratory Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The V*IST*A Laboratory interface provides the capability for V*IST*A to broadcast laboratory results that are entered into V*IST*A. Each time laboratory results are verified in V*IST*A, the laboratory interface determines if those results should be sent to the Interface Engine (see paragraph below).

Figure 1: V*IST*A Laboratory Interface

## VISTA Filtering of Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not all laboratory results are sent to the Interface Engine. Each time laboratory results are verified in V*IST*A, the location designated as the report routing location (this defaults to the ordering location entered at the time of ordering the laboratory tests in V*IST*A) is checked to see if the results should be sent to the CareVue. VISTA uses the FOREIGN INTERFACE file (#62.487) for this purpose.

If there is an entry in this file for the specified location, an HL7 message is generated and sent to the Interface Engine. The location must match exactly an entry in the FOREIGN INTERFACE and must be a valid location in the Hospital Location file (#44).

# VISTA System Environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

V*IST*A uses standardized HL7 messaging software, HLLP, for communicating with external systems. Within V*IST*A, different instances of the HLLP software (VMS processes) are associated with different applications. Each instance of the HLLP software is assigned a unique name in the V*IST*A device file.

Table 1 identifies the HLLP process names associated with the HOST integration.

## HLLP Operation - VISTA Results Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

V*IST*A provides the optional capability to automatically restart HLLP’s each time the running process is terminated (because of an interruption on the communications connection with the Interface Engine or other system interruption). This option should be selected for each HLLP communicating with the Interface Engine.

<table>
<caption><p>Table 1: VISTA HLLP Processes - HOST Integration Example</p></caption>
<colgroup>
<col style="width: 40%" />
<col style="width: 37%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VISTA Interface</strong></th>
<th><strong>VISTA HLLP<br />
Process</strong></th>
<th><strong>VISTA Virtual<br />
Device</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><strong>V</strong>IST<strong>A</strong> Outgoing Interfaces (<strong>V</strong>IST<strong>A</strong> to Interface Engine)</td>
</tr>
<tr class="even">
<td>ADT - Test</td>
<td>OG_TEST</td>
<td>LTA_9297</td>
</tr>
<tr class="odd">
<td>ADT - Production</td>
<td>OG_PROD</td>
<td>LTA_9299</td>
</tr>
<tr class="even">
<td>Laboratory Results - Test</td>
<td>OG_LAB_TEST</td>
<td>LTA_9333</td>
</tr>
<tr class="odd">
<td>Laboratory Results - Production</td>
<td>OG_LAB_PROD</td>
<td>LTA_9334</td>
</tr>
<tr class="even">
<td colspan="3"><strong>V</strong>IST<strong>A</strong> Incoming Interfaces (Interface Engine to <strong>V</strong>IST<strong>A</strong>)</td>
</tr>
<tr class="odd">
<td>Results - Test</td>
<td>IC_TEST</td>
<td>LTA_9161</td>
</tr>
<tr class="even">
<td>Results - Production</td>
<td>IC_PROD</td>
<td>LTA_9296</td>
</tr>
</tbody>
</table>

Table 1: VISTA HLLP Processes - HOST Integration Example

# VISTA Network Connectivity to Interface Engine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The V*IST*A HL7 software uses asynchronous type communications. Separate communications lines have been dedicated for each of the V*IST*A interfaces that have been implemented with the Interface Engine. Configuring the system to support both a test interface and a production interface requires an additional set of dedicated lines.

The communication lines between V*IST*A and the Interface Engine are implemented by dedicating ports on a Digital terminal server. Each of the lines requires two terminal server ports, one for the V*IST*A end of the communication and one for the Interface Engine end of the communication. The two terminal server ports are physically connected using a null modem cable.

Both V*IST*A and the Interface Engine communicate with the terminal server(s) using the Local Area Transport (LAT) protocol over the Ethernet backbone.

Figure 2 illustrates how the connections between V*IST*A and the Interface Engine are implemented.

Figure 2: VISTA to Interface Engine Network Connections

![](la-5-2-53-lr-5-2-254-laboratory-universal-interface-hp-carevue-interface-specifi/002.png)

These ports can be provided by any terminal server(s) connected to the network with the only requirement being that each pair (V*IST*A end and Interface Engine end) be physically connected using a null modem cable.

Table 2 identifies the terminal server ports, which are being used to communicate between V*IST*A and the Interface Engine.

Table 2: Terminal Server Ports - VISTA to Interface Engine Communications Example

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 31%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>VISTA Interface</strong></p>
<p><strong>HL7 LLP</strong></p></th>
<th><strong>Terminal Server Port<br />
(VISTA Connection)<br />
VISTA Virtual Device</strong></th>
<th><strong>Terminal Server Port<br />
(Interface Engine Connection)<br />
Interface Engine Virtual Device</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Laboratory Results I/F - Production</p>
<p>INTERFACE ENGINELABRESULTS LLP</p></td>
<td>DSV 104 Port 2<br />
LTA_9334<br />
OG_LAB_PROD</td>
<td>DSV 104 Port 1<br />
LAT device 649<br />
vista_ic_lab</td>
</tr>
</tbody>
</table>

Laboratory Results Interface (vista_ic_lab)

The laboratory interface is an outgoing interface from V*IST*A to the Interface Engine which transmits HL7 ORU messages to communicate laboratory results that have been verified in V*IST*A. The Interface Engine translates these incoming messages for communication to HP CareVue.

Communications lines and terminal server port designations are assigned in V*IST*A by the IRM operations staff and are defined as follows:

Outgoing

> NAME: OG_LAB_PROD \$I: \_LTA9334:

> LOCATION OF TERMINAL: COMPUTER ROOM ASK HOST FILE: YES

> SUBTYPE: C-OTHER TYPE: TERMINAL

> LAT SERVER NODE: DSV104 LAT SERVER PORT: PORT_6

Incoming

NAME: IC_LAB_PROD \$I: \_LTA9296:

LOCATION OF TERMINAL: IRM COMPUTER ROOM

SUBTYPE: P-OTHER TYPE: TERMINAL

LAT SERVER NODE: DSV104 LAT SERVER PORT: PORT_8

Communication between V*IST*A and the Interface Engine is accomplished using an asynchronous serial communications protocol as if the systems were connected using a standard RS232 asynchronous serial communications line.

Table 3 and Table 4 identify the terminal server port settings for the V*IST*A interface with the Interface Engine. These settings are used for terminal server ports, one for the V*IST*A end, and the other for the Interface Engine end. IRM operations staff can modify terminal server port settings.

Table 3: Terminal Server Port Settings - VISTA to Interface Engine ADT Interface

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 15%" />
<col style="width: 29%" />
<col style="width: 30%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Port <em>n</em></td>
<td></td>
<td colspan="2">Server: DSV<em>nnn</em></td>
</tr>
<tr class="even">
<td>Character Size:</td>
<td>8</td>
<td>Input Speed:</td>
<td>9600</td>
</tr>
<tr class="odd">
<td>Flow Control:</td>
<td>XON</td>
<td>Output Speed:</td>
<td>9600</td>
</tr>
<tr class="even">
<td>Parity:</td>
<td>None</td>
<td>Signal Control</td>
<td>Enabled</td>
</tr>
<tr class="odd">
<td>Stop Bits:</td>
<td>Dynamic</td>
<td>Signal Select:</td>
<td>CTS-DSR-RTS-DTR</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Access:</td>
<td>Remote</td>
<td>Local Switch:</td>
<td>None</td>
</tr>
<tr class="even">
<td>Backwards Switch:</td>
<td>None</td>
<td>Name:</td>
<td>PORT_<em>n</em></td>
</tr>
<tr class="odd">
<td>Break:</td>
<td>Remote</td>
<td>Session Limit</td>
<td>1</td>
</tr>
<tr class="even">
<td>Forwards Switch:</td>
<td>None</td>
<td>Type:</td>
<td>Soft</td>
</tr>
<tr class="odd">
<td>Default Protocol:</td>
<td>LAT</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">Preferred Service: None</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><p>Authorized Groups: 0</p>
<p>(Current) Groups: 0</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">Enabled Characteristics:<br />
Autoconnect, DTRwait</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table 4: Terminal Server Port Settings - VISTA to Interface Engine Results Interface

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 15%" />
<col style="width: 29%" />
<col style="width: 30%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Port <em>n</em></td>
<td></td>
<td colspan="2">Server: DSV<em>nnn</em></td>
</tr>
<tr class="even">
<td>Character Size:</td>
<td>8</td>
<td>Input Speed:</td>
<td>9600</td>
</tr>
<tr class="odd">
<td>Flow Control:</td>
<td>XON</td>
<td>Output Speed:</td>
<td>9600</td>
</tr>
<tr class="even">
<td>Parity:</td>
<td>None</td>
<td>Signal Control</td>
<td>Enabled</td>
</tr>
<tr class="odd">
<td>Stop Bits:</td>
<td>Dynamic</td>
<td>Signal Select:</td>
<td>CTS-DSR-RTS-DTR</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Access:</td>
<td>Remote</td>
<td>Local Switch:</td>
<td>None</td>
</tr>
<tr class="even">
<td>Backwards Switch:</td>
<td>None</td>
<td>Name:</td>
<td>PORT_<em>n</em></td>
</tr>
<tr class="odd">
<td>Break:</td>
<td>Remote</td>
<td>Session Limit</td>
<td>1</td>
</tr>
<tr class="even">
<td>Forwards Switch:</td>
<td>None</td>
<td>Type:</td>
<td>Soft</td>
</tr>
<tr class="odd">
<td>Default Protocol:</td>
<td>LAT</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">Preferred Service: None</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><p>Authorized Groups: 0</p>
<p>(Current) Groups: 0</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">Enabled Characteristics:<br />
Autoconnect, DTRwait</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

# Detailed Description - VISTA Laboratory Results Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

V*IST*A sends laboratory results messages to the INTERFACE ENGINE using an HL7 message format. The Interface Engine converts these messages to the message formats required by the CareVue systems and sends the messages to CareVue.

The VISTA Laboratory Results Interface Mapping describes the messages according to the HL7 format that is received from V*IST*A.

# VISTA Laboratory Results Interface Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Laboratory results are sent to the Interface Engine as HL7 ORU Unsolicited Results messages. Table 5 identifies the HL7 message segments that comprise the message format for result messages being sent from V*IST*A.

Table 5: ORU Message Layout

| HL7 Segment | Description                                      |
|-----------------|------------------------------------------------------|
| MSH             | Message Header Segment                               |
| PID             | Patient Identification Segment                       |
| OBR             | Observation Request Segment                          |
| NTE             | Optionally, one or more Notes and Comments Segments. |
| OBX             | One or more Observation Segments                     |

The following tables identify the specific data elements for each of the HL7 segments. These tables identify only those fields that are supported by the V*IST*A interface. All other fields in the HL7 segments are not currently used by V*IST*A.

> **NOTE:** V*IST*A uses HL7 control characters in a different manner than defined in the current HL7 Standard.

Table 6: MSH- Message Header Segment

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 24%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 44%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>HL7<br />
Seq</strong></td>
<td><strong>HL7 Field Name</strong></td>
<td><strong>Req’d<br />
or<br />
Opt</strong></td>
<td><strong>Data Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>VISTA Value/<br />
Comments</strong></td>
</tr>
<tr class="even">
<td>1</td>
<td>Field Separator</td>
<td>R</td>
<td>ST</td>
<td>1</td>
<td><p>“^”</p>
<p>see notes below</p></td>
</tr>
<tr class="odd">
<td>2</td>
<td>Encoding Characters</td>
<td>R</td>
<td>ST</td>
<td>4</td>
<td><p>“~|\&amp;”</p>
<p>see notes below</p></td>
</tr>
<tr class="even">
<td>3</td>
<td>Sending Application</td>
<td></td>
<td>ST</td>
<td>15</td>
<td><strong>V</strong><em>IST</em><strong>A</strong> sends as “DHCP CARELIFE”</td>
</tr>
<tr class="odd">
<td>4</td>
<td>Sending Facility</td>
<td></td>
<td>ST</td>
<td>20</td>
<td><strong>V</strong><em>IST</em><strong>A</strong> sends station number</td>
</tr>
<tr class="even">
<td>5</td>
<td>Receiving Application</td>
<td></td>
<td>ST</td>
<td>30</td>
<td><strong>V</strong><em>IST</em><strong>A</strong> sends as “INTERFACE ENGINE CARELIFE”</td>
</tr>
<tr class="odd">
<td>6</td>
<td>Receiving Facility</td>
<td></td>
<td>ST</td>
<td>30</td>
<td><strong>V</strong><em>IST</em><strong>A</strong> sends station number</td>
</tr>
<tr class="even">
<td>7</td>
<td>Date/Time of Message</td>
<td></td>
<td>TS</td>
<td>26</td>
<td><em>YYYYMMDDHHMMSS</em></td>
</tr>
<tr class="odd">
<td>8</td>
<td>Security</td>
<td></td>
<td>NM</td>
<td>40</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>9</td>
<td>Message Type</td>
<td>R</td>
<td>CM</td>
<td>7</td>
<td><p><strong>V</strong><em>IST</em><strong>A</strong> sends as “ORU^R01”</p>
<p>see notes below</p></td>
</tr>
<tr class="odd">
<td>10</td>
<td>Message Control ID</td>
<td>R</td>
<td>ST</td>
<td>20</td>
<td>Unique message ID generated by the sending system</td>
</tr>
<tr class="even">
<td>11</td>
<td>Processing ID</td>
<td>R</td>
<td>ID</td>
<td>1</td>
<td><p><strong>V</strong><em>IST</em><strong>A</strong> sends as “P”</p>
<p>see notes below</p></td>
</tr>
<tr class="odd">
<td>12</td>
<td>Version ID</td>
<td>R</td>
<td>ID</td>
<td>8</td>
<td><strong>V</strong><em>IST</em><strong>A</strong> sends as “2.3”</td>
</tr>
<tr class="even">
<td>15</td>
<td>Accept Acknowledgment Type</td>
<td></td>
<td>ID</td>
<td>2</td>
<td><strong>V</strong><em>IST</em><strong>A</strong> sends as “AL” (Always)</td>
</tr>
<tr class="odd">
<td>16</td>
<td>Application Acknowledgment Type</td>
<td></td>
<td>ID</td>
<td>2</td>
<td><strong>V</strong><em>IST</em><strong>A</strong> sends as “AL” (Always)</td>
</tr>
<tr class="even">
<td>17</td>
<td>Country Code</td>
<td></td>
<td>ID</td>
<td>2</td>
<td><strong>V</strong><em>IST</em><strong>A</strong> sends as “USA”</td>
</tr>
</tbody>
</table>

MSH Segment Notes

Data Type: ST: String data - left justified with optional trailing blanks  
TS: time stamp always in the format YYYYMMDDHHMM\[SS\]\[+/-ZZZZ\]  
CM: A field that is the combination of other meaningful data fields.  
ID: ST formatted data that corresponds to a table entry maintained by system

NM: Numeric

Field Separator & Encoding Characters:

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>VISTA</p>
<p>Value</p></td>
<td>Description</td>
</tr>
<tr class="even">
<td>^</td>
<td>field separator</td>
</tr>
<tr class="odd">
<td>~</td>
<td>component separator</td>
</tr>
<tr class="even">
<td>|</td>
<td>repetition separator</td>
</tr>
<tr class="odd">
<td>\</td>
<td>escape character</td>
</tr>
<tr class="even">
<td>&amp;</td>
<td>subcomponent separator</td>
</tr>
</tbody>
</table>

Message Type: \<message type\>\<trigger event\>

Processing ID: “D” - Debugging messages sent from INTERFACE ENGINE Test Environment  
“P” - Production messages sent from INTERFACE ENGINE Production Environment

Table 7: PID – Patient Identification Segment

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 28%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 10%" />
<col style="width: 36%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>HL7<br />
Seq</strong></td>
<td><strong>HL7 Field Name</strong></td>
<td><strong>Req’d<br />
or<br />
Opt</strong></td>
<td><strong>Data Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>VISTA Value /<br />
Comment</strong></td>
</tr>
<tr class="even">
<td>3</td>
<td>Patient ID (Internal ID)</td>
<td>R</td>
<td>CM</td>
<td>20</td>
<td><strong>V</strong><em>IST</em><strong>A</strong> internal entry number.</td>
</tr>
<tr class="odd">
<td>6</td>
<td>Mother’s Maiden Name</td>
<td></td>
<td>ST</td>
<td>48</td>
<td><strong>V</strong><em>IST</em><strong>A</strong> Mother’s maiden Name</td>
</tr>
</tbody>
</table>

PID Segment Table Notes:Data TypeCM: A field that is the combination of other meaningful data fields.  
ST: String data - left justified with optional trailing blanks

Patient ID (Internal ID): \<patient ID (ST)\>\<check digit (NM)\>\<check digit scheme (ID)\>  
\<assigning facility ID (ST)\>\<type (ID)\>

> **NOTE:** V*IST*A calculates the check digit as the check digit scheme applied to the sum of the digits, where non-numeric digits are calculated as zero (0).  
This check digit scheme DOES NOT conform to the HL7 standard.

Table 8: OBR – Observation Request Segment

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 25%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 42%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>HL7<br />
Seq</strong></td>
<td><strong>HL7 Field Name</strong></td>
<td><strong>Req’d<br />
or<br />
Opt</strong></td>
<td><strong>Data Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>VISTA Value /<br />
Comment</strong></td>
</tr>
<tr class="even">
<td>3</td>
<td>Filler Order Number</td>
<td>R</td>
<td>CM</td>
<td>75</td>
<td><strong>V</strong><em>IST</em><strong>A</strong> Accession Number<br />
see notes below</td>
</tr>
<tr class="odd">
<td>4</td>
<td>Universal Service ID</td>
<td>R</td>
<td>CE</td>
<td>200</td>
<td><strong>V</strong><em>IST</em><strong>A</strong> copies the accession area identification from Filler Order Number into the 1<sup>st</sup> component. see note below</td>
</tr>
<tr class="even">
<td>7</td>
<td>Observation Date/Time</td>
<td></td>
<td>TS</td>
<td>26</td>
<td><em>YYYYMMDDHHMMSS</em></td>
</tr>
<tr class="odd">
<td>14</td>
<td>Specimen Received Date/Time</td>
<td></td>
<td>TS</td>
<td>26</td>
<td><em>YYYYMMDDHHMMSS</em></td>
</tr>
<tr class="even">
<td>15</td>
<td>Specimen Source</td>
<td></td>
<td>CM</td>
<td>300</td>
<td><strong>V</strong><em>IST</em><strong>A</strong> limits to 150 characters.<br />
see notes below</td>
</tr>
<tr class="odd">
<td>22</td>
<td>Results Rpt/Status Chng - Date/Time</td>
<td></td>
<td>TS</td>
<td>26</td>
<td>Date/Time results are verified in <strong>V</strong><em>IST</em><strong>A</strong>.</td>
</tr>
<tr class="even">
<td>24</td>
<td>Diagnostic Serv Sect ID</td>
<td></td>
<td>ID</td>
<td>10</td>
<td><strong>V</strong><em>IST</em><strong>A</strong> sends as “LAB”</td>
</tr>
<tr class="odd">
<td>28</td>
<td>Result Copies To</td>
<td></td>
<td>CN</td>
<td>150</td>
<td><strong>V</strong><em>IST</em><strong>A</strong> sends the location specified in the order as the 1<sup>st</sup> component.</td>
</tr>
</tbody>
</table>

OBR Segment Table Notes:Data Type: CM: composite field which may include multiple components  
CE: Coded Element - contains six components in two groups as follows:  
\<identifier\>\<text\>\<name of coding system\>  
\<alternate identifier\>\<alternate text\>\<name of alternate coding system\>  
TS: time stamp always in the format YYYYMMDDHHMM\[SS\]\[+/-ZZZZ\]  
ID: ST formatted data that corresponds to a table entry maintained by system

Filler Order Number: \<unique filler ID\>\<filler application ID\>

\<unique filler ID\> contains V*IST*A accession number in the format  
*xxxx nnnn aaaa,* where

*xxxx* is a numerical prefix whose value depends on when (day (*mmdd*),  
month (*mm*) or year (*yy*)) the numeric accession number  
resets to 1.  
*nnnn* is the numeric accession number and  
*aaaa* is the V*IST*A accession area

\<filler application ID\> is not sent

Specimen Source: \<specimen source (CE)\>\<additives (TX)\>\<free text (TX)\>\<body site (CE)\>  
\<site modifier\>, where V*IST*A sends specimen source a s:  
\<SNOMED Code\>\<Topography Name\>

> Universal Service ID:

> \<AU~AUTOPSY~L\>

> \<BB~BLOOD BANK~L\>

> \<CH~CHEMISTRY~L\> or any other name

> \<CY~CYTOPATHOLOGY~L\>

> \<EM~ELECTRON MICROSCOPY~L\>

> \<MI~MICROBIOLOG~L\>

> \<SP~SURGICAL PATHOLOGY~L\>

Specimen Source: \<SNOMED code1 ;Topography name1~ SNOMED code2 ;Topography name2\>

> Example: \<0X400;Plasma~0X400;Plasma\>

Table 9: NTE – Notes and Comments Segment

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 27%" />
<col style="width: 10%" />
<col style="width: 7%" />
<col style="width: 10%" />
<col style="width: 36%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>HL7<br />
Seq</strong></td>
<td><strong>HL7 Field Name</strong></td>
<td><strong>Req’d<br />
or<br />
Opt</strong></td>
<td><strong>Data Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>VISTA Value /<br />
Comment</strong></td>
</tr>
<tr class="even">
<td>2</td>
<td>Source of Comment</td>
<td></td>
<td>ID</td>
<td>8</td>
<td><strong>V</strong><em>IST</em><strong>A</strong> sends as “L”</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Comment</td>
<td></td>
<td>TX</td>
<td>64K</td>
<td><strong>V</strong><em>IST</em><strong>A</strong> sends one line of comment text in each NTE segment and allows multiple segments.</td>
</tr>
</tbody>
</table>

NTE Segment Table Notes:Data Type: ID: Value corresponds to a table entry maintained by system  
TX: String data (including leading spaces)

Table 10: OBX – Result Segment - VISTA Laboratory Interface

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 26%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 11%" />
<col style="width: 38%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>HL7<br />
Seq</strong></td>
<td><strong>HL7 Field Name</strong></td>
<td><strong>Req’d<br />
or<br />
Opt</strong></td>
<td><strong>Data Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>VISTA Value /<br />
Comment</strong></td>
</tr>
<tr class="even">
<td>2</td>
<td>Value Type</td>
<td>R</td>
<td>ID</td>
<td>2</td>
<td><strong>V</strong><em>IST</em><strong>A</strong> does not send.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Observation Identifier</td>
<td>R</td>
<td>CE</td>
<td>80</td>
<td><strong>V</strong><em>IST</em><strong>A</strong> sends the lab test name as the 2<sup>nd</sup> component.</td>
</tr>
<tr class="even">
<td>5</td>
<td>Observation Results</td>
<td></td>
<td>ST</td>
<td>64K</td>
<td>Verified results<br />
<strong>V</strong><em>IST</em><strong>A</strong> limits to 20 characters</td>
</tr>
<tr class="odd">
<td>6</td>
<td>Units</td>
<td></td>
<td>CE</td>
<td>20</td>
<td>Verified units used in test, e.g. mg/dL, %, NEG-POS etc.</td>
</tr>
<tr class="even">
<td>7</td>
<td>References Range</td>
<td></td>
<td>ST</td>
<td>40</td>
<td>“<em>reference low</em> - <em>reference high</em>”<br />
“<em>critical low</em> - <em>critical high</em>”<br />
“<em>therapeutic low</em> - <em>therapeutic high</em>”</td>
</tr>
<tr class="odd">
<td>8</td>
<td>Abnormal Flags</td>
<td></td>
<td>ID</td>
<td>10</td>
<td><p><strong>V</strong><em>IST</em><strong>A</strong> sends as:</p>
<p>“_” or “N” = Normal<br />
“H” = High<br />
“HH” = Dangerously High<br />
“L” = Low<br />
“LL” = Dangerously Low</p></td>
</tr>
<tr class="even">
<td>11</td>
<td>Observe Result Status</td>
<td>R</td>
<td>ID</td>
<td>2</td>
<td><p><strong>V</strong><em>IST</em><strong>A</strong> only sends results with a status of “F” = Final.</p>
<p>Corrected results are also sent with a status of “F” = Final.</p></td>
</tr>
</tbody>
</table>

OBX Segment Table Notes:Data Type: ID: Value corresponds to a table entry maintained by system  
CE: Coded Element - contains six components in two groups as follows:  
\<identifier\>\<text\>\<name of coding system\>  
\<alternate identifier\>\<alternate text\>\<name of alternate coding system\>  
ST: String data  
CM: Composite field which may include multiple components.

Table 11: MSA – Message Acknowledgement Segment

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 26%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 11%" />
<col style="width: 38%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>HL7<br />
Seq</strong></td>
<td><strong>HL7 Field Name</strong></td>
<td><strong>Req’d<br />
or<br />
Opt</strong></td>
<td><strong>Data Type</strong></td>
<td><strong>Length</strong></td>
<td><strong>VISTA Value /<br />
Comment</strong></td>
</tr>
<tr class="even">
<td>1</td>
<td>Acknowledgment Code</td>
<td>R</td>
<td>ID</td>
<td>2</td>
<td>“AA”, “AE”, “AR”</td>
</tr>
<tr class="odd">
<td>2</td>
<td>Message Control ID</td>
<td>R</td>
<td>ST</td>
<td>20</td>
<td>Message Control ID of the sending system. It is echoed back by the receiving system.</td>
</tr>
<tr class="even">
<td>3</td>
<td>Text Message</td>
<td></td>
<td>ST</td>
<td>80</td>
<td>An optional text field that further describes an error condition.</td>
</tr>
</tbody>
</table>