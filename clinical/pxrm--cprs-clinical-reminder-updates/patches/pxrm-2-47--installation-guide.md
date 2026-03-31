---
title: PXRM*2*47 ICD-10 Follow-up Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: ICD-10 Follow-up
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*47
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - taxonomy
  - working
  - zzva
  - table
  - palli
  - cons
  - install
  - contents
  - pxrm
  - clinical
page_count: 0
word_count: 3579
section_count: 14
table_count: 5
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: December 2017
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_47_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_47_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

![](pxrm-2-47-icd-10-follow-up-installation-guide/001.png)

Clinical Reminders

ICD-10 Follow-up

Installation Guide

PXRM\*2.0\*47

GMTS\*2.7\*113

December 2017

Office of Information and Technology (OIT)

Product Development

(this page intentionally left blank)

Table of Contents

Introduction [1](#introduction)

Background [1](#background)

Patches in this project build [1](#patches-in-this-project-build)

Related Documentation [2](#related-documentation)

Related Web Sites [3](#related-web-sites)

Pre-Installation [4](#pre-installation)

1\. Required Software [4](#required-software)

Installation [4](#installation)

1\. Retrieve the host file containing the multi-package build. [4](#retrieve-the-host-file-containing-the-multi-package-build.)

2\. Install the patch first in a training or test account. [5](#install-the-patch-first-in-a-training-or-test-account.)

3\. Backout preparation; these steps are taken in case the patch needs to be backed out. [5](#backout-preparation-these-steps-are-taken-in-case-the-patch-needs-to-be-backed-out.)

4\. Load the distribution. [5](#load-the-distribution.)

5\. Backup a Transport Global [6](#backup-a-transport-global)

6\. Compare Transport Global to Current System [6](#compare-transport-global-to-current-system)

7\. Verify Checksums in Transport Global [7](#verify-checksums-in-transport-global)

8\. Install the build [7](#install-the-build)

Post-Install Instructions [9](#post-install-instructions)

Acronyms [9](#acronyms)

Appendix A: Installation Example [11](#appendix-a-installation-example)

Appendix B: Post-Install Checksums [19](#appendix-b-post-install-checksums)

Appendix C: Install File Print Example [22](#_Toc495584527)

Appendix D: Build File Print Example [24](#appendix-d-build-file-print-example)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Background](#background)
  - [Patches in this project build](#patches-in-this-project-build)
  - [Related Documentation](#related-documentation)
  - [Related Web Sites](#related-web-sites)
- [Pre-Installation](#pre-installation)
  - [Required Software](#required-software)
- [Installation](#installation)
  - [Retrieve the host file containing the multi-package build.](#retrieve-the-host-file-containing-the-multi-package-build)
  - [Install the patch first in a training or test account.](#install-the-patch-first-in-a-training-or-test-account)
  - [Backout preparation; these steps are taken in case the patch needs to be backed out.](#backout-preparation-these-steps-are-taken-in-case-the-patch-needs-to-be-backed-out)
  - [Load the distribution.](#load-the-distribution)
  - [Backup a Transport Global](#backup-a-transport-global)
  - [Compare Transport Global to Current System](#compare-transport-global-to-current-system)
  - [Verify Checksums in Transport Global](#verify-checksums-in-transport-global)
  - [## Install the build](#install-the-build)
- [Post-Install Instructions](#post-install-instructions)
- [Acronyms](#acronyms)
- [# Appendix A: Installation Example](#appendix-a-installation-example)
- [Appendix B: Post-Install Checksums](#appendix-b-post-install-checksums)
- [Appendix C: Install File Print Example](#appendix-c-install-file-print-example)
- [Appendix D: Build File Print Example](#appendix-d-build-file-print-example)

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch is the follow-up to patch PXRM\*2\*26. It removes the options, protocols, routines, and taxonomy fields made obsolete by PXRM\*2\*26, adds the taxonomy editor actions that could not be completed in time for the release of PXRM\*2\*26, and fixes some defects.

> Testing revealed that the ScreenMan variable DDSCHANG can sometimes falsely indicate that a taxonomy was changed by the user during an editing session. To create a reliable indicator, the SHA-256 hash is computed when a taxonomy is selected for editing and again when the editing session is finished. If there is any difference in the values, then the taxonomy has changed. The SHA-256 hash is computed using the Kernel SHA hash utility distributed in XU\*8.0\*657; consequently XU\*8.0\*657 is required by PXRM\*2.0\*47.

> PXRM\*2.0\*47 and GMTS\*2.7\*113 are distributed in a multi-package build named: CLINICAL REMINDERS ICD-10 FOLLOWUP 1.0.

## Patches in this project build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PXRM\*2.0\*47

> This build is the follow-up to PXRM\*2.0\*26. It deletes the Expanded Taxonomies file \#811.3, removes the options, protocols, routines, and taxonomy fields made obsolete by PXRM\*2.0\*26, adds the taxonomy editor actions that could not be completed for the release of PXRM\*2.0\*26, and fixes some defects.

> The following items are deleted:

> PRINT TEMPLATES:

> PXRM TAXONOMY DIALOG FILE \#811.2

> PXRM TAXONOMY INQUIRY FILE \#811.2

> PXRM TAXONOMY LIST FILE \#811.2

> PXRM TAXONOMY LIST HEADER FILE \#811.2

> ROUTINES:

> PXRMBXTL

> PXRMCSD

> PXRMCSSC

> PXRMCSU

> PXRMTAXS

> PXRMTDUP

> PXRMTECK

> PXRMTEDT

> PXRMVAL

> PXRMVALC

> PXRMVALU

> OPTIONS:

> PXRM TAX SELECTED CODES REPAIR

> PXRM TAXONOMY CODE SEARCH

> PXRM TAXONOMY COPY

> PXRM TAXONOMY EDIT

> PXRM TAXONOMY EXPANSION

> PXRM TAXONOMY EXPANSION ALL

> PXRM TAXONOMY EXPANSION VERIFY

> PXRM TAXONOMY INQUIRY

> PXRM TAXONOMY LIST

> PXRM TAXONOMY MANAGEMENT (OLD)

> PROTOCOLS:

> PXRM DIALOG ADD

> PXRM LEXICON VIEW

> PXRM TAXONOMY OLD INQUIRE

> The National Library of Medicine has a Value Set Authority Center (VSAC) web site, where value sets can be obtained. From the web site: “Value sets are lists of specific values (terms and their codes) derived from single or multiple standard vocabularies used to define clinical concepts (e.g. patients with diabetes, clinical visit, reportable diseases) used in quality measures and to support effective health information exchange.” These value sets cover many clinical areas of relevance to the VA and because they are very similar to taxonomies, they can be used to automatically generate taxonomies. Some value sets contain coding systems that are not supported in taxonomies; if a taxonomy is generated from one of these value sets, only the codes from supported coding systems will be included.

> The Value Set functionality requires three new files: NLM QUALITY MEASURE GROUPS, NLM VALUE SET CODING SYSTEMS, and NLM VALUE SETS. These files are populated with the VSAC’s most recent release: January 2017. The following new options were created and added to the PXRM MANAGERS MENU.

> 1 NLM CLINICAL QUALITY MEASURES PXRM NLM CQM MENU NLM Clinical Quality Measures Menu

> 2 NLM VALUE SET MENU PXRM NLM VALUE SET MENU NLM Value Set Menu

GMTS\*2.7\*113

> One of the defects that is fixed involves display of the status line when the frequency is in hours. This change adds time to the Date Due and Last Done fields. Because there are a number of Clinical Reminders Health Summary components, a Health Summary patch is required, it is: GMTS\*2.7\*113.

## Related Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                    |                         |
|--------------------|-------------------------|
| Documentation      | Documentation File name |
| Installation Guide | PXRM_2_0_47_IG.PDF      |
| Manager’s Manual   | PXRM_2_0_MM.PDF         |

> **NOTE:** In this document, you will see references to both PXRM\*2\*47 and PXRM\*2.0\*47. The difference is that PXRM\*2\*47 is the name of the patch and PXRM\*2.0\*47 is the name of the build.

## Related Web Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                           |                                                                                  |                                                                                                  |
|-----------------------------------------------------------|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| Site                                                      | URL                                                                              | Description                                                                                      |
| National Clinical Reminders site                          | <http://vista.med.va.gov/reminders>                                              | Contains manuals, PowerPoint presentations, and other information about Clinical Reminders       |
| National Clinical Reminders Committee                     | <http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx>                        | This committee directs the development of new and revised national reminders                     |
| VistA Document Library                                    | <http://www.va.gov/vdl/>                                                         | Contains manuals for Clinical Reminders and related applications.                                |
| Health Information Management (HIM) ICD-10 Implementation | <https://vaww.vha.vaco.portal.va.gov/sites/HDI/HIM/vaco_HIM/SitePages/Home.aspx> | Contains general information, training resources, and other tools for VA’s transition to ICD-10. |

# Pre-Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Previously, the computed finding VA-REMINDER DEFINITION would return false if the Computed Finding Parameter was set to a reminder definition that did not exist. The most likely reason for the definition not to exist is because it was renamed and the Computed Finding Parameter was not updated accordingly. Returning false was somewhat misleading because the reminder was never actually evaluated. To prevent this, the computed finding was changed so if the reminder definition does not exist it sets a fatal error and sends an error message to the Clinical Reminders mail group.

> Before installing, it would be a good idea to run the Finding Usage Report and get a list of definitions and terms that use VA-REMINDER DEFINITION as a finding. For each instance, make sure that the Computed Finding Parameter is set to a valid reminder definition. This will prevent getting fatal errors because of incorrectly configured Computed Finding Parameters.

## Required Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *PXRM\*2.0\*47*

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 18%" />
<col style="width: 13%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th>Package/Patch</th>
<th>Namespace</th>
<th>Version</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Clinical Reminders</p>
<p>PXRM*2*26</p></td>
<td>PXRM</td>
<td>2</td>
<td>Fully patched</td>
</tr>
<tr class="even">
<td><p>Kernel</p>
<p>XU*8.0*657</p></td>
<td>XU</td>
<td>8.0</td>
<td>Fully patched</td>
</tr>
<tr class="odd">
<td>VA FileMan</td>
<td>DI</td>
<td>22.2</td>
<td>Fully patched</td>
</tr>
</tbody>
</table>

> *GMTS\*2.7\*113*

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 18%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Package/Patch</td>
<td>Namespace</td>
<td>Version</td>
<td>Comments</td>
</tr>
<tr class="even">
<td><p>Health Summary</p>
<p>GMTS*2.7*89</p>
<p>PXRM*2.0*47</p></td>
<td>GMTS</td>
<td>2.7</td>
<td></td>
</tr>
</tbody>
</table>

# Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes how to install the multi-package build that includes builds , PXRM\*2.0\*47 and GMTS\*2.7\*113.

> This patch can be loaded with users on the system, but it should be done during

> off-hours. Estimated installation time is less than 5 minutes.

> *The installation needs to be done by a person with DUZ(0) set to "@."*

## Retrieve the host file containing the multi-package build. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use sftp to access the build (the name of the host file is CR_ICD-10_FOLLOWUP .KID) from one of the following locations (with the ASCII file type):

> Hines <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

> Salt Lake City <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

## Install the patch first in a training or test account. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installing in a non-production environment will give you time to get familiar with new functionality.

## Backout preparation; these steps are taken in case the patch needs to be backed out. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Backup files ^PXD(811.2), ^PXRMD(811.4), and ^PXD(811.9) using your site’s policy for backing up data.
- If the steps are unknown, here is a way it can be done, using ^PXD(811.2) as an example:
  - Go to a command prompt.
  - At the prompt, enter D GOGEN^%ZSPECIAL.
  - At the device prompt, enter the directory and file name where the global backup is to be stored.
  - At the Parameters? Prompt, press \<enter\>.
  - At the Global prompt, enter ^PXD(811.2.
  - Verify that the file was created and exists in the directory specified.

Example

> DEV5A4:DVFDEV\>D GOGEN^%ZSPECIAL

> Device: VA5\$:\[Local Directory\]811_2_BACKUP.GBL

> Parameters? ("WNS") =\>

> Warning: Use a "V" format to avoid problems with control characters.

> Global ^PXD(811.2,

> Global ^

## Load the distribution. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In programmer mode, type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD INSTALLATION MENU), and then the option LOAD a Distribution. Enter the directory name where you placed the host file followed by CR_ICD-10_FOLLOWUP.KID at the Host File prompt.

> Example

> Select Installation Option: LOAD a Distribution

> Enter a Host File: VA5\$:\[DOWNLOADS\]CR_ICD-10_FOLLOWUP.KID

> KIDS Distribution saved on Apr 24, 2017@08:21:25

> Comment: CLINICAL REMINDERS ICD-10 FOLLOWUP

> From the Installation menu, you may elect to use the following options:

## Backup a Transport Global 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Installation option, Backup a Transport Global \[XPD BACKUP\]. This option creates a MailMan message that will backup all current routines on your VistA/M system that will be replaced by the builds in this transport global. (If you need to preserve components that are not routines, you must back them up separately.)  

> At the Select INSTALL NAME: prompt, enter Clinical Reminders ICD-10 Followup 1.0

> Example:

> Select Installation \<TEST ACCOUNT\> Option: Backup a Transport Global

> Select INSTALL NAME: CLINICAL REMINDERS ICD-10 FOLLOWUP 1.0 7/11/16@14:17:39

> =\> PXRM\*2.0\*47, GMTS\*2.7\*113 ;Created on Jul 05, 2016@11:14:

> This Distribution was loaded on Apr 24, 2017@13:31:45with header of

> CLINICAL REMINDERS ICD-10 FOLLOWUP ;Created on Apr 24, 2017@08:21:25

> It consisted of the following Install(s):

> CLINICAL REMINDERS ICD-10 FOLLOWUP 1.0 PXRM\*2.0\*47 GMTS\*2.7\*113Subject: Backup of CLINICAL REMINDERS ICD-10 FOLLOWUP 1.0 install on Apr

> Replace

> No routines for CLINICAL REMINDERS ICD-10 FOLLOWUP 1.0

> Loading Routines for PXRM\*2.0\*47..

> Routine PXRMBXTL is not on the disk......

> Routine PXRMCSD is not on the disk..

> Routine PXRMCSSC is not on the disk...

> Routine PXRMCSU is not on the disk....................................

> Routine PXRMPTTX is not on the disk.........

> Routine PXRMTAXS is not on the disk..

> Routine PXRMTDUP is not on the disk..

> Routine PXRMTECK is not on the disk..

> Routine PXRMTEDT is not on the disk............

> Routine PXRMVAL is not on the disk..

> Routine PXRMVALC is not on the disk..

> Routine PXRMVALU is not on the disk..........

> Loading Routines for GMTS\*2.7\*113.

> Send mail to: PXRMPROGRAMMER, ONE

> Select basket to send to: IN// PATCH BACKUP 

> And Send to:

## Compare Transport Global to Current System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

## Verify Checksums in Transport Global 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to ensure the integrity of the routines that are in the transport global. If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system. Retrieve the file again from the anonymous directory (in case there was corruption in SFTPing) and Load the Distribution again. If the problem still exists, log a ticket and/or call the national Help Desk (<span class="mark">REDACTED</span>) to report the problem.

> Example

> CHOOSE 1-2: 2 Option: 2 Verify Checksums in Transport Global

> Select INSTALL NAME:

> CLINICAL REMINDERS ICD-10 FOLLOWUP 1.0 4/24/17@13:31:

> 45

> =\> CLINICAL REMINDERS ICD-10 FOLLOWUP ;Created on Apr 24, 2017@08:21:25This Distribution was loaded on Apr 24, 2017@13:31:45 with header of

> CLINICAL REMINDERS ICD-10 FOLLOWUP ;Created on Apr 24, 2017@08:21:25

> It consisted of the following Install(s):

> CLINICAL REMINDERS ICD-10 FOLLOWUP 1.0 PXRM\*2.0\*47 GMTS\*2.7\*113

> Want each Routine Listed with Checksums: Yes//

> DEVICE: HOME// ;;999 TELNET PORT

## ## Install the build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build CLINICAL REMINDERS ICD-10 FOLLOWUP 1.0 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Select Installation & Distribution System Option: Installation

> Select Installation Option: INSTALL PACKAGE(S)

> Select INSTALL NAME: CLINICAL REMINDERS ICD-10 FOLLOWUP 1.0

> Answer the following install questions as follows:

- Although typically the answer is "No," you can answer "Yes," to the question:

> Want KIDS to Rebuild Menu Trees Upon Completion of Install?

> *Please remember that rebuilding menu trees will increase patch installation time.*

- Answer "No" to the question:

> Want KIDS to INHIBIT LOGONs during the install?

- Answer "No" to the question:

> Want to DISABLE Scheduled Options, Menu Options, and Protocols?

# Post-Install Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Post-install: After a successful installation, the init routine PXRMP47I can be deleted.

# Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OIT Master Glossary is available at http://vaww.oed.wss.va.gov/process/Lists/glossary/default.aspx
> National Acronym Directory:
> <http://vaww1.va.gov/Acronyms/>
| Term       | Definition                                                                      |
|------------|---------------------------------------------------------------------------------|
| ASU        | Authorization/Subscription Utility                                              |
| Clin2      | National Customer Support team that supports Clinical Reminders                 |
| CPRS       | Computerized Patient Record System                                              |
| DBA        | Database Administration                                                         |
| DG         | Registration and Enrollment Package namespace                                   |
| ESM        | Enterprise Systems Management (ESM)                                             |
| FIM        | Functional Independence Measure                                                 |
| GMPL       | Problem List namespace                                                          |
| GMTS       | Health Summary namespace (also HSUM)                                            |
| GUI        | Graphic User Interface                                                          |
| HRMH/HRMHP | High Risk Mental Health Patient                                                 |
| IAB        | Initial Assessment & Briefing                                                   |
| ICD-10-CM  | International Classification of Diseases, 10th Revision Clinical Modification   |
| ICD-9-CM   | International Classification of Diseases, Ninth Revision, Clinical Modification |
| ICR        | Internal Control Number                                                         |
| IOC        | Initial Operating Capabilities                                                  |
| LSSD       | Last Service Separation Date                                                    |
| MH         | Mental Health                                                                   |
| OHI        | Office of Health Information                                                    |
| OI         | Office of Information                                                           |
| OIT/OI&T   | Office of Information Technology                                                |
| OMHS       | Office of Mental Health Services                                                |
| ORR        | Operational Readiness Review                                                    |
| PCS        | Patient Care Services                                                           |
| PD         | Product Development                                                             |
| PIMS       | Patient Information Management System                                           |
| PMAS       | Program Management Accountability System                                        |
| PTM        | Patch Tracker Message                                                           |
| PXRM       | Clinical Reminder Package namespace                                             |
| RSD        | Requirements Specification Document                                             |
| SD         | Scheduling Package Namespace                                                    |
| SG         | Scheduling, Registration, Admission/Discharge/Transfer namespace                |
| SME        | Subject Matter Expert                                                           |
| SNOMED CT  | Systematic Nomenclature of Medicine of Clinical Terms                           |
| SQA        | Software Quality Assurance                                                      |
| VA         | Department of Veteran Affairs                                                   |
| VHA        | Veterans Health Administration                                                  |
| VISN       | Veterans Integrated Service Network                                             |
| VistA      | Veterans Health Information System and Technology Architecture                  |

# # Appendix A: Installation Example 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a capture of a Clinical Reminders ICD-10 Followup installation that provides details of the install.

Example: First-time Install

Select INSTALL NAME: CLINICAL REMINDERS ICD-10 FOLLOWUP 1.0 Loaded from Distribution 4/25/17@09:21:38

=\> CLINICAL REMINDERS ICD-10 FOLLOWUP ;Created on Apr 24, 2017@08:21:25

This Distribution was loaded on Apr 25, 2017@09:21:38 with header of

CLINICAL REMINDERS ICD-10 FOLLOWUP ;Created on Apr 24, 2017@08:21:25

It consisted of the following Install(s):

CLINICAL REMINDERS ICD-10 FOLLOWUP 1.0 PXRM\*2.0\*47 GMTS\*2.7\*113

Checking Install for Package CLINICAL REMINDERS ICD-10 FOLLOWUP 1.0

Install Questions for CLINICAL REMINDERS ICD-10 FOLLOWUP 1.0

Checking Install for Package PXRM\*2.0\*47

Install Questions for PXRM\*2.0\*47

Incoming Files:

802.1 NLM VALUE SET CODING SYSTEMS

802.2 NLM VALUE SETS

802.3 NLM QUALITY MEASURE GROUPS

811.2 REMINDER TAXONOMY

> **NOTE:** You already have the 'REMINDER TAXONOMY' File.

811.4 REMINDER COMPUTED FINDINGS (including data)

> **NOTE:** You already have the 'REMINDER COMPUTED FINDINGS' File.

I will OVERWRITE your data with mine.

811.9 REMINDER DEFINITION (Partial Definition)

> **NOTE:** You already have the 'REMINDER DEFINITION' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Checking Install for Package GMTS\*2.7\*113

Install Questions for GMTS\*2.7\*113

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// TELNET

--------------------------------------------------------------------------------

Install Started for CLINICAL REMINDERS ICD-10 FOLLOWUP 1.0 :

Apr 25, 2017@09:22:59

Build Distribution Date: Apr 24, 2017

Installing Routines:

Apr 25, 2017@09:22:59

Install Started for PXRM\*2.0\*47 :

Apr 25, 2017@09:22:59

Build Distribution Date: Apr 24, 2017

Installing Routines:

Apr 25, 2017@09:23

Running Pre-Install Routine: PRE^PXRMP47I

DISABLE options.

DISABLE protocols.

Deleting the DATA DICTIONARY...

Deleting the INPUT TEMPLATES...

Deleting the PRINT TEMPLATES.......

Deleting the SORT TEMPLATES...

Deleting the FORMS...

Deleting the BLOCKS...

Installing Data Dictionaries:

Apr 25, 2017@09:23:08

Installing Data:

Apr 25, 2017@09:23:08

Installing PACKAGE COMPONENTS:

Installing PRINT TEMPLATE

Installing FORM

Installing PROTOCOL

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Located in the PXRM (CLINICAL REMINDERS) namespace.

Installing LIST TEMPLATE

Installing OPTION

Apr 25, 2017@09:23:08

Running Post-Install Routine: POST^PXRMP47I

Removing obsolete field data

Working on taxonomy GP IM PNEUMOC PCV13 PREVNAR

Working on taxonomy GP IM PNEUMOC PPSV23 PNEUMOVAX

Working on taxonomy HF LIPID LDL 120-129

Working on taxonomy HF LIPID LDL 71-99

Working on taxonomy HF LIPID LDL \>190

Working on taxonomy PALLI CONS DYSPNEA MILD (E)

Working on taxonomy PALLI CONS DYSPNEA SEVERE (E)

Working on taxonomy PALLI CONS INPT 99251 (E)

Working on taxonomy PALLI CONS INPT 99252 (E)

Working on taxonomy PALLI CONS INPT 99253 (E)

Working on taxonomy PALLI CONS INPT 99254 (E)

Working on taxonomy PALLI CONS INPT 99255 (E)

Working on taxonomy PALLI CONS OUTPT 99241 (E)

Working on taxonomy PALLI CONS OUTPT 99242 (E)

Working on taxonomy PALLI CONS OUTPT 99243 (E)

Working on taxonomy PALLI CONS OUTPT 99244 (E)

Working on taxonomy PALLI CONS OUTPT 99245 (E)

Working on taxonomy PALLI CONS OUTPT ENCOUNTER GP

Working on taxonomy PALLI CONS PAIN NONE (E)

Working on taxonomy PALLI CONS PAIN SEVERE (E)

Working on taxonomy PALLI CONS PT PREFER DOC NO (E)

Working on taxonomy PALLI CONS PT PREFER DOC YES (E)

Working on taxonomy VA-ABD AORTIC ANEURYSM

Working on taxonomy VA-ALCOHOL ABUSE

Working on taxonomy VA-BREAST TUMOR

Working on taxonomy VA-CERVICAL CA/ABNORMAL PAP

Working on taxonomy VA-DEPRESSION DIAGNOSIS

Working on taxonomy VA-DEPRESSION DX OUTPT VISIT

Working on taxonomy VA-DIABETES

Working on taxonomy VA-DIABETES HEDIS

Working on taxonomy VA-DIABETES HEDIS PROB LIST

Working on taxonomy VA-DRUG ABUSE FOR HCV TESTING

Working on taxonomy VA-EBOLA RISK TRIAGE DIAGNOSIS CODE

Working on taxonomy VA-ECOE DIAGNOSIS CODES

Working on taxonomy VA-HEPATITIS C INFECTION

Working on taxonomy VA-HEPATITIS C SEROPOSITIVE

Working on taxonomy VA-HERPES ZOSTER (SHINGLES) IMMUNIZATION

Working on taxonomy VA-HIV INFECTION

Working on taxonomy VA-HYPERTENSION

Working on taxonomy VA-HYPERTENSION CODES

Working on taxonomy VA-HYSTERECTOMY

Working on taxonomy VA-IHD AND ASVD

Working on taxonomy VA-IM FLU HIGH DOSE

Working on taxonomy VA-IMAGING FOR AAA (NON-SPECIFIC)

Working on taxonomy VA-IMMUNOCOMPROMISED

Working on taxonomy VA-MAMMOGRAM/SCREEN

Working on taxonomy VA-MASTECTOMY

Working on taxonomy VA-MHV BILATERAL AMPUTEE

Working on taxonomy VA-MHV COLONOSCOPY

Working on taxonomy VA-MHV DIABETIC RETINAL DISEASE

Working on taxonomy VA-MHV RETINAL EXAMINATION

Working on taxonomy VA-MHV SIGMOIDOSCOPY

Working on taxonomy VA-PALLI CONS CANCER/HEMA COND

Working on taxonomy VA-PALLI CONS CARDIO COND OTHER THAN CA

Working on taxonomy VA-PALLI CONS CNS COND OTHER THAN CA

Working on taxonomy VA-PALLI CONS DERM CONDITION DX

Working on taxonomy VA-PALLI CONS GI OTHER THAN CA

Working on taxonomy VA-PALLI CONS INFECTIOUS COND

Working on taxonomy VA-PALLI CONS RENAL OTHER THAN CA

Working on taxonomy VA-PALLI CONS RHEUM/VASC/THROMB

Working on taxonomy VA-PNEUMOC DZ RISK - CHEMOTHERAPY

Working on taxonomy VA-PNEUMOC DZ RISK - HIGH

Working on taxonomy VA-PNEUMOC DZ RISK - HIGHEST/NOT IMMUNO COMP

Working on taxonomy VA-PNEUMOC DZ RISK - IMMUNOCOMPROMISED

Working on taxonomy VA-PNEUMOC PCV13 IMMUNIZATION

Working on taxonomy VA-PNEUMOC PPSV23 IMMUNIZATION

Working on taxonomy VA-PSYCHOTHERAPY CPT CODES

Working on taxonomy VA-PTSD DIAGNOSIS

Working on taxonomy VA-PTSD DX OUTPT PRIMARY

Working on taxonomy VA-PTSD DX OUTPT VISIT

Working on taxonomy VA-SCHIZOPHRENIA

Working on taxonomy VA-TB/POSITIVE PPD

Working on taxonomy VA-TD VACCINE ADSORBED GENERIC (RD)

Working on taxonomy VA-TD VACCINE PRESERV FREE ADSORBED (RD)

Working on taxonomy VA-TDAP VACCINE (RD)

Working on taxonomy VA-TERATOGENIC MEDICATIONS ORDER CHECK EXCL (TAXONOMIES)

Working on taxonomy VA-TERMINAL CANCER PATIENTS

Working on taxonomy VA-TOBACCO USE

Working on taxonomy VA-WH BILATERAL MASTECTOMY

Working on taxonomy VA-WH HYSTERECTOMY W/CERVIX REMOVED

Working on taxonomy VA-WH PAP SMEAR OBTAINED

Working on taxonomy VA-WH PAP SMEAR SCREEN CODES

Working on taxonomy VA-WH TUBAL LIGATION CODES (TAXONOMY)

Working on taxonomy VA-WH TUBAL REANASTOMOSIS (TAXONOMY)

Working on taxonomy ZZVA-ALCOHOLISM SCREENING

Working on taxonomy ZZVA-CERVICAL CANCER SCREEN

Working on taxonomy ZZVA-CHOLESTEROL

Working on taxonomy ZZVA-COLORECTAL CA

Working on taxonomy ZZVA-COLORECTAL CANCER SCREEN

Working on taxonomy ZZVA-EXERCISE COUNSELING

Working on taxonomy ZZVA-FLEXISIGMOIDOSCOPY

Working on taxonomy ZZVA-FOBT

Working on taxonomy ZZVA-HIGH RISK FOR FLU/PNEUMONIA

Working on taxonomy ZZVA-HIGH RISK FOR INFLUENZA

Working on taxonomy ZZVA-HIGH RISK FOR TB

Working on taxonomy ZZVA-HYPERTENSION SCREEN

Working on taxonomy ZZVA-IM FLU H1N1 (1 DOSE)

Working on taxonomy ZZVA-INFLUENZA IMMUNIZATION

Working on taxonomy ZZVA-ISCHEMIC HEART 412 DISEASE

Working on taxonomy ZZVA-ISCHEMIC HEART DISEASE

Working on taxonomy ZZVA-MHV IHD AND ATHERSCLEROSIS

Working on taxonomy ZZVA-NUTRITION

Working on taxonomy ZZVA-OBESITY

Working on taxonomy ZZVA-PNEUMOCOCCAL VACCINE

Working on taxonomy ZZVA-POLYTRAUMA AMPUTATION

Working on taxonomy ZZVA-POLYTRAUMA AUDITORY

Working on taxonomy ZZVA-POLYTRAUMA BRAIN INJURY

Working on taxonomy ZZVA-POLYTRAUMA BURN

Working on taxonomy ZZVA-POLYTRAUMA INPT REHAB

Working on taxonomy ZZVA-POLYTRAUMA ORTHO

Working on taxonomy ZZVA-POLYTRAUMA PTSD

Working on taxonomy ZZVA-POLYTRAUMA SCI

Working on taxonomy ZZVA-POLYTRAUMA VISION

Working on taxonomy ZZVA-POLYTRAUMA WAR INJURY

Working on taxonomy ZZVA-PROSTATE CA

Working on taxonomy ZZVA-PSA

Working on taxonomy ZZVA-SAFETY COUNSELING

Working on taxonomy ZZVA-TETANUS DIPHTHERIA

Working on taxonomy ZZVA-WEIGHT AND NUTRITION SCREEN

Working on taxonomy ZZVA-WH IUD INSERTION (TAXONOMY)

Working on taxonomy ZZVA-WH IUD REMOVAL (TAXONOMY)

Building the Selected Codes multiple indexes.

Taxonomy: GP IM PNEUMOC PCV13 PREVNAR; IEN=100

Taxonomy: GP IM PNEUMOC PPSV23 PNEUMOVAX; IEN=71

Taxonomy: HF LIPID LDL 120-129; IEN=101

Taxonomy: HF LIPID LDL 71-99; IEN=99

Taxonomy: HF LIPID LDL \>190; IEN=98

Taxonomy: PALLI CONS DYSPNEA MILD (E); IEN=95

Taxonomy: PALLI CONS DYSPNEA SEVERE (E); IEN=94

Taxonomy: PALLI CONS INPT 99251 (E); IEN=91

Taxonomy: PALLI CONS INPT 99252 (E); IEN=90

Taxonomy: PALLI CONS INPT 99253 (E); IEN=84

Taxonomy: PALLI CONS INPT 99254 (E); IEN=83

Taxonomy: PALLI CONS INPT 99255 (E); IEN=82

Taxonomy: PALLI CONS OUTPT 99241 (E); IEN=78

Taxonomy: PALLI CONS OUTPT 99242 (E); IEN=77

Taxonomy: PALLI CONS OUTPT 99243 (E); IEN=74

Taxonomy: PALLI CONS OUTPT 99244 (E); IEN=73

Taxonomy: PALLI CONS OUTPT 99245 (E); IEN=72

Taxonomy: PALLI CONS OUTPT ENCOUNTER GP; IEN=79

Taxonomy: PALLI CONS PAIN NONE (E); IEN=97

Taxonomy: PALLI CONS PAIN SEVERE (E); IEN=96

Taxonomy: PALLI CONS PT PREFER DOC NO (E); IEN=92

Taxonomy: PALLI CONS PT PREFER DOC YES (E); IEN=93

Taxonomy: VA-ABD AORTIC ANEURYSM; IEN=13

Taxonomy: VA-ALCOHOL ABUSE; IEN=17

Taxonomy: VA-BREAST TUMOR; IEN=18

Taxonomy: VA-CERVICAL CA/ABNORMAL PAP; IEN=5

Taxonomy: VA-DEPRESSION DIAGNOSIS; IEN=49

Taxonomy: VA-DEPRESSION DX OUTPT VISIT; IEN=160

Taxonomy: VA-DIABETES; IEN=28

Taxonomy: VA-DIABETES HEDIS; IEN=317

Taxonomy: VA-DIABETES HEDIS PROB LIST; IEN=316

Taxonomy: VA-DRUG ABUSE FOR HCV TESTING; IEN=55

Taxonomy: VA-EBOLA RISK TRIAGE DIAGNOSIS CODE; IEN=153

Taxonomy: VA-ECOE DIAGNOSIS CODES; IEN=61

Taxonomy: VA-HEPATITIS C INFECTION; IEN=2

Taxonomy: VA-HEPATITIS C SEROPOSITIVE; IEN=152

Taxonomy: VA-HERPES ZOSTER (SHINGLES) IMMUNIZATION; IEN=159

Taxonomy: VA-HIV INFECTION; IEN=57

Taxonomy: VA-HYPERTENSION; IEN=1

Taxonomy: VA-HYPERTENSION CODES; IEN=46

Taxonomy: VA-HYSTERECTOMY; IEN=6

Taxonomy: VA-IHD AND ASVD; IEN=315

Taxonomy: VA-IM FLU HIGH DOSE; IEN=243

Taxonomy: VA-IMAGING FOR AAA (NON-SPECIFIC); IEN=12

Taxonomy: VA-IMMUNOCOMPROMISED; IEN=156

Taxonomy: VA-MAMMOGRAM/SCREEN; IEN=16

Taxonomy: VA-MASTECTOMY; IEN=19

Taxonomy: VA-MHV BILATERAL AMPUTEE; IEN=87

Taxonomy: VA-MHV COLONOSCOPY; IEN=85

Taxonomy: VA-MHV DIABETIC RETINAL DISEASE; IEN=88

Taxonomy: VA-MHV RETINAL EXAMINATION; IEN=89

Taxonomy: VA-MHV SIGMOIDOSCOPY; IEN=86

Taxonomy: VA-PALLI CONS CANCER/HEMA COND; IEN=70

Taxonomy: VA-PALLI CONS CARDIO COND OTHER THAN CA; IEN=68

Taxonomy: VA-PALLI CONS CNS COND OTHER THAN CA; IEN=69

Taxonomy: VA-PALLI CONS DERM CONDITION DX; IEN=65

Taxonomy: VA-PALLI CONS GI OTHER THAN CA; IEN=67

Taxonomy: VA-PALLI CONS INFECTIOUS COND; IEN=63

Taxonomy: VA-PALLI CONS RENAL OTHER THAN CA; IEN=66

Taxonomy: VA-PALLI CONS RHEUM/VASC/THROMB; IEN=64

Taxonomy: VA-PNEUMOC DZ RISK - CHEMOTHERAPY; IEN=80

Taxonomy: VA-PNEUMOC DZ RISK - HIGH; IEN=3

Taxonomy: VA-PNEUMOC DZ RISK - HIGHEST/NOT IMMUNO COMP; IEN=344

Taxonomy: VA-PNEUMOC DZ RISK - IMMUNOCOMPROMISED; IEN=81

Taxonomy: VA-PNEUMOC PCV13 IMMUNIZATION; IEN=149

Taxonomy: VA-PNEUMOC PPSV23 IMMUNIZATION; IEN=103

Taxonomy: VA-PSYCHOTHERAPY CPT CODES; IEN=50

Taxonomy: VA-PTSD DIAGNOSIS; IEN=161

Taxonomy: VA-PTSD DX OUTPT PRIMARY; IEN=37

Taxonomy: VA-PTSD DX OUTPT VISIT; IEN=176

Taxonomy: VA-SCHIZOPHRENIA; IEN=52

Taxonomy: VA-TB/POSITIVE PPD; IEN=10

Taxonomy: VA-TD VACCINE ADSORBED GENERIC (RD); IEN=157

Taxonomy: VA-TD VACCINE PRESERV FREE ADSORBED (RD); IEN=60

Taxonomy: VA-TDAP VACCINE (RD); IEN=102

Taxonomy: VA-TERATOGENIC MEDICATIONS ORDER CHECK EXCL (TAXONOMIES); IEN=108

Taxonomy: VA-TERMINAL CANCER PATIENTS; IEN=56

Taxonomy: VA-TOBACCO USE; IEN=22

Taxonomy: VA-WH BILATERAL MASTECTOMY; IEN=62

Taxonomy: VA-WH HYSTERECTOMY W/CERVIX REMOVED; IEN=58

Taxonomy: VA-WH PAP SMEAR OBTAINED; IEN=48

Taxonomy: VA-WH PAP SMEAR SCREEN CODES; IEN=59

Taxonomy: VA-WH TUBAL LIGATION CODES (TAXONOMY); IEN=75

Taxonomy: VA-WH TUBAL REANASTOMOSIS (TAXONOMY); IEN=76

Taxonomy: ZZVA-ALCOHOLISM SCREENING; IEN=34

Taxonomy: ZZVA-CERVICAL CANCER SCREEN; IEN=30

Taxonomy: ZZVA-CHOLESTEROL; IEN=24

Taxonomy: ZZVA-COLORECTAL CA; IEN=4

Taxonomy: ZZVA-COLORECTAL CANCER SCREEN; IEN=31

Taxonomy: ZZVA-EXERCISE COUNSELING; IEN=32

Taxonomy: ZZVA-FLEXISIGMOIDOSCOPY; IEN=15

Taxonomy: ZZVA-FOBT; IEN=27

Taxonomy: ZZVA-HIGH RISK FOR FLU/PNEUMONIA; IEN=9

Taxonomy: ZZVA-HIGH RISK FOR INFLUENZA; IEN=7

Taxonomy: ZZVA-HIGH RISK FOR TB; IEN=11

Taxonomy: ZZVA-HYPERTENSION SCREEN; IEN=23

Taxonomy: ZZVA-IM FLU H1N1 (1 DOSE); IEN=227

Taxonomy: ZZVA-INFLUENZA IMMUNIZATION; IEN=33

Taxonomy: ZZVA-ISCHEMIC HEART 412 DISEASE; IEN=44

Taxonomy: ZZVA-ISCHEMIC HEART DISEASE; IEN=14

Taxonomy: ZZVA-MHV IHD AND ATHERSCLEROSIS; IEN=40

Taxonomy: ZZVA-NUTRITION; IEN=21

Taxonomy: ZZVA-OBESITY; IEN=20

Taxonomy: ZZVA-PNEUMOCOCCAL VACCINE; IEN=25

Taxonomy: ZZVA-POLYTRAUMA AMPUTATION; IEN=54

Taxonomy: ZZVA-POLYTRAUMA AUDITORY; IEN=53

Taxonomy: ZZVA-POLYTRAUMA BRAIN INJURY; IEN=51

Taxonomy: ZZVA-POLYTRAUMA BURN; IEN=47

Taxonomy: ZZVA-POLYTRAUMA INPT REHAB; IEN=45

Taxonomy: ZZVA-POLYTRAUMA ORTHO; IEN=43

Taxonomy: ZZVA-POLYTRAUMA PTSD; IEN=42

Taxonomy: ZZVA-POLYTRAUMA SCI; IEN=41

Taxonomy: ZZVA-POLYTRAUMA VISION; IEN=39

Taxonomy: ZZVA-POLYTRAUMA WAR INJURY; IEN=38

Taxonomy: ZZVA-PROSTATE CA; IEN=8

Taxonomy: ZZVA-PSA; IEN=26

Taxonomy: ZZVA-SAFETY COUNSELING; IEN=35

Taxonomy: ZZVA-TETANUS DIPHTHERIA; IEN=29

Taxonomy: ZZVA-WEIGHT AND NUTRITION SCREEN; IEN=36

Taxonomy: ZZVA-WH IUD INSERTION (TAXONOMY); IEN=109

Taxonomy: ZZVA-WH IUD REMOVAL (TAXONOMY); IEN=110

Installing Value Set data.

Making sure all DO IN ADVANCE TIME FRAMEs are uppercase.

Making sure all reminder frequencies are uppercase.

Found lower case baseline frequency:

IEN=128 IND=2 Frequency=0y

Changing it to upper case.

ENABLE options.

ENABLE protocols.

Updating Routine file...

Updating KIDS files...

PXRM\*2.0\*47 Installed.

Apr 25, 2017@09:23:40

Not a production UCI

NO Install Message sent

Install Started for GMTS\*2.7\*113 :

Apr 25, 2017@09:23:40

Build Distribution Date: Apr 24, 2017

Installing Routines:

Apr 25, 2017@09:23:40

Updating Routine file...

Updating KIDS files...

GMTS\*2.7\*113 Installed.

Apr 25, 2017@09:23:40

Not a production UCI

NO Install Message sent

Updating Routine file...

Updating KIDS files...

CLINICAL REMINDERS ICD-10 FOLLOWUP 1.0 Installed.

Apr 25, 2017@09:23:40

No link to PACKAGE file

Install Completed

# Appendix B: Post-Install Checksums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Checksums: PXRM Routines

CPRS285A4:CPRS30\>D CHECK1^XTSUMBLD

New CheckSum CHECK1^XTSUMBLD:

This option determines the current checksum of selected routine(s).

The Checksum of the routine is determined as follows:

1\. Any comment line with a single semi-colon is presumed to be

followed by comments and only the line tag will be included.

2\. Line 2 will be excluded from the count.

3\. The total value of the routine is determined (excluding

exceptions noted above) by multiplying the ASCII value of each

character by its position on the line and position of the line in

the routine being checked.

Select one of the following:

P Package

B Build

Build from: Build

This will check the routines from a BUILD file.

Select BUILD NAME: PXRM\*2.0\*47 CLINICAL REMINDERS

PXRM value = 47307370

PXRMASL value = 4451968

PXRMCDEF value = 4852404

PXRMCOND value = 44611363

PXRMCQIN value = 24112852

PXRMCQLM value = 20001822

PXRMCSTX value = 2714904

PXRMDATE value = 72754452

PXRMDBLD value = 54628364

PXRMDEV value = 53641052

PXRMDIEV value = 75240155

PXRMDLL value = 147254046

PXRMDLLB value = 36248685

PXRMDRUG value = 62235689

PXRMDTAX value = 198889216

PXRMERRH value = 21386013

PXRMETXR value = 76063275

PXRMEXCC value = 14643642

PXRMEXCO value = 26994015

PXRMEXCS value = 16682539

PXRMEXFI value = 59766502

PXRMEXIC value = 87332423

PXRMEXIU value = 86717543

PXRMEXLM value = 51322537

PXRMEXMH value = 10558717

PXRMEXU0 value = 29114606

PXRMEXWB value = 1606210

PXRMFF value = 75070206

PXRMFF0 value = 19175056

PXRMFIND value = 14402705

PXRMFMTO value = 10636061

PXRMFNFT value = 58123785

PXRMHVET value = 1748161

PXRMICHK value = 238423274

PXRMLDR value = 18348692

PXRMLEX value = 8264453

PXRMLEXL value = 190120643

PXRMLOCF value = 97441474

PXRMLOCL value = 28870554

PXRMLOG value = 66402903

PXRMMSG value = 5151324

PXRMORCH value = 53534150

PXRMOUTC value = 38936387

PXRMOUTD value = 15041011

PXRMOUTM value = 29787683

PXRMOUTU value = 18283584

PXRMP47I value = 30350491

PXRMPDEM value = 65842415

PXRMPDR value = 52184470

PXRMPDRP value = 100715785

PXRMPRF value = 15497099

PXRMRCUR value = 13247111

PXRMREDF value = 84791298

PXRMREDT value = 70476581

PXRMRPCA value = 57506116

PXRMRUL1 value = 49947013

PXRMSXRM value = 98450970

PXRMTAXD value = 79799584

PXRMTAXL value = 80891432

PXRMTERM value = 55250159

PXRMTEXT value = 44027439

PXRMTXCR value = 23196731

PXRMTXDL value = 1372560

PXRMTXIM value = 196801557

PXRMTXIN value = 62837955

PXRMTXLS value = 150968479

PXRMTXSM value = 56360268

PXRMUIDE value = 17671178

PXRMUTIL value = 164856611

PXRMVCPT value = 52602127

PXRMVPOV value = 51972823

PXRMVSCS value = 6081007

PXRMVSIN value = 48824341

PXRMVSLM value = 26634140

PXRMVSTX value = 61497746

PXRMXEVL value = 1513078

PXRMXSE1 value = 30585167

done

Installation Checksums: GMTS Routines

CPRS285A4:CPRS30\>D CHECK1^XTSUMBLD

New CheckSum CHECK1^XTSUMBLD:

This option determines the current checksum of selected routine(s).

The Checksum of the routine is determined as follows:

1\. Any comment line with a single semi-colon is presumed to be

followed by comments and only the line tag will be included.

2\. Line 2 will be excluded from the count.

3\. The total value of the routine is determined (excluding

exceptions noted above) by multiplying the ASCII value of each

character by its position on the line and position of the line in

the routine being checked.

Select one of the following:

P Package

B Build

Build from: Build

This will check the routines from a BUILD file.

Select BUILD NAME: GMTS\*2.7\*113 HEALTH SUMMARY

GMTSPXHR value = 21877798

done

# Appendix C: Install File Print Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi-package build.

> Select OPTION NAME: XPD PRINT INSTALL FILE Install File Print

> Install File Print

> Select INSTALL NAME: PXRM\*2.0\*47 Install Completed 4/25/17@09:23:40

> =\> CLINICAL REMINDERS ICD-10 FOLLOWUP ;Created on Apr 24, 2017@08:21:25

> DEVICE: HOME// ;;999 TELNET

> PACKAGE: PXRM\*2.0\*47 Apr 25, 2017 9:40 am PAGE 1

> COMPLETED ELAPSED

> -------------------------------------------------------------------------------

> STATUS: Install Completed DATE LOADED: APR 25, 2017@09:21:38

> INSTALLED BY: TESTMASTER,USER

> NATIONAL PACKAGE: CLINICAL REMINDERS

> INSTALL STARTED: APR 25, 2017@09:22:59 09:23:40 0:00:41

> ROUTINES: 09:23 0:00:01

> PRE-INIT CHECK POINTS:

> XPD PREINSTALL STARTED 09:23:07 0:00:07

> XPD PREINSTALL COMPLETED 09:23:07

> FILES:

> NLM VALUE SET CODING SYSTEMS 09:23:07

> NLM VALUE SETS 09:23:07

> NLM QUALITY MEASURE GROUPS 09:23:08 0:00:01

> REMINDER TAXONOMY 09:23:08

> REMINDER COMPUTED FINDINGS 09:23:08

> REMINDER DEFINITION 09:23:08

> PRINT TEMPLATE 09:23:08

> FORM 09:23:08

> PROTOCOL 09:23:08

> LIST TEMPLATE 09:23:08

> OPTION 09:23:08

> POST-INIT CHECK POINTS:

> XPD POSTINSTALL STARTED 09:23:40 0:00:32

> XPD POSTINSTALL COMPLETED 09:23:40

> INSTALL QUESTION PROMPT ANSWER

> XPO1 Want KIDS to Rebuild Menu Trees Upon Completion of Install NO

> MESSAGES:

> Install Started for PXRM\*2.0\*47 :

> Apr 25, 2017@09:22:59

> Build Distribution Date: Apr 24, 2017

> Installing Routines:

> Apr 25, 2017@09:23

> Running Pre-Install Routine: PRE^PXRMP47I

> DISABLE options.

> DISABLE protocols.

> Installing Data Dictionaries:

> Apr 25, 2017@09:23:08

> Installing Data:

> Apr 25, 2017@09:23:08

> Installing PACKAGE COMPONENTS:

> Installing PRINT TEMPLATE

> Installing FORM

> Installing PROTOCOL

> Installing LIST TEMPLATE

> Installing OPTION

> Apr 25, 2017@09:23:08

> Running Post-Install Routine: POST^PXRMP47I

> Removing obsolete field data

> Working on taxonomy GP IM PNEUMOC PCV13 PREVNAR

> Working on taxonomy GP IM PNEUMOC PPSV23 PNEUMOVAX

> Working on taxonomy HF LIPID LDL 120-129

> Etc. See Installation example in [Appendix A](#appendix-a-installation-example)

# Appendix D: Build File Print Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Build File Print option to print out the build components. You can select the multi-package build or any of the individual builds included in the multi-package build.

> Select OPTION NAME: XPD PRINT BUILD Build File Print

> Build File Print

> Select BUILD NAME: PXRM\*2.0\*47 CLINICAL REMINDERS

> DEVICE: HOME// ;;999 TELNET PORT

> PACKAGE: PXRM\*2.0\*47 Apr 25, 2017 9:45 am PAGE 1

> -------------------------------------------------------------------------------

> TYPE: SINGLE PACKAGE TRACK NATIONALLY: YES

> NATIONAL PACKAGE: CLINICAL REMINDERS ALPHA/BETA TESTING: NO

> DESCRIPTION:

> Clinical Reminders ICD-10 follow-up build.

> ENVIRONMENT CHECK: DELETE ENV ROUTINE:

> PRE-INIT ROUTINE: PRE^PXRMP47I DELETE PRE-INIT ROUTINE: No

> POST-INIT ROUTINE: POST^PXRMP47I DELETE POST-INIT ROUTINE: No

> PRE-TRANSPORT RTN: VSSAVE^PXRMP47I

> UP SEND DATA USER

> DATE SEC. COMES SITE RSLV OVER

> FILE \# FILE NAME DD CODE W/FILE DATA PTRS RIDE

> -------------------------------------------------------------------------------

> 802.1 NLM VALUE SET CODING SYSTEMS YES YES NO

> 802.2 NLM VALUE SETS YES YES NO

> 802.3 NLM QUALITY MEASURE GROUPS YES YES NO

> 811.2 REMINDER TAXONOMY YES YES NO

> 811.4 REMINDER COMPUTED FINDINGS NO YES YES OVER NO NO

> DATA SCREEN: I \$\$CFINC^PXRMP47I(Y)

> 811.9 REMINDER DEFINITION YES YES NO NO

> Partial DD: subDD: 811.9256 fld: .01

> PRINT TEMPLATE: ACTION:

> PXRM TAXONOMY DIALOG FILE \#811.2 DELETE AT SITE

> PXRM TAXONOMY INQUIRY FILE \#811.2 DELETE AT SITE

> PXRM TAXONOMY LIST FILE \#811.2 DELETE AT SITE

> PXRM TAXONOMY LIST HEADER FILE \#811.2 DELETE AT SITE

> FORM: ACTION:

> PXRM DIALOG TAXONOMY EDIT FILE \#811.2 SEND TO SITE

> PXRM TAXONOMY CHANGE LOG FILE \#811.2 SEND TO SITE

> PXRM TAXONOMY EDIT FILE \#811.2 SEND TO SITE

> ROUTINE: ACTION:

> PXRM SEND TO SITE

> PXRMASL SEND TO SITE

> PXRMBXTL DELETE AT SITE

> PXRMCDEF SEND TO SITE

> PXRMCOND SEND TO SITE

> PXRMCQIN SEND TO SITE

> PXRMCQLM SEND TO SITE

> PXRMCSD DELETE AT SITE

> PXRMCSSC DELETE AT SITE

> PXRMCSTX SEND TO SITE

> PXRMCSU DELETE AT SITE

> PXRMDATE SEND TO SITE

> PXRMDBLD SEND TO SITE

> PXRMDEV SEND TO SITE

> PXRMDIEV SEND TO SITE

> PXRMDLL SEND TO SITE

> PXRMDLLB SEND TO SITE

> PXRMDRUG SEND TO SITE

> PXRMDTAX SEND TO SITE

> PXRMERRH SEND TO SITE

> PXRMETXR SEND TO SITE

> PXRMEXCC SEND TO SITE

> PXRMEXCO SEND TO SITE

> PXRMEXCS SEND TO SITE

> PXRMEXFI SEND TO SITE

> PXRMEXIC SEND TO SITE

> PXRMEXIU SEND TO SITE

> PXRMEXLM SEND TO SITE

> PXRMEXMH SEND TO SITE

> PXRMEXU0 SEND TO SITE

> PXRMEXWB SEND TO SITE

> PXRMFF SEND TO SITE

> PXRMFF0 SEND TO SITE

> PXRMFIND SEND TO SITE

> PXRMFMTO SEND TO SITE

> PXRMFNFT SEND TO SITE

> PXRMHVET SEND TO SITE

> PXRMICHK SEND TO SITE

> PXRMLDR SEND TO SITE

> PXRMLEX SEND TO SITE

> PXRMLEXL SEND TO SITE

> PXRMLOCF SEND TO SITE

> PXRMLOCL SEND TO SITE

> PXRMLOG SEND TO SITE

> PXRMMSG SEND TO SITE

> PXRMORCH SEND TO SITE

> PXRMOUTC SEND TO SITE

> PXRMOUTM SEND TO SITE

> PXRMOUTU SEND TO SITE

> PXRMP47I SEND TO SITE

> PXRMPDEM SEND TO SITE

> PXRMPDR SEND TO SITE

> PXRMPDRP SEND TO SITE

> PXRMPRF SEND TO SITE

> PXRMPTTX DELETE AT SITE

> PXRMRCUR SEND TO SITE

> PXRMREDF SEND TO SITE

> PXRMREDT SEND TO SITE

> PXRMRPCA SEND TO SITE

> PXRMRUL1 SEND TO SITE

> PXRMSXRM SEND TO SITE

> PXRMTAXD SEND TO SITE

> PXRMTAXL SEND TO SITE

> PXRMTAXS DELETE AT SITE

> PXRMTDUP DELETE AT SITE

> PXRMTECK DELETE AT SITE

> PXRMTEDT DELETE AT SITE

> PXRMTERM SEND TO SITE

> PXRMTEXT SEND TO SITE

> PXRMTXCR SEND TO SITE

> PXRMTXDL SEND TO SITE

> PXRMTXIM SEND TO SITE

> PXRMTXIN SEND TO SITE

> PXRMTXLS SEND TO SITE

> PXRMTXSM SEND TO SITE

> PXRMUIDE SEND TO SITE

> PXRMUTIL SEND TO SITE

> PXRMVAL DELETE AT SITE

> PXRMVALC DELETE AT SITE

> PXRMVALU DELETE AT SITE

> PXRMVCPT SEND TO SITE

> PXRMVPOV SEND TO SITE

> PXRMVSCS SEND TO SITE

> PXRMVSIN SEND TO SITE

> PXRMVSLM SEND TO SITE

> PXRMVSTX SEND TO SITE

> PXRMXEVL SEND TO SITE

> PXRMXSE1 SEND TO SITE

> OPTION: ACTION:

> PXRM DISABLE/ENABLE EVALUATION SEND TO SITE

> PXRM MANAGERS MENU USE AS LINK FOR MENU/ITEM/SUBS

> CRIBERS

> PXRM NLM CQM MENU SEND TO SITE

> PXRM NLM VALUE SET MENU SEND TO SITE

> PXRM TAX SELECTED CODES REPAIR DELETE AT SITE

> PXRM TAXONOMY CODE SEARCH DELETE AT SITE

> PXRM TAXONOMY COPY DELETE AT SITE

> PXRM TAXONOMY EDIT DELETE AT SITE

> PXRM TAXONOMY EXPANSION DELETE AT SITE

> PXRM TAXONOMY EXPANSION ALL DELETE AT SITE

> PXRM TAXONOMY EXPANSION VERIFY DELETE AT SITE

> PXRM TAXONOMY INQUIRY DELETE AT SITE

> PXRM TAXONOMY LIST DELETE AT SITE

> PXRM TAXONOMY MANAGEMENT (OLD) DELETE AT SITE

> PROTOCOL: ACTION:

> PXRM CQM INQUIRE SEND TO SITE

> PXRM CQM MENU SEND TO SITE

> PXRM CQM SELECT ENTRY SEND TO SITE

> PXRM DIALOG ADD DELETE AT SITE

> PXRM DIALOG EXIT SEND TO SITE

> PXRM DIALOG HISTORY SEND TO SITE

> PXRM DIALOG LINK SEND TO SITE

> PXRM LEXICON REMOVE FROM DIALOG SEND TO SITE

> PXRM LEXICON VIEW DELETE AT SITE

> PXRM TAXONOMY ADD SEND TO SITE

> PXRM TAXONOMY ALL SELECTED ADD SEND TO SITE

> PXRM TAXONOMY ALL SELECTED EXIT SEND TO SITE

> PXRM TAXONOMY ALL SELECTED MENU SEND TO SITE

> PXRM TAXONOMY ALL SELECTED RFD SEND TO SITE

> PXRM TAXONOMY ALL SELECTED RFT SEND TO SITE

> PXRM TAXONOMY ALL SELECTED SAVE SEND TO SITE

> PXRM TAXONOMY ALL SELECTED SELECT SEND TO SITE

> PXRM TAXONOMY ALL SELECTED UID SEND TO SITE

> PXRM TAXONOMY ALL SELECTED UID EDIT SEND TO SITE

> PXRM TAXONOMY CHANGE LOG SEND TO SITE

> PXRM TAXONOMY CODE SEARCH SEND TO SITE

> PXRM TAXONOMY COPY SEND TO SITE

> PXRM TAXONOMY EDIT SEND TO SITE

> PXRM TAXONOMY IMPORT SEND TO SITE

> PXRM TAXONOMY INQUIRE SEND TO SITE

> PXRM TAXONOMY MENU SEND TO SITE

> PXRM TAXONOMY OLD INQUIRE DELETE AT SITE

> PXRM TAXONOMY UID EDIT SEND TO SITE

> PXRM TAXONOMY UID REPORT SEND TO SITE

> PXRM TAXONOMY UIDE EXIT SEND TO SITE

> PXRM TAXONOMY UIDE SAVE SEND TO SITE

> PXRM TAXONOMY UIDE SELECT ENTRY SEND TO SITE

> PXRM TAXONOMY VALUE SET COMPARE SEND TO SITE

> PXRM VS CODE SEARCH SEND TO SITE

> PXRM VS CREATE TAXONOMY SEND TO SITE

> PXRM VS INQUIRE SEND TO SITE

> PXRM VS MENU SEND TO SITE

> PXRM VS SELECT ENTRY SEND TO SITE

> LIST TEMPLATE: ACTION:

> PXRM CQM MENU SEND TO SITE

> PXRM EX MAIN HELP DELETE AT SITE

> PXRM TAXONOMY ALL SELECTED SEND TO SITE

> PXRM TAXONOMY UID EDIT SEND TO SITE

> PXRM VS MENU SEND TO SITE

> INSTALL QUESTIONS:

> Default Rebuild Menu Trees Upon Completion of Install: NO

> Default INHIBIT LOGONs during the install: NO

> Default DISABLE Scheduled Options, Menu Options, and Protocols: NO

> REQUIRED BUILDS: ACTION:

> PXRM\*2.0\*26 Don't install, leave global

> PX\*1.0\*201 Don't install, leave global

> XU\*8.0\*657 Don't install, leave global

> PXRM\*2.0\*53 Don't install, leave global