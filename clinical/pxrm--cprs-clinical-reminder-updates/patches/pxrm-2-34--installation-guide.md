---
title: PXRM*2*34 Teratogenic Medication Reminder Order Check Update Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Teratogenic Medication Reminder Order Check Update
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*34
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: ![](pxrm-2-34-teratogenic-medication-reminder-order-check-update-installation-guide/001.png)
audience: 
keywords: 
  - contents
  - table
  - install
  - installation
  - order
  - check
  - pxrm
  - reminder
  - teratogenic
  - medications
page_count: 0
word_count: 1287
section_count: 14
table_count: 7
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: January 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_34_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_34_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

![](pxrm-2-34-teratogenic-medication-reminder-order-check-update-installation-guide/001.png)

Teratogenic Medication Reminder Order Check Update

PXRM\*2.0\*34

INSTALLATION and SETUP GUIDE

January 2014

Product Development

Contents

[Introduction [3](#introduction)](#introduction)

[Related Documentation](#related-documentation) 3

[Web Sites](#web-sites) 3

[Pre-Installation 3](#pre-installation)

[Required Software for PXRM\*2\*34 3](#required-software-for-pxrm234)

[Estimated Installation Time: 10-15 minutes](#this-patch-can-be-installed-with-users-on-the-system-but-it-should-be-done-during-non-peak-hours.-estimated-installation-time-10-15-minutes) 3

[Installation](#installation) 4

[1. Retrieve the host file containing from one of the following locations](#retrieve-the-host-file-from-one-of-the-following-locations-with-the-ascii-file-type) 4

[2. Install the build first in a training or test account.](#install-the-patch-first-in-a-training-or-test-account.) 4

[3. Load the distribution.](#load-the-distribution.) 4

[4. Backup a Transport Global](#backup-a-transport-global) 4

[a. Compare Transport Global to Current System](#compare-transport-global-to-current-system) 4

[5. Install the build.](#install-the-build.) 5

[6. Install File Print](#section-3) 5

[7. Build File Print](#build-file-print) 5

[8. Post-installation routines](#post-installation-routines) 5

[Post-Install Set-up Instructions](#post-install-set-up-instructions) 6

Appendix A: Installation Example 7

[Acronyms](#section-5) 9

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
- [Pre-Installation](#pre-installation)
  - [Required Software for PXRM\2\34](#required-software-for-pxrm234)
  - [## Related Documentation](#related-documentation)
    - [Web Sites](#web-sites)
- [Installation](#installation)
  - [This patch can be installed with users on the system, but it should be done during non-peak hours. Estimated Installation Time: 10-15 minutes](#this-patch-can-be-installed-with-users-on-the-system-but-it-should-be-done-during-non-peak-hours-estimated-installation-time-10-15-minutes)
  - [Retrieve the host file from one of the following locations (with the ASCII file type):](#retrieve-the-host-file-from-one-of-the-following-locations-with-the-ascii-file-type)
  - [Install the patch first in a training or test account.](#install-the-patch-first-in-a-training-or-test-account)
  - [Load the distribution.](#load-the-distribution)
  - [## Backup a Transport Global](#backup-a-transport-global)
  - [Compare Transport Global to Current System](#compare-transport-global-to-current-system)
  - [Install the build.](#install-the-build)
  - [## Install File Print](#install-file-print)
  - [## Build File Print](#build-file-print)
  - [Post-installation routines](#post-installation-routines)
- [Post-Install Set-up Instructions](#post-install-set-up-instructions)
  - [Activate the Reminder Order Check Rules](#activate-the-reminder-order-check-rules)
- [Appendix A: Installation Example](#appendix-a-installation-example)
- [# Acronyms](#acronyms)
The Teratogenic Medications Order Check Interim Solution was originally released as VistA patch PXRM\*2\*22 in July 2012. The interim solution is intended to have regular updates for clinical content, primarily to add newly approved medications with FDA Pregnancy Categories that warrant an order check. This patch, PXRM\*2\*34 represents the first such update. Included in this update are new medications, order check text changes consistent with the Notification of Teratogenic Medications project, support for reversal of tubal ligations, and updates to the taxonomies that define a women’s medical inability to conceive a pregnancy.
This patch also includes an update to a single dialog element for the Epilepsy Initial note that was released with PXRM\*2.0\*30. That element had a mapped Health Factor Category, instead of a mapped Health Factor. This element updates that mapped item.

# Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Required Software for PXRM\*2\*34

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                          |               |             |               |
|--------------------------|---------------|-------------|---------------|
| Package/Patch        | Namespace | Version | Comments  |
| Clinical Reminders       | PXRM          | 2.0         | Fully patched |
| Health Summary           | GMTS          | 2.7         | Fully patched |
| Kernel                   | XU            | 8.0         | Fully patched |
| NATIONAL DRUG FILE       | PSN           | 4.0         | Fully patched |
| Pharmacy Data Management | PSS           | 1.0         | Fully patched |
| Outpatient Pharmacy      | PSO           | 7.0         | Fully patched |
| VA FileMan               | DI            | 22          | Fully patched |

## ## Related Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                              |                             |
|------------------------------|-----------------------------|
| Documentation            | Documentation File name |
| Installation and Setup Guide | PXRM_2_0_34_IG.PDF          |

### Web Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                       |                                                           |                                                                                            |
|---------------------------------------|-----------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Site                              | URL                                                   | Description                                                                            |
| National Clinical Reminders site      | <http://vista.med.va.gov/reminders>                       | Contains manuals, PowerPoint presentations, and other information about Clinical Reminders |
| National Clinical Reminders Committee | <http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx> | This committee directs the development of new and revised national reminders               |
| VistA Document Library                | <http://www.va.gov/vdl/>                                  | Contains manuals for Clinical Reminders and                                                |

# Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## This patch can be installed with users on the system, but it should be done during non-peak hours. Estimated Installation Time: 10-15 minutes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*The installation needs to be done by a person with DUZ(0) set to "@."*NOTE: We recommend that a Clinical Reminders Manager or CAC be present during the install, so that if questions occur during the install of Reminder Exchange entries, a knowledgeable person can respond to them.

## Retrieve the host file from one of the following locations (with the ASCII file type): 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Albany <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

> Hines <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

> Salt Lake City <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

## Install the patch first in a training or test account. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

## Load the distribution. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name.KID at the Host File prompt.

Example

> Select Installation Option: LOAD a Distribution

> Enter a Host File: PXRM_2_0_34.KID

> KIDS Distribution saved on

From the Installation menu, you may elect to use the following options:

## ## Backup a Transport Global 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

## Compare Transport Global to Current System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

## Install the build.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PXRM\*2.0\*34 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Select Installation & Distribution System Option: Installation

> Select Installation Option: INSTALL PACKAGE(S)

> Select INSTALL NAME: PXRM\*2.0\*34

Answer "NO" to the following prompt:

> Want KIDS to INHIBIT LOGONs during install? NO// NO

> NOTE:DO NOT QUEUE THE INSTALLATION, because this installation asks questions requiring responses and queuing will stop the installation. A Reminders Manager or CAC should be present to respond to these.

> Installation Example

> See [Appendix A](\l).

## ## Install File Print 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi-package build.

> Select Utilities Option: Install File Print

> Select INSTALL NAME: PXRM\*2.0\*34

## ## Build File Print 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Build File Print option to print out the build components.

> Select Utilities Option: Build File Print

> Select BUILD NAME: PXRM\*2.0\*34

> DEVICE: HOME//

## Post-installation routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After successful installation, the following init routines may be deleted:

> PXRMP34E

> PXRMP34I

# Post-Install Set-up Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Activate the Reminder Order Check Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The installation of patch PXRM\*2\*34 will revert the STATUS of the Reminder Order Check Rules “VA-TERATOGENIC MEDICATIONS ORDER CHECK (CAT D) RULE” and “VA-TERATOGENIC MEDICATIONS ORDER CHECK (CAT X) RULE” to TEST. If your site is using these order checks, the rules will need to be re-activated to PROD status. Shown below are the steps to make this change, which should be done for both rules. The option represented here is Add/Edit Reminder Order Check Rule \[PXRM ORDER CHECK RULE EDIT\].

Select <u>Reminder Order Check Menu</u> Option: RE Add/Edit Reminder Order Check Rule

Select Reminder Order Check Rule by:  (N/R/T/Q): N// N  ORDER CHECK RULE NAME

Select Reminder Order Check Rule: ?

    Answer with REMINDER ORDER CHECK RULES RULE NAME

   Choose from:

     1   VA-TERATOGENIC MEDICATIONS ORDER CHECK (CAT D) RULE 

     2   VA-TERATOGENIC MEDICATIONS ORDER CHECK (CAT X) RULE 

CHOOSE 1-2: 1  VA-TERATOGENIC MEDICATIONS ORDER CHECK (CAT D) RULE

<u>RULE NAME</u>: VA-TERATOGENIC MEDICATIONS ORDER CHECK (CAT D) RULE            

<u>DISPLAY NAME</u>: Known or Potential Teratogen (FDA Cat. D or Cat. C w/other data)

<u>STATUS</u>: PROD ^ *change to PROD to activate Production Mode instead of Testing Mode*

<u>CLASS</u>: NATIONAL

SPONSOR:

REVIEW DATE:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

I=INACTIVE, P=PRODUCTION, T=TESTING

Enter a command or '^' followed by a caption to jump to a specific field.

# Appendix A: Installation Example 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: PXRM\*2.0\*34 11/6/13@10:22:54

=\> VA-TERATOGENIC MEDICATIONS ORDER CHECK UPDATE ;Created on Nov 06, 201

This Distribution was loaded on Nov 06, 2013@10:22:54 with header of

VA-TERATOGENIC MEDICATIONS ORDER CHECK UPDATE ;Created on Nov 06, 2013@10:00

:47

It consisted of the following Install(s):

PXRM\*2.0\*34

Checking Install for Package PXRM\*2.0\*34

Install Questions for PXRM\*2.0\*34

Incoming Files:

811.8 REMINDER EXCHANGE (including data)

> **NOTE:** You already have the 'REMINDER EXCHANGE' File.

I will OVERWRITE your data with mine.

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// TELNET PORT

--------------------------------------------------------------------------------

Install Started for PXRM\*2.0\*34 :

Nov 06, 2013@10:23:47

Build Distribution Date: Nov 06, 2013

Installing Routines:

Nov 06, 2013@10:23:47

Running Pre-Install Routine: PRE^PXRMP34I

DISABLE options.

DISABLE protocols.

Installing Data Dictionaries:

Nov 06, 2013@10:23:47

Installing Data:

Nov 06, 2013@10:23:47

Running Post-Install Routine: POST^PXRMP34I

ENABLE options.

ENABLE protocols.

There are 2 Reminder Exchange entries to be installed.

1\. Installing Reminder Exchange entry VA-TERATOGENIC MEDICATIONS ORDER CHECKS

(UPDATE \#1)

2\. Installing Reminder Exchange entry VA-ECOE PATCH 30 ELEMENT UPDATE

Deleting some DG entries from VA-TERATOGENIC MEDICATIONS (CAT D OR C) GROUP

Deleting some DG entries from VA-TERATOGENIC MEDICATIONS (CAT X) GROUP

Updating Routine file...

Updating KIDS files...

PXRM\*2.0\*34 Installed.

Nov 06, 2013@10:24:08

Not a production UCI

PXRM\*2.0\*34

Install Completed

# # Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OIT Master Glossary is available at <http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm>

| Term       | Definition                                                      |
|------------|-----------------------------------------------------------------|
| ASU        | Authorization/Subscription Utility                              |
| Clin4      | National Customer Support team that supports Clinical Reminders |
| CPRS       | Computerized Patient Record System                              |
| DBA        | Database Administration                                         |
| DG         | Registration and Enrollment Package namespace                   |
| ESM        | Enterprise Systems Management (ESM)                             |
| FIM        | Functional Independence Measure                                 |
| GMTS       | Health Summary namespace (also HSUM)                            |
| GUI        | Graphic User Interface                                          |
| HRMH/HRMHP | High Risk Mental Health Patient                                 |
| IAB        | Initial Assessment & Briefing                                   |
| ICD-10     | International Classification of Diseases, 10th Edition          |
| ICR        | Internal Control Number                                         |
| IOC        | Initial Operating Capabilities                                  |
| LSSD       | Last Service Separation Date                                    |
| MH         | Mental Health                                                   |
| MHTC       | Mental Health Treatment Coordinator                             |
| OHI        | Office of Health Information                                    |
| OI         | Office of Information                                           |
| OIF/OEF    | Operation Iraqi Freedom/Operation Enduring Freedom              |
| OIT/OI&T   | Office of Information Technology                                |
| OMHS       | Office of Mental Health Services                                |
| ORR        | Operational Readiness Review                                    |
| PCS        | Patient Care Services                                           |
| PD         | Product Development                                             |
| PIMS       | Patient Information Management System                           |
| PMAS       | Program Management Accountability System                        |
| PTM        | Patch Tracker Message                                           |
| PXRM       | Clinical Reminder Package namespace                             |
| RSD        | Requirements Specification Document                             |
| SD         | Scheduling Package Namespace                                    |
| SQA        | Software Quality Assurance                                      |
| USR        | ASU package namespace                                           |
| VA         | Department of Veteran Affairs                                   |
| VHA        | Veterans Health Administration                                  |
| VISN       | Veterans Integrated Service Network                             |
| VistA      | Veterans Health Information System and Technology Architecture  |