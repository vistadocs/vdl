---
title: "Laboratory: Universal Interface AutoRelease Version 1 Installation Backout and Rollback Guide"
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: anchor
doc_subject: Installation Backout and Rollback Guide
app_code: LA
app_name: "Laboratory: Universal Interface"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 1
patch_id: 
group_key: "LA::1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - span
  - auto
  - table
  - contents
  - release
  - mark
  - class
  - installation
  - install
  - interface
page_count: 0
word_count: 4862
section_count: 30
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2016
revision_count: 5
revision_newest: 6/28/2016
revision_oldest: 10/29/2015
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/labautorelease_1_0_installationguide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/labautorelease_1_0_installationguide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=120"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>VistA Laboratory Enhancements - Auto Verification

  Installation, Back-out, and Rollback Plan
---

![](laboratory-universal-interface-autorelease-version-1-installation-backout-and-ro/001.png)

June 2016

Revision History

| Date       | Version | Description                                                             | Author                             |
|------------|---------|-------------------------------------------------------------------------|------------------------------------|
| 6/28/2016  | 1.4     | Peer reviewed; removed blue instructional text.                         | <span class="mark">REDACTED</span> |
| 6/25/2016  | 1.3     | Update and incorporate feedback from <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| 6/24/2016  | 1.2     | Update for National Release                                             | <span class="mark">REDACTED</span> |
| 11/2/2015  | 1.1     | Update Rollback procedures                                              | <span class="mark">REDACTED</span> |
| 10/29/2015 | 1.0     | Original Draft - ORR                                                    | <span class="mark">REDACTED</span> |

Revision History includes date of changes, version number, description of changes, and author of revisions.

Artifact Rationale

The Installation, Back-out, Rollback Plan defines the ordered, technical steps required to install the product, and if necessary, to back-out the installation, and to roll back to the previously installed version of the product.

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
    - [Documentation Conventions](#documentation-conventions)
- [System Requirements](#system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Procedure](#download-and-extract-procedure)
  - [Database Creation](#database-creation)
- [Installation Process](#installation-process)
  - [Host File Selection](#host-file-selection)
  - [Environment Check](#environment-check)
  - [Select Account](#select-account)
  - [Backup Transport Global ![](laboratory-universal-interface-autorelease-version-1-installation-backout-and-ro/010.png)](#backup-transport-global-laboratory-universal-interface-autorelease-version-1-installation-backout-and-ro010png)
  - [Install Package](#install-package)
  - [COTS Driver Inquiry and Verification](#cots-driver-inquiry-and-verification)
  - [Final Install Questions](#final-install-questions)
- [Implementation Steps](#implementation-steps)
  - [Set Auto Release Results System Wide parameter to enabled.](#set-auto-release-results-system-wide-parameter-to-enabled)
  - [Enable the instrument(s) for Auto Release.](#enable-the-instruments-for-auto-release)
  - [Create Load/List profile for Auto Release](#create-loadlist-profile-for-auto-release)
  - [Run Configuration Report](#run-configuration-report)
  - [Create Lab users in GIM](#create-lab-users-in-gim)
  - [Configure Ordering Provider contact information](#configure-ordering-provider-contact-information)
  - [Configure Proxy Users](#configure-proxy-users)
- [Back-out Procedure](#back-out-procedure)
  - [Back-out Strategy](#back-out-strategy)
  - [Back-out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
  - [Back-out Criteria](#back-out-criteria)
  - [Back-out Risks](#back-out-risks)
  - [Authority for Back-out](#authority-for-back-out)
  - [Back-out Procedure](#back-out-procedure-1)
    - [![](laboratory-universal-interface-autorelease-version-1-installation-backout-and-ro/015.png) Preferred Method:](#laboratory-universal-interface-autorelease-version-1-installation-backout-and-ro015png-preferred-method)
    - [Inactivate Auto Verification](#inactivate-auto-verification)
  - [Disable the instrument(s) for Auto Release.](#disable-the-instruments-for-auto-release)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
This document provides installation instructions for LR\*5.2\*458 & LA\*5.2\*88 as managed through the VistA Lab Enhancement-Auto Verification project.

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual uses several methods to highlight different aspects of the material.
Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols.
Table 1. Documentation Symbols and Descriptions
| Symbol                                                                                                                                                                                                                                 | Description                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![](laboratory-universal-interface-autorelease-version-1-installation-backout-and-ro/004.png)                                                        | NOTE: Used to inform the reader of general information including references to additional reading material |
| ![](laboratory-universal-interface-autorelease-version-1-installation-backout-and-ro/005.png) | CAUTION: Used to caution the reader to take special notice of critical information                     |
Table used for formatting purposes onlySample Documentation Symbols Descriptions. An "i" with a circle around it indicates additional information. A triangle with an exclamation point inside indicates caution.
- “Snapshots” of computer online displays (i.e., character-based screen captures/dialogs) and computer source code are shown in a non-proportional font and enclosed within a box. Also included are Graphical User Interface (GUI) Microsoft Windows images (i.e., dialogs or forms).
- User's responses to online prompts (e.g., manual entry, taps, clicks, etc.) will be boldface type.
- All uppercase is reserved for the representation of acronyms, M code, variable names, or the formal name of options, field and file names, and security key (e.g., the XUPROGMODE key).

# System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provide the minimum requirements for the product to be installed, as well as the recommended hardware and software system requirements, including platform, OS, and storage requirements.

N/A, enhancements operate within VistA Laboratory.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption>Platform Installation and PreparationPlatform Installation and Preparation</caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](laboratory-universal-interface-autorelease-version-1-installation-backout-and-ro/006.png) ![](laboratory-universal-interface-autorelease-version-1-installation-backout-and-ro/007.png)</p>
<p>![](laboratory-universal-interface-autorelease-version-1-installation-backout-and-ro/008.png) <strong>Please note:</strong></p>
<p>The person installing the KIDS build will be prompted with 1 or 2 pre-install questions requiring yes/no answers.</p>
<ol type="1">
<li><p>The first question is: <strong>Is this site using the Lab UI V1.6 interface?</strong></p></li>
</ol>
<ul>
<li><p>If they answer NO then installation will proceed to update the interface to HL7 v2.5.1.</p></li>
<li><p>If they answer YES then a second question will be asked.</p></li>
</ul>
<ol start="2" type="1">
<li><p>The second question is: <strong>Has the Lab UI COTS driver been upgraded to send HL7 v2.5.1 messages?</strong></p>
<ol type="a">
<li><p>This normally involves a driver update on the COTS GIM system to allow the COTS system to send HL7 messages indicating either HL7 v2.2 or v2.5.1.</p></li>
</ol></li>
</ol>
<blockquote>
<p><strong>Contact your Laboratory Information Manager to confirm the status of the driver update</strong>.</p>
</blockquote>
<ul>
<li><p>If they answer YES then the installation will proceed to update the interface to HL7 v2.5.1</p></li>
<li><p>If they answer NO then the installation will abort.</p></li>
</ul>
<p>![](laboratory-universal-interface-autorelease-version-1-installation-backout-and-ro/009.png) If the installation is aborted during the pre-install, the installation can be restarted using the Install Package(s) option.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Platform Installation and PreparationPlatform Installation and Preparation

## Download and Extract Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Log in to and download the software from Software Anonymous

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Installation Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Host File Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select OPTION NAME: <span class="mark">XPD MAIN</span> Kernel Installation & Distribution System

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: <span class="mark">installation</span>

Select Installation \<TEST ACCOUNT\> Option: <span class="mark">LOAD a Distribution</span>

Enter a Host File: VA4\$:\[LAB\]<span class="mark">LAB_AUTORELEASE_1_0.KID</span>

KIDS Distribution saved on May 12, 2016@14:42:42

Comment: LAB AUTO-RELEASE 1.0

This Distribution contains Transport Globals for the following Package(s):

Build LA\*5.2\*88 has been loaded before, here is when:

LA\*5.2\*88 Install Completed

was loaded on Jun 03, 2015@15:12:27

OK to continue with Load? NO// <span class="mark">YES</span>

Build LR\*5.2\*458 Install Completed

was loaded on Mar 16, 2016@11:59:03

OK to continue with Load? NO// <span class="mark">YES</span>

Distribution OK!

Want to Continue with Load? YES// <span class="mark">YES</span>

Loading Distribution...

## Environment Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Build LA\*5.2\*88 has an Environmental Check Routine

Want to RUN the Environment Check Routine? YES// <span class="mark">YES</span>

LA\*5.2\*88

Will first run the Environment Check Routine, LA88A

Sending transport global loaded alert to mail group G.LMI

--- Environment is okay ---

LR\*5.2\*458

Use INSTALL NAME: <span class="mark">LA\*5.2\*88</span> to install this Distribution.

Transport global for patch LA\*5.2\*88 loaded on May 12, 2016@14:50

## Select Account 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation \<TEST ACCOUNT\> Option: <span class="mark">VERIF</span>Y Checksums in Transport Global

Select INSTALL NAME: <span class="mark">LA\*5.2\*88</span> Loaded from Distribution 5/12/16@14:49:43

=\> LAB AUTO-RELEASE 1.0 ;Created on May 12, 2016@14:42:42

This Distribution was loaded on May 12, 2016@14:49:43 with header of

LAB AUTO-RELEASE 1.0 ;Created on May 12, 2016@14:42:42

It consisted of the following Install(s):

LA\*5.2\*88 LR\*5.2\*458

Want each Routine Listed with Checksums: Yes// <span class="mark">YES</span>

DEVICE: <span class="mark">HOME</span>// ;80;1000 VIRTUAL TELNET

PACKAGE: LA\*5.2\*88 May 12, 2016 2:50 pm PAGE 1

-------------------------------------------------------------------------------

LA7UCFG Calculated 137316017

LA7UCFG1 Calculated 29526912

LA7UIO1 Calculated 75417661

LA7UTILB Calculated 23365722

LA7VHL Calculated 38289473

LA7VHLU8 Calculated 60447079

LA7VHLU9 Calculated 33364706

LA7VIN Calculated 31997123

LA7VIN1 Calculated 65233143

LA7VIN2 Calculated 46992282

LA7VIN2A Calculated 34119950

LA7VIN4 Calculated 81803911

LA7VIN4A Calculated 23154184

LA7VIN5 Calculated 85555425

LA7VIN5A Calculated 34608326

LA7VORC Calculated 22779822

LA88 Calculated 37005513

LA88A Calculated 100793409

18 Routines checked, 0 failed.

PACKAGE: LR\*5.2\*458 May 12, 2016 2:50 pm PAGE 1

-------------------------------------------------------------------------------

LR458 Calculated 3643881

LRDIQ Calculated 6385366

LRGP2 Calculated 21346835

LRLISTPS Calculated 17691343

LRNIGHT Calculated 7575682

LRVER5 Calculated 148324560

LRVR3 Calculated 108418700

LRVRAR Calculated 69670046

LRVRARU Calculated 32878283

9 Routines checked, 0 failed.

## Backup Transport Global ![](laboratory-universal-interface-autorelease-version-1-installation-backout-and-ro/010.png)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation \<TEST ACCOUNT\> Option: <span class="mark">BACKup a Transport Global</span>

Select INSTALL NAME: <span class="mark">LA\*5.2\*88</span> Loaded from Distribution 5/12/16@14:49:

43

=\> LAB AUTO-RELEASE 1.0 ;Created on May 12, 2016@14:42:42

This Distribution was loaded on May 12, 2016@14:49:43 with header of

LAB AUTO-RELEASE 1.0 ;Created on May 12, 2016@14:42:42

It consisted of the following Install(s):

LA\*5.2\*88 LR\*5.2\*458

Subject: <span class="mark">Backup of LA\*5.2\*88 install on May 12, 2016</span>

Replace

Loading Routines for LA\*5.2\*88................

Routine LA88 is not on the disk...

Loading Routines for LR\*5.2\*458

Routine LR458 is not on the disk..........

Send mail to: <span class="mark">LRUSER,DRI</span>// LRUSER,DRI

Select basket to send to: <span class="mark">IN</span>//

And Send to:

## Install Package 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation \<TEST ACCOUNT\> Option: <span class="mark">INSTAll Package(s)</span>

Select INSTALL NAME: <span class="mark">LA\*5.2\*88</span> Loaded from Distribution 5/12/16@14:49:

43

=\> LAB AUTO-RELEASE 1.0 ;Created on May 12, 2016@14:42:42

This Distribution was loaded on May 12, 2016@14:49:43 with header of

LAB AUTO-RELEASE 1.0 ;Created on May 12, 2016@14:42:42

It consisted of the following Install(s):

LA\*5.2\*88 LR\*5.2\*458

Checking Install for Package LA\*5.2\*88

Will first run the Environment Check Routine, LA88A

## COTS Driver Inquiry and Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sending install started alert to mail group G.LMI

Is this site using the Lab UI V1.6 interface? No// <span class="mark">YES</span>

Has the Lab UI COTS driver been upgraded to send HL7 v2.5.1 messages? No// <span class="mark">YES</span>

Disabling Option \[LA7 MAIN MENU\]

Shutting down currently running Lab HL7 processes

Acquiring locks ...

Locks acquired.

N O T E: If you abort this installation

D RESTORE^LA88A from this console.

--- Environment is okay ---

<table>
<caption>Pre install questions for KIDS BuildPre install questions for KIDS Build</caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](laboratory-universal-interface-autorelease-version-1-installation-backout-and-ro/011.png) <strong>Please note:</strong></p>
<p>The person installing the KIDS build will be prompted with 1 or 2 pre-install questions requiring yes/no answers.</p>
<p>The first question is: <strong>Is this site using the Lab UI V1.6 interface?</strong></p>
<ul>
<li><p>If they answer <strong><mark>NO</mark></strong> then installation will proceed to update the interface to HL7 v2.5.1.</p></li>
<li><p>If they answer <strong><mark>YES</mark></strong> then a second question will be asked.</p></li>
</ul>
<p>The second question is: <strong>Has the Lab UI COTS driver been upgraded to send HL7 v2.5.1 messages?</strong></p>
<p>This normally involves a driver update on the COTS GIM system to allow the COTS system to send HL7 messages indicating either HL7 v2.2 or v2.5.1.</p>
<p>Contact your Laboratory Information Manager to confirm the status of the driver update.</p>
<ul>
<li><p>If they answer <strong><mark>YES</mark></strong> then the installation will proceed to update the interface to HL7 v2.5.1</p></li>
<li><p>If they answer <strong><mark>NO</mark></strong> then the installation will abort.</p></li>
</ul>
<p>![](laboratory-universal-interface-autorelease-version-1-installation-backout-and-ro/012.png)If the installation is aborted during the pre-install, the installation can be restarted using the Install Package(s) option.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Pre install questions for KIDS BuildPre install questions for KIDS Build

## Final Install Questions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Install Questions for LA\*5.2\*88

Incoming Files:

62.4 AUTO INSTRUMENT (Partial Definition)

> **NOTE:** You already have the 'AUTO INSTRUMENT' File.

62.485 LA7 MESSAGE LOG BULLETINS (including data)

> **NOTE:** You already have the 'LA7 MESSAGE LOG BULLETINS' File.

I will OVERWRITE your data with mine.

Checking Install for Package LR\*5.2\*458

Install Questions for LR\*5.2\*458

Incoming Files:

68.2 LOAD/WORK LIST (Partial Definition)

> **NOTE:** You already have the 'LOAD/WORK LIST' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? <span class="mark">NO</span>//

Want KIDS to INHIBIT LOGONs during the install? <span class="mark">NO</span>//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// <span class="mark">NO</span>

Enter the Device you want to print the Install messages.

Enter a '^' to abort the install.

DEVICE: <span class="mark">HOME</span>// VIRTUAL TELNET

LR\*5.2\*458



Enabling Option \[LA7 MAIN MENU\]

Be sure to restart the Lab Universal Interface Auto Download Job

\*\*\* Post install completed \*\*\*

Sending install completion alert to mail group G.LMI

Updating Routine file...

Updating KIDS files...

LR\*5.2\*458 Installed.

May 12, 2016@14:52:52

Not a production UCI

NO Install Message sent





100%  25 50 75 

Complete 

Install Completed

# Implementation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Steps To Enable Auto Release

## Set Auto Release Results System Wide parameter to enabled. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Auto Release Results System Wide \[LA7UI AUTO RELEASE MASTER\] parameter is a system wide switch that can quickly enable/disable the auto release process. When this parameter is set to Disabled, it will disable the auto release process on this system, and will override the settings in the Auto Instrument file. When enabled, this will enable the auto release process for instruments that are marked for auto release (via the Auto Release field… see step \#2 below).

Select Lab Universal Interface Menu Option: <span class="mark">UIS</span> Lab Universal Interface Setup

Select one of the following:

1 LA7 MESSAGE PARAMETER (#62.48)

2 AUTO INSTRUMENT (#62.4)

3 Auto Release System Parameter

4 Configuration Report (132 COL)

5 Holders of Lab keys

6 Ordering Provider Contact Parameter

Select which file to setup: <span class="mark">3</span> Auto Release System Parameter

Auto Release Results System Wide may be set for the following:

1 System SYS \[xxxxxxxxxxxxxxx\]

10 Package PKG \[LAB MESSAGING\]

Enter selection:<span class="mark">1</span> System xxxx.xxxx.xxx.xx.xxx

Setting Auto Release Results System Wide for System: xxxx.xxxx.xxx.xx.xxx

AUTO RELEASE RESULTS SYSTEM WIDE: YES (ENABLED)// <span class="mark">??</span>

This parameter is used to determine whether lab results are sent to the

auto release process.

AUTO RELEASE RESULTS SYSTEM WIDE: YES (ENABLED)// <span class="mark">?</span>

Do you want to Auto Release Results System Wide?.

Select one of the following:

0 NO (DISABLED)

1 YES (ENABLED)

AUTO RELEASE RESULTS SYSTEM WIDE: <span class="mark">YES</span> (ENABLED)//

## Enable the instrument(s) for Auto Release. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Auto Release field (#99) in the Auto Instrument file (#62.4) enables auto release on an instrument basis. It allows for different levels of granularity.

• Data Type: Set of Codes

0: NO

1: YES

2: AUTO VERIFY ONLY

3: USER RELEASE ONLY

• Description: If results received via this auto instrument entry can be associated with an external auto or user verification system then enable this field.

This field will be checked in conjunction with the auto release master switch parameter LA7UI AUTO RELEASE MASTER and the specific HL7 message containing the results to determine if the lab results should be processed by the Laboratory Auto Release process.

It can be configured at several levels of granularity.

0 - no auto release for this auto instrument

1 - yes instrument is enabled for auto and user verification

2 - yes however only process results that have been auto verified

> 3 - yes however only process results that have been user verified, no auto verification.

Select Lab Universal Interface Menu Option: <span class="mark">UIS</span> Lab Universal Interface Setup

Select one of the following:

1 LA7 MESSAGE PARAMETER (#62.48)

2 AUTO INSTRUMENT (#62.4)

3 Auto Release System Parameter

4 Configuration Report (132 COL)

5 Holders of Lab keys

6 Ordering Provider Contact Parameter

Select which file to setup: <span class="mark">2</span> AUTO INSTRUMENT (#62.4)

Select AUTO INSTRUMENT NAME: <span class="mark">ASTRA</span>

NAME: ASTRA//

LOAD/WORK LIST: AUTO RELEASE//

ENTRY for LAGEN ROUTINE: Accession cross-reference

//

CROSS LINKED BY: IDE//

MESSAGE CONFIGURATION: LA7UI1//

METHOD: ASTRA1234//

DEFAULT ACCESSION AREA: CHEMISTRY//

OVERLAY DATA: YES//

STORE REMARKS:

VENDOR CARD ADDRESS:

SEND TRAY/CUP LOCATION:

AUTO DOWNLOAD: YES//

AUTO RELEASE: YES// <span class="mark">??</span>

If results received via this auto instrument entry can be associated with an

external auto or user verification system then enable this field. This field

will be checked in conjunction with the auto release master switch parameter

LA7UI AUTO RELEASE MASTER and the specific HL7 message containing the

Results to determine if the lab results should be processed by the

Laboratory Auto Release process.

It can be configured at several levels of granularity.

0 - no auto release for this auto instrument

1 - yes instrument is enabled for auto and user verification

2 - yes however only process results that have been auto verified

3 - yes however only process results that have been user verified,no auto verification.

Choose from:

0 NO

1 YES

2 AUTO VERIFY ONLY

3 USER RELEASE ONLY

AUTO RELEASE: YES// <span class="mark">^</span>

Setting fields for auto download FILE BUILD ENTRY (#93) to: EN

FILE BUILD ROUTINE (#94) to: LA7UID ...Done

## Create Load/List profile for Auto Release 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Default Reference Laboratory (#2.3) should be set to the Institution that should be used as the performing and releasing lab for results released via the auto release process.

b\. The Auto Release field (#2.4) in the Load/Work List file (#68.2) is used to mark a profile as being used by the auto release process. There should only be one profile flagged per load list.

Data Type: Set of Codes

0: NO

1: YES

Description: If an auto release process to accept and file laboratory results from an external system using auto verification and/or human verification is being used then this field indicates to the auto release process which profile on this load list to use to process the lab results. There should only be one profile flagged per load list.

Select Supervisor menu Option:<span class="mark">Edit the default parameters Load/Work list.</span>Select LOAD/WORK LIST NAME: <span class="mark">AUTO RELEASE</span>

LOAD TRANSFORM: UNIVERSAL//

TYPE: POINT OF CARE//

CUPS PER TRAY: 0//

FULL TRAY'S ONLY: NO//

EXPAND PANELS ON PRINT: YES//

INITIAL SETUP:

VERIFY BY: ACCESSION//

SUPPRESS SEQUENCE \#: NO//

INCLUDE UNCOLLECTED ACCESSIONS: NO//

SHORT TEST LIST: NO//

WKLD METHOD: AUTO//

Select PROFILE: AUTO RELEASE//

ACCESSION AREA: CHEMISTRY//

UID VERIFICATION: ANY ACCESSION AREA//

STORE DUPLICATE COMMENTS: YES//

DEFAULT REFERENCE LABORATORY: VISN 2//

AUTO RELEASE: YES// <span class="mark">??</span>

If an auto release process to accept and file laboratory results from an

external system using auto verification and/or human verification is

being used then this field indicates to the auto release process which

profile on this load list to use to process the lab results.

There should only be one profile flagged per load list.

Choose from:

0 NO

1 YES

AUTO RELEASE: <span class="mark">YES</span>//

Select PROFILE:Select LOAD/WORK LIST NAME:

## Run Configuration Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Checks the Auto Release configuration and to assist in configuring the middleware.

Select Lab Universal Interface Menu Option: <span class="mark">Lab Universal Interface Setup</span>Select one of the following:

1 LA7 MESSAGE PARAMETER (#62.48)

2 AUTO INSTRUMENT (#62.4)

3 Auto Release System Parameter

4 Configuration Report (132 COL)

5 Holders of Lab keys

6 Ordering Provider Contact Parameter

Select which file to setup: <span class="mark">4</span> Configuration Report (132 COL)

Select AUTO INSTRUMENT NAME:<span class="mark">ASTRA</span>

DEVICE: HOME// 0;132;9999

## Create Lab users in GIM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To assist in adding lab users to the middleware system, the following option can be used to print out a list of users that hold a certain lab key.

Select Lab Universal Interface Menu Option:<span class="mark">Lab Universal Interface Setup</span>Select one of the following:

1 LA7 MESSAGE PARAMETER (#62.48)

2 AUTO INSTRUMENT (#62.4)

3 Auto Release System Parameter

4 Configuration Report (132 COL)

5 Holders of Lab keys

6 Ordering Provider Contact Parameter

Select which file to setup:<span class="mark">5</span> Holders of Lab keys

Select LAB SECURITY KEY NAME:<span class="mark">LRVERIFY</span>Select Another LAB SECURITY KEY NAME:All USERS? Yes// <span class="mark">YES</span>

DEVICE:

## Configure Ordering Provider contact information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When VistA Lab sends a Lab HL7 Order message to the middleware, it will send the ordering provider’s contact info in the HL7 message. To override the default settings, and customize at a system or user level which contact info is sent, the following option can be used.

Select Lab Universal Interface Menu Option:<span class="mark">Lab Universal Interface Setup</span>Select one of the following:

1 LA7 MESSAGE PARAMETER (#62.48)

2 AUTO INSTRUMENT (#62.4)

3 Auto Release System Parameter

4 Configuration Report (132 COL)

5 Holders of Lab keys

6 Ordering Provider Contact Parameter

Select which file to setup: <span class="mark">6</span> Ordering Provider Contact Parameter

Lab Ordering Provider Contact Info may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 System SYS \[xxx.xxx.xxx.xx.xxx\]

3 Package PKG \[AUTOMATED LAB INSTRUMENTS\]

Enter selection:<span class="mark">2</span> System xxx.xxx.xxx.xx.xxx

Setting Lab Ordering Provider Contact Info for System: xxx.xxx.xxx.xx.xxx

Select Sequence: <span class="mark">??</span>

![](laboratory-universal-interface-autorelease-version-1-installation-backout-and-ro/013.png) Contains the list of which contact info for the ordering provider to send in a Lab HL7 Order message from the user's corresponding entry in NEW PERSON file (#200).

It can be specified at the system or the individual user level. If specified at the user level it takes precedence and overrides the setting at the system level allowing specific users to have their own specific set of contacts to send.

The sequence specifies the order and info to check, maximum of 6 allowed.

Only the first 2 with a value will be placed in the message as the HL7 standard constrains the number of repetitions for this information at 2.

The value specifies which field from the person's entry in NEW PERSON

file (#200) to send in the message.

These are the fields currently available.

> Field \# Field Name Description

> .131 PHONE (HOME) This is the telephone number for the new person.

> .132 OFFICE PHONE This is the business/office telephone for the new person.

> .133 PHONE \#3 This is an alternate telephone number where the new person might also be reached.

> .134 PHONE \#4 This is another alternate telephone number where the new person might also be reached.

> .135 COMMERCIAL PHONE This is a commercial phone number.

> .136 FAX NUMBER This field holds a phone number for a FAX machine for this user. It needs to be a format that can be understood by a sending MODEM.

> .137 VOICE PAGER This field holds a phone number for an ANALOG PAGER that this person carries with them.

> .138 DIGITAL PAGER This field holds a phone number for a DIGITAL PAGER that this person carries with them.

> The parameter is distributed pre-configured at the package level as follows:

> Sequence Value

> -------- -----

> 1 OFFICE PHONE

> 2 DIGITAL PAGER

> 3 VOICE PAGER

> 4 PHONE \#3

> 5 PHONE \#4

> 6 PHONE (HOME)

> 7 COMMERICAL PHONE

> 8 FAX NUMBER

Select Sequence:

## Configure Proxy Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](laboratory-universal-interface-autorelease-version-1-installation-backout-and-ro/014.png)Local site personnel should assign DIVISIONS to the new proxy users, LRLAB,AUTO RELEASE and LRLAB,AUTO VERIFY, that corresponds to the performing laboratories that will utilize the auto release process.

• A new option was added to the Supervisor reports \[LRSUPER REPORTS\] menu.

Summary List (Patient) \[LRLISTPS\] Description: All results for a given patient for a given area for a given date. This report can serve as an 'audit trail' for a patient. Includes information on person placing order, person performing test, verifying person, and dates and times of specimen collection and test completion. The report can be printed in an "extended" form, which includes the above mentioned information plus the test results and associated units/normals/LOINC coding and performing lab.

# Back-out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out pertains to a return to the last known good operational state of the software and appropriate platform settings.

## Back-out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An activation software switch is supplied in the configuration to allow sites to activate or deactivate the Auto Verification functionality.

## Back-out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LIM or Lab assigned personnel has the authority to determine activation of the Auto Verification functions.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- N/A

## Back-out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Failed baseline testing
- Non recoverable software error

## Back-out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- None determined at this time

## Authority for Back-out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Chief of Pathology

## Back-out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The preferred method is listed below in Section 5.6.1 but this patch can be backed out by installing the backup routines created by following the installation instructions in Section 3.4 Backup Transport Global. This option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as Data Dictionaries (DDs) or templates.

### ![](laboratory-universal-interface-autorelease-version-1-installation-backout-and-ro/015.png) Preferred Method: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Set the Auto Verification option to inactive.

### Inactivate Auto Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Set Auto Release Results System Wide parameter to disabled.

The Auto Release Results System Wide \[LA7UI AUTO RELEASE MASTER\] parameter is a system wide switch that can quickly enable/disable the auto release process.

> ![](laboratory-universal-interface-autorelease-version-1-installation-backout-and-ro/016.png) <u>When this parameter is set to Disabled, it will disable the auto release process on this system, and will override the settings in the Auto Instrument file</u>.

> ![](laboratory-universal-interface-autorelease-version-1-installation-backout-and-ro/017.png)When Enabled, this will enable the auto release process for instruments that are marked for auto release (via the Auto Release field… see step \#2 below).

> Select Lab Universal Interface Menu Option: <span class="mark">UIS</span> Lab Universal Interface Setup

> Select one of the following:

> 1 LA7 MESSAGE PARAMETER (#62.48)

> 2 AUTO INSTRUMENT (#62.4)

> 3 Auto Release System Parameter

> 4 Configuration Report (132 COL)

> 5 Holders of Lab keys

> 6 Ordering Provider Contact Parameter

> Select which file to setup: <span class="mark">3</span> Auto Release System Parameter

> Auto Release Results System Wide may be set for the following:

> 1 System SYS \[xxxxxxxxxxxxxxx\]

> 10 Package PKG \[LAB MESSAGING\]

> Enter selection: <span class="mark">1</span> System xxxx.xxxx.xxx.xx.xxx

> Setting Auto Release Results System Wide for System: xxxx.xxxx.xxx.xx.xxx

> AUTO RELEASE RESULTS SYSTEM WIDE: YES (ENABLED)// <span class="mark">??</span>

> This parameter is used to determine whether lab results are sent to the

> auto release process.

> <span class="mark">AUTO RELEASE RESULTS SYSTEM WIDE: YES (ENABLED)// ?</span>

> Do you want to Auto Release Results System Wide?.

> Select one of the following:

> <span class="mark">0 NO (DISABLED)</span>

> 1 YES (ENABLED)

> AUTO RELEASE RESULTS SYSTEM WIDE: <span class="mark">YES</span> (ENABLED)//

## Disable the instrument(s) for Auto Release.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The Auto Release field (#99) in the Auto Instrument file (#62.4) enables auto release on an instrument basis. It allows for different levels of granularity.
    1.  Data Type: Set of Codes
        1.  0: NO
        2.  1: YES
        3.  2: AUTO VERIFY ONLY
        4.  3: USER RELEASE ONLY
    2.  Description: If results received via this auto instrument entry can be associated with an external auto or user verification system then enable this field.

> This field will be checked in conjunction with the auto release master switch parameter LA7UI AUTO RELEASE MASTER and the specific HL7 message containing the results to determine if the lab results should be processed by the Laboratory Auto Release process.

> It can be configured at several levels of granularity.

1.  0 - no auto release for this auto instrument
2.  1 - yes instrument is enabled for auto and user verification
3.  2 - yes however only process results that have been auto verified
4.  3 - yes however only process results that have been user verified, no auto verification.

> Select Lab Universal Interface Menu Option: <span class="mark">UIS</span> Lab Universal Interface Setup

> Select one of the following:

> 1 LA7 MESSAGE PARAMETER (#62.48)

> 2 AUTO INSTRUMENT (#62.4)

> 3 Auto Release System Parameter

> 4 Configuration Report (132 COL)

> 5 Holders of Lab keys

> 6 Ordering Provider Contact Parameter

> Select which file to setup: <span class="mark">2</span> AUTO INSTRUMENT (#62.4)

> Select AUTO INSTRUMENT NAME: <span class="mark">ASTRA</span>

> NAME: ASTRA//

> LOAD/WORK LIST: AUTO RELEASE//

> ENTRY for LAGEN ROUTINE: Accession cross-reference

> //

> CROSS LINKED BY: IDE//

> MESSAGE CONFIGURATION: LA7UI1//

> METHOD: ASTRA1234//

> DEFAULT ACCESSION AREA: CHEMISTRY//

> OVERLAY DATA: YES//

> STORE REMARKS:

> VENDOR CARD ADDRESS:

> SEND TRAY/CUP LOCATION:

> AUTO DOWNLOAD: YES//

> <span class="mark">AUTO RELEASE: YES// ??</span>

> If results received via this auto instrument entry can be

> associated with an external auto or user verification system

> then enable this field.

> This field will be checked in conjunction with the auto release

> master switch parameter LA7UI AUTO RELEASE MASTER and the

> specific HL7 message containing the results to determine if the

> lab results should be processed by the Laboratory Auto Release

> process.

> It can be configured at several levels of granularity.

> 0 - no auto release for this auto instrument

> 1 - yes instrument is enabled for auto and user verification

> 2 - yes however only process results that have been auto

> verified

> 3 - yes however only process results that have been user

> verified, no auto verification.

> Choose from:

> 0 NO

> 1 YES

> 2 AUTO VERIFY ONLY

> 3 USER RELEASE ONLY

> AUTO RELEASE: YES// <span class="mark">^</span>

> Setting fields for auto download FILE BUILD ENTRY (#93) to: EN

> FILE BUILD ROUTINE (#94) to: LA7UID ...Done

2.  Previous and expected functionality returned? Submit help ticket to developers who will assist in troubleshooting and resolution.
3.  If previous and expected functionality not functioning move to 6:
4.  <u>Alternate:</u> Restore the routines (below) using the PacKMan package containing routines in their preinstallation state . The backout procedure for globals, data dictionary, and other VistA components is more complex and will require issuance of a follow-on patch to ensure all components are properly removed. All software components must be restored to their previous state at once and in conjunction with restoration of data, and with a database cleanup process if necessary. Please contact the Product Development team for assistance if needed.

Select MailMan Menu Option: <span class="mark">Read/Manage Messages</span>

Select message reader: Classic// <span class="mark">\[ENTER\]</span>

Read mail in basket: IN// <span class="mark">\[ENTER\]</span> (2 messages)

Last message number: 2 Messages in basket: 2

Enter ??? for help.

IN Basket Message: 1// <span class="mark">?</span>

IN Basket, 2 messages (1-2)

\*=New/!=Priority.......Subject........................From..................

1\. Backup of LR\*5.2\*458 install on Sep 17, 2015 LRUSER,DRI

2\. INCONSISTENCY EDIT LRUSER,DRI

IN Basket Message: 1// <span class="mark">\[ENTER\]</span>

Subj: Backup of LR\*5.2\*458 install on Sep 17, 2015 \[#43764\] 19/17/15@13:13

4336 lines

From: LRUSER,DRI In 'IN' basket. Page 1

-------------------------------------------------------------------------

\$TXT PACKMAN BACKUP Created on Thursday, 9/17/15 at 13:13:09 by LRUSER,DRI at V

AHVRR.FO-ALBANY.MED.VA.GOV

\$ROU LRGP2 (PACKMAN_BACKUP)

LRGP2 ;DALOI/STAFF - COMMON PARTS TO INSTRUMENT GROUP VERIFY/CHECK ;05/08/15 1

6:54

;;5.2;LAB SERVICE;\*\*153,221,263,290,350,446,458\*\*;Sep 27, 1994;Build 3

;

Q

;

;

EXPLODE ; from LRGP1, LRVR, LRVRARU, LRVRPOCU

; LRORDR="P" indicates background POC interface, order type=POC

; LRAUTORELEASE indicates background Auto Release of Lab UI results.

;

N %,C,DIC,DIR,DIROUT,DIRUT,DUOUT,LREND,LRI,LRTEST,LRX,I,X,X1,Y

I \$G(LRORDR)'="P" K ^TMP("LR",\$J)

S LRCFL="",LRI=0 S:'\$D(LRNX) LRNX=0

F S LRI=\$O(^LRO(68.2,LRLL,10,LRPROF,1,LRI)) Q:LRI\<1 I \$D(^(LRI,0))#2 D

Enter RETURN to continue or '^' to exit: <span class="mark">^</span>

Enter message action (in IN basket): Ignore// <span class="mark">Xtract</span> PackMan

Select PackMan function: <span class="mark">6</span> INSTALL/CHECK MESSAGE

> **WARNING:** Installing this message will cause a permanent update of globals and routines.

Do you really want to do this? NO// <span class="mark">YES</span>

Routines are the only parts that are backed up. NO other parts

are backed up, not even globals. You may use the 'Summarize Message'

option of PackMan to see what parts the message contains.

Those parts that are not routines should be backed up separately

if they need to be preserved.

Shall I preserve the routines on disk in a separate back-up message? YES// <span class="mark">NO</span>

...

...

...

Select PackMan function: <span class="mark">\[ENTER\]</span>

Enter message action (in IN basket): Ignore// <span class="mark">\[ENTER\]</span>

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback pertains to data.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- None determined at this time

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Installation failed baseline testing

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- May require a downtime of only Laboratory package/users

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Chief of Pathology

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the chronological steps to follow to roll back to the previous state of the data and to migrate any new data to the previous version of the software.

1.  Need for rollback is highly unlikely, however if desired execute VistA Rollback procedures and SOP
2.  This will require Lab downtime and a reinstall of any previous KIDS versions
3.  The rollback procedure for Auto verification is complicated and may require a follow-on patch to fully rollback to the pre–Auto verification state. This is due to the numerous data dictionary repairs and global updates that will need to be backed out to their previous state, including their cross references, and HL7 changes. Please contact the Product Development team for assistance