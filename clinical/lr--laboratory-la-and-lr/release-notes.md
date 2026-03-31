---
consolidated_title: "laboratory release notes"
app_code: LR
doc_type: RN
master_source: "LA*5.2*68 Laboratory Release Notes"
master_pub_date: July 2010
consolidated_from: 3 versions
prior_versions:
  - "LR*5.2*395 Laboratory Release Notes"
  - "LR*5.2*465 Laboratory Release Notes"
---

![](la-5-2-68-laboratory-release-notes/001.png)

Lab-VA HDR and COTS Interface  
Release Notes  
for Patch LA\*5.2\*68

July 2010

VistA Health Systems Design & Development

# Release Notes for Patch LA\*5.2\*68


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Release Notes for Patch LA\5.2\68](#release-notes-for-patch-la5268)
  - [Health Data Repository](#health-data-repository)
    - [## Blood Bank Clearance](#blood-bank-clearance)
- [Patch LA\5.2\68 Enhancements](#patch-la5268-enhancements)
  - [Enhancements/New](#enhancementsnew)
  - [Enhancements/Modifications](#enhancementsmodifications)
  - [Enhancements/Remedy Tickets](#enhancementsremedy-tickets)
Patch LA\*5.2\*68 supports the VA Health Data Repository (HDR) effort, by allowing changes to the VistA Laboratory LAB DATA file (#63) to be transmitted to the HDR and Commercial Off the Shelf (COTS) subscribers using a VistA Laboratory HL7 result (ORU) message. This patch includes additional enhancements, Remedy tickets, and modifications to the existing Laboratory software.
Patch LA\*5.2\*68 allows the HL7 ORU message containing patient laboratory results to be transmitted to the subscribers of the HL7 event protocol LA7 Lab Results Available (EVN), as these results are made available within the Laboratory package. This event supports subscripts: CH, MI, SP, CY, and EM.
| VistA Laboratory Subscript | Traditional Functional Sections                                |
|----------------------------|----------------------------------------------------------------|
| CH                         | Chemistry, Hematology, Coagulation, Serology, Urinalysis, etc. |
| MI                         | Microbiology, Virology, Mycology, Parasitology                 |
| SP                         | Surgical Pathology                                             |
| CY                         | Cytopathology                                                  |
| EM                         | Electron Microscopy                                            |

## Health Data Repository

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Patch LA*5.2*68 allows the HL7 ORU message containing patient laboratory results to be transmitted to the subscriber, LA7 LAB RESULTS TO HDR (SUB). This subscriber protocol is used to transmit laboratory results to the VA HDR.</p>
<ul>
<li><p>After you activate sending messages to the HDR, extracting existing laboratory data (HDR historical) will follow, so that there will be an overlap with no gaps of laboratory data within the HDR.</p></li>
<li><p>Once you activate sending messages to the HDR, do not inactivate, as this can cause gaps of laboratory data within the HDR.</p></li>
<li><p>If you must inactivate sending messages to the HDR, contact the HDR program office, so that the laboratory data can be tracked and recovered.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### ## Blood Bank Clearance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>VISTA Laboratory Package patch LA*5.2*68 contains changes to software controlled by VHA DIRECTIVE 99-053, titled VISTA BLOOD BANK SOFTWARE. Changes include:</p>
<p>New style indexes have been created for the following sub-files</p>
<p>of the LAB DATA file (#63):</p>
<p>ELECTRON MICROSCOPY (#63.02)</p>
<p>SURGICAL PATHOLOGY (#63.08)</p>
<p>CYTOPATHOLOGY (#63.09)</p>
<p>All of the above changes have been reviewed by the VISTA Blood Bank Developer and found to have no impact on the VISTA BLOOD BANK SOFTWARE control functions.</p>
<p>RISK ANALYSIS: Changes made by patch LA*5.2*68 have no effect on Blood Bank software functionality, therefore RISK is none.</p>
<p>EFFECT ON BLOOD BANK FUNCTIONAL REQUIREMENTS: <strong>P</strong>atch LA*5.2*68 does not alter or modify any software design safeguards or safety critical elements functions.</p>
<p>POTENTIAL IMPACT ON SITES: This patch contains changes to 0 routines and 1 file identified in Veterans Health Administration (VHA) Directive 99-053, group B listing. The changes have no effect on Blood Bank functionality or medical device control functions. There is no adverse potential to sites.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Patch LA\*5.2\*68 Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LA\*5.2\*68 adds enhancements–new, modifications, and Remedy tickets, to the existing Laboratory software.

## Enhancements/New

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The following protocols are added to the PROTOCOL file (#101).

NAME: LA7 LAB RESULTS ACTION

ITEM TEXT: Lab process results for HL7 messaging

TYPE: action

PACKAGE: AUTOMATED LAB INSTRUMENTS

DESCRIPTION: Action protocol to setup sending lab results to HL7 message subscribers via protocol LA7 LAB RESULTS AVAILABLE (EVN) - Lab Results Available Event. This protocol should be attached to protocol LAB RESULTS =\> EXTERNAL PACKAGE \[LR7O ALL EVSEND RESULTS\] which is an extended action protocol triggered by the lab result verification process.

ENTRY ACTION: D QUEUE^LA7HDR TIMESTAMP: 59056,40855

NAME: LA7 LAB RESULTS AVAILABLE (EVN) ITEM TEXT: Lab Results Available Event

TYPE: event driver CREATOR: LDSICREATOR,ONE

DESCRIPTION: A VistA Laboratory package HL7 ORU result message is created and sent by the HL package for transmission to any subscribers of event protocol LA7 LAB RESULTS AVAILABLE (EVN).

It provides the capability for the generation of a Laboratory HL7 ORU message containing patient laboratory results to subscribers of the HL7 event protocol LA7 LAB RESULTS AVAILABLE (EVN) as these results are made available within the Laboratory package.

The following subscripts are supported by the event: CH, MI, SP, CY, and EM.

TIMESTAMP: 59725,36770 SENDING APPLICATION: LA7LAB

TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

MESSAGE STRUCTURE: ORU_R01 ACCEPT ACK CODE: AL

APPLICATION ACK TYPE: NE VERSION ID: 2.4

RESPONSE PROCESSING ROUTINE: D ACK^LA7VHL

> SUBSCRIBERS: LA7 LAB RESULTS TO HDR (SUB)

NAME: LA7 LAB RESULTS TO HDR (SUB) ITEM TEXT: Send Lab Results to HDR

TYPE: subscriber CREATOR: LDSICREATOR,ONE

DESCRIPTION: This protocol should be attached to the HL7 event protocol LA7 LAB RESULTS AVAILABLE (EVN). See this protocol for further information.

This subscriber protocol is used by the Laboratory package to indicate to the HL package to send laboratory results to the VA Health Data Repository (HDR).

It utilizes the "Router" Subscriber Protocol supported by the VistA HL package. The routing logic uses the value of the parameter passed into the router to determine which Laboratory package subscript should be sent to the HDR.

> Examples

> ROUTING LOGIC: D RTR^LA7HDR("CH;") will only send to HDR results

> associated with Laboratory "CH" subscript.

> ROUTING LOGIC: D RTR^LA7HDR("MI;") will only send to HDR results

> associated with Laboratory "MI" subscript.

> ROUTING LOGIC: D RTR^LA7HDR("CH;MI;SP;") will only send to HDR results

> associated with Laboratory "CH", "MI", and "SP" subscripts.

TIMESTAMP: 59056,40125 RECEIVING APPLICATION: LA7HDR

EVENT TYPE: R01 LOGICAL LINK: VDEFVIE4

RESPONSE MESSAGE TYPE: ACK SENDING FACILITY REQUIRED?: YES

RECEIVING FACILITY REQUIRED?: YES ROUTING LOGIC: D RTR^LA7HDR("CH;")

> **NOTE:** This subscriber protocol is distributed with the Routing Logic disabled. See post-installation instructions for guidance to enable the protocol.

2.  The LA7 HDR Recover option is added to the OPTION file (#19).

NAME: LA7 HDR RECOVER MENU TEXT: Recover/Transmit Lab

HDR Result Messages

TYPE: run routine CREATOR:LDSICREATOR,ONE  
PACKAGE: AUTOMATED LAB INSTRUMENTS

DESCRIPTION: Option to recover from failed Lab HDR ORU Result message generation and/or transmission failure. This option allows the user to select those VistA Laboratory accessions that need to be transmitted to the VA HDR and other subscribers of the VistA Laboratory Result Available HL7 message capability via the protocol Lab Results Available Event \[LA7 LAB RESULTS AVAILABLE (EVN)\].

If the original message generation/transmission failed due to system or communication problems then using this option will allow the generation of new HL7 messages with the results associated with the selected accessions. Accessions can be selected using the human-readable accession designation (area abbreviation modified date accession number - "CH 1225 100") or the accession's associated 10 character unique identifier (UID)

ROUTINE: RECOVER^LA7HDR

UPPERCASE MENU TEXT: RECOVER/TRANSMIT LAB HDR RESUL

This option is assigned to the Lab liaison menu option \[LRLIAISON\] and can be assigned as needed to support/monitor message transmsission to the VA HDR and other subscribers.

## Enhancements/Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  When the configuration LA7HDR in LA7 MESSAGE PARAMETER file (#62.48) has an active status, the LA7HDR routine queues the record for transmission to the HDR via a HL7 ORU result message, which is transmitted by the HL package to any subscribers of event protocol, LA7 LAB RESULTS AVAILABLE (EVN), as well as to the HDR subscriber, LA7 LAB RESULTS TO HDR (SUB).

    The LA7 LAB RESULTS TO HDR (SUB) subscriber protocol uses the logical link VDEFVIE4. This is a router subscriber protocol that determines which Lab HL7 ORU messages are sent to the HDR.
3.  Anatomic Pathology is not *CPRS-aware* and is unable to notify CPRS of release of anatomic pathology results. HDR is notified of availability of anatomic pathology results via three new style cross-references in LAB DATA file (#63). When this capability is enabled, these indices also trigger generation of a Lab HL7 ORU message.
1.  Subfile \#63.02 – new style indices

AC (#98) FIELD MUMPS ACTION

Short Descr: Notify HDR and others that this report is available.

Description: This MUMPS cross-reference triggers the sending of this

report to the Health Data Repository (HDR) and other

subscribers when electron microscopy results are released.

Set Logic: D APQ^LA7HDR(DA(1),"EM",DA)

Kill Logic: Q

X(1): REPORT RELEASE DATE (63.02,.11) (Subscr 1) (forwards)

1.  Subfile \#63.08 – new style indices

AD (#95) FIELD MUMPS ACTION

Short Descr: Notify HDR and others that this report is available.

Description: This MUMPS cross-reference triggers the sending of this

report to the Health Data Repository (HDR) and other

subscribers when surgical pathology results are released.

Set Logic: D APQ^LA7HDR(DA(1),"SP",DA)

Kill Logic: Q

X(1): REPORT RELEASE DATE/TIME (63.08,.11) (Subscr 1)

(forwards)

2.  Subfile \#63.09 – new style indices

AD (#96) FIELD MUMPS ACTION

Short Descr: Notify HDR and others that this report is available.

Description: This MUMPS cross-reference triggers the sending of this

report to the Health Data Repository (HDR) and other

subscribers when cytopathology results are released.

Set Logic: D APQ^LA7HDR(DA(1),"CY",DA)

Kill Logic: Q

X(1): REPORT RELEASE DATE/TIME (63.09,.11) (Subscr 1)

(forwards)

4.  The current Laboratory package does not support LOINC encoding of microbiology results. A default encoding is enabled for LOINC encode of standard microbiology tests and antibiotics. LOINC codes valid as of version 2.14.

> There is default mapping of NLT/LOINC codes to standard fields within the MICROBIOLOGY file (#5) multiple of LAB DATA file (#63) .

Test Order NLT Result NLT LOINC Code

Bacteriology report (#11) 87993.0000

Gram stain (#11.6) 87993.0000 87754.0000 664-3

Bacteriology organism (#12) 87993.0000 87570.0000 11475-1

Bacteria colony count (#12,1) 87719.0000 564-5

Parasite report (#14) 87505.0000

Parasite organism (#16) 87505.0000 87576.0000 17784-0

Mycology report (#18) 87994.0000

Fungal organism (#20) 87994.0000 87578.0000 580-1

Fungal colony count (#20,1) 87994.0000 87723.0000 19101-5

Mycobacterium report (#22) 87995.0000

Acid Fast stain (#24) 87995.0000 87756.0000 11545-1

Acid Fast stain quantity (#25) 87995.0000 87583.0000 11545-1

Mycobacterium organism (#26) 87995.0000 87589.0000 543-9

Mycobacterium colony count (#26,1) 87995.0000 87719.0000 564-5

Virology report (#33) 87996.0000

Viral agent (#36) 87996.0000 87590.0000 6584-7

> Bacteriology or mycobacterium (TB) organism's susceptibilities are based on a local site's mapping of National VA Lab Code field (#64) in ANTIMICROBIAL SUSCEPTIBILITY file (#62.06) and the related default LOINC code associated with this VA NLT code.

> Use the Map/Unmap Antimicrobial Default LOINC Code \[LR LOINC MAP ANTIMICROBIAL\] option to configure the default LOINC code for each antibiotic.

5.  The current Laboratory package does not support LOINC encoding of surgical pathology results. LOINC codes valid as of version 2.14.

> There is default mapping of NLT/LOINC codes to standard fields within the SURGICAL PATHOLOGY (#8) multiple of LAB DATA file (#63).

Test Order NLT Result NLT LOINC Code

Specimen (#.012) 88515.0000 88539.0000 22633-2

Brief clinical history (#.013) 88515.0000 88542.0000 22636-5

Preoperative diagnosis (#.014) 88515.0000 88544.0000 10219-4

Operative findings (#.015) 88515.0000 88546.0000 10215-2

Postoperative diagnosis (#.016) 88515.0000 88547.0000 10218-6

Gross description (#1) 88515.0000 88549.0000 22634-0

Microscopic description (#1.1) 88515.0000 88563.0000 22635-7

Frozen section (#1.3) 88515.0000 88569.0000 22635-7

Surgical path diagnosis (#1.4) 88515.0000 88571.0000 22637-3

Supplementary report (#1.2) 88515.0000 88589.0000 22639-9

Specimen weight (#2) 88515.0000 81233.0000 3154-2

6.  The current Laboratory package does not support LOINC encoding of cytopathology results. LOINC codes valid as of version 2.14.

> There is default mapping of NLT/LOINC codes to standard fields within the CYTOPATHOLOGY (#9) multiple of LAB DATA file (#63).

Test Order NLT Result NLT LOINC Code

Specimens (#.012) 88593.0000 88539.0000 22633-2

Brief clinical history (#.013) 88593.0000 88542.0000 22636-5

Preoperative diagnosis (#.014) 88593.0000 88544.0000 10219-4

Operative findings (#.015) 88593.0000 88542.0000 10215-2

Postoperative diagnosis (#.016) 88593.0000 88547.0000 10218-6

Gross description (#1) 88593.0000 88549.0000 22634-0

Microscopic examination (#1.1) 88593.0000 88563.0000 22635-7

Supplementary report (#1.2) 88593.0000 88589.0000 22639-9

Cytopatholgy diagnosis (#1.4) 88593.0000 88571.0000 22637-3

7.  The current Laboratory package does not support LOINC encoding of electron microscopy.

> There is default mapping of NLT/LOINC codes to standard fields within the EM (#2) multiple of LAB DATA file (#63).

Test Order NLT Result NLT LOINC Code

Specimens (#.012) 88597.0000 88057.0000 22633-2

Brief clinical history (#.013) 88597.0000 88542.0000 22636-5

Preoperative diagnosis (#.014) 88597.0000 88544.0000 10219-4

Operative findings (#.015) 88597.0000 88542.0000 10215-2

Postoperative diagnosis (#.016) 88597.0000 88547.0000 10218-6

Gross description (#1) 88597.0000 88549.0000 22634-0

Microscopic examination (#1.1) 88597.0000 88563.0000 22635-7

Supplementary report (#1.2) 88597.0000 88589.0000 22639-9

EM diagnosis (#1.4) 88597.0000 88571.0000 22637-3

8.  This patch converts several FileMan DBS calls on INSTITUTION file (#4) to use the supported APIs, \$\$NS^XUAF4 and \$\$STA^XUAF4.
9.  To integrate the VistA-Office EHR with the regular VistA system, as well as add functionality available in the Indian Health Services system, the GQPR^LA7QRY API was modified to allow for VistA-Office EHR to use data geared specifically toward clinical operations, whether in a hospital or a stand alone clinic.
- The use of an Electronic Health Record number is supported as a patient identifier that the API accepts.
- The entry point, GCPR^LA7QRY, remains unchanged. However the parameter used to pass the patient identifier contains a second piece indicating the type of identifier contained in the first piece.
- This API supports three types of patient identifiers.
1.  SS= Social Security number
2.  PI = VA MPI Integration Control Number
3.  MR= medical record number of patient in file PATIENT/IHS (#9000001)

> **NOTE:** Regular VistA users will not see this modification.

10. To support HDR-Historical, which uses the GRPR^LA7QRY API to extract historical laboratory test results, the input parameter, LA7SC to GCPR^LA7QRY, supports a second piece. When the second piece of input parameter LA7SC equals 1, the API returns results encoded using VUIDs, when available.
11. This patch corrects a defect identified during patch development with processing input parameters for the GCPR^LA7QRY API. When the input parameter LA7SC identifies specific subscripts for which to search, the API searches those subscripts for any search code, even when specific search codes are passed to the API in the LA7SC array.
12. This patch corrects a defect identified during patch development with processing input parameters for the GCPR^LA7QRY API. When the input parameters, LA7SDT and LA7EDT, identify specific results for an available date range, the API returns anatomic pathology results that were not released. This API was corrected to check the Report Release Date field (#.11) for subscripts CY, EM, and SP.
13. This patch corrects a defect identified by MyHeatheVet, related to the encoding of four fields in the OBR segment for anatomic pathology reports.
1.  OBR-32 - Principal result interpreter
3.  OBR-33 - Assistant result interpreter
4.  OBR-34 – Technician
5.  OBR-35 - Transcriptionist

> The name component of these fields was encoded with the wrong HL7 delimiter (component separator). The name component is now encoded with the subcomponent separator per the HL7 standard.

## Enhancements/Remedy Tickets 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Remedy ticket HD0000000096207 reported a problem with the error code returned by the Lab API, LA7QRY. A FileMan DBS error code was erroroneously returned to the calling application.
- Routines, LA7QRY, LA7QRY1, and LA7QRY2 were modified to use a different namespaced variable,LA7QERR, to return to the calling application any error conditions.
- Routine LA7VOBX1 was modified to use another namespaced variable, LA7DDERR, to handle FileMan DBS error conditions related to FileMan data dictionary calls.
14. Remedy tickets HD0000000141922 and HD0000000148089 reported a problem: failure to generate the MailMan bulletin,LA7 ORDER STATUS CHANGED, at the *collection* laboratory facility.  
      
    Routine LA7VMSG1 was changed to set the interface type of the flag in the Lab HL7 ORU message indicating an order status change to trigger the generation of the bulletin at the collection site.