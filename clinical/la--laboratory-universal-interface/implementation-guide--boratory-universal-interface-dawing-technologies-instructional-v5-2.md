---
title: "Laboratory: Universal Interface Dawing Technologies Instructional Implementation Guide Version 5.2"
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
  - 60
  - 770
  - 771
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - strong
  - blockquote
  - table
  - class
  - contents
  - even
  - dawning
  - width
  - style
  - configuration
page_count: 0
word_count: 5342
section_count: 30
table_count: 6
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/dawning.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/dawning.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=120"
---

> ![](laboratory-universal-interface-dawing-technologies-instructional-implementation-/001.png)

> LABORATORY DAWNING TECHNOLOGIES

> INSTRUCTIONAL IMPLEMENTATION GUIDE

> VERSION 5.2

> March 1997

> Office of Employee Education Salt Lake Education Center Clin2 Customer Service

> Lab ADPAC Training Advisory Council
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Required Documentation](#required-documentation)
  - [Required Patches](#required-patches)
  - [Assistance](#assistance)
  - [Special Instructions for the First-Time Computer User](#special-instructions-for-the-first-time-computer-user)
  - [Special Notations](#special-notations)
  - [On-line Help](#on-line-help)
- [VISTA Site Preparation](#vista-site-preparation)
  - [Wiring Setup](#wiring-setup)
    - [Selecting Port](#selecting-port)
    - [Cable Connections](#cable-connections)
    - [Definitions for 25-pin Male Connector](#definitions-for-25-pin-male-connector)
  - [Terminal Setup](#terminal-setup)
- [Dawning Technologies PC Installation](#dawning-technologies-pc-installation)
  - [Vendor Installation](#vendor-installation)
  - [Site Installation](#site-installation)
- [Testing Communication](#testing-communication)
- [VISTA Configuration](#vista-configuration)
  - [DEVICE file (#3.5)](#device-file-35)
  - [HL7 DHCP APPLICATION PARAMETER file (#771)](#hl7-dhcp-application-parameter-file-771)
  - [HL7 NON-DHCP APPLICATION PARAMETER file (#770)](#hl7-non-dhcp-application-parameter-file-770)
  - [LA7 MESSAGE PARAMETER CONFIGURATION file (#62.48)](#la7-message-parameter-configuration-file-6248)
  - [AUTO INSTRUMENT file (#62.4)](#auto-instrument-file-624)
  - [Initiating Background HL7 Task](#initiating-background-hl7-task)
    - [Notes](#notes)
- [Dawning Technologies System Configuration](#dawning-technologies-system-configuration)
  - [MPCUP Setup](#mpcup-setup)
    - [Configuration](#configuration)
    - [Notes](#notes-1)
  - [ResultNet Configuration](#resultnet-configuration)
    - [Configuration for Host Port (COM1 port):](#configuration-for-host-port-com1-port)
    - [HOST](#host)
    - [530MPC Instrument Port Configuration](#530mpc-instrument-port-configuration)
    - [Quick Reference Guide](#quick-reference-guide)
  - [CONFIG.SYS](#configsys)
- [Confirming Data Transmission](#confirming-data-transmission)
  - [Upload (analyzer---\>Dawning---\>VISTA)](#upload-analyzer-dawning-vista)
  - [Download (VISTA ---\>Dawning---\>analyzer)](#download-vista-dawning-analyzer)
- [Troubleshooting](#troubleshooting)
  - [After a VISTA Crash:](#after-a-vista-crash)
  - [Pop-up Data Interpreter Error Messages](#pop-up-data-interpreter-error-messages)
- [Maintenance](#maintenance)
  - [ResultNet/MPCUP Software](#resultnetmpcup-software)
  - [530MPC Card Software](#530mpc-card-software)
  - [Printing Documentation of new 530MPC software](#printing-documentation-of-new-530mpc-software)
- [General File Maintenance](#general-file-maintenance)
  - [Weekly](#weekly)
  - [Monthly](#monthly)
  - [Semi-Annually](#semi-annually)
> This implementation guide provides you with information on how to setup and configure the Dawning Technologies Personal Computer (DPC). Information is divided into two main categories.
- V*IST*A Site Preparation
- DPC Installation
> In this document we are using our new name Veterans Health Information Systems and Technology Architecture (V*IST*A) instead of Decentralized Hospital Computer Program (DHCP). The files that have DHCP as part of their name remains the same.

## Required Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Laboratory Universal Interface (UI) Patch Documentation

## Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Laboratory Universal Interface Patches (LA\*5.2\*17 and LR\*5.2\*65)

## Assistance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For technical assistance, you may contact Dawning Technologies at (800) 332- 0499. For software upgrades, contact the Bulletin Board System (BBS) at (716) 223-0174.

## Special Instructions for the First-Time Computer User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you are not very familiar with V*IST*A software applications, we recommend that you study the DHCP User’s Guide to Computing. This orientation guide is a comprehensive handbook benefiting first time users of any V*IST*A application. The purpose of the introductory material is to help you become familiar with basic computer terms and the components of a computer. The guide is reproduced and distributed periodically by the Kernel Development Group. To request a copy, contact your local Information Resources Management (IRM) staff.

## Special Notations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In this manual, the user’s response is bolded. The bolded part of the entry is the letter or letters that must be typed so that the computer can identify the response. In most cases, you need only enter the first few letters. This increases speed and accuracy.

> Every response you type in must be followed by pressing the Return key (or Enter key for some keyboards). Whenever the Return or Enter key should be pressed, you will see the symbol \<RET\>. This symbol is not shown but is implied if there is bolded input.

> Within the examples representing actual terminal dialogues, editorial comments are enclosed in brackets and will not appear on the screen.

> To stop what you are doing, enter an up-arrow (^). You may use the up-arrow at almost any prompt to terminate the line of questioning and return to the previous level in the routine. Continue entering up-arrows to completely exit the system.

## On-line Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> On-line help is available at almost any prompt in the software. Entering a question mark (?) will provide information to help you answer the prompt. In some instances entering two or three question marks will provide even further information.

# V*IST*A Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The DPC can be located in the Laboratory, or in the Information Resource Management (IRM) service, dependent on availability of space and local policy.

## Wiring Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This is the wiring setup from V*IST*A system to the location of DPC.

### Selecting Port

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The IRM does the setup by using a dedicated line that emulates a printer setup.

> Example Dec Server 500 Port Setting

> Note Dawning PC comes configured at 9600 baud.

> Port xxx: Dawning Technologies Server: DSVxx

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 24%" />
<col style="width: 25%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>Character Size:</th>
<th>8</th>
<th>Input Speed:</th>
<th>9600</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Flow Control:</td>
<td>XON</td>
<td>Output:</td>
<td>9600</td>
</tr>
<tr class="even">
<td>Parity:</td>
<td>None</td>
<td>Modem Control:</td>
<td>Disabled</td>
</tr>
<tr class="odd">
<td>Stop Bits:</td>
<td>Dynamic</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Access:</td>
<td>Remote</td>
<td>Local Switch:</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Backward Switch:</td>
<td>None</td>
<td>Name:</td>
<td>LC-8-14</td>
</tr>
<tr class="even">
<td>Break:</td>
<td>Disabled</td>
<td>Session Limit:</td>
<td>1</td>
</tr>
<tr class="odd">
<td>Forward Switch:</td>
<td>None</td>
<td>Type:</td>
<td>Hard</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Preferred Service:</td>
<td>None</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>Authorized</p>
<p>Groups:</p></td>
<td>0-3</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>(Current) Groups:</td>
<td>0-3</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Enabled Characters:

> Loss Notification, Message codes, Verification

### Cable Connections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Cable connections from Analyzer to DPC are dependent on whether you will be using the Dawning Technologies cables or making your own.

> If using the Dawning Technologies cables (in instances where the DPC is located near the analyzer interfacing), the requirements can be determined by looking at the printout of the 530MPC interpreter program for that analyzer. If the DPC was preconfigured at the factory, a printout is shipped with the DPC. If the system was not preconfigured, Dawning Technologies will ship universal instrument cables with gender changes. If these do not work, the site will need to buy the instrument specific cables or make their own.

> If not using the Dawning Technologies pre-supplied cables, the site will need to make their own.

> The cable connections between the DPC and the host computer must be made at the site. The following chart gives the pin configuration(s) needed by the ResultNet Interface System serial ports:

### Definitions for 25-pin Male Connector

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 39%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Pin No.</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>RS-232C Signal Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Direction Relative to PC</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>Chassis Ground</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2 ---&gt;</p>
</blockquote></td>
<td>Transmit Data</td>
<td>Output</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3 &lt;---</p>
</blockquote></td>
<td>Receive Data</td>
<td>Input</td>
</tr>
<tr class="even">
<td><blockquote>
<p>4 &lt;---</p>
</blockquote></td>
<td>Request to Send</td>
<td>Input</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5 ---&gt;</p>
</blockquote></td>
<td>Clear to Send</td>
<td>Output</td>
</tr>
<tr class="even">
<td><blockquote>
<p>6 &lt;---</p>
</blockquote></td>
<td>Data Set Ready</td>
<td>Input</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td>Signal Ground</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8 &lt;---</p>
</blockquote></td>
<td>Data Carrier Detect</td>
<td>Input</td>
</tr>
<tr class="odd">
<td>20 ---&gt;</td>
<td>Data Terminal Ready</td>
<td>Output</td>
</tr>
</tbody>
</table>

> Definitions for 9-pin Male Connector

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 39%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Pin No.</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>RS-232C Signal Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Direction Relative to PC</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1 &lt;---</p>
</blockquote></td>
<td>Data Carrier Detect</td>
<td>Input</td>
</tr>
<tr class="even">
<td><blockquote>
<p>2 &lt;---</p>
</blockquote></td>
<td>Receive Data</td>
<td>Input</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3 ---&gt;</p>
</blockquote></td>
<td>Transmit Data</td>
<td>Output</td>
</tr>
<tr class="even">
<td><blockquote>
<p>4 ---&gt;</p>
</blockquote></td>
<td>Data Terminal Ready</td>
<td>Output</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td>Signal Ground</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6 &lt;---</p>
</blockquote></td>
<td>Data Set Ready</td>
<td>Input</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7 &lt;---</p>
</blockquote></td>
<td>Request to Send</td>
<td>Input</td>
</tr>
<tr class="even">
<td><blockquote>
<p>8 ---&gt;</p>
</blockquote></td>
<td>Clear to Send</td>
<td>Output</td>
</tr>
</tbody>
</table>

## Terminal Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note Terminal settings must be made on each node of the cluster (Alpha PC). This is at the VMS level, setup by IRM.

> 600A02 \$: SHO TERM LTAxxxx

> Terminal: \_LTAxxxx: Device_Type: Unknown Owner: No Owner

| Input:  | 9600 | LRfill: | 0   | Width: | 255 | Parity: None |
|---------|------|---------|-----|--------|-----|--------------|
| Output: | 9600 | CRfill: | 0   | Page:  | 24  |              |

> Terminal Characteristics

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 26%" />
<col style="width: 26%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Interactive</p>
</blockquote></th>
<th><blockquote>
<p>No Echo</p>
</blockquote></th>
<th><blockquote>
<p>Type_ahead</p>
</blockquote></th>
<th>No Escape</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Hostsync</p>
</blockquote></td>
<td><blockquote>
<p>TT sync</p>
</blockquote></td>
<td><blockquote>
<p>Lowercase</p>
</blockquote></td>
<td>No Tab</td>
</tr>
<tr class="even">
<td><blockquote>
<p>No Wrap</p>
</blockquote></td>
<td><blockquote>
<p>Scope</p>
</blockquote></td>
<td><blockquote>
<p>No Remote</p>
</blockquote></td>
<td>No Eightbit</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>No Broadcast</p>
</blockquote></td>
<td><blockquote>
<p>No Readsync</p>
</blockquote></td>
<td><blockquote>
<p>Form</p>
</blockquote></td>
<td>Fulldup</td>
</tr>
<tr class="even">
<td><blockquote>
<p>No Modem</p>
</blockquote></td>
<td><blockquote>
<p>No Local_echo</p>
</blockquote></td>
<td><blockquote>
<p>No Autobaud</p>
</blockquote></td>
<td>Hangup</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>No Brdcstmbx</p>
</blockquote></td>
<td><blockquote>
<p>No DMA</p>
</blockquote></td>
<td><blockquote>
<p>Altypeahead</p>
</blockquote></td>
<td>Set_speed</td>
</tr>
<tr class="even">
<td><blockquote>
<p>No Commsync</p>
</blockquote></td>
<td><blockquote>
<p>No Line Edit</p>
</blockquote></td>
<td><blockquote>
<p>Overstrike edit</p>
</blockquote></td>
<td>No Fallback</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>No Dialup</p>
</blockquote></td>
<td><blockquote>
<p>No Secure service</p>
</blockquote></td>
<td><blockquote>
<p>No Disconnect</p>
</blockquote></td>
<td>Pasthru</td>
</tr>
<tr class="even">
<td><blockquote>
<p>No Syspassword</p>
</blockquote></td>
<td><blockquote>
<p>No SIXEL gra</p>
</blockquote></td>
<td><blockquote>
<p>No Soft Characters</p>
</blockquote></td>
<td>No Printer Port</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Numeric Keypad</p>
</blockquote></td>
<td><blockquote>
<p>No ANSI_CRT</p>
</blockquote></td>
<td><blockquote>
<p>No Regis</p>
</blockquote></td>
<td>No Block_mode</td>
</tr>
<tr class="even">
<td><blockquote>
<p>No Advance_vid</p>
</blockquote></td>
<td><blockquote>
<p>No Edit_mode</p>
</blockquote></td>
<td><blockquote>
<p>No DEC_CRT</p>
</blockquote></td>
<td>No DEC_CRT2</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>No DEC_CRT3</p>
</blockquote></td>
<td><blockquote>
<p>No DEC_CRT</p>
</blockquote></td>
<td><blockquote>
<p>No DEC_CRT5</p>
</blockquote></td>
<td>No Ansi_Color</td>
</tr>
</tbody>
</table>

# Dawning Technologies PC Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Vendor Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Vendor installation is offered by Dawning Technologies. Contact the company for details.

## Site Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Unload equipment and check against packing slip.
2.  Assemble according to Dawning Technologies Installation Startup Procedure (should be received from Dawning Technologies).
3.  Power on, DPC should boot up to ResultNet Software at the Worklist Screen, if you do not boot up to this screen call Dawning Technologies at (800) 332- 0499.

# Testing Communication

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From V*IST*A System to Dawning Technologies PC Port

- IRM can send a test pattern to a dumb terminal that is connected to the Dawning Technologies port.
- IRM can repeat procedure from the DPC port to a dumb terminal in IRM.
- If necessary, use DOS commands on Dawning Technologies unit to confirm transmission out of the COM1 port to a dumb terminal or V*IST*A system.

# V*IST*A Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Setup of these files should be done in the following order:

> Note Make sure Patches LA\*5.2\*17, and LR\*5.2\*65, are installed. If not installed, follow the instructions for each patch. File \#68 must have the numeric identifier in place.

## DEVICE file (#3.5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- MSM sites refer to pages 19 through 22 of the Laboratory Universal Interface Patches LA\*5.2\*17, and LR\*5.2\*65.

> Note LA\*5.2\*17, and LR\*5.2\*65 patches will be referenced as UI patch.

- DSM site

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>NAME: <strong>DAWNING</strong></p>
</blockquote></th>
<th>$I: <strong>SITE SPECIFIC</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ASK DEVICE: <strong>NO</strong></td>
<td>ASK PARAMETER: <strong>NO</strong></td>
</tr>
<tr class="even">
<td>VOLUME SET (CPU): <strong>ROU</strong></td>
<td>LOCATION OF TERMINAL: <strong>SITE SPECIFIC</strong></td>
</tr>
<tr class="odd">
<td><p>SUPPRESS FORM FEED AT CLOSE:</p>
<blockquote>
<p><strong>YES</strong></p>
</blockquote></td>
<td>MARGIN WIDTH: <strong>132</strong></td>
</tr>
<tr class="even">
<td>FORM FEED: <strong>#</strong></td>
<td>PAGE LENGTH: <strong>64</strong></td>
</tr>
<tr class="odd">
<td>BACK SPACE: <strong>$C(8)</strong></td>
<td>SUBTYPE: <strong>P-OTHER</strong></td>
</tr>
<tr class="even">
<td>TYPE: <strong>TERMINAL</strong></td>
<td>LAT SERVER NODE: <strong>SITE SPECIFIC</strong></td>
</tr>
<tr class="odd">
<td><p>LAT SERVER PORT: <strong>SITE</strong></p>
<blockquote>
<p><strong>SPECIFIC</strong></p>
</blockquote></td>
<td>VMS DEVICE TYPE: <strong>LAB INSTRUMENT</strong></td>
</tr>
<tr class="even">
<td>LAT PORT SPEED: <strong>96</strong></td>
<td><p>TIMED READ ($ OF SECONDS):</p>
<blockquote>
<p><strong>99999</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

## HL7 DHCP APPLICATION PARAMETER file (#771)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 53%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th>NAME: <strong>LA AUTO INST</strong></th>
<th>ACTIVE/INACTIVE: <strong>ACTIVE</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>HL7 ENCODING CHARACTERS: <strong>^~\&amp;</strong></td>
<td>HL7 FIELD SEPARATOR: <strong>|</strong></td>
</tr>
<tr class="even">
<td>HL7 MESSAGE: <strong>ORU</strong></td>
<td><p>PROCESSING ROUTINE:</p>
<blockquote>
<p><strong>ORU^LA7HL7</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>HL7 MESSAGE: <strong>ORM</strong></td>
<td>PROCESSING ROUTINE: <strong>NONE</strong></td>
</tr>
<tr class="even">
<td>HL7 SEGMENT: <strong>OBR</strong></td>
<td>FIELDS USED IN THIS SEGMENT: <strong>4,7,8,9,14,22</strong></td>
</tr>
<tr class="odd">
<td>HL7 SEGMENT: <strong>OBX</strong></td>
<td>FIELDS USED IN THIS SEGMENT: <strong>2,3,4,5,6,7,8</strong></td>
</tr>
<tr class="even">
<td>HL7 SEGMENT: <strong>MSH</strong></td>
<td><p>FIELDS USED IN THIS SEGMENT:</p>
<blockquote>
<p><strong>1,2,3,4,5,6,7,8,9,10,11,12</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>HL7 SEGMENT: <strong>PID</strong></td>
<td>FIELDS USED IN THIS SEGMENT: <strong>3,5,7,8,19</strong></td>
</tr>
<tr class="even">
<td>HL7 SEGMENT: <strong>ORC</strong></td>
<td>FIELDS USED IN THIS SEGMENT: <strong>1,2,3</strong></td>
</tr>
<tr class="odd">
<td>HL7 SEGMENT: <strong>NTE</strong></td>
<td>FIELDS USED IN THIS SEGMENT: <strong>3</strong></td>
</tr>
</tbody>
</table>

| NAME: LAB INTERFACE | ACTIVE/INACTIVE: ACTIVE |
|-------------------------|-----------------------------|
| FACILITY: DAWNING   |                             |

> Note There must be one LAB INTERFACE entry for each entry in File \#770.

## HL7 NON-DHCP APPLICATION PARAMETER file (#770)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>NAME: <strong>LAB INTERFACE</strong></p>
</blockquote></th>
<th>DHCP STATION NUMBER:<strong>SITE SPECIFIC</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>NON-DHCP FACILITY NAME:</p>
<blockquote>
<p><strong>DAWNING</strong></p>
</blockquote></td>
<td>MAXIMUM BLOCK SIZE <strong>245</strong></td>
</tr>
<tr class="even">
<td>NUMBER OF RETRIES: <strong>3</strong></td>
<td>HL7 DEVICE: <strong>DAWNING</strong></td>
</tr>
<tr class="odd">
<td>HL7 VERSION NUMBER: <strong>2.2.</strong></td>
<td>DHCP APPLICATION: <strong>LA AUTO INST</strong></td>
</tr>
<tr class="even">
<td>LOWER LEVEL PROTOCOL TIMEOUT: <strong>5</strong></td>
<td>RELATED FILE #771 ENTRY: <strong>LAB INTERFACE</strong></td>
</tr>
<tr class="odd">
<td><p>HL7 PROCESSING ID:</p>
<p><strong>PRODUCTION</strong></p></td>
<td>START/STOP TRANSMISSION LOG: <strong>STOP LOG</strong></td>
</tr>
</tbody>
</table>

> Note Make sure there is one entry per Dawning Technologies system, that is, a second entry could be called LAB INTERFACE2 linking it with the second HL7 DEVICE, for example, DAWNING2

## LA7 MESSAGE PARAMETER CONFIGURATION file (#62.48)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th>CONFIGURATION: <strong>UNIVERSAL INTERFACE</strong></th>
<th>PROTOCOL: <strong>HEALTH LEVEL SEVEN</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>STATUS: <strong>ACTIVE</strong></td>
<td>DEBUG LOG: <strong>ON</strong></td>
</tr>
<tr class="even">
<td>HL7 NON-DHCP APPLICATION: <strong>LAB INTERFACE</strong></td>
<td>PROCESS IN: <strong>D QUE^LA7UIIN</strong></td>
</tr>
<tr class="odd">
<td><p>PROCESS DOWNLOAD:</p>
<blockquote>
<p><strong>D EN^LA7UID1</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>REMOTE SYSTEM ID:</td>
<td><p>[<strong>Note</strong> This is a free text field and should contain the following entries in order stated.]</p>
<p>.01 field of File #770,#3 field of File #770,#8 field of File #770 and the #2 field of File #770</p>
<p>Do <strong>not</strong> insert spaces between field entries. This text is case sensitive.</p>
<p><strong>Example</strong> from Long Beach:</p>
<p>LAB INTERFACEDAWNINGLA AUTO</p>
<p>INST600 (this will be different at each site)]</p></td>
</tr>
</tbody>
</table>

> Note Make sure there is one entry per Dawning Technologies system, that is, the second entry could be called UNIVERSAL INTERFACE2.

> The REMOTE SYSTEM ID: could then be LAB INTERFACE2DAWNINGLA AUTO INST600

## AUTO INSTRUMENT file (#62.4)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This discussion is limited to those fields pertinent to the Dawning Technologies Universal Interface.

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Discussion</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NAME</td>
<td><blockquote>
<p>The Name field <strong>must</strong> match the Station field under MPCUP configuration for each instrument. This is how the data is matched to the LAH global. The IEN is <strong>not</strong> used by the Dawning Technologies Interface (no LA global).</p>
<p><strong>Note</strong> This field is limited to four characters.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PROGRAM</td>
<td><blockquote>
<p>This field is not used for the UI instruments but is a required field so an entry must be typed. Since it is essentially free text, anything can be entered, but must be unique from any other entry, for example, zzcolt.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VENDOR CARD ADDRESS</td>
<td><blockquote>
<p>This field is used by Dawning Technologies for downloading. This field must match the Address field in ResultNet and the Analyzer field in MPCUP on the Dawning Technologies system for a bi-directional instrument, for example, 001, 002 (three digits).</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SHORT ACCESSION # LENGTH</td>
<td><blockquote>
<p>This field will pad the download accession number with an appropriate number of zeros to the designated length. This field will then match the barcode label that is scanned by the instrument. That is, if the length is set to 4 and the accession #10 will be downloaded as 0010; the barcode, scanned as 0010 will match. This is dependent upon the site label routine that determines the barcode</p>
<p>length.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MESSAGE CONFIGURATION</td>
<td><blockquote>
<p>This field is a pointer to LA7 MESSAGE PARAMETER CONFIGURATION file (#62.48). If there are multiple Dawning Technologies systems, this should match up with correct entry.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Discussion</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CHEM TEST</p>
<p>(multiple)</p></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td><blockquote>
<p>The name of the test from File #60.</p>
<p><strong>Note</strong> This may have to be entered multiple times (<strong>hint</strong>: use quotes for duplicates) to accommodate different UI Test codes being sent for that test. For example, Protimes on the MLA 1600, require a different UI Test code for the download and has three different UI Test Codes for the Upload.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PARAM 1</p>
</blockquote></td>
<td><blockquote>
<p>This field can be used to "pretty" up the data if needed. Any MUMPS Code written in this field will be executed on a given test result that is contained in the variable LA7VAL. For example, on the Coulter STKS, the definitive flags had 11 characters being sent such as 2+ Macrocyt. The site only wanted the 2+, so in PARAM 1 the following code was in put place:</p>
<p>SET LA7VAL=$E(LA7VAL,1,3). The $E is extracting the 1st through the 3rd piece of the LA7VAL variable. Also see page 47 of the UI patch documentation for further examples.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UI TEST CODE</p>
</blockquote></td>
<td><blockquote>
<p>This field is the identifier from the instrument for the test. This field is used for both uploading and downloading.</p>
<p>Dawning Technologies transmits to <strong>V</strong><em>IST</em><strong>A</strong> the test code as sent by the instrument. The test code can be determined by using the ResultNet transmission log (ALT-T) or by checking the LA7 ERROR LOG option.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CONVERT RESULTS TO REMARK</p>
</blockquote></td>
<td><blockquote>
<p>If this field is set to YES, any result will be stuffed into the comment field versus the result field. PARAM 1 can be used to translate a result into a different interpretation. See page 49 of UI Patch documentation.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Discussion</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CHEM TEST</p>
<p>(multiple)</p></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ACCEPT RESULTS FOR THIS TEST</p>
</blockquote></td>
<td><blockquote>
<p>This field must be set to YES in order for the result to be uploaded. The default is YES. It is also used to screen out extraneous test results sent from the instrument or to screen out the test for downloading only.</p>
<p>For example: The MLA uploads three sets of results for each test it runs, two duplicates and one average. Only the average result is to be uploaded into <strong>V</strong><em>IST</em><strong>A</strong>. This test will be the only one of the three that has this field set to YES. The other tests have to be set to NO.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DOWNLOAD TO INSTRUMENT</p>
</blockquote></td>
<td><blockquote>
<p>In this field the default <strong>must</strong> be set YES for the test to be downloaded. The default is YES. Set to NO for all those tests that are extraneous as described or are tests that will be calculated by the instrument or <strong>V</strong><em>IST</em><strong>A</strong>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IGNORE RESULTS NOT ORDERED</p>
</blockquote></td>
<td><blockquote>
<p>Default is NO. This field should be set to YES if you want to restrict results to only those tests that were ordered.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FILE BUILD ENTRY</td>
<td><blockquote>
<p>EN</p>
<p>[This File Build field is used to make a download record.]</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FILE BUILD ROUTINE</td>
<td><blockquote>
<p>LA7UID</p>
<p>[This File Build field is used to make a download record.]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>AUTO DOWNLOAD</td>
<td><blockquote>
<p>The default is NO. Set the default to YES if you want to download the test to the instrument upon accessioning.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Initiating Background HL7 Task

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You may contact IRM service to assign this HL7 package option to the Laboratory Information Manager (LIM).

> To initiate a background HL7 task:

1.  Select HL7 Main Menu option.
2.  From the Main Menu, select option 1, V1.5 options.
3.  From this menu, select option 2, Initiate Background Task.
4.  In option 2, select the entry LAB INTERFACE to start the HLLP background job.

### Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Make sure step four is done for each lab interface defined.
- It is a good idea to queue more than one HLLP task, we recommend you consult with IRM Service before queuing.

# Dawning Technologies System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When Dawning Technologies knows what initial instruments are going to be interfaced, they will send the system preconfigured. Additional 530MPC cards ordered later will be installed and configured by the site with Dawning Technologies help.

## MPCUP Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> At the status screen, do the following:

1.  To get to DOS type ALT-X.
2.  At the C prompt type MPCUP, you will see the Main menu with six options.
3.  From the Main menu select the Configuration option.

### Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The configuration must be set up for each instrument. The following page shows an example of a setup. What is displayed are only those fields to be edited. Be sure to check the host communication setup on the analyzer (for example, baud rate, etc.,). If not the same as the preconfigured DPC, update the analyzer settings to match.

> A list of the ports will be displayed. You can highlight the port you are going to edit.

> Example Configuration for Port 1 Select 07a

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Entry</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>BAUD</td>
<td><strong>9600</strong></td>
</tr>
<tr class="even">
<td>BITS</td>
<td><strong>8</strong></td>
</tr>
<tr class="odd">
<td>STOP</td>
<td><strong>1</strong></td>
</tr>
<tr class="even">
<td>PARITY</td>
<td><strong>NONE</strong></td>
</tr>
<tr class="odd">
<td>STATION</td>
<td><p><strong>ACS</strong></p>
<p>[<strong>Note</strong> This must match Name field (.01) of the AUTO INSTRUMENT file, limit of four characters.]</p></td>
</tr>
<tr class="even">
<td>ANALYZER</td>
<td><p><strong>001</strong></p>
<p>[<strong>Note</strong> This is the same as the Address field under ResultNet Protocol Definition and the Vendor Card Address in the Auto Instrument file.]</p></td>
</tr>
<tr class="odd">
<td>LABEL</td>
<td><strong>CORNING ACS 180</strong> [Free Text]</td>
</tr>
<tr class="even">
<td>EXECUTE</td>
<td><strong>YES</strong></td>
</tr>
</tbody>
</table>

### Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The rest of the fields are not to be edited unless you are instructed to by Dawning Technologies.
- The rest of the instruments have to be reviewed and edited as needed.

> To exit to DOS, do the following:

1.  To return to the C prompt, select Esc, or EXIT from the menu.
2.  At the C prompt, type RNET and press ENTER to return to the ResultNet Main Screen.

## ResultNet Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the Work list screen select Configuration:

### Configuration for Host Port (COM1 port):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  ALT-D - Highlight the HOST Device to edit
2.  ALT-F - HL7 HOST FORMAT DEFINITION

> Example HOST

| Field     | Entry                                                   |
|---------------|-------------------------------------------------------------|
| SEND APPL     | LAB INTERFACE \[from File \#770, NAME\]                 |
| FACILITY      | DAWNING \[from File \#770, NON- DHCP FACILITY NAME\]    |
| RECV APPL     | LA AUTO INST \[from File \#771, NAME\]                  |
| FACILITY      | 660 \[from File \#770, DHCP STATION NUMBER\]            |
| DELIM FIELD   | 7C                                                      |
| COMPONENT     | 5E                                                      |
| REPEAT        | 7E                                                      |
| ESCAPE        | 5C                                                      |
| SUB-COMP      | 26                                                      |
| DWNLD DETAILS | YES \[for downloading patient demographic information\] |

3.  ALT-P - HL7 HOST PROTOCOL

> Example HOST

| Field     | Entry  |
|---------------|------------|
| DEVICE        | COM1   |
| PROTOCOL      | HYBRID |
| BLOCK START   | OB     |
| END           | 1C     |
| CKSUM ENABLED | YES    |

4.  ALT-O - OPERATIONS

### HOST

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Field | Entry  |
|-----------|------------|
| ENABLED   | YES    |
| TRANSMIT  | YES    |
| PROTOCOL  | SERIAL |
| FORMAT    | HL7    |

> AUX

| Field | Entry  |
|-----------|------------|
| ENABLED:  | NO     |
| TRANSMIT  | NO     |
| PROTOCOL  | SERIAL |
| FORMAT    | CDF    |

### 530MPC Instrument Port Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  ALT-F - 530MPC FORMAT DEFINITION

> The FORMAT definitions are the same for all instruments unless you wish to suppress sending across specific information.

> Caution Do not edit or change these fields unless instructed by Dawning Technologies.

2.  ALT-P - 530MPC PROTOCOL definitions

> The protocols will be different for each instrument. The DEVICE indicates which MPC card (drive) the instrument is located. The ADDRESS is used to specify to which instrument to download. This must match the Vendor Card Address field in the AUTO INSTRUMENT file.

> Example 530MPC PROTOCOL

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Entry</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>LABEL</td>
<td><strong>CORNING ACS180</strong></td>
</tr>
<tr class="even">
<td>DEVICE</td>
<td><strong>E</strong></td>
</tr>
<tr class="odd">
<td>ADDRESS</td>
<td><strong>001</strong></td>
</tr>
<tr class="even">
<td>MODE</td>
<td><strong>BIDIRECTIONAL</strong></td>
</tr>
<tr class="odd">
<td>FORMAT</td>
<td><strong>CDF</strong></td>
</tr>
<tr class="even">
<td>ARCHIVE</td>
<td><p><strong>NO</strong> [Archive can be turned on, but remember to clean archive files periodically. Files get very large for a busy</p>
<p>analyzer.]</p></td>
</tr>
</tbody>
</table>

### Quick Reference Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This is a Quick Reference Guide to setting up one or more Dawning Technologies ResultNet systems.

![](laboratory-universal-interface-dawing-technologies-instructional-implementation-/002.png)

## CONFIG.SYS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CONFIG.SYS file on the DPC may be edited to increase the input and output of the buffer size. The handshake may have to be changed to XON/OFF. The factory default is NO HANDSHAKING. Check with IRM for DecServer handshaking requirements.

1.  Exit to DOS using ALT - X.
2.  At the DOS prompt check the parameters of the CONFIG.SYS file by entering TYPE CONFIG.SYS. The parameters are displayed on the screen. To get a printout, you will need a printer attached to the DPC, then type PRINT CONFIG.SYS.
3.  The line to edit contains the COM1 device and should look like: DEVICE=C:\RNET\BUFF.SYS COM1,3F8,4,4096,4096,8,1,N,N,1
4.  Using the DOS editor (EDIT CONFIG.SYS), change the 4096,4096 to 8192,8192. Also change the second N to X. The line now should look like:

> DEVICE=C:\RNET\BUFF.SYS COM1,3F8,4,8192,8192,8,1,N,X,1

5.  For additional information on the BUFF.SYS file, type BUFF.DOC and this will explain the different parameters.

# Confirming Data Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following information is used to confirm data transmission.

## Upload (analyzer---\>Dawning---\>V*IST*A)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Generate a data stream by running several specimens on the analyzer.
2.  Use the EA (enter/verify data auto instrument) option to check for successful transmission. If not completely successful, continue to step 3.
3.  If the data is not available for verification by the EA option, check the following first:
    - The transmission log screen in MPCUP to determine if the data was transmitted to the 530MPC card.

> (ResultNet--\>ALT-X--\>MPCUP--\>Diagnostics--\>Transmission Log --\> Analyzer)

- If data is not there, the problem lies with the analyzer cabling or configuration.
- If valid data appears in the MPCUP transmission log, the analyzer is transmitting data to the Dawning Technologies 530MPC card.

> Check ResultNet transmission log to verify that the data was processed by the 530MPC software.

> (Esc to DOS--\>RNET--\>ALT-T)

- If data from this analyzer is not present, then contact Dawning Technologies for technical assistance.
- If data does appear in the transmission log, check the worklist screen in ResultNet to determine if the data was transmitted to V*IST*A. This can be confirmed by noting if the accession numbers on the worklist have converted from white to blue or by noting the time listed in the transmission status box.
  - If data has not transmitted to V*IST*A, (the accession number remains white on the screen) the problem could be:
    - the cabling between Dawning Technologies and V*IST*A, or
    - the HLLP background job (not running or not processing data). Restart the HLLP job.
- If data has processed out of ResultNet, continue.
  - Check the LA7 transmission error log by using the LA7 Print Lab UI Error Log option. This will indicate if any of the data from the Dawning Technologies has failed to process, and will also list a reason for the failure. Some of these reasons include:
- a UI code ("test code") was transmitted but is not defined in the AUTO INSTRUMENT file entry for a specific analyte.
- an instrument name was transmitted but did not find a matching entry in the auto instrument file.

## Download (V*IST*A ---\>Dawning---\>analyzer)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note We suggested that auto downloads not be used during initial testing.

1.  Generate several accession numbers for building onto a worklist to download to the analyzer.
2.  Build the work list and download it to the analyzer, using the Download a Load List to an Instrument option.
3.  If the download is successful, those accession numbers will appear on the analyzer. Specific methods of reviewing download records varies from analyzer to analyzer.

> Note If the download was not successful, continue to step 4.

4.  Check to see if the download data appear as highlighted entries in the ResultNet transmission log (ALT T).
    - If the data is not there, the problem lies with the following:
      - the cabling between Dawning Technologies and V*IST*A, or
      - the V*IST*A background job (not running or not processing data). Restart the HLLP job.
    - If the data is there, check the MPCUP transmission log for that analyzer. The download records will be prefixed with a Rx. If the data is not there, then recheck the ResultNet transmission log for the following (need to redownload the worklist).
      - Is a VENDOR CARD ADDRESS defined for that analyzer and does it match the ADDRESS in ResultNet and MPCUP?
      - Is the Auto Instrument name the same as the STATION name in MPCUP?
    - If the data is in MPCUP but does not reach the analyzer, the problem could be with the following:
      - the cabling between Dawning Technologies and the analyzer.
      - the UI TEST CODE does not match the analyzer's requirements.

> Note Some instruments require a different download code than upload code.

> Check the instrument interface specifications.

- analyzer is not configured for bi-directional communications.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note Data will not be processed to ResultNet while in MPCUP. Transmission will resume once exited from MPCUP without loss of data.

## After a V*IST*A Crash:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Check ALT-T (in ResultNet) to see if good data is being transmitted. You should see highlighted records and black background records. The highlighted records are coming from V*IST*A while all black background records are from ResultNet. If there is no transmission from V*IST*A, see if the HLLP background job is running.

1.  If no HLLP job is running, initiate a new job. Check transmission log for valid data.
2.  If the HLLP job is running and has invalid looking data, log out port and allow new job to start. Check ALT-T again to see if transmission has resumed.

> Note: Exit to DOS before logging out port. After the new HLLP job is running go back to ResultNet and check transmission log.

3.  If V*IST*A crashes during transmission of data to the Dawning Technologies, it is possible to have corrupted data on the 530MPC card. This may slow down the ResultNet software or even stop receipt of data to the card. To correct this problem, the 530MPC card(s) need to be reformatted. To reformat from ResultNet:

> ALT-X--\>MPCUP--\>UTILITIES--\>Reformat Memory--\>select single device or all

## Pop-up Data Interpreter Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> These errors will be displayed as a box in the ResultNet work list screen. Contact Dawning Technologies for technical assistance, since data will not be processed through this port until the problem is resolved.

> Note: Reformatting memory for that analyzer will restart processing, but call Dawning before doing this to troubleshoot the error unless after hours and an emergency. Take note of the error and call Dawning the next day.

# Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ResultNet/MPCUP Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All new software upgrades are distributed to Dawning Technologies customers through Dawning Technologies BBS. Users are expected to become familiar with accessing this BBS, as well as some basic DOS commands.

## 530MPC Card Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Individual analyzer 530 software can be obtained from the software library on the BBS, through a personal e-mail message on the BBS or from the software library diskette received with the Dawning Technologies system.

> Once the software is available, it can be installed on the appropriate 530MPC card as follows:

1.  Use ALT-X to exit from ResultNet to DOS.
2.  MPCUP--\>Programming--\>select analyzer port.
3.  In the highlighted box, type in NEW (CR). System responds with OK.
4.  In the highlighted box, type in the path and the file name of the software to be loaded; for example, LOAD "B:\FILENAME.530". System responds by scrolling the software on the screen.
5.  In the highlighted box, type in SAVE. System responds again by scrolling the software on the screen.
6.  As a recommended practice, save a copy of the software to the C drive (or diskette), as well as loading it onto the 530MPC card. This can be accomplished by typing SAVE "C:\FILENAME.530" in the highlighted box (or SAVE A:\FILENAME.53).

## Printing Documentation of new 530MPC software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Access the drive containing the new software file.
2.  Type in PRINT FILENAME.530 - this will provide a print out of program plus notes.

# General File Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Weekly

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Perform a SCANDISK without selecting the Full Surface Test.
2.  Perform a Format Memory on each card in the system.

## Monthly

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Delete MPCssp.CAP and MPCssp.LOG files.
2.  Check for MESSAGES on the BBS.

## Semi-Annually

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Perform all the above steps.
2.  Dial into the BBS and make certain that the 530MPC Data Interpreter Programs and MPC drivers in use are the most current versions.
3.  Perform a VIRUS scan on the entire PC to check for corrupt files.
4.  Make backup copies of important files and store them in a secure place.
5.  Perform a SCANDISK function and select the Full Surface Test.