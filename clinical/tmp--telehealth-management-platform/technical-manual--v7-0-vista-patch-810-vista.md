---
title: TMP Version 7.0 Vista Patch 810 VistA Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: Vista Patch 810 VistA
app_code: TMP
app_name: Telehealth Management Platform
section: CLI
app_status: active
pkg_ns: TMP
patch_ver: 7.0
patch_id: TMP*7.0
group_key: "TMP:TMP:7.0"
file_numbers: []
security_keys: []
menu_options: 2
description: 
audience: 
keywords: 
  - vista
  - segment
  - stop
  - message
  - code
  - table
  - class
  - strong
  - health
  - clinic
page_count: 0
word_count: 3756
section_count: 8
table_count: 20
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Telehealth_Management_Platform/tmp_vista_technical_manual_v07.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Telehealth_Management_Platform/tmp_vista_technical_manual_v07.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=231"
---

Department of Veterans AffairsTelehealth Management Platform (TMP) Technical Manual  
  
Technical Manual

![](tmp-version-7-0-vista-patch-810-vista-technical-manual/001.png)

November 2021Version 1.1Revision History

| Date      | Version | Description                      | Author |
|---------------|-------------|--------------------------------------|------------|
| November 2021 | 1.1         | Add HL7 information for SD\*5.3\*780 | LTS        |
| June 2019     | 1.0         | Initial version for submission       | LTS        |
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [HL7 Interface](#hl7-interface)
  - [Assumptions](#assumptions)
  - [HL7/HLO Logical Link](#hl7hlo-logical-link)
  - [HL7 Protocols](#hl7-protocols)
  - [HL7 Application Parameters](#hl7-application-parameters)
  - [## HL7 Message Segments](#hl7-message-segments)
    - [Make and Cancel Appointment messages](#make-and-cancel-appointment-messages)
    - [Get Consults Message](#get-consults-message)
    - [Real Time Clinic Update Message](#real-time-clinic-update-message)
- [VistA Data Dictionary Changes](#vista-data-dictionary-changes)
  - [HOSPITAL LOCATION FILE](#hospital-location-file)
  - [SD TELE HEALTH STOP CODE FILE](#sd-tele-health-stop-code-file)
- [Troubleshooting](#troubleshooting)
The Telehealth Management Program (TMP) integrates with Veterans Health Information Systems and Technology Architecture (VistA) to schedule, cancel or update appointments in support of Telehealth services provided by the VA. When an appointment is made or canceled on TMP, a message is sent to VistA to update the VistA files with the appointment information. This information is then viewable in VistA Scheduling Options, Computerized Patient Record System (CPRS), Vista Scheduling Enhancements (VSE) and other applications. The integration with VistA is bi-directional and so Telehealth related appointments scheduled directly on VistA are also transmitted to TMP. The following is a diagram of the integration interfaces.
![](tmp-version-7-0-vista-patch-810-vista-technical-manual/002.png)
These interfaces use the Health Level 7 (HL7) international standard for communication of clinical and administrative health related data.
- The TMP – VistA interface uses the VistA HL7 and VistA HL7 Optimized (HLO) applications to send and receive HL7 messages on the VistA system. In addition to this guide, please refer to the VistA HL7 SITE MANAGER AND DEVELOPERS’ MANUAL and the HLO SYSTEM MANAGER MANUAL for information specific to these interfaces.
- The TMP messaging system includes the TMP application, a HealthConnect Ensemble Production and VistA. The HealthConnect Ensemble Production is maintained by the VA’s HealthShare Team. TMP doesn’t have a direct HL7 interface. TMP uses JavaScript Option Notation format (JSON) to exchange messages. However, VistA is not capable of receiving JSON messages directly. VistA relies on the HL7 messaging to do the translation and communication with TMP.
- TMP deploys an InterSystems HealthConnect Ensemble production (HC) that acts as a message transformation and routing system. TMP sends a JSON message to the TMP HC server. HC transforms the JSON to the appropriate HL7 message structure and routes the message to the correct VistA system. VistA responds by sending the appropriate HL7 message to HC where HC transforms the HL7 message to JSON and posts the response on the TMP Rest End Point.

# HL7 Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 messages formats used in the integration conform to the HL7 Version 2.4 standard, which includes use of the following:

- Message Type - Schedule Information Unsolicited (SIU)
- Message Structures - S12 for Schedule an appointment and an S15 for Cancel an appointment.

Additionally, TMP initiates an <u>HL7 query</u> to retrieve a patient’s list of consults and Return To Clinic (RTC) orders that are housed in VistA. These two lists are used by the schedulers to schedule appointments associated with specific consults and RTC orders.

VistA will also send out real time update messages to TMP to update TMP when appointments are scheduled or canceled for a tele health clinic. Tele health clinics are identified by either the Stop Code or the Credit Stop Code fields in the VistA Hospital Location file (#44). All real time update messages for make or cancel appointments use the same S12 and S15 message structure.

VistA will also send out a real time update when a tele health clinic is created, inactivated, reactivated or if the stop code or credit stop codes are modified. This real time update keeps the clinic information in sync between VistA and TMP.

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The scheduling messages contain only the data necessary to perform the scheduling action.
- The transmission of TMP HL7 appointment messages assumes all VistA systems have installed patch SD\*5.3\*704. This patch receives the HL7 messages from TMP and processes the appointment action.

## HL7/HLO Logical Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TMP_Send – An HLO link that is used to send the real time update messages from VistA to HealthConnect.

## HL7 Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| PROTOCOL                       | DESCRIPTION                                                                  |
|--------------------------------|------------------------------------------------------------------------------|
| SD IFS EVENT DRIVER            | Event driver protocol to send inter facility scheduling messages             |
| SD IFS SUBSCRIBER              | Subscriber protocol to process inter facility scheduling messages            |
| SD TMP RECEIVE CANCEL INTRA    | Event driver protocol to send intra facility scheduling messages             |
| SD TMP RECEIVE INTRAFACILITY   | Subscriber protocol to receive intra facility scheduling messages            |
| SD TMP S12 CLIENT SUBSCRIBER   | Subscriber protocol to receive make appointment scheduling messages from TMP |
| SD TMP S12 SERVER EVENT DRIVER | Event driver protocol for make appointment scheduling messages from TMP      |
| SD TMP S15 CLIENT SUBSCRIBER   | Subscriber protocol to receive cancel appointment scheduling messages        |
| SD TMP S15 SERVER EVENT DRIVER | Event driver protocol for cancel appointment scheduling messages             |
| SD TMP SEND CANCEL INTRA       | Event driver protocol for canceling intra facility appointment messages      |
| SD TMP SEND INTRAFACILITY      | Subscriber protocol for canceling intra facility appointment messages        |
| SD TMP SIU-12 SERVER           | Event driver protocol to send real time appointment messages to TMP          |
| SD TMP SIU-S12 CLIENT          | Subscriber protocol to send real time appointment messages to TMP            |
| TMP QBP-Q13 Event Driver       | Event driver for the get consults query message from TMP                     |
| TMP QBP-Q13 Subscriber         | Subscriber protocol for get consults query message from TMP                  |
| TMP RTB-K13 Event Drive        | Event driver protocol to return data for the get consults query from TMP     |
| TMP RTB-K13 Subscriber         | Subscriber protocol to return data for the get consults query from TMP       |

## HL7 Application Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| PARAMETERS                   | DESCRIPTION                                                                |
|------------------------------|----------------------------------------------------------------------------|
| SD TMP APPT RECEIVE          | Receiving application for the appointment messages from TMP                |
| SD TMP APPT SEND             | Sending application for the appointment messages from TMP                  |
| SD TMP IFS RECEIVE           | Receiving application for the inter facility scheduling messages           |
| SD TMP IFS SEND              | Sending application for the inter facility scheduling messages             |
| SD TMP RECEIVE CANCEL INTRA  | Receiving application for intra facility cancel appointment messages       |
| SD TMP RECEIVE INTRAFACILITY | Receiving application for intra facility make appointment messages         |
| SD TMP SEND CANCEL INTRA     | Sending application for intra facility cancel appointment messages         |
| SD TMP SEND INTRAFACILITY    | Sending application for intra facility make appointment messages           |
| SD-TMP-IN                    | Receiving application for real time appointment and clinic update messages |
| SD-TMP-OUT                   | Sending application for real time appointment and clinic update messages   |
| TMP GET CONSULTS             | Receiving application for get consult messages from TMP                    |
| TMP SEND CONSULTS            | Sending application for get consult messages from TMP                      |

## ## HL7 Message Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the HL7 messages used in the communications:

### Make and Cancel Appointment messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### SCH – Schedule Activity Information Segment

All scheduling messages used by TMP and VistA use the same structures for make and cancel appointments. The difference between make and cancel appointments is the message type on the MSH segment. Make appointments will be a SIU-S12 message and cancel appointments will be a SIU-S15 message.

In addition, Notification of Blocked Schedule Timeslot(s) and Notification of Opened (“un-blocked”) schedule time slot(s) are sent as SIU-S12 records. These records are differentiated by the ID information contained in field 25. The fields are used according to the definitions for S23 and S24 records.

The SCH segment contains general information about the scheduled appointment.

| SEQ | LEN | DT  | R/O/C | RP/# | TBL# | ITEM# | Element Name                 | VISTA DESCRIPTION                                            |
|-----|-----|-----|-------|------|------|-------|------------------------------|--------------------------------------------------------------|
| 1   | 75  | EI  | R     |      |      | 860   | Placer Appointment ID        | Not used/                                                    |
| 2   | 75  | EI  | C     |      |      | 861   | Filler Appointment ID        | Not used                                                     |
| 3   | 5   | NM  | C     |      |      | 862   | Occurrence Number            | VistA consult ID                                             |
| 4   | 22  | EI  | O     |      |      | 218   | Placer Group Number          | Not used                                                     |
| 5   | 250 | CE  | O     |      |      | 864   | Schedule ID                  | Not used                                                     |
| 6   | 250 | CE  | R     |      |      | 883   | Event Reason                 | Scheduled or Canceled                                        |
| 7   | 250 | CE  | O     |      |      | 866   | Appointment Reason           | Not used                                                     |
| 8   | 250 | CE  | O     |      |      | 867   | Appointment Type             | Not used                                                     |
| 9   | 20  | NM  | O     |      |      | 868   | Appointment Duration         | Appointment length                                           |
| 10  | 250 | CE  | O     |      |      | 869   | Appointment Duration Units   | Minutes or hours                                             |
| 11  | 200 | TQ  | R     | Y    |      | 884   | Appointment Timing Quantity  | ^^^Appointment Start Date Time^Appointment End Date Time     |
| 12  | 250 | XCN | O     | Y    |      | 874   | Placer Contact Person        | ^Provider Last Name^Provider First Name                      |
| 13  | 250 | XTN | O     |      |      | 875   | Placer Contact Phone Number  | ^^^Scheduler's VA exchange email                             |
| 14  | 250 | XAD | O     | Y    |      | 876   | Placer Contact Address       | Not used                                                     |
| 15  | 80  | PL  | O     |      |      | 877   | Placer Contact Location      | Not used                                                     |
| 16  | 250 | XCN | R     | Y    |      | 885   | Filler Contact Person        | Duz^name of person that scheduled the appointment            |
| 17  | 250 | XTN | O     |      |      | 886   | Filler Contact Phone Number  | Not used                                                     |
| 18  | 250 | XAD | O     |      |      | 887   | Filler Contact Address       | Not used                                                     |
| 19  | 80  | PL  | O     |      |      | 888   | Filler Contact Location      | Not used                                                     |
| 20  | 250 | XCN | R     | Y    |      | 878   | Entered by Person            | Free text scheduler name                                     |
| 21  | 250 | XTN | O     | Y    |      | 879   | Entered by Phone Number      |  Not Used                                                    |
| 22  | 80  | PL  | O     |      |      | 880   | Entered by Location          | Not used                                                     |
| 23  | 75  | EI  | O     |      |      | 881   | Parent Placer Appointment ID | Not used                                                     |
| 24  | 75  | EI  | O     |      |      | 882   | Parent Filler Appointment ID | Not used                                                     |
| 25  | 250 | CE  | R     |      |      | 889   | Filler Status Code           | Scheduled, Canceled, Non-Clinic Day or Cancel Non-Clinic Day |
| 26  | 22  | EI  | C     | Y    |      | 216   | PLACER ORDER NUMBER          | Not Used                                                     |
| 27  | 22  | EI  | C     | Y    |      | 217   | FILLER ORDER NUMBER          | Not Used                                                     |

#### PID – Patient information Segment

The PID segment has patient identification information.

| SEQ | LEN | DT  | OPT | RP/ \# | TBL \# | ITEM# | ELEMENT NAME                      | VistA Description                       |
|-----|-----|-----|-----|--------|--------|-------|-----------------------------------|-----------------------------------------|
| 1   | 4   | SI  | O   |        |        | 104   | Set ID - PID                      |  Not used                               |
| 2   | 20  | CX  | B   |        |        | 105   | Patient ID                        |  Not used                               |
| 3   | 250 | CX  | R   | Y      |        | 106   | Patient Identifier List           | Patient ICN^^^USAVHA^NI~DFN             |
| 4   | 20  | CX  | B   | Y      |        | 107   | Alternate Patient ID - PID        |  Not used                               |
| 5   | 250 | XPN | R   | Y      |        | 108   | Patient Name                      | Last Name^First Name^MI^^^^^L           |
| 6   | 250 | XPN | O   | Y      |        | 109   | Mother’s Maiden Name              |  Not used                               |
| 7   | 26  | TS  | O   |        |        | 110   | Date/Time of Birth                |  Patient Date of Birth                  |
| 8   | 1   | IS  | O   |        | 1      | 111   | Administrative Sex                |  Patient’s Gender                       |
| 9   | 250 | XPN | B   | Y      |        | 112   | Patient Alias                     |  Not used                               |
| 10  | 250 | CE  | O   | Y      | 5      | 113   | Race                              |  Not used                               |
| 11  | 250 | XAD | O   | Y      |        | 114   | Patient Address                   |  Not used                               |
| 12  | 4   | IS  | B   |        | 289    | 115   | County Code                       |  Not used                               |
| 13  | 250 | XTN | O   | Y      |        | 116   | Phone Number - Home               |  Not used                               |
| 14  | 250 | XTN | O   | Y      |        | 117   | Phone Number - Business           |  Not used                               |
| 15  | 250 | CE  | O   |        | 296    | 118   | Primary Language                  |  Not used                               |
| 16  | 250 | CE  | O   |        | 2      | 119   | Marital Status                    |  Not used                               |
| 17  | 250 | CE  | O   |        | 6      | 120   | Religion                          |  Not used                               |
| 18  | 250 | CX  | O   |        |        | 121   | Patient Account Number            |  Consult ID related to this appointment |
| 19  | 16  | ST  | B   |        |        | 122   | SSN Number - Patient              |  Not used                               |
| 20  | 25  | DLN | O   |        |        | 123   | Driver's License Number - Patient |  Not used                               |
| 21  | 250 | CX  | O   | Y      |        | 124   | Mother's Identifier               |  Not used                               |
| 22  | 250 | CE  | O   | Y      | 189    | 125   | Ethnic Group                      |  Not used                               |
| 23  | 250 | ST  | O   |        |        | 126   | Birth Place                       |  Not used                               |
| 24  | 1   | ID  | O   |        | 136    | 127   | Multiple Birth Indicator          |  Not used                               |
| 25  | 2   | NM  | O   |        |        | 128   | Birth Order                       |  Not used                               |
| 26  | 250 | CE  | O   | Y      | 171    | 129   | Citizenship                       |  Not used                               |
| 27  | 250 | CE  | O   |        | 172    | 130   | Veterans Military Status          |  Not used                               |
| 28  | 250 | CE  | B   |        | 212    | 739   | Nationality                       |  Not used                               |
| 29  | 26  | TS  | O   |        |        | 740   | Patient Death Date and Time       |  Not used                               |
| 30  | 1   | ID  | O   |        | 136    | 741   | Patient Death Indicator           |  Not used                               |
| 31  | 1   | ID  | O   |        | 136    | 1535  | Identity Unknown Indicator        |  Not used                               |
| 32  | 20  | IS  | O   | Y      | 445    | 1536  | Identity Reliability Code         |  Not used                               |
| 33  | 26  | TS  | O   |        |        | 1537  | Last Update Date/Time             |  Not used                               |
| 34  | 40  | HD  | O   |        |        | 1538  | Last Update Facility              |  Not used                               |
| 35  | 250 | CE  | C   |        | 446    | 1539  | Species Code                      |  Not used                               |
| 36  | 250 | CE  | C   |        | 447    | 1540  | Breed Code                        |  Not used                               |
| 37  | 80  | ST  | O   |        |        | 1541  | Strain                            |  Not used                               |
| 38  | 250 | CE  | O   | 2      | 429    | 1542  | Production Class Code             |  Not used                               |

#### PV1 – Patient Visit Segment

The PV1 segment has the patient visit information.

| SEQ | LEN | DT  | OPT | RP/# | TBL# | ITEM# | ELEMENT NAME              | VistA Description     |
|-----|-----|-----|-----|------|------|-------|---------------------------|-----------------------|
| 1   | 4   | SI  | O   |      |      | 131   | Set ID - PV1              |  Not used             |
| 2   | 1   | IS  | R   |      | 4    | 132   | Patient Class             |  Not used             |
| 3   | 80  | PL  | O   |      |      | 133   | Assigned Patient Location |  Not used             |
| 4   | 2   | IS  | O   |      | 7    | 134   | Admission Type            |  Not used             |
| 5   | 250 | CX  | O   |      |      | 135   | Preadmit Number           |  Not used             |
| 6   | 80  | PL  | O   |      |      | 136   | Prior Patient Location    |  Not used             |
| 7   | 250 | XCN | O   | Y    | 10   | 137   | Attending Doctor          |  Not used             |
| 8   | 250 | XCN | O   | Y    | 10   | 138   | Referring Doctor          |  Not used             |
| 9   | 250 | XCN | B   | Y    | 10   | 139   | Consulting Doctor         |  Not used             |
| 10  | 3   | IS  | O   |      | 69   | 140   | Hospital Service          |  Not used             |
| 11  | 80  | PL  | O   |      |      | 141   | Temporary Location        |  Not used             |
| 12  | 2   | IS  | O   |      | 87   | 142   | Preadmit Test Indicator   |  Not used             |
| 13  | 2   | IS  | O   |      | 92   | 143   | Re-admission Indicator    |  Not used             |
| 14  | 6   | IS  | O   |      | 23   | 144   | Admit Source              |  Not used             |
| 15  | 2   | IS  | O   | Y    | 9    | 145   | Ambulatory Status         |  Not used             |
| 16  | 2   | IS  | O   |      | 99   | 146   | VIP Indicator             |  Not used             |
| 17  | 250 | XCN | O   | Y    | 10   | 147   | Admitting Doctor          |  Not used             |
| 18  | 2   | IS  | O   |      | 18   | 148   | Patient Type              |  Not used             |
| 19  | 250 | CX  | O   |      |      | 149   | Visit Number              |  VistA Consult Id     |
| 20  | 50  | FC  | O   | Y    | 64   | 150   | Financial Class           |  Not used             |
| 21  | 2   | IS  | O   |      | 32   | 151   | Charge Price Indicator    |  Not used             |
| 22  | 2   | IS  | O   |      | 45   | 152   | Courtesy Code             |  Not used             |
| 23  | 2   | IS  | O   |      | 46   | 153   | Credit Rating             |  Not used             |
| 24  | 2   | IS  | O   | Y    | 44   | 154   | Contract Code             |  Not used             |
| 25  | 8   | DT  | O   | Y    |      | 155   | Contract Effective Date   |  Not used             |
| 26  | 12  | NM  | O   | Y    |      | 156   | Contract Amount           |  Not used             |
| 27  | 3   | NM  | O   | Y    |      | 157   | Contract Period           |  Not used             |
| 28  | 2   | IS  | O   |      | 73   | 158   | Interest Code             |  Not used             |
| 29  | 1   | IS  | O   |      | 110  | 159   | Transfer to Bad Debt Code |  Not used             |
| 30  | 8   | DT  | O   |      |      | 160   | Transfer to Bad Debt Date |  Not used             |
| 31  | 10  | IS  | O   |      | 21   | 161   | Bad Debt Agency Code      |  Not used             |
| 32  | 12  | NM  | O   |      |      | 162   | Bad Debt Transfer Amount  |  Not used             |
| 33  | 12  | NM  | O   |      |      | 163   | Bad Debt Recovery Amount  |  Not used             |
| 34  | 1   | IS  | O   |      | 111  | 164   | Delete Account Indicator  |  Not used             |
| 35  | 8   | DT  | O   |      |      | 165   | Delete Account Date       |  Not used             |
| 36  | 3   | IS  | O   |      | 112  | 166   | Discharge Disposition     |  Not used             |
| 37  | 25  | CM  | O   |      | 113  | 167   | Discharged to Location    |  Not used             |
| 38  | 250 | CE  | O   |      | 114  | 168   | Diet Type                 |  Not used             |
| 39  | 2   | IS  | O   |      | 115  | 169   | Servicing Facility        |  Not used             |
| 40  | 1   | IS  | B   |      | 116  | 170   | Bed Status                |  Not used             |
| 41  | 2   | IS  | O   |      | 117  | 171   | Account Status            |  Not used             |
| 42  | 80  | PL  | O   |      |      | 172   | Pending Location          |  Not used             |
| 43  | 80  | PL  | O   |      |      | 173   | Prior Temporary Location  |  Not used             |
| 44  | 26  | TS  | O   |      |      | 174   | Admit Date/Time           | Appointment Date/Time |
| 45  | 26  | TS  | O   | Y    |      | 175   | Discharge Date/Time       |  Not used             |
| 46  | 12  | NM  | O   |      |      | 176   | Current Patient Balance   |  Not used             |
| 47  | 12  | NM  | O   |      |      | 177   | Total Charges             |  Not used             |
| 48  | 12  | NM  | O   |      |      | 178   | Total Adjustments         |  Not used             |
| 49  | 12  | NM  | O   |      |      | 179   | Total Payments            |  Not used             |
| 50  | 250 | CX  | O   |      | 203  | 180   | Alternate Visit ID        |  Not used             |
| 51  | 1   | IS  | O   |      | 326  | 1226  | Visit Indicator           |  Not used             |
| 52  | 250 | XCN | B   | Y    | 10   | 1274  | Other Healthcare Provider |  Not used             |

#### RGS – Resource Group Segment

The RGS segment is the appointment grouper segment.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 24%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>OPT</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ITEM#</th>
<th>ELEMENT NAME</th>
<th>VISTA DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td> </td>
<td> </td>
<td>1203</td>
<td>Set ID - RGS</td>
<td>1</td>
</tr>
<tr class="even">
<td>2</td>
<td>3</td>
<td>ID</td>
<td>C</td>
<td> </td>
<td>206</td>
<td>763</td>
<td>Segment Action Code</td>
<td>A = Add/Insert<br />
D = Delete<br />
U = Update</td>
</tr>
<tr class="odd">
<td>3</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td> </td>
<td> </td>
<td>1204</td>
<td>Resource Group ID</td>
<td> Not used</td>
</tr>
</tbody>
</table>

#### AIS – Appointment Information Segment

The AIS segment contains information about the appointment.

| SEQ | LEN | DT  | OPT | RP/# | TBL# | ITEM# | ELEMENT NAME                            | VISTA DESCRIPTION                                                                          |
|-----|-----|-----|-----|------|------|-------|-----------------------------------------|--------------------------------------------------------------------------------------------|
| 1   | 4   | SI  | R   |      |      | 890   | Set ID - AIS                            |  Segment Sequence Numer                                                                    |
| 2   | 3   | ID  | C   |      | 206  | 763   | Segment Action Code                     | A=Add/Insert, D=Delete, U=Update, make appointment will be A, cancel appointment will be D |
| 3   | 250 | CE  | R   |      |      | 238   | Universal Service Identifier            |  ICD Code^Provisional Diagnosis                                                            |
| 4   | 26  | TS  | C   |      |      | 1202  | Start Date/Time                         | Appointment start date time in UTC                                                         |
| 5   | 20  | NM  | C   |      |      | 891   | Start Date/Time Offset                  |  Not used                                                                                  |
| 6   | 250 | CE  | C   |      |      | 892   | Start Date/Time Offset Units            |  Not used                                                                                  |
| 7   | 20  | NM  | O   |      |      | 893   | Duration                                | length of appointment                                                                      |
| 8   | 250 | CE  | O   |      |      | 894   | Duration Units                          | Not used                                                                                   |
| 9   | 10  | IS  | C   |      | 279  | 895   | Allow Substitution Code                 |  Not used                                                                                  |
| 10  | 250 | CE  | C   |      | 278  | 889   | Filler Status Code                      |  Not used                                                                                  |
| 11  | 250 | CE  | O   | Y    | 411  | 1474  | Placer Supplemental Service Information |  Not used                                                                                  |
| 12  | 250 | CE  | O   | Y    | 411  | 1475  | Filler Supplemental Service Information |  Not used                                                                                  |

#### AIG – Appointment Insurance Segment

<table style="width:100%;">
<colgroup>
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 19%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>OPT</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL#</strong></th>
<th><strong>ITEM#</strong></th>
<th><strong>ELEMENT NAME</strong></th>
<th><strong>VistA DATA ELEMENT</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td> </td>
<td> </td>
<td>896</td>
<td>Set ID - AIG</td>
<td>Segment Sequence Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>3</td>
<td>ID</td>
<td>C</td>
<td> </td>
<td>206</td>
<td>763</td>
<td>Segment Action Code</td>
<td>A = add,<br />
D = delete<br />
U = Update</td>
</tr>
<tr class="odd">
<td>3</td>
<td>250</td>
<td>CE</td>
<td>C</td>
<td> </td>
<td> </td>
<td>897</td>
<td>Resource ID</td>
<td>Provider Name</td>
</tr>
<tr class="even">
<td>4</td>
<td>250</td>
<td>CE</td>
<td>R</td>
<td> </td>
<td> </td>
<td>898</td>
<td>Resource Type</td>
<td>Provider </td>
</tr>
<tr class="odd">
<td>5</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td> </td>
<td>899</td>
<td>Resource Group</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>6</td>
<td>5</td>
<td>NM</td>
<td>O</td>
<td> </td>
<td> </td>
<td>900</td>
<td>Resource Quantity</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>7</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td> </td>
<td> </td>
<td>901</td>
<td>Resource Quantity Units</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>8</td>
<td>26</td>
<td>TS</td>
<td>C</td>
<td> </td>
<td> </td>
<td>1202</td>
<td>Start Date/Time</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>9</td>
<td>20</td>
<td>NM</td>
<td>C</td>
<td> </td>
<td> </td>
<td>891</td>
<td>Start Date/Time Offset</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>10</td>
<td>250</td>
<td>CE</td>
<td>C</td>
<td> </td>
<td> </td>
<td>892</td>
<td>Start Date/Time Offset Units</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>11</td>
<td>20</td>
<td>NM</td>
<td>O</td>
<td> </td>
<td> </td>
<td>893</td>
<td>Duration</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>12</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td> </td>
<td> </td>
<td>894</td>
<td>Duration Units</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>13</td>
<td>10</td>
<td>IS</td>
<td>C</td>
<td> </td>
<td><a href="file:///C:/Users/vhaistburkhw/Documents/cognosante/Scheduling%20Data%20Fields%20Mapping.xlsx#RANGE!HL70279"><u>279</u></a></td>
<td>895</td>
<td>Allow Substitution Code</td>
<td> Not used</td>
</tr>
<tr class="even">
<td>14</td>
<td>250</td>
<td>CE</td>
<td>C</td>
<td> </td>
<td><a href="file:///C:/Users/vhaistburkhw/Documents/cognosante/Scheduling%20Data%20Fields%20Mapping.xlsx#RANGE!HL70278"><u>278</u></a></td>
<td>889</td>
<td>Filler Status Code</td>
<td> Not used</td>
</tr>
</tbody>
</table>

#### AIL – Appointment Location Segment

The fields in the AIL segment are used in accordance with the S12, S23 and S24 records, depending on the ID information in the SCH segment.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 17%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SEQ</strong></th>
<th><strong>LEN</strong></th>
<th><strong>DT</strong></th>
<th><strong>OPT</strong></th>
<th><strong>RP/#</strong></th>
<th><strong>TBL#</strong></th>
<th><strong>ITEM#</strong></th>
<th><strong>ELEMENT NAME</strong></th>
<th><strong>VistA</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td> </td>
<td> </td>
<td>902</td>
<td>Set ID - AIL</td>
<td>Segment Sequence Number</td>
</tr>
<tr class="even">
<td>2</td>
<td>3</td>
<td>ID</td>
<td>C</td>
<td> </td>
<td>206</td>
<td>763</td>
<td>Segment Action Code</td>
<td>A = Add<br />
D=Cancel U=Update</td>
</tr>
<tr class="odd">
<td>3</td>
<td>80</td>
<td>PL</td>
<td>C</td>
<td> </td>
<td> </td>
<td>903</td>
<td>Location Resource ID</td>
<td>Consult Title</td>
</tr>
<tr class="even">
<td>4</td>
<td>250</td>
<td>CE</td>
<td>R</td>
<td> </td>
<td> </td>
<td>904</td>
<td>Location Type-AIL</td>
<td>Consult Title</td>
</tr>
<tr class="odd">
<td>5</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td> </td>
<td> </td>
<td>905</td>
<td>Location Group</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>6</td>
<td>26</td>
<td>TS</td>
<td>C</td>
<td> </td>
<td> </td>
<td>1202</td>
<td>Start Date/Time</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>7</td>
<td>20</td>
<td>NM</td>
<td>C</td>
<td> </td>
<td> </td>
<td>891</td>
<td>Start Date/Time Offset</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>8</td>
<td>250</td>
<td>CE</td>
<td>C</td>
<td> </td>
<td> </td>
<td>892</td>
<td>Start Date/Time Offset Units</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>9</td>
<td>20</td>
<td>NM</td>
<td>O</td>
<td> </td>
<td> </td>
<td>893</td>
<td>Duration</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>10</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td> </td>
<td> </td>
<td>894</td>
<td>Duration Units</td>
<td>Not used</td>
</tr>
<tr class="odd">
<td>11</td>
<td>10</td>
<td>IS</td>
<td>C</td>
<td> </td>
<td><a href="file:///C:/Users/vhaistburkhw/Documents/cognosante/Scheduling%20Data%20Fields%20Mapping.xlsx#RANGE!HL70279"><u>279</u></a></td>
<td>895</td>
<td>Allow Substitution Code</td>
<td>Not used</td>
</tr>
<tr class="even">
<td>12</td>
<td>250</td>
<td>CE</td>
<td>C</td>
<td> </td>
<td><a href="file:///C:/Users/vhaistburkhw/Documents/cognosante/Scheduling%20Data%20Fields%20Mapping.xlsx#RANGE!HL70278"><u>278</u></a></td>
<td>889</td>
<td>Filler Status Code</td>
<td>Not used</td>
</tr>
</tbody>
</table>

#### AIP – Appointment Provider Segment

| SEQ | LEN | DT | OPT | RP/# | TBL# | ITEM# | ELEMENT NAME             | VISTA DESCRIPTION                                |
|---------|---------|--------|---------|----------|----------|-----------|------------------------------|------------------------------------------------------|
| 1       | 4       | SI     | R       |          |          | 906       | Set ID - AIP                 |  Segment Sequence Number                             |
| 2       | 3       | ID     | C       |          | 206      | 763       | Segment Action code          | A=Add, D=Delete, U=Update                            |
| 3       | 250     | XCN    | C       | Y        |          | 913       | Personnel Resource ID        | Provider Duz^^Provider Last Name^Provider First Name |
| 4       | 250     | CE     | R       |          |          | 907       | Resource Role                |  Will be Provider                                    |
| 5       | 250     | CE     | O       |          |          | 899       | Resource Group               |  Not used                                            |
| 6       | 26      | TS     | C       |          |          | 1202      | Start Date/Time              |  Not used                                            |
| 7       | 20      | NM     | C       |          |          | 891       | Start Date/Time Offset       |  Not used                                            |
| 8       | 250     | CE     | C       |          |          | 892       | Start Date/Time Offset Units |  Not used                                            |
| 9       | 20      | NM     | O       |          |          | 893       | Duration                     |  Not used                                            |
| 10      | 250     | CE     | O       |          |          | 894       | Duration Units               |  Not used                                            |
| 11      | 10      | IS     | C       |          | 279      | 895       | Allow Substitution Code      |  Not used                                            |
| 12      | 250     | CE     | C       |          | 278      | 889       | Filler Status Code           |  Not used                                            |

### Get Consults Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TMP uses the QBP-Q13 message structure to request a list of patient consults and return to clinic orders. VistA responds to the query message with an RTB-K13 response message.

Get Consult Query Message from TMP to VistA

#### QPD – Query Parameter Definition Segment

The QPD segment defines the parameters for the query. It has the information to identify the patient and medical center to query.

| SEQ | LEN | DT | OPT | RP/# | TBL# | ITEM# | ELEMENT NAME   | VistA             |
|---------|---------|--------|---------|----------|----------|-----------|--------------------|-----------------------|
| 1       | 250     | CE     | R       |          | 471      | 1375      | Message Query Name | ControlId^TMP^HL7v2.4 |
| 2       | 32      | ST     | C       |          |          | 696       | Query Tag          | QueryName             |
| 3       | 30      | XCN    | R       |          |          | 1435      | Patient ID         | PatientDfn^PatientIcn |

#### RDF – Table Row Definition Segment

The RDF segment contains the list of requested data elements and the structure of the response message for the query.

| SEQ | LEN | DT | OPT | RP/# | TBL# | ITEM# | ELEMENT NAME          | VistA |
|---------|---------|--------|---------|----------|----------|-----------|---------------------------|-----------|
| 1       | 3       | NM     | R       |          |          | 701       | Number of Columns per Row |           |
| 2       | 30      | XCN    | R       |          |          | 1435      | Consult ID                |           |
| 3       | 26      | TS     | R       |          |          |           | Consult Date/Time         |           |
| 4       | 30      | XTN    | R       |          |          |           | Consulting Service        |           |
| 5       | 30      | XTN    | R       |          |          |           | Consult Title             |           |
| 6       | 30      | XTN    | R       |          |          |           | Clinically Indicated Date |           |
| 7       | 30      | XTN    | O       |          |          |           | Stop Codes                |           |
| 8       | 30      | XTN    | O       |          |          |           | Provider                  |           |
| 9       | 26      | XTN    | R       |          |          |           | Receiving Site Consult ID |           |

Get Consults Query Response Message from VistA to TMP

#### QAK – Query Acknowledgement Segment

The QAK segment contains information sent with the responses to the query.

| SEQ | LEN | DT | OPT | RP/# | TBL#                                                                                                                                     | ITEM# | ELEMENT NAME      | VistA                                      |
|---------|---------|--------|---------|----------|----------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------------|------------------------------------------------|
| 1       | 32      | ST     | C       |          |                                                                                                                                              | 696       | Query Tag             | Control ID from JSON                           |
| 2       | 2       | ID     | O       |          | [<u>208</u>](file:///J:/Business%20Intelligence%20Systems/TeleHealth/Consults%20Messaging/Get%20Consults%20HL7%20Message.xlsx#RANGE!HL70208) | 708       | Query Response Status | Table 208 in Chapter 5.                        |
| 3       | 250     | CE     | O       |          |                                                                                                                                              | 1375      | Message Query Name    | Name of the query from the QPD segment field 1 |
| 4       | 10      | NM     | O       |          |                                                                                                                                              | 1434      | Hit Count             | number of results                              |
| 5       | 10      | NM     | O       |          |                                                                                                                                              | 1622      | This payload          | number of results in this message              |
| 6       | 10      | NM     | O       |          |                                                                                                                                              | 1623      | Hits remaining        | not used                                       |

#### QPD – Query Parameters Definition Segment in the response.

The response to the query includes the QPD parameters from the original request.

| SEQ | LEN | DT | OPT | RP/# | TBL# | ITEM# | ELEMENT NAME   | JSON Tag          |
|---------|---------|--------|---------|----------|----------|-----------|--------------------|-----------------------|
| 1       | 250     | CE     | R       |          | 471      | 1375      | Message Query Name | ControlId^TMP^HL7v2.4 |
| 2       | 32      | ST     | C       |          |          | 696       | Query Tag          | QueryName             |
| 3       | 30      | XCN    | R       |          |          | 1435      | Patient ID         | PatientDfn^PatientIcn |

#### RDF – Table Row Definition Segment

The data on the RDF segment has the data as requested in the RDF segment in the original query message. The RDF segment is a repeating segment, one segment per consult or return to clinic order.

| SEQ | LEN | DT | OPT | RP/# | TBL# | ITEM# | ELEMENT NAME          | VistA                                         |
|---------|---------|--------|---------|----------|----------|-----------|---------------------------|---------------------------------------------------|
| 1       | 3       | NM     | R       |          |          | 701       | Number of Columns per Row |                                                   |
| 2       | 30      | XCN    | R       |          |          | 1435      | Consult ID                | Consult ID                                        |
| 3       | 26      | TS     | R       |          |          |           | Consult Date/Time         | Consult date/time                                 |
| 4       | 30      | XTN    | R       |          |          |           | Consulting Service        | Consulting service                                |
| 5       | 30      | XTN    | R       |          |          |           | Consult Title             | Consulting title                                  |
| 6       | 30      | XTN    | R       |          |          |           | Clinically Indicated Date | Clinically indicated date                         |
| 7       | 30      | XTN    | O       |          |          |           | Stop Codes                | Stop codes associated with the consult title      |
| 8       | 30      | XTN    | O       |          |          |           | Provider                  | Requesting Provider                               |
| 9       | 26      | XTN    | R       |          |          |           | Receiving Site Consult ID | remote site station number^remote site Consult ID |

### Real Time Clinic Update Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TMP sends a Master File MFN M05 message structure when a new clinic is added in VistA or if an existing clinic is inactivated or reactivate. The real time clinic update message is also generated when the default provider is edited, when the name of the clinic is edited, when either the stop code number or credit stop code is edited, when the treating specialty or service is edited or if the overbooks/day maximum is edited in the Hospital Location File (#44).

#### MFI – Master File Identification Segment

The MFI segment identifies the type of message.

| SEQ | LEN | DT | OPT | RP/# | TBL#                                                                                                                                                                    | ITEM# | ELEMENT NAME                   | VistA Data Element                                 |
|---------|---------|--------|---------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|------------------------------------|--------------------------------------------------------|
| 1       | 250     | CE     | R       |          | [<u>175</u>](file:///J:/Business%20Intelligence%20Systems/TeleHealth/Clinic%20Updates/Master%20File%20Clinic%20Update%20Message%20Segment%20Definitions.xlsx#RANGE!HL70175) | 658       | Master File Identifier             | IEN for the clinic in the Hospital Location File (#44) |
| 2       | 180     | HD     | O       |          |                                                                                                                                                                             | 659       | Master File Application Identifier | this will be set to 44^Hospital Location               |
| 3       | 3       | ID     | R       |          | [<u>178</u>](file:///J:/Business%20Intelligence%20Systems/TeleHealth/Clinic%20Updates/Master%20File%20Clinic%20Update%20Message%20Segment%20Definitions.xlsx#RANGE!HL70178) | 660       | File-Level Event Code              | UPD                                                    |
| 4       | 26      | TS     | O       |          |                                                                                                                                                                             | 661       | Entered Date/Time                  | Today's date/time in UTC format                        |
| 5       | 26      | TS     | O       |          |                                                                                                                                                                             | 662       | Effective Date/Time                | Today's date/time in UTC format                        |
| 6       | 2       | ID     | R       |          | [<u>179</u>](file:///J:/Business%20Intelligence%20Systems/TeleHealth/Clinic%20Updates/Master%20File%20Clinic%20Update%20Message%20Segment%20Definitions.xlsx#RANGE!HL70179) | 663       | Response Level Code                | This will be set to AL                                 |

#### MFE – Master File Entry Segment

The MFE segment has information to identify whether message is an add, update or deactivation of a clinic at the medical center.

| SEQ | LEN | DT | OPT | RP/# | TBL#                                                                                                                                                                    | ITEM# | ELEMENT NAME        | VistA Data Element                                                                                    |
|---------|---------|--------|---------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------|-----------------------------------------------------------------------------------------------------------|
| 1       | 3       | ID     | R       |          | [<u>180</u>](file:///J:/Business%20Intelligence%20Systems/TeleHealth/Clinic%20Updates/Master%20File%20Clinic%20Update%20Message%20Segment%20Definitions.xlsx#RANGE!HL70180) | 664       | Record-Level Event Code | This will be MAD for add, MUP for Update, MDC for deactivate, and MAC for reactivate a deactivated clinic |
| 2       | 20      | ST     | C       |          |                                                                                                                                                                             | 665       | MFN Control ID          | Clinic IEN from the Hospital Location file                                                                |
| 3       | 26      | TS     | O       |          |                                                                                                                                                                             | 662       | Effective Date/Time     | Date/time of the change in VistA in UTC format                                                            |
| 4       | 200     | Varies | R       | Y        |                                                                                                                                                                             | 667       | Primary Key Value - MFE | This is the IEN from the Hospital Location file for the new clinic or the edited clinic                   |
| 5       | 3       | ID     | R       | Y        | <u>355</u>                                                                                                                                                                  | 1319      | Primary Key Value Type  | This will always be CE                                                                                    |

#### LOC – Location Identification Segment

The LOC segment has location identification information.

| SEQ | LEN | DT | OPT | RP/# | TBL#                                                                                                                                                                    | ITEM# | ELEMENT NAME        | VistA Data Element                                           |
|---------|---------|--------|---------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------|------------------------------------------------------------------|
| 1       | 200     | PL     | R       |          |                                                                                                                                                                             | 1307      | Primary Key Value - LOC | IEN from the Hospital Location file                              |
| 2       | 48      | ST     | O       |          |                                                                                                                                                                             | 944       | Location Description    | Not Used                                                         |
| 3       | 2       | IS     | R       | Y        | [<u>260</u>](file:///J:/Business%20Intelligence%20Systems/TeleHealth/Clinic%20Updates/Master%20File%20Clinic%20Update%20Message%20Segment%20Definitions.xlsx#RANGE!HL70260) | 945       | Location Type - LOC     | Set to C                                                         |
| 4       | 250     | XON    | O       | Y        |                                                                                                                                                                             | 947       | Organization Name - LOC | This is the clinic name^institution number^^^visn&station number |
| 5       | 250     | XAD    | O       | Y        |                                                                                                                                                                             | 948       | Location Address        | Not Used                                                         |
| 6       | 250     | XTN    | O       | Y        |                                                                                                                                                                             | 949       | Location Phone          | Not Used                                                         |
| 7       | 250     | CE     | O       | Y        | [<u>461</u>](file:///J:/Business%20Intelligence%20Systems/TeleHealth/Clinic%20Updates/Master%20File%20Clinic%20Update%20Message%20Segment%20Definitions.xlsx#RANGE!HL70461) | 951       | License Number          | Not Used                                                         |
| 8       | 3       | IS     | O       | Y        | [<u>261</u>](file:///J:/Business%20Intelligence%20Systems/TeleHealth/Clinic%20Updates/Master%20File%20Clinic%20Update%20Message%20Segment%20Definitions.xlsx#RANGE!HL70261) | 953       | Location Equipment      | Not Used                                                         |
| 9       | 1       | IS     | O       |          | [<u>442</u>](file:///J:/Business%20Intelligence%20Systems/TeleHealth/Clinic%20Updates/Master%20File%20Clinic%20Update%20Message%20Segment%20Definitions.xlsx#RANGE!HL70442) | 1583      | Location Service Code   | Not Used                                                         |

#### LDP – Location Department Segment

The LDP segment has information for the location of the clinic to uniquely identify it from all other clinics in the VA.

| SEQ | LEN | DT | OPT | RP/# | TBL#                                                                                                                                                                    | ITEM# | ELEMENT NAME        | VistA Data Element                                                   |
|---------|---------|--------|---------|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-------------------------|--------------------------------------------------------------------------|
| 1       | 200     | PL     | R       |          |                                                                                                                                                                             | 963       | Primary Key Value - LDP | Clinic IEN from the Hospital Location file                               |
| 2       | 250     | CE     | R       |          | [<u>264</u>](file:///J:/Business%20Intelligence%20Systems/TeleHealth/Clinic%20Updates/Master%20File%20Clinic%20Update%20Message%20Segment%20Definitions.xlsx#RANGE!HL70264) | 964       | Location Department     | VISN^INSTITUTION NUMBER^STATION NUMBER                                   |
| 3       | 3       | IS     | O       | Y        | [<u>69</u>](file:///J:/Business%20Intelligence%20Systems/TeleHealth/Clinic%20Updates/Master%20File%20Clinic%20Update%20Message%20Segment%20Definitions.xlsx#RANGE!HL70069)  | 965       | Location Service        | From the Hospital Location file, Field \#9                               |
| 4       | 250     | CE     | O       | Y        | [<u>265</u>](file:///J:/Business%20Intelligence%20Systems/TeleHealth/Clinic%20Updates/Master%20File%20Clinic%20Update%20Message%20Segment%20Definitions.xlsx#RANGE!HL70265) | 966       | Specialty Type          | From the Hospital Location file, Field \#9.5                             |
| 5       | 1       | IS     | O       | Y        | 4                                                                                                                                                                           | 967       | Valid Patient Classes   |                                                                          |
| 6       | 1       | ID     | O       |          | 183                                                                                                                                                                         | 675       | Active/Inactive Flag    | If initial activation or a reactivation use 'A', if inactivation use 'I' |
| 7       | 26      | TS     | O       |          |                                                                                                                                                                             | 969       | Activation Date LDP     | Date of initial activation or reactivation in UTC format                 |
| 8       | 26      | TS     | O       |          |                                                                                                                                                                             | 970       | Inactivation Date - LDP | Date of inactivation in UTC format                                       |
| 9       | 80      | ST     | O       |          |                                                                                                                                                                             | 971       | Inactivated Reason      | Set to UNK since VistA doesn't store the inactivated reason.             |
| 10      | 80      | VH     | O       | Y        | [<u>267</u>](file:///J:/Business%20Intelligence%20Systems/TeleHealth/Clinic%20Updates/Master%20File%20Clinic%20Update%20Message%20Segment%20Definitions.xlsx#RANGE!HL70267) | 976       | Visiting Hours          | Clinic start time from the Hospital Location File                        |
| 11      | 250     | XTN    | O       |          |                                                                                                                                                                             | 978       | Contact Phone           | not used                                                                 |
| 12      | 250     | CE     | O       |          | [<u>462</u>](file:///J:/Business%20Intelligence%20Systems/TeleHealth/Clinic%20Updates/Master%20File%20Clinic%20Update%20Message%20Segment%20Definitions.xlsx#RANGE!HL70462) | 1584      | Location Cost Center    | Primary Stop Code^^Set to CLINIC STOP^Secondary Stop Code                |

#### ZPU – Local Privileged User Segment 

If the clinic is a restricted access clinic, the ZPU segment(s) will be populated. Each privileged user will be on a separated segment.

| SEQ | LEN | DT | OPT | RP/# | TBL# | ITEM# | ELEMENT NAME      | VistA Data Element                     |
|---------|---------|--------|---------|----------|----------|-----------|-----------------------|--------------------------------------------|
| 1       | 10      | NM     | R       |          |          |           | Set ID                |  Incremental number. Once segment per user |
| 2       | 200     | XCN    | R       |          |          |           | Privileged User Name  | New Person file, Field \#.01               |
| 3       | 200     | XCN    | O       |          |          |           | Privileged User eMail | New Person file, Field \#.151              |
| 4       | 25      | XCN    | O       |          |          |           | Privileged User VPID  | New Person file, Field \#9000              |

#### ZDP – Local Default Provider Segment

The ZDP segment has the default provider for the clinic location.

| SEQ | LEN | DT | OPT | RP/# | TBL# | ITEM# | ELEMENT NAME       | VistA Data Element        |
|---------|---------|--------|---------|----------|----------|-----------|------------------------|-------------------------------|
| 1       | 10      | NM     | R       |          |          |           | Set ID                 |                               |
| 2       | 250     | XCN    | R       |          |          |           | Default Provider Name  | New Person File, Field \#.01  |
| 3       | 250     | XCN    | O       |          |          |           | Default Provider eMail | New Person File, Field \#.151 |
| 4       | 25      | XCN    | O       |          |          |           | Default Provider VPID  | New Person File, Field \#9000 |

# VistA Data Dictionary Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TMP added two new style cross references to the VistA Patient File (#2). These two cross references, AX and AY, act as triggers to send the real time update messages to TMP when a new appointment is made, or an existing appointment is canceled and the appointment is for a tele health clinic. Tele health clinics are identified by the clinic stop code number or credit stop code.

<span id="_Toc14860785" class="anchor"></span>AX Cross Reference  
Triggers the update message when a new appointment is made.

AX    RECORD    MUMPS    IR    ACTION    WHOLE FILE (#2)

      Short Descr:  Action cross reference to send HL7 notification to TMP when

                    a new appt is made.

      Description:  The Tele Health Management Platform (TMP) application

                    allows users to schedule and cancel tele health

                    appointments in VistA. TMP needs to be kept up to date with

                    appointments scheduled by other applications in order to be

                    able to accurately display open appointment slots. This

                    index will trigger an HL7 message sent to TMP that will

                    update the clinic's and patient's appointments in the TMP

                    database system. 

        Set Logic:  D EN^SDTMPHLA(DA(1),DA)

         Set Cond:  S X=X1(1)=""

       Kill Logic:  Q

             X(1):  CLINIC  (2.98,.01)

         NO RE-INDEXING ALLOWED!

<span id="_Toc14860786" class="anchor"></span>AY Cross Reference  
  
Triggers the update message when an existing appointment is canceled.

  AY (#1521)    RECORD    MUMPS    IR    ACTION    WHOLE FILE (#2)

      Short Descr:  Action cross reference to send an HL7 notification when an

                    appt is cancelled.

      Description:  The Tele Health Management Platform (TMP) application

                    allows users to schedule and cancel tele health

                    appointments in VistA. TMP needs to be kept up to date with

                    appointments are cancelled by other applications in order

                    to be able to accurately display open appointment slots.

                    This index will trigger an HL7 message sent to TMP that

                    will update the clinic's and patient's appointments in the

                    TMP database system to reflect the cancellation. 

        Set Logic:  D EN^SDTMPHLA(DA(1),DA)

         Set Cond:  S X=X1(1)=""

       Kill Logic:  Q

             X(1):  STATUS  (2.98,3)

         NO RE-INDEXING ALLOWED!

<span id="_Toc14860787" class="anchor"></span>Style Cross Reference

TMP has also added a new style cross reference to the Hospital Location File (#44) that acts as a trigger to send an update message to TMP when a tele health clinic is edited in VistA. The cross-reference definition lists the fields that are monitored for changes.

              ATMP1    MUMPS    IR    ACTION

                  Short Descr:  TMP HL7

                  Description:  The Tele Health Management Platform (TMP)

                                application allows users to schedule and cancel

                                appointments in VistA.  TMP needs to be kept up

                                to date with specific clinic information in

                                order to be able to accurately display clinic

                                information. 

                                 

                                This index will trigger an update to be sent to

                                the TMP platform via HL7 when one of the fields

                                below is edited for a tele health clinic or if

                                a new tele health clinic is added. Tele health

                                clinics are identified by either the Stop Code

                                Number (primary stop code) or the Credit Stop

                                Code (secondary stop code). 

                                 

                                Name (#.01) Stop Code Number (#8) Credit Stop

                                Code (#2504) Service (#9) Treating Specialty

                                (#9.5) Overbooks/Day Maximum (#1918) Inactivate

                                Date (#2505) Reactivate Date (#2506). 

                    Set Logic:  D EN^SDTMPHLB(DA)

                    Set Cond:  S X=X1(1)'=""!X1(2)'=""!X1(3)'=""!X1(4)'=""!X1(

                                5)'=""!X1(6)'=""!X1(7)'=""!X1(8)'=""!X1(9)'=""

                   Kill Logic:  Q

                         X(1):  NAME  (44,.01)

                         X(2):  STOP CODE NUMBER  (44,8)

                         X(3):  CREDIT STOP CODE  (44,2503)

                         X(4):  TREATING SPECIALTY  (44,9.5)

                         X(5):  SERVICE  (44,9)

                         X(6):  DEFAULT PROVIDER  (44,16)

                         X(7):  OVERBOOKS/DAY MAXIMUM  (44,1918)

                         X(8):  INACTIVATE DATE  (44,2505)

                         X(9):  REACTIVATE DATE  (44,2506)

         NO RE-INDEXING ALLOWED!

## HOSPITAL LOCATION FILE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TMP added a field to the HOSPITAL LOCATION FILE (#44) in the APPOINTMENT Sub File (#400.03) to store the Uniform Resource Locator (URL) for the Veteran’s Video Call. The capture below shows just the field description, not the full data dictionary for the APPOINTMENT Sub File.

Using FileMan:

Select DATA DICTIONARY UTILITY OPTION: LIST FILE ATTRIBUTES

START WITH What File: HOSPITAL LOCATION// (424 entries)

GO TO What File: HOSPITAL LOCATION// (424 entries)

Select SUB-FILE: APPOINTMENT

Select SUB-FILE:

Select LISTING FORMAT: STANDARD//

Start with field: FIRST// .01 APPOINTMENT DATE/TIME

Go to field:

DEVICE: ;;1000 TELNET PORT Right Margin: 80//

STANDARD DATA DICTIONARY \#44.001 -- APPOINTMENT SUB-FILE 7/24/19 PAGE 1

STORED IN ^SC(D0,"S", SITE: VEHU MASTER UCI: TEST,ROU

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

-----------------------------------------------------------------------------

44.003,400 VETERAN VIDEO CALL URL URL;1 FREE TEXT

INPUT TRANSFORM:K:\$L(X)\>200!(\$L(X)\<3) X

MAXIMUM LENGTH: 200

LAST EDITED: OCT 30, 2018

HELP-PROMPT: Answer must be 3-200 characters in length.

## SD TELE HEALTH STOP CODE FILE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TMP also created a new VistA file, SD TELE HEALTH STOP CODE FILE (#40.6). This file stores the list of valid tele health stop codes. The file is used to determine if the clinic is a tele health clinic when the real times are triggered by one of the new style cross references described above. This file is installed pre-populated with the current list of tele health stop codes at the time the patch was released.

STANDARD DATA DICTIONARY \#40.6 -- SD TELE HEALTH STOP CODE FILE FILE 7/24/19

PAGE 1

STORED IN ^SD(40.6, (34 ENTRIES) SITE: VEHU MASTER UCI: TEST,ROU (VERSION 5

.3)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

-------------------------------------------------------------------------------

This file stores the list of current tele health stop codes. The Tele Health

Management Platform (TMP) uses this file to identify tele health clinics as

part of the TMP real time updates. TMP is monitoring the Hospital Location File

(#44) for edits to tele health clinics. These edits are sent to TMP in real

time in order to keep TMP in sync with each VistA system.

DD ACCESS: @

RD ACCESS: @

WR ACCESS: @

DEL ACCESS: @

LAYGO ACCESS: @

AUDIT ACCESS: @

CROSS

REFERENCED BY: STOP CODE NUMBER(B)

LAST MODIFIED: JUL 19,2019@02:30:01

40.6,.01 STOP CODE NUMBER 0;1 FREE TEXT (Required)

INPUT TRANSFORM: K:\$L(X)\>9!(\$L(X)\<3)!'(X'?1P.E) X

MAXIMUM LENGTH: 9

LAST EDITED: JAN 07, 2019

HELP-PROMPT: Enter the 3 to 9 digit stop code number.

DESCRIPTION: This is the stop code number from the Clinic

Stop File (#40.7).

CROSS-REFERENCE: 40.6^B

1)= S ^SD(40.6,"B",\$E(X,1,30),DA)=""

2)= K ^SD(40.6,"B",\$E(X,1,30),DA)

INPUT TEMPLATE(S):

PRINT TEMPLATE(S):

SORT TEMPLATE(S):

FORM(S)/BLOCK(S):

As stop codes change over time, it may be necessary to edit this file to add new tele health stop codes. This patch installs a new Option, SD EDIT TELE HEALTH STOP CODES to be used to edit this file.

Select OPTION NAME: SD EDIT TELE HEALTH STOP

Enter Stop Code: 680 <span class="mark">\<- Enter a valid stop code. The stop code must be in the CLINIC STOP FILE (#40.7)</span>

Do you want to edit another stop code? NO//

To delete an existing stop code from the file:

Select OPTION NAME: SD EDIT TELE HEALTH STOP CODES

Enter Stop Code: 680

This stop code is already in the file, do you want to delete it? NO// YES

Do you want to edit another stop code? NO//

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When VistA initiates the message, VistA sends the HL7 message to HC, HC transforms the HL7 message to the appropriate JSON message and posts the JSON on the TMP Rest End Point.

| Issue                                                                           | Action                                                                                                    | Resolve By                                                       |
|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| Messages are not flowing at all                                                 | Check that both the VistA HL7 and HLO listeners are started and the TMP_Send HL7 Logical Link is started. | Start the listeners                                              |
| Messages are not flowing from VistA to TMP for the real time updates            | Check the VistA HL7 and HLO listeners and the TMP_Send HL7 Logical Link is started.                       | Start the listeners                                              |
| If the listeners are started but VistA is still not receiving messages from TMP | Contact the VA HealthShare support team.                                                                  | Asking the VA HealthShare to troubleshoot the TMP HC Production. |