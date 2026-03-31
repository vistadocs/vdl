---
title: "Laboratory: Universal Interface Data Innovations Instructional Implementation Guide Version 5.2"
doc_type: IG-IMP
doc_label: Implementation Guide
doc_layer: anchor
doc_subject: 
app_code: LA
app_name: "Laboratory: Universal Interface"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 5.2
patch_id: 
group_key: "LA::5.2"
file_numbers: 
  - 770
security_keys: []
menu_options: 0
description: > ![](laboratory-universal-interface-data-innovations-instructional-implementation-gui/001.png)
audience: 
keywords: 
  - strong
  - table
  - contents
  - class
  - instrument
  - manager
  - even
  - auto
  - analyzer
  - setup
page_count: 0
word_count: 3642
section_count: 20
table_count: 6
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: March 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/datain.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/datain.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=120"
---

> ![](laboratory-universal-interface-data-innovations-instructional-implementation-gui/001.png)

LABORATORY

DATA INNOVATIONS INSTRUCTIONAL IMPLEMENTATION GUIDE

> VERSION 5.2

> March 1997

> Office of Employee Education Salt Lake Education Center Clin2 Customer Services

> Lab ADPAC Training Advisory Council Lab Development Team
# Site Preparation


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Site Preparation](#site-preparation)
  - [Placement Considerations](#placement-considerations)
  - [Port Configuration](#port-configuration)
    - [Test](#test)
  - [Wiring](#wiring)
    - [Test](#test-1)
- [Instrument Manager-Validation](#instrument-manager-validation)
  - [Instrument Manager Hardware](#instrument-manager-hardware)
- [VISTA Configuration](#vista-configuration)
  - [ACCESSION file (#68)](#accession-file-68)
    - [Notes](#notes)
  - [HL7 Package](#hl7-package)
    - [DEVICE file (# 3.5)](#device-file-35)
    - [HL7 APPLICATION PARAMETER file (#771)](#hl7-application-parameter-file-771)
    - [HL7 NON DHCP APPLICATION PARAMETER file (#770)](#hl7-non-dhcp-application-parameter-file-770)
    - [LA7 MESSAGE PARAMETER CONFIGURATION (#62.48)](#la7-message-parameter-configuration-6248)
    - [TOPOGRAPHY file (#61)](#topography-file-61)
    - [URGENCY file (#62.05)](#urgency-file-6205)
    - [AUTO INSTRUMENT file (#62.4)](#auto-instrument-file-624)
    - [Other Files](#other-files)
- [Instrument Manager Configuration](#instrument-manager-configuration)
  - [Instrument Manager System Configuration](#instrument-manager-system-configuration)
  - [Configuration for each Analyzer](#configuration-for-each-analyzer)
  - [Cluster Definition](#cluster-definition)
- [Analyzer Configuration](#analyzer-configuration)
  - [Analyzer Host Communications to Instrument Manager](#analyzer-host-communications-to-instrument-manager)
  - [Barcode Labels](#barcode-labels)
- [Confirming Data Transmission](#confirming-data-transmission)
  - [Test Data Stream (Upload Results)](#test-data-stream-upload-results)
    - [Analyzer to Instrument Manager](#analyzer-to-instrument-manager)
    - [Interface Manager to VISTA](#interface-manager-to-vista)
    - [Troubleshooting](#troubleshooting)
  - [Test Data Stream (Download Orders)](#test-data-stream-download-orders)
    - [Data-VISTA to Instrument Manager](#data-vista-to-instrument-manager)
    - [Instrument Manager to Analyzer](#instrument-manager-to-analyzer)
    - [Troubleshooting](#troubleshooting-1)
- [Training](#training)
- [Appendix A: Sample Instrument](#appendix-a-sample-instrument)
  - [Clinitek 100](#clinitek-100)
    - [Load/Work List:](#loadwork-list)
    - [Auto Instrument Setup:](#auto-instrument-setup)
  - [Beckman CX Series](#beckman-cx-series)
    - [Load/Work List:](#loadwork-list-1)
    - [Auto Instrument Setup:](#auto-instrument-setup-1)
    - [Auto Instrument Setup (continued):](#auto-instrument-setup-continued)
    - [Auto Instrument Setup (continued):](#auto-instrument-setup-continued-1)
    - [CX Host Communication Parameters:](#cx-host-communication-parameters)
  - [Modulus Differential Counter](#modulus-differential-counter)
    - [Load/Work List:](#loadwork-list-2)
    - [Auto Instrument Setup:](#auto-instrument-setup-2)
    - [Auto Instrument Setup (continued):](#auto-instrument-setup-continued-2)
  - [Coulter STKS](#coulter-stks)
    - [Load/Work List:](#loadwork-list-3)
    - [Auto Instrument Setup:](#auto-instrument-setup-3)
  - [Uro-Comp for Clinitek 200](#uro-comp-for-clinitek-200)
    - [Load/Work List:](#loadwork-list-4)
    - [Auto Instrument Setup:](#auto-instrument-setup-4)
    - [Auto Instrument Setup (continued):](#auto-instrument-setup-continued-3)
  - [Axsym](#axsym)
    - [Load/Work List:](#loadwork-list-5)
    - [Auto Instrument Setup:](#auto-instrument-setup-5)

## Placement Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In determining where the Data Innovations Instrument Manager should be located, consideration should be given to the present and planned locations of Laboratory and Non-Laboratory Analyzers.

- If all analyzers are located in one area, the Instrument Manager may be located within the same area.
- If analyzers are, or will be located in separate distinct areas or facilities, the Instrument Manager should be located in an area that would facilitate connection with minimum routing of communication lines.
- If network capabilities are available throughout the facilities, that is, Local Area Network (LAN) using LAT or TCP/IP Protocols, then the Instrument Manager can be located at any location with network access.

## Port Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For port configuration information see Appendix A pages 95 through 98 of Laboratory Universal Interface Patch Documentation.

### Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If using RS-232 Serial connection, test the line by connecting a CRT and successfully send and receive data at the terminal.

## Wiring

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Modem wiring for Data Innovations Instrument Managers Dial-In Modem Provide direct inward dial line (DID).
- Wiring for Data Innovations Instrument Manager to analyzer(s) Use Port Configuration if necessary.
  - See Appendix A pages 95 through 98 of Laboratory Universal Interface Patch Documentation.
  - If the analyzer is connected through a terminal server, supply IRMS with analyzer specific host communication settings: baud rate, data bits, stop bits, parity and protocol for each analyzer.

### Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If using RS-232 Serial connection, test line by connecting a CRT and successfully send/receive data at the terminal.

# Instrument Manager-Validation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Instrument Manager Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Install PC, monitor, keyboard, and modem per installation instructions.
2.  Power Up Instrument Manager.
3.  Install Instrument Manager software if not purchased pre-installed per vendor instructions.
4.  Notify Data Innovations of individual analyzer software drivers required and provide the following information.
    - Analyzer Name
    - Analyzer software version
    - Communication protocol
    - Unidirectional
    - Bidirectional
    - Cluster

# V*IST*A Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ACCESSION file (#68)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Using FileMan edit the ACCESSION file according to instructions in the Lab Universal Interface Patch Documentation (page 28).

### Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Field \#.091, Numeric Identifier, has been changed to Field \#.4.

> The Numeric Identifier field is a 1-2 alpha-numeric character(s) using the combination of numbers 1-9 and/or uppercase letters A-Z. If using the UID and an analyzer requires a numeric UID, then use number(s) 1-99.

## HL7 Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When Version 1.6 of the HL7 package is installed, use HL7 V 1.5 options in configuring package parameters related to the Universal Interface.

> You must configure the following files:

### DEVICE file (# 3.5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Define entry-NULL DEVICE

> The V*IST*A HL7 package requires the entry of a NULL DEVICE. The NULL DEVICE must be defined if not already defined.

> For DSM Sites, Suggested Setup:

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Entry</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>NAME:</td>
<td><strong>NULL DEVICE</strong></td>
</tr>
<tr class="odd">
<td>$I:</td>
<td><strong>_NLA0:</strong></td>
</tr>
<tr class="even">
<td>VOLUME SET(CPU):</td>
<td><strong>ROU</strong></td>
</tr>
<tr class="odd">
<td>SIGN-ON/SYSTEM DEVICE:</td>
<td><strong>NO</strong></td>
</tr>
<tr class="even">
<td><p>LOCATION OF</p>
<p>TERMINAL:</p></td>
<td><strong>COMPUTER ROOM</strong></td>
</tr>
<tr class="odd">
<td>SUBTYPE:</td>
<td><strong>P-OTHER</strong> [or any generic terminal type]</td>
</tr>
<tr class="even">
<td>TYPE:</td>
<td><strong>TERMINAL</strong></td>
</tr>
</tbody>
</table>

> For MSM sites running additional HL7 interfaces, more than one Null device must be defined. Refer to pages 19 through 22 of the Laboratory Universal Interface Patch Documentation for specifics.

2.  Define the device used by the V*IST*A HL7 package to communicate with the Instrument Manager.

> Suggested Setup:

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Entry</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>NAME:</td>
<td><strong>LABDATA-IM</strong></td>
</tr>
<tr class="odd">
<td>$I:</td>
<td>[Set to appropriate value per operating system]</td>
</tr>
<tr class="even">
<td>ASK DEVICE:</td>
<td><strong>NO</strong></td>
</tr>
<tr class="odd">
<td>ASK PARAMETERS:</td>
<td><strong>NO</strong></td>
</tr>
<tr class="even">
<td>SIGN ON/SYSTEM DEVICE:</td>
<td><strong>NO</strong></td>
</tr>
<tr class="odd">
<td><p>LOCATION OF</p>
<p>TERMINAL:</p></td>
<td>[Location of IM]</td>
</tr>
<tr class="even">
<td>SUPPRESS FORM FEED AT CLOSE:</td>
<td><strong>YES</strong></td>
</tr>
<tr class="odd">
<td>SUBTYPE:</td>
<td><strong>P-OTHER</strong> [or any generic terminal type, e.g., No codes in Open/Close Execute fields or other fields allowing control codes.]</td>
</tr>
<tr class="even">
<td>TYPE:</td>
<td><strong>TERMINAL</strong></td>
</tr>
</tbody>
</table>

> Suggested Setup for Alpha VMS/DSM Systems:

| Field        | Entry                        |
|------------------|----------------------------------|
|                  |                                  |
| LAT SERVER NODE: | \[Terminal Server Name\]         |
| LAT SERVER PORT: | \[Terminal Server Port Address\] |
| VMS DEVICE TYPE: | LAB INSTRUMENT               |
| LAT PORT SPEED:  | \[Baud rate of this port\]       |

### HL7 APPLICATION PARAMETER file (#771)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> LA\*5.2\*17 patch post init should create the entry LA AUTO INST as follows:

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Entry</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>NAME:</td>
<td><strong>LA AUTO INST</strong></td>
</tr>
<tr class="odd">
<td>ACTIVE/INACTIVE:</td>
<td><strong>ACTIVE</strong></td>
</tr>
<tr class="even">
<td>HL7 ENCODING CHARACTERS:</td>
<td><blockquote>
<p><strong>~^\&amp;</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>HL7 FIELD SEPARATOR:</td>
<td><strong>|</strong></td>
</tr>
<tr class="even">
<td>HL7 MESSAGE:</td>
<td><strong>ORU</strong></td>
</tr>
<tr class="odd">
<td>PROCESSING ROUTINE:</td>
<td><strong>ORU^LA7HL7</strong></td>
</tr>
<tr class="even">
<td>HL7 MESSAGE:</td>
<td><strong>ORM</strong></td>
</tr>
<tr class="odd">
<td>PROCESSING ROUTINE:</td>
<td><strong>NONE</strong></td>
</tr>
<tr class="even">
<td>HL7 SEGMENT:</td>
<td><strong>OBR</strong></td>
</tr>
<tr class="odd">
<td>FIELDS USED IN THIS SEGEMENT:</td>
<td><strong>4,7,8,9,14,22</strong></td>
</tr>
<tr class="even">
<td>HL7 SEGMENT:</td>
<td><strong>OBX</strong></td>
</tr>
<tr class="odd">
<td>FIELDS USED IN THIS SEGEMENT:</td>
<td><strong>2,3,4,5,6,7,8</strong></td>
</tr>
<tr class="even">
<td>HL7 SEGMENT:</td>
<td><p><strong>MSH</strong></p>
<p>[FIELDS USED IN THIS SEGEMENT: 1,2,3,4,5,6,7,8,9,10,11,12]</p></td>
</tr>
<tr class="odd">
<td>HL7 SEGMENT:</td>
<td><strong>PID</strong></td>
</tr>
<tr class="even">
<td>FIELDS USED IN THIS SEGEMENT:</td>
<td><strong>3,5,7,8,19</strong></td>
</tr>
<tr class="odd">
<td>HL7 SEGMENT:</td>
<td><strong>ORC</strong></td>
</tr>
<tr class="even">
<td>FIELDS USED IN THIS SEGEMENT:</td>
<td><strong>1,2,3</strong></td>
</tr>
<tr class="odd">
<td>HL7 SEGMENT:</td>
<td><strong>NTE</strong></td>
</tr>
<tr class="even">
<td>FIELDS USED IN THIS SEGEMENT:</td>
<td><strong>3</strong></td>
</tr>
</tbody>
</table>

> Note An entry must also be created or exist in File \# 771 for LAB INTERFACE:

| Field        | Entry              |
|------------------|------------------------|
|                  |                        |
| NAME:            | LAB INTERFACE      |
| ACTIVE/INACTIVE: | ACTIVE             |
| FACILITY NAME:   | Instrument Manager |

### HL7 NON DHCP APPLICATION PARAMETER file (#770)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Set up Lab Interface using the HL7 Main Menu

- Version 1.5 Option
- Non- V*IST*A Application Parameter Enter/Edit Suggested field entries:

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Entry</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>NAME:</td>
<td><strong>LAB INTERFACE</strong></td>
</tr>
<tr class="odd">
<td><strong>V</strong><em>IST</em><strong>A</strong> STATION NUMBER:</td>
<td>[Site’s VA station number]</td>
</tr>
<tr class="even">
<td>NON- <strong>V</strong><em>IST</em><strong>A</strong> FACILITY NAME:</td>
<td><strong>Instrument Manager</strong></td>
</tr>
<tr class="odd">
<td>MAXIMUM BLOCK SIZE:</td>
<td><strong>245</strong></td>
</tr>
<tr class="even">
<td>NUMBER OF RETRIES:</td>
<td><strong>3</strong></td>
</tr>
<tr class="odd">
<td>HL7 DEVICE:</td>
<td><p>[Name of device specified in DEVICE file (#3.5) to which the Instrument Manager is</p>
<p>connected for <strong>V</strong><em>IST</em><strong>A</strong> connection.]</p></td>
</tr>
<tr class="even">
<td>HL7 VERSION NUMBER:</td>
<td><p>[Version of HL7 Specification used by Data Innovations. At this writing it is</p>
<p>V. 2.2]</p></td>
</tr>
<tr class="odd">
<td><strong>V</strong><em>IST</em><strong>A</strong> APPLICATION:</td>
<td><strong>LA AUTO INST</strong></td>
</tr>
<tr class="even">
<td>LOWER LEVEL PROTOCOL TIMEOUT:</td>
<td><strong>5</strong></td>
</tr>
<tr class="odd">
<td>RELATED FILE 771 ENTRY:</td>
<td><strong>LAB INTERFACE</strong></td>
</tr>
<tr class="even">
<td>HL7 PROCESING ID:</td>
<td><strong>PRODUCTION</strong></td>
</tr>
<tr class="odd">
<td>START/STOP TRANSMISSION LOG:</td>
<td><strong>STOP LOG</strong></td>
</tr>
</tbody>
</table>

### LA7 MESSAGE PARAMETER CONFIGURATION (#62.48)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following entries are required for this file:

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Entry</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>CONFIGURATION:</td>
<td><strong>UNIVERSAL INTERFACE</strong></td>
</tr>
<tr class="odd">
<td>PROTOCOL:</td>
<td><strong>HEALTH LEVEL SEVEN</strong></td>
</tr>
<tr class="even">
<td>STATUS:</td>
<td><strong>ACTIVE</strong></td>
</tr>
<tr class="odd">
<td>DEBUG LOG:</td>
<td><strong>ON</strong> [Turning this on logs errors]</td>
</tr>
<tr class="even">
<td><p>HL7 NON- <strong>V</strong><em>IST</em><strong>A</strong></p>
<p>APPLICATION:</p></td>
<td><strong>LAB INTERFACE</strong></td>
</tr>
<tr class="odd">
<td>PROCESS IN:</td>
<td><strong>D QUE^LA7UIIN</strong></td>
</tr>
<tr class="even">
<td>PROCESS DOWNLOAD:</td>
<td><strong>D EN^LA7UID1</strong></td>
</tr>
<tr class="odd">
<td>REMOTE SYSTEM ID:</td>
<td><p>[This is a free text field and should contain the following entries in order.</p>
<p>.01 field of file #770, #3 field of file #770, field #8 of file # 770 and field #2 of file # 770.</p>
<p>Do not insert spaces between field entries. This entry is case sensitive.</p>
<p>Example</p>
<p>LAB INTERFACEInstrument ManagerLA AUTO INST695]</p></td>
</tr>
</tbody>
</table>

### TOPOGRAPHY file (#61)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Map those entries that are used by your site to define test specimens to the appropriate HL7 specimen type.

> Refer to page 29 of the Lab Universal Interface Patch Documentation.

### URGENCY file (#62.05)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Map V*IST*A Lab urgency to the HL7 urgency. These entries are used when downloading to analyzer and analyzer accepts multiple urgencies. It is unnecessary to map workload urgencies.

### AUTO INSTRUMENT file (#62.4)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Create an entry for each instrument connected through the Instrument Manager.

> Entries in the Auto Instrument file must be created as specified in the Laboratory Planning and Implementation Guide. The following are unique requirements for entries using the universal interface.

| Field               | Description/Entry                                                                                                         |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------|
|                         |                                                                                                                               |
| NUMBER                  | Select an entry that is \<100 and does not conflict with any Laboratory System Interface (LSI) entries                        |
| NAME:                   | This name should be 1-8 alpha numeric characters, unique and match exactly the corresponding entry in the Instrument Manager. |
| PROGRAM:                | This field is not used by the universal interface.                                                                            |
| LOAD/WORK LIST          | Name of load/work list associated with this instrument                                                                        |
| ENTRY for LAGEN ROUTINE | IDE                                                                                                                       |
| CROSS LINKED BY         | Accession cross-reference                                                                                                     |
| MESSAGE CONFIGURATION:  | UNIVERSAL INTERFACE                                                                                                           |

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Description/Entry</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>CHEM TEST (Multiples)</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PARAM 1:</p>
</blockquote></td>
<td><p>This is an old field with a new use. Any M code written into this field will be executed on a given test result that is contained in the variable LA7VAL. Any prior code in this field will need to be removed. If additional coding is required, refer to page</p>
<p>47 of the Laboratory Universal Interface Patch Documentation</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PARAM 2 &amp; 3:</p>
</blockquote></td>
<td>These fields are not used by the universal interface.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>UI TEST CODE:</p>
</blockquote></td>
<td><p>Refer to analyzer vendor documentation for</p>
<p>specific codes required.</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NUMBER OF DECIMAL PLACES:</p>
</blockquote></td>
<td><strong>Site preference</strong></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CONVERT RESULT TO</p>
<p>REMARK:</p>
</blockquote></td>
<td><strong>Site preference</strong></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ACCEPT RESULTS FOR THIS TEST:</p>
</blockquote></td>
<td><strong>Site preference</strong></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DOWNLOAD TO INSTRUMENT:</p>
</blockquote></td>
<td><strong>Site preference</strong></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IGNORE RESULTS NOT ORDERED:</p>
</blockquote></td>
<td><strong>Site preference</strong></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>REMOVE SPACES FROM RESULT:</p>
</blockquote></td>
<td><strong>Site preference</strong></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DOWNLOAD ENTRY &amp; DOWNLOAD</p>
<p>PROTOCOL:</p>
</blockquote></td>
<td>These fields are not used by the universal interface.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>FILE BUILD ENTRY:</td>
<td><strong>EN</strong></td>
</tr>
<tr class="odd">
<td>FILE BUILD ROUTINE:</td>
<td><strong>LA7UID</strong></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AUTO DOWNLOAD:</p>
</blockquote></td>
<td><p>Set to YES if analyzer is run in Bidirectional mode in order to send orders</p>
<p>automatically to the analyzer</p></td>
</tr>
</tbody>
</table>

### Other Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Additional entries must be created in Files \#'s 3.5, 770, 771, 62.48, and 62.4, for each Instrument Manager in use. (Suggested naming: LAB INTERFACE2, LAB INTERFACE3, etc., UNIVERSAL INTERFACE2, UNIVERSAL INTERFACE3, as

> applicable.)

# Instrument Manager Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Instrument Manager System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When setting up the system configuration, the following four parameters must match the corresponding entries in the V*IST*A HL7 package:

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Parameter</strong></th>
<th><strong>Entry</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Sending Application:</td>
<td>[.01 Name field in the NON-DHCP APPLICATION PARAMETER file (# 770).]</td>
</tr>
<tr class="odd">
<td>Sending Site:</td>
<td><p>[The NON-DHCP FACILITY NAME field in</p>
<p>the NON-DHCP APPLICATION PARAMETER file (#770).]</p></td>
</tr>
<tr class="even">
<td>Receiving Application:</td>
<td><p>[LA AUTO INST as specified in the HL7</p>
<p>APPLICATION PARAMETER file (#771).]</p></td>
</tr>
<tr class="odd">
<td>Receiving Site:</td>
<td>[Your VAMC Site number.]</td>
</tr>
<tr class="even">
<td>Port location:</td>
<td>[Device used by Instrument Manager to communicate to <strong>V</strong><em>IST</em><strong>A</strong>.]</td>
</tr>
</tbody>
</table>

## Configuration for each Analyzer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Analyzer configuration must be specified on the Instrument Manager using the System Configuration-Configuration Editor-Add/Edit Configuration. (See the Data Innovations Instrument Manager User Manual for further explanation.)

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Configuration Name:</td>
<td>Brief name for the configuration (1-6 alpha- numeric characters).</td>
</tr>
<tr class="odd">
<td>Configuration Description:</td>
<td>Detailed description of the configuration. (1- 25 alpha-numeric characters).</td>
</tr>
<tr class="even">
<td>Driver type:</td>
<td><p>Choose the appropriate driver for the instrument you are interfacing. All</p>
<p>available drivers will be listed for selection.</p></td>
</tr>
</tbody>
</table>

> Test Mapping performed (if necessary). If you use the test code transmitted by the instrument as the UI test code in the DHCP Auto Instrument file (#62.4), no test code mapping will be required.

> Test code mapping is unique to each instrument. If further information is required, refer to the Data Innovations Instrument Manager User Manual.

> Configurations may be copied and assigned to multiple identical instruments. (See the Data Innovations Instrument Manager User Manual for further information.)

> Port connection for each analyzer is defined on the Instrument Manager using the System Configuration Menu option/Connection Assignment. (See the Data Innovations Instrument Manager User Manual for further explanation.)

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Connection Name:</td>
<td><p>A unique one to eight character name must be entered which has a corresponding identical entry in the DHCP AUTO</p>
<p>INSTRUMENT file (#62.4).</p></td>
</tr>
<tr class="odd">
<td>Configuration Name:</td>
<td>Choose entry created using configuration editor</td>
</tr>
<tr class="even">
<td>Device:</td>
<td>This field is similar to the <strong>V</strong><em>IST</em><strong>A</strong> Device file, in that a device name is associated with a physical device and the system address to access that device. Refer to Data Innovations Instrument Manager User Manual for specifications.</td>
</tr>
<tr class="odd">
<td>Days of data to keep:</td>
<td><p>This field is selected by the site. This field determines the number of days in which the orders and results are kept on the Instrument Manager for the specified analyzer. Orders will be purged after the specified number of days and will be unavailable for host query purposes.</p>
<p>Increase this parameter when testing is not performed within the number of days specified.</p></td>
</tr>
<tr class="even">
<td>Destination Line(s):</td>
<td>This field is generally left blank. It is only used when running multiple applications (lab and non-lab).</td>
</tr>
<tr class="odd">
<td>Auto Start on System Start:</td>
<td><p>This field determines if the instrument interface should be started automatically</p>
<p>when the Instrument Manager system is started.</p></td>
</tr>
</tbody>
</table>

## Cluster Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Groups of similar instruments may be "clustered" together. Clustering allows a specimen to be run and reported on any of the analyzers included in the cluster without specifying a particular analyzer. The individual analyzers must have unique entries, and an additional "cluster" entry that contains all tests to be analyzed in the V*IST*A Auto Instrument file (#62.4). Orders are downloaded using the "cluster" entry and results are returned to the individual analyzer entry that performed the test All individual analyzers must be defined in the Instrument Manager as specified above. The Cluster is then created using the System Configuration/Connection Assignment/Cluster Definition option on the Data Innovations Instrument Manager. See the Data Innovations Instrument Manager User Manual for further explanation.

> When changes are made to any configuration, save the changes to an appropriately labeled floppy disk as per instructions in the Data Innovations Instrument Manager User Manual.

# Analyzer Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Each analyzer must be defined in the AUTO INSTRUMENT file (#62.4)

> Refer to technical notes in the Lab Universal Interface Patch Documentation pages 47 through 51 for more detailed information.

## Analyzer Host Communications to Instrument Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Refer to specific analyzer documentation for the required host communication setups.

## Barcode Labels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If barcode labels are utilized for instrument interfacing, the following steps are necessary:

1.  Printer should be installed and functioning.
2.  Barcode capable label routine should be installed and printing barcodes.
3.  Barcodes should be set to YES using field \#5 Barcode Print of the ACCESSION file (#68) for each accession area that has an analyzer utilizing barcodes.
4.  Barcode type should be identified as SHORT (accession number) or LONG (UID) in the Type Of Accession Number field (#092) of the ACCESSION file (#68).

> Each analyzer utilizing barcodes should have barcode capabilities enabled. Barcodes should be functional before interfacing is attempted.

# Confirming Data Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Test Data Stream (Upload Results)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Turn on the Instrument Manager system
2.  Start the individual interface to the analyzer to be tested as per the Data Innovations Instrument Manager User Manual instructions.

> Note Upload testing should always be successfully performed prior to download testing.

### Analyzer to Instrument Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Transmit results from analyzer to Instrument Manager.

> Note This may be accomplished by either running a specimen on the analyzer or retransmitting a prior unverified result.

2.  Watch Instrument Manager System Status screen for incrementing IN Status for the analyzer.

### Interface Manager to V*IST*A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Turn on Transmission Log via HL7 Menu Option

> Note The log will be stored in global TMP("HL",hl7 device name for Instrument Manager,date/time,"SEND" or "REC." The SEND node is what V*IST*A is sending to the Instrument Manager. The REC node is what V*IST*A is receiving from the Instrument Manager.

> Caution Remember to turn off transmission log after communication is successfully established. If transmission log is left on then site incurs danger of disk containing TMP global becoming full. Use above option to purge log, user must be on same system which contains TMP global used to log transmissions.

2.  Make sure Background Job is running.

> Note Check for routine HLLP in the system status. If not running, start job using the V1.5 HL7 option INITIATE BACKGROUND TASK and selecting LAB INTERFACE. If task appears to start then stop, check for availability of V*IST*A DEVICE “NULL DEVICE”, required in addition to device connected to Instrument Manager, also check ability of V*IST*A to open device that the Instrument Manager is connected to.

3.  Message should be sent once background job has been initiated.

### Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Successful receipt of message by V*IST*A HL7 package can be confirmed by viewing the TMP("HL",...global. If a message is rejected by the HL7 package due to transmission problems, the V*IST*A HL7 package will send an N21 message that indicates a checksum problem with the message.

> This usually indicates a possible line noise problem. Recheck line connections.

> If the message is successfully received by the V*IST*A HL7 package it will then pass the message off to the Laboratory package. The Laboratory package will process the message and create an MSA message segment. This will show in the transmission log in the SEND node. The MSA segment will have the following:

- AA - Application Accept
- AR - Application Reject

> If AA, then the laboratory package will process the message. Any problems detected in processing the message will be logged in the "debug log" if the site has set “DEBUG LOG” on in File \#62.48, LA7 MESSAGE CONFIGURATION. This log is

> viewed using the LA7 PRINT LAB UI ERROR LOG option.

> If AR, then the laboratory package could not find the entry in File \#62.48 that will process this message. Review the field "REMOTE ID" for entry "UNIVERSAL INTERFACE" and for correct spelling. Corresponding entries in Files \#770, \#771 and on Instrument Manager for sending application/facility and receiving application/facility need to be uniform.

> If you see that the message is not transmitting, review file setups and check for presence of routines on all the systems. If routines are mapped, check to see if appropriate changes have been made for mapping. Review entries in the Instrument Manager.

## Test Data Stream (Download Orders)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Accession test specimen or utilize specimen that has been accessioned but not yet assigned to a load/work list.
2.  For testing of bidirectional load/work list download, build a load/work list for the analyzer to be tested.

> All processes for testing upload should remain active.

### Data-V*IST*A to Instrument Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  For auto download, a message should be created upon accessioning.
2.  Download load/work list for testing of bidirectional load/work list download.

### Instrument Manager to Analyzer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Messages should be sent from the Instrument Manager to the analyzer including tests to be run on the specimen and may include specimen ID and location on the analyzer if applicable. If unsuccessful, the analyzers host computer will flag an error and reject the request.

### Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Watch TMP("HL"...global for messages. If messages are not created, utilize the LA7 PRINT LAB UI ERROR LOG option to review errors as listed above. Review the lab files for correct and complete entries Watch for spelling. If mapping was performed on the Instrument Manager, review for correct and complete entries and spelling. If the message is not transmitting, review file setups and checks for presence of routines on all the systems. If routines are mapped, check to see if appropriate changes have been made for mapping.

> If checking data from the Instrument Manager to the Analyzer, check Host Configuration Parameters on your analyzer.

> For more information regarding HL7 messages, refer to the Laboratory Universal Interface Patch Documentation pages 65 through 83.

# Training

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Most of the changes present will be transparent to the lab user. Individuals that are responsible for set up, training and workflow should be informed of any new capabilities. Be aware that the operation of the analyzers may change, especially when moving from a unidirectional to a bidirectional mode.

> If the Instrument Manager is located in the laboratory, users may be trained in the following operations of the Instrument Manager:

- Starting/Stopping of individual interfaces.
- Monitoring System Status screen on the Instrument Manager for changes in the IN and SEND queues that would indicate transmission and receipt of messages.

> IRMS should be aware that the interface should be re-started after any system downtime. IRM can task multiple background jobs. Only one job will run at a time. If the background job should stop or the system rebooted, then TaskMan will automatically start one of the waiting tasks.

> The Laboratory Information Manager (LIM) should be assigned the LA7 MAIN MENU (Lab Universal Interface menu).

> It is recommended that the error log be reviewed once a day (on screen or printed) using the option LA7 PRINT LAB UI ERROR LOG.

# Appendix A: Sample Instrument

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Clinitek 100

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load/Work List:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NAME: CLINITEK-100 LOAD TRANSFORM: UNIVERSAL TYPE: TRAY,CUP CUPS PER TRAY: 10

> FULL TRAY'S ONLY: NO EXPAND PANELS ON PRINT: NO

> VERIFY BY: ACCESSION SUPPRESS SEQUENCE \#: NO

> INCLUDE UNCOLLECTED ACCESSIONS: NO ADDITIONAL LAB TESTS: Instrument Set

> Up - Urinalysis

> PROFILE: URINALYSIS ACCESSION AREA: URINALYSIS

> TEST: URINALYSIS BUILD NAME ONLY: NO

> TEST: T.REACTION,URINE BUILD NAME ONLY: NO

> TEST: URINE MICROSCOPIC BUILD NAME ONLY: NO TRAY \#: 1

> CUP or SEQUENCE \#: 1 CONTROL: CLINITEK QC LEVEL 1

> CUP or SEQUENCE \#: 2 CONTROL: CLINITEK QC LEVEL 2

> WKLD METHOD: CLINITEK 100 WKLD CODE METHOD NAME: CLINITEK 100 WKLD CODE SUFFIX: .4339 MAJOR ACCESSION AREA: URINALYSIS

### Auto Instrument Setup:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NUMBER: 18 NAME: CL100-IM

> LOAD/WORK LIST: CLINITEK-100

> ENTRY for LAGEN ROUTINE: Accession cross-reference CROSS LINKED BY: ID

> MESSAGE CONFIGURATION: UNIVERSAL INTERFACE

> METHOD: CLT100 DEFAULT ACCESSION AREA: URINALYSIS OVERLAY DATA: YES

> NUMBER: 1 TEST: URINE COLOR

> UI TEST CODE: URINE COLOR ROUTINE STORAGE: TV(683,1)

> CONVERT RESULT TO REMARK: NO

> NUMBER: 2 TEST: URINE CLARITY

> UI TEST CODE: URINE CLARITY ROUTINE STORAGE: TV(162,1)

> CONVERT RESULT TO REMARK: NO

> NUMBER: 3 TEST: SPECIFIC GRAVITY (URINES) UI TEST CODE: SPECIFIC GRAVITY (URINES)

> ROUTINE STORAGE: TV(685,1) NUMBER OF DECIMAL PLACES: 3 NUMBER: 4 TEST: URINE PH

> UI TEST CODE: URINE PH ROUTINE STORAGE: TV(692,1) NUMBER OF DECIMAL PLACES: 1

> NUMBER: 7 TEST: URINE KETONES

> PARAM 1: S LA7VAL=\$S(LA7VAL="Negative":"Negative",1:\$P("TRACE;SMALL;MOD;LARGE",";",LA7VA L+1)) UI TEST CODE: URINE KETONES

> ROUTINE STORAGE: TV(689,1) CONVERT RESULT TO REMARK: NO WKLD METHOD: CLINITEK 100 WKLD CODE METHOD NAME:

> CLINITEK 100

> WKLD CODE SUFFIX: .4339

## Beckman CX Series

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load/Work List:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NAME: CX7M TYPE: SEQUENCE/BATCH

CUPS PER TRAY: 0 FULL TRAY'S ONLY: NO

EXPAND PANELS ON PRINT: NO VERIFY BY: ACCESSION

> SUPPRESS SEQUENCE \#: YES INCLUDE UNCOLLECTED ACCESSIONS: NO

> SHORT TEST LIST: YES

> PROFILE: CX7 ACCESSION AREA: CHEMISTRY

> TEST: GLUCOSE (PLASMA/SERUM) BUILD NAME ONLY: NO

> TEST: UREA NITROGEN BUILD NAME ONLY: NO

> TEST: CREATININE BUILD NAME ONLY: NO

> TEST: CHEM 7 BUILD NAME ONLY: YES

> TEST: CHEM 3 BUILD NAME ONLY: YES

> TEST: ELECTROLYTES BUILD NAME ONLY: YES

> TEST: CREATININE CLEARANCE BUILD NAME ONLY: YES

> TEST: GLUCOSE, FLUID BUILD NAME ONLY: NO

> TEST: PROTEIN,TOTAL (FLUID) BUILD NAME ONLY: NO

> Specimens to EXCLUDE!: BLOOD

> PROFILE: HDL ACCESSION AREA: CHEMISTRY

> TEST: HDL CHOLESTEROL BUILD NAME ONLY: NO

> TEST: LDL CHOLESTEROL BUILD NAME ONLY: NO

> TEST: LDL CALCULATED BUILD NAME ONLY: NO

> PROFILE: DAU ACCESSION AREA: CHEMISTRY

> TEST: AMPHETAMINES BUILD NAME ONLY: NO

> TEST: BENZODIAZEPINES BUILD NAME ONLY: NO TEST: ZDRUGS OF ABUSE - URINE SCREEN BUILD NAME ONLY: YES

> WKLD METHOD: SYNCHRON CX7 WKLD CODE METHOD NAME: SYNCHRON CX7 WKLD CODE SUFFIX: .4009 MAJOR ACCESSION AREA: CHEMISTRY

> LAB SUBSECTION: SYNCHRON BENCH

### Auto Instrument Setup:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NUMBER: 16 NAME: CX5-IM

> LOAD/WORK LIST: CX7M

> ENTRY for LAGEN ROUTINE: Accession cross-reference CROSS LINKED BY: ID

> MESSAGE CONFIGURATION: UNIVERSAL INTERFACE METHOD: CX5

> DEFAULT ACCESSION AREA: CHEMISTRY OVERLAY DATA: YES NUMBER: 1 TEST: UREA NITROGEN

> UI TEST CODE: O5C

> ROUTINE STORAGE: TV(3,1) NUMBER OF DECIMAL PLACES: 0 DOWNLOAD TO INSTRUMENT: YES

> NUMBER: 2 TEST: GLUCOSE

> UI TEST CODE: 06C

> ROUTINE STORAGE: TV(608085,1) NUMBER OF DECIMAL PLACES: 0 DOWNLOAD TO INSTRUMENT: YES

> NUMBER: 3 TEST: CREATININE

> UI TEST CODE: 03C

> ROUTINE STORAGE: TV(4,1) NUMBER OF DECIMAL PLACES: 1

> DOWNLOAD TO INSTRUMENT: YES

### Auto Instrument Setup (continued):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NUMBER: 37 TEST: HDL CHOLESTEROL UI TEST CODE: 83A

> ROUTINE STORAGE: TV(80,1) NUMBER OF DECIMAL PLACES: 0 DOWNLOAD TO INSTRUMENT: NO

> NUMBER: 38 TEST: LDL CHOLESTEROL UI TEST CODE: LDL(CALC)

> ROUTINE STORAGE: TV(291,1) NUMBER OF DECIMAL PLACES: 0 DOWNLOAD TO INSTRUMENT: NO

> NUMBER: 40 TEST: AMPHETAMINES

> PARAM 1: S LA7VAL=\$S(LA7VAL=1:"POS",LA7VAL=0:"NEG",1:"") S:LA7VAL="" LA7VAL="

> ",LA7XFORM(3)=0 UI TEST CODE: 84A

> ROUTINE STORAGE: TV(26,1) DOWNLOAD TO INSTRUMENT:YES NUMBER: 41 TEST: BENZODIAZEPINES

> PARAM 1: S LA7VAL=\$S(LA7VAL=1:"POS",LA7VAL=0:"NEG",1:"") S:LA7VAL="" LA7VAL="

> ",LA7XFORM(3)=0 UI TEST CODE: 86A

> ROUTINE STORAGE: TV(216,1) DOWNLOAD TO INSTRUMENT:YES METH NAME: CX5-IM

> FILE BUILD ENTRY: EN FILE BUILD ROUTINE: LA7UID

> SEND TRAY/CUP LOCATION: yes AUTO DOWNLOAD: NO

> WKLD METHOD: SYNCHRON CX5CE WKLD CODE METHOD NAME: SYNCHRON CX5CE

> WKLD CODE SUFFIX: .4576

> NUMBER: 15 NAME: CX7-IM

> LOAD/WORK LIST: CX7M

> ENTRY for LAGEN ROUTINE: Accession cross-reference CROSS LINKED BY: ID

> MESSAGE CONFIGURATION: UNIVERSAL INTERFACE METHOD: CX7

> DEFAULT ACCESSION AREA: CHEMISTRY OVERLAY DATA: YES NUMBER: 1 TEST: GLUCOSE

> UI TEST CODE: 06C

> ROUTINE STORAGE: TV(608085,1) NUMBER OF DECIMAL PLACES: 0 DOWNLOAD TO INSTRUMENT: YES

> NUMBER: 2 TEST: UREA NITROGEN

> UI TEST CODE: 05C

> ROUTINE STORAGE: TV(3,1) NUMBER OF DECIMAL PLACES: 0 DOWNLOAD TO INSTRUMENT: YES

> NUMBER: 3 TEST: CREATININE

> UI TEST CODE: 03C ROUTINE STORAGE: TV(4,1) NUMBER OF DECIMAL PLACES: 1 DOWNLOAD TO INSTRUMENT: YES

> NUMBER: 25 TEST: HDL CHOLESTEROL UI TEST CODE: 83A

> ROUTINE STORAGE: TV(80,1) NUMBER OF DECIMAL PLACES: 0 DOWNLOAD TO INSTRUMENT: NO

> NUMBER: 27 TEST: LDL CHOLESTEROL UI TEST CODE: LDL(CALC)

> ROUTINE STORAGE: TV(291,1) NUMBER OF DECIMAL PLACES: 0 DOWNLOAD TO INSTRUMENT: NO

> METH NAME: 195

> FILE BUILD ENTRY: EN FILE BUILD ROUTINE: LA7UID

> SEND TRAY/CUP LOCATION: yes AUTO DOWNLOAD: NO

> WKLD METHOD: SYNCHRON CX7 WKLD CODE METHOD NAME: SYNCHRON CX7

> WKLD CODE SUFFIX: .4009

### Auto Instrument Setup (continued):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NUMBER: 22 NAME: CX-CLUS

> LOAD/WORK LIST: CX7M

> ENTRY for LAGEN ROUTINE: Accession cross-reference CROSS LINKED BY: ID

> MESSAGE CONFIGURATION: UNIVERSAL INTERFACE METHOD: CX5

> DEFAULT ACCESSION AREA: CHEMISTRY OVERLAY DATA: YES NUMBER: 1 TEST: UREA NITROGEN

> UI TEST CODE: O5C

> ROUTINE STORAGE: TV(3,1) NUMBER OF DECIMAL PLACES: 0 DOWNLOAD TO INSTRUMENT: YES

> NUMBER: 2 TEST: GLUCOSE

> UI TEST CODE: 06C

> ROUTINE STORAGE: TV(608085,1) NUMBER OF DECIMAL PLACES: 0 DOWNLOAD TO INSTRUMENT: YES

> NUMBER: 3 TEST: CREATININE

> UI TEST CODE: 03C

> ROUTINE STORAGE: TV(4,1) NUMBER OF DECIMAL PLACES: 1 DOWNLOAD TO INSTRUMENT: YES

> NUMBER: 37 TEST: HDL CHOLESTEROL UI TEST CODE: 83A

> ROUTINE STORAGE: TV(80,1) NUMBER OF DECIMAL PLACES: 0 DOWNLOAD TO INSTRUMENT: NO

> NUMBER: 38 TEST: LDL CHOLESTEROL UI TEST CODE: LDL(CALC)

> ROUTINE STORAGE: TV(291,1) NUMBER OF DECIMAL PLACES: 0 DOWNLOAD TO INSTRUMENT: NO

> NUMBER: 40 TEST: AMPHETAMINES

> PARAM 1: S LA7VAL=\$S(LA7VAL=1:"POS",LA7VAL=0:"NEG",1:"") S:LA7VAL="" LA7VAL="

> ",LA7XFORM(3)=0 UI TEST CODE: 84A ROUTINE STORAGE: TV(26,1) DOWNLOAD TO INSTRUMENT:

> YES

> NUMBER: 41 TEST: BENZODIAZEPINES PARAM 1: S LA7VAL=\$S(LA7VAL=1:"POS",LA7VAL=0:"NEG",1:"")

> S:LA7VAL="" LA7VAL="

> ",LA7XFORM(3)=0 UI TEST CODE: 86A ROUTINE STORAGE: TV(216,1) DOWNLOAD TO INSTRUMENT:

> YES

> METH NAME: CX5-IM

> FILE BUILD ENTRY: EN FILE BUILD ROUTINE: LA7UID

> SEND TRAY/CUP LOCATION: yes AUTO DOWNLOAD: YES WKLD METHOD: SYNCHRON CX7 WKLD CODE METHOD NAME:

> SYNCHRON CX7

> WKLD CODE SUFFIX: .4009

### CX Host Communication Parameters:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enable Barcode type that prints on label printer. Host Communications:

> Mode: Bidirectional Baud Rate: 9600 Data Bits: 8 Stop Bits: 1 Parity: None Device ID: 0

> Flow Control: XON/XOFF For Query Mode:

> Stream 700 Special Functions /Func 2 Host Set-up = ON Stream 701 Sample/Cup/Func 6 Host Query= ON Stream 702 Results/Func 3 Test Results= ON

> Stream 703 Instrument Status /Func 2 Bidirectional Start Up = ON.

## Modulus Differential Counter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load/Work List:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NAME: DIFFERENTIAL (BLOOD) LOAD TRANSFORM: UNIVERSAL TYPE: TRAY,CUP CUPS PER TRAY: 30

> FULL TRAY'S ONLY: NO EXPAND PANELS ON PRINT: NO

> VERIFY BY: ACCESSION SUPPRESS SEQUENCE \#: NO INCLUDE UNCOLLECTED ACCESSIONS: NO

> PROFILE: DIFFERENTIAL (BLOOD) ACCESSION AREA: HEMATOLOGY TEST: DIFFERENTIAL (BLOOD) BUILD NAME ONLY: YES

> TEST: WBC SCAN BUILD NAME ONLY: NO

> TEST: SEGS BUILD NAME ONLY: NO

> TEST: BANDS BUILD NAME ONLY: NO

> TEST: POLYCHROMASIA BUILD NAME ONLY: NO

> TEST: NUCLEATED RBC/100WBC BUILD NAME ONLY: NO

> PROFILE: SCAN COMPLETE ACCESSION AREA:HEMATOLOGY

> TEST: SEGS BUILD NAME ONLY: YES

> TEST: BANDS BUILD NAME ONLY: YES

> TEST: PLT (ESTM) BUILD NAME ONLY: YES

> TEST: POLYCHROMASIA BUILD NAME ONLY: YES

> TEST: HYPOCHROMIA BUILD NAME ONLY: YES

> TEST: DIFFERENTIAL (BLOOD) BUILD NAME ONLY: YES

> TEST: SCAN-COMPLETE BUILD NAME ONLY: NO

> PROFILE: RBC MORPHOLOGY ACCESSION AREA: HEMATOLOGY

> TEST: PLT (ESTM) SPECIMEN: BLOOD BUILD NAME ONLY: YES

> TEST: RBC SCAN SPECIMEN: BLOOD BUILD NAME ONLY: YES

> WKLD METHOD: MANUAL WKLD CODE METHOD NAME: MANUAL

> WKLD CODE SUFFIX: .3000 MAJOR ACCESSION AREA: HEMATOLOGY

### Auto Instrument Setup:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NUMBER: 13 NAME: DIFF1-IM

> LOAD/WORK LIST: DIFFERENTIAL (BLOOD)

> ENTRY for LAGEN ROUTINE: Accession cross-reference CROSS LINKED BY: ID

> MESSAGE CONFIGURATION: UNIVERSAL INTERFACE METHOD: MODULUS

> DEFAULT ACCESSION AREA: HEMATOLOGY OVERLAY DATA: YES NUMBER: 1 TEST: EOSINOPHILS

> PARAM 1: S LA7VAL=+LA7VAL UI TEST CODE: EOSINOPHILS ROUTINE STORAGE: TV(398,1)

> NUMBER: 14 TEST: POLYCHROMASIA

> PARAM 1: S LA7VAL=LA7VAL\_"+" UI TEST CODE:POLYCHROMASIA ROUTINE STORAGE: TV(412,1)

> NUMBER: 18 TEST: PLT (ESTM)

> PARAM 1: S LA7VAL=\$S(LA7VAL="0":"ADQ",LA7VAL="1":"DEC", LA7VAL="2":"INC",1:LA7VAL)

> UI TEST CODE: PLT (ESTM) ROUTINE STORAGE: TV(405,1)

> NUMBER: 30 TEST: WBC SCAN

> PARAM 1: S LA7VAL=\$S(LA7VAL="1":"OK",1:LA7VAL)

> UI TEST CODE: WBC SCAN ROUTINE STORAGE:TV(608029,1)

### Auto Instrument Setup (continued):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NUMBER: 33 TEST: LARGE PLATELETS PARAM 1: S

> LA7VAL=\$S(LA7VAL="1":"OCC",LA7VAL="2":"MODERATE",LA7VAL="3":"MANY",1:LA7VAL) UI TEST CODE: LARGE PLATELETS

> ROUTINE STORAGE: TV(608050,1)

> INTERFACE NOTES: PIN CONFIGURATION: 3(GREEN)...7(RED)...ONLY.

## Coulter STKS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load/Work List:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NAME: COULTER STKS LOAD TRANSFORM: UNIVERSAL TYPE: SEQUENCE/BATCH CUPS PER TRAY: 200

> FULL TRAY'S ONLY: NO EXPAND PANELS ON PRINT: NO

> VERIFY BY: ACCESSION SUPPRESS SEQUENCE \#: NO INCLUDE UNCOLLECTED ACCESSIONS: NO SHORT TEST LIST: YES

> ADDITIONAL LAB TESTS: Instrument Set Up - Hematology

> PROFILE: COULTER CBC ACCESSION AREA: HEMATOLOGY TEST: WBC SPECIMEN: BLOOD BUILD NAME ONLY: NO

> TEST: RBC SPECIMEN: BLOOD BUILD NAME ONLY: NO

> TEST: CBC SPECIMEN: BLOOD BUILD NAME ONLY: YES Specimens to EXCLUDE!: PERITONEAL FLUID

> WKLD METHOD: STKS WKLD CODE METHOD NAME: STKS

> WKLD CODE SUFFIX: .4191 MAJOR ACCESSION AREA: HEMATOLOGY

### Auto Instrument Setup:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NUMBER: 11 NAME: STKS-IM

> LOAD/WORK LIST: COULTER STKS

> ENTRY for LAGEN ROUTINE: Accession cross-reference CROSS LINKED BY: IDE

> MESSAGE CONFIGURATION: UNIVERSAL INTERFACE

> METHOD: STKS DEFAULT ACCESSION AREA: HEMATOLOGY OVERLAY DATA: YES

> NUMBER: 1 TEST: WBC

> UI TEST CODE: WBC

> ROUTINE STORAGE: TV(384,1) NUMBER OF DECIMAL PLACES: 1 NUMBER: 2 TEST: RBC

> METH NAME: STKS-IM

> INTERFACE NOTES: Timeout (secs) 9 Baud rate 9600 Parity none

> Stop Bits 1 Handshake Yes Block size 256 Enable Spooler Yes Replace NULL by SP Yes

> AUTO DOWNLOAD: NO

## Uro-Comp for Clinitek 200

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load/Work List:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NAME: CLINITEK-200 LOAD TRANSFORM: UNIVERSAL TYPE: TRAY,CUP CUPS PER TRAY: 10

> FULL TRAY'S ONLY: NO EXPAND PANELS ON PRINT: NO

> VERIFY BY: ACCESSION SUPPRESS SEQUENCE \#: NO INCLUDE UNCOLLECTED ACCESSIONS: NO PROFILE: URINALYSIS

> ACCESSION AREA: URINALYSIS

> TEST: URINALYSIS BUILD NAME ONLY: NO

> TEST: T.REACTION,URINE BUILD NAME ONLY: NO

> TEST: URINE MICROSCOPIC BUILD NAME ONLY: NO

> TEST: URINE COLOR BUILD NAME ONLY: YES

> TEST: URINE CLARITY BUILD NAME ONLY: YES

> TEST: URINE GLUCOSE BUILD NAME ONLY: YES

> TEST: URINE WBC/HPF BUILD NAME ONLY: YES

> TEST: URINE RBC/HPF BUILD NAME ONLY: YES

> TEST: SQUAMOUS EPITHELIAL BUILD NAME ONLY: YES

> EST: AMORPHOUS CRYSTALS BUILD NAME ONLY: YES TRAY \#: 1

> CUP or SEQUENCE \#: 1 CONTROL: CLINITEK QC LEVEL 1

> CUP or SEQUENCE \#: 2 CONTROL: CLINITEK QC LEVEL 2

> WKLD METHOD: CLINITEK 200 WKLD CODE METHOD NAME: CLINITEK 200 WKLD CODE SUFFIX: .3100 MAJOR ACCESSION AREA: URINALYSIS

### Auto Instrument Setup:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NUMBER: 12 NAME: URO-IM

> LOAD/WORK LIST: CLINITEK-200

> ENTRY for LAGEN ROUTINE: Accession cross-reference CROSS LINKED BY: ID

> MESSAGE CONFIGURATION: UNIVERSAL INTERFACE METHOD: UROC/CLINT

> DEFAULT ACCESSION AREA: URINALYSIS OVERLAY DATA: YES NUMBER: 1 TEST: URINE COLOR

> PARAM 1: S LA7VAL=\$P("YELLOW;PALE YEL;STRAW;AMBER;DK.AMBER;ORANGE;RED;BROWN;BLUE;GREEN",";",LA7VAL+1) UI TEST CODE: URINE COLOR

> ROUTINE STORAGE: TV(683,1)

> NUMBER: 2 TEST: URINE CLARITY

> PARAM 1: S LA7VAL=\$P("CLEAR;HAZY;CLOUDY;TURBID;FLOC;SMOKEY;MUCOID",";",LA7VAL+1) UI TEST CODE: URINE CLARITY

> ROUTINE STORAGE: TV(162,1)

> NUMBER: 3 TEST: SPECIFIC GRAVITY (URINES) UI TEST CODE: SPECIFIC GRAVITY (URINES)

> ROUTINE STORAGE: TV(685,1) NUMBER OF DECIMAL PLACES: 3 NUMBER: 5 TEST: URINE PROTEIN

> PARAM 1: S LA7VAL=\$S(LA7VAL=0:"NEG",LA7VAL=1:"TRACE",1:LA7VAL) UI TEST CODE: URINE PROTEIN ROUTINE STORAGE: TV(691,1)

> NUMBER OF DECIMAL PLACES: 0

### Auto Instrument Setup (continued):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NUMBER: 6 TEST: URINE GLUCOSE

> PARAM 1: S LA7VAL=\$S(LA7VAL=0:"NEG",1:LA7VAL)

> UI TEST CODE: URINE GLUCOSE ROUTINE STORAGE: TV(690,1)

> NUMBER OF DECIMAL PLACES: 0

> NUMBER: 7 TEST: URINE KETONES

> PARAM 1: S LA7VAL=\$S(LA7VAL="\>80":"LARGE",1:\$P("NEG;TRACE;SMALL;MOD",";",LA7VAL+1)) UI TEST CODE: URINE KETONES

> ROUTINE STORAGE: TV(689,1)

NUMBER: 8 TEST: URINE BILIRUBIN

PARAM 1: S LA7VAL=\$P("NEG;;SMALL;MOD;LARGE",";",LA7VAL+1)

> UI TEST CODE: URINE BILIRUBIN ROUTINE STORAGE: TV(688,1) NUMBER: 10 TEST: NITRITE, URINE

> PARAM 1: S LA7VAL=\$S(LA7VAL=0:"NEG",LA7VAL=6:"POS",1:LA7VAL)

> UI TEST CODE: NITRITE, URINE ROUTINE STORAGE: TV(795,1) NUMBER: 13 TEST: URINE WBC/HPF

> PARAM 1: S LA7VAL=\$P("NONE;0-4;5-10;10-20;20-30;30-50;50- 100;100+;TNTC",";",LA7VAL+1) UI TEST CODE: URINE WBC/HPF

> ROUTINE STORAGE: TV(693,1)

> NUMBER: 15 TEST: SQUAMOUS EPITHELIAL PARAM 1: S LA7VAL=\$P("NONE;OCC;FEW;MOD;MANY",";",LA7VAL+1)

> UI TEST CODE: SQUAMOUS EPITHELIAL ROUTINE STORAGE: TV(777,1)

> INTERFACE NOTES: Clinitek 200 interfaced through a URO-Comp PIN CONFIGURATION: 3(GREEN)...7(RED)

## Axsym

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load/Work List:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NAME: AXSYM TYPE: SEQUENCE/BATCH CUPS PER TRAY: 0 FULL TRAY'S ONLY: NO

> VERIFY BY: ACCESSION INCLUDE UNCOLLECTED ACCESSIONS: NO

> PROFILE: TDM ACCESSION AREA: SPECIAL CHEMISTRY

> TEST: DIGOXIN BUILD NAME ONLY: NO

> PROFILE: PSA ACCESSION AREA: SPECIAL CHEMISTRY TEST: PROSTATE SPECIFIC ANTIGEN BUILD NAME ONLY: NO

> WKLD METHOD: ABBOTT AXSYM WKLD CODE METHOD NAME: ABBOTT AXSYM WKLD CODE SUFFIX: .4455 MAJOR ACCESSION AREA: CHEMISTRY LAB SUBSECTION: SPECIAL CHEMISTRY

### Auto Instrument Setup:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NUMBER: 20 NAME: AXSYM

> LOAD/WORK LIST: AXSYM

> ENTRY for LAGEN ROUTINE: Accession cross-reference CROSS LINKED BY: ID

> MESSAGE CONFIGURATION: UNIVERSAL INTERFACE METHOD: AXSYM

> DEFAULT ACCESSION AREA: SPECIAL CHEMISTRY OVERLAY DATA: YES

> NUMBER: 1 TEST: PROSTATE SPECIFIC ANTIGEN UI TEST CODE: 441 ROUTINE STORAGE: TV(608312,1) NUMBER OF DECIMAL PLACES: 1 DOWNLOAD TO INSTRUMENT: NO

> NUMBER: 2 TEST: DIGOXIN UI TEST CODE: 601 ROUTINE STORAGE: TV(608060,1)

> NUMBER OF DECIMAL PLACES: 1 DOWNLOAD TO INSTRUMENT: YES METH NAME: AXSYM

> FILE BUILD ENTRY: EN FILE BUILD ROUTINE: LA7UID SEND TRAY/CUP LOCATION: yes AUTO DOWNLOAD: YES

> WKLD METHOD: ABBOTT AXSYM WKLD CODE METHOD NAME: ABBOTT AXSYM WKLD CODE SUFFIX: .4455

> Note UI test codes are the assay numbers for each test. Test codes may be found using the axsym instrument terminal, configuration option, or assay parameters.

> At this time, the Digoxins are set to run Host/Query. The PSAs are only run once a week and are set up to run Unidirectional and options for Host Query and Auto-ID are turned off. Only Transmit to Host is left on.

> On the instrument:

> Main Menu:

> Configuration:

> General:

> 6, 26, 28, and 29 set to on.

> Sample Bar Code: (We use the LRLABEL routine for Intermec 4100 10 part label)

> Code 39

> Enable Symbology: YES

> Use Checksum: NO

> Ports:

> Host Port: Parity- NONE Baud Rate- 9600

> Data Bits- 8

> Stop Bits- 1

> Pin Configuration:

> STD RS232:

> AXSYM V*IST*A

> Pin 1----------Shield 1 \|\|

> Pin 2----------Output-----\\ /---\>\> 2

> \\

> /\\

> Pin 3\<\<--------Input------/ \\ \>\> 3

> Pin 7----------Ground 7

> Pins 2 and 3 are "crossed" in this twisted pair diagram.

> Further documentation may be found in patch LR\*5.2\*11 SEQ 6.

> The Data Innovations Instrument Manager will automatically default the LRDFN as the patient ID. You must go into Configuration Edit on the Instrument Manager and change the PID to SSN.