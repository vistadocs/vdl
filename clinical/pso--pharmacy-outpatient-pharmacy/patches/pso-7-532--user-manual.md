---
title: PSO*7*532 One VA Pharmacy User Guide
doc_type: UG
doc_label: User Guide
doc_layer: patch
doc_subject: One VA Pharmacy
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*532
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 2
description: 
audience: 
keywords: 
  - pharmacy
  - oneva
  - prescription
  - table
  - patient
  - contents
  - vista
  - prescriptions
  - report
  - message
page_count: 0
word_count: 11207
section_count: 16
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_0_p532_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_0_p532_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Outpatient Pharmacy

  OneVA Pharmacy

  User Guide
---

![](pso-7-532-one-va-pharmacy-user-guide/001.png)

December 1997

(Revised February 2019)

Office of Information and Technology (OIT)

Enterprise Program Management Office

Revision History

When updates occur, the Title Page lists the new revised date and this page describes the changes. Bookmarks link the described content changes to its place within manual. There are no bookmarks for format updates. Page numbers change with each update; therefore, they are not included as a reference in the Revision History.

<table>
<caption><p>Table : Documentation Symbols and Descriptions</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 18%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Patch Number</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>02/2019</td>
<td>PSO*7*532</td>
<td><p>Changed the <a href="#PSO_7_532">System Message under Use Case: Dispense Order from another VA Pharmacy Location</a></p>
<p>Replaced <a href="\l">“Steps to Turn on ONEVA PHARMACY FLAG (#101)” with “Pharmacy System Parameters Edit”.</a></p>
<p>Updated references of ONEVA PHARMACY FLAG (#3001) to (#101) throughout.</p>
<p>Updated references of Outpatient Site file (#59) to PHARMACY SYSTEM File (#59.7) throughout.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>05/2017</td>
<td>PSO*7*479</td>
<td><p>Modifies the prompt to the user when printing a OneVA Pharmacy label. (pg. ii, <a href="#p14">14</a>, <a href="#p26">26</a>, <a href="#p27">27</a>, and <a href="#p30">30</a>)</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>11/2016</td>
<td>PSO*7*454</td>
<td>Initial Issue</td>
</tr>
</tbody>
</table>

Table : Documentation Symbols and Descriptions

Table of Contents

1\. Introduction [1](#introduction)

1.1. Purpose [1](#purpose)

1.2. Document Orientation [1](#document-orientation)

1.2.1. Organization of the Manual [1](#organization-of-the-manual)

1.2.2. Assumptions [1](#assumptions)

1.2.3. Coordination [2](#coordination)

1.2.4. Disclaimers [2](#disclaimers)

1.2.4.1. Software Disclaimer [2](#software-disclaimer)

1.2.4.2. Documentation Disclaimer [2](#documentation-disclaimer)

1.2.5. Documentation Conventions [2](#documentation-conventions)

1.2.6. References and Resources [3](#references-and-resources)

1.3. National Service Desk and Organizational Contacts [3](#national-service-desk-and-organizational-contacts)

2\. System Summary [5](#system-summary)

2.1. System Configuration [6](#system-configuration)

2.1.1. Host Site OneVA Pharmacy Flag Not Set On Message [7](#host-site-oneva-pharmacy-flag-not-set-on-message)

2.1.2. Pharmacy System Parameters Edit \[PSS SYS EDIT\] [7](#pharmacy-system-parameters-edit-pss-sys-edit)

2.2. Data Flows [8](#data-flows)

2.2.1. Use Case: View Orders [8](#use-case-view-orders)

2.2.2. Use Case: Dispense Order from another VA Pharmacy Location [10](#use-case-dispense-order-from-another-va-pharmacy-location)

2.2.3. Use Case: OneVA Pharmacy Prescription Report [12](#use-case-oneva-pharmacy-prescription-report)

2.3. User Access Levels [13](#user-access-levels)

2.4. Continuity of Operation [13](#continuity-of-operation)

2.4.1. New OneVA Pharmacy Checking for Prescriptions Message [13](#new-oneva-pharmacy-checking-for-prescriptions-message)

2.4.2. New OneVA Pharmacy System Down or Not Responding Message [14](#new-oneva-pharmacy-system-down-or-not-responding-message)

2.4.3. OneVA Pharmacy Patient Found No Rxs Informational Message [14](#oneva-pharmacy-patient-found-no-rxs-informational-message)

3\. Getting Started [14](#getting-started)

3.1. Logging On [14](#logging-on)

3.2. System Menu [14](#system-menu)

3.3. Changing User ID and Password [15](#changing-user-id-and-password)

3.4. Exit System [15](#exit-system)

3.5. Caveats and Exceptions [15](#caveats-and-exceptions)

3.5.1. Label Reprinting [15](#label-reprinting)

3.5.2. Target VistA Time Out Awaiting Reply Message [15](#target-vista-time-out-awaiting-reply-message)

3.5.3. Host Site OneVA Pharmacy Flag Not Set On [15](#host-site-oneva-pharmacy-flag-not-set-on)

4\. Using the Software [16](#using-the-software)

4.1. Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\] [16](#patient-prescription-processing-pso-lm-backdoor-orders)

4.1.1. Selecting a Patient [16](#selecting-a-patient)

4.1.2. View Order Rxs from other VA Pharmacy Locations [16](#view-order-rxs-from-other-va-pharmacy-locations)

4.1.3. Patient Information View [18](#patient-information-view)

4.1.4. Medication Profile View [18](#medication-profile-view)

4.1.4.1. Medication Profile View Example with ‘Non-VA MEDS’ [21](#medication-profile-view-example-with-non-va-meds)

4.1.5. Dispense (Local) Order Originating from Dispensing (Local) Site [22](#dispense-local-order-originating-from-dispensing-local-site)

4.1.6. Dispense Rx Order from another VA Pharmacy Location [22](#dispense-rx-order-from-another-va-pharmacy-location)

4.1.6.1. Refill Prescription Order [24](#refill-prescription-order)

4.1.6.2. Partial Fill Prescription Order [26](#partial-fill-prescription-order)

4.1.6.3. Drug Matching Process [29](#drug-matching-process)

4.1.6.3.1. Drug Matching: One-to-One [29](#drug-matching-one-to-one)

4.1.6.3.2. Drug Matching: One-to-Many [30](#drug-matching-one-to-many)

4.1.6.3.3. Drug Matching: No Drug Match [31](#drug-matching-no-drug-match)

4.1.6.3.4. Drug Matching: Exception Messages [31](#drug-matching-exception-messages)

4.2. OneVA Pharmacy Prescription Report \[PSO REMOTE RX REPORT [32](#oneva-pharmacy-prescription-report-pso-remote-rx-report)

4.2.1. OneVA Pharmacy Report Menu [32](#oneva-pharmacy-report-menu)

4.2.2. Accessing OneVA Pharmacy Reports [33](#accessing-oneva-pharmacy-reports)

4.2.2.1. Selecting a Report and Report Search Options [33](#selecting-a-report-and-report-search-options)

4.2.2.2. Search Option D – DATE RANGE [34](#search-option-d-date-range)

4.2.2.3. Search Option P – PATIENT [35](#search-option-p-patient)

4.2.2.4. Search Option S – SITE [36](#search-option-s-site)

4.2.3. OneVA Pharmacy Report Content [38](#oneva-pharmacy-report-content)

5\. Troubleshooting [39](#troubleshooting)

5.1. Special Instructions for Error Correction [40](#special-instructions-for-error-correction)

6\. Acronyms and Abbreviations [40](#acronyms-and-abbreviations)

7\. Appendix [42](#appendix)

A. Frequently Asked Questions (FAQ) [42](#frequently-asked-questions-faq)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Document Orientation](#document-orientation)
    - [Organization of the Manual](#organization-of-the-manual)
    - [Assumptions](#assumptions)
    - [Coordination](#coordination)
    - [Disclaimers](#disclaimers)
    - [Documentation Conventions](#documentation-conventions)
    - [References and Resources](#references-and-resources)
  - [National Service Desk and Organizational Contacts](#national-service-desk-and-organizational-contacts)
- [System Summary](#system-summary)
  - [System Configuration](#system-configuration)
    - [Host Site OneVA Pharmacy Flag Not Set on Message](#host-site-oneva-pharmacy-flag-not-set-on-message)
    - [Pharmacy System Parameters Edit \[PSS SYS EDIT\]](#pharmacy-system-parameters-edit-pss-sys-edit)
  - [Data Flows](#data-flows)
    - [Use Case: View Orders](#use-case-view-orders)
    - [Use Case: Dispense Order from another VA Pharmacy Location](#use-case-dispense-order-from-another-va-pharmacy-location)
    - [Use Case: OneVA Pharmacy Prescription Report](#use-case-oneva-pharmacy-prescription-report)
  - [User Access Levels](#user-access-levels)
  - [Continuity of Operation](#continuity-of-operation)
    - [New OneVA Pharmacy Checking for Prescriptions Message](#new-oneva-pharmacy-checking-for-prescriptions-message)
    - [New OneVA Pharmacy System Down or Not Responding Message](#new-oneva-pharmacy-system-down-or-not-responding-message)
    - [OneVA Pharmacy Patient Found No Rxs Informational Message](#oneva-pharmacy-patient-found-no-rxs-informational-message)
- [Getting Started](#getting-started)
  - [Logging On](#logging-on)
  - [System Menu](#system-menu)
  - [Changing User ID and Password](#changing-user-id-and-password)
  - [Exit System](#exit-system)
  - [Caveats and Exceptions](#caveats-and-exceptions)
    - [Label Reprinting](#label-reprinting)
    - [Target VistA Time Out Awaiting Reply Message](#target-vista-time-out-awaiting-reply-message)
    - [Host Site OneVA Pharmacy Flag Not Set On](#host-site-oneva-pharmacy-flag-not-set-on)
- [Using the Software](#using-the-software)
  - [Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\]](#patient-prescription-processing-pso-lm-backdoor-orders)
    - [Selecting a Patient](#selecting-a-patient)
    - [View Order Rxs from other VA Pharmacy Locations](#view-order-rxs-from-other-va-pharmacy-locations)
    - [Patient Information View](#patient-information-view)
    - [Medication Profile View](#medication-profile-view)
    - [Dispense (Local) Order Originating from Dispensing (Local) Site](#dispense-local-order-originating-from-dispensing-local-site)
    - [Dispense Rx Order from another VA Pharmacy Location](#dispense-rx-order-from-another-va-pharmacy-location)
  - [OneVA Pharmacy Prescription Report \[PSO REMOTE RX REPORT](#oneva-pharmacy-prescription-report-pso-remote-rx-report)
    - [OneVA Pharmacy Report Menu](#oneva-pharmacy-report-menu)
    - [Accessing OneVA Pharmacy Reports](#accessing-oneva-pharmacy-reports)
    - [OneVA Pharmacy Report Content](#oneva-pharmacy-report-content)
- [Troubleshooting](#troubleshooting)
  - [Special Instructions for Error Correction](#special-instructions-for-error-correction)
- [Acronyms and Abbreviations](#acronyms-and-abbreviations)
- [Appendix](#appendix)
- [Frequently Asked Questions (FAQ)](#frequently-asked-questions-faq)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of the OneVA Pharmacy User Manual is to describe the new capability that will allow a Pharmacist from any VA Pharmacy location to refill or partial a patient’s prescription that originated from another VA Pharmacy location, contingent on the host site status where the prescription originated.

In addition, this User Manual will provide instructions on how to obtain the details of the prescriptions dispensed by another VA Pharmacy location by introducing the new OneVA Pharmacy report menu.

Lastly, Frequently Asked Questions (FAQs) are addressed regarding the new OneVA Pharmacy capabilities and limitations.

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Organization of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OneVA Pharmacy User Manual contains the following sections:

- ‘Introduction’ section that includes the assumed experience and skill level a user will have in order to use the software patch and provides the specifics related to the support of the software. This section also lists the references, resources, documentation conventions, disclaimers, and the organization of the manual.
- ‘System Summary’ section that includes the system configuration steps necessary to turn on the OneVA Pharmacy software and the data flow diagrams for the View Orders, Dispense Order from another VA Pharmacy Location, and OneVA Pharmacy Prescription Report Use Cases. This section also lists specific messages for the user regarding continuity of operation.
- ‘Getting Started’ section provides the overview of logging into the system, introduces the system menu, and lists the caveats and exceptions for this software patch.
- ‘Using the Software’ section provides the detailed steps for using the OneVA Pharmacy capability within both the ‘PATIENT PRESCRIPTION PROCESSING \[PSO LM BACKDOOR ORDERS\]’ and the ‘ONEVA PHARMACY PRESCRIPTION REPORT \[PSO REMOTE RX REPORT\]’ menus.
- ‘Troubleshooting’ section includes common system messages and actions to take if a significant error occurs.
- ‘Acronyms and Abbreviation’ section lists all acronyms and abbreviations used throughout this document.
- ‘Appendix’ details the Frequently Asked Questions (FAQs) associated with the new capabilities and provides the programs limitations.

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OneVA Pharmacy User Manual assumes the user has the following experience/skills:

- User has basic knowledge of the Veterans Health Information Systems and Technology Architecture (VistA) system (such as the use of commands, menu options, and navigation tools).
- User has access to the ‘Rx (PRESCRIPTIONS) \[PSO RX\]’ menu within VistA and holds appropriate security keys for their user role, such as PSORPH, to identify the user as a Pharmacist.
- User has completed any prerequisite training.

### Coordination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veterans Affairs Medical Center (VAMC) VistA Coordinator responsible for the implementation of OneVA Pharmacy patch will address the ability of Pharmacists to fulfill non-controlled substance prescriptions from any VA Pharmacy location where a prescription originated at another VA Pharmacy site.

The Audience for this User Manual is the Pharmacist and anyone else eligible to fulfill prescriptions (non-controlled).

The OneVA Pharmacy Implementation Manager and the Implementation team will coordinate with the Regional VistA Services teams for a National Rollout using a phased approach. As part of the distribution and installation of the OneVA Pharmacy patch, the deployment will include a checklist to confirm that the site connects to VAs Enterprise Messaging Infrastructure (eMI) Enterprise Service Bus (ESB) located in the Austin Information Technology Center (AITC).

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

Employees of the Federal Government in the course of their official duties developed this software at the Department of Veterans Affairs (VA). Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely if any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the VA of this Web site or the information, products, or services contained therein. VA does not exercise any editorial control over the information found at these locations. Such links are consistent with the stated purpose of VA.

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All patient data displayed on screen images within this document consists of mocked up test data therefore there is no concern regarding misuse or violation of Personally Identifiable Information (PII) as defined in Office of Management and Budget (OMB) Memorandum M-07-1616.

Various symbols used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols.

| Symbol                                                                                                                                                                                                                                     | Description                                                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![](pso-7-532-one-va-pharmacy-user-guide/002.png)                  | NOTE: Used to inform the reader of general information including references to additional reading material |
| ![](pso-7-532-one-va-pharmacy-user-guide/003.png) | CAUTION: Used to caution the reader to take special notice of critical information                         |

Table : OneVA Pharmacy Support Entities

### References and Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

References and resources for the OneVA Pharmacy patch available on the VA Software Document Library (VDL) and are as follows:

- [Pharm: Outpatient Pharmacy: Technical Manual/Security Guide](http://www.va.gov/vdl/application.asp?appid=90)
- [OneVA Pharmacy Release Notes: provides an overview of features and functions that are new with this patch.](http://www.va.gov/vdl/application.asp?appid=90)
- 
- Pharm: Outpatient Pharmacy: Deployment, Installation, Rollback, and Back-out Plan - provides information necessary to install the software.[Pharm: Outpatient Pharmacy: User Manual – Manager: includes the processing and functions for the Manager.](http://www.va.gov/vdl/application.asp?appid=90)
- 
- Pharm: Outpatient Pharmacy: User Manual – Pharmacist Menu: includes the processing and functions for the Pharmacist.[Pharm: Outpatient Pharmacy: User Manual – Supplemental: includes information about the OneVA Pharmacy label printing.](http://www.va.gov/vdl/application.asp?appid=90)
- 

Pharm: Outpatient Pharmacy: User Manual – Technician: includes the processing and functions for the Technician.OneVA Pharmacy training videos are available and can be found by following these links:

> Training Video – View Order Use Case

> <span class="mark">REDACTED</span>

> Training Video - Dispense Order From Another Location

> <span class="mark">REDACTED</span>

## National Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists the Operational Tier 1 through Tier 5 Support resources for the OneVA Pharmacy VistA patch including the National Service Desk (NSD), Regional Application Service Line, Clinical Product Support team, OneVA Pharmacy Development team, and VistA maintenance support team.

![](pso-7-532-one-va-pharmacy-user-guide/004.png)The support entities listed in the following table does not include support for the integration areas that are part of the OneVA Pharmacy software but not part of the OneVA Pharmacy patch. Not included is support for eMI ESB, HL7, nor for the HDR/CDS Repository.

| Name                                                              | Role                                                                                                                                                                                                                                                   | Gov or non-Gov | FTE                                     | Org                     | Contact Info                       |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|-----------------------------------------|-------------------------|------------------------------------|
| Tier 1: National Service Desk                                     | NSD Tier 1 Support                                                                                                                                                                                                                                     | Gov            | No change to existing VistA support FTE | NSD                     | <span class="mark">REDACTED</span> |
| Tier 2: National Service Desk                                     | NSD Tier 1 Support                                                                                                                                                                                                                                     | Gov            | No change to existing VistA support FTE | NSD                     | <span class="mark">REDACTED</span> |
| Tier 3: Regional Application Service Line                         | Install Patch – Tier 3                                                                                                                                                                                                                                 | Gov            | No change to existing VistA support FTE | OI&T Field Operations   | <span class="mark">REDACTED</span> |
| Tier 4: EPMO – Clinical Product Support Team – Clin 1             | Clin 1 Support/Provider Systems                                                                                                                                                                                                                        | Gov            | No change to existing VistA support FTE | EPMO, OI&T              | <span class="mark">REDACTED</span> |
| Tier 5: Development Team for first 30-days after National Release | Support defect fixing if identified after National Release. The development team is responsible for development and release of all fix patches for defects occurring with the first 30-days of release.                                                | Non-Gov        | No change to existing VistA support FTE | VHA Innovations Program | <span class="mark">REDACTED</span> |
| Tier 5: VistA Maintenance Team subsequent to first 30-days        | Support defect fixing if identified 30-days after National Release. The VistA Maintenance team is an existing long-term team that works closely with application services line representatives to implement patches beyond the 30-day warranty period. | Non-Gov        | No change to existing VistA support FTE | EPMO, OI&T              | <span class="mark">REDACTED</span> |

Table Acronym & Abbreviation Table

# System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OneVA Pharmacy software provides the Department of Veterans Health Administration (VHA) the capability to allow Veterans traveling across the United States to refill or partial their active VA non-controlled substance prescriptions at any VA Pharmacy location regardless of where the prescription originated. The patch expands available pharmacy information in VistA to Pharmacists, providing direct access to any active and refillable prescription from any VA Pharmacy location.

OneVA Pharmacy software provides a foundation to build and extend new capabilities to the Veteran.

Patch PSO\*7.0\*454 is being released to enhance VistA’s “Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\]” menu (found within the VistA Pharmacy Outpatient Pharmacy package). The OneVA Pharmacy patch will allow the Pharmacist to query for and refill patient’s active and refillable prescriptions from other VA Pharmacy VistA instances.

The overall OneVA Pharmacy software design has several components. They are:

1.  Veterans Health Information Systems and Technology Architecture (VistA) (Patch PSO\*7.0\*454)
2.  Health Level 7 (HL7) Messaging
3.  Enterprise Messaging Infrastructure (eMI) Enterprise Service Bus (ESB)
4.  Health Data Repository/Clinical Data Service (HDR/CDS) Repository

VistA is the user interface where a pharmacist uses the “Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\]” menu (found within the VistA Pharmacy Outpatient Pharmacy package) to query for and refill patient’s active and refillable prescriptions from other VA Pharmacy VistA instances. Patch PSO\*7.0\*454 uses Health Level 7 (HL7) messaging to query and receive remote prescription details to and from the Health Data Repository/Clinical Data Services (HDR/CDS) Oracle Repository.

The VistA instance where the Veteran is requesting the refill or partial is considered the ‘dispensing’ VistA instance. This patch allows a Pharmacist, using a ‘dispensing’ VistA instance, to refill or partial prescription that originated from another VA Pharmacy VistA instance and print a prescription label. The VA Pharmacy VistA instance where the prescription originated and currently exists is the ‘host’ VistA instance. The host VistA instance is where the update to the prescription record is made once the fill is processed. The label data elements are extracted from the host VistA instance and returned to the dispensing site via HL7 creating the OneVA Pharmacy label. The bar code on the label will be valid at the host site but not at the dispensing site.

The OneVA Pharmacy patch sends the HL7 query message through the Enterprise Service Bus (ESB) Enterprise Messaging Services (eMI). eMI executes a Web Service call to query the HDR/CDS Repository for specific medication information obtained from all VA Pharmacy’s VistA sites. The eMI configuration contains filtering processes that applies specific business rules against the HDR/CDS Web Service call to return the appropriate prescriptions to the dispensing VistA. VistA and eMI communicate using HL7 v2.5.1 over Minimal Layer Protocol (MLLP). Communication to the HDR/CDS Repository takes place via Simple Object Access Protocol (SOAP) Web Services.

The medication data elements return to the dispensing site via HL7 messaging. Once the prescriptions arrive at the dispensing site, they display below any 'local' prescriptions on the Medication Profile view. The prescriptions displayed to the Pharmacist sort by VA Pharmacy site and status. The dispensing Pharmacist can view the remote prescriptions and select one to refill or partially fill. For label printing, VistA triggers the HL7 message stream that executes during the refill or partial fill prescription processes. The host label data elements are returned to the dispensing site within the HL7 segment. The event triggers the Pharmacist to select the dispensing sites printing device to print a host label.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To use OneVA Pharmacy, the user turns on the ‘ONEVA PHARMACY FLAG (#101)’. The 'ONEVA PHARMACY FLAG (#101)’ is located on the ‘PHARMACY SYSTEM File (#59.7)’ file. This field will allow each division to toggle the OneVA Pharmacy logic 'on' or 'off' depending on current needs. The user changes the field by using ‘FILEMAN \[FM\]’ and editing the 'ONEVA PHARMACY FLAG (#101)’ field. The software patch delivers the ‘ONEVA PHARMACY FLAG (#101)’ in the 'off' state. When this flag is in the 'off' state, the HDR/CDS Repository is not queried for external prescriptions and other VistA instances will not be able to refill prescriptions that belong to the VistA instance with the flag set to the 'off' state. When in the 'on' state, all prescription queries and actions may be taken for remote queries, refills, and partial fills. In order to process prescriptions from another VistA instance, that instance will also need to have its ‘ONEVA PHARMACY FLAG (#101)’ set to the 'on' state.

### Host Site OneVA Pharmacy Flag Not Set on Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the ‘ONEVA PHARMACY FLAG (#101)’ is not set to the ‘on’ state at the host site, the dispensing site will receive the following message:

> *The OneVA Pharmacy flag is turned ‘OFF’ at this facility. Unable to process refill/partial fill requests. Queries will NOT be made to other VA Pharmacy locations.*

### Pharmacy System Parameters Edit \[PSS SYS EDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Pharmacy System Parameters Edit* \[PSS SYS EDIT\] option allows the user to edit the Pharmacy System Parameters used in PDM.

Example: *Pharmacy System Parameters Edit* \[PSS SYS EDIT\] Option

> Select Pharmacy Data Management Option: Pharmacy System Parameters Edit

> PMIS PRINTER: LASSIE PRINTER HALLWAY

> PMIS LANGUAGE: ?

> This language will be used as the default for the printing of Patient

> Medication Instruction Sheets (PMIS).

> Choose from:

> 1 English

> 2 Spanish

> PMIS LANGUAGE: 1 English

> WARNING LABEL SOURCE: ?

> Enter "N" for NEW to use commercial data source for warning labels.

> Choose from:

> N NEW

> WARNING LABEL SOURCE: N NEW

> CMOP WARNING LABEL SOURCE: ?

> Enter "N" for NEW to use commercial data source for CMOP warning labels.

> Choose from:

> N NEW

> CMOP WARNING LABEL SOURCE: N NEW

> OPAI WARNING LABEL SOURCE: ?

> Enter "N" for NEW to use commercial data source for OPAI warning labels.

> Choose from:

> N NEW

> OPAI WARNING LABEL SOURCE: N NEW

> AUTOMATE CPRS REFILL: ?

> Enter Y to process CPRS refills automatically or N to process manually in

> Pharmacy backdoor.

> Choose from:

> 0 NO

> 1 YES

> AUTOMATE CPRS REFILL: NO//

> ONEVA PHARMACY FLAG: ?

> Select '1' to turn on the OneVA Pharmacy remote prescription logic. Select

> '0' to turn it off.

> Choose from:

> 1 ON

> 0 OFF

> ONEVA PHARMACY FLAG:

> Select Pharmacy Data Management Option:

A new field, ONEVA PHARMACY FLAG (#101) was created in the PHARMACY SYSTEM File (#59.7) with Patch PSO\*7\*497. This field will allow sites to toggle the OneVA Pharmacy logic 'on' or 'off' depending on current needs. The user changes the field value by using the *Pharmacy System Parameters Edit* \[PSS SYS EDIT\] Option

Patch PSS\*1\*212 delivered the ONEVA PHARMACY FLAG field in the 'off' state. When this flag is in the 'off' state, the HDR/CDS Repository is not queried for external prescriptions and other VistA instances will not be able to refill prescriptions that belong to the VistA instance with the flag set to the 'off' state. When in the 'on' state, all prescription queries and actions may be taken for remote queries, refills, and partial fills. In order to process prescriptions from another VistA instance, that instance will also need to have its ‘ONEVA PHARMACY FLAG set to the 'on' state.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th>![](pso-7-532-one-va-pharmacy-user-guide/005.png)</th>
<th><p><strong>*Important*</strong></p>
<p>DO NOT turn on the OneVA Pharmacy Flag until directed to do so. The software will be released, deployed, and installed with the activation flag set to the “off” position. The Existing Product Intake Program (EPIP) Implementation Team will coordinate with the sites Pharmacy Automatic Data Processing Application Coordinator (ADPAC) on the specific date in which to activate the software.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Use Case: View Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the Pharmacist enters a request to display the Medication Profile view from a dispensing VistA instance, a query message is sent to eMI. eMI will harvest the necessary information to send a request to the HDR/CDS Repository for the patient’s prescriptions. The response is transformed into another message that contains the patient’s prescription data. The patient’s prescription data is returned to the dispensing VistA instance and displayed on the Medication Profile screen on VistA. This process is refered to as the OneVA Pharmacy View Orders Use Case.

The ‘View Orders’ Use Case describes the process for users to view all of a patient’s active, suspended, on hold, discontinued, or expired prescription orders. This process allows a user to view prescription order information in one place whether the order originated from a dispensing or host VistA instance.

![](pso-7-532-one-va-pharmacy-user-guide/006.png) The OneVA Pharmacy’s feature to query the HDR/CDS Repository (step 2 in the flow of events) will not execute if the patient has not been treated at more than one VA Medical Center.

Actors

- User (e.g. Pharmacist)
- Dispensing VistA Instance
- HDR/CDS Repository
- eMI ESB (proxy to host VistAs)

Pre-Conditions

- Patient must have an Integration Control Number (ICN)
- Patient must have information populated in the system
- User must have accessed the ‘RX (PRESCRIPTIONS) \[PSO RX\]’ menu within VistA and hold the appropriate security keys for their user role, such as PSORPH to identify the user as a Pharmacist. (No separate Security Key required.).

Flow of Events

1.  User enters the Medication Profile view.
2.  The dispensing VistA instance will retrieve the prescriptions from HDR/CDS Repository.
3.  The dispensing VistA instance will send a request via the eMI ESB to the HDR/CDS Repository with the patient identifiers to retrieve the prescriptions with a status of ‘Suspended’, ‘Active’, ‘Hold’, “Discontinued (within the past 120 days)” or “Expired (within the past 120 days)” from all previous treatment facilities *excluding* local facility.
4.  The eMI ESB will exclude the Clinical Data Health Care Repository/Department of Defense (CHDR/DoD) prescriptions that are available in the HDR/CDS Repository for active dual patients.

Exceptions

- 2a. Patient Not Found
- 2b. Patient Found, No Prescription Records
- 2c. eMI ESB is not accessible.
- 2d. HDR/CDS Repository is not accessible.
- 2e. Multiple Patients Found
- 3a. Patient Found, No Prescription Records Matching Filter

System Message

- 1a. Please wait. Checking for prescriptions at other VA Pharmacy locations. This may take a moment…
- 1b. Eligibility: RX PATIENT STATUS: OPT NSC
- 2a. Patient Identifier Not Found
- 2b. Patient Found with no Prescription Records
- 2c. The system is down or not responding. Press RETURN to continue.
- 2d. The RX Database is not Responding to the Request
- 2d. The RX Database responded with an error
- 2e. Multiple Patient Matches Found – Correct MVI (note: MVI is the Master Veteran Index. Please know the acronym is not spelled out in the error message.)
- 3a. Patient Found with no Prescription Records Matching Search Criteria

### Use Case: Dispense Order from another VA Pharmacy Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a Pharmacist selects a prescription from the Medication Profile screen on a dispensing VistA instance (to refill a prescription for a Veteran visiting this location), an HL7 ‘Pharmacy Treatment Dispense’ message transmits via eMI. eMI will receive the request, determine the destination facility, and forward the message to the host VistA instance. The host VistA instance will process the message, decrement the number of refills remaining, update the last fill date, and if a partial request, update the partial information. The host VistA will create an HL7 message (Prescription Refill/Partial Services Response) which contains the prescription label information. eMI will route the HL7 message back to the dispensing VistA instance, displaying the completion of the transaction to the Pharmacist on the screen. The Medication Profile view refreshes by executing the View Order Use Case again. The refilling or partial filling of a prescription order is referred to as the OneVA Pharmacy Dispense Order from another VA Pharmacy Location Use Case.

The ‘Dispense another VA Pharmacy Order’ Use Case describes the process for users to dispense an order that originated from another VA Pharmacy location. Once the user executes the View Order Use Case, the user can select an active prescription from the Medication Profile view that originated in another VA Pharmacy VistA instance to dispense. After selecting the prescription and executing the fill order request, the system will send a message to the originating host VistA instance. This request will decrement the prescription count but will not affect the inventory of the host facility. When the decrement is successful, communication is made back to the dispensing VistA instance to complete the process and to print a prescription label.

Actors

- User (e.g. Pharmacist)
- Dispensing VistA Instance
- eMI ESB
- Host VistA Instance

Pre-Conditions

- Patient must have an ICN.
- Patient must have information populated in the system
- Dispensing VistA instance has the required amount of prescribed medication inventory on-hand.
- User must have accessed the ‘RX (PRESCRIPTIONS) \[PSO RX\]’ menu within VistA and hold the appropriate security keys for their user role, such as PSORPH to identify the user as a Pharmacist. (No separate Security Key required.).

Flow of Events

1.  User selects a prescription that originated from another VA Pharmacy VistA instance and RF (Refill) from the Medication Profile view.
2.  The prescription must be in ‘Active’ status.
3.  The dispensing VistA instance will send a refill order request to the eMI ESB.
4.  The eMI ESB will route the refill order request to the host VistA instance.
5.  The host VistA will conduct order checks.
1.  The host VistA will update the prescription order and decrement refills.
2.  The host VistA will create a prescription label.
6.  The dispensing VistA instance will dispense medication.
7.  The dispensing VistA instance will print the label to the dispensing location printer.

Alternate Flow

1.  User selects a prescription that originated from another VA Pharmacy VistA instance and PF (Partial fill) from the Medication Profile view.
2.  The prescription must be in ‘Active’ status.
3.  The dispensing VistA instance will send a partial fill order request to the eMI ESB.
4.  The eMI ESB will send a partial fill order request to the host VistA instance.
5.  The host VistA will conduct order checks.
1.  The host VistA will update the prescription order and update partial fill date.
2.  The host VistA will create a prescription label.
6.  The dispensing VistA instance will dispense medication.
7.  The dispensing VistA instance will print the label to the dispensing location printer.

Exceptions

- 2\. Status is not ‘Active’
- 3a. eMI ESB is not accessible.
- 4a. The host VistA is not accessible
- 4b. The prescription is a controlled substance
- 5a. The host VistA instance fails the order.

System Message

- 1a. Please wait. Checking for remote prescriptions. This may take a moment…
- 1b. Eligibility: RX PATIENT STATUS: OPT NSC//
- 2\. Only 'ACTIVE' remote prescriptions may be actioned at this time.
- 3a. The system is down or not responding. Press RETURN to continue.
- 3b. Invalid HL7 Data Format
- 4a. The system is down or not responding. Could not query other VA Pharmacy locations. Press RETURN to continue.
- 4b. Cannot refill Rx# xxxxxxx. This is a controlled substance.
- 5a. The following are the various standard system messages that could display
  - \*\*\* Drug is inactive for Rx \# xxxxxxx cannot be refilled \*\*\*" (refill prescription <span id="p14" class="anchor"></span>not allowed on inactive drugs)
  - Can't refill Rx \# xxxxxxx it is not for this patient.
  - Cannot refill, Rx is discontinued or expired. Later Rx may exist.
  - Can't refill, no refills remaining.
  - This drug has been changed; no refills allowed.
  - The system is down or not responding (Connection Failed). Could not query prescriptions at other VA Pharmacy locations. Press RETURN to continue:
  - <span id="PSO_7_532" class="anchor"></span>The system is down or not responding. The other VA Pharmacy location has not installed the OneVA Pharmacy functionality.
  - The system is down or not responding. The other VA Pharmacy location has installed the OneVA Pharmacy software but is currently not accepting refill or partial fill request.

### Use Case: OneVA Pharmacy Prescription Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ‘OneVA Pharmacy Prescription Report’ allows the user to access reports related to the orders created from the OneVA Pharmacy process. Once the user executes the OneVA Pharmacy Prescription Report, the user can generate three different reports. The reports allow the user to view prescriptions filled by another VA Pharmacy location or what other VA Pharmacy locations filled prescriptions for a targeted facility.

Pre-Conditions

- User has access to the OneVA Pharmacy Prescription Report \[PSO REMOTE RX REPORT\] menu
- User must have access to the ‘RX (PRESCRIPTIONS) \[PSO RX\]’ menu within VistA and hold the appropriate security keys for their user role, such as PSORPH to identify the user as a Pharmacist. (No separate Security Key required.)

Flow of Events

1.  User selects a report option from the ‘OneVA Pharmacy Prescription Report’ menu.
1.  User selects ‘Prescriptions we have filled for other facilities’ report.
2.  User selects ‘Our prescriptions, filled by other facilities’ report.
3.  User selects ‘All activity for Other VA Pharmacy locations’ report
2.  User selects ‘D’ – ‘Date Range’ or go to step 3 or step 4
1.  User enters start date.
2.  User enters end date.
3.  User selects ‘P’ - ‘Patient’ or go to step 4.
1.  User enters Patient Name
4.  User selects ‘S’ - ‘Site’.
1.  User enters Institution Name.

## User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To access the OneVA Pharmacy software the user must have access to the ‘RX (PRESCRIPTIONS) \[PSO RX\]’ menu within VistA and hold the appropriate security keys for their user role, such as PSORPH to identify the user as a Pharmacist. (No separate Security Key required.).

## Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New OneVA Pharmacy Checking for Prescriptions Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OneVA Pharmacy software uses a new service call to the HDR/CDS Repository each time the Medication Profile view activates via the ‘PATIENT PRESCRIPTION PROCESSING \[PSO LM BACKDOOR ORDERS\]’ menu. This new service call activates if the patient has been treated at more than one VA Medical Center. This additional service call retrieves all prescriptions associated with the patient from the repository, which requires additional time. In order to execute the query to the HDR/CDS Repository, the user must accept the default of ‘YES’ to the ‘Would you like to query prescriptions from other OneVA Pharmacy locations?’ prompt and displayed in the following image.

Figure : Query Prescription from other OneVA Pharmacy Locations Prompt

![](pso-7-532-one-va-pharmacy-user-guide/007.png)

The user will receive the following message while the query processes:

Figure : OneVA Pharmacy Checking for Prescriptions Message

![](pso-7-532-one-va-pharmacy-user-guide/008.png)

![](pso-7-532-one-va-pharmacy-user-guide/009.png) The OneVA Pharmacy’s feature to query the HDR/CDS Repository will not execute if the patient has only one entry in the ‘TREATING FACILITY LIST (#391.91)’. Prior to validating the ‘TREATING FACILITY LIST’ entries, the process filters on the following list of valid facility types: VAMC, M&ROC, M&ROC(M&RO), OC, OPC, CBOC, PRRTP, DOM, HCS, MC(M), MC(M&D), MORC, NHC, VANPH, SOC, SARRTP.

If there are not two or more valid entries, the system will not display the ‘Executing OneVA Pharmacy Query Message’ listed in the figure above nor will medications that originated from another VA Pharmacy location display on the Medication Profile view.

### New OneVA Pharmacy System Down or Not Responding Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](pso-7-532-one-va-pharmacy-user-guide/010.png)The system identifies and queries the HDR/CDS Repository for all the prescriptions that are active, suspended, on hold, expired (within 120 days), or discontinued (within 120 days). If the connection fails, the system is down message will display as shown in the following image.

Figure : OneVA Pharmacy System Not Responding Message

![](pso-7-532-one-va-pharmacy-user-guide/011.png)

![](pso-7-532-one-va-pharmacy-user-guide/012.png)[Contact local support](#national-service-desk-and-organizational-contacts) if this problem persists.

![](pso-7-532-one-va-pharmacy-user-guide/013.png) When the system is down message displays, the VistA session will continue to display the local/dispensing sites prescriptions on the Medication Profile view. There will be no indication if a patient is registered or has prescriptions on other sites (i.e., remote site prescriptions will not display on the Medication Profile view.)

### OneVA Pharmacy Patient Found No Rxs Informational Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](pso-7-532-one-va-pharmacy-user-guide/014.png)The system identifies and queries the HDR/CDS Repository but if the patient does not have any prescription records from other VA Pharmacy locations, matching the search criteria, the following informational message displays:

Figure : Informational Message Patient Exists but Has No Remote Prescriptions

![](pso-7-532-one-va-pharmacy-user-guide/015.png)

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Logging On

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OneVA Pharmacy patch is an enhancement to the VistA ‘PHARMACY \[PS MENU\]’ \> ‘OUTPATIENT PHARMACY’ package. To access the application, the user must enter access and verify codes to login.

## System Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OneVA Pharmacy patch is an enhancement to the VistA ‘PHARMACY \[PSO MENU\]’ \> ‘OUTPATIENT PHARMACY MANAGER \[PSO MANAGER\]’ \> ‘RX (PRESCRIPTION) \[PSO RX\]’ menu. The user must have access to these menus in order to execute the OneVA Pharmacy software.

## Changing User ID and Password

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OneVA Pharmacy feature occurs fully within the context of VistA and as such relies on the pre-existing procedures to log in and change the user password.

## Exit System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OneVA Pharmacy feature occurs fully within the context of VistA and as such relies on the pre-existing functionality to exit the system. The VistA application will also close if the user is inactive.

## Caveats and Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Label Reprinting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OneVA Pharmacy patch retrieves the prescription information for the label from the host site and transmits the data back to the dispensing site for printing. As of this writing, there is no ‘REMOTE REPRINT’ option available for OneVA Pharmacy orders. The ‘REPRINT’ action is not operational for the OneVA Pharmacy refills or partials; however, plans are being made to release a new action option as part of the OneVA Pharmacy Phase II initiative.

In order to reprint a label due to a paper jam, a malfunction of the printer, or the need to label multiple packages like inhalers, it is suggested to use the OneVA Pharmacy ‘[Partial Fill Prescription Order](#partial-fill-prescription-order)’ process and perform the transaction again.

### Target VistA Time Out Awaiting Reply Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OneVA Pharmacy remote refill and remote partial fill actions at times receives the following exception message:

> MESSAGE SENT TO TARGET VISTA; TIME OUT AWAITING REPLY

> Press RETURN to continue:

The user pressed RETURN and must execute the transaction steps for a second time. If the user repeats the transaction, the process successfully executes.

### Host Site OneVA Pharmacy Flag Not Set On

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As stated in the ‘[Systems Configuration](#system-configuration)’ section of this document, if the ‘ONEVA PHARMACY FLAG (#101)’ is not set to the ‘on’ state at the host site, the dispensing site will receive the following message:

> The OneVA Pharmacy flag is turned ‘OFF’ at this facility. Unable to process refill/partial fill requests. Queries will NOT be made to other VA Pharmacy locations.

# Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Selecting a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sign-in to the VistA system and select the menu option:

> PATIENT PRESCRIPTION PROCESSING \[PSO LM BACKDOOR ORDERS\]

1.  Enter a patient identifying information at the ‘Select PATIENT NAME:’ prompt.

Figure : Select PATIENT NAME Prompt

> ![](pso-7-532-one-va-pharmacy-user-guide/016.png)

![](pso-7-532-one-va-pharmacy-user-guide/017.png) The process for selection a patient is unchanged. The system responds with the patient name, date of birth, and other patient information.

2.  Press \<ENTER\> if this is the correct patient.

Figure : Patient Found Press RETURN to Continue Prompt

> ![](pso-7-532-one-va-pharmacy-user-guide/018.png)

3.  Press \<ENTER\> if the ‘Allergy Assessment’ message is received:

Figure : Allergy Assessment Message

> ![](pso-7-532-one-va-pharmacy-user-guide/019.png)

### View Order Rxs from other VA Pharmacy Locations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system begins to execute the OneVA Pharmacy query for prescriptions from all other VA Pharmacy locations if it meets the conditions documented in the ‘[Continuity of Operation](#continuity-of-operation)’ section of this document.

4.  Press \<ENTER\> and accept the default of ‘Yes’ at the ‘Query Prescription from other OneVA Pharmacy locations’ prompt.

Figure : Query Prescription from other OneVA Pharmacy Locations Prompt

![](pso-7-532-one-va-pharmacy-user-guide/020.png)

After entering yes, the ‘OneVA Pharmacy Checking for Prescriptions’ information message displays.

The system will display the checking for prescriptions message as shown in the following image.

Figure : Executing OneVA Pharmacy Query Message

![](pso-7-532-one-va-pharmacy-user-guide/021.png)

![](pso-7-532-one-va-pharmacy-user-guide/022.png) The OneVA Pharmacy’s feature to query the HDR/CDS Repository will not execute if the patient has only one entry in the ‘TREATING FACILITY LIST (#391.91)’. Prior to validating the ‘TREATING FACILITY LIST’ entries, the process filters on the following list of valid facility types: VAMC, M&ROC, M&ROC(M&RO), OC, OPC, CBOC, PRRTP, DOM, HCS, MC(M), MC(M&D), MORC, NHC, VANPH, SOC, SARRTP.

If there are not two or more valid entries, the system will not display the ‘Executing OneVA Pharmacy Query Message’ listed in the figure above nor will medications that originated from another VA Pharmacy location display on the Medication Profile view.

![](pso-7-532-one-va-pharmacy-user-guide/023.png)The system identifies and queries the HDR/CDS Repository for all the prescriptions that are active, suspended, on hold, expired (within 120 days), or discontinued (within 120 days). If the connection fails, the system is down message will display as shown in the following image.

Figure : System is Down or Not Responding Exception Message

![](pso-7-532-one-va-pharmacy-user-guide/024.png)

![](pso-7-532-one-va-pharmacy-user-guide/025.png)[Contact local support](#national-service-desk-and-organizational-contacts) if this problem persists.

![](pso-7-532-one-va-pharmacy-user-guide/026.png) When the system is down message displays, the VistA session will continue to display the local/dispensing sites prescriptions on the Medication Profile view. There will be no indication if a patient is registered or has prescriptions on other sites (i.e., remote site prescriptions will not display on the Medication Profile view.)

> Press \<ENTER\> if the ‘system is down’ message displays.

As mentioned in the ‘[Systems Summary](#system-summary)’ section, the OneVA Pharmacy program was an initiative from the grassroots Innovation Program. As such, development requirements were limited, and specific software areas were to remain untouched; kept ‘as-is’.

An example can be found in the following figure where the original ‘REMOTE PRESCRIPTION AVAILABLE – DISPLAY REMOTE DATA’ prompt still remains. The user bypasses the display of remote data once the OneVA Pharmacy patch is available by entering ‘No’.

5.  Enter \<N\> to accept the ‘Display Remote Data? N//’ prompt.
6.  Press \<ENTER\> to accept the default or enter a valid status code change to the status.

Figure : Patient Status Message: Update or Press RETURN to Continue Prompt

> ![](pso-7-532-one-va-pharmacy-user-guide/027.png)

### Patient Information View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After selecting a patient, the system displays the first page of the ‘Patient Information’ view.

7.  Press \<ENTER\> to continue to the second page of the ‘Patient Information’ view.

### Medication Profile View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

8.  Press \<ENTER\> to continue to the ‘Medication Profile’ view.

The ‘Medication Profile’ view lists all prescriptions that originated at the dispensing Pharmacy first, followed by ‘[Non-VA MEDS (Not Dispensed by VA)](#NonVAMEDS)’, then by the prescriptions retrieved from the HDR/CDS Repository that originated at other VA Pharmacy locations. The prescriptions originating from other VA Pharmacy locations display under a divider header line showing the site name, site number, and status.

The first page of the Medication Profile view, in the example displayed in the following image, displays the ‘dispensing site’ (aka ‘local’) prescription orders. The divider heading displays ‘ACTIVE’ and includes the ‘Active’, ‘Suspended’, and ‘Expired’ medications (no changes were made to this format), followed by the orders listed as ‘Discontinued’ medications, then prescriptions in the ‘Hold’ status.

The following image also shows the divider heading for the first ‘other’ VA Pharmacy location site and displays: ‘DAYTON (552) ACTIVE’.

Figure : Medication Profile (Page 1 of 3) Example (Remote Rxs)

> ![](pso-7-532-one-va-pharmacy-user-guide/028.png)

9.  Press \<ENTER\> to continue to the next ‘Medication Profile’ view.

Page 2 of the Medication Profile view, in the example displayed in the following image, displays the ‘Active’, ‘Discontinued’, prescriptions in the ‘Hold’ status, and ‘Suspended’ medications for the ‘DAYTON (552)’ site.

The following image also shows the divider heading for the second ‘other’ VA Pharmacy location site and displays: ‘DAYTSHR TEST LAB (984) ACTIVE’.

Figure : Medication Profile (Page 2 of 3) Example (Remote Rxs)

> ![](pso-7-532-one-va-pharmacy-user-guide/029.png)

10. Press \<ENTER\> to continue to the next ‘Medication Profile’ view.

Page 3 of the Medication Profile view, in the example displayed in the following image, displays the ‘Active’, ‘Discontinued’, prescriptions in the ‘Hold’ status, and ‘Suspended’ medications for the ‘DAYTON (552)’ site,

The following image also shows the divider heading for the second ‘other’ VA Pharmacy location site and displays: ‘DAYTSHR TEST LAB (984) ACTIVE’.

Figure : Medication Profile (Page 3 of 3) Example (Remote Rxs)

> ![](pso-7-532-one-va-pharmacy-user-guide/030.png)

#### Medication Profile View Example with ‘Non-VA MEDS’

The ‘Medication Profile’ views, displayed in the following two images, show the format when ‘Non-VA MEDS (Not Dispensed by VA)’ are available. The dispensing site prescriptions display first, followed by the ‘Non-VA MEDS (Not Dispensed by VA)’, then by prescriptions that originated from other VA Pharmacy locations.

Figure : Medication Profile (Page 1 of 2) Example (Non-VA MEDS)

![](pso-7-532-one-va-pharmacy-user-guide/031.png)

Figure : Medication Profile (Page 2 of 2) Example (Non-VA MEDS)

![](pso-7-532-one-va-pharmacy-user-guide/032.png)

### Dispense (Local) Order Originating from Dispensing (Local) Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The dispensing process for filling a prescription order that originated locally from the dispensing site was unaffected by the OneVA Pharmacy patch.

The software still provides access to all previously available actions – no changes were made to the action options related to the dispensing/local prescription refill process. To refill a prescription, the action id is ‘RF’. The action option to execute a partial fill for a prescription order is ‘PR’.

The following lists all action options available from the ‘OP Medication Profile’ view.

Figure : Action Options for Local/Dispensing Orders

> ![](pso-7-532-one-va-pharmacy-user-guide/033.png)

### Dispense Rx Order from another VA Pharmacy Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ‘Medication Profile’ view displays both the dispensing Pharmacy’s medications that originated on the local VistA instance followed by the prescriptions originating from other VA Pharmacy locations.

In the example that follows, there are no prescriptions for the patient at the dispensing site. The message ‘\<No local prescriptions found\>’ displays before the first divider header.

Figure : Medication Profile view with no ‘local’ Prescriptions (Remote Rxs Only)

![](pso-7-532-one-va-pharmacy-user-guide/034.png)

To access prescriptions originating on other sites, the same process is used.

1.  The user can either enter \<SO\> and press \<ENTER\> at the ‘Select Action’ prompt or use the short cut feature to enter \<3\> and press \<ENTER\> as displayed in the following image.

Figure : Select Action ‘SO’ and Select Order by number Prompts Example

> ![](pso-7-532-one-va-pharmacy-user-guide/035.png)

The system displays the REMOTE OP Medications view.

![](pso-7-532-one-va-pharmacy-user-guide/036.png) For the following example, note the two data fields:

- Refills
- Last Fill Date
2.  Press \<ENTER\> to continue.

During the remote refill or partial fill of a prescription order that originated from another VA Pharmacy location, the number of refills remaining is decremented by one and the last refill date is updated with the current date on the host VistA. In the example displayed in the following image, the patient has ‘11’ refills remaining, and the last refill date was ‘05/31/16’.

Figure : Remote OP Medications view for a prescription

> ![](pso-7-532-one-va-pharmacy-user-guide/037.png)

For prescription orders that originated from other VA Pharmacy locations, the dispensing Pharmacy only has two actions available. They are:

- [RF Refill Remote Order](#refill-prescription-order)
- [PR Partial](#partial-fill-prescription-order)

#### Refill Prescription Order

1.  Enter \<RF\> and press \<ENTER\> at the Select Action prompt as shown in the following image.

Figure : Remote OP Medication RF Refill Action Item Example

> ![](pso-7-532-one-va-pharmacy-user-guide/038.png)

The system confirms the action selected by showing Refill Remote Order on the prompt line as displayed in the following image.

Figure : Remote OP Medication RF Refill Action Item Results Example

> ![](pso-7-532-one-va-pharmacy-user-guide/039.png)

The system then checks for a local drug that matches the remote drug description and if found, displays a question asking the user if the matched drug is acceptable. The prompt is expecting a ‘Yes’ or ‘No’ response. The system provides ‘No’ as the default, as displayed in the following image. In order to process the refill, the user enters ‘Yes’.

![](pso-7-532-one-va-pharmacy-user-guide/040.png) For various reasons, there may not be a one to one match of the drug matching between the host and the dispensing sites therefore the message displayed in the following image may change. Follow this [LINK](#drug-matching-process) to the ‘Drug Matching’ section for drug matching messages, prompts, and instructions.

Figure : Remote Drug Match Response Example

> ![](pso-7-532-one-va-pharmacy-user-guide/041.png)

2.  Press \<ENTER\> to continue.

The system displays the processing refill request message as shown in the following image.

Figure : Remote Refill Processing Message

> ![](pso-7-532-one-va-pharmacy-user-guide/042.png)

The system completes the remote refill process and generates the label data for printing. The ‘LABEL DEVICE’ message displays as shown in the following image.

Figure : Label Device Prompt

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><span id="p26" class="anchor"></span>TRANSACTION SUCCESSFUL... The refill for RX #763002 has been recorded on</p>
<p>the prescription at the host system.</p>
<p>Select a printer to generate the label or '^' to bypass printing.</p>
<p>QUEUE TO PRINT ON</p>
<p>DEVICE:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The user enters the dispensing site printer information to print the label.

![](pso-7-532-one-va-pharmacy-user-guide/043.png)IMPORTANT: The OneVA Pharmacy requires stock prescription labels and a laser printer that is accessible at the Select LABEL DEVICE: prompt. If either one of the requirements are lacking, then the label will not print as programmed.

![](pso-7-532-one-va-pharmacy-user-guide/044.png)<span id="p27" class="anchor"></span>IMPORTANT: If the user enters an “^” at the Select LABEL DEVICE: prompt, the prescription label will not be printed and at this time. There is no way to do a reprint of the refill or partial fill label.

The label prints and the system displays a message to indicate the prescription order process completed as shown in the following image.

Figure : Successful Refill Status Message

> ![](pso-7-532-one-va-pharmacy-user-guide/045.png)

3.  Press \<ENTER\> to continue.

The system displays a message informing that the prescription list is updating. The background process is executing the ‘[View Order Use Case](#use-case-view-orders)’ and retrieving the updated information about the patient’s prescription orders from the HDR/CDS Repository.

The system displays the following message while the query to the HDR/CDS Repository is executing.

Figure : System Message: Updating Prescription Order List

> ![](pso-7-532-one-va-pharmacy-user-guide/046.png)

The system will retrieve all prescriptions from the HDR/CDS repository and redisplay the Medication Profile view showing the updated prescription information.

In the following image the example shows the last refill date has been updated to be ‘07/27’ and the refills remaining is now set to ‘10’.

Figure : Refill Successful: Medication Profile View Updated

> ![](pso-7-532-one-va-pharmacy-user-guide/047.png)

#### Partial Fill Prescription Order

1.  Enter \<PR\> and press \<ENTER\> at the Select Action prompt as shown in the following image.

Figure : Remote OP Medication PR Partial Action Item Example

> ![](pso-7-532-one-va-pharmacy-user-guide/048.png)

The system checks for a local drug that matches the remote drug description. If the system matches the drug, a ‘Yes’ or ‘No’ prompt displays. The system provides ‘No’, as the default, as displayed in the following image. In order to fill this partial prescription, order the user enters ‘Yes’.

![](pso-7-532-one-va-pharmacy-user-guide/049.png) For various reasons, there may not be a one to one match of the drug matching between the host and the dispensing sites therefore the message displayed in the following image may change. Follow this [LINK](#drug-matching-process) to the ‘Drug Matching’ section for drug matching messages, prompts, and instructions.

Figure : Remote Drug Match Response Example

> ![](pso-7-532-one-va-pharmacy-user-guide/050.png)

2.  Enter \<Y \>and press \<ENTER\>.

The system displays ‘YES’ and the ‘Enter Quantity’ prompt displays as shown in the following image.

Figure : Partial Fill Example: Quantity

> ![](pso-7-532-one-va-pharmacy-user-guide/051.png)

3.  Enter \<10\> and press \<ENTER\>.

The system displays ‘10’ and the ‘DAYS SUPPLY’ prompt displays as shown in the following image.

Figure : Partial Fill Example: Days Supply

> ![](pso-7-532-one-va-pharmacy-user-guide/052.png)

4.  Enter \<10\> and press \<ENTER\>.

The system displays ‘10’ and the ‘Pharmacist’ prompt displays defaulting to the name of the Pharmacist as shown in the following image.

Figure : Partial Fill Example: Pharmacist

> ![](pso-7-532-one-va-pharmacy-user-guide/053.png)

5.  Press \<ENTER\>.

The system displays the name of the Pharmacist, the Site, and the ‘Remarks’ prompt displays as shown in the following image.

Figure : Partial Fill Example: Remarks

> ![](pso-7-532-one-va-pharmacy-user-guide/054.png)

6.  Enter \<LAST REFILL LOST\> and press \<ENTER\>.

The system displays ‘LAST REFILL LOST’ as shown in the following image.

Figure : Partial Fill Example: Remarks Example

> ![](pso-7-532-one-va-pharmacy-user-guide/055.png)

The system displays the processing refill request message as shown in the following image.

Figure : Remote Refill Processing Message

> ![](pso-7-532-one-va-pharmacy-user-guide/056.png)

The system completes the remote partial fill process and generates the label data for printing. The ‘LABEL DEVICE’ message displays as shown in the following image.

Figure : Label Device Prompt

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><span id="p30" class="anchor"></span>TRANSACTION SUCCESSFUL... The refill for RX #763002 has been recorded on</p>
<p>the prescription at the host system.</p>
<p>Select a printer to generate the label or '^' to bypass printing.</p>
<p>QUEUE TO PRINT ON</p>
<p>DEVICE:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The user enters the dispensing site printer information to print the label.

The label prints and the system displays a message to indicate the prescription order process completed as shown in the following image.

Figure : Successful Partial Fill Status Message

> ![](pso-7-532-one-va-pharmacy-user-guide/057.png)

7.  Press \<ENTER\> to continue.

The system displays a message informing that the prescription list is updating. The background process is executing the ‘[View Order Use Case](#use-case-view-orders)’ and retrieving the updated information about the patient’s prescription orders from the HDR/CDS Repository.

The system displays the following message while the query to the HDR/CDS Repository is executing.

Figure : System Message: Updating Prescription Order List

> ![](pso-7-532-one-va-pharmacy-user-guide/058.png)

The system will retrieve all prescriptions from the HDR/CDS repository and redisplay the Medication Profile view showing the updated prescription information.

Use the OneVA Pharmacy Prescription Reports capability to review the partial fill activity for both the dispensing and host sites transactions. Follow this [LINK](#oneva-pharmacy-prescription-report-pso-remote-rx-report) to the OneVA Pharmacy Report section for details.

#### Drug Matching Process

Overall, three outcomes occur during the OneVA Pharmacy Drug Matching function. They are:

1.  One-to-One Match
2.  One-to-Many Match
3.  No Drug Match

#### Drug Matching: One-to-One

When the drug matching logic identifies a one-to-one match at the dispensing site for the selected host prescription, the systems displays the ‘Remote site drug name:’ and the ‘Matching Drug Found for Dispensing:’ and prompts the user to respond ‘YES’ or ‘NO’ as displayed in the following image.

Figure : Drug Matching: One-to-One Match

![](pso-7-532-one-va-pharmacy-user-guide/059.png)

#### Drug Matching: One-to-Many

When the drug matching logic identifies a one-to-many match at the dispensing site for the selected host prescription, the system the ‘Remote site drug name:’ and the ‘Select matching local drug:’ prompt as displayed in the following image.

Figure : Drug Matching: One-to-Many - Select matching local drug Prompt

![](pso-7-532-one-va-pharmacy-user-guide/060.png)

To display the list of possible entries, the user enters two questions marks \<??\> at the ‘Select matching local drug’ prompt and presses \<ENTER\> as displayed in the following image.

Figure : Drug Matching: One-to-Many

![](pso-7-532-one-va-pharmacy-user-guide/061.png)

The system displays the list of possible drug matches and prompts the user to select a drug as shown in the following image.

Figure : Drug Matching: One-to-Many – Select from List of Possible Matches

![](pso-7-532-one-va-pharmacy-user-guide/062.png)

In the following example, the user enters \<2043\> and presses \<ENTER\>. The system displays the selected drug and prompts the user to respond ‘YES’ or ‘NO’ as displayed in the following image.

Figure : Drug Matching: One-to-Many – Select Drug 2042 Example

![](pso-7-532-one-va-pharmacy-user-guide/063.png)

#### Drug Matching: No Drug Match

When the drug matching logic does not identify any drug match the system at the dispensing site for the selected host prescription, the system the ‘Remote site drug name:’ and the ‘Select matching local drug:’ prompt as displayed in the following image.

Figure : Drug Matching: No Drug Match

![](pso-7-532-one-va-pharmacy-user-guide/064.png)

#### Drug Matching: Exception Messages

The OneVA Pharmacy patch contains specific business rules to prevent refill and/or partial orders that originated at other VA Pharmacy locations from being processed. They include the following list:

- Patient's prescription that originated from another VA Pharmacy location cannot be refilled before the next refill date.

> Unable to complete transaction.

> Cannot refill Rx# xxxxxxx. Next possible fill date is MM/DD/YYYY

- Patient’s prescription that originated from another VA Pharmacy location is not fully or partially dispensed when the prescription status is ‘discontinued’, ‘expired’, is on ‘hold’, or ‘suspended’.

> Only 'ACTIVE' remote prescriptions may be refilled at this time.

- Patient’s prescription that originated from another VA Pharmacy location and cannot be dispensed (refilled) when there are zero remaining refills. Note: Partial fills are allowed.

> Unable to complete transaction. Cannot refill Rx \# xxxxxxx. No refills left.

- Patient’s prescription that originated from another VA Pharmacy location and cannot be dispensed (refill or partial fill) when the drug is classified as a controlled substance on the dispensing site.

> This is a controlled substance. Cannot refill Rx \# xxxxxxx.

- Patient’s prescription that originated from another VA Pharmacy location and cannot be dispensed (refill or partial fill) when the drug is classified as a controlled substance on the host site.

> Unable to complete transaction.  Rx \#xxxxxxx cannot be refilled.

> The associated drug is considered a controlled substance at the host facility.

- Patient’s prescription that originated from another VA Pharmacy location and cannot be dispensed (refill or partial fill) when the drug is inactive on the dispensing site.

> Matched Drug \<DRUG NAME\> is inactive. Cannot refill.

- Patient’s prescription that originated from another VA Pharmacy location and cannot be dispensed (refill or partial fill) when the drug has no dispensing site match.

> No local match could be found for \<DRUG NAME\>

- Patient’s prescription that originated from another VA Pharmacy location and cannot be dispensed (refill or partial fill) when no drug on the dispensing site has a matching VA Product ID.

> Missing VA Product ID. Rx \#xxxxxxx cannot be refilled.

## OneVA Pharmacy Prescription Report \[PSO REMOTE RX REPORT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### OneVA Pharmacy Report Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OneVA Pharmacy patch comes with a new menu option for retrieving the OneVA Pharmacy Prescription Reports. The ‘ONEVA PHARMACY PRESCRIPTION REPORT \[PSO REMOTE RX REPORT\]’ menu is located on the ‘RX (PRESCRIPTIONS) \[PSO RX\]’ menu as highlighted in the following image.

Figure : OneVA Pharmacy Prescription Report \[PSO REMOTE RX REPORT\] Menu

![](pso-7-532-one-va-pharmacy-user-guide/065.png)

There are three new reports available on the menu with self-describing titles. They are:

1.  Prescriptions dispensed for other Host Pharmacies
2.  Our prescriptions, filled by other facilities as the Dispensing Pharmacy
3.  All OneVA Pharmacy Prescription Activity

### Accessing OneVA Pharmacy Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following section provides the details to access the report menu, how to select specific refill information using various search options and provides the description of the report content.

Sign-in to the VistA system and select the menu option:

> ONEVA PHARMACY PRESCRIPTION REPORT \[PSO REMOTE RX REPORT\]

> The system will display the three OneVA Pharmacy reports as shown in the following image:

Figure : OneVA Pharmacy Menu and Reports

> ![](pso-7-532-one-va-pharmacy-user-guide/066.png)

- Selecting \<1\> will display the list of prescriptions that our local facility has dispensed on behalf of other host Pharmacy locations.
- Selecting \<2\> will display the list of prescriptions other VA Pharmacy locations have filled as a dispensing site for a prescription that originated from our location.
- Selecting \<3\> will list all prescriptions that we have filled for other Pharmacy locations as the dispensing site and all prescriptions other Pharmacy locations have filled on our behalf.

> The user has the option to answer with \<1\>, \<2\>, or \<3\>.

#### Selecting a Report and Report Search Options

Use the report number to select the desired report.

1.  Enter \<1\> to select the report ‘Prescriptions we have dispensed for other Host Pharmacies’ and press \<ENTER\>.

Figure : Example: Select 1 for Prescriptions dispensed for other Host Pharmacies

> ![](pso-7-532-one-va-pharmacy-user-guide/067.png)

> The system displays the name of the report selected, shows the three search options, and prompts for user to enter the date range, patient, or site as shown in the following image.

Figure : Report Search Options

> ![](pso-7-532-one-va-pharmacy-user-guide/068.png)

#### Search Option D – DATE RANGE

When selecting the ‘DATE RANGE’ option ‘D’ search feature all refills or partial fills performed between ranges of dates display. When selecting this option, the user enters two additional data items. They are:

- Start date (defaults to 30-days prior to today’s date)
- End date (defaults to today’s date)
1.  Enter \<D\> and press \<ENTER\>.

> The system displays the option name and prompts for the start date.as displayed in the following image.

> ![](pso-7-532-one-va-pharmacy-user-guide/069.png) Examples of valid date entry options are available using the ‘HELP’ command ‘?’ as displayed in the following image.

Figure : Report Date Range Search Example: Start Date

> ![](pso-7-532-one-va-pharmacy-user-guide/070.png)

2.  Press \<ENTER\> to accept the default start date.

> The system displays the defaulted start date and prompts for the end date.as displayed in the following image

Figure : Report Date Range Search Example: End Date

> ![](pso-7-532-one-va-pharmacy-user-guide/071.png)

3.  Press \<ENTER\> to accept the default end date.

Figure : Report Date Range Search Example: End Date Image 2

> ![](pso-7-532-one-va-pharmacy-user-guide/072.png)

> The system displays the ‘Summary Report’ for the selected report.

Figure : Report Date Range Search Example Results: Summary Report

> ![](pso-7-532-one-va-pharmacy-user-guide/073.png)

#### Search Option P – PATIENT

When selecting the ‘PATIENT’ option ‘P’ search feature all refills or partial fills performed for a single patient display. Select a patient by specifying the patient name, social security number, last 4-digits of the social security number, or the first initial of the last name with last 4-digits of social security numbers.

1.  Enter \<P\> and press \<ENTER\>.

> The system displays the option name and prompts for the patient’s name as displayed in the following image.

Figure : Report Patient Search Example: Patient Name

> ![](pso-7-532-one-va-pharmacy-user-guide/074.png)

2.  Enter \<PSOPATIENT, THREE\> and press \<ENTER\>.

> If the text matches multiple patients, a list will display for the user to select a specific patient. If the text matches only one patient, the patient information displays as shown in the following image.

Figure : Report Patient Search Example: Patient Name Display

> ![](pso-7-532-one-va-pharmacy-user-guide/075.png)

3.  Press \<ENTER\> to continue.

> The system displays the ‘Summary Report’ for the selected report.

Figure : Report Patient Search Example: Results Summary Report

> ![](pso-7-532-one-va-pharmacy-user-guide/076.png)

#### Search Option S – SITE

The ‘SITE’ option ‘S’ selects all refills performed at a specific VA site. A site can be selected by specifying the Institution’s Name, Status, Station Number, Official VA Name, Current Location, Coding System/ID Pair, National Provider Identifier (NPI), Status, Name (Changed From), or Coding System.

1.  Enter \<S\> and press \<ENTER\>.

> The system displays the option name and prompts for site identification text as displayed in the following image.

Figure : Report Site Search Example

> ![](pso-7-532-one-va-pharmacy-user-guide/077.png)

2.  Enter \<DAYTON\> and press \<ENTER\>.

> If the text matches only one site, the summary report page displays. If the text matches multiple sites, a list will display for the user to select a facility as shown in the following image.

3.  Enter \<1\> and press \<ENTER\>.

Figure : Report Site Search Example: Select Site from Multiple List

> ![](pso-7-532-one-va-pharmacy-user-guide/078.png)

> The system displays the ‘Summary Report’ for the selected report.

Figure : Report Site Search Example: Results Summary Report

> ![](pso-7-532-one-va-pharmacy-user-guide/079.png)

### OneVA Pharmacy Report Content

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All OneVA Pharmacy reports contain a summary page and a detailed page and all three reports have the same format and basic information regardless of the search option selected.

The following is an example of the summary page layout for the OneVA Pharmacy reports.

Figure : OneVA Pharmacy Report Example: Summary Page

![](pso-7-532-one-va-pharmacy-user-guide/080.png)

The type of report selected determines the refills shown on a report and the search option specified as described within this document. A row number identifies each refill/partial fill. For each row the date processed, patient name, drug name, quantity dispensed, and the quantity supplied displays. There are four refill type values. They are:

- RF – refills
- PR - partial refills
- OR – refills performed by other sites
- OP – partial fills performed by other sites

The total cost is the sum of the costs of all items included in this report and is available on the report ‘Prescriptions we have dispensed for other Host Pharmacies’. The cost is calculated by using the dispensing sites ‘Price Per Dispense Unit’ and multiplying that by the quantity being dispensed.

To review more information about the orders, perform the following steps:

1.  Enter \<SI\> at the ‘Select Action’ prompt and press \<ENTER\>.

> The system displays the action name and prompts for the item to display:

2.  Enter \<11\> at the ‘Enter a number’ prompt and press \<ENTER\>.

> The following image displays the ‘Select Action’ and ‘Enter a number’ prompts.

Figure : OneVA Pharmacy Report Example: Select Item

> ![](pso-7-532-one-va-pharmacy-user-guide/081.png)

> The system displays the detail report for that item as displayed in the following image.

Figure : OneVA Pharmacy Report Example: Details Page

> ![](pso-7-532-one-va-pharmacy-user-guide/082.png)

3.  Press \<ENTER\> to return to the summary report view.
4.  Continue to press \<ENTER\> to return to the report menu prompt.
5.  Select a report and search options section to view another report.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OneVA Pharmacy introduces new functionality that allows a Pharmacist to refill or partial fill a prescription from another VA Pharmacy location. This software patch uses HL7 messaging to send and receive remote prescription details from another VA Pharmacy location. This allows a ‘dispensing’ (‘non-custodial’ or ‘local’ pharmacy) to refill a prescription that originated from another VA Pharmacy location. The VA Pharmacy location where the prescription originated is the ‘host’ (‘remote’) facility.

VistA utilizes HL7 to send a query message to the eMI ESB. eMI sends the HL7 message to the HDR/CDS Repository and medications return to the querying site. The prescriptions display below any ‘local’ prescriptions on the Medication Profile view. The Pharmacist can then view and choose a ‘host’ prescription and will be able to refill or partially fill any active non-controlled substance prescription at either facility.

Entries log for all ‘host’ and ‘dispensing’ refills and partial fills into a new file called ‘REMOTE PRESCRIPTION LOG (#52.09)’. The entries are viewable using the OneVA Pharmacy Prescription Report functionality.

With this integrated VistA patch, several points of failure could occur. The systems design will allow the process to continue if any of the various integration points fail, however, remote prescriptions will not display to the Pharmacist on the Medication Profile view.

There are application error messages that will display during the search for the patient and the patient’s prescriptions. They are:

- No patient error message:

> PATIENT IDENTIFIER NOT FOUND

- Multiple patients returned error messages:

> MORE THAN ONE PATIENT RETURNED IN CALL TO HDR-CDS

> MORE THAN ONE PATIENT FOUND ON RX DATABASE, CHECK ICN

- Patient returned; no prescription data returned error message:

> PATIENT FOUND WITH NO PRESCRIPTION RECORDS

- Patient returned; no prescription data matching filters returned error message:

> PATIENT FOUND WITH NO PRESCRIPTION RECORDS MATCHING SEARCH CRITERIA

## Special Instructions for Error Correction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Significant errors are errors or conditions that affect the system stability, availability, performance, or otherwise make the system unavailable to its user base. For any significant error, please contact your local support.

# Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table provides the list of acronyms used throughout the document along with their descriptions.

| Acronym/Abbreviation   | Description                                                           |
|----------------------------|---------------------------------------------------------------------------|
| \[DIUSER\]                 | FileMan Menu                                                              |
| \[PSO LM BACKDOOR ORDERS\] | Patient Prescription Processing Menu                                      |
| \[PSO MANAGER\]            | Outpatient Pharmacy Manager Menu                                          |
| \[PSO MENU\]               | Pharmacy Menu                                                             |
| \[PSO REMOTE RX REPORT\]   | OneVA Pharmacy Prescription Report Menu                                   |
| \[PSO RX\]                 | Rx (Prescriptions) Menu                                                   |
| AITC                       | Austin Information Technology Center                                      |
| C/HDR                      | Clinical/Health Data Repository                                           |
| CDS                        | Clinical Data Services                                                    |
| Clin1                      | Clinical Product Support Team 1                                           |
| DAYTSHR                    | Dayton Test Laboratory VistA instance                                     |
| DoD                        | Department of Defense                                                     |
| eMI                        | Enterprise Messaging Infrastructure                                       |
| EPMO                       | Office of Information and Technology Enterprise Program Management Office |
| ESB                        | Enterprise Service Bus                                                    |
| GOV                        | Government                                                                |
| HDR                        | Health Data Repository                                                    |
| HL7                        | Health Level 7                                                            |
| ICN                        | Integrated Control Number                                                 |
| IOC                        | Initial Operating Capability                                              |
| IT                         | Information Technology                                                    |
| MVI                        | Master Veteran Index                                                      |
| NPI                        | National Provider Identifier                                              |
| NSD                        | National Service Desk                                                     |
| OI&T                       | Office of Information and Technology                                      |
| OMB                        | Office of Management and Budget                                           |
| OP                         | Outpatient Pharmacy                                                       |
| OP                         | OneVA Pharmacy Partial Fill                                               |
| OR                         | OneVA Pharmacy Refill                                                     |
| PII                        | Personally Identifiable Information                                       |
| PR                         | Partial Refill (Local)                                                    |
| PSO                        | Outpatient Prescription Pharmacy                                          |
| RF                         | Refill (Local)                                                            |
| Rx                         | Prescription                                                              |
| SDM                        | Service Desk Manager                                                      |
| VA                         | Department of Veterans Affairs                                            |
| VAMC                       | Veterans Affairs Medical Center                                           |
| VDL                        | VA Software Document Library                                              |
| VHA                        | Department of Veterans Health Administration                              |
| VistA                      | Veterans Health Information Systems and Technology Architecture           |

# Appendix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Frequently Asked Questions (FAQ)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1)  What is the Value to me as the Veteran?

The previous ‘Coordinated Care for Traveling Veterans’ handbook required either a visit to the Emergency Room/Urgent Care Center or a pharmacy clinic visit to obtain a new prescription. OneVA Pharmacy makes the best use of the prescription already on file at another VA medical center.

Audience: Veteran

2)  What if I have never been registered at the VA where I’m trying to pick up my prescription?

Veterans must register/enroll at the VA medical center in order for the pharmacy to see their records.

Audience: Veteran

3)  Does OneVA pharmacy benefit me if I’m not traveling?

Use existing processes to contact the VA where your prescription is on file to request a refill.

Audience: Veteran

4)  Do you still need to enter Allergies into the Pharmacy profile?

VistA pharmacy will display allergies and adverse reactions from all remote facilities.

Audience: Pharmacy

5)  Can we send the prescription to CMOP?

OneVA Pharmacy is designed to provide an immediate fill at the Pharmacy window.

Audience: Pharmacy

6)  Can any prescription be filled by OneVA pharmacy?

Controlled substances (CS at one or both facilities) cannot be filled via OneVA pharmacy. Drugs not matched to the National Drug file cannot be filled via OneVA Pharmacy. Prescriptions will no remaining refills, on suspense or on hold cannot be filled.

Audience: Pharmacy, Veteran

7)  What should I do if I do not have the medication in stock?

Order the medication if the Veteran can return the next day, mail from CMOP to a temporary address, utilize the Coordinated Care for Traveling Veteran Handbook. “What would a prudent pharmacist do?”

Audience: Pharmacy

8)  What information is kept in my VistA system and what information is kept at the host VistA system?

The dispensing VistA system tracks the information in a new OneVA Pharmacy file (not the prescription file) for reporting purposes. The refill or partial fill is tracked in the host system’s prescription file and activity log.

Audience: Pharmacy

9)  What if it is too soon to fill?

Prescription will not be available to refill. Partial fills will be an available option. Sites can use Remote Data Views to see the fill history from the host station, especially if there are concerns for frequent partial fill requests of the same Rx.

Audience: Pharmacy

10) What is the dispensing name and address on the label?

The host pharmacy will be the name and address printed on the label which is consistent with how CMOP processes prescriptions.

Audience: Pharmacy

11) Are there any responsibilities for the host pharmacy in OneVA pharmacy?

To account for copay billing, insurance billing and subsequent refill capabilities all sites are asked to print to an OneVA Report and manually release prescriptions filled by other stations. Recommended frequency of printing report is no less than weekly.

Audience: Pharmacy

12) Does this affect the routine process of finishing prescriptions from the Pending file (ordering from OERR)?

Yes, OneVA pharmacy will bring in prescriptions from other VA treating facilities to create the first enterprise-wide patient-centric actionable medication profile.

Audience: Pharmacy

13) How does OneVA pharmacy select the drug from my drug file?

The original prescription resides in the Health Data Repository (HDR). OneVA pharmacy identifies the national drug file (NDF) “VA Product” for the prescription. Matching drugs in your local drug file are identified based on that NDF product. If there is a 1:1 match found, OneVA pharmacy will recommend that drug. If there are multiple possible matches found, OneVA pharmacy will present a pick list to select from.

Audience: Pharmacy

14) How much information can you see from the Host prescription file?

OneVA pharmacy displays a limited subset of the prescription. Once the patient is registered, VistAWeb can be utilized to see details of the prescription.

Audience: Pharmacy

15) What if the original prescription uses an abbreviation that is not in our instruction file?

The prescription label is generated from the host prescription file. This is consistent with how CMOP processes prescriptions.

Audience: Pharmacy

16) OneVA pharmacy reports show cost information, which system is used to calculate medication cost?

The dispensing system’s cost is used in the report.

Audience: Pharmacy

17) Can I send an OneVA Pharmacy prescription to automation via the Outpatient Pharmacy Automation Interfaces (OPAI)?

No, this is being evaluated for future functionality. Consider window processing workflows to dispense OneVA Pharmacy fills.

Audience: Pharmacy

18) If a patient is requesting a medication that requires in-clinic administration, could I use OneVA pharmacy?

OneVA pharmacy functionality is intended for outpatient prescriptions to be dispensed at the Pharmacy window.

Audience: Pharmacy

19) How will a patient be notified that their OneVA prescription is ready for pick up?

OneVA Pharmacy does not interface with prescription ready notification boards. Consider alternative processes and workflow.

Audience: Pharmacy

*(This page included for two-sided copying.)*