---
title: Women's Health Version 1 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: WV
app_name: Womens Health
section: CLI
app_status: active
pkg_ns: WV
patch_ver: 1
patch_id: WV*1
group_key: "WV:WV:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - blockquote
  - table
  - contents
  - health
  - class
  - colspan
  - women
  - installation
  - package
  - software
page_count: 0
word_count: 2850
section_count: 25
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 1998
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Womens_Health/wv1_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Womens_Health/wv1_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=109"
---

> ![](women-s-health-version-1-installation-guide/001.png)

WOMEN’S HEALTH INSTALLATION GUIDE

> Version 1.0

> September 1998

## Department of Veterans Affairs Veterans Health Administration Office of Chief Information Officer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[Overview 1](#overview)

Women’s Health Installation 2

> Installation Guide

# Overview


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Department of Veterans Affairs Veterans Health Administration Office of Chief Information Officer](#department-of-veterans-affairs-veterans-health-administration-office-of-chief-information-officer)
- [Overview](#overview)
  - [The package namespace is WV.](#the-package-namespace-is-wv)
  - [The following describes the installation environment for Version 1 of the Women’s Health package:](#the-following-describes-the-installation-environment-for-version-1-of-the-womens-health-package)
  - [VA FileMan V. 21 or greater,](#va-fileman-v-21-or-greater)
  - [Kernel V. 8.0 or greater,](#kernel-v-80-or-greater)
  - [Kernel Toolkit V. 7.3 or greater,](#kernel-toolkit-v-73-or-greater)
  - [PIMS V. 5.3 or greater,](#pims-v-53-or-greater)
  - [Radiology/Nuclear Medicine V. 5.0 or greater (optional),](#radiologynuclear-medicine-v-50-or-greater-optional)
  - [MailMan V. 7.1 or greater.](#mailman-v-71-or-greater)
  - [If Radiology/Nuclear Medicine V. 5.0 and patch RA\5.0\2 are installed patient mammograms can be automatically entered into the Women’s Health database.](#if-radiologynuclear-medicine-v-50-and-patch-ra502-are-installed-patient-mammograms-can-be-automatically-entered-into-the-womens-health-database)
  - [The environment check routine will display a warning message if RA\5.0\2 is not installed. You may still continue with the package installation.](#the-environment-check-routine-will-display-a-warning-message-if-ra502-is-not-installed-you-may-still-continue-with-the-package-installation)
  - [Resource Requirements](#resource-requirements)
  - [The size of the table files that come with the package are insignificant. Data storage for the package is very roughly 2 megabytes per 1000 patients per year.](#the-size-of-the-table-files-that-come-with-the-package-are-insignificant-data-storage-for-the-package-is-very-roughly-2-megabytes-per-1000-patients-per-year)
  - [This is the first version of the VISTA Women’s Health package. Some VA facilities are running the Indian Health Service Women’s Health software (namespace is BW, file range is 9002086- 9002086.93). A pre-installation routine will check if the IHS Women’s Health software is installed, and if it is, the pre-installation process will copy the IHS data into the appropriate VISTA Women’s Health files. It will not change the IHS database.](#this-is-the-first-version-of-the-vista-womens-health-package-some-va-facilities-are-running-the-indian-health-service-womens-health-software-namespace-is-bw-file-range-is-9002086-900208693-a-pre-installation-routine-will-check-if-the-ihs-womens-health-software-is-installed-and-if-it-is-the-pre-installation-process-will-copy-the-ihs-data-into-the-appropriate-vista-womens-health-files-it-will-not-change-the-ihs-database)
  - [Before installation of the Women’s Health software:](#before-installation-of-the-womens-health-software)
  - [Coordinate the installation with the package ADPAC and/or Women’s Health Coordinator.](#coordinate-the-installation-with-the-package-adpac-andor-womens-health-coordinator)
  - [If the facility is using the IHS Women’s Health software, then the Women’s Health software should be installed when the IHS software is not being used.](#if-the-facility-is-using-the-ihs-womens-health-software-then-the-womens-health-software-should-be-installed-when-the-ihs-software-is-not-being-used)
  - [Set variables DUZ and DUZ(0)="@" by executing the following command D ^XUP.](#set-variables-duz-and-duz0-by-executing-the-following-command-d-xup)
  - [Place the ^WV global in an appropriate volume set on your system. Translate ^WV across all CPUs. This global must be placed with appropriate protection assignments (RWD for System, World, Group, and UCI).](#place-the-wv-global-in-an-appropriate-volume-set-on-your-system-translate-wv-across-all-cpus-this-global-must-be-placed-with-appropriate-protection-assignments-rwd-for-system-world-group-and-uci)
- [Example – Women’s Health Installation](#example-womens-health-installation)
  - [NOTE: The decision to rebuild menus is left up to each facility, ‘No’ was used for this example. Please follow whatever policy your facility uses for rebuilding menus when installing software.](#note-the-decision-to-rebuild-menus-is-left-up-to-each-facility-no-was-used-for-this-example-please-follow-whatever-policy-your-facility-uses-for-rebuilding-menus-when-installing-software)
- [Post Initialization Tasks](#post-initialization-tasks)
  - [There are no routines recommended for mapping.](#there-are-no-routines-recommended-for-mapping)
  - [The following globals should be journaled and appear in the UCI translation table for each CPU: WV\](#the-following-globals-should-be-journaled-and-appear-in-the-uci-translation-table-for-each-cpu-wv)
  - [Move the WV\ routines onto all appropriate systems, if applicable.](#move-the-wv-routines-onto-all-appropriate-systems-if-applicable)
  - [For information on assigning menus, refer to Chapter 1 Implementation and Maintenance of the Women’s Health User Manual.](#for-information-on-assigning-menus-refer-to-chapter-1-implementation-and-maintenance-of-the-womens-health-user-manual)
- [File Security](#file-security)

## The package namespace is WV.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## The following describes the installation environment for Version 1 of the Women’s Health package:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VA FileMan V. 21 or greater,

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Kernel V. 8.0 or greater,

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Kernel Toolkit V. 7.3 or greater,

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## PIMS V. 5.3 or greater,

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Radiology/Nuclear Medicine V. 5.0 or greater (optional),

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## MailMan V. 7.1 or greater.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## If Radiology/Nuclear Medicine V. 5.0 and patch RA\*5.0\*2 are installed patient mammograms can be automatically entered into the Women’s Health database.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## The environment check routine will display a warning message if RA\*5.0\*2 is not installed. You may still continue with the package installation.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## The size of the table files that come with the package are insignificant. Data storage for the package is very roughly 2 megabytes per 1000 patients per year.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installation Guide

> Women’s Health V. 1 Installation

## This is the first version of the V*IST*A Women’s Health package. Some VA facilities are running the Indian Health Service Women’s Health software (namespace is BW, file range is 9002086- 9002086.93). A pre-installation routine will check if the IHS Women’s Health software is installed, and if it is, the pre-installation process will copy the IHS data into the appropriate V*IST*A Women’s Health files. It will not change the IHS database.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Before installation of the Women’s Health software:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Coordinate the installation with the package ADPAC and/or Women’s Health Coordinator.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## If the facility is using the IHS Women’s Health software, then the Women’s Health software should be installed when the IHS software is not being used.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Set variables DUZ and DUZ(0)="@" by executing the following command D ^XUP.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Place the ^WV global in an appropriate volume set on your system. Translate ^WV across all CPUs. This global must be placed with appropriate protection assignments (RWD for System, World, Group, and UCI).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 2 Women’s Health V. 1.0 September 1998

Installation Guide

# Example – Women’s Health Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \> D ^XUP

> Setting up programmer environment Terminal Type set to: C-VT320

> Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

> Edits and Distribution ... Utilities ...

> Installation ...

> Select Kernel Installation & Distribution System Option: INSTALLATION

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Select Installation Option: 1 Load a Distribution Enter a Host File: WV1.KID

> KIDS Distribution saved on Jul 06, 1998@10:34:52 Comment: WOMEN’S HEALTH V1.0

> This Distribution contains Transport Globals for the following Package(s): WOMEN’S HEALTH 1.0

> Want to Continue with Load? YES// \<RET\>

> Loading Distribution...

> WOMEN’S HEALTH 1.0

> Use INSTALL NAME: WOMEN’S HEALTH 1.0 to install this Distribution.

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Select Installation Option: 6 Install Package(s)

> Select INSTALL NAME: WOMEN’S HEALTH 1.0 Loaded from Distribution 7/6/98@10:38:25

> =\> WOMEN’S HEALTH V1.0 ;Created on Jul 06, 1998@10:34:52

> This Distribution was loaded on Jul 06, 1998@10:38:25 with header of WOMEN’S HEALTH V1.0 ;Created on Jul 06, 1998@10:34:52

> September 1998 Women’s Health V. 1.0 3

> Installation Guide

> It consisted of the following Install(s):

> WOMEN’S HEALTH 1.0

> WOMEN’S HEALTH 1.0

> Will first run the Environment Check Routine, WVENV

> NOTE: The Radiology/Nuclear Medicine v5.0 package has an event point (included with RA\*5.0\*2) which will notify the Women’s Health package whenever a radiology report is verified

> for a mammogram. This event point allows mammograms to be automatically entered into the Women’s Health Procedure file (#790.1).

> To use this functionality install RA\*5.0\*2. Please continue with this package installation.

> Install Questions for WOMEN’S HEALTH 1.0 Incoming Files:

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 12%" />
<col style="width: 5%" />
<col style="width: 54%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="13"></th>
<th><blockquote>
<p>790</p>
</blockquote></th>
<th>WV</th>
<th><blockquote>
<p>PATIENT</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>790.01</p>
</blockquote></th>
<th>WV</th>
<th><blockquote>
<p>CASE MANAGER</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>790.02</p>
</blockquote></th>
<th>WV</th>
<th><blockquote>
<p>SITE PARAMETER</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>790.03</p>
</blockquote></th>
<th>WV</th>
<th><blockquote>
<p>PAP REGIMEN (including data)</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>790.04</p>
</blockquote></th>
<th>WV</th>
<th><blockquote>
<p>PAP REGIMEN LOG</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>790.05</p>
</blockquote></th>
<th>WV</th>
<th><blockquote>
<p>PREGNANCY LOG</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>790.07</p>
</blockquote></th>
<th>WV</th>
<th><blockquote>
<p>REFERRAL SOURCE</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>790.1</p>
</blockquote></th>
<th>WV</th>
<th><blockquote>
<p>PROCEDURE</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>790.2</p>
</blockquote></th>
<th>WV</th>
<th><blockquote>
<p>PROCEDURE TYPE (including data)</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>790.3</p>
</blockquote></th>
<th>WV</th>
<th><blockquote>
<p>REFUSALS</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>790.31</p>
</blockquote></th>
<th>WV</th>
<th><blockquote>
<p>RESULTS/DIAGNOSIS (including data)</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>790.32</p>
</blockquote></th>
<th>WV</th>
<th><blockquote>
<p>DIAGNOSTIC CODE TRANSLATION</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>790.4</p>
</blockquote></th>
<th>WV</th>
<th><blockquote>
<p>NOTIFICATION</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>790.403</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>NOTIFICATION TYPE (including data)</p>
<p>Women’s Health V. 1.0</p>
</blockquote></td>
<td><blockquote>
<p>September 1998</p>
</blockquote></td>
</tr>
</tbody>
</table>

Installation Guide

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 7%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>790.404</p>
</blockquote></th>
<th>WV</th>
<th><blockquote>
<p>NOTIFICATION PURPOSE (including data)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>790.405</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>NOTIFICATION OUTCOME (including data)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.5</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>CERVICAL TX NEED (including data)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.51</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>BREAST TX NEED (including data)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.6</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>LETTER (including data)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.71</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>SNAPSHOT REPORTS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.72</p>
</blockquote></td>
<td>WV</td>
<td><blockquote>
<p>AGE RANGE DEFAULT</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// \<RET\> TELNET

> Install Started for WOMEN’S HEALTH 1.0 :

> Jul 06, 1998@10:39:02

> Installing Routines:

> Jul 06, 1998@10:39:04

> Running Pre-Install Routine: ^WVPRE Installing Data Dictionaries:

> Jul 06, 1998@10:39:09

> Installing Data: .

> Jul 06, 1998@10:39:11

> Installing PACKAGE COMPONENTS: Installing SECURITY KEY Installing FUNCTION

> Installing PRINT TEMPLATE Installing FORM

> Installing OPTION

> Jul 06, 1998@10:39:20

> Running Post-Install Routine: ^WVPOST.

> September 1998 Women’s Health V. 1.0 5

> Installation Guide

> Updating Routine file... Updating KIDS files...

> WOMEN’S HEALTH 1.0 Installed.

> Jul 06, 1998@10:39:22

> Install Message sent \#13038

> An Option(s) has been added by this build.

> Electing to rebuild menus now is highly recommended. Do you want to rebuild Menu’s now? Y// NO

## NOTE: The decision to rebuild menus is left up to each facility, ‘No’ was used for this example. Please follow whatever policy your facility uses for rebuilding menus when installing software.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 6 Women’s Health V. 1.0 September 1998

Installation Guide

# Post Initialization Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## There are no routines recommended for mapping.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## The following globals should be journaled and appear in the UCI translation table for each CPU: WV\*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Move the WV\* routines onto all appropriate systems, if applicable.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## For information on assigning menus, refer to Chapter 1 Implementation and Maintenance of the Women’s Health User Manual.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 25%" />
<col style="width: 19%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>NUMBER</p>
</blockquote></th>
<th><blockquote>
<p>NAME</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>GLOBAL NAME</p>
</blockquote></th>
<th><blockquote>
<p>DD ACC</p>
</blockquote></th>
<th><blockquote>
<p>RD ACC</p>
</blockquote></th>
<th><blockquote>
<p>WR ACC</p>
</blockquote></th>
<th><blockquote>
<p>DEL ACC</p>
</blockquote></th>
<th><blockquote>
<p>LAY ACC</p>
</blockquote></th>
<th><blockquote>
<p>AUDIT</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>790</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>PATIENT</td>
<td><blockquote>
<p>^WV(790,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.01</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>CASE MANAGER</td>
<td><blockquote>
<p>^WV(790.01,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.02</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>SITE PARAMETER</td>
<td><blockquote>
<p>^WV(790.02,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.03</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>PAP REGIMEN</td>
<td><blockquote>
<p>^WV(790.03,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.04</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>PAP REGIMEN LOG</td>
<td><blockquote>
<p>^WV(790.04,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.05</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>PREGNANCY LOG</td>
<td><blockquote>
<p>^WV(790.05,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.07</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>REFERRAL SOURCE</td>
<td><blockquote>
<p>^WV(790.07,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.1</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>PROCEDURE</td>
<td><blockquote>
<p>^WV(790.1,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.2</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>PROCEDURE TYPE</td>
<td><blockquote>
<p>^WV(790.2,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.3</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>REFUSALS</td>
<td><blockquote>
<p>^WV(790.3,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.31</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>RESULTS/DIAGNOSIS</td>
<td><blockquote>
<p>^WV(790.31,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.32</p>
</blockquote></td>
<td><blockquote>
<p>WV</p>
</blockquote></td>
<td>DIAGNOSTIC CODE</td>
<td></td>
<td></td>
<td colspan="5"></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>TRANSLATION</p>
</blockquote></td>
<td><blockquote>
<p>^WV(790.32,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.4</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>WV NOTIFICATION</p>
</blockquote></td>
<td><blockquote>
<p>^WV(790.4,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.403</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>WV NOTIFICATIN TYPE</p>
</blockquote></td>
<td><blockquote>
<p>^WV(790.403,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.404</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>WV NOTIFICATION PURPOSE</p>
</blockquote></td>
<td><blockquote>
<p>^WV(790.404,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.405</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>WV NOTIFICATION OUTCOME</p>
</blockquote></td>
<td><blockquote>
<p>^WV(790.405,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.5</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>WV CERVICAL TX NEED</p>
</blockquote></td>
<td><blockquote>
<p>^WV(790.5,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.51</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>WV BREAST TX NEED</p>
</blockquote></td>
<td><blockquote>
<p>^WV(790.51,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.6</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>WV LETTER</p>
</blockquote></td>
<td><blockquote>
<p>^WV(790.6,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>790.71</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>WV SNAPSHOT REPORTS</p>
</blockquote></td>
<td><blockquote>
<p>^WV(790.71,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
<tr class="even">
<td><blockquote>
<p>790.72</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>WV AGE RANGE DEFAULT</p>
</blockquote></td>
<td><blockquote>
<p>^WV(790.72,</p>
</blockquote></td>
<td>@</td>
<td colspan="5">@</td>
</tr>
</tbody>
</table>

> September 1998 Women’s Health V. 1.0 7

> Installation Guide

> 8 Women’s Health V. 1.0 September 1998