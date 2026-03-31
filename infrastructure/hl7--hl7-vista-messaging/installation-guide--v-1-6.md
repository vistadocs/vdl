---
title: HL7 V. 1.6 Installation Guide
doc_type: IG
doc_label: Installation Guide
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
menu_options: 6
description: - [Minimum Versions Required](#minimum-versions-required) - [Resource Consumption](#resource-consumption) - [Step 7. Load DHCP HL7 Software Tape](#step-7-load-dhcp-hl7-software-tape) - [Step 10. Initialization](#step-10-initialization) - [Step 10. Initialization](#step-10-initialization-1) - [Step 1
audience: 
keywords: 
  - filed
  - hlini
  - protocol
  - table
  - step
  - strong
  - contents
  - initialization
  - class
  - message
page_count: 0
word_count: 3080
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 1995
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Health_Level_7_(HL7)/hl71_6ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Health_Level_7_(HL7)/hl71_6ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=8"
---

Decentralized Hospital Computer Program

DHCP

Health LEVEL Seven

(HL7)

Installation Guide

October 1995

IRM Field Office

Albany, New York

Table of Contents

Resource Requirements 1

> Minimum Versions Required 1

> Resource Consumption 1

Installation Instructions 3Installation Screen Examples 7

> Load DHCP HL7 Software Tape 7

> Initialization 8

> Add The HL7 Main Menu 13

Resource Requirements

# Minimum Versions Required


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Minimum Versions Required](#minimum-versions-required)
- [Resource Consumption](#resource-consumption)
- [Step 7. Load DHCP HL7 Software Tape](#step-7-load-dhcp-hl7-software-tape)
- [Step 10. Initialization](#step-10-initialization)
- [Step 10. Initialization](#step-10-initialization-1)
- [Step 10. Initialization](#step-10-initialization-2)
- [Step 10. Initialization](#step-10-initialization-3)
- [Step 10. Initialization](#step-10-initialization-4)
- [Step 10. Initialization](#step-10-initialization-5)
- [Step 11. Add The HL7 Main Menu](#step-11-add-the-hl7-main-menu)
The following minimum package versions are required in order to install this version of DHCP HL7:
- Kernel V. 7.1
- VA FileMan V. 21.0
- VA MailMan V. 7.1
- OE/RR V. 2.5

# Resource Consumption

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ^HL global will consume approximately 17K of disk space for static file entries, and about 1K of disk space for every 10 entries in the HL7 MESSAGE TEXT file (#772).

The ^HLCS global will consume approximately 50K of disk space for every 100 messages (500 byte average length) in the HL LOGICAL LINK (#870) file.

The ^HLMA global will consume approximately 400 bytes for every 10 entries in the HL7 MESSAGE ADMINISTRATION file (#773).

CPU usage is insignificant for a few links, but will increase linearly as more links are added.

Installation Instructions

This installation guide can be used to install the DHCP HL7 system into either a Test UCI (T) or a Production UCI (P) by following the steps in the table below. Users do not need to be off the system when installing this package if global placement (Step 1 below) is accomplished in advance. Installation will normally take 5 minutes or less.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 76%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Step</strong></td>
<td><strong>Description</strong></td>
<td><strong>UCI</strong></td>
</tr>
<tr class="even">
<td>1.</td>
<td><p>DSM: Disable journalling for HL* globals.</p>
<p>MSM: Follow standard journalling practices.</p></td>
<td>T, P</td>
</tr>
<tr class="odd">
<td>2.</td>
<td>Check schedule for IVM and EDR background jobs (and any other applications that are using the DHCP HL7 V. 1.5 package). Reschedule for after install of V. 1.6.</td>
<td>T, P</td>
</tr>
<tr class="even">
<td>3.</td>
<td><p>Global Placement:</p>
<ul>
<li><p>If your site has never installed DHCP HL7 before, you must set the ^HL global to null and place it in the appropriate translation.</p></li>
<li><p>Whether or not your site has installed DHCP HL7 before, you must set the ^HLCS and ^HLMA globals to null and place them in the appropriate translation, then restart the configurations to activate translation.</p></li>
<li><p>READ/WRITE/DELETE access is recommended for all classes (system, world, group, and UCI or user, depending on OS).</p></li>
<li><p>It is recommended that the globals ^HL, ^HLCS, and ^HLMA be journaled.</p></li>
</ul></td>
<td>T, P</td>
</tr>
<tr class="odd">
<td>4.</td>
<td><p>Sign into UCI where package is to be loaded.</p>
<p>DSM: Logon into a standard partition.</p>
<p>MSM: Logon into a 40k partition.</p></td>
<td>T, P</td>
</tr>
<tr class="even">
<td>5.</td>
<td><p>Stop all V. 1.5 LLPs that are currently running.</p>
<ul>
<li><p>Find tasks with a description of “HL7 Message Processor for XXX” (where XXX is the name of the Non-DHCP application).</p></li>
<li><p>Use the TaskMan User options [ZTMUSER] to request stopping of these tasks.</p></li>
</ul></td>
<td>T, P</td>
</tr>
<tr class="odd">
<td>6.</td>
<td>Delete HLIN* routines.</td>
<td>T, P</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 76%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Step</strong></td>
<td><strong>Description</strong></td>
<td><strong>UCI</strong></td>
</tr>
<tr class="even">
<td>7.</td>
<td><p>Load DHCP HL7 software tape.</p>
<p><strong>D ^%RR</strong></p>
<p>(See example on Page 7.)</p></td>
<td>T, P</td>
</tr>
<tr class="odd">
<td>8.</td>
<td><p>Run integrity routine(s).</p>
<p><strong>D ^HLNTEG</strong></p>
<p><em>NOTE: Call your IRM Field Office if any routines fail the integrity routine.</em></p></td>
<td>T, P</td>
</tr>
<tr class="even">
<td>9.</td>
<td>Please insure that the variables DUZ and DUZ(0) are defined prior to attempting initialization. The initialization will abort if DUZ is not set to a valid user number and DUZ(0) does not equal "@". Additionally, the variables DT, DTIME, and U must be defined, and the variable DIRUT must not exist.</td>
<td>T, P</td>
</tr>
<tr class="odd">
<td>10.</td>
<td><p>Run the HLINIT routine to initialize the DHCP HL7 package files.</p>
<p><strong>D ^HLINIT</strong></p>
<p>(See example beginning on Page 8.)</p></td>
<td>T, P</td>
</tr>
<tr class="even">
<td>11.</td>
<td><p>Add the HL7 MAIN MENU option to the menus of appropriate IRM staff.</p>
<p><strong>D P^DI</strong></p>
<p>(See example on Page 13.)</p></td>
<td>T, P</td>
</tr>
<tr class="odd">
<td>12.</td>
<td><p>Restart the V. 1.5 LLPs.</p>
<ul>
<li><p>From the HL7 Main Menu [HL MAIN MENU] option, go to the V1.5 OPTIONS [HL MENU 1.5] submenu.</p></li>
<li><p>Use the Initiate Background Task option [HL TASK] to restart the LLPs that you stopped in Step 5.</p></li>
</ul></td>
<td>T, P</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 8%" />
<col style="width: 76%" />
<col style="width: 15%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Step</strong></td>
<td><strong>Description</strong></td>
<td colspan="2"><strong>UCI</strong></td>
</tr>
<tr class="even">
<td>13.</td>
<td><p>Start the incoming and outgoing filers.</p>
<ul>
<li><p>From the HL7 Main Menu [HL MAIN MENU] option, go to the V1.6 OPTIONS [HL MENU 1.6] submenu.</p></li>
<li><p>Go to the Communications Server [HL COMMUNICATIONS SERVER] submenu.</p></li>
<li><p>Go to the Manage incoming and outgoing filers [HL MANAGE FILERS] submenu.</p></li>
<li><p>Choose the Start default number of incoming &amp; outgoing filers [HL START DEFAULT FILERS] option.</p></li>
</ul></td>
<td>T, P</td>
<td></td>
</tr>
<tr class="odd">
<td>14.</td>
<td>Delete the HLIN* routines.</td>
<td colspan="2">T, P</td>
</tr>
<tr class="even">
<td>15.</td>
<td>Move the HL* routines to all systems as necessary.</td>
<td colspan="2">P</td>
</tr>
<tr class="odd">
<td>16.</td>
<td>Enable Journalling for HL* globals</td>
<td colspan="2">T, P</td>
</tr>
</tbody>
</table>

*NOTE: Examples of some of the above steps are provided on the following pages of this manual.*

Installation Screen Examples

This section provides screen examples (as indicated in the table beginning on Page 3) for some of the steps in the Installation Instructions. For ease of reproduction, user input is both underlined and in boldface type.

# Step 7. Load DHCP HL7 Software Tape

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>D ^%RR</u>

Routine Restore

Input Device ? \> <u>\*\*Enter site-specific device name \*\*</u>

Restore All (A), Selected (S), or Confirm on overwrite (C) ? <u>A</u>

HLCHK HLCS HLCS1 HLCSDL HLCSDL1 HLCSDL2 HLCSDR HLCSDR1

HLCSDR2 HLCSFMN HLCSFMN0 HLCSFMN1 HLCSHDR HLCSIN HLCSLNCH HLCSMM

HLCSMM1 HLCSMON HLCSMON1 HLCSORA1 HLCSORA2 HLCSORAT HLCSOUT HLCSQUE

HLCSQUE1 HLCSQUED HLCSRE1 HLCSREP HLCSREQ HLCSRES HLCSRQ HLCSRV

HLCSTERM HLCSUTL HLCSUTL1 HLCSUTL2 HLDTIW01 HLDTIW02 HLDTIW03 HLDTIW04

HLDTIW05 HLDTIW2A HLDTIW2B HLDTIW2C HLDTIWP0 HLDTIWP1 HLDTIWP2 HLDTIWP3

HLDTIWP4 HLDTIWP5 HLDTIWP6 HLDTIWU0 HLDTIWU1 HLDTIWU2 HLDTIWU3 HLDTIWU4

HLDTIWU5 HLFNC HLFNC1 HLFNC2 HLFNC3 HLINI001 HLINI002 HLINI003

HLINI004 HLINI005 HLINI006 HLINI007 HLINI008 HLINI009 HLINI00A HLINI00B

HLINI00C HLINI00D HLINI00E HLINI00F HLINI00G HLINI00H HLINI00I HLINI00J

HLINI00K HLINI00L HLINI00M HLINI00N HLINI00O HLINI00P HLINI00Q HLINI00R

HLINI00S HLINI00T HLINI00U HLINI00V HLINI00W HLINI00X HLINI00Y HLINI00Z

HLINI010 HLINI011 HLINI012 HLINI013 HLINI014 HLINI015 HLINI016 HLINI017

HLINI018 HLINI019 HLINI01A HLINI01B HLINI01C HLINI01D HLINI01E HLINI01F

HLINI01G HLINI01H HLINI01I HLINI01J HLINI01K HLINI01L HLINI01M HLINI01N

HLINI01O HLINI01P HLINI01Q HLINI01R HLINI01S HLINI01T HLINI01U HLINI01V HLINI01W HLINI01X HLINI01Y HLINI01Z HLINI020 HLINI021 HLINI022 HLINI023

HLINI024 HLINI025 HLINI026 HLINI027 HLINI028 HLINI029 HLINI02A HLINI02B

HLINI02C HLINI02D HLINI02E HLINI02F HLINI02G HLINI02H HLINI02I HLINI02J

HLINI02K HLINI02L HLINI02M HLINI02N HLINI02O HLINI02P HLINI02Q HLINI02R

HLINI02S HLINI02T HLINI02U HLINI02V HLINI02W HLINI02X HLINI02Y HLINIS

HLINIT HLINIT1 HLINIT2 HLINIT3 HLINIT4 HLINIT5 HLLM HLLM1

HLLP HLMA HLMA0 HLMA1 HLMA2 HLNTEG HLNTEG0 HLONI001

HLONI002 HLONI003 HLONI004 HLONI005 HLONI006 HLONI007 HLONI008 HLONI009

HLONI010 HLONI011 HLONIT HLONIT1 HLONIT2 HLONIT3 HLPOST HLPOST16

HLPOSTQ HLPRE16 HLSERV HLTASK HLTF HLTF0 HLTF1 HLTP

HLTP0 HLTP01 HLTP1 HLTP2 HLTPCK1 HLTPCK1A HLTRANS HLUOPT

HLUOPT1 HLUTIL1 HLUTIL2 HLUTIL3

220 routines

# Step 10. Initialization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*NOTE: This example assumes that your site previously installed DHCP HL7 V. 1.5.*

\><u>D ^HLINIT</u>

This version (#1.6) of 'HLINIT' was created on 13-SEP-1995

(at ALBANY CAMPUS DEVELOPMENT, by VA FileMan V.21.0)

I AM GOING TO SET UP THE FOLLOWING FILES:

101 PROTOCOL (Partial Definition)

> **NOTE:** You already have the 'PROTOCOL' File.

770 HL7 NON-DHCP APPLICATION PARAMETER

> **NOTE:** You already have the 'HL7 NON-DHCP APPLICATION PARAMETER' File.

771 HL7 APPLICATION PARAMETER

\*BUT YOU ALREADY HAVE 'HL7 DHCP APPLICATION PARAMETER' AS FILE \#771!

Shall I change the NAME of the file to HL7 APPLICATION PARAMETER? NO// <u>YES</u>

771 HL7 APPLICATION PARAMETER

> **NOTE:** You already have the 'HL7 APPLICATION PARAMETER' File.

771.1 HL7 FIELD (including data)

> **NOTE:** You already have the 'HL7 FIELD' File.

I will OVERWRITE your data with mine.

771.2 HL7 MESSAGE TYPE (including data)

> **NOTE:** You already have the 'HL7 MESSAGE TYPE' File.

I will OVERWRITE your data with mine.

771.3 HL7 SEGMENT TYPE (including data)

\*BUT YOU ALREADY HAVE 'HL7 SEGMENT NAME' AS FILE \#771.3!

Shall I change the NAME of the file to HL7 SEGMENT TYPE? NO// <u>YES</u>

771.3 HL7 SEGMENT TYPE (including data)

> **NOTE:** You already have the 'HL7 SEGMENT TYPE' File.

I will OVERWRITE your data with mine.

771.4 HL7 DATA TYPE (including data)

> **NOTE:** You already have the 'HL7 DATA TYPE' File.

I will OVERWRITE your data with mine.

771.5 HL7 VERSION (including data)

> **NOTE:** You already have the 'HL7 VERSION SUPPORTED' File.

I will OVERWRITE your data with mine.

# Step 10. Initialization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

771.6 HL7 MESSAGE STATUS (including data)

> **NOTE:** You already have the 'HL7 MESSAGE STATUS' File.

I will OVERWRITE your data with mine.

771.7 HL7 ERROR MESSAGE (including data)

> **NOTE:** You already have the 'HL7 ERROR MESSAGE' File.

I will OVERWRITE your data with mine.

771.8 HL7 STANDARD (including data)

> **NOTE:** You already have the 'HL7 STANDARD' File.

I will OVERWRITE your data with mine.

772 HL7 MESSAGE TEXT

\*BUT YOU ALREADY HAVE 'HL7 TRANSMISSION' AS FILE \#772!

Shall I change the NAME of the file to HL7 MESSAGE TEXT? NO// <u>YES</u>

772 HL7 MESSAGE TEXT

> **NOTE:** You already have the 'HL7 MESSAGE TEXT' File.

773 HL7 MESSAGE ADMINISTRATION

> **NOTE:** You already have the 'HL7 MESSAGE ADMINISTRATION' File.

779.001 HL7 EVENT TYPE CODE (including data)

> **NOTE:** You already have the 'HL7 EVENT TYPE CODE' File.

I will OVERWRITE your data with mine.

779.002 HL7 ACKNOWLEDGMENT CODE (including data)

> **NOTE:** You already have the 'HL7 ACKNOWLEDGMENT CODE' File.

I will OVERWRITE your data with mine.

779.003 HL7 ACCEPT/APPLICATION ACK CONDITION (including data)

> **NOTE:** You already have the 'HL7 ACCEPT/APPLICATION ACK CONDITION' File.

I will OVERWRITE your data with mine.

779.004 COUNTRY CODE (including data)

> **NOTE:** You already have the 'COUNTRY CODE' File.

I will OVERWRITE your data with mine.

869.1 HL LOWER LEVEL PROTOCOL TYPE (including data)

> **NOTE:** You already have the 'HL LOWER LEVEL PROTOCOL TYPE' File.

I will MERGE your data with mine.

869.2 HL LOWER LEVEL PROTOCOL PARAMETER

> **NOTE:** You already have the 'HL LOWER LEVEL PROTOCOL PARAMETER' File.

869.3 HL COMMUNICATION SERVER PARAMETERS

> **NOTE:** You already have the 'HL COMMUNICATION SERVER PARAMETERS' File.

870 HL LOGICAL LINK

> **NOTE:** You already have the 'HL LOGICAL LINK' File.

SHALL I WRITE OVER FILE SECURITY CODES? No// <u>\<RET\></u> (No)

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? Yes// <u>\<RET\></u> (Yes)

# Step 10. Initialization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? Yes// <u>\<RET\></u> (Yes)

ARE YOU SURE EVERYTHING'S OK? No// <u>YES</u>

Starting Pre-Init

Pre-Init Finished

...EXCUSE ME, I'M WORKING AS FAST AS I CAN....................................

..............................................................................

........................................................

Compiling Cross-Reference(s) of File 101.

...SORRY, THIS MAY TAKE A FEW MOMENTS...

'ORD11' ROUTINE FILED.

'ORD12' ROUTINE FILED.

'ORD13' ROUTINE FILED.

'ORD14' ROUTINE FILED.

'ORD15' ROUTINE FILED.

'ORD16' ROUTINE FILED.

'ORD17' ROUTINE FILED.

'ORD18' ROUTINE FILED.

'ORD19' ROUTINE FILED.

'ORD110' ROUTINE FILED.

'ORD111' ROUTINE FILED.

'ORD112' ROUTINE FILED.

'ORD1' ROUTINE FILED..........................................................

......

'HL CLEAR COMMUNICATIONS ERROR' Option Filed

'HL CLEAR QUEUE' Option Filed

'HL COMMUNICATIONS SERVER' Option Filed

'HL COPY QUEUE ENTRY' Option Filed

'HL CRE/ED QUEUE TEST ENTRY' Option Filed

'HL CUSTOM REPORT' Option Filed

'HL EDIT APPL PARAM' Option Filed

'HL EDIT COMM SERVER PARAMETERS' Option Filed

'HL EDIT SITE PARAM' Option Filed

'HL FILER MONITOR' Option Filed

'HL INTERFACE WORKBENCH' Option Filed

'HL MAIN MENU' Option Filed

'HL MANAGE FILERS' Option Filed

'HL MENU 1.5' Option Filed

'HL MENU 1.6' Option Filed

'HL MESSAGE MONITOR' Option Filed

'HL MESSAGE REQUEUER' Option Filed

'HL MS SERVER' Option Filed

'HL PRINT APPL PARAM' Option Filed

'HL PRINT DATA TYPE' Option Filed

'HL PRINT FAILED TRANS' Option Filed

'HL PRINT FIELDS' Option Filed

'HL PRINT MENU' Option Filed

'HL PRINT MSG TYPE' Option Filed

'HL PRINT PENDING TRANS' Option Filed

'HL PRINT SEGMENT' Option Filed

'HL PRINT SITE PARAM' Option Filed

# Step 10. Initialization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

'HL PRINT VERSION' Option Filed

'HL PURGE TRANSMISSIONS' Option Filed

'HL QUEUE MANAGEMENT' Option Filed

'HL SERVER' Option Filed

'HL SHOW COMMUNICATIONS ERROR' Option Filed

'HL START' Option Filed

'HL START DEFAULT FILERS' Option Filed

'HL START ONE INCOMING FILER' Option Filed

'HL START ONE OUTGOING FILER' Option Filed

'HL STOP' Option Filed

'HL STOP ALL INCOMING FILERS' Option Filed

'HL STOP ALL OUTGOING FILERS' Option Filed

'HL STOP ONE INCOMING FILER' Option Filed

'HL STOP ONE OUTGOING FILER' Option Filed

'HL TASK' Option Filed

'HL TRANSMISSION LOG' Option Filed

'HL V16 SERVER' Option Filed..

NO SECURITY-CODE PROTECTION HAS BEEN MADE

Initial entry in HL COMMUNICATION SERVER PARAMETER file

(#869.3) has been created.

This version of 'HLONIT' was created on 13-SEP-1995

(at ALBANY CAMPUS DEVELOPMENT, by OE/RR V.2.5)

PROTOCOL INSTALLATION

...OK, this may take a while, hold on please..................................

..............................................

'HL CS/RQ - DESELECT MESSAGES' Protocol Filed

'HL CS/RQ - SELECT MESSAGES' Protocol Filed

'HL CS/RQ - VIEW MESSAGE' Protocol Filed

'HL CS/RQ MENU - SCREEN 2' Protocol Filed

'HL DT/IW - ACTIVATE/INACTIVATE APPLICATION' Protocol Filed

'HL DT/IW - AI FOR SCREEN 1' Protocol Filed

'HL DT/IW - BLANK 1' Protocol Filed

'HL DT/IW - BLANK 2' Protocol Filed

'HL DT/IW - BLANK 3' Protocol Filed

'HL DT/IW - CA FOR SCREEN 1' Protocol Filed

'HL DT/IW - CC FOR SCREEN 4' Protocol Filed

'HL DT/IW - CL FOR SCREEN 2' Protocol Filed

'HL DT/IW - CREATE APPLICATION' Protocol Filed

'HL DT/IW - CREATE CLIENT PROTOCOL' Protocol Filed

'HL DT/IW - CREATE LOGICAL LINK' Protocol Filed

'HL DT/IW - CREATE SERVER PROTOCOL' Protocol Filed

'HL DT/IW - CS FOR SCREEN 3' Protocol Filed

'HL DT/IW - DA FOR SCREEN 1' Protocol Filed

'HL DT/IW - DC FOR SCREEN 4' Protocol Filed

'HL DT/IW - DELETE APPLICATION' Protocol Filed

'HL DT/IW - DELETE CLIENT PROTOCOL' Protocol Filed

'HL DT/IW - DELETE LOGICAL LINK' Protocol Filed

'HL DT/IW - DELETE SERVER PROTOCOL' Protocol Filed

'HL DT/IW - DL FOR SCREEN 2' Protocol Filed

# Step 10. Initialization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

'HL DT/IW - DS FOR SCREEN 3' Protocol Filed

'HL DT/IW - EA FOR SCREEN 1' Protocol Filed

'HL DT/IW - EC FOR SCREEN 4' Protocol Filed

'HL DT/IW - EDIT APPLICATION' Protocol Filed

'HL DT/IW - EDIT CLIENT PROTOCOL' Protocol Filed

'HL DT/IW - EDIT LOGICAL LINK' Protocol Filed

'HL DT/IW - EDIT SERVER PROTOCOL' Protocol Filed

'HL DT/IW - EL FOR SCREEN 2' Protocol Filed

'HL DT/IW - ES FOR SCREEN 3' Protocol Filed

'HL DT/IW - JUMP TO APPLICATION (SCREEN 1)' Protocol Filed

'HL DT/IW - JUMP TO CLIENT (SCREEN 4)' Protocol Filed

'HL DT/IW - JUMP TO LINK (SCREEN 2)' Protocol Filed

'HL DT/IW - JUMP TO NEXT APP (SCREEN 1)' Protocol Filed

'HL DT/IW - JUMP TO NEXT CLIENT (SCREEN 4)' Protocol Filed

'HL DT/IW - JUMP TO NEXT LINK (SCREEN 2)' Protocol Filed

'HL DT/IW - JUMP TO NEXT SERVER (SCREEN 3)' Protocol Filed

'HL DT/IW - JUMP TO NEXT SERVER (SCREEN 5)' Protocol Filed

'HL DT/IW - JUMP TO PREVIOUS APP (SCREEN 1)' Protocol Filed

'HL DT/IW - JUMP TO PREVIOUS CLNT (SCREEN 4)' Protocol Filed

'HL DT/IW - JUMP TO PREVIOUS LINK (SCREEN 2)' Protocol Filed

'HL DT/IW - JUMP TO PREVIOUS SRVR (SCREEN 3)' Protocol Filed

'HL DT/IW - JUMP TO PREVIOUS SRVR (SCREEN 5)' Protocol Filed

'HL DT/IW - JUMP TO SERVER (SCREEN 3)' Protocol Filed

'HL DT/IW - JUMP TO SERVER (SCREEN 5)' Protocol Filed

'HL DT/IW - REBUILD SCREEN 1' Protocol Filed

'HL DT/IW - REBUILD SCREEN 2' Protocol Filed

'HL DT/IW - REBUILD SCREEN 3' Protocol Filed

'HL DT/IW - REBUILD SCREEN 4' Protocol Filed

'HL DT/IW - REBUILD SCREEN 5' Protocol Filed

'HL DT/IW - REMOVE SUBSCRIPTION' Protocol Filed

'HL DT/IW - RS FOR SCREEN 5' Protocol Filed

'HL DT/IW - S2 FOR SCREEN 5' Protocol Filed

'HL DT/IW - SHOW CLIENT PROTOCOLS' Protocol Filed

'HL DT/IW - SHOW LOGICAL LINKS' Protocol Filed

'HL DT/IW - SHOW SERVER PROTOCOLS' Protocol Filed

'HL DT/IW - SUBSCRIBE' Protocol Filed

'HL DT/IW - SUBSCRIBE TO SERVER' Protocol Filed

'HL DT/IW MENU - SCREEN 1' Protocol Filed

'HL DT/IW MENU - SCREEN 2' Protocol Filed

'HL DT/IW MENU - SCREEN 3' Protocol Filed

'HL DT/IW MENU - SCREEN 4' Protocol Filed

'HL DT/IW MENU - SCREEN 5' Protocol Filed

OK, Protocol Installation is Complete.

'HL INTERFACE WORKBENCH - 1' List Template...Filed.

'HL INTERFACE WORKBENCH - 2' List Template...Filed.

'HL INTERFACE WORKBENCH - 3' List Template...Filed.

'HL INTERFACE WORKBENCH - 4' List Template...Filed.

'HL INTERFACE WORKBENCH - 5' List Template...Filed.

'HL MESSAGE REQUEUER - 1' List Template...Filed.

'HL MESSAGE REQUEUER - 2' List Template...Filed.

'HL MESSAGE REQUEUER - 3' List Template...Filed.

Select output device for file conversion: HOME// <u>\<RET\></u> LAT

# Step 10. Initialization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\- File conversions started on 13-SEP-95 @ 06:39:31 -

Copying entries from HL7 NON-DHCP APPLICATION PARAMETER file (#770)

to HL7 APPLICATION PARAMETER file (#771)

Purging data from HL7 MESSAGE TEXT file (#772) ..........................................

Converting newly defined fields in HL7 MESSAGE TEXT file (#772) ...

\- File conversions completed on 13-SEP-95 @ 06:39:51 -

\>

# Step 11. Add The HL7 Main Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\><u>D P^DI</u>

VA FileMan 21

Select OPTION: <u>ENTER</u> OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: OPTION// <u>19</u> OPTION (3071 entries)

EDIT WHICH FIELD: ALL// <u>MENU</u>

1 MENU (multiple)

2 MENU TEXT

CHOOSE 1-2: <u>1</u>

EDIT WHICH MENU SUB-FIELD: ALL// <u>\<RET\></u>

THEN EDIT FIELD: <u>\<RET\></u>

Select OPTION NAME: <u>EVE</u> System Manager Menu

Select ITEM: <u>HL MAIN MENU</u> HL7 Main Menu

ARE YOU ADDING 'HL MAIN MENU' AS A NEW MENU (THE 9TH FOR THIS OPTION)? <u>Y</u>

(YES)

MENU SYNONYM: <u>\<RET\></u>

SYNONYM: <u>\<RET\></u>

DISPLAY ORDER: <u>\<RET\></u>

Select ITEM: <u>^</u>

Select OPTION NAME: <u>\<RET\></u>

Select OPTION: <u>\<RET\></u>

\>