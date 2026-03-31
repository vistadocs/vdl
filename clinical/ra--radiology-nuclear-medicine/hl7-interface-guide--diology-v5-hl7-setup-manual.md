---
title: Radiology Version 5 HL7 Setup Manual
doc_type: INT
doc_label: Interface Specification
doc_layer: anchor
doc_subject: HL7 Setup Manual
app_code: RA
app_name: Radiology/Nuclear Medicine
section: CLI
app_status: active
pkg_ns: RA
patch_ver: 5
patch_id: RA*5
group_key: "RA:RA:5"
file_numbers: 
  - 78
  - 79
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - message
  - report
  - event
  - vista
  - link
  - interface
  - application
  - radiology
  - cots
  - protocol
page_count: 0
word_count: 24182
section_count: 33
table_count: 5
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2000
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med/ra5_0hl7.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med/ra5_0hl7.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=98"
---

![](radiology-version-5-hl7-setup-manual/001.png)

Radiology/Nuclear Medicine 5.0  
  
HL7 Setup/Implementation Manual  
  

July 2000

Revised for  
Patch RA\*5.0\*144

March 2018

Health Systems Design and Development  
Provider Systems

Revision History

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 11%" />
<col style="width: 61%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Change</th>
<th>Page</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2000</td>
<td>1.0</td>
<td>Initial version of this document</td>
<td></td>
</tr>
<tr class="even">
<td>February 2007</td>
<td>2.0</td>
<td><p>Fully updated to include current functionality</p>
<p>Document reformatted to meet current Documentation Standards</p></td>
<td></td>
</tr>
<tr class="odd">
<td>May 2009</td>
<td>3.0</td>
<td><p>For Patch RA*5*78:</p>
<ul>
<li><p>Added <strong>Legacy</strong> to the heading</p></li>
<li><p>Added <strong>Legacy</strong> to the heading</p></li>
<li><p>Added <strong>Legacy</strong> to the heading</p></li>
<li><p>Added a section for TCP/IP Optimized HL7 Interfaces</p></li>
<li><p>Refer to the HL7 Message Specifications document for more information on the structure of these v2.3 HL7 query and response messages</p></li>
<li><p>Assuming that patch HL*1.6*139 is released when RA*5.0*78 is released. Naturally, the VistA Health Level Seven application should be fully patched</p></li>
<li><p>Points 2 and 3 reference the double-headed arrow in the diagram</p></li>
<li><p>Specific IP Port numbers for NTP: <strong>21999</strong> as the required TCP/IP PORT field value and <strong>21998</strong> as the required TCP/IP PORT (OPTIMIZED) field value</p></li>
<li><p>Body means that all HL7 segments are stored, except the MSH (Message Header) segment</p></li>
<li><p>Header means that the only HL7 segment stored, is the MSH (Message Header) segment</p></li>
</ul></td>
<td><p><a href="#_Ref221675367">3</a></p>
<p><a href="#_Ref257282710">13</a></p>
<p><a href="#_Ref221675403">23</a></p>
<p>93</p>
<p>93</p>
<p>93</p>
<p>94</p>
<p>96</p>
<p>98</p>
<p>98</p></td>
</tr>
<tr class="even">
<td>August 2011</td>
<td>4.0</td>
<td><p>Patch RA*5*47</p>
<ul>
<li><p>Added the name of the updated HL7 Specification for v2.4</p></li>
<li><p>Added an example message for HL7 v2.4</p></li>
<li><p>Added an example message for HL7 v2.4, single procedure</p></li>
<li><p>Added an example message for HL7 v2.4, printset</p></li>
<li><p>Added an example message for HL7 v2.4, ACK</p></li>
<li><p>Removed the original <em>20. TalkStation users are not allowed to group sets of exams together and mark them for a single report….</em></p></li>
<li><p>Removed the original <em>19. PowerScribe users are not allowed to group sets of exams together and mark them for a single report….</em></p></li>
<li><p>Added a section about the HL7 messaging version 2.4: Setup Instructions/Examples for using IHE compliant HL7 v2.4 Protocols</p></li>
<li><p>Updated three v2.4 message examples</p></li>
</ul></td>
<td><p><a href="#_Ref256761960">3</a></p>
<p><a href="#_Ref257282758">7</a></p>
<p><a href="#_Ref257282768">9</a></p>
<p><a href="#_Ref257282776">10</a></p>
<p><a href="#_Ref257282789">11</a></p>
<p><a href="#_Ref257118979">44</a></p>
<p><a href="#_Ref257118989">64</a></p>
<p><a href="#section-15">94</a></p></td>
</tr>
<tr class="odd">
<td>March 2018</td>
<td>5.0</td>
<td><p>Patch RA*5*144</p>
<p>Remove patch 78 Query documentation</p>
<p>Release Study (NTP)</p></td>
<td><p>93</p>
<p>1, 5, 85</p></td>
</tr>
</tbody>
</table>

*This page intentionally left blank*

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Rad/Nuc Med Legacy[^1] HL7 Interface Specifications](#radnuc-med-legacy1-hl7-interface-specifications)
  - [Discussion of Vendor-Initiated Messages](#discussion-of-vendor-initiated-messages)
  - [Sample Clinical Scenario for Vendor-Initiated Messaging](#sample-clinical-scenario-for-vendor-initiated-messaging)
  - [Messaging Specifics for Vendor-Initiated Messages](#messaging-specifics-for-vendor-initiated-messages)
  - [Discussion of Rad/Nuc Med-Initiated Messages](#discussion-of-radnuc-med-initiated-messages)
  - [Clinical Scenarios for Rad/Nuc Med-Initiated Messages](#clinical-scenarios-for-radnuc-med-initiated-messages)
    - [Registration](#registration)
    - [Exam Edited](#exam-edited)
    - [Cancellation/Deletion](#cancellationdeletion)
    - [Verified/Released Unverified Report](#verifiedreleased-unverified-report)
    - [Release Study](#release-study)
  - [Messaging Specifics for Rad/Nuc Med-Initiated Messages](#messaging-specifics-for-radnuc-med-initiated-messages)
- [Setup Instructions/Examples for VistA to VistA Same-system, Different Application Messages Initiated by Rad/Nuc Med](#setup-instructionsexamples-for-vista-to-vista-same-system-different-application-messages-initiated-by-radnuc-med)
  - [Introduction](#introduction-1)
  - [Requirements](#requirements)
  - [Setup of Legacy[^9] HL7 Files for VistA-VistA Radiology Interface](#setup-of-legacy9-hl7-files-for-vista-vista-radiology-interface)
- [Setup Instructions/Examples for TCP/IP Legacy[^10] HL7 Interfaces between Rad/Nuc Med and COTS[^11] Products](#setup-instructionsexamples-for-tcpip-legacy10-hl7-interfaces-between-radnuc-med-and-cots11-products)
  - [Introduction](#introduction-2)
  - [Requirements](#requirements-1)
  - [Setup of HL7 Files for One-way Radiology to COTS Interface](#setup-of-hl7-files-for-one-way-radiology-to-cots-interface)
  - [Setup of HL7 Files for Two-way Radiology/COTS Interface](#setup-of-hl7-files-for-two-way-radiologycots-interface)
  - [Message Flow Diagram](#message-flow-diagram)
    - [Scenario 1 - VA Sends Order or Report Messages to the COTS Product Server](#scenario-1-va-sends-order-or-report-messages-to-the-cots-product-server)
    - [Scenario 2 - Processing Reports from COTS Product Server](#scenario-2-processing-reports-from-cots-product-server)
  - [Startup and Recovery](#startup-and-recovery)
    - [One-way TCP/IP Interface](#one-way-tcpip-interface)
    - [Two-way TCP/IP Interface](#two-way-tcpip-interface)
  - [VistA HL7 Message Files](#vista-hl7-message-files)
- [Implementing and Maintaining an Interface between Radiology and the TalkStation Voice Reporting Tool](#implementing-and-maintaining-an-interface-between-radiology-and-the-talkstation-voice-reporting-tool)
  - [Introduction](#introduction-3)
  - [Requirements](#requirements-2)
  - [Operational Features of the Interface](#operational-features-of-the-interface)
  - [IRM and ADPAC Setup Procedures](#irm-and-adpac-setup-procedures)
  - [Setup of HL7 Files](#setup-of-hl7-files)
  - [Detailed Explanation of Start-up/Recovery Procedure](#detailed-explanation-of-start-uprecovery-procedure)
  - [Start-up/Recovery Procedure Quick Reference](#start-uprecovery-procedure-quick-reference)
- [Implementing and Maintaining an Interface between Radiology and the PowerScribe Voice Reporting Tool](#implementing-and-maintaining-an-interface-between-radiology-and-the-powerscribe-voice-reporting-tool)
  - [Introduction](#introduction-4)
  - [Requirements](#requirements-3)
  - [Operational Features of the Interface](#operational-features-of-the-interface-1)
  - [IRM and ADPAC Set-up Procedures](#irm-and-adpac-set-up-procedures)
  - [Setup of HL7 Files](#setup-of-hl7-files-1)
  - [Configuring PowerScribe HL7 Protocol Settings](#configuring-powerscribe-hl7-protocol-settings)
  - [Detailed Explanation of Start-up/Recovery Procedure](#detailed-explanation-of-start-uprecovery-procedure-1)
  - [Start-up/Recovery Procedure Quick Reference](#start-uprecovery-procedure-quick-reference-1)
- [VistA Rad/Nuc Med HL7 Error Message and Troubleshooting Table for TalkStation and PowerScribe Interfaces](#vista-radnuc-med-hl7-error-message-and-troubleshooting-table-for-talkstation-and-powerscribe-interfaces)
- [# # # # # # # # # # # # # # Setup Instructions/Examples for Using IHE compliant HL7 v2.4 Protocols[^39]](#setup-instructionsexamples-for-using-ihe-compliant-hl7-v24-protocols39)
  - [Setting Up the Voice Recognition Event Driver Protocols](#setting-up-the-voice-recognition-event-driver-protocols)
    - [Step 1 - Remove subscribers from existing ORM event driver protocols](#step-1-remove-subscribers-from-existing-orm-event-driver-protocols)
    - [Step 2 - Remove subscribers from existing ORU event driver protocol](#step-2-remove-subscribers-from-existing-oru-event-driver-protocol)
    - [Step 3 - Add subscribers to new ORM event driver protocols](#step-3-add-subscribers-to-new-orm-event-driver-protocols)
    - [Step 5 - Change the Version ID field of existing message receipt protocol to 2.4](#step-5-change-the-version-id-field-of-existing-message-receipt-protocol-to-24)
    - [Step 6 - Turn on the use of the long site accession number](#step-6-turn-on-the-use-of-the-long-site-accession-number)
- [### ### #### [^1]: <span id="Ref221675367" class="anchor"></span> Patch RA\5\78 May 2009: Added Legacy to the heading](#1-span-idref221675367-classanchorspan-patch-ra578-may-2009-added-legacy-to-the-heading)
The Radiology/Nuclear Medicine (Rad/Nuc Med) package is a comprehensive software package designed to assist with the functions related to processing patients for imaging examinations.
The package automates a range of Rad/Nuc Med functions, including order entry of requests for exams by clinical staff, registration of patients for exams, processing of exams, recording reports/results, and verification of reports. The package interfaces with and through the Health Level Seven (HL7) package to exchange this exam and report information.
HL7 is an ANSI messaging transaction standard for healthcare. It is the main strategy used in a variety of healthcare providers and applications vendors to achieve Enterprise Application Integration (EAI) between disparate clinical applications.
The Rad/Nuc Med package supports the Integrating the Healthcare Enterprise (IHE) initiative. IHE is an initiative by healthcare professionals and industry to improve the way computer systems in healthcare share information. IHE promotes the coordinated use of established standards such as DICOM and HL7 to address specific clinical needs in support of optimal patient care.
Because many vendors support the IHE initiative, it allows Rad/Nuc Med to exchange key datasets with other VistA and Commercial Off-The-Shelf (COTS) products.
Rad/Nuc Med allows report transmission. That is, reports can be transmitted to Rad/Nuc Med from an outside source and filed as if entered in the Rad/Nuc Med package.
Rad/Nuc Med also has the ability to broadcast messages to outside sources. These messages are typically consumed by vendor PACS Systems, VistA Imaging, and Voice Recognition (VR) dictation systems. Rad/Nuc Med broadcasts messages when exams are registered, edited, cancelled or deleted, and reported or released.
The following chapters describe the information that can be manipulated with the Rad/Nuc Med and HL7 software. It also describes how to set up an HL7 interface to and from Radiology (both TCP/IP and non-TCP), and later describes how to implement/maintain the three VR system interfaces (for PowerScribe, TalkStation, and RadWhere) which have been developed, and are supported by, the Rad/Nuc Med developers.
*This page intentionally left blank*

# Rad/Nuc Med Legacy[^1] HL7 Interface Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For a description of the HL7 messages shared between the Rad/Nuc Med application and those commercial off the shelf (COTS) applications subscribing to the Rad/Nuc Med application, refer to the

- *Radiology/Nuclear Medicine Health Level Seven (HL7) Interface Specifications for Voice Recognition Dictation Systems* – HL7 version 2.3
- *Radiology/Nuclear Medicine 5.0 HL7 Interface Specificatio*n – HL7 version 2.4<span id="_Ref256761960" class="anchor"></span>[^2]

## Discussion of Vendor-Initiated Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vendor systems or other applications may send report (ORU) results for a selected exam back to the Rad/Nuc Med package. The report will be acknowledged (ACK) either positively or negatively with an error message. If the case selected is one of a "printset" (e.g., same report should apply to multiple cases) the Rad/Nuc Med software will detect this when the report message is received and will use the report for all cases in the set.

## Sample Clinical Scenario for Vendor-Initiated Messaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A patient is registered within the VistA Rad/Nuc Med system for an exam. The imaging exam is performed and the images for the case are given to a radiologist or nuclear medicine physician. The physician uses the vendor equipment to enter findings in a report and performs whatever action is necessary to trigger the vendor software to create and send to VistA an HL7 ORU message containing the report. VistA accepts and files the report and sends a positive acknowledgment (ACK) message, or rejects the report and sends an HL7 response (ACK) indicating why it was rejected.

## Messaging Specifics for Vendor-Initiated Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the vendor (or other) application sends report results, they send an Observational Results Unsolicited (ORU) message to the Rad/Nuc Med package. The ORU message consists of the following segments:

- MSH Message Header
- PID Patient Identification
- OBR Observational Request
- OBX Result

Example for HL7 v2.3MSH^~\|\\^RA-SERVER-IMG^HINES CIOFO^MAGD-CLIENT^884

^20050426130221-0600^^ORU~R01^499539643619^P^2.3.1^^^^^US

PID^^00-22-4444\~~^121~4~M10^^REALLYLONGSURNAMEXXXX~

MISSXXXX^^19730414^F^^^^^^^^^^^000224444

OBR^^^6958798.8966-1~120104-1732~L^76090~MAMMOGRAM, ONE BREAST~C4~435~MAMMOGRAM UNILAT~99RAP^^^200412011033-0600^""^""^^^^^20050426130124-0600^^0123~ STAFF~FIRST~M

^^MAMMOGRAM TEST CASE I^^23~MAMMOGRAPHY LAB~499~SUPPORT ISC^^2005042613020600^^^F^^^^^^^0123~STAFF~FIRST~M ^0456~RESIDENT~FIRST^^0123~STAFF~FIRST~M^200412011033-0600

OBX^^CE^P~PROCEDURE~L^^435~MAMMOGRAM UNILAT~L^^^^^^F

OBX^^TX^I~IMPRESSION~L^^impression txt checking the HL7 messaged format for verified (ORU) messages. ^^^^^^F

OBX^^CE^D~DIAGNOSTIC CODE~L^^1~NORMAL~L^^^^^^F

OBX^^TX^R~REPORT~L^^report text checking the HL7 messaged format for verified (ORU) messages. ^^^^^^F

OBX^^TX^M~MODIFIERS~L^^RIGHT^^^^^^F

OBX^^TX^TCM~TECH COMMENT~L^^testing the VR interface with WH

MAMMOGRAM UNILAT (MAM Detailed) CPT:76090^^^^^^F

Notes: The Diagnostic Code sent to VistA must be one of a predefined set in the VistA Rad/Nuc Med's Diagnostic Codes file (#78.3). These codes are facility specific. Impression is mandatory when ‘Impression required on Reports’ (field .116) is set for the Division (file \#79).  
  
The Rad/Nuc Med package sends back a General Acknowledgment (ACK) message. If the report is rejected, possible reasons are invalid or duplicate diagnostic code, provider not classified as "staff" or "resident" within the Rad/Nuc Med package, missing or invalid patient identification, an attempt was made to edit a canceled case, or a case where a report is already on file, missing impression text, or missing segment or field from a message.

## Discussion of Rad/Nuc Med-Initiated Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Rad/Nuc Med package will send an HL7 message with exam information to all site specified subscribers, if one or more is defined within the VistA Health Level Seven package setup, when each exam has been registered, examined (i.e., images have been collected), canceled, and when a report has been put in a status of Verified or Released/Not Verified. Subscribers may choose to subscribe to a subset rather than all of the available messages. Later sections show examples of VistA file setup that is necessary to accomplish this.

## Clinical Scenarios for Rad/Nuc Med-Initiated Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Registration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A VAMC may register a patient for an imaging exam at the time the patient arrives at the radiology or nuclear medicine reception desk for his/her appointment, or registration may be done up to a week prior to the appointment depending on the policy of that VAMC's imaging services. At this point, the registration message is broadcast and can be sent as an "order" to the PACS/Imaging, Voice Recognition, or other recipients. For exam sets, each procedure will be sent in its own HL7 message.

### Exam Edited

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Anytime the exam is edited, either through edit or status tracking, an ‘examined’ message will be broadcast. In the past, the VistA Rad/Nuc Med software allowed the ADPAC to specify an exam status that will trigger this event. Unfortunately, exam specific data could be edited without moving to a status that triggers an examined message. If, for example, the "Examined" status is specified, when the radiology tech enters the required data to cause the exam record to reach the "Examined" status, the examined message will be broadcast. This message is intended to signal the recipient that images have been collected. This is especially useful for interfacing with PACS equipment if the VAMC is running the VistA Imaging/Multi-Media software, which will then expect a message containing image ID's back from the PACS equipment. The Imaging/Multi-Media software then files the image ID's with the Rad/Nuc Med report through an Imaging-Rad/Nuc Med interface.

### Cancellation/Deletion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If an imaging tech or other VistA Rad/Nuc Med software user cancels or deletes an exam, this will trigger the cancel message broadcast. An exam is usually canceled before it is done. However, since exam data may have been erroneously entered, or entered for the wrong patient, the VistA Rad/Nuc Med system allows users to back data out and cancel after an exam is done, and possibly after results reports are entered. So, there is a possibility that an examined message and a report message would have been broadcast prior to a cancellation message.

### Verified/Released Unverified Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The report message is triggered when a VistA Rad/Nuc Med radiologist or transcriptionist enters data causing the findings report to move to a "Verified" (final) or "Released/Unverified" (preliminary) status. Depending on the policy of the VAMC, the "Released/Unverified" status may or may not be allowed. If the released/unverified report is broadcast on a message, a later message will contain the verified (final) report. It is also possible for a verified report to be retracted ("Unverified"), then re-verified later. If this happens a second report message would be broadcast with the amended, re-verified report, or else an exam cancel/delete message would be broadcast retracting the entire exam.

The registration message will always be the first message generated since registration must be done before any of the other events can take place. There is no software setup that can prevent users from entering and verifying a report prior to the tech entering exam information, so there is no guarantee that the "Examined" message will be sent before the "Report" message. However, a facility can choose to enforce the practice of case editing before entering and verifying reports to guarantee that the case gets to the proper "Examined" status before the report is verified.

### Release Study

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The v2.4 report message is triggered when National Teleradiology (NTP) releases a study back to the local facility for interpretation. This ‘Release Study’ message will always follow a NTP ‘Released/Unverified (preliminary)’ message.

## Messaging Specifics for Rad/Nuc Med-Initiated Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When an exam is registered, examined or cancelled by the Rad/Nuc Med package, an Order (ORM) message is sent to the site-specified application. The ORM message consists of the following segments:

- MSH Message Header
- PID Patient Identification
- ORC Common Order
- OBR Observational Request
- OBX Result
- ZDS Study Instance UID

Example for HL7 v2.3MSH^~\|\\^RA-SERVER-IMG^HINES CIOFO^MAGD-CLIENT^884^20050331082734-0600^^ORM~O01^499539642582^P^2.3.1^^^^^US

PID^^^666000000\~\~~USSSA&&0363~SS~VA FACILITY ID&&L\|00\~\~~USVHA&&0363~PI~VA FACILITY ID&&L^^RADPATIENT~FIRST~I\~\~\~~L^^19450000^M^^""^111 NOWHERE~PO BOX ALLEY~CHICAGO~IL~60612\~~P~""\|\~~""~""\~\~~N^^""^""^^^^^666000000^^^""^^^^^

^^^^

PV1^^I^7AS~200~RADLOCATION^^^^0000~RADTECH~FIRSTNAME~I^^^7AS^^^^^A2^^^^2729

ORC^NW^033105-1821^0331051821^^IP^^\~\~\~\~~R^^200503310819480600^

0000~RADSTAFF~FIRSTNAME~I ^^0000~RADSTAFF~FIRSTNAME~I^INFORMATION RESOURCE MGMT^786-5904~WPN~PH^^^IRM~INFORMATION RESOURCE MGMT~VistA49

OBR^1^033105-1821^033105-1821^73020~X-RAY EXAM OF SHOULDER~C4~123~SHOULDER 1

VIEW~99RAP^R^^^^^^^^^^\~\~\~~&left^0000~RADSTAFF~FIRSTNAME~I^000-0000~WPN~PH^6949668.9189-1^033105-1821^4~X-RAY CLINIC COUNT~499~SUPPORT ISC^RAD~GENERAL RADIOLOGY^^^^^^\~\~\~\~~R^^^WHLC^See History

ZDS^\*\*\* TESTING, THIS NODE IS A THROWAWAY \*\*\*.1.4.6025.6949668.9189.1.033105.1821

~VistA~Application~DICOM

OBX^^CE^P~PROCEDURE~L^^SHOULDER 1 VIEW^^^^^^O

OBX^1^TX^M~MODIFIERS~L^^LEFT^^^^^^O

OBX^1^TX^H~HISTORY~L^^test clinical history/reason for version 2.3.1 HL7 messages ^^^^^^O

OBX^1^TX^A~ALLERGIES~L^^PENICILLIN(V)^^^^^^O

OBX^2^TX^A~ALLERGIES~L^^TETRACYCLINE(V)^^^^^^O

OBX^3^TX^A~ALLERGIES~L^^ERYTHROMYCIN(V)^^^^^^O

OBX^4^TX^A~ALLERGIES~L^^AMIODARONE(N)^^^^^^O

OBX^5^TX^A~ALLERGIES~L^^ESTRADIOL CYPIONATE(V)^^^^^^O

OBX^6^TX^A~ALLERGIES~L^^ASPIRIN(V)^^^^^^O

OBX^7^TX^A~ALLERGIES~L^^FORTAZ ADD-VANTAGE(V)^^^^^^O

OBX^8^TX^A~ALLERGIES~L^^CODEINE(N)^^^^^^O

OBX^9^TX^A~ALLERGIES~L^^RADIOLOGICAL/CONTRAST MEDIA(V)^^^^^^O

OBX^1^TX^TCM~TECH COMMENT~L^^sample technologist comments for display purposes only^^^^^^O

  
Example for HL7 v2.4 [^3]

> MSH\|^~\\\|RA-VOICE-SERVER\|HINES CIOFO\|RA-TALKLINK-TCP\|TalkStation\|20110629092627-

> 0500\|\|ORM^O01\|4993885697\|P\|2.4\|\|\|\|\|USA

> PID\|\|141-167^^^USVHA^PI\|666432134^^^USVHA^NI\|6666559019V812454^^^USVHA^NI\|INPATI

> ENT^VISIT\|\|19350101\|M\|\|""^^0005^""^^CDC\|""^""^""^""^""\|\|\|\|\|\|\|\|666432134\|\|\|""^^01

> 89^""^^CDC

> PV1\|\|I\|4AS-1^410^1\|\|\|\|28^RAD^PROVIDER1\|28^RAD^PROVIDER1\|\|CARDIOLOGY\|\|\|\|\|A2\|\|28^RAD

> ^PROVIDER1\|\|I2189\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|20070119094640-0500

> ORC\|NW\|141-062911-3432\|141-062911-3432\|\|IP\|\|^^^^^R\|\|201106290920-0500\|1901^RADIOLOGY

> ^USER1\|\|1901^RADIOLOGY^USER1\|INFORMATION RESOURCE MGMT\|123-456-7890^PRN^PH~098-7

> 65-4321^WPN^PH~543-543-5435^^PH\|\|\|IRM^INFORMATION RESOURCE MGMT^VISTA49

> OBR\|1\|141-062911-3432\|141-062911-3432\|73562^X-RAY EXAM OF KNEE 3^C4^155^KNEE 3 VIEWS

> ^99RAP\|R\|\|\|\|\|\|\|\|\|\|^^^^&right\|1901^RADIOLOGY^USER1\|123-456-7890^PRN^PH~098-765-4321

> ^WPN^PH~543-543-5435^^PH\|141-062911-3432\|3432\|141-062911-3432\|RAD_GENERAL RADIOLO

> GY\`3_RADIOLOGY LAB\`499_SUPPORT ISC\|\|\|\|\|\|^^^^^R\|\|\|WHLC\|^Pain in right knee when

> walking.

> ZDS\|1.2.840.113754.1.4.141.6889370.9079.1.141.62911.3432^VISTA^Application^DICOM

> OBX\|1\|CE\|P^PROCEDURE^L\|\|155^KNEE 3 VIEWS^L\|\|\|\|\|\|O

> OBX\|2\|TX\|M^MODIFIERS^L\|\|RIGHT\|\|\|\|\|\|O

> OBX\|3\|CE\|C4^CPT MODIFIERS^L\|\|26^PROFESSIONAL COMPONENT^C4\|\|\|\|\|\|O

> OBX\|4\|CE\|C4^CPT MODIFIERS^L\|\|LT^LEFT SIDE^C4\|\|\|\|\|\|O

> OBX\|5\|TX\|H^HISTORY^L\|\|Reason for Study: Pain in right knee when walking.\|\|\|\|\|\|O

> OBX\|6\|TX\|H^HISTORY^L\|\| \|\|\|\|\|\|O

> OBX\|7\|TX\|H^HISTORY^L\|\|Clinical history text entered here for this sample case us

> ing the v2.4 HL7\|\|\|\|\|\|O

> OBX\|8\|TX\|H^HISTORY^L\|\|interface. \|\|\|\|\|\|O

> OBX\|9\|TX\|A^ALLERGIES^L\|\|APRICOTS(V)\|\|\|\|\|\|O

> OBX\|10\|TX\|A^ALLERGIES^L\|\|KIWI FRUIT(V)\|\|\|\|\|\|O

> OBX\|11\|TX\|TCM^TECH COMMENT^L\|\|The tech comment is that this is case \#3432.\|\|\|\|\|\|O

> **NOTE:** The messages broadcast at these three event points (registered, examined and cancelled) are almost identical, with the exception of the Order Control, Order Status, and Mode of Transportation. Differences to note between an HL7 message for registration, image collection (examined) and cancellation are shown.

| HL7 ORC Field | Registration | Cancel/Delete | Examined |
|-------------------|------------------|-------------------|--------------|
| 1-Order Contro    | NW               | CA                | XO           |
| 5-Order Status    | IP               | CA                | CM           |

The Mode of Transportation value on the OBR segment (in the example above, ~R) is omitted from the cancellation message.

Be aware that the OBR segment may exceed 255 characters. This means that other VistA applications will have to receive those segments in an array. See section Continuation Pointers section of the VistA HL7 Site Manager & Developer manual for more information about the method for handling segments greater than 255 characters. Outside vendor recipients should not be affected since they receive the message as a data stream.

When a report is Verified or Released/Not Verified by the Rad/Nuc Med package, an Observational Results Unsolicited (ORU) message is sent to the site specified application. The ORU message consists of the following segments:

- MSH Message Header
- PID Patient Identification
- OBR Observational Request
- OBX Result

Example for HL7 v2.3 [^4]

ORU message containing report for single procedure

MSH^~\|\\^RA-SERVER-IMG^HINES CIOFO^MAGD-CLIENT^884^20050407062538-0600^^ORU~R01^499539642886^P^2.3.1^^^^^US

PID^^^000377777\~\~~USSSA&&0363~SS~VA FACILITY ID&&L\|186\~\~~USVHA&&0363~PI~VA FACILITY ID&&L^^ZZCED~TEST~AMOK~II\~\~~L^^19550303^M^^""^123 ALF WAY~TEST 2~CHICAGO~IL~77777\~~P~TEST 3\|\~~""~""\~\~~N^^(708)999-9898^""^^^^^000377777^^^""^^^^^^^^^

OBR^1^040705-1821^040705-1821^74010~X-RAY EXAM OF ABDOMEN~C4~173~ABDOMEN 2 VIEWS~99RAP^^^200504070624-0600^^^^^^^^\~\~\~~&left right^67~ZZZNOTHING~NOTHING^^6949592.9387-1^040705-1821^4~X-RAY CLINIC COUNT~499~SUPPORT ISC^RAD~GENERAL RADIOLOGY^200504070625-0600^^^F^^^^^^^ZZZNOTHING~NOTHING^RADIOLOGY~USER~G

OBX^^CE^P~PROCEDURE~L^^ABDOMEN 2 VIEWS^^^^^^F

OBX^1^TX^I~IMPRESSION~L^^impression text for our ORU HL7 message examples... ^^^^^^F

OBX^1^CE^D~DIAGNOSTIC CODE~L^^NORMAL^^^^^^F

OBX^2^CE^D~DIAGNOSTIC CODE~L^^MINOR ABNORMALITY^^^^^^F

OBX^3^CE^D~DIAGNOSTIC CODE~L^^CODE WITH AN \T\\ INIT (HL7 TEST)^^^^^^F

OBX^1^TX^M~MODIFIERS~L^^LEFT^^^^^^F

OBX^2^TX^M~MODIFIERS~L^^RIGHT^^^^^^F

OBX^1^TX^TCM~TECH COMMENT~L^^This is a test registration to capture HL7 messages, both ORM \T\\ ORU. (techcomments)^^^^^^F

OBX^1^CE^C4~CPT MODIFIERS~L^^192~RESIDENT/TEACHING PHYS SERV~H^^^^^^F

OBX^2^CE^C4~CPT MODIFIERS~L^^367~'OPT OUT' PHYS/PRACT EMERG OR URGENT SERVICE~H^^^^^^F

Example for HL7 v2.3 [^5]

ORU messages for "printset", (i.e., multiple procedures and single report)

MSH^~\|\\^RA-SERVER-IMG^HINES CIOFO^MAGD-CLIENT^884^20050331130243-0600^^ORU~R01^499539642659^P^2.3.1^^^^^US

PID^^^000453231\~\~~USSSA&&0363~SS~VA FACILITY ID&&L\|97\~\~~USVHA&&0363~PI~VA FACILITY ID&&L^^ RADPATIENT~FIRST \~\~\~\~~L^^19391212^M^^""^""~"

"~""~""~""\~~P~""\|\~~""~""\~\~~N^^""^""^^^^^000453231^^^""^^^^^^^^^

OBR^1^092601-1453^092601-1453^75658~ARTERY X-RAYS,

ARM~C4~279~ANGIO BRACHIAL RETROGRADE S\T\I~99RAP^^^20050331130122-0600^^^^^^^^^

4569~RAD1~FIRST1^^6989073.865-1^092601-1453^4~X-RAY CLINIC COUNT~499~SUPPORT ISC^R

AD~GENERAL RADIOLOGY^200503311302-0600^^^F^^^^Printset: ZZRAD'S PRINTSET PARENT

^^^ RAD2~FIRST2~M ^ RAD1~FIRST1

OBX^^CE^P~PROCEDURE~L^^ANGIO BRACHIAL RETROGRADE S\T\I^^^^^^F

OBX^1^TX^I~IMPRESSION~L^^impression text used as an example for documentation purposes. ^^^^^^F

OBX^1^CE^D~DIAGNOSTIC CODE~L^^NORMAL^^^^^^F

OBX^2^CE^D~DIAGNOSTIC CODE~L^^N5-Malignant ACR Mammogram^^^^^^F

OBX^3^CE^D~DIAGNOSTIC CODE~L^^CODE WITH AN \T\\ INIT (HL7 TEST)^^^^^^F

OBX^1^TX^M~MODIFIERS~L^^RIGHT^^^^^^F

OBX^1^TX^TCM~TECH COMMENT~L^^^^^^^^F

OBX^2^TX^TCM~TECH COMMENT~L^^Edit Exam: added RIGHT^^^^^^F

OBX^3^TX^TCM~TECH COMMENT~L^^^^^^^^F^1^CE^C4~CPT MODIFIERS~L^^7~PROFESSIONAL COMPONENT~C^^^^^^F

MSH^~\|\\^RA-SERVER-IMG^HINES CIOFO^MAGD-CLIENT^884^20050331130243-0600^^ORU~R01^499539642663^P^2.3.1^^^^^US

PID^^^000453231\~\~~USSSA&&0363~SS~VA FACILITY ID&&L\|97\~\~~USVHA&&0363~PI~VA FACILITYID&&L^^RADPATIENT~FIRST\~\~\~\~~L^^19000101^M^^""^""~""~""~""~""\~~P~""\|\~~""~""\~\~~N^^""^""^^^^^000453231^^^""^^^^^^^^^

OBR^1^092601-1454^092601-1454^75685~ARTERY X-RAYS, SPINE~C4~297~ANGIO VERTEBRAL S\T\I~99RAP^^^20050331130122-0600^^^^^^^^^4569~ RAD1~FIRST1^^6989073.865-2^092601-1454^4~X-RAY CLINIC COUNT~499~SUPPORT ISC^RAD~GENERAL RADIOLOGY^

200503311302-0600^^^F^^^^Printset: ZZRAD'S PRINTSET PARENT^^^RAD2~FIRST2~M^ RAD1~FIRST1

OBX^^CE^P~PROCEDURE~L^^ANGIO VERTEBRAL S\T\I^^^^^^F

OBX^1^TX^I~IMPRESSION~L^^impression text used as an example for documentation purposes. ^^^^^^F

OBX^1^TX^TCM~TECH COMMENT~L^^^^^^^^F

OBX^1^CE^C4~CPT MODIFIERS~L^^7~PROFESSIONAL COMPONENT~C^^^^^^F

Example for HL7 v2.4 [^6]

ORU message containing report for single procedure

> MSH\|^~\\\|RA-VOICE-SERVER\|HINES CIOFO\|RA-TALKLINK-TCP\|TalkStation\|20110629133221-

> 0500\|\|ORU^R01\|4993885703\|P\|2.4\|\|\|\|\|USA

> PID\|\|141-167^^^USVHA^PI\|666432134^^^USVHA^NI\|6666559019V812454^^^USVHA^NI\|INPATI

> ENT^VISIT\|\|19350101\|M\|\|""^^0005^""^^CDC\|""^""^""^""^""\|\|\|\|\|\|\|\|666432134\|\|\|""^^01

> 89^""^^CDC

> OBR\|1\|141-062911-3432\|141-062911-3432\|73562^X-RAY EXAM OF KNEE 3^C4^155^KNEE 3 VIEWS

> ^99RAP\|\|\|20110629132828-0500\|\|\|\|\|\|\|\|^^^^&right\|1901^PROVIDER^RADTHREE\|123-456-

> 7890^PRN^PH~098-765-4321^WPN^PH~543-543-5435^^PH\|141-062911-3432\|3432\|141

> 0629113432\|RAD_GENERAL RADIOLOGY\`3_RADIOLOGY LAB\`499_SUPPORT ISC\|201106291331-

> 0500\|\|\|F\|\|\|\|\|\|\|76^OERR^CLINICIAN^G\|2188^RADIOLOGY^USER^G~22^STAFF^PROVIDER~4569^

> STAFF^PROVIDERTWO\|\|1901^PROVIDER^RADTHREE

> ZDS\|1.2.840.113754.1.4.141.6889370.9079.1.141.62911.3432^VISTA^Application^DICOM

> OBX\|1\|CE\|P^PROCEDURE^L\|\|155^KNEE 3 VIEWS^L\|\|\|\|\|\|F

> OBX\|2\|TX\|I^IMPRESSION^L\|\|This is the generic impression text entered for this sa

> mple report for \|\|\|\|\|\|F

> OBX\|3\|TX\|I^IMPRESSION^L\|\|documentation purposed. \|\|\|\|\|\|F

> OBX\|4\|TX\|I^IMPRESSION^L\|\| \|\|\|\|\|\|F

> OBX\|5\|TX\|I^IMPRESSION^L\|\|This is the last line of the sample impression text. \|

> \|\|\|\|\|F

> OBX\|6\|CE\|D^DIAGNOSTIC CODE^L\|\|1^NORMAL^L\|\|\|\|\|\|F

> OBX\|7\|CE\|D^DIAGNOSTIC CODE^L\|\|1000^NO ALERT REQUIRED^L\|\|\|\|\|\|F

> OBX\|8\|CE\|D^DIAGNOSTIC CODE^L\|\|9^NO DISCRETE MASS^L\|\|\|\|\|\|F

> OBX\|9\|TX\|M^MODIFIERS^L\|\|RIGHT\|\|\|\|\|\|F

> OBX\|10\|TX\|TCM^TECH COMMENT^L\|\|The tech comment is that this is case \#3432.\|\|\|\|\|\|F

> OBX\|11\|CE\|C4^CPT MODIFIERS^L\|\|26^PROFESSIONAL COMPONENT^C4\|\|\|\|\|\|F

> OBX\|12\|CE\|C4^CPT MODIFIERS^L\|\|LT^LEFT SIDE^C4\|\|\|\|\|\|F

> OBX\|13\|CE\|C4^CPT MODIFIERS^L\|\|99^MULTIPLE MODIFIERS^C4\|\|\|\|\|\|F

> OBX\|14\|TX\|R^REPORT^L\|\|This is the report text for case \#3432, which was a Knee e

> xam for the \|\|\|\|\|\|F

> OBX\|15\|TX\|R^REPORT^L\|\|patient. This sample report text will be filed in the Rad

> iology Report \|\|\|\|\|\|F

OBX\|16\|TX\|R^REPORT^L\|\|file for the patient/exam. \|\|\|\|\|\|F

Example for HL7 v2.4 [^7]

ORU messages for "printset", (i.e., multiple procedures and single report)

> MSH\|^~\\\|RA-VOICE-SERVER\|HINES CIOFO\|RA-TALKLINK-TCP\|TalkStation\|20110629134632-

> 0500\|\|ORU^R01\|4993885704\|P\|2.4\|\|\|\|\|USA

> PID\|\|141-167^^^USVHA^PI\|666432134^^^USVHA^NI\|6666559019V812454^^^USVHA^NI\|INPATI

> ENT^VISIT\|\|19350101\|M\|\|""^^0005^""^^CDC\|""^""^""^""^""\|\|\|\|\|\|\|\|666432134\|\|\|""^^01

> 89^""^^CDC

> OBR\|1\|141-062911-3433\|141-062911-3433\|74330^X-RAY BILE/PANC ENDOSCOPY^C4^207^ENDOSCO

> PIC CATH BIL \T\\ PANC DUCTS S\T\I^99RAP\|\|\|20110629133257-0500\|\|\|\|\|\|\|\|\|1901^PROVIDER

> ^RADTHREE\|123-456-7890^PRN^PH~098-765-4321^WPN^PH~543-543-5435^^PH\|141-062911-3433

> \|3433\|141-062911-3433\|RAD_GENERAL RADIOLOGY\`3_RADIOLOGY LAB\`499_SUPPORT ISC\|2011

> 06291346-0500\|\|\|F\|\|\|\|Printset: ZZPRINTSET PROCEDURE\|\|\|76^OERR^CLINICIAN^G\|2188^R

> ADIOLOGY^USER^G~2178^STAFF^PROVIDER~4569^STAFF^PROVIDERTWO\|\|1901^PROVIDER^RADTHREE

> ZDS\|1.2.840.113754.1.4.141.6889370.907.1.141.62911.3433^VISTA^Application^DICOM

> OBX\|1\|CE\|P^PROCEDURE^L\|\|207^ENDOSCOPIC CATH BIL \T\\ PANC DUCTS S\T\I^L\|\|\|\|\|\|F

> OBX\|2\|TX\|I^IMPRESSION^L\|\|This is the impression text for the printset. \|\|\|\|\|\|F

> OBX\|3\|TX\|I^IMPRESSION^L\|\| \|\|\|\|\|\|F

> OBX\|4\|TX\|I^IMPRESSION^L\|\|Cases 3433, 3434 and 3435 will all receive the same text.

> \|\|\|\|\|\|F

> OBX\|5\|TX\|I^IMPRESSION^L\|\| \|\|\|\|\|\|F

> OBX\|6\|TX\|I^IMPRESSION^L\|\|Final line of impression text. \|\|\|\|\|\|F

> OBX\|7\|CE\|D^DIAGNOSTIC CODE^L\|\|1^NORMAL^L\|\|\|\|\|\|F

> OBX\|8\|CE\|D^DIAGNOSTIC CODE^L\|\|9^NO DISCRETE MASS^L\|\|\|\|\|\|F

> OBX\|9\|CE\|D^DIAGNOSTIC CODE^L\|\|13^CODE WITH AN \T\\ IN IT (HL7 TEST)^L\|\|\|\|\|\|F

> OBX\|10\|TX\|M^MODIFIERS^L\|\|PORTABLE EXAM\|\|\|\|\|\|F

> OBX\|11\|TX\|TCM^TECH COMMENT^L\|\|This is the first case (3433) in the Printset.\|\|\|\|\|\|F

> OBX\|12\|TX\|R^REPORT^L\|\|This is the report text for the printset exam, case number

> s 3433, 3434 and\|\|\|\|\|\|F

> OBX\|13\|TX\|R^REPORT^L\|\|3435. \|\|\|\|\|\|F

> OBX\|14\|TX\|R^REPORT^L\|\| \|\|\|\|\|\|F

> OBX\|15\|TX\|R^REPORT^L\|\|This sample report text will be filed in the Radiology Rep

> ort file and all\|\|\|\|\|\|F

> OBX\|16\|TX\|R^REPORT^L\|\|3 cases in the printset will point to the same report. \|\|\|\|\|\|F

> OBX\|17\|TX\|R^REPORT^L\|\| \|\|\|\|\|\|F

OBX\|18\|TX\|R^REPORT^L\|\|This is the last line of the report text. \|\|\|\|\|\|F

If the receiving application is outside of VistA, it should then send a General Acknowledgment

(ACK) message back to the HL7 package. The ACK message consists of the following segments:

- MSH Message Header
- MSA Message Acknowledgment

Example for HL7 v2.3MSH^~\|\\^PACS^HINES^RADIOLOGY^578^199504121041^^ACK^170^P^2.3.1

MSA^AA^170

Example for HL7 v2.4 [^8]

MSH\|^~\\\|RA-VOICE-SERVER\|HINES CIOFO\|RA-TALKLINK-TCP\|TalkStation\|20091130110935-

0500\|\|ACK^R01\|4993882144\|P\|2.4\|\|\|\|\|USA

MSA\|AA\|\|

*This page intentionally left blank*

# Setup Instructions/Examples for VistA to VistA Same-system, Different Application Messages Initiated by Rad/Nuc Med

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the steps required to setup and maintain a non-TCP/IP VistA-VistA same-system, different application HL7 interface from VistA Rad/Nuc Med.

VistA messages can be any one of the following:

1.  Registration
2.  Cancellation
3.  Exam edited (i.e., images collected, usually set up in sites using the VistA Imaging package and/or a PACS system)
4.  VistA reports which are Verified or Released/Not Verified. (These reports must be broadcast in order to synchronize VistA and the receiving system’s databases.)

## Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Familiarity with the VistA HL7 Site Manager & Developer Manual is recommended before proceeding to create non-TCP/IP HL7 interfaces from Rad/Nuc Med.

All released Radiology, HL7 and Kernel patches must be installed. In particular, patch HL\*1.6\*57, and Rad/Nuc Med patch RA\*5\*17.

## Setup of Legacy[^9] HL7 Files for VistA-VistA Radiology Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### HL7 Application Parameter File \#771 Setup

Two HL7 Applications are required for VistA to VistA same system interfaces; one for each side of the interface.

Rad/Nuc Med v5.0 exports the RA-SERVER-IMG and RA-CLIENT-IMG applications for use in a VistA to VistA interface.

Next is an example of the HL7 Application setup for a VistA to VistA interface. Refer to section 7.4 of the VistA HL7 Site Manager & Developer Manual for an explanation of individual fields. There is also a screen shot from the HL7 Main Menu, HL7 Interface Developers Options…, Application Edit option.

NAME: RA-SERVER-IMG ACTIVE/INACTIVE: ACTIVE

FACILITY NAME: RADIOLOGY INTERFACE COUNTRY CODE: US

> HL7 APPLICATION EDIT

> -----------------------------------------------------------------------------

> NAME: RA-SERVER-IMG ACTIVE/INACTIVE: ACTIVE

> FACILITY NAME: RADIOLOGY INTERFACE COUNTRY CODE: US

> HL7 FIELD SEPARATOR: HL7 ENCODING CHARACTERS:

> MAIL GROUP:

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> Enter a command or '^' followed by a caption to jump to a specific field.

> COMMAND: Press \<PF1\>H for help Insert

NAME: RA-CLIENT-IMG ACTIVE/INACTIVE: ACTIVE

FACILITY NAME: IMAGING INTERFACE COUNTRY CODE: US

> HL7 APPLICATION EDIT

> ------------------------------------------------------------------------------

> NAME: RA-CLIENT-IMG ACTIVE/INACTIVE: ACTIVE

> FACILITY NAME: IMAGING INTERFACE COUNTRY CODE: US

> HL7 FIELD SEPARATOR: HL7 ENCODING CHARACTERS:

> MAIL GROUP:

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> Enter a command or '^' followed by a caption to jump to a specific field.

> COMMAND: Press \<PF1\>H for help Insert

The HL7 Field Separator will default to ‘^’, and the encoding characters default to ‘~\|\\’. These are the VistA HL7 defaults and should not be changed for VistA to VistA interfaces.

#### Protocol File \#101 Setup

Four event driver protocols (RA REG 2.3.1, RA EXAMINED 2.3.1, RA CANCEL 2.3.1, RA RPT 2.3.1) were exported with Rad/Nuc Med and subsequent patches to send exam or report data from the Rad/Nuc Med package to another VistA application such as an imaging system via the HL7 V. 1.6 package. It is unlikely that you will be required to create new event driver protocols, but changes may be required to some fields in order to utilize the exported protocols.

Protocol Triggering event in VistA Rad/Nuc Med processing

RA REG 2.3.1 Rad/Nuc Med case registration

RA CANCEL 2.3.1 Rad/Nuc Med case cancellation or deletion

RA EXAMINED 2.3.1 Rad/Nuc Med case edit

RA RPT 2.3.1 Rad/Nuc Med report status changes to "Released/Not Verified" or

> “Verified"

Two "subscriber" protocols, RA SEND ORM and RA SEND ORU, were also exported. RA SEND ORM should be entered in the SUBSCRIBERS field of the three ORM event driver protocols (RA REG 2.3.1, RA CANCEL 2.3.1, RA EXAMINED 2.3.1), and RA SEND ORU should be entered in the SUBSCRIBERS field of the ORU event driver protocol (RA RPT 2.3.1). Sites can set up their own equivalent of the subscriber protocols for a single message or various combinations of messages. The RA SEND ORM and RA SEND ORU protocols are only exported for convenience; they can be used as subscribers, or they can serve as an example for creating new subscriber protocols.

Although sample setup for messaging is described below, this should in no way replace or act as a substitute for the instructions in the VistA HL7 Site Manager & Developers Guide documentation. The descriptions and samples below are subject to change based on new versions or patches to the Health Level Seven package.

Setup involves editing fields on exported records, and, in some cases, adding records depending on the needs of the site. The subscriber protocols should be set as SUBSCRIBERS in the associated event driver protocols. The event driver protocols will also require a valid Sending Application, which points to a record in file \#771. Subscriber protocols should have this application entered as Receiving Application. However, if you are using 2 HL7 Applications for the interface, the second HL7 Application should be used as the subscriber Receiving Application.

> **NOTE:** Once you've entered a sending application for an event driver protocol, File \#772 (HL7 MESSAGE TEXT) will start growing. See VistA HL7 Site Manager & Developer Manual for instructions on purging. If you are not receiving and processing the messages, you may want to remove the sending application name from the event drivers to prevent growth of File 772. If you experience problems and wish to temporarily disable the interface, just delete the contents of the Sending Application field on whichever event driver protocols are causing the errors.

For VistA to VistA interfaces, M code will have to be created and specified so that another VistA application can capture and process the information from the HL7 message. The M code to be executed (for receiving and processing the message) should be specified in the PROCESSING ROUTINE field of the subscriber protocol.

  
Example

In the RA SEND ORM protocol, PROCESSING ROUTINE: D EN^OTHERPKG

where EN^OTHERPKG should be replaced by a real line label and routine references. The routine you enter as the PROCESSING ROUTINE should contain M code like the following:

> EN N I,J,X

> F I=1:1 X HLNEXT Q:HLQUIT'\>0 D

> .S X(I)=HLNODE,J=0 ; get first segment node

> .;get continuation nodes for long segments, if any

> .F S J=\$O(HLNODE(J)) Q:'J S X(I,J)=HLNODE(J)

> This sample code is taken from the VistA HL7 Site Manager & Developer Manual Section 9.7 How To Parse Message Text. It is used to retrieve each message segment.

Listed below are example subscriber and event driver protocols for an interface to a same system VistA application. Also shown are screen shots from the HL7 Main Menu, Interface Developers Options…, Edit Protocols option showing how the example was created.

In the next examples, the two Processing routines ^ZZTEST1 and ^ZZTEST2 should be replaced by the routines in the receiving package that will process the data received. Nothing is exported to these fields by Rad/Nuc Med v5.0 or associated patches

NAME: RA SEND ORM ITEM TEXT: Client for Imaging

TYPE: subscriber PACKAGE: ANYPKG

RECEIVING APPLICATION: RA-CLIENT-IMG EVENT TYPE: O01

VERSION ID: 2.3.1 RESPONSE MESSAGE TYPE: ACK

PROCESSING ROUTINE: D ^ZZTEST1 SENDING FACILITY REQUIRED?: NO

RECEIVING FACILITY REQUIRED?: NO SECURITY REQUIRED?: NO

HL7 INTERFACE SETUP PAGE 1 OF 2

-------------------------------------------------------------------------------

NAME: RA SEND ORM

DESCRIPTION (wp): (empty)

ENTRY ACTION:

EXIT ACTION:

TYPE: subscriber

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 SUBSCRIBER PAGE 2 OF 2

RA SEND ORM

-------------------------------------------------------------------------------

RECEIVING APPLICATION: RA-CLIENT-IMG

RESPONSE MESSAGE TYPE: ACK EVENT TYPE: O01

SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

SECURITY REQUIRED?: NO

LOGICAL LINK:

PROCESSING RTN: D ^ZZTEST1 \<-- empty when exported

ROUTING LOGIC:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

NAME: RA SEND ORU ITEM TEXT: Client for Imaging

TYPE: subscriber PACKAGE: ANYPKG

RECEIVING APPLICATION: RA-CLIENT-IMG EVENT TYPE: R01

VERSION ID: 2.3.1 RESPONSE MESSAGE TYPE: ACK

PROCESSING ROUTINE: D ^ZZTEST2 SENDING FACILITY REQUIRED?: NO

RECEIVING FACILITY REQUIRED?: NO SECURITY REQUIRED?: NO

HL7 INTERFACE SETUP PAGE 1 OF 2

-------------------------------------------------------------------------------

NAME: RA SEND ORU

DESCRIPTION (wp): (empty)

ENTRY ACTION:

EXIT ACTION:

TYPE: subscriber

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 SUBSCRIBER PAGE 2 OF 2

RA SEND ORU

-------------------------------------------------------------------------------

RECEIVING APPLICATION: RA-CLIENT-IMG

RESPONSE MESSAGE TYPE: ACK EVENT TYPE: R01

SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

SECURITY REQUIRED?: NO

LOGICAL LINK:

PROCESSING RTN: D ^ZZTEST2 \<-- empty when exported

ROUTING LOGIC:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

NAME: RA REG 2.3.1

ITEM TEXT: Rad/Nuc Med exam registered (v2.3.1 HL7)

TYPE: event driver PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is triggered whenever a Radiology/Nuclear

Medicine exam is registered. It executes code that creates an HL7 ORM message

consisting of PID, ORC, OBR, OBX and ZDS segments. The message contains all

relevant information about the exam, including procedure, time of

registration, procedure modifiers, patient allergies, and clinical history.

This protocol is used to trigger v2.3.1 compliant HL7 messages.

TIMESTAMP: 59851,50559 SENDING APPLICATION: RA-SERVER-IMG

TRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01

VERSION ID: 2.3.1

SUBSCRIBERS: RA SEND ORM

HL7 INTERFACE SETUP PAGE 1 OF 2

-------------------------------------------------------------------------------

NAME: RA REG 2.3.1

DESCRIPTION (wp): \[This protocol is triggered whenever a Radiology\]

ENTRY ACTION:

EXIT ACTION:

TYPE: event driver

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 EVENT DRIVER PAGE 2 OF 2

RA REG

-------------------------------------------------------------------------------

SENDING APPLICATION: RA-SERVER-IMG

TRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01

PROCESSING ID: VERSION ID: 2.3.1

ACCEPT ACK CODE: APPLICATION ACK TYPE:

RESPONSE PROCESSING RTN:

SUBSCRIBERS

RA SEND ORM

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for Help Insert

NAME: RA CANCEL 2.3.1

ITEM TEXT: Rad/Nuc Med exam cancellation (v2.3.1 HL7)

TYPE: event driver PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is triggered whenever a Radiology/Nuclear

Medicine exam is cancelled. It executes code that creates an HL7 ORM message

consisting of PID, ORC, OBR, OBX and ZDS segments. The message contains all

relevant information about the exam, including procedure, time of

cancellation, procedure modifiers, patient allergies and clinical history.

This protocol is used to trigger v2.3.1 compliant HL7 messages.

TIMESTAMP: 59851,50573 SENDING APPLICATION: RA-SERVER-IMG

TRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01

VERSION ID: 2.3.1

SUBSCRIBERS: RA SEND ORM

HL7 INTERFACE SETUP PAGE 1 OF 2

-------------------------------------------------------------------------------

NAME: RA CANCEL 2.3.1

DESCRIPTION (wp): \[This protocol is triggered whenever a Radiology\]

ENTRY ACTION:

EXIT ACTION:

TYPE: event driver

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 EVENT DRIVER PAGE 2 OF 2

RA CANCEL

-------------------------------------------------------------------------------

SENDING APPLICATION: RA-SERVER-IMG

TRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01

PROCESSING ID: VERSION ID: 2.3.1

ACCEPT ACK CODE: APPLICATION ACK TYPE:

RESPONSE PROCESSING RTN:

SUBSCRIBERS

RA SEND ORM

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

NAME: RA EXAMINED 2.3.1

ITEM TEXT: Rad/Nuc Med examined case (v2.3.1 HL7)

TYPE: event driver PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is triggered whenever a Radiology/Nuclear

Medicine exam has been edited by the user. It executes code that creates

an HL7 ORM message consisting of PID, ORC, OBR, OBX and ZDS segments. This

message contains all relevant information about the exam, including procedure,

time of registration, procedure modifiers, patient allergies, and clinical

history.

This protocol is used to trigger v2.3.1 compliant HL7 messages.

TIMESTAMP: 59851,50545 SENDING APPLICATION: RA-SERVER-IMG

TRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01

VERSION ID: 2.3.1

SUBSCRIBERS: RA SEND ORM

HL7 INTERFACE SETUP PAGE 1 OF 2

------------------------------------------------------------------------------

NAME: RA EXAMINED 2.3.1

DESCRIPTION (wp): \[This protocol is triggered whenever a Radiology\]

ENTRY ACTION:

EXIT ACTION:

TYPE: event driver

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 EVENT DRIVER PAGE 2 OF 2

RA EXAMINED

-------------------------------------------------------------------------------

SENDING APPLICATION: RA-SERVER-IMG

TRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01

PROCESSING ID: VERSION ID: 2.3.1

ACCEPT ACK CODE: APPLICATION ACK TYPE:

RESPONSE PROCESSING RTN:

SUBSCRIBERS

RA SEND ORM

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

NAME: RA RPT 2.3.1

ITEM TEXT: Rad/Nuc Med report released/verified (v2.3.1 HL7)

TYPE: event driver PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is triggered whenever a Radiology/Nuclear

Medicine report enters into a status of Verified or Released/Not Verified. It

executes code that creates an HL7 ORU message consisting of PID, OBR and OBX

segments. The message contains relevant information about the report,

including procedure, procedure modifiers, diagnostic code, interpreting

physician, impression text and report text.

This protocol is used to trigger v2.3.1 compliant HL7 messages.

TIMESTAMP: 59851,50886 SENDING APPLICATION: RA-SERVER-IMG

TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

VERSION ID: 2.3.1

SUBSCRIBERS: RA SEND ORU

HL7 INTERFACE SETUP PAGE 1 OF 2

-------------------------------------------------------------------------------

NAME: RA RPT 2.3.1

DESCRIPTION (wp): \[This protocol is triggered whenever a Radiology\]

ENTRY ACTION:

EXIT ACTION:

TYPE: event driver

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 EVENT DRIVER PAGE 2 OF 2

RA RPT

-------------------------------------------------------------------------------

SENDING APPLICATION: RA-SERVER-IMG

TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

PROCESSING ID: VERSION ID: 2.3.1

ACCEPT ACK CODE: APPLICATION ACK TYPE:

RESPONSE PROCESSING RTN:

SUBSCRIBERS

RA SEND ORU

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

# Setup Instructions/Examples for TCP/IP Legacy[^10] HL7 Interfaces between Rad/Nuc Med and COTS[^11] Products

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the steps required to setup and maintain a TCP/IP HL7 link between VistA Rad/Nuc Med and a COTS product.

VistA messages can be any one of the following:

1.  Registration
5.  Cancellation
6.  Examined (i.e., images collected, usually set up in sites using the VistA Imaging package and/or a PACS system)
7.  VistA reports which are Verified or Released/Not Verified. (These reports must be sent to COTS product in order to synchronize VistA and COTS product's databases.)

Radiology will currently only accept result messages (i.e. Radiology reports) from a COTS product.

## Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Familiarity with the VistA HL7 Site Manager & Developer Manual is recommended before proceeding to create Radiology TCP/IP HL7 interfaces.

All released Radiology, HL7 and Kernel patches must be installed. In particular, patch HL\*1.6\*57, and Rad/Nuc Med patch RA\*5\*17.

To run HL7 messages under TCP/IP, Alpha/AXP sites running more than one instance of TaskMan MUST run TaskMan from DCL Context. This is the recommendation of the HL7 developers. Please refer to the SETUP OF HL7 FILES section of this document to determine the impact on the Startup Node field for file 870.

Consider putting the COTS server on a UPS. Power blips and outages have proven to be a problem in reliable TCP/IP message transmission.

## Setup of HL7 Files for One-way Radiology to COTS Interface 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### HL7 Application Parameter File \#771 Setup

Two HL7 Applications will always be required with a VistA Radiology to COTS product TCP/IP HL7 interface. One will serve as the VistA Radiology side of the interface; the other will represent the COTS system.

Several HL7 applications are exported with Rad/Nuc Med v5.0 and associated patches, these can be used as exported, or they can serve as an example for creating new HL7 applications:

File 771 Entry Explanation

RA-VOICE-SERVER Exported for use as VistA Rad/Nuc Med Application (HL7 v2.3)

RA-TALKLINK-TCP Exported for supported interface to TalkStation (HL7 v2.3)

RA-PSCRIBE-TCP Exported for PowerScribe product (HL7 v2.3)

TalkStation is a Voice Recognition reporting tool from TalkTechnology with a supported interface to VistA Radiology. See the ‘Implementing and maintaining an Interface between Radiology and the TalkStation Voice Reporting Tool’ section later in this documentation for information.

PowerScribe is another Voice Recognition reporting tool with a supported interface to Radiology. The ‘Implementing and maintaining an Interface between Radiology and the PowerScribe Voice Reporting Tool’ has further details on this implementation.

If you intend to interface with a different COTS Voice Recognition Dictation system vendor, they may find it useful to study the Rad/Nuc Med V. 5.0 HL7 Interface Specifications for Voice Recognition Systems manual, which defines all data passed by, and accepted by, the Radiology HL7 interface software.

Next is an example of two HL7 applications created for a TCP/IP interface. Refer to Section 7.4 of the VistA HL7 Site Manager & Developer Manual for an explanation of individual fields. Also shown are screen shots from the HL7 Main Menu, HL7 Interface Developers Options…, Application Edit option:

> **NOTE:** The HL7 field separator and encoding characters listed below are the HL7 standard, but are not the VistA HL7 standard. When interfacing with a COTS product you will most likely be required to use the HL7 standard. Be aware, however, that these may have to be entered manually, as the ScreenMan application does not allow the ‘^’ character to be entered as the first character in a field. The VistA HL7 standard, and default, is a field separator of ‘^’ and encoding characters of ‘~\|\\’

NAME: RA-RADSERVER ACTIVE/INACTIVE:ACTIVE

FACILITY NAME: VistA RADIOLOGY COUNTRY CODE: US

HL7 ENCODING CHARACTERS: ^~\\ HL7 FIELD SEPARATOR: \|

HL7 APPLICATION EDIT

--------------------------------------------------------------------------------

NAME: RA-RADSERVER ACTIVE/INACTIVE: ACTIVE

FACILITY NAME: VistA RADIOLOGY COUNTRY CODE: US

HL7 FIELD SEPARATOR: \| HL7 ENCODING CHARACTERS: ^~\\

MAIL GROUP:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

NAME: RA-COTSCLIENT ACTIVE/INACTIVE: ACTIVE

FACILITY NAME: COTS EXAMPLE COUNTRY CODE: US

HL7 ENCODING CHARACTERS: ^~\\ HL7 FIELD SEPARATOR: \|

HL7 APPLICATION EDIT

--------------------------------------------------------------------------------

NAME: RA-COTSCLIENT ACTIVE/INACTIVE: ACTIVE

FACILITY NAME: COTS EXAMPLE COUNTRY CODE: US

HL7 FIELD SEPARATOR: \| HL7 ENCODING CHARACTERS: ^~\\

MAIL GROUP:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

#### HL Logical Link File \#870 Sender Setup

Depending on the interface you will either require one or two HL7 Logical Links for message transactions. One sender link is required for VistA to send order and results messages to a COTS product and to receive acknowledgments to those messages from the COTS product. A listener link would be required if the COTS product is to send results messages to VistA and to receive acknowledgments to those messages from VistA. For now, we will discuss sender links only. The additional setup required for listener links follows later in this document.

File \#870 contains the links used by the HL7 package to send messages. It is used to identify the TCP/IP address of the COTS product server, as well as the TCP/IP port numbers that will be used.

This file also stores parameters that define the behavior of the lower level protocols and information that is used with the Systems Link Monitor, which gives the user feedback about the state of each link.

Several sender links are exported with Rad/Nuc Med and subsequent patches. These are exported for use in specific supported interfaces but can be viewed as examples of sender links:

Logical Link Reason exported

RA-PSCRIBE Radiology-PowerScribe link

RA-TALK Radiology-TalkStation link

Next is an example of a newly created sender link which could be used to send order messages (i.e., exam registered, exam cancelled, patient examined, and report verified or released/not verified) from VistA to a COTS product. This link would also receive the order Acknowledgment from the COTS product.

The example shows active, run-time data. Some of the fields are populated by the HL7 package when you start up the link and do not need to be entered manually.

It is strongly recommended that you add an ACK timeout for these links. If you do not enter a value then a default of 10 seconds will be used and experience has shown than this is not enough for a busy TCP/IP network. We recommend using between 300 and 600 seconds.

Regardless of the ‘Exceed Re-Transmit Action’ entered, when the ‘Re-Transmission Attempts’ for a message is exceeded, an alert is sent to the mail group defined in the MAIL GROUP FOR ALERTS field in the HL COMMUNICATIONS SERVER PARAMETERS (#869.3) file. This can be edited using the HL7 Main Menu, Site Parameter Edit option.

We have used a Persistent Client in the example below, but you may prefer to define the link as a Non-Persistent Client. The difference being that the link connects only when required rather than remaining open at all times.

See the VistA HL7 Site Manager and Developer Manual section 2.4 TCP Link Setup for additional field definitions.

NODE: RA-COTS LLP TYPE: TCP

DEVICE TYPE: Persistent Client AUTOSTART: Enabled

RE-TRANSMISSION ATTEMPTS: 3 ACK TIMEOUT: 300

EXCEED RE-TRANSMIT ACTION: ignore TCP/IP ADDRESS: <span class="mark">REDACTED</span>

TCP/IP PORT: 7077 TCP/IP SERVICE TYPE: CLIENT (SENDER)

STARTUP NODE: PERSISTENT: YES

HL7 LOGICAL LINK

-------------------------------------------------------------------------------

NODE: RA-COTS

INSTITUTION:

DOMAIN:

AUTOSTART: Enabled\<- set to Enabled if autostart of link required

QUEUE SIZE:

LLP TYPE: TCP

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 LOGICAL LINK

-------------------------------------------------------------------------------

┌──────────────────────TCP LOWER LEVEL PARAMETERS─────────────────────────┐

│ RA-COTS │

│ │

│ TCP/IP SERVICE TYPE: CLIENT (SENDER) │

│ TCP/IP ADDRESS: <span class="mark">REDACTED</span> \<- address of COTS server │

│ TCP/IP PORT: 7077\<- port COTS server receives on │

│ │

│ │

│ ACK TIMEOUT: 300\<- recommended RE-TRANSMISION ATTEMPTS: 3 │

│ READ TIMEOUT: EXCEED RE-TRANSMIT ACTION: ignore │

│ BLOCK SIZE: │

│ │

│STARTUP NODE: \<- ONLY set if multiple TaskMan/DCL PERSISTENT: YES │

│ RETENTION: UNI-DIRECTIONAL WAIT: │

└─────────────────────────────────────────────────────────────────────────┘

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Close Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Close Press \<PF1\>H for help Insert

#### Protocol File \#101 Setup

Eight event driver protocols (RA REG, RA REG 2.3, RA EXAMINED, RA EXAMINED 2.3, RA CANCEL, RA CANCEL 2.3, RA RPT and RA RPT 2.3) were exported with VistA Rad/Nuc Med and subsequent patches to send exam or report data from the Rad/Nuc Med package to a COTS product via HL7. It is unlikely that you will have to create new event driver protocols, but changes will be required to some fields in order to utilize the exported protocols.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 51%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><strong><br />
Event Driver Protocol</strong></th>
<th><strong><br />
Triggering Event in Rad/Nuc Med</strong></th>
<th><strong>HL7 Version</strong></th>
<th><strong>Message Type</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>RA REG 2.3.1</td>
<td>Rad/Nuc Med case registration</td>
<td>2.3</td>
<td>ORM</td>
</tr>
<tr class="even">
<td>RA EXAMINED 2.3.1</td>
<td>When all Rad/Nuc Med exam edit and status tracking options are exercised.</td>
<td>2.3</td>
<td>ORM</td>
</tr>
<tr class="odd">
<td>RA CANCEL 2.3.1</td>
<td>Rad/Nuc Med case cancellation or deletion</td>
<td>2.3</td>
<td>ORM</td>
</tr>
<tr class="even">
<td>RA RPT 2.3.1</td>
<td>Rad/Nuc Med report status changes to ‘Verified’ or ‘Released/Not Verified’</td>
<td>2.3</td>
<td>ORU</td>
</tr>
</tbody>
</table>

Six subscriber protocols (RA TCP ORM, RA TALKLINK ORM and RA PSCRIBE ORM and RA TCP ORU, RA TALKLINK ORU and RA PSCRIBE ORU) were also exported by Rad/Nuc Med and subsequent patches. All of these protocols are exported purely for convenience; they can be used as subscribers, or they can serve as examples for creating new subscriber protocols.

The subscriber protocols need to be entered in the SUBSCRIBERS multiple of event driver protocols. Once subscriber protocols are added, messages will be built and will stack up until the interface is started. The ORM protocols are for general order messages and should be used with the ORM event drivers. The ORU protocols are for observation results messages (reports) and should be used with the ORU event drivers.

If ever you need to completely disable an interface and want to stop new messages from being created for this interface, simply remove the subscriber protocols from the event driver protocols.

The TALKLINK protocols are intended for use with the TalkStation interface. The PSCRIBE protocols are intended for use with the PowerScribe interface. The TALKLINK and PSCRIBE protocols are essentially the same but are exported under different names for ease of support.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 50%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong><br />
Subscriber Protocol</strong></td>
<td><strong><br />
Potential SUBSCRIBER to</strong></td>
<td><strong>HL7 Version</strong></td>
<td><strong>Message Type</strong></td>
</tr>
<tr class="even">
<td>RA TALKLINK ORM</td>
<td>RA REG 2.3.1, RA CANCEL 2.3.1, RA EXAMINED 2.3.1</td>
<td>2.3.1</td>
<td>ORM</td>
</tr>
<tr class="odd">
<td>RA TALKLINK ORU</td>
<td>RA RPT 2.3.1</td>
<td>2.3.1</td>
<td>ORU</td>
</tr>
<tr class="even">
<td>RA PSCRIBE ORM</td>
<td>RA REG 2.3.1, RA CANCEL 2.3.1, RA EXAMINED 2.3.1</td>
<td>2.3.1</td>
<td>ORM</td>
</tr>
<tr class="odd">
<td>RA PSCRIBE ORU</td>
<td>RA RPT 2.3.1</td>
<td>2.3.1</td>
<td>ORU</td>
</tr>
</tbody>
</table>

Listed next are examples subscriber and event driver protocols for an interface to a COTS product. Also shown are screen shots from the HL7 Main Menu, Interface Developers Options…, Edit Protocols option showing how the example was created.

NAME: RA COTS ORM ITEM TEXT: TCP Client

TYPE: subscriber PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

RECEIVING APPLICATION: RA-COTSCLIENT EVENT TYPE: O01

LOGICAL LINK: RA-COTS VERSION ID: 2.3.1

RESPONSE MESSAGE TYPE: ACK SENDING FACILITY REQUIRED?: NO

RECEIVING FACILITY REQUIRED?: NO SECURITY REQUIRED?: NO

HL7 INTERFACE SETUP PAGE 1 OF 2

-------------------------------------------------------------------------------

NAME: RA COTS ORM

DESCRIPTION (wp): (empty)

ENTRY ACTION:

EXIT ACTION:

TYPE: subscriber

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 SUBSCRIBER PAGE 2 OF 2

RA COTS ORM

-------------------------------------------------------------------------------

RECEIVING APPLICATION: RA-COTSCLIENT

RESPONSE MESSAGE TYPE: ACK EVENT TYPE: O01

SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

SECURITY REQUIRED?: NO

LOGICAL LINK: RA-COTS

PROCESSING RTN:

ROUTING LOGIC:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

NAME: RA COTS ORU ITEM TEXT: TCP Client

TYPE: subscriber PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

RECEIVING APPLICATION: RA-COTSCLIENT EVENT TYPE: R01

LOGICAL LINK: RA-COTS VERSION ID: 2.3.1

RESPONSE MESSAGE TYPE: ACK SENDING FACILITY REQUIRED?: NO

RECEIVING FACILITY REQUIRED?: NO SECURITY REQUIRED?: NO

HL7 INTERFACE SETUP PAGE 1 OF 2

-------------------------------------------------------------------------------

NAME: RA COTS ORU

DESCRIPTION (wp): (empty)

ENTRY ACTION:

EXIT ACTION:

TYPE: subscriber

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 SUBSCRIBER PAGE 2 OF 2

RA COTS ORU

-------------------------------------------------------------------------------

RECEIVING APPLICATION: RA-COTSCLIENT

RESPONSE MESSAGE TYPE: ACK EVENT TYPE: R01

SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

SECURITY REQUIRED?: NO

LOGICAL LINK: RA-COTS

PROCESSING RTN:

ROUTING LOGIC:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

NAME: RA REG 2.3.1

ITEM TEXT: Rad/Nuc Med exam registered for HL7 v2.3 message

TYPE: event driver PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is triggered whenever a Radiology/Nuclear

Medicine exam is registered. It executes code that creates an HL7 ORM version

2.3 message consisting of PID, ORC, OBR, and OBX segments. The message

contains all relevant information about the exam, including procedure, time

of registration, procedure modifiers, patient allergies, and clinical history.

SENDING APPLICATION: RA-RADSERVER TRANSACTION MESSAGE TYPE: ORM

EVENT TYPE: O01 VERSION ID: 2.3.1

SUBSCRIBERS: RA COTS ORM

HL7 INTERFACE SETUP PAGE 1 OF 2

-------------------------------------------------------------------------------

NAME: RA REG 2.3.1

DESCRIPTION (wp): \[This protocol is triggered whenever a Radiology\]

ENTRY ACTION:

EXIT ACTION:

TYPE: event driver

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 EVENT DRIVER PAGE 2 OF 2

RA REG 2.3

-------------------------------------------------------------------------------

SENDING APPLICATION: RA-RADSERVER

TRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01

PROCESSING ID: VERSION ID: 2.3.1

ACCEPT ACK CODE: APPLICATION ACK TYPE:

RESPONSE PROCESSING RTN:

SUBSCRIBERS

RA COTS ORM

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for Help Insert

NAME: RA CANCEL 2.3.1 ITEM TEXT: Rad/Nuc Med exam cancellation

TYPE: event driver PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is triggered whenever a Radiology/Nuclear

Medicine exam is cancelled. It executes code that creates an HL7 ORM version

2.3 message consisting of PID,ORC, OBR, and OBX segments. The message

contains all relevant information about the exam, including procedure, time of

cancellation, procedure modifiers, patient allergies and clinical history.

SENDING APPLICATION: RA-RADSERVER TRANSACTION MESSAGE TYPE: ORM

EVENT TYPE: O01 VERSION ID: 2.3.1

SUBSCRIBERS: RA COTS ORM

HL7 INTERFACE SETUP PAGE 1 OF 2

-------------------------------------------------------------------------------

NAME: RA CANCEL 2.3.1

DESCRIPTION (wp): \[This protocol is triggered whenever a Radiology\]

ENTRY ACTION:

EXIT ACTION:

TYPE: event driver

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 EVENT DRIVER PAGE 2 OF 2

RA CANCEL 2.3

-------------------------------------------------------------------------------

SENDING APPLICATION: RA-RADSERVER

TRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01

PROCESSING ID: VERSION ID: 2.3

ACCEPT ACK CODE: APPLICATION ACK TYPE:

RESPONSE PROCESSING RTN:

SUBSCRIBERS

RA COTS ORM

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

NAME: RA EXAMINED 2.3 ITEM TEXT: Rad/Nuc Med examines case

TYPE: event driver PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is triggered whenever a Radiology/Nuclear

Medicine exam has reached a status where GENERATE EXAMINED HL7 MSG is Y at

that (or at a lower) status. This message contains all relevant information

about the exam, including procedure, time of registration, procedure

modifiers, patient allergies, and clinical history.

SENDING APPLICATION: RA-RADSERVER TRANSACTION MESSAGE TYPE: ORM

EVENT TYPE: O01 VERSION ID: 2.3

SUBSCRIBERS: RA COTS ORM

HL7 INTERFACE SETUP PAGE 1 OF 2

------------------------------------------------------------------------------

NAME: RA EXAMINED 2.3

DESCRIPTION (wp): \[This protocol is triggered whenever a Radiology\]

ENTRY ACTION:

EXIT ACTION:

TYPE: event driver

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 EVENT DRIVER PAGE 2 OF 2

RA EXAMINED 2.3

------------------------------------------------------------------------------

SENDING APPLICATION: RA-RADSERVER

TRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01

PROCESSING ID: VERSION ID: 2.3

ACCEPT ACK CODE: APPLICATION ACK TYPE:

RESPONSE PROCESSING RTN:

SUBSCRIBERS

RA COTS ORM

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

NAME: RA RPT 2.3

ITEM TEXT: Rad/Nuc Med report released/verified

TYPE: event driver PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is triggered whenever a Radiology/Nuclear

Medicine report enters into a status of Verified or Released/Not Verified. It

executes code that creates an HL7 ORU message consisting of PID, OBR and OBX

segments. The message contains relevant information about the report,

including procedure, procedure modifiers, diagnostic code, interpreting

physician, impression text and report text.

SENDING APPLICATION: RA-RADSERVER TRANSACTION MESSAGE TYPE: ORU

EVENT TYPE: R01 VERSION ID: 2.3

SUBSCRIBERS: RA COTS ORU

HL7 INTERFACE SETUP PAGE 1 OF 2

-------------------------------------------------------------------------------

NAME: RA RPT 2.3

DESCRIPTION (wp): \[This protocol is triggered whenever a Radiology\]

ENTRY ACTION:

EXIT ACTION:

TYPE: event driver

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 EVENT DRIVER PAGE 2 OF 2

RA RPT 2.3

-------------------------------------------------------------------------------

SENDING APPLICATION: RA-RADSERVER

TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

PROCESSING ID: VERSION ID: 2.3

ACCEPT ACK CODE: APPLICATION ACK TYPE:

RESPONSE PROCESSING RTN:

SUBSCRIBERS

RA COTS ORU

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

## Setup of HL7 Files for Two-way Radiology/COTS Interface 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Skip this section if you do not require your interface to allow the COTS product to update Rad/Nuc Med with results messages.

Having followed the previous section to create a Radiology to COTS HL7 interface, you can now setup a COTS to Radiology HL7 interface. This means creating an additional link and two additional protocols.

#### HL Logical Link File \#870 Listener Setup

The link that is required to receive reports from a COTS product will be setup as a listener. HL7 developers strongly recommend that the site’s Multiple Listener, running on port 5000, be used as the listener.. The main benefit being that it is that the multi-listener is capable of handling many connections at once, requires less support, and has proven to be the most reliable type of listener over time.

#### Protocol File \#101 Setup

Two protocols will be required for Radiology to receive reports from a COTS product. An ORU message type subscriber protocol, and an event-driver.

Three event driver protocols (RA VOICE TCP SERVER RPT, RA TALKLINK TCP SERVER RPT and RA PSCRIBE TCP SERVER RPT) were exported with VistA Rad/Nuc Med and subsequent patches.

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 36%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong><br />
Event Driver Protocol</strong></td>
<td><strong><br />
Reason Exported</strong></td>
<td><strong>HL7 Version</strong></td>
<td><strong>Message Type</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>RA TALKLINK TCP SERVER RPT</td>
<td>Event driver for TalkStation rpts</td>
<td>2.3</td>
<td>ORU</td>
</tr>
<tr class="even">
<td>RA PSCRIBE TCP SERVER RPT</td>
<td>Event driver for PowerScribe rpts</td>
<td>2.3</td>
<td>ORU</td>
</tr>
</tbody>
</table>

Three subscriber protocols (RA VOICE TCP REPORT, RA TALKLINK TCP REPORT, RA PSCRIBE REPORT) were also exported and were added to the SUBSCRIBERS multiple of their respective event driver protocols.

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 35%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong><br />
Subscriber Protocol</strong></td>
<td><strong><br />
Reason Exported</strong></td>
<td><strong>HL7 Version</strong></td>
<td><strong>Message Type</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>RA TALKLINK TCP REPORT</td>
<td>TalkStation subscriber protocol</td>
<td>2.3</td>
<td>ORU</td>
</tr>
<tr class="even">
<td>RA PSCRIBE TCP REPORT</td>
<td>PowerScribe subscriber protocol</td>
<td>2.3</td>
<td>ORU</td>
</tr>
</tbody>
</table>

These event driver and subscriber protocols can be used but are best viewed as examples of COTS-Radiology subscribers. When creating new protocols, the subscriber protocol must be entered in the SUBSCRIBERS multiple of the event driver protocol.

The subscriber protocol requires a Processing Routine to be defined. This will be the name of an M routine which processes the inbound report message and updates VistA Radiology accordingly. If an acknowledgment needs to be returned to the sending COTS product, the code should call GENACK^HLMA1. Rad/Nuc Med exports one Processing Routine, RAHLTCPB, which can be used as an example. This Processing Routine is used for the PowerScribe and TalkStation interfaces and is therefore generic by design.

NAME: RA COTS TCP REPORT ITEM TEXT: Client for COTS TCP rpt

TYPE: subscriber PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: Subscriber protocol for sending report to VistA

Radiology/Nuclear Medicine. This protocol is used by the HL7 package to

process messages sent to VistA from a COTS unit using TCP/IP for message flow.

RECEIVING APPLICATION: RA-RADSERVER EVENT TYPE: R01

LOGICAL LINK: COTS-RA VERSION ID: 2.3

RESPONSE MESSAGE TYPE: ACK PROCESSING ROUTINE: D REP^ZZRAHL7

SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

SECURITY REQUIRED?: NO

HL7 INTERFACE SETUP PAGE 1 OF 2

------------------------------------------------------------------------------

NAME: RA COTS TCP REPORT

DESCRIPTION (wp): \[Subscriber protocol for sending report to VistA\]

ENTRY ACTION:

EXIT ACTION:

TYPE: subscriber

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 SUBSCRIBER PAGE 2 OF 2

RA COTS TCP REPORT

------------------------------------------------------------------------------

RECEIVING APPLICATION: RA-RADSERVER

RESPONSE MESSAGE TYPE: ACK EVENT TYPE: R01

SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

SECURITY REQUIRED?: NO

LOGICAL LINK: COTS-RA

PROCESSING RTN: D RPT^ZZHL7RA

ROUTING LOGIC:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

NAME: RA COTS TCP REPORT SERVER

ITEM TEXT: COTS product sends report to VistA

TYPE: event driver PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

SENDING APPLICATION: RA-COTSCLIENT TRANSACTION MESSAGE TYPE: ORU

EVENT TYPE: R01 VERSION ID: 2.3

SUBSCRIBERS: RA COTS TCP REPORT

HL7 INTERFACE SETUP PAGE 1 OF 2

------------------------------------------------------------------------------

NAME: RA COTS TCP REPORT SERVER

DESCRIPTION (wp): (empty)

ENTRY ACTION:

EXIT ACTION:

TYPE: event driver

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 EVENT DRIVER PAGE 2 OF 2

RA COTS TCP REPORT SERVER

------------------------------------------------------------------------------

SENDING APPLICATION: RA-COTSCLIENT

TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

PROCESSING ID: VERSION ID: 2.3

ACCEPT ACK CODE: APPLICATION ACK TYPE:

RESPONSE PROCESSING RTN:

SUBSCRIBERS

RA COTS TCP REPORT

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

## Message Flow Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following chart shows the message flow for each of the 4 event point messages generated by VistA Rad/Nuc Med, and also for the report message generated by COTS product. Two HL7 links are required for this interface:

- One to send new orders, (i.e., registration data, cancels, examined messages, and reports) to COTS product, and to receive ACK’s from COTS product for these orders, and
- A second to receive reports from COTS product and send ACK’s to COTS product.

Because the Rad/Nuc Med report messages are broadcast messages, even the reports that originate from a COTS product are sent back out to all broadcast recipients, including the same COTS product.

### Scenario 1 - VA Sends Order or Report Messages to the COTS Product Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### VA Rad/Nuc Med Sends Order Message (ORM) to COTS Product Server

There are 3 varieties of this message – a) new registration, b) cancelled exam, and c) exam images collected.

File \#771

(server application)

RA-RADSERVER

File \#101

(protocol) RA REG 2.3, RA CANCEL 2.3, or RA EXAMINED 2.3

(item) RA COTS ORM

(File \#771 client subscriber) RA-COTSCLIENT

(File \#870 logical link) RA-COTS (tcp/ip address) <span class="mark">REDACTED</span>

(tcp/ip port) 7077 (vendor's ORDER_PORT)

#### VA Rad/Nuc Med Sends Verified or Preliminary (Released/Not Verified) Report Order Message (ORU) to COTS Product Server

This is similar to order message above, but HL7 requires different protocol setup because the message type is ORU rather than ORM.

File \#771

(server application)

RA-RADSERVER

File \#101

(protocol) RA RPT 2.3

(item) RA COTS ORU

(File \#771 client subscriber) RA-COTSCLIENT

(File \#870 logical link) RA-COTS (tcp/ip address) <span class="mark">REDACTED</span>

(tcp/ip port) 7078 (vendor’s ORDER_PORT)

#### COTS Product Server Sends Acknowledgment for Order Message or Report Message To VA

(File \#870 logical link) RA-COTS (tcp/ip address) <span class="mark">REDACTED</span>

(tcp/ip port) 7077 (vendor’s ORDER_PORT)

### Scenario 2 - Processing Reports from COTS Product Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Cots Product Server Sends Report Message (ORU) To VA

(File \#870 logical link) VAHIN (tcp/ip port) 5000 (vendor’s REPORT_PORT)

#### VA Sends Report Acknowledgment To COTS Product Server

(server application)

RA-COTSCLIENT

(protocol) RA COTS TCP REPORT SERVER

(subscriber)RA COTS TCP REPORT

(File \#101 client subscriber) RA-RADSERVER

(File \#870 logical link) VAHIN

(tcp/ip port) 5000(vendor’s REPORT_PORT)

Notes: VistA orders are sent to the COTS server's TCP/IP address, <span class="mark">REDACTED</span> Acknowledgments of those orders are sent back on the same link.  
  
Reports are sent to the VistA TCP/IP address of our listener link. VistA sends acknowledgments of those reports back over the same link.

## Startup and Recovery

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### One-way TCP/IP Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With a one-way interface from Radiology you will only have one link, similar to the RA-COTS link described earlier. The link can be stopped and started using the HL7 Main Menu, Filer and Link Management Options ..., Start/Stop Links option.

The link status will be shown on the Systems Link Monitor. Once opened the link usually toggles between LISTEN and READING. If the link status toggles between OPEN and OPENFAIL then the link has been unable to start. Most likely the COTS product service is not available for connection on the defined TPC/IP address and port.

### Two-way TCP/IP Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are using a two-way TCP/IP interface with two links; the site’s multi-listener link, like the VAHIN (using Hines as an example) link described earlier; and a sender link, like the RA-COTS link described earlier; you need to stop and start the RA-COTS link following the guidelines.

UCX Multi-Threaded Listener System

1.  Stop ONLY the VistA HL7 sender link using the HL7 Main Menu, Filer and Link Management Options ..., Start/Stop Links option. You do NOT need to shut down the UCX listener link because generic UCX tools control this service.
8.  Start ONLY the VistA HL7 sender link using the HL7 Main Menu, Filer and Link Management Options ..., Start/Stop Links option. The UCX listener link is a UCX service and will be started by UCX when Open VMS is brought up.

The status of the RA-COTS link will be shown on the Systems Link Monitor. If the sender link status toggles between OPEN and OPENFAIL then the link has been unable to start. Most likely the COTS product service is not available for connection on the defined TPC/IP address and port.

## VistA HL7 Message Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At times, you may find it necessary to look at the actual HL7 messages stored on file to find out more information on an order or report message.

HL7 Message Headers are stored on File \#773, the HL7 Message Administration file, and the associated message text is stored in File \#772, the HL7 Message Text file.

For a much more detailed discussion on VistA HL7 message files and interface debugging see the VistA HL7 Site Manager & Developer Manual.

Next is an example of an Examined message, which was created by the COTS example interface described above. Messages can be selected by Date/Time Entered.

#### File \#773: HL7 Message Administration

NUMBER: 68438 DATE/TIME ENTERED: APR 11,2000@11:47:32

MESSAGE ID: 49968438 TRANSMISSION TYPE: OUTGOING

PRIORITY: DEFERRED INITIAL MESSAGE: APR 11, 2000@11:47:32

LOGICAL LINK: RA-COTS SUBSCRIBER PROTOCOL: RA COTS ORM

SENDING APPLICATION: RA-RADSERVER RECEIVING APPLICATION: RA-COTSCLIENT

MESSAGE TYPE: ORM EVENT TYPE: O01

MSH: MSH\|^~\\\|RA-RADSERVER\|VistA RADIOLOGY\|RA-COTSCLIENT\|COTS EXAMPLE

\|20000411114732-0600\|ORM^O01\|49968438\|P\|2.3\|\|\|US

STATUS: SUCCESSFULLY COMPLETED

STATUS UPDATE DATE/TIME: APR 21, 2000@09:56:21

RETRANSMISSIONS: 1

DATE/TIME PROCESSED: APR 21, 2000@09:56:21

#### File \#772: HL7 Message Text

DATE/TIME ENTERED: APR 11, 2000@11:47:32

SERVER APPLICATION: RA-RADSERVER TRANSMISSION TYPE: OUTGOING

MESSAGE ID: 49980527 PARENT MESSAGE: APR 11, 2000@11:47:32

PRIORITY: DEFERRED RELATED EVENT PROTOCOL: RA EXAMINED 2.3

MESSAGE TYPE: SINGLE MESSAGE

MESSAGE TEXT:

PID\|345-67-0987^^\|24^0^M10\|\|LANDO^JOSEPH\|\|19570105\|M\|\|\|\|\|\|345670987\|

ORC\|XO\|\|\|CM\|\|\|20000411114732\|

OBR\|041000-802\|6999589.8799-1^041000-802^L\|74020^X-RAY EXAM OF

ABDOMEN^C4^174^ABDOMEN 3 OR MORE VIEWS^99RAP\|\|20000411114732\|""\|

""\|\|\|""\|\|1895^SHAMUKHAMEDOV^SHAVKAT\|\|2ASM\|\|4^X-RAY CLINIC^49

9^SUPPORT ISC\|RAD^GENERAL RADIOLOGY\|20000411114732\|\|\|^^^^^R

OBX\|\|CE\|P^PROCEDURE^L\|\|174^ABDOMEN 3 OR MORE VIEWS^L\|\|\|\|\|\|X

OBX\|\|TX\|M^MODIFIERS^L\|\|LEFT\|\|\|\|\|\|X

OBX\|\|CE\|C4^CPT MODIFIERS^C4\|\|26^PROFESSIONAL COMPONENT^C4^09926^PROFESSIONAL

COMPONENT^C4\|\|\|\|\|\|X

OBX\|\|TX\|H^HISTORY^L\|\|test for multiexam for one visit \|\|\|\|\|\|X

OBX\|\|TX\|TCM^TECH COMMENT^L\|\|This is a Tech Comment\|\|\|\|\|\|X [^12]

STATUS: SUCCESSFULLY COMPLETED

DATE/TIME PROCESSED: APR 11, 2000@11:47:33

NO. OF CHARACTERS IN MESSAGE: 509 NO. OF EVENTS IN MESSAGE: 1

*This page intentionally left blank*

# Implementing and Maintaining an Interface between Radiology and the TalkStation Voice Reporting Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the steps required to setup and maintain a link between VistA Rad/Nuc Med and the TalkStation COTS Voice Recognition System.

This is a two-way TCP/IP HL7 interface using two links for message transactions. The sender link, RA-TALK, has been exported by Rad/Nuc Med and subsequent patches to send order messages to TalkStation. The listener link, TALK-RA, has been exported by Rad/Nuc Med to receive reports from TalkStation. Message acknowledgments are sent across the same link as the originating message.

On the TalkStation server, the TalkStation Link service must be running to complete the links and allow message flow to begin.

## Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All released Radiology, HL7 and Kernel patches should be installed. In particular, HL7 patch HL\*1.6\*57, and Rad/Nuc Med patch RA\*5\*17.

A TalkStation server should also be installed on the network with a permanent TCP/IP address which is reachable from Vista.

Consider putting the TalkStation server PC on a UPS. Power blips and outages have proven to be a problem in reliable message transmission.

## Operational Features of the Interface 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  When an exam is registered, it should be retrievable in the TalkStation database, and you should be able to enter a report for it.
2.  When an exam is cancelled or deleted, it should be removed from the TalkStation database, and you should not be able to enter a report for it.
3.  If a verified report exists on the VistA Rad/Nuc Med system for an exam, you should no longer be able to enter a report on TalkStation. However, you should be able to enter addenda on TalkStation.
4.  An addendum entered on TalkStation should cause the report on VistA to be automatically unverified, updated, and re-verified. The contents of the re-verified report should be viewable through VistA’s options: Supervisor menu, then Access Uncorrected Reports. (Although TalkStation does not receive a message when the report is unverified, TalkStation will receive a message when the report is re-verified.)
5.  If a TalkStation report is rejected by VistA Rad/Nuc Med software, the report should NOT be filed in the Rad/Nuc Med Report database. The rejected report will remain available on TalkStation, in Preliminary status, for correction.
6.  If a diagnostic code that is entered via TalkStation is not an entry in File \#78.3, DIAGNOSTIC CODES, the report should be rejected with an appropriate error message.
7.  If an unauthorized user attempts to enter a report on the TalkStation unit, the report should be rejected with an appropriate error message.
8.  n unauthorized user is someone who either (1) doesn't have a Rad/Nuc Med staff or resident classification or (2) has a classification inactive date that is prior to the report date.
9.  If a resident or staff interpreting physician without the RA VERIFY key enters a report on TalkStation, the report should be filed, but should be in a ‘DRAFT’ status (or a ‘RELEASED/NOT VERIFIED’ status if site parameters allow it).
10. If the division where the exam was performed does not allow residents to verify reports, reports entered on TalkStation by residents should go into ‘DRAFT’ status (or a ‘RELEASED/NOT VERIFIED’ status if site parameters allow it).
11. If the division where the exam was performed requires impression text, and the TalkStation report does not include impression text, the report should be rejected with an appropriate error message.
12. If the impression text or the report text consists of a single character or any number of special (non-alphanumeric) characters, the report should be rejected with an appropriate error message.
13. If a TalkStation report is transmitted at the same time a user is entering a report for the same case through VistA Rad/Nuc Med in the Report Entry/Edit option, the TalkStation report should be rejected with an appropriate error message.
14. If a TalkStation report is transmitted at the same time a user is case editing a case that is a member of the same printset, the TalkStation report should be rejected with an appropriate error message.
15. If a TalkStation report is transmitted at the same time a user is status tracking a case that is a member of the same printset, the TalkStation report should be rejected with an appropriate error message.
16. If the TalkStation user does not have security privileges to verify a report, the report should be rejected with an appropriate error message. Requirements include the RA VERIFY key, no INACTIVE DATE in File \#200, Field \#53.4 (e.g., the verifier must be an active provider), Rad/Nuc Med staff or resident classification if site parameters allow residents to verify, or staff classification if site parameters don’t allow residents to verify.
17. Reports entered through TalkStation should be viewable, printable, etc. through VistA Rad/Nuc Med, Health Summary, mail messages, and alerts in a way identical to that of reports entered through VistA Rad/Nuc Med. All options operating on reports should behave the same whether the source of the report was VistA or TalkStation.
18. TalkStation reports may include an electronic signature. This will be visible when the report is displayed or printed on Vista. Electronic signatures will only appear on the VistA report if the Rad/Nuc Med Division (file \#79) parameter ALLOW E-SIG ON COTS HL7 RPTS is set.
19. When a TalkStation report for a printset is transmitted and results in an accepted, verified report on VistA, all members of the printset on VistA should now include the same report when retrieved through patient profiles, View Exam by Case No., etc. Also, the report content should include the procedures for all members of the set.

> [^13]

20. If a report is entered in TalkStation as ‘preliminary’, when it reaches Vista, it should be set to ‘DRAFT’ or, if the site parameters allow, ‘RELEASED/NOT VERIFIED’.
21. At integrated sites using more than one COTS Voice Reporting system, it may be necessary to limit messages to specific Divisions for optimal performance. This can be achieved by using ROUTING LOGIC, as described later in this section.[^14]

## IRM and ADPAC Setup Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Most of the VistA HL7 file setup has been done by the installation of RA\*5.0\*17, but some must be manually completed by IRM. See a sample of the VistA setup in Setup of HL7 Files, later in this section.

1.  You must provide the TCP/IP address for the TalkStation unit and TCP/IP port numbers for both VistA and TalkStation. See a sample of the VistA setup in Setup of HL7 Files, later in this appendix.

> **NOTE:** You will only be required to put in a TCP/IP Address for the listener on Cache for NT sites.

9.  The Rad/Nuc Med coordinator who supports the TalkStation unit must follow the TalkStation documentation/instructions for proper user definition. The Physician ID field in the TalkStation user set-up must be identical to the corresponding internal entry number of the VistA New Person file \#200. This ensures that the correct name will be entered as the verifying physician for medical/legal purposes. Reports will be rejected if the TalkStation user is not identical to the entry in the New Person file.
10. If electronic signature is to be allowed across the interface, the Rad/Nuc Med coordinator must initialize the parameters in the RAD/NUC MED DIVISION file \#79 to allow this feature. Set field \#.127 ‘ALLOW E-SIG ON COTS HL7 RPTS’ to yes. All reports with an HL7 status of Final, or Addendum, will be filed in the Rad/Nuc Med Reports file \#74 with the electronic signature block printed name defined in file \#200 of the verifying physician who signed the report on the TalkStation unit. Before a report can be filed in VistA with an electronic signature, it must pass all validation processes outlined in the section on Operational Features later in this appendix.

> **WARNING:** See the Rad/Nuc Med Technical Manual section on Security for further electronic signature information.

11. At integrated sites using more than one COTS Voice Reporting system, it may be necessary to limit messages to specific Divisions for optimal performance.[^15] This can be achieved by setting the ROUTING LOGIC field to 'D ^RAHLROUT' for all subscriber protocols in use by Radiology HL7 event drivers (RA REG 2.3, RA CANCEL 2.3, RA EXAMINED 2.3, RA RPT 2.3). The ROUTING LOGIC routine, ^RAHLROUT, will check the HL7 RECEIVING APPLICATIONS multiple field in the Rad/Nuc Med Division file (#79). If this field includes 'RA-TALKLINK-TCP', then messages created in the Division will be passed to TalkStation, otherwise they will not be sent to TalkStation.
12. The Rad/Nuc Med coordinator who supports the TalkStation unit must follow the TalkStation documentation/instructions for defining Rad/Nuc Med Diagnostic Codes. However TalkStation is pre-loaded to use ICD9 codes; these will have to be removed before entering VistA Diagnostic Codes. An SQL command, run on the TalkStation server, of ‘delete from icd9’ should accomplish this. Diagnostic Codes entered on the TalkStation unit must be identical to the active diagnostic codes in VistA File \#78.3. Use the TalkRIS ICD9 option documented in the TalkRIS User Guide Chapter 9.

![](radiology-version-5-hl7-setup-manual/002.png)Talk RIS\>ICD9 Codes\>Add/Update ICD9 Codes

13. Make sure all other TalkStation setup is correct and complete according to TalkStation documentation.
14. If the TalkStation interface is moved from a test account to the production account, update the TCP/IP port numbers on both sides, and delete the TalkStation database (using SQL commands) to prevent cross-over of test data to the live account. (The change of port numbers ensures a unique socket connection. But the TCP/IP address of the TalkStation remains the same.)
15. It is very helpful to synchronize the TalkStation PC clock to closely agree with the VistA system clock.
16. Responsibility for starting, stopping, and monitoring the links can belong to IRM, or IRM can delegate this to the Rad/Nuc Med coordinator with the understanding that if problems occur, IRM may have to provide support.
17. TalkStation users and IRM should learn how to find and interpret error messages for rejected reports. If VistA Rad/Nuc Med rejects a report sent by TalkStation, an error message is sent back to TalkStation. If the error is returned by Radiology, rather than the HL7 software, then it will be logged in the HL7 Message Exceptions file \#79.3 and can be viewed using the Rad/Nuc Med HL7 Voice Reporting Errors option. Additionally, setting a MAIL GROUP for the TalkStation application in the HL7 APPLICATION PARAMETERS file (#771) will mean that these errors will also be sent as mail messages to the defined mail group and the verifying physician.[^16]
18. This interface requires link tasks to always start up on the same node. So, if your site is an Alpha/AXP site running more than one instance of TaskMan, you must start up TaskMan in DCL context. Consult the Kernel System Manual for instructions on running TaskMan in DCL context.

## Setup of HL7 Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All of the setup, except for site-specific fields, was done automatically by the Rad/Nuc Med patch RA\*5.0\*17. However, the site is responsible for entering the TCP/IP address, TCP/IP port numbers, Startup Node and other fields that are site-specific (these items are shown in bold).

A sample setup follows. IRM should only populate the fields in bold print. Your responses should be specific to your site, and not necessarily what you see below. The VistA screen shots are taken from the HL7 Main Menu, Interface Developers Option. Windows style screen shots are taken from the TalkStation/Link utility.

#### HL7 Application Parameter File \#771 Setup

NAME: RA-TALKLINK-TCP ACTIVE/INACTIVE: ACTIVE

> FACILITY NAME: TALKSTATION MAIL GROUP:[^17] RAD HL7 REJECTIONS COUNTRY CODE: US HL7 ENCODING CHARACTERS: ^~\\

HL7 FIELD SEPARATOR: \|

HL7 APPLICATION EDIT

------------------------------------------------------------------------------

NAME: RA-TALKLINK-TCP ACTIVE/INACTIVE: ACTIVE

FACILITY NAME: TALKSTATION\<- enter name COUNTRY CODE: US

HL7 FIELD SEPARATOR: \| HL7 ENCODING CHARACTERS: ^~\\

MAIL GROUP:[^18] RAD HL7 REJECTIONS \<-- optional mail group defined

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

NAME: RA-VOICE-SERVER ACTIVE/INACTIVE:ACTIVE

FACILITY NAME: VistA RADIOLOGY MAIL GROUP:[^19] RAD HL7 REJECTIONS

COUNTRY CODE: US HL7 ENCODING CHARACTERS: ^~\\

HL7 FIELD SEPARATOR: \|

HL7 APPLICATION EDIT

------------------------------------------------------------------------------

NAME: RA-VOICE-SERVER ACTIVE/INACTIVE: ACTIVE

FACILITY NAME: VistA RADIOLOGY\<- enter name COUNTRY CODE: US

HL7 FIELD SEPARATOR: \| HL7 ENCODING CHARACTERS: ^~\\

MAIL GROUP:[^20] RAD HL7 REJECTIONS \<-- optional mail group defined

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

Notes: See vendor documentation for more information on TalkStation setup. The following items are a subset that correlate to VistA setup.  
  
TalkStation settings can be altered using the TalkStation/Link application (Start Button, Settings, Control Panel, TalkStation Link). Click the RisHL7 tab and enter the same application names as the HL7 Application Parameter file. In this example the following values would be entered:

> Sending App: RA-TALKLINK-TCP

> Sending Fac.: TALKSTATION

> Receiving App: RA-VOICE-SERVER

> Receiving Fac.: VistA RADIOLOGY

Although the values of Sending Facility and Receiving Facility are unimportant, they must match in TalkStation/Link and VistA HL7 Application Parameter file \#771.

TalkStation/Link includes a box to define the OBX-3 format used by VistA Rad/Nuc Med for clinical history, allergies, and modifiers. The line that should appear in this box is:

OBX filter for order notes: (“/”delimited)

> /H^HISTORY^L/A^ALLERGIES^L/M^MODIFIERS^L

> /C4^CPT MODIFIERS^C4/TCM^TECH COMMENT^L [^21]

The Trigger Event needs to be defined in the RisHL7 tab of the TalkStation/Link Application:  
Trigger Event: R01

For TalkStation, within the TalkStation/Link application and RisHL7 tab, the RIS Type needs to be specified as VA. Set the following:  
RIS Type: VA

To ensure that TalkStation functions correctly the Report and Order modules must be defined. Within the TalkLink Service tab of the TalkStation/Link application choose the following values:  
Report Module: TalkReport

Order Module: RisHL7

If you would like to be able to edit reports that VistA has rejected on TalkStation, then check the ‘Set rejected reports to preliminary’ box in the TalkReport tab. (Recommended).

TalkStation will recognize the Observation Value and several other VistA specifics if, in the TalkStation System Preferences, the ‘Use VA (Veteran’s Administration) settings’ option is checked within the Workflow tab; and the ‘Use TalkLink’ option within the Local Machine tab is checked.

In TalkStation/Link, within the TalkReport tab, ‘Allow combined reports’ should not be set. Similarly, in the TalkStation System Preferences Workflow tab, ‘Break up combined results’ should not be set. If either option is checked then printsets will not be handled correctly by the interface.

![](radiology-version-5-hl7-setup-manual/003.png)

![](radiology-version-5-hl7-setup-manual/004.png)![](radiology-version-5-hl7-setup-manual/005.png)

Screen Captures of TalkStation Link Properties

#### #### <u> </u>HL Logical Link File \#870 Setup

This file contains the links used by the HL7 package to send messages. It is used to identify the TCP/IP address of the TalkStation unit, as well as the TCP/IP port numbers that will be used. These addresses are all site-specific and must be entered by IRM before the links are started.

This file also stores parameters that define the behavior of the lower level protocols and information that is used with the Systems Link Monitor, which gives the user feedback about the state of each link. When a message is received, the link moves from an IDLE state to a READING state. In this sample the link used for the following messages:

> RA-TALK is used to send order messages (i.e., exam registered, exam cancelled, patient examined, and report verified or released/not verified) from VistA to TalkStation. This link also receives the order Acknowledgment from TalkStation.

This sample shows active, run-time data. Some of the fields are populated by Rad/Nuc Med patch RA\*5\*17. The remainder of the fields are populated by the HL7 package when you start up the links.

Although not exported, it is strongly recommended that you add an ACK timeout for the sender link. If you do not enter a value then a default of 10 seconds will be used and experience has shown that this is not enough for a busy TCP/IP network. We recommend using between 300 and 600 seconds.

You may choose to automatically start all HL7 Logical Links and Inbound/Outbound Filers when TaskMan is restarted. To do this, run the TaskMan, Schedule/Unschedule options, select Restart All Links and Filers, and place an ‘S’ in the SPECIAL QUEUEING field. Then, remember to set AUTOSTART to ‘1’ (Enabled) for each link.

Regardless of the ‘Exceed Re-Transmit Action’ entered, when the ‘Re-Transmission Attempts’ for a message is exceeded, an alert is sent to the mail group defined in the MAIL GROUP FOR ALERTS field in the HL COMMUNICATION SERVER PARAMETERS (#869.3) file. This can be edited using the HL7 Main Menu, Site Parameter Edit option.

The RA-TALK sender link is exported as a Persistent Client, but with TalkStation v2.0 or greater it will be possible to change it to a Non-Persistent Client. The advantage of Non-Persistent clients is that the link only connects when required, rather than leaving the process open at all times.

See the VistA HL7 Site Manager & Developer Manual section 2.4 TCP Link Setup for additional field definitions. The values shown below have been proven to work in the past.

NODE: RA-TALK LLP TYPE: TCP

DEVICE TYPE: Persistent Client AUTOSTART: Enabled

RE-TRANSMISSION ATTEMPTS: 3 ACK TIMEOUT: 300

EXCEED RE-TRANSMIT ACTION: ignore TCP/IP ADDRESS: <span class="mark">REDACTED</span>

TCP/IP PORT: 7077 TCP/IP SERVICE TYPE: CLIENT (SENDER)

PERSISTENT: YES STARTUP NODE:

HL7 LOGICAL LINK

-------------------------------------------------------------------------------

NODE: RA-TALK

INSTITUTION:

DOMAIN:

AUTOSTART: Enabled\<- set to Enabled if autostart of link required

QUEUE SIZE:

LLP TYPE: TCP \<- hit \<return\> here to edit LLP parameters

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 LOGICAL LINK

-------------------------------------------------------------------------------

┌──────────────────────TCP LOWER LEVEL PARAMETERS─────────────────────────┐

│ RA-TALK │

│ │

│ TCP/IP SERVICE TYPE: CLIENT (SENDER) │

│ TCP/IP ADDRESS: <span class="mark">REDACTED</span> \<- address of TalkStation server │

│ TCP/IP PORT: 7077\<- port TalkStation receives on │

│ │

│ │

│ ACK TIMEOUT: 300\<- recommended RE-TRANSMISION ATTEMPTS: 3 │

│ READ TIMEOUT: EXCEED RE-TRANSMIT ACTION: ignore │

│ BLOCK SIZE: │

│ │

│STARTUP NODE: \<- ONLY set if multiple TaskMan/DCL PERSISTENT: YES │

│ RETENTION: UNI-DIRECTIONAL WAIT: │

└─────────────────────────────────────────────────────────────────────────┘

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Close Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Close Press \<PF1\>H for help Insert

#### <u> </u>Protocol File \#101 Setup

The event driver entries (RA REG 2.3, RA EXAMINED 2.3, RA CANCEL 2.3, RA RPT 2.3 and RA TALKLINK TCP SERVER RPT) are exported with the Rad/Nuc Med VistA patch RA\*5.0\*17 for use with this interface.

Also exported are the subscriber protocols (RA TALKLINK ORM, RA TALKLINK ORU and RA TALKLINK TCP REPORT)

(Refer to the ‘Rad/Nuc Med HL7 Interface Specifications’ section of this document for information about messages initiated by Rad/Nuc Med.)

In order to associate the event driver protocols with the Radiology-TalkStation interface and thereby initiate messages, the TalkStation subscriber protocols need to be added to the associated event driver SUBSCRIBERS multiple.

Once the subscriber protocols are added, messages will be built and will stack up until the links are started.

If ever you need to completely disable the interface and want to stop new messages from being created for this interface, simply remove the TalkStation subscriber protocols from the event driver protocols.

Listed below are examples of the event driver protocols with the subscriber protocols that require addition shown in bold. You may see other subscribers listed on your system, these should not be removed.

Also below are screen shots from the HL7 Main Menu, Interface Developer Options …, Protocol Edit highlighting the steps required to add the subscriber protocols.

The subscriber protocols shown (RA TALKLINK ORM and RA TALKLINK ORU) are setup to use ROUTING LOGIC to filter messages depending on Division. This is not the usual situation, but is shown to highlight how this can be achieved.[^22]

> **NOTE:** If the ROUTING LOGIC field is set, but no Rad/Nuc Med Division file (#79) has 'RA-TALKLINK-TCP' as an HL7 RECEIVING APPLICATION, then no messages will be sent to TalkStation.

If other subscriber protocols exist for the event drivers (RA REG 2.3, RA CANCEL 2.3, RA EXAMINED 2.3, RA RPT 2.3), for example RA PSCRIBE ORM, then these will also need to be setup to use ROUTING LOGIC. Otherwise all HL7 subscribers will receive messages from all divisions, and all messages will still be passed to TalkStation.

If in doubt, do not set the ROUTING LOGIC field.

NAME: RA REG 2.3

ITEM TEXT: Rad/Nuc Med exam registered for HL7 v2.3 message

TYPE: event driver PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is triggered whenever a Radiology/Nuclear

Medicine exam is registered. It executes code that creates an HL7 ORM version

2.3 message consisting of PID, ORC, OBR, and OBX segments. The message

contains all relevant information about the exam, including procedure, time

of registration, procedure modifiers, patient allergies, and clinical history.

SENDING APPLICATION: RA-VOICE-SERVER TRANSACTION MESSAGE TYPE: ORM

EVENT TYPE: O01 VERSION ID: 2.3

SUBSCRIBERS: RA TALKLINK ORM

HL7 INTERFACE SETUP PAGE 1 OF 2

-------------------------------------------------------------------------------

NAME: RA REG 2.3

DESCRIPTION (wp): \[This protocol is triggered whenever a Radiology\]

ENTRY ACTION:

EXIT ACTION:

TYPE: event driver hit \<return\> here to edit event driver details

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 EVENT DRIVER PAGE 2 OF 2

RA REG 2.3

-------------------------------------------------------------------------------

SENDING APPLICATION: RA-VOICE-SERVER

TRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01

PROCESSING ID: VERSION ID: 2.3

ACCEPT ACK CODE: APPLICATION ACK TYPE:

RESPONSE PROCESSING RTN:

SUBSCRIBERS

RA TALKLINK ORM add this subscriber

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for Help Insert

NAME: RA CANCEL 2.3 ITEM TEXT: Rad/Nuc Med exam cancellation

TYPE: event driver PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is triggered whenever a Radiology/Nuclear

Medicine exam is cancelled. It executes code that creates an HL7 ORM version

2.3 message consisting of PID,ORC, OBR, and OBX segments. The message

contains all relevant information about the exam, including procedure, time of

cancellation, procedure modifiers, patient allergies and clinical history.

SENDING APPLICATION: RA-VOICE-SERVER TRANSACTION MESSAGE TYPE: ORM

EVENT TYPE: O01 VERSION ID: 2.3

SUBSCRIBERS: RA TALKLINK ORM

HL7 INTERFACE SETUP PAGE 1 OF 2

-------------------------------------------------------------------------------

NAME: RA CANCEL 2.3

DESCRIPTION (wp): \[This protocol is triggered whenever a Radiology\]

ENTRY ACTION:

EXIT ACTION:

TYPE: event driver \<- hit \<return\> here to edit event driver details

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 EVENT DRIVER PAGE 2 OF 2

RA CANCEL 2.3

-------------------------------------------------------------------------------

SENDING APPLICATION: RA-VOICE-SERVER

TRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01

PROCESSING ID: VERSION ID: 2.3

ACCEPT ACK CODE: APPLICATION ACK TYPE:

RESPONSE PROCESSING RTN:

SUBSCRIBERS

RA TALKLINK ORM\<- add this subscriber

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

NAME: RA EXAMINED 2.3 ITEM TEXT: Rad/Nuc Med examines case

TYPE: event driver PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is triggered whenever a Radiology/Nuclear

Medicine exam has reached a status where GENERATE EXAMINED HL7 MSG is Y at

that (or at a lower) status. This message contains all relevant information

about the exam, including procedure, time of registration, procedure

modifiers, patient allergies, and clinical history.

SENDING APPLICATION: RA-VOICE-SERVER TRANSACTION MESSAGE TYPE: ORM

EVENT TYPE: O01 VERSION ID: 2.3

SUBSCRIBERS: RA TALKLINK ORM

HL7 INTERFACE SETUP PAGE 1 OF 2

------------------------------------------------------------------------------

NAME: RA EXAMINED 2.3

DESCRIPTION (wp): \[This protocol is triggered whenever a Radiology\]

ENTRY ACTION:

EXIT ACTION:

TYPE: event driver \<- hit \<return\> here to edit event driver details

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 EVENT DRIVER PAGE 2 OF 2

RA EXAMINED 2.3

-------------------------------------------------------------------------------

SENDING APPLICATION: RA-VOICE-SERVER

TRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01

PROCESSING ID: VERSION ID: 2.3

ACCEPT ACK CODE: APPLICATION ACK TYPE:

RESPONSE PROCESSING RTN:

SUBSCRIBERS

RA TALKLINK ORM\<- add this subscriber

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

NAME: RA RPT 2.3

ITEM TEXT: Rad/Nuc Med report released/verified

TYPE: event driver PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is triggered whenever a Radiology/Nuclear

Medicine report enters into a status of Verified or Released/Not Verified. It

executes code that creates an HL7 ORU message consisting of PID, OBR and OBX

segments. The message contains relevant information about the report,

including procedure, procedure modifiers, diagnostic code, interpreting

physician, impression text and report text.

SENDING APPLICATION: RA-VOICE-SERVER TRANSACTION MESSAGE TYPE: ORU

EVENT TYPE: R01 VERSION ID: 2.3

SUBSCRIBERS: RA TALKLINK ORU

HL7 INTERFACE SETUP PAGE 1 OF 2

-------------------------------------------------------------------------------

NAME: RA RPT 2.3

DESCRIPTION (wp): \[This protocol is triggered whenever a Radiology\]

ENTRY ACTION:

EXIT ACTION:

TYPE: event driver \<- hit \<return\> here to edit driver details

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 EVENT DRIVER PAGE 2 OF 2

RA RPT 2.3

-------------------------------------------------------------------------------

SENDING APPLICATION: RA-VOICE-SERVER

TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

PROCESSING ID: VERSION ID: 2.3

ACCEPT ACK CODE: APPLICATION ACK TYPE:

RESPONSE PROCESSING RTN:

SUBSCRIBERS

RA TALKLINK ORU \<- add this subscriber

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

NAME: RA TALKLINK ORM ITEM TEXT: TCP Client

TYPE: subscriber PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is used in conjunction with the RA REG 2.3, RA

EXAMINED 2.3, and RA CANCEL 2.3 event protocols. It is used by the VistA HL7

package to send ORM messages to TCP/IP recipients. This protocol should be

entered in the SUBSCRIBERS multiple field of those event point protocols if

this type of messaging scenario is used at a facility. This is part of the

file set-up to enable HL7 message flow when exams are registered, cancelled,

and when they reach the status flagged as ‘examined’ by the site.

RECEIVING APPLICATION: RA-TALKLINK-TCP EVENT TYPE: O01

LOGICAL LINK: RA-TALK VERSION ID: 2.3

RESPONSE MESSAGE TYPE: ACK SENDING FACILITY REQUIRED?: NO

RECEIVING FACILITY REQUIRED?: NO SECURITY REQUIRED?: NO

ROUTING LOGIC:[^23] D ^RAHLROUT

HL7 INTERFACE SETUP PAGE 1 OF 2

--------------------------------------------------------------------------------

NAME: RA TALKLINK ORM

DESCRIPTION (wp): \[This protocol is used in conjunction with the R\]

ENTRY ACTION:

EXIT ACTION:

TYPE: subscriber \<- hit \<return\> here to edit subscriber details

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 SUBSCRIBER PAGE 2 OF 2

RA TALKLINK ORM

--------------------------------------------------------------------------------

RECEIVING APPLICATION: RA-TALKLINK-TCP

RESPONSE MESSAGE TYPE: ACK EVENT TYPE: O01

SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

SECURITY REQUIRED?: NO

LOGICAL LINK: RA-TALK

PROCESSING RTN:

ROUTING LOGIC: D ^RAHLROUT \<--only set if using divisional filtering

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

NAME: RA TALKLINK ORU ITEM TEXT: TCP Client

TYPE: subscriber PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is used in conjunction with the RA RPT 2.3 event

point protocol. The HL7 package uses this protocol to send rad/nuc med report

(ORU) messages to TCP/IP recipients. This protocol should be entered in the

SUBSCRIBERS multiple field of the RA RPT protocol if this messaging scenario

is used in a facility. This is part of the file set-up to enable message flow

when a rad/nuc med report is verified.

RECEIVING APPLICATION: RA-TALKLINK-TCP EVENT TYPE: R01

LOGICAL LINK: RA-TALK VERSION ID: 2.3

RESPONSE MESSAGE TYPE: ACK SENDING FACILITY REQUIRED?: NO

RECEIVING FACILITY REQUIRED?: NO SECURITY REQUIRED?: NO

ROUTING LOGIC:[^24] D ^RAHLROUT

HL7 INTERFACE SETUP PAGE 1 OF 2

--------------------------------------------------------------------------------

NAME: RA TALKLINK ORU

DESCRIPTION (wp): \[This protocol is used in conjunction with the R\]

ENTRY ACTION:

EXIT ACTION:

TYPE: subscriber \<- hit \<return\> here to edit subscriber details

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 SUBSCRIBER PAGE 2 OF 2

RA TALKLINK ORU

--------------------------------------------------------------------------------

RECEIVING APPLICATION: RA-TALKLINK-TCP

RESPONSE MESSAGE TYPE: ACK EVENT TYPE: R01

SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

SECURITY REQUIRED?: NO

LOGICAL LINK: RA-TALK

PROCESSING RTN:

ROUTING LOGIC: D ^RAHLROUT \<--only set if using divisional filtering

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

The following protocols, shown without screen shots, are exported as part of the Radiology TalkStation interface, but do not require amendment:[^25]

NAME: RA TALKLINK TCP SERVER RPT

ITEM TEXT: TalkStation TCP sends report to VistA

TYPE: event driver PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

SENDING APPLICATION: RA-TALKLINK-TCP TRANSACTION MESSAGE TYPE: ORU

EVENT TYPE: R01 VERSION ID: 2.3

SUBSCRIBERS: RA TALKLINK TCP REPORT

NAME: RA TALKLINK TCP REPORT ITEM TEXT: Client for TalkStation TCP rpt

TYPE: subscriber PACKAGE: RADIOLOGY/NUCLEAR MEDICINE RECEIVING APPLICATION: RA-VOICE-SERVER EVENT TYPE: R01

LOGICAL LINK: TALK-RA VERSION ID: 2.3

RESPONSE MESSAGE TYPE: ACK PROCESSING ROUTINE: D ^RAHLTCPB

SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

SECURITY REQUIRED?: NO

## Detailed Explanation of Start-up/Recovery Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Stop the appropriate links from the HL7 Main Menu, Filer and Link Management Options ..., Start/Stop Links:

> UCX Multi-Threaded Listener System: Stop only the RA-TALK link. (You do NOT need to shut down the UCX listener. Generic UCX tools control UCX services.)

19. If necessary, boot or reboot the TalkStation unit (i.e., reboot only if an application error occurred on the TalkStation unit, or a previous attempt at recovery has failed). Rebooting can be done using the Start button and selecting ‘Shut Down’. To gain more control over the TalkStation Link service on the TalkStation machine, you can set up these service to start manually rather than auto-start. If set up to auto-start, it should start automatically during reboot.
20. If TalkStation Link is not setup to start automatically on the TalkStation server, or has failed to restart automatically, use the Start button, Settings, Control Panel, Services, then select TalkStation Link to get a pop-up box and click on ‘start’. The status of TalkStation Link should change from null to ‘started’. The status should change to running.
21. On Open-M/Cache systems only, it is a good idea to kill off the logical link listener job (%ZISTCP) before restarting the links. This step is optional, but will prevent an extinct job from unnecessarily using up CPU time. Use the system status utility to find these jobs. They appear as running the %ZISTCP routine using port numbers that you entered as TCP/IP PORT in the setup (i.e., File \#870, Field \#400.02 TCP/IP PORT, for entries RA-TALK and TALK-RA). This step may be unnecessary after additional HL7 package patches.
22. Regarding the site specific “multi-listener link” ’Vaxxx’:

> UCX Multi-Threaded Listener System: No action is needed. The listener is an OpenVMS UCX service and UCX starts running when OpenVMS is brought up.

23. Verify that the listener link is up and running:

> UCX Multi-Threaded Listener System: The OpenVMS UCX service should be enabled. The columns indicating message totals for the TALK-RA HL7 link are accurately reflected in the System Link Monitor. Disregard the information presented in the Device Type and State columns for the TALK-RA HL7 link.

24. Start the “sender” link RA-TALK: From the HL7 Main Menu, Filer and Link Management Options ..., Start/Stop Links.

> Enter RA-TALK at the ‘Select HL LOGICAL LINK NODE:’ prompt, then press enter to accept the default of ‘BACKGROUND’ at the ‘Method for running the receiver;’ prompt.

25. Use the Systems Link Monitor option again to verify that the RA-TALK sender link is up and running. If the TalkStation Link service is not running on the TalkStation server then the RA-TALK link will toggle between an Open and OpenFail state.

## Start-up/Recovery Procedure Quick Reference

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Radiology-TalkStation Interface

|      |             |                                                                                  |                                                                                            |
|------|-------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Step | Machine     | Action                                                                           | Mandatory, Optional, or Conditional                                                        |
| 1    | VistA       | UCX Multi-Threaded Listener System: Shut down the RA-TALK link.                  | Mandatory                                                                                  |
| 2    | TalkStation | Reboot                                                                           | Only if TalkStation application error occurred or TalkStation PC suffered power loss, etc. |
| 3    | TalkStation | Startup TalkStation Link service (if applicable)                                 | Only if down and not set to auto-start                                                     |
| 6    | VistA       | UCX Multi-Threaded Listener System: enable the OpenVMS UCX Service (if disabled) | Mandatory                                                                                  |
| 7    | VistA       | Start the sender logical link: RA-TALK                                           | Mandatory                                                                                  |

> Notes: If the TalkStation TalkStation Link service goes down, the recovery process is necessary.  
> *Shutdown the RA-TALK link*  

> If the VistA machine is going to be shutdown:  
> *Shut down the RA-TALK link.This page intentionally left blank*

# Implementing and Maintaining an Interface between Radiology and the PowerScribe Voice Reporting Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the steps required to setup and maintain a link between VistA Rad/Nuc Med and the PowerScribe COTS Voice Recognition System.

This is a two-way TCP/IP HL7 interface using two links for message transactions. The sender link, RA-PSCRIBE, has been exported by Rad/Nuc Med and subsequent patches to send order messages to PowerScribe. The listener link, PSCRIBE-RA, has been exported by Rad/Nuc Med to receive reports from PowerScribe. Message acknowledgments are sent across the same link as the originating message.

On the PowerScribe server, the HL7CLIENT and HL7CLIENT executables must be running to complete the links and allow message flow to begin

## Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All released Radiology, HL7 and Kernel patches should be installed. In particular, HL7 patch HL\*1.6\*57, and Rad/Nuc Med patch RA\*5\*17.

A PowerScribe server should also be installed on the network with a permanent TCP/IP address which is reachable from VistA.

Consider putting the PowerScribe PC on a UPS. Power blips and outages have proven to be a problem in reliable message transmission.

## Operational Features of the Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  When an exam is registered, it should be retrievable in the PowerScribe database, and you should be able to enter a report for it.
26. When an exam is cancelled or deleted, it should be removed from the PowerScribe database, and you should not be able to enter a report for it.
27. If a verified report exists on the VistA Rad/Nuc Med system for an exam, you should no longer be able to enter a report on PowerScribe.
28. If a PowerScribe report is rejected by VistA Rad/Nuc Med software, the report should NOT be filed in the Rad/Nuc Med Report database.
29. If a diagnostic code that is entered via PowerScribe is not an entry in File \#78.3, DIAGNOSTIC CODES, the report should be rejected with an appropriate error message.
30. If an unauthorized user attempts to enter a report on the PowerScribe unit, the report should be rejected with an appropriate error message. An unauthorized user is someone who either (1) doesn't have a Rad/Nuc Med staff or resident classification or (2) has a classification inactive date that is prior to the report date.
31. If a resident or staff interpreting physician without the RA VERIFY key enters a report on PowerScribe, the report should be filed, but should be in a ‘DRAFT’ status (or a ‘RELEASED/NOT VERIFIED’ status if site parameters allow it).
32. If the division where the exam was performed does not allow residents to verify reports, reports entered on PowerScribe by residents should go into ‘DRAFT’ status (or a ‘RELEASED/NOT VERIFIED’ status if site parameters allow it).
33. If the division where the exam was performed requires impression text, and the PowerScribe report does not include impression text, the report should be rejected with an appropriate error message.
34. If the impression text or the report text consists of a single character or any number of special (non-alphanumeric) characters, the report should be rejected with an appropriate error message.
35. If a PowerScribe report is transmitted at the same time a user is entering a report for the same case through VistA Rad/Nuc Med in the Report Entry/Edit option, the PowerScribe report should be rejected with an appropriate error message.
36. If a PowerScribe report is transmitted at the same time a user is case editing a case that is a member of the same printset, the PowerScribe report should be rejected with an appropriate error message.
37. If a PowerScribe report is transmitted at the same time a user is status tracking a case that is a member of the same printset, the PowerScribe report should be rejected with an appropriate error message.
38. If the PowerScribe user does not have security privileges to verify a report, the report should be rejected with an appropriate error message. Requirements include the RA VERIFY key, no INACTIVE DATE in File \#200, Field \#53.4 (e.g., the verifier must be an active provider), Rad/Nuc Med staff or resident classification if site parameters allow residents to verify, or staff classification if site parameters don’t allow residents to verify.
39. Reports entered through PowerScribe should be viewable, printable, etc. through VistA Rad/Nuc Med, Health Summary, mail messages, and alerts in a way identical to that of reports entered through VistA Rad/Nuc Med. All options operating on reports should behave the same whether the source of the report was VistA or PowerScribe.
40. If the PowerScribe report has a status of Final or Addendum, it may include an electronic signature in the VistA Rad/Nuc Med report. To include an electronic signature in the VistA Rad/Nuc Med report, the field (#.127) “ALLOW E-SIG ON COTS HL7 RPTS:” in the RAD/NUC MED DIVISION file \#79 must be set to YES.
41. When a PowerScribe report for a printset is transmitted and results in an accepted, verified report on VistA, all members of the printset on VistA should now include the same report when retrieved through patient profiles, View Exam by Case No., etc. Also, the report content should include the procedures for all members of the set.
42. If the site has the GENERATE EXAMINED HL7 MESSAGE field set to ‘yes’ on one or more statuses in File \#72, the “examined” messages generated should have no effect on PowerScribe.
43. If a report is entered in PowerScribe as ‘preliminary’, when it reaches VistA, it should be set to ‘DRAFT’ or, if the site parameters allow, ‘RELEASED/NOT VERIFIED’.

> [^26]

44. At integrated sites using more than one COTS Voice Reporting system, it may be necessary to limit messages to specific Divisions for optimal performance. This can be achieved by using ROUTING LOGIC, as described later in this section.[^27]

## IRM and ADPAC Set-up Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Most of the VistA HL7 file setup will be done by the installation of RA\*5.0\*17, but some must be manually completed by IRM. See a sample of the VistA setup in Setup of HL7 Files, later in this section.

1.  You must provide the TCP/IP address for the PowerScribe unit and TCP/IP port numbers for both VistA and PowerScribe. See a sample of the VistA setup in Setup of HL7 Files, later in this appendix.

> **NOTE:** Depending on your operating system, you may or may not have to put in a TCP/IP Address for the listener.

45. The Rad/Nuc Med coordinator who supports the PowerScribe unit must follow the PowerScribe documentation/instructions for proper user definition. The Physician ID field in the PowerScribe user set-up must be identical to the corresponding internal entry number of the VistA New Person file \#200. This ensures that the correct name will be entered as the verifying physician for medical/legal purposes. Reports will be rejected if the PowerScribe user is not identical to the entry in the New Person file.
46. If electronic signature is to be allowed across the interface, the Rad/Nuc Med coordinator must initialize the parameters in the RAD/NUC MED DIVISION file \#79 to allow this feature. Set field \#.127 ‘ALLOW E-SIG ON COTS HL7 RPTS’ to YES. All reports with an HL7 status of Final, or Addendum, will be filed in the Rad/Nuc Med Reports file \#74 with the electronic signature block printed name defined in file \#200 of the verifying physician who signed the report on the PowerScribe unit. Before a report can be filed in VistA with an electronic signature, it must pass all validation processes outlined in the section on Operational Features earlier in this section.

> **WARNING:** See also the Rad/Nuc Med Technical Manual section on Security for further electronic signature information.

47. At integrated sites using more than one COTS Voice Reporting system, it may be necessary to limit messages to specific Divisions for optimal performance.[^28] This can be achieved by setting the ROUTING LOGIC field to ‘D ^RAHLROUT’ for all subscriber protocols in use by Radiology HL7 event drivers (RA REG 2.3, RA CANCEL 2.3, RA EXAMINED 2.3, RA RPT 2.3). The ROUTING LOGIC routine, ^RAHLROUT, will check the HL7 RECEIVING APPLICATIONS multiple field in the Rad/Nuc Med Division file (file \#79). If this field includes ‘RA-PSCRIBE-TCP’, then messages created in the Division will be passed to PowerScribe, otherwise they will not be sent to PowerScribe.
48. The Rad/Nuc Med coordinator who supports the PowerScribe unit must define Rad/Nuc Med diagnostic codes on the PowerScribe unit. Vista Diagnosis codes from file 78.3 need to be added using the Coding Manager in PowerScribe and they need to be associated with CPT4 Procedure Codes used by Radiology. Follow the steps below to configure PowerScribe with the diagnostic codes used in the DIAGNOSTIC CODES file (#78.3) in FileMan. The list below is an example of some of common diagnosis codes that may be defined in file 78.3, however, this file is configurable and could be different for each site.

> 1 NORMAL

> 2 MINOR ABNORMALITY

> 3 MAJOR ABNORMALITY, NO ATTN. NEEDED

> 4 ABNORMALITY, ATTN. NEEDED

> 5 MAJOR ABNORMALITY, PHYSICIAN AWARE

> 6 UNDICTATED FILMS NOT RETURNED, 3 DAYS

> 7 UNSATISFACTORY/INCOMPLETE EXAM

> 8 POSSIBLE MALIGNANCY, FOLLOW-UP NEEDED

> From the PowerScribe – Coding Manager toolbar, choose View and select Diagnosis Codes. This will bring up a window with all of the valid ICD9 codes. Click on the New button and type 1 in the box beneath “Diagnosis Code”. This number should match the Internal Entry Number (IEN) of the diagnosis code in file 78.3. Next type NORMAL in the box beneath “Diagnosis Description:”. Select OK and follow the same procedure for the other codes.

49. Make sure all other PowerScribe setup is correct and complete according to PowerScribe documentation.
50. If the PowerScribe interface is moved from a test account to the production account, update the TCP/IP port numbers on both sides, and delete the PowerScribe database (using SQL commands) to prevent cross-over of test data to the live account. (The change of port numbers ensures a unique socket connection. But the TCP/IP address of the PowerScribe remains the same.)
51. It is very helpful to synchronize the PowerScribe PC clock to closely agree with the VistA system clock.
52. Responsibility for starting, stopping, and monitoring the links can belong to IRM, or IRM can delegate this to the Rad/Nuc Med coordinator with the understanding that if problems occur, IRM may have to provide support.
53. PowerScribe users and IRM should learn how to find and interpret error messages for rejected reports. See the section for VistA Rad/Nuc Med HL7 Error Message and Troubleshooting Table for TalkStation and PowerScribe Interfaces later in this manual for a detailed procedure for finding and interpreting error messages. If the error is returned by Radiology, rather than the HL7 software, then it will be logged in the HL7 Message Exceptions file \#79.3 and can be viewed using the Rad/Nuc Med HL7 Voice Reporting Errors option. Additionally, setting a MAIL GROUP for the PowerScribe application in the HL7 APPLICATION PARAMETERS file \#771 will mean that these errors will also be sent as mail messages to the defined mail group and the verifying physician.[^29]
54. This interface requires link tasks to always start up on the same node. So, if your site is an Alpha/AXP site running more than one instance of TaskMan, you must start up TaskMan in DCL context. Consult the Kernel System Manual for instructions on running TaskMan in DCL context.

## Setup of HL7 Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All of this setup, except for site-specific fields, is done automatically by the Rad/Nuc Med patch RA\*5\*17. However, the site is responsible for entering the TCP/IP address, TCP/IP port numbers, Startup Node and other fields that are site-specific (these items are shown in bold).

A sample setup follows. IRM should only populate the fields in bold print. Your responses should be specific to your site, and not necessarily what you see below. The VistA screen shots are taken from the HL7 Main Menu, Interface Developers Option. Details are also provided on configuring PowerScribe using the PowerScribe Administrator.

#### HL7 Application Parameter File \#771 Setup

NAME: RA-PSCRIBE-TCP ACTIVE/INACTIVE: ACTIVE

FACILITY NAME: POWERSCRIBE MAIL GROUP:[^30] RAD HL7 REJECTIONS

COUNTRY CODE: US HL7 ENCODING CHARACTERS: ^~\\

HL7 FIELD SEPARATOR: \|

HL7 APPLICATION EDIT

------------------------------------------------------------------------------

NAME: RA-PSCRIBE-TCP ACTIVE/INACTIVE: ACTIVE

FACILITY NAME: POWERSCRIBE \<-- enter name COUNTRY CODE: US

HL7 FIELD SEPARATOR: \| HL7 ENCODING CHARACTERS: ^~\\

MAIL GROUP:[^31] RAD HL7 REJECTIONS \<- optional mail group defined

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

NAME: RA-VOICE-SERVER ACTIVE/INACTIVE: ACTIVE

FACILITY NAME: VistA RADIOLOGY MAIL GROUP:[^32] RAD HL7 REJECTIONS

COUNTRY CODE: US HL7 ENCODING CHARACTERS: ^~\\

HL7 FIELD SEPARATOR: \|

HL7 APPLICATION EDIT

------------------------------------------------------------------------------

NAME: RA-VOICE-SERVER ACTIVE/INACTIVE: ACTIVE

FACILITY NAME: VistA RADIOLOGY \<-- enter name COUNTRY CODE: US

HL7 FIELD SEPARATOR: \| HL7 ENCODING CHARACTERS: ^~\\

MAIL GROUP:[^33] RAD HL7 REJECTIONS \<-- optional mail group defined

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

> **NOTE:** See vendor documentation for more information on PowerScribe setup. The following items are a subset that correlate to VistA setup.

PowerScribe settings can be altered using PowerScribe Administrator application (Start button, Programs, PowerScribe Radiology, PowerScribe Administrator). See CONFIGURING POWERSCRIBE HL7 PROTOCOL SETTINGS later in this section for a detailed explanation on defining settings on PowerScribe.

> Sending App: RA-PSCRIBE-TCP  
> Receiving App: RA-VOICE-SERVER

#### HL Logical Link File \#870 Setup

This file contains the links used by the HL7 package to send messages. It is used to identify the TCP/IP address of the PowerScribe unit, as well as the TCP/IP port numbers that will be used. These addresses are all site-specific and must be entered by IRM before the links are started.

This file also stores parameters that define the behavior of the lower level protocols and information that is used with the Systems Link Monitor, which gives the user feedback about the state of each link. When a message is received, the link moves from an IDLE state to a READING state. In this sample the links are used for the following messages:

> RA-PSCRIBE is used to send order messages (i.e., exam registered, exam cancelled, patient examined, and report verified or released/not verified) from VistA to PowerScribe. This link also receives the order Acknowledgment from PowerScribe.

This sample shows active, run-time data. Some of the fields are populated by the Rad/Nuc Med patch RA\*5\*17. The remainder of the fields is populated by the HL7 package when you start up the links.

Although not exported, it is strongly recommended that you add an ACK timeout for the sender link. If you do not enter a value then a default of 10 seconds will be used and experience has shown that this is not enough for a busy TCP/IP network. We recommend using between 300 and 600 seconds.

You may choose to automatically start all HL7 Logical Links and Inbound/Outbound Filers when TaskMan is restarted. To do this, run the TaskMan, Schedule/Unschedule options, select Restart All Links and Filers, and place an ‘S’ in the SPECIAL QUEUEING field. Then, remember to set AUTOSTART to ‘1’ (Enabled) for each link.

Regardless of the ‘Exceed Re-Transmit Action’ entered, when the ‘Re-Transmission Attempts’ for a message is exceeded, an alert is sent to the mail group defined in the MAIL GROUP FOR ALERTS field in the HL COMMUNICATION SERVER PARAMETERS (#869.3) file. This can be edited using the HL7 Main Menu, Site Parameter Edit option.

The RA-PSCRIBE sender link is exported as a Persistent Client, but it is possible to change it to a Non-Persistent Client. The advantage of Non-Persistent clients is that the link only connects when required, rather than leaving the process open at all times.

See the VistA HL7 Site Manager & Developer Manual section 2.4 TCP Link Setup for additional field definitions. The values shown below have been proven to work in the past.

NODE: RA-PSCRIBE LLP TYPE: TCP

DEVICE TYPE: Persistent Client AUTOSTART: Enabled

RE-TRANSMISSION ATTEMPTS: 3 ACK TIMEOUT: 300

EXCEED RE-TRANSMIT ACTION: ignore TCP/IP ADDRESS: <span class="mark">REDACTED</span>

TCP/IP PORT: 8410 TCP/IP SERVICE TYPE: CLIENT (SENDER)

PERSISTENT: YES STARTUP NODE:

HL7 LOGICAL LINK

------------------------------------------------------------------------------

NODE: RA-PSCRIBE

INSTITUTION:

DOMAIN:

AUTOSTART: Enabled \<-- set to Enabled if autostart of link required

QUEUE SIZE:

LLP TYPE: TCP \<-- hit \<return\> here to edit LLP parameters

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 LOGICAL LINK

------------------------------------------------------------------------------

┌──────────────────────TCP LOWER LEVEL PARAMETERS─────────────────────────┐

│ RA-PSCRIBE │

│ │

│ TCP/IP SERVICE TYPE: CLIENT (SENDER) │

│ TCP/IP ADDRESS: <span class="mark">REDACTED</span> \<-- address of PowerScribe server│

│ TCP/IP PORT: 8410 \<-- port PowerScribe receives on │

│ │

│ │

│ ACK TIMEOUT: 300 \<-- recommended RE-TRANSMISION ATTEMPTS: 3 │

│ READ TIMEOUT: EXCEED RE-TRANSMIT ACTION: ignore │

│ BLOCK SIZE: │

│ │

│STARTUP NODE: \<-- ONLY set if multiple TaskMan/DCL PERSISTENT: YES │

│ RETENTION: UNI-DIRECTIONAL WAIT: │

└─────────────────────────────────────────────────────────────────────────┘

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Close Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Close Press \<PF1\>H for help Insert

#### Protocol File \#101 Setup

The event driver entries (RA REG 2.3, RA EXAMINED 2.3, RA CANCEL 2.3, RA RPT 2.3 and RA PSCRIBE TCP SERVER RPT) are exported with the Rad/Nuc Med VistA patch RA\*5.0\*17 for use with this interface.

Also exported are the subscriber protocols (RA PSCRIBE ORM, RA PSCRIBE ORU and RA PSCRIBE TCP REPORT).

(Refer to the ‘Rad/Nuc Med HL7 Interface Specifications’ section of this manual for information about messages initiated by Rad/Nuc Med.)

In order to associate the event driver protocols with the Radiology-PowerScribe interface and thereby initiate messages, the PowerScribe subscriber protocols need to be added to the associated event driver SUBSCRIBERS multiple.

Once the subscriber protocols are added, messages will be built and will stack up until the links are started.

If ever you need to completely disable the interface and want to stop new messages from being created for this interface, simply remove the PowerScribe subscriber protocols from the event driver protocols.

Listed below are examples of the event driver protocols with the subscriber protocols that require addition shown in bold. You may see other subscribers listed on your system, these should not be removed.

Next are screen shots from the HL7 Main Menu, Interface Developer Options …, Protocol Edit highlighting the steps required to add the subscriber protocols.

The subscriber protocols shown (RA PSCRIBE ORM and RA PSCRIBE ORU) are setup to use ROUTING LOGIC to filter messages depending on Division. This is not the usual situation, but is shown to highlight how this can be achieved.[^34]

> **NOTE:** If the ROUTING LOGIC field is set, but no Rad/Nuc Med Division (file \#79) has ‘RA-PSCRIBE-TCP’ as an HL7 RECEIVING APPLICATION, then no messages will be sent to PowerScribe.

Also, if other subscriber protocols exist for the event drivers (RA REG 2.3, RA CANCEL 2.3, RA EXAMINED 2.3, RA RPT 2.3), for example RA TALKLINK ORM, then these will need to be setup to use ROUTING LOGIC also. Otherwise all HL7 subscribers will receive messages from all divisions, and messages will still be passed to PowerScribe.

If in doubt, do not set the ROUTING LOGIC field.

NAME: RA REG 2.3

ITEM TEXT: Rad/Nuc Med exam registered for HL7 v2.3 message

TYPE: event driver PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is triggered whenever a Radiology/Nuclear

Medicine exam is registered. It executes code that creates an HL7 ORM version

2.3 message consisting of PID, ORC, OBR, and OBX segments. The message

contains all relevant information about the exam, including procedure, time

of registration, procedure modifiers, patient allergies, and clinical history.

SENDING APPLICATION: RA-VOICE-SERVER TRANSACTION MESSAGE TYPE: ORM

EVENT TYPE: O01 VERSION ID: 2.3

SUBSCRIBERS: RA PSCRIBE ORM

HL7 INTERFACE SETUP PAGE 1 OF 2

-------------------------------------------------------------------------------

NAME: RA REG 2.3

DESCRIPTION (wp): \[This protocol is triggered whenever a Radiology\]

ENTRY ACTION:

EXIT ACTION:

TYPE: event driver hit \<return\> here to edit event driver details

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 EVENT DRIVER PAGE 2 OF 2

RA REG 2.3

-------------------------------------------------------------------------------

SENDING APPLICATION: RA-VOICE-SERVER

TRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01

PROCESSING ID: VERSION ID: 2.3

ACCEPT ACK CODE: APPLICATION ACK TYPE:

RESPONSE PROCESSING RTN:

SUBSCRIBERS

RA PSCRIBE ORM add this subscriber

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for Help Insert

NAME: RA CANCEL 2.3 ITEM TEXT: Rad/Nuc Med exam cancellation

TYPE: event driver PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is triggered whenever a Radiology/Nuclear

Medicine exam is cancelled. It executes code that creates an HL7 ORM version

2.3 message consisting of PID,ORC, OBR, and OBX segments. The message

contains all relevant information about the exam, including procedure, time of

cancellation, procedure modifiers, patient allergies and clinical history.

SENDING APPLICATION: RA-VOICE-SERVER TRANSACTION MESSAGE TYPE: ORM

EVENT TYPE: O01 VERSION ID: 2.3

SUBSCRIBERS: RA PSCRIBE ORM

HL7 INTERFACE SETUP PAGE 1 OF 2

-------------------------------------------------------------------------------

NAME: RA CANCEL 2.3

DESCRIPTION (wp): \[This protocol is triggered whenever a Radiology\]

ENTRY ACTION:

EXIT ACTION:

TYPE: event driver \<- hit \<return\> here to edit event driver details

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 EVENT DRIVER PAGE 2 OF 2

RA CANCEL 2.3

-------------------------------------------------------------------------------

SENDING APPLICATION: RA-VOICE-SERVER

TRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01

PROCESSING ID: VERSION ID: 2.3

ACCEPT ACK CODE: APPLICATION ACK TYPE:

RESPONSE PROCESSING RTN:

SUBSCRIBERS

RA PSCRIBE ORM\<- add this subscriber

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

NAME: RA EXAMINED 2.3 ITEM TEXT: Rad/Nuc Med examines case

TYPE: event driver PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is triggered whenever a Radiology/Nuclear

Medicine exam has reached a status where GENERATE EXAMINED HL7 MSG is Y at

that (or at a lower) status. This message contains all relevant information

about the exam, including procedure, time of registration, procedure

modifiers, patient allergies, and clinical history.

SENDING APPLICATION: RA-VOICE-SERVER TRANSACTION MESSAGE TYPE: ORM  
EVENT TYPE: O01 VERSION ID: 2.3

SUBSCRIBERS: RA PSCRIBE ORM

HL7 INTERFACE SETUP PAGE 1 OF 2

------------------------------------------------------------------------------

NAME: RA EXAMINED 2.3

DESCRIPTION (wp): \[This protocol is triggered whenever a Radiology\]

ENTRY ACTION:

EXIT ACTION:

TYPE: event driver \<- hit \<return\> here to edit event driver details

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 EVENT DRIVER PAGE 2 OF 2

RA EXAMINED 2.3

-------------------------------------------------------------------------------

SENDING APPLICATION: RA-VOICE-SERVER

TRANSACTION MESSAGE TYPE: ORM EVENT TYPE: O01

PROCESSING ID: VERSION ID: 2.3

ACCEPT ACK CODE: APPLICATION ACK TYPE:

RESPONSE PROCESSING RTN:

SUBSCRIBERS

RA PSCRIBE ORM\<- add this subscriber

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

NAME: RA RPT 2.3

ITEM TEXT: Rad/Nuc Med report released/verified

TYPE: event driver PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is triggered whenever a Radiology/Nuclear

Medicine report enters into a status of Verified or Released/Not Verified. It

executes code that creates an HL7 ORU message consisting of PID, OBR and OBX

segments. The message contains relevant information about the report,

including procedure, procedure modifiers, diagnostic code, interpreting

physician, impression text and report text.

SENDING APPLICATION: RA-VOICE-SERVER TRANSACTION MESSAGE TYPE: ORU

EVENT TYPE: R01 VERSION ID: 2.3

SUBSCRIBERS: RA PSCRIBE ORU

HL7 INTERFACE SETUP PAGE 1 OF 2

-------------------------------------------------------------------------------

NAME: RA RPT 2.3

DESCRIPTION (wp): \[This protocol is triggered whenever a Radiology\]

ENTRY ACTION:

EXIT ACTION:

TYPE: event driver \<- hit \<return\> here to edit driver details

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 EVENT DRIVER PAGE 2 OF 2

RA RPT 2.3

-------------------------------------------------------------------------------

SENDING APPLICATION: RA-VOICE-SERVER

TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

PROCESSING ID: VERSION ID: 2.3

ACCEPT ACK CODE: APPLICATION ACK TYPE:

RESPONSE PROCESSING RTN:

SUBSCRIBERS

RA PSCRIBE ORU \<- add this subscriber

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

NAME: RA PSCRIBE ORM ITEM TEXT: TCP Client

TYPE: subscriber PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is used in conjunction with the RA REG 2.3, RA

EXAMINED 2.3, and RA CANCEL 2.3 event protocols. It is used by the VistA HL7

package to send ORM messages to TCP/IP recipients. This protocol should be

entered in the SUBSCRIBERS multiple field of those event point protocols if

this type of messaging scenario is used at a facility. This is part of the

file set-up to enable HL7 message flow when exams are registered, cancelled,

and when they reach the status flagged as ‘examined’ by the site.

RECEIVING APPLICATION: RA-PSCRIBE-TCP EVENT TYPE: O01

LOGICAL LINK: RA-PSCRIBE VERSION ID: 2.3

RESPONSE MESSAGE TYPE: ACK SENDING FACILITY REQUIRED?: NO

RECEIVING FACILITY REQUIRED?: NO SECURITY REQUIRED?: NO

ROUTING LOGIC:[^35] D ^RAHLROUT

HL7 INTERFACE SETUP PAGE 1 OF 2

--------------------------------------------------------------------------------

NAME: RA PSCRIBE ORM

DESCRIPTION (wp): \[This protocol is used in conjunction with the R\]

ENTRY ACTION:

EXIT ACTION:

TYPE: subscriber \<- hit \<return\> here to edit subscriber details

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 SUBSCRIBER PAGE 2 OF 2

RA PSCRIBE ORM

--------------------------------------------------------------------------------

RECEIVING APPLICATION: RA-PSCRIBE-TCP

RESPONSE MESSAGE TYPE: ACK EVENT TYPE: O01

SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

SECURITY REQUIRED?: NO

LOGICAL LINK: RA-PSCRIBE

PROCESSING RTN:

ROUTING LOGIC: D ^RAHLROUT \<--only set if using Divisional filtering

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

NAME: RA PSCRIBE ORU ITEM TEXT: TCP Client

TYPE: subscriber PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: This protocol is used in conjunction with the RA RPT 2.3 event

point protocol. The HL7 package uses this protocol to send rad/nuc med report

(ORU) messages to TCP/IP recipients. This protocol should be entered in the

SUBSCRIBERS multiple field of the RA RPT protocol if this messaging scenario

is used in a facility. This is part of the file set-up to enable message flow

when a rad/nuc med report is verified.

RECEIVING APPLICATION: RA-PSCRIBE-TCP EVENT TYPE: R01

LOGICAL LINK: RA-PSCRIBE VERSION ID: 2.3

RESPONSE MESSAGE TYPE: ACK SENDING FACILITY REQUIRED?: NO

RECEIVING FACILITY REQUIRED?: NO SECURITY REQUIRED?: NO

ROUTING LOGIC:[^36] D ^RAHLROUT

HL7 INTERFACE SETUP PAGE 1 OF 2

--------------------------------------------------------------------------------

NAME: RA PSCRIBE ORU

DESCRIPTION (wp): \[This protocol is used in conjunction with the R\]

ENTRY ACTION:

EXIT ACTION:

TYPE: subscriber \<- hit \<return\> here to edit subscriber details

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 SUBSCRIBER PAGE 2 OF 2

RA PSCRIBE ORU

--------------------------------------------------------------------------------

RECEIVING APPLICATION: RA-PSCRIBE-TCP

RESPONSE MESSAGE TYPE: ACK EVENT TYPE: R01

SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

SECURITY REQUIRED?: NO

LOGICAL LINK: RA-PSCRIBE

PROCESSING RTN:

ROUTING LOGIC: D ^RAHLROUT \<--only set if using Divisional filtering

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

The following protocols, shown without screen shots, are exported as part of the Radiology TalkStation interface but do not require amendment:[^37]

NAME: RA PSCRIBE TCP SERVER RPT

ITEM TEXT: PowerScribe TCP sends report to VistA

TYPE: event driver PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

SENDING APPLICATION: RA-PSCRIBE-TCP TRANSACTION MESSAGE TYPE: ORU

EVENT TYPE: R01 VERSION ID: 2.3

SUBSCRIBER: RA PSCRIBE TCP REPORT

NAME: RA PSCRIBE TCP REPORT ITEM TEXT: Client for PowerScribe TCP rpt

TYPE: subscriber PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

DESCRIPTION: Subscriber protocol for sending report to VistA

Radiology/Nuclear Medicine. This protocol is used by the HL7 package to

process messages sent to VistA from a COTS voice recognition unit using TCP/IP

for message flow. This protocol should be entered in the SUBSCRIBERS multiple

of the RA PSCRIBE TCP SEREVR RPT protocol.

RECEIVING APPLICATION: RA-VOICE-SERVER EVENT TYPE: R01

LOGICAL LINK: PSCRIBE-RA VERSION ID: 2.3

RESPONSE MESSAGE TYPE: ACK PROCESSING ROUTINE: D ^RAHLTCPB

SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

SECURITY REQUIRED?: NO

## Configuring PowerScribe HL7 Protocol Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the example listed above, HL7 Logical Link settings for RA-PSCRIBE show that 152.132.126.222 is the PowerScribe TCP/IP address on the LAN. The PowerScribe system sends the report back to the TCP/IP address that has been defined in the PowerScribe Administrator under the Interface tab and the HL7 Protocol Settings button. On systems running more than one instance of TaskMan, the link tasks must be forced to start up on the same CPU (i.e. same TCP/IP address) every time. This is accomplished by entering a “STARTUP NODE”. If this is not done, PowerScribe will not be able to establish a link to the VistA Listener. PowerScribe also needs to have TCP/IP PORT numbers defined. For this example, the PowerScribe Administrator HL7 Protocol Settings would show the following port and TCP/IP configuration entries:

![](radiology-version-5-hl7-setup-manual/006.png)

## Detailed Explanation of Start-up/Recovery Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Stop the appropriate links from the HL7 Main Menu, Filer and Link Management Options…, Start/Stop Links:

> UCX Multi-Threaded Listener System: Stop only the RA-PSCRIBE link. (You do NOT need to shut down the UCX listener. Generic UCX tools control UCX services.)

55. If necessary, boot or reboot the PowerScribe unit (i.e., reboot only if an application error occurred on the PowerScribe unit, or a previous attempt at recovery has failed). Rebooting can be done using the Start button and selecting ‘Shut Down’.
56. The PowerScribe HL7Server.exe and HL7Client.exe icons should be located on the desktop of the PowerScribe unit. Double click on the icons to start the links. If the icons are not located on the desktop you can create a shortcut to the executable located in C:\PowerScribe, or simply start the executable from this directory.
57. On Open-M/Cache systems only, it is a good idea to kill off the logical link listener job (%ZISTCP) before restarting the links. This step is optional, but will prevent an extinct job from unnecessarily using up CPU time. Use the system status utility to find these jobs. They appear as running the %ZISTCP routine using port numbers that you entered as TCP/IP PORT in the setup (i.e., File \#870, Field \#400.02 TCP/IP PORT, for entries RA-PSCRIBE and PSCRIBE-RA). This step may be unnecessary after additional HL7 package patches.
58. Regarding the site specific “multi-listener link” VAxxx:

> UCX Multi-Threaded Listener System: No action is needed. The listener is an OpenVMS UCX service and UCX starts running when OpenVMS is brought up.

59. Verify that the listener link is up and running:

> UCX Multi-Threaded Listener System: The OpenVMS UCX service should be enabled. The columns indicating message totals for the PSCRIBE-RA HL7 link are accurately reflected in the System Link Monitor. Disregard the information presented in the Device Type and State columns for the PSCRIBE-RA HL7 link.

60. Start the “sender” link RA-PSCRIBE: From the HL7 Main Menu, Filer and Link Management Options…, Start/Stop Links.

> Enter RA-PSCRIBE at the ‘Select HL LOGICAL LINK NODE:’ prompt, then press enter to accept the default of ‘BACKGROUND’ at the ‘Method for running the receiver;’ prompt.

61. Use the Systems Link Monitor option again to verify that the RA-PSCRIBE sender link is up and running. If the HL7Server and HL7Client processes are not running on the PowerScribe server then the RA-PSCRIBE link will toggled between an Open and OpenFail state.

## Start-up/Recovery Procedure Quick Reference

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Radiology-PowerScribe Interface

|      |             |                                                                                  |                                                                                            |
|------|-------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Step | Machine     | Action                                                                           | Mandatory, Optional, or Conditional                                                        |
| 1    | VistA       | UCX Multi-Threaded Listener System: Shut down the RA-PSCRIBE link.               | Mandatory                                                                                  |
| 2    | PowerScribe | Reboot                                                                           | Only if PowerScribe application error occurred or PowerScribe PC suffered power loss, etc. |
| 3    | PowerScribe | Startup HL7Server.exe and HL7Client.exe                                          | Only if down and not connected                                                             |
| 6    | VistA       | UCX Multi-Threaded Listener System: enable the OpenVMS UCX Service (if disabled) | Mandatory                                                                                  |
| 7    | VistA       | Start the sender logical link: RA-PSCRIBE                                        | Mandatory                                                                                  |

Notes: If the PowerScribe HL7Server goes down or loses the link, the recovery process is necessary.  
*Shutdown the RA-PSCRIBE link*  
  
If the VistA machine is going to be shutdown:  
*Shut down the RA-PSCRIBE linkThis page intentionally left blank.*

# VistA Rad/Nuc Med HL7 Error Message and Troubleshooting Table for TalkStation and PowerScribe Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because the PowerScribe and TalkStation interfaces all currently use the same Processing Routine, the errors reported will be the same.

There follows a list of the possible errors that might be returned by Radiology when a report message is passed from one of the COTS products. The errors are stored on the HL7 Exceptions File \#79.3, and can be viewed using the Rad/Nuc Med HL7 Voice Reporting Errors option. Additionally, setting a MAIL GROUP for the application in the HL7 APPLICATION PARAMETERS file (#771) will mean that these errors will also be sent as mail messages to the defined mail group and the verifying physician.[^38]

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th>Error Message</th>
<th>Cause/Solution</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Missing Case Number</p>
<p>Internal Patient ID Missing</p>
<p>Missing Exam Date</p>
<p>Missing Exam Date and/or</p>
<p>Case Number</p>
<p>Missing Patient ID</p>
<p>Missing report date</p>
<p>Missing Internal Patient ID</p>
<p>Invalid Report Date</p></td>
<td>HL7 message from vendor does not contain adequate information to determine case number, or patient, or exam date. (These errors should not happen in a debugged, operational interface.)</td>
</tr>
<tr class="even">
<td><p>Internal patient identifier and SSN</p>
<p>don’t match</p></td>
<td>Could happen if patient SSN in VistA was changed/corrected after an exam was registered in VistA, but before a report was created on COTS product. May require IRM to manually change the COTS product data to match the corrected VistA SSN. Before making changes, verify that the patient report applies to the right patient.</td>
</tr>
<tr class="odd">
<td><p>Invalid Exam Date and/or</p>
<p>Case Number</p>
<p>Report for CANCELLED case</p>
<p>not permitted</p>
<p>Please use VistA to edit CANCELLED printset cases.</p></td>
<td>Unlikely, but could happen if an exam is deleted or cancelled from Rad/Nuc Med at a time when the cancel message cannot reach COTS product, or if a pre-existing COTS product report that was once rejected is re-sent after the exam is deleted or cancelled. A failure to deliver the cancel message to COTS product would have had to happen to create this scenario. May need to clean this exam out of the COTS product database manually.</td>
</tr>
<tr class="even">
<td><p>Can’t add addendum, no report</p>
<p>Can’t add addendum to an unverified report</p></td>
<td>Unlikely, but could happen if a report is deleted or unverified in Rad/Nuc Med, then an addendum is sent from COTS product. May need to clean this exam out of the COTS product database manually and use VistA Rad/Nuc Med to make corrections.</td>
</tr>
<tr class="odd">
<td>Report already on file</td>
<td>Would happen if there was a failure to send COTS product a message containing a report entered on VistA Rad/Nuc Med. Or if a message was resent by a COTS product having already been filed by VistA Rad/Nuc Med</td>
</tr>
<tr class="even">
<td><p>Missing addendum report/impression</p>
<p>text</p></td>
<td>Unlikely because COTS product software will not allow a blank report to be sent. Re-edit and re-send report from COTS product.</td>
</tr>
<tr class="odd">
<td><p>Missing Impression Text</p>
<p>Impression Text missing for current</p>
<p>record</p></td>
<td>The division where this exam was registered has its Rad/Nuc Med Division file #79 parameter ‘Impression Req’d on Rpts’ set to ‘Yes’, but the COTS product user did not include an impression when s/he entered the report. Re-edit to add impression text and re-send report from COTS product.</td>
</tr>
<tr class="even">
<td><p>No Imaging Type for Location where</p>
<p>exam was performed</p></td>
<td>VistA Rad/Nuc Med Patient file has a partial, corrupted record for this exam. IRM and Radiology Service should investigate and determine whether to delete the record or attempt to enter missing data.</td>
</tr>
<tr class="odd">
<td><p>Provider not classified as resident or</p>
<p>staff</p></td>
<td>COTS product user does not have Rad/Nuc Med Personnel classification. Use Rad/Nuc Med Personnel Classification option to enter ‘resident’ or ‘staff’ status if appropriate. Re-transmit report.</td>
</tr>
<tr class="even">
<td><p>Residents are not permitted to verify</p>
<p>reports</p></td>
<td>The division where this exam was performed does not allow residents to verify reports. (See Rad/Nuc Med Division file #79 parameter ‘ALLOW VERIFYING BY RESIDENTS’). This is a facility-determined practice.</td>
</tr>
<tr class="odd">
<td><p>Provider does not meet security</p>
<p>requirements to verify report</p></td>
<td>COTS product user does not have the ‘RA VERIFY’ key. IRM can give this key to the user if it is appropriate, then the report can be re-sent.</td>
</tr>
<tr class="even">
<td><p>Inactive Rad/Nuc Med Classification</p>
<p>for Interpreting Physician</p></td>
<td>The COTS product user has been inactivated under the Rad/Nuc Med Personnel Classification option.</td>
</tr>
<tr class="odd">
<td>Staff review required to verify report</td>
<td>The COTS product user has a ‘resident’ classification, and the division where the exam was performed requires staff review before report verification.</td>
</tr>
<tr class="even">
<td><p>Invalid Impression Text</p>
<p>Invalid Report Text</p></td>
<td>Report or Impression text does not meet VistA Rad/Nuc Med requirements – possibly too few characters or all special characters.</td>
</tr>
<tr class="odd">
<td>Missing Diagnostic Code</td>
<td>Unlikely. A null diagnostic code was entered. Re-edit diagnostic code and re-send report.</td>
</tr>
<tr class="even">
<td>Invalid Diagnostic Code</td>
<td>Unlikely to happen in a debugged operational system. No exact match for diagnostic code found in the Diagnostic Code file #78.3. Check COTS product Diagnostic Code table for spelling and typographical errors.</td>
</tr>
<tr class="odd">
<td><p>ANOTHER USER IS CURRENTLY</p>
<p>EDITING THIS PRINTSET. TRY</p>
<p>LATER</p>
<p>This report is being edited by another user</p></td>
<td>Likely to happen in high-volume imaging services. This may happen if another Rad/Nuc Med employee is editing the same report for a single case, or editing one of the cases or report for a parent/descendant printset when the COTS product report is transmitted. Re-send the report later.</td>
</tr>
<tr class="even">
<td>An &lt;UNDEFINED&gt; error in the HL7 routine HLTP01 is logged in the error trap</td>
<td>Probable cause: a protocol entered as an item on an event driver protocol is not completely set up. This is likely if there is more than one protocol entered in the ‘ITEM’ multiple of the event driver protocols RA REG 2.3, RA RPT 2.3.1, RA CANCEL 2.3.1, RA EXAMINED 2.3.1. The RA TALKLINK ORU protocol must be an item under RA RPT 2.3.1, and the RA TALKLINK ORM protocol must be an item under the rest of the event drivers.</td>
</tr>
<tr class="odd">
<td>Messages not always reaching VistA machine</td>
<td>Make sure that the COTS product knows its own domain name on your LAN. (See instructions from vendor.)</td>
</tr>
<tr class="even">
<td>Open-M/Cache systems only -- some %ZISTCP processes continue to run when all links are shut down.</td>
<td>Since Open-M/Cache does not kill off these jobs like DSM, you must manually kill these jobs when all links are down.</td>
</tr>
<tr class="odd">
<td>Site wants to activate only one or two of the three ORM messages (RA REG 2.3, RA EXAMINED 2.3, RA CANCEL 2.3), but none of the messages go across if any of them is inactivated.</td>
<td>The inactivated messages may be causing the problem. Delete the data in the Server Application field and the Item multiple field of the event point protocols that are de-activated.</td>
</tr>
<tr class="even">
<td>COTS product rejects an ACK message after sending a report. The ACK message generated by VistA has an incorrect mix of field separators.</td>
<td>The RA TALKLINK TCP SERVER protocol may have been accidentally renamed. This protocol must not be renamed because it is used to initialize variables, and its name is hard-coded in the Rad/Nuc Med “bridge” program.</td>
</tr>
<tr class="odd">
<td>On a clustered system running more than one TaskMan, links will not stay up.</td>
<td>Clustered Alpha systems running more than one TaskMan need to run TaskMan in DCL context, and use the link startup parameters in file 870, so that the links always start up on the same node. COTS product requires persistent connections for links on the same TCP/IP address.</td>
</tr>
<tr class="even">
<td>Link statuses indicate that the links are up and running, but no messages are being sent or received.</td>
<td>If the VistA system crashed or was shut down without first stopping the LLP links, the status looks normal, but the link jobs are no longer running. Shut down the links and start them back up in the recommended order.</td>
</tr>
</tbody>
</table>

*This page intentionally left blank*

# # # # # # # # # # # # # # # Setup Instructions/Examples for Using IHE compliant HL7 v2.4 Protocols[^39]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Four newly created event driver protocols are exported in patch RA\*5.0\*47: RA REG 2.4, RA EXAMINED 2.4, RA CANCEL 2.4, and RA RPT 2.4.

A new event driver protocol RA RELEASE 2.4 is exported with patch RA\*5.0\*144. Add ORU subscribers of this event driver to receive ‘Release Study’ messages initiated from National Teleradiology (NTP). The ‘Release Study’ message indicates the study was released back to the local facility for interpretation.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Notes:</strong></th>
<th><p><strong>Do not proceed with these steps until ready to begin using the new</strong></p>
<p><strong>HL7 v2.4 messaging.</strong></p>
<ul>
<li><p><strong>Once you are ready to switch over to the new HL7 v2.4 messaging, you must perform the following steps.</strong></p></li>
<li><p><strong>These steps must be done in coordination with the voice recognition software in use at the site.</strong></p></li>
<li><p><strong>These steps should be done when the Radiology options or voice recognition software is not in use.</strong></p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Setting Up the Voice Recognition Event Driver Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to use the new IHE compliant HL7 v2.4 messaging provided by this patch, you must add the corresponding voice recognition subscriber protocols as SUBSCRIBERS to the new v2.4 event driver protocols exported in this patch.

> **NOTE:** For setting up the VistA Imaging MAGD SEND ORM and MAGD SEND ORU subscriber protocols, refer to MAG\*3.0\*49 patch documentation.

The voice recognition subscriber protocols are likely the subscriber protocols that the site currently uses for the existing v2.3 (or previous) protocols.

Prior to adding the voice recognition subscriber protocols to the new v2.4 event driver protocols, the corresponding voice recognition subscriber protocols must be removed from the existing v2.3 event driver protocols, to prevent sending duplicate messages.

> **NOTE:** If the listed protocols were renamed locally at your site, use the appropriately named protocols.

In the examples, TalkStation is used to illustrate the process, but the steps are the same for PowerScribe and RadWhere; so, substitute the correct name.

### Step 1 - Remove subscribers from existing ORM event driver protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For the RA CANCEL 2.3, RA EXAMINED 2.3 and RA REG 2.3 protocols (or the appropriate protocols if the site is using a version previous to v2.3), remove the voice recognition ORM subscriber protocol.

For TalkStation, it is usually RA TALKLINK ORM Note ORM

For PowerScribe, it is usually RA PSCRIBE ORM Note ORM

For RadWhere, it is usually RA RADWHERE ORM Note ORM  
Example for Step 1Note: You must perform step 1 for the RA REG 2.3, RA CANCEL 2.3, and RA EXAM 2.3 protocols, but only RA REG 2.3 is shown in this example.

Select OPTION NAME: HL7 MAIN MENU  HL MAIN MENU     HL7 Main Menu

 

                 Event monitoring menu ...

                 Systems Link Monitor

                 Filer and Link Management Options ...

                 Message Management Options ...

                 Interface Developer Options ...

                 Site Parameter Edit

          HLO    HL7 (Optimized) MAIN MENU ...

 

Select HL7 Main Menu Option:  Interface Developer Options

 

          EA     Application Edit

          EP     Protocol Edit

          EL     Link Edit

          VI     Validate Interfaces

                 Reports ...

 

Select Interface Developer Options Option:  Protocol Edit

 

Select PROTOCOL NAME: RA REG 2.3   Select v2.3 event driver protocol

   

              HL7 INTERFACE SETUP                         PAGE 1 OF 2

-----------------------------------------------------------------------

 

              NAME: RA REG 2.3                                            

 

DESCRIPTION (wp):   \[This protocol is triggered whenever a Radiology\]

  

ENTRY ACTION:

 

EXIT ACTION:

  

TYPE: event driver  Press \<return\> at this field to go to next screen

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

   

COMMAND:                                  Press \<PF1\>H for help

             HL7 EVENT DRIVER                         PAGE 2 OF 2

             RA REG 2.3                   

------------------------------------------------------------------------

     

SENDING APPLICATION: RA-VOICE-SERVER

TRANSACTION MESSAGE TYPE: ORM                        EVENT TYPE: O01

       MESSAGE STRUCTURE:

           PROCESSING ID:                            VERSION ID: 2.3

         ACCEPT ACK CODE:                  APPLICATION ACK TYPE:

 

 RESPONSE PROCESSING RTN: \*\*\*\*\*\*\*\*\*\*\*\*\*\*                           

                       SUBSCRIBERS

      RA TALKLINK ORM   Remove VR ORM subscriber

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  

### Step 2 - Remove subscribers from existing ORU event driver protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For the RA RPT 2.3 protocol (or the appropriate protocol if the site is using a version previous to v2.3), remove the voice recognition ORU subscriber protocol.

For TalkStation, it is usually RA TALKLINK ORU Note ORU

For PowerScribe, it is usually RA PSCRIBE ORU Note ORU

For RadWhere, it is usually RA RADWHERE ORU Note ORUExample for Step 2

Select OPTION NAME: HL7 MAIN MENU  HL MAIN MENU     HL7 Main Menu

 

                 Event monitoring menu ...

                 Systems Link Monitor

                 Filer and Link Management Options ...

                 Message Management Options ...

                 Interface Developer Options ...

                 Site Parameter Edit

          HLO    HL7 (Optimized) MAIN MENU ...

 

Select HL7 Main Menu Option:  Interface Developer Options

 

          EA     Application Edit

          EP     Protocol Edit

          EL     Link Edit

          VI     Validate Interfaces

                 Reports ...

 

Select Interface Developer Options Option:  Protocol Edit

 

Select PROTOCOL NAME: RA RPT 2.3   Select v2.3 event driver protocol

   

       HL7 INTERFACE SETUP                         PAGE 1 OF 2

-----------------------------------------------------------------------

 

       NAME: RA RPT 2.3                                            

 

DESCRIPTION (wp):   \[This protocol is triggered whenever a Radiology\]

 

ENTRY ACTION:

 

EXIT ACTION: 

 

TYPE: event driver  Press \<return\> at this field to go to next screen

 

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

   

COMMAND:                                  Press \<PF1\>H for help

         HL7 EVENT DRIVER                         PAGE 2 OF 2

         RA RPT 2.3                   

-----------------------------------------------------------------------

     

SENDING APPLICATION: RA-VOICE-SERVER

TRANSACTION MESSAGE TYPE: ORU                        EVENT TYPE: R01

       MESSAGE STRUCTURE:

           PROCESSING ID:                            VERSION ID: 2.3  

         ACCEPT ACK CODE:                  APPLICATION ACK TYPE:

 

 RESPONSE PROCESSING RTN: \*\*\*\*\*\*\*\*\*\*\*\*\*\*                         

                    SUBSCRIBERS

    RA TALKLINK ORU   Remove appropriate VR ORU subscriber

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ 

### Step 3 - Add subscribers to new ORM event driver protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For the RA CANCEL 2.4, RA EXAMINED 2.4, and RA REG 2.4 protocols, add the voice recognition ORM subscriber protocol.

For TalkStation, it is usually RA TALKLINK ORM Note ORM

For PowerScribe, it is usually RA PSCRIBE ORM Note ORM

For RadWhere, it is usually RA RADWHERE ORM Note ORMExample for Step 3Note: You must perform step 1 for the RA REG 2.4, RA CANCEL 2.4 and RA EXAM 2.4 protocols, but only RA REG 2.4 is shown in this example.

Select OPTION NAME: HL7 MAIN MENU  HL MAIN MENU     HL7 Main Menu

 

                 Event monitoring menu ...

                 Systems Link Monitor

                 Filer and Link Management Options ...

                 Message Management Options ...

                 Interface Developer Options ...

                 Site Parameter Edit

          HLO    HL7 (Optimized) MAIN MENU ...

 

Select HL7 Main Menu Option:  Interface Developer Options

 

          EA     Application Edit

          EP     Protocol Edit

          EL     Link Edit

          VI     Validate Interfaces  
Reports ...

 

Select Interface Developer Options Option:  Protocol Edit

 

Select PROTOCOL NAME: RA REG 2.4   Select v2.4 event driver protocol

   

         HL7 INTERFACE SETUP                         PAGE 1 OF 2

-----------------------------------------------------------------------

 

         NAME: RA REG 2.4                                             

DESCRIPTION (wp):   \[This protocol is triggered whenever a Radiology\]

  

ENTRY ACTION: 

EXIT ACTION:

  

  TYPE: event driver  Press \<return\> at this field to go to next screen

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

   

COMMAND:                                  Press \<PF1\>H for help

          HL7 EVENT DRIVER                         PAGE 2 OF 2

          RA REG 2.4                   

-----------------------------------------------------------------------

      

SENDING APPLICATION: RA-VOICE-SERVER

 TRANSACTION MESSAGE TYPE: ORM                      EVENT TYPE: O01

        MESSAGE STRUCTURE:

            PROCESSING ID:                      VERSION ID: 2.4   

          ACCEPT ACK CODE:                APPLICATION ACK TYPE:

 

  RESPONSE PROCESSING RTN: \*\*\*\*\*\*\*\*\*\*\*\*\*\*                              

                   SUBSCRIBERS

       RA TALKLINK ORM   Add appropriate VR ORM subscriber

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

#### Step 4 - Add subscribers to new ORU event driver protocol

For the RA RPT 2.4 protocol, add the voice recognition ORU subscriber protocol.

For TalkStation, it is usually RA TALKLINK ORU Note ORU

For PowerScribe, it is usually RA PSCRIBE ORU Note ORU

For RadWhere, it is usually RA RADWHERE ORU Note ORUExample for Step 4

Select OPTION NAME: HL7 MAIN MENU  HL MAIN MENU     HL7 Main Menu

 

                 Event monitoring menu ...

                 Systems Link Monitor

                 Filer and Link Management Options ...

                 Message Management Options ...

                 Interface Developer Options ...

                 Site Parameter Edit

          HLO    HL7 (Optimized) MAIN MENU ...

 

Select HL7 Main Menu Option:  Interface Developer Options

 

          EA     Application Edit

          EP     Protocol Edit

          EL     Link Edit

          VI     Validate Interfaces

                 Reports ...

 

Select Interface Developer Options Option:  Protocol Edit

 

Select PROTOCOL NAME: RA RPT 2.4   Select v2.4 event driver protocol

   

         HL7 INTERFACE SETUP                         PAGE 1 OF 2

-----------------------------------------------------------------------

 

NAME: RA RPT 2.4                                            

 

DESCRIPTION (wp):   \[This protocol is triggered whenever a Radiology\]

 

ENTRY ACTION:

 

EXIT ACTION:

  

        TYPE: event driver  Press \<return\> at this field to go to next screen

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

   

COMMAND:                                  Press \<PF1\>H for help

         HL7 EVENT DRIVER                         PAGE 2 OF 2

         RA RPT 2.4                   

-----------------------------------------------------------------------

     

SENDING APPLICATION: RA-VOICE-SERVER

TRANSACTION MESSAGE TYPE: ORU                        EVENT TYPE: R01

       MESSAGE STRUCTURE:

           PROCESSING ID:                            VERSION ID: 2.4  

         ACCEPT ACK CODE:                  APPLICATION ACK TYPE:

 RESPONSE PROCESSING RTN: \*\*\*\*\*\*\*\*\*\*\*\*\*\*                       

                     SUBSCRIBERS

         RA TALKLINK ORU   Add appropriate VR ORU subscriber

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_   

### Step 5 - Change the Version ID field of existing message receipt protocol to 2.4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For the existing message receipt protocol, change the Version ID field to 2.4.

For TalkStation, it is usually RA TALKLINK TCP SERVER REPORT

For PowerScribe, it is usually RA PSCRIBE TCP SERVER REPORT

For RadWhere, it is usually RA RADWHERE TCP SERVER REPORT

Example for Step 5

Select OPTION NAME: HL7 MAIN MENU  HL MAIN MENU     HL7 Main Menu

 

               Event monitoring menu ...

               Systems Link Monitor

               Filer and Link Management Options ...

               Message Management Options ...

               Interface Developer Options ...

               Site Parameter Edit

        HLO    HL7 (Optimized) MAIN MENU ...

 

Select HL7 Main Menu Option:  Interface Developer Options

 

        EA     Application Edit

        EP     Protocol Edit

        EL     Link Edit

        VI     Validate Interfaces

               Reports ...

 

Select Interface Developer Options Option: EP  Protocol Edit

 

Select PROTOCOL NAME:  RA TALKLINK TCP SERVER RPT  Select existing message receipt event

> driver protocol (TALKLINK is used in this example)

 

        HL7 INTERFACE SETUP                         PAGE 1 OF 2

-----------------------------------------------------------------------

 

NAME: RA TALKLINK TCP SERVER RPT                            

 

DESCRIPTION (wp):   \[Driver protocol for sending report to VISTA Rad\]

 

ENTRY ACTION:

 

EXIT ACTION: 

 

        TYPE: event driver  Press \<return\> at this field to go to next screen

 

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

 

          HL7 EVENT DRIVER                         PAGE 2 OF 2

          RA TALKLINK TCP SERVER RPT 

  

-----------------------------------------------------------------------

SENDING APPLICATION: RA-TALKLINK-TCP

 TRANSACTION MESSAGE TYPE: ORU              EVENT TYPE: R01

        MESSAGE STRUCTURE:          

            PROCESSING ID:                  VERSION ID: 2.3 Change this field to 2.4

 

          ACCEPT ACK CODE:                  APPLICATION ACK TYPE:

 

 RESPONSE PROCESSING RTN:

                           SUBSCRIBERS

  RA TALKLINK TCP REPORT

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### Step 6 - Turn on the use of the long site accession number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option, Site Accession Number Set-up, functions as the *switch* to turn on the use of the Site Specific Accession Number (SSAN).

Until this field is set to YES, the system will not generate and store the SSAN during the registration of a new case.

Only when all devices are able to handle the SSAN, should this field be set to YES, at which point, the system will generate and store the SSAN during Registration.

Example for Step 6

    

Select OPTION NAME: RA SITEMANAGER       IRM Menu

  

          Device Specifications for Imaging Locations

          Distribution Queue Purge

          Failsoft Parameters

          Imaging Type Activity Log

          Purge Data Function

          Rebuild Distribution Queues

          Report File x-ref Clean-up Utility

          Site Accession Number Set-up

          Credit completed exams for an Imaging Location

          Resource Device Specifications for Division

          Schedule Perf. Indic. Summary for 15th of month

          Template Compilation

  Select IRM Menu Option: Site Accession Number Set-up

 

   Warning: Turning on the Site Specific Accession Number should only

   be done in conjunction with using the RA v2.4 messaging protocols.

 

   NOTE: Changing the Site Specific Accession Number parameter at a

   multidivisional site will change the parameter for ALL divisions.

 

Current value of Site Specific Accession Number parameter: NO

Use Site Specific Accession Number? YES

# ### ### #### [^1]: <span id="_Ref221675367" class="anchor"></span> Patch RA\*5\*78 May 2009: Added Legacy to the heading

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[^2]: Patch RA\*5\*47 August 2011: Added the name of the updated HL7 Specification for v2.4

[^3]: <span id="_Ref257282758" class="anchor"></span> Patch RA\*5\*47 August 2011: Added an example message for HL7 v2.4.

[^4]: Patch RA\*5\*25 Example changed to add OBX segments

[^5]: Patch RA\*5\*25 Example changed

[^6]: <span id="_Ref257282768" class="anchor"></span> Patch RA\*5\*47 August 2011: Added an example message for HL7 v2.4, single procedure.

[^7]: <span id="_Ref257282776" class="anchor"></span> Patch RA\*5\*47 August 2011: Added an example message for HL7 v2.4, printset.

[^8]: <span id="_Ref257282789" class="anchor"></span> Patch RA\*5\*47 August 2011: Added an example message for HL7 v2.4, ACK.

[^9]: <span id="_Ref257282710" class="anchor"></span> Patch RA\*5\*78 May 2009: Added Legacy to the heading

[^10]: <span id="_Ref221675403" class="anchor"></span> Patch RA\*5\*78 May 2009: Added Legacy to the heading

[^11]: The term COTS product is used throughout meaning Commercial Off-The-Shelf product

[^12]: Patch RA\*5\*25 Tech comment added

[^13]: <span id="_Ref257118979" class="anchor"></span> Patch RA\*5\*47 August 2011: Removed the original 20. TalkStation users are not allowed to group sets of exams together and mark them for a single report….

[^14]: Patch RA\*5\*25, Divisional Filtering

[^15]: Patch RA\*5\*25, Divisional Filtering

[^16]: Patch RA\*5\*25

[^17]: Patch RA\*5\*25

[^18]: Patch RA\*5\*25

[^19]: Patch RA\*5\*25

[^20]: Patch RA\*5\*25

[^21]: Patch RA\*5\*25

[^22]: Patch RA\*5\*25, Divisional Filtering

[^23]: Patch RA\*5\*25, Divisional Filtering

[^24]: Patch RA\*5\*25, Divisional Filtering

[^25]: Patch RA\*5\*25

[^26]: <span id="_Ref257118989" class="anchor"></span> Patch RA\*5\*47 August 2011: Removed the original 19. PowerScribe users are not allowed to group sets of exams together and mark them for a single report….

[^27]: Patch RA\*5\*25, Divisional Filtering

[^28]: Patch RA\*5\*25, Divisional Filtering

[^29]: Patch RA\*5\*25

[^30]: Patch RA\*5\*25

[^31]: Patch RA\*5\*25

[^32]: Patch RA\*5\*25

[^33]: Patch RA\*5\*25

[^34]: Patch RA\*5\*25, Divisional Filtering

[^35]: Patch RA\*5\*25, Divisional Filtering

[^36]: Patch RA\*5\*25, Divisional Filtering

[^37]: Patch RA\*5\*25

[^38]: Patch RA\*5\*25

[^39]: Patch RA\*5\*47 August 2011: Added a section about the HL7 messaging version 2.4: S*etup Instructions/Examples for using IHE compliant HL7 v2.4 Protocols*