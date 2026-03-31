---
title: YS*5.01*158 Suicide Prevention Package Patch Deployment, Installation, Back-Out and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: Suicide Prevention Package Patch
app_code: YS
app_name: Mental Health
section: CLI
app_status: active
pkg_ns: YS
patch_ver: 5.01
patch_id: YS*5.01*158
group_key: "YS:YS:5.01"
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
  - global
  - install
  - transport
  - distribution
  - procedure
  - rollback
page_count: 0
word_count: 2608
section_count: 22
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/clin_0004ax_ig_ys_501_158.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/clin_0004ax_ig_ys_501_158.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=78"
---

Mental Health – Suicide Prevention

Suicide Prevention Package Patch YS\*5.01\*158

![](ys-5-01-158-suicide-prevention-package-patch-deployment-installation-back-out-an/001.png)

May 2021

Deployment, Installation, Back-Out and Rollback Guide-YS\*5.01\*158

Submitted as CLIN 0004AX

Contract VA118-16-D-1007, Task Order VA11817F10070006

*Submitted by:*

Booz Allen Hamilton Inc.

141 W. Front Street, Suite 200

Red Bank, NJ 07701

Phone: 732-936-3500

Fax: 732-936-3535

![](ys-5-01-158-suicide-prevention-package-patch-deployment-installation-back-out-an/002.png)

Revision History

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 46%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Version</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>02/28/2021</td>
<td>1.3</td>
<td><p>Update – Build 14</p>
<ul>
<li><p>Update application name from MHA PaSE to MHA Web</p></li>
</ul></td>
<td>Booz Allen</td>
</tr>
<tr class="even">
<td>12/11/2020</td>
<td>1.2</td>
<td>Update – Build 13</td>
<td>Booz Allen</td>
</tr>
<tr class="odd">
<td>09/11/2020</td>
<td>1.1</td>
<td>Update</td>
<td>Booz Allen</td>
</tr>
<tr class="even">
<td>06/26/2020</td>
<td>1.0</td>
<td>Initial Draft</td>
<td>Booz Allen</td>
</tr>
</tbody>
</table>

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Dependencies](#dependencies)
  - [Constraints](#constraints)
- [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Backup Server Side Components](#backup-server-side-components)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
- [Installation Procedure](#installation-procedure)
  - [Install React/Java Components](#install-reactjava-components)
  - [Install VistA Components](#install-vista-components)
    - [Load the KIDS Distribution](#load-the-kids-distribution)
    - [Verify the Checksums](#verify-the-checksums)
    - [Print the Transport Global](#print-the-transport-global)
    - [Compare the Transport Global](#compare-the-transport-global)
    - [Backup the Transport Global](#backup-the-transport-global)
    - [Install the KIDS Distribution](#install-the-kids-distribution)
  - [Installation Verification Procedure](#installation-verification-procedure)
- [Implementation Procedure](#implementation-procedure)
  - [User Configuration](#user-configuration)
    - [Configure NEW PERSON](#configure-new-person)
    - [Add the Necessary SECURITY KEYs](#add-the-necessary-security-keys)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-Out Procedure](#back-out-procedure-1)
    - [VistA Component Backout](#vista-component-backout)
    - [React/Java Component Backout](#reactjava-component-backout)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
The Deployment, Installation, Back-Out, Rollback Guide defines the ordered, technical steps required to install the product, and if necessary, to back-out the installation, and to roll back to the previously installed version of the product. It provides installation instructions for the patch YS\*5.01\*158 MHA Planning and Staff entry (MHA Web), as managed through the Suicide Prevention Project.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a document that describes how, when, where, and to whom Mental Health patch YS\*5.01\*158 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Minimum requirements:

|                      |                            |
|----------------------|----------------------------|
| Application Name | Minimum Version Needed |
| CPRS                 | 31 A                       |
| Clinical Reminders   | 2.0                        |
| Kernel               | 8.0                        |
| RPC Broker           | 1.1                        |
| PIMS                 | 5.3                        |
| VA FileMan           | 22.2                       |
| Mailman              | 8.0                        |

It is assumed that this patch is being installed into a fully patched Veterans Health Information System and Technology Architecture (VistA) system.

The following patches are required:

YS\*5.01\*141 – MHA GUI and Web Updates

YS\*5.01\*150 – Suicide Prevention Instruments

YS\*5.01\*173 - INACTIVATE I9 INSTRUMENTS, UPDATE PROMIS29

The following patch is strongly recommended:

DG\*5.3\*1026 – Master Veteran Index VistA Enhancement – TFL API Update

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no constraints beyond the installation into an up-to-date VistA system.

# Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch installs one new Remote Procedure Call (RPC) and updates two VistA files.

## Backup Server Side Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The React/Java server side implementation is managed through the Azure administration console. The person designated to maintain the Azure Docker based application will be responsible for backup of the current image.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation will require:

- Access to the cloud environment by the Azure application administrator
- Programmer Access to VistA
- Knowledge of the Kernel Installation and Distribution System (KIDS) function in VistA
- Knowledge of the FileMan Enter/Edit function in VistA
- Access to file system resources to access and install host files if necessary.

# Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Install React/Java Components 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Azure administrator will be responsible for the installation. Further information can be found in the document Azure installation guide, CLIN 0004AX-A_IG.docx, in the Suicide Prevention Project (SPP) MHA documentation.

## Install VistA Components 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load the KIDS Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Load the contents of the package by logging in to VistA. Go to the MailMan menu, select the PackMan patch message containing the YS\*5.01\*158 patch. At the message action prompt, select extract the KIDS package.

Type \<Enter\> to continue or '^' to exit: ^

Enter message action (in IN basket): Ignore// x Xtract KIDS

Select PackMan function: 6 INSTALL/CHECK MESSAGE

Line 3 Message \#130243 Unloading KIDS Distribution YS\*5.01\*158

Loading Distribution...

YS\*5.01\*158

### Verify the Checksums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Kernel Installation &Distribution System Installation menu choose Verify Checksums in Transport Global for YS\*5.01\*158.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 2 Verify Checksums in Transport Global

Select INSTALL NAME: YS\*5.01\*158

This Distribution was loaded on …

Want each Routine Listed with Checksums: Yes// YES

### Print the Transport Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Kernel Installation &Distribution System Installation menu choose Print Transport Global for YS\*5.01\*158. (Note: Below is just an example. Actual display may vary slightly)

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 3 Print Transport Global

Select INSTALL NAME: YS\*5.01\*158

Select one of the following:

1 Print Summary

2 Print Summary and Routines

3 Print Routines

What to Print: 1 Print Summary

DEVICE: HOME// PSEUDO-TERMINAL SLAVE

PACKAGE: YS\*5.01\*158 Feb 11, 2021 3:11 pm PAGE 1

-------------------------------------------------------------------------------

TYPE: SINGLE PACKAGE TRACK NATIONALLY: YES

NATIONAL PACKAGE: MENTAL HEALTH ALPHA/BETA TESTING: NO

DESCRIPTION:

Mental Health web application support

ENVIRONMENT CHECK: DELETE ENV ROUTINE:

PRE-INIT ROUTINE: DELETE PRE-INIT ROUTINE:

POST-INIT ROUTINE: POST^YS158PST DELETE POST-INIT ROUTINE: No

PRE-TRANSPORT RTN:

UP SEND DATA USER

DATE SEC. COMES SITE RSLV OVER

FILE \# FILE NAME DD CODE W/FILE DATA PTRS RIDE

-------------------------------------------------------------------------------

601.71 MH TESTS AND SURVEYS YES YES NO NO

Partial DD: subDD: 601.71 fld: 95

fld: 96

601.712 MH TEST/SURVEY SPEC NO NO YES OVER YES NO

DATA SCREEN: I "^BAM^EAT^POQ^COP^"\[("^"\_\$E(\$G(^YTT(601.71,+\$P(^(0),U),0)),1,3)

\_"^")

601.84 MH ADMINISTRATIONS YES YES NO NO

Partial DD: subDD: 601.84 fld: 16

ROUTINE: ACTION:

YS158PST SEND TO SITE

YTQREST SEND TO SITE

YTQRQAD SEND TO SITE

YTQRQAD3 SEND TO SITE

YTQRQAD4 SEND TO SITE

YTQRQAD5 SEND TO SITE

YTQRQAD6 SEND TO SITE

YTQRUTL SEND TO SITE

OPTION: ACTION:

YS BROKER1 SEND TO SITE

YTQREST MHA SEND TO SITE

REMOTE PROCEDURE: ACTION:

YTQREST QADMIN SEND TO SITE

INSTALL QUESTIONS:

Default Rebuild Menu Trees Upon Completion of Install: NO

Default INHIBIT LOGONs during the install: NO

Default DISABLE Scheduled Options, Menu Options, and Protocols: NO

REQUIRED BUILDS: ACTION:

YS\*5.01\*150 Don't install, remove global

DG\*5.3\*1026 Warning only

YS\*5.01\*141 Don't install, remove global

YS\*5.01\*173 Don't install, remove global

### Compare the Transport Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Kernel Installation & Distribution System Installation menu choose Compare Transport Global for YS\*5.01\*158. The output should identify changes to the transport global. If there are no changes identified, the installation package is faulty, and a developer must be notified.

### Backup the Transport Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the Kernel Installation & Distribution System Installation menu choose Backup a Transport Global for YS\*5.01\*158. This is a critical step as it will allow a roll-back if necessary.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 5 Backup a Transport Global

Select INSTALL NAME: YS\*5.01\*135

Subject: Backup of YS\*5.01\*158 install on Feb 7, 2019

Replace

Loading Routines for YS\*5.01\*158.........

Send mail to: INSTALLER,NAME// INSTALLER,NAME

Select basket to send to: IN//

And Send to:

### Install the KIDS Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Log in to VistA and go to the Kernel Installation and Distribution System (KIDS) Menu \[XPD MAIN\]:

Edits and Distribution ...

> Utilities ...

Installation ...

Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System Option: Installation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Use the Install Package(s) option and select the package YS\*5.01\*158.

1.  When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//", answer NO.
2.  When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//", answer NO.
3.  When prompted "Want to DISABLE Scheduled Options and Menu Options and Protocols? NO//", answer NO.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the KIDS package has been installed, a person with sufficient access should check the system error trap and verify there are no errors.

# Implementation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the KIDS and React/Java packages have been installed, configure the users to enable them to use MHA Web.

## User Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Configure NEW PERSON

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The users must have the following Secondary Menu assigned:

- YS BROKER1

> **NOTE:** This is done to streamline installation. All users who have access via YS BROKER1 will automatically have access to this application.

### Add the Necessary SECURITY KEYs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new Security Keys required at this time.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is possible to back-out the installation of YS\*5.01\*158. The back-out of changes to the data dictionary is not recommended. This should be done in consultation with the developers and would require a patch to a patch. The server side Java environment would have to be restored by Azure administrator.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please contact VistA support and the development team before attempting a back-out.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TBD

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TBD

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A back-out should only be considered if there is a patient safety issue, if Mental Health Assistant no longer functions, or if there is some other catastrophic failure.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The risks vary depending on what is causing the failure of the system. The main risk is that the Mental Health package would be left in an unknown configured state.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA system manager determines if a back-out of YS\*5.01\*158 should be considered.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VistA Component Backout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See below for a screen scrape of removal using programmer mode.

In order to back out the VistA Components of the MHA Web the following routines need to be removed:

- YS158PST
- YTQREST
- YTQRQAD
- YTQRQAD3
- YTQRQAD4
- YTQRQAD5
- YTQRQAD6

> **NOTE:** There is overlap in routine YTQRQAD3 with Patch YS\*5.01\*141. Care must be taken not to adversely affect YS\*5.01\*141.

Next, restore the routines from backup made in 3.2.5.

The files below have fields added and could be rolled back at the discretion of the system administrator. However, this is not recommended unless with the consultation with the developers as these fields may contain data.

- 601.71 MH TESTS AND SURVEYS
  - 95: ROUTINE FOR SUICIDE RISK-Name of routine for calculating suicide risk
  - 96: TAG FOR SUICIDE RISK-Name of tag for calculating suicide risk
- 601.84 MH ADMINISTRATIONS
  - 16: SUICIDE RISK- Calculated suicide risk value

Using Fileman, next delete OPTION (#19) YTQREST MHA and REMOTE PROCEDURE (#8994) YTQREST QADMIN. You can do this using the roll and scroll interface, or use the APIs shown below.

Here are detailed instructions from Programmer Mode. User typed text is in bold. Text between \[ \] describes sections that are omitted or user instructions.

V2004\>F X="YS158PST","YTQREST","YTQRQAD","YTQRQAD4","YTQRQAD5","YTQRQAD6","YTQRUTL" X ^%ZOSF("DEL")

V2004\>D ^XM

\[Read the message then then use X to load it into Packman\]

Enter message action (in IN basket): Ignore// Xtract PackMan

Select PackMan function: 6 INSTALL/CHECK MESSAGE

> **WARNING:** Installing this message will cause a permanent update of globals

and routines.

Do you really want to do this? NO// YES

Routines are the only parts that are backed up. NO other parts

are backed up, not even globals. You may use the 'Summarize Message'

option of PackMan to see what parts the message contains.

Those parts that are not routines should be backed up separately

if they need to be preserved.

Shall I preserve the routines on disk in a separate back-up message? YES// NO

No backup message built.

Line 2 Message \#129673 Unloading Routine YTQREST (PACKMAN_BACKUP)

Line 66 Message \#129673 Unloading Routine YTQRQAD (PACKMAN_BACKUP)

Line 241 Message \#129673 Unloading Routine YTQRQAD4 (PACKMAN_BACKUP)

Line 449 Message \#129673 Unloading Routine YTQRQAD5 (PACKMAN_BACKUP)

Line 624 Message \#129673 Unloading Routine YTQRUTL (PACKMAN_BACKUP)

; \[Verify Routine has been rolled back. Patch list shouldn’t contain 158\]

V2004\>ZL YTQRUTL P +2

;;5.01;MENTAL HEALTH;\*\*130\*\*;Dec 30, 1994;Build 62

; \[It is not recommended to delete the data dictionaries as data may exist in there. Please consult with the developers for instructions on what to do.\]

; \[Delete option and then verify deletion\]

V2004\>S FDA(19,\$\$FIND1^DIC(19,,"XQ","YTQREST MHA","B")\_",",.01)="@" D FILE^DIE(,"FDA")

V2004\>W \$\$FIND1^DIC(19,,"XQ","YTQREST MHA","B")

0

; \[Delete RPC and then verify deletion\]

V2004\>S FDA(8994,\$\$FIND1^DIC(8994,,"XQ","YTQREST QADMIN","B")\_",",.01)="@" D FILE^DIE(,"FDA")

V2004\>W \$\$FIND1^DIC(8994,,"XQ","YTQREST QADMIN","B")

0

### React/Java Component Backout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Azure administrator will be responsible for backing out the React/Java component.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Since the MHA Web contains new components only, there is no data to rollback.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A