---
title: LA*5.2*80/LR*5.2*427 LDSI/LEDI IV AP MICRO Configuration Guide
doc_type: CFG
doc_label: Configuration Guide
doc_layer: patch
doc_subject: 
app_code: LEDI
app_name: "Laboratory: Electronic Data Interchange"
section: CLI
app_status: active
pkg_ns: LA
patch_ver: 5.2
patch_id: LA*5.2*80
group_key: "LEDI:LA:5.2"
file_numbers: 
  - 64
security_keys: []
menu_options: 3
description: 
audience: 
keywords: 
  - span
  - class
  - mark
  - host
  - shipping
  - facility
  - test
  - laboratory
  - edit
  - collection
page_count: 0
word_count: 25544
section_count: 13
table_count: 0
figure_count: 42
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Electr_Data_Intrchg_(LEDI)/ledi_iv_ap_micro_configuration_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Electr_Data_Intrchg_(LEDI)/ledi_iv_ap_micro_configuration_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=75"
---

Laboratory Electronic Data Interchange  
(LEDI IV)

VA Shield

![](la-5-2-80-lr-5-2-427-ldsi-ledi-iv-ap-micro-configuration-guide/001.png)

LEDI IV Update  
AP/MICRO Configuration Guide

Patches LR\*5.2\*427/LA\*5.2\*80

September 2013

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Development (PD)

Revision History

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 51%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>August 2009</td>
<td><p>For Patches LA*5.2*74 and LR*5.2*350</p>
<p>created Implementation Guide, Technical Manual, and Security Guide</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>March 2013</td>
<td><p>Made modifications to this document for Patches LA*5.2*80 and LR*5.2*427.</p>
<p>Lab personnel configuring the AP/MICRO interface for VA-to-VA, VA to DoD and VA to Commercial Reference Labs will use it.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>April 2013</td>
<td><p>Added paragraph numbering.</p>
<p>Included input from LEDI IV Update Development.</p>
<p>Working draft ready for test site use.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>May 2013</td>
<td><p>Added disclaimer for AP/MICRO testing with the LEDI IV Update.</p>
<p>Cleaned up the headings.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>July 2013</td>
<td><p>CLIN Team 4 and Development changes are below:</p>
<ul>
<li><p>Section 1 Introduction: Reduced the number of paragraphs.</p></li>
<li><p>Section 1 Introduction: Added that the LIMs at the host and collection sites must have matching shipping configurations. Added reference to the LEDI IV Install Guide for details.</p></li>
<li><p>Overview, C, Step 7: Replaced the words “A new Set-of-Codes field” with “New fields”.</p></li>
<li><p>Overview, C Step 10: Clarified the wording in this sentence.</p></li>
<li><p>Section C., A, 3: Deleted an entry in the Lab Electronic Codes File #64.061.</p></li>
<li><p>Section C. Step 3: Changed the wording from “Database Code” to “Entry in the Lab Electronic Codes File # 64.061”.</p></li>
<li><p>Section C. 5, step 5: Changed the order of the wording in the title to: “LIM: Set up the HL7 environment and Auto Instrument file to receive results from a Host Facility laboratory”.</p></li>
<li><p>Section C. 5, step 5: Bolded those fields on the LEDI Setup screen that require user input,</p></li>
<li><p>Section C. Step 7 (IRM Setups) Item 3, Note: Removed entire Note.</p></li>
<li><p>Section C. Step 7 (IRM Setups) Item 4: Moved up the example of setting up the HL7 Environment Screen.</p></li>
<li><p>Section 2. A, point 3: Removed the reference to the LDSI National Implementation Plan.</p></li>
<li><p>Section 2.D: Modified steps 3, 5, 6 and 9 under AP.</p></li>
<li><p>Section 2. C, step 1: Added details on who can be added to the Alert Mail Group.</p></li>
<li><p>Section 3. C, Step 3, item 7: Added the option Map All Susceptibilities to the VA to DoD interface.</p></li>
<li><p>Section D, 2, Step 1: DoD to VA Step 2: Added details on who can be added to the Alert Mail Group.</p></li>
<li><p>Section 3. D, Step 3, VA to DoD: Specified that sample codes and names for each test should be exchanged between VA and DoD.</p></li>
<li><p>Section 3. D, Step 4 VA to DoD: Added screen capture showing how to Manage AP Test Mappings.</p></li>
<li><p>Section 3. D, Step 8: Clarified 4 of the steps that the Collecting Facility must do,</p></li>
<li><p>Section 3. E, Step 1: Added CLIA ID field to the</p></li>
<li><p>Institution set up instructions.</p></li>
<li><p>Section 3. E, Step 3, bullet points 3 and 4: Added details for the LIM on how to Map All Susceptibilities and Test Mappings between VA Collecting and VA Host facilities when doing interface Set ups.</p></li>
<li><p>Section 3. F, Step 1: Added CLIA ID field to the</p></li>
<li><p>Host and Collection Institution set up instructions.</p></li>
<li><p>Section 3. F, 2: Added details on who can be added to the Orders Received Alert mail group.</p></li>
<li><p>Section 4. A and B: Specified that a hyperlink can take the user from the checklists for host and collection facilities direct to sample screen shots.</p></li>
<li><p>For all three Collecting Facility Interface (VA to VA, VA to DoD, VA to Commercial Reference Lab) Set ups: Standardized the process for setting up Load Work List and adding a profile to the load/work list used to process results for each subscript handled at that lab.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>August 2013</td>
<td><ul>
<li><blockquote>
<p>Added updates based on feedback from the LEDI IV Update Patch using the AP/MICRO Interface. (See revision marks below.)</p>
</blockquote></li>
<li><blockquote>
<p>Decision made on 8/8/13 to remove the AP Results from the LEDI IV Update Patch, due to regulatory concerns. Added a disclaimer to each of the relevant sections – VA Collecting, DoD Collecting and Commercial Reference Lab Collecting that AP Results would still be disabled in this patch. This decision is made per Sr. Level Leadership on 8/8/13.</p>
</blockquote></li>
<li><blockquote>
<p>Added the following mail group passage to sections 3.3.2, 3.4.2, 3.5.2, 3.6.2: “If a mail group already exists for lab HL7 error alerts, then the existing mail group can be used instead of creating a new one”.</p>
</blockquote></li>
<li><blockquote>
<p>Section 3.3.8 &amp; 3.5.7.2: Added “Answer YES to the Exclude previously removed tests from building’ question so that previous tests – which could number in the thousands- will not be included.” (Issue was reported from field-testing.)</p>
</blockquote></li>
<li><blockquote>
<p>Updated Collecting Facility - VA to VA with one note under the Micro section: That the LIM must ensure that the topography and etiology must match exactly between the host and collection sites.</p>
</blockquote></li>
<li><blockquote>
<p>Updated Collecting Facility - VA to VA with two notes under the AP section: The first is that the LIMS must ensure that the topography and etiology must match exactly between the host and collection sites. The second is that the LIMS may use an alternate specimen of “TISSUE” if there is a Collection Sample that does not map to a SNOMED CT.</p>
</blockquote></li>
<li><blockquote>
<p>Updated Section Collecting Facility - VA to VA with details of a user prompt when the LEDI HL7 code is “Other” or “Another message part”. The system prompts the user at the Host site to update the specimen and collection sample.</p>
</blockquote></li>
<li><blockquote>
<p>Made the following changes per the August 22<sup>nd</sup> peer review:</p>
</blockquote></li>
<li><blockquote>
<p>Made the General Overview section generic.</p>
</blockquote></li>
<li><blockquote>
<p>Moved the VA to VA interface detailed instructions up to Sections 3.3 and 3.4.</p>
</blockquote></li>
<li><blockquote>
<p>Moved the VA to DoD interface detailed instructions down to Sections 3.5 and 3.6</p>
</blockquote></li>
<li><blockquote>
<p>Removed all but one reference to the sending of the HL7 message for AP results still being disabled.</p>
</blockquote></li>
<li><blockquote>
<p>Moved the Message Validation Section for AP and MICRO to a newly-created appendix.</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>August 2013</td>
<td>Technical edit</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>August 2013</td>
<td><p>Several more minor edits:</p>
<ul>
<li><p>Realigned two letters in Figure 36,</p></li>
<li><p>Added “VA Shield” for 508.</p></li>
</ul>
<ul>
<li><p>Updates from Peer Review:</p></li>
<li><p>Added File names next to File numbers.</p></li>
<li><p>Modified bulleting throughout to ensure consistency between sections.</p></li>
<li><p>Added cross reference links between the LIM set up sections and the Appendix section.</p></li>
<li><p>Lined up sections to standardize bullet points.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>August 2013</td>
<td>Edited format</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>September 2013</td>
<td><p>Modified revision history to reflect the August 22 Peer Review and to address several defects:</p>
<ul>
<li><blockquote>
<p>This revision from August 2013 no longer applies: Section 3.3.8 &amp; 3.5.7.2: Added “Answer YES to the Exclude previously removed tests from building’ question so that previous tests – which could number in the thousands- will not be included.”</p>
</blockquote></li>
<li><blockquote>
<p>Appendix - Message Validation and Creating Order – MICRO Exceptions: Removed the sentence that read, “If no existing entry is found, the system will automatically create a new entry in Topography Field file (#61) based off the SCT information from the message”. It was fixed by a Code change.</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

Table of Contents

This page intentionally left blank for double-sided printing.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Overview of LEDI IV](#overview-of-ledi-iv)
  - [General Processing Overview](#general-processing-overview)
  - [LEDI IV Microbiology](#ledi-iv-microbiology)
  - [LEDI IV Anatomic Pathology](#ledi-iv-anatomic-pathology)
- [Implementation and Updates for Patches LA\5.2\80 and LR\5.2\427](#implementation-and-updates-for-patches-la5280-and-lr52427)
  - [LEDI IV HL7 Messaging Interface Implementation Requirements](#ledi-iv-hl7-messaging-interface-implementation-requirements)
  - [LEDI IV Two-part Implementation Instructions](#ledi-iv-two-part-implementation-instructions)
    - [Collecting Facility](#collecting-facility)
    - [Host Facility](#host-facility)
  - [Collecting Facility–VA to VA Implementation Instructions](#collecting-facilityva-to-va-implementation-instructions)
    - [Step 1: IRM set up the INSTITUTION file (#4)](#step-1-irm-set-up-the-institution-file-4)
    - [Step 2: IRM create LEDI-related mail groups using the ‘Mail Group Edit \[XMEDITMG\]’ option](#step-2-irm-create-ledi-related-mail-groups-using-the-mail-group-edit-xmeditmg-option)
    - [Step 3: LIM set up the lab test files to send specimens to the Host facility laboratory](#step-3-lim-set-up-the-lab-test-files-to-send-specimens-to-the-host-facility-laboratory)
    - [Step 4: LIM set up the Lab Shipping Files](#step-4-lim-set-up-the-lab-shipping-files)
    - [Step 5: LIM set up HL7 Environment and the Lab Auto-instrument file to receive results from a Host facility laboratory](#step-5-lim-set-up-hl7-environment-and-the-lab-auto-instrument-file-to-receive-results-from-a-host-facility-laboratory)
    - [Step 6: LIM Map Micro and/or AP Test](#step-6-lim-map-micro-andor-ap-test)
    - [Step 7: LIM map code concepts to related area of Lab](#step-7-lim-map-code-concepts-to-related-area-of-lab)
    - [Step 8: IRM no further action is required for VA to VA LEDI interfaces](#step-8-irm-no-further-action-is-required-for-va-to-va-ledi-interfaces)
    - [Step 9: LIM work with the LIM at the Host facility to test the system](#step-9-lim-work-with-the-lim-at-the-host-facility-to-test-the-system)
    - [Step 10: LIM train end users](#step-10-lim-train-end-users)
  - [Host Facility–VA to VA Implementation Instructions](#host-facilityva-to-va-implementation-instructions)
    - [Step 1: IRM set up the INSTITUTION file (#4)](#step-1-irm-set-up-the-institution-file-4-1)
    - [Step 2: IRM create LEDI-related mail groups using the ‘Mail Group Edit \[XMEDITMG\]’ option](#step-2-irm-create-ledi-related-mail-groups-using-the-mail-group-edit-xmeditmg-option-1)
    - [Step 3: LIM set up the lab test files to receive specimens from the Collecting Facility laboratory](#step-3-lim-set-up-the-lab-test-files-to-receive-specimens-from-the-collecting-facility-laboratory)
    - [Step 4: LIM must set up the Host facility LAB SHIPPING CONFIGURATION file (#62.9)](#step-4-lim-must-set-up-the-host-facility-lab-shipping-configuration-file-629)
    - [Step 5: LIM set up a Collecting and/or Host facility HL7 Environment](#step-5-lim-set-up-a-collecting-andor-host-facility-hl7-environment)
    - [Step 6: IRM no further action is required for VA to VA LEDI interfaces](#step-6-irm-no-further-action-is-required-for-va-to-va-ledi-interfaces)
    - [Step 7: LIM work with the LIM at the Collecting Facility to test the system](#step-7-lim-work-with-the-lim-at-the-collecting-facility-to-test-the-system)
  - [Collecting Facility–VA to DoD Laboratory Implementation Instructions](#collecting-facilityva-to-dod-laboratory-implementation-instructions)
    - [Step 1: IRM set up the INSTITUTION file (#4)](#step-1-irm-set-up-the-institution-file-4-2)
    - [Step 2: IRM create LEDI-related mail groups using the ‘Mail Group Edit \[XMEDITMG\]’ option](#step-2-irm-create-ledi-related-mail-groups-using-the-mail-group-edit-xmeditmg-option-2)
    - [Step 3: LIM set up the lab test files to send specimens to the Host facility laboratory](#step-3-lim-set-up-the-lab-test-files-to-send-specimens-to-the-host-facility-laboratory-1)
    - [Step 4: LIM set up the Lab Shipping Files](#step-4-lim-set-up-the-lab-shipping-files-1)
    - [Step 5: LIM set up the HL7 Environment and Auto Instrument file to receive results from a Host facility laboratory](#step-5-lim-set-up-the-hl7-environment-and-auto-instrument-file-to-receive-results-from-a-host-facility-laboratory)
    - [Step 6: LIM populate Lab Code Mapping file with DoD codes](#step-6-lim-populate-lab-code-mapping-file-with-dod-codes)
    - [Step 7: IRM complete the HL7 Environment setup for TCP/IP HL7 transport protocol](#step-7-irm-complete-the-hl7-environment-setup-for-tcpip-hl7-transport-protocol)
    - [Step 8: LIM work with the interface coordinator at the Reference laboratory to test the system](#step-8-lim-work-with-the-interface-coordinator-at-the-reference-laboratory-to-test-the-system)
    - [Step 9: LIM train end users](#step-9-lim-train-end-users)
  - [Host Facility–DoD to VA Laboratory Implementation Instructions](#host-facilitydod-to-va-laboratory-implementation-instructions)
    - [Step 1: IRM set up the INSTITUTION file (#4)](#step-1-irm-set-up-the-institution-file-4-3)
    - [Step 2: IRM create LEDI-related mail groups using the ‘Mail Group Edit \[XMEDITMG\]’ option](#step-2-irm-create-ledi-related-mail-groups-using-the-mail-group-edit-xmeditmg-option-3)
    - [Step 3: LIM provide DoD laboratory with your electronic test catalog](#step-3-lim-provide-dod-laboratory-with-your-electronic-test-catalog)
    - [Step 4: LIM Map Micro and/or AP Test](#step-4-lim-map-micro-andor-ap-test)
    - [Step 5: LIM set up the LAB SHIPPING CONFIGURATION file (#62.9)](#step-5-lim-set-up-the-lab-shipping-configuration-file-629)
    - [Step 6: LIM set up the HL7 Environment to receive orders from the Collecting facility laboratories](#step-6-lim-set-up-the-hl7-environment-to-receive-orders-from-the-collecting-facility-laboratories)
    - [Step 7: IRM complete the HL7 Environment setup for TCP/IP HL7 transport protocol](#step-7-irm-complete-the-hl7-environment-setup-for-tcpip-hl7-transport-protocol-1)
    - [Step 8: LIM work with the interface coordinator at the Collecting facility laboratory to test the system](#step-8-lim-work-with-the-interface-coordinator-at-the-collecting-facility-laboratory-to-test-the-system)
    - [Step 9: LIM train end users](#step-9-lim-train-end-users-1)
  - [Collecting Facility–VA to Commercial Reference Laboratory](#collecting-facilityva-to-commercial-reference-laboratory)
    - [Step 1: IRM set up the INSTITUTION file (#4)](#step-1-irm-set-up-the-institution-file-4-4)
    - [Step 2: IRM create LEDI-related mail groups using the ‘Mail Group Edit \[XMEDITMG\]’ option](#step-2-irm-create-ledi-related-mail-groups-using-the-mail-group-edit-xmeditmg-option-4)
    - [Step 3: LIM set up the lab test files to send specimens to the commercial Reference laboratory](#step-3-lim-set-up-the-lab-test-files-to-send-specimens-to-the-commercial-reference-laboratory)
    - [Step 4: LIM set up the Lab Shipping Files](#step-4-lim-set-up-the-lab-shipping-files-2)
    - [Step 5: LIM set up the HL7 Environment and the Lab Auto-instrument file to receive results from a Host facility laboratory](#step-5-lim-set-up-the-hl7-environment-and-the-lab-auto-instrument-file-to-receive-results-from-a-host-facility-laboratory)
    - [Step 6: LIM map Micro and/or AP Tests](#step-6-lim-map-micro-andor-ap-tests)
    - [Step 7: LIM map code concepts to related area of Lab](#step-7-lim-map-code-concepts-to-related-area-of-lab-1)
    - [Step 8: IRM complete the HL7 Environment setup for TCP/IP HL7 transport protocol](#step-8-irm-complete-the-hl7-environment-setup-for-tcpip-hl7-transport-protocol)
    - [Step 9: LIM work with the interface coordinator at the Reference laboratory to test the system](#step-9-lim-work-with-the-interface-coordinator-at-the-reference-laboratory-to-test-the-system)
    - [Step 10: LIM train end users](#step-10-lim-train-end-users-1)
- [LEDI IV Update AP/MICRO Configuration Checklist](#ledi-iv-update-apmicro-configuration-checklist)
  - [Checklist for a Collecting Facility Setting up a Host Facility](#checklist-for-a-collecting-facility-setting-up-a-host-facility)
  - [Checklist for a Host Facility Setting Up a Collecting Facility](#checklist-for-a-host-facility-setting-up-a-collecting-facility)
- [Appendix](#appendix)
LEDI IV Update introduces an interface for Anatomic Pathology and Microbiology (AP/MICRO) that allows VA, Commercial Reference and DoD laboratories to communicate with each other. The software has the capacity and features necessary for sharing secure, encrypted laboratory data between the VA, Commercial Reference and DoD facilities.
LEDI IV Update patch allows lab tests in the Microbiology subscript area of the lab to be electronically ordered and resulted. The software supports the sending and receiving of Microbiology orders and results between two facilities, the Collecting and Host lab (reference).
Note 1: This patch enables the micro interface for orders and results, as well as the AP orders interface. However, the sending of AP results from VA Host Labs to other VA Labs, DoD Labs and Commercial Reference Labs will still be disabled. The AP Host Labs will continue to use their existing processes to return the AP report to the Collecting Labs.
This document provides the lab users with what is necessary to configure the AP/MICRO interface. Refer to the LEDI IV User Manual for instructions on how to use the AP/MICRO interface to send and receive lab orders.
Note 2: This patch modifies the checks that are performed when an incoming order is received at a host site. Previously, if the specimen from the order matched the specimen configured on the shipping configuration, the order would be accepted, even if the SNOMED CT mappings did not match. This patch changes the checking, so that in this scenario the host site rejects the order with an HL7 Application Error (AE). Due to this change, after a LEDI host site installs this patch, they might start seeing Application Errors (AEs) being generated for incoming HL7 orders. If this occurs, notify the collecting site. The collecting site will need to ensure that the specimen and collection samples they are using are correctly mapped to the same SNOMED CT ID at the host site.
Exceptions to Testing
The AP/Micro interface is being enabled with the LEDI IV Update patch and there are no test sites available to test the AP/Micro interface between commercial labs or the DoD labs. This functionality was tested with LEDI IV Version 19 test sites in the past. However, the functionality was disabled in the LEDI IV national release.
There will be no further testing with DoD or Commercial Reference Labs prior to going live.
This page intentionally left blank for double-sided printing.

# Overview of LEDI IV

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## General Processing Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the Laboratory software, the collection site creates an HL7-formatted electronic order message.

- The AP and Microbiology order message contains all required patient and test information to indicate to the collecting system which procedures to perform.
- The order message contains the demographics of the patient (name, social security number, location, and ordering physician), as well as lab test information.
- The software hands the HL7-formatted message to the HL7 software for delivery to the host system HL7 server.

The host system’s HL7 server processes the order message of the collecting site.

- The host system’s Laboratory performs the analytical test procedures to generate lab test results.
- The lab test results are verified and released in the host system by authorized laboratory personnel.
- The host Laboratory creates an HL7-formatted message containing result information, and sends the message to the HL7 server of the collecting site.

Refer to Note 1 in the Introduction section for AP Results – they are still disabled.

The collecting site HL7 server accepts and processes the HL7 message. The HL7 server passes the message to the LEDI software for further processing.

- The LEDI software stores the electronic result message to be accepted by the medical center’s laboratory personnel.
- The submitting laboratory staff reviews the lab results on the screen for completeness and clinical credibility.
- If the lab results are acceptable, the submitting laboratory personnel certify and record the results in the laboratory system and the lab results become part of the electronic clinical record of the patient.

## LEDI IV Microbiology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several enhancements were provided by patches LA\*5.2\*74 and LR\*5.2\*350 for Microbiology. These enhancements are now utilized in this update patch for the MICRO interface.

- TOPOGRAPHY FIELD file (#61), ETIOLOGY FIELD file (#61.2), and COLLECTION SAMPLE file (#62) include mapping specimen and sample codes using appropriate SNOMED CT codes.
- New codes are added to the LAB ELECTRONIC CODES file (#64.061) to support messaging via HL7 messaging.
- Additional information is added to the LABORATORY PENDING ORDER file (#69.6) for HL7 messaging.
- HL7 messaging is enhanced to process the following sections.
1.  Bacteriology
2.  Mycobacterium
3.  Mycology
4.  Virology
5.  Parasitology
- The electronic messaging functionality of the LAB DATA file (#63) is enhanced to handle multiple *Isolate* for any given culture.
- Eight new fields are added to the LAB DATA file (#63), ORDER TEST multiple field (#.35), which includes microbiology data resulting from LEDI-generated orders.
1.  Ordered Urgency field (#2)
6.  CPRS Order \# field (#3)
7.  Lab Order \# field (#4)
8.  Ordered Type field (#5)
9.  Ordering Provider Local field (#6)
10. Ordering Provider Remote field (#7)
11. Specimen Topography field (#8)
12. Collection Sample field (#9)
- New fields are added to the LAB DATA file (#63) (result storage) for urgency: the CPRS order number and the order type (i.e., original, reflex, add-on).
- The LEDI software application is enhanced by triggering an event to notify and return results to the Collecting facility laboratory, once an order is identified as LEDI associated and released. A new API was created to generate the new LEDI messages.
- Six new fields are added to the LAB DATA file (#63) (result storage) for the LEDI result (ORU) node in the MI subscript for LDSI generated orders.
1.  UID field (#.31)
13. Ordering site field (#.32)
14. Collection site field (#.33)
15. Host UID field (#.34)
16. Order Site UID field (#.342)
17. Ordered Test field (#.35)
- The LAB DATA file (#63) was enhanced to store LOINC, NLT and SNOMED CT codes on each result and ordered test.
- The VistA Laboratory package is enhanced by creating the new LAB CODE MAPPING file (#62.47). This new file is used to map standard code system concepts to the related area of the Laboratory package database, as well as support mapping codes used in the role identifying the result or expressing the answer.

Several modifications were provided by patches LA\*5.2\*74 and LR\*5.2\*350 for Microbiology. These modifications are now utilized in this update patch for the MICRO interface.

- Routines are modified to store HL7 messaging data in LAB DATA file (#63).
- The MICROBIOLOGY sub file (#63.05) is modified to track ordered tests and ordering information for HL7.

## LEDI IV Anatomic Pathology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several enhancements were provided by patches LA\*5.2\*74 and LR\*5.2\*350 for Anatomic Pathology. These enhancements are now utilized in this update patch for the AP interface.

- The VistA Laboratory Anatomic Pathology section is enhanced by populating the LAB DATA file (#63), ACCESSION file (#68), and LABORATORY ORDER file (#69) with new functionality.
1.  Make AP accession consistent with the rest of laboratory’s accession process.
18. Create and store UID, ordering data, and order number.
- The AP SP, EM, and CY sections are enhanced by creating the new ORDERED TEST sub file (#63.53, \#63.52 and \#63.51). These sub files contain information about the ordered test(s) for this accession. The Ordered Test field (#.01) contains the ordered test NLT code requested by the clinical provider. If the ordered test is a panel, all atomic tests within the panel are associated with the ordered test using that NLT code. These new sub files (#63.53, \#63.52 and \#63.51) contain fifteen fields.
1.  Ordered Test field (#.01)
19. Ordered Urgency field (#2)
20. CPRS Order \# field (#3)
21. Lab Order \# field (#4)
22. Order Type field (#5)
23. Ordering Provider Local field (#6)
24. Ordering Provider Remote field (#7)
25. Specimen Topography field (#8)
26. Collection Sample field (#9)
27. Disposition (#10)
28. Disposition Date/Time (#11)
29. Disposition By (#12)
30. Lab Test Ordered (#13)
31. Parent Test (#14)
32. Parent NLT (#15)
- The SP, CY and EM login process is modified to require a test code selection, an entry from the TOPOGRAPHY FIELD file (#61) and a selection of multiple orderable test code names from LABORATORY TEST file (#60), during AP login using the enhanced ‘Log-in, anat path \[LRAPLG\]’ option.
- The Lab HL7 messaging software is enhanced to handle AP data by storing incoming HL7 result (ORU) messages in the intermediate LAH global for three AP sections.
1.  Cytology – CY
33. Electron Microscopy – EM
34. Surgical Pathology – SP
- The Select Accession Number/Pt Name prompt is modified to accept UIDs, in addition to selecting AP accession numbers for UIDs.
- The AP verification process is modified to accept incoming results processed by personnel outside the VA. The new ‘AP LEDI Data Entry \[LRAP VR\]’ option allows data from the LEDI HOST automated instrument configuration for Anatomic Pathology (LEDI results) to be reviewed individually by accession or by UID.
1.  This new option is located on the ‘\[LRAPD\]’menu.
2.  Incoming results are accepted or rejected by staff via the new ‘AP LEDI Data Entry \[LRAP VR\]’ option.
3.  This option moves the data from the LAH global for storage in LAB DATA file (#63).
4.  Once verified, the data is not available for viewing with this option.

Figure 1. Example of Modified Selection Screen

Data entry for 2008 ? YES// <span class="mark">\<Enter\></span> (YES)

Select one of the following:

1 Accession number

2 Unique Identifier (UID)

3 Patient Name

Select one: 1//

- The *‘Refer*ral Patient Multi-purpose Accession \[LRLEDI\]’ option is modified to process incoming Laboratory HL7 orders for AP.
- The VistA Laboratory LEDI software is used to capture the same data elements that are captured in the ‘Log-in, anat path \[LRAPLG\]’ option.
1.  The captured data elements are stored in the LABORATORY ORDER file (#69).
35. The option ‘Referral Patient Multi-purpose Accession \[LRLEDI\]’ performs the same function as the AP Log-in for referral patients.
- Upon verification of an AP report, an outgoing HL7 result message is triggered via the ‘Verify/release reports, anat path \[LRAPRS\]’ option.

> **NOTE:** Because the outgoing HL7 result messages are for referral patients, these AP reports are not stored in TIU at the HOST site.

- The ‘Manage MI/AP Test Mappings \[LRCAPFF\]’ option is modified to establish the relationships between the LABORATORY TEST file (#60), the WKLD file (#64), and the LAB ELECTRONIC CODES file (#64.061) for LEDI MI/AP tests.
- The patches support the acceptance and processing of AP electronic orders and results via LEDI HL7 messaging.
1.  Determine the test order number, type of specimen and collection sample code for an outgoing order message.
36. Generate HL7 messaging exceptions for incomplete LEDI orders located in LABORATORY PENDING ORDER file (#69.6).
37. Generate HL7 messaging exceptions for LEDI results that cannot be processed.
38. Process incoming HL7 order (ORM) messages from DoD facilities.
39. Process messages and store the orders in the LABORATORY PENDING ORDER file (#69.6).

# Implementation and Updates for Patches LA\*5.2\*80 and LR\*5.2\*427

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## LEDI IV HL7 Messaging Interface Implementation Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Implementation of the HL7 messaging interface between VA to VA, VA to DoD, or VA to Commercial Reference Laboratory, consists of three parts.

1.  VistA Laboratory LEDI IV software
2.  Certified communication software and hardware
3.  Non-VA information system capable of sending and receiving Laboratory HL7 order and result messages

All three requirements must be functional to utilize the capabilities of the LEDI IV software.

> **NOTE:** Implementation, setup, and configuration of vendor- provided hardware and software is not addressed in this document; consult the vendor.

In addition, when implementing an interface with a DoD facility, the Austin Information Technical Center (AITC), VA/DoD Virtual Private Network (VPN)/Firewall will need to be configured to allow traffic between the two facilities.

## LEDI IV Two-part Implementation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To successfully implement the LEDI IV software, the IRM and LIM staffs must follow the detailed setup instructions in the sequence provided. Use the checklists below to ensure that the AP/MICRO interface configuration steps are completed in the appropriate order.

The setup instructions for the LEDI IV implementation consists of two parts: one for the Collecting facility and one for the Host facility.

### Collecting Facility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Collecting facility laboratory must be set up to be able to do four tasks.

- Create an electronic Shipping Manifest, such as specifying lab tests to be performed by the receiving Host facility laboratory.
- Transmit the Shipping Manifest to the Host facility laboratory.
- Transport the specimens to the Host facility laboratory.
- Approve the results received from the Host facility.

### Host Facility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Host facility laboratory must be set up to be able to do four tasks.

- Receive the electronic Shipping Manifest List, transmitted by the Collecting facility laboratory.
- Accession the shipping manifest upon specimen arrival at the Host facility, either by scanning the manifest bar codes or by manually selecting the electronic orders.
- Perform the specified lab tests and verify the lab test results.
- Transmit the lab test results back to the Collecting facility.

## Collecting Facility–VA to VA Implementation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA-to-VA The IRM and LIM staffs must coordinate the implementation of the LEDI IV software and perform the setup instructions in the following sequence for a successful implementation.

### Step 1: IRM set up the INSTITUTION file (#4)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Load or update the local INSTITUTION file (#4), using the ‘Update/refresh Institution file with IMF data \[XUMF LOAD INSTITUTION\]’, if not performed previously.

Check both the Host and Collecting institutions for the four fields from the INSTITUTION file (#4) used by the LEDI IV software.

- Name (#.01) field: The Institution Master File maintains nationally controlled entries for VA and DoD facilities.
- Agency Code (#95) field: Should be set to VA.  
  This field determines the status of the facility and how to set up the LEDI software application.
- Station Number (#99) field: This field is controlled nationally by the Institution Master File. It is used by LEDI to configure VA facilities and set up Lab Shipping fields in the ‘Lab Shipping Management Menu \[LA7S MGR MENU\]’ option.
- CLIA Identifier field: The CLIA ID \# is in the IDENTIFIER field: (#9999) multiple field ID(#.02) field. This field is used to enter the CLIA ID \#. The CLIA ID \# is used when printing lab reports.

### Step 2: IRM create LEDI-related mail groups using the ‘Mail Group Edit \[XMEDITMG\]’ option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Local mail group for the NEW RESULTS Alert: This mail group notifies members when the Lab Universal Interface software processes an HL7 message containing test results.

Example Alert

Lab Messaging–New results received for LA7V HOST 578

- Designate the LIM as the coordinator for the NEW RESULTS Alert mail group.
- The mail group must contain at least one active lab user member.
- This mail group should be comprised of the lab users who process results from the Host facility.

Local mail group for the ERROR ON MESSAGE Alert: This mail group notifies members of error conditions encountered during the processing of a Laboratory HL7 message.

- The LAB MESSAGING mail group can be used for this function. The LAB MESSAGING mail group is a general mail group used by the LAB Universal Interface and LEDI software to address alerts when conditions are detected requiring review and/or corrective action.
- If a mail group already exists for lab HL7 error alerts, then the existing mail group can be used instead of creating a new one.
- The members of this mail group must include the LIM and selected Lab and IRM personnel responsible for maintenance and support of the LAB Universal Interface and LEDI software.
- Designate the LIM as a member of the ERROR ON MESSAGE Alert mail group.

### Step 3: LIM set up the lab test files to send specimens to the Host facility laboratory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Contact the LIM of the Host facility to acquire the following information:
- Accession Area numeric identifier (two-character alphanumeric code).  
  Use an identifier that is not already active in the system.
1.  This identifier is only required when the Host facility laboratory is using the specimen labels and identifiers of the Collecting facility.
2.  If the Host facility is relabeling the Collecting facility specimens, the Collecting facility can use any accession area for the specimens/lab tests.
- Specific test information sent to the Host facility laboratory  
  Use the Host Systems ‘Electronic Catalog Menu \[LAS7 CATALOG MENU\]’ to produce this information.
- Specimen collection requirements
- Schedule of testing
- Patient prep instructions
- National VA Lab Code
4.  Create/edit an accession area in the ACCESSION file (#68) for specimens sent to the Host laboratory. Use the ‘VA FileMan \[DIUSER\], Enter or Edit \[DIEDIT\] option.’
- If your VA Host lab is utilizing your specimen labels, assign the Numeric Identifier provided by the Host facility to the ACCESSION file (#68), Numeric Identifier field (#4).
- Existing or multiple accession areas can be utilized for reference testing.
5.  Edit the LABORATORY TEST file (#60) to send specimens to the Host facility laboratory.  
    New lab tests can be created to match the Host facility laboratory requirements, or existing lab tests can be utilized, if the entries are compatible with the Host facility laboratory requirements.

> **NOTE:** All tests must utilize the Accession Area (file \#68 entry) created in step \#2 that corresponds to the specified numeric identifier.

The option Map All Susceptibilities \[LA7V 62.47 MAP SUSCS\] should be used to ensure that all susceptibilities in the Antimicrobial Susceptibility file (#62.06) are mapped to LOINC codes.

Both Host and Collection sites should use the Manage MI/AP Test Mappings \[LRCAPFF\] to coordinate the mapping of the related LABORATORY tests (#60) to the interface database code mappings from the WKLD CODE file (#64) and the LAB ELECTRONIC CODES file (#64.061). Each AP or MI test being transmitted in the interface should be mapped to a National VA Lab Code and then subsequently mapped to an appropriate SP, CY, EM or MI database code.

Figure 2. Example of Laboratory Test File (#60) Entry for AP Request

NUMBER: 6744                            <span class="mark">NAME:</span> CYTOLOGY REQUEST

  TYPE: OUTPUT (CAN BE DISPLAYED) <span class="mark">SUBSCRIPT:</span> CYTOLOGY

  UNIQUE COLLECTION SAMPLE: NO          HIGHEST URGENCY ALLOWED: ROUTINE

  REQUIRED TEST: YES                    PRINT NAME: CYTOLOGY EXAM

  PRETTY PRINT ENTRY: LRP               PRETTY PRINT ROUTINE: LRSOR

<span class="mark">COLLECTION SAMPLE:</span> TISSUE

<span class="mark">INSTITUTION:</span> LEXINGTON-LD VAMC          <span class="mark">ACCESSION AREA:</span> CYTOPATHOLOGY

INSTITUTION: LEXINGTON-CDD VAMC         ACCESSION AREA: CYTOPATHOLOGY

  <span class="mark">NATIONAL VA LAB CODE:</span> Report Cytology

Figure 3. Example of Laboratory Test File (#60) Entry for Micro Request

NAME: ANAEROBIC CULTURE TYPE: OUTPUT (CAN BE DISPLAYED)

SUBSCRIPT: MICROBIOLOGY UNIQUE ACCESSION \#: NO

UNIQUE COLLECTION SAMPLE: NO LAB COLLECTION SAMPLE: UNKNOWN

TEST COST: 15.38 \*QUICK INDEX: YES

EDIT CODE: BACTERIOLOGY EXTRA LABELS: 0

HIGHEST URGENCY ALLOWED: ASAP FORCED URGENCY: ROUTINE

PRINT NAME: ANAEROB PRETTY PRINT ENTRY: EN

PRETTY PRINT ROUTINE: LRMIPC

COLLECTION SAMPLE: WOUND FORM NAME/NUMBER: MICRO

COLLECTION SAMPLE: DECUBITUS FORM NAME/NUMBER: 10-2129

COLLECTION SAMPLE: EXUDATE FORM NAME/NUMBER: 10-2129

COLLECTION SAMPLE: ABCESS FORM NAME/NUMBER: 10-2129

COLLECTION SAMPLE: ASPIRATE FORM NAME/NUMBER: 10-2129

\*BATCH DATA CODE: NEG BACT RESULTS

SYNONYM: ANA.

GENERAL WARD INSTRUCTIONS: See Microbiology specimen requirements

INSTITUTION: COLLECTOR VAMC ACCESSION AREA: SENDOUTS

ACCESSION WKLD CODE: Micro Bacteriology Culture~MANUAL MICRO

ACCESSION WKLD CODE \#: 87993.7000

NATIONAL VA LAB CODE: Micro Anerobic Culture

RESULT NLT CODE: Micro Anerobic Culture

> **NOTE:** Topographies assigned to collection samples used in the interface must have LEDI HL7 codes assigned that match the Host facility configuration.

Figure 4. Example of Topography Field (#61) File Entry

NUMBER: 8729 <span class="mark">NAME:</span> TISSUE

SNOMED CODE: TISSU WEIGH: YES

ABBREVIATION: TIS <span class="mark">HL7 CODE:</span> TISS

<span class="mark">LEDI HL7:</span> Tissue, unspecified TIME ASPECT: POINT

SYNONYM: TISS

<span class="mark">SNOMED CT ID:</span> 85756007 <span class="mark">SCT CODE STATUS:</span> PREFERRED TERM

<span class="mark">SCT TOP CONCEPT:</span> SCT Body Structure

> **NOTE:** Collection samples used must have SCT ID entries in the Collection Sample (#62) file that match the Host facility configuration.

Figure 5. Example of Collection Sample (#62) File Entry

NUMBER: 133                             <span class="mark">NAME</span>: TISSUE

  <span class="mark">SNOMED CT ID</span>: \<if available\>               SCT CODE STATUS: LOCAL

  <span class="mark">SCT TOP CONCEPT</span>: SCT Specimen

SCT STATUS DATE: DEC 26, 2012@14:49:32  SCT STATUS CHANGED TO: LOCAL

  SCT STATUS USER: LRUSER,LEDI

SCT COMMENT TEXT:  

 File used to apply mapping and/or disposition: LEXINGTON_SCT_1-20-11.TXT;1

- If you do not already have an established LEDI Host Load/Work List for this configuration, then you should create a new test LOAD/WORK LIST file (#68.2) entry to define and accept lab results transmitted by the Host facility laboratory.
- If you already have a LEDI Host Load/Work List for this configuration, then the existing Load/Work List entry should be used.
6.  Add a profile to the load/work list used to process results for each subscript processed. The profiles must contain all resultable lab tests processed by the Host facility laboratory. Configuration of the Default Reference Laboratory field is not required, but it will facilitate the entry of results.

> **NOTE:** There must be separate profiles specified for CH, MI, SP, CY, and EM subscripts.

7.  Add Host antibiotics not currently configured in VistA, using one of the following options:
- If the antibiotic is not defined in LAB DATA file (#63), use the ‘Add a new internal name for an antibiotic \[LRWU7\]’ option to create an internal name for the antibiotic.
- If the antibiotic is not currently in the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06), use the ‘Edit an Antibiotic \[LRWU7 EDIT\]’ option to add the antibiotic.  
  Include mapping to Result NLT and LOINC codes and configure appropriate susceptibility interpretations.
8.  Map Host LOINC codes used to report susceptibility testing using the ‘Edit Susceptibility \[LA7V 62.47 EDIT SUSC\]’ option.

### Step 4: LIM set up the Lab Shipping Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The lab shipping files are located on the ‘Lab Shipping Management Menu \[LA7S MGR MENU\]’ option under the ‘Lab liaison menu \[LRLIAISON\]’ option.

Configure the following four files in the order listed.

- First–LAB SHIPPING METHOD file (#62.92)
- Second–LAB SHIPPING CONDITION file (#62.93)
- Third–LAB SHIPPING CONTAINER file (#62.91)
- Fourth–LAB SHIPPING CONFIGURATION (#62.9)

> **NOTE:** Online Help is available by entering two question marks (??) at the field prompt.

1.  Configure the LAB SHIPPING METHOD file (#62.92), using the ‘Edit Shipping Method \[LA7S EDIT 62.92\]’ option.  
    It contains the transport method to ship specimens, such as Courier, Taxi, FEDEX, and UPS.

Figure 6. Example of CME-Edit Shipping Method \[LA7S EDIT 62.92\] option

Select Lab Shipping Management Menu Option: <span class="mark">CME \<Enter\></span> Edit Shipping Method

Select SHIPPING METHOD: <span class="mark">FEDEX</span>

Are you adding 'FEDEX’ as a new LAB SHIPPING METHOD (the 3RD)? No// <span class="mark">Y \<Enter\></span> (Yes)

NAME: FEDEX// <span class="mark">\<Enter\></span>

Select Lab Shipping Management Menu Option: <span class="mark">\<Enter\></span>

9.  Configure the LAB SHIPPING CONDITION file (#62.93), using the ‘Edit Shipping Condition \[LA7S EDIT 62.93\]’ option.  
    It contains entries that describe the conditions under which a lab shipment is transported, such as Ambient temperature, Frozen, Refrigerated.

Figure 7. Example of CDE-Edit Shipping condition \[LA7S EDIT 62.93\] option

Select Lab Shipping Management Menu Option: <span class="mark">CDE\<Enter\></span> Edit Shipping Condition

Select SHIPPING CONDITION: ROOM TEMPERATURE\<Enter\>

Are you adding 'ROOM TEMPERATURE' as

a new LAB SHIPPING CONDITIONS (the 4TH)? No// <span class="mark">Y (Yes) \<Enter\></span>

NAME: ROOM TEMPERATURE//<span class="mark">\<Enter\></span>

ABBREVIATION: <span class="mark">RT\<Enter\></span>

Select Lab Shipping Management Menu Option:<span class="mark">\<Enter\></span>

10. Configure the LAB SHIPPING CONTAINER file (#62.91), using the ‘Edit Shipping Container \[LA7S EDIT 62.91\]’ option.  
    It contains the type of containers that the laboratory uses to ship laboratory test specimens. There are three types of containers used for shipping laboratory test specimens.
- Primary–specimen is shipped in the original collection container, such as a Lavender top tube.
- Aliquot–specimen is transferred to a tube/jar before shipment, such as a Plastic Transport Tube and Brown Plastic Tube.
- Packaging–packaging containers used for holding the specimen containers, such as a box.

Figure 8. Example of CTE-Edit Shipping Container \[LA7S EDIT 62.91) option

Select Lab Shipping Management Menu Option: <span class="mark">CTE \<Enter\></span> Edit Shipping Container

Select SHIPPING CONTAINER: <span class="mark">STYROFOAM BOX</span>

Are you adding 'STYROFOAM BOX' as

a new LAB SHIPPING CONTAINER (the 3RD)? No// <span class="mark">Y \<Enter\></span> (Yes)

NAME: STYROFOAM BOX// <span class="mark">\<Enter\></span>

TYPE: <span class="mark">1 \<Enter\></span> PACKAGING

11. Configure the LAB SHIPPING CONFIGURATION file (#62.9), using the ‘Edit Shipping Configuration \[LA7S EDIT 62.9\]’ option.
- This file contains the specimen volume, weight, collection end date/time (collection duration), patient height and weight.
- If an established lab shipping configuration exists for other tests, then the MI and/or AP tests can be added to the Lab Shipping Configuration File (#62.9) if they are being sent to the same Host facility

> **NOTE:** LOINC codes are used to identify patient height and weight, and specimen weight when appropriate.

Figure 9. Example of CFE-Edit Shipping Configuration \[LA7S EDIT 62.9\] option

Select Lab Shipping Management Menu Option: <span class="mark">EDIT SHIPPING CONFIGURATION</span>

Select SHIPPING CONFIGURATION: <span class="mark">MILWAUKEE HOST LAB</span>

     Select one of the following:

          1         Collecting facility

          2         Host facility

Are you editing this entry as the: <span class="mark">1 \<Enter\></span> Collecting facility

NAME: MILWAUKEE HOST LAB// <span class="mark">\<Enter\></span>

COLLECTING FACILITY: REGION 7 ISC,TX (DEMO)// <span class="mark">\<Enter\></span>

COLLECTING FACILITY'S SYSTEM: REGION 5// <span class="mark">\<Enter\></span>

HOST FACILITY: MILWAUKEE VAMC// <span class="mark">\<Enter\></span>

HOST FACILITY'S SYSTEM: MILWAUKEE VAMC// <span class="mark">\<Enter\></span>

STATUS: ACTIVE// <span class="mark">\<Enter\></span>

LAB MESSAGING LINK: LA7V HOST 695// <span class="mark">\<Enter\></span>

SHIPPING METHOD: FEDEX// <span class="mark">\<Enter\></span>

BARCODE MANIFEST: YES-COMPACT// <span class="mark">\<Enter\></span>

MANIFEST RECEIPT: NO// <span class="mark">Y \<Enter\></span> YES

INCLUDE UNCOLLECTED SPECIMENS: NO// <span class="mark">\<Enter\></span>

Select TEST/PROFILE: <span class="mark">TISSUE REQUEST</span>

      Are you adding 'TISSUE REQUEST SURGICAL PATHOLOGY' as

a new TEST/PROFILE? No//<span class="mark">Y \<Enter\></span> (YES)

ACCESSION AREA: <span class="mark">AP OUT</span>

DIVISION: <span class="mark">\<Enter\></span>

Select FEEDER SHIPPING CONFIGURATION: <span class="mark">\<Enter\></span>

  URGENCY: <span class="mark">ROUTINE</span>

  SPECIMEN CONTAINER: <span class="mark">PLASTIC TUBE</span>

  SHIPPING CONDITION: <span class="mark">REFRIGERATED</span>

  PACKAGING CONTAINER: <span class="mark">BOX STYROFOAM</span>

  REQUIRE PATIENT HEIGHT: <span class="mark">\<Enter\></span>

  REQUIRE PATIENT WEIGHT: <span class="mark">\<Enter\></span>

  REQUIRE COLLECTION VOLUME: <span class="mark">\<Enter\></span>

  REQUIRE COLLECTION WEIGHT: <span class="mark">\<Enter\></span>

  REQUIRE COLLECTION END D/T: <span class="mark">\<Enter\></span>

Select TEST/PROFILE:

### Step 5: LIM set up HL7 Environment and the Lab Auto-instrument file to receive results from a Host facility laboratory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the ‘LEDI Setup \[LA7V SETUP\]’ option located on the ‘Lab Shipping Management Menu \[LA7S MGR MENU\]’ option of the ‘Lab liaison menu \[LRLIAISON\]’ option.

Multi-divisional facilities must only use the LEDI Setup option for the primary facility. All other facilities with a multi-divisional facility must use the primary facility to transmit and receive HL7 messages.

Figure 10. Example of LSU LEDI Setup\[LA7V SETUP\] option

Select Lab Shipping Management Menu Option: <span class="mark">LSU LEDI SETUP</span>

-----------------------------------------------------------------------------

LEDI Setup

-----------------------------------------------------------------------------

COLLECTION Labs: Use option \#1 to setup HOST labs.

HOST Labs : Use option \#2 to setup COLLECTION labs.

1\. Add/Edit HOST Lab

2\. Add/Edit COLLECTION Lab

Enter a number (1-2): <span class="mark">1</span>

-----------------------------------------------------------------------------

HOST Lab(s)

-----------------------------------------------------------------------------

1\. TRIPLER ARMY MEDICAL CENTER (LA7V HOST 0052)

2\. WILFORD HALL MEDICAL CENTER (LA7V HOST 0117)

3\. ANCH6A BAY PINES (LA7V HOST 170BP)

4\. ZZ ALBANY (LA7V HOST 500)

5\. NEW MEXICO HCS (LA7V HOST 501)

6\. BROCKTON VAMC (LA7V HOST 525)

7\. HOUSTON VAMC (LA7V HOST 580)

8\. MEMPHIS VAMC (LA7V HOST 614)

9\. Add HOST Lab

Enter a number (1-9): <span class="mark">9</span>

-----------------------------------------------------------------------------

HOST Lab(s)

-----------------------------------------------------------------------------

1\. HOST Lab: <span class="mark">\<Enter\></span>

Enter a number (1-1): <span class="mark">1</span>

Select INSTITUTION NAME: <span class="mark">MILWAUKEE VAMC \<Enter\></span> WI VAMC 695

Setting up the following Host Labs for REGION 7 ISC,TX (DEMO)

Updating HL7 APPLICATION PARAMETER file (#771).

Updating PROTOCOL file (#101).

LA7V Receive Results from 695

LA7V Process Results from 695

LA7V Order to 695

LA7V Send Order to 695

Updating LA7 MESSAGE PARAMETER file (#62.48) for the HOST Lab MILWAUKEE VAMC.

Adding LA7V HOST 695

Updating LAB AUTO INSTRUMENT file (#62.4) for HOST Lab MILWAUKEE VAMC.

Adding LA7V HOST 695

HL7 v1.6 Environment setup is complete!!

Enter RETURN to continue or '^' to exit:

-----------------------------------------------------------------------------

HOST Lab(s)

-----------------------------------------------------------------------------

1\. HOST Lab: MILWAUKEE VAMC (Uneditable)

2\. Logical Link: \<Enter\>

3\. Message Configuration: LA7V HOST 695

4\. Auto Instrument: LA7V HOST 695

Enter a number (1-4): <span class="mark">2</span>

-----------------------------------------------------------------------------

Logical Link for transmissions to/from MILWAUKEE VAMC

-----------------------------------------------------------------------------

Protocol Logical Link

---------- ---------------

LA7V Process Results from 695 VAMIW (TCP)

LA7V Send Order to 695 VAMIW (TCP)

Setup/update Logical Link? <span class="mark">YES</span>

Updating HL LOGICAL LINK file (#870).

Updating the PROTOCOL file (#101).

-----------------------------------------------------------------------------

HOST Lab(s)

-----------------------------------------------------------------------------

1\. HOST Lab: MILWAUKEE VAMC (Uneditable)

2\. Logical Link: VAMIW

3\. Message Configuration: LA7V HOST 695

4\. Auto Instrument: LA7V HOST 695

Enter a number (1-4): <span class="mark">3</span>

GRACE PERIOD FOR MESSAGES: 1// <span class="mark">\<Enter\></span>

LOG ERRORS: ON// <span class="mark">\<Enter\></span>

MULTIPLE ORDERS: MULTIPLE PATIENTS// <span class="mark">\<Enter\></span>

Select ALERT CONDITION: ERROR ON MESSAGE// <span class="mark">\<Enter\></span>

ALERT CONDITION: ERROR ON MESSAGE//<span class="mark">\<Enter\></span>

MAIL GROUP: LAB MESSAGING//<span class="mark">\<Enter\></span>

Select ALERT CONDITION: <span class="mark">NEW \<Enter\></span> (1 NEW RESULTS)

ALERT CONDITION: NEW RESULTS// <span class="mark">\<Enter\></span>

MAIL GROUP: LAB MESSAGING// <span class="mark">\<Enter\></span>

Select ALERT CONDITION: <span class="mark">\<Enter\></span>

-----------------------------------------------------------------------------

HOST Lab(s)

-----------------------------------------------------------------------------

1\. HOST Lab: MILWAUKEE VAMC (Uneditable)

2\. Logical Link: VAMIW

3\. Message Configuration: LA7V HOST 695

4\. Auto Instrument: LA7V HOST 695

Enter a number (1-4): <span class="mark">4</span>

AUTOMATED INSTRUMENT: LA7V HOST 695

LOAD/WORK LIST: SEND OUTS // <span class="mark">\<Enter\></span>

METHOD: VAMC695// <span class="mark">\<Enter\></span>

DEFAULT ACCESSION AREA: AP // <span class="mark">\<Enter\></span>

OVERLAY DATA: YES// <span class="mark">\<Enter\></span>

STORE REMARKS: YES//<span class="mark">\<Enter\></span>

Select SITE NOTES DATE: <span class="mark">\<Enter\></span>

Add Chem Tests to the LA7V HOST 695 Automated Instrument for MILWAUKEE VAMC.

Select CHEM TESTS: <span class="mark">\<Enter\></span>

-----------------------------------------------------------------------------

HOST Lab(s)

-----------------------------------------------------------------------------

1\. HOST Lab: MILWAUKEE VAMC (Uneditable)

2\. Logical Link: VAMIW

3\. Message Configuration: LA7V HOST 695

4\. Auto Instrument: LA7V HOST 695

Enter a number (1-4): <span class="mark">\<Enter\></span>

-----------------------------------------------------------------------------

HOST Lab(s)

-----------------------------------------------------------------------------

1\. TRIPLER ARMY MEDICAL CENTER (LA7V HOST 0052)

2\. WILFORD HALL MEDICAL CENTER (LA7V HOST 0117)

3\. ANCH6A BAY PINES (LA7V HOST 170BP)

4\. ZZ ALBANY (LA7V HOST 500)

5\. NEW MEXICO HCS (LA7V HOST 501)

6\. ZZ BROCKTON VAMC (LA7V HOST 525)

7\. HOUSTON VAMC (LA7V HOST 580)

8\. MEMPHIS VAMC (LA7V HOST 614)

9\. MILWAUKEE VAMC (LA7V HOST 695)

10\. Add HOST Lab

Enter a number (1-10): <span class="mark">\<Enter\></span>

-----------------------------------------------------------------------------

LEDI Setup

-----------------------------------------------------------------------------

COLLECTION Labs: Use option \#1 to setup HOST labs.

HOST Labs : Use option \#2 to setup COLLECTION labs.

1\. Add/Edit HOST Lab

2\. Add/Edit COLLECTION Lab

### Step 6: LIM Map Micro and/or AP Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Map the LEDI Micro and/or AP tests using option ‘Manage MI/AP Test Mappings’ \[LRCAPFF\] located on the ‘National Laboratory File \[LR7O 60-64\]’ menu. The tests need to be mapped to an appropriate NLT code and a Database Code.

> **NOTE:** A report of the mappings can be printed using option ‘Print MI/AP Test Mappings \[LA7VPFL\]‘ located on the ‘Lab Shipping Management Menu \[LA7S MGR MENU\]’.

Figure 11. Example of Manage MI/AP Test Mappings

Select LOINC Main Menu Option: <span class="mark">NATIONAL LABORATORY FILE</span>

1 Semi-automatic Linking of file 60 to 64

2 Manual Linking of file 60 to 64

3 Result NLT Auto Linker

4 Link Result NLT Manual

5 Manage MI/AP Test Mappings

Select National Laboratory File Option: <span class="mark">5 \<Enter\></span> Manage MI/AP Test Mappings

Select one of the following:

MI Microbiology

SP Surgical Pathology

CY Cytopathology

EM Electron Microscopy

Choose Lab Area Subscript: <span class="mark">MI \<Enter\></span> Microbiology

Enter Laboratory Test Name: <span class="mark">ANAEROBIC CULTURE</span>

Editing LABORATORY TEST file (#60)

NATIONAL VA LAB CODE: Micro Anerobic Culture// <span class="mark">\<Enter\></span><span class="mark">60</span> = ANAEROBIC CULTURE \[553\]

64 = Micro Anerobic Culture (87998.0000) \[2070\]

Link the two entries? No// <span class="mark">Y \<Enter\></span> (Yes)

o----LINKED----o

No Database Code on file for this NLT code.

Select an MI Database Code: <span class="mark">?</span>

Answer with LAB ELECTRONIC CODES SEQUENCE, or NAME, or LOINC ABBR, or

HL7 ABBR, or LAB ABBR, or TYPE

Do you want the entire LAB ELECTRONIC CODES List? <span class="mark">Y \<Enter\></span> (Yes)

Choose from:

9193 MI Bacteria Rpt Date GENERAL BACTERIA RPT DATABASE

9194 MI Gram Stain Rpt Date GENERAL GRAM STAIN DATANAME

9197 MI Parasitology Complete Rpt Date GENERAL PARASITOLOGY RPT DATE

DATANAME

9201 MI Mycology Rpt Date GENERAL MYCOLOGY RPT DATE DATANAME

9205 MI TB Rpt Date GENERAL TB RPT DATE DATANAME

9209 MI Virology Rpt Date GENERAL VIROLOGY RPT DATE DATANAME

Select an MI Database Code: <span class="mark">9193 \<Enter\></span> MI Bacteria Rpt Date GENERAL BACTERIA RPT DATABASE

Update complete.

### Step 7: LIM map code concepts to related area of Lab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The standard code system concepts returned with the result need to be mapped to the related area of the Laboratory package database (refer to the LEDI IV User Manual). Standard codes used by a VA Host Lab are already mapped nationally. However, if necessary, additional codes can be mapped locally using option ‘Add/Edit Local Identifier \[LA7V 62.47 LOCAL IDENTIFIER\]’ located on the ‘Lab Code Mapping File \[LA7V 62.47 MENU\]’ menu of the ‘Lab Shipping Management Menu \[LA7S MGR MENU\]’.

Figure 12. Example of Lab Code Mapping File Option

Select Lab Code Mapping File Option: <span class="mark">AEL \<Enter\></span> Add/Edit Local Identifier

Select LAB CODE MAPPING CONCEPT: <span class="mark">SP BRIEF CLINICAL HISTORY \<Enter\></span> SP Brief Clinical History

Select IDENTIFIER: <span class="mark">88541.0000</span>

  Are you adding '88541.0000' as a new IDENTIFIER? No// <span class="mark">Y \<Enter\></span> (Yes)

   IDENTIFIER CODING SYSTEM: <span class="mark">99VA64</span>

IDENTIFIER: 88541.0000// <span class="mark">\<Enter\></span>

CODING SYSTEM: 99VA64// <span class="mark">\<Enter\></span>

PURPOSE: <span class="mark">RESULT \<Enter\></span> RESULT

OVERRIDE CONCEPT: <span class="mark">\<Enter\></span>

RELATED ENTRY: <span class="mark">\<Enter\></span>

MESSAGE CONFIGURATION: <span class="mark">LA7V HOST 968</span>

### Step 8: IRM no further action is required for VA to VA LEDI interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LEDI software uses the standard HL7 TCP listeners and clients (VAxxx links) of the site.

### Step 9: LIM work with the LIM at the Host facility to test the system

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Test the system by performing the following steps.

1.  Order laboratory test(s) on a test patient.
12. Build the test(s) on a shipping manifest.
13. Close and ship the manifest.
14. Provide the LIM of the Host facility with the manifest number.

> **NOTE:** The Host facility LIM must be able to accept the manifest, process orders, and enter test results.

15. Approve the results received from the Host facility.

> **NOTE:** To troubleshoot issues with the order being rejected at the host site, refer to Section 5 Appendix, where it outlines the validation that is done at the host site when parsing the HL7 message and creating the order.

### Step 10: LIM train end users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To assist with training end users, review the *LEDI IV Update User Manual*.

## Host Facility–VA to VA Implementation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IRM and LIM staffs must coordinate the implementation of the LEDI IV software and perform the setup instructions in the following sequence for a successful implementation.

### Step 1: IRM set up the INSTITUTION file (#4)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Load or update the local INSTITUTION file (#4), using the ‘Update/refresh Institution file with IMF data \[XUMF LOAD INSTITUTION\]’, if not previously performed.

Check both the Host and Collecting institutions for the four fields from the INSTITUTION file (#4) used by the LEDI IV software.

- Name (#.01) field: The Institution Master File maintains nationally controlled entries for VA and DoD facilities.
- Agency Code (#95) field: Should be set to VA.  
  This field determines the status of the facility and how to set up the LEDI software application.
- Station Number (#99) field: This field is controlled nationally by the Institution Master File.  
  It is used by LEDI to configure VA facilities and set up Lab Shipping fields in the ‘Lab Shipping Management Menu \[LA7S MGR MENU\]’ option.
- CLIA Identifier field: The CLIA ID \# is in the IDENTIFIER (#9999) multiple field ID(#.02) field. This field is used to enter the CLIA ID \#. The CLIA ID \# is used when printing lab reports.

### Step 2: IRM create LEDI-related mail groups using the ‘Mail Group Edit \[XMEDITMG\]’ option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Local mail group for the ORDERS RECEIVED Alert: This mail group notifies members when the Lab Universal Interface software processes an HL7 message containing test orders.

Example Alert

Lab Messaging - Manifest# 170-20130415-1 received from LA7V COLLECTION 170

- Designate the LIM as the coordinator for the ORDERS RECEIVED Alert mail group.
- This mail group should have at least one active lab user member either currently in the group or added to it.
- This mail group should be comprised of the lab users who receive the orders from the collection facility.

Local mail group for the ERROR ON MESSAGE Alert: This mail group notifies members of error conditions encountered during the processing of a Laboratory HL7 message.

- The LAB MESSAGING mail group can be used for this function. The LAB MESSAGING mail group is a general mail group used by the LAB Universal Interface and LEDI software to address alerts when conditions are detected requiring review and/or corrective action.
- If a mail group already exists for lab HL7 error alerts, then the existing mail group can be used instead of creating a new one.
- The members of this mail group must include the LIM and selected Lab and IRM personnel responsible for maintenance and support of the LAB Universal Interface and LEDI software.
- Designate the LIM as a member of the ERROR ON MESSAGE Alert mail group.

### Step 3: LIM set up the lab test files to receive specimens from the Collecting Facility laboratory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Contact the LIM of the Collecting facility to acquire the following information:
- Accession Area numeric identifier (two-character alphanumeric code)  
  Use an identifier that is not already active in the system.
1.  The Host facility must not use the specific numeric identifier for any local accessioning.
3.  The numeric identifier is used only by the Collecting facility laboratory for which it was assigned.
4.  If the Host facility is relabeling the Collecting facility specimens, the Collecting facility can use any accession area for the specimens/lab tests.
- Specific test information sent to the Host facility laboratory.  
  Use the Host Systems ‘Electronic Catalog Menu \[LAS7 CATALOG MENU\]’ to produce this information. The Collection Facility must configure their files according to what the Host Facility configuration is. Failure to do so will result in messaging errors.
- Specimen collection requirements
- Schedule of testing
- Patient prep instructions
- National VA Lab Code
16. Map the LEDI Micro and/or AP tests using option ‘Manage MI/AP Test Mappings’ \[LRCAPFF\] located on the ‘National Laboratory File \[LR7O 60-64\]’ menu. The tests need to be mapped to an appropriate NLT code and a Database Code.

> **NOTE:** A report of the mappings can be printed using option ‘Print MI/AP Test Mappings \[LA7VPFL\]’ located on the ‘Lab Shipping Management Menu \[LA7S MGR MENU\]’.

The option Map All Susceptibilities \[LA7V 62.47 MAP SUSCS\] should be used to ensure that all susceptibilities in the Antimicrobial Susceptibility file (#62.06) are mapped to LOINC codes.

Both Host and Collection sites should use the Manage MI/AP Test Mappings \[LRCAPFF\] to coordinate the mapping of the related LABORATORY tests (#60) to the interface database code mappings from the WKLD CODE file (#64) and the LAB ELECTRONIC CODES file (#64.061). Each AP or MI test being transmitted in the interface should be mapped to a National VA Lab Code and then subsequently mapped to an appropriate SP, CY, EM or MI database code.

Figure 13. Example of Mapping AP/MICRO Configurations

Select LOINC Main Menu Option: <span class="mark">NATIONAL LABORATORY FILE</span>

1 Semi-automatic Linking of file 60 to 64

2 Manual Linking of file 60 to 64

3 Result NLT Auto Linker

4 Link Result NLT Manual

5 Manage MI/AP Test Mappings

Select National Laboratory File Option: <span class="mark">5 \<Enter\></span> Manage MI/AP Test Mappings

Select one of the following:

MI Microbiology

SP Surgical Pathology

CY Cytopathology

EM Electron Microscopy

Choose Lab Area Subscript: <span class="mark">MI \<Enter\></span> Microbiology

Enter Laboratory Test Name: <span class="mark">ANAEROBIC CULTURE</span>

Editing LABORATORY TEST file (#60)

NATIONAL VA LAB CODE: Micro Anerobic Culture// <span class="mark">\<Enter\></span><span class="mark">60</span> = ANAEROBIC CULTURE \[553\]

64 = Micro Anerobic Culture (87998.0000) \[2070\]

Link the two entries? No// <span class="mark">Y \<Enter\></span> (Yes)

o----LINKED----o

No Database Code on file for this NLT code.

Select an MI Database Code: <span class="mark">?</span>

Answer with LAB ELECTRONIC CODES SEQUENCE, or NAME, or LOINC ABBR, or

HL7 ABBR, or LAB ABBR, or TYPE

Do you want the entire LAB ELECTRONIC CODES List? <span class="mark">Y \<Enter\></span> (Yes)

Choose from:

9193 MI Bacteria Rpt Date GENERAL BACTERIA RPT DATABASE

9194 MI Gram Stain Rpt Date GENERAL GRAM STAIN DATANAME

9197 MI Parasitology Complete Rpt Date GENERAL PARASITOLOGY RPT DATE

DATANAME

9201 MI Mycology Rpt Date GENERAL MYCOLOGY RPT DATE DATANAME

9205 MI TB Rpt Date GENERAL TB RPT DATE DATANAME

9209 MI Virology Rpt Date GENERAL VIROLOGY RPT DATE DATANAME

Select an MI Database Code: <span class="mark">9193 \<Enter\></span> MI Bacteria Rpt Date GENERAL BACTERIA RPT DATABASE

Update complete

### Step 4: LIM must set up the Host facility LAB SHIPPING CONFIGURATION file (#62.9)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** A Host facility that is also a Collecting facility must follow the setup instructions for a Collecting facility, because it pertains to the specimens that are shipped to a Host facility.

Configure the LAB SHIPPING CONFIGURATION file (#62.9) for a VA facility, using the ‘Edit Shipping Configuration \[LA7S EDIT 62.9\]’ option under the ‘Lab Shipping Management \[LA7S MGR MENU\]’ menu.

- This file defines the two members (institutions) that have a relationship.
- This file groups the Collecting and Host facilities and describes particulars of the relationship, such as what specimen ID is used, what types of tests/specimens are shipped, who is the Collecting/Host facility, are the facilities linked electronically, and are they on the same computer system.
- If there is an established lab shipping configuration for other tests, then the MI and/or AP tests can be added to the Lab Shipping Configuration File (#62.9) provided they will be received from the same Collecting facility

> **NOTE:** Refer to Section 5 Appendix for further information on configuring the tests on the shipping configuration

Figure 14. Example of Edit Shipping Configuration

Select Lab Shipping Management Menu Option: <span class="mark">EDIT SHIPPING CONFIGURATION</span>

Select SHIPPING CONFIGURATION: <span class="mark">MILWAUKEE REMOTE</span>

Select one of the following:

1 Collecting facility

2 Host facility

Are you editing this entry as the: <span class="mark">2 \<Enter\></span> Host facility

Select one of the following:

0 Do NOT copy

1 Another Shipping Configuration

2 Test Catalog - LABORATORY TEST File \#60

Copy a test profile from: Do NOT copy// <span class="mark">\<Enter\></span>

NAME: MILWAUKEE REMOTE// <span class="mark">\<Enter\></span>

COLLECTING FACILITY: MILWAUKEE VAMC// <span class="mark">\<Enter\></span>

COLLECTING FACILITY'S SYSTEM: MILWAUKEE VAMC// <span class="mark">\<Enter\></span>

HOST FACILITY: REGION 7 ISC,TX (DEMO)// <span class="mark">\<Enter\></span>

HOST FACILITY'S SYSTEM: REGION 7 ISC,TX (DEMO)// <span class="mark">\<Enter\></span>

STATUS: ACTIVE// <span class="mark">\<Enter\></span>

COLLECTING FACILITY'S SPEC ID: HOST FACILITY// <span class="mark">\<Enter\></span>

Select TEST/PROFILE: <span class="mark">TISSUE EXAM</span>

TEST/PROFILE: TISSUE EXAM // <span class="mark">\<Enter\></span>

URGENCY: <span class="mark">ROUTINE</span>

HOST COLLECTION SAMPLE: TISSUE // <span class="mark">\<Enter\></span>

> **NOTE:** The collection sample TISSUE \[IEN 37\] does NOT have a default specimen.

Therefore at the SPECIMEN field prompt specify the specimen type to use to

build pending orders from incoming order messages.

SPECIMEN:

Select TEST/PROFILE: <span class="mark">\<Enter\></span>

### Step 5: LIM set up a Collecting and/or Host facility HL7 Environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the ‘LEDI Setup \[LA7V SETUP\]’ option located on the ‘Lab Shipping Management Menu \[LA7S MGR MENU\]’ option of the ‘Lab liaison menu \[LRLIAISON\]’ option.

If the Collecting facility is a division of a multi-divisional facility, set up the system of the primary facility as the Collecting facility.

Figure 15. Example of LEDI Setup \[LA7V SETUP\] option

Select Lab Shipping Management Menu Option: <span class="mark">LEDI SETUP</span>

-----------------------------------------------------------------------------

LEDI Setup

-----------------------------------------------------------------------------

COLLECTION Labs: Use option \#1 to setup HOST labs.

HOST Labs : Use option \#2 to setup COLLECTION labs.

1\. Add/Edit HOST Lab

2\. Add/Edit COLLECTION Lab

Enter a number (1-2): <span class="mark">2</span>

-----------------------------------------------------------------------------

COLLECTION Lab(s)

----------------------------------------------------------------------------

1\. MILWAUKEE VAMC (LA7V COLLECTION 695)

2\. Add COLLECTION Lab

Enter a number (1-2): <span class="mark">2</span>

-----------------------------------------------------------------------------

COLLECTION Lab Setup

-----------------------------------------------------------------------------

1\. COLLECTION Lab: MILWAUKEE VAMC (Uneditable)

2\. Logical Link (TCP/IP): VAMIW

3\. Message Configuration: LA7V COLLECTION 695

Enter a number (1-3): <span class="mark">1</span>

Are you sure you want to update the MILWAUKEE VAMC interface? <span class="mark">YES</span>

Setting up the REMOTE Lab, MILWAUKEE VAMC and HOST Lab REGION 7 ISC,TX (DEMO)

Updating HL7 APPLICATION PARAMETER file (#771).

Updating PROTOCOL file (#101).

LA7V Results Reporting to 695

LA7V Send Results to 695

LA7V Receive Order from 695

LA7V Process Order from 695

Updating LA7 MESSAGE PARAMETER file (#62.48) for the REMOTE Lab MILWAUKEE VAMC.

Adding LA7V COLLECTION 695

HL7 v1.6 Environment setup is complete!!

-----------------------------------------------------------------------------

COLLECTION Lab Setup

-----------------------------------------------------------------------------

1\. COLLECTION Lab: MILWAUKEE VAMC (Uneditable)

2\. Logical Link (TCP/IP): LA7V 695

3\. Message Configuration: LA7V COLLECTION 695

Enter a number (1-3): <span class="mark">2</span>

-----------------------------------------------------------------------------

Logical Link for transmissions to/from MILWAUKEE VAMC

----------------------------------------------------------------------------

Protocol Logical Link

---------- ---------------

LA7V Process Order from 695 VAMIW (TCP)

LA7V Send Results to 695 VAMIW (TCP)

Setup/update Logical Link? <span class="mark">YES</span>

Updating HL LOGICAL LINK file (#870).

Updating the PROTOCOL file (#101).

-----------------------------------------------------------------------------

COLLECTION Lab Setup

-----------------------------------------------------------------------------

1\. COLLECTION Lab: MILWAUKEE VAMC (Uneditable)

2\. Logical Link (TCP/IP): VAMIW

3\. Message Configuration: LA7V COLLECTION 695

Enter a number (1-3): 3 \<Enter\>

GRACE PERIOD FOR MESSAGES: 30<span class="mark">//</span><span class="mark">\<Enter\></span>

LOG ERRORS: ON// <span class="mark">\<Enter\></span>

MULTIPLE ORDERS: <span class="mark">0 \<Enter\></span> MULTIPLE PATIENTS

Select ALERT CONDITION: ERROR ON MESSAGE// <span class="mark">\<Enter\></span>

ALERT CONDITION: ERROR ON MESSAGE// <span class="mark">\<Enter\></span>

MAIL GROUP: LAB MESSAGING// <span class="mark">\<Enter\></span>

Select ALERT CONDITION: <span class="mark">OR \<Enter\></span> (3 ORDERS RECEIVED)

ALERT CONDITION: ORDERS RECEIVED// <span class="mark">\<Enter\></span>

MAIL GROUP: LAB MESSAGING// <span class="mark">\<Enter\></span>

Select ALERT CONDITION: <span class="mark">\<Enter\></span>

-----------------------------------------------------------------------------

COLLECTION Lab Setup

-----------------------------------------------------------------------------

1\. COLLECTION Lab: MILWAUKEE VAMC (Uneditable)

2\. Logical Link (TCP/IP): VAMIW\<Enter\>

3\. Message Configuration: LA7V COLLECTION 695

Enter a number (1-3): <span class="mark">\<Enter\></span>

-----------------------------------------------------------------------------

COLLECTION Lab(s)

-----------------------------------------------------------------------------

1\. MILWAUKEE VAMC (LA7V COLLECTION 695)

2\. Add COLLECTION Lab

Enter a number (1-2): <span class="mark">\<Enter\></span>

-----------------------------------------------------------------------------

LEDI Setup

-----------------------------------------------------------------------------

COLLECTION Labs: Use option \#1 to setup HOST labs.

HOST Labs : Use option \#2 to setup COLLECTION labs.

1\. Add/Edit HOST Lab

2\. Add/Edit COLLECTION Lab

Enter a number (1-2): <span class="mark">^\<Enter\></span>

--------------------------------------------------------------------------

### Step 6: IRM no further action is required for VA to VA LEDI interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LEDI software uses the standard HL7 TCP listeners and clients (VAxxx links) of the site.

### Step 7: LIM work with the LIM at the Collecting Facility to test the system

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To test the system perform the following steps.

1.  Have the Collecting Facility order laboratory test(s) on a test patient.
17. Have the Collecting Facility build the test(s) on a shipping manifest.
18. Have the Collecting Facility close and ship the manifest.
19. Provide the LIM of the Host facility with the manifest number.
20. Have the Collecting Facility verify that the test results entered at the Host Facility are properly received.

Note 1: The Host facility LIM must be able to accept the manifest, process orders, and enter test results.

Note 2: To assist with training end users, review the *LEDI IV Update User Manual*.

Note 3: To troubleshoot issues with the order being rejected at the host site, refer to Section 5 Appendix, where it outlines the validation that is done at the host site when parsing the HL7 message and creating the order.

## Collecting Facility–VA to DoD Laboratory Implementation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IRM and LIM staffs must coordinate the implementation of the LEDI IV software and perform the setup instructions in the following sequence for a successful implementation.

> **NOTE:** When implementing this interface with a DoD facility, consult the LDSI National Implementation Plan for guidance to establish communication with the DoD facility via the VA/DoD VPN.

### Step 1: IRM set up the INSTITUTION file (#4)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Load the DoD DMIS ID codes into the INSTITUTION file (#4), using the ‘Load DMIS ID \[XUMF DMIS ID LOAD\]’ option installed by the Kernel Patch XU\*8.0\*261, if not previously performed.

Check both the Host and Collecting institutions for the four fields from the INSTITUTION file (#4) used by the LEDI IV software.

- Name (#.01) field: The Institution Master File maintains nationally controlled entries for VA and DoD facilities.
- Agency Code (#95) field: This field indicates to the LEDI IV software whether the facility is a VA or DoD facility.
1.  VA facilities should be set to: VA
2.  DoD facilities should be set to:
- AF–AIR FORCE
- ARMY–ARMY
- N–NAVY
- Station Number (#99) field: For VA facilities
- Identifier (#9999) field: For DoD facilities to identify the DMIS ID for a facility

### Step 2: IRM create LEDI-related mail groups using the ‘Mail Group Edit \[XMEDITMG\]’ option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Local mail group for the NEW RESULTS Alert: This mail group notifies members when the Lab LEDI software processes an HL7 message containing test results.

Example Alert

Lab Messaging–New results received for LA7V HOST 578

- Designate the LIM as the coordinator for the NEW RESULTS Alert mail group.
- At least one active lab user must be currently part of or added to this mail group as a recipient.
- This mail group should be comprised of the lab users that process the results that return from the Host site.

Local mail group for the ERROR ON MESSAGE Alert: This mail group notifies members of error conditions encountered during the processing of a Laboratory HL7 message.

- The LAB MESSAGING mail group can be used for this function. The LAB MESSAGING mail group is a general mail group used by the LAB Universal Interface and LEDI software to address alerts when conditions are detected requiring review and/or corrective action.
- If a mail group already exists for lab HL7 error alerts, then the existing mail group can be used, instead of creating a new one.
- The members of this mail group must include the LIM and selected Lab and IRM personnel responsible for maintenance and support of the LAB Universal Interface and LEDI software.
- Designate the LIM as a member of the ERROR ON MESSAGE Alert mail group.

### Step 3: LIM set up the lab test files to send specimens to the Host facility laboratory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Contact the Reference laboratory to acquire the following information:
- Specimen collection requirements
- Specimen handling/minimum requirements
- Alternate specimen (if any)
- Stability (for shipping conditions)
- Patient prep instructions
- Schedule of testing and TAT
- Order code to order the tests
- Exact test name for non-VA test name
- DoD specimen code and name for each test, including assigned SNOMED CT ID
- DoD collection sample code and name for each test, including assigned SNOMED CT ID
- List of tests for panel tests
- Result code(s) used to report the results
- Microbiology result test codes (LOINC/Local), such as culture result, acid fast stain result, and antibiotic susceptibility
- Normal Range and Critical Values
- Units of measure
- DoD Organism ID codes (local) if non-SNOMED CT
- List of antibiotics and corresponding LOINC and/or local codes used by DoD to report antimicrobial susceptibilities
21. Edit the LABORATORY TEST file (#60) to send specimens to the Host facility laboratory.  
    New lab tests can be created to match the Host facility laboratory requirements, or existing lab tests can be utilized, if the entries are compatible with the Host facility laboratory requirements.
- If DoD requires a SNOMED CT code for specimen source (topography) and/or collection sample for ordering purposes, which does not conform to VA Data Standardization, use the ‘Map Non-VA SNOMED CT codes \[LA7S MAP NON-VA SNOMED CODES\]’ option to map VA terms to the requested DoD SNOMED CT code.
- If DoD requires local, non-VA codes (i.e., that are not from the NLT, SNOMED CT, or HL7 0070 code sets) for the test, specimen source (topography), and/or collection sample for ordering purposes, the non-VA codes can be mapped when setting up the shipping configuration (refer to 3.5.4 Step 4: LIM set up the Lab Shipping Files).
22. Map the LEDI Micro and/or AP tests using option ‘Manage MI/AP Test Mappings’ \[LRCAPFF\] located on the ‘National Laboratory File \[LR7O 60-64\]’ menu. The tests need to be mapped to an appropriate NLT code and an entry in the Lab Electronic Codes File \#64.061.

> **NOTE:** A report of the mappings can be printed using option ‘Print MI/AP Test Mappings \[LA7VPFL\]’ located on the ‘Lab Shipping Management Menu \[LA7S MGR MENU\]’).

Figure 16. Example of Manage MI/AP Test Mappings

Select LOINC Main Menu Option: <span class="mark">NATIONAL LABORATORY FILE</span>

1 Semi-automatic Linking of file 60 to 64

2 Manual Linking of file 60 to 64

3 Result NLT Auto Linker

4 Link Result NLT Manual

5 Manage MI/AP Test Mappings

Select National Laboratory File Option: <span class="mark">5 \<Enter\></span> Manage MI/AP Test Mappings

Select one of the following:

MI Microbiology

SP Surgical Pathology

CY Cytopathology

EM Electron Microscopy

Choose Lab Area Subscript: <span class="mark">MI \<Enter\></span> Microbiology

Enter Laboratory Test Name: <span class="mark">ANAEROBIC CULTURE</span>

Editing LABORATORY TEST file (#60)

NATIONAL VA LAB CODE: Micro Anerobic Culture// <span class="mark">\<Enter\></span>

60 = ANAEROBIC CULTURE \[553\]

64 = Micro Anerobic Culture (87998.0000) \[2070\]

Link the two entries? No// <span class="mark">Y \<Enter\></span> (Yes)

o----LINKED----o

No Database Code on file for this NLT code.

Select an MI Database Code: <span class="mark">?</span>

Answer with LAB ELECTRONIC CODES SEQUENCE, or NAME, or LOINC ABBR, or

HL7 ABBR, or LAB ABBR, or TYPE

Do you want the entire LAB ELECTRONIC CODES List? <span class="mark">Y \<Enter\></span> (Yes)

Choose from:

9193 MI Bacteria Rpt Date GENERAL BACTERIA RPT DATABASE

9194 MI Gram Stain Rpt Date GENERAL GRAM STAIN DATANAME

9197 MI Parasitology Complete Rpt Date GENERAL PARASITOLOGY RPT DATE

DATANAME

9201 MI Mycology Rpt Date GENERAL MYCOLOGY RPT DATE DATANAME

9205 MI TB Rpt Date GENERAL TB RPT DATE DATANAME

9209 MI Virology Rpt Date GENERAL VIROLOGY RPT DATE DATANAME

Select an MI Database Code: <span class="mark">9193 \<Enter\></span> MI Bacteria Rpt Date GENERAL BACTERIA RPT DATABASE

Update complete.

- If you do not already have an established LEDI Host Load/Work List for this configuration, then you should create a new test LOAD/WORK LIST file (#68.2) entry to define and accept lab results transmitted by the Host facility laboratory.
- If you already have a LEDI Host Load/Work List for this configuration, then the existing Load/Work List entry should be used.
23. Add a profile to the Load/Work list used to process results for each subscript processed. The profiles must contain all resultable lab tests processed by the Host facility laboratory. Configuration of the Default Reference Laboratory field is not required, but it will facilitate the entry of results.

> **NOTE:** There must be separate profiles specified for CH, MI, SP, CY, and EM subscripts.

24. Use the ‘Edit the default parameters Load/Work list \[LRLLE DFT\]’ option to configure the following four fields:
- Accession Area
- UID Verification
- Store Duplicate Comments
- Default Reference Laboratory
25. Add DoD antibiotics not currently configured in VistA, using one of the following options:
- If the antibiotic is not defined in LAB DATA file (#63), use the ‘Add a new internal name for an antibiotic \[LRWU7\]’ option to create an internal name for the antibiotic.
- If the antibiotic is not currently in the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06), use the ‘Edit an Antibiotic \[LRWU7 EDIT\]’ option to add the antibiotic.  
  Include mapping to the National VA Lab Code and the related LOINC code if already defined and configure appropriate susceptibility interpretations.
26. Map DoD CHCS LOINC and local codes used to report susceptibility testing by using the ‘Edit Susceptibility \[LA7V 62.47 EDIT SUSC\]’ option.

### Step 4: LIM set up the Lab Shipping Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access for configuring the lab shipping files is via the ‘Lab Shipping Management Menu \[LA7S MGR MENU\]’ option under the ‘Lab liaison menu \[LRLIAISON\]’ option.

Configure the following four files in the order listed.

- First–LAB SHIPPING METHOD file (#62.92)
- Second–LAB SHIPPING CONDITION file (#62.93)
- Third–LAB SHIPPING CONTAINER file (#62.91)
- Fourth–LAB SHIPPING CONFIGURATION (#62.9)

> **NOTE:** The first three files may already be set up if a VA-to-VA interface exists for the facility. Online Help is available by entering two question marks (??) at the field prompt.

Figure 17. Example of CME—Edit Shipping Method \[LA7S EDIT 62.92\] option

Select Lab liaison menu Option: <span class="mark">SMGR \<Enter\></span> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: <span class="mark">?</span>

CFE Edit Shipping Configuration

CTE Edit Shipping Container

CME Edit Shipping Method

CDE Edit Shipping Condition

LSU LEDI Setup

LSCT Load SNOMED SCT Mapping

MSCT Map Non-VA SNOMED CT codes

CAT Electronic Catalog Menu ...

LCM Lab Code Mapping File ...

PTM Print MI/AP Test Mappings

CU Code Usage

DSC Display a Shipping Configuration

DSO Display SCT Overrides

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Lab Shipping Management Menu Option: <span class="mark">CME \<Enter\></span> Edit Shipping Method

Select SHIPPING METHOD: <span class="mark">?</span>

Answer with LAB SHIPPING METHOD NAME

You may enter a new LAB SHIPPING METHOD, if you wish

NAME MUST BE 3-30 CHARACTERS, NOT NUMERIC OR STARTING WITH

PUNCTUATION

Select SHIPPING METHOD: <span class="mark">FEDEX</span>

Are you adding 'FEDEX' as a new LAB SHIPPING METHOD (the 1ST)? <span class="mark">Y \<Enter\></span> (Yes)

NAME: FEDEX//<span class="mark">\<Enter\></span>

Select Lab Shipping Management Menu Option: CME \<Enter\> Edit Shipping Method

Select SHIPPING METHOD: <span class="mark">COURIER</span>

Are you adding 'COURIER' as a new LAB SHIPPING METHOD (the 2ND)? <span class="mark">Y \<Enter\></span> (Yes)

NAME: COURIER// <span class="mark">^\<Enter\></span>

1.  Configure the LAB SHIPPING METHOD file (#62.92), using the ‘Edit Shipping Method \[LA7S EDIT 62.92\]’ option.  
    It contains the transport method to ship specimens, such as Courier, Taxi, FEDEX, and UPS.
27. Configure the LAB SHIPPING CONDITION file (#62.93), using the ‘Edit Shipping Condition \[LA7S EDIT 62.93\]’ option.  
    It contains entries that describe the conditions under which a lab shipment is transported, such as Ambient temperature, Frozen, Refrigerated.

Figure 18. Example of CDE—Edit Shipping Condition \[LA7S EDIT 62.93\] option

Select Lab liaison menu Option: <span class="mark">SMGR \<Enter\></span> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: <span class="mark">??</span>

CFE Edit Shipping Configuration

CTE Edit Shipping Container

CME Edit Shipping Method

CDE Edit Shipping Condition

LSU LEDI Setup

LSCT Load SNOMED SCT Mapping

MSCT Map Non-VA SNOMED CT codes

CAT Electronic Catalog Menu ...

LCM Lab Code Mapping File ...

PTM Print MI/AP Test Mappings

CU Code Usage

DSC Display a Shipping Configuration

DSO Display SCT Overrides

Select Lab Shipping Management Menu Option: <span class="mark">CDE \<Enter\></span> Edit Shipping Condition

Use this option to setup the Lab Shipping Condition file.

Select SHIPPING CONDITION: <span class="mark">? \<Enter\></span>

Answer with LAB SHIPPING CONDITIONS NAME

You may enter a new LAB SHIPPING CONDITIONS, if you wish

NAME MUST BE 3-30 CHARACTERS, NOT NUMERIC OR STARTING WITH

PUNCTUATION

Select SHIPPING CONDITION: Room Temperature <span class="mark">\<Enter\></span>

Are you adding 'Room Temperature' as

a new LAB SHIPPING CONDITIONS (the 1ST)? No// <span class="mark">Y \<Enter\></span> (Yes)

NAME: Room Temperature// <span class="mark">\<Enter\></span>

ABBREVIATION: <span class="mark">RT \<Enter\></span>

28. Configure the LAB SHIPPING CONTAINER file (#62.91), using the ‘Edit Shipping Container \[LA7S EDIT 62.91\]’ option.  
    It contains the type of containers that the laboratory uses to ship laboratory test specimens.  
    There are three types of containers used for shipping laboratory test specimens.
- Primary–specimen is shipped in the original collection container, such as a Lavender top tube.
- Aliquot–specimen is transferred to a tube/jar before shipment, such as a Plastic Transport Tube and Brown Plastic Tube.
- Packaging-packaging containers used for used for holding the specimen containers, such as a box.

Figure 19. Example of CTE—Edit Shipping Container \[LA7S EDIT 62.91\] option

Select Lab liaison menu Option: <span class="mark">SMGR \<Enter\></span> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: <span class="mark">?</span>

CFE Edit Shipping Configuration

<span class="mark">CTE Edit Shipping Container</span>

CME Edit Shipping Method

CDE Edit Shipping Condition

LSU LEDI Setup

LSCT Load SNOMED SCT Mapping

MSCT Map Non-VA SNOMED CT codes

CAT Electronic Catalog Menu ...

LCM Lab Code Mapping File ...

PTM Print MI/AP Test Mappings

CU Code Usage

DSC Display a Shipping Configuration

DSO Display SCT Overrides

Select Lab Shipping Management Menu Option: <span class="mark">CTE \<Enter\></span> Edit Shipping Container

Use this option to setup the Lab Shipping Container file.

Select SHIPPING CONTAINER: <span class="mark">?</span>

Answer with LAB SHIPPING CONTAINER NAME

You may enter a new LAB SHIPPING CONTAINER, if you wish

NAME MUST BE 3-30 CHARACTERS, NOT NUMERIC OR STARTING WITH

PUNCTUATION

Select SHIPPING CONTAINER: Plastic Tube <span class="mark">\<Enter\></span>

Are you adding 'Plastic Tube' as

a new LAB SHIPPING CONTAINER (the 1ST)? No// <span class="mark">Y \<Enter\></span> (Yes)

NAME: Plastic Tube// <span class="mark">\<Enter\></span>

TYPE: <span class="mark">?</span>

Enter what this container is used for.

Choose from:

1 PACKAGING

2 PRIMARY

3 ALIQUOT

TYPE: <span class="mark">3 \<Enter\></span> ALIQUOT

29. Configure the LAB SHIPPING CONFIGURATION file (#62.9), using the ‘Edit Shipping Configuration \[LA7S EDIT 62.9\]’ option.  
    It contains the specimen volume, weight, collection end date/time (collection duration), patient height and weight.

> **NOTE:** LOINC codes are used to identify patient height and weight, and specimen weight when appropriate.

Figure 20. Example of CFE—Edit Shipping Configuration \[LA7S EDIT 62.9\] option

Select Lab Shipping Management Menu Option: <span class="mark">CFE \<Enter\></span> Edit Shipping Configuration

Select SHIPPING CONFIGURATION: <span class="mark">TRIPLER AMC</span>

Are you adding 'TRIPLER AMC' as

a new LAB SHIPPING CONFIGURATION (the 14TH)? No// <span class="mark">Y \<Enter\></span> (Yes)

LAB SHIPPING CONFIGURATION COLLECTING FACILITY: HONOLULU

LAB SHIPPING CONFIGURATION HOST FACILITY: TRIPLER ARMY MEDICAL CENTER

Select one of the following:

1 Collecting facility

2 Host facility

Are you editing this entry as the: <span class="mark">1 \<Enter\></span> Collecting facility

NAME: TRIPLER AMC// <span class="mark">\<Enter\></span>

COLLECTING FACILITY: HONOLULU//<span class="mark">\<Enter\></span>

COLLECTING FACILITY'S SYSTEM: <span class="mark">HONOLULU</span>

HOST FACILITY: TRIPLER ARMY MEDICAL CENTER// <span class="mark">\<Enter\></span>

HOST FACILITY'S SYSTEM: <span class="mark">TRIPLER ARMY MEDICAL CENTER</span>

STATUS: <span class="mark">A \<Enter\></span> ACTIVE

LAB MESSAGING LINK: <span class="mark">\<Enter\></span>

SHIPPING METHOD: <span class="mark">COURIER</span>

BARCODE MANIFEST: <span class="mark">N \<Enter\></span> NO

MANIFEST RECEIPT: <span class="mark">Y \<Enter\></span> YES

INCLUDE UNCOLLECTED SPECIMENS: <span class="mark">N \<Enter\></span> NO

Select TEST/PROFILE: <span class="mark">AP-DOD</span>

Are you adding AP '-DOD' as a new TEST/PROFILE (the 1ST for this LAB SHIPPING CONFIGURATION)? No// <span class="mark">Y \<Enter\></span> (Yes)

ACCESSION AREA: <span class="mark">SURGICAL PATHOLOGY</span>

DIVISION: <span class="mark">\<Enter\></span>

Select FEEDER SHIPPING CONFIGURATION: <span class="mark">\<Enter\></span>

SPECIMEN: <span class="mark">TISSUE</span>

URGENCY: <span class="mark">\<Enter\></span>

SPECIMEN CONTAINER: <span class="mark">PLASTIC TUBE</span>

SHIPPING CONDITION: <span class="mark">REFRIGERATE</span>

PACKAGING CONTAINER: <span class="mark">STYROFOAM BOX</span>

NON-NLT TEST ORDER CODE: <span class="mark">1234</span>

NON-NLT TEST ORDER NAME: <span class="mark">TISSUE EXAM</span>

NON-NLT SPECIMEN CODE: <span class="mark">72</span>

NON-NLT SPECIMEN NAME: <span class="mark">TISSUE</span>

COLLECTION SAMPLE CODE: <span class="mark">99</span>

COLLECTION SAMPLE NAME: <span class="mark">TISSUE</span>

REQUIRE PATIENT HEIGHT: <span class="mark">N \<Enter\></span> NO

REQUIRE PATIENT WEIGHT: <span class="mark">N \<Enter\></span> NO

REQUIRE COLLECTION VOLUME: <span class="mark">N \<Enter\></span> NO

REQUIRE COLLECTION WEIGHT: <span class="mark">N \<Enter\></span> NO

REQUIRE COLLECTION END D/T: <span class="mark">N \<Enter\></span> NO

### Step 5: LIM set up the HL7 Environment and Auto Instrument file to receive results from a Host facility laboratory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Use the ‘LEDI Setup \[LA7V SETUP\]’ option located on the ‘Lab Shipping Management Menu \[LA7S MGR MENU\]’ option of the ‘Lab liaison menu \[LRLIAISON\]’ option.
- TCP/IP must be used as the HL7 transport protocol for VA to DoD Lab interfaces.
- When defining institution names, do not use the Host or Collecting facility name of either of the two institutions from the example.

Example Screen

> (The two institution names in the following screen capture are used only as examples.)

Figure 21. Example of LEDI Setup \[LA7V SETUP\] option

Select OPTION NAME: <span class="mark">LEDI SETUP LA7V</span>

---------------------------------------------------------------------------

LEDI Setup

----------------------------------------------------------------------------

COLLECTION Labs: Use option \#1 to setup HOST labs.

HOST Labs Use option \#2 to setup COLLECTION labs.

1\. Add/Edit HOST Lab

2\. Add/Edit COLLECTION Lab

Enter a number (1-2): <span class="mark">1</span>

---------------------------------------------------------------------------

HOST Lab(s)

----------------------------------------------------------------------------

1\. Add HOST Lab

Enter a number (1-1): <span class="mark">1</span>

---------------------------------------------------------------------------

HOST Lab(s)

---------------------------------------------------------------------------

1\. HOST Lab: <span class="mark">\<Enter\></span>

Enter a number (1-1): <span class="mark">1</span>

Select INSTITUTION NAME: <span class="mark">TRIPLER ARMY MEDICAL CENTER \<Enter\></span> HI USAH 459CN

Setting up the following Host Labs for REGION 7 ISC,TX (DEMO)

Updating HL7 APPLICATION PARAMETER file (#771).

Updating PROTOCOL file (#101).

LA7V Receive Results from 0052

LA7V Process Results from 0052

LA7V Order to 0052

LA7V Send Order to 0052

Updating LA7 MESSAGE PARAMETER file (#62.48) for the HOST Lab TRIPLER ARMY MEDICAL CENTER.

Adding LA7V HOST 0052

Updating LAB AUTO INSTRUMENT file (#62.4) for HOST Lab TRIPLER ARMY MEDICAL CENTER.

Adding LA7V HOST 0052

HL7 v1.6 Environment setup is complete!!

Enter RETURN to continue or '^' to exit: <span class="mark">\<Enter\></span>

---------------------------------------------------------------------------

HOST Lab(s)

----------------------------------------------------------------------------

1\. HOST Lab: TRIPLER ARMY MEDICAL CENTER (Uneditable)

2\. Logical Link: LA7V0052

3\. Message Configuration: LA7V HOST 0052

4\. Auto Instrument: LA7V HOST 0052

Enter a number (1-4): <span class="mark">2</span>

---------------------------------------------------------------------------

Logical Link for transmissions to/from TRIPLER ARMY MEDICAL CENTER

---------------------------------------------------------------------------

Protocol Logical Link

---------- ---------------

LA7V Process Results from 0052

LA7V Send Order to 0052

Enter a Logical Link: (MM/TCP): <span class="mark">TCP/IP</span>

Updating HL LOGICAL LINK file (#870).

Updating the PROTOCOL file (#101).

---------------------------------------------------------------------------

HOST Lab(s)

---------------------------------------------------------------------------

1\. HOST Lab: TRIPLER ARMY MEDICAL CENTER (Uneditable)\<Enter\>

2\. Logical Link: LA7V0052\<Enter\>

3\. Message Configuration: LA7V HOST 0052\<Enter\>

4\. Auto Instrument: LA7V HOST 0052\<Enter\>

Enter a number (1-4): <span class="mark">3</span>

GRACE PERIOD FOR MESSAGES: <span class="mark">5</span>

LOG ERRORS: ON// <span class="mark">\<Enter\></span>

MULTIPLE ORDERS: <span class="mark">?</span>

Select if multiple/single patients/orders should be sent in a single message. See description (??) for additional help.

Choose from:

0 MULTIPLE PATIENTS

1 SINGLE PATIENT

2 SINGLE ORDER

MULTIPLE ORDERS: <span class="mark">2 \<Enter\></span> SINGLE ORDER

Select ALERT CONDITION: <span class="mark">ERROR \<Enter\></span> (2 ERROR ON MESSAGE)

Are you adding 'ERROR ON MESSAGE' as a new ALERT CONDITION (the 1ST for this LA7 MESSAGE PARAMETER)? No// <span class="mark">Y \<Enter\></span> (Yes)

MAIL GROUP: <span class="mark">LAB MESSAGING</span>

Select ALERT CONDITION: <span class="mark">?</span>

Answer with ALERT CONDITION: <span class="mark">\<Enter\></span>

ERROR ON MESSAGE

You may enter a new ALERT CONDITION, if you wish

Enter "1" to receive alerts for new results, a "2" to receive alerts

for errors during processing, and "3" when orders are received.

Error on message alert may only be selected if Field \#4, LOG

ERRORS, is set to "ON".

Choose from:

1 NEW RESULTS

2 ERROR ON MESSAGE

3 ORDERS RECEIVED

Select ALERT CONDITION: <span class="mark">1 \<Enter\></span> (1 NEW RESULTS)

Are you adding 'NEW RESULTS' as a new ALERT CONDITION (the 2ND for this LA7 MESSAGE PARAMETER)? No// <span class="mark">Y \<Enter\></span> (Yes)

MAIL GROUP: <span class="mark">LAB MESSAGING</span>

Select ALERT CONDITION: <span class="mark">\<Enter\></span>

--------------------------------------------------------------------------

HOST Lab(s)

---------------------------------------------------------------------------

1\. HOST Lab: TRIPLER ARMY MEDICAL CENTER (Uneditable)

2\. Logical Link: LA7V0052

3\. Message Configuration: LA7V HOST 0052

4\. Auto Instrument: LA7V HOST 0052

Enter a number (1-4): <span class="mark">4</span>

AUTOMATED INSTRUMENT: LA7V HOST 0052

LOAD/WORK LIST: DOD

METHOD: DOD

DEFAULT ACCESSION AREA: SURGICAL PATHOLOGY

OVERLAY DATA: <span class="mark">Y \<Enter\></span> YES

STORE REMARKS: YES// <span class="mark">\<Enter\></span>

Select SITE NOTES DATE: <span class="mark">\<Enter\></span>

Add Chem Tests to the LA7V HOST 0052 Automated Instrument for TRIPLER ARMY MEDICAL CENTER. <span class="mark">\<Enter\></span>

--------------------------------------------------------------------------

HOST Lab(s)

-------------------------------------------------------------------------

1\. HOST Lab: TRIPLER ARMY MEDICAL CENTER (Uneditable)

2\. Logical Link: LA7V0052

3\. Message Configuration: LA7V HOST 0052

4\. Auto Instrument: LA7V HOST 0052 <span class="mark">\<Enter\></span>

Enter a number (1-4): <span class="mark">\<Enter\></span>

### Step 6: LIM populate Lab Code Mapping file with DoD codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use option ‘Initialize DOD Codes \[LA7V 62.47 ADD DOD\]’ to populate the Lab Code Mapping file with the standard DOD local codes for this message configuration. This option is located on the ‘Lab Code Mapping File menu \[LA7V 62.47 MENU\]’, which is located on the ‘Lab Shipping Management Menu \[LA7S MGR MENU\].’

### Step 7: IRM complete the HL7 Environment setup for TCP/IP HL7 transport protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL LOGICAL LINK file (#870) contains the links used by the HL7 software to send messages. This file stores parameters that define the actions of the lower level protocols and information that the Systems Link Monitor uses to provide feedback regarding the status of each link.

1.  Select the logical link created for the DoD facility (LA7Vnnnn, where nnnn is the 4-digit DMIS ID of the DoD facility).
30. Use the ‘Link Edit \[HL EDIT LOGICAL LINKS\]’ option within the ‘Filer and Link Management Options \[HL MENU FILER LINK MGT\]’ menu within the ‘HL7 Main Menu \[HL MAIN MENU\]’ to edit the HL LOGICAL LINK file (#870), AUTOSTART field (#4.5) in the Logical Link Information section.
31. Set the AUTOSTART field (#4.5) to 1 (Enabled), to start the link automatically after TaskMan is restarted.  
    If the link is not set to restart automatically, it must be started manually using the ‘Start/Stop Links \[HL START\]’ option within the ‘Filer and Link Management Options \[HL MENU FILER LINK MGT\]’ menu within the ‘HL7 Main Menu \[HL MAIN MENU\]’ menu.
32. Set up the client device for the Host facility laboratory.  
    The client device is the link that connects to the listener device of the other facility to transmit order messages from a Collecting facility and to transmit result messages from a Host facility. Refer to the Example of HL7 Environment Setup Screen that follows.

> **NOTE:** A separate client device must be created for each facility to which LEDI manifests are sent.

Figure 22. Example of HL7 Environment Setup Screen

NODE: LA7Vnnnn (where nnnn is the HOST lab DoD DMIS ID)

LLP TYPE: TCP

DEVICE TYPE: Non-Persistent Client

QUEUE SIZE: 10

RE-TRANSMISSION ATTEMPTS: 5

TCP/IP ADDRESS: *xx.xxx.xxx.xx* (IP address of the Austin Automation Center’s (AAC) Vitria Interface Engine (IE))

TCP/IP PORT: *xxxxx* the port the AAC Vitria IE listener device is listening on.

TCP/IP SERVICE TYPE: CLIENT (Sender)

PERSISTENT: NO (If a link gets tied up, other systems will not be able to connect

and transmit messages to you. Therefore it must be set to persistent: NO).

### Step 8: LIM work with the interface coordinator at the Reference laboratory to test the system

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Test the system by performing the following steps.

1.  Order laboratory test(s) on a test patient.
33. Build the test(s) on a shipping manifest.
34. Close and ship the manifest.
35. Provide the interface coordinator with the manifest number.

> **NOTE:** The interface coordinator must be able to accept the manifest, process orders, and enter test results.

### Step 9: LIM train end users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** To assist with training end users, review the *LEDI IV Update User Manual*.

## Host Facility–DoD to VA Laboratory Implementation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IRM and LIM staffs must coordinate the implementation of the LEDI IV software and perform the setup instructions in the following sequence for a successful implementation.

> **NOTE:** When implementing this interface with a DoD facility, consult the LDSI National Implementation Plan for guidance to establish communication with the DoD facility via the VA/DoD VPN.

### Step 1: IRM set up the INSTITUTION file (#4)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Load the DoD DMIS ID codes into the INSTITUTION file (#4), using the ‘Load DMIS ID \[XUMF DMIS ID LOAD\]’ option installed by the Kernel Patch XU\*8.0\*261, if not previously performed.

Check both the Host and Collecting institutions for the four fields from the INSTITUTION file (#4) used by the LEDI IV software.

- Name (#.01) field: The Institution Master File maintains nationally controlled entries for VA and DoD facilities.
- Agency Code (#95) field: This field indicates to the LEDI IV software whether the facility is a VA or DoD facility.
1.  VA facilities should be set to: VA
40. DoD facilities should be set to:
- AF–AIR FORCE
- ARMY–ARMY
- N–NAVY
- Station Number (#99) field: For VA facilities
- Identifier (#9999) field: For DoD facilities to identify the DMIS ID for a facility

### Step 2: IRM create LEDI-related mail groups using the ‘Mail Group Edit \[XMEDITMG\]’ option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Local mail group for the ORDERS RECEIVED Alert: This mail group notifies members when the Lab Universal Interface software processes an HL7 message containing test orders.

Example Alert

Lab Messaging - Manifest# 170-20130415-1 received from LA7V COLLECTION 170

- Designate the LIM as the coordinator for the ORDERS RECEIVED Alert mail group.
- The mail group must have at least one active lab user currently assigned or added.
- This mail group should be comprised of the users in the lab that receive the orders from the collection sites.

Local mail group for the ERROR ON MESSAGE Alert: This mail group notifies members of error conditions encountered during the processing of a Laboratory HL7 message.

- The LAB MESSAGING mail group can be used for this function. The LAB MESSAGING mail group is a general mail group used by the LAB Universal Interface and LEDI software to address alerts when conditions are detected requiring review and/or corrective action.
- If a mail group already exists for lab HL7 error alerts, then the existing mail group can be used instead of creating a new one.
- The members of this mail group must include the LIM and selected Lab and IRM personnel responsible for maintenance and support of the LAB Universal Interface and LEDI software.
- Designate the LIM as a member of the ERROR ON MESSAGE Alert mail group.

### Step 3: LIM provide DoD laboratory with your electronic test catalog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Contact the DoD laboratory to provide VA specimen codes and name, as well as collection sample codes and names for each test that the VA site is able to accept for testing from the DOD collection site. The VA site will also need to acquire the equivalent DOD specimen and sample codes for the same tests for mapping in VistA.

- VistA needs this information to handle the non-HL7 codes that the DoD CHCS systems use to identify specimens and collection samples.
- These codes are entered on the VistA side during set up of shipping configurations, which are used to process laboratory test orders from a DoD facility.
- The DoD specimen/collection sample codes are mapped to the corresponding VA VistA specimen/collection samples.

### Step 4: LIM Map Micro and/or AP Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Map the LEDI Micro and/or AP tests using option ‘Manage MI/AP Test Mappings’ \[LRCAPFF\] located on the ‘National Laboratory File \[LR7O 60-64\]’ menu. The tests need to be mapped to an appropriate NLT code and a Database Code.

> **NOTE:** A report of the mappings can be printed using option ‘Print MI/AP Test Mappings \[LA7VPFL\]’ located on the ‘Lab Shipping Management Menu \[LA7S MGR MENU\]’.

Figure 23. Example of Manage MI/AP Test Mappings

Select LOINC Main Menu Option: <span class="mark">NATIONAL LABORATORY FILE</span>

1 Semi-automatic Linking of file 60 to 64

2 Manual Linking of file 60 to 64

3 Result NLT Auto Linker

4 Link Result NLT Manual

5 Manage MI/AP Test Mappings

Select National Laboratory File Option: <span class="mark">5 \<Enter\></span> Manage MI/AP Test Mappings

Select one of the following:

MI Microbiology

SP Surgical Pathology

CY Cytopathology

EM Electron Microscopy

Choose Lab Area Subscript: <span class="mark">MI \<Enter</span> Microbiology

Enter Laboratory Test Name: <span class="mark">ANAEROBIC CULTURE</span>

Editing LABORATORY TEST file (#60)

NATIONAL VA LAB CODE: Micro Anerobic Culture// <span class="mark">\<Enter\></span>

60 = ANAEROBIC CULTURE \[553\]

64 = Micro Anerobic Culture (87998.0000) \[2070\]

Link the two entries? No// <span class="mark">Y \<Enter\></span> (Yes)

o----LINKED----o

No Database Code on file for this NLT code.

Select an MI Database Code: <span class="mark">?</span>

Answer with LAB ELECTRONIC CODES SEQUENCE, or NAME, or LOINC ABBR, or

HL7 ABBR, or LAB ABBR, or TYPE

Do you want the entire LAB ELECTRONIC CODES List? <span class="mark">Y \<Enter\></span> (Yes)

Choose from:

9193 MI Bacteria Rpt Date GENERAL BACTERIA RPT DATABASE

9194 MI Gram Stain Rpt Date GENERAL GRAM STAIN DATANAME

9197 MI Parasitology Complete Rpt Date GENERAL PARASITOLOGY RPT DATE

DATANAME

9201 MI Mycology Rpt Date GENERAL MYCOLOGY RPT DATE DATANAME

9205 MI TB Rpt Date GENERAL TB RPT DATE DATANAME

9209 MI Virology Rpt Date GENERAL VIROLOGY RPT DATE DATANAME

Select an MI Database Code: <span class="mark">9193 \<Enter\></span> MI Bacteria Rpt Date GENERAL BACTERIA RPT DATABASE

Update complete.

Figure 24. Example of Manage MI/AP Test Mappings

Select LOINC Main Menu Option: <span class="mark">5 \<Enter\></span> National Laboratory File

1 Semi-automatic Linking of file 60 to 64

2 Manual Linking of file 60 to 64

3 Result NLT Auto Linker

4 Link Result NLT Manual

5 Manage MI/AP Test Mappings

Select National Laboratory File Option: <span class="mark">5 \<Enter\></span> Manage MI/AP Test Mappings

Select one of the following:

MI Microbiology

SP Surgical Pathology

CY Cytopathology

EM Electron Microscopy

Choose Lab Area Subscript: CY// <span class="mark">\<Enter\></span> Cytopathology

Enter Laboratory Test Name: <span class="mark">CYTOLOGY REQUEST</span>

Editing LABORATORY TEST file (#60)

NATIONAL VA LAB CODE: Report Cytology// <span class="mark">\<Enter\></span>60 = CYTOLOGY REQUEST \[5475\]

<span class="mark">64</span> = Report Cytology (88593.0000) \[3660\]

Link the two entries? No// <span class="mark">Y \<Enter\></span> (Yes)

o----LINKED----o

No Database Code on file for this NLT code.

Select an CY Database Code: <span class="mark">?</span>

Choose from:

9269 CY Supplementary Rpt Date GENERAL SUPPLEMNETARY REPORT DATANAME

9371 CY Complete Rpt Date GENERAL DATE REPORT COMPLETE DATABASE

Select an CY Database Code: <span class="mark">9371 \<Enter\></span> CY Complete Rpt Date GENERAL DATE REPORT COMPLETE DATABASE

Update complete.

### Step 5: LIM set up the LAB SHIPPING CONFIGURATION file (#62.9)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the ‘Edit Shipping Configuration \[LA7S EDIT 62.9\]’ option under the ‘Lab Shipping Management Menu \[LA7S MGR MENU\]’ option, to configure the file.

The LAB SHIPPING CONFIGURATION file (#62.9) contains the test information to process orders received from the DoD facility.

### Step 6: LIM set up the HL7 Environment to receive orders from the Collecting facility laboratories

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the ‘LEDI Setup \[LA7V SETUP\]’ option to set up the HL7 environment. It is located on the ‘Lab Shipping Management Menu \[LA7S MGR MENU\]’ option under the ‘Lab liaison menu \[LRLIAISON\]’ option.

- TCP/IP must be used as the HL7 transport protocol for VA to DoD Lab interfaces.
- When defining institution names, do not use the Host or Collecting facility name of either of the two institutions from the example.

Example Screen

(The two institution names in the following screen capture are used only as examples.)

Figure 25. Example of LEDI Setup \[LA7V SETUP\] option

Select OPTION NAME: <span class="mark">LA7V SETUP \<Enter\></span> LEDI Setup

LEDI Setup

-----------------------------------------------------------------------------

LEDI Setup

-----------------------------------------------------------------------------

COLLECTION Labs: Use option \#1 to setup HOST labs.

HOST Labs : Use option \#2 to setup COLLECTION labs.

1\. Add/Edit HOST Lab

2\. Add/Edit COLLECTION Lab

Enter a number (1-2): <span class="mark">2</span>

-----------------------------------------------------------------------------

COLLECTION Lab(s)

-----------------------------------------------------------------------------

1\. Add COLLECTION Lab

Enter a number (1-10): <span class="mark">1</span>

-----------------------------------------------------------------------------

COLLECTION Lab Setup

-----------------------------------------------------------------------------

1\. COLLECTION Lab:

Enter a number (1-1): <span class="mark">1</span>

Select INSTITUTION NAME: <span class="mark">TRIPLER ARMY MEDICAL CENTER \<Enter\></span> HI USAH 459CN

Setting up the REMOTE Lab, TRIPLER ARMY MEDICAL CENTER and HOST Lab REGION 7 ISC, TX (DEMO)

Updating HL7 APPLICATION PARAMETER file (#771).

Updating PROTOCOL file (#101).

LA7V Results Reporting to 0052

LA7V Send Results to 0052

LA7V Receive Order from 0052

LA7V Process Order from 0052

Updating LA7 MESSAGE PARAMETER file (#62.48) for the REMOTE Lab TRIPLER ARMY MEDICAL CENTER.

Adding LA7V COLLECTION 0052

HL7 v1.6 Environment setup is complete!!

-----------------------------------------------------------------------------

COLLECTION Lab Setup

-----------------------------------------------------------------------------

1\. COLLECTION Lab: TRIPLER ARMY MEDICAL CENTER (Uneditable)

2\. Logical Link (MailMan or TCP/IP): LA7V0052

3\. Message Configuration: LA7V COLLECTION 0052

Enter a number (1-3): <span class="mark">2</span>

-----------------------------------------------------------------------------

Logical Link for transmissions to/from TRIPLER ARMY MEDICAL CENTER

-----------------------------------------------------------------------------

Protocol Logical Link

---------- ---------------

LA7V Process Order from 0052 LA7V0052 (TCP)

LA7V Send Results to 0052 LA7V0052 (TCP)

Enter a Logical Link: (MM/TCP): <span class="mark">TCP/IP</span>

Updating HL LOGICAL LINK file (#870).

Updating the PROTOCOL file (#101).

-----------------------------------------------------------------------------

COLLECTION Lab Setup

-----------------------------------------------------------------------------

1\. COLLECTION Lab: TRIPLER ARMY MEDICAL CENTER (Uneditable)

2\. Logical Link (MailMan or TCP/IP): LA7V0052

3\. Message Configuration: LA7V COLLECTION 0052

Enter a number (1-3): <span class="mark">3</span>

GRACE PERIOD FOR MESSAGES: <span class="mark">3</span>

LOG ERRORS: ON// <span class="mark">\<Enter\></span>

MULTIPLE ORDERS: <span class="mark">2 \<Enter\></span> SINGLE ORDER

Select ALERT CONDITION: ): <span class="mark">\<Enter\></span>

-----------------------------------------------------------------------------

COLLECTION Lab Setup

-----------------------------------------------------------------------------

1\. COLLECTION Lab: TRIPLER ARMY MEDICAL CENTER (Uneditable)

2\. Logical Link (MailMan or TCP/IP): LA7V0052

3\. Message Configuration: LA7V COLLECTION 0052

Enter a number (1-3): <span class="mark">\<Enter\></span>

-----------------------------------------------------------------------------

COLLECTION Lab(s)

-----------------------------------------------------------------------------

1\. TRIPLER ARMY MEDICAL CENTER (LA7V COLLECTION 0052)

2\. Add COLLECTION Lab

Enter a number (1-2): <span class="mark">\<Enter\></span>

-----------------------------------------------------------------------------

LEDI Setup

-----------------------------------------------------------------------------

COLLECTION Labs: Use option \#1 to setup HOST labs.

HOST Labs: Use option \#2 to setup COLLECTION labs.

1\. Add/Edit HOST Lab

2\. Add/Edit COLLECTION Lab

-----------------------------------------------------------------------------

### Step 7: IRM complete the HL7 Environment setup for TCP/IP HL7 transport protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL LOGICAL LINK file (#870) contains the links used by the HL7 software to send messages. This file stores parameters that define the actions of the lower level protocols and information that the Systems Link Monitor uses to provide feedback regarding the status of each link.

1.  Select the logical link created for the DoD facility (LA7Vnnnn, where nnnn is the 4-digit DMIS ID of the DoD facility).
36. Use the ‘Link Edit \[HL EDIT LOGICAL LINKS\]’ option within the ‘Filer and Link Management Options \[HL MENU FILER LINK MGT\]’ menu within the ‘HL7 Main Menu \[HL MAIN MENU\]’ menu to edit the HL LOGICAL LINK file (#870), AUTOSTART field (#4.5) in the Logical Link Information section.
37. Set the AUTOSTART field (#4.5) to 1 (Enabled), to start the link automatically after TaskMan is restarted.  
    If the link is not set to restart automatically, it must be started manually using the ‘Start/Stop Links \[HL START\]’ option within the ‘Filer and Link Management Options \[HL MENU FILER LINK MGT\]’ menu within the ‘HL7 Main Menu \[HL MAIN MENU\]’ menu.

> **NOTE:** For information on single and multi-threaded listeners, refer to the *VistA Health Level Seven (HL7) Site Manager & Developer Manual* in the HL7 section of the VDL.

38. Set up the client device for the Collecting facility laboratory. The client device is the link that connects to the listener device of the other facility to transmit order messages from a Host facility and to transmit result messages from a Host facility.

> **NOTE:** A separate client device must be created for each facility to which LEDI manifests are sent.

Figure 26. Example of Setting Up Device for Collecting Lab

NODE: LA7Vnnnn (where nnnn is the COLLECTING lab DoD DMIS ID)

LLP TYPE: TCP

DEVICE TYPE: Non-Persistent Client

QUEUE SIZE: 10

RE-TRANSMISSION ATTEMPTS: 5

TCP/IP ADDRESS: xx.xxx.xxx.xx (IP address of the Austin Automation Center’s (AAC) Vitria

Interface Engine (IE)).

TCP/IP PORT: xxxxx (the port the AAC IE listener device is listening on).

TCP/IP SERVICE TYPE: CLIENT (Sender)

PERSISTENT: NO (If a link gets tied up, other systems will not be able to connect and

transmit messages to you. Therefore, it must be set to persistent: NO).

### Step 8: LIM work with the interface coordinator at the Collecting facility laboratory to test the system

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Collecting facility tests the system.

- The Collecting facility orders laboratory test(s) on a test patient.
- The Collecting facility builds the test(s) on a shipping manifest.
- The Collecting facility closes and ships the manifest.
- The Collecting facility contact provides the LIM of the Host facility with the manifest number.
- The Collecting facility interface coordinator must be able to verify the laboratory test result(s) on the test patient via the appropriate CHCS options in the Collecting system.

> **NOTE:** The Host facility LIM must be able to accept the manifest, process orders, and enter test results.

### Step 9: LIM train end users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To assist with training end users, review the *LEDI IV Update User Manual*.

## Collecting Facility–VA to Commercial Reference Laboratory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IRM and LIM staffs must coordinate the implementation of the LEDI IV software and perform the setup instructions in the following sequence for a successful implementation.

### Step 1: IRM set up the INSTITUTION file (#4)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Load or update the local INSTITUTION file (#4), using the ‘VA FileMan \[DIUSER\], Enter or Edit File Entries \[DIEDIT\]’ option.

Check both the Host and Collecting institutions for the two fields from the INSTITUTION file (#4) used by the LEDI IV software.

- Name (#.01) field: This applies only for non-VA entries. The Institution Master File maintains nationally controlled entries.
- Agency Code (#95) field: Set to Other for commercial reference laboratories and non-US government health care facilities.  
  This field indicates to the LEDI IV software whether the facility is a VA or non-VA facility. This is applicable only for non-VA entries. The Institution Master File maintains nationally controlled entries.

### Step 2: IRM create LEDI-related mail groups using the ‘Mail Group Edit \[XMEDITMG\]’ option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Local mail group for the ERROR ON MESSAGE Alert: This mail group notifies members of error conditions encountered during the processing of a Laboratory HL7 message.

- The LAB MESSAGING mail group can be used for this function. The LAB MESSAGING mail group is a general mail group used by the LAB Universal Interface and LEDI software to address alerts when conditions are detected requiring review and/or corrective action.
- If a mail group already exists for lab HL7 error alerts, then the existing mail group can be used instead of creating a new one.
- The members of this mail group must include the LIM and selected Lab and IRM personnel responsible for maintenance and support of the LAB Universal Interface and LEDI software.
- Designate the LIM as a member of the ERROR ON MESSAGE Alert mail group.

### Step 3: LIM set up the lab test files to send specimens to the commercial Reference laboratory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Contact the reference laboratory to acquire the following information:
- Specimen collection requirements
- Specimen handling/minimum requirements
- Alternate specimen (if any)
- Stability (for shipping conditions)
- Patient prep instructions
- Schedule of testing and TAT
- Order code to order the tests
- Exact test name for Non-VA test name
- List of tests for panel tests
- Result code(s) used to report the results
- Normal Range and Critical Values
- Units of measure
- Account number for use with the interface samples
39. Create/edit an accession area in the ACCESSION file (#68) only for tests/specimens sent to the Host laboratory for processing.
40. Use the ‘VA FileMan \[DIUSER\], Enter or Edit \[DIEDIT\]’ option to assign a Numeric Identifier to the Numeric Identifier field (#4).
41. Edit the LABORATORY TEST file (#60) to send specimens to the Host facility laboratory.  
    New lab tests can be created to match the Host facility laboratory requirements, or existing lab tests can be utilized, if the entries are compatible with the Host facility laboratory requirements.

> **NOTE:** All tests must utilize the Accession Area from \#2.

- If you do not already have an established LEDI Host Load/Work List for this configuration, then you should create a new test LOAD/WORK LIST file (#68.2) entry to define and accept lab results transmitted by the Host facility laboratory.
- If you already have a LEDI Host Load/Work List for this configuration, then the existing Load/Work List entry should be used.
42. Add a profile to the Load/Work list used to process results for each subscript processed. The profiles must contain all resultable lab tests processed by the Host facility laboratory. Configuration of the Default Reference Laboratory field is not required, but it will facilitate the entry of results.

> **NOTE:** There must be separate profiles specified for CH, MI, SP, CY, and EM subscripts.

43. Add Host antibiotics not currently configured in VistA, using one of the following options:
- If the antibiotic is not defined in LAB DATA file (#63), use the ‘Add a new internal name for an antibiotic \[LRWU7\]’ option to create an internal name for the antibiotic.
- If the antibiotic is not currently in the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06), use the ‘Edit an Antibiotic \[LRWU7 EDIT\]’ option to add the antibiotic.  
  Include mapping to National VA Lab Code NLT and related LOINC codes if already mapped to the NLT and configure appropriate susceptibility interpretations.
44. Map Host LOINC codes used to report susceptibility testing using the ‘Edit Susceptibility \[LA7V 62.47 EDIT SUSC\]’option.

### Step 4: LIM set up the Lab Shipping Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The lab shipping files are located on the ‘Lab Shipping Management Menu \[LA7S MGR MENU\]’ option under the ‘Lab liaison menu \[LRLIAISON\]’ option.

Configure the following four files in the order listed.

- First–LAB SHIPPING METHOD file (#62.92)
- Second–LAB SHIPPING CONDITION file (#62.93)
- Third–LAB SHIPPING CONTAINER file (#62.91)
- Fourth–LAB SHIPPING CONFIGURATION (#62.9)

> **NOTE:** The first three files may already be set up, if a VA-to-VA interface exists for your facility. Online Help is available by entering two question marks (??) at the field prompt.

1.  Configure the LAB SHIPPING METHOD file (#62.92), using the ‘Edit Shipping Method \[LA7S EDIT 62.92\]’ option.  
    It contains the transport method to ship specimens, such as Courier, Taxi, FEDEX and USPS.

Figure 27. Example of CME—Edit Shipping Method \[LA7S EDIT 62.92\] option

Select Lab liaison menu Option: <span class="mark">SMGR \<Enter\></span> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: <span class="mark">?</span>

CFE Edit Shipping Configuration

CTE Edit Shipping Container

CME Edit Shipping Method

CDE Edit Shipping Condition

LSU LEDI Setup

LSCT Load SNOMED SCT Mapping

MSCT Map Non-VA SNOMED CT codes

CAT Electronic Catalog Menu ...

LCM Lab Code Mapping File ...

PTM Print MI/AP Test Mappings

CU Code Usage

DSC Display a Shipping Configuration

DSO Display SCT Overrides

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Lab Shipping Management Menu Option: <span class="mark">CME \<Enter\></span> Edit Shipping Method

Select SHIPPING METHOD: <span class="mark">?</span>

Answer with LAB SHIPPING METHOD NAME

You may enter a new LAB SHIPPING METHOD, if you wish

NAME MUST BE 3-30 CHARACTERS, NOT NUMERIC OR STARTING WITH

PUNCTUATION

Select SHIPPING METHOD: <span class="mark">FEDEX</span>

Are you adding 'FEDEX' as a new LAB SHIPPING METHOD (the 1ST)? <span class="mark">Y \<Enter\></span> (Yes)

NAME: FEDEX// <span class="mark">\<Enter\></span>

Select Lab Shipping Management Menu Option: <span class="mark">CME \<Enter\></span> Edit Shipping Method

Select SHIPPING METHOD: <span class="mark">COURIER</span>

Are you adding 'COURIER' as a new LAB SHIPPING METHOD (the 2ND)? <span class="mark">Y \<Enter\></span> (Yes)

NAME: COURIER// <span class="mark">\<Enter\></span>

45. Configure the LAB SHIPPING CONDITION file (#62.93), using the ‘Edit Shipping Condition \[LA7S EDIT 62.93\]’ option.  
    It contains entries that describe the conditions under which a lab shipment is transported, such as Ambient temperature, Frozen, Refrigerated.

Figure 28. Example of CDE—Edit Shipping Condition \[LA7S EDIT 62.93\] option

Select Lab liaison menu Option: <span class="mark">SMGR \<Enter\></span> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: <span class="mark">??</span>

CFE Edit Shipping Configuration

CTE Edit Shipping Container

CME Edit Shipping Method

CDE Edit Shipping Condition

LSU LEDI Setup

LSCT Load SNOMED SCT Mapping

MSCT Map Non-VA SNOMED CT codes

CAT Electronic Catalog Menu ...

LCM Lab Code Mapping File ...

PTM Print MI/AP Test Mappings

CU Code Usage

DSC Display a Shipping Configuration

DSO Display SCT Overrides

Select Lab Shipping Management Menu Option: <span class="mark">CDE \<Enter\></span> Edit Shipping Condition

Use this option to setup the Lab Shipping Condition file.

Select SHIPPING CONDITION: <span class="mark">?</span>

Answer with LAB SHIPPING CONDITIONS NAME

You may enter a new LAB SHIPPING CONDITIONS, if you wish

NAME MUST BE 3-30 CHARACTERS, NOT NUMERIC OR STARTING WITH

PUNCTUATION

Select SHIPPING CONDITION: <span class="mark">ROOM TEMPERATURE</span>

Are you adding 'Room Temperature' as

a new LAB SHIPPING CONDITIONS (the 1ST)? No// <span class="mark">Y \<Enter\></span> (Yes)

NAME: Room Temperature// <span class="mark">\<Enter\></span>

ABBREVIATION: <span class="mark">RT</span>

46. Configure the LAB SHIPPING CONTAINER file (#62.91), using the ‘Edit Shipping Container \[LA7S EDIT 62.91\]’ option.  
    It contains the type of containers that the laboratory uses to ship laboratory test specimens. There are three types of containers used for shipping laboratory test specimens.
- Primary–specimen is shipped in the original collection container, such as a Lavender top tube.
- Aliquot–specimen is transferred to a tube/jar before shipment, such as a Plastic Transport Tube and Brown Plastic Tube.
- Packaging–packaging containers used for holding the specimen containers, such as a box.

Figure 29. Example of CTE—Edit Shipping Container \[LA7S EDIT 62.91\] option

Select Lab liaison menu Option: <span class="mark">SMGR \<Enter\></span> Lab Shipping Management Menu

Select Lab Shipping Management Menu Option: <span class="mark">?</span>

CFE Edit Shipping Configuration

CTE Edit Shipping Container

CME Edit Shipping Method

CDE Edit Shipping Condition

LSU LEDI Setup

LSCT Load SNOMED SCT Mapping

MSCT Map Non-VA SNOMED CT codes

CAT Electronic Catalog Menu ...

LCM Lab Code Mapping File ...

PTM Print MI/AP Test Mappings

CU Code Usage

DSC Display a Shipping Configuration

DSO Display SCT Overrides

Select Lab Shipping Management Menu Option: <span class="mark">CTE \<Enter\></span> Edit Shipping Container

Use this option to setup the Lab Shipping Container file.

Select SHIPPING CONTAINER: <span class="mark">?</span>

Answer with LAB SHIPPING CONTAINER NAME

You may enter a new LAB SHIPPING CONTAINER, if you wish

NAME MUST BE 3-30 CHARACTERS, NOT NUMERIC OR STARTING WITH

PUNCTUATION

Select SHIPPING CONTAINER: <span class="mark">PLASTIC TUBE</span>

Are you adding 'Plastic Tube' as

a new LAB SHIPPING CONTAINER (the 1ST)? No// <span class="mark">Y \<Enter\></span> (Yes)

NAME: Plastic Tube// <span class="mark">\<Enter\></span>

TYPE: <span class="mark">?</span>

Enter what this container is used for.

Choose from:

1 PACKAGING

2 PRIMARY

3 ALIQUOT

TYPE: <span class="mark">3 \<Enter\></span> ALIQUOT

47. Configure the LAB SHIPPING CONFIGURATION file (#62.9), using the ‘Edit Shipping Configuration \[LA7S EDIT 62.9\]’ option.  
    It contains the specimen volume, weight, collection end date/time (collection duration), patient height and weight.

> **NOTE:** LOINC codes are used to identify patient height and weight, and specimen weight when appropriate.

Figure 30. Example of Edit Shipping Configuration (Next 5 Screens)

Select Lab Shipping Management Menu Option: <span class="mark">CFE \<Enter\></span> Edit Shipping Configuration

Select SHIPPING CONFIGURATION: <span class="mark">MAD</span>

1 MADISON TO HINES

2 MADISON TO MILWAUKEE

3 MADISON TO QUEST

CHOOSE 1-3: <span class="mark">3 \<Enter\></span> MADISON TO QUEST

Select one of the following:

1 Collecting facility

2 Host facility

Are you editing this entry as the: <span class="mark">1 \<Enter\></span> Collecting facility

NAME: MADISON TO QUEST// <span class="mark">\<Enter\></span>

COLLECTING FACILITY: WM S MIDDLETON MEM VA HOSP// <span class="mark">\<Enter\></span>

COLLECTING FACILITY'S SYSTEM: WM S MIDDLETON MEM VA HOSP

// <span class="mark">\<Enter\></span>

HOST FACILITY: QUEST// <span class="mark">\<Enter\></span>

HOST FACILITY'S SYSTEM: QUEST// <span class="mark">\<Enter\></span>

NON-VA SYSTEM IDENTIFIER: QDI// <span class="mark">??</span>

If this is used to communicate with a non-VA system, enter the 2-3

character identifier used to name the HL7 application.

NON-VA SYSTEM IDENTIFIER: QDI// <span class="mark">\<Enter\></span>

ACCOUNT NUMBER: 113779// <span class="mark">??</span>

If the system that you are shipping to requires an account number for

billing or other purposes enter the number here. It will be printed on

shipping manifests and transmitted in electronic messages if applicable.

ACCOUNT NUMBER: 113779// <span class="mark">\<Enter\></span> *\<\<\< from Step 4a above.*

TEST CODING SYSTEM: NON-VA// <span class="mark">??</span>

If orders are being sent to a non-VA facility and the facility

cannot accept VA test order codes then answer with the type of

coding system. "NON-VA" indicates that the other system is using

a local coding system. The laboratory shipping software will then

use the non-VA test codes entered for each test on this

configuration.

If the non-VA facility can accept VA test codes then answer "NLT"

and the software will sent VA test order codes.

VA test order codes are usually NLT codes but in the future may

be LOINC codes. Selecting "LOINC" is currently not supported.

Support will be added in a future version of the LEDI software

when LOINC coding has been implemented within VA facilities.

Choose from:

0 NLT

1 NON-VA

2 LOINC

TEST CODING SYSTEM: NON-VA// <span class="mark">\<Enter\></span>

SPECIMEN CODING SYSTEM: <span class="mark">??</span>

Collecting facility:

If orders are sent to a non-VA facility and the

facility cannot receive HL7 specimen codes from HL7

table 0070 then answer with the type of coding system

"LOCAL".

Choose from:

0 HL7 TABLE 0070

1 LOCAL-NON HL7

SPECIMEN CODING SYSTEM:

STATUS: ACTIVE// <span class="mark">??</span>

This field is used to designate whether this shipping configuration is

"active", i.e. selectable by the user for use in building, processing

and receipting shipments of laboratory test.

Choose from:

0 INACTIVE

1 ACTIVE

STATUS: ACTIVE// <span class="mark">\<Enter\></span>

LAB MESSAGING LINK: LA7V HOST QDI// <span class="mark">??</span>

This field is used to link a shipping configuration with an electronic

transmission of shipping manifests. When a shipping manifest is shipped, this field is checked to determine if the software should transmit the orders on the manifest to the host facility. It identifies the entry in the LA7 MESSAGE PARAMETER file \#62.8 to use for building and transmitting the manifest.

Choose from:

LA7V COLLECTION 585

LA7V COLLECTION 676

LA7V COLLECTION 695

LA7V HOST 578

LA7V HOST 695

LA7V HOST QDI

UNIVERSAL INTERFACE

LAB MESSAGING LINK: LA7V HOST QDI// <span class="mark">\<Enter\></span>

SHIPPING METHOD: COURIER// <span class="mark">??</span>

This field is used to designate the method of shipment used by a shipping configuration. Examples could be courier, taxi, commercial carrier, etc.

COURIER

SHIPPING METHOD: COURIER// <span class="mark">\<Enter\></span>

BARCODE MANIFEST: YES// <span class="mark">??</span>

This field determines if site/patient/specimen information is barcoded

on the shipping manifest when it has a status of "shipped".

There are two styles of bar codes. The regular style (code="YES"), which was released with the original version of Laboratory Electronic Data Interchange (LEDI), produces a long bar code. If the receiving site, which is reading these type of bar codes, has problems then switch to the compact style (code="YES-COMPACT"). This will produce a shorter bar code.

Choose from:

0 NO

1 YES

2 YES-COMPACT

BARCODE MANIFEST: YES// <span class="mark">\<Enter\></span>

MANIFEST RECEIPT: YES// <span class="mark">??</span>

Allows site to have a receipt printed with a shipping manifest when the status of the manifest is "SHIPPED". This receipt can be used to record acknowledgment of receipt of the shipment by the courier service used to transport the specimens to the host facility.

Choose from:

0 NO

1 YES

MANIFEST RECEIPT: YES// <span class="mark">\<Enter\></span>

INCLUDE UNCOLLECTED SPECIMENS: NO// <span class="mark">??</span>

If specimens that are still pending receipt in lab are to build on a

shipping manifest then answer "YES". If only specimens that have been received in the lab, i.e. have a lab arrival time, are to build then

answer "NO".

Figure 31. Example of Edit Shipping Configuration Screen 3

If field is blank then default is "NO".

Choose from:

0 NO

1 YES

INCLUDE UNCOLLECTED SPECIMENS: NO// <span class="mark">\<Enter\></span>

Select TEST/PROFILE: INTERLEUKIN 6// <span class="mark">??</span>

You may enter a new TEST/PROFILE, if you wish

Enter the laboratory test that is used by this shipping

configuration.

Answer with LABORATORY TEST NAME, or LOCATION (DATA NAME), or

PRINT NAME

Do you want the entire 3537-Entry LABORATORY TEST List?

Select TEST/PROFILE: INTERLEUKIN 6// <span class="mark">\<Enter\></span>

TEST/PROFILE: INTERLEUKIN 6// <span class="mark">\<Enter\></span> *Editor Note: CH Test sample…*

ACCESSION AREA: QUEST// <span class="mark">??</span>

COLLECTION FACILITIES:

This field is used to designate the accession area to check when

searching for tests to build onto a shipping manifest. If it is blank

then the building process will skip over this test.

ACCESSION AREA: QUEST// <span class="mark">\<Enter\></span>

DIVISION: WM S MIDDLETON MEM VA HOSP// <span class="mark">??</span>

Collecting facilities:

If the manifest building process should only build accessions'

from a certain division on a manifest then enter the division

to screen these accessions. The division used here will be the

division associated with the user who created the accession.

This field will allow a site to screen accessions from

multiple divisions, only placing on the manifest an accession

from the specified division.

DIVISION: WM S MIDDLETON MEM VA HOSP// <span class="mark">\<Enter\></span>

Select FEEDER SHIPPING CONFIGURATION: <span class="mark">??</span>

You may enter a new FEEDER SHIPPING CONFIGURATION, if you wish

Allows the site to indicate that this test is eligible for a

manifest related to this shipping configuration if the specimen/test

has been received via the designated feeder shipping configuration

which was used to receive the specimen.

Example: A CBOC ships a specimen/test to the main VistA facility. The

main VistA facility then needs to place this specimen/test on another

shipping configuration manifest to ship to another laboratory. By

designating the feeder shipping configuration this test will only be

added to the manifest if it has been received by the laboratory via

a manifest related to the feeder shipping configuration.

If the manifest related to the feeder shipping configuration has not

been received then the test will not be added to prevent it being

placed on a manifest before the specimen has arrived.

Figure 32. Example of Edit Shipping Configuration Screen 4

SPECIMEN: <span class="mark">??</span>

This field is used to determine if a test for a particular specimen type should build on the shipping manifest. If left blank, i.e. no entry then

all specimens for this test are eligible for building on a shipping manifest. If a specimen type is entered then the specimen type of the accession must match before the test is eligible for building onto a shipping manifest. SPECIMEN:

URGENCY: <span class="mark">??</span>

COLLECTING FACILITIES:

If shipping laboratory tests that are a certain

urgency, specify the urgency that must match the

test urgency of the accession for the accession/test

to be placed on the shipping manifest.

Choose from:

1 EMERGENCY

2 STAT

3 PRIORITY

4 PRE-OP

5 OPR

6 ADMIT

7 OUTPATIENT

8 TODAY

9 ROUTINE

URGENCY: <span class="mark">\<Enter\></span>

SPECIMEN CONTAINER: ALIQUOT// <span class="mark">??</span>

COLLECTING FACILITIES:

The container used to hold the specimen. This could be the original collection container or a tube/vial/jar that the specimen is transferred to prior to shipment to another facility. It is the container that actually hold/contains the specimen.

Choose from:

ALIQUOT

PRIMARY

TRANS MEDIA

SPECIMEN CONTAINER: ALIQUOT// <span class="mark">\<Enter\></span>

SHIPPING CONDITION: FROZEN// <span class="mark">??</span>

COLLECTING FACILITIES:

This field describes under what temperature/environmental condition the specimen is to be shipped. Examples would be frozen, refrigerated or ambient temperature.

Choose from:

FECES-ROOM TEMP

FROZEN

INCUBATOR

REFRIGERATED

ROOM TEMPERATURE

URINE-REF

SHIPPING CONDITION: FROZEN// <span class="mark">\<Enter\></span>

PACKAGING CONTAINER: PACKAGE// <span class="mark">??</span>

COLLECTING FACILITIES:

Figure 33. Example of Edit Shipping Configuration Screen 5

SHIPPING CONDITION: FROZEN// <span class="mark">\<Enter\></span>

PACKAGING CONTAINER: PACKAGE// <span class="mark">??</span>

COLLECTING FACILITIES:

This field is used to determine what packaging container a test's specimen container is placed in when the specimen is being shipped to another facility.

Choose from:

PACKAGE

PACKAGING CONTAINER: PACKAGE// <span class="mark">\<Enter\></span>

NON-NLT TEST ORDER CODE: 46557P// <span class="mark">??</span>

Collecting facilities:

If sending test orders to a non-VA facility use

this field to store the test order codes used

by the non-VA system. It will be used when the

TEST CODING SYSTEM field (#.14) is set to "NON-VA".

NON-NLT TEST ORDER CODE: 46557P// <span class="mark">\<Enter\></span>

NON-NLT TEST ORDER NAME: INTERLEUKIN 6// <span class="mark">??</span>

Collecting facility:

If sending test orders to a non-VA facility use

this field to store the test order name used

by the non-VA system. The lab software to identify

the test name on the non-VA system when orders are

transmitted electronically uses this field. It will

be used when the TEST CODING SYSTEM field (#.14) is

set to "NON-VA".

NON-NLT TEST ORDER NAME: INTERLEUKIN 6// <span class="mark">\<Enter\></span>

NON-NLT TEST CODING SYSTEM: <span class="mark">??</span>

Collecting facilities:

If sending test orders to a non-VA facility use

this field to store the name of the coding system

used by the non-VA system. It will be used when the

TEST CODING SYSTEM field (#.14) is set to "NON-VA".

Name usually begins with "99" to indicate a local

coding system in the HL7 Standard.

NON-NLT TEST CODING SYSTEM: <span class="mark">\<Enter\></span>

REQUIRE PATIENT HEIGHT: <span class="mark">??</span>

Allows site to specify that the patient's height be sent with

an order for this test. Patient's height will be prompted for

and printed on manifest.

Choose from:

0 NO

1 YES

Figure 34. Example of Edit Shipping Configuration Screen 6

REQUIRE PATIENT HEIGHT: <span class="mark">Y \<Enter\></span> YES

PATIENT HEIGHT UNITS: <span class="mark">??</span>

Units used to measure the patient's height.

Select an entry from the LAB ELECTRONIC CODE

file (#74.061) that are measurements.

PATIENT HEIGHT UNITS: <span class="mark">IN \<Enter\></span> in MEASUREMENTS Inches

PATIENT HEIGHT CODE: <span class="mark">??</span>

Select the appropriate LOINC code to identify

the patient's height.

PATIENT HEIGHT CODE: <span class="mark">\<Enter\></span>

REQUIRE PATIENT WEIGHT: YES// <span class="mark">??</span>

Determines if the patient's weight is required

to be sent in the HL7 ORM order message and

printed on the shipping manifest. Actual

shipping and/or electronic transmission of a

shipping manifest will check for entry of the

patient's weight and prevent release if absent.

Choose from:

0 NO

1 YES

REQUIRE PATIENT WEIGHT: <span class="mark">Y \<Enter\></span> YES

PATIENT WEIGHT UNITS: <span class="mark">??</span>

Units used to measure the patient's weight.

Select an entry from the LAB ELECTRONIC CODE

file (#74.061) that are measurements.

PATIENT WEIGHT UNITS: <span class="mark">\<Enter\></span>

PATIENT WEIGHT CODE: <span class="mark">??</span>

Select the appropriate LOINC code to identify

the patient's weight.

PATIENT WEIGHT CODE: <span class="mark">\<Enter\></span>

REQUIRE COLLECTION VOLUME: YES// <span class="mark">??</span>

Determines if the specimen's collection volume

is required to be sent in the HL7 ORM order

message and printed on the shipping manifest.

Actual shipping and/or electronic transmission

of a shipping manifest will check for entry of

the specimen's collection volume and prevent

release if absent.

Choose from:

0 NO

1 YES

REQUIRE COLLECTION VOLUME: NO// <span class="mark">Y \<Enter\></span> YES

COLLECTION VOLUME UNITS: ml// <span class="mark">??</span>

Units used to measure the specimen's collection

volume. Select an entry from the LAB ELECTRONIC

CODE file \#74.061) that is a measurement.

COLLECTION VOLUME UNITS: ml// <span class="mark">\<Enter\></span>

COLLECTION VOLUME CODE: 3160// <span class="mark">??</span>

Enter the appropriate LOINC code to identify

the specimen's collection volume.

COLLECTION VOLUME CODE: 3160// <span class="mark">3160</span> -9 <span class="mark">\<Enter\></span>

SPECIMEN VOLUME:VOL:PT:SMN:<span class="mark">QN \<Enter\></span>

REQUIRE COLLECTION WEIGHT: YES// <span class="mark">??</span>

Determines if the specimen's collection weight

is required to be sent in the HL7 ORM order

message and printed on the shipping manifest.

Actual shipping and/or electronic transmission

of a shipping manifest will check for entry of

the specimen's collection weight and prevent

release if absent.

Figure 35. Example of Edit Shipping Configuration Screen 7

REQUIRE COLLECTION WEIGHT: YES// <span class="mark">??</span>

Determines if the specimen's collection weight

is required to be sent in the HL7 ORM order

message and printed on the shipping manifest.

Actual shipping and/or electronic transmission

of a shipping manifest will check for entry of

the specimen's collection weight and prevent

release if absent.

Choose from:

0 NO

1 YES

REQUIRE COLLECTION WEIGHT: <span class="mark">Y \<Enter\></span> YES

COLLECTION WEIGHT UNITS: <span class="mark">??</span>

Units used to measure the specimen's collection weight.

Select an entry from the LAB ELECTRONIC CODE file

( \#74.061) that is a measurement.

COLLECTION WEIGHT UNITS: <span class="mark">\<Enter\></span>

COLLECTION WEIGHT CODE: <span class="mark">??</span>

Enter the appropriate LOINC code to identify

the specimen's collection weight.

COLLECTION WEIGHT CODE: <span class="mark">\<Enter\></span>

REQUIRE COLLECTION END D/T: YES// <span class="mark">??</span>

Determines if the specimen's collection end

date/time is required to be sent in the HL7 ORM

order message and printed on the shipping

manifest. Actual shipping and/or electronic

transmission of a shipping manifest will check

for entry of the specimen's collection end

date/time and prevent release if absent.

Choose from:

0 NO

1 YES

REQUIRE COLLECTION END D/T: <span class="mark">YES</span>

COLLECTION DURATION UNITS: hr// <span class="mark">??</span>

Units used to calculate the specimen's

collection duration. Select an entry from the

LAB ELECTRONIC CODE file (#74.061) that is a

measurement and relates to time. // <span class="mark">Y \<Enter\></span> YES

Choose from:

hr hr MEASUREMENTS Hour

min min MEASUREMENTS Minute

s s MEASUREMENTS Seconds

COLLECTION DURATION UNITS: hr// <span class="mark">\<Enter\></span>

COLLECTION DURATION CODE: 24454// <span class="mark">??</span>

Enter the appropriate LOINC code to identify

the specimen's collection duration.

COLLECTION DURATION CODE: 24454// 24454 -1 <span class="mark">\<Enter\></span>

COLLECTION DURATION:TIME:\*:GAST:<span class="mark">QN\<Enter\></span>

Select TEST/PROFILE: <span class="mark">\<Enter\></span>

### Step 5: LIM set up the HL7 Environment and the Lab Auto-instrument file to receive results from a Host facility laboratory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the ‘LEDI Setup \[LA7V SETUP\]’ option located on the ‘Lab Shipping Management Menu \[LA7S MGR MENU\]’ option of the ‘Lab liaison menu \[LRLIAISON\]’option.

- TCP/IP must be used as the HL7 transport protocol for VA to Reference Lab interfaces.
- When defining institution names, do not use the Host or Collecting facility name of either of the two institutions from the example.

Example Screen

(The two institution names in the following screen capture are used only as examples.)

Figure 36. Example of LEDI Setup \[LA7V SETUP\] option

Select Lab Shipping Management Menu Option: <span class="mark">LSU \<Enter\></span> LEDI Setup

-----------------------------------------------------------------------------

LEDI Setup

-----------------------------------------------------------------------------

COLLECTION Labs: Use option \#1 to setup HOST labs.

HOST Labs : Use option \#2 to setup COLLECTION labs.

1\. HINES HOSPITAL (LA7V HOST 578)

2\. MILWAUKEE VAMC (LA7V HOST 695)

3\. Add HOST Lab

Enter a number (1-2): <span class="mark">1</span>

-----------------------------------------------------------------------------

HOST Lab(s)

-----------------------------------------------------------------------------

1\. HINES HOSPITAL (LA7V HOST 578)

2\. MILWAUKEE VAMC (LA7V HOST 695)

3\. Add HOST Lab

Enter a number (1-3): <span class="mark">3</span>

-----------------------------------------------------------------------------

HOST Lab(s)

-----------------------------------------------------------------------------

1\. HOST Lab:

Enter a number (1-1): <span class="mark">1</span>

Select INSTITUTION NAME: <span class="mark">??</span>

Choose from:

13TH & MISSION CA D 662BU

410TH STRATEGIC HOSPITAL SGAM MI

ABERDEEN SD CBOC 438GD

ABILENE, KS (CBOC) KS CBOC 589GK

ABILENE, TX (CBOC) TX CBOC 519HC

ABILENE, TX (ORC) TX ORC 519HA

AIR FORCE USAF 381

AKRON OH CBOC 541GG

ALAMOGORDO NM CBOC 501GI

Select INSTITUTION NAME: QUEST <span class="mark">\<Enter\></span>

Setting up the following Host Labs for QUEST

Updating HL7 APPLICATION PARAMETER file (#771).

Adding LA7V HOST QDI

Updating PROTOCOL file (#101).

Located in the LA7 (LAB MESSAGING) namespace.

LA7V Receive Results from QDI

Adding LA7V Receive Results from QDI

Located in the LA7 (LAB MESSAGING) namespace.

LA7V Process Results from QDI

Adding LA7V Process Results from QDI

Located in the LA7 (LAB MESSAGING) namespace.

LA7V Order to QDI

Adding LA7V Order to QDI

Located in the LA7 (LAB MESSAGING) namespace.

LA7V Send Order to QDI

Adding LA7V Send Order to QDI

Updating LA7 MESSAGE PARAMETER file (#62.48) for the HOST Lab QUEST.

Adding LA7V HOST QDI

Updating LAB AUTO INSTRUMENT file (#62.4) for HOST Lab QUEST.

Adding LA7V HOST QDI

HL7 v1.6 Environment setup is complete!!

-----------------------------------------------------------------------------

HOST Lab(s)

-----------------------------------------------------------------------------

1\. HOST Lab: QUEST (Uneditable)

2\. Logical Link: LA7QDI

3\. Message Configuration: LA7V HOST QDI

4\. Auto Instrument: LA7V HOST QDI

Enter a number (1-4): <span class="mark">2</span>

-----------------------------------------------------------------------------

Logical Link for transmissions to/from TOMAH VAMC

-----------------------------------------------------------------------------

Protocol Logical Link

---------- ---------------

LA7V Process Results from QDI

LA7V Send Order to QDI

Enter a Logical Link: (MM/TCP): <span class="mark">TCP \<Enter\></span> TCP/IP

Updating the PROTOCOL file (#101).

------------------------------------------------------------------------------

HOST Lab(s)

-----------------------------------------------------------------------------

1\. HOST Lab: QUEST (Uneditable)

2\. Logical Link: LA7VQDI

3\. Message Configuration: LA7V HOST QDI

4\. Auto Instrument: LA7V HOST QDI

Enter a number (1-4): <span class="mark">3</span>

GRACE PERIOD FOR MESSAGES: <span class="mark">??</span>

Grace period determines the number of days that messages for this configuration are kept on the system before purging when the message status is "purgeable". If this field is left blank, the system assumes 3 days. These messages are found in the LA7 MESSAGE QUEUE file (#62.49).

When messages have status of "error" they remain on the system until their corresponding error message is removed from the XTMP global by a KERNEL cleanup task. The messages then become "purgeable".

GRACE PERIOD FOR MESSAGES: <span class="mark">30</span>

LOG ERRORS: ON// <span class="mark">??</span>

If turned on, errors or exceptional conditions that occur during message processing are stored in the ^XTMP global for review. To review the log, in programmer mode, type D PRINT^LA7LOG.

Choose from:

0 OFF

1 ON

LOG ERRORS: ON// <span class="mark">\<Enter\></span>

MULTIPLE ORDERS: <span class="mark">??</span>

Determines when building a HL7 message if message should contain only

one patient/order or multiple patients/orders.

Default is multiple patients per message if possible.

This allows site to configure message building when communicating with

a non-VA system that cannot handle a message that has more than one

patient in the message. It applies to both order (ORM) and result

(ORU) messages.

When communicating with a VA facility this field can be left blank

(default) or set to 0 - MULTIPLE PATIENTS

If the receiving system can only accept one patient per HL7 message

then select 1 - SINGLE PATIENT. This will place multiple orders or

results for multiple orders in one message but only one patient will

be contained in the message.

If the receiving system can only accept one order per HL7 message then

select 2 - SINGLE ORDER. This will place in the message one order or

the results associated with one order for a single patient

> **NOTE:** An order in the VA is considered those tests found on one

accession. What the VA considers as an accession other non-VA systems

may refer to as an order.

Choose from:

0 MULTIPLE PATIENTS

1 SINGLE PATIENT

2 SINGLE ORDER

MULTIPLE ORDERS: <span class="mark">2 \<Enter\></span> SINGLE ORDER

Select ALERT CONDITION: <span class="mark">??</span>

You may enter a new ALERT CONDITION, if you wish

This field allows the user to identify whether to receive alerts when

there are new results and when an error is logged to the ^XTMP global.

Choose from:

1 NEW RESULTS

2 ERROR ON MESSAGE

3 ORDERS RECEIVED

Select ALERT CONDITION: <span class="mark">1 \<Enter\></span> (1 NEW RESULTS)

Are you adding 'NEW RESULTS' as a new ALERT CONDITION (the 1ST for this LA7 ME

SSAGE PARAMETER)? No// <span class="mark">Y \<Enter\></span> (Yes)

MAIL GROUP: <span class="mark">LAB LEDI</span>

Select ALERT CONDITION: <span class="mark">2 \<Enter\></span> (2 ERROR ON MESSAGE)

Are you adding 'ERROR ON MESSAGE' as a new ALERT CONDITION

(the 2ND for this LA7 MESSAGE PARAMETER)? No// <span class="mark">Y \<Enter\></span> (Yes)

MAIL GROUP: <span class="mark">LAB LEDI</span>

Select ALERT CONDITION: <span class="mark">\<Enter\></span>

-----------------------------------------------------------------------------

HOST Lab(s)

----------------------------------------------------------------------------

1\. HOST Lab: QUEST (Uneditable)

2\. Logical Link: LA7VQDI

3\. Message Configuration: LA7V HOST QDI

4\. Auto Instrument: LA7V HOST QDI

Enter a number (1-4): <span class="mark">4</span>

AUTOMATED INSTRUMENT: LA7V HOST QDI

LOAD/WORK LIST: QUEST// <span class="mark">??</span>

This points to the single worklist where processed data from the LA global is to be directed.

Choose from:

This will list available Load/Work lists in your system

LOAD/WORK LIST: QUEST// <span class="mark">\<Enter\></span>

METHOD: <span class="mark">??</span>

This is the name of the method or instrument used.

METHOD: <span class="mark">\<Enter\></span>

DEFAULT ACCESSION AREA: <span class="mark">??</span>

This field contains the default accession list name for this instrument.

Points to FILE \#68.

Choose from:

Lists available accession areas for your system

DEFAULT ACCESSION AREA: <span class="mark">SEND</span>

1 AP SEND SEND OUT

2 SENDOUT HINES

3 SENDOUT MILWAUKEE

4 SENDOUT UW

CHOOSE 1-4: <span class="mark">1 \<Enter\></span> AP SEND OUT

OVERLAY DATA: <span class="mark">??</span>

Setting this field to YES will cause a rerun of instrument data

to overlay existing data.

Choose from:

0 NO

1 YES

OVERLAY DATA: <span class="mark">\<Enter\></span>

STORE REMARKS: YES// <span class="mark">??</span>

This field controls if comments that are associated with an accession

or specimen are stored with the results. The default is NO.

There is a similar companion field at the test level which controls

comments associated with tests results.

Choose from:

0 NO

1 YES

STORE REMARKS: YES// <span class="mark">\<Enter\></span>

Add Chem Tests to the LA7V HOST 676 Automated Instrument for TOMAH VAMC. <span class="mark">\<Enter\></span>

### Step 6: LIM map Micro and/or AP Tests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Map the LEDI Micro and/or AP tests using option ‘Manage MI/AP Test Mappings’ \[LRCAPFF\] located on the ‘National Laboratory File \[LR7O 60-64\]’ menu. The tests need to be mapped to an appropriate NLT code and a Database Code.

> **NOTE:** A report of the mappings can be printed using option ‘Print MI/AP Test Mappings \[LA7VPFL\]’ located on the ‘Lab Shipping Management Menu \[LA7S MGR MENU\]’.

Figure 37. Example of Manage MI/AP Test Mappings

Select LOINC Main Menu Option: <span class="mark">NATIONAL LABORATORY FILE</span>

1 Semi-automatic Linking of file 60 to 64

2 Manual Linking of file 60 to 64

3 Result NLT Auto Linker

4 Link Result NLT Manual

5 Manage MI/AP Test Mappings

Select National Laboratory File Option: <span class="mark">5 \<Enter\></span> Manage MI/AP Test Mappings

Select one of the following:

MI Microbiology

SP Surgical Pathology

CY Cytopathology

EM Electron Microscopy

Choose Lab Area Subscript: <span class="mark">MI \<Enter\></span> Microbiology

Enter Laboratory Test Name: <span class="mark">ANAEROBIC CULTURE</span>

Editing LABORATORY TEST file (#60)

NATIONAL VA LAB CODE: Micro Anerobic Culture// <span class="mark">\<Enter\></span>

60 = ANAEROBIC CULTURE \[553\]

64 = Micro Anerobic Culture (87998.0000) \[2070\]

Link the two entries? No// <span class="mark">Y \<Enter\></span> (Yes)

o----LINKED----o

No Database Code on file for this NLT code.

Select an MI Database Code: <span class="mark">?</span>

Answer with LAB ELECTRONIC CODES SEQUENCE, or NAME, or LOINC ABBR, or

HL7 ABBR, or LAB ABBR, or TYPE

Do you want the entire LAB ELECTRONIC CODES List? <span class="mark">Y \<Enter\></span> (Yes)

Choose from:

9193 MI Bacteria Rpt Date GENERAL BACTERIA RPT DATABASE

9194 MI Gram Stain Rpt Date GENERAL GRAM STAIN DATANAME

9197 MI Parasitology Complete Rpt Date GENERAL PARASITOLOGY RPT DATE

DATANAME

9201 MI Mycology Rpt Date GENERAL MYCOLOGY RPT DATE DATANAME

9205 MI TB Rpt Date GENERAL TB RPT DATE DATANAME

9209 MI Virology Rpt Date GENERAL VIROLOGY RPT DATE DATANAME

Select an MI Database Code: <span class="mark">9193 \<Enter\></span> MI Bacteria Rpt Date GENERAL BACTERIA RPT DATABASE

Update complete.

### Step 7: LIM map code concepts to related area of Lab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The standard code system concepts returned with the result need to be mapped to the related area of the Laboratory package database (Refer to Section 4.3 of the *LEDI IV User Manual*).

Contact the Commercial Reference Laboratory to acquire the result codes used in OBX-3. These codes will need to be mapped locally using option ‘Add/Edit Local Identifier \[LA7V 62.47 LOCAL IDENTIFIER\]’ located on the ‘Lab Code Mapping File \[LA7V 62.47 MENU\]’ menu of the ‘Lab Shipping Management Menu \[LA7S MGR MENU\]’.

Figure 38. Example of Lab Code Mapping File Option

Select Lab Code Mapping File Option: <span class="mark">AEL \<Enter\></span> Add/Edit Local Identifier

Select LAB CODE MAPPING CONCEPT: <span class="mark">SP BRIEF CLINICAL HISTORY \<Enter\></span> SP Brief Clinical History

Select IDENTIFIER: <span class="mark">88541.0000</span>

  Are you adding '88541.0000' as a new IDENTIFIER? No// <span class="mark">Y \<Enter\></span> (Yes)

   IDENTIFIER CODING SYSTEM: 99VA64

IDENTIFIER: 88541.0000// <span class="mark">\<Enter\></span>

CODING SYSTEM: 99VA64// <span class="mark">\<Enter\></span>

PURPOSE: <span class="mark">RESULT \<Enter\></span> RESULT

OVERRIDE CONCEPT: <span class="mark">\<Enter\></span>

RELATED ENTRY: <span class="mark">\<Enter\></span>

MESSAGE CONFIGURATION: <span class="mark">LA7V HOST</span> <span class="mark">QDI</span>

### Step 8: IRM complete the HL7 Environment setup for TCP/IP HL7 transport protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL LOGICAL LINK file (#870) contains the links used by the HL7 software to send messages. This file stores parameters that define the actions of the lower level protocols and information that the Systems Link Monitor uses to provide feedback regarding the status of each link.

1.  Use the ‘Link Edit \[HL EDIT LOGICAL LINKS\]’ option within the ‘Filer and Link Management Options \[HL MENU FILER LINK MGT\]’ menu within the ‘HL7 Main Menu \[HL MAIN MENU\]’ to edit the HL LOGICAL LINK file (#870), AUTOSTART field (#4.5) in the Logical Link Information section.
48. Set the AUTOSTART field (#4.5) to 1 (Enabled), to start the link automatically after TaskMan is restarted.
- If the link is not set to restart automatically, it must be started manually using the ‘Start/Stop Links \[HL START\]’ option within the ‘Filer and Link Management Options \[HL MENU FILER LINK MGT\]’ menu within the ‘HL7 Main Menu \[HL MAIN MENU\]’ menu.
- For VA to commercial Reference laboratory LEDI interfaces, the LEDI IV software uses the standard HL7 TCP listener on port 5000 of the site to receive HL7 messages.

> **NOTE:** For information on single and multi-threaded listeners, refer to the *VistA Health Level Seven (HL7) Site Manager & Developer Manual* under the HL7 section of the VDL.

49. Set up the client device for the Host facility laboratory.  
    The client device is the link that connects to the listener device of the other facility to transmit order messages from a Collecting facility and to transmit result messages from a Host facility.

> **NOTE:** A separate client device must be created for each facility to which LEDI manifests are sent.

Figure 39. Example of Setting up a Client Device

NODE: LA7Vyyy - Where yyy is the commercial reference lab three character identifier specified in the LAB SHIPPING CONFIGURATION file (#62.9)

LLP TYPE: TCP

DEVICE TYPE: Non-Persistent Client

QUEUE SIZE: 10 HL7 package default

RE-TRANSMISSION ATTEMPTS: 5 - pick a reasonable attempt value.

TCP/IP ADDRESS: nnn.nnn.nnn.nnn - IP address of the commercial reference lab system.

TCP/IP PORT: - The port the host lab’s listener device is listening on.

TCP/IP SERVICE TYPE: CLIENT (Sender)

PERSISTENT: NO – unless volume of message traffic dictates a persistent connection.

### Step 9: LIM work with the interface coordinator at the Reference laboratory to test the system

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** If possible, use a mirrored account to test the interface.

To test the system perform the following steps:

1.  Order laboratory test(s) on a test patient.
50. Build the test(s) on a shipping manifest.
51. Close and ship the manifest.
52. Provide the interface coordinator with the manifest number.

> **NOTE:** The interface coordinator must be able to accept the manifest, process orders, and enter test results.

A View Alert is generated at the Collecting facility indicating results are available. The Collecting facility LIM must be able to verify the laboratory test result(s) on the test patient via the ‘EA Enter/verify data (auto instrument)’ option using the Load/ Work List and workload areas created in an earlier step.

### Step 10: LIM train end users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To assist with training end users, review the *LEDI IV Update User Manual*.

This page intentionally left blank for double-sided printing.

# LEDI IV Update AP/MICRO Configuration Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This checklist is provided to ensure that all required LEDI IV Update patch AP/MICRO Interface setup instructions are completed.

## Checklist for a Collecting Facility Setting up a Host Facility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Use this checklist to confirm that the LEDI IV, Collecting Facility Implementation Instructions [Step 4: LIM set up the Lab Shipping Files](#step-4-lim-set-up-the-lab-shipping-files-2), is completed as instructed. (A screen capture example can be seen by selecting the hyperlinked text above.)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th><p>Ensure the name of the Host facility is in the INSTITUTION file (#4), Name field (.01).</p>
<p><strong>Note:</strong> DoD facilities are added by Kernel patch XU*8.0*161. Follow the instructions in the Kernel patch to add DoD facilities to the local INSTITUTION file (#4). Currently, the VAMCs need to locally add non-VistA, non-DoD organizations to the local INSTITUTION file (#4), using the Kernel options to maintain the file.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td>The Institution Master File maintains nationally controlled entries. Currently, the VA Institution Master File maintains entries for VAMC and DoD facilities.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><p>If the Host facility is a VA institution, verify:</p>
<ul>
<li><p>Agency Code field (#95) = <strong>VA</strong></p></li>
<li><p>Station Number field (#99) = A unique Central Office assigned station number.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><p>If the Host facility is a DoD facility, verify:</p>
<p>Agency Code field (#95):</p>
<ul>
<li><p><strong>AF</strong>–Air Force</p></li>
<li><p><strong>ARMY</strong>–Army</p></li>
<li><p><strong>N</strong>–Navy</p></li>
</ul>
<p>Coding System: DMIS ID: 4-digit ID</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><p>If the Host facility is a non-VistA, non-DoD institution, verify:</p>
<ul>
<li><p>Agency Code field (#95) = <strong>Other</strong></p></li>
<li><p>Station Number field (#99) = <strong>&lt;blank&gt;</strong></p></li>
</ul></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>Set up LAB SHIPPING METHOD file (#62.92), using the ‘Edit Shipping Method [LA7S EDIT 62.92]’ option.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>Set up LAB SHIPPING CONDITION file (#62.93), using the ‘Edit Shipping Condition [LA7S EDIT 62.93]’ option.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>Set up LAB SHIPPING CONTAINER file (#62.91), using the ‘Edit Shipping Container [LA7S EDIT 62.91]’ option.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><p>Set up LAB SHIPPING CONFIGURATION (#62.9), using the ‘Edit Shipping Configuration [LA7S EDIT 62.9]’ option.</p>
<ul>
<li><p>When initially setting up the LAB SHIPPING CONFIGURATION file, do not edit the Lab Messaging Link field (#.07).<br />
It is filled in after the ‘LEDI Setup [LA7V SETUP]’ option configures the HL7 interface for the configuration.</p></li>
<li><p>If the Host facility is a non-VA/non-DoD facility, determine a 3-letter identifier to assign in place of the VA Station Number/DoD DMIS ID code.</p></li>
</ul>
<p><strong>Note:</strong> Refer to the examples in Collecting facility, <u>Step 4: LIM set up the Lab Shipping Files</u> for commercial Reference laboratories.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>When setting up an electronic link (HL7 interface) to the Host facility laboratory, use the ‘LEDI Setup [LA7V SETUP]’ option to add/edit a Host facility laboratory.<br />
This option sets up the laboratory and HL7 files for the HL7 interface to the Host facility.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>Map the LEDI Micro and AP tests using option ‘Manage MI/AP Test Mappings’ [LRCAPFF] which establishes the relationships between the LABORATORY TEST (#60), the WKLD CODE (#64) and the LAB ELECTRONIC CODES (#64.061) files for LEDI MI/AP tests. Coordinate this information with the Host facility, which must match the Collecting facility MI/AP mappings.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>If using the HL7 TCP/IP communication protocol, the IRM must complete the HL LOGICAL LINK file (#870) setup, using the HL package ‘Link Edit [HL EDIT LOGICAL LINKS]’ option to edit a logical link when communicating with non-VA facilities.<br />
When setting up LEDI between VA facilities, the standard HL7 VAxxx logical links are utilized.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><p>If an electronic link (HL7 interface) is setup for the Host facility, use the ‘Edit Shipping Configuration [LA7S EDIT 62.9]’ option to edit the Lab Messaging Link field (#.07) to link the shipping configuration to the HL7 interface.</p>
<ul>
<li><p>Select the message configuration <strong>LA7V HOST xxx</strong> (such as, xxx is the VA station number of the Host facility, the 4-digit DMIS ID of DoD facilities, or the three-letter identifier previously assigned for a non-VA, non-DoD facility).</p></li>
<li><p>The ‘LEDI Setup [LA7V SETUP]’ option attempts to fill in this field. However, if there are multiple shipping configurations for the same Collecting and Host facilities, you must manually setup these configurations.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>If an electronic link (HL7 interface) is setup for the Host facility, use the ‘Edit Susceptibility [LA7V 62.47 EDIT SUSC]’ option to link local Antimicrobial Susceptibility to the result codes used by the Reference laboratory to report antibiotic susceptibilities.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>If an electronic link (HL7 interface) is setup for this Host facility and it is a DoD, use the ‘Initialize DOD Codes [LA7V 62.47 ADD DOD]’ option to populate the LAB CODE MAPPING file (#62.47) with the standard DoD local codes.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>If an electronic link (HL7 interface) is setup for the Host facility, use the ‘Add/Edit Local Identifier [LA7V 62.47 LOCAL IDENTIFIER]’ option to map Host local result codes for microbiology and anatomic pathology.</td>
</tr>
</tbody>
</table>

## Checklist for a Host Facility Setting Up a Collecting Facility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Use this checklist to confirm that the LEDI IV, Host Facility Implementation Instructions, Step 4: LIM must set up the Host facility LAB SHIPPING CONFIGURATION file (#62.9).

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th><p>Ensure the Collecting facility is configured in the INSTITUTION file (#4).</p>
<p>The Institution Master File maintains nationally controlled entries.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><p>If the Collecting facility is a VA institution, verify:</p>
<ul>
<li><p>Agency Code field (#95) = <strong>VA</strong></p></li>
<li><p>Station Number field (#99) = Unique Central Office assigned station number.</p></li>
</ul></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><p>If the Collecting facility is a DoD facility, verify:</p>
<p>Agency Code field (#95):</p>
<ul>
<li><p><strong>AF</strong>–Air Force</p></li>
<li><p><strong>ARMY</strong>–Army</p></li>
<li><p><strong>N</strong>–Navy</p></li>
</ul>
<p>Coding System: DMIS ID: 4-digit ID</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><p>If the Collecting facility is a non-VistA, non-DoD institution, verify:</p>
<ul>
<li><p>Agency Code field (#95) = <strong>Other</strong></p></li>
<li><p>Station Number field (#99) = <strong>&lt;blank&gt;</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><p>Set up the SHIPPING CONFIGURATION file (#62.9), using the ‘Edit Shipping Configuration [LA7S EDIT 62.9]’ option.</p>
<p>When asked how the configuration is edited, specify <strong>Host facility</strong>.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>Add local lab tests that the Collecting facility is shipping, specifying local collection sample with urgency to build the LAB PENDING ORDERS ENTRY file (#69.6) entries.<br />
If the Collecting facility is a non-VA facility, determine a 3-letter identifier to assign in place of the VA Station Number.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>Map the LEDI Micro and AP tests using option ‘Manage MI/AP Test Mappings’ [LRCAPFF], which establishes the relationships between the LABORATORY TEST (#60), the WKLD CODE (#64) and the LAB ELECTRONIC CODES (#64.061) files for LEDI MI/AP tests. Coordinate the MI/AP mappings with the Collecting facility, which must match the Host facility mappings.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>If setting up an electronic link (HL7 interface) to the Collecting laboratory, use the ‘LEDI Setup [LA7V SETUP]’ option to add/edit a Collecting laboratory. This option sets up the laboratory and HL7 files for the HL7 interface to the Collecting facility.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>If using the HL7 TCP/IP interface, the IRM must complete the HL LOGICAL LINK file (#870) setup, using the HL package ‘Link Edit [HL EDIT LOGICAL LINKS]’ option to edit a logical link when communicating with non-VA facilities. When setting up LEDI between VA facilities, the standard HL7 VAxxx logical links are utilized.</td>
</tr>
</tbody>
</table>

This page intentionally left blank for double-sided printing.

# Appendix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Message Validation and Creating Order-MICRO

- The Host system’s Shipping Configuration does not need to be configured with a specimen and host collection sample.
- The incoming order must match what is configured in the Host system’s Shipping Configuration for the TEST/PROFILE entry. However, the specimen and collection sample codes do not have to match.
- In general the system will use the Laboratory Test, Specimen (Topography) and Host Collection Sample that were configured on the shipping configuration when creating the order at the Host site (if they were defined).

Exceptions

- If the entry in the Host’s shipping configuration was not configured with a Specimen (or the specimen on the shipping configuration had a different SNOMED CT ID (SCT ID) than the message) AND the message coded the specimen using the SCT coding system, then the system will try to find an entry in Topography Field file (#61) that is mapped to the SCT ID from the message. The system will use that entry when creating the order.
- If the entry in the Host’s shipping configuration was not configured with a Specimen AND the message coded the specimen using the HL7 specimen code, then the system will try to find an entry in file \#61 that is mapped to the HL7 specimen code from the message. The system will use that entry when creating the order.
- If the LEDI HL7 code was “Other” or “Another message part”, the system will prompt the user at the Host site to update the specimen and collection samples when accessioning the referral order via option “Referral Patient Multi-purpose Accession”.

Figure 40. Example of Referral Patient Multi-purpose Accession

Collecting site order comments:

For test CULTURE & SUSCEPTIBILITY

Specimen source: Other \[ORH:HL70070\] ; LIVING ORGANISM, NOS \[8821:99VA61\]

Collection sample: Biopsy sample (specimen) \[258415003:SCT\] ; BIOPSY \[26:99VA62\]

<span class="mark">Update missing order information for:</span>

<span class="mark">SPECIMEN: LIVING ORGANISM UNKNOWN//</span>

<span class="mark">COLLECTION SAMPLE: BIOPSY//</span>

- If a matching specimen cannot be found at the Host site (and the message did not code the specimen using the SCT coding system), the system will prompt the user at the Host site to enter the specimen when accessioning the referral order via option “Referral Patient Multi-Purpose Accession”.

Figure 41. Example of Referral Patient Multi-Purpose Accession

Collecting site order comments:

For test CULTURE & SUSCEPTIBILITY

Specimen source: LIVING ORGANISM, NOS \[8821:99VA61\]

Collection sample: Biopsy sample (specimen) \[258415003:SCT\] ; BIOPSY \[26:99VA62\]

<span class="mark">Update missing order information for:</span>

<span class="mark">SPECIMEN:</span>

- If the entry in the shipping configuration was not configured with a Host Collection Sample (or the collection sample on the shipping configuration had a different SCT ID than the message) AND the message coded the collection sample using the SCT coding system, then the system will try to find an entry in file \#62 that is mapped to the SCT ID from the message. The system will use that entry when creating the order.  
  If no existing entry is found, the system will automatically create a new entry in \#62 based off the SCT information from the message.
- If a matching Collection Sample cannot be found (and the message did not code the collection sample using the SCT coding system), the system will prompt the user at the Host site to enter the collection sample when accessioning the referral order via option “Referral Patient Multi-Purpose Accession”.

Figure 42. Example of Referral Patient Multi-Purpose Accession

Collecting site order comments:

For test CULTURE & SUSCEPTIBILITY

Specimen source: Other \[ORH:HL70070\] ; LIVING ORGANISM, NOS \[8821:99VA61\]

Collection sample: BIOPSY \[26:99VA62\]

<span class="mark">Update missing order information for:</span>

<span class="mark">COLLECTION SAMPLE:</span>

Message Validation and Creating Order-AP

Note 1: The user may have potential issues with the SNOMED CT Mapping between the Collecting and Host sites. Therefore, ensure that the Collection Sample File (#62) topography mapping matches exactly between the two sites.

Note 2: If any collections sample does not map to a SNOMED SCT, it will not be able to be used with the LEDI manifest system. Ensure that the Collection Sample used is mapped to a SNOMED CT.

- The Host system’s Shipping Configuration must be configured with a Host collection sample, but does not need to be configured with a specimen.
- The lab order from the collecting site must match what is configured in the LAB SHIPPING CONFIGURATION File (#62.9) for the TEST/PROFILE lab test and the HOST COLLECTION SAMPLE entry.  
  If a specimen was defined in the shipping configuration or if the Collection Sample File (#62) entry has a DEFAULT SPECIMEN defined, then the specimen codes must match as well.  
  However, it is acceptable if the specimen was not defined in the Host Shipping Configuration as long as the Test/Profile and the Host Collection Sample entries match.
- In general, the system will use the Laboratory Test, Specimen (Topography) and Host Collection Sample that were configured on the shipping configuration when creating the order at the Host site.

Exceptions

- If the entry in the Host’s shipping configuration was not configured with a Specimen (or the specimen on the shipping configuration had a different SCT ID than the message) AND the message coded the specimen using the SCT coding system, then the system will try to find an entry in Topography Field file (#61) that is mapped to the SCT ID from the message, and will use that entry when creating the order.  
  If no existing entry is found, the system will automatically create a new entry in Topography Field file (#61) based off the SCT information from the message for AP.
- If the entry in the Host’s shipping configuration was not configured with a Specimen AND the message coded the specimen using the HL7 specimen code, then the system will try to find an entry in Topography Field file (#61) that is mapped to the HL7 specimen code set from the message, and will use that entry when creating the order.
- If the entry in the Host’s shipping configuration was not configured with a Specimen AND the message did not code the specimen using the SCT coding system AND a match was not found using the HL7 specimen code, then the system will use the first entry in Topography Field file (#61) that it finds is mapped to the HL7 specimen code XXX - “Another message part”.