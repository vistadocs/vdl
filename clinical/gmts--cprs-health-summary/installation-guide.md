---
title: Health Summary Version 2.7 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: GMTS
app_name: "CPRS: Health Summary"
section: CLI
app_status: active
pkg_ns: GMTS
patch_ver: 2.7
patch_id: GMTS*2.7
group_key: "GMTS:GMTS:2.7"
file_numbers: []
security_keys: []
menu_options: 0
description: Version 2.7December 2019Department of Veterans Affairs (VA)Decentralized Hospital Computer ProgramRevision History
audience: 
keywords: 
  - blockquote
  - strong
  - class
  - health
  - summary
  - table
  - gmtsi
  - style
  - width
  - contents
page_count: 0
word_count: 4946
section_count: 8
table_count: 1
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: December 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Health_Summary/hsum_2_7_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Health_Summary/hsum_2_7_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=63"
---

Health Summary (GMTS\*2.7\*129)Installation Guide & Release Notes

![](health-summary-version-2-7-installation-guide/001.png)

Version 2.7December 2019Department of Veterans Affairs (VA)Decentralized Hospital Computer ProgramRevision History

| Revision Date | Description                                                                            | Author(s)                      |
|-------------------|--------------------------------------------------------------------------------------------|------------------------------------|
| December 2019     | GMTS\*2.7\*129 - Updated Title page, TOC, footers, and removed all mentions of Social Work | <span class="mark">REDACTED</span> |

Preface

> The Health Summary package integrates clinical data from DHCP ancillary packages into patient health summaries which can be viewed online or printed as reports. Version 2.7 includes several new components and features, including Patient Care Encounter (PCE) components, which are described in the Release Notes section of this manual.

> This manual is intended to be used as an installation and set-up guide for IRM Service, Clinical Coordinators, and ADPACs.

> It also contains Release Notes describing new components and features included in Version 2.7 of Health Summary.

> Appendix A contains a Component Checklist to help Clinical Coordinators and users determine which components may need disabling.

> Appendix B contains a post-init matrix which shows how the post-init reconciles package components to local package installation statuses.

# Table ofContents


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Table ofContents](#table-ofcontents)
  - [Pre-Installation Information](#pre-installation-information)
  - [Installation Procedures](#installation-procedures)
  - [Installation Over Version 2.5 Example](#installation-over-version-25-example)
    - [First Time Installation Example](#first-time-installation-example)
  - [Setting up Health Summary](#setting-up-health-summary)
    - [Security Key Assignment](#security-key-assignment)
    - [Menu Assignment](#menu-assignment)
    - [Disable/Enable Health Summary Components](#disableenable-health-summary-components)
    - [Review site parameters](#review-site-parameters)
    - [Customize the Ad Hoc Health Summary type](#customize-the-ad-hoc-health-summary-type)
    - [Schedule batch printing](#schedule-batch-printing)
    - [Set up Batch Print Location](#set-up-batch-print-location)
  - [Release Notes](#release-notes)
    - [Changes to Files](#changes-to-files)
  - [Appendix A  Component Checklist](#appendix-a-component-checklist)
  - [Appendix B  Post-init Matrix](#appendix-b-post-init-matrix)
> <u>INSTALLATION GUIDE</u>

## Pre-Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Required Packages

> Before installing Health Summary 2.7, the following DHCP packages must be installed.

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package</strong></p>
</blockquote></th>
<th><strong>Required Version (or later)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Kernel</p>
</blockquote></td>
<td><blockquote>
<p>7.1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Registration</p>
</blockquote></td>
<td><blockquote>
<p>5.3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Scheduling</p>
</blockquote></td>
<td><blockquote>
<p>5.3</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA FileMan</p>
</blockquote></td>
<td><blockquote>
<p>21</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Because of the integrated nature of this package, certain versions of ancillary packages must be in place to support their corresponding Health Summary components. The following chart lists the package version numbers.

> Notes: The packages and versions listed below support the components that are exported with Health Summary V. 2.7. During the installation, components that are supported by packages which have not been installed will be automatically disabled. If you load a package version which requires updated routines (Outpatient Pharmacy 6.0, Medicine 2.2, and Problem List 2.0), see Appendix B in this manual for instructions.

<table>
<colgroup>
<col style="width: 66%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Minimum Version</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Allergy Tracking System</p>
</blockquote></td>
<td><blockquote>
<p>3.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Automated Med Info Exchange (AMIE)</p>
</blockquote></td>
<td><blockquote>
<p>2.7</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Dietetics</p>
</blockquote></td>
<td><blockquote>
<p>4.6</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Discharge Summary</p>
</blockquote></td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Gen. Med. Rec. - Vitals</p>
</blockquote></td>
<td><blockquote>
<p>2.5</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Inpatient Medications</p>
</blockquote></td>
<td><blockquote>
<p>4.5</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Lab Service</p>
</blockquote></td>
<td><blockquote>
<p>5.2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Medicine</p>
</blockquote></td>
<td><blockquote>
<p>2.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Mental Health</p>
</blockquote></td>
<td><blockquote>
<p>5.01</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Order Entry/Results Reporting (OE/RR)</p>
</blockquote></td>
<td><blockquote>
<p>2.5</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Outpatient Pharmacy</p>
</blockquote></td>
<td><blockquote>
<p>6.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PCE Patient Care Encounter</p>
</blockquote></td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Problem List</p>
</blockquote></td>
<td><blockquote>
<p>2.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Progress Notes</p>
</blockquote></td>
<td><blockquote>
<p>2.5</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Radiology</p>
</blockquote></td>
<td><blockquote>
<p>4.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Surgery</p>
</blockquote></td>
<td><blockquote>
<p>3.0</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Resource Requirements

> The Health Summary routines and globals use approximately 750K of disk space. CPU cycles and paper consumption will vary with usage by each site. The ^GMT global only grows minimally.

> Version Installation Order First Time Installation

> Health Summary V. 2.7 may be installed in an account (test or production) in which no previous version of Health Summary existed.

> Over Version 2.5

> You can install V. 2.7 over V. 2.5, but you must delete all GMTS\* routines prior to installing the new version. Remember to exclude all locally created GMTSZ\* routines.

> NOTE: Any locally developed components that you have set up in the Component File \#142.1 will be preserved when you install V. 2.7.

> Package Namespace

> GMTS is the namespace assigned to Health Summary. All Health Summary V. 2.7 routines, options, bulletins, mail groups, and security keys use this namespace.

> Global and File List

> The Health Summary package contains the following files. The amount of disk space it uses depends on the number of local components and types created. This has averaged approximately 750K of disk space.

<table style="width:100%;">
<colgroup>
<col style="width: 21%" />
<col style="width: 31%" />
<col style="width: 22%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Number</strong></p>
</blockquote></th>
<th><strong>Name</strong></th>
<th><strong>Global</strong></th>
<th><blockquote>
<p><strong>Data Exported</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>142</strong></p>
</blockquote></td>
<td><p>HEALTH</p>
<p>SUMMARY TYPE</p></td>
<td>^GMT(142,</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>142.1</strong></p>
</blockquote></td>
<td>HEALTH SUMMARY COMPONENT</td>
<td>^GMT(142.1,</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>142.99</strong></p>
</blockquote></td>
<td>HEALTH SUMMARY PARAMETERS</td>
<td>^GMT(142.99,</td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Global Protection

> *DSM cluster configuration*: the Health Summary Globals must be set and protected on the proper volume set using the %GLOMAN utility.

> *MSM configurations*: use the %GCH system utility to create and change globals and their attributes. First-Time Install: MSM sites must set the new global to null on the file server (S ^GMT="").

> On DSM and MSM systems, all Health Summary globals should be defined as follows:

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>System</strong></p>
</blockquote></th>
<th><strong>World</strong></th>
<th><blockquote>
<p><strong>Group</strong></p>
</blockquote></th>
<th><strong>UCI/USER</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>DSM</strong></p>
</blockquote></td>
<td><blockquote>
<p>RWP</p>
</blockquote></td>
<td>RWP</td>
<td><blockquote>
<p>RWP</p>
</blockquote></td>
<td>RWP</td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>MSM</strong></p>
</blockquote></td>
<td><blockquote>
<p>RWD</p>
</blockquote></td>
<td>RWD</td>
<td><blockquote>
<p>RWD</p>
</blockquote></td>
<td>RWD</td>
</tr>
</tbody>
</table>

> Pre-init, Init, and Post-init Actions

> In addition to the standard initialization routines (GMTSI\*), Health Summary also exports environment check (GMTSENV), Pre-init (GMTSPREI), and Post-init (GMTSPOS\*) routines.

> Environment check routine

> The environment check routine (GMTSENV) checks to see if the person installing Health Summary is an active user, has his/her DUZ(0) set to “@,” and that the U variable has been defined.

> Pre-init routine

> The Pre-init routine adds GMTS as an application group to files 60, 71, and 120.51. It also adds GMTS to 811.9 (PCE REMINDER/ MAINTENANCE ITEMS), 9001017 (HEALTH SUMMARY MEAS

> PANEL), and 9999999.64 (HEALTH FACTORS), which are Patient Care Encounter files that won’t exist until PCE is installed. PCE will install them with GMTS as an application group if PCE is installed after Health Summary V. 2.7. The pre-init renames the abbreviation for the Medicine Summary component from “MED” to “MEDS” and deletes the following fields from the HEALTH SUMMARY TYPE file (#142).

> *Fields deleted*

2.  ICD TEXT DISPLAYED
3.  PROVIDER NARRATIVE
4.  MEASUREMENT PANEL
5.  LAB TEST PANEL
6.  SURVEILLANCE PANEL

> Inits

> The standard inits create/update the Health Summary files, and establish data dictionaries and file options.

> Post-init routines

> See Appendix B, Post init Matrix, for detailed information of what the Post inits do.

Estimated Installation Time

<table style="width:100%;">
<colgroup>
<col style="width: 28%" />
<col style="width: 23%" />
<col style="width: 23%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Activity</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>MSM 486</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DSM ALPHA</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Remarks</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>TCP/IP</p>
</blockquote></td>
<td><blockquote>
<p>10 min</p>
</blockquote></td>
<td><blockquote>
<p>10 min</p>
</blockquote></td>
<td><blockquote>
<p>Times vary greatly based on line traffic; they do not apply to MSM sites receiving the data</p>
<p>on diskette.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Initialization</p>
</blockquote></td>
<td><blockquote>
<p>5 min</p>
</blockquote></td>
<td><blockquote>
<p>2 min</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

## Installation Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Preparation
    1.  We recommend that you install the software into a test account before installing it into a production account.
    2.  Users may be on the system during installation of Health Summary, but we encourage you to back up your system before you install.
    3.  Prevent Health Summary users from accessing the following Health Summary options while installing the new software by placing an OUT OF ORDER MESSAGE through the option “Restrict Availability of Options” on the Menu Management option, which is on Kernel’s EVE menu.
        - Print Health Summary Menu \[GMTS HS MENU\]
        - Health Summary Menu \[GMTS USER\]
        - Health Summary Enhanced Menu \[GMTS ENHANCED USER\]
        - Health Summary Coordinator’s Menu \[GMTS COORDINATOR\]
        - Any locally created Health Summary Menu Options
    4.  Disable routine mapping (DSM).
    5.  If you have a previous version of Health Summary installed, delete all GMTS\* routines prior to installing the new version. Remember to exclude all locally created GMTSZ\* routines.
2.  Routines

> Sign into the UCI where you plan to install Health Summary and load GMTS\* routines from the media by D ^%RR.

<table style="width:100%;">
<colgroup>
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th>GMTS</th>
<th><blockquote>
<p>GMTS1</p>
</blockquote></th>
<th>GMTS2</th>
<th>GMTSADH</th>
<th>GMTSADH1</th>
<th>GMTSADH2</th>
<th>GMTSADH3</th>
<th>GMTSADH4</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>GMTSADHC</td>
<td><blockquote>
<p>GMTSADOR</p>
</blockquote></td>
<td>GMTSALG</td>
<td>GMTSALGB</td>
<td>GMTSAMIE</td>
<td>GMTSCI</td>
<td>GMTSCM</td>
<td>GMTSCW</td>
</tr>
<tr class="even">
<td>GMTSDA</td>
<td><blockquote>
<p>GMTSDCB</p>
</blockquote></td>
<td>GMTSDD</td>
<td>GMTSDEM</td>
<td>GMTSDEMB</td>
<td>GMTSDGA</td>
<td>GMTSDGA1</td>
<td>GMTSDGA2</td>
</tr>
<tr class="odd">
<td>GMTSDGC1</td>
<td><blockquote>
<p>GMTSDGC2</p>
</blockquote></td>
<td>GMTSDGCH</td>
<td>GMTSDGD</td>
<td>GMTSDGH</td>
<td>GMTSDGP</td>
<td>GMTSDS</td>
<td>GMTSDSB</td>
</tr>
<tr class="even">
<td>GMTSDVR</td>
<td><blockquote>
<p>GMTSENV</p>
</blockquote></td>
<td>GMTSFH</td>
<td>GMTSI001</td>
<td>GMTSI002</td>
<td>GMTSI003</td>
<td>GMTSI004</td>
<td>GMTSI005</td>
</tr>
<tr class="odd">
<td>GMTSI006</td>
<td><blockquote>
<p>GMTSI007</p>
</blockquote></td>
<td>GMTSI008</td>
<td>GMTSI009</td>
<td>GMTSI00A</td>
<td>GMTSI00B</td>
<td>GMTSI00C</td>
<td>GMTSI00D</td>
</tr>
<tr class="even">
<td>GMTSI00E</td>
<td><blockquote>
<p>GMTSI00F</p>
</blockquote></td>
<td>GMTSI00G</td>
<td>GMTSI00H</td>
<td>GMTSI00I</td>
<td>GMTSI00J</td>
<td>GMTSI00K</td>
<td>GMTSI00L</td>
</tr>
<tr class="odd">
<td>GMTSI00M</td>
<td><blockquote>
<p>GMTSI00N</p>
</blockquote></td>
<td>GMTSI00O</td>
<td>GMTSI00P</td>
<td>GMTSI00Q</td>
<td>GMTSI00R</td>
<td>GMTSI00S</td>
<td>GMTSI00T</td>
</tr>
<tr class="even">
<td>GMTSI00U</td>
<td><blockquote>
<p>GMTSI00V</p>
</blockquote></td>
<td>GMTSI00W</td>
<td>GMTSI00X</td>
<td>GMTSI00Y</td>
<td>GMTSI00Z</td>
<td>GMTSI010</td>
<td>GMTSI011</td>
</tr>
<tr class="odd">
<td>GMTSI012</td>
<td><blockquote>
<p>GMTSI013</p>
</blockquote></td>
<td>GMTSI014</td>
<td>GMTSI015</td>
<td>GMTSI016</td>
<td>GMTSI017</td>
<td>GMTSI018</td>
<td>GMTSI019</td>
</tr>
<tr class="even">
<td>GMTSI01A</td>
<td><blockquote>
<p>GMTSI01B</p>
</blockquote></td>
<td>GMTSI01C</td>
<td>GMTSI01D</td>
<td>GMTSINI1</td>
<td>GMTSINI2</td>
<td>GMTSINI3</td>
<td>GMTSINI4</td>
</tr>
<tr class="odd">
<td>GMTSINI5</td>
<td><blockquote>
<p>GMTSINIS</p>
</blockquote></td>
<td>GMTSINIT</td>
<td>GMTSLOAD</td>
<td>GMTSLRA</td>
<td>GMTSLRAE</td>
<td>GMTSLRB</td>
<td>GMTSLRBE</td>
</tr>
<tr class="even">
<td>GMTSLRC</td>
<td><blockquote>
<p>GMTSLRCE</p>
</blockquote></td>
<td>GMTSLRCP</td>
<td>GMTSLREE</td>
<td>GMTSLREM</td>
<td>GMTSLRM</td>
<td>GMTSLRM1</td>
<td>GMTSLRMB</td>
</tr>
<tr class="odd">
<td>GMTSLRME</td>
<td><blockquote>
<p>GMTSLRMX</p>
</blockquote></td>
<td>GMTSLROB</td>
<td>GMTSLROE</td>
<td>GMTSLROS</td>
<td>GMTSLRPE</td>
<td>GMTSLRS</td>
<td>GMTSLRS7</td>
</tr>
<tr class="even">
<td>GMTSLRSC</td>
<td><blockquote>
<p>GMTSLRSE</p>
</blockquote></td>
<td>GMTSLRT</td>
<td>GMTSLRTE</td>
<td>GMTSLTR</td>
<td>GMTSLTR2</td>
<td>GMTSMCMA</td>
<td>GMTSMCPZ</td>
</tr>
<tr class="odd">
<td>GMTSMCZZ</td>
<td><blockquote>
<p>GMTSMHPE</p>
</blockquote></td>
<td>GMTSNTE0</td>
<td>GMTSNTEG</td>
<td>GMTSO001</td>
<td>GMTSO002</td>
<td>GMTSO003</td>
<td>GMTSO004</td>
</tr>
<tr class="even">
<td>GMTSO005</td>
<td><blockquote>
<p>GMTSO006</p>
</blockquote></td>
<td>GMTSO007</td>
<td>GMTSO008</td>
<td>GMTSO009</td>
<td>GMTSO010</td>
<td>GMTSO011</td>
<td>GMTSO012</td>
</tr>
<tr class="odd">
<td>GMTSO013</td>
<td><blockquote>
<p>GMTSO014</p>
</blockquote></td>
<td>GMTSO015</td>
<td>GMTSO016</td>
<td>GMTSO017</td>
<td>GMTSO018</td>
<td>GMTSO019</td>
<td>GMTSO020</td>
</tr>
<tr class="even">
<td>GMTSO021</td>
<td><blockquote>
<p>GMTSO022</p>
</blockquote></td>
<td>GMTSO023</td>
<td>GMTSO024</td>
<td>GMTSONI1</td>
<td>GMTSONI2</td>
<td>GMTSONI3</td>
<td>GMTSONIT</td>
</tr>
<tr class="odd">
<td>GMTSORC</td>
<td><blockquote>
<p>GMTSPCD</p>
</blockquote></td>
<td>GMTSPD</td>
<td>GMTSPD2</td>
<td>GMTSPDX</td>
<td>GMTSPDXZ</td>
<td>GMTSPL</td>
<td>GMTSPLST</td>
</tr>
<tr class="even">
<td>GMTSPLSZ</td>
<td><blockquote>
<p>GMTSPN</p>
</blockquote></td>
<td>GMTSPN1</td>
<td>GMTSPN2</td>
<td>GMTSPNB</td>
<td>GMTSPNE</td>
<td>GMTSPNJ</td>
<td>GMTSPNS</td>
</tr>
<tr class="odd">
<td>GMTSPOS1</td>
<td><blockquote>
<p>GMTSPOS2</p>
</blockquote></td>
<td>GMTSPOST</td>
<td>GMTSPP</td>
<td>GMTSPREI</td>
<td>GMTSPSG</td>
<td>GMTSPSI</td>
<td>GMTSPSO</td>
</tr>
<tr class="even">
<td>GMTSPSZO</td>
<td><blockquote>
<p>GMTSPXEP</p>
</blockquote></td>
<td>GMTSPXFP</td>
<td>GMTSPXHP</td>
<td>GMTSPXHR</td>
<td>GMTSPXIM</td>
<td>GMTSPXM</td>
<td>GMTSPXMP</td>
</tr>
<tr class="odd">
<td>GMTSPXOP</td>
<td><blockquote>
<p>GMTSPXSK</p>
</blockquote></td>
<td>GMTSPXTP</td>
<td>GMTSPXU1</td>
<td>GMTSPXU2</td>
<td>GMTSPXXP</td>
<td>GMTSRAD</td>
<td>GMTSRAE</td>
</tr>
<tr class="even">
<td>GMTSRAI</td>
<td><blockquote>
<p>GMTSRAS</p>
</blockquote></td>
<td>GMTSRASP</td>
<td>GMTSRI</td>
<td>GMTSRM</td>
<td>GMTSRM1</td>
<td>GMTSRM1A</td>
<td>GMTSRM2</td>
</tr>
<tr class="odd">
<td>GMTSRM3</td>
<td><blockquote>
<p>GMTSRM4</p>
</blockquote></td>
<td>GMTSRM5</td>
<td>GMTSRN</td>
<td>GMTSRO</td>
<td>GMTSROB</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>GMTSU</td>
<td><blockquote>
<p>GMTSUP</p>
</blockquote></td>
<td>GMTSUP1</td>
<td>GMTSVS</td>
<td>GMTSVSS</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="8"><blockquote>
<p>211 routines restored</p>
</blockquote></td>
</tr>
</tbody>
</table>

3.  Run the GMTSNTEG routine.
4.  Disable journaling (DSM).
5.  D ^XUP and D Q^DI

> D ^XUP and D Q^DI to ensure required variables are defined prior to starting initialization. A message informing you that the environment is not appropriately initialized will appear if your DUZ is not set to a valid user number and DUZ(0) does not equal "@".

6.  D ^GMTSINIT

> See installation examples on the next pages. GMTSINIT contains an environment check, pre-init, and post-init routines.

7.  Post-Installation
    1.  Clean up your system by deleting GMTSI\*, GMTSON\*, GMTSPREI, and GMTSO0\* routines.
    2.  DSM sites with multiple CPUs and all MSM sites: Copy all Health Summary routines and package routines sent out with Health Summary to each system after the init is completed, according to the table below:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package</strong></p>
</blockquote></th>
<th><strong>Routine(s)</strong></th>
<th><blockquote>
<p><strong>Comments</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Health Summary</p>
</blockquote></td>
<td>GMTS*</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Problem List</p>
</blockquote></td>
<td>GMPLHS</td>
<td><blockquote>
<p>If Problem List 2.0 is installed</p>
</blockquote></td>
</tr>
</tbody>
</table>

3.  Re-enable journaling and routine mapping (DSM). We recommend mapping the GMTS\* routines (excluding init and onit routines) to optimize system performance.
4.  Set up the Health Summary package according to site requirements.
5.  Remove the OUT OF ORDER message from the Health Summary options, to enable Health Summary option use.
    - Print Health Summary Menu \[GMTS HS MENU\]
    - Health Summary Menu \[GMTS USER\]
    - Health Summary Enhanced Menu \[GMTS ENHANCED USER\]
    - Health Summary Coordinator’s Menu \[GMTS COORDINATOR\]
    - Any locally created Health Summary Menu Options
6.  Inform your users that Health Summary V. 2.7 is available for use.

## Installation Over Version 2.5 Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section shows the terminal dialogue seen during installation of Health Summary V. 2.7 in a Health Summary V. 2.5 account.

\>D ^GMTSINIT

> This version (#2.7) of 'GMTSINIT' was created on 19-OCT-1995 (at ISCSLC, by VA FileMan V.21.0)

> I HAVE TO RUN AN ENVIRONMENT CHECK ROUTINE. I AM GOING TO SET UP THE FOLLOWING FILES:

> 142 HEALTH SUMMARY TYPE (including data) Note: You already have the 'HEALTH SUMMARY TYPE' File. I will OVERWRITE your data with mine.

> 142.1 HEALTH SUMMARY COMPONENT (including data) Note: You already have the 'HEALTH SUMMARY COMPONENT' File. I will OVERWRITE your data with mine.

> 142.99 HEALTH SUMMARY PARAMETERS

> Note: You already have the 'HEALTH SUMMARY PARAMETERS' File.

> SHALL I WRITE OVER FILE SECURITY CODES? No// \<RET\>(No)

> NOTE: This package also contains SORT TEMPLATES

> SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME?

> Yes// \<RET\>(Yes)

> NOTE: This package also contains INPUT TEMPLATES

> SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME?

> Yes// \<RET\>(Yes)

> NOTE: This package also contains PRINT TEMPLATES

> SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME?

> Yes// \<RET\>(Yes)

> NOTE: This package also contains FUNCTIONS

> SHALL I WRITE OVER EXISTING FUNCTIONS OF THE SAME NAME? Yes// \<RET\>(Yes)

> NOTE: This package also contains SECURITY KEYS

> SHALL I WRITE OVER EXISTING SECURITY KEYS OF THE SAME NAME? Yes// \<RET\>(Yes)

> NOTE: This package also contains OPTIONS

> SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? Yes// \<RET\>(Yes) ARE YOU SURE EVERYTHING'S OK? No// Y (Yes)

> First I need to run a pre-init....

> Starting pre-init now....

> \*\* Renaming Medicine Summary Abbreviation from MED to MEDS \*\* Deleting field \# 2 in the Health Summary Type (#142) file.

> Deleting field \# 3 in the Health Summary Type (#142) file. Deleting field \# 4 in the Health Summary Type (#142) file. Deleting field \# 5 in the Health Summary Type (#142) file. Deleting field \# 6 in the Health Summary Type (#142) file. Pre-init successfully completed!

> ...SORRY, THIS MAY TAKE A FEW MOMENTS...........................................

> ....................................................

> 'GMTS BUILD MENU' Option Filed 'GMTS COMP DESC LIST' Option Filed 'GMTS COMP INQ' Option Filed

> 'GMTS COMP LIST' Option Filed 'GMTS COORDINATOR' Option Filed 'GMTS ENHANCED USER' Option Filed 'GMTS HS ADHOC' Option Filed

> 'GMTS HS BY LOC' Option Filed

> 'GMTS HS BY LOC PARAMETERS' Option Filed

> 'GMTS HS BY PATIENT' Option Filed

> 'GMTS HS BY PATIENT & DATE RANG' Option Filed 'GMTS HS BY PATIENT & VISIT' Option Filed 'GMTS HS FOR ALL CLINICS' Option Filed

> 'GMTS HS MENU' Option Filed

> 'GMTS INFO ONLY MENU' Option Filed

> 'GMTS IRM/ADPAC ADHOC EDIT' Option Filed 'GMTS IRM/ADPAC ADHOC LOAD' Option Filed 'GMTS IRM/ADPAC COMP EDIT' Option Filed 'GMTS IRM/ADPAC ENABLE/DISABLE' Option Filed 'GMTS IRM/ADPAC MAINT MENU' Option Filed 'GMTS IRM/ADPAC PARAMETER EDIT' Option Filed

> 'GMTS IRM/ADPAC TYPE RESEQUENCE' Option Filed

> 'GMTS MANAGER' Option Filed

> 'GMTS TASK LOCATIONS LIST' Option Filed

> 'GMTS TASK STARTUP' Option Filed 'GMTS TYPE DELETE' Option Filed 'GMTS TYPE ENTER/EDIT' Option Filed 'GMTS TYPE INQ' Option Filed

> 'GMTS TYPE LIST' Option Filed

> 'GMTS USER' Option Filed...............

> NO SECURITY-CODE PROTECTION HAS BEEN MADE

> Starting post-init action now....

> Converting SPOOL to a pointer value for Spool Device in Site Parameter file. SPOOL converted successfully.

> \*\* Installing GMPLHS routine for Problem List components. \*\* Renaming GMTSPLSZ as GMPLHS.. Done.

> PCE LOCATION OF HOME Health Summary Component disabled PCE CLINICAL REMINDERS Health Summary Component disabled

> PCE HEALTH FACTORS SELECTED Health Summary Component disabled PCE HEALTH FACTORS ALL Health Summary Component disabled

> PCE OUTPATIENT ENCOUNTERS Health Summary Component disabled PCE MEASUREMENTS NON-TABULAR Health Summary Component disabled PCE IMMUNIZATIONS Health Summary Component disabled

> PCE SKIN TESTS Health Summary Component disabled

> PCE MEASUREMENTS SELECTED Health Summary Component disabled PCE EDUCATION Health Summary Component disabled

> PCE EDUCATION LATEST Health Summary Component disabled

> PCE OUTPATIENT DIAGNOSIS Health Summary Component disabled PCE EXAMS LATEST Health Summary Component disabled

> PCE TREATMENTS PROVIDED Health Summary Component disabled PCE CLINICAL MAINTENANCE Health Summary Component disabled

> \*\* Installing GMTSMCPS routine for Medicine 2.2 components. \*\* Renaming GMTSMCZZ as GMTSMCPS. Done.

> \*\* Installing PDX Data Segments for Health Summary Components \*\*

> Pce Health Factors All added to VAQ - DATA SEGMENT file (#394.71). Pce Outpatient Encounters added to VAQ - DATA SEGMENT file (#394.71).

> Pce Measurements Non-tabular added to VAQ - DATA SEGMENT file (#394.71). Pce Immunizations added to VAQ - DATA SEGMENT file (#394.71).

> Pce Skin Tests added to VAQ - DATA SEGMENT file (#394.71). Pce Education added to VAQ - DATA SEGMENT file (#394.71).

> Pce Education Latest added to VAQ - DATA SEGMENT file (#394.71).

> Pce Outpatient Diagnosis added to VAQ - DATA SEGMENT file (#394.71). Pce Exams Latest added to VAQ - DATA SEGMENT file (#394.71).

> Pce Treatments Provided added to VAQ - DATA SEGMENT file (#394.71). Compensation And Pension Exams added to VAQ - DATA SEGMENT file (#394.71).

> Discharge Summary already exists in VAQ - DATA SEGMENT file Discharge Summary Brief already exists in VAQ - DATA SEGMENT file

> Mas Adt History Expanded added to VAQ - DATA SEGMENT file (#394.71). Medicine Abnormal Brief added to VAQ - DATA SEGMENT file (#394.71). Medicine Brief Report added to VAQ - DATA SEGMENT file (#394.71).

> Medicine Full Captioned added to VAQ - DATA SEGMENT file (#394.71). Medicine Full Report added to VAQ - DATA SEGMENT file (#394.71).

> Problem List All added to VAQ - DATA SEGMENT file (#394.71). Problem List Active added to VAQ - DATA SEGMENT file (#394.71). Problem List Inactive added to VAQ - DATA SEGMENT file (#394.71).

> Mental Health Physical Exam added to VAQ - DATA SEGMENT file (#394.71).

> Lab Electron Microscopy added to VAQ - DATA SEGMENT file (#394.71). Adverse Reactions/allerg Brief added to VAQ - DATA SEGMENT file (#394.71).

> Done installing PDX Data Segments....

> 'C' cross-reference on the GMTS AD HOC OPTION type in file 142 deleted. It will be rebuilt

> Rebuilding Ad Hoc Summary.......................................................

> .........

> Done.

> This version of 'GMTSONIT' was created on 19-OCT-1995 (at ISCSLC, by OE/RR V.2.5)

> PROTOCOL INSTALLATION

> ...OK, this may take a while, hold on please....................................

> ..................................................................

> 'GMTS ADC' Protocol Filed 'GMTS ADR' Protocol Filed 'GMTS ADT' Protocol Filed 'GMTS BADR' Protocol Filed 'GMTS BDEM' Protocol Filed 'GMTS BDS' Protocol Filed 'GMTS BLO' Protocol Filed 'GMTS BMIC' Protocol Filed 'GMTS BPN' Protocol Filed 'GMTS BSR' Protocol Filed 'GMTS BT' Protocol Filed 'GMTS CD' Protocol Filed 'GMTS CH' Protocol Filed 'GMTS CN' Protocol Filed

> 'GMTS COMP DESC LIST' Protocol Filed 'GMTS COMP INQ' Protocol Filed

> 'GMTS COMP LIST' Protocol Filed 'GMTS CP' Protocol Filed

> 'GMTS CVF' Protocol Filed 'GMTS CVP' Protocol Filed 'GMTS CW' Protocol Filed 'GMTS CY' Protocol Filed 'GMTS DC' Protocol Filed 'GMTS DCS' Protocol Filed 'GMTS DD' Protocol Filed 'GMTS DEM' Protocol Filed 'GMTS DIET' Protocol Filed 'GMTS DS' Protocol Filed 'GMTS EADT' Protocol Filed 'GMTS ED' Protocol Filed 'GMTS EDL' Protocol Filed 'GMTS EM' Protocol Filed 'GMTS EXAM' Protocol Filed 'GMTS HF' Protocol Filed

> 'GMTS HS ADHOC' Protocol Filed 'GMTS HS BY LOC' Protocol Filed 'GMTS HS BY PATIENT' Protocol Filed 'GMTS IM' Protocol Filed

> 'GMTS INFO ONLY MENU' Protocol Filed 'GMTS LH' Protocol Filed

> 'GMTS LO' Protocol Filed 'GMTS MED' Protocol Filed 'GMTS MEDA' Protocol Filed 'GMTS MEDB' Protocol Filed 'GMTS MEDC' Protocol Filed 'GMTS MEDF' Protocol Filed 'GMTS MHPE' Protocol Filed 'GMTS MIC' Protocol Filed 'GMTS NTM' Protocol Filed 'GMTS OD' Protocol Filed 'GMTS OE' Protocol Filed 'GMTS OPC' Protocol Filed 'GMTS ORC' Protocol Filed 'GMTS PLA' Protocol Filed 'GMTS PLI' Protocol Filed 'GMTS PLL' Protocol Filed 'GMTS PN' Protocol Filed 'GMTS PRC' Protocol Filed 'GMTS RI' Protocol Filed 'GMTS RP' Protocol Filed 'GMTS RS' Protocol Filed 'GMTS RXIV' Protocol Filed 'GMTS RXOP' Protocol Filed 'GMTS RXUD' Protocol Filed 'GMTS SP' Protocol Filed 'GMTS SR' Protocol Filed 'GMTS ST' Protocol Filed 'GMTS TP' Protocol Filed 'GMTS TR' Protocol Filed 'GMTS TS' Protocol Filed

> 'GMTS TYPE INQUIRE' Protocol Filed 'GMTS TYPE LIST' Protocol Filed 'GMTS USER' Protocol Filed

> 'GMTS VS' Protocol Filed

> OK, Protocol Installation is Complete. Post-init successfully completed.

> HEALTH SUMMARY VERSION 2.7 INITIALIZATION COMPLETE!

### First Time Installation Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### This section shows the terminal dialogue seen during installation of Health Summary V. 2.7 in an account with no previously installed version of Health Summary.

> 'GMTS HS BY PATIENT & VISIT' Option Filed 'GMTS HS FOR ALL CLINICS' Option Filed

> 'GMTS HS MENU' Option Filed

> 'GMTS INFO ONLY MENU' Option Filed

> 'GMTS IRM/ADPAC ADHOC EDIT' Option Filed 'GMTS IRM/ADPAC ADHOC LOAD' Option Filed 'GMTS IRM/ADPAC COMP EDIT' Option Filed 'GMTS IRM/ADPAC ENABLE/DISABLE' Option Filed 'GMTS IRM/ADPAC MAINT MENU' Option Filed 'GMTS IRM/ADPAC PARAMETER EDIT' Option Filed

> 'GMTS IRM/ADPAC TYPE RESEQUENCE' Option Filed

> 'GMTS MANAGER' Option Filed

> 'GMTS TASK LOCATIONS LIST' Option Filed

> 'GMTS TASK STARTUP' Option Filed 'GMTS TYPE DELETE' Option Filed 'GMTS TYPE ENTER/EDIT' Option Filed 'GMTS TYPE INQ' Option Filed

> 'GMTS TYPE LIST' Option Filed

> 'GMTS USER' Option Filed...............

> NOTE THAT FILE SECURITY-CODE PROTECTION HAS BEEN MADE

> Starting post-init action now....

> \*\* Installing GMPLHS routine for Problem List components. \*\* Renaming GMTSPLSZ as GMPLHS.. Done.

> PCE LOCATION OF HOME Health Summary Component disabled PCE CLINICAL REMINDERS Health Summary Component disabled

> PCE HEALTH FACTORS SELECTED Health Summary Component disabled PCE HEALTH FACTORS ALL Health Summary Component disabled

> PCE OUTPATIENT ENCOUNTERS Health Summary Component disabled PCE MEASUREMENTS NON-TABULAR Health Summary Component disabled PCE IMMUNIZATIONS Health Summary Component disabled

> PCE SKIN TESTS Health Summary Component disabled

> PCE MEASUREMENTS SELECTED Health Summary Component disabled PCE EDUCATION Health Summary Component disabled

> PCE EDUCATION LATEST Health Summary Component disabled

> PCE OUTPATIENT DIAGNOSIS Health Summary Component disabled PCE EXAMS LATEST Health Summary Component disabled

> PCE TREATMENTS PROVIDED Health Summary Component disabled PCE CLINICAL MAINTENANCE Health Summary Component disabled

> \*\* Installing GMTSMCPS routine for Medicine 2.2 components. \*\* Renaming GMTSMCZZ as GMTSMCPS. Done.

> \*\* Installing PDX Data Segments for Health Summary Components \*\*

> Pce Health Factors All added to VAQ - DATA SEGMENT file (#394.71). Pce Outpatient Encounters added to VAQ - DATA SEGMENT file (#394.71).

> Pce Measurements Non-tabular added to VAQ - DATA SEGMENT file (#394.71). Pce Immunizations added to VAQ - DATA SEGMENT file (#394.71).

> Pce Skin Tests added to VAQ - DATA SEGMENT file (#394.71). Pce Education added to VAQ - DATA SEGMENT file (#394.71).

> Pce Education Latest added to VAQ - DATA SEGMENT file (#394.71).

> Pce Outpatient Diagnosis added to VAQ - DATA SEGMENT file (#394.71). Pce Exams Latest added to VAQ - DATA SEGMENT file (#394.71).

> Pce Treatments Provided added to VAQ - DATA SEGMENT file (#394.71).

> Compensation And Pension Exams added to VAQ - DATA SEGMENT file (#394.71). Discharge Summary added to VAQ - DATA SEGMENT file (#394.71).

> Discharge Summary Brief added to VAQ - DATA SEGMENT file (#394.71). Mas Adt History Expanded added to VAQ - DATA SEGMENT file (#394.71). Medicine Abnormal Brief added to VAQ - DATA SEGMENT file (#394.71). Medicine Brief Report added to VAQ - DATA SEGMENT file (#394.71).

> Medicine Full Captioned added to VAQ - DATA SEGMENT file (#394.71). Medicine Full Report added to VAQ - DATA SEGMENT file (#394.71).

> Problem List All added to VAQ - DATA SEGMENT file (#394.71). Problem List Active added to VAQ - DATA SEGMENT file (#394.71). Problem List Inactive added to VAQ - DATA SEGMENT file (#394.71).

> Mental Health Physical Exam added to VAQ - DATA SEGMENT file (#394.71).

> Lab Electron Microscopy added to VAQ - DATA SEGMENT file (#394.71). Adverse Reactions/allerg Brief added to VAQ - DATA SEGMENT file (#394.71).

> Done installing PDX Data Segments....

> 'C' cross-reference on the GMTS AD HOC OPTION type in file 142 deleted. It will be rebuilt

> Rebuilding Ad Hoc Summary.......................................................

> Done.

> This version of 'GMTSONIT' was created on 19-OCT-1995 (at ISCSLC, by OE/RR V.2.5)

> PROTOCOL INSTALLATION

> ...OK, this may take a while, hold on please....................................

> ..................................................................

> 'GMTS ADC' Protocol Filed 'GMTS ADR' Protocol Filed 'GMTS ADT' Protocol Filed 'GMTS BADR' Protocol Filed 'GMTS BDEM' Protocol Filed 'GMTS BDS' Protocol Filed 'GMTS BLO' Protocol Filed 'GMTS BMIC' Protocol Filed 'GMTS BPN' Protocol Filed 'GMTS BSR' Protocol Filed 'GMTS BT' Protocol Filed 'GMTS CD' Protocol Filed 'GMTS CH' Protocol Filed 'GMTS CN' Protocol Filed

> 'GMTS COMP DESC LIST' Protocol Filed 'GMTS COMP INQ' Protocol Filed

> 'GMTS COMP LIST' Protocol Filed 'GMTS CP' Protocol Filed

> 'GMTS CVF' Protocol Filed 'GMTS CVP' Protocol Filed 'GMTS CW' Protocol Filed 'GMTS CY' Protocol Filed

> 'GMTS DC' Protocol Filed 'GMTS DCS' Protocol Filed 'GMTS DD' Protocol Filed 'GMTS DEM' Protocol Filed 'GMTS DIET' Protocol Filed 'GMTS DS' Protocol Filed 'GMTS EADT' Protocol Filed 'GMTS ED' Protocol Filed 'GMTS EDL' Protocol Filed 'GMTS EM' Protocol Filed 'GMTS EXAM' Protocol Filed 'GMTS HF' Protocol Filed

> 'GMTS HS ADHOC' Protocol Filed

> GMTS HS ADHOC added as item to OR OE/RR MENU CLINICIAN. GMTS HS ADHOC added as item to OR OE/RR MENU NURSE.

> GMTS HS ADHOC added as item to OR OE/RR MENU WARD CLERK. 'GMTS HS BY LOC' Protocol Filed

> 'GMTS HS BY PATIENT' Protocol Filed 'GMTS IM' Protocol Filed

> 'GMTS INFO ONLY MENU' Protocol Filed

> GMTS COMP DESC LIST added as item to GMTS INFO ONLY MENU.

> GMTS COMP INQ added as item to GMTS INFO ONLY MENU. GMTS COMP LIST added as item to GMTS INFO ONLY MENU. GMTS TYPE INQUIRE added as item to GMTS INFO ONLY MENU.

> GMTS TYPE LIST added as item to GMTS INFO ONLY MENU. 'GMTS LH' Protocol Filed

> 'GMTS LO' Protocol Filed 'GMTS MED' Protocol Filed 'GMTS MEDA' Protocol Filed 'GMTS MEDB' Protocol Filed 'GMTS MEDC' Protocol Filed 'GMTS MEDF' Protocol Filed 'GMTS MHPE' Protocol Filed 'GMTS MIC' Protocol Filed 'GMTS NTM' Protocol Filed 'GMTS OD' Protocol Filed 'GMTS OE' Protocol Filed 'GMTS OPC' Protocol Filed 'GMTS ORC' Protocol Filed 'GMTS PLA' Protocol Filed 'GMTS PLI' Protocol Filed 'GMTS PLL' Protocol Filed 'GMTS PN' Protocol Filed 'GMTS PRC' Protocol Filed 'GMTS RI' Protocol Filed 'GMTS RP' Protocol Filed 'GMTS RS' Protocol Filed 'GMTS RXIV' Protocol Filed 'GMTS RXOP' Protocol Filed 'GMTS RXUD' Protocol Filed 'GMTS SP' Protocol Filed 'GMTS SR' Protocol Filed 'GMTS ST' Protocol Filed 'GMTS TP' Protocol Filed 'GMTS TR' Protocol Filed 'GMTS TS' Protocol Filed

> 'GMTS TYPE INQUIRE' Protocol Filed 'GMTS TYPE LIST' Protocol Filed 'GMTS USER' Protocol Filed

> GMTS HS ADHOC added as item to GMTS USER. GMTS HS BY LOC added as item to GMTS USER.

> GMTS HS BY PATIENT added as item to GMTS USER. GMTS INFO ONLY MENU added as item to GMTS USER.

> 'GMTS VS' Protocol Filed

> OK, Protocol Installation is Complete.

## Setting up Health Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Security Key Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The GMTSMGR security key allows holders to override the LOCK and OWNER access restrictions for editing health summary types. The IRM Chief and Health Summary Coordinators are likely key holders.

> This security key allows the holder to edit general usage health summary types which are locked with the GMTSMGR key. It also provides master edit access to all other health summary types.

> The GMTS VIEW ONLY Security Key allows holders to view a health summary on the CRT. Holders may use all the familiar Health Summary options but will not be prompted for a device for printing paper copies of the health summary.

### Menu Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  If IRM staff members or the Clinical Coordinator need access to all menus, give them the Health Summary Overall Menu \[GMTS MANAGER\] rather than assigning each menu option separately.
2.  Give the Health Summary Menu \[GMTS USER\] menu to users who only need to print or display health summaries.
3.  Give the Health Summary Enhanced Menu \[GMTS ENHANCED USER\] menu to users who need to create, modify, or delete their own health summary types, in addition to printing health summaries.
4.  Give the Health Summary Coordinator’s Menu \[GMTS COORDINATOR\] menu to users who need to print or display health summaries, and who will also need to create, modify, or delete health summary types, and set up nightly batch printing at specified locations.
5.  Give the Health Summary Maintenance Menu \[GMTS IRM/ADPAC MAINT MENU\] to IRM staff or the Clinical Coordinator for any implementation and maintenance issues in Health Summary. This menu contains options to disable/enable health summary components for selection/display, create/modify new health summary components, edit and rebuild the Ad Hoc Health Summary Type, resequence the components in a health summary

> type, create/modify a health summary type, delete a health summary type, and edit health summary site parameters.

### Disable/Enable Health Summary Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

6.  *Disable*

> Disable those Health Summary components that you don’t intend to use. Confer with your coordinator and use the Component Checklist in Appendix A or print a list using the List Health Summary Components \[GMTS COMP LIST\] option to help you determine which components may need disabling. Use the List Health Summary Component Descriptions \[GMTS COMP DESC LIST\] option to print a full description of the contents of each component, if necessary, and then use the Disable/Enable Health Summary Components \[GMTS IRM/ADPAC ENABLE/DISABLE\] option to disable the components.

> When disabling a component, you have the choice of temporarily or permanently disabling it. When a component is permanently disabled, a user doesn’t know of its existence, because it is not displayed during user interaction or in printouts. A component that is temporarily disabled is non-selectable but is displayed to the user with a helpful message.

> *Example*

> Enter “@” at the DISABLE FLAG prompt to delete a permanent or temporary disable flag.

7.  *Enable*

> Use the Disable/Enable Health Summary Components \[GMTS IRM/ADPAC ENABLE/DISABLE\] option to enable any disabled components you plan to use.

> If you’ve enabled or disabled any components, use the Rebuild Ad Hoc Health Summary Type \[GMTS IRM/ADPAC ADHOC LOAD\] option in the Health Summary Maintenance Menu \[GMTS IRM/ADPAC MAINT MENU\] option, so that components you have disabled won’t be selectable by users.

> NOTE: Whenever your site creates or modifies components run the Rebuild Ad Hoc Health Summary Type \[GMTS IRM/ADPAC ADHOC LOAD\] option to rebuild the Ad Hoc Health Summary type so that it will include all new and modified components.

> *Example*

### Review site parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the Edit Health Summary Site Parameters option in the Health Summary Maintenance Menu \[GMTS IRM/ADPAC MAINT MENU\] to review and set up the site parameters. These parameters allow you to:

- Print an Outpatient Pharmacy Action Profile in tandem with a health summary printing.
- Print bar codes when Action Profiles are printed.
- Present Lab comments at display or the !! symbol indicating comments are available for the Lab Chemistry and Hematology, the Lab Cumulative Selected, and the Lab Tests Selected components.
- Specify a spool device where PDX requests will be stored.

> *Example*

> Select Health Summary Maintenance Menu Option: 7 Edit Health Summary Site Parameters

> Select HEALTH SUMMARY PARAMETERS: ?

> ANSWER WITH HEALTH SUMMARY PARAMETERS NAME: HOSPITAL

> YOU MAY ENTER A NEW HEALTH SUMMARY PARAMETERS, IF YOU WISH NAME MUST BE HOSPITAL

> Select HEALTH SUMMARY PARAMETERS: HOSPITAL

> PROMPT FOR ACTION PROFILE: YES// ??

> If this parameter is set to Y or YES, the user will be prompted to include the Outpatient Pharmacy Action Profile when printing Health

> Summaries by location (both interactive and batch mode) and by patient. CHOOSE FROM:

> Y yes

> N no

> PROMPT FOR ACTION PROFILE: YES// Y YES INCLUDE BAR CODES ON ACTION PROFILES: ?

> Enter YES to include bar cod es when Action Profiles are printed by Health Summary.

> Choose from:

> Y yes

> N no

> INCLUDE BAR CODES ON ACTION PROFILES: YES// \<RET\> YES

> INCLUDE COMMENTS FOR LABS: YES// ??

> If this parameter is set to Y or YES, the Chemistry & Hematology , the Lab Tests Selected, and the Lab Cumulative Selected components will present comments for results. For the Chemistry & Hematology and the Lab Tests Selected components, the comments will be displayed

> immediately following the results. For the Lab Cumulative Selected components, a lower-case letter will be displayed to the left of the date for entries with comments. Comments will be displayed after all the results are displayed, with the comments linked by the lower-case letter. Up to 26 comments can be included.

> If blank, N or NO, the Chemistry & Hematology and the Lab Tests component s will present the symbol "!!" next to tests which include

> comments, and a footnote referring the user to the Lab Interim Report. CHOOSE FROM:

> Y yes

> N no

> INCLUDE COMMENTS FOR LABS: YES// \<RET\> YES SPOOL DEVICE: SPOOL// ??

> This is the SPOOL DEVICE to which Health Summary output can be directed during a PDX request for one or more Health Summary components.

> Choose from:

> SPOOL SPOOL TO VMS DSAB:\[MUMPS,DEVMGR\]

> SPOOL DEVICE: SPOOL

> Select HEALTH SUMMARY PARAMETERS: \<RET\>

### Customize the Ad Hoc Health Summary type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You may customize this health summary type by modifying time and occurrence limits, assigning Selection Items (tests like WBC, Glucose) to the selected Health Summary components (Lab Cumulative Selected, Lab Cumulative Selected 1-4, Lab Tests Selected, Vital Signs Selected, Radiology Impression Selected, PCE Health Factors Selected, and PCE Measurements Selected), or entering Header Names for components.

> The Problem List components and some of the new PCE components give you the option of determining if the hospital location should be displayed, if ICD text should be long, short, code, or none, and if provider narrative should be displayed.

> To help you customize Health Summary components, an *example* of some Selection Item assignments and the dialogue is shown here.

> You may select individual components and edit their default parameters, or use the ^LOOP feature at the Select COMPONENT: prompt to loop through all of the components, editing the default values as you go.

> NOTE: When selecting components from the Ad Hoc Health Summary menu, entering “ALL” allows all components to be selected. If the first three characters of a HEADER NAME for a component are designated as “All,” however, then only the defined component will be selected. Avoid conflicts and loss of functionality by not using “all” at the front of new header names.

> *Example:*

> Choose from:

> L long text

> S short text

> C code only

> T text only

> N none

> ICD TEXT DISPLAYED: S short text PROVIDER NARRATIVE DISPLAYED: ??

> This field controls whether provider narrative is displayed or not. It applies to components where provider narrative is applicable (e.g., PCE Outpatient Encounters, PCE Outpatient Diagnosis, Problem List All). This control is independent of whether or not ICD text is displayed -- either or both may be specified. If not specified, provider narrative will be displayed by default.

> Choose from:

> Y yes

> N no

> PROVIDER NARRATIVE DISPLAYED: Y yes

> HEADER NAME: Active Problems// \<RET\>

> Do you wish to review the Summary Type structure before continuing? NO// YES

HEALTH SUMMARY TYPE INQUIRY

> Type Name: GMTS HS ADHOC OPTION

> Title: Ad Hoc Health Summary Type

Owner: LOCK: GMTSMGR

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA:

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 25%" />
<col style="width: 34%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"></th>
<th><blockquote>
<p>Max Hosp ICD</p>
</blockquote></th>
<th><blockquote>
<p>Prov</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Abb. Order</td>
<td><blockquote>
<p>Component Name</p>
</blockquote></td>
<td><blockquote>
<p>Occ Time Loc Text</p>
</blockquote></td>
<td><blockquote>
<p>Narr Selection</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ------------------------------------------------------------------------------

> PLA 5 Active Problems short yes

> \* = Disabled Components Select COMPONENT: \<RET\>

### Schedule batch printing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the Schedule/Unschedule option on the Task Manager menu to schedule the GMTS TASK STARTUP option for batch printing. Identify the date and time you want this option to be started.

> The Health Summary package allows coordinators to schedule nightly batch processing of health summaries for patients in a particular ward, patients in outpatient clinics, or patients scheduled for operating room surgeries the following day or up to ten days ahead. The advantages of Batch processing are

> 1\) it enables the clinic to have the most current clinical information available when the patient arrives for the appointment, and 2) processing can take place in non-peak computer hours.

> *Example*

### Set up Batch Print Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the Set-up Batch Print Location \[GMTS HS BY LOC PARAMETERS\] option to assign Health Summary types so that they coincide with the batch prints required for all patients at a specific hospital location.

> This option lets you set, edit, or delete parameters that will be used to print batches of health summaries of a specific type, in a particular hospital location. Only one set of parameters exists for a particular location and patient.

> *Example*

> <u>RELEASE NOTES</u>

## Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> New components which display information gathered by the Patient Care Encounter (PCE) package

- Clinical Maintenance ♦ Location of Home
- Clinical Reminders ♦ Measurement Selected
- Education ♦ Non-Tabular Measurements
- Education Latest ♦ Outpatient Diagnosis
- Exams latest ♦ Outpatient Encounter
- Health Factors ♦ Skin Tests
- Health Factors Select ♦ Treatments Provided
- Immunizations

> Other new components included in Health Summary V. 2.7

- Electron Microscopy component
- Four new Medicine components for Medicine V. 2.2 (E3R#s 581, 694, and 4545,)
- A Mental Health physical exam component
- Compensation & Pension Exam component (E3R# 983)
- Expanded ADT History Component that consolidates into one component the D/C Diagnosis, Procedures, LOS, Treating Specialty, and Transfer information (E3R# 814)
- Brief Adverse Reaction/Allergy component

> New Features

- An option has been added, Range of Dates Patient Health Summary, that allows data to be printed for a given date range. Users can select the beginning or ending date and a Health Summary type. For components within the Health Summary type that allow time limits, only data within the date range chosen by the user will be seen. (E3R# 4502)
- An option has been added, Visit Patient Health Summary, that allows the data to be printed for the date of a given outpatient visit or date range for a given inpatient visit.
- An option has been added, Batch Print of All Clinics by Visit Date, to interactively print Health Summary types and clinics defined by the Hospital Location parameters. Users can choose the date of the clinics and specify when to queue the print. (E3R# 862)
- The nightly batch job has been enhanced to recognize non-workdays (weekends and holidays). Data will not be printed out on non-workdays. For example, if you want a Health Summary type printed out for Monday clinics one day in advance, it will now print on the previous Friday rather than on Sunday. (E3R#s 1799 and 4213)
- The Dietetic component now includes Dietetic Encounters. (E3R#s 763 and 765)
- A site parameter has been added to allow sites to specify whether or not to print bar codes on Action Profiles which are queued to print with Health Summaries (dependent on whether the desired printer is set up to print bar codes). (E3R# 5778, NOIS# NOP-1294-10102)
- Users can now print Action Profiles in tandem with Health Summary, by patient, as well as by clinic or location. (E3R# 6568)
- The Radiology components have been modified to print only Radiology impressions that have been verified. (E3R# 5880, NOIS# BRX-1194- 10351)
- The Problem List components have been enhanced to display problems in the same order as in the Problem List package. These components will also include the Comment field and sites may specify the format for ICD9 text and Provider Narrative. (E3R#s 5546 and 6004)
- The Microbiology component has been expanded to include comments, AFB smear results, test names, and smear/prep results. (E3R#s 4069, 5480, and 6394)
- When no data is available for components that allow for the selection of certain types of data, the “No Data Available” message will now specify the selection items also. (E3R# 4313)
- Users can now select multiple locations to queue to print at the same time for the Hospital Location option. (E3R# 1244)
- The MAS Admission/Discharge component now includes Scheduled Admissions. (E3R# 1283)
- When no data is available for a component in a Health Summary type, the Health Summary Type can now be set up to suppress the “No Data Available” message and component header for printed (but not displayed) health summaries. (E3R# 1729)
- The Outpatient Pharmacy component has been enhanced to display only active medications. This can be done by excluding the time limit for the component. (E3R#s 2565 and 3860)
- Users can now pick multiple patients prior to printing a Health Summary type. (E3R# 4928)
- The Lab Cum Selected Components results will now be displayed according to the print code that is set up for a particular test result, to be consistent with the way results are displayed in the Lab package. (E3R# 5424)
- Word-wrap problems with the Progress Notes component have been corrected, to allow “full-screen” display. (NOIS#s TOM-0795-42380 and LOU-1293-30053)
- The wording for a prompt in the Ad Hoc Health Summary was changed to make it easier for users to understand how to change occurrence limits, time limits or add items. (E3R# 6522)

> *Old wording*:

> Select Additional or Existing COMPONENT(S) to ADD or EDIT:

> *New wording*:

> Select COMPONENT(S) to EDIT or other COMPONENT(S) to ADD:

- An APIMAIN^GMTSADORwas created to allow programmers to define components and defaults through the Ad Hoc menu interface and print health summaries for a programmer-specified patient and device. Use of this API by other packages requires a Database Integration Agreement. (E3R# 6734)
- Display of Lab components was changed back to the way it was in Health Summary V. 1.2, to base occurrence limits on total number of occurrences rather than on each atomic test of a panel. (NOIS# MAD-0494-40110 and E3R# 0293)

> NOTE: Other issues and problems identified in NOIS calls (BIL-0895-31476, MAC-0795- 60037, MAD-0695-40375, BOI-0595-50198, TOG-10186-30068, REN-0495-60020, AMA-

> 0395-70286, and AUG-0595-30068) have also been resolved with this version of Health Summary (these are mostly technical bugs that have been fixed).

### Changes to Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New fields

> *Health Summary Type File (#142)*

- .08 SUPPRESS COMP WITHOUT DATA

> Three new fields in the STRUCTURE multiple field (*\#142.01*):

- 6 HOSPITAL LOCATION DISPLAYED
- 7 ICD TEXT DISPLAYED
- 8 PROVIDER NARRATIVE DISPLAYED

> *Health Summary Component File (#142.1)*

- 10 HOSPITAL LOCATION APPLICABLE
- 11 ICD TEXT APPLICABLE
- 12 PROVIDER NARRATIVE APPLICABLE

> *Health Summary PARAMETERS File (#142.99)*

- .05 INCLUDE BAR CODES ON ACT PROF

#### Fields deleted

> *from the Health Summary Type file (#142).*

2.  ICD TEXT DISPLAYED
3.  PROVIDER NARRATIVE
4.  MEASUREMENT PANEL
5.  LAB TEST PANEL
6.  SURVEILLANCE PANEL

#### Fields Modified

> *Health Summary PARAMETERS File (#142.99)*

- .02 PROMPT FOR ACTION PROFILE
- .03 INCLUDE COMMENTS FOR LABS
- .04 SPOOL DEVICE
- .05 INCLUDE BAR CODES ON ACT PROF

> <u>Appendices</u>

## Appendix A  Component Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Indicate in the left column the version number of the package you have on your system. Check the components you will use in the right column.

> *<u>Package Data Comes From</u>* Version *<u>Component in Health Summary </u>*

> Allergy Tracking System Adverse Reactions/Allergies

> Adverse Reactions/Allergies Brief

> Automated Medical Information

> Exchange (AMIE) Compensation and Pension Exams

> Dietetics Dietetics

> Discharge Summary

> Discharge Summary

> Discharge Summary Brief

> LAB

> Lab Blood Availability

> Lab Blood Transfusions

> Lab Chemistry & Hematology

> Lab Cumulative Selected

> Lab Cumulative Selected 1

> Lab Cumulative Selected 2

> Lab Cumulative Selected 3

> Lab Cumulative Selected 4

> Lab Cytopathology

> Lab Electron Microscopy

> Lab Microbiology

> Lab Microbiology Brief

> Lab Orders

> Lab Orders Brief

> Lab Surgical Pathology

> Lab Tests Selected

> Medicine

> Medicine Summary

> Medicine Abnormal Brief

> Medicine Brief Report

> Medicine Full Captioned

> Medicine Full Report

> Mental Health

> Mental Health Physical Exam

> Progress Notes *(also checks Generic Progress Notes)*

> Progress Notes Brief *(also*

> *checks Generic Progress Notes)*

> Nursing Vital Signs

> Vital Signs Selected

> *<u>Package Data Comes From</u>* Version *<u>Component in Health Summary </u>*

> OE/RR Version Orders Current

> Patient Care Encounter (PCE)

> PCE Clinical Maintenance

> PCE Clinical Reminders

> PCE Education

> PCE Education Latest

> PCE Exams Latest

> PCE Health Factors All

> PCE Health Factors Selected

> PCE Immunizations

> PCE Location of Home

> PCE Measurements Non-Tabular

> PCE Measurements Selected

> PCE Outpatient Diagnosis

> PCE Outpatient Encounters

> PCE Skin Tests

> PCE Treatments Provided

> PIMS

> MAS Admissions/Discharges

> MAS ADT History

> MAS ADT History Expanded

> MAS Clinic Visits Future

> \_\_\_\_\_\_MAS Clinic Visits Past

> MAS Demographics

> MAS Demographics Brief

> MAS Disabilities

> MAS Discharge Diagnosis

> MAS Discharges

> MAS Procedures ICD Codes

> MAS Surgeries ICD Codes

> MAS Transfers

> MAS Treating Specialty

> Pharmacy Pharmacy Intravenous

> Pharmacy Outpatient

> Pharmacy Unit Dose

> Problem List

> Problem List Active

> Problem List All

> Problem List Inactive

> *<u>Package Data Comes From</u>* Version *<u>Component in Health Summary </u>*

> Progress Notes

> Advance Directive

> Clinical Warnings

> Crisis Notes

> Progress Notes *(also checks Mental Health)*

> Progress Notes Brief *(also checks Mental Health)*

> Radiology Radiology Impression

> Radiology Impression Selected

> Radiology Profile

> Radiology Status

> Surgery Surgery Reports

> Surgery Reports Brief

## Appendix B  Post-init Matrix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table describes what the post-init (GMTSPOST) does for each package depending on the status of the package.

> If a DHCP package is installed after Health Summary V. 2.7 is installed, see the instructions following the table.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 22%" />
<col style="width: 19%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>GMTSPOST (Post</strong></p>
<p><strong>init)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Update Condition</strong></p>
</blockquote></th>
<th><strong>Automatic Disable Condition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>AMIE</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td><p>If $$VERSION^XPDUTL(“DVBA”)&lt;2.7</p>
<p>Disable: Compensation and Pension Exams</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Dietetics</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td>If routine FHWHEA doesn’t exist Disable: Dietetics</td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Discharge Summary</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td><p>If $D(^GMR(128))&lt;10</p>
<p>Disable: Discharge Summary Discharge Summary Brief</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Health Summary</strong></p>
</blockquote></td>
<td><blockquote>
<p>Converts Spool Device Name Text to pointer in File 3.5.</p>
<p>Converts Y/N fields in File 142.99.</p>
<p>Delete ‘C’ Cross- reference on the GMTS AD HOC</p>
<p>OPTION type in File 142.</p>
<p>Update AD HOC SUMMARY Type.</p>
<p>Install Health Summary protocols.</p>
</blockquote></td>
<td><blockquote>
<p>If the field = 1 it is converted to a “Y” If the field = 0 it is converted to a NULL</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Inpatient Medications</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td>If routine PSJEEU0 doesn’t exist Disable: Pharmacy Intravenous Pharmacy Unit Dose</td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Lab</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td><p>If $$VERSION^XPDUTL(“LR”)&lt;5.1</p>
<p>Disable: Lab Blood Availability Lab Blood Transfusions</p>
<p>Lab Chemistry &amp; Hematology Lab Cumulative Selected Lab Cumulative Selected 1 Lab Cumulative Selected 2 Lab Cumulative Selected 3 Lab Cumulative Selected 4 Lab Cytopathology</p>
<p>Lab Electron Microscopy Lab Microbiology</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 22%" />
<col style="width: 19%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>GMTSPOST (Post</strong></p>
<p><strong>init)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Update Condition</strong></p>
</blockquote></th>
<th><strong>Automatic Disable Condition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Lab (cont'd)</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td><p>Lab Microbiology Brief Lab Orders</p>
<p>Lab Orders Brief</p>
<p>Lab Surgical Pathology Lab Tests Selected</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Medicine</strong></p>
</blockquote></td>
<td><blockquote>
<p>Copy GMTSMCZZ to GMTSMCPS</p>
<p>Copy GMTSMCPZ to GMTSMCPS</p>
</blockquote></td>
<td><blockquote>
<p>If Version &gt;2.19</p>
<p>If Version &lt;2.2</p>
</blockquote></td>
<td><p>If $$VERSION^XPDUTL(“MC”)&lt;2.2</p>
<p>Disable: Medicine Abnormal Brief Medicine Brief Report</p>
<p>Medicine Full Captioned Medicine Full Report</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Mental Health</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td><p>If $$VERSION^XPDUTL(“YS”)&lt;5 D</p>
<p>Disable: Mental Health Physical Exam</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Nursing (Vital Measurements)</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td><p>If routine GMRVUT0 doesn’t exist Disable: Vital Signs</p>
<p>Vital Signs Selected</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>OE/RR</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td>If routine ORF4 doesn’t exist Disable: Orders Current</td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Outpatient Pharmacy</strong></p>
</blockquote></td>
<td><blockquote>
<p>Copy GMTSPSZO to GMTSPSO</p>
</blockquote></td>
<td><blockquote>
<p>If Version &lt; 6.0</p>
</blockquote></td>
<td>If routine PSOHCSUM doesn’t exist Disable: Pharmacy Outpatient</td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Patient Care Encounter (PCE)</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td><p>If $$VERSION^XPDUTL(“PX”)’&gt;0,</p>
<p>Disable: PCE Location of Home PCE Clinical Reminders</p>
<p>PCE Health Factors All</p>
<p>PCE Health Factors Selected PCE Outpatient Encounters PCE Measurement Non-tabular PCE Immunizations</p>
<p>PCE Skin Tests</p>
<p>PCE Measurement Selected PCE Education</p>
<p>PCE Education Latest PCE Outpatient Diagnosis PCE Exams Latest</p>
<p>PCE Treatments Provided PCE Clinical Maintenance</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 22%" />
<col style="width: 19%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>GMTSPOST (Post</strong></p>
<p><strong>init)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Update Condition</strong></p>
</blockquote></th>
<th><strong>Automatic Disable Condition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Patient Data Exchange</strong></p>
</blockquote></td>
<td><blockquote>
<p>Install all new components (minus selected item components) into the VAQ-Data Segment File (#394.71)</p>
<p>so sites can make PDX requests for these new components</p>
</blockquote></td>
<td><blockquote>
<p>If $$Version</p>
<p>^XPDUTL(“VAQ”)</p>
<p>&gt;1.49</p>
<p>If routine VAQUTL40</p>
<p>doesn’t exist</p>
<p>Copy GMTSPDXZ to VAQUTL50</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Problem List</strong></p>
</blockquote></td>
<td><blockquote>
<p>Copy GMTSPLSZ to GMPLHS</p>
</blockquote></td>
<td><blockquote>
<p>If Version &gt; 1.99</p>
</blockquote></td>
<td><p>If $$VERSION^XPDUTL(“GMPL”)&lt;2</p>
<p>Disable: Problem List Active Problem List Inactive Problem List All</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Progress Notes</strong> (<strong>Mental Health &amp; Generic)</strong></p>
<p><strong>Crisis Notes Clinical Warnings Advance Directives</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td><p>If ($D(^YSP(606))&lt;10),</p>
<p>($D(^GMR(121))&lt;10)</p>
<p>Disable: Progress Notes Progress Notes Brief</p>
<p>If $D(GMR(121))&lt;10</p>
<p>Disable: Advance Directive Clinical Warnings</p>
<p>Crisis Notes</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Radiology</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td><p>If $$VERSION^XPDUTL(“RA”)&lt;3</p>
<p>Disable: Radiology Impression Selected</p>
<p>Radiology Profile Radiology Status</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Surgery</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td><p>If $D(^SRF)&lt;10</p>
<p>Disable: Surgery Reports Surgery Reports Brief</p></td>
</tr>
</tbody>
</table>

> Post-init instructions if a package is installed at a later date

- If Outpatient Pharmacy Version 6.0 is installed over Version 5.6, the GMTSPSO routine must be restored from the distributed VMS file containing Health Summary V. 2.7.
- If Medicine Version 2.2 is installed, execute the MED^GMTSPOS1 entry point to install the GMTSMCPS routine (D MED^GMTSPOS1).
- If Problem List Version 2.0 is installed, execute the PL^GMTSPOS1 entry point to install the GMPLHS routine

> (D PL^GMTSPOS1). The GMTSPLST routine must be restored from the distributed VMS file that contains the routines and inits because the Problem List post-inits install these components.

> Health Summary Version 2.7 updates these components.

- Once you complete the necessary steps above, use the Disable/Enable Health Summary Component option on the Health Summary Maintenance menu to enable the components for the newly installed package