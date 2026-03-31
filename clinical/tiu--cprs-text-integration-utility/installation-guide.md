---
title: TIU/ASU Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: plain
doc_subject: TIU/ASU
app_code: TIU
app_name: "CPRS: Text Integration Utility"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: TEXT INTEGRATION UTILITIES (TIU)&AUTHORIZATION/SUBSCRIPTION UTILITY (ASU)INSTALLATION GUIDE
audience: 
keywords: 
  - strong
  - class
  - table
  - template
  - install
  - filed
  - notes
  - installation
  - print
  - style
page_count: 0
word_count: 6774
section_count: 6
table_count: 20
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Text_Integration_Utility_(TIU)/tiuig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Text_Integration_Utility_(TIU)/tiuig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=65"
---

![](tiu-asu-installation-guide/001.png)

TEXT INTEGRATION UTILITIES (TIU)&AUTHORIZATION/SUBSCRIPTION UTILITY (ASU)INSTALLATION GUIDE

July 1997

Technical Service

Computerized Patient Record System Product Line

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Patch TIU\*1\*234 Disallow general edit of signed docs | [Page 33](#e3r) | Jan 2008 | <span class="mark">REDACTED</span> |
|--------------------------------------------------------|-----------------|----------|------------------------------------|
| Patch TIU\*1\*220 Edit expected cosigner               | [Page 33](#e3r) | Dec 2006 | <span class="mark">REDACTED</span> |
|                                                        |                 |          |                                    |
|                                                        |                 |          |                                    |
|                                                        |                 |          |                                    |
|                                                        |                 |          |                                    |
|                                                        |                 |          |                                    |

Table of Contents

Introduction [1](#introduction)

Preliminary Considerations [2](#preliminary-considerations)

Namespaces [2](#namespaces)

Software Requirements [2](#software-requirements)

Resource Requirements [2](#resource-requirements)

Global Instructions [3](#global-instructions)

TIU and ASU Files [4](#tiu-and-asu-files)

Routines Installed [4](#routines-installed)

Post-Installation Routine [5](#post-installation-routine)

Installation [7](#installation)

Back up all systems [7](#back-up-all-systems)

Estimated Installation Time [7](#estimated-installation-time)

Install TIU/ASU first in a training or test account [7](#install-tiuasu-first-in-a-training-or-test-account)

Load the distribution for ASU V1.0 [8](#load-the-distribution-for-asu-v1.0)

Verify Checksums in the transport global [9](#verify-checksums-in-the-transport-global)

Install ASU V1.0 [10](#install-asu-v1.0)

Load the TIU distribution [14](#load-the-tiu-distribution)

Verify Checksums in the transport global [15](#verify-checksums-in-the-transport-global-1)

(optional) Print, Compare, and Backup Transport Globals [15](#optional-print-compare-and-backup-transport-globals)

Install TIU [16](#install-tiu)

Print results of the installation process [17](#print-results-of-the-installation-process)

Verify that routines were moved to appropriate systems [22](#verify-that-tiu-usr-and-supporting-routines-were-moved-to-appropriate-systems)

(Optional) Print a list of package components [22](#optional-print-a-list-of-package-components)

Create a new Resource Device [23](#create-a-new-resource-device)

See the TIU Implementation Guide for set-up instructions [24](#see-the-tiu-implementation-guide-for-set-up-instructions)

Release Notes [25](#release-notes)

Features of TIU [25](#features-of-tiu)

Changes to Progress Notes and Discharge Summary [26](#changes-to-progress-notes-and-discharge-summary)

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
- [# Introduction](#introduction)
  - [Preliminary Considerations](#preliminary-considerations)
  - [SRCFULL or CODEFUL Errors on DSM Systems](#srcfull-or-codeful-errors-on-dsm-systems)
- [Installation](#installation)
    - [<table>](#table)
    - [### TIU Installation Print-out Example](#tiu-installation-print-out-example)
- [# Release Notes](#release-notes)
  - [Features of TIU](#features-of-tiu)
  - [Changes to Progress Notes and Discharge Summary](#changes-to-progress-notes-and-discharge-summary)
    - [Technical Changes](#technical-changes)
    - [Progress Notes](#progress-notes)
    - [Discharge Summary](#discharge-summary)
Purpose of Package:
Text Integration Utilities (TIU) is a collection of software tools that manage clinical documents in a standardized way. They allow clinicians and other users to view, enter, edit, sign, and print different kinds of documents from a single program.
The initial release of TIU includes Discharge Summary and Progress Notes. TIU replaces the previous versions of these DHCP packages and incorporates all of their functionality.
Intended Audience for this Manual:
The *Text Integration Utilities Installation Guide* provides VAMC IRM Services with the technical information necessary to properly install the TIU package.
See the *TIU Implementation Guide* for pre-installation steps and post-installation set-up instructions
Related Manuals
*Text Integration Utilities (TIU) Implementation and Training GuideText Integration Utilities (TIU) Technical ManualText Integration Utilities (TIU) Clinical Coordinator & User ManualText Integration Utilities (TIU) Quick Reference GuideAuthorization/Subscription (ASU) Technical Manual*

## Preliminary Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="section-1"></h2></td>
<td><h2 id="namespaces">Namespaces</h2></td>
</tr>
</tbody>
</table>

Text Integration Utilities : TIU

Authorization/Subscription Utility: USR

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="section-2"></h2></td>
<td><h2 id="software-requirements">Software Requirements</h2></td>
</tr>
</tbody>
</table>

The following packages and patches must be installed before TIU:

<table>
<colgroup>
<col style="width: 65%" />
<col style="width: 34%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Package</strong></td>
<td><strong>Minimum Version</strong></td>
</tr>
<tr class="even">
<td>Adverse Reaction Tracking (ART)</td>
<td>4.0</td>
</tr>
<tr class="odd">
<td>Health Summary (recommended)</td>
<td>2.7</td>
</tr>
<tr class="even">
<td>Incomplete Record Tracking (IRT), if you plan to interface with it</td>
<td>5.3</td>
</tr>
<tr class="odd">
<td>Kernel</td>
<td>8.0</td>
</tr>
<tr class="even">
<td>Patient Care Encounter (PCE)</td>
<td>1.0</td>
</tr>
<tr class="odd">
<td>Patient Information Management System (PIMS)</td>
<td>5.3</td>
</tr>
<tr class="even">
<td>VA FileMan</td>
<td>21</td>
</tr>
<tr class="odd">
<td>Visit Tracking</td>
<td>2.0</td>
</tr>
<tr class="even">
<td></td>
<td><strong>Patch</strong></td>
</tr>
<tr class="odd">
<td>Incomplete Record Tracking (IRT)</td>
<td>DG*5.3*112</td>
</tr>
<tr class="even">
<td>List Manager</td>
<td>VALM *1*1</td>
</tr>
<tr class="odd">
<td>Order Entry/Results Reporting (OE/RR)</td>
<td>OR*2.5*51</td>
</tr>
<tr class="even">
<td>Progress Notes</td>
<td><p>GMRP*2.5*44</p>
<p>GMRP*2.5*47</p></td>
</tr>
<tr class="odd">
<td>XQOR (Unwinder)</td>
<td>XU*8.0*56</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="section-3"></h2></td>
<td><h2 id="resource-requirements">Resource Requirements</h2></td>
</tr>
</tbody>
</table>

Be sure to place ^TIU on a database volume with LOTS of space to grow. You can calculate the disk space required using the following formula:

|                   |                           |
|-------------------|---------------------------|
| Component     | Resource Requirements |
| Progress Notes    | 1.6K per Note             |
| Discharge Summary | 8.1K per Summary          |
| Visit Tracking    | 100 bytes per record      |

Total disk requirement=(# of Progress Notes X 1.5KB/note) + (# of Discharge Summaries X 8KB/summary)+(# visits X 100 bytes).

> **NOTE:** You will also see growth in the encounter file.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="section-4"></h2></td>
<td><h2 id="global-instructions">Global Instructions</h2></td>
</tr>
</tbody>
</table>

The file list on the next page shows the globals that are installed.

- *Alpha cluster configuration (DSM)*: The TIU global ^TIU and ASU global ^USR must be placed and protected on the proper volume set using the %GLOMAN utility.
- *OPEN M*: Use the GUI system utility to create and change the globals and their attributes.
- On DSM/VMS and OPEN M/NT systems, the globals should be defined as follows for the install:

|            |            |           |           |              |
|------------|------------|-----------|-----------|--------------|
|            | System | World | Group | UCI/USER |
| DSM    | RWP        | RWP       | RWP       | RWP          |
| OPEN M | RWD        | RWD       | RWD       | RWD          |

Journaling

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 26%" />
<col style="width: 36%" />
<col style="width: 19%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>System</strong></td>
<td><strong>During Installation</strong></td>
<td><strong>During Conversion</strong></td>
<td><strong>After Conversion</strong></td>
</tr>
<tr class="even">
<td><p><strong>DSM/VMS</strong></p>
<p><strong>OPEN M/NT</strong></p>
<p><strong>MSM/NT</strong></p></td>
<td>Leave journaling enabled</td>
<td>Disable journaling <em>only</em> on the ^TIU global. Leave journaling enabled on all other globals, including ^GMR</td>
<td>Re-enable</td>
</tr>
</tbody>
</table>

> **NOTE:** Sites using Kernel Part 3 (optional) must set user access to these files. See the *TIU Security Guide* (in the *TIU Technical Manual*) for specific information.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="section-5"></h2></td>
<td><h2 id="tiu-and-asu-files">TIU and ASU Files</h2></td>
</tr>
</tbody>
</table>

TIU Files

|                                 |             |              |          |
|---------------------------------|-------------|--------------|----------|
| File Name                   | File \# | Global   | Data |
| TIU Document                    | 8925        | ^TIU(8925    |          |
| TIU Document Definition         | 8925.1      | ^TIU(8925.1  | Yes      |
| TIU Upload Buffer               | 8925.2      | ^TIU(8925.2  |          |
| TIU Upload Error Definition     | 8925.3      | ^TIU(8925.3  | Yes      |
| TIU Upload Log                  | 8925.4      | ^TIU(8925.4  |          |
| TIU Audit Trail                 | 8925.5      | ^TIU(8925.5  |          |
| TIU Status                      | 8925.6      | ^TIU(8925.6  | Yes      |
| TIU Multiple Signature          | 8925.7      | ^TIU(8925.7  |          |
| TIU Search Categories           | 8925.8      | ^TIU(8925.8  | Yes      |
| TIU Problem Link                | 8925.9      | ^TIU(8925.9  |          |
| TIU External Data Link File     | 8925.91     | ^TIU(8925.91 |          |
| TIU Print Parameters            | 8925.93     | ^TIU(8925.93 |          |
| TIU Division Print Parameters   | 8925.94     | ^TIU(8925.94 |          |
| TIU Document Parameters         | 8925.95     | ^TIU(8925.95 | Yes      |
| TIU Conversions                 | 8925.97     | ^TIU(8925.97 | Yes      |
| TIU Personal Document Type List | 8925.98     | ^TIU(8925.98 |          |
| TIU Parameters                  | 8925.99     | ^TIU(8925.99 |          |
| TIU Personal Preferences        | 8926        | ^TIU(8926    |          |

ASU Files

|                          |             |             |          |     |
|--------------------------|-------------|-------------|----------|-----|
| File Name            | File \# | Global  | Data |     |
| USR CLASS                | 8930        | ^USR(8930   |          | Yes |
| USR AUTHORIZATION/SUBSCR | 8930.1      | ^USR(8930.1 |          | Yes |
| USR ROLE                 | 8930.2      | ^USR(8930.2 |          | Yes |
| USR CLASS MEMBERSHIP     | 8930.3      | ^USR(8930.3 |          |     |
| USR SEARCH CATEGORIES    | 8930.4      | ^USR(8930.4 |          | Yes |
| USR RECORD STATUS        | 8930.6      | ^USR(8930.6 |          | Yes |
| USR ACTION               | 8930.8      | ^USR(8930.8 |          | Yes |

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="section-6"></h2></td>
<td><h2 id="routines-installed">Routines Installed</h2></td>
</tr>
</tbody>
</table>

ASU Routines

USRAEDT USRCLASS USRCLST USRECLST USRIL USRL USRLA USRLM USRLS USRM USRMEMBR USRMLST USRNTEG USRPOST USRPRE USRPROV USRRUL USRRUL1 USRRULA USRULST USRUM USRUMMBR

TIU Routines

TIUADD TIUALRT TIUAPIOK TIUAUDIT TIUBPEDT

TIUBR TIUBRWS TIUCHLP TIUCNSLT TIUDD TIUDD0 TIUDD01 TIUDD8 TIUDD98 TIUDEV TIUDIRH TIUDIRT TIUDPEDT TIUDSCNV TIUEDI1 TIUEDI2 TIUEDIH TIUEDIM TIUEDIT TIUEDITR TIUELST TIUENV TIUEPRNT TIUFA TIUFA1

TIUFC TIUFC1 TIUFD TIUFD1 TIUFD2 TIUFD3 TIUFD4 TIUFH TIUFH1 TIUFHA TIUFHA1 TIUFHA2 TIUFHA3 TIUFHA4 TIUFHA5 TIUFHA6 TIUFHLP TIUFHLP1 TIUFJ TIUFL TIUFL1 TIUFLA TIUFLA1 TIUFLD TIUFLD1 TIUFLF TIUFLF1 TIUFLF2 TIUFLF3 TIUFLF4 TIUFLF5 TIUFLF6 TIUFLF7 TIUFLF8 TIUFLJ TIUFLJ1 TIUFLLM TIUFLLM1 TIUFLLM2 TIUFLLM3 TIUFLT TIUFLX TIUFPR TIUFT TIUFT1

TIUFX TIUFXHL1 TIUFXHLX TIUHELP TIUIL TIUIL1 TIUIL10 TIUIL2 TIUIL3 TIUIL4 TIUIL5 TIUIL6 TIUIL7 TIUIL8 TIUIL9

TIULA TIULA1 TIULA2 TIULA3 TIULA4 TIULAB TIULADR TIULAPI TIULAPIC TIULAPIS

TIULC TIULC1 TIULD TIULE TIULEXP

TIULF TIULG TIULIP TIULM TIULMED

TIULO TIULO1 TIULP TIULP1 TIULQ TIULQ2 TIULS TIULS1 TIULV TIULX TIUMOVE TIUNTEG TIUNTEG0 TIUPD TIUPEDSP TIUPEFIX TIUPEVN1 TIUPEVNT TIUPL TIUPLST TIUPNAPI TIUPNCV TIUPNCV1 TIUPNCV2 TIUPNCV3 TIUPNCV4 TIUPNCV5 TIUPNCV6 TIUPNCV7 TIUPNCV8 TIUPNCVX TIUPOST TIUPRD TIUPRDS TIUPRDS1 TIUPRDS2 TIUPREF TIUPRPN TIUPRPN1 TIUPRPN2 TIUPRPN3 TIUPRPN4 TIUPRPN5 TIUPRPN6 TIUPRPN7 TIUPUTC TIUPUTD TIUPUTPN TIUPUTU TIUPXAP1 TIUPXAP2 TIUPXAPC TIUPXAPI TIUPXAPS TIUR

TIURA TIURA1 TIURB TIURB1 TIURC

TIURD TIURD1 TIURE TIURH TIURL

TIURM TIURMH TIUROR TIURORL TIURP TIURPN TIURPTTL TIURS TIURS1 TIURT TIURTITH TIURTITL TIUSRV TIUSRV1 TIUSRVA TIUSRVD TIUSRVE TIUSRVG TIUSRVL TIUSRVL1 TIUSRVLC TIUSRVLL TIUSRVLO TIUSRVLV TIUSRVP TIUSRVP1 TIUSRVR TIUSRVR1 TIUT TIUTHLP TIUTSK TIUU TIUUPEDT TIUUPLD TIUVISIT TIUVSIT

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="section-7"></h2></td>
<td><h2 id="post-installation-routine">Post-Installation Routine</h2></td>
</tr>
</tbody>
</table>

A post-installation routine (^USRPOST), part of the KIDS build, installs a number of list templates used by ASU to create User Classes.

## SRCFULL or CODEFUL Errors on DSM Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On DSM Systems, the compilation of the Input Template TIU ENTER/EDIT PROGRESS NOTE during the KIDS Installation of TIU may result in a MUMPS error, \<SRCFULL\>, when VA FileMan builds the resulting routines in the TIUEPN\* namespace. If this occurs, try invoking DSM with a larger SOURCE BUFFER size (e.g., 30000), and Restart the Kids Installation, which should then run to completion. This results from the excessive size (i.e., ~10,500 bytes) to which ^DIEZ compiles the routines for this particular Input Template.

> **NOTE:** You don’t need to modify the default source buffer or partition size using ^SYSGEN; temporarily increasing the source buffer size for the partition in which TIU is being installed should be sufficient.

You may observe another MUMPS error, \<CODEFUL\> in the TIUEPN routines, when users attempt to enter Progress Notes. If this should occur, try using ^DIEZ to re-compile the input template, as shown below:

\> D ^DIEZ

Maximum routine size on this computer (in bytes):(2400-5000):5000//4000

Select INPUT TEMPLATE: TIU ENTER/EDIT PROGRESS NOTE FILE \#8925^TIUEPN

Input Template currently compiled under namespace ^TIUEPN.

UNCOMPILE the Input Template? NO// \<Enter\>

Routine Name: TIUEPN// \<Enter\>

Note that ^TIUEPN is already in the routine directory.

Should the compilation run now? y YES

Compiling TIU ENTER/EDIT PROGRESS NOTE Input Template of File 8925..

'TIUEPN' ROUTINE FILED..

'TIUEPN1' ROUTINE FILED....

'TIUEPN2' ROUTINE FILED..

'TIUEPN3' ROUTINE FILED...

'TIUEPN4' ROUTINE FILED...

'TIUEPN5' ROUTINE FILED...

'TIUEPN6' ROUTINE FILED...

'TIUEPN7' ROUTINE FILED...

'TIUEPN8' ROUTINE FILED....

'TIUEPN9' ROUTINE FILED...

'TIUEPN10' ROUTINE FILED.

\>

If the \<CODEFUL\> error persists, use ^DIEZ to “uncompile” the template:

\> D ^DIEZ

Maximum routine size on this computer (in bytes):(2400-5000):5000//4000

Select INPUT TEMPLATE: TIU ENTER/EDIT PROGRESS NOTE FILE \#8925^TIUEPN

Input Template currently compiled under namespace ^TIUEPN.

UNCOMPILE the Input Template? NO// \<ENTER\>

Input Template is now uncompiled.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="section-8">1</h2></td>
<td><h2 id="back-up-all-systems">Back up all systems</h2></td>
</tr>
</tbody>
</table>

TIU’s direct impact on V*IST*A functions outside of its namespace are minimal, but if you can, it’s probably wise to do a full back-up within one day of an installation of this magnitude. Users can remain on the system. It is not necessary to disable log-ins during this install process or to install during off-hours, as the impact on the system is minimal.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h2 id="section-9">2</h2></td>
<td><h2 id="estimated-installation-time">Estimated Installation Time</h2></td>
</tr>
</tbody>
</table>

It takes approximately six minutes each to install TIU and ASU on either Open M or DSM systems. However, the Progress Notes and Discharge Summary conversions take much longer, depending on the number of notes and summaries at your site. Notes convert at the rate of approximately 2300 notes per hour, depending on the length of the notes.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>3</strong></td>
<td><h2 id="install-tiuasu-first-in-a-training-or-test-account">Install TIU/ASU first in a training or test account</h2></td>
</tr>
</tbody>
</table>

We recommend that you install TIU/ASU first in a training or test account. Install the required post-install patches (GMRA\*4\*6, GMTS\*2.7\*12, GMRP\*2.5\*45) *after* the installation *andafter* the Progress Notes and Discharge Summary conversionsjust before cut-over to TIU. These patches and other set-up instructions are described in the *TIU Implementation Guide.* Make sure all of the set-up works as intended and that your users are familiar with the changes before you install TIU into production.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 87%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>4</strong></td>
<td><h2 id="load-the-distribution-for-asu-v1.0">Load the distribution for ASU V1.0 </h2></td>
</tr>
</tbody>
</table>

> Select the option Kernel Installation and Distribution System, XPD MAIN. Choose the Installation option, followed by the option to Load the distribution from ASU1_0.KID, as shown below:

\>D ^XUP

Setting up programmer environment

Access Code: \[your code\]

Terminal Type set to: C-VT320

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: INstallation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: LOad a Distribution

Enter a Host File:ASU1_0.KID

KIDS Distribution saved on Jun 20, 1997@13:47:55

Comment: AUTHORIZATION/SUBSCRIPTION (ASU) v1.0 (6/20/97)

This Distribution contains Transport Globals for the following Package(s):

AUTHORIZATION/SUBSCRIPTION 1.0

Want to Continue with Load? YES// \<Enter\>

Loading Distribution...

Want to RUN the Environment Check Routine? YES// \<Enter\>

AUTHORIZATION/SUBSCRIPTION 1.0

Will first run the Environment Check Routine, USRPRE

\*\* CHECKING DHCP ENVIRONMENT \*\*

Everything looks fine!

Use INSTALL NAME: AUTHORIZATION/SUBSCRIPTION 1.0 to install this Distribution..

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 87%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>5</strong></td>
<td><h2 id="verify-checksums-in-the-transport-global">Verify Checksums in the transport global</h2></td>
</tr>
</tbody>
</table>

Run the option *Verify Checksums in Transport Global* to verify that all routines have the correct checksum. If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system. Call your IRM Field Office and report the problem.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 2 Verify Checksums in Transport Global

Select INSTALL NAME: AUTHORIZATION/SUBSCRIPTION 1.0 Loaded from Distribution 6/20/97@16:37:15

=\> AUTHORIZATION/SUBSCRIPTION (ASU) v1.0 (6/20/97) ;Created on Jun 20, 1

DEVICE: HOME// ANYWHERE

PACKAGE: AUTHORIZATION/SUBSCRIPTION 1.0 Jun 20, 1997 4:38 pm PAGE 1

------------------------------------------------------------------------

22 Routine checked, 0 failed.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>6</strong></td>
<td><h2 id="install-asu-v1.0">Install ASU V1.0 </h2></td>
</tr>
</tbody>
</table>

The dialogue you see on your screen won’t look exactly like the example below, as the KIDS process doesn’t allow an exact screen capture.

ASU Installation Example

Select Installation Option: INstall Package(s)

Select INSTALL NAME: AUTHORIZATION/SUBSCRIPTION 1.0 Loaded from Distribution 6/20/97@16:37:15

=\> AUTHORIZATION/SUBSCRIPTION (ASU) v1.0 (6/20/97) ;Created on Jun 20, 1

This Distribution was loaded on Jun 20, 1997@16:37:15 with header of

AUTHORIZATION/SUBSCRIPTION (ASU) v1.0 (6/20/97) ;Created on Jun 20, 1997@13:47:55

It consisted of the following Install(s):

AUTHORIZATION/SUBSCRIPTION 1.0

AUTHORIZATION/SUBSCRIPTION 1.0

Will first run the Environment Check Routine, USRPRE

\*\* CHECKING DHCP ENVIRONMENT \*\*

Everything looks fine!

Install Questions for AUTHORIZATION/SUBSCRIPTION 1.0

Incoming Files:

8930 USR CLASS (including data)

8930.1 USR AUTHORIZATION/SUBSCRIPTION (including data)

8930.2 USR ROLE (including data)

8930.3 USR CLASS MEMBERSHIP

8930.4 USR SEARCH CATEGORIES (including data)

8930.6 USR RECORD STATUS (including data)

8930.8 USR ACTION (including data)

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<device of your choice\>

ASU Installation Print

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: Utilities

Build File Print

Install File Print

Convert Loaded Package for Redistribution

Display Patches for a Package

Purge Build or Install Files

Rollup Patches into a Build

Update Routine File

Verify a Build

Verify Package Integrity

Select Utilities Option: Install File Print

Select INSTALL NAME: AUTHORIZATION/SUBSCRIPTION 1.0

INSTALL and BUILD FILES for AUTHORIZATION/SUBSCRIPTION 1.0 and TEXT

INTEGRATION UTILITIES 1.0:

PACKAGE: AUTHORIZATION/SUBSCRIPTION 1.0 Jun 20, 1997 5:23 pm PAGE 1

COMPLETED ELAPSED

------------------------------------------------------------------------

STATUS: Install Completed DATE LOADED: JUN 20, 1997@16:37:15

INSTALLED BY: <span class="mark">REDACTED</span>

NATIONAL PACKAGE: AUTHORIZATION/SUBSCRIPTION

INSTALL STARTED: JUN 20, 1997@16:40:01 16:40:30 0:00:29

ROUTINES: 16:40:02 0:00:01

FILES:

USR CLASS 16:40:04 0:00:02

USR AUTHORIZATION/SUBSCRIPTION 16:40:05 0:00:01

USR ROLE 16:40:05

USR CLASS MEMBERSHIP 16:40:06 0:00:01

USR SEARCH CATEGORIES 16:40:06

USR RECORD STATUS 16:40:06

USR ACTION 16:40:07 0:00:01

INPUT TEMPLATE 16:40:19 0:00:12

PROTOCOL 16:40:25 0:00:06

OPTION 16:40:28 0:00:03

POST-INIT CHECK POINTS:

XPD POSTINSTALL STARTED 16:40:29 0:00:01

XPD POSTINSTALL COMPLETED 16:40:29

INSTALL QUESTION PROMPT ANSWER

XPZ1 Want to DISABLE Scheduled Options, Menu Options, and Protocols NO

MESSAGES:

*ASU Installation Print, cont’d*

Install Started for AUTHORIZATION/SUBSCRIPTION 1.0 :

Jun 20, 1997@16:40:01

Installing Routines:

Jun 20, 1997@16:40:02

Installing Data Dictionaries:

Jun 20, 1997@16:40:07

Installing Data:

Jun 20, 1997@16:40:19

Installing PACKAGE COMPONENTS:

Installing INPUT TEMPLATE

Installing PROTOCOL

Installing OPTION

Jun 20, 1997@16:40:28

Running Post-Install Routine: ^USRPOST

'USR DEFINE CLASSES' List Template...

Filed.

'USR LIST MEMBERSHIP BY CLASS' List Template...

Filed.

'USR LIST MEMBERSHIP BY USER' List Template...

Filed.

'USR RULE BROWSER' List Template...

Filed.

Updating Routine file...

Updating KIDS files...

AUTHORIZATION/SUBSCRIPTION 1.0 Installed.

Jun 20, 1997@16:40:30

Install Started for AUTHORIZATION/SUBSCRIPTION 1.0 :

Jun 20, 1997@16:40:01

Installing Routines:.......................

Jun 20, 1997@16:40:02

Installing Data Dictionaries: ........

Jun 20, 1997@16:40:07

Installing Data: ....

Jun 20, 1997@16:40:19

Installing PACKAGE COMPONENTS:

Installing INPUT TEMPLATE.....

Installing PROTOCOL..........

*ASU Installation Print, cont’d*

Located in the USR (AUTHORIZATION/SUBSCRIPTION) namespace..

Located in the USR (AUTHORIZATION/SUBSCRIPTION) namespace..

Located in the USR (AUTHORIZATION/SUBSCRIPTION) namespace..

.

.

.

Located in the USR (AUTHORIZATION/SUBSCRIPTION) namespace..

Installing OPTION........

Jun 20, 1997@16:40:28

Running Post-Install Routine: ^USRPOST.

'USR DEFINE CLASSES' List Template...

Filed.

'USR LIST MEMBERSHIP BY CLASS' List Template...

Filed.

'USR LIST MEMBERSHIP BY USER' List Template...

Filed.

'USR RULE BROWSER' List Template...

Filed.

Updating Routine file......

Updating KIDS files.......

AUTHORIZATION/SUBSCRIPTION 1.0 Installed.

Jun 20, 1997@16:40:30

Install Message sent \#2642638

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong><br />
7</strong></td>
<td><h2 id="load-the-tiu-distribution">Load the TIU distribution</h2></td>
</tr>
</tbody>
</table>

Install the TIU package from the distribution by choosing the Install Name TIU1_0.KID as shown below. *If the installations abort, run the Unload a Distribution option to remove the Transport Global from your system. Call your IRM Field Office and report the problem.*TIU Load a Distribution Example

\> D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT320

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: INstallation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

You have PENDING ALERTS

Enter "VA VIEW ALERTS to review alerts

Select Installation Option: Load a Distribution

Enter a Host File: BETA:TIU1_0.KID

KIDS Distribution saved on Jun 20, 1997@12:35:55

Comment: TEXT INTEGRATION UTILITIES (TIU) v1.0 (6/20/97)

This Distribution contains Transport Globals for the following Package(s):

TEXT INTEGRATION UTILITIES 1.0

Want to Continue with Load? YES//

Loading Distribution...

Want to RUN the Environment Check Routine? YES//

TEXT INTEGRATION UTILITIES 1.0

Will first run the Environment Check Routine, TIUENV

\*\* CHECKING DHCP ENVIRONMENT \*\*

Everything looks fine!

Use INSTALL NAME: TEXT INTEGRATION UTILITIES 1.0 to install this Distribution.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>8</strong></td>
<td><h2 id="verify-checksums-in-the-transport-global-1">Verify Checksums in the transport global</h2></td>
</tr>
</tbody>
</table>

Run the option *Verify Checksums in Transport Global* to verify that all routines have the correct checksum. If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system. Call your IRM Field Office and report the problem.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 2 Verify Checksums in Transport Global

Select INSTALL NAME: TEXT INTEGRATION UTILITIES 1.0 Loaded from Distribution 6/20/97@16:44:05

=\> TEXT INTEGRATION UTILITIES (TIU) v1.0 (6/20/97) ;Created on Jun 20, 1

DEVICE: HOME// ANYWHERE

PACKAGE:TEXT INTEGRATION UTILITIES 1.0 Jun 20, 1997 4:44 pm PAGE 1

---------------------------------------------------------------------

211 Routines checked, 0 failed.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 87%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>9</strong></td>
<td><h2 id="optional-print-compare-and-backup-transport-globals">(optional) Print, Compare, and Backup Transport Globals </h2></td>
</tr>
</tbody>
</table>

Run the next three options on the KIDS Installation menu, if desired.

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 87%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>10</strong></td>
<td><h2 id="install-tiu">Install TIU</h2></td>
</tr>
</tbody>
</table>

TIU Installation Example

Select Installation Option: INstall Package(s)

Select INSTALL NAME: TEXT INTEGRATION UTILITIES 1.0 Loaded from Distribution 6/20/97@16:44:05

=\> TEXT INTEGRATION UTILITIES (TIU) v1.0 (6/20/97) ;Created on Jun 20, 1997

This Distribution was loaded on Jun 20, 1997@16:44:05 with header of

TEXT INTEGRATION UTILITIES (TIU) v1.0 (6/20/97) ;Created on Jun 20, 1997@12:35:55

It consisted of the following Install(s):

TEXT INTEGRATION UTILITIES 1.0

TEXT INTEGRATION UTILITIES 1.0

Will first run the Environment Check Routine, TIUENV

\*\* CHECKING DHCP ENVIRONMENT \*\*

Everything looks fine!

Install Questions for TEXT INTEGRATION UTILITIES 1.0

Incoming Files:

8925 TIU DOCUMENT

8925.1 TIU DOCUMENT DEFINITION (including data)

8925.2 TIU UPLOAD BUFFER

8925.3 TIU UPLOAD ERROR DEFINITION (including data)

8925.4 TIU UPLOAD LOG

8925.5 TIU AUDIT TRAIL

8925.6 TIU STATUS (including data)

8925.7 TIU MULTIPLE SIGNATURE

8925.8 TIU SEARCH CATEGORIES (including data)

8925.9 TIU PROBLEM LINK

8925.91 TIU EXTERNAL DATA LINK

8925.93 TIU PRINT PARAMETERS

8925.94 TIU DIVISION PRINT PARAMETERS

8925.95 TIU DOCUMENT PARAMETERS (including data)

8925.97 TIU CONVERSIONS (including data)

*TIU Installation, cont’d*

8925.98 TIU PERSONAL DOCUMENT TYPE LIST

8925.99 TIU PARAMETERS

8926 TIU PERSONAL PREFERENCES

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<device of your choice\>

### <table>
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<colgroup>
<col style="width: 12%" />
<col style="width: 88%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>11</strong></td>
<td><h2 id="print-results-of-the-installation-process">Print results of the installation process</h2></td>
</tr>
</tbody>
</table>

Use the KIDS Install File Print option if you’d like to print out the results of the installation process.

### ### TIU Installation Print-out Example 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PACKAGE: TEXT INTEGRATION UTILITIES 1.0 Jun 20, 1997 5:25 pm PAGE 1

COMPLETED ELAPSED

------------------------------------------------------------------------------

STATUS: Install Completed DATE LOADED: JUN 20, 1997@16:44:05

INSTALLED BY: <span class="mark">REDACTED</span>

NATIONAL PACKAGE: TEXT INTEGRATION UTILITIES

INSTALL STARTED: JUN 20, 1997@16:45:52 16:48:32 0:02:40

ROUTINES: 16:46:06 0:00:14

FILES:

TIU DOCUMENT 16:46:30 0:00:24

TIU DOCUMENT DEFINITION 16:46:35 0:00:05

TIU UPLOAD BUFFER 16:46:36 0:00:01

TIU UPLOAD ERROR DEFINITION 16:46:36

TIU UPLOAD LOG 16:46:37 0:00:01

TIU AUDIT TRAIL 16:46:37

TIU STATUS 16:46:38 0:00:01

TIU MULTIPLE SIGNATURE 16:46:38

TIU SEARCH CATEGORIES 16:46:38

TIU PROBLEM LINK 16:46:39 0:00:01

TIU EXTERNAL DATA LINK 16:46:40 0:00:01

TIU PRINT PARAMETERS 16:46:40

TIU DIVISION PRINT PARAMETERS 16:46:40

TIU DOCUMENT PARAMETERS 16:46:41 0:00:01

TIU CONVERSIONS 16:46:41

TIU PERSONAL DOCUMENT TYPE LIST 16:46:42 0:00:01

TIU PARAMETERS 16:46:43 0:00:01

*TIU Installation Print, cont’d*

TIU PERSONAL PREFERENCES 16:46:44 0:00:01

BULLETIN 16:46:49 0:00:05

SECURITY KEY 16:46:50 0:00:01

FUNCTION 16:46:50

PRINT TEMPLATE 16:46:54 0:00:04

INPUT TEMPLATE 16:47:03 0:00:09

DIALOG 16:47:04 0:00:01

PROTOCOL 16:47:37 0:00:33

REMOTE PROCEDURE 16:47:39 0:00:02

OPTION 16:48:16 0:00:37

POST-INIT CHECK POINTS:

XPD POSTINSTALL STARTED 16:48:21 0:00:05

XPD POSTINSTALL COMPLETED 16:48:21

INSTALL QUESTION PROMPT ANSWER

XPZ1 Want to DISABLE Scheduled Options, Menu Options, and Protocols NO

MESSAGES:

Install Started for TEXT INTEGRATION UTILITIES 1.0 :

Jun 20, 1997@16:45:52

Installing Routines:...................................................

Jun 20, 1997@16:46:06

Installing Data Dictionaries: ...................

Jun 20, 1997@16:46:44

Installing Data:

Jun 20, 1997@16:46:48

Installing PACKAGE COMPONENTS:

Installing BULLETIN.....

Installing SECURITY KEY..

Installing FUNCTION....

Installing PRINT TEMPLATE......

Installing INPUT TEMPLATE.............

Installing DIALOG......

Installing PROTOCOL...

Located in the TIU (TEXT INTEGRATION UTILITIES) namespace..

Located in the TIU (TEXT INTEGRATION UTILITIES) namespace.

.

.

.

Located in the TIU (TEXT INTEGRATION UTILITIES) namespace..

Installing REMOTE PROCEDURE.........................

Installing OPTION......................................................

......................................

Jun 20, 1997@16:48:16

*TIU Installation Print-out, cont’d*

Running Post-Install Routine: ^TIUPOST.

'TIU BROWSE FOR CLINICIAN' List Template...

Filed.

'TIU BROWSE FOR MGR' List Template...

Filed.

'TIU BROWSE FOR MRT' List Template...

Filed.

'TIU BROWSE FOR READ ONLY' List Template...

Filed.

'TIU CHANGE TITLE' List Template...

Filed.

'TIU COMPLETE NOTES' List Template...

Filed.

'TIU COPY DOCUMENT' List Template...

Filed.

'TIU DISPLAY AUDIT TRAIL' List Template...

Filed.

'TIU DISPLAY FILING EVENT' List Template...

Filed.

'TIU EDIT ADDENDUM' List Template...

Filed.

'TIU LINK TO PROBLEM' List Template...

Filed.

'TIU OE/RR REVIEW PN' List Template...

Filed.

'TIU REASSIGN' List Template...

Filed.

'TIU REVIEW BY PATIENT & TITLE' List Template...

Filed.

'TIU REVIEW BY TITLE' List Template...

Filed.

'TIU REVIEW DS CLINICIAN' List Template...

Filed.

'TIU REVIEW DS MGR' List Template...

Filed.

'TIU REVIEW DS MRT' List Template...

Filed.

'TIU REVIEW FILING ERRORS' List Template...

Filed.

*  
TIU Installation Print-out, cont’d*

'TIU REVIEW FILING EVENTS' List Template...

Filed.

'TIU REVIEW PN CLINICIAN' List Template...

Filed.

'TIU REVIEW PN MGR' List Template...

Filed.

'TIU REVIEW PN MRT' List Template...

Filed.

'TIU REVIEW SCREEN CLINICIAN' List Template...

Filed.

'TIU REVIEW SCREEN DS UNSIGNED' List Template...

Filed.

'TIU REVIEW SCREEN MGR' List Template...

Filed.

'TIU REVIEW SCREEN MRT' List Template...

Filed.

'TIU REVIEW SCREEN PN UNSIGNED' List Template...

Filed.

'TIU REVIEW SCREEN READ ONLY' List Template...

Filed.

'TIU SEARCH LIST MGR' List Template...

Filed.

'TIU SEARCH LIST MRT' List Template...

Filed.

'TIU SEND BACK' List Template...

Filed.

'TIU SIGN ON CHART' List Template...

Filed.

'TIU SIGN/COSIGN' List Template...

Filed.

'TIU VERIFY' List Template...

Filed.

'TIUFA SORT DDEFS CLIN' List Template...

Filed.

'TIUFA SORT DDEFS MGR' List Template...

Filed.

'TIUFC CREATE DDEFS MGR' List Template...

Filed.

'TIUFD DISPLAY CLIN' List Template...

Filed.

*  
TIU Installation Print-out, cont’d*

'TIUFD DISPLAY MGR' List Template...

Filed.

'TIUFD DISPLAY VIEW' List Template...

Filed.

'TIUFDJ DISPLAY OBJECT MGR' List Template...

Filed.

'TIUFH EDIT DDEFS CLIN' List Template...

Filed.

'TIUFH EDIT DDEFS MGR' List Template...

Filed.

'TIUFJ OBJECTS CLIN' List Template...

Filed.

'TIUFJ OBJECTS MGR' List Template...

Filed.

'TIUFT ITEMS ADD/EDIT/VIEW MGR' List Template...

Filed.

'TIUFT ITEMS EDIT/VIEW CLIN' List Template...

Filed.

'TIUFT ITEMS VIEW MGR/CLIN' List Template...

Filed.

'TIUFX BOILERPLATE TEXT' List Template...

Filed.

'TIUFX BOILERPLATE TEXT VIEW' List Template...

Filed.

\*\*\* COMPILING HIDDEN PROTOCOL MENUS \*\*\*

TIU HIDDEN ACTIONS.

TIU HIDDEN ACTIONS ADVANCED.

TIU HIDDEN ACTIONS OE/RR.

TIU HIDDEN ACTIONS BROWSE.

Updating Routine file....

The following Routines were created during this install:

TIUXRC

TIUXRC1

TIUXRC2

TIUXRC3

TIUXRC4

TIUXRC5

TIUXRC6

TIUXRC7

TIUXRC8

TIUEDS

TIUEDS1

TIUEDS2

*  
TIU Installation Print-out, cont’d*

TIUEDS3

TIUEDS4

TIUEDS5

TIUEDS6

TIUEPN

TIUEPN1

TIUEPN2

TIUEPN3

TIUEPN4

TIUEPN5

TIUEPN6

TIUEPN7

TIUEPN8

TIUPREL

TIUSTA

TIUSTT

TIUSTS..

Updating KIDS files.......

TEXT INTEGRATION UTILITIES 1.0 Installed.

Jun 20, 1997@16:48:32

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>12</strong></td>
<td><h2 id="verify-that-tiu-usr-and-supporting-routines-were-moved-to-appropriate-systems">Verify that TIU*, USR*, and supporting routines were moved to appropriate systems</h2></td>
</tr>
</tbody>
</table>

Verify that TIU\* and USR\* routines were moved to appropriate systems, according to your local configurations.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>13</strong></td>
<td><h2 id="optional-print-a-list-of-package-components">(Optional) Print a list of package components</h2></td>
</tr>
</tbody>
</table>

Use the KIDS Build File Print option if you would like a complete listing of package components (e.g., routines and options) exported with this software. You will need to print each build exported with TIU.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 87%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>14</strong></td>
<td><h2 id="create-a-new-resource-device">Create a new Resource Device</h2></td>
</tr>
</tbody>
</table>

After Installing ASU and TIU v1.0, create a new Resource Device called TIU/PXAPI RESOURCE using the option XUDEVEDITRES, as shown below:

\>D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT320

You have 4 new messages.

Select OPTION NAME: XUDEVEDITRES Resource Device Edit

Resource Device Edit

Select Resource Device: TIU/PXAPI RESOURCE

Are you adding 'TIU/PXAPI RESOURCE' as a new DEVICE? No// Y (Yes)

DEVICE LOCATION OF TERMINAL: NA

DEVICE \$I: TIU/PXAPI RESOURCE

DEVICE VOLUME SET(CPU): \<Enter\>

DEVICE TYPE: RES RESOURCES

NAME: TIU/PXAPI RESOURCE// \<Enter\>

\$I: TIU/PXAPI RESOURCE// \<Enter\>

VOLUME SET(CPU): \<Enter\>

RESOURCE SLOTS: 1// 10

Select Resource Device:

\> hNOTE: It is critical that both the name and \$I for this device be entered exactly as shown. The number of slots is site configurable. If you find that there are frequently tasks waiting for the TIU/PXAPI RESOURCE device (by checking ^ZTMON), you may wish to increase the number of slots. At West Palm Beach, where approximately 3000 documents per day are entered into the system, ten slots have been found to be adequate.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>15</strong></td>
<td><h2 id="see-the-tiu-implementation-guide-for-set-up-instructions">See the TIU Implementation Guide for set-up instructions </h2></td>
</tr>
</tbody>
</table>

The Implementation Guide is intended for Clinical Coordinators or IRMS staff who are assigned to implement and/or maintain TIU and ASU. The guide contains help in the following areas:

- Converting from Progress Notes 2.5 and Discharge Summary 1.0
- Setting up User Classes, Business Rules, Document Definitions, site parameters, and menus
- Using the upload process for other reports (with storage outside TIU)
- Troubleshooting TIU and ASU

# # Release Notes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Features of TIU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

a. Integration

The initial release of Text Integration Utilities (TIU) Version 1.0 includes Discharge Summary and Progress Notes. Consult Reports will be added when the Computerized Patient Record System (CPRS) is released. TIU has also been designed to meet the needs of other clinical applications that address document handling. Upload of ASCII formatted documents into V*IST*A, which in the past has only been possible for Discharge Summaries, is now available for many kinds of documents (including Progress Notes).

*Standardized and common user interface*

Clinicians can go through the same program to enter, review, and sign Discharge Summaries, Progress Notes, and other clinical documents through TIU.

#### Database

Clinicians and management can search for and retrieve clinical documents more efficiently because documents reside in a single location within the database. This is also a benefit for other uses such as Incomplete Record Tracking, quality management, results reporting, order checking, research, etc.

*Improved Management of Documents—Document Definition Hierarchy*

In connection with Authorization/Subscription Utility (ASU), a hospital can set up policies and practices for determining who is responsible or has the privilege for performing various actions on required VHA documents.

TIU has a consistent file structure for defining elements and parameters of a document. It allows

- Entry, edit, deletion, printing, and viewing of document definition
- Shared components
- Ownership (personal or class) of document definitions
- “Locking” of National Standard document definitions
- Boilerplate Text functionality
- Objects such as “PATIENT AGE” which can be embedded in boilerplate text

  *Release Notes, cont’d*b. More Links to Other Packages.

  TIU provides more interfaces for Discharge Summary and Progress Notes with such applications as Health Summary, Problem List, Patient Care Encounter/Visit Tracking, and Incomplete Record Tracking, and will also interface with the Computerized Patient Record System (CPRS) when it is released.

## Changes to Progress Notes and Discharge Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although Text Integration Utilities is a new package, it incorporates and modifies functionality of Progress Notes 2.5 and Discharge Summaries 1.0. Changes that users and managers will see to these packages are noted below. When appropriate, a relevant E3R is listed.

New Functionality for Clinical Coordinators & IRM

1\. The set of Progress Notes Types released with GMRP 2.5 will no longer be used by TIU. It has been replaced by the Document Hierarchy which gives the site more flexibility in designing and implementing progress notes for their users.

2\. Specialized menus are available to assist various user populations.

For example, there is a menu for Management Information Service as well as one for Medical Records Technician.

3\. A TIU Maintenance Menu has been created to assist IRM and Clinical Coordinator personnel with individualizing the software for use by the site and by the user.

4\. Sites are now able to upload progress notes into VISTA.

5\. Sites can create and store boilerplates/templates for a variety of notes and consults.

### Technical Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. All clinical documents entered by through TIU are stored in ^TIU(8925, TIU Document File. This includes progress notes.

2\. A single set of software routines is used to process clinical documents.

  
New Functionality for Clinicians, Nurses, and HIMS users

### Progress Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*New menus and options*

- MAS Progress Note Print Menu
- Integrated menu for Clinicians
- Document Definition Menu for Clinicians
- Ability to go through the OE/RR Clinician Menu (in OE/RR 2.5 or CPRS 1.0) menus to review, sign, or add progress notes
- Ability to see more views of progress notes, for an individual patient or across patients

######## Printing

- Users can set print formats (E3R 2550)
- Outputs for both inpatients and outpatients(E3R 3304)
- Discharge patient outputs. (E3R 3305)
- New progress notes report (E3R 4870)
- Default printing (E3R 4933)
- Unsigned notes lists (E3R 4968)
- Print notes for author/title (E3R 6525)
- Separate page option on print by title (E3R 7407)
- Additional configuration for “print by author” (E3R 7036)
- Print division associated with hospital location (E3R 8350)
- Separate in/outpatient batch prints (E3R 8457)

  *Copy*the new Copy functionality lets you:
- Copy an existing note to an amended progress note (E3R 4307)
- Copy group notes (E3R 4647)
- Copy an outpatient note and use it for an inpatient note (when an outpatient is admitted). (E3R 7433)
- Copy boilerplate text and objects
- Copy components

  *New types of notes*
- Ability to create a new type of formatted note (E3R 4571)
- Telephone contact format (E3R 4599)
- For Patients with two-levels of care (E3R 3306)
- Titles with menus (E3R 4983)
- Ability to set up new types (E3R 5383)

  *New Functionality for Clinicians, Nurses, and HIIMS users, cont’dSigning*
- Multiple cosigners (E3R 5792)
- Lock review/print options with security key (E3R 5953)
- Co-signer allowed to edit note (E3R 6180)
- Modify cosigner comment (E3R 7274)
- Signature block text (E3R 6549)
- VA alert for unsigned notes (E3R 6961)
- Signature title (E3R 7023)
- Editing of title and location in unsigned note (E3R 7310)
- Addition of co-signer’s name (E3R 7519)
- Modified patient/author display for co-sign options (E3R 7522)
- Ability to look up unsigned progress notes by patient (E3R 8704)
- Modified co-sign progress note(s) by author option (E3R 9038)
- Editing of progress note by co-signer before signing (E3R 5172)

  *Other*
- Expanded title to maximum length (E3R 6266)
- Patient location field (E3R 6279)
- Changed views of progress notes through OE/RR (E3R 6321)
- Function to create templates/boilerplates (E3R 6477)
- Confidentiality of progress notes (E3R 6478)
- Ability to bring other packages’ data into progress notes (E3R 6515)
- Ability to restrict access to notes (E3R 6925,)
- Added location field to review option (E3R 7146)
- Can look up signed notes for by title (E3R 7260)
- Ability to edit header information (E3R 7618)
- Additional progress note sorting capabilities (E3R 7851)
- Added prompt for additional titles of progress note (E3R 7906)
- Transcriptionist name display (E3R 8263)
- Late entries marked as such (E3R 5209)

### Discharge Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New or changed functionality for Clinicians and HIMS users

*New features*

- Ability to review Progress Notes, Discharge Summary, and other documents from the same screen
- Boilerplate functionalityability to use templates with embedded objects (pulling data from other VISTA packages, such as Lab, Dietetics, Radiology, etc.)
- Added verify/unverify to Discharge Summary Manager Menu (browse) (E3R \#6963)
- Ability to upload two admissions on the same day
- Added copying functionality (E3R \#6912)
- Added configurable options for Attending physicians’ leave (E3R \#7390)
- Personal preferences options which allow default patient lists and other default selections, to speed up the entry process

  *Additions/Changes to the Discharge Summary Form*
- Current admission listed first in Discharge Summary Enter/edit options (E3R \#5637)
- Added a D/C date field (E3R \#4941)
- Added DOB on the Discharge Summary form (E3R \#8454)
- Added Transcription date (E3R \#8776)
- Transcriptionist ID modification (E3R \#5287)
- Initials for transcription ID (E3R \#5623)
- Fixed Discharge summary ward ID (E3R \#4594)
- Added Transcriptionist name field (E3R \#5267)
- Added identification of interim summaries
- Report format uses VA form (E3R \#6185)
- Added signature date (E3R \#6601)

  *Alerts*
- Differentiate alerts (E3R \#6194)
- View alerts to show work type (E3R \#6094)
- Separate alerts for each work type (E3R \#6095)

  *New or changed functionality for Clinicians and HIMS users, cont’dSigning/Cosigning*
- Signed on chart signature date (E3R \#6677)
- Date of signature (E3R \#5753)
- Signature blocks on addenda (E3R \#8676)
- New parameters for signature blocks (E3R \#8679)
- Amend signature blocks (E3R \#8680)
- Optional electronic signature (E3R \#6149)

  *Addenda*
- Allows replacement of original note with addendum (E3R \#5779)
- Allows promotion of addenda to originals (E3R \#8774)
- Allows page breaks when printing addenda (E3R \#8775)

Progress Note E3Rs Resolved By Text Integration Utilities

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>E3R #</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td><strong>2550</strong></td>
<td>Allow user to set print format</td>
</tr>
<tr class="odd">
<td><strong>3151</strong></td>
<td>Option to move notes</td>
</tr>
<tr class="even">
<td><strong>3304</strong></td>
<td>In/out pt. Outputs</td>
</tr>
<tr class="odd">
<td><strong>3305</strong></td>
<td>Discharge patient outputs</td>
</tr>
<tr class="even">
<td><strong>3306</strong></td>
<td>Patients with two-levels of care.</td>
</tr>
<tr class="odd">
<td><strong>4307</strong></td>
<td>Copy existing note to an amended progress note</td>
</tr>
<tr class="even">
<td><strong>4583</strong></td>
<td>Additional options for co-signature set-up</td>
</tr>
<tr class="odd">
<td><strong>4571</strong></td>
<td>Ability to create a new type of formatted note</td>
</tr>
<tr class="even">
<td><strong>4599</strong></td>
<td>Telephone contact format</td>
</tr>
<tr class="odd">
<td><strong>4647</strong></td>
<td>Copy group notes</td>
</tr>
<tr class="even">
<td><strong>4870</strong></td>
<td>Progress note report</td>
</tr>
<tr class="odd">
<td><strong>4933</strong></td>
<td>Default printing</td>
</tr>
<tr class="even">
<td><strong>4968</strong></td>
<td>Unsigned notes lists</td>
</tr>
<tr class="odd">
<td><strong>4983</strong></td>
<td>Titles with menus</td>
</tr>
<tr class="even">
<td><strong>5172</strong></td>
<td>Editing of Progress Note by co-signer before sealing</td>
</tr>
<tr class="odd">
<td><strong>5209</strong></td>
<td>Late entries should be marked as such</td>
</tr>
<tr class="even">
<td><strong>5383</strong></td>
<td>Need to be able to set up new types</td>
</tr>
<tr class="odd">
<td><strong>5592</strong></td>
<td>Focus type</td>
</tr>
<tr class="even">
<td><strong>5733</strong></td>
<td>H&amp;P The Text Integration Utility (TIU) will allow sites to format Progress Notes such as the History &amp; Physical Note.</td>
</tr>
<tr class="odd">
<td><strong>5792</strong></td>
<td>Multiple cosigners</td>
</tr>
<tr class="even">
<td><strong>5953</strong></td>
<td>Lock review/print options with security key</td>
</tr>
<tr class="odd">
<td><strong>5988</strong></td>
<td>Inactive wards/notes</td>
</tr>
<tr class="even">
<td><strong>6174</strong></td>
<td>Allocation error when listing unsigned notes</td>
</tr>
<tr class="odd">
<td><strong>6180</strong></td>
<td>Co-signer allowed to edit note?</td>
</tr>
<tr class="even">
<td><strong>6234</strong></td>
<td>Do not allow signature if ____ present in note.</td>
</tr>
<tr class="odd">
<td><strong>6251</strong></td>
<td>Enter a note through consult/request tracking</td>
</tr>
<tr class="even">
<td><strong>6266</strong></td>
<td>Expand title to maximum</td>
</tr>
<tr class="odd">
<td><strong>6279</strong></td>
<td>Patient location field</td>
</tr>
<tr class="even">
<td><strong>6321</strong></td>
<td>Change view of progress notes through OE/RR</td>
</tr>
<tr class="odd">
<td><strong>6477</strong></td>
<td>Function to create templates</td>
</tr>
<tr class="even">
<td><strong>6478</strong></td>
<td>Confidentiality of progress notes integration utilities v1.0 and authorization/subscription utilities v1.0.software in support of this security need will be developed in a subsequent patch to both releases.</td>
</tr>
<tr class="odd">
<td><strong>6502</strong></td>
<td>Need stable electronic signature block title</td>
</tr>
<tr class="even">
<td><strong>6515</strong></td>
<td>Moving other packages into progress notes</td>
</tr>
<tr class="odd">
<td><strong>6525</strong></td>
<td>Print notes for author/title</td>
</tr>
<tr class="even">
<td><strong>6549</strong></td>
<td>Signature block text</td>
</tr>
<tr class="odd">
<td><strong>6890</strong></td>
<td>Memory</td>
</tr>
<tr class="even">
<td><strong>6925</strong></td>
<td><p>Ability to restrict access to notes</p>
<p>The structure required to support this request will be released with text integration utilities v1.0 and authorization/subscription utilities v1.0. The software to implement this function will be released in subsequent patches</p></td>
</tr>
<tr class="odd">
<td><strong>6961</strong>.</td>
<td>VA alert for unsigned notes</td>
</tr>
</tbody>
</table>

|            |                                                                                                                                                                                     |
|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| E3R \# | Description                                                                                                                                                                     |
| 7023   | Signature title                                                                                                                                                                     |
| 7036   | Additional configuration for 'print by author'                                                                                                                                      |
| 7146   | Add location field to review option                                                                                                                                                 |
| 7260   | Auto-retrieve signed notes for lookup by title                                                                                                                                      |
| 7274   | Modify cosigner comment default                                                                                                                                                     |
| 7310   | Add editing of title and location in unsigned note                                                                                                                                  |
| 7407   | Include separate page option on print by title                                                                                                                                      |
| 7433   | Copy outpatient note and use inpatient.                                                                                                                                             |
| 7519   | Addition of co-signers name                                                                                                                                                         |
| 7522   | Modify patient/author display for co-sign options                                                                                                                                   |
| 7551   | DISCHARGE PLANNING ENHANCEMENT Unable to address this E3R due to lack of information. A Discharge Planning document may be developed and supported under Text Integration Utilities |
| 7575   | Add 'buffer' saving to Progress Notes                                                                                                                                               |
| 7618   | Edit header info.                                                                                                                                                                   |
| 7652   | Refile option                                                                                                                                                                       |
| 7809   | Option for specifying co-signature desired                                                                                                                                          |
| 7851   | ADDITIONAL PROGRESS NOTE SORT A wide variety of sorting actions is available in Text Integration Utilities. V1.0. The requested sort is supported.                                  |
| 7906   | Prompt for additional titles: title of progress note                                                                                                                                |
| 8263   | Transcriptionist name display                                                                                                                                                       |
| 8274   | Transcriptionist exiting note                                                                                                                                                       |
| 8350   | Print division associated with hospital location                                                                                                                                    |
| 8457   | Separate in/outpatient batch prints                                                                                                                                                 |
| 8704   | Unsigned progress notes by pt                                                                                                                                                       |
| 9038   | Modify co-sign progress note(s) by author option                                                                                                                                    |
| 10724  | Ability to boilerplate addenda                                                                                                                                                      |
| 11334  | Concurrence & Comment prompts for interdiciplinary signer                                                                                                                           |
| 11536  | View notes by title                                                                                                                                                                 |
| 11560  | Multi-seclected dcoument, multiple author                                                                                                                                           |
| 11881  | Verification when moving documents                                                                                                                                                  |
| 11895  | Linking progress notes together                                                                                                                                                     |
| 11898  | Historical encounter                                                                                                                                                                |
| 11926  | Personal preference parameter                                                                                                                                                       |
| 11964  | TIU new visits to create unsheduled visit                                                                                                                                           |
| 12089  | Search action for browsing notes, reports                                                                                                                                           |
| 12128  | Templated addendums                                                                                                                                                                 |
| 12133  | Add sort to notes tab: Notes by service                                                                                                                                             |
| 12792  | Suspense status key to clarify meaning (partially in that it now displays suspended medications now display as active)                                                              |
| 13234  | Sort notes by type rather than by author                                                                                                                                            |
| 13436  | Discharge summary alerts                                                                                                                                                            |
| 13527  | Identified signers not getting to view alters                                                                                                                                       |
| 13590  | Limits to TIU titles for consult completion                                                                                                                                         |
| 13842  | Unsigned progress note alert to signer & cosigner together                                                                                                                          |

|                                                                       |                                                               |
|-----------------------------------------------------------------------|---------------------------------------------------------------|
| <span id="e3r" class="anchor"></span><span class="mark">E3R \#</span> | <span class="mark">Description</span>                         |
| 13560                                                             | Electronic signature of operation reports                     |
| 14142                                                             | Combine search categories                                     |
| 14192                                                             | Sorting/access ease                                           |
| 14738                                                             | TIU/ASU to recognize (2) types of edit                        |
| 15215                                                             | Security violation                                            |
| 15828                                                             | Health Summary and PCE components into TIU objects            |
| 15908                                                             | TIU Alerts for additional signers are confusing               |
| 16020                                                             | Nesting TIU template fields                                   |
| 16045                                                             | 2<sup>nd</sup> alert for unsigned or uncosigned TIU documents |
| 16078                                                             | Forward unsigned notes to service chief                       |
| 16496                                                             | Improve additional signer functionality for surrogates        |
| 17062                                                             | Expected cosigner can be changed without audit                |
| 17281                                                             | Alerts mechanism defined in for the document definition       |
| 17292                                                             | Alert recipient by document type                              |
| 17784                                                             | Unsigned document alert to cosigner when the author is gone   |
| 17785                                                             | Ability to generate an alert for a third party signer         |
| 19386                                                             | Allow editing of expected cosigner                            |

#### Discharge Summaries E3Rs Resolved by TIU

|                |                                                                      |
|----------------|----------------------------------------------------------------------|
| E3R Number | Description                                                      |
| 4594       | Fix Discharge summary ward ID                                        |
| 4941       | Add a DC date field                                                  |
| 5287       | Transcriptionist ID modification                                     |
| 5528       | Identify interim summaries                                           |
| 5623       | Initials for transcription ID                                        |
| 5637       | List current admission first in Discharge Summary Enter/edit options |
| 5779       | Replace original with addendum                                       |
| 5833       | Need ability to upload for 2 admissions on same day                  |
| 6094       | View alerts to show work type                                        |
| 6095       | Separate alerts for each work type                                   |
| 6149       | Optional electronic signature                                        |
| 6185       | Use VA form for report format                                        |
| 6194       | Differentiate alerts                                                 |
| 6601       | Add signature date                                                   |
| 6677       | Signed on chart signature date                                       |
| 6753       | Date signed                                                          |
| 6912       | Copy function                                                        |
| 6963       | Add verify/unverify to Discharge Summary Manager Menu (browse)       |
| 7390       | Add configurable options for attending MD leave                      |
| 8454       | DOB on the discharge summary form                                    |
| 8676       | Signature blocks on addenda                                          |
| 8680       | Amend signature blocks                                               |
| 8774       | Allow promotion of addenda to originals                              |
| 8775       | Page breaks when printing addenda                                    |
| 8776       | Transcription date                                                   |