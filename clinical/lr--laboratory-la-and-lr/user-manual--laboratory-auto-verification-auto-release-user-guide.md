---
title: Laboratory Auto Verification/Auto Release User Guide
doc_type: UG
doc_label: User Guide
doc_layer: plain
doc_subject: Laboratory Auto Verification/Auto Release
app_code: LR
app_name: Laboratory (LA and LR)
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - auto
  - release
  - vista
  - table
  - results
  - result
  - laboratory
  - instrument
  - contents
  - verification
page_count: 0
word_count: 8421
section_count: 8
table_count: 5
figure_count: 5
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Laboratory/labautorelease1_0_userguide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Laboratory/labautorelease1_0_userguide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=71"
---

## Table of Contents

  - [Introduction](#introduction)
    - [Purpose](#purpose)
    - [Document Orientation](#document-orientation)
    - [National Service Desk and Organizational Contacts](#national-service-desk-and-organizational-contacts)
  - [System Summary](#system-summary)
    - [High-Level Application Design](#high-level-application-design)
    - [System Configuration](#system-configuration)
    - [Data Flows](#data-flows)
    - [User Access Levels](#user-access-levels)
    - [Continuity of Operation](#continuity-of-operation)
  - [Getting Started](#getting-started)
    - [Logging On](#logging-on)
    - [System Menu](#system-menu)
    - [Changing User ID and Password](#changing-user-id-and-password)
    - [Exit System](#exit-system)
    - [Caveats and Exceptions](#caveats-and-exceptions)
  - [Using the Software](#using-the-software)
    - [Auto Verified Results from External System](#auto-verified-results-from-external-system)
    - [Tech Verified Result from External System](#tech-verified-result-from-external-system)
  - [Post Release Patches, LR\5.2\475 and LR\5.2\94](#post-release-patches-lr52475-and-lr5294)
  - [Troubleshooting](#troubleshooting)
    - [Order Message Acknowledgements](#order-message-acknowledgements)
    - [Result Acknowledgements](#result-acknowledgements)
  - [Acronyms, Abbreviations, Definitions](#acronyms-abbreviations-definitions)
VistA Lab EnhancementsAuto Verification/Auto ReleaseUser GuideVersion 0.7
![](laboratory-auto-verification-auto-release-user-guide/001.png)
October 2024Department of Veterans AffairsOffice of Information and Technology (OI&T)
Revision History
<table>
<caption><p>Table 1. Documentation Symbols and Descriptions</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 12%" />
<col style="width: 45%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
<tr class="odd">
<th>9/2024</th>
<th>0.7</th>
<th><p>Release: LR*5.2*574</p>
<p>A note was added that results which are auto released do not trigger automatic printing of the Interim Report.</p></th>
<th><mark>REDACTED</mark></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>12/1/16</td>
<td>0.6</td>
<td>Added Warranty Release: LA*5.2*94 &amp; LR*5.2*475 information</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>6/28/2016</td>
<td>0.5</td>
<td>Final peer review; remove template’s instructional text (blue)</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>6/24/2016</td>
<td>0.4</td>
<td>Updated support information, clarified as necessary</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>06/23/2016</td>
<td>0.3</td>
<td>Merge edits from peer reviews; formatted examples of screen/print shots.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>6/10/16</td>
<td>0.2</td>
<td>Updates</td>
<td>SME input</td>
</tr>
<tr class="even">
<td>05/11/2016</td>
<td>0.1</td>
<td>Draft</td>
<td>VLE_PMO</td>
</tr>
</tbody>
</table>
Table 1. Documentation Symbols and Descriptions
Table of Contents

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Laboratory software enhancement will enable Auto Verification and Auto Release of normal lab results. Initially developed at the Kansas City Veterans Affairs Medical Center (VAMC), this new process involves automatic review and release of test results based on lab-established set of boundaries, also referred as rules, rule sets, and algorithms. Lab results that are in a "normal" range, as pre-determined by the laboratory, will transmit directly from the middleware to VistA Laboratory files and on to Computerized Patient Record System (CPRS) without the intermediate step of requiring a lab technologist to manually review and sign off on these normal lab results. This process will eliminate the need for a qualified technologist to manually approve all "normal" results before those results are filed in VistA Laboratory files and available for clinicians to view in CPRS.

Each VAMC site will determine which instruments will use this functionality as it can be set up on an instrument by instrument basis. Essentially VistA Laboratory instruments are set up as either being available for auto verification or not available for auto verification. If an instrument is set up for auto verification, then a lab result passing the rule set will be filed by the middleware in VistA Laboratory files and available in CPRS and a lab result that cannot pass the rule set will be held in the middleware system for review by a lab technologist.

### Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Organization of the Manual

This manual is prepared primarily for Laboratory Information Managers (LIM) or those acting in that role, and for those Laboratory representatives installing, supporting, and maintaining auto verification functions.

#### Assumptions

The users of the laboratory information automatically released include physicians, nurses, laboratory staff, and Veterans. However, it is important to note that for the VistA patches providing the new Auto Release Capabilities, this will be transparent to the end users of the information. Only LIMs and Medical Technologists may have a need to review processing queues.

#### Coordination

The site LIM, or site application coordinator if designated, is responsible for the implementation and coordination of these patches with local or Regional Office of Information & Technology (OI&T) personnel and Laboratory operations.

No downtime is required for installation of these patches, however, testing to confirm installation and normal operation is still recommended.

#### Disclaimers

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

Blood Bank Review:

EFFECT ON BLOOD BANK FUNCTIONAL REQUIREMENTS: Patches LA\*5.2\*88 and LR\*5.2\*458 do not contain any changes to the VISTA BLOOD BANK Software as defined by ProPath standard titled: BBM Team Review of VistA Patches.

EFFECT ON BLOOD BANK FUNCTIONAL REQUIREMENTS: Patches LA\*5.2\*88 and LR\*5.2\*458 do not alter or modify any software design safeguards or safety critical elements functions.

RISK ANALYSIS: Changes made by patches LA\*5.2\*88 and LR\*5.2\*458 have no effect on Blood Bank software functionality, therefore RISK is none.

VALIDATION REQUIREMENTS BY OPTION: Because of the nature of the changes made,

no specific validation requirements exist as a result of installation of this patch.

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the VA of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

#### Documentation Conventions

This manual uses several methods to highlight different aspects of the material.

Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols.

| Symbol                                                                                                                                                                                                                                 | Description                                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| ![](laboratory-auto-verification-auto-release-user-guide/002.png)                                                        | NOTE: Used to inform the reader of general information including references to additional reading material. |
| ![](laboratory-auto-verification-auto-release-user-guide/003.png) | CAUTION: Used to caution the reader to take special notice of critical information.                     |

Table 2. Tier Support Contact Information for VistA

“Snapshots” of computer online displays (i.e., character-based screen captures/dialogs) and computer source code are shown in a non-proportional font and enclosed within a box. Also included are Graphical User Interface (GUI) Microsoft Windows images (i.e., dialogs or forms).

User's responses to online prompts (e.g., manual entry, taps, clicks, etc.) will be boldface type.

All uppercase is reserved for the representation of acronyms, M code, variable names, or the formal name of options, field and file names, and security key (e.g., the XUPROGMODE key).

#### References and Resources

The following documents have been updated/added as a result of the enhancements made for Auto Verification. These are available at SOFTWARE.DIR and the VistA Documentation Library (VDL) website as a secondary source.

- Lab UI HL V1.6 Upgrade Interface Specifications Document
- LR\*5.2\*458 and LA\*5.2\*88-Universal Interface-Release Notes
- LR\*5.2\*458 and LA\*5.2\*88-(Lab Auto Release 1.0) User Guide
- LR\*5.2\*458 and LA\*5.2\*88-(Lab Auto Release 1.0) Technical Manual/Security Guide

Reference material for Lab Universal Interface 1.6, also available on SOFTWARE.DIR and VDL as a secondary source:

- Lab UI HL V1.6 Upgrade Installation and User Guide LA\*5.2\*66

### National Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA support follows your site’s already functioning support structure, and any issues with Auto Verification installation, set up, or use within VistA should be directed to your normal support channels, most common listed in the table 2 below.

VistA support representatives will not be able to assist with commercial off-the-shelf (COTS) vendor products, their rules creation and use, troubleshooting, and operations; these should be directed to your COTS middleware vendor.

<table>
<caption>Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><strong>Role</strong></th>
<th><strong>Org</strong></th>
<th><strong>Contact Info</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>LIM</td>
<td>Tier 0 Support</td>
<td>VHA</td>
<td>Site Laboratory Information Manager</td>
</tr>
<tr class="even">
<td>OI&amp;T Local Support</td>
<td>Tier 2 Support</td>
<td>OI&amp;T</td>
<td>OI&amp;T Local Helpdesk</td>
</tr>
<tr class="odd">
<td>OI&amp;T National Service Desk</td>
<td>Tier 1 Support</td>
<td>OI&amp;T</td>
<td><p><a href="mailto:Nationalservicedeskanr@va.gov">Nationalservicedeskanr@va.gov</a></p>
<p>1-855-673-4357</p></td>
</tr>
<tr class="even">
<td>Health Product Support</td>
<td>Tier 2 Support</td>
<td>VHA</td>
<td><p><a href="mailto:Nationalservicedeskanr@va.gov">Nationalservicedeskanr@va.gov</a></p>
<p>1-855-673-4357</p></td>
</tr>
<tr class="odd">
<td>VistA Patch Maintenance</td>
<td>Tier 3 Application Support</td>
<td>OI&amp;T</td>
<td><p><a href="mailto:Nationalservicedeskanr@va.gov">Nationalservicedeskanr@va.gov</a></p>
<p>1-855-673-4357</p></td>
</tr>
</tbody>
</table>

Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.

Table 3. Tier Support Contact Information for COTS GIM

| Name    | Role       | Org | Contact Info                    |
|-------------|----------------|---------|-------------------------------------|
| LIM         | Tier 0 Support | VHA     | Site Laboratory Information Manager |
| COTS Vendor | Tier 2 Support | Vendor  | COTS Vendor                         |

Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.

## System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Auto Release Capability works in conjunction with an external COTS product that allows the VA to implement rules that evaluate results transmitted by Laboratory instrumentation and verifies them automatically or holds them for review and manual release by a Medical Technologist (MT). Once verified by either middleware rules or an MT and sent to VistA via the Laboratory Universal Interface, the new VistA Auto Release Capability accepts, stores, and makes the results available to clinical providers without the need for human interaction.

The Figure 1 section outlines the major functions of the VistA Auto Release Capability enhancements as well as the COTS Auto Verification System. For purposes of this release all testing was performed with the predominant COTS system in use throughout the VA, the Data Innovations (DI) Instrument Manager (IM).

Figure 1: VistA Auto Verification and Auto Release Major Functions

![](laboratory-auto-verification-auto-release-user-guide/004.png)

The VistA Auto Release Capability is an enhancement to the VistA Legacy Laboratory module which gives VistA Laboratory the ability to accept automatically verified results from COTS middleware and automatically release those results.

The Figure 1 diagram below shows the context of the VistA Legacy Laboratory Auto Release Capability to the COTS Auto Verification System using such a COTS product. In this case, Instrument Manager by Data Innovations is shown.

Figure 2: VistA Auto Release Enhancement to the VistA Lab Application - Context Diagram

![](laboratory-auto-verification-auto-release-user-guide/005.png)

Table 4, below, describes the information in the Application Context Diagram.

Table 4: Application Context Description

<table>
<caption>Information in the Application Context Diagram in four sections. Note that the system for which this design applies is represented by a single object (typically in the center of the diagram).</caption>
<colgroup>
<col style="width: 6%" />
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 18%" />
<col style="width: 13%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th>ID</th>
<th>Name</th>
<th>Description</th>
<th>Interface Name</th>
<th colspan="2">Interface System</th>
</tr>
<tr class="odd">
<th>1</th>
<th>VistA Laboratory System – Auto Release Enhancements</th>
<th>Shows how VistA Legacy Laboratory system is enhanced to include the ability to Auto Release verified results.</th>
<th><p>ORM Order Message</p>
<p>ORU Result Message</p>
<p>Remote Procedure Calls (many)- existing</p></th>
<th colspan="2"><p>Data Innovations</p>
<p>CPRS</p>
<p>Health Data Repository (HDR)</p>
<p>Clinical Data Warehouse (CDW) and 32+ downstream systems.</p></th>
</tr>
<tr class="header">
<th>ID</th>
<th>Name</th>
<th>Related Object</th>
<th>Input Messages</th>
<th>Output Messages</th>
<th>External Party</th>
</tr>
<tr class="odd">
<th>2</th>
<th>External Laboratory Systems</th>
<th>External Lab</th>
<th>Lab Orders</th>
<th>Lab Results</th>
<th>Varies: VistA, LabCorp, Quest, etc.</th>
</tr>
<tr class="header">
<th>ID</th>
<th>Name</th>
<th>Related Object</th>
<th>Input Messages</th>
<th>Output Messages</th>
<th>External Party</th>
</tr>
<tr class="odd">
<th>3</th>
<th>CPRS</th>
<th>Remote Procedure Calls</th>
<th>Lab Orders</th>
<th>Lab Results</th>
<th>N/A</th>
</tr>
<tr class="header">
<th>ID</th>
<th>Name</th>
<th colspan="2">Data Stored</th>
<th>Owner</th>
<th>Access</th>
</tr>
<tr class="odd">
<th>4</th>
<th>HDR &amp; CDW</th>
<th colspan="2">Laboratory Results</th>
<th>OIT</th>
<th>HL7 Interface</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Information in the Application Context Diagram in four sections. Note that the system for which this design applies is represented by a single object (typically in the center of the diagram).

### High-Level Application Design

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the high level design for the VistA Auto Release Capability, shown in Figure 3.

Figure 3: High-Level Application Diagram

![](laboratory-auto-verification-auto-release-user-guide/006.png)

> **NOTE:** Results which are auto released do not trigger automatic printing of the Interim Report.

Table 5, below, describes Objects in the High Level Application Diagram.

Table 5: Objects in the High Level Application Diagram

| ID  | Name                      | Description                                                             | Service or Legacy Code |
|-----|---------------------------|-------------------------------------------------------------------------|------------------------|
| 1   | VistA Legacy Lab          | Manages Laboratory Order Requests & Result Reports                      | VistA                  |
| 2   | VistA Universal Interface | Manages interfaces between VistA Lab and Instruments/Middleware         | VistA                  |
| 3   | Auto Release              | New Routines added to automatically release externally verified results | VistA                  |

Objects / Components to be Built or Modified

Table 6, below, describes the Internal Data Stores.

Table 6: Internal Data Stores

| ID         | Name  | Data Stored                        | Steward    | Access     |
|------------|-------|------------------------------------|------------|------------|
| No Changes | VistA | Lab order requests and Lab results | No Changes | No Changes |

Internal Data Stores

### System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following diagram shows the Data Innovations middleware, Instrument Manager and the Laboratory instruments on the local area network, while the VistA systems may be locally or regionally located and on the VA’s wide area network.

Figure 4: VistA Lab System Configuration

![](laboratory-auto-verification-auto-release-user-guide/007.png)

#### Configuration Considerations for External Generic Interface Manager (GIM)

Ensure the minimum version level meets specifications

i.e. (8.13.03) of Data Innovations (DI) Instrument Manager and the latest DI VA driver (currently V 8.00.0017). Follow vendor provided instructions to properly configure for Auto Verification.

Make sure all Laboratory Techs have the LRVERIFY security key in VistA. If not done, and a user manually verifies a result on IM and sends to VistA it will fail and generate an interface Application Error. See item \#5 in section 2.2.2 below for a report that will list users and related security keys to be used as source document to configure generic interface manager (GIM). Also the Troubleshooting section in this guide.

#### Initial Configuration to Activate VistA Auto Release

1.  Set Auto Release Results System Wide parameter to enabled.

The Auto Release Results System Wide \[LA7UI AUTO RELEASE MASTER\] parameter is a system-wide switch that can quickly enable/disable the Auto Release process. When this parameter is set to Disabled, it will disable the Auto Release process on this system, and will override the settings in the Auto Instrument file. When enabled, this will enable the Auto Release process for instruments that are marked for Auto Release (via the Auto Release field… see step \#4 below).

Select Lab Universal Interface Menu Option: UIS Lab Universal Interface Setup

Select one of the following:

1 LA7 MESSAGE PARAMETER (#62.48)

2 AUTO INSTRUMENT (#62.4)

3 Auto Release System Parameter

4 Configuration Report (132 COL)

5 Holders of Lab keys

6 Ordering Provider Contact Parameter

7 Convert LAB UI 1.6 to Enhanced Acknowledgement Mode

Select which file to setup: 3 Auto Release System Parameter

Auto Release Results System Wide may be set for the following:

1 System SYS \[xxxxxxxxxxxxxxx\]

10 Package PKG \[LAB MESSAGING\]

Enter selection: 1 System xxxx.xxxx.xxx.xx.xxx

Setting Auto Release Results System Wide for System: xxxx.xxxx.xxx.xx.xxx

AUTO RELEASE RESULTS SYSTEM WIDE: YES (ENABLED)// ??

This parameter is used to determine whether lab results are sent to the

auto release process.

AUTO RELEASE RESULTS SYSTEM WIDE: YES (ENABLED)// ?

Do you want to Auto Release Results System Wide?.

Select one of the following:

0 NO (DISABLED)

1 YES (ENABLED)

AUTO RELEASE RESULTS SYSTEM WIDE: YES (ENABLED)//

2.  Enable the instrument(s) for Auto Release.

The Auto Release field (#99) in the Auto Instrument file (#62.4) enables Auto Release on an instrument by instrument basis. It allows for different levels of granularity.

- Data Type: AUTO RELEASE (or any data type)
  - 0: NO
  - 1: YES
  - 2: AUTO VERIFY ONLY
  - 3: USER RELEASE ONLY
- Description: If results received via this auto instrument entry can be associated with an external auto or user verification system then enable this field.

> This field will be checked in conjunction with the Auto Release master switch parameter LA7UI AUTO RELEASE MASTER and the specific HL7 message containing the results to determine if the lab results should be processed by the Laboratory Auto Release process.

> ![](laboratory-auto-verification-auto-release-user-guide/008.png)

> It can be configured at several levels of granularity:

- 0 - no auto release for this auto instrument
- 1 - yes instrument is enabled for *<u>both</u>* auto and user verification
- 2 - yes however, only release results that have been *auto verified*
- 3 – yes however, only release results that have been *user verified, no auto verification*.

<table>
<caption>Lab Universal Interface SetupLab Universal Interface Setup</caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Lab Universal Interface Menu Option: <strong>UIS</strong> Lab Universal Interface Setup</p>
<p>Lab Universal Interface Setup</p>
<p>Select one of the following:</p>
<p>1 LA7 MESSAGE PARAMETER (#62.48)</p>
<p><strong>2 AUTO INSTRUMENT (#62.4)</strong></p>
<p>3 Auto Release System Parameter</p>
<p>4 Configuration Report (132 COL)</p>
<p>5 Holders of Lab keys</p>
<p>6 Ordering Provider Contact Parameter</p>
<p>7 Convert LAB UI 1.6 to Enhanced Acknowledgement Mode</p>
<p>Select which function to configure/report: <strong>2</strong> AUTO INSTRUMENT (#62.4)</p>
<p>Select AUTO INSTRUMENT NAME: <strong>ARCH</strong></p>
<p>1 ARCH1</p>
<p>2 ARCH2</p>
<p>3 ARCHC</p>
<p>4 ARCH-i1000 I1000</p>
<p>5 ARCHI C-ARCHI</p>
<p>CHOOSE 1-5: <strong>1</strong> ARCH1</p>
<p>NAME: ARCH1//</p>
<p>LOAD/WORK LIST: ARCH//</p>
<p>ENTRY for LAGEN ROUTINE: Accession cross-reference</p>
<p>//</p>
<p>CROSS LINKED BY: ID//</p>
<p>MESSAGE CONFIGURATION: LA7UI9//</p>
<p>METHOD: ARCH1//</p>
<p>DEFAULT ACCESSION AREA: CHEMISTRY//</p>
<p>OVERLAY DATA: YES//</p>
<p>STORE REMARKS: YES//</p>
<p>VENDOR CARD ADDRESS:</p>
<p>SEND TRAY/CUP LOCATION:</p>
<p>AUTO DOWNLOAD:</p>
<p>AUTO RELEASE: YES// <strong>??</strong></p>
<blockquote>
<p>If results received via this auto instrument entry can be associated with an external auto or user verification system then enable this field.</p>
<p>This field will be checked in conjunction with the auto release master switch parameter LA7UI AUTO RELEASE MASTER and the specific HL7 message containing the results to determine if the lab results should be processed by the Laboratory Auto Release process.</p>
<p>It can be configured at several levels of granularity.</p>
<p>0 - no auto release for this auto instrument</p>
<p>1 - yes instrument is enabled for auto and user verification</p>
<p>2 - yes however only process results that have been auto verified</p>
<p>3 - yes however only process results that have been user verified, no auto verification.</p>
<p>Choose from:</p>
<p>0 NO</p>
<p>1 YES</p>
<p>2 AUTO VERIFY ONLY</p>
<p>3 USER RELEASE ONLY</p>
</blockquote>
<p>Select TEST: <strong>GLUCOSE</strong></p>
<p>TEST: GLUCOSE//</p>
<p>UI TEST CODE: GLU//</p>
<p>DOWNLOAD TO INSTRUMENT: YES//</p>
<p>ACCESSION AREA: CHEMISTRY//</p>
<p>SPECIMEN: PLASMA//</p>
<p>URGENCY:</p>
<p>NUMBER OF DECIMAL PLACES: 0//</p>
<p>CONVERT RESULT TO REMARK:</p>
<p>ACCEPT RESULTS FOR THIS TEST: YES//</p>
<p>IGNORE RESULTS NOT ORDERED:</p>
<p>REMOVE SPACES FROM RESULT:</p>
<p>STORE REMARKS: YES//</p>
<p>REMARK PREFIX:</p>
<p>Select TEST:</p>
<p>Select SITE NOTES DATE: NOV 15,2015//</p>
<p>SITE NOTES DATE: NOV 15,2015//</p>
<p>TEXT:</p>
<p>SET AI FOR AUTO-RELEASE-LTW</p>
<p>Edit? NO//</p>
<p>Setting fields for auto download FILE BUILD ENTRY (#93) to: EN</p>
<p>FILE BUILD ROUTINE (#94) to: LA7UID ...Done</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Lab Universal Interface SetupLab Universal Interface Setup

3.  Create Load/List profile for Auto Release

> Use option Edit the default parameters Load/Work list \[LRLLE DFT\] to configure the load/work list. Auto Release can use an existing load/work list or can create a new one. This load list should be associated with the corresponding auto instrument file (#62.4) entry.

1.  The Default Reference Laboratory (#2.3) should be set to the Institution that should be used as the performing and releasing lab for results released via the Auto Release process.

> ![](laboratory-auto-verification-auto-release-user-guide/009.png) Failure to do so will cause all results to generate a user division error in VistA

2.  The Auto Release field (#2.4) in the Load/Work List file (#68.2) is used to mark a profile as being used by the Auto Release process.

> ![](laboratory-auto-verification-auto-release-user-guide/010.png) There should only be one profile flagged per load list.

> Data Type: AUTO RELEASE (or any data type)

1.  0: NO
2.  1: YES

> Description: If an auto release process to accept and file laboratory results from an external system using auto verification and/or human verification is being used then this field indicates to the auto release process which profile on this load list to use to process the lab results.

![](laboratory-auto-verification-auto-release-user-guide/011.png) There should only be one profile flagged per load list.

<table>
<caption>Load/List profile for Auto ReleaseLoad/List profile for Auto Release</caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select OPTION NAME: <strong>LRLLE DFT</strong> Edit the default parameters Load/Work list.</p>
<p>Edit the default parameters Load/Work list.</p>
<p>Select LOAD/WORK LIST NAME: <strong>AUTO RELEASE</strong></p>
<p>LOAD TRANSFORM: UNIVERSAL//</p>
<p>TYPE: SEQUENCE/BATCH//</p>
<p>CUPS PER TRAY: 0//</p>
<p>FULL TRAY'S ONLY: NO//</p>
<p>EXPAND PANELS ON PRINT: YES//</p>
<p>INITIAL SETUP:</p>
<p>VERIFY BY: ACCESSION//</p>
<p>SUPPRESS SEQUENCE #: NO//</p>
<p>INCLUDE UNCOLLECTED ACCESSIONS: NO//</p>
<p>SHORT TEST LIST: NO//</p>
<p>WKLD METHOD: AUTO//</p>
<p>Select PROFILE: AUTO RELEASE CHEMISTRY</p>
<p>ACCESSION AREA: CHEMISTRY//</p>
<p>UID VERIFICATION: ANY ACCESSION AREA//</p>
<p>STORE DUPLICATE COMMENTS: YES//</p>
<p>DEFAULT REFERENCE LABORATORY: ZZ ALBANY//</p>
<p>AUTO RELEASE: YES//</p>
<p>Select PROFILE:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Load/List profile for Auto ReleaseLoad/List profile for Auto Release

4.  Run Configuration Report to check the Auto Release configuration and to assist in configuring the middleware.

Select Lab Universal Interface Menu Option: Lab Universal Interface Setup

Select one of the following:

1 LA7 MESSAGE PARAMETER (#62.48)

2 AUTO INSTRUMENT (#62.4)

3 Auto Release System Parameter

4 Configuration Report (132 COL)

5 Holders of Lab keys

6 Ordering Provider Contact Parameter

7 Convert LAB UI 1.6 to Enhanced Acknowledgement Mode

Select which file to setup: 4 Configuration Report (132 COL)

Select AUTO INSTRUMENT NAME: ASTRA

DEVICE: HOME// 0;132;9999

Lab Universal Interface Configuration Report Page:1

for interface: ASTRA Printed: Jun 21, 2016@15:05:20

========================================================================================

VistA Lab Auto Release Master: YES (ENABLED)

VistA Application Proxy ID/DUZ HL7 encoding format

--------------------------------------------------------------------------------------

LRLAB, AUTO VERIFY 101099 101099-VA500^LRLAB^AUTO^VERIFY^^^^99VA4

LRLAB, AUTO RELEASE 101098 101098-VA500^LRLAB^AUTO^RELEASE^^^^99VA4

HL7 Components: \<ID Number (ST)\> ^ \<Family Name (FN)\> ^ \<Given Name (ST)\> ^ ^ ^ ^ ^ \<Source Table (IS)\> ^

Instrument Auto Download Status.: YES

Instrument Auto Download Routine: EN^LA7UID

Instrument Auto Release Status: YES

Associated Lab UI Message Configuration: LA7UI4

Associated Load/Work List: AUTO RELEASE

Auto Release Profile: AUTO RELEASE

Performing Lab: ZZ ALBANY

ORDERABLE TESTS

Entry Name UI Test Code Accession Area Data Name \[IEN\]

---------------------------------------------------------------------------------

\[1\] SODIUM 01A SODIUM \[5\]

\[2\] POTASSIUM 02A POTASSIUM \[6\]

\[3\] CO2 03A CO2 \[8\]

\[4\] CREATININE 04A CREATININE \[4\]

\[5\] CHLORIDE 05A CHLORIDE \[7\]

\[6\] UREA NITROGEN 06A UREA NITROGEN \[3\]

\[7\] GLUCOSE 07A GLUCOSE \[2\]

\[8\] PROTEIN,TOTAL 08A PROTEIN,TOTAL \[13\]

\[9\] ALBUMIN 09A ALBUMIN \[14\]

\[10\] CALCIUM 10A CALCIUM \[9\]

\[11\] AMYLASE 11A AMYLASE \[40\]

\[12\] TOT. BILIRUBIN 12A BILIRUBIN,TOTAL \[15\]

\[13\] DIR. BILIRUBIN 13A BILIRUBIN,DIRECT \[16\]

\[14\] URIC ACID 14A URIC ACID \[11\]

\[15\] TRIGLYCERIDE 15A TRIGLYCERIDE \[47\]

\[16\] PO4 16A PO4 \[10\]

\[17\] CHOLESTEROL 17A CHOLESTEROL \[12\]

\[18\] SGOT 18A SGOT \[19\]

\[19\] SGPT 19A SGPT \[20\]

\[20\] CPK 20A CPK \[41\]

\[21\] PROTEIN,TOTAL 21A PROTEIN,TOTAL \[13\]

\[22\] LDH 22A LDH \[18\]

\[23\] ALKALINE PHOSPHATASE 23A ALKALINE PHOSPHATASE \[17\]

\[24\] GAMMA-GTP 24A GAMMA-GTP \[21\]

REPORTABLE TESTS Decimal Result to Accept Ignore Remove Store

Entry Name UI Test Code Places Remark Results Results Spaces Remarks

\[1\] SODIUM 01A

\[2\] POTASSIUM 02A

\[3\] CO2 03A

\[4\] CREATININE 04A

\[5\] CHLORIDE 05A

\[6\] UREA NITROGEN 06A

\[7\] GLUCOSE 07A

\[8\] PROTEIN,TOTAL 08A

\[9\] ALBUMIN 09A

\[10\] CALCIUM 10A

\[11\] AMYLASE 11A

\[12\] TOT. BILIRUBIN 12A

\[13\] DIR. BILIRUBIN 13A

\[14\] URIC ACID 14A

\[15\] TRIGLYCERIDE 15A

\[16\] PO4 16A

\[17\] CHOLESTEROL 17A

\[18\] SGOT 18A

\[19\] SGPT 19A

\[20\] CPK 20A

\[21\] PROTEIN,TOTAL 21A

\[22\] LDH 22A

\[23\] ALKALINE PHOSPHATASE 23A

\[24\] GAMMA-GTP 24A

5.  To assist in adding lab users to the middleware system, the following option can be used to print out a list of users that hold a certain lab security key. Make sure users who will be verifying results on the external system hold the LRVERIFY key on VistA.

> ![](laboratory-auto-verification-auto-release-user-guide/012.png) For multi-division sites: All users in the division will populate the report, not just facility.

Select Lab Universal Interface Menu Option: Lab Universal Interface Setup

Select one of the following:

1 LA7 MESSAGE PARAMETER (#62.48)

2 AUTO INSTRUMENT (#62.4)

3 Auto Release System Parameter

4 Configuration Report (132 COL)

5 Holders of Lab keys

6 Ordering Provider Contact Parameter

7 Convert LAB UI 1.6 to Enhanced Acknowledgement Mode

Select which file to setup: 5 Holders of Lab keys

Select LAB SECURITY KEY NAME: LRLAB

Select Another LAB SECURITY KEY NAME: LRVERIFY

Select Another LAB SECURITY KEY NAME:

All USERS? Yes// YES

DEVICE: HOME// 0;80;99999 VIRTUAL TELNET

Jun 21, 2016@15:11 Page: 1

HOLDERS OF LAB KEYS

DUZ/ID NAME LRLAB LRVERIFY

-------------------------------------------------------------------------------

101097 LRUSER,DRI X

235 LRUSER,ONE X X

101053 LRUSER,TWO X X

6.  When VistA Lab sends a Lab HL7 Order message to the middleware, it will send the ordering provider’s contact info in the HL7 message. To override the default settings, and customize at a system or user level which contact info is sent, the following Lab Universal Interface Setup option can be used.

Select Lab Universal Interface Menu Option: Lab Universal Interface Setup

Select one of the following:

1 LA7 MESSAGE PARAMETER (#62.48)

2 AUTO INSTRUMENT (#62.4)

3 Auto Release System Parameter

4 Configuration Report (132 COL)

5 Holders of Lab keys

6 Ordering Provider Contact Parameter

7 Convert LAB UI 1.6 to Enhanced Acknowledgement Mode

Select which file to setup: 6 Ordering Provider Contact Parameter

Lab Ordering Provider Contact Info may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 System SYS \[xxx.xxx.xxx.xx.xxx\]

3 Package PKG \[AUTOMATED LAB INSTRUMENTS\]

Enter selection: 2 System xxx.xxx.xxx.xx.xxx

Setting Lab Ordering Provider Contact Info for System: xxx.xxx.xxx.xx.xxx

Select Sequence: ??

Contains the list of which contact info for the ordering provider to send

in a Lab HL7 Order message from the user's corresponding entry in NEW

PERSON file (#200).

It can be specified at the system or the individual user level. If

specified at the user level it takes precedence and overrides the setting

at the system level allowing specific users to have their own specific set

of contacts to send.

The sequence specifies the order and info to check, maximum of 6 allowed.

Only the first 2 with a value will be placed in the message as the HL7

standard constrains the number of repetitions for this information at 2.

The value specifies which field from the person's entry in NEW PERSON

file (#200) to send in the message.

These are the fields currently available.

Field \# Field Name Description

.131 PHONE (HOME) This is the telephone number for the new

person.

.132 OFFICE PHONE This is the business/office telephone for the

new person.

.133 PHONE \#3 This is an alternate telephone number where the

new person might also be reached.

.134 PHONE \#4 This is another alternate telephone number

where the new person might also be reached.

.135 COMMERCIAL PHONE This is a commercial phone number.

.136 FAX NUMBER This field holds a phone number for a FAX

machine for this user. It needs to be a format

that can be understood by a sending MODEM.

.137 VOICE PAGER This field holds a phone number for an ANALOG

PAGER that this person carries with them.

.138 DIGITAL PAGER This field holds a phone number for a DIGITAL

PAGER that this person carries with them.

![](laboratory-auto-verification-auto-release-user-guide/013.png)The parameter is distributed pre-configured at the package level as

follows:

Sequence Value

-------- -----

1 OFFICE PHONE

2 DIGITAL PAGER

3 VOICE PAGER

4 PHONE \#3

5 PHONE \#4

6 PHONE (HOME)

7 COMMERICAL PHONE

8 FAX NUMBER

Select Sequence:

7.  ![](laboratory-auto-verification-auto-release-user-guide/014.png)Once the GIM has been updated to implement enhanced acknowledgement mode (check with your vendor for the correct enhanced acknowledgement version), the following option is used to enable enhanced acknowledgement mode for LAB UI 1.6.

![](laboratory-auto-verification-auto-release-user-guide/015.png)![](laboratory-auto-verification-auto-release-user-guide/016.png)

Select Lab Universal Interface Menu \<TEST ACCOUNT\> Option: Lab Universal Interface Setup

Select one of the following:

1 LA7 MESSAGE PARAMETER (#62.48)

2 AUTO INSTRUMENT (#62.4)

3 Auto Release System Parameter

4 Configuration Report (132 COL)

5 Holders of Lab keys

6 Ordering Provider Contact Parameter

7 Convert LAB UI 1.6 to Enhanced Acknowledgement Mode

Select which function to configure/report: 7 Convert LAB UI 1.6 to Enhanced Acknowledgement Mode

Has the Lab UI COTS driver been upgraded to send HL7 v2.5.1 messages? No// ?

Enter either 'Y' or 'N'.

This normally involves a driver update on the COTS system

to allow the COTS system to send HL7 messages indicating

either HL7 v2.2 or v2.5.1. Contact your Laboratory Information

Manager to confirm the status of the driver update.

Has the Lab UI COTS driver been upgraded to send HL7 v2.5.1 messages? No// YES

Implement enhanced acknowledgement mode transmission? No// ?

Enter either 'Y' or 'N'.

Implement enhanced acknowledgement mode transmission? No// YES

Starting checking and updating related Lab UI protocols in file \#101

Protocol LA7UI ORM-O01 EVENT already updated to HL7 version 2.5.1

Protocol LA7UI ORM-O01 EVENT updated to HL7 Enhanced Mode Acknowledgments.

Protocol LA7UI ORM-O01 SUBS already updated to HL7 version 2.5.1

.

Protocol LA7UI9 ORU-R01 EVENT already updated to HL7 version 2.5.1

Protocol LA7UI9 ORU-R01 EVENT updated to HL7 Enhanced Mode Acknowledgments.

Finished checking and updating related Lab UI protocols in file \#101

8.  Local site personnel should assign DIVISIONS to the new proxy users, LRLAB, AUTO RELEASE and LRLAB, AUTO VERIFY that corresponds to the performing laboratories that will utilize the Auto Release process.

The LRLAB, AUTO RELEASE and LRLAB, AUTO VERIFY user records are automatically created in VistA File \#200 NEW PERSON FILE.

1.  LRLAB, AUTO RELEASE is used to reflect results released within VistA Lab that were verified by an auto verification process (LRLAB, AUTO VERIFY) or released/approved by a human on an external system (DI or other COTS/external lab).
2.  LRLAB, AUTO VERIFY – used to indicate that the results were approved by an automated process using a rules-based system.
9.  New option was added to the Supervisor reports \[LRSUPER REPORTS\] menu.

> Summary List (Patient) \[LRLISTPS\]  
> Description: All results for a given patient for a given area for a given date. This report can serve as an 'audit trail' for a patient. Includes information on person placing order, person performing test, verifying person, and dates and times of specimen collection and test completion. The report can be printed in an "extended" form, which includes the above mentioned information plus the test results and associated units/normals/LOINC coding and performing lab.

### Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 5 depicts graphically the overall flow of data in the system.

Figure 5: Data Flow Diagram

![](laboratory-auto-verification-auto-release-user-guide/017.png)

### User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two primary user roles for this new capability:

Laboratory Information Manager (LIM) – responsible for initial configuration and ongoing support, including troubleshooting of Application Errors.

Medical Technologists authorized to verify results external to VistA on the COTS package – these users will need to have the LRVERIFY key and an active VistA account and have appropriate security settings in the COTS GIM system.

### Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No changes, continuity of operations in the case of an emergency or disaster for the laboratory universal interface and modules on VistA continue as per current policy and procedures.

## Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Logging On

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No changes, VistA log-on continues as per current operations.

### System Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Modifications to the AUTO INSTRUMENT (#62.4) option.

Select Lab Universal Interface Menu \<TEST ACCOUNT\> Option: Lab Universal Interface Setup

Select one of the following:

LA7 MESSAGE PARAMETER (#62.48)

AUTO INSTRUMENT (#62.4)

Auto Release System Parameter

Configuration Report (132 COL)

Holders of Lab keys

Ordering Provider Contact Parameter

Convert LAB UI 1.6 to Enhanced Acknowledgement Mode

#### New Auto Release System Parameter Option

Select Lab Universal Interface Menu \<TEST ACCOUNT\> Option: Lab Universal Interface Setup

Select one of the following:

LA7 MESSAGE PARAMETER (#62.48)

AUTO INSTRUMENT (#62.4)

Auto Release System Parameter

Configuration Report (132 COL)

Holders of Lab keys

Ordering Provider Contact Parameter

Convert LAB UI 1.6 to Enhanced Acknowledgement Mode

#### New Summary List (Patient) Report Option

Select Supervisor reports Option: sum

Summary list (extended supervisors')

Summary List (Patient)

Summary list (supervisors')

CHOOSE 1-3: 2 Summary List (Patient)

### Changing User ID and Password

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No changes, VistA password resets continue as per current operations.

### Exit System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No changes, VistA log-offs continue as per current operations.

### Caveats and Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please review the Troubleshooting section of this guide to learn about how to triage and act upon interface application errors.

## Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Auto Verified Results from External System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When results are Auto Verified on an external system such as DI’s Instrument Manager, then when the results are received and stored on VistA, proxy users are entered in the “VERIFY PERSON” and “PERFORMED/RELEASED BY” fields. An example is shown below using the Summary List (Patient) Report on the Supervisor Reports menu off of the Lab Menu.

<table>
<caption>Example of Autoverified Result with Proxy UsersExample of Autoverified Result with Proxy Users</caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>EXAMPLE OF AUTO VERIFIED RESULT with PROXY USERS</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select Supervisor reports Option: summ</p>
<p> 1 Summary list (extended supervisors')</p>
<p> 2 Summary List (Patient)</p>
<p> 3 Summary list (supervisors')</p>
<p>CHOOSE 1-3: 2 Summary List (Patient)</p>
<p>Select Patient Name: ####nnnnn ZZDUCK,ZBYEV MMM 9-30-48 ####nnnnn</p>
<p> NO NON-VETERAN (OTHER)</p>
<p>WARNING : You may have selected a test patient.</p>
<p>WARNING :  This patient has been flagged with a Bad Address Indicator.</p>
<p>Enrollment Priority: Category: NOT ENROLLED End Date: 03/28/2005</p>
<p>Enrollment Status: NOT ELIGIBLE; INELIGIBLE DATE</p>
<p>Select LR SUBSCRIPT: CH// EM, HEM, TOX, RIA, SER, etc.</p>
<p>Enter START date: TODAY//T (MAY 18, 2016)</p>
<p>Enter END date: T-1//T (MAY 18, 2016)</p>
<p>Display an Extended Listing? YES//</p>
<p>Display associated global? NO//</p>
<p>DEVICE: HOME// Linux Telnet/SSH</p>
<p>Patient Summary Report WORK COPY ONLY - DO NOT FILE Printed: May 18, 2016</p>
<p>ZZDUCK,DAISY SUE ####nnnnn Sex: F</p>
<p> For date range: May 18, 2016 to May 18, 2016@24:00 for CHEM, HEM, TOX, RIA, SE</p>
<p>R, etc.</p>
<p>DATE/TIME SPECIMEN TAKEN: MAY 18, 2016@07:27:23</p>
<p> DATE REPORT COMPLETED: MAY 18, 2016@07:37:28</p>
<p> VERIFY PERSON: LRLAB,AUTO RELEASE SPECIMEN TYPE: PLASMA</p>
<p> ACCESSION: COAG 0518 18 METHOD OR SITE: ACLTOP(AR)</p>
<p> REQUESTING PERSON: MATHUR,SHARAD C REQUESTING LOCATION: LAB</p>
<p> REQUESTING LOC/DIV: KC-PATHOLOGY LABORATORY</p>
<p> ACCESSIONING INSTITUTION: VA HEARTLAND - WEST, VISN 15</p>
<p> INR EK: 3.0 ( INR) PERFORMED/RELEASED BY: Lrlab,Auto Verify</p>
<p> PERFORMED/RELEASED ON: May 18, 2016@07:37:28</p>
<p> PERFORMING LAB: VA HEARTLAND - WEST, VISN 15</p>
<p> LOINC Code: 6301-6 EII: ACPTOP1;LRAV</p>
<p> PT(10/01): 32.2 H (9.6-12.5 Sec) PERFORMED/RELEASED BY: Lrlab,Auto Verify</p>
<p> PERFORMED/RELEASED ON: May 18, 2016@07:37:28</p>
<p> PERFORMING LAB: VA HEARTLAND - WEST, VISN 15</p>
<p> LOINC Code: 5902-2 EII: ACPTOP1;LRAV</p>
<p> APTT ACL: 63.5 H (25.8-36.6 Sec) PERFORMED/RELEASED BY: Lrlab,Auto Verify</p>
<p> PERFORMED/RELEASED ON: May 18, 2016@07:37:28</p>
<p> PERFORMING LAB: VA HEARTLAND - WEST, VISN 15</p>
<p>LOINC Code: 14979-9 EII: ACPTOP1;LRAV</p></td>
</tr>
</tbody>
</table>

Example of Autoverified Result with Proxy UsersExample of Autoverified Result with Proxy Users

### Tech Verified Result from External System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a user with appropriate authority including an active VistA account and holder of the LRVERIFY key manually verifies a result outside of VistA (for example on the GIM), then when the results are sent back to VistA via the Laboratory Universal Interface, this user will be recorded as the ‘PERFORMED/RELEASED BY’ tech. To view this information please use the Summary List (Patient) Report on the Supervisor Reports menu off of the Lab Menu. The screen capture below shows an example of how the report will look.

<table>
<caption>Example of Externally Verified Result and AutoReleased on VistA with Proxy UserExample of Externally Verified Result and AutoReleased on VistA with Proxy User</caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>EXAMPLE OF Externally VERIFIED RESULT and AUTO RELEASED on VistA with PROXY USER</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select Process data in lab menu &lt;TEST ACCOUNT&gt; Option: ^SUPERVISOR REPorts</p>
<p>Select Supervisor reports &lt;TEST ACCOUNT&gt; Option: SUMM</p>
<p> 1 Summary list (extended supervisors')</p>
<p> 2 Summary List (Patient)</p>
<p> 3 Summary list (supervisors')</p>
<p>CHOOSE 1-3: 2 Summary List (Patient)</p>
<p>Select Patient Name: ####nnnnn BLUSAHN,AAXNI THKULY 10-21-75 ####nnnnn</p>
<p>6 YES SC VETERAN</p>
<p> Enrollment Priority: GROUP 1 Category: ENROLLED End Date:</p>
<p> Combat Vet Status: EXPIRED End Date: 05/18/2009</p>
<p>Select LR SUBSCRIPT: CH// EM, HEM, TOX, RIA, SER, etc.</p>
<p>Enter START date: TODAY//0517 (MAY 17, 2016)</p>
<p>Enter END date: T-1// (MAY 26, 2016)</p>
<p>Display an Extended Listing? YES//</p>
<p>Display associated global? NO//</p>
<p>DEVICE: HOME// Linux Telnet/SSH</p>
<p>Patient Summary Report WORK COPY ONLY - DO NOT FILE Printed: May 27, 2016</p>
<p>BLUSAHN,AAXNI THKULY ####nnnnn Sex: M</p>
<p> For date range: May 17, 2016 to May 26, 2016@24:00 for CHEM, HEM, TOX, RIA, SE</p>
<p>R, etc.</p>
<p>DATE/TIME SPECIMEN TAKEN: MAY 17, 2016@08:54:51</p>
<p> DATE REPORT COMPLETED: MAY 18, 2016@09:27:06</p>
<p> VERIFY PERSON: LRLAB,AUTO RELEASE SPECIMEN TYPE: PLASMA</p>
<p> ACCESSION: CH 0517 88 METHOD OR SITE: ARCH1(AR)</p>
<p> REQUESTING PERSON: MATHUR,SHARAD C REQUESTING LOCATION: LAB</p>
<p> REQUESTING LOC/DIV: KC-PATHOLOGY LABORATORY</p>
<p> ACCESSIONING INSTITUTION: VA HEARTLAND - WEST, VISN 15</p>
<p> SODIUM: 137 (136-145 mEq/L) PERFORMED/RELEASED BY: <mark>REDACTED</mark></p>
<p> PERFORMED/RELEASED ON: May 17, 2016@09:28:17</p>
<p> PERFORMING LAB: VA HEARTLAND - WEST, VISN 15</p>
<p> LOINC Code: 2951-2</p>
<p> POTASSIUM: 4.1 ( ) PERFORMED/RELEASED BY: <mark>REDACTED</mark></p>
<p> PERFORMED/RELEASED ON: May 18, 2016@09:27:03</p>
<p> PERFORMING LAB: VA HEARTLAND - WEST, VISN 15</p>
<p> LOINC Code: 2823-3 EII: VISTA IN-ORDERS;LRTV</p>
<p> CL: 108 ( ) PERFORMED/RELEASED BY: <mark>REDACTED</mark></p>
<p>Enter RETURN to continue or '^' to exit:</p>
<p> PERFORMED/RELEASED ON: May 18, 2016@09:27:03</p>
<p> PERFORMING LAB: VA HEARTLAND - WEST, VISN 15</p>
<p> LOINC Code: 2075-0 EII: VISTA IN-ORDERS;LRTV</p>
<p> CARBONDI: 25 ( ) PERFORMED/RELEASED BY: <mark>REDACTED</mark></p>
<p> PERFORMED/RELEASED ON: May 18, 2016@09:27:03</p>
<p> PERFORMING LAB: VA HEARTLAND - WEST, VISN 15</p>
<p> LOINC Code: 2028-9 EII: VISTA IN-ORDERS;LRTV</p>
<p> UID: 2361380088</p>
<p>ORDERED TEST: Electrolytes ORDERED URGENCY: ROUTINE</p>
<p> CPRS ORDER #: 105362623 LAB ORDER #: LR-430-316138</p>
<p> ORDER TYPE: Lab Collect ORDERING PROVIDER LOCAL: MATHUR,SHARAD C</p>
<p> SPECIMEN TOPOGRAPHY: PLASMA COLLECTION SAMPLE: GREEN TOP TUBE</p>
<p> LAB TEST ORDERED: ELECTROLYTES</p>
<p> RELEASING SITE: VA HEARTLAND - WEST, VISN 15</p>
<p>Enter RETURN to continue or '^' to exit:</p></td>
</tr>
</tbody>
</table>

Example of Externally Verified Result and AutoReleased on VistA with Proxy UserExample of Externally Verified Result and AutoReleased on VistA with Proxy User

## Post Release Patches, LR\*5.2\*475 and LR\*5.2\*94

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LR\*5.2\*475 adds functionality to store Lab Test (#60) configuration data which doesn’t come from the middleware for verified results.

This will allow the user to edit previously auto-released results using the normal VistA lab EM/EA options utilizing the values used at the time of original verification.

LR\*5.2\*94 corrects an issue with the “Holders of Lab Keys” report, where the report would seem to queue up when user requested a printed report, but the report would not print. The report could be displayed on screen.

## Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA software enhancement for Lab Auto Release 1.0 includes enhanced interface messaging support between GIM and the VistA Laboratory Universal Interface. VistA will send an application acknowledgement (ACK) to IM when a Health Level 7 (HL7) message errors when VistA Laboratory is trying to process and save the data. This error will show on the IM Status page. The enhanced acknowledgement Support can be activated on the vadhl7hl 8.00.0017driver.

### Order Message Acknowledgements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the option for enhanced acknowledgement support is unchecked, then the GIM will send an Application Acknowledgment (ORR) in response to an order message (ORM) and will not send any values in MSH.15 or MSH.16.

If the option for enhanced acknowledgement support is enabled then the GIM will send a Commit Acknowledgment (ACK) on the inbound connection in response to an order (ORM) followed by an Application Acknowledgment (ORR) on the outbound connection.

### Result Acknowledgements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](laboratory-auto-verification-auto-release-user-guide/018.png) For results, the GIM will populate MSH.15 and MSH.16 to indicate the Commit Acknowledgment and the Application Acknowledgement conditions.

Upon receipt of a result message (ORU), the VistA HL package responds with a commit acknowledgment (ACK) based on the value specified in MSH.15. The VistA Laboratory system responds with an application acknowledgment (ACK) message based on the condition specified by MSH.16 of the result (ORU) message. The application ACK message consists of the following segments.

> <u>ACK General Acknowledgment Message</u>

> MSH Message Header

> MSA Message Acknowledgment

> ERR Error

> When triaging an Application Acknowledgment please refer to the following message structure information below for where to identify data related to errors.

> MSA-2 Message Control ID will contain the message control ID of the ORU message being acknowledged.

> MSA-3 Text Message will contain either of the following:

> • If MSA-1 Acknowledgment Code is AA then MSA-3 will be blank.

> • If MSA-1 Acknowledgment Code is AE then MSA-3 will contain an error message.

> ERR-3 HL7 Error Code

- If MSA-1 Acknowledgment Code is AA then ERR-3 will contain value 0 from HL7 Table 0357.
- If MSA-1 Acknowledgment Code is AE then ERR-3 will contain an error code/message from HL7 Table 0357.

> ERR-4 Severity

- If MSA-1 Acknowledgment Code is AA then ERR-4 will be blank.
- If MSA-1 Acknowledgment Code is AE then ERR-4 will contain an error code/message from HL7 Table 0357

ERR-5 Application Error Code

- If MSA-1 Acknowledgment Code is AA then ERR-5 will be blank.
- If MSA-1 Acknowledgment Code is AE then ERR-4 will contain an error code/message from VistA Laboratory LA7 MESSAGE LOG BULLETINS FILE (#62.485) (see troubleshooting table below)

ERR-8 User Message

- If MSA-1 Acknowledgment Code is AA then ERR-8 will be blank.
- If MSA-1 Acknowledgment Code is AE then ERR-8 will contain text message from ERR-5.

ERR-9 Inform Person Indicator

• If MSA-1 Acknowledgment Code is AA then ERR-9 will be blank.

• If MSA-1 Acknowledgment Code is AE then ERR-9 will contain”USR”.

> EXAMPLE:

> Message with an AA application accept

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>MSH|^~\&amp;|LA7LAB|500|LA7UI1|500|20160108183946-0500||ACK^R01|500396|T|2.5.1|||AL|NE|USA</p>
<p>MSA|AA|64014,61262</p>
<p>ERR|||0^Message accepted^HL70357|I"</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Message with an AE application error

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>MSH|^~\&amp;|LA7LAB|500|LA7UI1|500|20160108183946-0500||ACK^R01|500399|T|2.5.1|||AL|NE|USA</p>
<p>MSA|AE|63886,49648|Msg #30, Auto Release not allowed for accession UID CH53230012</p>
<p>ERR|||207^Application internal error^HL70357|E|307^Msg #30, Auto Release not allowed for accession UID CH53230012. Results have previously been released.^99VA62.485|||Msg #30, Auto Release not allowed for accession UID CH53230012. Results have previously been released.|USR</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Troubleshooting VistA Generated Application Error Codes 

The following table provides troubleshooting information on VistA Generated Application Error Codes sent to Data Innovations (DI) when it fails to process/save the information on the received Result Messages. Error information is found in the 5<sup>th</sup> sequence of the ERR segment in the HL7 message ACK. All possible errors in this sequence may be found in LA7 MESSAGE LOG BULLETINS FILE (#62.485).

![](laboratory-auto-verification-auto-release-user-guide/019.png) For additional Error Codes, see File 62.485

Table7: Troubleshooting VistA Generated Application Error Codes

<table>
<caption>Troubleshooting Information TableTroubleshooting Information Table</caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 17%" />
<col style="width: 20%" />
<col style="width: 31%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th>Code</th>
<th>Text</th>
<th>Scenario</th>
<th>Fix</th>
<th>Test Scenario</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>301</td>
<td>301 Msg #|1|, User |2| [DUZ: |3|] does not own the LRVERIFY security key. Auto Release not allowed for accession UID |4|.</td>
<td>User verifies a result on GIM but does not hold the LRVERIFY key on VistA.</td>
<td><ol type="1">
<li><p>Follow facility policy for requesting security key, if assigned in a timely manner, resend result from GIM</p></li>
</ol>
<p>OR</p>
<ol start="2" type="1">
<li><p>Have a tech with the proper VistA key, verify the result and resend to VistA</p></li>
<li><p> Verify transmitted results using normal VistA Lab Enter/verify data (auto instrument) option [LRVR].</p></li>
</ol></td>
<td>Testing Scenario-1 A user will be configured in IM Security setting that does not hold the LRVERIFY Lab Key. A test will be ordered and run on an instrument. The result should be one that does not pass the rule set and is held in IM Workspace. Log into IM Workspace as the user configured above and release the result. This should cause an error on the Vista side since the user does not hold the LRVERIFY Lab Key. VistA should send an ACK ERR message back to GIM which should appear on the Status screen.</td>
</tr>
<tr class="even">
<td>302</td>
<td>302 Msg #|1|, User |2| [DUZ: |3|] is not an active user on the system. Auto Release not allowed for accession UID |4|.</td>
<td>A result is released from GIM with a user that does not have an Active VistA User Record/Account</td>
<td><ol type="1">
<li><p>Have results released by a user with an active account on VistA.</p></li>
</ol>
<p>OR</p>
<ol start="2" type="1">
<li><p>Have a tech with an active account on VistA verify the result and resend to VistA</p></li>
</ol></td>
<td>Testing Scenario-2: A user will be configured in IM Security setting that does not exist on VistA. A test will be ordered and run on an instrument. The result should be one that does not pass the rule set and is held in IM Workspace. Log into IM Workspace as the user configured above and release the result. This should cause an error on the Vista side since the user does not exist on VistA. Vista should send an ACK ERR message back to GIM which should appear on the Status screen.</td>
</tr>
<tr class="odd">
<td>303</td>
<td>303 Msg #|1|, No verifying user or application proxy found. Auto Release not allowed for accession UID |2|.</td>
<td>A result is released from GIM without a user or proxy user in the message.</td>
<td><ol type="1">
<li><p>Consult the Install Guide and ensure that the required proxy users and valid VistA users are set up on GIM.</p></li>
<li><p>Alternatively, use LRVERIFY EA in VistA to release manually</p></li>
</ol></td>
<td></td>
</tr>
<tr class="even">
<td>304</td>
<td>304 Msg #|1|, User |2| [DUZ: |3|] is not a valid user to verify results. Auto Release not allowed for accession UID |4|.</td>
<td>A result is released from GIM and indicated the performing user was the application proxy LRLAB, AUTO RELEASE This application proxy is invalid.</td>
<td><ol type="1">
<li><p>Need to transmit the identity of the actual user (VistA DUZ number) or the application proxy LRLAB, AUTO VERIFY. Configured in the COTS driver configuration.</p></li>
<li><p>Alternatively, use LRVERIFY EA in VistA to release manually</p></li>
</ol></td>
<td></td>
</tr>
<tr class="odd">
<td>305</td>
<td>305 Msg #|1|, User |2| [DUZ: |3|] is not allowed to verify. Only auto verification enabled for this instrument. Auto Release not allowed for accession UID |4|.</td>
<td>A result is released from GIM by a tech versus the application proxy LRLAB AUTO VERIFY when VistA is configured to only allow auto verification for the instrument, and the instrument does not allow external tech verification.</td>
<td><ol type="1">
<li><p>Either configure VistA Lab auto instrument entry to allow tech verification or disable tech verification on Generic Instrument Manager (GIM).</p></li>
<li><p>Alternatively, use LRVERIFY EA in VistA to release manually</p></li>
</ol></td>
<td></td>
</tr>
<tr class="even">
<td>306</td>
<td>306 Msg #|1|, User |2| [DUZ: |3|] is not allowed to verify. Only tech verification enabled for this instrument. Auto Release not allowed for accession UID |4|.</td>
<td>A result indicates that it was released by an auto verification process when VistA is configured to only allow tech verification on the GIM.</td>
<td><ol type="1">
<li><p>Either configure VistA Lab auto instrument entry to allow auto verification or disable auto verification on GIM.</p></li>
<li><p>Alternatively, use LRVERIFY EA in VistA to release manually</p></li>
</ol></td>
<td></td>
</tr>
<tr class="odd">
<td>307</td>
<td>307 Msg #|1|, Auto Release not allowed for accession UID |2|. Results have previously been released.</td>
<td><p>A result (data packet) is transmitted from GIM which contains at least one result that has already been resulted or cancelled in VistA</p>
<p>![](laboratory-auto-verification-auto-release-user-guide/020.png) *NOTE* A single “previously verified” or “previously cancelled” result will invalidate Auto Release for ALL results present in a given data packet, regardless of their Auto Verification status or eligibility</p></td>
<td>Compare the result on GIM and VistA, if needed issue an amended report thru VistA.</td>
<td>Testing Scenario-B. A test will be ordered in Vista and run on an instrument. The result should be one that does not pass the rule set and is held in IM Workspace. Once the result is held the tester will go into Vista and using EM result out the test. Once the test is resulted using EM the tester will release the result from IM. This should cause an error on the Vista side since the test will have a status of “Completed” making the result ineligible for processing. Vista should send an ACK ERR message back to Instrument Manager which should appear on the Status screen.</td>
</tr>
<tr class="even">
<td>13</td>
<td>13 Msg #|1|, accession not found in file 68 for area |2| (Auto Instrument Name), date |3|, entry |4|, using LRUID</td>
<td>A result has been released by the GID that does not exist in the corresponding Auto Instrument file</td>
<td>Confirm the UID is correct. This error typically happens with UID numbers that do not correspond to a patient and erroneously passed through the Auto Verification logic. If necessary, modify Auto Verification rules so that only acceptable UID numbers pass through to VISTA.</td>
<td></td>
</tr>
</tbody>
</table>

Troubleshooting Information TableTroubleshooting Information Table

#### Example of Error Messages on Instrument Manager Console

The image below shows a screen shot of the Data Innovations Instrument Manager (IM) console and all Application Errors are shown on the bottom third of this view.

![](laboratory-auto-verification-auto-release-user-guide/021.png)

![](laboratory-auto-verification-auto-release-user-guide/022.png)Check with your vendor for examples of error messages

## Acronyms, Abbreviations, Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|              | Term and/or Definition                                                                                                        |
|--------------|-------------------------------------------------------------------------------------------------------------------------------|
| ACK          | Acknowledgement                                                                                                               |
| Auto Release | Results automatically released from VistA upon receipt from GIM                                                               |
| Auto Verify  | Results verified and released from the GIM that satisfy the set rules and algorithms defined for said test, and sent to VistA |
| DI           | Data Innovations – Corporation that develops the Instrument Interface Manager used with VistA Laboratory Universal Interface  |
| DUZ          | Unique Identifier of a VistA User                                                                                             |
| ERR          | Error Segment in an Health Level 7 (HL7) Interface Transmission                                                               |
| GIM          | Generic Interface Manager                                                                                                     |
| HL7          | Health Level 7 Interface Standard                                                                                             |
| IM           | Instrument Manager, product that manages the interface of orders and results between VistA and Laboratory Analyzers           |
| LIM          | Laboratory Information Manager                                                                                                |
| MSA          | Message Acknowledgment                                                                                                        |
| Msg          | Message                                                                                                                       |
| MSH          | Message Header                                                                                                                |
| OI&T         | Office of Information and Technology                                                                                          |
| UID          | Unique Identifier                                                                                                             |
| UI           | Universal Interface                                                                                                           |
| VA           | Department of Veterans Affairs                                                                                                |
| VistA        | Veterans Health Information Systems and Technology Architecture                                                               |

AcronymsAcronyms