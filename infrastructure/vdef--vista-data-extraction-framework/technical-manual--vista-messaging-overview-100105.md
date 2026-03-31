---
title: VDEF VistA Messaging Overview 100105
doc_type: TM
doc_label: Technical Manual
doc_layer: plain
doc_subject: 
app_code: VDEF
app_name: VistA Data Extraction Framework
section: INF
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: - [VistA Data Extraction Framework (VDEF)](#vista-data-extraction-framework-vdef) - [![](vdef-vista-messaging-overview-100105/002.png)![](vdef-vista-messaging-overview-100105/003.png)![](vdef-vista-messaging-overview-100105/004.png)![](vdef-vista-messaging-overview-100105/005.png)![](vdef-vista-mess
audience: 
keywords: 
  - vdef
  - vista
  - messaging
  - overview
  - strong
  - table
  - contents
  - blockquote
  - pngvdef
  - message
page_count: 0
word_count: 1160
section_count: 3
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Vista_Data_Ex_(VDEF)/vistamessagingoverview_vdef_100105.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Vista_Data_Ex_(VDEF)/vistamessagingoverview_vdef_100105.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=144"
---

> ![](vdef-vista-messaging-overview-100105/001.png)

# VistA Data Extraction Framework (VDEF)


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [VistA Data Extraction Framework (VDEF)](#vista-data-extraction-framework-vdef)
- [![](vdef-vista-messaging-overview-100105/002.png)![](vdef-vista-messaging-overview-100105/003.png)![](vdef-vista-messaging-overview-100105/004.png)![](vdef-vista-messaging-overview-100105/005.png)![](vdef-vista-messaging-overview-100105/006.png)![](vdef-vista-messaging-overview-100105/007.png)![](vdef-vista-messaging-overview-100105/008.png)![](vdef-vista-messaging-overview-100105/009.png)![](vdef-vista-messaging-overview-100105/010.png)![](vdef-vista-messaging-overview-100105/011.png)![](vdef-vista-messaging-overview-100105/012.png)VDEF Overall Diagram](#vdef-vista-messaging-overview-100105002pngvdef-vista-messaging-overview-100105003pngvdef-vista-messaging-overview-100105004pngvdef-vista-messaging-overview-100105005pngvdef-vista-messaging-overview-100105006pngvdef-vista-messaging-overview-100105007pngvdef-vista-messaging-overview-100105008pngvdef-vista-messaging-overview-100105009pngvdef-vista-messaging-overview-100105010pngvdef-vista-messaging-overview-100105011pngvdef-vista-messaging-overview-100105012pngvdef-overall-diagram)
  - [Trigger](#trigger)
- [![](vdef-vista-messaging-overview-100105/023.png)VDEF Export VistA data](#vdef-vista-messaging-overview-100105023pngvdef-export-vista-data)
- [![](vdef-vista-messaging-overview-100105/027.png)VDEF Main Menu](#vdef-vista-messaging-overview-100105027pngvdef-main-menu)
    - [![](vdef-vista-messaging-overview-100105/030.png)VDEF – Activate/Inactivate Requestor](#vdef-vista-messaging-overview-100105030pngvdef-activateinactivate-requestor)
    - [![](vdef-vista-messaging-overview-100105/031.png)VDEF – Suspend/Run Request Queue](#vdef-vista-messaging-overview-100105031pngvdef-suspendrun-request-queue)
    - [![](vdef-vista-messaging-overview-100105/034.png)VDEF – Status of VDEF Components](#vdef-vista-messaging-overview-100105034pngvdef-status-of-vdef-components)
    - [![](vdef-vista-messaging-overview-100105/035.png)VDEF – Request Processor Schedule](#vdef-vista-messaging-overview-100105035pngvdef-request-processor-schedule)
- [![](vdef-vista-messaging-overview-100105/044.png)VDEF – Error Messages](#vdef-vista-messaging-overview-100105044pngvdef-error-messages)
- [![](vdef-vista-messaging-overview-100105/045.png)VDEF - Advantages](#vdef-vista-messaging-overview-100105045pngvdef-advantages)
- [![](vdef-vista-messaging-overview-100105/048.png)VDEF Application](#vdef-vista-messaging-overview-100105048pngvdef-application)
  - [Questions ??](#questions)
> REDACTED

# ![](vdef-vista-messaging-overview-100105/002.png)![](vdef-vista-messaging-overview-100105/003.png)![](vdef-vista-messaging-overview-100105/004.png)![](vdef-vista-messaging-overview-100105/005.png)![](vdef-vista-messaging-overview-100105/006.png)![](vdef-vista-messaging-overview-100105/007.png)![](vdef-vista-messaging-overview-100105/008.png)![](vdef-vista-messaging-overview-100105/009.png)![](vdef-vista-messaging-overview-100105/010.png)![](vdef-vista-messaging-overview-100105/011.png)![](vdef-vista-messaging-overview-100105/012.png)VDEF Overall Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vdef-vista-messaging-overview-100105/013.png)![](vdef-vista-messaging-overview-100105/014.png)![](vdef-vista-messaging-overview-100105/015.png)

![](vdef-vista-messaging-overview-100105/016.png)

![](vdef-vista-messaging-overview-100105/017.png)![](vdef-vista-messaging-overview-100105/018.png)![](vdef-vista-messaging-overview-100105/019.png)

> ![](vdef-vista-messaging-overview-100105/020.png)VDEF domain applications & Trigger request

- *Domain applications:*
  - *Allergies*
  - *Outpatient Pharmacy*
  - *Vitals*

## Trigger

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- *adds entry to VDEF Request Queue (FIFO)*
- *then VDEF task processes the trigger event*

> ![](vdef-vista-messaging-overview-100105/021.png)VDEF Activities within Messaging

#### VistA Data Extraction Framework (VDEF)

- *Extract LIVE data from VistA database*
- *Generate HL7 message (using HL7 v2.4 standard)*
- *Hand off HL7 message to HL7 application*

#### HL7 Engine (v1.6)

- *Deliver HL7 message to VIE*

#### VistA Interface Engine (VIE)

- *Deliver HL7 message to Receiving Facility*
- *Receiving Facility - Health Data Repository system (HDR / HDR II)*
  - *Parse HL7 message and store data on target systems*

> ![](vdef-vista-messaging-overview-100105/022.png)VDEF’s Events & Message Types

> *Vitals Package: GEN. MED. REC. – VITALS ORU-R01-VTLS PATIENT VITALS*

> *Allergy Package: ADVERSE REACTION TRACKING ORU-R01-ALGY ALLERGY UPDATE/INSERT ORU-R01-ADAS ALLERGY ASSESSMENT*

> *ORU-R01-ADRA ADVERSE REACTION REPORT*

> *Outpatient Pharmacy Package: OUTPATIENT PHARMACY RDE-O11-PRES OP PHARM PRESCRIPTION*

> *RDS-O13-PPAR OP PHARM PRESCRIPTION PARTIAL*

> *RDS-O13-PREF OP PHARM PRESCRIPTION REFILL*

# ![](vdef-vista-messaging-overview-100105/023.png)VDEF Export VistA data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Convert VistA data into HL7 Message*

![](vdef-vista-messaging-overview-100105/024.png)![](vdef-vista-messaging-overview-100105/025.png)![](vdef-vista-messaging-overview-100105/026.png)

# ![](vdef-vista-messaging-overview-100105/027.png)VDEF Main Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select Systems Manager Menu Option: VDEF VDEF Configuration and Status

> Site Site-Wide Parameters Req Request Queue Parameters

> ActR Activate/Inactivate Requestor

> SusR Suspend/Run Request Queue

> Cust VDEF Custodial Package Activate/Inactivate API VDEF Event API Activate/Inactivate

> Stat Status of VDEF components Sch Request Processor Schedule

> ![](vdef-vista-messaging-overview-100105/028.png)VDEF – Site-Wide Parameters

> Site Site-Wide Parameters Req Request Queue Parameters

> ActR Activate/Inactivate Requestor SusR Suspend/Run Request Queue

> Cust VDEF Custodial Package Activate/Inactivate API VDEF Event API Activate/Inactivate

> Stat Status of VDEF components Sch Request Processor Schedule

> Select VDEF Configuration and Status Option: SITE Site-Wide Parameters

> VDEF SYSTEM: TEST.REDACTED.MED.VA.GOV// VDEF MONITOR DELAY: 30S//

> ![](vdef-vista-messaging-overview-100105/029.png)VDEF – Request Queue Parameters

> Select VDEF Configuration and Status Option: Req Request Queue Parameters

> Select Request Queue: ??

> MAINTENANCE

> Select Request Queue: MAINTENANCE ARCHIVAL PARAMETER: 30D 23H 59M 59S// CHECKED OUT TIME LIMIT: 10M//

> REQUEST QUEUE WAKEUP PERIOD: 10S//

### ![](vdef-vista-messaging-overview-100105/030.png)VDEF – Activate/Inactivate Requestor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Select VDEF Configuration and Status Option: ActR Activate/Inactivate Requestor

> Select Requestor: MAINTENANCE

> Inactivating a requestor has a significant effect on the synchronization of VistA and remote system(s). All VDEF requests made while the requestor is inactive will be PERMANENTLY lost. Make sure you really want to turn it off.

> REQUESTOR ACTIVATION FLAG: ACTIVE//

### ![](vdef-vista-messaging-overview-100105/031.png)VDEF – Suspend/Run Request Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Site Site-Wide Parameters

> Req Request Queue Parameters

> ActR Activate/Inactivate Requestor SusR Suspend/Run Request Queue

> Cust VDEF Custodial Package Activate/Inactivate API VDEF Event API Activate/Inactivate

> Stat Status of VDEF components Sch Request Processor Schedule

> Select VDEF Configuration and Status Option: SusR Suspend/Run Request Queue

> Select Request Queue: MAINTENANCE SUSPENDED FLAG: RUNNING//

> ![](vdef-vista-messaging-overview-100105/032.png)VDEF – VDEF Custodial Package Activate/Inactivate

> Select VDEF Configuration and Status Option: Cust VDEF Custodial Package Activate/Inactivate

> Select Custodial Package: ??

> Choose from:

> OUTPATIENT PHARMACY GEN. MED. REC. - VITALS

> ADVERSE REACTION TRACKING

> Select Custodial Package: OUTPATIENT PHARMACY PSO

> Inactivating a custodial package has a significant effect on the synchronization of VistA and remote system(s). All VDEF requests for HL7 messages associated with this custodial package made while the package is inactivated will be PERMANENTLY lost. Make sure you really want to turn this custodial package off.

> ACTIVATION STATUS: ACTIVE// ?

> Sending messages for this package is "A"ctive or "I"nactive Choose from:

> A ACTIVE

> I INACTIVE ACTIVATION STATUS: ACTIVE//

> ![](vdef-vista-messaging-overview-100105/033.png)VDEF – VDEF Event API Activate/Inactivate

> Select VDEF Configuration and Status Option: API VDEF Event API Activate/Inactivate

> Select VDEF API Event: ??

> Choose from:

1.  ORU-R01-VTLS PATIENT VITALS Status: ACTIVE Pkg: GEN. MED. REC. - VITALS HL7 Engine: HL7 1.6
2.  ORU-R01-ALGY ALLERGY UPDATE/INSERT Status: ACTIVE Pkg: ADVERSE REACTION TRACKING HL7 Engine: HL7 1.6
3.  ORU-R01-ADAS ALLERGY ASSESSMENT Status: ACTIVE Pkg: ADVERSE REACTION TRACKING HL7 Engine: HL7 1.6
4.  ORU-R01-ADRA ADVERSE REACTION REPORT Status: ACTIVE Pkg: ADVERSE REACTION TRACKING HL7 Engine: HL7 1.6
5.  RDE-O11-PRES OP PHARM PRESCRIPTION Status: ACTIVE Pkg: OUTPATIENT PHARMACY HL7 Engine: HL7 1.6
6.  RDS-O13-PPAR OP PHARM PRESCRIPTION PARTIAL Status: ACTIVE Pkg: OUTPATIENT PHARMACY HL7 Engine: HL7 1.6
7.  RDS-O13-PREF OP PHARM PRESCRIPTION REFILL Status: ACTIVE Pkg: OUTPATIENT PHARMACY HL7 Engine: HL7 1.6

> Select VDEF API Event: 5 OP PHARM PRESCRIPTION Status: ACTIVE Pkg: OUTPATIENT PHARMACY HL7 Engine: HL7 1.6

> Inactivating a VDEF API event will cause all requests for that API to be PERMANENTLY lost. Make sure you really want to turn this API event off.

> API EVENT ACTIVE FLAG: ACTIVE//

### ![](vdef-vista-messaging-overview-100105/034.png)VDEF – Status of VDEF Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

####### Select VDEF Configuration and Status Option: Stat Status of VDEF components

> VDEF Status - JUN 03, 2009@19:26:52

> Logical Link Status

> VDEFVIE1: stopped or caught up VDEFVIE2: stopped or caught up VDEFVIE3: stopped or caught up

> Requestor Status

> MAINTENANCE: Activated Dest.: VISTA HL7 Req. Queue: MAINTENANCE

> Request Processor Status MAINTENANCE: Running

> Current Task \# \[Proc\]: 1440227 \[20C008F5\] Task status: Active-Running Requests waiting for purge: 1271405 last request#: 2934699 Checked Out(98) Queued Up(\>1000) Errored Out(0)

### ![](vdef-vista-messaging-overview-100105/035.png)VDEF – Request Processor Schedule

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Site Site-Wide Parameters

> Req Request Queue Parameters ActR Activate/Inactivate Requestor SusR Suspend/Run Request Queue

> Cust VDEF Custodial Package Activate/Inactivate API VDEF Event API Activate/Inactivate

> Stat Status of VDEF components Sch Request Processor Schedule

> Select VDEF Configuration and Status Option: Sch Request Processor Schedule

> Select Request Queue: MAINTENANCE

> No Scheduling Rules currently defined for this queue

> Select Entry:

> ![](vdef-vista-messaging-overview-100105/036.png) HL7 – System Link Monitor

> SYSTEM LINK MONITOR for REDACTED VAMC (T System)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>NODE</strong></th>
<th><blockquote>
<p><strong>MESSAGES</strong></p>
<p><strong>RECEIVED</strong></p>
</blockquote></th>
<th><p><strong>MESSAGES</strong></p>
<p><strong>PROCESSED</strong></p></th>
<th><p><strong>MESSAGES</strong></p>
<p><strong>TO SEND</strong></p></th>
<th><p><strong>MESSAGES</strong></p>
<p><strong>SENT</strong></p></th>
<th><p><strong>DEVICE</strong></p>
<p><strong>TYPE</strong></p></th>
<th><blockquote>
<p><strong>STATE</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>VDEFVIE1</strong></td>
<td><blockquote>
<p><strong>10</strong></p>
</blockquote></td>
<td><strong>10</strong></td>
<td><strong>10</strong></td>
<td><strong>10</strong></td>
<td><blockquote>
<p><strong>NC</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Enabled</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>VDEFVIE2</strong></td>
<td><blockquote>
<p><strong>437</strong></p>
</blockquote></td>
<td><strong>437</strong></td>
<td><strong>764</strong></td>
<td><strong>437</strong></td>
<td><blockquote>
<p><strong>NC</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Enabled</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>VDEFVIE3</strong></td>
<td><blockquote>
<p><strong>620</strong></p>
</blockquote></td>
<td><strong>620</strong></td>
<td><strong>620</strong></td>
<td><strong>620</strong></td>
<td><blockquote>
<p><strong>NC</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Enabled</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> Incoming filers running =\> 1 TaskMan running Outgoing filers running =\> 1 Link Manager running

> Monitor current \[next job 0.1 hr\]

> Select a Command:

> (N)EXT (B)ACKUP (A)LL LINKS (S)CREENED (V)IEWS (Q)UIT (?) HELP:

> ![](vdef-vista-messaging-overview-100105/037.png)VDEF – File 579.3 VDEF Request Queue

#### VDEF Request Queue before HL7 message is generated:

> ^VDEFHL7(579.3,1,1,3307,0)=3307^Q^RDE^O11^^1^1^3080827.173717^^^^^^^^^^5

> ^VDEFHL7(579.3,1,1,3307,.05,0)=^579.311^2^2

> ^VDEFHL7(579.3,1,1,3307,.05,1,0)=1^SUBTYPE=PRES

> ^VDEFHL7(579.3,1,1,3307,.05,2,0)=2^IEN=1614645

> ^VDEFHL7(579.3,1,1,3307,1,"B",1,1)=

> ^VDEFHL7(579.3,1,1,3307,1,"B",2,2)=

#### VDEF Request Queue after HL7 message is generated:

> ^VDEFHL7(579.3,1,1,3307,0)=3307^P^RDE^O11^^1^1^3080827.173717^3080827.17392^3080 827.17392^^44233620030^3080827.17392^^^^^5

> ^VDEFHL7(579.3,1,1,3307,.05,0)=^579.311^2^2

> ^VDEFHL7(579.3,1,1,3307,.05,1,0)=1^SUBTYPE=PRES

> ^VDEFHL7(579.3,1,1,3307,.05,2,0)=2^IEN=1614645

> ^VDEFHL7(579.3,1,1,3307,1,"B",1,1)=

> ^VDEFHL7(579.3,1,1,3307,1,"B",2,2)=

> ![](vdef-vista-messaging-overview-100105/038.png)VDEF – HL7 Message Header File (File-773)

> File-773 : HL7 Message Administration

> ^HLMA(33620030,0)=35387771^44233620030^O^D^^33620030^210^6776^^^

> 133^132^1^^^^210

> ^HLMA(33620030,"MSH",0)=^773.01^1^1

> ^HLMA(33620030,"MSH",1,0)=MSH^~\|\\^HDRPRES^442~TEST.REDACTED. MED.VA.GOV~DNS^PSO VDEF IE SIDE^200HD~HDR.MED.VA.GOV~DNS^20080827173920- 0500^^RDE~O11^44233620030^T^2.4^^^AL^NE^USA

> ^HLMA(33620030,"P")=1

> ![](vdef-vista-messaging-overview-100105/039.png)VDEF – HL7 Message Header File (File-773)

> HL7 MESSAGE ADMINISTRATION:

> NUMBER: 33620030 DATE/TIME ENTERED: AUG 27, 2008@17:39:20 MESSAGE ID: 44233620030 TRANSMISSION TYPE: OUTGOING

> PRIORITY: DEFERRED INITIAL MESSAGE: AUG 27, 2008@17:39:20 LOGICAL LINK: VDEFVIE3

> SUBSCRIBER PROTOCOL: PSO VDEF RDE O11 OP PHARM PRES HR

> SENDING APPLICATION: HDRPRES RECEIVING APPLICATION: PSO VDEF IE SIDE MESSAGE TYPE: ACK LOGICAL LINK - IN QUEUE: VDEFVIE3

> MSH:

> MSH^~\|\\^HDRPRES^442~TEST.REDACTED.MED.VA.GOV~DNS^PSO VDEF IE SIDE^200HD~HDR.MED.VA.GOV~DNS^20080827173920-0500^^RDE~O11^44233620030^T^2.4^^^AL^NE^USA\|

> STATUS: PENDING TRANSMISSION MESSAGE SIZE (c): 1705

> ![](vdef-vista-messaging-overview-100105/040.png)VDEF – HL7 Message Text

> File-772 : HL7 Message Text

> ^HL(772,35387771,0)=3080827.17392^133^^O^^44235387771^^35387771^D^6777^^^^M

> ^HL(772,35387771,"IN",0)=^^15^15^3080827^

> ^HL(772,35387771,"IN",1,0)=PID^1^6661234567V666123^6661234567V666123\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|666123456\~\~~USSSA&&0363~SS~VA FACILITY ID&442&L\|666123\~\~~USVHA&&0363~PI~VA FACILITY ID&442&L\|66612345\~\~~USVBA&&0363~PN~VA FACILITY ID&442&L^^OPPATIENT~ONE\~\~\~\~~L^OPMOTHER

> ^HL(772,35387771,"IN",2,0)=\~\~\~\~\~~M^19500509^M^^1111-3-SLF\~~2222~1111-3\~~CDC^666 ADDRESS

> ~""~CITY~ST~66666~""~P~""~021\|\~~CITY~ST\~\~~N^021^(777)777-7777~PRN~PH\|(111)111-1111~ORN~CP^""^^W^29^^666123456^^^3333-3-

> SLF\~~4444~5555-5\~~CDC^AAAABBBB MA^^^^^^""^^

> ^HL(772,35387771,"IN",3,0)=

> ^HL(772,35387771,"IN",4,0)=ORC^RE^3389378~442_52_39.3^1614645~442_52\_.001^^CM^^\~\~~20070305~20070404

> \~~FILL/EXPIRATION\|\~\~\~~20070305\~~ISSUED\|\~\~~20070305~20070305\~~DISPENSED/LAST DISPENSED^^20070305165017-

> 0500^2229~OPENTER~ONE\~\~\~\~~VistA200^^2453~OPORDER~ONE~D\~\~~MD~RE^^^

> ^HL(772,35387771,"IN",5,0)=^^442~REDACTED VAM\T\ROC~442_52_20~5203651~REDACTED VAM\T\ROC~NCPDP^^^^REDACTED VAMC^^^^4500659~ACTIVE~99VA_52_100

> ^HL(772,35387771,"IN",6,0)=

> ^HL(772,35387771,"IN",7,0)=RXE^&ONE TABLET\~\~~20070305~20070404\~~FILL/EXPIRATION^4003067~OXYCODONE HCL 5MG /ACETAMINOPHEN 325MG TAB~99VA_52_6~00406-0512-01\~~NDC^0^^0\~~442_52_6^63~TAB~442_50.7\_.02^ ~TAKE~442_52.0113_8\|~TID~442_52.0113_7\|~F CHRONIC PAIN~442_52_114\|~FOR CHRONIC

> ^HL(772,35387771,"IN",8,0)=PAIN~442_52_115^\~\~\~\~~WINDOW^^21^^0^^666111111~OPPARM~ONE~M\~\~\~~PHARMACIST^856897 ^^^20070305165648- 0500^^^TAKE ONE TABLET BY MOUTH THREE TIMES A DAY FOR CHRONIC PAIN\~~442_52_10.2 ^D7^^^^^^^^^344~OXYCODONE 5MG \T\\ ACETAMINOPHEN 325MG TAB~442_50\_.01

> ^HL(772,35387771,"IN",9,0)=

> ^HL(772,35387771,"IN",10,0)=RXR^1~ORAL (BY MOUTH)~442_52.0113_6

> ^HL(772,35387771,"IN",11,0)=

> ^HL(772,35387771,"IN",12,0)=FT1^1^^^20070305^^CG^893~OXYCODONE/ACETAMINOPHEN~442_52_39.2^^^^^0.0338^^^^^^OPT SC^^6666~OPPROVIDER~ONE\~\~\~\~~442_52_38

> ^HL(772,35387771,"IN",13,0)=

> ^HL(772,35387771,"IN",14,0)=OBX^1^CE^WAS THE PATIENT COUNSELED^^4500630~NO~99VA_52_41^^^^^^F

> ^HL(772,35387771,"IN",15,0)=

> ^HL(772,35387771,"P")=3^3080827.17392

> "S")=1548^1

> ![](vdef-vista-messaging-overview-100105/041.png)VDEF – HL7 Message Text

######## HL7 MESSAGE TEXT

> NUMBER: 35387771 DATE/TIME ENTERED: AUG 27, 2008@17:39:20 SERVER APPLICATION: HDRPRES TRANSMISSION TYPE: OUTGOING

> MESSAGE ID: 44235387771 PARENT MESSAGE: AUG 27, 2008@17:39:20 PRIORITY: DEFERRED

> RELATED EVENT PROTOCOL: PSO VDEF RDE O11 OP PHARM PRES VS MESSAGE TYPE: SINGLE MESSAGE

> MESSAGE TEXT:

> PID^1^6661234567V666123^6661234567V666123\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|666123456\~\~~USSSA&&0363~SS~VA FACILITY ID&442&L\|666123\~\~~USVHA&&0363~PI~VA FACILITY ID&442&L\|66612345\~\~~USVBA&&0363~PN~VA FACILITY ID&442&L^^OPPATIENT~ONE\~\~\~\~~L^OPMOTHER

> \~\~\~\~\~~M^19500509^M^^1111-3-SLF\~~2222~1111-3\~~CDC^666 ADDRESS ~""~CITY~ST~66666~""~P~""~021\|\~~CITY~ST\~\~~N^021^(777)777- 7777~PRN~PH\|(111)111-1111~ORN~CP^""^^W^29^^666123456^^^3333-3-SLF\~~4444~5555-5\~~CDC^AAAABBBB MA^^^^^^""^^

> ORC^RE^3389378~442_52_39.3^1614645~442_52\_.001^^CM^^\~\~~20070305~20070404\~~FILL/EXPIRATION\|\~\~\~~20070305\~~ISSUED\|\~\~~20070305~20070 305\~~DISPENSED/LAST DISPENSED^^20070305165017-

> 0500^2229~OPENTER~ONE\~\~\~\~~VistA200^^2453~OPORDER~ONE~D\~\~~MD~RE^^^^^442~REDACTED VAM\T\ROC~442_52_20~5203651~REDACTED VAM\T\ROC~NCPDP^^^^REDACTED VAMC^^^^4500659~ACTIVE~99VA_52_100

> RXE^&ONE TABLET\~\~~20070305~20070404\~~FILL/EXPIRATION^4003067~OXYCODONE HCL 5MG /ACETAMINOPHEN 325MG TAB~99VA_52_6~00406-0512- 01\~~NDC^0^^0\~~442_52_6^63~TAB~442_50.7\_.02^ ~TAKE~442_52.0113_8\|~TID~442_52.0113_7\|~F CHRONIC PAIN~442_52_114\|~FOR CHRONIC

> PAIN~442_52_115^\~\~\~\~~WINDOW^^21^^0^^666111111~OPPARM~ONE~M\~\~\~~PHARMACIST^856897 ^^^20070305165648-0500^^^TAKE ONE TABLET BY MOUTH THREE TIMES A DAY FOR CHRONIC PAIN\~~442_52_10.2 ^D7^^^^^^^^^344~OXYCODONE 5MG \T\\ ACETAMINOPHEN 325MG TAB~442_50\_.01

> RXR^1~ORAL (BY MOUTH)~442_52.0113_6

> FT1^1^^^20070305^^CG^893~OXYCODONE/ACETAMINOPHEN~442_52_39.2^^^^^0.0338^^^^^^OPT SC^^6666~OPPROVIDER~ONE\~\~\~\~~442_52_38 OBX^1^CE^WAS THE PATIENT COUNSELED^^4500630~NO~99VA_52_41^^^^^^F

> STATUS: SUCCESSFULLY COMPLETED

> DATE/TIME PROCESSED: AUG 27, 2008@17:39:20

> NO. OF CHARACTERS IN MESSAGE: 1548 NO. OF EVENTS IN MESSAGE: 1

> ![](vdef-vista-messaging-overview-100105/042.png)VDEF – Messaging Work Bench

![](vdef-vista-messaging-overview-100105/043.png)

# ![](vdef-vista-messaging-overview-100105/044.png)VDEF – Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Error Message in VDEF File-579.3:

> ^VDEFHL7(579.3,1,1,2190679,0)=2190679^E^ORU^R01^^1^1^3080605.114245^3080610.114852^^^^^^^^^1

> ^VDEFHL7(579.3,1,1,2190679,.05,0)=^579.311^2^2

> ^VDEFHL7(579.3,1,1,2190679,.05,1,0)=1^SUBTYPE=VTLS

> ^VDEFHL7(579.3,1,1,2190679,.05,2,0)=2^IEN=10515224

> ^VDEFHL7(579.3,1,1,2190679,1,"B",1,1)=

> ^VDEFHL7(579.3,1,1,2190679,1,"B",2,2)=

> ^VDEFHL7(579.3,1,1,2190679,"ERRMSG")=Invalid data in file GMR(120.5) for IEN 10515224

#### Examples of VDEF Alerts in FORUM:

- RECORD \<IEN\> IN QUEUE \<QUEUE NAME\> HUNG IN CHECKED OUT STATUS.

> *Reason: IEN in VDEF REQUEST QUEUE has been in the Checked Out status longer than the allowed time period.*

- VDEF HAS REQUEUED CHECKED OUT RECORDS. NO ACTION NEEDED.

> *Reason: VDEF queue process has re-queued one or more requests that were hung in the Checked Out status*

- VDEF HAS REQUEUED ERRORED OUT RECORDS. NO ACTION NEEDED.

> *Reason: VDEF queue process has re-queued one or more requests that were in the Error Out status*

# ![](vdef-vista-messaging-overview-100105/045.png)VDEF - Advantages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Standardize HL7 Messages

- *Reuse code and API calls*

#### Reuse Message Segments and Fields

- *Simplify regeneration of HL7 message if needed*

#### Verify data before HL7 message is generated

- *Generate HL7 message from LIVE data that will not duplicate or overwrite previous HL7 message*

#### Monitor HL7 message generation process

- *Document individual HL7 field in Messaging Work Bench*

#### Provide VDEF Alerts

- *And much more . . .*

> ![](vdef-vista-messaging-overview-100105/046.png)VDEF – Job Requirement :

> Decode VistA data into HL7 message

![](vdef-vista-messaging-overview-100105/047.png)

# ![](vdef-vista-messaging-overview-100105/048.png)VDEF Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Questions ??
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)