---
title: "LA*5.2*480 Laboratory: Universal Interface Micro Installation Guide"
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: "Laboratory: Universal Interface Micro"
app_code: LA
app_name: "Laboratory: Universal Interface"
section: CLI
app_status: active
pkg_ns: LA
patch_ver: 5.2
patch_id: LA*5.2*480
group_key: "LA:LA:5.2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - installation
  - back
  - rollback
  - procedure
  - patch
  - strong
  - instructions
  - class
page_count: 0
word_count: 2534
section_count: 28
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2017
revision_count: 1
revision_newest: 02/08/2017
revision_oldest: 02/08/2017
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/micro_lr_5_2_480_install_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/micro_lr_5_2_480_install_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=120"
---

VistA Laboratory Enhancements (VLE) –Microbiology

Release: LR\*5.2\*480

Installation, Back-Out, and Rollback Guide

![](la-5-2-480-laboratory-universal-interface-micro-installation-guide/001.png)

February 2017

Document Version 1.0

Office of Information and Technology (OI&T)

Revision History

| Date       | Version | Description         | Author                             |
|------------|---------|---------------------|------------------------------------|
| 02/08/2017 | 1.0     | Document baselined. | <span class="mark">REDACTED</span> |

<span id="_Toc428787969" class="anchor"></span>Table 1: Release for Installation

Artifact Rationale

The Installation, Back-out, Rollback Plan defines the ordered, technical steps required to install the product, and if necessary, to back-out the installation, and to roll back to the previously installed version of the product.

Table of Contents

1\. Introduction [1](#introduction)

1.1. Dependencies [1](#dependencies)

1.2. Constraints [1](#constraints)

1.3. Orientation [1](#orientation)

1.3.1. Computer Dialogue [1](#computer-dialogue)

1.3.2. Instructions [1](#instructions)

1.3.3. User Response [2](#user-response)

1.3.4. Warnings and Annotations [2](#warnings-and-annotations)

2\. System Requirements [2](#system-requirements)

3\. Pre-Installation and Installation Preparation Instructions [2](#pre-installation-and-installation-preparation-instructions)

3.1. Installation Timing Recommendation [2](#installation-timing-recommendation)

3.2. Estimated Timing [2](#estimated-timing)

3.3. Kernel Patches [2](#kernel-patches)

3.4. Global Growth [2](#global-growth)

3.5. Download and Extract Files [3](#download-and-extract-files)

3.6. Database Creation [3](#database-creation)

3.7. Installation Scripts [3](#installation-scripts)

3.8. CRON Scripts [3](#cron-scripts)

3.9. Access Requirements and Skills Needed for the Installation [3](#access-requirements-and-skills-needed-for-the-installation)

4\. Pre-installation and System Requirements for Patch LR\*5.2\*480 [4](#_Toc474246980)

4.1. Installation Procedure for Patch LR\*5.2\*480 [4](#_Toc474246981)

4.2. Installation Verification Procedure [5](#installation-verification-procedure)

5\. Back-Out Procedure [5](#back-out-procedure)

5.1. Back-Out Strategy [5](#back-out-strategy)

5.2. Back-Out Considerations [5](#back-out-considerations)

5.2.1. Load Testing [5](#load-testing)

5.3. Back-Out Criteria [5](#back-out-criteria)

5.4. Back-Out Risks [5](#back-out-risks)

5.5. Authority for Back-Out [5](#authority-for-back-out)

5.6. Back-Out Procedure [6](#back-out-procedure-1)

5.7. Back-out Verification Procedure [6](#back-out-verification-procedure)

6\. Rollback Procedure [6](#rollback-procedure)

6.1. Rollback Considerations [6](#rollback-considerations)

6.2. Rollback Criteria [6](#rollback-criteria)

6.3. Rollback Risks [6](#rollback-risks)

6.4. Authority for Rollback [6](#authority-for-rollback)

6.5. Rollback Procedure [6](#rollback-procedure-1)

6.6. Rollback Verification Procedure [6](#rollback-verification-procedure)

List of Tables

[Table 1: Release for Installation [3](#_Toc428787969)](#_Toc428787969)

[Table 2: M Code Installation Instructions for Patch LR\*5.2\*480 [4](#_Toc474247000)](#_Toc474247000)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Dependencies](#dependencies)
  - [Constraints](#constraints)
  - [Orientation](#orientation)
    - [Computer Dialogue](#computer-dialogue)
    - [Instructions](#instructions)
    - [User Response](#user-response)
    - [Warnings and Annotations](#warnings-and-annotations)
- [System Requirements](#system-requirements)
- [Pre-Installation and Installation Preparation Instructions](#pre-installation-and-installation-preparation-instructions)
  - [Installation Timing Recommendation](#installation-timing-recommendation)
  - [Estimated Timing](#estimated-timing)
  - [Kernel Patches](#kernel-patches)
  - [Global Growth](#global-growth)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [CRON Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
- [Pre-installation and System Requirements for Patch LR\5.2\480](#pre-installation-and-system-requirements-for-patch-lr52480)
  - [Installation Procedure for Patch LR\5.2\480](#installation-procedure-for-patch-lr52480)
  - [Installation Verification Procedure](#installation-verification-procedure)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-Out Procedure](#back-out-procedure-1)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
This document provides installation instructions for release patch LR\*5.2\*480 as managed through the VistA Laboratory Enhancement Microbiology project.
Patch LR\*5.2\*480 addresses an issue related to released patch LR\*5.2\*474, which is part of the Lab Micro Interface Release 1.0 build. In brief, patch LR\*5.2\*480 resolves the issue of a Microbiology accession being erroneously removed from the ‘Incomplete Test Status Report’ (LRWRKINC) option when a ‘Preliminary’ result is released in the Laboratory Universal Interface (UI) package. A symptom of the issue was presented when the released accessions from Laboratory UI were set to a ‘Complete’ status.
The patch modifies the routine LRVR0 at ACCEPT+68.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LR\*5.2\*480 contains the following dependency:

- LR\*5.2\*474

## Constraints 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security controls will be inherited from VistA and therefore will be fully compliant with National Institute of Standards and Technology (NIST) controls and in compliance with Directive 6500. In addition, patch LR\*5.2\*480 will be 508 compliant and designed to ensure no performance impacts will be experienced in the production environments.

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section addresses package or audience specific notations or directions (e.g., symbols used

to indicate terminal dialogues or user responses) for the installation and post-installation instructions included in this document.

All headings and text in this guide are intentionally formatted flush left, regardless of the heading level, to save space and to make for better readability.

In tables which list mandatory steps (for pre-installation and installation), a column is provided at the right-hand side so that users may check () off the step as it is performed.

### Computer Dialogue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The computer dialogue will appear in Courier New 11-point font.

Example: Courier New font 11 points

### Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Instructions will appear in Arial 11-point font.

Example: Arial font 11 points

### User Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User entry responses will appear in Courier New 11-point font.

Example: Courier New font 11 points

### Warnings and Annotations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The verbiage warning and note will appear in Arial 11-point bold font to alert the user about important information that will follow.

Example: Arial bold font 11 points

Warnings of high importance will be denoted with a ![](la-5-2-480-laboratory-universal-interface-micro-installation-guide/002.png) symbol.

# System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](la-5-2-480-laboratory-universal-interface-micro-installation-guide/003.png)

Install LR\*5.2\*474 first (part of the Lab Micro Interface Release 1.0 build), followed by the installation of patch LR\*5.2\*480.

# Pre-Installation and Installation Preparation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the pre-installation and installation preparation instructions for patch LR\*5.2\*480. Specific pre-installation instructions are not required for the patch. The information provided in this section are general preparation instructions and recommendations.

## Installation Timing Recommendation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be loaded with users on the system. If desired, perform the installation during non-peak hours.

## Estimated Timing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation will take less than 5 minutes.

## Kernel Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel patches must be current on the target system to avoid problems loading and/or installing this patch.

## Global Growth

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no significant change to global growth.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of the builds shall be achieved via Packman messages. Associated documentation will be available on the VistA Document Library (VDL). The online versions will be updated as needed. Please look for the latest version on the VDL:

<http://www.va.gov/vdl>

The following table lists the releases that are available for installation.

<table>
<caption><p><span id="_Toc474247000" class="anchor"></span>Table 2: M Code Installation Instructions for Patch LR*5.2*480</p></caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th>Host File</th>
<th>File Name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Packman Distribution</td>
<td><p>Each Packman message contains 1 patch:</p>
<ul>
<li><p>LR*5.2*480</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc474247000" class="anchor"></span>Table 2: M Code Installation Instructions for Patch LR\*5.2\*480

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable as there will not be any databases created.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable as there will not be any installation scripts.

## CRON Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable as there will not be any CRON scripts.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide is written with the assumption that the reader is experienced or familiar with the following:

- VistA computing environment
- VA FileMan data structures and terminology
- Microsoft Windows

Product Support will coordinate the patch installation with the LIM at each site. The LIM and Product Support have the necessary access and skill set to conduct the installation.

# Pre-installation and System Requirements for Patch LR\*5.2\*480

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LR\*5.2\*480 does not require any pre-installation or system requirements.

## Installation Procedure for Patch LR\*5.2\*480

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow the instructions outlined in the table below to perform the installation of Patch LR\*5.2\*480.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 7%" />
<col style="width: 66%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step #</strong></th>
<th colspan="3"><strong>Description</strong></th>
<th><strong></strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>1</strong></td>
<td colspan="3">On the PackMan menu, use the INSTALL/CHECK MESSAGE option. This option loads the patch into a Transport Global on your system.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>2</strong></td>
<td colspan="3">From the Kernel Installation and Distribution System (KIDS) menu, select the Installation menu.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>3</strong></td>
<td colspan="3">From this menu, you may elect to use the following options:</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><strong>a</strong></td>
<td>Verify Checksums in Transport Global: This option will allow you to ensure the integrity of the routines that are in the transport global.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><strong>b</strong></td>
<td>Print Transport Global: This option will allow you to view the components of the KIDS build.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><strong>c</strong></td>
<td>Compare Transport Global to Current System: This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, Data Dictionaries (DD's), templates, etc.).</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><strong>d</strong></td>
<td>Backup a Transport Global: This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>4</strong></td>
<td colspan="3">Under the Installation menu, select the package LR*5.2*480.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>5</strong></td>
<td colspan="3">When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install?  NO//', respond "NO".</td>
<td></td>
</tr>
<tr class="even">
<td><strong>6</strong></td>
<td colspan="3">When prompted 'Want KIDS to INHIBIT LOGONs during the install?  NO//', respond "NO".</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>7</strong></td>
<td colspan="3">When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', respond "NO".</td>
<td></td>
</tr>
<tr class="even">
<td><strong>8</strong></td>
<td colspan="3"><p>Enter the Device you want to print the Install message.</p>
<p>You can queue the install by enter a “Q” at the device prompt.</p>
<p>Enter a “^” to abort the install.</p></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>9</strong></td>
<td colspan="3">When prompted ‘Delay Install (Minutes): (0 – 60)://’, respond “0”.</td>
<td></td>
</tr>
</tbody>
</table>

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No specific verification procedures are required after the installations of patch LR\*5.2\*480. If desired, run Verify Checksums in Transport Global or use the following command: CHECK1^XTSUMBLD.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Back-Out pertains to a return to the last known good operational state of the software and appropriate platform settings.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During installation, if the option to back up routines was run as directed, ‘Backup a Transport Global’, then routines have the ability to be restored from the “backup” MailMan message that was generated. However, the KIDS installation process does not perform a restore of other VistA components, such as data dictionary, cross-reference, and template changes, etc.

Prior to attempting a back-out of the software, contact the VA Help Desk at 1-855-673-4357 for support or assistance.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LIM and the Chief of Pathology have the authority to order the back-out.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Load testing was not performed for the patches.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Criteria for a back-out includes, but are not limited, to the following:

1.  Failed baseline testing.
2.  Non-recoverable software error.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No back-out risks have been determined at this time.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LIM and the Chief of Pathology have the authority to order the Back-out Procedure.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Restore the backup message of any routines exported with the patches and reload the transport global.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify the back-out procedure by comparing the transport global to the current system state.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LR\*5.2\*480 and any installed dependent patches need to be taken out in reverse of the order in which these patches were installed; routines and data dictionary modifications and populated data must also be rolled back in reverse order.

Contact the VA Help Desk at 1-855-673-4357 for support or assistance regarding roll-back procedures.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No rollback considerations have been determined at this time.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The only criteria for a rollback that has been determined at this time is that the installation failed baseline testing.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The only risk determined at this time is the possibility of downtime which would only effect the users of the Laboratory package.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LIM and the Chief of Pathology have the authority to require the rollback and accept the risks.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The need for a rollback is highly unlikely, however if it is required, contact the product development team for assistance if needed. The rollback procedure may require Lab downtime and a reinstall of any previous KIDS versions.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No specific rollback verification procedures are required after the installations of patch LR\*5.2\*480.