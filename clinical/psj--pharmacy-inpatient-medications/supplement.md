---
title: Inpatient Medications Pharmacy Interface Automation (PIA) Startup and Troubleshooting Guide (updated for PSJ*5*432)
doc_type: SUP
doc_label: Supplement
doc_layer: plain
doc_subject: 
app_code: PSJ
app_name: "Pharmacy: Inpatient Medications"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: 
  - PSJ PADE ADV
  - PSJ PADE MGR
  - PSS PADE INIT
menu_options: 0
description: 
audience: 
keywords: 
  - pade
  - span
  - class
  - clinic
  - send
  - mark
  - setup
  - group
  - messages
  - device
page_count: 0
word_count: 14443
section_count: 16
table_count: 1
figure_count: 30
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2022
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_tg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_tg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=88"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Pharmacy Interface Automation (PIA)

  Startup and Troubleshooting Guide
---

![](inpatient-medications-pharmacy-interface-automation-pia-startup-and-troubleshoot/001.png)

June 2022

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Enterprise Program Management Office (EPMO)

Revision History

<table>
<caption><p><span id="_Toc508171887" class="anchor"></span>Table 1: Phase 2: Outbound to PADE Setup</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 11%" />
<col style="width: 44%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>06/22/2022</td>
<td>0.5</td>
<td>PSJ*5.0*432 - Added <u>3.4.2.9</u> Re-Send Orders at Check-In Parameter Description.</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>05/02/2018</td>
<td>0.4</td>
<td><p>Tech Edits:</p>
<p>From REDACTED</p></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>03/07/2018</td>
<td>0.3</td>
<td><p>Tech Edits:</p>
<ul>
<li><p>Reformatted document to follow current OIT Documentation Standards and Style Guidelines (e.g., added Title page, updated all styles and formatting throughout, added figure captions, etc.).</p></li>
<li><p>Accepted all previous tracked changes.</p></li>
<li><p>Verified Word document is currently Section 508 conformant (no errors remain).</p></li>
</ul></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>??/??/2018</td>
<td>0.2</td>
<td><p>Reviewed and updated document:</p>
<ul>
<li><p>Changed “Healthconnect” to “Health Connect” throughout the document.</p></li>
<li><p>???</p></li>
</ul></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>??/??/2018</td>
<td>0.1</td>
<td>Initial Document.</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

<span id="_Toc508171887" class="anchor"></span>Table 1: Phase 2: Outbound to PADE Setup

Table of Contents

List of Figures

List of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Phase 1: ACL Request/Connectivity Setup Checklist](#phase-1-acl-requestconnectivity-setup-checklist)
  - [ACL Connectivity Setup](#acl-connectivity-setup)
- [Phase 2: Outbound to PADE Setup](#phase-2-outbound-to-pade-setup)
  - [Security Keys](#security-keys)
  - [Logical Link](#logical-link)
  - [PSJ PADE MAIN MENU Options](#psj-pade-main-menu-options)
  - [Accessing the PADE Main Menu](#accessing-the-pade-main-menu)
    - [PADE Send Area Setup](#pade-send-area-setup)
    - [PADE System Setup](#pade-system-setup)
  - [PADE Send Surgery Cases](#pade-send-surgery-cases)
  - [PADE Send Patient Orders](#pade-send-patient-orders)
  - [Nightly Job](#nightly-job)
- [Phase 3: Inbound to VistA Setup](#phase-3-inbound-to-vista-setup)
  - [HL7 Multi-Listener](#hl7-multi-listener)
  - [PADE Inbound Setup Capture](#pade-inbound-setup-capture)
  - [PADE Inventory System](#pade-inventory-system)
    - [DWO Message Entity](#dwo-message-entity)
    - [DWO Entity Mail Group](#dwo-entity-mail-group)
    - [Config Errors Mail Group](#config-errors-mail-group)
    - [Data Errors Mail Group](#data-errors-mail-group)
    - [Alternate System Name](#alternate-system-name)
    - [Display PADE Balances in IOE?](#display-pade-balances-in-ioe)
  - [Set Up PADE Dispensing Device (Cabinet)](#set-up-pade-dispensing-device-cabinet)
    - [Dispensing Device](#dispensing-device)
    - [PADE Status](#pade-status)
    - [Reset/Initialize PADE Device?](#resetinitialize-pade-device)
    - [Delete Single Drug from PADE Cabinet?](#delete-single-drug-from-pade-cabinet)
    - [Division](#division)
    - [Ward Group](#ward-group)
    - [Ward Location](#ward-location)
    - [Clinic Group](#clinic-group)
    - [Clinic Location](#clinic-location)
    - [Wildcard Clinic Name](#wildcard-clinic-name)
    - [Send 'PATIENT NOT ON FILE' Msg](#send-patient-not-on-file-msg)
    - [Send DWO Messages?](#send-dwo-messages)
    - [DWO Entity Mail Group](#dwo-entity-mail-group-1)
  - [PADE Inventory Error Messages](#pade-inventory-error-messages)
  - [Dispensed Without Orders (DWO) Messages](#dispensed-without-orders-dwo-messages)
- [Phase 4: Implementation](#phase-4-implementation)
- [Troubleshooting](#troubleshooting)
  - [Key Contacts](#key-contacts)
The Pharmacy Interface Automation project created an automated interface between the Pharmacy Automated Dispensing Equipment (PADE) used in the inpatient and outpatient care settings and Veterans Health Information Systems and Technology Architecture (VistA). The purpose of this Setup and Troubleshooting Guide is to walk through the setup of the Pharmacy Interface Automation (PIA) functionality included in patches PSJ\*5\*317 and PSS\*1\*193.
![](inpatient-medications-pharmacy-interface-automation-pia-startup-and-troubleshoot/002.png) CAUTION: It is highly suggested that you read the supporting documentation *BEFORE* beginning with setup.
Supporting documents are listed below:
- User Manual
- Technical Manual
- Installation Guide (this is for VistA installation)
We *recommend* the following approach to begin setting up and using the Pharmacy Interface Automation functionality. This will vary greatly from site to site and depend on the vendor at the site. Click the links for details:
- [<u>Phase 1: ACL Request/Connectivity Setup Checklist</u>](\l) (2-3 weeks)
  - Outbound (Health Connect à PADE)
  - Inbound (PADE à Health Connect)
- [<u>Phase 2: Outbound to PADE Setup</u>](\l)
![](inpatient-medications-pharmacy-interface-automation-pia-startup-and-troubleshoot/003.png) NOTE: The outbound setup can be started while waiting for ACL approval and connectivity.
- [<u>Phase 3: Inbound to VistA Setup</u>](\l)
![](inpatient-medications-pharmacy-interface-automation-pia-startup-and-troubleshoot/004.png) NOTE: Wait until Health Connect connectivity is established to begin setup.
- <u>Phase 4: Implementation</u>

# Phase 1: ACL Request/Connectivity Setup Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Phase 1 Roles:

The following roles are involved with Phase 1: ACL Request/Connectivity Setup Checklist:

- Region COTS team
- Biomed group
- VIE National Admins REDACTED
- Region LAN group
- Region IT support
- REDACTED
- Vendor Engineer
- Pharmacy

![](inpatient-medications-pharmacy-interface-automation-pia-startup-and-troubleshoot/005.png) NOTE: It may take up to two to three weeks to setup your ACL.

## ACL Connectivity Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the steps to get an ACL connection established:

1.  Ensure the latest patches are installed in VistA (PSJ\*5\*317 and PSS\*1\*193).
2.  System owners (e.g., Biomed or Pharmacy depending on the site setup) need to initiate changes to the VLAN ACL for the PADE system(s) via a CA Ticket that lists all changes needed to be done to the ACL:
1.  Work with VistA Interface Engine (VIE) national admin group (VIE National Admins REDACTED to get the exact information that needs to go into the ticket:
    1.  Open CA ticket for their support.
    2.  Email: REDACTED
    3.  Get confirmation that the ACLs are open.
3.  Conduct connectivity testing (testing of communication of information)–suggest getting a call with all parties (usually about one hour):
1.  Confirm Health Connect can establish a connection to the VistA Health Level Seven (HL7) multi-listener (Inbound).
2.  Test Health Connect to vendor (Outbound).
3.  Test vendor to Health Connect (Inbound).
4.  Test communication to/from VistA and Health Connect.
5.  Suggest sending a few test patients or drug information to PADE and having information from PADE come back into VistA to make sure the communication is going through properly.

![](inpatient-medications-pharmacy-interface-automation-pia-startup-and-troubleshoot/006.png) REF: For more details on Inbound Setup, see Section <u>4</u>, “[Phase 3 Inbound to VistA Setup](#phase-3-inbound-to-vista-setup).”

# Phase 2: Outbound to PADE Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In Phase 2, the setup will be configured in VistA to send the information to the appropriate PADE. Phase 2 can happen simultaneously with [Phase 1](#phase-1-acl-requestconnectivity-setup-checklist). The main purpose of the outbound setup is to map the send areas to the location of the cabinets in the wards, clinics, and/or operating rooms.

Phase 2 Roles:

The following roles are involved with Phase 2: Outbound to PADE Setup:

- Pharmacy Staff (Automated Data Processing Application Coordinator \[ADPAC\])
- Vendor Engineer or Implementation Support
- REDACTED
- VIE National Admins REDACTED
- Region Information Technology (IT) support (if needed)

<table>
<caption><p><span id="_Ref508176572" class="anchor"></span>Table 2: Security Keys for Outbound and Inbound PADE Setup</p></caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 49%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th>Phase 2:</th>
<th>Step (click link for more details.)</th>
<th>POC</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>☐</td>
<td><ol type="1">
<li><blockquote>
<p>Confirm Vendor point of contact (POCs) and adjust contract if needed.</p>
</blockquote></li>
</ol></td>
<td>Pharmacy Staff / Biomed</td>
</tr>
<tr class="even">
<td>☐</td>
<td><ol start="2" type="1">
<li><blockquote>
<p><a href="#psj-pade-main-menu-options">Determine that you have the appropriate <u>security keys</u> and <u>menus.</u></a></p>
</blockquote></li>
</ol></td>
<td>Pharmacy</td>
</tr>
<tr class="odd">
<td>☐</td>
<td><ol start="3" type="1">
<li><blockquote>
<p><a href="#logical-link">PSJ PADE Logical Link Setup</a>.</p>
</blockquote></li>
</ol></td>
<td></td>
</tr>
<tr class="even">
<td>☐</td>
<td><ol start="4" type="1">
<li><blockquote>
<p>(SA) <a href="#pade-send-area-setup">PADE Send Area Setup</a>.</p>
</blockquote></li>
</ol></td>
<td></td>
</tr>
<tr class="odd">
<td>☐</td>
<td><ol start="5" type="1">
<li><blockquote>
<p>(SS) <a href="#pade-system-setup">PADE System Setup</a>.</p>
</blockquote></li>
</ol></td>
<td></td>
</tr>
<tr class="even">
<td>☐</td>
<td><ol start="6" type="1">
<li><blockquote>
<p>(SO) <a href="#pade-system-setup">PADE Send Patient Orders</a>.</p>
</blockquote></li>
</ol></td>
<td></td>
</tr>
<tr class="odd">
<td>☐</td>
<td><ol start="7" type="1">
<li><blockquote>
<p><a href="#pade-send-surgery-cases">Nightly Job</a>.</p>
</blockquote></li>
</ol></td>
<td></td>
</tr>
<tr class="even">
<td>☐</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>☐</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>☐</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Ref508176572" class="anchor"></span>Table 2: Security Keys for Outbound and Inbound PADE Setup

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 2</u> lists the security keys needed for Outbound and Inbound PADE setup and functionality.

| Security Key  | Description                                                                                                                                                                                                                                                                                                                       |
|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSJ PADE MGR  | This security key is given to Pharmacy users who will need full access to the PSJ PADE MAIN MENU, including the PADE System setup.                                                                                                                                                                                                |
| PSJ PADE ADV  | This security key is given to Pharmacy users in addition to the PSJ PADE MGR security key to prevent the user from PADE System setup like IP address/port, and to allow setting up division specific lower level parameters (i.e., wards and clinics) of the PADE system.                                                         |
| PSS PADE INIT | This security key enables users to transmit the entire drug file (or UD and IV marked drugs) to Pharmacy Automated Dispensing Equipment (PADE) System(s) within the Send Drug File Entries to External Interface VistA option. This action is typically a onetime event to send a copy of the formulary to a new PADE vendor. |

<span id="_Ref508115208" class="anchor"></span>Table 3: PSJ PADE MAIN MENU Options (Functions)

## Logical Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To set up your logical links, complete the following steps:

1.  From the HL7 Main Menu, select the Interface Developer Options menu.

<span id="_Toc103081832" class="anchor"></span>Figure 1: HL7 Main Menu—Selecting Interface Developer Options Menu

Select OPTION NAME: <span class="mark">HL7 MAIN MENU \<Enter\></span> HL MAIN MENU HL7 Main Menu

Event monitoring menu ...

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

<span class="mark">Interface Developer Options ...</span>

Site Parameter Edit

HLO HL7 (Optimized) MAIN MENU ...

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

Select HL7 Main Menu \<TEST ACCOUNT\> Option: <span class="mark">Interface Developer Options</span>

4.  From the Interface Developer Options menu, select the EL—Link Edit option.

<span id="_Toc103081833" class="anchor"></span>Figure 2: Interface Developer Options Menu—Selecting Link Edit Option

EA Application Edit

EP Protocol Edit

<span class="mark">EL Link Edit</span>

VI Validate Interfaces

Reports ...

Select Interface Developer Options \<TEST ACCOUNT\> Option: <span class="mark">EL \<Enter\></span> Link Edit

5.  From the EL—Link Edit option, at the “HL LOGICAL LINK NODE:” prompt, enter PSJ PADE.  
      
    The system puts you into ScreenMan mode. Tab down to the “LLP TYPE” field and press \<Enter\>. The “TCP LOWER LEVEL PARAMETERS” screen is displayed (<u>Figure 4</u>).

<span id="_Toc103081834" class="anchor"></span>Figure 3: Link Edit option—Selecting Logical Link Node

Select HL LOGICAL LINK NODE: <span class="mark">PSJ PADE</span>HL7 LOGICAL LINK-------------------------------------------------------------------------

<u>NODE</u>: PSJ PADE DESCRIPTION:

INSTITUTION:

MAILMAN DOMAIN:

AUTOSTART: Enabled

QUEUE SIZE: 10

<span class="mark"><u>LLP TYPE</u>: TCP</span>

DNS DOMAIN:

6.  From the “TCP LOWER LEVEL PARAMETERS” screen for the PSJ PADE node:
1.  Tab to the “TCP/IP ADDRESS:” field and update the entry with the Health Connect IP address.
2.  Tab to the “TCP/IP PORT:” field and update the entry with the Health Connect port.

> <span id="_Ref508115030" class="anchor"></span>Figure 4: HL Logical Link (ScreenMan)—Updating IP Address and Port

> HL7 LOGICAL LINK

> ----------------------------------------------------------------------

> TCP LOWER LEVEL PARAMETERS

>  PSJ PADE 

>  

>  TCP/IP SERVICE TYPE: CLIENT (SENDER) 

>  TCP/IP ADDRESS: *<span class="mark">update with the Health Connect IP address</span>* 

>  TCP/IP PORT: *<span class="mark">update with the Health Connect port</span>* 

>  TCP/IP PORT (OPTIMIZED): 

>  

>  ACK TIMEOUT: RE-TRANSMISION ATTEMPTS: 5 

>  READ TIMEOUT: EXCEED RE-TRANSMIT ACTION: 

>  BLOCK SIZE: SAY HELO: 

>  TCP/IP OPENFAIL TIMEOUT: 

> STARTUP NODE: PERSISTENT: 

>  RETENTION: UNI-DIRECTIONAL WAIT: 

> 

## PSJ PADE MAIN MENU Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 3</u> lists the options (functions) that you can access from the PSJ PADE MAIN MENU:

<table>
<caption><p><span id="_Toc508171890" class="anchor"></span>Table 4: Phase 3: Inbound to VistA Tasks</p></caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 30%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>Synonym</th>
<th>Option Text [Name]</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SA</td>
<td>PADE Send Area Setup</td>
<td>This option is used to setup the Pharmacy Automated Dispensing Equipment (PADE) send area, which will help map locations to the cabinets on the vendor systems.</td>
</tr>
<tr class="even">
<td>SS</td>
<td>PADE System Setup</td>
<td>This option is used to setup the PADE system (e.g., Pyxis, OmniCell, AccuDose, etc.) that supports single/multiple cabinets, located in Inpatient Wards and Outpatient Clinics to stock items (drug/<em>non</em>-drug) for dispensing.</td>
</tr>
<tr class="odd">
<td>IN</td>
<td>PADE Inventory Setup</td>
<td><p>This menu contains options used to set up PADE Inbound information.</p>
<p>PADE vendor system parameters can be set, including the activation of the display of vendor drug item balances in the Inpatient Order Entry and the entry of mail groups to which inbound HL7 error messages are sent. Individual PADE dispensing device (cabinet) parameters can also be defined, including:</p>
<ul>
<li><p>Initializing the device.</p></li>
<li><p>Activating/Inactivating the device.</p></li>
<li><p>Linking the device to a hospital division and ward or clinic location.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>RP</td>
<td>PADE Reports</td>
<td><p>This menu contains options to run PADE Inbound inventory reports.</p>
<p>The PADE Transaction Report contains information on individual HL7 transactions received from the PADE vendor, and is run for a specific date range. The PADE On Hand Report contains current inventory information for each drug item stocked in each PADE dispensing device (cabinet).</p></td>
</tr>
<tr class="odd">
<td>SC</td>
<td>PADE Send Surgery Cases</td>
<td>This option can be used to send surgery cases manually to a PADE for that date or future date.</td>
</tr>
<tr class="even">
<td>SO</td>
<td>PADE Send Patient Orders</td>
<td>This option is used to send UD/IV orders to PADE.</td>
</tr>
</tbody>
</table>

<span id="_Toc508171890" class="anchor"></span>Table 4: Phase 3: Inbound to VistA Tasks

## Accessing the PADE Main Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PADE Main Menu \[PSJ PADE MAIN MENU\] is located on the Unit Dose Medications menu \[PSJU MGR \]. The PADE Main Menu is locked with the PSJ PADE MGR security key.

<span id="_Toc103081836" class="anchor"></span>Figure 5: Accessing the PADE Main Menu—Sample User Entries and System Responses

Select OPTION NAME: <span class="mark">PSJU MGR Unit Dose Medications</span>

(Inpatient Medications - Version 5.0 09/17/98)

Align Labels (Unit Dose)

Discontinue All of a Patient's Orders

ECO Edit Clinic Med Orders Start Date/Time

EUP Edit Inpatient User Parameters

IOE Inpatient Order Entry

IPF Inpatient Profile

Check Drug Interaction

INQuiries Menu ...

Label Print/Reprint

Non-Verified/Pending Orders

Order Entry

<span class="mark">PADE Main Menu ...</span>

PAtient Profile (Unit Dose)

Reports Menu ...

Supervisor's Menu ...

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

Select Unit Dose Medications \<TEST ACCOUNT\> Option: <span class="mark">PADE Main Menu</span>

SA PADE Send Area Setup

SS PADE System Setup

IN PADE Inventory Setup ...

RP PADE Reports ...

SC PADE Send Surgery Cases

<span id="pade_sendpatientorders_so" class="anchor"></span>SO PADE Send Patient Orders

### PADE Send Area Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Coordinate with your vendor to get a list of send areas on the vendor side, so when the message is sent the vendor will know to which cabinet to route the message.

<span id="_Toc103081837" class="anchor"></span>Figure 6: PADE Send Area Setup Option—Sample User Entries and System Responses

<span class="mark">SA PADE Send Area Setup</span>

SS PADE System Setup

IN PADE Inventory Setup ...

RP PADE Reports ...

SC PADE Send Surgery Cases

SO PADE Send Patient Orders

Select PADE Main Menu \<TEST ACCOUNT\> Option: <span class="mark">SA \<Enter\></span> PADE Send Area Setup

Select PADE SEND AREA: <span class="mark">??</span>

Choose from:

EMERGENCY ROOM 1

EMERGENCY ROOM 2

MIKE’S CLINIC GROUP SA

NICU FLOOR 7

OP CLINIC

SURGERY FLOOR 2

You may enter a new PADE SEND AREA, if you wish. These are the pre-defined locations on the PADE vendor system where the messages will be sent to.

Select PADE SEND AREA:

### PADE System Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PADE SYSTEM SETUP is the name of the Pharmacy Automated Dispensing Equipment (PADE) system (e.g., Pyxis, OmniCell, AccuDose etc.) that supports single/multiple cabinets, located in Inpatient Wards and Outpatient Clinics to stock items (drug/*non*-drug) for dispensing.

<u>Figure 7</u> shows you how to enter a new PADE SYSTEM SETUP:

<span id="_Ref508177540" class="anchor"></span>Figure 7: PADE System Setup Option—Sample User Entries and System Responses

SA PADE Send Area Setup

<span class="mark">SS PADE System Setup</span>

IN PADE Inventory Setup ...

RP PADE Reports ...

SC PADE Send Surgery Cases

SO PADE Send Patient Orders

Select PADE Main Menu \<TEST ACCOUNT\> Option: <span class="mark">SS \<Enter\></span> PADE System Setup

Select PADE SYSTEM SETUP: <span class="mark">??</span>

Choose from:

ASEYNT

OMNICELL

PYXIS

Select PADE SYSTEM SETUP: <span class="mark">PYXIS</span>

PADE SYSTEM: PYXIS// <span class="mark">\<Enter\></span>

DNS NAME/IP ADDRESS: 10.168.11.186// <span class="mark">??</span>

This is the DNS name or the IP address of the PADE System.

DNS NAME/IP ADDRESS: 10.168.11.186// <span class="mark">\<Enter\></span>

PORT: 4800// <span class="mark">??</span>

This is the port number associated with the PADE System.

PORT: 4800// <span class="mark">\<Enter\></span>

SEND DRUG FILE MESSAGES: NONE//

#### Send Drug File Messages

The SEND DRUG FILE MESSAGES prompt of the PADE SYSTEM SETUP option \[PSJ PADE SETUP\] will determine if the user will be prompted to send HL7 drug formulary messages to PADE when using the DRUG ENTER/EDIT option \[PSS DRUG ENTER/EDIT\]. When set to N (for New DRUGS), the user will be prompted to send a message to PADE only when the DRUG ENTER/EDIT option is used to create NEW entries.

If the parameter is set to U (for UPDATES) then the user is only prompted to send messages when updating/changing current entries with the DRUG ENTER/EDIT OPTION. If this parameter is set to B (for BOTH), then the user is prompted during both of these scenarios. If the parameter is set to X (or left NULL/blank), then the user is never prompted to send NEW or UPDATES to PADE when using the DRUG ENTER/EDIT option.

This parameter does *not* impact the functioning of the Send Drug File Entries to External Interface option \[PSS MASTER FILE ALL\], which can always be used to send the formulary update messages for one or all appropriate drugs to PADE.

<span id="_Toc103081839" class="anchor"></span>Figure 8: Send Drug File Messages Prompt—Sample User Entries and System Responses

SEND DRUG FILE MESSAGES: NONE// <span class="mark">??</span>

Choose from:

N NEW DRUGS

U UPDATES

B BOTH

X NONE

SEND DRUG FILE MESSAGES: BOTH//

#### Inactive Date

<u>Figure 9</u> is an example of the PADE inactivation date. This is the date on or after which the division will no longer communicate with the PADE system. If the year is omitted, the computer uses *current year.* Two-digit year assumes no more than 20 years in the future, or 80 years in the past.

<span id="_Ref508116217" class="anchor"></span>Figure 9: Inactive Date—Examples of Valid Dates

INACTIVE DATE: ?

Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.

T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.

![](inpatient-medications-pharmacy-interface-automation-pia-startup-and-troubleshoot/007.png) IMPORTANT: Until your site is ready to use PADE, it is *recommended* that you set the inactivation date to “T-1” to prevent generation of HL7 messages. Once your site is ready to use PADE, this inactivation date should be deleted.

#### Send Checkin/Surg HL7 for INPT

This is vendor-dependent and should only be set to NO when it is known that these messages could cause the inpatient to be removed from their Internet Protocol (IP) location on the vendor device.

<span id="_Toc103081841" class="anchor"></span>Figure 10: Send Checkin/Surg HL7 for INPT Prompt—Sample User Entries and System Responses

SEND CHECKIN/SURG HL7 FOR INPT: YES// ?

Choose from:

Y YES

N NO

#### Days To Pull Ahead for BG Job

Check-in for a clinic generates HL7 messages to PADE in real time. For clinics that do *not* have check-in, there is a nightly background (BG) job that can be scheduled to run on a daily basis that will generate HL7 messages to PADE. If there is a need for you to send clinic appointments for future days as well then populating this field helps to pull those appointments in your nightly BG job. The system allows a maximum of 30 days, but keep this to a minimum as it may impact your network traffic.

#### Select Division

DIVISION is the MEDICAL CENTER DIVISION associated with the WARDS and CLINICS that are to be defined for this PADE system. You will only be able to define WARDS and Clinics that are associated with this DIVISION.

Users with the PSJ PADE ADV key can only edit existing divisions in the Multiple and *cannot* add new ones.

Figure 11: Select Division Prompt—Sample User Entries and System Responses

Select DIVISION: XXXXX// <span class="mark">??</span>

Choose from:

1 TROY 888

2 XXXXX 500

9 CINCINNATI 539

10 ALB-PRRTP 500PA

11 XXXXX OPC 500A4

12 ISC 3 13000

Select DIVISION: XXXXX// <span class="mark">\<Enter\></span>

DIVISION: XXXXX// <span class="mark">\<Enter\></span>

#### Send Clinic IV Package Orders

At the “SEND CLINIC IV PACKAGE ORDERS?: YES//” prompt, enter YES if all IV package orders associated with clinics of this division will send messages to PADE.

Figure 12: Send Clinic IV Package Orders Prompt—Sample User Entries and System Responses

SEND CLINIC IV PACKAGE ORDERS?: YES// ??

Choose from:

Y YES

N NO

SEND CLINIC IV PACKAGE ORDERS?: YES// <span class="mark">\<Enter\></span>

#### Send Surgery Messages

At the “SEND SURGERY MESSAGES?: YES//” prompt, enter YES to send ADT messages for surgical cases scheduled in operating rooms defined within this division. This feature may *not* be needed if surgical cases for this division have associated clinic appointments into which patients are being checked into.

Figure 13: Send Surgery Messages Prompt—Sample User Entries and System Responses

SEND SURGERY MESSAGES?: YES// <span class="mark">??</span>

Choose from:

Y YES

N NO

SEND SURGERY MESSAGES?: YES// <span class="mark">\<Enter\></span>

#### Send Pharmacy Order Messages

At the “SEND ORDER MESSAGES?: YES//” prompt, enter YES to allow pharmacy order messages from the inpatient medication package (including clinic orders) to be sent for wards and clinics defined in the PADE parameters for this division.

Figure 14: Send Pharmacy Order Messages Prompt—Sample User Entries and System Responses

SEND ORDER MESSAGES?: YES// <span class="mark">??</span>

Choose from:

Y YES

N NO

SEND ORDER MESSAGES?: YES// <span class="mark">\<Enter\></span>

#### Re-send Order Messages At Check-In

If the RE-SEND ORDERS AT CHECK-IN parameter is set to YES at the CLINIC, PADE CLINIC GROUP, VISTA CLINIC GROUP, or PADE WILDCARD CLINIC NAME level (or if set to null and the parameter is set to YES at the DIVISION level, or if set to null at all other levels and set to YES at the SYSTEM level), a clinic appointment check-in that triggers a check-in message to be sent will also trigger messages for all active clinic orders associated with the same patient and send area.

If a clinic is defined at more than one level, the hierarchy for determining if order messages should be re-sent for the clinic at check-in is as follows:

1)  CLINIC – Re-sending a patient’s active clinic orders at check-in for the send area associated with the clinic will honor the RE-SEND ORDER AT CHECK-IN parameter set at this level.
2)  PADE CLINIC GROUP – Re-sending a patient’s active clinic orders at check-in for the send area associated with the PADE Clinic Group will honor the RE-SEND ORDER AT CHECK-IN parameter set at this level if the clinic is not also defined at the CLINIC level.
3)  VISTA CLINIC GROUP – Re-sending a patient’s active clinic orders at check-in for the send area associated with the VISTA Clinic Group clinic will honor the RE-SEND ORDER AT CHECK-IN parameter set at this level if a clinic is not also defined at either the CLINIC or PADE CLINIC GROUP levels.
4)  PADE WILDCARD CLINIC NAME – Re-sending a patient’s active clinic orders at check-in for the send area associated with the PADE Wildcard Clinic Name will honor the RE-SEND ORDER AT CHECK-IN parameter set at this level if a clinic is not also defined at any of the CLINIC, PADE CLINIC GROUP, or VISTA CLINIC GROUP levels.

Figure 47: Re-Send Orders at Check-In—Sample User Entries and System Responses

RE-SEND ORDERS AT CHECK-IN: YES// <span class="mark">?</span>

Enter "YES" if medication clinic orders should be resent when a patient

checks into a clinic with the same SEND AREA as the send area for the

orders.

Choose from:

1 YES

0 NO

RE-SEND ORDERS AT CHECK-IN: YES// <span class="mark">??</span>

This parameter allows clinic orders to be resent when a patient checks

into a clinic appointment (either directly or via PADE background job)

sharing the same send area as the orders. This parameter follows the same

hierarchy to determine if clinic orders will be resent, as is used for

the routine sending of PADE order messages. That hierarchy is (1) Clinic

\(2\) PADE Clinic Group (3) VistA Clinic Group (4) PADE Wildcard Clinic

Name and the parameter is available at all of these levels. If set to

YES at this SYSTEM level, any setting of the parameter at these lower

levels (e.g Clinic, PADE Clinic group, VistA Clinic Group, PADE Wildcard

Clinic Name), being left blank or set to YES, will send their associated

Clinic orders messages on check-in. This parameter does not need to be

set to YES or NO for lower level YES or NO values to be honored.

Choose from:

1 YES

0 NO

RE-SEND ORDERS AT CHECK-IN: YES//

#### Send Controlled Substance Orders

When the “SEND CS ORDERS ONLY?:” prompt is set to YES, and the "SEND ORDER MESSAGES?" prompt is also set to YES; then only order messages for medications with a dispense drug having a DEA, SPECIAL HDLG (#3) field of the DRUG (#50) file containing 2, 3, 4, or 5 will transmit to PADE for the wards and clinics defined for this division. Use the SPECIAL HDLG (#3) field if you only use the PADE cabinets of this division to stock controlled substances.

<span id="_Toc103081842" class="anchor"></span>Figure 15: Send Controlled Substance Orders Prompt—Sample User Entries and System Responses

SEND CS ORDERS ONLY?: <span class="mark">??</span>

Choose from:

Y YES

N NO

SEND CS ORDERS ONLY?: <span class="mark">YES</span>

#### Send all Clinic Medication Orders to PADE

At the “SEND MESSAGES FOR ALL CLINICS?: NO//” prompt, enter YES if *all* clinic medication order messages will be sent to PADE. This also includes SIU messages generated by clinic appointment activity/triggers.

When set to YES, *all* clinic messages (orders and SIU) will be sent to PADE for *all* clinics in that division using the *full* clinic name instead of a DEFAULT CLINIC ORDER SEND AREA. This can create a distinct location on the vendor side for each unique clinic name passed.

![](inpatient-medications-pharmacy-interface-automation-pia-startup-and-troubleshoot/008.png) CAUTION: Take caution when choosing to send *all* clinic messages (orders and ADT) from a particular division due to the potentially large volume of messages sent. This is particularly true if you answer YES to this field and leave the DEFAULT CLINIC ORDER SEND AREA field NULL/Blank.  
  
Be sure to work with the vendor to ensure their capabilities prior to setting this field to YES.

Figure 16: Send all Clinic Medication Orders to PADE Prompt—Sample User Entries and System Responses

SEND MESSAGES FOR ALL CLINICS?: NO// <span class="mark">??</span>

Choose from:

Y YES

N NO

SEND MESSAGES FOR ALL CLINICS?: NO// <span class="mark">\<Enter\></span>

#### Select VISTA Clinic Group

You can associate groups of clinics by their membership in the CLINIC GROUP file (#57.8).). It is important to understand that this feature should only be used for sites that do *not* allow one clinic to be in more than one CLINIC GROUP.

In the event that a clinic is defined in *two* clinic groups associated with this file, the message will be sent to the VISTA CLINIC GROUP SEND AREA associated with the first entered CLINIC in the CLINIC GROUP File (#57.8). If this is unacceptable, then that clinic should be defined individually.

<span id="_Toc103081843" class="anchor"></span>Figure 17: Select VISTA Clinic Group Prompt—Sample User Entries and System Responses

Select VISTA CLINIC GROUP: MIKE’S CLINIC GROUP// <span class="mark">\<Enter\></span>

VISTA CLINIC GROUP: MIKE’S CLINIC GROUP// <span class="mark">\<Enter\></span>

VISTA CLINIC GROUP SEND AREA: MIKE’S CLINIC GROUP SA// <span class="mark">??</span>

This is the PADE cabinet location that will be used for this clinic group when sending messages.

Choose from:

AL-SARRTP

EMERGENCY ROOM 1

EMERGENCY ROOM 2

MIKE’S CLINIC GROUP SA

NICU FLOOR 7

OP CLINIC

SURGERY FLOOR 2

VISTA CLINIC GROUP SEND AREA: MIKE’S CLINIC GROUP SA// <span class="mark">\<Enter\></span>

INCLUDE CLINICS IN BG JOB: YES// <span class="mark">??</span>

Choose from:

Y YES

INCLUDE CLINICS IN BG JOB: YES// <span class="mark">\<Enter\></span>

Select VISTA CLINIC GROUP: <span class="mark">\<Enter\></span>

At the “INCLUDE CLINICS IN BG JOB: YES//” prompt, enter YES if the nightly background (BG) job should run for all clinics in this group and generate appointment messages to PADE. Do *not* answer YES to this prompt if check-in is done in these clinics as check-in will generate appointment messages to PADE in real time.

#### Select PADE Clinic Group

The PADE CLINIC GROUP allows you to create a custom grouping of clinics for PADE messages that will all transmit to the same PADE CLINIC GROUP SEND AREA. The benefit of adding clinics to this group, rather than individually, would be that the OP PADE CLINIC GROUP SEND AREA only has to be defined *once* for the group vs. each time if the clinics were added individually.

It also makes the process easier for changing the PADE CLINIC GROUP SEND AREA for an entire group, vs. if they were defined individually.

Figure 18: Select PADE Clinic Group Prompt—Sample User Entries and System Responses

Select PADE CLINIC GROUP: TONY’S PADE CLINIC// <span class="mark">\<Enter\></span>

PADE CLINIC GROUP: TONY’S PADE CLINIC// <span class="mark">\<Enter\></span>

#### Select PADE Clinic

If you want to set up a clinic group just for PADE use only to send messages to a particular PADE location then you can do so here by defining all the clinics and putting them under one group.

If you intend to use the CLINIC GROUP already existing in VistA and there is no overlap of clinics within those clinic groups then you can do so by selecting the VISTA CLINIC GROUP multiple provided as part of the input template.

Figure 19: Select PADE Clinic Prompt—Sample User Entries and System Responses

Select PADE CLINIC: SHERYL'S CLINIC// <span class="mark">??</span>

Choose from:

SHERYL'S CLINIC

REGINA’S CLINIC

Select PADE CLINIC: SHERYL'S CLINIC// <span class="mark">\<Enter\></span>

PADE CLINIC GROUP SEND AREA: EMERGENCY ROOM 1

// <span class="mark">??</span>

This is the PADE cabinet location that will be used to send messages associated with clinics under this group.

Choose from:

AL-SARRTP

EMERGENCY ROOM 1

EMERGENCY ROOM 2

MIKE’S CLINIC GROUP SA

NICU FLOOR 7

OP CLINIC

SURGERY FLOOR 2

PADE CLINIC GROUP SEND AREA: EMERGENCY ROOM 1

// <span class="mark">\<Enter\></span>

INCLUDE CLINICS IN BG JOB: YES// <span class="mark">??</span>

Choose from:

Y YES

INCLUDE CLINICS IN BG JOB: YES// <span class="mark">\<Enter\></span>

Select PADE CLINIC GROUP: <span class="mark">\<Enter\></span>

At the “INCLUDE CLINICS IN BG JOB: YES//” prompt, enter YES if the nightly background (BG) job should run for all clinics in this group and generate appointment messages to PADE. Do *not* answer YES to this prompt if check-in is done in these clinics as check-in will generate appointment messages to PADE in real time.

#### Select PADE Wildcard Clinic Name

The PADE WILDCARD CLINIC NAME allows you to define clinics for PADE that follow a specific naming convention. For example, if all of surgery clinics in a division begin with AL-SURGERY XXXX, then you could define all of them by creating a wildcard called "AL-SURGERY". When an order for a clinic is completed, or a SIU event for that clinic is triggered, the software checks the clinic name against this pattern/wildcard to determine if the message should be sent to PADE.

<span id="_Toc103081844" class="anchor"></span>Figure 20: Select PADE Wildcard Clinic Name Prompt—Sample User Entries and System Responses (1 of 2)

Select PADE WILDCARD CLINIC NAME: ALB-ER// <span class="mark">\<Enter\></span>

PADE WILDCARD CLINIC NAME: ALB-ER// <span class="mark">\<Enter\></span>

PADE WILDCARD CLINIC SEND AREA: <span class="mark">??</span>

This is the PADE cabinet location that will be used to send messages associated with clinics with this naming convention.

Choose from:

ANWERS SEND AREA

AL-SARRTP

EMERGENCY ROOM 1

EMERGENCY ROOM 2

MIKE’S CLINIC GROUP SA

NICU FLOOR 7

OP CLINIC

SURGERY FLOOR 2

PADE WILDCARD CLINIC SEND AREA: <span class="mark">EMERGENCY ROOM 2</span>

INCLUDE CLINICS IN BG JOB: <span class="mark">??</span>

Choose from:

Y YES

INCLUDE CLINICS IN BG JOB: <span class="mark">YES</span>

Select PADE WILDCARD CLINIC NAME: \<Enter\>

At the “INCLUDE CLINICS IN BG JOB:” prompt, enter YES if the nightly background (BG) job should run for these clinics and generate appointment messages to PADE. If you do check-in then do *not* answer YES to this prompt as check-in will also generate appointment messages to PADE.

#### Select CLINIC

The CLINIC field allows you to select clinics that are associated with PADE. When an order for a clinic is completed, or an ADT event for that clinic is triggered, messages will be sent to PADE.

<span id="_Toc103081845" class="anchor"></span>Figure 21: Select CLINIC Prompt—Sample User Entries and System Responses

Select CLINIC: CT SCAN// <span class="mark">??</span>

Choose from:

MIKE'S MEDICAL CLINIC

SHERYL'S CLINIC

REGINA’S CLINIC

Select CLINIC: MIKE'S MEDICAL CLINIC// <span class="mark">\<Enter\></span>

CLINIC: MIKE'S MEDICAL CLINIC// <span class="mark">\<Enter\></span>

CLINIC SEND AREA: NICU FLOOR 7// <span class="mark">??</span>

This is the PADE cabinet location that will be used for this clinic when sending messages.

Choose from:

AL-SARRTP

EMERGENCY ROOM 1

EMERGENCY ROOM 2

MIKE’S CLINIC GROUP SA

NICU FLOOR 7

OP CLINIC

SURGERY FLOOR 2

CLINIC SEND AREA: NICU FLOOR 7// <span class="mark">\<Enter\></span>

INCLUDE CLINIC IN BG JOB: YES// <span class="mark">??</span>

Choose from:

Y YES

INCLUDE CLINIC IN BG JOB: <span class="mark">YES</span>

Select CLINIC: <span class="mark">\<Enter\></span>

At the “INCLUDE CLINIC IN BG JOB:” prompt, enter YES if the nightly background (BG) job should run for this clinic and generate appointment messages to PADE. Do *not* answer YES to this prompt if check-in is done in this clinic as check-in will generate appointment messages to PADE in real time.

#### Send INPT IV Package Orders

At the “SEND INPT IV PACKAGE ORDERS?: YES//” prompt, enter YES if all IV package orders associated with wards of this division will send messages to PADE.

Figure 22: Send INPT IV Package Orders Prompt—Sample User Entries and System Responses

SEND INPT IV PACKAGE ORDERS?: YES// <span class="mark">??</span>

Choose from:

Y YES

N NO

SEND INPT IV PACKAGE ORDERS?: YES// <span class="mark">\<Enter\></span>

#### Select Ward Group

You can use ward groups to associate all the wards within a "P" type ward group to this Division instead of defining them individually. If you also define a WARD individually, which is part of a ward group defined within this field, then the WARD GROUP SEND AREA in this multiple will be ignored for that ward and the send location of the individually defined ward will be used to send messages. This allows you to define behavior for an entire ward group but create exceptions for specific wards that are part of that group.

Figure 23: Select Ward Group Prompt—Sample User Entries and System Responses

Choose from:

10C SARRTP-AL

Select WARD GROUP: 10C SARRTP-AL// <span class="mark">\<Enter\></span>

WARD GROUP: 10C SARRTP-AL// <span class="mark">\<Enter\></span>

WARD GROUP SEND AREA: AL-SARRTP// <span class="mark">??</span>

All the messages associated to the wards under this ward group

will be sent to the PADE location defined here.

Choose from:

ANWERS SEND AREA

AL-SARRTP

EMERGENCY ROOM 1

EMERGENCY ROOM 2

MIKE’S CLINIC GROUP SA

NICU FLOOR 7

OP CLINIC

SURGERY FLOOR 2

WARD GROUP SEND AREA: AL-SARRTP// <span class="mark">\<Enter\></span>

WARD GROUP SEND AREA: <span class="mark">??</span>

All the messages associated to the wards under this ward group will

be sent to the PADE location defined here.

Choose from:

ANWERS SEND AREA

EMERGENCY ROOM 1

EMERGENCY ROOM 2

Select WARD GROUP: <span class="mark">\<Enter\></span>

#### Create a New PADE Bed Group

The PADE BED GROUP NAME is an arbitrary name of your choosing that will be used to group beds for which the messages for patients in those beds will be sent to a specific send location.

You should only define this for wards that have multiple PADE cabinets (i.e., two "wings"); where the bed designations can indicate which PADE cabinet will support the patients in that groups of beds. If both cabinets will support all patients on the ward, then the ward only need be defined and *not* specific groups of beds.

<span id="_Toc103081846" class="anchor"></span>Figure 245: Create a New PADE Bed Group—Sample User Entries and System Responses (1 of 2)

Select PADE BED GROUP NAME: PDBG1// <span class="mark">\<Enter\></span>

PADE BED GROUP NAME: PDBG1// <span class="mark">\<Enter\></span>

Select PADE INDIVIDUAL BED: AS-9// <span class="mark">??</span>

Choose from:

A-2

AS-1

AS-9

Select PADE INDIVIDUAL BED: AS-9// <span class="mark">\<Enter\></span>

PADE BED GROUP SEND AREA: SURGERY FLOOR 2//

The PADE BEDS contains the room-beds belonging to this group. Grouping the beds is helpful if there are more than one PADE cabinets supporting a ward. Defining the related send area with the accurate group of beds will help send HL7 messages to the PADE BED GROUP SEND AREA.

Figure 25: Create a New PADE Bed Group—Sample User Entries and System Responses (2 of 2)

PADE BED GROUP SEND AREA: SURGERY FLOOR 2// <span class="mark">??</span>

This is the PADE cabinet location that will be used for this bed group when sending messages.

Choose from:

ANWERS SEND AREA

AL-SARRTP

EMERGENCY ROOM 1

EMERGENCY ROOM 2

MIKE’S CLINIC GROUP SA

NICU FLOOR 7

OP CLINIC

SURGERY FLOOR 2

PADE BED GROUP SEND AREA: SURGERY FLOOR 2// <span class="mark">\<Enter\></span>

Select PADE BED GROUP NAME: <span class="mark">\<Enter\></span>

#### Select Ward

The WARD prompt allows you to select wards that are associated with PADE. When an order for an inpatient is completed, or an ADT event for that Ward is triggered, messages will be sent to PADE.

Figure 26: Select Ward Prompt—Sample User Entries and System Responses

Select WARD: UNIT 1// <span class="mark">??</span>

Choose from:

5 West Psych

MIKE'S IP WARD

UNIT 1

Select WARD: UNIT 1// <span class="mark">\<Enter\></span>

WARD SEND AREA: EMERGENCY ROOM 1// <span class="mark">??</span>

This is the PADE cabinet location that will be used for this ward when sending messages.

Choose from:

ANWERS SEND AREA

EMERGENCY ROOM 1

EMERGENCY ROOM 2

#### Select Operating Room

You have the option to enter a new OPERATING ROOM. If you have set the "SEND SURGERY MESSAGES?” prompt to YES for this division, you *must* also define the operating rooms whose scheduled cases should generate surgery messages to PADE.

Figure 27: Select Operating Room Prompt—Sample User Entries and System Responses

Select OPERATING ROOM: GENERAL SURGERY// <span class="mark">??</span>

Choose from:

GENERAL SURGERY

Select OPERATING ROOM: GENERAL SURGERY// <span class="mark">\<Enter\></span>

OPERATING ROOM: GENERAL SURGERY// <span class="mark">\<Enter\></span>

OPERATING ROOM SEND AREA: SURGERY FLOOR 2// <span class="mark">??</span>

Choose a send location for the surgery messages that will generate for surgical cases scheduled for this operating room. If you leave this field blank, the operating room name will be used as the location for the message.

Choose from:

ANWERS SEND AREA

AL-SARRTP

EMERGENCY ROOM 1

EMERGENCY ROOM 2

MIKE’S CLINIC GROUP SA

NICU FLOOR 7

OP CLINIC

SURGERY FLOOR 2

OPERATING ROOM SEND AREA: SURGERY FLOOR 2// <span class="mark">\<Enter\></span>

Select OPERATING ROOM: <span class="mark">\<Enter\></span>

Select DIVISION: <span class="mark">\<Enter\></span>

Select PADE SYSTEM SETUP:

## PADE Send Surgery Cases

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the PADE Send Surgery Cases \[PSJ PADE SEND SURGERY CASES\] option to send surgery cases manually to PADE for that date or future date.

Figure 28: PADE Send Surgery Cases Option—Sample User Entries and System Responses

SA PADE Send Area Setup

SS PADE System Setup

IN PADE Inventory Setup ...

RP PADE Reports ...

<span class="mark">SC PADE Send Surgery Cases</span>

SO PADE Send Patient Orders

Select PADE Main Menu \<TEST ACCOUNT\> Option: <span class="mark">SC \<Enter\></span> PADE Send Surgery Cases

Enter date of Surgery cases to send to PADE: T// <span class="mark">\<Enter\></span> (JUN 17, 2016)

Do you want to continue? NO// <span class="mark">YES</span>

Requested Start Time: NOW// <span class="mark">\<Enter\></span> (JUN 17, 2016@10:19:57)

Task Queued !

## PADE Send Patient Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the PADE Send Patient Orders \[PSJ PADE SEND ORDERS\] option to send patient UD/IV orders to PADE, especially when initializing PADE with initial load of all the orders, so that the patients can be established along with their orders.

Figure 29: PADE Send Patient Orders Option—Sample User Entries and System Responses

SA PADE Send Area Setup

SS PADE System Setup

IN PADE Inventory Setup ...

RP PADE Reports ...

SC PADE Send Surgery Cases

<span class="mark">SO PADE Send Patient Orders</span>

Select PADE Main Menu \<TEST ACCOUNT\> Option: <span class="mark">SO \<Enter\></span> PADE Send Patient Orders

Select By: (PT/WD/CL/E): PT// <span class="mark">?</span>

Enter 'PT' to send orders by Patient

'WD' to send orders by Ward

'CL' to send orders by Clinic

or 'E' or '^' to exit

Select one of the following:

PT PATIENT

WD WARD

CL CLINIC

E EXIT

Select By: (PT/WD/CL/E): PT// <span class="mark">\<Enter\></span> PATIENT

Select PATIENT: ANTPATNM,A,A <span class="mark">\<Enter\></span> ANTPATNM,A 666-00-0099 04/10/08 3 NORTH GU

1 Order(s) Queued for ANTPATNM,A (0099)

Select By: (PT/WD/CL/E): PT// <span class="mark">WD \<Enter\></span> WARD

Select PADE: <span class="mark">PYXIS</span>

You are logged under PADE: PYXIS

Select DIVISION: <span class="mark">TROY \<Enter\></span> 888

You are logged under Division: TROY

Select a Ward or ^ALL for all Wards: <span class="mark">?</span>

Answer with WARD LOCATION NAME, or SERVICE, or \*NSERV, or SYNONYM

Do you want the entire WARD LOCATION List? N (No)

Select a Ward or ^ALL for all Wards:

Select a Ward or ^ALL for all Wards: <span class="mark">^ALL</span>

Sending ward 3 NORTH SURG

No patients with active orders for this ward

Sending ward 3 NORTH GU

1 Order(s) Queued for ANTPATNM,A (0099)

Sending ward ICU/CCU

No patients with active orders for this ward

No patient in WARD REHAB

No patient in WARD DSS OBSERVATION

Select By: (PT/WD/CL/E): WD// <span class="mark">CLINIC</span>

You are logged under PADE: PYXIS

Select DIVISION: <span class="mark">TROY \<Enter\></span> 888

Select a Clinic or ^ALL for all Clinics:

CECELIA'S CLINIC TROY PSJPROVIDER,ONE T

Orders Queued to be sent to PADE

Select a Clinic or ^ALL for all Clinics: <span class="mark">MIKE</span>

S MENTAL CLINIC TROY PSJPROVIDERY,ONE T

Clinic is not setup for this PADE.

Select a Clinic or ^ALL for all Clinics: <span class="mark">^</span>

Select By: (PT/WD/CL/E): CL//

## Nightly Job

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two options for nightly jobs:

1.  PADE Appointment Task \[PSJ PADE APPOINTMENT TASK\]

Use this option to schedule a nightly job to generate HL7 messages of the appointments for that day to send to a PADE. If the DAYS TO PULL AHEAD FOR BG JOB field (#3.6) in the PADE SYSTEM SETUP (#58.7) file have a value, the appointments for those days will be included in the messages.

7.  PADE Surgery Task \[PSJ PADE SURGERY TASK\]

Use this option to schedule a nightly job to generate HL7 messages of surgery cases for that day to be sent to PADE.

# Phase 3: Inbound to VistA Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Phase 3 Roles:

The following roles are involved with Phase 3: Inbound to VistA Setup:

- Pharmacy Staff (ADPAC)
- Vendor Engineer or Implementation Support
- Clinical Product Support

<table>
<caption><p><span id="_Ref507777522" class="anchor"></span>Table 5: PADE Inventory System Setup Fields</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 43%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th>Phase 3:</th>
<th>Inbound to VistA Task</th>
<th>POC</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>☐</td>
<td><ol type="1">
<li><p><a href="#hl7-multi-listener">HL7 Multi-Listener</a></p></li>
</ol></td>
<td></td>
</tr>
<tr class="even">
<td>☐</td>
<td><ol start="2" type="1">
<li><p>(IN) <a href="#pade-inbound-setup-capture">PADE Inventory Setup (Inbound)</a></p></li>
</ol></td>
<td>Pharmacy</td>
</tr>
<tr class="odd">
<td>☐</td>
<td><ol start="3" type="1">
<li><p><a href="#pade-inventory-error-messages">PADE Inventory Error Messages</a></p></li>
</ol></td>
<td></td>
</tr>
<tr class="even">
<td>☐</td>
<td><ol start="4" type="1">
<li><p><a href="#dispensed-without-orders-dwo-messages">Dispensed Without Orders (DWO) Messages</a></p></li>
</ol></td>
<td></td>
</tr>
<tr class="odd">
<td>☐</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>☐</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>☐</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>☐</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Ref507777522" class="anchor"></span>Table 5: PADE Inventory System Setup Fields

## HL7 Multi-Listener

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PADE uses the VA Standard VistA HL7 multi-listener of port 5000 for production systems for all inbound HL7 messages from Health Connect. For *non*-production accounts/*non*-VA Sites, IP address/port numbers are needed by Health Connect for processing of inbound messaging to VistA.

Contact your System Administrator for details on your sites VistA HL7 multi-listener configuration and status.

## PADE Inbound Setup Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PADE Inventory System requires configuration at the PADE system level, and at the PADE dispensing device (or cabinet) level. There are many system and cabinet parameters available that allow PADE inventory functionality to be adjusted to meet the needs of the facility; however, there are three setup items that *must* be completed to enable the core PADE Inventory functionality:

1.  PADE Inbound System:

This step *must* be done first, and it *must* be done *before* any incoming PADE HL7 messages can be filed. In order to file incoming PADE pocket activity transactions in the PADE INBOUND TRANSACTIONS (#58.6) file, the PADE Inventory System *must* be defined in the PADE INVENTORY SYSTEM (#58.601) file via the PADE Inventory System Setup \[PSJ PADE INVENTORY SYSTEM\] option.

1.  The PADE Inventory System name *must* exactly match the value of the Dispensing System field (ZPM-2) received in the incoming HL7 message.
6.  PADE dispensing devices (cabinets) are automatically filed into the PADE DISPENSING DEVICE (#58.63) file as they are received via HL7 messaging. Therefore, the suggested approach to initially populating the PADE DISPENSING DEVICE (#58.63) file with the new PADE dispensing devices is to define the PADE INVENTORY SYSTEM (#58.601) file, then trigger an ”inventory”, or “count” message from each PADE dispensing device.

The above actions will automatically file all PADE dispensing devices in VistA. If the dispensing devices are added manually, an incorrect device name may be inadvertently entered.

7.  As each transaction is filed into the PADE INBOUND TRANSACTIONS (#58.6) file, the total balance for each PADE dispensing device/cabinet is updated in the PADE INVENTORY SYSTEM (#58.601) file.
8.  Dispensing Device Division:

In order to access the incoming PADE transaction and PADE inventory information via PADE reports, each PADE dispensing device (cabinet) *must* be associated with a division via the PADE Dispensing Device Setup \[PSJ PADE DEVICE SETUP\] option.

9.  Dispensing Device Dispense Location:

In order for PADE drug balance information to display in the Inpatient Order Entry \[option name?\] option, each PADE dispensing device (cabinet) *must* be associated with one (or more) of the following:

- Ward Location
- Ward Group
- Clinic Location
- Clinic Group
- Wildcard Clinic Name

Figure 30: Example: Define a PADE Inventory System—Sample User Entries and System Responses

Select OPTION NAME: <span class="mark">PSJ PADE MAIN MENU \<Enter\></span> PADE Main Menu

SA PADE Send Area Setup

SS PADE System Setup

<span class="mark">IN PADE Inventory Setup ...</span>

RP PADE Reports ...

SC PADE Send Surgery Cases

SO PADE Send Patient Orders

Select PADE Main Menu \<TEST ACCOUNT\> Option: <span class="mark">IN \<Enter\></span> PADE Inventory Setup

DEV PADE Dispensing Device Setup

<span class="mark">SYS PADE Inventory System Setup</span>

Select PADE Inventory Setup \<TEST ACCOUNT\> Option: <span class="mark">SYS \<Enter\></span> PADE Inventory System Setup

Select PADE INVENTORY SYSTEM: <span class="mark">TESTSYS</span>

Are you adding 'TESTSYS' as a new PADE INVENTORY SYSTEM (the 6TH)? No// <span class="mark">Y \<Enter\></span> (Yes)

PADE INVENTORY SYSTEM: TESTSYS//

Figure 31: Example: Define a PADE Dispensing Device/Cabinet—Sample User Entries and System Responses

Select OPTION NAME: <span class="mark">PSJ PADE MAIN MENU \<Enter\></span> PADE Main Menu

SA PADE Send Area Setup

SS PADE System Setup

<span class="mark">IN PADE Inventory Setup ...</span>

RP PADE Reports ...

SC PADE Send Surgery Cases

SO PADE Send Patient Orders

Select PADE Main Menu \<TEST ACCOUNT\> Option: <span class="mark">IN \<Enter\></span> PADE Inventory Setup

<span class="mark">DEV PADE Dispensing Device Setup</span>

SYS PADE Inventory System Setup

Select PADE Inventory Setup \<TEST ACCOUNT\> Option: <span class="mark">DEV \<Enter\></span> PADE Dispensing Device Setup

Select PADE DISPENSING DEVICE: <span class="mark">PV_1 \<Enter\></span> TESTSYS ACTIVE

...OK? Yes// <span class="mark">\<Enter\></span> (Yes)

DIVISION: // <span class="mark">XXXXX \<Enter\></span> 500A4

Select WARD GROUP: // <span class="mark">TESTWG</span>

Select WARD LOCATION: GENERAL SURGERY// <span class="mark">\<Enter\></span>

Select CLINIC GROUP: // <span class="mark">TESTCG</span>

Select CLINIC LOCATION: // <span class="mark">AMB CLINIC</span>

Select WILDCARD CLINIC NAME: // <span class="mark">DIABETES</span>

## PADE Inventory System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PADE INVENTORY SYSTEM is the name of the Pharmacy Automated Dispensing Equipment (PADE) system that sends PADE activity to VistA. This *must* be the same as the Sending Application in the message header (ZPM.2) of the HL7 messages received from the PADE vendor interface.

### DWO Message Entity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Dispensed Without Order (DWO) Entities link Pharmacy Automated Dispensing Equipment (PADE) to mail groups that will receive a message when a medication is dispensed from PADE with no VistA Pharmacy order. DWO entities, in order from highest to lowest priority, are:

1.  PADE DEVICE (CABINET)
10. WARD/CLINIC
11. WARD GROUP/CLINIC GROUP
12. PADE SYSTEM/DIVISION

Messages are *only* sent for entities defined with the highest priority. For example, if a ward, clinic, and ward group are all linked to a PADE device, and all contain DWO mail groups, only mail group(s) associated with the ward and clinic receive a DWO message, since they both have the same priority (2), and it is higher than the ward group priority (3).

![](inpatient-medications-pharmacy-interface-automation-pia-startup-and-troubleshoot/009.png) NOTE: For more details, see Section <u>4.6</u>, “<u>Dispensed Without Orders (DWO) Messages</u>.”

Figure 32: DWO Message Entity Help Text

Enter one of the following:

DIV.EntryName to select a DIVISION for DWO messages.

PS.EntryName to select a PADE SYSTEM for DWO messages.

WG.EntryName to select a WARD GROUP for DWO messages.

WD.EntryName to select a WARD for DWO messages.

CL.EntryName to select a CLINIC for DWO messages.

CG.EntryName to select a CLINIC GROUP for DWO messages.

PC.EntryName to select a PADE DEVICE for DWO messages.

To see the entries in any particular file type \<Prefix.?\>

If you simply enter a name then the system will search each of

the above files for the name you have entered. If a match is

found the system will ask you if it is the entry that you desire.

However, if you know the file the entry should be in, then you can

speed processing by using the following syntax to select an entry:

\<Prefix\>.\<entry name\>

or

\<Message\>.\<entry name\>

or

\<File Name\>.\<entry name\>

Also, you do NOT need to enter the entire file name or message

to direct the look up. Using the first few characters will suffice.

Select DWO MESSAGE ENTITY:

### DWO Entity Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Dispensed Without Order (DWO) Entity Mail Groups receive a message when a medication is dispensed from PADE with no VistA Pharmacy order, for the DWO entity associated with the mail group. Messages are only sent for cabinets that also have the SEND DWO MESSAGES prompt in the PADE Dispensing Device Setup \[PSJ PADE DEVICE SETUP\] option set to YES.

### Config Errors Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Config Errors Mail Groups receive PADE Configuration error messages when PADE configuration problems are encountered by the PADE HL7 inbound interface processor. Examples of PADE inbound configuration errors are when a PADE HL7 message is received for an undefined inbound PADE system, or when a PADE HL7 message is received for a PADE cabinet that is *not* associated with a VistA division.

### Data Errors Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data Errors Mail Groups receive PADE Data validation error messages when data validation problems are encountered by the PADE HL7 inbound interface processor. Examples of PADE inbound data validation errors are missing or invalid patient, drug, or other required data.

### Alternate System Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Alternate System Name is an alternate name or alias name used to identify the PADE Inventory System name during lookups.

### Display PADE Balances in IOE?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Display PADE Balances in IOE? field is used by the Inpatient Order Entry \[PSJ OE\] option to determine if PADE information should be displayed in the following lookups:

- Inpatient Profile
- Inpatient Order (detailed) View
- Dispense Drug

The field sets the PSJ PADE OE BALANCES Kernel parameter.

## Set Up PADE Dispensing Device (Cabinet)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PADE dispensing devices (cabinets) *must* be configured prior to first use.

The PADE dispensing devices are set up using the PADE Dispensing Device Setup \[PSJ PADE INVENTORY SYSTEM\] option, which is available via the following menus:

Figure 33: PADE Dispensing Device Setup Option \[PSJ PADE INVENTORY SYSTEM\]—Menu Location

PADE Main Menu \[PSJ PADE MAIN MENU\]

PADE Inventory Setup \[PSJ PADE INVENTORY MENU\]

PADE Dispensing Device Setup \[PSJ PADE DEVICE SETUP\]

The specific fields in the PADE Inbound System set up are listed in <u>Table 5</u>.

<table>
<caption><p><span id="_Ref508190508" class="anchor"></span>Table 6: Phase 4: Implementation Tasks</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><ol type="1">
<li><p><strong>DISPENSING DEVICE</strong></p></li>
<li><p><strong>PADE STATUS</strong></p></li>
<li><p><strong>RESET/INITIALIZE PADE DEVICE?</strong></p></li>
<li><p><strong><mark>DELETE SINGLE DRUG FROM PADE CABINET?</mark></strong></p></li>
<li><p><strong>DIVISION</strong></p></li>
<li><p><strong>WARD GROUP</strong></p></li>
<li><p><strong>WARD LOCATION</strong></p></li>
<li><p><strong>CLINIC GROUP</strong></p></li>
<li><p><strong>CLINIC LOCATION</strong></p></li>
<li><p><strong>WILDCARD CLINIC NAME</strong></p></li>
<li><p><strong><mark>SEND 'PATIENT NOT ON FILE' MSG</mark></strong></p></li>
<li><p><strong>SEND DWO MESSAGES</strong></p></li>
<li><p><strong>DWO ENTITY</strong></p></li>
<li><p><strong>DWO ENTITY MAIL GROUP</strong></p></li>
</ol></td>
</tr>
</tbody>
</table>

<span id="_Ref508190508" class="anchor"></span>Table 6: Phase 4: Implementation Tasks

### Dispensing Device

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DISPENSING DEVICE field contains the name of the PADE dispensing device/cabinet. The name *must* exactly match the name of the device on the PADE vendor system, as it appears in the HL7 messages received by the PADE inbound interface. The DISPENSING DEVICE name *must* only be unique within the specific PADE Inbound system; while it is advisable to avoid duplicate device/cabinet names across different vendor systems to avoid confusion. The PADE inbound configuration allows the same dispensing device name to be used by different PADE inbound inventory systems.

### PADE Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PADE STATUS field allows a PADE dispensing device's status to be set to ACTIVE or INACTIVE. Setting the status to INACTIVE does *not* affect the PADE's medication balances; however, an INACTIVE status prevents the PADE cabinet's medication balances from being displayed as available in the Inpatient Order Entry \[option name?\] option. Inactive PADE cabinets will continue to display in all PADE reports.

If a PADE cabinet is being removed from service, the list of medications stocked in a cabinet may be deleted using the RESET/INITIALIZE PADE DEVICE? field.

### Reset/Initialize PADE Device?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RESET/INITIALIZE PADE DEVICE? field removes all medications linked to this PADE cabinet in VistA, making the cabinet appear empty to VistA users. Resetting a PADE cabinet does *not* affect the PADE vendor, and does *not* trigger any HL7 messages to the PADE system. Resetting a PADE cabinet makes the device unavailable for selection when running the PADE INVENTORY REPORT, and also removes the device from the list PADE cabinets used to display PADE information in the Inpatient Order Entry \[PSJ OE \] option.

After a PADE cabinet is reset, medications will be automatically added back to the PADE cabinet as new HL7 messages are received from the vendor.

### Delete Single Drug from PADE Cabinet?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Delete Single Drug from PADE Cabinet removes one drug item from a specific pocket from the PADE dispensing device in VistA. This does *not* affect the PADE vendor, and does *not* trigger any HL7 messages to be sent to the PADE vendor system. Manually deleting a drug item reduces the quantity of the drug that displays as available in VistA when running the PADE INVENTORY REPORT, and also removes the drug from balances displayed in the Inpatient Order Entry \[PSJ OE\]option.

After a drug is deleted, the drug can be added back to the cabinet's inventory as new HL7 messages are received from the vendor.

### Division

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DIVISION field contains the primary division associated with the PADE dispensing device/cabinet. The PADE cabinet supplies medications to hospital locations associated with this division, and division is required for inventory and reporting purposes. PADE activity received via HL7 messages will be filed into the PADE INBOUND TRANSACTIONS (#58.6) file if the PADE dispensing device/cabinet is *not* associated with a division; however, the transaction will *not* display in the Transaction Report, nor update the Inventory Report, until it is associated with a division.

### Ward Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The WARD GROUP field contains ward groups associated with the PADE dispensing device/cabinet. The PADE cabinet supplies medications to ward locations associated with this ward group. A PADE cabinet can be associated with any combination of ward groups, ward locations, clinic groups, and clinic locations, provided each location is associated with the PADE cabinet’s division.

### Ward Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The WARD LOCATION field contains ward locations associated with the PADE dispensing device/cabinet. The PADE cabinet supplies medications to these ward locations. A PADE cabinet may be associated with any combination of ward groups, ward locations, clinic groups, and clinic locations, provided each location is associated with the PADE cabinet’s division.

### Clinic Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CLINIC GROUP field contains clinic groups associated with the PADE dispensing device/cabinet. The PADE cabinet supplies medications to clinic locations associated with this clinic group. A PADE cabinet can be associated with any combination of ward groups, ward locations, clinic groups, and clinic locations, provided each location is associated with the PADE cabinet’s division.

### Clinic Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CLINIC LOCATION field contains clinic locations associated with the PADE dispensing device/cabinet. The PADE cabinet supplies medications to these clinic locations. A PADE cabinet can be associated with any combination of ward groups, ward locations, clinic groups, and clinic locations, provided each location is associated with the PADE cabinet’s division.

### Wildcard Clinic Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The WILDCARD CLINIC NAME contains a text string, representing a partial clinic location name, that allows a group of Clinics with a common naming convention, or “wildcard”, to be linked to a PADE cabinet, automatically linking all matching clinic location names with the PADE cabinet. The PADE cabinet supplies medications to matching clinic location names.

For example, if all of a division's surgery clinics began with “AL-SURGERY”, all the surgery clinics could be linked to a PADE cabinet by creating a wildcard called "AL-SURGERY".

### Send 'PATIENT NOT ON FILE' Msg

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SEND 'PATIENT NOT ON FILE' MSG field contains a flag indicating whether or not an error message should be generated by the inbound PADE HL7 interface when a patient ID received from PADE does *not* exist in VistA.

### Send DWO Messages?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SEND DWO MESSAGES? field contains a flag indicating if Dispensed Without Order (DWO) MailMan messages should be sent when this PADE device is involved in a dispense transaction that is *not* linked to a pharmacy order.

This field *must* be set to YES in order for the PADE cabinet to generate a DWO message; however, a DWO Entity and a DWO Entity Mail Group *must* also be defined for the DWO message to be routed to members of a mail group.

### DWO Entity Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DWO ENTITY MAIL GROUP field contains mail groups that receive Dispensed Without Orders (DWO) MailMan messages when a PADE dispense transaction is received without a corresponding pharmacy order.

When setting up a PADE dispensing device/cabinet, the DWO Entity is always the PADE cabinet; multiple mail groups can be entered, and the DWO message will be sent to all members of all mail groups defined.

## PADE Inventory Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA PADE Inventory interface receives HL7 messages when there is activity at the dispensing device (cabinet). Examples of dispensing device activity that generates an HL7 messages are loading, unloading, and dispensing drug items. When a PADE HL7 message is received that contains missing or invalid data, an error message may be sent if the VistA PADE System has been configured to send error messages.

There are two types of PADE Inventory error messages, CONFIGURATION and DATA error messages.

- CONFIGURATION error messages—This type of error indicates there is a problem with the configuration of the PADE Inventory interface. The two specific errors that are classified as CONFIGURATION errors are:
  - Missing or Invalid Required HL7 Segment(s)
  - Missing or Unknown PADE Inventory System
- DATA error messages—This type of error indicates there is a problem with the validation of the data received from the PADE vendor system. The following errors are classified as DATA errors:
  - Missing or Invalid USER ID
  - Missing or Invalid Transaction Date/Time
  - Missing or Invalid Transaction Type
  - Patient Not on File (optional-controlled by parameter)
  - FileMan Error – Transaction not Filed
  - Drug Not on File
  - Outdated Transaction

Mail groups can be defined separately for Configuration and Data errors using the PADE Dispensing Device Setup \[PSJ PADE DEVICE SETUP\] option. Configuration error messages are sent to mail groups defined at the CONFIG ERRORS MAIL GROUPS parameter, and Data error messages are sent to mail groups defined at the DATA ERRORS MAIL GROUPS parameter. Multiple mail groups can be defined for each type of error. If an error occurs and *no* mail recipients are defined, the interface checks for holders of the PSJ PADE MGR security key, and forwards the error message to all holders of that key.

To set up mail groups to receive Configuration errors, enter one or mail groups at the “Select CONFIG ERRORS MAIL GROUPS:” prompt using the PADE Inventory System Setup \[PSJ INVENTORY SYSTEM\] option:

<span id="_Toc103081847" class="anchor"></span>Figure 34: PADE Inventory Setup Option: Setting up Mail Groups for CONFIGURATION Errors—Sample User Entries and System Responses

Select OPTION NAME: <span class="mark">PSJ PADE MAIN MENU \<Enter\></span> PADE Main Menu

SA PADE Send Area Setup

SS PADE System Setup

<span class="mark">IN PADE Inventory Setup ...</span>

RP PADE Reports ...

SC PADE Send Surgery Cases

SO PADE Send Patient Orders

Select PADE Main Menu \<TEST ACCOUNT\> Option: <span class="mark">IN \<Enter\></span> PADE Inventory Setup

DEV PADE Dispensing Device Setup

SYS PADE Inventory System Setup

Select PADE Inventory Setup \<TEST ACCOUNT\> Option: <span class="mark">SYS \<Enter\></span> PADE Inventory System Setup

Select PADE INVENTORY SYSTEM: <span class="mark">TESTSYS</span>

PADE INVENTORY SYSTEM: TESTSYS// <span class="mark">^CONFIG ERRORS MAIL GROUP</span>

Select CONFIG ERRORS MAIL GROUPS: <span class="mark">MAILGROUP1</span>

Are you adding 'MAILGROUP1' as

a new CONFIG ERRORS MAIL GROUP (the 1ST for this PADE INVENTORY SYSTEM)? No// <span class="mark">Y \<Enter\></span> Yes)

Select CONFIG ERRORS MAIL GROUPS:

To set up mail groups to receive Data errors, enter one or mail groups at the “Select DATA ERRORS MAIL GROUPS:” prompt using the PADE Inventory System Setup \[PSJ INVENTORY SYSTEM\] option:

Figure 35: PADE Inventory Setup: Setting up Mail Groups for DATA Errors —Sample User Entries and System Responses

Select OPTION NAME: <span class="mark">PSJ PADE MAIN MENU \<Enter\></span> PADE Main Menu

SA PADE Send Area Setup

SS PADE System Setup

<span class="mark">IN PADE Inventory Setup ...</span>

RP PADE Reports ...

SC PADE Send Surgery Cases

SO PADE Send Patient Orders

Select PADE Main Menu \<TEST ACCOUNT\> Option: <span class="mark">IN \<Enter\></span> PADE Inventory Setup

DEV PADE Dispensing Device Setup

SYS PADE Inventory System Setup

Select PADE Inventory Setup \<TEST ACCOUNT\> Option: <span class="mark">SYS \<Enter\></span> PADE Inventory System Setup

Select PADE INVENTORY SYSTEM: <span class="mark">TESTSYS</span>

PADE INVENTORY SYSTEM: TESTSYS// ^DATA ERRORS MAIL GROUP

Select DATA ERRORS MAIL GROUPS: <span class="mark">MAILGROUP2</span>

Are you adding 'MAILGROUP2' as

a new DATA ERRORS MAIL GROUP (the 1ST for this PADE INVENTORY SYSTEM)? No// <span class="mark">Y \<Enter\></span> (Yes)

Select DATA ERRORS MAIL GROUPS:

Patient Not on File parameter

The PATIENT NOT ON FILE error message, indicating a patient ID is *not* recognized, will *not* be sent unless the PADE dispensing device involved in the incoming PADE activity has been configured in VistA to send PATIENT NOT ON FILE errors. The SEND ‘PATIENT NOT ON FILE’ MSG parameter controlling this error message can be set using the PADE DISPENSING DEVICE SETUP \[PSJ PADE DEVICE SETUP\] option. If *not* set, the parameter is interpreted as NO, and PATIENT NOT ON FILE error messages will *not* be sent.

To send PATIENT NOT ON FILE error messages, set the “SEND ‘PATIENT NOT ON FILE’ MSG” prompt to YES using the PADE Dispensing Device Setup \[PSJ PADE DEVICE SETUP\] option.

Figure 36: PADE Inventory Setup Option: Setting up SEND ‘PATIENT NOT ON FILE’ MSG Parameter—Sample User Entries and System Responses

Select OPTION NAME: <span class="mark">PSJ PADE MAIN MENU \<Enter\></span> PADE Main Menu

SA PADE Send Area Setup

SS PADE System Setup

<span class="mark">IN PADE Inventory Setup ...</span>

RP PADE Reports ...

SC PADE Send Surgery Cases

SO PADE Send Patient Orders

Select PADE Main Menu \<TEST ACCOUNT\> Option: <span class="mark">IN \<Enter\></span> PADE Inventory Setup

<span class="mark">DEV PADE Dispensing Device Setup</span>

SYS PADE Inventory System Setup

Select PADE Inventory Setup \<TEST ACCOUNT\> Option: <span class="mark">DEV \<Enter\></span> PADE Dispensing Device Setup

Select PADE DISPENSING DEVICE: <span class="mark">TESTSTN \<Enter\></span> console

...OK? Yes// <span class="mark">\<Enter\></span> (Yes)

PADE STATUS: <span class="mark">^SEND 'PATIENT NOT ON FILE' MSG</span>

SEND 'PATIENT NOT ON FILE' MSG: <span class="mark">Y \<Enter\></span> YES

Figure 37: Example: Missing Required HL7 Segment Message

Subj: PADE Error-Msg:482146 \[#181575\] 06/16/16@14:04 6 lines

From: PADE In 'IN' basket. Page 1 \*New\*

--------------------------------------------------------------------------

An error was encountered while processing a message from PADE

Date: Jun 16, 2016 14:04:39

Patient: PIAPATIENT, ELEVEN^768

Error Msg: Missing RQD segment. \|CABINET=RDO-01\|SYSTEM=TESTSYSO

Header: MSH\|~^\\\|PSJ PADE SERVER\|500~FO-XXXXX.MED.VA.GOV~DNS\|PSJ VISTA\|\~~D

NS\|20160616140433-0400\|\|OMS~O05~OMS_O05\|500444576\|P\|2.5\|\|\|AL\|NE\|USA

Enter message action (in IN basket): Ignore//

![](inpatient-medications-pharmacy-interface-automation-pia-startup-and-troubleshoot/010.png) NOTE: For missing required HL7 segment, check with the PADE vendor and provide the information (e.g., date, patient, error msg, and header) as shown in the error message.

Figure 38: Example: Missing or Invalid Data Message

Subj: PADE Error-Msg:482152 \[#181576\] 06/16/16@14:34 5 lines

From: PADE In 'IN' basket. Page 1 \*New\*

--------------------------------------------------------------------------

An error was encountered while processing a message from PADE

Date: Apr 11, 2016 12:58:49

Error Msg: TRANS CODE -ZPM.1 is null or invalid\|CABINET= RDO-01\|SYSTEM=TESTSYSO

Header: MSH\|~^\\\|PSJ PADE SERVER\|500~FO-XXXXX.MED.VA.GOV~DNS\|PSJ VISTA\|\~~D

NS\|20160616143429-0400\|\|OMS~O05~OMS_O05\|500444582\|P\|2.5\|\|\|AL\|NE\|USA

Enter message action (in IN basket): Ignore//

![](inpatient-medications-pharmacy-interface-automation-pia-startup-and-troubleshoot/011.png) NOTE: For missing or invalid data, check with the PADE vendor and provide the information (e.g., date, error msg, and header) as shown in the error message.

Figure 39: Example: VA FileMan Error Attempting to File Incoming Transaction Message

Subj: PADE Error-Msg:482154 \[#181577\] 06/16/16@14:47 5 lines

From: PADE In 'IN' basket. Page 1 \*New\*

--------------------------------------------------------------------------

An error was encountered while processing a message from PADE

Date: Apr 11, 2015 12:58:49

Error Msg: PADE DEVICE NOT UPDATED Unable to file PADE Device RDO-01\|CABINET=

RDO-01\|SYSTEM=TESTSYSO

Header: MSH\|~^\\\|PSJ PADE SERVER\|500~FO-XXXXX.MED.VA.GOV~DNS\|PSJ VISTA\|\~~D

NS\|20160616144653-0400\|\|OMS~O05~OMS_O05\|500444584\|P\|2.5\|\|\|AL\|NE\|USA

Enter message action (in IN basket): Ignore//

![](inpatient-medications-pharmacy-interface-automation-pia-startup-and-troubleshoot/012.png) NOTE: For PADE DEVICE NOT UPDATED errors check with the PADE vendor (provide the date, error msg, and header as displayed in the error message) if the PADE device is valid. If the PADE device is valid, add the device to the PADE Inventory Setup option. The PADE device inventory will be updated when an HL7 message from PADE is processed.

Figure 40: Example: Drug Not on File Message

Subj: PADE Error-Msg:483244-DRUG NOT ON FILE \[#181654\] 06/23/16@15:54 5 lines

From: PADE In 'IN' basket. Page 1 \*New\*

--------------------------------------------------------------------------

An error was encountered while processing a message from PADE

Date: Jun 23, 2016 15:21:01

Error Msg: DRUG/DEVICE NOT UPDATED DRUG NOT ON FILE\|DRG ID=8000\|NAME=TEST DRUG

:CABINET=RDO-01:SYSTEM= TESTSYSO

Header: MSH\|~^\\\|PSJ PADE SERVER\|500~FO-XXXXX.MED.VA.GOV~DNS\|PSJ VISTA\|\~~D

NS\|20160623155453-0400\|\|OMS~O05~OMS_O05\|500445711\|P\|2.5\|\|\|AL\|NE\|USA

Enter message action (in IN basket): Ignore//

![](inpatient-medications-pharmacy-interface-automation-pia-startup-and-troubleshoot/013.png) NOTE: For Drug not on File, the drug ID (e.g., 8000) was *not* found in VistA. Check with the PADE Vendor (provide the date, error msg, and header) if this is a valid drug.

Figure 41: Example: Outdated Transaction

Date: Aug 02, 2016 20:12:13

Error Msg: - OUTDATED TRANSACTION - PADE.RDO-01.DRUG=RANITIDINE HCL 30

0MG TAB(1962).POCKET=34940.LAST UPDATED=3160802.212457.TRANS DT=3160802.201213\|

CABINET=RDO-01\|SYSTEM=TESTSYSO

Header: MSH\|~^\\\|PSJ PADE SERVER\|~500~FO-XXXXX.MED.VA.GOV~DNS\|PSJ VISTA\|\~~D

NS\|20160802224522\|SECURE\|OMS~O05~OMS_O05\|ZPM-068776606

2\|P\|2.5\|\|\|AL\|NE

Enter message action (in IN basket): Ignore//

![](inpatient-medications-pharmacy-interface-automation-pia-startup-and-troubleshoot/014.png) NOTE: An outdated transaction error message means that the HL7 message from PADE has a date and time stamp that was *prior* to the date and time stamp of the HL7 message that was last used to update the inventory. Hence, the HL7 message was *not* used to update the inventory.

## Dispensed Without Orders (DWO) Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A medication dispensed from a PADE dispensing device/cabinet without a corresponding pharmacy order can generate a MailMan message to one or more mail groups. For Dispensed Without Order (DWO) messages to be sent, the SEND DWO MESSAGES field *must* be set to YES for each PADE dispensing device that should be triggering DWO messages. The SEND DWO MESSAGES flag can be set via the PADE Dispensing Device Setup \[PSJ PADE DEVICE SETUP\] option. Dispensed Without Order (DWO) mail groups can be defined for seven types of entities that are ranked in order in terms of priority.

The seven types of DWO entities are:

1.  PADE Dispensing Device (Cabinet)
13. Ward Location
14. Clinic Location
15. Ward Group
16. Clinic Group
17. PADE System
18. Division

The seven types of DWO entities are grouped into four priority categories. The four priority groupings, in order from highest priority to lowest priority, are:

1.  Priority 1 – PADE Device (Cabinet)
19. Priority 2 – Ward Location/Clinic Location
20. Priority 3 – Ward Group/Clinic Group
21. Priority 4 – PADE System/Division

When a PADE HL7 message is received indicating a medication was dispensed without an order, the PADE dispensing device is first checked for a YES in the SEND DWO MESSAGES field, and if YES, the dispensing device entry is checked for a DWO mail group or groups:

- If DWO mail groups are defined for the dispensing device entry, the DWO message is sent to those mail groups and no other entities are checked.
- If no DWO mail groups are found at the first (cabinet) priority, the next highest entity priority grouping is checked (ward location and/or clinic location).
- If no DWO mail groups are found at the second (ward location and/or clinic location) priority, entities at the next highest entity is checked (ward group and/or clinic group).
- If no DWO mail groups are found, entities at the fourth and lowest priority grouping (PADE System and Division) is checked for any DWO mail groups.

When a DWO mail group is found at a given priority, a DWO message is sent to all mail groups defined at that priority, and all lower ranked DWO entities are ignored. For example, if no DWO mail group is defined for the dispensing device, all ward locations and clinic locations linked to the dispensing device are checked for DWO mail groups, and if at least one DWO mail group is found, a DWO message is sent and no additional checking is done. If multiple mail groups are found, the DWO message is sent to every mail group defined at that priority.

In the diagram in <u>Figure 42</u>:

- A medication dispensed without an order from Dispensing Device 1 sends a DWO message to Mail Group 1, defined for the PADE system, as no mail group is defined for Device 2, or for Ward 1.
- A medication dispensed without an order from Dispensing Device 2 sends a DWO message to Mail Group 2 (defined for Ward 2) and Mail Group 3 (defined for Ward 3), since the Device has no DWO mail group, and the Ward Locations have a higher priority than the PADE System.
- A medication dispensed from dispensing device CAB3 sends a DWO message to mail group TST5, defined for the dispensing device, since the dispensing device has the highest priority and all lower priorities are ignored.

Figure 42: Example Setup: Cabinet1 Supplies Ward1; Cabinet2 Supplies Wards1, 2, 3; Cabinet3 Supplies Ward3 and Clininc1

![](inpatient-medications-pharmacy-interface-automation-pia-startup-and-troubleshoot/015.png)

<u>Figure 43</u> is an example of how to define a DWO Mail Group for Ward OBSERVATION with Exclusive Dispensing Device OBS-CAB, using the PADE Dispensing Device Setup \[PSJ PADE DEVICE SETUP\] option:

Figure 43: PADE Dispensing Device Setup \[PSJ PADE DEVICE SETUP\] Option: Define a DWO Mail Group (1 of 2)

Select OPTION NAME: <span class="mark">PADE DISPENSING DEVICE SETUP \<Enter\></span> PSJ PADE DEVICE SETUP PADE

Dispensing Device Setup

PADE Dispensing Device Setup

Select PADE DISPENSING DEVICE: <span class="mark">OBS-CAB \<Enter\></span> TESTSYS ACTIVE

...OK? Yes// <span class="mark">\<Enter\></span> (Yes)

PADE STATUS: ACTIVE// <span class="mark">^ SEND DWO MESSAGES</span>

SEND DWO MESSAGES: <span class="mark">Y \<Enter\></span> Y

DWO ENTITY: <span class="mark">OBS-CAB</span>

Select DWO ENTITY MAIL GROUP: <span class="mark">LOC</span>

1 LOC GRP1

2 LOC GRP2

CHOOSE 1-2: <span class="mark">1 \<Enter\></span> LOC GRP1

Are you adding 'LOC GRP1' as a new DWO ENTITY MAIL GROUP (the 1ST for this DWO MESSAGE ENTITY)? No// <span class="mark">Y \<Enter\></span> (Yes)

Select DWO ENTITY MAIL GROUP: <span class="mark">\<Enter\></span>

Select DWO MESSAGE ENTITY:

is an example of how to define a DWO mail group for ward NHCU-1, where there is no exclusive dispensing device (i.e., dispensing device is shared with other wards, or ward is supplied by more than on dispensing device), using the PADE Inventory System Setup \[PSJ PADE INVENTORY SYSTEM\] option. This only generates DWO messages for dispensing devices with the SEND DWO MESSAGES? field set to YES.

Figure 44: PADE Dispensing Device Setup \[PSJ PADE DEVICE SETUP\] Option: Define a DWO Mail Group (2 of 2)

Select PADE Inventory Setup Option: <span class="mark">PADE Inventory System Setup</span>

Select PADE INVENTORY SYSTEM: <span class="mark">TESTSYS</span>

PADE INVENTORY SYSTEM: TESTSYS// <span class="mark">\<Enter\></span>

Select DWO MESSAGE ENTITY: <span class="mark">WD.NHCU</span>

Searching for a WARD for DWO messages., (pointed-to by DWO MESSAGE ENTITY) (NH NHCU)

Searching for a WARD for DWO messages.

NHCU XXXXX

...OK? Yes// <span class="mark">\<Enter\></span> (Yes)

Are you adding 'NHCU' as a new DWO MESSAGE ENTITY (the 1ST for this PADE INVENTORY SYSTEM)? No// <span class="mark">Y \<Enter\></span> (Yes)

Select DWO ENTITY MAIL GROUP: <span class="mark">LOC</span>

1 LOC GRP1

2 LOC GRP2

CHOOSE 1-2: <span class="mark">1 \<Enter\></span> LOC GRP1

Are you adding 'LOC GRP1' as a new DWO ENTITY MAIL GROUP (the 1ST for this DWO MESSAGE ENTITY)? No// <span class="mark">Y \<Enter\></span> (Yes)

Select DWO ENTITY MAIL GROUP: <span class="mark">\<Enter\></span>

Select DWO MESSAGE ENTITY:

<u>Figure 45</u> is an example of a DWO message generated from Dispensing Device OBS-CAB, for drug FIDAXOMICIN 200MG dispensed for patient INPATIENT,ONE:

Figure 45: Example: DWO Message Generated from Dispensing Device

Subj: PADE Dispensed Without Order \[#179605\] 01/26/16@20:19 11 lines

From: PADE In 'IN' basket. Page 1 \*New\*

--------------------------------------------------------------------------

A medication was dispensed from a PADE device without an order

PADE Device: JOB5

Date: Jan 26, 2016@20:19:06

Drug: FIDAXOMICIN 200MG

Patient: INPATIENT,ONE

User: NURSE,ONE - ID: 11361

Enter message action (in IN basket): Ignore//

# Phase 4: Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Phase 4 Roles:

The following roles are involved with Phase 4: Implementation:

- Pharmacy Staff (ADPAC)
- Vendor Engineer or Implementation Support
- <span class="mark">REDACTED</span>
- VIE National Admins <span class="mark">REDACTED</span>

Phase 4 will be mostly driven by your vendor implementation team, but <u>Table 6</u> lists some items that the pharmacy staff needs to do:

<table>
<caption><p><span id="_Toc508171893" class="anchor"></span>Table 7: Common Issues and Resolution</p></caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 42%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Phase 4:</strong></th>
<th><strong>Implementation Task</strong></th>
<th><strong>POC</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>☐</td>
<td>Confirm Implementation steps and plan with vendor.</td>
<td>Inpatient Pharmacy ADPAC</td>
</tr>
<tr class="even">
<td>☐</td>
<td><p>Notify facility (nursing, scheduling, etc.) when the cutover date will occur and any down time.</p>
<p>![](inpatient-medications-pharmacy-interface-automation-pia-startup-and-troubleshoot/016.png) <strong>NOTE:</strong> There is a down time associated with the initial setup and testing connectivity. The vendors have to wipe out their current patient list as seen at Xxxxx and Long Beach.</p></td>
<td>Inpatient Pharmacy ADPAC</td>
</tr>
<tr class="odd">
<td>☐</td>
<td>From VistA, you need to re-send all ward orders across to PADE so that the PADE vendor can rebuild their patients list. Depending on the number of patient and the orders they have, this process will take about 2–3 hours. During this down time (go-live period), the nurses are allowed to take medications from the cabinets using the override feature.</td>
<td></td>
</tr>
<tr class="even">
<td>☐</td>
<td>Inbound Step: Check the vendor’s PADE drug formulary for drug IDs that are <em>not</em> directly mapped to VISTA DRUG (#50) file Internal Entry Numbers (IENs).</td>
<td></td>
</tr>
<tr class="odd">
<td>☐</td>
<td>Verify that there are <strong>no</strong> purely numeric “<em>no</em>n-Vista Drug File” drug IDs in the vendor’s drug formulary.</td>
<td></td>
</tr>
<tr class="even">
<td>☐</td>
<td>If any purely numeric drug IDs are found in the vendor’s PADE formulary that do <em>not</em> correspond to the same drug in the VISTA DRUG (#50) file, the vendor’s drug ID <em>must</em> be changed to an alpha or alpha-numeric ID, so that it is <em>not</em> inadvertently linked to the wrong drug in VistA’s PADE inventory functionality.</td>
<td></td>
</tr>
<tr class="odd">
<td>☐</td>
<td><p>Request Health Connect connection Information.</p>
<p>IP and Port information for both PSJ PADE and Vendor Server as well as ACL edit for the VLAN where the Vendor server is located.</p>
<p>![](inpatient-medications-pharmacy-interface-automation-pia-startup-and-troubleshoot/017.png) <strong>NOTE:</strong> Getting these ACL edits applied by the LAN teams require a couple of weeks lead time.</p></td>
<td>VIE National Admin Team <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>☐</td>
<td>Test connectivity once ACL Edits are applied.</td>
<td>VIE National Admin Team/Vendor/VLAN Manager</td>
</tr>
<tr class="odd">
<td>☐</td>
<td>Schedule a day/time for the interface to be brought up. This has typically taken <strong>2+</strong> hours. It seems to be best in the early morning hours.</td>
<td>Inpatient Pharmacy ADPAC /Health Connect/Vendor</td>
</tr>
<tr class="even">
<td>☐</td>
<td>Notify the facility.</td>
<td>Inpatient Pharmacy ADPAC /Health Connect/Vendor</td>
</tr>
<tr class="odd">
<td>☐</td>
<td>Initialize data and patient information. This will happen right before go-live.</td>
<td>Vendor</td>
</tr>
<tr class="even">
<td>☐</td>
<td><p>Bring up the Interface.</p>
<p>![](inpatient-medications-pharmacy-interface-automation-pia-startup-and-troubleshoot/018.png) <strong>NOTE:</strong> The Inpatient Pharmacy ADPAC, Health Connect, vendor, and any local or regional IT support need to be present. This typically takes <strong>2+</strong> hours.</p></td>
<td>Inpatient Pharmacy ADPAC /Health Connect/Vendor</td>
</tr>
<tr class="odd">
<td>☐</td>
<td>In VistA, the pharmacist should process new orders and the vendor should confirm the receipt of the orders to ensure the interface is working.</td>
<td>Inpatient Pharmacy ADPAC/Vendor</td>
</tr>
<tr class="even">
<td>☐</td>
<td>Set up the new field, DEFAULT 0 ON PADE PRE-EXCHANGE (#??) to <strong>YES</strong> in Inpatient Ward Parameters Edit (PSJ IWP EDIT) for wards that are cart less or 100% PADE. If this parameter is set to <strong>YES</strong>, field defaults to <strong>zero</strong> in the "Pre-Exchange DOSES:" prompt for orders that may be dispensed from PADE.</td>
<td>Inpatient Pharmacy ADPAC</td>
</tr>
</tbody>
</table>

<span id="_Toc508171893" class="anchor"></span>Table 7: Common Issues and Resolution

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Key Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Clinical Product Support—Submit a CA ticket for support
- VIE National Admins <span class="mark">REDACTED</span>
- Support sites/ Documentation

See the “<u>Introduction</u>” section for all supporting documents. All information and discussion can be found on VA Pulse at: <span class="mark">REDACTED</span>

<span class="mark">Outbound HL7 messages will remain on file in the PADE OUTBOUND MESSAGES file (#58.72) for 90 days for troubleshooting purposes, after which they are purged by the the nightly unit dose cleanup process.</span>

Common Issues and Resolution

<table>
<caption>Common Issues and ResolutionCommon Issues and Resolution</caption>
<colgroup>
<col style="width: 37%" />
<col style="width: 30%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th>Issue</th>
<th>Common Resolution</th>
<th>Support Contact</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Certain edits/corrections to historical ADT (admission, discharge, transfer) transactions can cause the patients/orders to fall off the cabinet even though they are still admitted.</td>
<td><p>In this situation, the nurse will contact the pharmacy.</p>
<p>The pharmacy can send the orders using the <a href="#pade_sendpatientorders_so">PSJ PADE Send Order</a> option.</p></td>
<td></td>
</tr>
<tr class="even">
<td>Vendor Messaging Server is <em>not</em> receiving messages.</td>
<td><p>Submit a CA ticket.</p>
<p>Check to see if logical link is working.</p></td>
<td></td>
</tr>
<tr class="odd">
<td>What is the contingency plan if Health Connect goes down?</td>
<td>For all of the applications that are supported by Health Connect, if a site has an issue they think is potentially related to Health Connect, a CA ticket should be opened. In the case of Outpatient Automation Interface (OPAI) or PADE they should open a High Priority CA ticket by calling the VA Service Desk. Request that the help desk get a member of the VIE National Admin team on the phone 24/7. PADE will be supported in the same way as OPAI.</td>
<td>VIE National Admins <mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

Common Issues and ResolutionCommon Issues and Resolution