---
title: "Laboratory: Universal Interface Micro Interface Version 1 User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: 
app_code: LA
app_name: "Laboratory: Universal Interface"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 1
patch_id: 
group_key: "LA::1"
file_numbers: 
  - 61
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - release
  - default
  - contents
  - blockquote
  - class
  - micro
  - parameters
  - level
  - code
page_count: 0
word_count: 5020
section_count: 13
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2017
revision_count: 9
revision_newest: 04/12/2017
revision_oldest: 12/13/2016
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/lab_micro_interface_release_1_0_user_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/lab_micro_interface_release_1_0_user_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=120"
---

VistA Lab Enhancements – Microbiology

Release: Lab Micro Interface Release 1.0

(combined build for LA\*5.2\*90 and LR\*5.2\*474)

User Guide

![](laboratory-universal-interface-micro-interface-version-1-user-guide/001.png)

April 2017

Document Version 1.8

Office of Information and Technology (OI&T)

Revision History

> **NOTE:** The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

| Date       | Revision | Description                                                                                            | Author                             |
|------------|----------|--------------------------------------------------------------------------------------------------------|------------------------------------|
| 04/12/2017 | 1.8      | Updated System Summary section.                                                                        | <span class="mark">REDACTED</span> |
| 01/10/2017 | 1.7      | Addition of version number for Data Innovation’s Instrument Manager.                                   | <span class="mark">REDACTED</span> |
| 01/06/2017 | 1.6      | Removed version numbers from Patch Descriptions, section 1.2.6.                                        | <span class="mark">REDACTED</span> |
| 01/04/2017 | 1.5      | Updated cover page and references.                                                                     | <span class="mark">REDACTED</span> |
| 12/19/2016 | 1.4      | Clarifying information added to section 1.2.6; deletion of section 4.2.                                | <span class="mark">REDACTED</span> |
| 12/15/2016 | 1.3      | Minor revision of table 2 text and a sentence in section 2.                                            | <span class="mark">REDACTED</span> |
| 12/14/2016 | 1.2      | Addition of section 5.2. Figure 7 updated with example provided by <span class="mark">REDACTED</span>. | <span class="mark">REDACTED</span> |
| 12/13/2016 | 1.1      | Section 4.1 updated for preliminary and final status.                                                  | <span class="mark">REDACTED</span> |
| 12/13/2016 | 1.0      | Document baselined.                                                                                    | <span class="mark">REDACTED</span> |

<span id="_Ref251310381" class="anchor"></span>Table 1: Text Conventions

Artifact Rationale

Per the Veteran-focused Integrated Process (VIP) Guide, the User’s Guide is required to be completed prior to Critical Decision Point \#2 (CD2), with the expectation that it will be updated as needed. A User Guide is a technical communication document intended to give assistance to people using a particular system, such as VistA end users. It is usually written by a technical writer, although it can also be written by programmers, product or project managers, or other technical staff. Most user guides contain both a written guide and the associated images. In the case of computer applications, it is usual to include screenshots of the human-machine interfaces, and hardware manuals often include clear, simplified diagrams. The language used is matched to the intended audience, with jargon kept to a minimum or explained thoroughly. The User Guide is a mandatory, build-level document, and should be updated to reflect the contents of the most recently deployed build.

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
  - [Data Flows](#data-flows)
  - [User Access Levels](#user-access-levels)
  - [Continuity of Operation](#continuity-of-operation)
- [Using the Software](#using-the-software)
  - [Enter/verify data (auto instrument)](#enterverify-data-auto-instrument)
  - [Setting the Release Default at the Package Level](#setting-the-release-default-at-the-package-level)
  - [Setting the Release Default at the User Level](#setting-the-release-default-at-the-user-level)
  - [Review of User Settings](#review-of-user-settings)
- [Troubleshooting](#troubleshooting)
  - [HL7 ERR Segment](#hl7-err-segment)
- [Glossary](#glossary)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide describes the important features of the Lab Micro Interface Release 1.0 Kernel Installation and Distribution System (KIDs) combined build. The combined build contains the LR\*5.2\*474 and the LA\*5.2\*90 releases in support of the VistA Laboratory Microbiology initiative.

Patch LR\*5.2\*474 will provide new functionality to the Enter/Verify Data option of the Lab Universal Interface (UI) package. Three new release actions will now be available to the Technologist with the authority to release results. Results will be available to the applicable authorized clinicians and providers. In addition, the patch will allow a VA Medical Center the option of setting release defaults at the Package or User level.

Patch LA\*5.2\*90 will provide the constructs necessary to allow Microbiology or MI subscripted tests to be added to an Auto Instrument entry. An enhancement is also included for antibiotic susceptibility result processing which will now allow laboratories the ability to report susceptibilities to antimicrobial agents by utilizing SNOMED CT codes such as Positive and Negative. The handling of variations is also included in the build, such as the reporting of extended-spectrum beta-lactamases or ESBL enzymes that are resistant to most beta-lactam antibiotics. Locally mapped codes using an “L” for code set ID will now be processed for antibiotic susceptibilities.

All of the following SNOMED CT codes shall be supported with the release of patch LA\*5.2\*90:

- 131196009 Susceptible
- 260357007 Moderately susceptible
- 264841006 Intermediately susceptible
- 30714006 Resistant
- 10828004 Positive
- 260385009 Negative

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Organization of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide is arranged in a manner in which Laboratory Information Manager (LIM) and Automated Data Processing Application Coordinator (ADPAC) staff members who are well versed in the VistA Laboratory package will utilize the software.

The manual provides users with an explanation of the features that are a part of the Lab Micro Interface Release 1.0 build.

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide was written with the following assumed experience/skills of the audience:

- User has basic knowledge of the operating system (such as the use of commands, menu options, and navigation tools).
- User has been provided the appropriate active roles, menus, and security keys required.
- User is familiar with the VistA Laboratory software package.
- User has an understanding of Generic Instrument Managers (GIMs), such as Data Innovation’s Instrument Manager<sup>TM</sup> (IM).

### Coordination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Microbiology initiative is a collaborative solution between the VistA Laboratory Enhancement (VLE) Team and Clinical Laboratory personnel. This solution provides Microbiology Laboratory Technologists a system that integrates with the existing VistA Microbiology system, specifically, the Laboratory Universal Interface.

Deployment will be performed by Local Facility staff and supported by team members from one or more of the operations organizations: Enterprise Systems Engineering (ESE), Field Operations (FO), Enterprise Operations (EO), Lab Subject Matter Experts (SME) and / or others.

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely if any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section includes descriptions of any formatting or symbols and their meaning.

Various symbols are used throughout the documentation to alert the reader to special information. Table 1 gives a description of each of these symbols.

| Font              | Use                              | Example                                                                                                               |
|-----------------------|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Blue text, underlined | Hyperlink to another document or URL | For further instructions, refer to the following link: <http://www.va.gov/vdl>                                            |
| Courier New           | Menu options                         | MDRO Tools Parameter Setup                                                                                                |
|                       | Screen prompts                       | Want KIDS to INHIBIT LOGONs during the install? YES//                                                                     |
|                       | VistA filenames                      | XYZ file \#798.1                                                                                                          |
|                       | VistA field names                    | “In the Indicator field, enter the logic that is to be used to determine if the test was positive for the selected MDRO.” |
| Courier New, bold     | User responses to screen prompts     | NO                                                                                                                    |
| Courier New, bold     | Keyboard keys                        | \< F1 \>, \< Alt \>, \< L \>, \<Tab\>, \<Enter\>                                                                          |
| Courier New           | Report names                         | Procedures report                                                                                                         |
| Times New Roman       | Body text (Normal text)              | “There are no changes in the performance of the system once the installation process is complete.”                        |
| Times New Roman Bold  | Emphasis                             | Note: You can also type the access code, followed by a semicolon, followed by the verify code.                        |
| Times New Roman Bold  | Very Important                       | ![](laboratory-universal-interface-micro-interface-version-1-user-guide/002.png) symbol                |

<span id="_Toc393900385" class="anchor"></span>Table 2: Tier Support Contact Information

### References and Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation is also available on the VistA Document Library (VDL) The online versions will be updated as needed. Please look for the latest version on the VDL:

<http://www.va.gov/vdl>

The following documents were used in preparation of this guide:

- Technical Manual and Security Guide for Lab Micro Interface Release 1.0. December 2016, version 1.0.
- LA\*5.2\*90 Patch Description. November 2016. Note: this document is available via Forum only.
- LR\*5.2\*474 Patch Description. November 2016. Note: this document is available via Forum only.

## National Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The four tiers of support documented herein are intended to restore normal service operation as quickly as possible and minimize the adverse impact on business operations, ensuring that the best possible levels of service quality and availability are maintained.

Table 2 lists organizational contacts needed by site users for troubleshooting purposes. Support contacts are listed by name of service responsible to fix the problem, description of the incident escalation, associated tier level, and contact information.

| Name                                  | Role                   | Organization | Contact Information            |
|-------------------------------------------|----------------------------|------------------|------------------------------------|
| Site Laboratory Information Manager (LIM) | Tier 0 Support             | VHA              | Local to each facility             |
| OI&T National Service Desk                | Tier 1 Support             | OI&T             | <span class="mark">REDACTED</span> |
| OI&T Local Support                        | Tier 2 Support             | OI&T             | <span class="mark">REDACTED</span> |
| Health Product Support                    | Tier 2 Support             | VHA              | <span class="mark">REDACTED</span> |
| OI&T System Admin/Field Operation Support | Tier 2 & 3 support         | OI&T             | <span class="mark">REDACTED</span> |
| VistA Patch Maintenance                   | Tier 3 Application Support | OI&T             | <span class="mark">REDACTED</span> |
| Enterprise Operations                     | Tier 3 & 4 Support         | OI&T             | <span class="mark">REDACTED</span> |

<span id="_Toc469389182" class="anchor"></span>Table 3: Tier Support Contact Information for COTS Software

<table>
<caption>Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.</caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><strong>Role</strong></th>
<th><strong>Organization</strong></th>
<th><strong>Contact Information</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>LIM</td>
<td>Tier 0 Support</td>
<td>VHA</td>
<td>Local to each facility</td>
</tr>
<tr class="even">
<td>Commercial of-the-shelf (COTS) Vendor</td>
<td>Tier 2 Support</td>
<td>Vendor</td>
<td><p>Data Innovations</p>
<p><a href="http://www.datainnovations.com/">http://www.datainnovations.com/</a></p></td>
</tr>
</tbody>
</table>

Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.

# System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The combined build, Lab Micro Interface Release 1.0, which contains LR\*5.2\*474 and LA\*5.2\*90, are enhancements to the VistA Legacy Laboratory module to support the ability to electronically transfer organism identification and drug susceptibility testing results (generated by an automated instrument) to VistA.

Lab Micro Interface Release 1.0 is an upgrade to the VistA Laboratory UI and will work in conjunction with the functionality in the Auto Release 1.0 (LR\*5.2\*458 and LA\*5.2\*88) software build and Data Innovation’s enhanced IM driver software. Thus, the prerequisites for the utilization of the full functionality in the Lab Micro Interface Release 1.0 build includes the following:

- Auto Release 1.0 (LR\*5.2\*458 and LA\*5.2\*88)<span id="_Toc471369959" class="anchor"></span>.
- Data Innovations IM version 8.13.03 or greater.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following diagram depicts the high-level network configuration for a Veteran Affairs Medical Center (VAMC).

> <span id="_Toc471369981" class="anchor"></span>Figure 1: Simplified Topology for a VAMC

> ![](laboratory-universal-interface-micro-interface-version-1-user-guide/003.png)

## Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following illustration depicts the data flow between the VistA/Laboratory UI, Data Innovation’s IM, and the analyzers. The Laboratory UI generates the HL7 ORM, which is sent to the COTS middleware IM; the IM interfaces with the various instruments to receive data and sends an HL7 ORU back to the VistA Laboratory UI. Lab results are available through the VistA or the Computerized Patient Record System (CPRS).

> <span id="_Toc471369982" class="anchor"></span>Figure 2: Data Flow Diagram

> ![](laboratory-universal-interface-micro-interface-version-1-user-guide/004.png)

The diagram below depicts the sequence of events for both an inbound and an outbound message regarding messages and acknowledgments.

> <span id="_Toc471369983" class="anchor"></span>Figure 3: Inbound and Outbound Messaging

![](laboratory-universal-interface-micro-interface-version-1-user-guide/005.png)

## User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The core intended user base of the Lab Micro Interface Release 1.0 software build includes the following: laboratory staff; laboratory staff includes microbiology medical technologists and LIMs.

## Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event of an emergency, disaster, or accident, please contact the National Service Desk for support: <Nationalservicedeskanr@va.gov> or 1-855-673-4357.

# Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Enter/verify data (auto instrument) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enter/verify data (auto instrument) option will allow the releasing technologist the following release actions:

- 0 Quit
- 1 Release
- 2 Comments/Release
- 3 Edit (full)

Entering 0 will abort review/release.

Entering 1 will allow release 'as is' with no editing.

Entering 2 will allow you to enter/edit comments then release.

Entering 3 will allow you to enter full edit, similar to 'Results entry' option.

Selections 1-3 will allow editing of status and approved date/time.

## Setting the Release Default at the Package Level 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new parameter LR MI UI RELEASE DEFAULT is included with this patch which provides the VAMC site the ability to set the release default at the package and/or user levels.

To update the release default at the package level, perform the following steps:

1.  At the prompt, enter CC for Update CPRS Parameters.
2.  At the prompt, enter PP for Package Level Parameter Edit.
3.  Enter a default release action at the prompt Default Micro Instrument Release Action.
4.  If desired, set other applicable parameters and exit.

An example configuration is provided below.

<span id="_Toc471369984" class="anchor"></span>Figure 4: Example for setting the default release option at the Package Level

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Update CPRS Parameters &lt;TEST ACCOUNT&gt; Option: PP Package Level</p>
<p>Parameter Edit</p>
<p>Lab Package Level Parameters for Package: LAB SERVICE</p>
<p>--------------------------------------------------------------------------</p>
<p>Collect on Monday YES</p>
<p>Collect on Tuesday YES</p>
<p>Collect on Wednesday YES</p>
<p>Collect on Thursday YES</p>
<p>Collect on Friday YES</p>
<p>Collect on Saturday YES</p>
<p>Collect on Sunday YES</p>
<p>Lab Collects on Holidays YES</p>
<p>Lab Collect Days Allowed in Future 7</p>
<p>Maximum Days for Continuous Orders</p>
<p>Default manual verify method</p>
<p>Default load/work list verify method</p>
<p>Display Provider in Micro Result Entry</p>
<p>Default Micro Instrument Release Action VITEK Edit (full)</p>
<p>Prompt CPRS Alert in Micro Result Entry Don't Ask</p>
<p>Prompt CPRS Alert in CH Result Entry</p>
<p>EGFR Creatinine IDMS-traceable Method</p>
<p>EGFR Patient's Age Cutoff</p>
<p>EGFR Result Cutoff</p>
<p>Send an alert after AP release</p>
<p>Default AP Report Selection Prompt</p>
<p>Ask Performing Lab AP YES</p>
<p>Ask Performing Lab Micro YES</p>
<p>Print SNOMED Code System SNOMED I</p>
<p>Document Surgery Package Case Info NO</p>
<p>Chemistry GUI Report Right Margin</p>
<p>Microbiology GUI Report Right Margin</p>
<p>AP GUI Report Right Margin</p>
<p>Method of Assigning AP Accession Number</p>
<p>Default Accessioning Specimen</p>
<p>Default Accessioning Collection Sample</p>
<p>Default Accessioning Lab Test</p>
<p>Exclude removed tests from building</p>
<p>Use default accession dates</p>
<p>Print Reporting/Printing Facility None</p>
<p>Days to keep of instrument data 1 2</p>
<p>Lab STS Default Mapping Files Directory</p>
<p>Lab STS Default Mapping Filespec *.TXT</p>
<p>--------------------------------------------------------------------------</p>
<p>COLLECT MONDAY: YES//</p>
<p>COLLECT TUESDAY: YES//</p>
<p>COLLECT WEDNESDAY: YES//</p>
<p>COLLECT THURSDAY: YES//</p>
<p>COLLECT FRIDAY: YES//</p>
<p>COLLECT SATURDAY: YES//</p>
<p>COLLECT SUNDAY: YES//</p>
<p>IGNORE HOLIDAYS: YES//</p>
<p>LAB COLLECT DAYS ALLOWED IN FUTURE: 7//</p>
<p>MAXIMUM DAYS FOR CONTINUOUS ORDERS:</p>
<p>Default manual verify method:</p>
<p>For Default load/work list verify method -</p>
<p>Select Accession Area:</p>
<p>Display Provider in Micro Result Entry:</p>
<p>For Default Micro Instrument Release Action -</p>
<p>Select Load/Work List: VITEK</p>
<p>Load/Work List: VITEK// VITEK VITEK</p>
<p>Default load/work list verify method: Edit (full)//</p>
<p>For Default Micro Instrument Release Action -</p>
<p>Select Load/Work List:</p>
<p>NOTE: This parameter will allow the default release action to be</p>
<p>Load/Work List specific.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Setting the Release Default at the User Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To update the release default at the package level, perform the following steps:

1.  Select the Information Help menu option.
2.  At the prompt, enter PP for the General Lab User Parameters menu option.
3.  Enter a default release action at the prompt Default Micro Instrument Release Action.
4.  If desired, set other applicable parameters and exit.

An example configuration is provided below.

<span id="_Toc471369985" class="anchor"></span>Figure 5: Example for setting the default release option at the User Level

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Information-help menu &lt;TEST ACCOUNT&gt; Option: PP General Lab User</p>
<p>Parameters</p>
<p>Lab User Level Parameters for User: TECH,MICRO</p>
<p>--------------------------------------------------------------------------</p>
<p>Default lab label printer</p>
<p>Display previous comments for test</p>
<p>Default Performing Laboratory</p>
<p>Ask Performing Lab AP</p>
<p>Ask Performing Lab Micro</p>
<p>Display Provider in Micro Result Entry</p>
<p>Prompt CPRS Alert in CH Result Entry</p>
<p>Prompt CPRS Alert in Micro Result Entry</p>
<p>Default Micro Instrument Release Action VITEK Release</p>
<p>Default AP Report Selection Prompt</p>
<p>Send an alert after AP release</p>
<p>Default Accessioning Specimen</p>
<p>Default Accessioning Collection Sample</p>
<p>Default Accessioning Lab Test</p>
<p>Exclude removed tests from building</p>
<p>Use default accession dates</p>
<p>Lab Messaging - Parse HL7 Messages</p>
<p>Lab Messaging - Display using Browser</p>
<p>Lab Messaging - Show Identifiers</p>
<p>Chemistry GUI Report Right Margin</p>
<p>Microbiology GUI Report Right Margin 132</p>
<p>AP GUI Report Right Margin 240</p>
<p>Lab STS Default Mapping Files Directory</p>
<p>Lab STS Default Mapping Filespec</p>
<p>--------------------------------------------------------------------------</p>
<p>For Default lab label printer -</p>
<p>Select Division:</p>
<p>For Display previous comments for test -</p>
<p>Select Laboratory Test:</p>
<p>Default Performing Laboratory:</p>
<p>Ask Performing Lab AP:</p>
<p>Ask Performing Lab for MICRO:</p>
<p>Display Provider in Micro Result Entry:</p>
<p>Send CPRS Alert in CH Result Entry:</p>
<p>Send CPRS Alert in Micro Result Entry:</p>
<p>For Default Micro Instrument Release Action -</p>
<p>Select Load/Work List: VITEK</p>
<p>Are you adding VITEK as a new Load/Work List? Yes// YES</p>
<p>Load/Work List: VITEK// VITEK VITEK</p>
<p>Default load/work list verify method: Release</p>
<p>For Default Micro Instrument Release Action -</p>
<p>Select Load/Work List:</p>
<p>NOTE: This parameter will allow the default release action to be</p>
<p>Load/Work List specific.</p>
<p>AP Report Selection Default: ^</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Review of User Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If desired, the User Settings may be reviewed by performing the following steps:

1.  At the Lab Liaison menu prompt select OE/RR for the Interface Parameters menu option.
2.  At the OE/RR Interface Parameters prompt select CC for the Update CPRS Parameters menu option
3.  At the Update CPRS Parameters prompt select UL for the Display Lab User Parameters menu option.

An example of how to review the user settings is illustrated below.

<span id="_Toc471369986" class="anchor"></span>Figure 6: Example of Review User Settings option

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Lab liaison menu &lt;TEST ACCOUNT&gt; Option: OE/RR interface parameters</p>
<p>   EH     Edit HOSPITAL SITE parameters</p>
<p>   AS     Edit a lab administration schedule</p>
<p>   IL     Inquire to a Lab administration schedule</p>
<p>   CC     Update CPRS Parameters ...</p>
<p>Select OE/RR interface parameters &lt;TEST ACCOUNT&gt; Option: CC Update CPRS</p>
<p>Parameters</p>
<p>   PA     Update CPRS with Lab order parameters</p>
<p>   SI     Update CPRS with Single Lab test</p>
<p>   UP     Update CPRS with all Lab test parameters</p>
<p>   DO     Domain Level Parameter Edit</p>
<p>   LO     Location Level Parameter Edit</p>
<p>   PP     Package Level Parameter Edit</p>
<p>   UL     Display Lab User Parameters</p>
<p>Select Update CPRS Parameters &lt;TEST ACCOUNT&gt; Option: UL Display Lab User</p>
<p>Parameters</p>
<p>Select PARAMETER DEFINITION NAME:    LR MI UI RELEASE DEFAULT   Default Micro</p>
<p>Instrument Release Action</p>
<p>Values for LR MI UI RELEASE DEFAULT</p>
<p>Parameter                      Instance             Value</p>
<p>----------------------------------------------------------------------------</p>
<p>USR: TECH,MICRO                VITEK                Release</p>
<p>Enter RETURN to continue:</p>
<p>   PA     Update CPRS with Lab order parameters</p>
<p>   SI     Update CPRS with Single Lab test</p>
<p>   UP     Update CPRS with all Lab test parameters</p>
<p>   DO     Domain Level Parameter Edit</p>
<p>   LO     Location Level Parameter Edit</p>
<p>   PP     Package Level Parameter Edit</p>
<p>   UL     Display Lab User Parameters</p>
<p>Select Update CPRS Parameters &lt;TEST ACCOUNT&gt; Option:    </p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## HL7 ERR Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ERR segment is used to add error comments to acknowledgment messages when receiving ORU Result Messages. The fields supported are listed below and can be utilized in troubleshooting issues.

> ERR-3 HL7 Error Code

- If MSA-1 Acknowledgment Code is AA then ERR-3 will contain value 0 from HL7 Table 0357.
- If MSA-1 Acknowledgment Code is AE then ERR-3 will contain an error code/message from HL7 Table 0357.

> ERR-4 Severity

- If MSA-1 Acknowledgment Code is AA then ERR-4 will be blank.
- If MSA-1 Acknowledgment Code is AE then ERR-4 will contain an error code/message from HL7 Table 0357

ERR-5 Application Error Code

- If MSA-1 Acknowledgment Code is AA then ERR-5 will be blank.
- If MSA-1 Acknowledgment Code is AE then ERR-5 will contain an error code/message from VistA Laboratory LA7 MESSAGE LOG BULLETINS FILE (#62.485)

ERR-8 User Message

- If MSA-1 Acknowledgment Code is AA then ERR-8 will be blank.
- If MSA-1 Acknowledgment Code is AE then ERR-8 will contain text message from ERR-5.

ERR-9 Inform Person Indicator

- If MSA-1 Acknowledgment Code is AA then ERR-9 will be blank.
- If MSA-1 Acknowledgment Code is AE then ERR-9 will contain “USR”.

An example of an AE application error is shown below.

<span id="_Toc471369987" class="anchor"></span>Figure 7: Example Message with an AE application error.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>DATE/TIME ENTERED: NOV 19, 2016@07:37:36</p>
<p>  TRANSMISSION TYPE: OUTGOING</p>
<p>  RELATED EVENT PROTOCOL: LA7UI1 ORU-R01 EVENT</p>
<p>MESSAGE TEXT:  </p>
<p> MSA|AE|AITC001|Msg # 469, specimen source HL7 MAR in message does not match accession's UID 3716000013 related topography code. See file #61, TOPOGRAPHY entry # 70.</p>
<p> </p>
<p> ERR|||207^Application internal error^HL70357|E|49^Msg # 469, specimen source HL7 MAR in message does not match accession's UID 3716000013 related topography code. See file #61, TOPOGRAPHY entry # 70.^99VA62.485||</p>
<p>|Msg # 469, specimen source HL7 MAR in message does not match accession's UID 3</p>
<p>716000013 related topography code. See file #61, TOPOGRAPHY entry # 70.|USR</p>
<p> </p>
<p>  NO. OF CHARACTERS IN MESSAGE: 530   NO. OF EVENTS IN MESSAGE: 1</p></th>
</tr>
</thead>
<tbody>
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
<td><blockquote>
<p>A code that allows the computer to identify you as a user authorized to gain access to the computer. Your code is greater than six and less than twenty characters long; can be numeric, alphabetic, or a combination of both; and is usually assigned by a site manager or application coordinator.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>ADPAC</td>
<td><p>Automated Data Processing Coordinator.</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>The ADPAC is the person responsible for planning and implementing new work methods and technology for employees throughout a medical center. ADPACs train employees and assist users when they run into difficulties, and needs to know how all components of the system work. ADPACs maintain open communication with their supervisors and Service Chiefs, as well as their counterparts in Fiscal and Acquisitions and Materiel Management (A&amp;MM), or Information Resource Management (IRM). Also, the designated individual responsible for user-level management and maintenance of an application package (<em>e.g.</em>, Laboratory).</td>
</tr>
<tr class="even">
<td></td>
</tr>
</tbody>
</table></td>
</tr>
<tr class="odd">
<td>Auto Instruments</td>
<td><blockquote>
<p>Automated instruments used in the Lab that identify and measure tissue or other specimens.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Bactec<sup>TM</sup></td>
<td><blockquote>
<p>An automated instrument used for analyzing blood cultures within the Microbiology module.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>COTS</td>
<td><blockquote>
<p>Commercial off-the-shelf. Software or hardware that can be purchased as a packaged solution.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Driver</td>
<td><blockquote>
<p>Computer program which transports electronic information such as data or commands going between two computers or devices.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FileMan</td>
<td><blockquote>
<p>FileMan is a set of M utilities written in the late 1970s and early 1980s which allow the definition of data structures, menus and security, reports, and forms.</p>
<p>Its first use was in the development of medical applications for the Veterans Administration (now the Department of Veterans Affairs). Since it was a work created by the government, the source code cannot be copyrighted, placing that code in the public domain. For this reason, it has been used for rapid development of applications across a number of organizations, including commercial products.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FORUM</td>
<td><blockquote>
<p>FORUM is the VA’s national-scale email system. FORUM uses the VistA mail software and provides an excellent interface for threaded messages that can take the form on ongoing discussions. The National Patch Module is a VistA application that helps developers to manage the numbering, inventory, and release of patches. Patches are developed in response to request submissions and an error reporting request system known as National Online Information Sharing. A process called the Kernel Installation Distribution System (KIDS) is used to roll up patches into text messages that can be sent to sites along with installation instructions. The patch builds are sent as text messages via email, and the recipient (e.g., a site administrator) can run a PackMan function to unpack the KIDS build and install the selected routines.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>File Transfer Protocol (FTP)</td>
<td><blockquote>
<p>A client-server protocol which allows a user on one computer to transfer files to and from another computer over a TCP/IP network. Also the client program the user executes to transfer files. It is defined in Internet Standard 9, Request for Comments 959.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Generic Instrument Manager (GIM)</td>
<td><blockquote>
<p>Vendor system communicating with VistA is called a Generic Interface Manager (GIM).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Globals</td>
<td><blockquote>
<p>M uses globals: variables which are intrinsically stored in files and which persist beyond the program or process completion. Globals appear as normal variables with the caret character in front of the name. For example, the M statement…</p>
</blockquote>
<p>SET ^A(“first_name”)=”Brendan”</p>
<blockquote>
<p>…will result in a new record being created and inserted in the persistent just as a file persists in an operating system. Globals are stored, naturally, in highly structured data files by the language and accessed only as M globals. Huge databases grow randomly rather than in a forced serial order, and the strength and efficiency of M is based on its ability to handle all this flawlessly and invisibly to the programmer.</p>
<p>For all of these reasons, one of the most common M programs is a database management system. FileMan is one such example. M allows the programmer much wider control of the data; there is no requirement to fit the data into square boxes of rows and columns.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Kernel</td>
<td><blockquote>
<p>The VistA software that enables VistA applications to coexist in a standard operating system independent computing environment.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Kernel Installation and Distribution System (KIDS)</td>
<td><blockquote>
<p>KIDS provides a mechanism to create a distribution of packages and patches; allows distribution via a MailMan message or a host file; and allows queuing the installation of a distribution for off-hours.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>LIM</td>
<td><blockquote>
<p>Laboratory Information Manager.</p>
<p>The LIM manages the laboratory files in VistA. Additional duties include creation of new tests, interface set-up and maintenance of instruments, coordination with staff outside of lab to create quick orders, order sets and other Computerized Patient Record System (CPRS) functions.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>M</td>
<td><blockquote>
<p>M is a procedural, interpreted, multi-user, general-purpose programming language designed to build and control massive databases. It provides a simple abstraction that all data values are strings of characters, and that all data can be structured as multiple dimensional arrays. M data structures are sparse, using strings of characters as subscripts.</p>
<p>M was formerly (and is still commonly) called MUMPS, for Massachusetts General Hospital Utility Multiprogramming System.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Massachusetts General Hospital Utility Multi-Programming System (MUMPS)</td>
<td><blockquote>
<p>See M</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MailMan</td>
<td><blockquote>
<p>MailMan is an electronic messaging system that transmits messages, computer programs, data dictionaries, and data between users and applications located at the same or at different facilities. Network MailMan disseminates information across any communications medium.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Mass Spec<sup>TM</sup></td>
<td><blockquote>
<p>An automated instrument used for organism identification within the Microbiology module.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MUMPS</td>
<td><blockquote>
<p>See M</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Namespace</td>
<td><blockquote>
<p>A logical partition on a physical device that contains all the artifacts for a complete M system, including globals, routines, and libraries. Each namespace is unique, but data can be shared between namespaces with proper addressing within the routines. In VistA, namespaces are usually dedicated to a particular function. The MMMS namespace, for example, is designed for use by MRSA-PT.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PackMan</td>
<td><blockquote>
<p>A specific type of MailMan message used to distribute KIDS builds.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SNOMED CT</td>
<td><blockquote>
<p>Systematized Nomenclature of Medicine Clinical Terms was developed to standardize the coding of information regarding specific diseases.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VAMC</td>
<td><blockquote>
<p>Department of Veterans Affairs Medical Center.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Vitek<sup>TM</sup></td>
<td><blockquote>
<p>An automated instrument used for measuring antibiotic susceptibility within the Microbiology module.</p>
</blockquote></td>
</tr>
</tbody>
</table>
