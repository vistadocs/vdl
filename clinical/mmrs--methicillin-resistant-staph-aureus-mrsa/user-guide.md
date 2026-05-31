---
title: MMRS*1*4 User Guide
doc_type: UG
doc_label: User Guide
doc_layer: patch
doc_subject: null
app_code: MMRS
app_name: Methicillin Resistant Staph Aureus (MRSA)
section: CLI
app_status: active
pkg_ns: MMRS
patch_ver: 1
patch_id: MMRS*1*4
group_key: MMRS:MMRS:1
file_numbers:
- '60'
- '61.2'
- '62.06'
- '104.1'
security_keys:
- MMRS SETUP
- PROVIDER
menu_options: 1
description: '| Date | Revision | Description | Author | |------------|----------|-----------------------|------------------------------------| | 04/12/2017 | 1.1 | Introduction updated. | REDACTED | | 01/27/2017 | 1.0 | Document baselined. | REDACTED'
audience: End users and package coordinators (ADPAC)
keywords: []
page_count: 0
word_count: 25817
section_count: 28
table_count: 6
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: April 2017
revision_count: 2
revision_newest: 04/12/2017
revision_oldest: 01/27/2017
docx_url: https://www.va.gov/vdl/documents/Clinical/Methicillin_Resistant_Staph_Aurerus/vle_micro_mmrs_1_0_4_user_guide.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Methicillin_Resistant_Staph_Aurerus/vle_micro_mmrs_1_0_4_user_guide.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=189
audit_applied: '2026-05-31'
master_source: MMRS*1*4 User Guide
master_pub_date: April 2017
consolidated_from: 2 versions
prior_versions:
- MMRS*1*5 User Guide
consolidated_title: user guide
---

VistA Lab Enhancements (VLE) – Microbiology

Releases: LR\*5.2\*463 and MMRS\*1.0\*4

User Guide

![](mmrs-1-4-user-guide/001.png)

April 2017

Document Version 1.1

Office of Information and Technology (OI&T)

*.*

Revision History

| Date       | Revision | Description           | Author                             |
|------------|----------|-----------------------|------------------------------------|
| 04/12/2017 | 1.1      | Introduction updated. | <span class="mark">REDACTED</span> |
| 01/27/2017 | 1.0      | Document baselined.   | <span class="mark">REDACTED</span> |

<span id="_Toc454522212" class="anchor"></span>Table 1: Documentation Descriptions

Table of Contents

List of Figures

List of Tables

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
  - [User Access Levels](#user-access-levels)
  - [Continuity of Operation](#continuity-of-operation)
- [Getting Started](#getting-started)
  - [Logging On](#logging-on)
  - [System Menu](#system-menu)
  - [Changing User ID and Password](#changing-user-id-and-password)
  - [Exit System](#exit-system)
  - [Keyboard Conventions](#keyboard-conventions)
- [Using the Software](#using-the-software)
  - [Program Tools Setup Menu Options](#program-tools-setup-menu-options)
    - [MDRO Tools Parameter Setup (Main)](#mdro-tools-parameter-setup-main)
  - [MDRO Tools Lab Parameter Setup Screen and Help Prompts](#mdro-tools-lab-parameter-setup-screen-and-help-prompts)
  - [MDRO Tools Lab Parameter Setup](#mdro-tools-lab-parameter-setup)
    - [MDRO Tools Lab Parameter Setup for MRSA](#mdro-tools-lab-parameter-setup-for-mrsa)
    - [MDRO Tools Lab Parameter Setup for Carbapenem-Resistance](#mdro-tools-lab-parameter-setup-for-carbapenem-resistance)
    - [MDRO Tools Lab Parameter Setup for Vancomycin-Resistant Enterococcus](#mdro-tools-lab-parameter-setup-for-vancomycin-resistant-enterococcus)
    - [MDRO Tools Lab Parameter Setup for Clostridium difficile](#mdro-tools-lab-parameter-setup-for-clostridium-difficile)
    - [MDRO Tools Lab Parameter Setup for Extended-Spectrum Beta-Lactamase](#mdro-tools-lab-parameter-setup-for-extended-spectrum-beta-lactamase)
    - [MDRO Tools Lab Parameter Setup: Deleting Information Previously Entered](#mdro-tools-lab-parameter-setup-deleting-information-previously-entered)
  - [MRSA Tools Ward Mapping Setup](#mrsa-tools-ward-mapping-setup)
    - [Deleting a Geographical Unit](#deleting-a-geographical-unit)
  - [MDRO Historical Days Edit](#mdro-historical-days-edit)
  - [CRE Tools Site Parameter Setup](#cre-tools-site-parameter-setup)
  - [Isolation Orders Add/Edit](#isolation-orders-addedit)
  - [MDRO Tools Reports Menu](#mdro-tools-reports-menu)
    - [MRSA IPEC Report](#mrsa-ipec-report)
    - [Print Isolation Report](#print-isolation-report)
    - [Print Nares Screen Compliance List](#print-nares-screen-compliance-list)
    - [Print CDI Report](#print-cdi-report)
    - [Print CRE Report](#print-cre-report)
  - [Tasked Reports](#tasked-reports)
    - [Print Isolation Report (Tasked)](#print-isolation-report-tasked)
    - [Print Nares Screen Compliance List (Tasked)](#print-nares-screen-compliance-list-tasked)
    - [MDRO Print CDI Report (Tasked)](#mdro-print-cdi-report-tasked)
    - [Obtaining a Division IEN](#obtaining-a-division-ien)
    - [Deleting a Variable Name](#deleting-a-variable-name)
- [Troubleshooting](#troubleshooting)
  - [Warning Message that Lab Test or Etiology Parameters are not configured](#warning-message-that-lab-test-or-etiology-parameters-are-not-configured)
  - [Warning Message that Etiology Parameter is not configured](#warning-message-that-etiology-parameter-is-not-configured)
  - [Warning Message that Specimen is not Configured](#warning-message-that-specimen-is-not-configured)
  - [Warning Message that Division(s) are not configured](#warning-message-that-divisions-are-not-configured)
  - [Warning Message that Chemistry Subscripted Tests are not configured](#warning-message-that-chemistry-subscripted-tests-are-not-configured)
  - [Warning Message that the etiology Staphylococcus Aureus Methicillin Resistant (MRSA) has not been configured](#warning-message-that-the-etiology-staphylococcus-aureus-methicillin-resistant-mrsa-has-not-been-configured)
  - [Warning Message that the Geographical Unit has not been configured](#warning-message-that-the-geographical-unit-has-not-been-configured)
- [Printing in Landscape](#printing-in-landscape)
- [MAS Movement](#mas-movement)
- [Glossary](#glossary)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Multi-Drug Resistant Organisms (MDRO) Program Tools (PT) application provides a method to extract data related to Methicillin-Resistant Staphylococcus aureus (MRSA), Carbapenem-Resistance (CRB-R), Vancomycin-Resistant Enterococcus (VRE), Clostridium difficile (C. diff), and Extended-spectrum beta-lactamase (ESBL). MDRO-PT contains reports that will extract and consolidate required data for entry into the Inpatient Evaluation Center (IPEC) system. Reports can also be generated to display real-time patient specific information, and can be used to identify patients that have a selected MDRO, and to identify patients who either received or did not receive a nares screening upon admission to the unit.

Patch LR\*5.2\*463 includes the necessary microbiology enhancements to allow Department of Veterans Affairs (VA) labs the ability to document and utilize standard data in VistA for Carbapenem Resistant Enterobacteriaceae (CRE) and other MDROs. In addition, it includes the ability to distribute nationally these microbiology enhancements and other MDRO standardized reporting etiologies without requiring each individual lab to update its own local files manually.

Patch MMRS\*1.0\*4 shall support the timely identification of MDROs, provide enhanced reporting capabilities for CRE and Clostridium Difficile Infection (CDI) positive cases, and streamline the MRSA initiative by updating the legacy MRSA Program Tools menu options and naming conventions to MDRO where applicable.

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Organization of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide is arranged in a manner in which Laboratory Information Manager (LIM) and Automated Data Processing Application Coordinator (ADPAC) staff members who are well versed in the VistA Laboratory package and VistA's roll-and-scroll functionality will utilize the software.

An explanation of the features and functions in the LR\*5.2\*463 and MMRS\*1.0\*4 releases are provided in this Guide.

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide was written with the following assumed experience/skills of the audience:

- User has basic knowledge of the operating system (such as the use of commands, menu options, and navigation tools).
- User has been provided the appropriate active roles, menus, and required security keys.
- User is familiar with the VistA Laboratory software package.

### Coordination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Microbiology initiative is a collaborative solution between the VistA Laboratory Enhancement (VLE) Team and Clinical Laboratory personnel. This solution provides Microbiology Laboratory Technologists a system that integrates with the existing VistA Microbiology system.

Deployment will be performed by Local Facility staff and supported by team members from one or more of the operations organizations: Enterprise Systems Engineering (ESE), Field Operations (FO), Enterprise Operations (EO), Lab SMEs and/or others.

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. The VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. However, the VA would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely if any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the VA of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section includes descriptions of any formatting or symbols and their meaning.

Various symbols are used throughout the documentation to alert the reader to special information. Table 1 gives a description of each of these symbols.

| Font              | Use                              | Example                                                                                                               |
|-----------------------|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Blue text, underlined | Hyperlink to another document or URL | For further instructions, refer to the link: <http://www.va.gov/vdl>                                                      |
| Courier New           | Menu options                         | MDRO Tools Parameter Setup                                                                                                |
|                       | Screen prompts                       | Want KIDS to INHIBIT LOGONs during the install? YES//                                                                     |
|                       | VistA filenames                      | XYZ file \#798.1                                                                                                          |
|                       | VistA field names                    | "In the Indicator field, enter the logic that is to be used to determine if the test was positive for the selected MDRO." |
| Courier New, bold     | User responses to screen prompts     | NO                                                                                                                    |
| Courier New, bold     | Keyboard keys                        | \< F1 \>, \< Alt \>, \< L \>, \<Tab\>, \<Enter\>                                                                          |
| Courier New           | Report names                         | Procedures report                                                                                                         |
| Times New Roman       | Body text (Normal text)              | "There are no changes in the performance of the system once the installation process is complete."                        |
| Times New Roman Bold  | Emphasis                             | Note: You can also type the access code, followed by a semicolon, followed by the verify code.                        |

<span id="_Toc393900385" class="anchor"></span>Table 2: Tier Support Contact Information

### References and Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation is also available on the VistA Document Library (VDL) The online versions will be updated as needed. Please look for the latest version on the VDL:

<http://www.va.gov/vdl>

The following documents were used in preparation of this guide:

- LR\*5.2\*463 Patch Description. February 2016.
- MMRS\*1.0\*4 Patch Description. December 2016.
- Microbiology Systems Design Document (SDD). March 2016, version 0.6.
- MMRS\*1.0\*3 User Manual. July 2010, version 1.0
- MMRS\*1.0\*3 Technical Manual. July 2010, version 1.0.

## National Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The four tiers of support documented herein are intended to restore normal service operation as quickly as possible and minimize the adverse impact on business operations, ensuring that the best possible levels of service quality and availability are maintained.

The table below lists organizational contacts needed by site users for troubleshooting purposes. Support contacts are listed by name of service responsible to fix the problem, description of the incident escalation, associated tier level, and contact information.

| Name                                  | Role                   | Organization | Contact Information             |
|-------------------------------------------|----------------------------|------------------|-------------------------------------|
| Clinical Application Coordinator          | Tier 0 Support             | VHA              | To be determined (TBD).             |
| OI&T National Service Desk                | Tier 1 Support             | OI&T             | <span class="mark">REDACTED</span>  |
| OI&T Local Support                        | Tier 2 Support             | OI&T             | <span class="mark">REDACTED</span>  |
| Health Product Support                    | Tier 2 Support             | VHA              | <span class="mark">REDACTED</span>  |
| OI&T System Admin/Field Operation Support | Tier 2 & 3 support         | OI&T             | <span class="mark">REDACTED</span>  |
| VistA Patch Maintenance                   | Tier 3 Application Support | OI&T             | <span class="mark">REDACTED</span>  |
| Enterprise Operations                     | Tier 3 & 4 Support         | OI&T             | OI&T Enterprise Operations Helpdesk |

<span id="_Ref251670564" class="anchor"></span>Table 3: Business Rules for Nares Screening Compliance

# System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the LR\*5.2\*463 patch has been installed and post-installation procedures have been applied, the following organisms will be available for configuration and report generation purposes:

- KLEBSIELLA PNEUMONIAE, CARBAPENEM RESISTANT (CRE)
- KLEBSIELLA OXYTOCA, CARBAPENEM RESISTANT (CRE)
- ESCHERICHIA COLI, CARBAPENEM RESISTANT (CRE)
- ENTEROBACTER CLOACAE, CARBAPENEM RESISTANT (CRE)
- ENTEROBACTER SPP, CARBAPENEM RESISTANT (CRE)

The features and functionality provided in the MMRS\*1.0\*4 patch will provide technicians, MDRO Prevention Coordinators (MPCs) and Infection Prevention (IP) personnel automated tools thereby increasing efficiency and reducing the labor hours required previously with manual data mining.

In regards to enhanced reporting capabilities, the MMRS\*1.0\*4 patch shall provide the following new reporting capabilities:

- CDI reporting functionality shall capture positive cases for the wards of a particular facility.
- CRE reporting functionality shall capture positive cases within a facility.

> **NOTE:** As indicated in the Installation Guide, it is required that patch LR\*5.2\*463 is installed prior to patch MMRS\*1.0\*4.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following diagram depicts the high-level network configuration for a Veteran Affairs Medical Center (VAMC).

> <span id="_Toc461559551" class="anchor"></span>Figure 1: Simplified Topology for one VA Medical Center.

![](mmrs-1-4-user-guide/002.png)

## User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The core intended user base include Information Resource Management (IRM), LIMs and MPCs.

IRM and MPC personnel will be responsible for assigning the MDRO Tools Setup Menu, the MDRO Tools Reports Menu*,* and the MMRS SETUP security key to the appropriate users.

IRM personnel, LIMs, and MPCs will be jointly responsible for setting up the parameter options in the MDRO Tools Setup Menu.

## Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">REDACTED</span>

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides a general walkthrough of the system from initiation through exit. The logical arrangement of the information shall enable the functional personnel to understand the sequence and flow of the system.

1.  Obtain an access code and a verify code from your Clinical Coordinator.
2.  Type in your access and verify codes when prompted.

> **NOTE:** If the MMRS Setup Security key has not been assigned, the user will only have access to the MDRO Tools Reports Menu.

## Logging On

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before you can login, you will need to obtain an access code and a verify code. Typically, your Clinical Coordinator issues these codes.

To login, follow these steps:

> 1\. Open/access the VistA instance on your desktop.

The VistA logo window and the VistA Sign-on dialog will appear.

> 2\. If the Connect To dialog appears, click the down-arrow, select the appropriate account (if more than one exists), and click OK.

> 3\. Type your access code into the Access Code field and press the Tab key.

> 4\. Type the verify code into the verify code field and press the Enter key or click OK.

> **NOTE:** You can also type the access code, followed by a semicolon, followed by the verify code. Once you have completed this process press the Enter key or click OK.

## System Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Various menu options are available to the user. However, it should be noted that a user who <u>does</u> <u>not</u> have the MMRS Setup security key will only have access to the MDRO Tools Reports Menu.

## Changing User ID and Password

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To change your access and verify codes, contact your Clinical Coordinator.

## Exit System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To exit or opt out of answering any question or prompt, enter the carat (^) and the \<ENTER\> key at the field prompt.

## Keyboard Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Text centered between arrows represents a keyboard key that should be pressed in order for the system to capture a user response or to move the cursor to another field. \<Enter\> indicates that the Enter key (or Return key on some keyboards) must be selected. \<Tab\> indicates that the Tab key must be selected. For information on the use of the keys is provided below.

- Use the \<Tab\> key to move the cursor to the next field.
- Use the \<Enter\> to select the default.

One, two, or three question marks can be entered at any of the prompts for online help.

| ?   | One question mark displays a brief statement of what information is appropriate for the prompt.             |
|-----|-------------------------------------------------------------------------------------------------------------|
| ??  | Two question marks provide more help, plus any hidden actions.                                              |
| ??? | Three question marks will provide more detailed help, including a list of possible answers, if appropriate. |

<span id="_Ref251670457" class="anchor"></span>Table 4: MDRO-PT Laboratory Parameter Options

The caret (^) plus the \<Enter\> key can be used to exit the current option.

# Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Program Tools Setup Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the parameters for the six options listed under the MDRO Program Tools Menu. Included in this section are screen captures which contain examples with pre-populated fields. In order to obtain access to the menu, the IRM will need to assign access rights to the MDRO Program Tools Menu and provide the MMRS SETUP key.

The MDRO Tools Setup Menu Options are illustrated in the screen capture below.

<span id="_Toc473541961" class="anchor"></span>Figure 2: MDRO Tools Setup Menu Options

<table>
<caption><p><span id="_Toc268767177" class="anchor"></span>Table 5: Descriptions for MRSA IPEC Admission Report</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MMRS MDRO TOOLS SETUP MENU     MDRO Tools Setup Menu </p>
<p>   1      MRSA Tools Site Parameter Setup <br />
   2      MDRO Tools Lab Parameter Setup <br />
   3      MRSA Tools Ward Mapping Setup <br />
   4      MDRO Historical Days Edit <br />
   5      CRE Tools Site Parameter Setup</p>
<p>6 Isolation Orders Add/Edit</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc268767177" class="anchor"></span>Table 5: Descriptions for MRSA IPEC Admission Report

### MDRO Tools Parameter Setup (Main)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MDRO Tools Parameter Setup menu allows the user(s) to setup the following:

- Divisions for their facility.
- Business rules for nares screening for each division.

When adding divisions, include the following facility areas:

- Acute care hospital(s)
- Community Living Centers

> **NOTE:** When adding divisions, do not include Community Based Outreach Clinics (CBOC), behavioral/mental health facilities, domiciliary facilities, etc.

During parameter setup, the user will have to answer prompts regarding business rules for nares screening on transfer and discharge. Based on the business rules at the facility enter either YES or NO in the prompts.

Business rules for nares screening on transfer and/or discharge instituted by facilities are listed in the table below. Answer either YES or NO if the following prompt/statement is true for your facility.

After the parameters have been configured as directed in the sections that follow, the MDRO Tools parameters should not be changed except under one of the following five conditions:

1.  Changes in business rules for nares screening upon transfer or discharge to ensure the program captures the most current practices.
2.  Adding/Removing a ward/unit from the program.
3.  Ward mapping.
4.  A Lab changes how they report results for the specified MDROs.
5.  Changes have been made to the orderable items used for isolation purposes.

> **NOTE:** The MDRO-PT national package materials (i.e., IPEC Reports) should be reviewed periodically by the sites for data validation.

| Business Rules/Prompts                                            | Respond with: Yes |                                                                                                   | Respond with: No                                                                                                                                                                                                                                                                        |
|-------------------------------------------------------------------|-------------------|---------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Receiving unit screen on unit-to-unit transfers.                  |                   | The receiving unit is responsible for nares screening for unit-to-unit transfers.                 | Only the discharging/sending unit is responsible for screening for unit-to-unit transfers, and not the receiving unit.                                                                                                                                                                  |
| Discharging unit screen on unit-to-unit transfers.                |                   | The discharging/sending unit is responsible for nares screening on unit-to-unit transfers.        | Only the receiving unit is responsible for nares screening on unit-to-unit transfers, and not the discharging unit.                                                                                                                                                                     |
| Screen patients with MRSA history on transfer-in.                 |                   | Patients are screened for MRSA on all transfer-ins, regardless of MRSA status.                    | Nares screens are not required for known MRSA positive patients (i.e., patients with a history of MRSA in the past year) for any transfer-in, via an inter-ward transfer. To be considered 'known positive' the lab result must have been verified before the patient entered the unit. |
| Screen patient with MRSA history on discharge/death/transfer-out. |                   | Patients are screened for MRSA on all discharges/deaths/transfer-outs, regardless of MRSA status. | Nares screens are not required for known MRSA positive patients (i.e., patients with a history of MRSA in the past year) for any discharge, death, or transfer-out. To be considered 'known positive' the lab result must have been verified before the patient left the unit.          |

<span id="_Ref232825538" class="anchor"></span>Table 6: Descriptions for Prevalence Measures (Facility Wide)

<span id="_Toc473541962" class="anchor"></span>Figure 3: MDRO Tools Parameter Setup

<table>
<caption><p><span id="_Ref232825550" class="anchor"></span>Table 7: Descriptions for Prevalence Measures (Unit Specific)</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MDRO Tools Setup Menu Option: <strong>MDRO Tools Parameter Setup</strong></p>
<p>Select MRSA SITE PARAMETERS DIVISION: <strong>XXXXX VAMC</strong></p>
<p>Are you adding 'XXXXX VAMC' as</p>
<p>a new MRSA SITE PARAMETERS (the 1ST)? No// <strong>Y</strong> (Yes)</p>
<p>1. Receiving unit screen on unit-to-unit transfers: <strong>YES</strong></p>
<p>2. Discharging unit screen on unit-to-unit transfers: <strong>YES</strong></p>
<p>3. Screen patients with MRSA history on transfer-in: <strong>YES</strong></p>
<p>4. Screen patients with MRSA history on discharge/death/transfer-out: <strong>YES</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Ref232825550" class="anchor"></span>Table 7: Descriptions for Prevalence Measures (Unit Specific)

> **NOTE:** There should never be a NO listed for both the Receiving unit screen on unit-to-unit transfers and Discharging unit screen on unit-to-unit transfers prompts. This would indicate to the program that neither the receiving nor discharging unit is screening the patients on unit-to-unit transfers.

> **NOTE:** It is required that business rules are added for each division.

## MDRO Tools Lab Parameter Setup Screen and Help Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MDRO Tools Lab Parameter Setup option screen prompts and help prompts definitions are described in the table below.

<table>
<caption><p><span id="_Ref266799883" class="anchor"></span>Table 8: Descriptions for MRSA IPEC Discharge/Transmission Report</p></caption>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th>MDRO Tools Lab Parameter Setup Screen Prompt</th>
<th>MDRO Tools Lab Parameter Setup Screen Help Prompt</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Laboratory Tests(s)</td>
<td>Used only for Chemistry(CH) subscripted tests. This is the test name to identify MRSA nares or CDI CH subscripted tests. Select from the LABORATORY TEST file #60.</td>
</tr>
<tr class="even">
<td>Indicator (for Laboratory Test(s) only)</td>
<td><p>Select the code that will determine how to match lab results:</p>
<p>1 = Use Reference Ranges</p>
<p>2 = Contains</p>
<p>3 = Greater Than</p>
<p>4 = Less Than</p>
<p>5 = Equal To</p></td>
</tr>
<tr class="odd">
<td>Value</td>
<td>Enter POS, Positive, or 1. This is a free text field that allows letters, numbers, punctuation, and spaces. It is not case-sensitive. Answers must be 1-30 characters in length.</td>
</tr>
<tr class="even">
<td>Selected Etiology</td>
<td>Consider synonymous with organism, final microbial diagnosis/<a href="#Glos_isolate">isolate</a>. Select from the ETIOLOGY FIELD file #61.2.</td>
</tr>
<tr class="odd">
<td>Antimicrobial Susceptibility</td>
<td>Enter the antimicrobial that will be used in screening out sensitive Etiologies (e.g., "Oxacillin" for Staphylococcus aureus). Select from the ANTIMICROBIAL SUSCEPTIBILITY file #62.06.</td>
</tr>
<tr class="even">
<td>Indicator (for Antimicrobial Susceptibility only)</td>
<td><p>Select the code that will determine how to match susceptibility interpretations:</p>
<p>1 = Contains</p>
<p>2 = Greater Than</p>
<p>3 = Less Than</p>
<p>4 = Equal To</p></td>
</tr>
<tr class="odd">
<td>Indicated Value</td>
<td><p>Choose a code to report susceptibility to antimicrobial agents:</p>
<p>For example:</p>
<ul>
<li><p>R for Resistant</p></li>
<li><p>S for Susceptible</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Include (for Bacteriology Report Remarks)</td>
<td>Enter information pertaining to positive results. This is a free text field that allows letters, numbers, punctuation, and spaces. Answers must be 1-68 characters in length.</td>
</tr>
<tr class="odd">
<td>Exclude (for Bacteriology Report Remarks)</td>
<td>Enter reporting information pertaining to negative results. This is a free text field that allows letters, numbers, punctuation, and spaces. Answers must be 1-68 characters in length.</td>
</tr>
</tbody>
</table>

<span id="_Ref266799883" class="anchor"></span>Table 8: Descriptions for MRSA IPEC Discharge/Transmission Report

## MDRO Tools Lab Parameter Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to enter laboratory parameters for historical reporting of the following multi-drug resistant organisms (MDROs):

- METHICILLIN-RESISTANT STAPHYLOCOCCUS AUREUS (MRSA)
- CARBAPENEM-RESISTANCE (CRB-R)
- VANCOMYCIN-RESISTANT ENTEROCOCCUS (VRE)
- CLOSTRIDIUM DIFFICILE (C. DIFF)
- EXTENDED-SPECTRUM BETA-LACTAMASE (ESBL)

> **NOTE:** The user may choose to configure all five of the MDROs or may choose to define only the required MDROs; the required MDROs are MRSA and Clostridium difficile. The other MDRO(s) are optional and will only need to be configured if the Print Isolation Report option will be utilized.

> **NOTE:** The following Laboratory Tests do not need to be added to the laboratory parameters setup: MRSA SURVL NARES DNA, MRSA SURVL NARES AGAR, MRSA SURVL OTHER DNA, and MRSA SURVL OTHER AGAR.

> **NOTE:** Do not add STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT to the Selected Etiology section. This information is already available in the program.

### MDRO Tools Lab Parameter Setup for MRSA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Adding Methicillin-resistant Staphylococcus aureus to the MDRO Tools Lab Parameter Setup is <u>mandatory</u>. The purpose of adding this pathogen to the parameter set-up is to identify prior history of MRSA (either by clinical culture or nares screen) based on laboratory reporting. If the facility fails to use the laboratory standards set forth, the program will be unable to generate accurate reports.

Methicillin (or oxacillin)-resistant Staphylococcus aureus (MRSA) is a pathogen of continuing importance for healthcare facilities. It is a Gram-positive coccus that can be resistant to multiple antibiotics, causes serious disease, and is often difficult to treat. It is the cause of healthcare-associated infections (HAIs), and is an emerging pathogen from community-associate sources. MRSA can be cultured from the nares and other sites in patients who are colonized or infected with the organism. It is transmitted, in general, by contact with the hands of patients or health care workers or inanimate objects contaminated with MRSA. Such transmission amplifies the number of patients who may become colonized and who are then at risk for clinical infection.

It is important to capture all positive tests for MRSA, both clinical cultures and surveillance screening tests (e.g., nares screens). Any Staphylococcus aureus isolate that is resistant to Methicillin (or oxacillin) should be captured. Veterans Health Administration (VHA) Laboratory Service must record results of MRSA tests performed using the following methodology:

- MI-subscripted tests will be used for clinical cultures only. STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA) is the only etiology that will be used to report positive clinical cultures.
- CH-subscripted tests will be used for MRSA nares screens or MRSA surveillance cultures. Laboratory is required to use the following test names: MRSA SURVL NARES DNA, MRSA SURVL OTHER DNA, MRSA SURVL NARES AGAR, MRSA SURVL OTHER AGAR.

> **NOTE:** Refer to the "Laboratory Reporting of MRSA Test" for information on how to setup the standardized test names and etiologies.

This option allows the user to enter laboratory parameters for historical reporting of MRSA in the past 12 months. The data entered in using this option will be used by the MRSA IPEC Reports and the MDRO Isolation Report to obtain laboratory information.

> <span id="_Toc473541963" class="anchor"></span>Figure 4: MDRO Tools Lab Parameter Setup Display

<table>
<caption><p><span id="_Toc473542037" class="anchor"></span>Table 10: Descriptions for Census List and MDRO History</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MDRO Tools Setup Menu Option: <strong>MDRO Tools Lab Parameter Setup</strong></p>
<p>Select the Division: <strong>XXXXX VAMC</strong></p>
<p>Select the MDRO: ?</p>
<p>Answer with MDRO TYPES NUMBER, or ABBREVIATION</p>
<p>Choose from:</p>
<p>1 MRSA Methicillin-resistant Staphylococcus aureus</p>
<p>2 CRB-R Carbapenem-Resistance</p>
<p>3 VRE Vancomycin-Resistant Enterococcus</p>
<p>4 C. diff Clostridium difficile</p>
<p>5 ESBL Extended-spectrum beta-lactamase</p>
<p>Select the MDRO: <strong>MRSA</strong></p>
<p>Do you want to see a description for MRSA? YES//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc473542037" class="anchor"></span>Table 10: Descriptions for Census List and MDRO History

1.  Enter the name of the division. Press the \<ENTER\> key.

> Note: If only one division has been set up at the site, this prompt will not be displayed.

2.  Enter MRSA for Methicillin-resistant Staphylococcus aureus and press the \<ENTER\> key.
3.  At the prompt, Do you want to see a description for C. diff?
1.  To view the description, respond with Y and press the \<ENTER\> key twice to view the entire description.
2.  Otherwise, respond with N and press the \<ENTER\> key.
4.  In the Laboratory Test(s) field, enter MRSA and press the \<TAB\> key.
5.  In the Indicator field, enter the logic that is to be used to determine if the test was positive. As this field utilizes a set of codes, enter the code that will determine how to match susceptibility interpretations:
- 1 = Contains
- 2 = Greater Than
- 3 = Less Than
- 4 = Equal To

> After entering the code, press the \<TAB\> key.

6.  In the Value field, enter either POS, Positive, or 1. Press the \<TAB\> key.

> Note: This is a free text field that allows letters, numbers, punctuation, and spaces. It is not case-sensitive. Answers must be 1-30 characters in length. <u>Do</u> <u>not</u> search for negative results.

<span id="_Toc473541964" class="anchor"></span>Figure 5: MDRO Tools Lab Parameter Display for MRSA

<table>
<caption><p><span id="_Toc268767183" class="anchor"></span>Table 11: Descriptions for Nares Screen Compliance List</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: MRSA</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p><strong>MRSA (BY PCR) SCREEN Contains POS</strong></p>
<p>Selected Etiology</p>
<p>____________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc268767183" class="anchor"></span>Table 11: Descriptions for Nares Screen Compliance List

7.  Configure the MDRO by following the instructions below for either Chemistry (CH) subscripted tests or Microbiology (MI) subscripted tests:
    1.  Select the CH-subscripted test from the LABORATORY TEST file (#60) and press the \<TAB\> key.

> Note: The system will not let you choose a test with a subscript field (Field \#4 in File \#60) set to anything other than CH. Laboratory is required to use the following test names: MRSA SURVL NARES DNA, MRSA SURVL OTHER DNA, MRSA SURVL NARES AGAR, MRSA SURVL OTHER AGAR.

2.  For MI-subscripted tests, the Selected Etiology field will be used. Select the etiology from the ETIOLOGY FIELD file (#61.2). For example, enter STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT and press the \<TAB\> key.

> Note: STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA) is the only etiology that will be used to report positive clinical cultures.

> Note: Refer to the "Laboratory Reporting of MRSA Test" for information on how to setup the standardized test names and etiology.

<span id="_Toc473541965" class="anchor"></span>Figure 6: MDRO Tools Parameter Setup for MRSA Selected Etiology

<table>
<caption><p><span id="_Toc473542039" class="anchor"></span>Table 12: Descriptions for Excel™ spreadsheet CDI Reporting Tool</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: MRSA</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p>MRSA (BY PCR) SCREEN Contains POS</p>
<p>Selected Etiology</p>
<p><strong>STAPHYLOCOCCUS AUREUS</strong></p>
<p>______________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc473542039" class="anchor"></span>Table 12: Descriptions for Excel™ spreadsheet CDI Reporting Tool

8.  Enter the Antimicrobial Susceptibility for the organism and press the \<TAB\> key.

> Note: Utilize the Susceptibility Template that is appropriate for the site.

> Note: If an antimicrobial susceptibility is not entered, the program will consider the result positive. However, if an antimicrobial susceptibility is entered, the program will only consider the result positive if the organism meets the condition that is entered for one of the antimicrobials; for example, if Oxacillin Contains R (R for resistant) is entered in the Antimicrobial Susceptibility section for the Staphylococcus Aureus organism, then the test result will only be considered positive if it contains that organism, and it is Oxacillin Resistant.

> If more than one antimicrobial susceptibility is entered, the program will consider the result positive if one of the antimicrobial susceptibilities entered matches the indicated value.

9.  Enter the code for the Indicator field that will determine how to match susceptibility interpretations:
- 1 = Contains
- 2 = Greater Than
- 3 = Less Than
- 4 = Equal To
10. In the Indicated Value field, enter a code to report the susceptibility to antimicrobial agents and press the \<ENTER\> key:
- R for Resistant
- S for Susceptible

> <span id="_Toc473541966" class="anchor"></span>Figure 7: MDRO Tools Parameter Setup for MRSA Antimicrobial Susceptibility

<table>
<caption><p><span id="_Toc473542040" class="anchor"></span>Table 13: CRE Print Descriptions</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: MRSA</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p>MRSA (BY PCR) SCREEN Contains POS</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Selected Etiology</p>
<p>STAPHYLOCOCCUS AUREUS</p>
<table>
<caption><p><span id="_Toc473542041" class="anchor"></span>Table 14: MAS Movement Program Explanations</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ANTIMICROBIAL SUSCEPTIBILITY INDICATOR INDICATED VALUE</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>OXACILLIN Contains R</strong></td>
</tr>
</tbody>
</table>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></td>
</tr>
</tbody>
</table>

<span id="_Toc473542040" class="anchor"></span>Table 13: CRE Print Descriptions

11. If desired, enter information in the second page of the form for the Bacteriology Report Remarks. Use discernment when entering information into the Bacteriology Report Remarks as it is a free text field and therefore introduces risk for entering information incorrectly which will adversely affect the results generated by the program.
    1.  If desired, enter reporting information pertaining to positive results into the Include field. This is a free text field that allows letters, numbers, punctuation, and spaces. Answers must be 1-68 characters in length.
    2.  If desired, enter reporting information pertaining to negative results into the Exclude field. This is a free text field that allows letters, numbers, punctuation, and spaces. Answers must be 1-68 characters in length.

> Note: To include the positive results and exclude the negative results, use both the Include and the Exclude fields. For example, for molecular based tests, the following two phrases are commonly used: MRSA DNA DETECTED for positive results and NO MRSA DNA DETECTED for negative results. If NO MRSA DNA DETECTED has not been entered in the Exclude section, then a result that has the remark NO MRSA DNA DETECTED will be considered positive.

12. At the prompt, Save changes before leaving form (Y/N)? Respond with Y and press the \<ENTER\> key.
13. At the Command prompt, enter E to exit the form(s).

<span id="_Toc473541967" class="anchor"></span>Figure 8: MDRO Bacteriology Report Remarks Display for MRSA

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 2 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: MRSA</p>
<p>________________________________________________________________________</p>
<p>BACTERIOLOGY REPORT REMARKS</p>
<p>Include Exclude</p>
<p><strong>MRSA DNA DETECTED NO MRSA DNA DETECTED</strong></p>
<p>________________________________________________________________________</p>
<p>Exit Save Next Page Refresh</p>
<p>Enter a command or '^' followed by a caption to jump to a specific field.</p>
<p>Save changes before leaving form (Y/N)? Y Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### MDRO Tools Lab Parameter Setup for Carbapenem-Resistance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Carbapenems are a class of beta-lactam antibiotics with a broad spectrum of antibacterial activity. These agents have the broadest antibacterial spectrum compared to other beta-lactam classes. They are active against both Gram positive and Gram negative bacteria, and can be used to treat nosocomial and mixed bacterial infections. Resistance to carbapenems is of importance because it limits therapeutic options.  

> **NOTE:** The purpose of adding carbapenem-resistant enterobacteriacea (CRE) etiologies to the MDRO Tools Lab Parameter Setup is to identify a patient's current or prior history of CRE based on laboratory reporting and the time frames that are entered to search for the patient's status. The result must occur as a CRE bacterial etiology and any result contained in a "free-text" section will not allow incorporation of the CRE into the MDRO Program Tools software.

> **NOTE:** If desired, configure the Lab Parameter for CRE for multiple divisions. Setup the divisions according to local facility policy.

1.  Enter the name of the division. Press the \<ENTER\> key.

> Note: If only one division has been set up at the site, this prompt will not be displayed.

2.  Enter CRB-R for Carbapenem-Resistance and press the \<ENTER\> key.
3.  At the prompt, Do you want to see a description for CRB-R?
    1.  To view the description, respond with Y and press the \<ENTER\> key twice to view the entire description.
    2.  Otherwise, respond with N and press the \<ENTER\> key.
4.  In the Laboratory Test(s) field, press the \<TAB\> key to leave the field blank.
5.  In the Indicator field, press the \<TAB\> key to leave the field blank.
6.  In the Value field, press the \<TAB\> key to leave the field blank.

> <span id="_Toc473541968" class="anchor"></span>Figure 9: MDRO Tools Lab Parameter Display for CRB-R

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: CRB-R</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p>Selected Etiology</p>
<p>____________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

7.  For MI-subscripted tests, the Selected Etiology field will be used. Select the etiology from the ETIOLOGY FIELD file (#61.2) For example, enter part of the etiology name; for example, enter kleb to display a list associated with KLEBSIELLA. Select the etiology from the list. After the installation of patch LR\*5.2\*463, the following etiologies will be available for configuration:
- KLEBSIELLA PNEUMONIAE, CARBAPENEM RESISTANT (CRE)
- KLEBSIELLA OXYTOCA, CARBAPENEM RESISTANT (CRE)
- ESCHERICHIA COLI, CARBAPENEM RESISTANT (CRE)
- ENTEROBACTER CLOACAE, CARBAPENEM RESISTANT (CRE)
- ENTEROBACTER SPP, CARBAPENEM RESISTANT (CRE)
  1.  Enter the name of <u>each</u> etiology from the Etiology Field File and press the \<ENTER\> key until all five of the etiologies listed above have been entered.

<span id="_Toc473541969" class="anchor"></span>Figure 10: MDRO Tools Parameter Setup for Selected Etiology

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: CRB-R</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p>Selected Etiology</p>
<p><strong>KLEBSIELLA PNEUMONIAE (CRE)</strong></p>
<p><strong>KLEBSIELLA OXYTOCA, CARBAPENEM RESISTANT (CRE)                       </strong><br />
<strong>ESCHERICHIA COLI, CARBAPENEM RESISTANT (CRE)                         </strong><br />
<strong>ENTEROBACTER CLOACAE, CARBAPENEM RESISTANT (CRE)                     </strong><br />
<strong>ENTEROBACTER SPP, CARBAPENEM RESISTANT (CRE)</strong></p>
<p>______________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

8.  <u>Do</u> <u>not</u> enter the Antimicrobial Susceptibility for the organism. Select the \<TAB\> key to exit.

> **NOTE:** When the antimicrobial susceptibility is not entered, the program will consider the result positive. Only positive results will be obtained.

9.  At the Command prompt, select the \<ENTER\> key to accept the default to close the form.
10. At the prompt, Save changes before leaving form (Y/N)? Respond with Y and press the \<ENTER\> key.
11. At the Command prompt, enter E to exit the form(s).

### MDRO Tools Lab Parameter Setup for Vancomycin-Resistant Enterococcus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Adding Vancomycin-resistant Enterococcus (VRE) to the MDRO Tools Lab Parameter Setup is optional. The purpose of adding VRE to the parameter set-up is to identify a patient's current or prior history of the MDRO. This information can optionally be displayed on the Isolation Report and will include positive cultures for prevalence and surveillance review, with specimens of stool and rectal swabs.

VRE is a pathogen of increasing importance for healthcare facilities. Enterococcus is a bacterium that lives in the intestinal tract and in the female genital tract. Vancomycin is an antibiotic that is often used to treat infections caused by enterococci, and recently enterococci have become resistant to this drug. Most VRE infections occur in the hospital.

> **NOTE:** The laboratory parameter setup for the MDRO Program Tools should match the same parameter setup for the EPI (Emerging Pathogens Initiative). If changes are made to how VRE is reported it should also be changed in EPI parameter setup.

1.  Enter the name of the division. Press the \<ENTER\> key.

> Note: If only one division has been set up at the site, this prompt will not be displayed.

2.  Enter VRE for Vancomycin-resistant Enterococcus and press the \<ENTER\> key.
3.  At the prompt, Do you want to see a description for VRE?
1.  To view the description, respond with Y and press the \<ENTER\> key twice to view the entire description.
    1.  Otherwise, respond with N and press the \<ENTER\> key.
4.  In the Laboratory Test(s) field, press the \<TAB\> key.
5.  In the Indicator field, press the \<TAB\> key.
6.  In the Value field, press the \<TAB\> key.

> <span id="_Toc473541970" class="anchor"></span>Figure 11: MDRO Tools Lab Parameter Display for VRE

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: VRE</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p>Selected Etiology</p>
<p>____________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

7.  For MI-subscripted tests, the Selected Etiology field will be used. Select the etiology from the ETIOLOGY FIELD file (#61.2). Enter the name of the etiology, for example, ENTEROCOCCUS, and press the \<TAB\> key.

> <span id="_Toc473541971" class="anchor"></span>Figure 12: MDRO Tools Parameter Setup for Selected Etiology

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: VRE</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p>Selected Etiology</p>
<p><strong>ENTEROCOCCUS</strong></p>
<p>______________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

8.  Enter the code for the Indicator field that will determine how to match susceptibility interpretations:
- 1 = Contains
- 2 = Greater Than
- 3 = Less Than
- 4 = Equal To
9.  In the Indicated Value field, enter a code to report the susceptibility to antimicrobial agents and press the \<ENTER\> key:
- R for Resistant
- S for Susceptible
10. At the prompt, Save changes before leaving form (Y/N)? Respond with Y and press the \<ENTER\> key.
11. At the Command prompt, enter E to exit the form(s).

> <span id="_Toc473541972" class="anchor"></span>Figure 13: MDRO Tools Parameter Setup for Antimicrobial Susceptibility

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: VRE</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Selected</p>
<p>ENTEROCOCCUS</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ANTIMICROBIAL SUSCEPTIBILITY INDICATOR INDICATED VALUE</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>VANCOMYCIN Contains R</strong></td>
</tr>
</tbody>
</table>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></td>
</tr>
</tbody>
</table>

### MDRO Tools Lab Parameter Setup for Clostridium difficile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clostridium difficile (C. difficile or C. diff) is a species of gram-positive bacteria. The disease is associated with the presence of Clostridium difficile enterotoxin, which can cause significant morbidity, as well as mortality. It is of importance, as its predominant acquisition appears to occur nosocomially and is the most serious cause of antibiotic-associated diarrhea. Presence of clostridium toxin (either enterotoxin or cytotoxin L) by assay (whether it be EIA, latex agglutination, cytotoxicity of cell culture neutralization, or culture of organism with subsequent colony testing) is the best indicator that an inflammatory diarrheal disease is due to presence of Clostridium difficile.

 Laboratory services are quite varied as to how they identify the presence of Clostridium difficile. Some labs are set up to identify C. difficile as the final microbiological (bacterial) etiology of a culture, even if a culture method was not used. Other labs use a final etiology of "see comment" and then enter the results in a free text format. Still others enter the text under a hematology or chemistry format where a reference range and "positive" and "negative" result values can be entered.   Wherever the VHA Laboratory Service places the results, which are used to demonstrate the presence of toxin-producing C. difficile, should be accessible as a standardized field in order to allow the MDRO Programs Tool software to capture its presence.  

> **NOTE:** The purpose of adding Clostridium difficile to the MDRO Tools Lab Parameter Setup is to identify a patient's current or prior history of Clostridium difficile based on laboratory reporting and the time-frames that are entered to search for the patient's status.  The result must occur as a Clostridium difficile (a bacterial etiology) or as a retrievable "positive" result for a chemistry/serology laboratory test. Any results contained in a "Free-Text" section will not allow incorporation of Clostridium difficile into the MDRO Program Tools/Print CDI Report format. 

1.  Enter the name of the division. Press the \<ENTER\> key.

> Note: If only one division has been set up at the site, this prompt will not be displayed.

2.  Enter C. diff for Clostridium difficile and press the \<ENTER\> key.
3.  At the prompt, Do you want to see a description for C. diff?
    1.  To view the description, respond with Y and press the \<ENTER\> key twice to view the entire description.
    2.  Otherwise, respond with N and press the \<ENTER\> key.

> Note: The instructions provided below are in regard to the configuration of Laboratory Tests and Etiologies. Facilities have the option of configuring for Laboratory Tests only, Etiologies only, or for configuring for both Lab Tests and Etiologies.

4.  In the Laboratory Test(s) field, enter the exact name of the C. diff toxin that has been configured, for example, CLOSTRIDUM DIFFICILE TOXIN. Press the \<TAB\> key.
5.  In the Indicator field, enter Contains and press the \<TAB\> key.
6.  In the Value field, enter POS and press the \<TAB\> key.

> Note: This is a free text field that allows letters, numbers, punctuation, and spaces; it is not case-sensitive. Answers must be 1-30 characters in length. <u>Do</u> <u>not</u> search for negative results.

<span id="_Toc473541973" class="anchor"></span>Figure 14: MDRO Tools Lab Parameter Display for C. Diff

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: C. diff</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p><strong>CLOSTRIDUM DIFFICILE TOXIN CONTAINS POS</strong></p>
<p>Selected Etiology</p>
<p>____________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

7.  For MI-subscripted tests, the Selected Etiology field will be used. Select CLOSTRIDIUM DIFFICILE from the ETIOLOGY FIELD file (#61.2).
8.  <u>Do</u> <u>not</u> enter the Antimicrobial Susceptibility for the organism. Select the \<TAB\> key to exit.

> Note: When the antimicrobial susceptibility is not entered, the program will consider the result positive. Only positive results will be obtained for C. diff.

9.  At the command prompt, type Close and press the \<ENTER\> key.
10. Press the \<TAB\> key.
11. At the command prompt, type S to save the form and press the \<ENTER\> key.
12. At the command prompt, type E to exit and press the \<ENTER\> key.

> Note: When the antimicrobial susceptibility is not entered, or the field is left blank, the program will consider the result <u>positive</u>. Only positive results will be obtained for C. diff.

<span id="_Toc473541974" class="anchor"></span>Figure 15: MDRO Tools Parameter Setup for Selected Etiology

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: C. diff</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p>CLOSTRIDUM DIFFICILE TOXIN CONTAINS POS</p>
<p>Selected Etiology</p>
<p><strong>CLOSTRIDIUM DIFFICILE</strong></p>
<p>______________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### MDRO Tools Lab Parameter Setup for Extended-Spectrum Beta-Lactamase

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Adding Extended-Spectrum Beta-Lactamase (ESBL) to the MDRO Tools Lab Parameter setup is optional. The purpose of adding pathogens containing this form of antimicrobial resistance to the parameter set-up is to identify a patient's current or prior history of ESBL. This information can optionally be displayed on the Isolation Report. To find and display this information, enter information into the Bacteriology Report Remarks section.

ESBLs are enzymes that mediate resistance to extended-spectrum (third generation) cephalosporins (e.g., ceftazidime, cefotaxime, and ceftriaxone) and monobactams (e.g., aztreonam) but do not affect cephamycins (e.g., cefoxitin and cefotetan) or carbapenems (e.g., imipenem or meropenem).

ESBLs can be difficult to detect because they have different levels of activity against various cephalosporins. It is critical to test the appropriate antimicrobial agent, thus an appropriate Committee on Laboratory Standards Institute (CLSI) testing schema should be utilized. If an isolate is confirmed as an ESBL-producer by the CLSI-recommended phenotypic confirmatory test procedure, then all penicillins, cephalosporins and aztreonams should be reported as resistant. Cephamycins should be reported according to their routine test results.

> **NOTE:** Any information contained in a free-text section will not allow incorporation of ESBL into the Isolation Report.

1.  Enter the name of the division. Press the \<ENTER\> key.

> Note: If only one division has been set up at the site, this prompt will not be displayed.

2.  Enter ESBL for Extended-Spectrum Beta-Lactamase and press the \<ENTER\> key.
3.  At the prompt, Do you want to see a description for ESBL?
    1.  To view the description, respond with Y and press the \<ENTER\> key twice to view the entire description.
    2.  Otherwise, respond with N and press the \<ENTER\> key.
4.  In the Laboratory Test(s) field, press the \<TAB\> key.
5.  In the Indicator field, press the \<TAB\> key.
6.  In the Value field, press the \<TAB\> key.

> <span id="_Toc473541975" class="anchor"></span>Figure 16: MDRO Tools Lab Parameter Display for ESBL

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: ESBL</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p>Selected Etiology</p>
<p>____________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

7.  For MI-subscripted tests, the Selected Etiology field will be used. Select the etiology from the ETIOLOGY FIELD file (#61.2). In the example below, ESCHERICHIA COLI was entered. Enter the name of the etiology and press the \<TAB\> key.

> <span id="_Toc473541976" class="anchor"></span>Figure 17: MDRO Tools Parameter Setup for Selected Etiology

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: ESBL</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p>Selected Etiology</p>
<p><strong>ESCHERICHIA COLI</strong></p>
<p>______________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

8.  Enter the Antimicrobial Susceptibility for the organism.

> Note: If an antimicrobial susceptibility is not entered, the program will consider the result positive. However, if an antimicrobial susceptibility is entered, the program will only consider the result positive if the organism meets the condition that is entered for one of the antimicrobials; for example, if Meropenem Contains R (R for resistant) is entered in the Antimicrobial Susceptibility section for the organism, then the test result will only be considered positive if it contains that organism, and it is Meropenem Resistant.

> Note: If more than one antimicrobial susceptibility is entered, the program will consider the result positive if one of the antimicrobial susceptibilities entered matches the indicated value.

9.  In the Indicator field, enter the logic that is to be used to determine if the test was positive. As this field utilizes a set of codes, enter the code that will determine how to match susceptibility interpretations:
- 1 = Contains
- 2 = Greater Than
- 3 = Less Than
- 4 = Equal To

> After entering the code, press the \<TAB\> key.

10. In the Indicated Value field, enter a code to report the susceptibility to antimicrobial agents and press the \<ENTER\> key:
- R for Resistant
- S for Susceptible

> <span id="_Toc473541977" class="anchor"></span>Figure 18: MDRO Tools Parameter Setup for Antimicrobial Susceptibility

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: ESBL</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Selected</p>
<p>ESCHERICHIA COLI</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ANTIMICROBIAL SUSCEPTIBILITY INDICATOR INDICATED VALUE</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CEFPODOXIME Contains R</strong></td>
</tr>
</tbody>
</table>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></td>
</tr>
</tbody>
</table>

14. If desired, enter information in the second page of the form for the Bacteriology Report Remarks. Use discernment when entering information into the Bacteriology Report Remarks as it is a free text field and therefore introduces risk for entering information incorrectly which will adversely affect the results generated by the program.
    1.  If desired, enter reporting information pertaining to positive results into the Include field. This is a free text field that allows letters, numbers, punctuation, and spaces. Answers must be 1-68 characters in length.
    2.  If desired, enter reporting information pertaining to negative results into the Exclude field. This is a free text field that allows letters, numbers, punctuation, and spaces. Answers must be 1-68 characters in length.

> Note: To include the positive results and exclude the negative results, use both the Include and the Exclude fields. For example, for molecular based tests, the following two phrases are commonly used: ESBL POSITIVE for positive results and NOT ESBL POSITIVE for negative results. If NOT ESBL POSITIVE has not been entered in the Exclude section, then a result that has the remark NOT ESBL POSITIVE will be considered positive.

15. At the prompt, Save changes before leaving form (Y/N)? Respond with Y and press the \<ENTER\> key.
16. At the Command prompt, enter E to exit the form(s).

> <span id="_Toc473541978" class="anchor"></span>Figure 19: Bacteriology Report Remarks

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 2 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: ESBL</p>
<p>________________________________________________________________________</p>
<p>BACTERIOLOGY REPORT REMARKS</p>
<p>Include Exclude</p>
<p><strong>ESBL POSITIVE NOT ESBL POSITIVE</strong></p>
<p>________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### MDRO Tools Lab Parameter Setup: Deleting Information Previously Entered

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Facilities may delete information that has been previously entered from the following fields:

- Laboratory Test
- Selected (Etiology)
- Antimicrobial Susceptibility
- Bacteriology Report Remarks

To delete information previously entered, perform the following steps:

1.  Go to the field where the change needs to occur and place the @ symbol in the field.
2.  When prompted, Are you sure you want to delete this entire Subrecord (Y/N)? respond with Y with the \<ENTER\> key to delete the information from the field.

> <span id="_Toc473541979" class="anchor"></span>Figure 20: Deleting information from MDRO Tools Lab Parameters Setup

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MDRO TOOLS LAB SEARCH/EXTRACT PARAMETERS SETUP Page 1 of 2</p>
<p>DIVISION: XXXXX VAMC MDRO: MRSA</p>
<p>______________________________________________________________________________</p>
<p>Laboratory Test(s) Indicator Value</p>
<p>MRSA (BY PCR) SCREEN Contains POS</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Selected</p>
<p>STAPHYLOCOCCUS AUREUS</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>ANTIMICROBIAL SUSCEPTIBILITY INDICATOR INDICATED VALUE</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>@</strong> Contains R</td>
</tr>
</tbody>
</table>
<p>WARNING: DELETIONS ARE DONE IMMEDIATELY!</p>
<p>(EXITING WITHOUT SAVING WILL NOT RESTORE DELETED RECORDS.)</p>
<p>Are you sure you want to delete this entire Subrecord (Y/N)? <strong>Y</strong></p></td>
</tr>
</tbody>
</table>

## MRSA Tools Ward Mapping Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to define geographical units within each division for the purpose of running reports. A geographical unit can consist of one or more wards listed in VistA, and for all intents and purposes is considered one unit. Units may be mapped or grouped together for reporting purposes. For example, one unit may be divided into Unit X Medicine and Unit X Surgery, but is one geographical unit. By mapping the wards (e.g., Unit X Med-Surg), the report will consider all the wards mapped together as one location and all transfers between Unit X Medicine and Unit X Surgery will be ignored.

> **NOTE:** Ward mappings must be configured for every unit for the purpose of running reports.

To configure the MRSA Tools Ward Mapping, perform the following steps:

1.  When prompted, enter the name of the Unit to either create a new Geographical Unit or to edit an existing one.

> Note: When adding a new location, use discretion and enter a descriptive name.

2.  When prompted, enter the MRSA Ward Mappings Type and IPEC Unit ID.

> Note: This information is required for the program to extract the data for upload to the IPEC website for data reporting purposes.

3.  For the Location Type, choose from the following: Acute Care (AC), Community Living Center (CLC), Observation (OBS), or Other(OT).
4.  When prompted, enter the location's IPEC Unit ID.

> Note: This is the ID number that identifies this unit in IPEC which is only for Acute Care and CLC units reported to IPEC. <u>Do</u> <u>not</u> assign a Unit ID to any unit that is classified as OBS or Other. IPEC Unit IDs are available from the VHA MRSA Program Office and/or IPEC.

5.  When prompted, enter the ward(s) in VistA to be included in the Geographical Unit.

> Note: OBS patients should not be included in the number of admissions, discharges, and bed days of care that is reported to IPEC for the inpatient units; these patients are considered outpatients. Therefore, sites should not generate a MRSA IPEC Report for any OBS units. However, if desired, the site may run the Isolation Report or Nares Screen Compliance List for an OBS unit.

> In order to prevent data from OBS wards erroneously reported to IPEC, sites should not map any OBS wards together with an inpatient ward (Acute Care or CLC). If the site desires the generation of the Isolation Report or Nares Screen Compliance List for an OBS unit, a separate Geographical Location should be utilized that includes the OBS ward only. For example, a site may have three wards in VistA entitled "4West Medicine", "4West Surgery" and "4West OBS" and may desire to create a Geographical Location entitled "4West"; "4West" could consist of "4West Medicine" and "4West Surgery". In another scenario, a site may also wish to create a separate Geographical Location called "4West OBS" that could contain the "4West OBS" ward only. However, in these examples, under no circumstances should the "4West OBS" ward be mapped together with the "4West Medicine" and "4West Surgery" wards under the same Geographical Location.

6.  Enter the \<TAB\> key to get to the Command prompt.
7.  At the command prompt, enter S and the \<ENTER\> key to save.
8.  At the command prompt, enter E and the \<ENTER\> key to exit.
9.  To return to the main menu, enter ^ and the \<ENTER\> key.

<span id="_Toc473541980" class="anchor"></span>Figure 21: MDRO Tools Ward Mapping Setup

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MDRO Tools Setup Menu Option: <strong>MDRO Tools Ward Mapping Setup</strong></p>
<p>Select Geographical Unit: <strong>11AB</strong></p>
<p>  Are you adding '11AB' as a new MRSA WARD MAPPINGS (the 2ND)? No// <strong>Y</strong>  (Yes)</p>
<p>   MRSA WARD MAPPINGS TYPE: <strong>ACUTE CARE</strong></p>
<p>   MRSA WARD MAPPINGS IPEC UNIT ID: <strong>999</strong></p>
<p>MDRO TOOLS WARD MAPPING SETUP</p>
<p>DIVISION: XXXXX VAMC                        </p>
<p>GEOGRAPHICAL UNIT: 11AB                         </p>
<p>_____________________________________________________________________________</p>
<p>WARD LOCATIONS:</p>
<p><strong>11AB                         </strong></p>
<p><strong>11ASURG                      </strong></p>
<p>                     </p>
<p>_____________________________________________________________________________</p>
<p>COMMAND:                                                Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Deleting a Geographical Unit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To delete a Geographical Unit, perform the following steps:

1.  Select the desired geographical unit.
2.  Enter the @ symbol and press the \<ENTER\> key.
3.  When prompted, SURE YOU WANT TO DELETE THE ENTIRE 'UNIT NAME' MRSA WARD MAPPINGS? respond with Y and the \<ENTER\> key to delete the entire geographical unit from the setup.

he prograhe program will ask if the desired field shoulto beuser can delete this information. To do so, <span id="_Toc473541981" class="anchor"></span>Figure 22: MDRO Tools Ward Mapping Setup: Deleting a Geographical Unit

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MDRO Tools Setup Menu Option: <strong>MDRO Tools Ward Mapping Setup</strong></p>
<p>DIVISION: <strong>XXXXX VAMC</strong>                        </p>
<p>SELECT GEOGRAPHICAL UNIT: <strong>PACU</strong>                         </p>
<p>_____________________________________________________________________________</p>
<p>NAME: PACU//<strong>@</strong></p>
<p>SURE YOU WANT TO DELETE THE ENTIRE 'PACU' MRSA WARD MAPPINGS? <strong>Y</strong> (Yes)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## MDRO Historical Days Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to define the time frame selected for each MDRO defined in the MDRO Tools Lab Parameter Setup. The information entered in this menu provides information for the Print Isolation Report option (the report displays patient's historical lab data for certain MDROs). The user will be asked to enter the number of historical days the program should search for a positive result for each MDRO. This information can only be entered in days (e.g., 30 for 1 month; 90 for 1 quarter; 365 for 1 year). If no response is entered, the program will not display that MDRO on the Isolation Report.

> **NOTE:** All sites must enter the following for MRSA in historical days: 365; this will ensure that the history of MRSA within the past year is identified for prevalence and transmission purposes.

For other MDROs selected, it is at the discretion of the facility to determine the time frame to search for the last positive MDRO result.

1.  Select the division by entering it. Press the \<ENTER\> key. For a list of divisions, enter a ?
2.  When prompted, enter the number of historical days the program should search for a positive result for each MDRO.

<span id="_Toc473541982" class="anchor"></span>Figure 23: MDRO Historical Days Edit

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MDRO Tools Setup Menu Option: <strong>MDRO Historical Days Edit</strong></p>
<p>Select the Division: <strong>XXXXX VAMC</strong></p>
<p>Enter the number of days to search for MRSA: <strong>365</strong></p>
<p>Enter the number of days to search for IMP: <strong>365</strong></p>
<p>Enter the number of days to search for VRE: <strong>365</strong></p>
<p>Enter the number of days to search for C. diff: <strong>28</strong></p>
<p>Enter the number of days to search for ESBL: <strong>365</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## CRE Tools Site Parameter Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CRE Tools Parameter Setup menu allows the user(s) to configure the CRE parameters for division(s) by either adding or editing specimens.

1.  When prompted, enter the name of the division and press the \<ENTER\> key or press the ? for a list of divisions and select the division from the list.
2.  When prompted, select either Add to add a specimen for CRE Surveillance Screens or Edit to edit an existing specimen.
    1.  If adding a specimen, type Add and press the \<ENTER\> key. Enter the name of the specimen and press the \<ENTER\> key.
    2.  If editing a specimen, type Edit and press the \<ENTER\> key. Enter the name of the specimen and press the \<ENTER\> key. To obtain a list of specimens, type ? and the \<ENTER\> key.

<span id="_Toc473541983" class="anchor"></span>Figure 24: CRE Tools Site Parameter Setup: Add a Specimen

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MDRO Tools Setup Menu &lt;FACILITY ACCOUNT&gt; Option: 5 CRE Tools Site Parameter</p>
<p>Setup</p>
<p>Select CRE Site Parameters Division: ?</p>
<p>Answer with MDRO SITE PARAMETERS DIVISION</p>
<p>Choose from:</p>
<p>CASPER</p>
<p>CHEYENNE MOC</p>
<p>CHEYENNE VAMROC</p>
<p>FORT COLLINS</p>
<p>GREELEY</p>
<p>SIDNEY</p>
<p>You may enter a new MDRO SITE PARAMETERS, if you wish Enter the division the parameters are for.</p>
<p>Answer with MEDICAL CENTER DIVISION NUM, or NAME</p>
<p>Choose from:</p>
<p>1 CHEYENNE VAMROC 442</p>
<p>2 CASPER 442GA</p>
<p>3 FORT COLLINS 442GC</p>
<p>4 GREELEY 442GD</p>
<p>5 SIDNEY 442GB</p>
<p>6 CHEYENNE MOC 442HK</p>
<p>Select CRE Site Parameters Division: 1 CHEYENNE VAMROC 442</p>
<p>...OK? Yes// (Yes)</p>
<p>Select one of the following:</p>
<p>A ADD</p>
<p>E EDIT</p>
<p>Do you want to Add or Edit specimen(s) for CRE Surveillance Screens: E// ADD</p>
<p>Select Specimen: FECES</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc473541984" class="anchor"></span>Figure 25: CRE Tools Site Parameter Setup: Edit a Specimen

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MDRO Tools Setup Menu &lt;FACILITY ACCOUNT&gt; Option: 5 CRE Tools Site Parameter</p>
<p>Setup</p>
<p>Select CRE Site Parameters Division: ?</p>
<p>Answer with MDRO SITE PARAMETERS DIVISION</p>
<p>Choose from:</p>
<p>CASPER</p>
<p>CHEYENNE MOC</p>
<p>CHEYENNE VAMROC</p>
<p>FORT COLLINS</p>
<p>GREELEY</p>
<p>SIDNEY</p>
<p>You may enter a new MDRO SITE PARAMETERS, if you wish Enter the division the parameters are for.</p>
<p>Answer with MEDICAL CENTER DIVISION NUM, or NAME</p>
<p>Choose from:</p>
<p>1 CHEYENNE VAMROC 442</p>
<p>2 CASPER 442GA</p>
<p>3 FORT COLLINS 442GC</p>
<p>4 GREELEY 442GD</p>
<p>5 SIDNEY 442GB</p>
<p>6 CHEYENNE MOC 442HK</p>
<p>Select CRE Site Parameters Division: 1 CHEYENNE VAMROC 442</p>
<p>...OK? Yes// (Yes)</p>
<p>Select one of the following:</p>
<p>A ADD</p>
<p>E EDIT</p>
<p>Do you want to Add or Edit specimen(s) for CRE Surveillance Screens: E// EDIT</p>
<p>Select Specimen to delete: ?</p>
<p>Answer with SPECIMEN</p>
<p>Choose from:</p>
<p>FECES</p>
<p>SKIN</p>
<p>Enter the specimen you want to edit.</p>
<p>Select Specimen to delete: FECES</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Isolation Orders Add/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Isolation Orders Add/Edit option allows the user to enter the orderable item(s) at their site that are used for isolation purposes. Each Isolation Order added must be mapped to one of the following Expanded Precaution Types: Contact Precautions, Contact Precautions Special, Airborne Infection, Droplet, Protective Environment, and Isolation Order. The information entered will be used to populate the Print Isolation Report option.

> **NOTE:** This option should only be used if the site uses orderable items when a patient is required to be in isolation.

1.  Select the division.
2.  At the Isolation Orders, enter an order and press \<TAB\>
3.  At the Expanded Precaution Type, enter a precaution type and press \<TAB\> to return to the Isolation Orders field.
4.  When finished, enter the \<TAB\> key at the Isolation Orders field.
5.  At the Command prompt, enter S to save the form and press the \<ENTER\> key.
6.  At the Command prompt, enter E to exit the form and press the \<ENTER\> key.

<span id="_Toc473541985" class="anchor"></span>Figure 26: MDRO Tools Isolation Orders Setup

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MDRO TOOLS ISOLATION ORDERS SETUP</p>
<p>DIVISION: XXXXX VAMC</p>
<p>___________________________________________________________________________</p>
<p>Isolation Orders Expanded Precaution Type</p>
<p><strong>CONTACT PRECAUTIONS CONTACT PRECAUTIONS</strong></p>
<p><strong>CONTACT PRECAUTIONS SPECIAL CONTACT PRECAUTIONS SPECIAL</strong></p>
<p><strong>AIRBORNE INFECTION ISOLATIOTI AIRBORNE INFECTION</strong></p>
<p><strong>DROPLET PRECAUTIONS DROPLET</strong></p>
<p><strong>PROTECTIVE ENVIRONMENT PROTECTIVE ENVIRONMENT</strong></p>
<p><strong>ISOLATION ORDER ISOLATION ORDER</strong></p>
<p>__________________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## MDRO Tools Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the five options in the MRSA Tools Setup Menu have been configured, reports may be printed for a particular Division and/or Unit from the MRSA Tools Reports Menu. The following options are available from the MRSA Tools Reports Menu:

- Print MRSA IPEC Report
- Print Isolation Report
- Print Nares Screen Compliance List
- Print CDI Report
- Print CRE Report

<span id="_Toc473541986" class="anchor"></span>Figure 27: MDRO Tools Reports Menu

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MDRO Tools Reports Menu</p>
<p>1 Print MRSA IPEC Report</p>
<p>2 Print Isolation Report</p>
<p>3 Print Nares Screen Compliance List</p>
<p>4 Print CDI Report</p>
<p>5 Print CRE Report</p>
<p>Select MDRO Tools Reports Menu &lt;TEST ACCOUNT&gt; Option:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### MRSA IPEC Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MRSA IPEC Report is used to obtain all pertinent information for data entry into IPEC for Facility-Wide Prevalence Measures and Unit-Specific Prevalence and Transmission Measures.

The Admission Report uses unit admission dates, while the Discharge Report uses unit discharge dates. For example, if the Admission Report is set to run for the CCU for the month of February 2017, it will display all patients admitted into the CCU during February 2017, regardless of when they were discharged from the unit (or if they still remain on the unit). If the Discharge Report is run for February 2017, it will display all patients that were discharged from the CCU during February 2017, regardless of when they entered the unit. The Discharge report will also display all patients that were still on the unit at the end of February.

More information regarding the reports follow in this section.

> **NOTE:** The MRSA IPEC Report should be run no earlier than 5 business days after the close of the month. This allows the laboratory to complete testing and enter the results into VistA. This is a suggested timeframe; it will be dependent on the laboratory practices at each facility.

> **NOTE:** The MRSA IPEC Report should be run monthly to gather the required data for entry into IPEC. The reports are not meant for daily monitoring. Daily monitoring can be conducted using the Isolation Report and Nares Screen Compliance Report.

To generate the report, perform the following steps:

1.  When prompted, select the report; choose either the Admission Report or Discharge/Transmission Report.
2.  When prompted, enter a start date to run the report and an end date for the report.

> Note: Reports should be run beginning with the first day of the month and should end with the last day of the month.

3.  When prompted, enter the Geographical Locations for the report.

> Note: The report can be run for one unit or all units. Only Geographical Units created using the MRSA Tools Ward Mapping Setup option may be selected. The report is designed for a 176 column format (landscape).

> Note: Do not generate a MRSA IPEC Report for any Geographical Unit that is an OBS unit.

<span id="_Toc473541987" class="anchor"></span>Figure 28: Print MRSA IPEC Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MRSA Tools Reports Menu Option: <strong>Print MRSA IPEC Report</strong></p>
<p>Select the Division: <strong>XXXXX VAMC</strong></p>
<p>Select one of the following:</p>
<p>A Admission Report</p>
<p>D Discharge/Transmission Report</p>
<p>Run (A)dmission Or (D)ischarge/Transmission Report: Admission Report</p>
<p>Begin with ward admission date: <strong>020117</strong> (FEB 01, 2017)</p>
<p>End with ward admission date: <strong>022817</strong> (FEB 28, 2017)</p>
<p>Do you want to select all locations? NO//</p>
<p>Select Geographical Location: <strong>11AB</strong></p>
<p>Select another Geographical Location:</p>
<p>Do you want to only print the summary report? NO//</p>
<p>This report is designed for a 176 column format (landscape).</p>
<p>DEVICE: HOME// <strong>IDM1$PRT LANDSCAPE</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Admission Report

The Admission Report displays the listing of patients that have been admitted to the unit for the calendar month. If a patient was admitted to the unit multiple times during the calendar month, then the patient will be displayed for each admission to the unit.

<span id="_Toc268767186" class="anchor"></span>Figure 29: Print MRSA IPEC Admission Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA IPEC ADMISSION REPORT</p>
<p>GEOGRAPHICAL LOCATION: 11AB</p>
<p>Report period: Oct 01, 2016 to Oct 31, 2016@24:00</p>
<p>Report printed on: Jan 16, 2017@14:07:26 PAGE: 1</p>
<p>NARES NARES CULTURE</p>
<p>DATE MAS MOVE SCREEN RESULT RESULT MRSA IN</p>
<p>WARD PATIENT SSN ENTERED WARD ADT TYPE 24H 48H 48H PAST YEAR</p>
<p>---------------------------------------------------------------------------------------------------------</p>
<p>11ABSURG *XXXXXXXXXXXXXXXXXX XXXX 10/1/16@09:43 A DIRECT Y</p>
<p>11ABSURG XXXXXXXXXXXXXXXXXX XXXX 10/1/16@16:11 T INTEWARD TRA Y</p>
<p>11ABMED *XXXXXXXXXXXXXXXXXX XXXX 10/1/16@20:25 A DIRECT Y</p>
<p>11ABSURG *XXXXXXXXXXXXXXXXXX XXXX 10/1/16@23:49 A DIRECT Y</p>
<p>11ABSURG *XXXXXXXXXXXXXXXXXX XXXX 10/1/16@19:57 A DIRECT</p>
<p>11ABMED *XXXXXXXXXXXXXXXXXX XXXX 10/1/16@11:01 A DIRECT Y</p>
<p>11ABSURG *XXXXXXXXXXXXXXXXXX XXXX 10/13/16@13:42 A DIRECT Y POS</p>
<p>11ABMED *XXXXXXXXXXXXXXXXXX XXXX 10/13/16@18:41 A DIRECT Y</p>
<p>11ABSURG XXXXXXXXXXXXXXXXXX XXXX 10/20/16@23:14 T INTERWARD TRA Y</p>
<p>11ABMED XXXXXXXXXXXXXXXXXX XXXX 10/21/16@14:34 T INTERWARD TRA Y POS POS</p>
<p>11ABSURG *XXXXXXXXXXXXXXXXXX XXXX 10/23/16@01:19 A DIRECT Y POS</p>
<p>11ABSURG *XXXXXXXXXXXXXXXXXX XXXX 10/13/16@13:42 A DIRECT Y</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

A description for the headings from the report are outlined in the table below.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th>Heading</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WARD</td>
<td>The patient was admitted or transferred into this Ward location.</td>
</tr>
<tr class="even">
<td>PATIENT</td>
<td>The patient's last name, followed by first name. An asterisk (*) before the patient's name denotes that the patient was indicated for a nasal screen upon admission to the unit based on the site's business rules.</td>
</tr>
<tr class="odd">
<td>SSN</td>
<td>The last 4 digits of the patient's social security number</td>
</tr>
<tr class="even">
<td>DATE ENTERED WARD</td>
<td>The date patient was admitted or transferred into the unit.</td>
</tr>
<tr class="odd">
<td>ADT</td>
<td>How the patient entered the unit, either by: admission or transfer into the unit.</td>
</tr>
<tr class="even">
<td><a href="#Glos_MAS">MAS</a> MOVE TYPE</td>
<td>The type of Medical Administration Service (MAS) movement.</td>
</tr>
<tr class="odd">
<td>NARES SCREEN 24H</td>
<td><p>This will be a Y (yes) if the patient received a nares screen within 24 hours of arriving on the unit. Only tests that follow the new MRSA lab standards will be captured.</p>
<p><strong>Note:</strong> The test names must be called MRSA SURVL NARES AGAR or MRSA SURVL NARES DNA.</p></td>
</tr>
<tr class="even">
<td>NARES RESULT 48H</td>
<td><p>This will be POS (positive) if the patient's nares screen or surveillance culture was positive within 48 hours of admission/transfer into the unit. Only tests that follow the new MRSA lab standards will be captured.</p>
<p><strong>Note:</strong> For nares screens, the test names must be called MRSA SURVL NARES AGAR or MRSA SURVL NARES DNA; for surveillance cultures the test names must be called MRSA SURVL OTHER AGAR or MRSA SURVL OTHER DNA.</p></td>
</tr>
<tr class="odd">
<td>CULTURE RESULT 48H</td>
<td><p>This will be POS (positive) if the patient had a clinical culture and it was positive within 48 hours of admission/transfer-in to the unit. Only cultures that were reported using the new MRSA lab standards will be captured.</p>
<p><strong>Note:</strong> The site must report positives cultures using the Etiology STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA).</p></td>
</tr>
<tr class="even">
<td>MRSA IN PAST YEAR</td>
<td>The patient's MRSA history going back one year prior to admission/transfer into the unit until the date/time of admission/transfer in. It will display a POS, if the patient ever had a positive nares screen, surveillance culture or clinical culture for MRSA in the past year. The program will determine a MRSA positive based on the parameter setup and national standards for laboratory reporting of MRSA.</td>
</tr>
</tbody>
</table>

#### Admission Summary Report

The Admission Summary Report displays all pertinent information to enter Prevalence Measure data into the Inpatient Evaluation Center (IPEC). The report displays Facility-Wide and Unit-Specific information.

The report will print a summary report for each unit. If multiple units were printed together, then an additional summary report will print which will contain a summary for all the units combined. This combined summary report can be useful to obtain the Facility-Wide prevalence measures that are required entries into IPEC, thereby eliminating the task of adding all the individual Facility wide measures together.

<span id="_Toc473541989" class="anchor"></span>Figure 30: MRSA IPEC Admission Summary Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA IPEC ADMISSION SUMMARY REPORT</p>
<p>Geographical Location: 11AB</p>
<p>Report period: Oct 01, 2016 to Oct 31, 2016@24:00</p>
<p>Report printed on: Jan 16, 2017@14:07:26 PAGE: 2</p>
<p>Prevalence Measures (Facility Wide)</p>
<p>1. Number of Admissions to the facility: 31</p>
<p>2. Number of (1) who received MRSA nasal screening upon admission to facility: 28</p>
<p>3. Number of (1) positive for MRSA based on nasal screening upon admission to facility: 5</p>
<p>4. Number of those in (1) positive for MRSA based on clinical cultures upon admission to facility: 0</p>
<p>Prevalence Measures (Unit Specific)</p>
<p>1. Number of admissions (admissions + transfers in) to the unit for the month: 41</p>
<p>2. Number of (1) for whom nasal screening was indicated: 41</p>
<p>3. Number of (2) who received nasal screening upon admission to unit (within 24 hours): 38</p>
<p>4. Number of (1) positive for MRSA based on nasal screening upon admission to unit: 6</p>
<p>5. Number of (1) positive for MRSA based on clinical cultures upon admission to unit: 0</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

A description for the headings from the report are outlined in the tables below.

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th>Heading</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Number of admissions to the facility</td>
<td>Direct admissions to the facility for the calendar month. <strong>Note:</strong> This includes all admissions (direct, non-service connected, etc.) and TO ASIH admissions; it does not include unit-to-unit transfers.</td>
</tr>
<tr class="even">
<td>Number of (1) who received MRSA nasal screening upon admission to facility</td>
<td>Direct admissions who received a MRSA nasal screen within 24 hours of admission to the facility.</td>
</tr>
<tr class="odd">
<td>Number of (1) positive for MRSA based on nasal screening upon admission to facility</td>
<td>Direct admissions who received a MRSA nares screen or surveillance culture within 48 hours of arriving to the facility and results were positive for MRSA, plus those direct admissions that had a prior history of MRSA in the past 12 months based on nares screen or clinical culture. Patients who had a positive clinical culture within 48 hours of arriving to the facility will be excluded.</td>
</tr>
<tr class="even">
<td>Number of those in (1) positive for MRSA based on clinical cultures upon admission to facility</td>
<td><p>Direct admissions that had a clinical culture upon admission to the facility and results were positive within 48 hours of admission.</p>
<p><strong>Note:</strong> If a patient has a positive nares screen or history of MRSA, and positive clinical culture, it is counted once under the clinical culture category.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th>Heading</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Number of admissions (admissions + transfers) into the unit for the month</td>
<td>Direct admissions plus transfers into the unit for the calendar month.</td>
</tr>
<tr class="even">
<td>Number of (1) for whom nasal screening was indicated</td>
<td><p>The number of admissions and transfers into the unit for the calendar month for whom a nasal screen was indicated. The program will determine this information based on the site parameters entered during setup.</p>
<p>If the admitting unit at a site does not screen patients on unit-to-unit transfers, but the discharging unit does, then only Facility admissions will be indicated for a swab.</p>
<p>If a site does not screen patients with MRSA history on transfers into the unit, then a patient with a known MRSA history (within 365 days prior to entering the unit) will not be indicated for a swab on unit-to-unit transfers. To be considered "known positive" the lab result must have been verified before the patient entered the unit.</p>
<p><strong>Note:</strong> This is different from the column heading MRSA IN PAST YEAR, where the collection date, not the verification date, was used.</p></td>
</tr>
<tr class="odd">
<td>Number of (2) who received MRSA nasal screening upon admission to unit (within 24 hours)</td>
<td>Admissions and transfers into the unit for the calendar month that were indicated for a MRSA nares screen and who received a MRSA nasal screen within 24 hours of admission to the unit.</td>
</tr>
<tr class="even">
<td>Number of (1) positive for MRSA based on nasal screening upon admission to unit</td>
<td>Admissions and transfers into the unit for the calendar month who received a MRSA nares screen or surveillance culture within 48 hours of arriving to the unit and results were positive for MRSA, plus those admissions and transfers into the unit that had a prior history of MRSA in the past 12 months, either by nares screen or clinical culture. Patients who had a positive clinical culture within 48 hours of arriving to the unit will be excluded.</td>
</tr>
<tr class="odd">
<td>Number of (1) positive for MRSA based on clinical cultures upon admission to unit</td>
<td><p>Admissions and transfers into the unit who had a clinical culture upon admission to the unit and results were positive within 48 hours of admission to unit.</p>
<p><strong>Note:</strong> If a patient has a positive nares screen or history of MRSA, and positive clinical culture, it is counted once under the clinical culture category.</p></td>
</tr>
</tbody>
</table>

#### Discharge/Transmission Report

The Discharge/Transmission Report displays all discharges that occurred for the calendar month. It also includes all patients that were still on the unit at the end of the calendar month. If a patient was discharged from the unit more than once, they will show up multiple times.

<span id="_Toc473541990" class="anchor"></span>Figure 31: MRSA IPEC Discharge/Transmission Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>MRSA IPEC DISCHARGE/TRANSMISSION REPORT</strong></p>
<p><strong>Geographical Location: 11AB</strong></p>
<p><strong>Report period: Oct 01, 2016 to Oct 31, 2016@24:00</strong></p>
<p><strong>Report printed on: Jan 16, 2017#14:25:15 PAGE: 1</strong></p>
<p><strong>ADM NARES NARES DIS NARES NARES MRSA</strong></p>
<p><strong>DATE ADM MAS MOVE SCREEN RESULT MRSA IN DATE DIS MAS MOVE SCREEN RESULT IN CURR</strong></p>
<p><strong>WARD PATIENT SSN ENTERED WARD ADT TYPE 24H 48H PAST YR LEFT WARD ADT TYPE 24H 48H PRD TRANS</strong></p>
<p><strong>---------------------------------------------------------------------------------------------------------------------------------------------------------------</strong></p>
<p><strong>11ABS XXXXXXXXXXXXXXX XXXX 9/7/16@17:51 T INTERWARD TRA POS 10/27/16@18:20 D NON-SERVICE C Y</strong></p>
<p><strong>11ABM *XXXXXXXXXXXXXXX XXXX 9/26/16@18:17 A DIRECT Y POS 10/12/16@15:24 D MPM=SERVICE C</strong></p>
<p><strong>11ABS XXXXXXXXXXXXXXX XXXX 9/27/16@16:26 T INTERWARD TRA Y POS POS 10/1/16@12:07 T INTERWARD TRA Y POS POS</strong></p>
<p><strong>11ABM *XXXXXXXXXXXXXXX XXXX 9/28/16@19:58 A DIRECT Y 10/2/16@21:22 D MOM-SERVICE C</strong></p>
<p><strong>11ABS *XXXXXXXXXXXXXXX XXXX 9/28/16@20:03 A DIRECT Y 10/2/16@21:12 D TRANSFER OUR Y</strong></p>
<p><strong>11ABS *XXXXXXXXXXXXXXX XXXX 9/28/16@22:11 A DIRECT Y 10/1/16@16:40 D NON-SERVICE C Y</strong></p>
<p><strong>11ABM XXXXXXXXXXXXXXX XXXX 10/13/16@13:42 A DIRECT Y POS POS 10/14/16@23:57 D IRREGULAR POS</strong></p>
<p><strong>11ABS *XXXXXXXXXXXXXXX XXXX 10/14/16@15:11 A DIRECT Y 10/26/16@17:21 D NON-SERVICE C Y</strong></p>
<p><strong>11ABS *XXXXXXXXXXXXXXX XXXX 10/16/16@11:05 T INTERWARD TRA Y 10/18/16@19:50 T INTEWARD TRA Y</strong></p>
<p><strong>11ABS *XXXXXXXXXXXXXXX XXXX 10/16/16@17:35 A DIRECT Y 10/20/16@13:10 D NON-SERVICE C Y POS POS T</strong></p>
<p><strong>11ABS *XXXXXXXXXXXXXXX XXXX 10/17/16@17:00 A DIRECT Y 10/17/16@22:19 T INTERWARD TRA</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

A description for the headings from the report are outlined in the table below.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>Heading</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WARD</td>
<td>The patient was admitted/transferred into this Ward location.</td>
</tr>
<tr class="even">
<td>PATIENT</td>
<td>Patient's last name, followed by first name. An asterisk (*) before the patient's name denotes that the patient was indicated for a nasal screen upon discharge from the unit based on the site's business rules.</td>
</tr>
<tr class="odd">
<td>SSN</td>
<td>The last 4 digits of the patient's social security number.</td>
</tr>
<tr class="even">
<td>DATE ENTERED WARD</td>
<td>The date patient was admitted or transferred into the unit.</td>
</tr>
<tr class="odd">
<td>ADM ADT</td>
<td>How the patient entered the ward, either by admission or transfer into the unit.</td>
</tr>
<tr class="even">
<td><a href="#Glos_MAS">MAS</a> MOVE TYPE</td>
<td>The type of Medical Administration Service (MAS) movement.</td>
</tr>
<tr class="odd">
<td>NARES SCREEN 24H</td>
<td><p>This will be Y (yes) if the patient received a nares screen within 24 hours of arriving on the unit. Only tests that follow the new MRSA laboratory standards will be captured.</p>
<p><strong>Note:</strong> The test names must be called MRSA SURVL NARES AGAR or MRSA SURVL NARES DNA.</p></td>
</tr>
<tr class="even">
<td>NARES RESULT 48H</td>
<td><p>This will be POS (positive) if the patient's nares screen or surveillance culture was positive within 48 hours of admission to the unit. Only tests that follow the new MRSA lab standards will be captured.</p>
<p><strong>Note:</strong> For nares screens, the test names must be called MRSA SURVL NARES AGAR or MRSA SURVL NARES DNA; for surveillance cultures they must be called MRSA SURVL OTHER AGAR or MRSA SURVL OTHER DNA.</p></td>
</tr>
<tr class="odd">
<td>MRSA IN PAST YEAR</td>
<td><p>The patient's MRSA history going back one year prior to admission until 48 hours after admission. It will display a POS, if the patient ever had a positive nares screen, surveillance culture or clinical culture for MRSA in the past year.</p>
<p>Begin time frame: (Admission – 365 days) or (report start date – 365 days); use the later timeframe.</p>
<p>End time frame: (Admission + 48 hours) or (report start date); use the later timeframe.</p>
<p><strong>Note:</strong> The program will determine a MRSA positive based on the parameter set-up (MDRO Tools Lab Parameter Setup) and national standards for laboratory reporting of MRSA.</p></td>
</tr>
<tr class="even">
<td>DATE LEFT WARD</td>
<td>Date the patient left the unit.</td>
</tr>
<tr class="odd">
<td>DIS ADT</td>
<td>How the patient left the unit: Discharge or Transfer-out.</td>
</tr>
<tr class="even">
<td>DIS MAS MOVE TYPE</td>
<td>Type of discharge movement.</td>
</tr>
<tr class="odd">
<td>NARES SCREEN 24H</td>
<td><p>Y (yes) if the patient had a nares screen within 24 hours of being discharged from the unit. Only tests that follow the new MRSA lab standards will be captured.</p>
<p><strong>Note:</strong> The test names must be called MRSA SURVL NARES AGAR or MRSA SURVL NARES DNA.</p></td>
</tr>
<tr class="even">
<td>NARES RESULT 48H</td>
<td><p>POS (positive) if the patient's nares screen or surveillance culture was positive within 48 hours of exiting the unit. Only tests that follow the new MRSA lab standards will be captured.</p>
<p><strong>Note:</strong> For nares screens, the test names must be called MRSA SURVL NARES AGAR or MRSA SURVL NARES DNA; for surveillance cultures they must be called MRSA SURVL OTHER AGAR or MRSA SURVL OTHER DNA.</p></td>
</tr>
<tr class="odd">
<td>MRSA IN CURR PRD</td>
<td><p>POS (positive) if the patient had a positive MRSA nasal screen, surveillance culture or clinical culture during the current admission.</p>
<ul>
<li><p>Begin time frame: (Admission + 48 hours) or (Report start date); use the later timeframe.</p></li>
</ul>
<ul>
<li><p>End time frame: (Discharge + 48 hours) or (Report end date); use the earlier timeframe.</p></li>
</ul>
<p><strong>Note:</strong> The program will determine what's considered a MRSA positive based on the parameter set-up (MDRO Tools Lab Parameter Setup) and national standards for laboratory reporting of MRSA.</p></td>
</tr>
<tr class="even">
<td>TRANS</td>
<td><p>T if the patient had a transmission within the selected time range.</p>
<p><strong>Note:</strong> Transmission is defined as a patient with a negative nares screen within 48 hours of admission to the unit (NARES RESULT 48H) and no history of MRSA within the past 365 days (MRSA IN PAST YEAR). In addition, on transfer and/or discharge from the unit the patient must have a positive nares screen (NARES RESULT 48H), or be positive for MRSA during the current admission (MRSA IN CURR PRD).</p></td>
</tr>
</tbody>
</table>

#### Discharge/Transmission Summary Report

The Discharge/Transmission Summary Report displays all pertinent information to enter Transmission Measure data into the Inpatient Evaluation Center (IPEC). The report displays information for Unit-Specific data entry.

<span id="_Toc473541991" class="anchor"></span>Figure 32: MRSA IPEC Discharge/Transmission Summary Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MRSA IPEC DISCHARGE/TRANSMISSION SUMMARY REPORT</p>
<p>Geographical Location: SICU</p>
<p>Report period: Mar 01, 2017 to Mar 15, 2017@24:00 PAGE: 1</p>
<p>Transmission Measures (Unit Specific)</p>
<p>10. Number of bed days of care for the unit: 115</p>
<p>11. Number of exits (discharges + deaths + transfers out) from the unit: 33</p>
<p>12. Number of (11) for whom a discharge/transfer swab was indicated: 33</p>
<p>13. Number of (12) who received MRSA nasal screening upon exit from unit: 31</p>
<p>14. Number of MRSA transmissions on unit based on MRSA nasal screening or clinical cultures: 0</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

A description for the headings from the report are outlined in the table below.

<span id="_Toc473542036" class="anchor"></span>Table 9: Descriptions for Transmission Measures (Unit Specific)

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>Heading</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Number of bed days of care for the unit</td>
<td>Bed days of care for the unit for the calendar month.</td>
</tr>
<tr class="even">
<td>Number of exits (discharges + deaths + transfers out) from the unit</td>
<td>The number of exits (discharges/deaths/transfers out) from the unit for the calendar month.</td>
</tr>
<tr class="odd">
<td>Number of (11) for whom a discharge/transfer swab was indicated</td>
<td><p>The number of discharges, deaths and transfer out from the unit for the calendar month, for whom a nasal screen was indicated. The program will determine this information based on the site parameters entered during setup.</p>
<p><strong>Note:</strong> If the discharging unit at a site does not screen patients on unit-to-unit transfers (but the admitting unit does), then only facility discharge(s) or death will be indicated for a swab.</p>
<p><strong>Note:</strong> If a site does not screen patients with MRSA history on discharge/death/transfer-outs, then a patient with a known MRSA history (within 365 days prior to leaving the unit) will not be indicated for a swab. To be considered "known positive" the lab result must have been verified before the patient left the unit.</p>
<p><strong>Note:</strong> This is different than the column heading MRSA IN PAST YEAR, where the collection date (not verification date) was used.</p></td>
</tr>
<tr class="even">
<td>Number of (12) who received MRSA nasal screening upon exit from the unit</td>
<td>Those discharges, deaths and transfers out who were indicated for a MRSA nares screen and received a MRSA nares screen within 24 hours from exit from the unit.</td>
</tr>
<tr class="odd">
<td>Number of MRSA transmissions on unit based on MRSA nasal screening or clinical cultures</td>
<td>The number of transmissions on the units for the calendar month identified either by MRSA nares screen or clinical culture, while taking into account the patient's history of MRSA in the past 12 months.</td>
</tr>
</tbody>
</table>

### Print Isolation Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Isolation Report is an optional report. It can be used to print a ward census and will identify patients on the unit that have a selected MDRO (i.e., MRSA, CRB-R, VRE, C. diff, VRE, ESBL). The report displays real-time unit-specific patient information and is based on the information entered in the parameter setup (MDRO and Historical Days, and Isolation Orders, if applicable). The report will display the patient's last known positive MDRO and active Isolation Orders if this information is used by the facility.

The report is designed for a 176 column (landscape) format.

<span id="_Toc473541992" class="anchor"></span>Figure 33: Print Isolation Report Option

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MRSA Tools Reports Menu Option: <strong>Print Isolation Report</strong></p>
<p>Select the Division: <strong>XXXXX VAMC</strong></p>
<p>Do you want to select all locations? NO//</p>
<p>Select Geographical Location: <strong>11AB</strong></p>
<p>Select another Location:</p>
<p>This report is designed for a 176 column format (landscape).</p>
<p>DEVICE: HOME// <strong>IDM1$PRT LANDSCAPE</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The Print Isolation Report may be tasked to print to a specific unit at one or more specific times of day which will allow the unit to identify patients to be placed in contact precautions and to see if any Isolation Orders have been ordered for the patient. See information regarding the Print Isolation Report (Tasked) for configuration instructions for this option.

<span id="_Toc473541993" class="anchor"></span>Figure 34: Isolation Report

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>CENSUS LIST AND MDRO HISTORY</strong></p>
<p><strong>Geographical location: 11AB</strong></p>
<p><strong>Report printed on: Mar 05, 2017@14:28:10 PAGE: 1</strong></p>
<p><strong>LAST MRSA POS LAST CRB-R POS LAST ESBL POS LAST VRE POS LAST CDF POS</strong></p>
<p><strong>PATIENT SSN IN 365 DAYS IN 365 DAYS IN 356 DAYS IN 365 DAYS IN 28 DAYS ISOLATION ORDER START DATE</strong></p>
<p><strong>--------------------------------------------------------------------------------------------------------------------------------------------------</strong></p>
<p><strong>XXXXXXXXXXXXXXXXXXX XXXX CONTACT PRECAUTIONS 3/1/16</strong></p>
<p><strong>XXXXXXXXXXXXXXXXXXX XXXX</strong></p>
<p><strong>XXXXXXXXXXXXXXXXXXX XXXX 2/28/16@17:00 6/1/16@13:30 5/13/16@15:15 6/5/16@13:30 CONTACT PRECAUTIONS 2/27/16</strong></p>
<p><strong>XXXXXXXXXXXXXXXXXXX XXXX 2/28/16@17:00 6/1/16@13:30 5/13/16@15:15 6/5/16@13:30 CONTACT PRECAUTIONS 11/13/16</strong></p>
<p><strong>XXXXXXXXXXXXXXXXXXX XXXX 10/7/16@21:57</strong></p>
<p><strong>XXXXXXXXXXXXXXXXXXX XXXX</strong></p>
<p><strong>XXXXXXXXXXXXXXXXXXX XXXX 2/25/16@15:05 5/14/16@20:01 CONTACT PRECAUTIONS 2/25/16</strong></p>
<p><strong>XXXXXXXXXXXXXXXXXXX XXXX</strong></p>
<p><strong>XXXXXXXXXXXXXXXXXXX XXXX</strong></p>
<p><strong>XXXXXXXXXXXXXXXXXXX XXXX 3/3/16@18:44 CONTACT PRECAUTIONS 3/4/16</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

A description for the headings from the report are outlined in the table below.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>Heading</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT</td>
<td>The patient's last name, followed by first name.</td>
</tr>
<tr class="even">
<td>SSN</td>
<td>The last 4 digits of the patient's social security number.</td>
</tr>
<tr class="odd">
<td>MRSA IN 365 DAYS</td>
<td><p>The last positive MRSA result (either by nares screen, surveillance culture or clinical culture) in the past 365 days.</p>
<p><strong>Note:</strong> The program will determine a MRSA positive based on the parameter setup (MDRO Tools Lab Parameter Setup) and national standards for laboratory reporting of MRSA.</p></td>
</tr>
<tr class="even">
<td>CRB-R IN XXX DAYS</td>
<td><p>The last positive CRB-R result in the past XXX day; it is optional. It will only be displayed if during the initial setup the user identified the number of historical days for this MDRO (using the MDRO Historical Days Edit option).</p>
<p><strong>Note:</strong> The program will determine a CRB-R positive based on the parameter set-up (MDRO Tools Lab Parameter Setup).</p></td>
</tr>
<tr class="odd">
<td>ESBL IN XXX DAYS</td>
<td><p>The last positive ESBL result in the past XXX days; it is optional. It will only be displayed if during the initial setup the user identified the number of historical days for this MDRO (using the MDRO Historical Days Edit option).</p>
<p><strong>Note:</strong> The program will determine an ESBL positive based on the parameter set-up (MDRO Tools Lab Parameter Setup).</p></td>
</tr>
<tr class="even">
<td>VRE IN XXX DAYS</td>
<td><p>This will display the last positive VRE result in the past XXX days; it is optional. It will only be displayed if during the initial setup the user identified the number of historical days for this MDRO (using the MDRO Historical Days Edit option).</p>
<p><strong>Note:</strong> The program will determine a VRE positive based on the parameter set-up (MDRO Tools Lab Parameter Setup).</p></td>
</tr>
<tr class="odd">
<td>CDIFF IN XXX DAYS</td>
<td><p>Last positive C. difficile result in the past XXX days; it is optional. It will only be displayed if during the initial setup the user identified the number of historical days for this MDRO (using the MDRO Historical Days Edit option).</p>
<p><strong>Note:</strong> The program will determine a C. diff positive based on the parameter set-up (MDRO Tools Lab Parameter Setup).</p></td>
</tr>
<tr class="even">
<td>ISOLATION ORDER</td>
<td>Type of Isolation Order the provider has ordered for the patient. Note that the information will only be displayed if the site uses Isolation Orders; the information about Isolation Orders was added during the initial set-up (using option Isolation Orders Add/Edit). If more than one Isolation Order has been ordered for the patient, then the patient will be listed multiple times on the report, dependent on the number of Isolation Orders.</td>
</tr>
<tr class="odd">
<td>START DATE</td>
<td>Start Date for the Isolation Order that the provider ordered for the patient. Note that the information will only be displayed if the site uses Isolation Orders, and information about Isolation Orders was added during the initial set-up (using option Isolation Orders Add/Edit).</td>
</tr>
</tbody>
</table>

### Print Nares Screen Compliance List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Nares Screen Compliance List is an optional report. If desired, the report may be used to print a ward census and identify if a MRSA nares screen was ordered for the patient. The report prints real-time patient information on the unit and is designed for a 132 column (compressed) format.

<span id="_Toc473541994" class="anchor"></span>Figure 35: Nares Screen Compliance List

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MRSA Tools Reports Menu Option: <strong>Print Nares Screen Compliance List</strong></p>
<p>Select the Division: <strong>XXXXX VAMC</strong></p>
<p>Do you want to select all locations? NO//</p>
<p>Select Geographical Location: <strong>11AB</strong></p>
<p>Select another Location:</p>
<p>This report is designed for a 132 column format (compressed).</p>
<p>DEVICE: HOME// <strong>IDM1$PRT COMPRESSED</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc473541995" class="anchor"></span>Figure 36: Nares Swab Order List

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>NARES SWAB ORDER LIST</p>
<p>Geographical Location: 11AB</p>
<p>Report printed on: Mar 02, 2017@15:31:27 PAGE: 1</p>
<p>DATE MRSA IN NARES LAB</p>
<p>PATIENT SSN ENTERED WARD ADT PAST YEAR ORDERED ORDER DATE RECEIVED</p>
<p>-------------------------------------------------------------------------------------------</p>
<p>XXXXXXXXXXXXXXX XXXX 2/27/17@19:13 T POS YES 2/27/17@18:53 YES</p>
<p>XXXXXXXXXXXXXXX XXXX 2/27/17@19:37 A YES 2/27/17@23:30 YES</p>
<p>XXXXXXXXXXXXXXX XXXX 2/24/17@18:37 A POS YES 2/24/17@22:05 YES</p>
<p>XXXXXXXXXXXXXXX XXXX 3/2/17@14:19 A</p>
<p>XXXXXXXXXXXXXXX XXXX 3/2/17@02:48 A YES 3/2/17@07:00 YES</p>
<p>XXXXXXXXXXXXXXX XXXX 3/1/17@13:40 A YES 3/1/17@14:15 YES</p>
<p>XXXXXXXXXXXXXXX XXXX 2/22/17@11:02 T POS YES 2/22/17@01:48 YES</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

A description for each of the headings from the report are outlined in the table below.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>Heading</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PATIENT</td>
<td>Patient's last name, first name.</td>
</tr>
<tr class="even">
<td>SSN</td>
<td>Last 4 digits of the patient's social security number.</td>
</tr>
<tr class="odd">
<td>DATE ENTERED WARD</td>
<td>Date the patient was admitted to the unit.</td>
</tr>
<tr class="even">
<td>ADT</td>
<td>How the patient entered the ward: Admission or Transfer-In to the unit</td>
</tr>
<tr class="odd">
<td>MRSA IN PAST YEAR</td>
<td><p>POS (positive) if the patient had a positive MRSA result (either by nares screen or clinical culture).</p>
<p><strong>Note:</strong> The program will determine a MRSA positive based on the parameter set-up (MDRO Tools Lab Parameter Setup) and national standards for laboratory reporting of MRSA.</p></td>
</tr>
<tr class="even">
<td>NARES ORDERED</td>
<td><p>If a nares screen was ordered for the patient, the report starts searching for a nares screen beginning 24 hours before admission – going forward. The first active or completed order it finds once it starts searching, is the order that gets displayed on the report. If there are no active or completed orders, then the first pending order within that time frame will be displayed.</p>
<p><strong>Note:</strong> Only orders for tests that follow the new MRSA lab standards will be picked up (the test names must be called 'MRSA SURVL NARES AGAR' or 'MRSA SURVL NARES DNA').</p></td>
</tr>
<tr class="odd">
<td>ORDER DATE</td>
<td>Date the nares screen was ordered for the patient.</td>
</tr>
<tr class="even">
<td>LAB RECEIVED</td>
<td>If the nares screen was received in the lab, labs received will be utilized during the search by the program.</td>
</tr>
</tbody>
</table>

The Print Nares Screen Compliance List report can be tasked to print to a specific unit at one or more specified times of the day. This allows the unit to determine if a patient did not have a nares screen upon admission and to obtain one, if needed.

> **NOTE:** The Print Nares Screen Compliance List report is based on the laboratory standards for the following test names: MRSA SURVL NARES DNA and MRSA SURVL NARES AGAR. If the standards have not been implemented or have been set up incorrectly, then the report will not display accurate information.

### Print CDI Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Printing the CDI Report to a Printer

> **NOTE:** Before running the report, ensure that the laboratory test(s), e.g., the Clostridium Difficile Etiology, are configured in the MDRO TOOLS LAB SEARCH/EXTRACT file (#104.1).  To configure the lab test(s), use the MDRO Tools Lab Parameter Setup option.

To generate the report, perform the following steps:

1.  From the MDRO Tools Reports Menu, enter 4 for Print CDI Report and press the \<ENTER\> key.
2.  At the Do you want to select all Divisions: NO// prompt, enter either Yes or No based on the following criteria:
    1.  Entering Yes will obtain results for <u>all</u> divisions.
    2.  Entering No will obtain results for a particular division or divisions. After No is entered, a prompt will be displayed to enter the name of the division. Enter the name of the division and press the \<ENTER\> key. If desired, enter additional divisions.

> Note: The prompt will not display for a facility that is setup as a Single Division, it will only display for a Multi-Division Facility.

3.  At the prompt, Beginning POS CDI Lab ID Event (Collection) Date: Nov 12, 2015// enter a start date to run the report or accept the default for 365 days.
4.  At the prompt Ending POS CDI Lab ID Event (Collection) Date: enter an end date. Note: An end date must be entered to run the report.
5.  At the prompt, Device: HOME//, enter the name of the printer.

> **NOTE:** This report is designed for a 132 column format (compressed).

<span id="_Toc473541996" class="anchor"></span>Figure 37: Example of Printing the CDI Report for a Division

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MDRO Tools Reports Menu &lt;TEST ACCOUNT&gt; Option: 4 Print CDI Report</p>
<p>Do you want to select all divisions: NO// n NO</p>
<p>Select Division: CHEYENNE VAMROC</p>
<p>Select another Division:</p>
<p>Beginning POS CDI Lab ID Event (Collection) Date: Jan 21, 2016//0811 (AUG 11, 2016)</p>
<p>Ending POS CDI Lab ID Event (Collection) Date: 0818 (AUG 18, 2016)</p>
<p>This report is designed for a 132 column format (compressed).</p>
<p>DEVICE: HOME// ;180;999 HOME (CRT)</p>
<p>FACILITY CDI CASES REPORT</p>
<p>Division: CHEYENNE VAMROC</p>
<p>Geographical Location: C MEDICINE</p>
<p>Report printed on: Jan 19, 2017@11:38:37 PAGE: 1</p>
<p>PATIENT SSN DOB CDI Event D/T ADM D/T LOCATION DC D/T PREV CDI Event D/T</p>
<p>---------------------------------------------------------------------------------------------------------------------------------------------------------------</p>
<p>SQA,TESTPATIENTFOUR 5543 04/13/1969 8/14/16 08:00 8/13/16 00:39:23 C MEDICINE 8/13/16 17:31:37</p>
<p>FACILITY CDI CASES REPORT</p>
<p>Division: CHEYENNE VAMROC</p>
<p>Geographical Location: CHY ANTICOAG</p>
<p>Report printed on: Jan 19, 2017@11:38:37 PAGE: 2</p>
<p>PATIENT SSN DOB CDI Event D/T ADM D/T LOCATION DC D/T PREV CDI Event D/T</p>
<p>---------------------------------------------------------------------------------------------------------------------------------------------------------------</p>
<p>SQA,TESTPATIENTONE 0090 09/05/1989 8/13/16 08:00 CHY ANTICOAG</p>
<p>SQA,TESTPATIENTTWO 4412 07/30/1969 8/13/16 09:00 CHY ANTICOAG</p>
<p>FACILITY CDI CASES REPORT</p>
<p>Division: CHEYENNE VAMROC</p>
<p>Geographical Location: CLC</p>
<p>Report printed on: Jan 19, 2017@11:38:37 PAGE: 3</p>
<p>PATIENT SSN DOB CDI Event D/T ADM D/T LOCATION DC D/T PREV CDI Event D/T</p>
<p>---------------------------------------------------------------------------------------------------------------------------------------------------------------</p>
<p>SQA,TESTPATIENTFOUR 5543 04/13/1969 8/16/16 12:26:15 8/13/16 00:39:23 ICU-M 8/14/16 08:00</p>
<p>SQA,TESTPATIENTTHREE 2254 05/14/1977 8/13/16 17:25:25 8/13/16 00:36:44 ICU-M</p>
<p>SQA,TESTPATIENTTWO 4412 07/30/1969 8/14/16 22:25:16 8/14/16 22:06:52 ICU-M 8/13/16 09:00</p>
<p>SQA,TESTPATIENTTWO 4412 07/30/1969 8/16/16 12:37:27 8/14/16 22:06:52 ICU-M 8/16/16 10:45:11</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc473541997" class="anchor"></span>Figure 38: Rendition of Printing the CDI Report to a Printer

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>FACILITY CDI CASES REPORT</p>
<p>Division: CASPER</p>
<p>Geographical Location: ICU-M</p>
<p>Report printed on: Dec 16, 2016@13:20:44 PAGE: 1</p>
<p>PATIENT SSN DOB CDI Event D/T ADM D/T LOCATION PREV CDI Event D/T</p>
<p>DC D/T</p>
<p>----------------------------------------------------------------------------</p>
<p>XXXXXXXXXXXXXXX XXXX 04/13/1969 8/16/16 12:26:15 8/13/16 00:39:23 ICU-M 8/14/16 08:00</p>
<p>XXXXXXXXXXXXXXX XXXX 05/14/1977 8/13/16 17:25:25 8/13/16 00:36:44 ICU-M 8/15/16 08:00</p>
<p>XXXXXXXXXXXXXXX XXXX 07/30/1969 8/14/16 22:25:16 8/14/16 22:06:52 ICU-M 8/13/16 09:00</p>
<p>XXXXXXXXXXXXXXX XXXX 07/30/1969 8/16/16 12:37:27 8/14/16 22:06:52 ICU-M 8/16/16 10:45:11</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Displaying the CDI report to screen.

> **NOTE:** Before running the report, ensure that the laboratory test(s), e.g., the Clostridium Difficile Etiology, are configured in the MDRO TOOLS LAB SEARCH/EXTRACT file (#104.1).  To configure the lab test(s), use the MDRO Tools Lab Parameter Setup option.

To generate the report, perform the following steps:

1.  From the MDRO Tools Reports Menu, enter 4 for Print CDI Report and press the \<ENTER\> key.
2.  At the Select Division: prompt, enter the name of the Division.
3.  At the Do you want to select all Divisions: NO// prompt, enter either Yes or No based on the following criteria:
    1.  Entering Yes will obtain results for <u>all</u> divisions.
    2.  Entering No will obtain results for a particular division or divisions. After No is entered, a prompt will be displayed to enter the name of the division. Enter the name of the division and press the \<ENTER\> key. If desired, enter additional divisions.

> Note: The prompt will not display for a facility that is setup as a Single Division, it will only display for a Multi-Division Facility.

4.  At the prompt, Beginning POS CDI Lab ID Event (Collection) Date: Nov 12, 2015// enter a start date to run the report or accept the default for 365 days.
5.  At the prompt Ending POS CDI Lab ID Event (Collection) Date: enter an end date. Note: An end date must be entered to run the report.
6.  At the prompt, Device: HOME//, press the \<ENTER\> key.
7.  At the prompt, Print a delimited report to the screen? (Y/N): enter Yes and press the \<ENTER\> key.
8.  Open Reflection™
9.  Select Setup from the File Menu toolbar.
10. Select Display from Setup drop down.
11. From the Display window, Select the Screen tab.
12. Select Auto Resize Screen.
13. Enter 160 into the Columns box. Press the \<OK\> button.

<span id="_Toc473541998" class="anchor"></span>Figure 39: Reflection<sup>TM</sup> Column Size

![](mmrs-1-4-user-guide/003.png)

14. In VistA, when prompted at Device: Home// enter the following: ;160;9999 and press the \<ENTER\> key.

> <span id="_Toc473541999" class="anchor"></span>Figure 40: Displaying the CDI Report to Screen

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Print a delimited report to the screen? (Y/N): y YES</p>
<p>Delimited Report will now be printed to the screen...</p>
<p>DEVICE: HOME// ;160;999 HOME (CRT)</p>
<p>SQA,TESTPATIENTFOUR^5543^04/13/1969^8/14/16 08:00^8/13/16 00:39:23^C EDICINE^WARD^MEDICINE^13^^^8/13/16 17:31:37</p>
<p>SQA,TESTPATIENTONE^0090^09/05/1989^8/13/16 08:00^^CHY ANTICOAG^CLINIC^MEDICINE^161^^^</p>
<p>SQA,TESTPATIENTTWO^4412^07/30/1969^8/13/16 09:00^^CHY ANTICOAG^CLINIC^MEDICINE^161^^^</p>
<p>KORDISH,ELI SQAPATIENT^8397^05/13/1925^8/13/16 23:13:29^8/11/10 15:45:36^CLC^WARD^MEDICINE^13^^7/17/08 16:30^</p>
<p>SQA,TESTPATIENTFOUR^5543^04/13/1969^8/16/16 12:26:15^8/13/16 00:39:23^ICU-M^WARD^MEDICINE^13^^^8/14/16 08:00</p>
<p>SQA,TESTPATIENTTHREE^2254^05/14/1977^8/13/16 17:25:25^8/13/16 00:36:44^ICU-M^WARD^MEDICINE^13^^^</p>
<p>SQA,TESTPATIENTTWO^4412^07/30/1969^8/14/16 22:25:16^8/14/16 22:06:52^ICU-M^WARD^MEDICINE^13^^^8/13/16 09:00</p>
<p>SQA,TESTPATIENTTWO^4412^07/30/1969^8/16/16 12:37:27^8/14/16 22:06:52^ICU-M^WARD^MEDICINE^13^^^8/16/16 10:45:11</p>
<p>SQA,OUTPATIENTSIX^3876^03/18/1973^8/14/16 22:54:18^8/14/16 08:00^INTERMEDIATE MEDICINE^WARD^NONE^112^^^</p>
<p>SQA,TESTPATIENTSIX^8899^06/28/1968^8/13/16 17:31:57^8/13/16 00:24:38^INTERMEDIATE MEDICINE^WARD^NONE^112^^^</p>
<p>SQA,TESTPATIENTFIVE^3389^07/16/1972^8/16/16 10:27:39^8/13/16 00:14:13^TRANSITIONAL^WARD^^145^^^</p>
<p>END OF REPORT.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Importing the Delimited data into Excel™ Spreadsheet 

An Excel™ spreadsheet has been developed entitled CDI Reporting Tool which can be utilized to determine how a case should be defined (e.g. duplicate, recurrent, incident, CO-, CO-CLC-Associated, CO-not-CLC-Associated, CLC Onset-CLC-Associated, etc.) for reporting to IPEC. All CDI positive laboratory assays (obtained from inpatients as well as outpatients) should be captured each month in the CDI Reporting Tool.

> **NOTE:** Before running the report, ensure that the laboratory test(s), e.g., the Clostridium Difficile Etiology, are configured in the MDRO TOOLS LAB SEARCH/EXTRACT file (#104.1).  To configure the lab test(s), use the MDRO Tools Lab Parameter Setup option.

To generate the report, perform the following steps:

1.  From the MDRO Tools Reports Menu, enter 4 for Print CDI Report and press the \<ENTER\> key.
2.  At the Do you want to select all Divisions: NO// prompt, enter either Yes or No based on the following criteria:
    1.  Entering Yes will obtain results for <u>all</u> divisions.
    2.  Entering No will obtain results for a particular division or divisions. After No is entered, a prompt will be displayed to enter the name of the division. Enter the name of the division and press the \<ENTER\> key. If desired, enter additional divisions.

> Note: The prompt will not display for a facility that is setup as a Single Division, it will only display for a Multi-Division Facility.

3.  At the Beginning POS CDI LAB ID Event (Collection)Date: prompt, enter a begin date and press the \<ENTER\> key.
4.  At the Ending POS CDI LAB ID Event (Collection)Date: prompt, enter an end date and press the \<ENTER\> key.
5.  At the prompt, Device: HOME//, press the \<ENTER\> key.
6.  At the prompt, Print a delimited report to the screen? (Y/N): enter Yes and press the \<ENTER\> key.
7.  Open Reflection™
8.  Select Setup from the File Menu toolbar.
9.  Select Display from Setup drop down.
10. From the Display window, Select the Screen tab.
11. Select Auto Resize Screen.
12. Enter 160 into the Columns box. Press the \<OK\> button.

<span id="_Toc473542000" class="anchor"></span>Figure 41: Reflection<sup>TM</sup> Column Size

![](mmrs-1-4-user-guide/004.png)

13. In VistA, when prompted at Device: Home// enter the following: ;160;9999 and press the \<ENTER\> key.
14. Select all of the delimited data when it is displayed.
15. Copy the selected delimited data.
16. Open the NotePad™ application.
17. Select Paste from the Menu toolbar.
18. Save the file as a Text file with a .TXT extension to either the desktop or network drive. Note the location of the saved file.
19. Open the Excel™ spreadsheet CDI Reporting Tool.
20. Click once on the tab entitled Import VistA Report.
21. Select the cell A2 by placing the mouse in the cell and clicking once in the cell.

> **NOTE:** The example shown below is the CDI Acute Care Reporting Tool. Select the CDI Reporting Tool that is applicable, either CLC, Acute Care SCIU, or Acute Care.

<span id="_Toc473542001" class="anchor"></span>Figure 42: Select A2 in CDI Reporting Tool

![](mmrs-1-4-user-guide/005.png)

22. Select Data from the Excel™ Menu toolbar.
23. Select From Text to import data from the previously saved text file.
24. Navigate to the location of the previously saved Text file and select the Import button.
25. Select the Delimited button in the Text Import Wizard – Step 1 of 3 window. See the figure shown below for more information.

<span id="_Toc473542002" class="anchor"></span>Figure 43: Importing Delimited Data, Import Wizard Step 1 of 3

> ![](mmrs-1-4-user-guide/006.png)

26. Select the Next button in the Text Import Wizard – Step 1 of 3 window.
27. In the Text Import Wizard – Step 1 of 2 window, deselect the Tab Delimiter by clicking once in the checkbox.
28. In the Text Import Wizard – Step 1 of 2 window, select the Other Delimiter by clicking once in the checkbox and placing the carat ^ symbol in the box. See the figure shown below for more information.

<span id="_Toc473542003" class="anchor"></span>Figure 44: Importing Delimited Data, Import Wizard Step 2 of 3

> ![](mmrs-1-4-user-guide/007.png)

29. Select the Next button in the Text Import Wizard – Step 2 of 3 window.
30. Select the Finish button in the Text Import Wizard – Step 3 of 3 window.

<span id="_Toc473542004" class="anchor"></span>Figure 45: Importing Delimited Data, Import Wizard Step 3 of 3

> ![](mmrs-1-4-user-guide/008.png)

31. In the Import Data Window, select the OK button to accept the Existing Worksheet=\$A\$2. See the figure shown below for more information.
32. After importing the data, select Save As from the File Menu and save the worksheet to the local desktop or network drive.
33. Select all of the data imported in rows A through L by dragging the mouse across the data.
34. Select Copy from the Home menu.
35. Select the CDI Cases tab at the bottom of the Excel™ spreadsheet.
36. Click once into the A2 cell.
37. Select Paste from the Home menu.
38. Evaluate the data in cells F through I (regarding location) to determine a selection in cell J. Select a Patient location when CDI LabID Event was collected from the drop down list in cell J. Repeat this step for each patient.
39. Select Save from the File Menu to save the worksheet.

A description for the columns and headings from the report are outlined in the table below.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Heading</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Name</td>
<td>This field contains the patient's name.</td>
</tr>
<tr class="even">
<td>SSAN</td>
<td>This field contains the last 4 numbers of the patient's Social Security Account Number (SSAN).</td>
</tr>
<tr class="odd">
<td>Birth date</td>
<td>This field contains the patient's birth date and may be useful as some patients have the same name and last 4 digits of the SSAN. It is displayed in MM/DD/YY format.</td>
</tr>
<tr class="even">
<td>Date &amp; time of CDI LabID Event</td>
<td>This field contains the date and time that the <em>C. difficile</em> positive stool specimen for this episode was <u>collected</u> in MM/DD/YY HH:MM format.</td>
</tr>
<tr class="odd">
<td>Date &amp; time of admission associated with CDI LabID Event in Column D</td>
<td>This field contains the date and time the patient was admitted to the CLC facility in MM/DD/YY HH:MM format.</td>
</tr>
<tr class="even">
<td>Location Name</td>
<td>Information shown in this column will enable the user to choose the appropriate Patient Location when CDI LabID Event was collected in Column J.</td>
</tr>
<tr class="odd">
<td>Location Type</td>
<td>Information shown in this column will enable the user to choose the appropriate Patient Location when CDI LabID Event was collected in Column J.</td>
</tr>
<tr class="even">
<td>Location Service</td>
<td>Information shown in this column will enable the user to choose the appropriate Patient Location when CDI LabID Event was collected in Column J.</td>
</tr>
<tr class="odd">
<td>Location Stop Code</td>
<td>Information shown in this column will enable the user to choose the appropriate Patient Location when CDI LabID Event was collected in Column J.</td>
</tr>
<tr class="even">
<td>Patient location when CDI LabID Event collected</td>
<td>Select either acute input, output/ED, SCIU, CLC, or mental health as appropriate from the drop-down box.</td>
</tr>
<tr class="odd">
<td>Date &amp; time of most recent discharge from your inpt facility before Column E</td>
<td><p>This field contains the most recent discharge date &amp; time (MM/DD/YY HH:MM) if patient was discharged from the CLC facility at any time prior to the admission date in Column E;</p>
<p>Note: Mental health or observation discharges should not be included.</p></td>
</tr>
<tr class="even">
<td>Date &amp; time of most recent pos CDI LabID Event before test in Column D</td>
<td>If the patient had a previous CDI LabID Event, the date and time the most recent previous positive CDI LabID Event was collected (MM/DD/YY HH:MM) from any setting (acute inpatient, outpatient/ED, SCIU, CLC, or mental health) will be displayed. A CDI LabID Event can be counted from an outside (either VA or non-VA) facility if there is documentation (e.g. a scanned report) in CPRS.</td>
</tr>
<tr class="odd">
<td>Duplicate case</td>
<td>This field is automatically calculated using the formula: (TRUE/FALSE) = number of days from previous positive CDI LabID Event to current positive CDI LabID Event ≤14 days.</td>
</tr>
<tr class="even">
<td>Recurrent case</td>
<td>This field is automatically calculated using the formula: (TRUE/FALSE) = number of days from previous positive CDI LabID Event to current positive CDI LabID Event is &gt;14 and ≤56.</td>
</tr>
<tr class="odd">
<td>Incident case</td>
<td>This field is automatically calculated using the formula: (TRUE/FALSE) = number of days from previous positive CDI LabID Event to current positive CDI LabID Event is &gt;56 or there was no positive stool specimen.</td>
</tr>
<tr class="even">
<td>Pos CDI LabID Event collected upon admission</td>
<td>This field is automatically calculated using the formula: (TRUE/FALSE) = case where non-duplicate CDI LabID Event (Column D) was collected as an outpatient ≤24 hours before admission or as an inpatient ≤48 hours after the admission to your CLC facility listed in Column E. This includes recurrent cases (non-duplicate CDI LabID Events where the second CDI LabID Event was collected &gt;14 and ≤56 days after the first CDI LabID Event).</td>
</tr>
<tr class="odd">
<td><p>Community-</p>
<p>Onset CDI (CO-CDI)</p></td>
<td><p>This field is automatically calculated using the formula:</p>
<p>(TRUE/FALSE) = Patient admitted and a positive stool CDI LabID Event was collected as an outpatient ≤24 hours before admission or as an inpatient ≤48 hours after admission to your CLC facility AND non-duplicate/non-recurrent case AND patient location when the</p>
<p>CDI LabID Event was collected was "CLC", "acute inpt," "outpt/ED," or "SCIU."</p></td>
</tr>
<tr class="even">
<td>Community-Onset, CLC-Associated CDI (CO-CLC-Associated CDI)</td>
<td>This field is automatically calculated using the formula: (TRUE/FALSE) = Patient admitted and a positive stool CDI LabID Event was collected as an outpatient ≤24 hours before admission or as an inpatient ≤48 hours after admission to your CLC facility AND non-duplicate/non-recurrent case AND patient discharged from your CLC facility ≤28 days from date positive stool specimen was collected AND patient location when the CDI LabID Event was collected was "CLC", "acute inpt," "outpt/ED," or "SCIU."</td>
</tr>
<tr class="odd">
<td>CLC -Onset, CLC-Associated CDI case (CLC-Onset, CLC-Associated CDI)</td>
<td>This field is automatically calculated using the formula: field (TRUE/FALSE) = Positive stool CDI LabID Event collected &gt;48 hours after admission to your Community Living Center facility AND non-duplicate/non-recurrent case AND patient location when the CDI LabID Event was collected was "CLC".</td>
</tr>
<tr class="even">
<td>Clinically Confirmed CLC-Onset-CLC-Associated CDI</td>
<td><p>From the drop-down menu, enter whether the patient</p>
<p>was a Clinically Confirmed CLC-Onset, CLC-Associated CDI case (i.e. a patient with a positive CDI LabID Event plus either 1) diarrhea or 2) colonoscopic or histopathologic findings of pseudomembranous colitis). Enter "yes," "no," or "N/A" (not applicable) after chart review.</p></td>
</tr>
<tr class="odd">
<td>Date for 30-day review</td>
<td><p>This field is automatically calculated using the formula: when 30 days have passed since the positive laboratory CDI LabID Event in Column D.</p>
<p><strong>Note:</strong> This is the time to determine whether CDI complications occurred.</p></td>
</tr>
<tr class="even">
<td>CDI Complications</td>
<td>From the drop-down menu, select any adverse outcomes associated with CDI: ICU admit, colectomy, death, or combinations of outcomes if known.</td>
</tr>
<tr class="odd">
<td>Comments</td>
<td>If desired, enter any relevant notes or clinical details related to the case.</td>
</tr>
</tbody>
</table>

### Print CRE Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From the MDRO Tools Reports Menu, enter 5 for Print CRE Report and press the \<ENTER\> key.
2.  At the Do you want to select all Divisions: NO// prompt, enter either Yes or No based on the following criteria:
    1.  Entering Yes will obtain results for <u>all</u> divisions. See the figure below.
    2.  Entering No will obtain results for a particular division or divisions. After No is entered, a prompt will be displayed to enter the name of the division. Enter the name of the division and press the \<ENTER\> key. If desired, enter additional divisions.

> Note: The prompt will not display for a facility that is setup as a Single Division, it will only display for a Multi-Division Facility.

3.  At the Begin with facility admission date: prompt, enter a begin date and press the \<ENTER\> key.
4.  At the End with facility admission date: prompt, enter an end date and press the \<ENTER\> key.
5.  At the Do you want to only print the summary report? NO// prompt, enter either Yes or No based on the following criteria:
    1.  Enter No and press the \<ENTER\> key to print the Detailed Report.
    2.  Enter Yes and press the \<ENTER\> key to print the Summary Report.
6.  At the Device: HOME// prompt, enter the name of the printer or format to print to screen by entering the following: ;160;999 HOME and press the \<ENTER\> key.

<span id="_Toc473542005" class="anchor"></span>Figure 46: CRE Print Detailed Report for All Divisions

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MDRO Tools Reports Menu &lt;TEST ACCOUNT&gt; Option: 5  Print CRE Report</p>
<p>Do you want to select all divisions: NO// y  YES</p>
<p>Begin with facility admission date: 0911  (SEP 11, 2016)</p>
<p>End with facility admission date: 0918  (SEP 18, 2016)</p>
<p>Do you want to only print the summary report? NO//</p>
<p>This report is designed for a 176 column format (landscape).</p>
<p>DEVICE: HOME// ;160;999  HOME  (CRT)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> <span id="_Toc473542006" class="anchor"></span>Figure 47: Example of CRE Print Detail Report for All Divisions

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>CRE ACUTE CARE IPEC REPORT - DETAILED</p>
<p>             Division: FORT COLLINS</p>
<p>             Report period: Sep 11, 2016 to Sep 18, 2016@24:00</p>
<p>             Report printed on: Nov 10, 2016@11:22:18                 PAGE: 1</p>
<p>Basic Measures and Device Days of Care</p>
<p>   01 Total # of admissions to the acute care inpatient facility for the period: 8</p>
<p>   02 Total # of bed days of care for acute care for the period: 0</p>
<p>Admission Prevalence Measures (Facility/Division Wide)</p>
<p>   07 # of (01) with surveillance screens for CRE/CPE collected upon admission: 1</p>
<p>   08 # of (07) that were positive for CRE/CPE based on surveillance screen: 1</p>
<p>   09 # of (01) that were positive for CRE/CPE based on clinical cultures: 0</p>
<p>   10 % of (01) that were positive for CRE/CPE based on surveillance screening: 100%</p>
<p>   11 % of (01) that were positive for CRE/CPE based on clinical cultures: 0%</p>
<p>Incidence Measures: Healthcare-Associated Colonized Cases</p>
<p>   12 # of patients with screens for CRE/CPE collected 3 or more days after admission: 4</p>
<p>   13 # of (12) that were positive for CRE/CPE based on surveillance screen Collected 3 or more</p>
<p>days after admission: 2</p>
<p>   14 # of patients with clinical cultures positive for CRE/CPE 3 or more days after admission:</p>
<p>2</p>
<p>   15 Rate of healthcare-associated colonized cases: 0</p>
<p>Infection Prevention and Control Measures</p>
<p>   33 # of cases with CRE/CPE for the period: 5</p>
<p>             CRE ACUTE CARE IPEC REPORT - DETAILED</p>
<p>             Division: FORT COLLINS</p>
<p>             Report period: Sep 11, 2016 to Sep 18, 2016@24:00</p>
<p>             Report printed on: Nov 10, 2016@11:22:18                 PAGE: 2</p>
<p>DATE MAS MOVE SURVEILLANCE CLINICAL CULTURE</p>
<p>WARD SERVICE PATIENT LAST4  ENTERED WARD ADT TYPE SOURCE CULTURE CULTURE RESULT</p>
<p>---------------------------------------------------------------------------------------</p>
<p>---------------------------------------------------------------------------------------</p>
<p>C MEDICINE GENERAL(ACUTE MEDICINE)  PATIENTONE 6612   Sep 12,2016@22:28 DIRECT ACTIVE SKIN Y N POS</p>
<p>C MEDICINE GENERAL(ACUTE MEDICINE)  PATIENTTWO 1199   Sep 12,2016@23:00 DIRECT ACTIVE FECES N Y POS</p>
<p>ICU-S SURGICAL ICU             PATIENTTHREE 6610   Sep 12, 2016@23:19 DIRECT ACTIVE SKIN Y N POS</p>
<p>ICU-M      MEDICAL ICU              PATIENTFOUR 7722   Sep 12, 2016@23:25 DIRECT ACTIVE FECES N Y POS</p>
<p>END OF REPORT</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> <span id="_Toc473542007" class="anchor"></span>Figure 48: Example of CRE Print Detail Report for a Single Division

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>CRE ACUTE CARE IPEC REPORT - SUMMARY</p>
<p>             Division: CHEYENNE VAMROC</p>
<p>             Report period: Sep 08, 2016 to Sep 30, 2016@24:00</p>
<p>             Report printed on: Nov 10, 2016@11:10:59                 PAGE: 1</p>
<p>Basic Measures and Device Days of Care</p>
<p>01 Total # of admissions to the acute care inpatient facility for the period:5</p>
<p>02 Total # of bed days of care for acute care for the period: 0</p>
<p>Admission Prevalence Measures (Facility/Division Wide)</p>
<p>07 # of (01) with surveillance screens for CRE/CPE collected upon admission: 4</p>
<p>   08 # of (07) that were positive for CRE/CPE based on surveillance screen: 1</p>
<p>   09 # of (01) that were positive for CRE/CPE based on clinical cultures: 0</p>
<p>   10 % of (01) that were positive for CRE/CPE based on surveillance screening: 25%</p>
<p>   11 % of (01) that were positive for CRE/CPE based on clinical cultures: 0%</p>
<p>Incidence Measures: Healthcare-Associated Colonized Cases</p>
<p>   12 # of patients with screens for CRE/CPE collected 3 or more days after admission: 0</p>
<p>   13 # of (12) that were positive for CRE/CPE based on surveillance screen collected 3 or more</p>
<p>days after admission: 0</p>
<p>   14 # of patients with clinical cultures positive for CRE/CPE 3 or more days after admission:</p>
<p>0</p>
<p>   15 Rate of healthcare-associated colonized cases: 0</p>
<p>Infection Prevention and Control Measures</p>
<p>   33 # of cases with CRE/CPE for the period: 1</p>
<p>END OF REPORT</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

A description for the headings from the report are outlined in the table below.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>Basic Measures and Device Days of Care</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Header</strong></p>
</blockquote></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>01 Total # of admissions to the acute care inpatient facility for the period</td>
<td><p>Total number of admissions (not patients) to all units (excluding mental health and observation) of the hospital for the calendar month. In multi-division facilities transfers from one division to another are included as admissions (excluding in-hospital unit-to-unit transfers).</p>
<p><strong>Note:</strong> Some patients may be admitted more than once during the month.</p></td>
</tr>
<tr class="odd">
<td>02 Total # of bed days of care for acute care for the period</td>
<td>The number of bed days of care for the acute care facility for the month.</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>Admission Prevalence Measures (Facility/Division Wide)</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>07 # of (01) with surveillance screens for CRE/CPE collected upon admission</td>
<td><p>The number of admissions (not patients) to all acute care units of the hospital for the calendar month who received surveillance screening for CRE/CPE on admission (days 1 or 2of admission) to the facility during the month.</p>
<p><strong>Note:</strong> This number may include patients determined by the facility to be high risk for CRE/CPE and others who received screening.</p></td>
</tr>
<tr class="even">
<td colspan="2"><strong>Admission Prevalence Measures (Facility/Division Wide)</strong></td>
</tr>
<tr class="odd">
<td># of (07) positive for CRE/CPE based on surveillance screen</td>
<td>The number of surveillance screens on line (07) that were positive for CRE/CPE.</td>
</tr>
<tr class="even">
<td># of (01) positive for CRE/CPE based on clinical cultures</td>
<td>The number of admissions (not patients) to all acute care units (excluding mental health and observation) of the hospital for the calendar month with one or more clinical cultures positive for CRE/CPE upon admission during the month.</td>
</tr>
<tr class="odd">
<td>% (01) positive for CRE/CPE based on surveillance screening.</td>
<td>This field is automatically calculated by using the formula: (line 8 / line 7) * 100).</td>
</tr>
<tr class="even">
<td>% (01) positive for CRE/CPE based on clinical cultures</td>
<td>This field is automatically calculated by using the formula: (line 9 / line 1) * 100).</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Incidence Measures: Healthcare-Associated Colonized Cases</strong></td>
</tr>
<tr class="even">
<td>12 # of patients with screens for CRE/CPE collected 3 or more days after admission</td>
<td>The date of the surveillance screen occurs greater than or equal to (≥) 3 calendar days after the date of admission where the date of admission is calendar day one. The number of patients who had surveillance screens collected greater than or equal to (≥) 3 days after admission to determine presence of CRE/CPE. This includes patients who are epidemiologically linked to other patient(s) positive for CRE/CPE.</td>
</tr>
<tr class="odd">
<td>13 # of (12) that were positive for CRE/CPE based on surveillance screen collected 3 or more days after admission</td>
<td>the number of patients with CRE/CPE positive surveillance screens collected ≥ 3 days after admission for the facility for the month.</td>
</tr>
<tr class="even">
<td>14 # of patients with clinical cultures positive for CRE/CPE 3 or more days after admission</td>
<td>These are cultures that do not fit the NHSN definition for infection (i.e., they are colonized). Infections are defined using the current NHSN definitions. This is the number of patients with one or more clinical cultures positive for CRE/CPE that do not fit the NHSN definition for healthcare-associated infection (HAI) (those with actual infection should be counted for in lines 16 – 27). This may indicate that the patient is colonized with CRE/CPE. Each patient with a positive culture should only be counted once as patients may have more than one culture positive for CRE/CPE. There is a note # 2 (circled in red above) at the left side of the data entry field stating that these are cultures that do not fit the NHSN definition for infection (i.e., they are colonized) and that cases with both a CRE/CPE positive clinical culture and surveillance specimen will be recorded ONLY as a clinical culture case.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><strong>Incidence Measures: Healthcare-Associated Colonized Cases</strong></td>
</tr>
<tr class="odd">
<td>15 Rate of healthcare-associated colonized cases</td>
<td>This field is automatically calculated by using the formula: ((line 13 + line 14) / line 2) * 1000).</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Infection Prevention and Control Measures</strong></td>
</tr>
<tr class="odd">
<td>33 # of cases with CRE/CPE for the period</td>
<td>Total number of patients who were found to be positive for CRE/CPE on admission plus those found to have CRE/CPE colonization or infection after admission to the facility. This includes all patients with a positive CRE/CPE screening or clinical culture throughout admission. Although patients who are being screened should be placed in Contact Precautions awaiting the results of the screening, do not include those whose screens were negative on Line 33. Do not include patients who have a prior history of CRE/CPE but do not have a positive CRE/CPE clinical culture or surveillance screen during this admission.</td>
</tr>
</tbody>
</table>

## Tasked Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following reports can be set up in TaskMan to run automatically and print to a designated printer at specified frequencies during the day:

<table>
<colgroup>
<col style="width: 57%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>MMRS ISOLATION REPORT (TASKED)</p></li>
</ul></th>
<th>Print Isolation Report (Tasked)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>MMRS NARES SWAB LIST (TASKED)</p></li>
</ul></td>
<td>Print Nares Screen Compliance List</td>
</tr>
<tr class="even">
<td><ul>
<li><p>MDRO PRINT CDI REPORT (TASKED)</p></li>
</ul></td>
<td>Print Facility CDI Report (Tasked)</td>
</tr>
</tbody>
</table>

If the clinical staff desires to schedule any of the reports to automatically print to designated printers at specified times during the day, schedule these tasks in TaskMan.

### Print Isolation Report (Tasked)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option <u>should</u> <u>not</u> be run interactively. It should be scheduled by IRM staff to run via TaskMan using option Schedule/Unschedule Options \[XUTM SCHEDULE\]; this option will print the Isolation Report at specified times.

<span id="_Toc473542008" class="anchor"></span>Figure 49: Print Isolation Report (Tasked)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select TaskMan Management Option: <strong>Schedule/Unschedule Options</strong></p>
<p>Select OPTION to schedule or reschedule: <strong>"MMRS ISOLATION REPORT (TASKED)"</strong></p>
<p>Are you adding 'MMRS ISOLATION REPORT (TASKED)' as</p>
<p>a new OPTION SCHEDULING (the 329TH)? No// <strong>Y</strong> (Yes)</p>
<p>Edit Option Schedule</p>
<p>Option Name: MMRS ISOLATION REPORT (TASKED</p>
<p>Menu Text: Print Isolation Report (Tasked) TASK ID:</p>
<p>_______________________________________________________________</p>
<p>QUEUED TO RUN AT WHAT TIME: <strong>MAR 5,2017@15:50</strong></p>
<p>DEVICE FOR QUEUED JOB OUTPUT: <strong>IDM1$PRT LANDSCAPE;P-TCP LANDS</strong></p>
<p>QUEUED TO RUN ON VOLUME SET:</p>
<p>RESCHEDULING FREQUENCY: 12H</p>
<p>TASK PARAMETERS:</p>
<p>SPECIAL QUEUEING:</p>
<p>_______________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> **NOTE:** In order for the report to run correctly, when the option is scheduled to run in TaskMan via the option Schedule / Unschedule Options \[XUTM SCHEDULE\], several variables need to be configured on the second page of the form as described below.

1.  Add the Variable Name MMRSDIV and set the value of it to the Internal Entry Number (IEN) in File \#104 for the applicable Division.

> **NOTE:** See the Section entitled Obtaining a Division IEN Number for more information.

2.  Setting the variables:
    1.  To print the report for all locations or divisions, add the Variable Name. Set its value to "ALL"; the quotations are required.
    2.  To print for specific locations, add the Variable Name for each location. For example: MMRSLOC(LOCIEN), where LOCIEN is the geographical unit IEN from File \#104.3. Set its value to "". Use the \<TAB\> key to enter each variable. Note: the two double quotes are required for the Value; <u>do</u> <u>not</u> leave the Value blank.
3.  After configuring the variables, press the \<ENTER\> key.
4.  At the command prompt, type S to save the form and press the \<ENTER\> key.
5.  At the command prompt, type E to exit and press the \<ENTER\> key.

The figure below illustrates how to generate the option for Division 1 with geographical locations 3 and 5.

<span id="_Toc473542009" class="anchor"></span>Figure 50: Print Isolation Report (Tasked) with Division 1 and Geographical Locations 3, 5

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Edit Option Schedule</p>
<p>Option Name: MMRS ISOLATION REPORT (TASKED)</p>
<p>______________________________________________________________</p>
<p>USER TO RUN TASK:</p>
<p>VARIABLE NAME: MMRSDIV VALUE: 1</p>
<p>VARIABLE NAME: MMRSLOC(3) VALUE: ""</p>
<p>VARIABLE NAME: MMRSLOC(5) VALUE: ""</p>
<p>VARIABLE NAME: VALUE:</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The figure below illustrates how to generate the option for Division 1 with all Geographical Locations.

> **NOTE:** When tasking options, ALL has to be in quotations (i.e., "ALL").

<span id="_Toc473542010" class="anchor"></span>Figure 51: Print Isolation Report (Tasked) with Division 1 and All Geographical Locations

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Edit Option Schedule</p>
<p>Option Name: MMRS ISOLATION REPORT (TASKED)</p>
<p>______________________________________________________________</p>
<p>USER TO RUN TASK:</p>
<p>VARIABLE NAME: MMRSDIV VALUE: 1</p>
<p>VARIABLE NAME: MMRSLOC VALUE: "ALL"</p>
<p>VARIABLE NAME: VALUE:</p>
<p>VARIABLE NAME: VALUE:</p>
<p>VARIABLE NAME: VALUE:</p>
<p>­­­­­­­­­­­­­­­­­­­_________________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> **NOTE:** This option may be scheduled more than once. For example, if the site wants to schedule the report to print at different printers for different locations, place the option name in quotes as it will allow for the scheduling of the option for more than a single time.

### Print Nares Screen Compliance List (Tasked)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Nares Screen Compliance List (Tasked) option should not be run interactively; it should only be scheduled by IRM staff to run via TaskMan using option Schedule/Unschedule Options \[XUTM SCHEDULE\]. This option will print the Nares Compliance List at specified times.

<span id="_Toc473542011" class="anchor"></span>Figure 52: Print Nares Screen Compliance List (Tasked)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select TaskMan Management Option: <strong>Schedule/Unschedule Options</strong></p>
<p>Select OPTION to schedule or reschedule: <strong>"MMRS NARES SWAB LIST (TASKED)"</strong></p>
<p>Are you adding 'MMRS NARES SWAB LIST (TASKED)' as</p>
<p>a new OPTION SCHEDULING (the 329TH)? No// <strong>Y</strong> (Yes)</p>
<p>Edit Option Schedule</p>
<p>Option Name: MMRS NARES SWAB LIST (TASKED</p>
<p>Menu Text: Print Nares Screen Compliance List (Tasked) TASK ID:</p>
<p>_______________________________________________________________</p>
<p>QUEUED TO RUN AT WHAT TIME: MAR 5,2017@15:50</p>
<p>DEVICE FOR QUEUED JOB OUTPUT: IDM1$PRT LANDSCAPE;P-TCP LANDS</p>
<p>QUEUED TO RUN ON VOLUME SET:</p>
<p>RESCHEDULING FREQUENCY: 12H</p>
<p>TASK PARAMETERS:</p>
<p>SPECIAL QUEUEING:</p>
<p>_______________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> **NOTE:** In order for the report to run correctly, when the option is scheduled to run in TaskMan via the option Schedule / Unschedule Options \[XUTM SCHEDULE\], several variables need to be configured on the second page of the form as described below.

1.  Add the Variable Name MMRSDIV and set the value of it to the Internal Entry Number (IEN) in File \#104 for the applicable Division.

> **NOTE:** See the Section entitled Obtaining a Division IEN Number for more information.

2.  Setting the variables:
    1.  To print the report for all locations or divisions, add the Variable Name. Set its value to "ALL"; the quotations are required.
    2.  To print for specific locations, add the Variable Name for each location. For example: MMRSLOC(LOCIEN), where LOCIEN is the geographical unit IEN from File \#104.3. Set its value to "". Use the \<TAB\> key to enter each variable. Note: the two double quotes are required for the Value; <u>do</u> <u>not</u> leave the Value blank.
3.  After configuring the variables, press the \<ENTER\> key.
4.  At the command prompt, type S to save the form and press the \<ENTER\> key.
5.  At the command prompt, type E to exit and press the \<ENTER\> key.

The figure below illustrates how to generate the option for Division 1 with geographical locations 3 and 5.

<span id="_Toc473542012" class="anchor"></span>Figure 53: Print Nares Swab List (Tasked) with Division 1 and Geographical Locations 3, 5

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Edit Option Schedule</p>
<p>Option Name: MMRS NARES SWAB LIST (TASKED)</p>
<p>_______________________________________________________________</p>
<p>USER TO RUN TASK:</p>
<p>VARIABLE NAME: MMRSDIV VALUE: 1</p>
<p>VARIABLE NAME: MMRSLOC(3) VALUE: ""</p>
<p>VARIABLE NAME: MMRSLOC(5) VALUE: ""</p>
<p>VARIABLE NAME: VALUE:</p>
<p>_______________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The figure below illustrates how to generate the option for Division 1 and all Geographical Locations.

<span id="_Toc473542013" class="anchor"></span>Figure 54: Print Nares Swab List (Tasked) with Division 1 and All Geographical Locations

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Edit Option Schedule</p>
<p>Option Name: MMRS NARES SWAB LIST (TASKED)</p>
<p>_______________________________________________________________</p>
<p>USER TO RUN TASK:</p>
<p>VARIABLE NAME: MMRSDIV VALUE: 1</p>
<p>VARIABLE NAME: MMRSLOC VALUE: "ALL"</p>
<p>VARIABLE NAME: VALUE:</p>
<p>VARIABLE NAME: VALUE:</p>
<p>_______________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### MDRO Print CDI Report (Tasked)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MDRO Print CDI Report (Tasked) option should not be run interactively. It should only be scheduled by IRM staff to run via TaskMan using option Schedule/Unschedule Options \[XUTM SCHEDULE or MAIN^MMRSCDI2\]. This option will print the Facility CDI report at specified times utilizing the default date range of the previous month.

1.  In TaskMan, Select the option Schedule/Unschedule and press the \<ENTER\> key.
2.  When prompted, Select OPTION to schedule or reschedule:, enter MDRO and press the \<ENTER\> key.
3.  When prompted, enter the option number for MDRO PRINT CDI REPORT (TASKED) and press the \<ENTER\> key.
4.  When prompted, Are you adding 'MDRO PRINT CDI REPORT (TASKED)' as a new OPTION SCHEDULING (the 237TH)? No// Y respond Yes and press the \<ENTER\> key.

<span id="_Toc473542014" class="anchor"></span>Figure 55: MDRO Print CDI Report (Tasked)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Taskman Management &lt;TEST ACCOUNT&gt; Option: Schedule/Unschedule Options</p>
<p>Select OPTION to schedule or reschedule: MDRO</p>
<p>  1   MDRO PRINT CDI REPORT (TASKED) Print Facility CDI Report (Tasked)</p>
<p>  2   MDRO HISTORICAL DAYS EDIT MMRS MDRO HIST DAYS EDIT MDRO Historical</p>
<p>Days Edit</p>
<p>  3   MDRO TOOLS LAB PARAMETER SETUP MMRS MDRO LAB PARAMETER SETUP MDRO</p>
<p>Tools Lab Parameter Setup</p>
<p>CHOOSE 1-3: 1  MDRO PRINT CDI REPORT (TASKED)     Print Facility CDI Report (Tasked)</p>
<p>  Are you adding 'MDRO PRINT CDI REPORT (TASKED)' as</p>
<p>    a new OPTION SCHEDULING (the 237TH)? No// Y (Yes)</p>
<p>Edit Option Schedule</p>
<p>Option Name: MDRO Print CDI Report (TASKED</p>
<p>Menu Text: MDRO Print CDI Report (Tasked) TASK ID:</p>
<p>_______________________________________________________________</p>
<p>QUEUED TO RUN AT WHAT TIME: JAN 5,2017@15:50</p>
<p>DEVICE FOR QUEUED JOB OUTPUT: IDM1$PRT LANDSCAPE;P-TCP LANDS</p>
<p>QUEUED TO RUN ON VOLUME SET:</p>
<p>RESCHEDULING FREQUENCY: 1D</p>
<p>TASK PARAMETERS:</p>
<p>SPECIAL QUEUEING:</p>
<p>_______________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> **NOTE:** In order for the report to run correctly, when the option is scheduled to run in TaskMan via the option Schedule / Unschedule Options \[XUTM SCHEDULE\], several variables need to be configured on the second page of the form as described below.

5.  Add the Variable Name MMRSDIV and set the value of it to the Internal Entry Number (IEN) in File \#104 for the applicable Division.

> **NOTE:** See the Section entitled Obtaining a Division IEN Number for more information.

6.  Setting the variables:
    1.  To print the report for all locations or divisions, add the Variable Name. Set its value to "ALL"; the quotations are required.
    2.  To print for specific locations, add the Variable Name for each location. For example: MMRSLOC(LOCIEN), where LOCIEN is the geographical unit IEN from File \#104.3. Set its value to "". Use the \<TAB\> key to enter each variable. Note: the two double quotes are required for the Value; <u>do</u> <u>not</u> leave the Value blank.
7.  After configuring the variables, press the \<ENTER\> key.
8.  At the command prompt, type S to save the form and press the \<ENTER\> key.
9.  At the command prompt, type E to exit and press the \<ENTER\> key.

The figure below illustrates how to generate the option for Division 1 with geographical locations 3 and 5.

<span id="_Toc473542015" class="anchor"></span>Figure 56: MDRO Print CDI Report (Tasked) Division 1 and Geographical Locations 3, 5

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Edit Option Schedule</p>
<p>Option Name: MDRO PRINT CDI REPORT (TASKED)</p>
<p>_______________________________________________________________</p>
<p>USER TO RUN TASK:</p>
<p>VARIABLE NAME: MMRSDIV VALUE: 1</p>
<p>VARIABLE NAME: MMRSLOC(3) VALUE: ""</p>
<p>VARIABLE NAME: MMRSLOC(5) VALUE: ""</p>
<p>VARIABLE NAME: VALUE:</p>
<p>_______________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The figure below illustrates how to generate the option for Division 1 and all Geographical Locations.

<span id="_Toc473542016" class="anchor"></span>Figure 57: MDRO Print CDI Report (Tasked) with Division 1 and All Geographical Locations

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Edit Option Schedule</p>
<p>Option Name: MDRO PRINT CDI REPORT (TASKED)</p>
<p>_______________________________________________________________</p>
<p>USER TO RUN TASK:</p>
<p>VARIABLE NAME: MMRSDIV VALUE: 1</p>
<p>VARIABLE NAME: MMRSLOC VALUE: "ALL"</p>
<p>VARIABLE NAME: VALUE:</p>
<p>VARIABLE NAME: VALUE:</p>
<p>_______________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Obtaining a Division IEN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To obtain a division IEN, follow the instructions below.

1.  In FileMan, enter the option INQUIRE TO FILE ENTRIES and press the \<ENTER\> key.
2.  When prompted, OUTPUT FROM WHAT FILE:, enter MRSA SITE PARAMETERS and press the \<ENTER\> key.
3.  When prompted, Select MRSA SITE PARAMETERS DIVISION:, enter the division and press the \<ENTER\> key.

> The figure below illustrates how to obtain the IEN for a Division. The number highlighted in yellow is the IEN.

<span id="_Toc473542017" class="anchor"></span>Figure 58: Obtain MRSA Division IEN

VA FileMan 22.0

Select OPTION: INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: MRSA SITE PARAMETERS

Select MRSA SITE PARAMETERS DIVISION: XXXXX VAMC

ANOTHER ONE:

STANDARD CAPTIONED OUTPUT? Yes// (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// Record Number (IEN)

<span class="mark">NUMBER: 1</span> DIVISION: XXXXX VAMC

RECEIVING UNIT SCREEN: YES DISCHARGING UNIT SCREEN: YES

SCREEN POS ON TRANSFER IN: YES SCREEN POS ON DISCHARGE: YES

To obtain a Geographical Location IEN, follow the instructions below

1.  In FileMan, enter the option INQUIRE TO FILE ENTRIES and press the \<ENTER\> key.
2.  When prompted, OUTPUT FROM WHAT FILE:, enter MRSA WARD MAPPINGS and press the \<ENTER\> key.
3.  When prompted, Select MRSA WARD MAPPINGS NAME:, enter the ward and press the \<ENTER\> key.

> The figure below illustrates how to obtain the IEN for a Geographical Location. The number highlighted in yellow is the IEN.

<span id="_Toc473542018" class="anchor"></span>Figure 59: Obtain Geographical Location IEN

VA FileMan 22.0

Select OPTION: INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: MRSA WARD MAPPINGS

Select MRSA WARD MAPPINGS NAME: 11AB

ANOTHER ONE:

STANDARD CAPTIONED OUTPUT? Yes// (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// Record Number (IEN)

<span class="mark">NUMBER: 5</span> NAME: 11AB

DIVISION: XXXXX VAMC TYPE: ACUTE CARE

IPEC UNIT ID: 726

WARD LOCATION: 11AB

WARD LOCATION: 11ASURG

### Deleting a Variable Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To delete a variable name, follow the instructions below.

1.  Select the desired variable.
2.  Enter the @ symbol and press the \<ENTER\> key.

<span id="_Toc473542019" class="anchor"></span>Figure 60: Deleting a Variable Name

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Edit Option Schedule</p>
<p>Option Name: MDRO PRINT CDI REPORT (TASKED)</p>
<p>_______________________________________________________________</p>
<p>USER TO RUN TASK:</p>
<p>VARIABLE NAME: @ VALUE: "ALL"</p>
<p>VARIABLE NAME: VALUE:</p>
<p>VARIABLE NAME: VALUE:</p>
<p>VARIABLE NAME: VALUE:</p>
<p>_______________________________________________________________</p>
<p>COMMAND: Press &lt;PF1&gt;H for help</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3.  When prompted, SURE YOU WANT TO DELETE This entire subrecord? respond with Y and the \<ENTER\> key to delete the entire geographical unit from the setup.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes warning messages that will be displayed if errors are encountered when generating a report.

## Warning Message that Lab Test or Etiology Parameters are not configured

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Laboratory Test or Etiology parameters have not been configured, and a user attempts to generate the CDI Report, the following message will be displayed to the user:

<span id="_Toc473197311" class="anchor"></span>Figure 61: Warning Dialog regarding Lab Test/Etiology Configuration

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>The report cannot be run because the Laboratory Test(s) or</p>
<p>the Etiology is not configured in the MDRO TOOLS LAB</p>
<p>SEARCH/EXTRACT file, (104.1).  Use the MDRO Tools Lab Parameter Setup option to configure.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Consult the on MDRO Tools Lab Parameter Setup for information on how to enter laboratory and/or etiology parameters for historical reporting of multi-drug resistant organisms (MDROs).

## Warning Message that Etiology Parameter is not configured

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Etiology parameter has not been configured, and a user attempts to generate the CRE Report, the following message will be displayed to the user:

<span id="_Toc473197312" class="anchor"></span>Figure 62: Warning Dialog regarding Etiology Configuration

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>The report cannot be run because the Etiology has not been</p>
<p>configured in the MDRO TOOLS LAB SEARCH/EXTRACT file,</p>
<p>(#104.1).  Use the MDRO Tools Lab Parameter Setup option to configure.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Correct the issue by configuring the etiology parameters. Consult the section regarding MDRO Tools Lab Parameter Setup for more information.

## Warning Message that Specimen is not Configured

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a site has not configured specimen(s), and a user attempts to run the CRE Report, the following message will be displayed to the user:

<span id="_Toc473197313" class="anchor"></span>Figure 63: Warning Dialog regarding Specimen Configuration

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Make sure a division and/or a Surveillance specimen has been</p>
<p>setup using the option: 'CRE Tools Site Parameter Setup'</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Consult the section regarding the CRE Tools Parameter Setup menu option on how to configure the CRE parameters for division(s).

## Warning Message that Division(s) are not configured

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If divisions have not been configured, and the user attempts to generate a report without first defining a Division, a warning dialog will be displayed.

<span id="_Toc473542023" class="anchor"></span>Figure 64: Warning Dialog regarding Division Setup

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>&gt;&gt;&gt; Make sure the division has been setup using option:</p>
<p>'MDRO Tools Parameter Setup (Main)'</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Correct the issue by configuring the division(s). Consult the MDRO Tools Parameter Setup section for more information.

## Warning Message that Chemistry Subscripted Tests are not configured

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If Chemistry subscripted tests (MRSA SURVL NARES DNA, MRSA SURVL NARES AGAR) have not been configured, and the user attempts to generate a report, a warning dialog will be displayed.

<span id="_Toc473542024" class="anchor"></span>Figure 65: Warning Dialog regarding Chemistry Subscripted Tests

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>&gt;&gt;&gt; Make sure the MRSA Chemistry subscripted tests have been setup according to the National Guidelines. Laboratory needs to setup at least one of the lab tests in the system before generating reports:</p>
<p>1. 'MRSA SURVL NARES DNA'</p>
<p>2. 'MRSA SURVL NARES AGAR'</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Correct the issue by configuring the Chemistry subscripted tests. Consult the MDRO Tools Parameter Setup section for more information.

## Warning Message that the etiology Staphylococcus Aureus Methicillin Resistant (MRSA) has not been configured

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Staphylococcus Aureus Methicillin Resistant etiology has not been configured, and the user attempts to generate a report, a warning dialog will be displayed.

<span id="_Toc473542025" class="anchor"></span>Figure 66: Warning Dialog regarding Staphylococcus Aureus Methicillin Resistant etiology

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>&gt;&gt;&gt; Make sure the Etiology has been setup according to the National Guidelines. The following etiology must be added to the Etiology Field File (#61.2):</p>
<p>'STAPHYLOCOCCUS AUREUS METHICILLIN RESISTANT (MRSA)'</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Correct the issue by configuring the etiology parameters. Consult the section regarding MDRO Tools Lab Parameter Setup for more information.

## Warning Message that the Geographical Unit has not been configured

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Geographical Unit has not been configured, and the user attempts to generate a report, a warning dialog will be displayed.

<span id="_Toc473542026" class="anchor"></span>Figure 67: Warning Dialog regarding Geographical Unit

| \>\>\> Make sure the Ward Mappings for each Geographical Unit has been setup |
|------------------------------------------------------------------------------|

Correct the issue by configuring the Geographical Unit. Consult the section regarding MDRO Tools Ward Mapping Setup for more information.

# Printing in Landscape

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a sample Terminal Type for a landscape setup. Actual entries may vary depending on make and model of the printer.

<span id="_Toc473542027" class="anchor"></span>Figure 68: Printing in Landscape

NAME: P-TCP LANDSCAPE RIGHT MARGIN: 176

FORM FEED: \# PAGE LENGTH: 51

BACK SPACE: \$C(8)

OPEN EXECUTE: W \$C(27),"&l1O",\$C(27),"&l7C",\$C(27),"&k2S",\$C(27),"&l2E"

CLOSE EXECUTE: W \$C(27),"E" D CLOSE^NVSPRTU

# MAS Movement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes how MDRO-PT handles or interprets Medical Administration Service (MAS) movements.

For example, for a transaction type of Specialty Transfer, the MAS movement is excluded as there was not a change to the patient's room; there was only a change to the patient's status or service.

In the scenario of patients who float between the CLC and acute care, theoretically, two movements are created: one for the actual Transfer and one for the Absent Sick in Hospital (ASIH); however, the program will ignore the ASIH. The program will respond to the patient's movement as a discharge from the CLC and an Admission back into the CLC.

The table below states how the MDRO-PT handles or interprets Medical Administration Service (MAS) movements.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 28%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
<th>Clinical Transaction Type</th>
<th><p>Include/</p>
<p>Exclude</p></th>
<th>MDRO-PT Program Response</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AMBULATORY CARE (OPT-AC)</td>
<td>Admission to the VA facility from the Ambulatory Care (A/C) rolls.</td>
<td>Admission</td>
<td>Include</td>
<td>Admission</td>
</tr>
<tr class="even">
<td>DIRECT</td>
<td>Direct admission to the VA facility for treatment.</td>
<td>Admission</td>
<td>Include</td>
<td>Admission</td>
</tr>
<tr class="odd">
<td>NON-SERVICE CONNECTED (OPT-NSC)</td>
<td>Admission for inpatient treatment from the facility OPT-NSC program.</td>
<td>Admission</td>
<td>Include</td>
<td>Admission</td>
</tr>
<tr class="even">
<td>NON-VETERAN (OPT-NVE)</td>
<td>Admission of a patient who is not a veteran applicant for inpatient treatment.</td>
<td>Admission</td>
<td>Include</td>
<td>Admission</td>
</tr>
<tr class="odd">
<td>OPT-SC</td>
<td>Admission for inpatient treatment from the facility OPT-SC program.</td>
<td>Admission</td>
<td>Include</td>
<td>Admission</td>
</tr>
<tr class="even">
<td>PRE-BED CARE (OPT-PBC)</td>
<td>Admission from the OPT-PBC program for inpatient treatment.</td>
<td>Admission</td>
<td>Include</td>
<td>Admission</td>
</tr>
<tr class="odd">
<td>READMISSION TO IMLTC/NHCU/DOMICILIARY</td>
<td>Readmission to NHCU or Domiciliary within 30 days of last discharge from NHCU/Domiciliary.</td>
<td>Admission</td>
<td>Include</td>
<td>Admission</td>
</tr>
<tr class="even">
<td>TO ASIH</td>
<td>To the parent VA Hospital from the VANH or VAD in Absent Sick in Hospital (ASIH) status. Does not cause discharge from sending facility.</td>
<td>Admission</td>
<td>Include</td>
<td>Admission</td>
</tr>
<tr class="odd">
<td>TRANSFER IN</td>
<td>Transfer in (admission) from another VA facility to this VA facility.</td>
<td>Admission</td>
<td>Include</td>
<td>Admission</td>
</tr>
<tr class="even">
<td>WAITING LIST</td>
<td>Admission type to be used when admitting a patient from a waiting list.</td>
<td>Admission</td>
<td>Include</td>
<td>Admission</td>
</tr>
<tr class="odd">
<td>CHECK-IN LODGER</td>
<td>Check a lodger into the VA facility without impacting census data.</td>
<td>Check-in lodger</td>
<td>Exclude</td>
<td><u>Excluded</u></td>
</tr>
<tr class="even">
<td>CHECK-IN LODGER (OTHER FACILITY)</td>
<td>Check a lodger into a non-VA facility such as a local hotel.</td>
<td>Check-in lodger</td>
<td>Exclude</td>
<td><u>Excluded</u></td>
</tr>
<tr class="odd">
<td>CHECK-OUT LODGER</td>
<td>Check a lodger out of lodger status from either VA or non-VA facility.</td>
<td>Check-out lodger</td>
<td>Exclude</td>
<td><u>Excluded</u></td>
</tr>
<tr class="even">
<td>CONTINUED ASIH (OTHER FACILITY)</td>
<td>Discharge from the parent facility to ASIH in another VA (or non-VA) facility. Patient must have been sent to parent facility in ASIH status originally.</td>
<td>Discharge</td>
<td>Exclude</td>
<td><u>Excluded</u></td>
</tr>
<tr class="odd">
<td>DEATH</td>
<td>Expired while in receipt of inpatient care either in VA facility or in non-VA facility under VA auspices. Autopsy was NOT accomplished.</td>
<td>Discharge</td>
<td>Include</td>
<td>Discharge</td>
</tr>
<tr class="even">
<td>DEATH WITH AUTOPSY</td>
<td>Expired while in receipt of inpatient care either in VA facility or in non-VA facility under VA auspices. Autopsy was accomplished.</td>
<td>Discharge</td>
<td>Include</td>
<td>Discharge</td>
</tr>
<tr class="odd">
<td>DISCHARGE FROM IMLTC/NHCU/DOM WHILE ASIH</td>
<td>This movement type is used when discharging a patient from the NHCU/DOM ward prior to his hospital discharge and prior to 30 days. Use this type when it is evident that the patient will not return to the NHCU/DOM ward.</td>
<td>Discharge</td>
<td>Exclude</td>
<td><u>Excluded</u></td>
</tr>
<tr class="even">
<td>DISCHARGE TO CNH</td>
<td>Discharge type for the AMIE package for use when discharging a patient to a community nursing home.</td>
<td>Discharge</td>
<td>Include</td>
<td>Discharge</td>
</tr>
<tr class="odd">
<td>FROM ASIH</td>
<td>Discharge from VAH ASIH status with resumption of VANH/VAD episode of care.</td>
<td>Discharge</td>
<td>Include</td>
<td>Discharge</td>
</tr>
<tr class="even">
<td>IRREGULAR</td>
<td>Discharge from inpatient treatment against medical advice.</td>
<td>Discharge</td>
<td>Include</td>
<td>Discharge</td>
</tr>
<tr class="odd">
<td>NON-BED CARE</td>
<td>Discharge from inpatient treatment to the NBC (Non-bed care) rolls.</td>
<td>Discharge</td>
<td>Exclude</td>
<td><u>Excluded</u></td>
</tr>
<tr class="even">
<td>NON-SERVICE CONNECTED (OPT-NSC)</td>
<td>Discharge from inpatient treatment to the facility OPT-NSC rolls.</td>
<td>Discharge</td>
<td>Include</td>
<td>Discharge</td>
</tr>
<tr class="odd">
<td>NON-VETERAN</td>
<td>Discharge of a patient from inpatient care who was treated in a status other than as a veteran.</td>
<td>Discharge</td>
<td>Include</td>
<td>Discharge</td>
</tr>
<tr class="even">
<td>OPT-SC</td>
<td>Discharge from inpatient treatment to the OPT-SC rolls.</td>
<td>Discharge</td>
<td>Include</td>
<td>Discharge</td>
</tr>
<tr class="odd">
<td>REGULAR</td>
<td>Regular discharge from inpatient treatment.</td>
<td>Discharge</td>
<td>Include</td>
<td>Discharge</td>
</tr>
<tr class="even">
<td>TO DOM FROM HOSP</td>
<td>Discharge type created for the AMIE package to be used when discharging a hospital patient for admission to a domiciliary ward.</td>
<td>Discharge</td>
<td>Include</td>
<td>Discharge</td>
</tr>
<tr class="odd">
<td>TO IMLTC/NHCU FROM DOM</td>
<td>Discharge type created for AMIE for use when discharging a patient from a ward for admission to a nursing home care unit.</td>
<td>Discharge</td>
<td>Exclude</td>
<td><u>Excluded</u></td>
</tr>
<tr class="even">
<td>TO IMLTC/NHCU FROM HOSP</td>
<td>Discharge type created for the AMIE package used when discharging a hospital patient to the nursing home care unit.</td>
<td>Discharge</td>
<td>Include</td>
<td>Discharge</td>
</tr>
<tr class="odd">
<td>TRANSFER OUT</td>
<td>Transfer out (discharge) to another VA facility from this VA facility.</td>
<td>Discharge</td>
<td>Include</td>
<td>Discharge</td>
</tr>
<tr class="even">
<td>VA IMLTC/NHCU TO CNH</td>
<td>Discharge type added for the AMIE package to be used when discharging a patient from a VA nursing home care unit to a community nursing home.</td>
<td>Discharge</td>
<td>Include</td>
<td>Discharge</td>
</tr>
<tr class="odd">
<td>WHILE ASIH</td>
<td>Discharge from VAD/VANH while in an ASIH status at other facility either by termination of inpatient care or exceeding the 30-day ASIH period.</td>
<td>Discharge</td>
<td>Exclude</td>
<td><u>Excluded</u></td>
</tr>
<tr class="even">
<td>PROVIDER/SPECIALTY CHANGE</td>
<td>Change of provider and/or treating specialty without any other change in status, <em>i.e.</em>, ward, room remain same as prior to change.</td>
<td>Specialty transfer</td>
<td>Exclude</td>
<td><u>Excluded</u></td>
</tr>
<tr class="odd">
<td>AUTH ABSENCE 96 HOURS OR LESS</td>
<td>Transfer to an absence (pass) of 96 hours or less.</td>
<td>Transfer</td>
<td>Exclude</td>
<td><u>Excluded</u></td>
</tr>
<tr class="even">
<td>AUTHORIZED ABSENCE</td>
<td>To an authorized absence status of more than 96 hours but not greater than 7 days for hospital or 30 days for NHCU/Domiciliary.</td>
<td>Transfer</td>
<td>Include</td>
<td>Discharge</td>
</tr>
<tr class="odd">
<td>CHANGE ASIH LOCATION (OTHER FACILITY)</td>
<td>Continuation of ASIH status but to another VA or Non-VA facility at VA expense. [Previously called CONTINUED ASIH (OTHER FACILITY)]</td>
<td>Transfer</td>
<td>Exclude</td>
<td><u>Excluded</u></td>
</tr>
<tr class="even">
<td>FROM ASIH (VAH)</td>
<td>Return to NHCU or Domiciliary within the 30-day timeframe from Absence Sick in Hospital status.</td>
<td>Transfer</td>
<td>Include</td>
<td>Admission</td>
</tr>
<tr class="odd">
<td>FROM AUTH. ABSENCE OF 96 HOURS OR LESS</td>
<td>Return from a pass status which didn't exceed 96 hours in duration.</td>
<td>Transfer</td>
<td>Exclude</td>
<td><u>Excluded</u></td>
</tr>
<tr class="even">
<td>FROM AUTHORIZED ABSENCE</td>
<td>Return from authorized absence which was scheduled for greater than 96 hours.</td>
<td>Transfer</td>
<td>Include</td>
<td>Admission</td>
</tr>
<tr class="odd">
<td>FROM AUTHORIZED TO UNAUTHORIZED ABSENCE</td>
<td>Transfer from an authorized absence status to an unauthorized absence status.</td>
<td>Transfer</td>
<td>Exclude</td>
<td><u>Excluded</u></td>
</tr>
<tr class="even">
<td>FROM UNAUTHORIZED ABSENCE</td>
<td>Return from an unauthorized absence status within the 30-day limit (hospital) or 90-day limit (NHCU/Domiciliary).</td>
<td>Transfer</td>
<td>Include</td>
<td>Admission</td>
</tr>
<tr class="odd">
<td>FROM UNAUTHORIZED TO AUTHORIZED ABSENCE</td>
<td>Transfer from unauthorized absence to authorized absence status.</td>
<td>Transfer</td>
<td>Exclude</td>
<td><u>Excluded</u></td>
</tr>
<tr class="even">
<td>INTERWARD TRANSFER</td>
<td>Transfer from one ward location in the VA facility to another.</td>
<td>Transfer</td>
<td>Include</td>
<td>Transfer</td>
</tr>
<tr class="odd">
<td>RESUME ASIH IN PARENT FACILITY</td>
<td>Return to the parent VAH to continue ASIH status after being ASIH in another VA or non-VA facility. [Previously called CONTINUED ASIH]</td>
<td>Transfer</td>
<td>Include</td>
<td>Admission</td>
</tr>
<tr class="even">
<td>TO ASIH (OTHER FACILITY)</td>
<td>To Absent Sick in Hospital Status (ASIH) to somewhere other than the parent VA Hospital.</td>
<td>Transfer</td>
<td>Include</td>
<td>Discharge</td>
</tr>
<tr class="odd">
<td>TO ASIH (VAH)</td>
<td>Transfer from NHCU/Domiciliary to VA hospital for further care in Absent Sick in Hospital status. Can't exceed 30 days in duration.</td>
<td>Transfer</td>
<td>Include</td>
<td>Discharge</td>
</tr>
<tr class="even">
<td>UNAUTHORIZED ABSENCE</td>
<td>To an unauthorized absence status of not more than 30 days for hospital or 90 days for NHCU/Domiciliary.</td>
<td>Transfer</td>
<td>Include</td>
<td>Discharge</td>
</tr>
</tbody>
</table>

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Glossary of Terms</strong></th>
<th><strong>Definitions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Access Code</td>
<td><p>A code that allows the computer to identify</p>
<p>a user authorized to gain access to the computer. The code is greater than six and less than twenty characters long; can be numeric, alphabetic, or a combination of both. The code is usually assigned to a user by a site manager or application coordinator.</p></td>
</tr>
<tr class="even">
<td>ADPAC</td>
<td><p>Automated Data Processing Coordinator.</p>
<p>The ADPAC is the person responsible for planning and implementing new work methods and technology for employees throughout a medical center. ADPACs train employees and assist users when they run into difficulties, and needs to know how all components of the system work. ADPACs maintain open communication with their supervisors and Service Chiefs, as well as their counterparts in Fiscal and Acquisitions and Materiel Management (A&amp;MM), or Information Resource Management (IRM).</p></td>
</tr>
<tr class="odd">
<td>FileMan</td>
<td><p>FileMan is a set of M or MUMPS utilities written in the late 1970s and early 1980s which allow the definition of data structures, menus and security, reports, and forms.</p>
<p>FileMan's first use was in the development of medical applications for the Veterans Administration (now the Department of Veterans Affairs). Since it was a work created by the government, the source code cannot be copyrighted, placing that code in the public domain. For this reason, it has been used for rapid development of applications across a number of organizations, including commercial products.</p></td>
</tr>
<tr class="even">
<td>FORUM</td>
<td><blockquote>
<p>FORUM is the VA's national-scale email system. FORUM uses the VistA mail software and provides an excellent interface for threaded messages that can take the form on ongoing discussions. The National Patch Module is a VistA application that helps developers to manage the numbering, inventory, and release of patches. Patches are developed in response to request submissions and an error reporting request system known as National Online Information Sharing. A process called the Kernel Installation Distribution System (KIDS) is used to roll up patches into text messages that can be sent to sites along with installation instructions. The patch builds are sent as text messages via email, and the recipient (e.g., a site administrator) can run a PackMan function to unpack the KIDS build and install the selected routines.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>File Transfer Protocol (FTP)</td>
<td><blockquote>
<p>A client-server protocol which allows a user on one computer to transfer files to and from another computer over a TCP/IP network. Also the client program the user executes to transfer files. It is defined in Internet Standard 9, Request for Comments 959.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Globals</td>
<td><p>M uses globals or variables which are intrinsically stored in files and which persist beyond the program or process completion. Globals appear as normal variables with the caret character in front of the name. For example, the M statement…</p>
<p>SET ^A("first_name")="Keeley"</p>
<p>…will result in a new record being created and inserted in the persistent just as a file persists in an operating system. Globals are stored, naturally, in highly structured data files by the language and accessed only as M globals. Huge databases grow randomly rather than in a forced serial order, and the strength and efficiency of M is based on its ability to handle all this flawlessly and invisibly to the programmer.</p>
<p>One of the most common M programs is a database management system; FileMan is an example. M allows the programmer much wider control of the data; there is no requirement to fit the data into square boxes of rows and columns.</p></td>
</tr>
<tr class="odd">
<td>Kernel</td>
<td>The VistA software that enables VistA applications to coexist in a standard operating system independent computing environment.</td>
</tr>
<tr class="even">
<td>Kernel Installation and Distribution System (KIDS)</td>
<td>KIDS provides a mechanism to create a distribution of packages and patches; allows distribution via a MailMan message or a host file; and allows queuing the installation of a distribution for off-hours.</td>
</tr>
<tr class="odd">
<td>LIM</td>
<td><p>Laboratory Information Manager.</p>
<p>The LIM manages the laboratory files in VistA. Additional duties include creation of new tests, interface set-up and maintenance of instruments, coordination with staff outside of lab to create quick orders, order sets and other Computerized Patient Record System (CPRS) functions.</p></td>
</tr>
<tr class="even">
<td>M</td>
<td><p>M is a procedural, interpreted, multi-user, general-purpose programming language designed to build and control massive databases. It provides a simple abstraction that all data values are strings of characters, and that all data can be structured as multiple dimensional arrays. M data structures are sparse, using strings of characters as subscripts.</p>
<p>M was formerly (and is still commonly) called MUMPS, for Massachusetts General Hospital Utility Multiprogramming System.</p></td>
</tr>
<tr class="odd">
<td>Massachusetts General Hospital Utility Multi-Programming System (MUMPS)</td>
<td>See M</td>
</tr>
<tr class="even">
<td>MailMan</td>
<td>MailMan is an electronic messaging system that transmits messages, computer programs, data dictionaries, and data between users and applications located at the same or at different facilities. Network MailMan disseminates information across any communications medium.</td>
</tr>
<tr class="odd">
<td>MUMPS</td>
<td>See M</td>
</tr>
<tr class="even">
<td>Namespace</td>
<td>A logical partition on a physical device that contains all the artifacts for a complete M system, including globals, routines, and libraries. Each namespace is unique, but data can be shared between namespaces with proper addressing within the routines. In VistA, namespaces are usually dedicated to a particular function. The MMMS namespace, for example, is designed for use by MDRO-PT.</td>
</tr>
<tr class="odd">
<td>PackMan</td>
<td>A specific type of MailMan message used to distribute KIDS builds.</td>
</tr>
<tr class="even">
<td>VAMC</td>
<td><p>Department of Veterans Affairs Medical</p>
<p>Center.</p></td>
</tr>
</tbody>
</table>
#


---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: MMRS*1*5 User Guide

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Release MMRS\*1.0\*5 includes the following dependencies:

- MMRS\*1.0\*4
- LR\*5.2\*463
- Remediation steps completed per the MMRS\*1.0\*4 *Post-Installation Remediation Guide*. The guide is available on the Department of Veterans Affairs Software Document Library (VDL).

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security controls will be inherited from VistA and therefore will be fully compliant with National Institute of Standards and Technology (NIST) controls and in compliance with Directive 6500. In addition, the MMRS\*1.0\*5 release will be 508 compliant and designed to ensure no performance impacts will be experienced in the production environments.
