---
title: EN Version 7 Release Notes Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: Release Notes
app_code: EN
app_name: Engineering (AEMS / MERS)
section: FIN
app_status: active
pkg_ns: EN
patch_ver: 7
patch_id: EN*7
group_key: "EN:EN:7"
file_numbers: []
security_keys: []
menu_options: 0
description: - [Release Notes](#release-notes) - [New Functionalities in Engineering Version 7.0](#new-functionalities-in-engineering-version-70) - [Work Orders/MERS (Medical Equipment Reporting System )](#work-ordersmers-medical-equipment-reporting-system) - [Projects](#projects) - [Equipment Management](#equip
audience: 
keywords: 
  - blockquote
  - enini
  - filed
  - class
  - even
  - enlbl
  - table
  - ensp
  - enary
  - contents
page_count: 0
word_count: 9765
section_count: 7
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 1993
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Engineering/engre7_0.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Engineering/engre7_0.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=37"
---

> Department of Veterans Affairs Decentralized Hospital Computer System

> ENGINEERING

RELEASE NOTES AND INSTALLATION GUIDE

> Version 7.0

> August 1993

> Information Systems Center Washington, D.C.

# Release Notes


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Release Notes](#release-notes)
  - [New Functionalities in Engineering Version 7.0](#new-functionalities-in-engineering-version-70)
    - [Work Orders/MERS (Medical Equipment Reporting System )](#work-ordersmers-medical-equipment-reporting-system)
    - [Projects](#projects)
    - [Equipment Management](#equipment-management)
    - [Space/Facility Management](#spacefacility-management)
  - [Resource Requirements](#resource-requirements)
  - [Implementation Issues](#implementation-issues)
  - [Special Menu Options](#special-menu-options)
- [Installation Guide](#installation-guide)
  - [DHCP Engineering Package (AEMS/MERS) Version 7.0](#dhcp-engineering-package-aemsmers-version-70)
  - [Engineering Installation](#engineering-installation)

## New Functionalities in Engineering Version 7.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Work Orders/MERS (Medical Equipment Reporting System )

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Work orders are automatically generated for failed preventive maintenance inspections if the preventive maintenance is recorded via bar code reader or electrical safety analyzer. If being done manually, the user will be prompted for the creation of a regular work order.

> The Incomplete Work Order option now allows counts (by shop) as well as incomplete work orders. The LOCATION field is now a pointer to the Space file rather than free text.

> There is a new set of work actions which includes 31 choices. Before installing Version 7.0, sites must install Patch EN\*6.5\*5. Pointers to the New Work Action file must be established for all existing WORK ACTIONS before Version 7.0 can be installed.

> With Version 7.0, as many as four different work actions may be associated with each work order. Work order numbers can now be printed in bar code on the hard copy of the work order.

### Projects

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Five Year Facility Plans can now be prepared within the Automated Engineering Management System /Medical Equipment Reporting System (AEMS/MERS) and transmitted to the Regions electronically. They may also be printed in hard copy.

> Project applications (Form 1193, and Form 1193a) may be entered into AEMS/MERS and electronically transmitted to the Regional Construction Offices for approval. The information will be carried over into the Construction Project Progress Reporting options.

> Prioritization scores are calculated for proposed projects in the Nonrecurring Maintenance (NRM), Minor Misc., and Minor programs. The prioritization methodology sheets may be printed.

> The Construction Project Progress Report (Form 10-0051) has been redesigned to meet the needs of the regions.

### Equipment Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The LOCATION field is now a pointer to the Space file rather than free text.

> Information can be posted to the Equipment Repair Histories without going through the Work Order module. VA FileMan sort templates may be used for this purpose.

### Space/Facility Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Users may now distinguish between leased buildings and other types of space.

> Provisions have been made for entering data on planned space as well as actual space. Planned buildings may be associated with projects.

## Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Disk space required for data storage will vary greatly from site to site depending upon such variables as level of activity and archiving policies. At an average site, Engineering files would probably consume between 50 and 100 megabytes of disk space.

> This version of the Engineering package frequently invokes VA Kernel Version 6.5 or later and VA FileMan Version 18.0 or later for device selection, task queuing, data entry, and data presentation.

> The Project Application, 5-Yr Plan and Environmental Analysis (Form 1193a) reports require a printer capable of printing 132 columns. A laser printer is highly recommended for this. Bar code printers and bar code readers are required in order to utilize the bar code feature of the Equipment Management module.

## Implementation Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are 19 site parameters in Version 7.0 of the Engineering package. Nine (9) are found in the Eng Init Parameters file (#6910).

> PM HOURLY COST

> DELETE PM WORK ORDERS? TEMPORARY WORK SECTION REGION

> EQUIPMENT CATEGORY ON BAR CODE LABEL? EQUIPMENT LABEL PRINT FIELD

> COMPANION LIST PRINT FIELD

> SPACE FUNCTION ON LOCATION LABEL? MULTI-DIVISION (Y/N)

> Ten (10) site parameters are found in the Eng Software Options file ( \#6910.2).

> AUTO PRINT NEW WORK ORDERS? EQUIPMENT REPLACEMENT TEMPLATE EXPANDED PM WORK ORDERS?

> INVENTORY TEMPLATE

> PM DEVICE TYPE IDENTIFIER PM SORT

> PRINT BAR CODES ON WORK ORDERS? SAFETY PRINTOUT

> SPACE SURVEY PRINTOUT WARRANTY EXPIRATION TEMPLATE

> Detailed descriptions of each of these parameters may be found in the E ngineering 7.0 Technical Manual.

## Special Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are five (5) options that may be useful as Primary Menu options for users who have limited needs for access to the Engineering Package.

> ENPMINSP (Engineering PM Clerk Main Menu) ENCCLERK (Engineering Accounting Clerk Main Menu) ENSEC (Engineering Secretary Main Menu) ENSECFORM (Engineering Foreman Main Menu) ENWCLERK (Engineering Work Control Main Menu)

> Since the DHCP nonexpendable equipment file is contained within the Engineering package, Acquisition and Material Management Service (A&MM) personnel engaged in property management activities will need access to selected menu options within the Engineering namespace. Menu option ENMM MGR, Nonexpendable Equipment Module (A&MM), is intended to meet the needs of these users. Note that not all PPM employees will need to hold all of the sub- options contained in ENMM MGR.

# Installation Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## DHCP Engineering Package (AEMS/MERS) Version 7.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before installing Engineering 7.0, sites must install Patch EN\*6.5\*5 and follow the instructions given for populating the New Work Action file.

> To install Engineering 7.0 you should:

1.  Backup your system (alternatively, you could just make a copy of your ^ENG global).
2.  Disable routine mapping for the EN\* namespace (if appropriate).
3.  Disable journalling of the ^ENG global.
4.  Delete existing EN\* routines (minus any in the ENZ\* namespace).
5.  Load Engineering 7.0.
6.  DO ^ENINIT (please refer to the sample installation).

> No one should attempt to use the Engineering package while the installation is in progress. It is not necessary to restrict access to other packages while Engineering 7.0 is being installed.

> There is a pre-initialization routine (ENNEWPKG) that checks to see that all WORK ACTIONS have pointers to the New Work Action file.

> The initialization routine (ENNEWPK2) deletes some data entry screens and data definitions in preparation for installation of Engineering 7.0.

> There is a post-initialization routine (ENPOST) that changes the root of the Work Order file from

> ^ENG("WO", to ^ENG(6920,. It also converts LOCATION fields in the Work Order file and the Equipment file into pointers and updates selected fields in the Construction Project file.

> Installation times will depend heavily on the size of the Work Order file. VAX sites can expect the installation to take about one hour plus an additional hour for each 15,000 entries in the Work Order file.

> Installation of Engineering 7.0 will require about 15 megabytes of disk space at sites that are not presently running the Engineering package. Upgrading from Engineering 6.5 to Engineering 7.0 will require about one megabyte of disk space.

## Engineering Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> SAMPLE INSTALLATION

> DHCP Engineering Package (AEMS/MERS) Version 7.0

- \>D ^%RDEL

•

- MSM - Routine Delete Utility

•

- Routine selector: EN\*

•

- 225 routines selected.

•

- Routine selector: -ENZ\*

•

- 54 routines de-selected.

•

- Routine selector:

•

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><blockquote>
<p>Delete Selected Routines? &lt;N&gt;</p>
</blockquote></li>
</ul></th>
<th><blockquote>
<p><strong>Y</strong></p>
</blockquote></th>
<th colspan="4" rowspan="3"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>•</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><ul>
<li><blockquote>
<p>Deleting ...</p>
</blockquote></li>
</ul></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><blockquote>
<p>EN ENAR ENAR1</p>
</blockquote></li>
</ul></td>
<td><blockquote>
<p>ENAR2</p>
</blockquote></td>
<td><blockquote>
<p>ENARG</p>
</blockquote></td>
<td><blockquote>
<p>ENARG1</p>
</blockquote></td>
<td><blockquote>
<p>ENARG2</p>
</blockquote></td>
<td><blockquote>
<p>ENARG21</p>
</blockquote></td>
</tr>
<tr class="even">
<td><ul>
<li><blockquote>
<p>ENARG22 ENARGO ENARGR</p>
</blockquote></li>
</ul></td>
<td><blockquote>
<p>ENARL</p>
</blockquote></td>
<td><blockquote>
<p>ENARY101</p>
</blockquote></td>
<td><blockquote>
<p>ENARY102</p>
</blockquote></td>
<td><blockquote>
<p>ENARY11</p>
</blockquote></td>
<td><blockquote>
<p>ENARY12</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><ul>
<li><blockquote>
<p>ENARY13 ENARY14 ENARY201</p>
</blockquote></li>
</ul></td>
<td><blockquote>
<p>ENARY202</p>
</blockquote></td>
<td><blockquote>
<p>ENARY203</p>
</blockquote></td>
<td><blockquote>
<p>ENARY21</p>
</blockquote></td>
<td><blockquote>
<p>ENARY22</p>
</blockquote></td>
<td><blockquote>
<p>ENARY23</p>
</blockquote></td>
</tr>
<tr class="even">
<td><ul>
<li><blockquote>
<p>ENARY24 ENBCPM ENBCPM1</p>
</blockquote></li>
</ul></td>
<td><blockquote>
<p>ENBCPM2</p>
</blockquote></td>
<td><blockquote>
<p>ENBCPM3</p>
</blockquote></td>
<td><blockquote>
<p>ENBCPM4</p>
</blockquote></td>
<td><blockquote>
<p>ENBCPM5</p>
</blockquote></td>
<td><blockquote>
<p>ENBCPM6</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><ul>
<li><blockquote>
<p>ENCTBAR ENCTFLD ENCTLAB</p>
</blockquote></li>
</ul></td>
<td><blockquote>
<p>ENCTMAN</p>
</blockquote></td>
<td><blockquote>
<p>ENCTMES1</p>
</blockquote></td>
<td><blockquote>
<p>ENCTMES2</p>
</blockquote></td>
<td><blockquote>
<p>ENCTPRG</p>
</blockquote></td>
<td><blockquote>
<p>ENCTQUES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><ul>
<li><blockquote>
<p>ENCTRCH ENCTREAD ENCTRED</p>
</blockquote></li>
</ul></td>
<td><blockquote>
<p>ENCTTI</p>
</blockquote></td>
<td><blockquote>
<p>ENCTUTL</p>
</blockquote></td>
<td><blockquote>
<p>ENEQ</p>
</blockquote></td>
<td><blockquote>
<p>ENEQ1</p>
</blockquote></td>
<td><blockquote>
<p>ENEQ2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><ul>
<li><blockquote>
<p>ENEQCMR ENEQHS ENEQNX</p>
</blockquote></li>
</ul></td>
<td><blockquote>
<p>ENEQNX1</p>
</blockquote></td>
<td><blockquote>
<p>ENEQNX2</p>
</blockquote></td>
<td><blockquote>
<p>ENEQNX3</p>
</blockquote></td>
<td><blockquote>
<p>ENEQNX4</p>
</blockquote></td>
<td><blockquote>
<p>ENEQNX5</p>
</blockquote></td>
</tr>
<tr class="even">
<td><ul>
<li><blockquote>
<p>ENEQPMP ENEQPMP1 ENEQPMP2</p>
</blockquote></li>
</ul></td>
<td><blockquote>
<p>ENEQPMP3</p>
</blockquote></td>
<td><blockquote>
<p>ENEQPMR</p>
</blockquote></td>
<td><blockquote>
<p>ENEQPMR1</p>
</blockquote></td>
<td><blockquote>
<p>ENEQPMR2</p>
</blockquote></td>
<td><blockquote>
<p>ENEQPMR3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><ul>
<li><blockquote>
<p>ENEQPMR4 ENEQPMR5 ENEQPMR6</p>
</blockquote></li>
</ul></td>
<td><blockquote>
<p>ENEQPMS</p>
</blockquote></td>
<td><blockquote>
<p>ENEQPMS1</p>
</blockquote></td>
<td><blockquote>
<p>ENEQPMS2</p>
</blockquote></td>
<td><blockquote>
<p>ENEQPMS3</p>
</blockquote></td>
<td><blockquote>
<p>ENEQPMS4</p>
</blockquote></td>
</tr>
<tr class="even">
<td><ul>
<li><blockquote>
<p>ENEQPMS5 ENEQPMS6 ENEQPMS7</p>
</blockquote></li>
</ul></td>
<td><blockquote>
<p>ENEQPMS8</p>
</blockquote></td>
<td><blockquote>
<p>ENEQRP</p>
</blockquote></td>
<td><blockquote>
<p>ENEQRP1</p>
</blockquote></td>
<td><blockquote>
<p>ENEQRP2</p>
</blockquote></td>
<td><blockquote>
<p>ENEQRP3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><ul>
<li><blockquote>
<p>ENEQRP4 ENEQRP5 ENEQRPI</p>
</blockquote></li>
</ul></td>
<td><blockquote>
<p>ENETRAN</p>
</blockquote></td>
<td><blockquote>
<p>ENETRAN1</p>
</blockquote></td>
<td><blockquote>
<p>ENETRAN2</p>
</blockquote></td>
<td><blockquote>
<p>ENEWOD</p>
</blockquote></td>
<td><blockquote>
<p>ENEWOD1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><ul>
<li><blockquote>
<p>ENFSA ENFSA1 ENFSA2</p>
</blockquote></li>
</ul></td>
<td><blockquote>
<p>ENJ</p>
</blockquote></td>
<td><blockquote>
<p>ENJC2</p>
</blockquote></td>
<td><blockquote>
<p>ENJDPL</p>
</blockquote></td>
<td><blockquote>
<p>ENJINJ</p>
</blockquote></td>
<td><blockquote>
<p>ENJINJ1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><ul>
<li><blockquote>
<p>ENJINJ2 ENJINJ3 ENJINK</p>
</blockquote></li>
</ul></td>
<td><blockquote>
<p>ENJINQ</p>
</blockquote></td>
<td><blockquote>
<p>ENJMUL</p>
</blockquote></td>
<td><blockquote>
<p>ENJPARAM</p>
</blockquote></td>
<td><blockquote>
<p>ENLBL</p>
</blockquote></td>
<td><blockquote>
<p>ENLBL1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><ul>
<li><blockquote>
<p>ENLBL10 ENLBL11 ENLBL12</p>
</blockquote></li>
</ul></td>
<td><blockquote>
<p>ENLBL13</p>
</blockquote></td>
<td><blockquote>
<p>ENLBL14</p>
</blockquote></td>
<td><blockquote>
<p>ENLBL15</p>
</blockquote></td>
<td><blockquote>
<p>ENLBL16</p>
</blockquote></td>
<td><blockquote>
<p>ENLBL2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><ul>
<li><blockquote>
<p>ENLBL3 ENLBL4 ENLBL5</p>
</blockquote></li>
</ul></td>
<td><blockquote>
<p>ENLBL6</p>
</blockquote></td>
<td><blockquote>
<p>ENLBL7</p>
</blockquote></td>
<td><blockquote>
<p>ENLBL8</p>
</blockquote></td>
<td><blockquote>
<p>ENLBL9</p>
</blockquote></td>
<td><blockquote>
<p>ENLIB</p>
</blockquote></td>
</tr>
<tr class="even">
<td><ul>
<li><blockquote>
<p>ENLIB1 ENLIB2 ENMAN</p>
</blockquote></li>
</ul></td>
<td><blockquote>
<p>ENNEWPKG</p>
</blockquote></td>
<td><blockquote>
<p>ENNTEG</p>
</blockquote></td>
<td><blockquote>
<p>ENNTEG0</p>
</blockquote></td>
<td><blockquote>
<p>ENPOST</p>
</blockquote></td>
<td><blockquote>
<p>ENPOST1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><ul>
<li><blockquote>
<p>ENPROJ ENPROJ1 ENPROJ2</p>
</blockquote></li>
</ul></td>
<td><blockquote>
<p>ENPROJ3</p>
</blockquote></td>
<td><blockquote>
<p>ENPROJ4</p>
</blockquote></td>
<td><blockquote>
<p>ENPROJ5</p>
</blockquote></td>
<td><blockquote>
<p>ENPROJ6</p>
</blockquote></td>
<td><blockquote>
<p>ENSA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><ul>
<li><blockquote>
<p>ENSA1 ENSA2 ENSA3</p>
</blockquote></li>
</ul></td>
<td><blockquote>
<p>ENSA4</p>
</blockquote></td>
<td><blockquote>
<p>ENSA5</p>
</blockquote></td>
<td><blockquote>
<p>ENSA6</p>
</blockquote></td>
<td><blockquote>
<p>ENSA7</p>
</blockquote></td>
<td><blockquote>
<p>ENSED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><ul>
<li><blockquote>
<p>ENSED0 ENSED1 ENSED2</p>
</blockquote></li>
</ul></td>
<td><blockquote>
<p>ENSP</p>
</blockquote></td>
<td><blockquote>
<p>ENSP1</p>
</blockquote></td>
<td><blockquote>
<p>ENSP2</p>
</blockquote></td>
<td><blockquote>
<p>ENSP3</p>
</blockquote></td>
<td><blockquote>
<p>ENSP4</p>
</blockquote></td>
</tr>
<tr class="even">
<td><ul>
<li><blockquote>
<p>ENSP5 ENTEXT ENWARD</p>
</blockquote></li>
</ul></td>
<td><blockquote>
<p>ENWARD1</p>
</blockquote></td>
<td><blockquote>
<p>ENWARD2</p>
</blockquote></td>
<td><blockquote>
<p>ENWO</p>
</blockquote></td>
<td><blockquote>
<p>ENWO1</p>
</blockquote></td>
<td><blockquote>
<p>ENWO2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><ul>
<li><blockquote>
<p>ENWOCOMP ENWOD ENWOD1</p>
</blockquote></li>
</ul></td>
<td><blockquote>
<p>ENWOD2</p>
</blockquote></td>
<td><blockquote>
<p>ENWOINV</p>
</blockquote></td>
<td><blockquote>
<p>ENWONEW</p>
</blockquote></td>
<td><blockquote>
<p>ENWONEW1</p>
</blockquote></td>
<td><blockquote>
<p>ENWOP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><ul>
<li><blockquote>
<p>ENWOP1 ENWOREP ENWOST</p>
</blockquote></li>
</ul></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

D ^%ZTMOVE

Task Number: 1444

Delete Task After Loading? Y

1336 routines transfered from READY TO BE LOADED INTO 'VAH,PSC' ...OK? YES//

EN ENAR ENAR1 ENAR2 ENARG ENARG1 ENARG2 ENARG21 ENARG22 ENARGO ENARGR ENARL ENARY101 ENARY102 ENARY11 ENARY12 ENARY13 ENARY14 ENARY201 ENARY202 ENARY203 ENARY21 ENARY22 ENARY23 ENARY24 ENBCPM ENBCPM1 ENBCPM2 ENBCPM3 ENBCPM4 ENBCPM5 ENBCPM6 ENBCPM7 ENBCPM8 ENBCPM9 ENCTBAR ENCTFLD ENCTLAB ENCTMAN ENCTMES1 ENCTMES2 ENCTPRG ENCTQUES ENCTRCH ENCTREAD ENCTRED ENCTTI ENCTUTL ENEQ ENEQ1 ENEQ2 ENEQCMR ENEQHS ENEQNX ENEQNX1 ENEQNX2 ENEQNX3 ENEQNX4 ENEQNX5 ENEQP ENEQP1 ENEQPMP ENEQPMP1

ENEQPMP2 ENEQPMP3 ENEQPMR ENEQPMR1 ENEQPMR2 ENEQPMR3 ENEQPMR4 ENEQPMR5 ENEQPMR6 ENEQPMS ENEQPMS1 ENEQPMS2 ENEQPMS3 ENEQPMS4 ENEQPMS5 ENEQPMS6 ENEQPMS7 ENEQPMS8 ENEQRP ENEQRP1 ENEQRP2 ENEQRP3 ENEQRP4 ENEQRP5 ENEQRPI ENETRAN ENETRAN1 ENETRAN2 ENEWOD ENEWOD1 ENFSA ENFSA1 ENFSA2 ENINI001

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>ENINI002</p>
</blockquote></th>
<th>ENINI003</th>
<th>ENINI004</th>
<th><blockquote>
<p>ENINI005</p>
</blockquote></th>
<th><blockquote>
<p>ENINI006</p>
</blockquote></th>
<th><blockquote>
<p>ENINI007</p>
</blockquote></th>
<th>ENINI008</th>
<th>ENINI009</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ENINI010</p>
</blockquote></td>
<td>ENINI011</td>
<td>ENINI012</td>
<td><blockquote>
<p>ENINI013</p>
</blockquote></td>
<td><blockquote>
<p>ENINI014</p>
</blockquote></td>
<td><blockquote>
<p>ENINI015</p>
</blockquote></td>
<td>ENINI016</td>
<td>ENINI017</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI018</p>
</blockquote></td>
<td>ENINI019</td>
<td>ENINI020</td>
<td><blockquote>
<p>ENINI021</p>
</blockquote></td>
<td><blockquote>
<p>ENINI022</p>
</blockquote></td>
<td><blockquote>
<p>ENINI023</p>
</blockquote></td>
<td>ENINI024</td>
<td>ENINI025</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI026</p>
</blockquote></td>
<td>ENINI027</td>
<td>ENINI028</td>
<td><blockquote>
<p>ENINI029</p>
</blockquote></td>
<td><blockquote>
<p>ENINI030</p>
</blockquote></td>
<td><blockquote>
<p>ENINI031</p>
</blockquote></td>
<td>ENINI032</td>
<td>ENINI033</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI034</p>
</blockquote></td>
<td>ENINI035</td>
<td>ENINI036</td>
<td><blockquote>
<p>ENINI037</p>
</blockquote></td>
<td><blockquote>
<p>ENINI038</p>
</blockquote></td>
<td><blockquote>
<p>ENINI039</p>
</blockquote></td>
<td>ENINI040</td>
<td>ENINI041</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI042</p>
</blockquote></td>
<td>ENINI043</td>
<td>ENINI044</td>
<td><blockquote>
<p>ENINI045</p>
</blockquote></td>
<td><blockquote>
<p>ENINI046</p>
</blockquote></td>
<td><blockquote>
<p>ENINI047</p>
</blockquote></td>
<td>ENINI048</td>
<td>ENINI049</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI050</p>
</blockquote></td>
<td>ENINI051</td>
<td>ENINI052</td>
<td><blockquote>
<p>ENINI053</p>
</blockquote></td>
<td><blockquote>
<p>ENINI054</p>
</blockquote></td>
<td><blockquote>
<p>ENINI055</p>
</blockquote></td>
<td>ENINI056</td>
<td>ENINI057</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI058</p>
</blockquote></td>
<td>ENINI059</td>
<td>ENINI060</td>
<td><blockquote>
<p>ENINI061</p>
</blockquote></td>
<td><blockquote>
<p>ENINI062</p>
</blockquote></td>
<td><blockquote>
<p>ENINI063</p>
</blockquote></td>
<td>ENINI064</td>
<td>ENINI065</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI066</p>
</blockquote></td>
<td>ENINI067</td>
<td>ENINI068</td>
<td><blockquote>
<p>ENINI069</p>
</blockquote></td>
<td><blockquote>
<p>ENINI070</p>
</blockquote></td>
<td><blockquote>
<p>ENINI071</p>
</blockquote></td>
<td>ENINI072</td>
<td>ENINI073</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI074</p>
</blockquote></td>
<td>ENINI075</td>
<td>ENINI076</td>
<td><blockquote>
<p>ENINI077</p>
</blockquote></td>
<td><blockquote>
<p>ENINI078</p>
</blockquote></td>
<td><blockquote>
<p>ENINI079</p>
</blockquote></td>
<td>ENINI080</td>
<td>ENINI081</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI082</p>
</blockquote></td>
<td>ENINI083</td>
<td>ENINI084</td>
<td><blockquote>
<p>ENINI085</p>
</blockquote></td>
<td><blockquote>
<p>ENINI086</p>
</blockquote></td>
<td><blockquote>
<p>ENINI087</p>
</blockquote></td>
<td>ENINI088</td>
<td>ENINI089</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI090</p>
</blockquote></td>
<td>ENINI091</td>
<td>ENINI092</td>
<td><blockquote>
<p>ENINI093</p>
</blockquote></td>
<td><blockquote>
<p>ENINI094</p>
</blockquote></td>
<td><blockquote>
<p>ENINI095</p>
</blockquote></td>
<td>ENINI096</td>
<td>ENINI097</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI098</p>
</blockquote></td>
<td>ENINI099</td>
<td>ENINI0AA</td>
<td><blockquote>
<p>ENINI0AB</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0AC</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0AD</p>
</blockquote></td>
<td>ENINI0AE</td>
<td>ENINI0AF</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI0AG</p>
</blockquote></td>
<td>ENINI0AH</td>
<td>ENINI0AI</td>
<td><blockquote>
<p>ENINI0AJ</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0AK</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0AL</p>
</blockquote></td>
<td>ENINI0AM</td>
<td>ENINI0AN</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI0AO</p>
</blockquote></td>
<td>ENINI0AP</td>
<td>ENINI0AQ</td>
<td><blockquote>
<p>ENINI0AR</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0AS</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0AT</p>
</blockquote></td>
<td>ENINI0AU</td>
<td>ENINI0AV</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI0AW</p>
</blockquote></td>
<td>ENINI0AX</td>
<td>ENINI0AY</td>
<td><blockquote>
<p>ENINI0AZ</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0Aa</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0Ab</p>
</blockquote></td>
<td>ENINI0Ac</td>
<td>ENINI0Ad</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI0Ae</p>
</blockquote></td>
<td>ENINI0Af</td>
<td>ENINI0Ag</td>
<td><blockquote>
<p>ENINI0Ah</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0Ai</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0Aj</p>
</blockquote></td>
<td>ENINI0Ak</td>
<td>ENINI0Al</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI0Am</p>
</blockquote></td>
<td>ENINI0An</td>
<td>ENINI0Ao</td>
<td><blockquote>
<p>ENINI0Ap</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0Aq</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0Ar</p>
</blockquote></td>
<td>ENINI0As</td>
<td>ENINI0At</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI0Au</p>
</blockquote></td>
<td>ENINI0Av</td>
<td>ENINI0Aw</td>
<td><blockquote>
<p>ENINI0Ax</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0Ay</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0Az</p>
</blockquote></td>
<td>ENINI0BA</td>
<td>ENINI0BB</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI0BC</p>
</blockquote></td>
<td>ENINI0BD</td>
<td>ENINI0BE</td>
<td><blockquote>
<p>ENINI0BF</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0BG</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0BH</p>
</blockquote></td>
<td>ENINI0BI</td>
<td>ENINI0BJ</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI0BK</p>
</blockquote></td>
<td>ENINI0BL</td>
<td>ENINI0BM</td>
<td><blockquote>
<p>ENINI0BN</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0BO</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0BP</p>
</blockquote></td>
<td>ENINI0BQ</td>
<td>ENINI0BR</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI0BS</p>
</blockquote></td>
<td>ENINI0BT</td>
<td>ENINI0BU</td>
<td><blockquote>
<p>ENINI0BV</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0BW</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0BX</p>
</blockquote></td>
<td>ENINI0BY</td>
<td>ENINI0BZ</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI0Ba</p>
</blockquote></td>
<td>ENINI0Bb</td>
<td>ENINI0Bc</td>
<td><blockquote>
<p>ENINI0Bd</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0Be</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0Bf</p>
</blockquote></td>
<td>ENINI0Bg</td>
<td>ENINI0Bh</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI0Bi</p>
</blockquote></td>
<td>ENINI0Bj</td>
<td>ENINI0Bk</td>
<td><blockquote>
<p>ENINI0Bl</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0Bm</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0Bn</p>
</blockquote></td>
<td>ENINI0Bo</td>
<td>ENINI0Bp</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI0Bq</p>
</blockquote></td>
<td>ENINI0Br</td>
<td>ENINI0Bs</td>
<td><blockquote>
<p>ENINI0Bt</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0Bu</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0Bv</p>
</blockquote></td>
<td>ENINI0Bw</td>
<td>ENINI0Bx</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI0By</p>
</blockquote></td>
<td>ENINI0Bz</td>
<td>ENINI0CA</td>
<td><blockquote>
<p>ENINI0CB</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0CC</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0CD</p>
</blockquote></td>
<td>ENINI0CE</td>
<td>ENINI0CF</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI0CG</p>
</blockquote></td>
<td>ENINI0CH</td>
<td>ENINI0CI</td>
<td><blockquote>
<p>ENINI0CJ</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0CK</p>
</blockquote></td>
<td><blockquote>
<p>ENINI0CL</p>
</blockquote></td>
<td>ENINI0CM</td>
<td>ENINI0CN</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI0CO</p>
</blockquote></td>
<td>ENINI0CP</td>
<td>ENINI0CQ</td>
<td><blockquote>
<p>ENINI100</p>
</blockquote></td>
<td><blockquote>
<p>ENINI101</p>
</blockquote></td>
<td><blockquote>
<p>ENINI102</p>
</blockquote></td>
<td>ENINI103</td>
<td>ENINI104</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI105</p>
</blockquote></td>
<td>ENINI106</td>
<td>ENINI107</td>
<td><blockquote>
<p>ENINI108</p>
</blockquote></td>
<td><blockquote>
<p>ENINI109</p>
</blockquote></td>
<td><blockquote>
<p>ENINI110</p>
</blockquote></td>
<td>ENINI111</td>
<td>ENINI112</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI113</p>
</blockquote></td>
<td>ENINI114</td>
<td>ENINI115</td>
<td><blockquote>
<p>ENINI116</p>
</blockquote></td>
<td><blockquote>
<p>ENINI117</p>
</blockquote></td>
<td><blockquote>
<p>ENINI118</p>
</blockquote></td>
<td>ENINI119</td>
<td>ENINI120</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI121</p>
</blockquote></td>
<td>ENINI122</td>
<td>ENINI123</td>
<td><blockquote>
<p>ENINI124</p>
</blockquote></td>
<td><blockquote>
<p>ENINI125</p>
</blockquote></td>
<td><blockquote>
<p>ENINI126</p>
</blockquote></td>
<td>ENINI127</td>
<td>ENINI128</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI129</p>
</blockquote></td>
<td>ENINI130</td>
<td>ENINI131</td>
<td><blockquote>
<p>ENINI132</p>
</blockquote></td>
<td><blockquote>
<p>ENINI133</p>
</blockquote></td>
<td><blockquote>
<p>ENINI134</p>
</blockquote></td>
<td>ENINI135</td>
<td>ENINI136</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI137</p>
</blockquote></td>
<td>ENINI138</td>
<td>ENINI139</td>
<td><blockquote>
<p>ENINI140</p>
</blockquote></td>
<td><blockquote>
<p>ENINI141</p>
</blockquote></td>
<td><blockquote>
<p>ENINI142</p>
</blockquote></td>
<td>ENINI143</td>
<td>ENINI144</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI145</p>
</blockquote></td>
<td>ENINI146</td>
<td>ENINI147</td>
<td><blockquote>
<p>ENINI148</p>
</blockquote></td>
<td><blockquote>
<p>ENINI149</p>
</blockquote></td>
<td><blockquote>
<p>ENINI150</p>
</blockquote></td>
<td>ENINI151</td>
<td>ENINI152</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI153</p>
</blockquote></td>
<td>ENINI154</td>
<td>ENINI155</td>
<td><blockquote>
<p>ENINI156</p>
</blockquote></td>
<td><blockquote>
<p>ENINI157</p>
</blockquote></td>
<td><blockquote>
<p>ENINI158</p>
</blockquote></td>
<td>ENINI159</td>
<td>ENINI160</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI161</p>
</blockquote></td>
<td>ENINI162</td>
<td>ENINI163</td>
<td><blockquote>
<p>ENINI164</p>
</blockquote></td>
<td><blockquote>
<p>ENINI165</p>
</blockquote></td>
<td><blockquote>
<p>ENINI166</p>
</blockquote></td>
<td>ENINI167</td>
<td>ENINI168</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI169</p>
</blockquote></td>
<td>ENINI170</td>
<td>ENINI171</td>
<td><blockquote>
<p>ENINI172</p>
</blockquote></td>
<td><blockquote>
<p>ENINI173</p>
</blockquote></td>
<td><blockquote>
<p>ENINI174</p>
</blockquote></td>
<td>ENINI175</td>
<td>ENINI176</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI177</p>
</blockquote></td>
<td>ENINI178</td>
<td>ENINI179</td>
<td><blockquote>
<p>ENINI180</p>
</blockquote></td>
<td><blockquote>
<p>ENINI181</p>
</blockquote></td>
<td><blockquote>
<p>ENINI182</p>
</blockquote></td>
<td>ENINI183</td>
<td>ENINI184</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI185</p>
</blockquote></td>
<td>ENINI186</td>
<td>ENINI187</td>
<td><blockquote>
<p>ENINI188</p>
</blockquote></td>
<td><blockquote>
<p>ENINI189</p>
</blockquote></td>
<td><blockquote>
<p>ENINI190</p>
</blockquote></td>
<td>ENINI191</td>
<td>ENINI192</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI193</p>
</blockquote></td>
<td>ENINI194</td>
<td>ENINI195</td>
<td><blockquote>
<p>ENINI196</p>
</blockquote></td>
<td><blockquote>
<p>ENINI197</p>
</blockquote></td>
<td><blockquote>
<p>ENINI198</p>
</blockquote></td>
<td>ENINI199</td>
<td>ENINI200</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI201</p>
</blockquote></td>
<td>ENINI202</td>
<td>ENINI203</td>
<td><blockquote>
<p>ENINI204</p>
</blockquote></td>
<td><blockquote>
<p>ENINI205</p>
</blockquote></td>
<td><blockquote>
<p>ENINI206</p>
</blockquote></td>
<td>ENINI207</td>
<td>ENINI208</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI209</p>
</blockquote></td>
<td>ENINI210</td>
<td>ENINI211</td>
<td><blockquote>
<p>ENINI212</p>
</blockquote></td>
<td><blockquote>
<p>ENINI213</p>
</blockquote></td>
<td><blockquote>
<p>ENINI214</p>
</blockquote></td>
<td>ENINI215</td>
<td>ENINI216</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI217</p>
</blockquote></td>
<td>ENINI218</td>
<td>ENINI219</td>
<td><blockquote>
<p>ENINI220</p>
</blockquote></td>
<td><blockquote>
<p>ENINI221</p>
</blockquote></td>
<td><blockquote>
<p>ENINI222</p>
</blockquote></td>
<td>ENINI223</td>
<td>ENINI224</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI225</p>
</blockquote></td>
<td>ENINI226</td>
<td>ENINI227</td>
<td><blockquote>
<p>ENINI228</p>
</blockquote></td>
<td><blockquote>
<p>ENINI229</p>
</blockquote></td>
<td><blockquote>
<p>ENINI230</p>
</blockquote></td>
<td>ENINI231</td>
<td>ENINI232</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI233</p>
</blockquote></td>
<td>ENINI234</td>
<td>ENINI235</td>
<td><blockquote>
<p>ENINI236</p>
</blockquote></td>
<td><blockquote>
<p>ENINI237</p>
</blockquote></td>
<td><blockquote>
<p>ENINI238</p>
</blockquote></td>
<td>ENINI239</td>
<td>ENINI240</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI241</p>
</blockquote></td>
<td>ENINI242</td>
<td>ENINI243</td>
<td><blockquote>
<p>ENINI244</p>
</blockquote></td>
<td><blockquote>
<p>ENINI245</p>
</blockquote></td>
<td><blockquote>
<p>ENINI246</p>
</blockquote></td>
<td>ENINI247</td>
<td>ENINI248</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI249</p>
</blockquote></td>
<td>ENINI250</td>
<td>ENINI251</td>
<td><blockquote>
<p>ENINI252</p>
</blockquote></td>
<td><blockquote>
<p>ENINI253</p>
</blockquote></td>
<td><blockquote>
<p>ENINI254</p>
</blockquote></td>
<td>ENINI255</td>
<td>ENINI256</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI257</p>
</blockquote></td>
<td>ENINI258</td>
<td>ENINI259</td>
<td><blockquote>
<p>ENINI260</p>
</blockquote></td>
<td><blockquote>
<p>ENINI261</p>
</blockquote></td>
<td><blockquote>
<p>ENINI262</p>
</blockquote></td>
<td>ENINI263</td>
<td>ENINI264</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI265</p>
</blockquote></td>
<td>ENINI266</td>
<td>ENINI267</td>
<td><blockquote>
<p>ENINI268</p>
</blockquote></td>
<td><blockquote>
<p>ENINI269</p>
</blockquote></td>
<td><blockquote>
<p>ENINI270</p>
</blockquote></td>
<td>ENINI271</td>
<td>ENINI272</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI273</p>
</blockquote></td>
<td>ENINI274</td>
<td>ENINI275</td>
<td><blockquote>
<p>ENINI276</p>
</blockquote></td>
<td><blockquote>
<p>ENINI277</p>
</blockquote></td>
<td><blockquote>
<p>ENINI278</p>
</blockquote></td>
<td>ENINI279</td>
<td>ENINI280</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI281</p>
</blockquote></td>
<td>ENINI282</td>
<td>ENINI283</td>
<td><blockquote>
<p>ENINI284</p>
</blockquote></td>
<td><blockquote>
<p>ENINI285</p>
</blockquote></td>
<td><blockquote>
<p>ENINI286</p>
</blockquote></td>
<td>ENINI287</td>
<td>ENINI288</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI289</p>
</blockquote></td>
<td>ENINI290</td>
<td>ENINI291</td>
<td><blockquote>
<p>ENINI292</p>
</blockquote></td>
<td><blockquote>
<p>ENINI293</p>
</blockquote></td>
<td><blockquote>
<p>ENINI294</p>
</blockquote></td>
<td>ENINI295</td>
<td>ENINI296</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI297</p>
</blockquote></td>
<td>ENINI298</td>
<td>ENINI299</td>
<td><blockquote>
<p>ENINI300</p>
</blockquote></td>
<td><blockquote>
<p>ENINI301</p>
</blockquote></td>
<td><blockquote>
<p>ENINI302</p>
</blockquote></td>
<td>ENINI303</td>
<td>ENINI304</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI305</p>
</blockquote></td>
<td>ENINI306</td>
<td>ENINI307</td>
<td><blockquote>
<p>ENINI308</p>
</blockquote></td>
<td><blockquote>
<p>ENINI309</p>
</blockquote></td>
<td><blockquote>
<p>ENINI310</p>
</blockquote></td>
<td>ENINI311</td>
<td>ENINI312</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI313</p>
</blockquote></td>
<td>ENINI314</td>
<td>ENINI315</td>
<td><blockquote>
<p>ENINI316</p>
</blockquote></td>
<td><blockquote>
<p>ENINI317</p>
</blockquote></td>
<td><blockquote>
<p>ENINI318</p>
</blockquote></td>
<td>ENINI319</td>
<td>ENINI320</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI321</p>
</blockquote></td>
<td>ENINI322</td>
<td>ENINI323</td>
<td><blockquote>
<p>ENINI324</p>
</blockquote></td>
<td><blockquote>
<p>ENINI325</p>
</blockquote></td>
<td><blockquote>
<p>ENINI326</p>
</blockquote></td>
<td>ENINI327</td>
<td>ENINI328</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI329</p>
</blockquote></td>
<td>ENINI330</td>
<td>ENINI331</td>
<td><blockquote>
<p>ENINI332</p>
</blockquote></td>
<td><blockquote>
<p>ENINI333</p>
</blockquote></td>
<td><blockquote>
<p>ENINI334</p>
</blockquote></td>
<td>ENINI335</td>
<td>ENINI336</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI337</p>
</blockquote></td>
<td>ENINI338</td>
<td>ENINI339</td>
<td><blockquote>
<p>ENINI340</p>
</blockquote></td>
<td><blockquote>
<p>ENINI341</p>
</blockquote></td>
<td><blockquote>
<p>ENINI342</p>
</blockquote></td>
<td>ENINI343</td>
<td>ENINI344</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI345</p>
</blockquote></td>
<td>ENINI346</td>
<td>ENINI347</td>
<td><blockquote>
<p>ENINI348</p>
</blockquote></td>
<td><blockquote>
<p>ENINI349</p>
</blockquote></td>
<td><blockquote>
<p>ENINI350</p>
</blockquote></td>
<td>ENINI351</td>
<td>ENINI352</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI353</p>
</blockquote></td>
<td>ENINI354</td>
<td>ENINI355</td>
<td><blockquote>
<p>ENINI356</p>
</blockquote></td>
<td><blockquote>
<p>ENINI357</p>
</blockquote></td>
<td><blockquote>
<p>ENINI358</p>
</blockquote></td>
<td>ENINI359</td>
<td>ENINI360</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI361</p>
</blockquote></td>
<td>ENINI362</td>
<td>ENINI363</td>
<td><blockquote>
<p>ENINI364</p>
</blockquote></td>
<td><blockquote>
<p>ENINI365</p>
</blockquote></td>
<td><blockquote>
<p>ENINI366</p>
</blockquote></td>
<td>ENINI367</td>
<td>ENINI368</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI369</p>
</blockquote></td>
<td>ENINI370</td>
<td>ENINI371</td>
<td><blockquote>
<p>ENINI372</p>
</blockquote></td>
<td><blockquote>
<p>ENINI373</p>
</blockquote></td>
<td><blockquote>
<p>ENINI374</p>
</blockquote></td>
<td>ENINI375</td>
<td>ENINI376</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI377</p>
</blockquote></td>
<td>ENINI378</td>
<td>ENINI379</td>
<td><blockquote>
<p>ENINI380</p>
</blockquote></td>
<td><blockquote>
<p>ENINI381</p>
</blockquote></td>
<td><blockquote>
<p>ENINI382</p>
</blockquote></td>
<td>ENINI383</td>
<td>ENINI384</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI385</p>
</blockquote></td>
<td>ENINI386</td>
<td>ENINI387</td>
<td><blockquote>
<p>ENINI388</p>
</blockquote></td>
<td><blockquote>
<p>ENINI389</p>
</blockquote></td>
<td><blockquote>
<p>ENINI390</p>
</blockquote></td>
<td>ENINI391</td>
<td>ENINI392</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI393</p>
</blockquote></td>
<td>ENINI394</td>
<td>ENINI395</td>
<td><blockquote>
<p>ENINI396</p>
</blockquote></td>
<td><blockquote>
<p>ENINI397</p>
</blockquote></td>
<td><blockquote>
<p>ENINI398</p>
</blockquote></td>
<td>ENINI399</td>
<td>ENINI400</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI401</p>
</blockquote></td>
<td>ENINI402</td>
<td>ENINI403</td>
<td><blockquote>
<p>ENINI404</p>
</blockquote></td>
<td><blockquote>
<p>ENINI405</p>
</blockquote></td>
<td><blockquote>
<p>ENINI406</p>
</blockquote></td>
<td>ENINI407</td>
<td>ENINI408</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI409</p>
</blockquote></td>
<td>ENINI410</td>
<td>ENINI411</td>
<td><blockquote>
<p>ENINI412</p>
</blockquote></td>
<td><blockquote>
<p>ENINI413</p>
</blockquote></td>
<td><blockquote>
<p>ENINI414</p>
</blockquote></td>
<td>ENINI415</td>
<td>ENINI416</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI417</p>
</blockquote></td>
<td>ENINI418</td>
<td>ENINI419</td>
<td><blockquote>
<p>ENINI420</p>
</blockquote></td>
<td><blockquote>
<p>ENINI421</p>
</blockquote></td>
<td><blockquote>
<p>ENINI422</p>
</blockquote></td>
<td>ENINI423</td>
<td>ENINI424</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI425</p>
</blockquote></td>
<td>ENINI426</td>
<td>ENINI427</td>
<td><blockquote>
<p>ENINI428</p>
</blockquote></td>
<td><blockquote>
<p>ENINI429</p>
</blockquote></td>
<td><blockquote>
<p>ENINI430</p>
</blockquote></td>
<td>ENINI431</td>
<td>ENINI432</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI433</p>
</blockquote></td>
<td>ENINI434</td>
<td>ENINI435</td>
<td><blockquote>
<p>ENINI436</p>
</blockquote></td>
<td><blockquote>
<p>ENINI437</p>
</blockquote></td>
<td><blockquote>
<p>ENINI438</p>
</blockquote></td>
<td>ENINI439</td>
<td>ENINI440</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI441</p>
</blockquote></td>
<td>ENINI442</td>
<td>ENINI443</td>
<td><blockquote>
<p>ENINI444</p>
</blockquote></td>
<td><blockquote>
<p>ENINI445</p>
</blockquote></td>
<td><blockquote>
<p>ENINI446</p>
</blockquote></td>
<td>ENINI447</td>
<td>ENINI448</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>ENINI449</p>
</blockquote></th>
<th>ENINI450</th>
<th>ENINI451</th>
<th><blockquote>
<p>ENINI452</p>
</blockquote></th>
<th><blockquote>
<p>ENINI453</p>
</blockquote></th>
<th><blockquote>
<p>ENINI454</p>
</blockquote></th>
<th>ENINI455</th>
<th><blockquote>
<p>ENINI456</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ENINI457</p>
</blockquote></td>
<td>ENINI458</td>
<td>ENINI459</td>
<td><blockquote>
<p>ENINI460</p>
</blockquote></td>
<td><blockquote>
<p>ENINI461</p>
</blockquote></td>
<td><blockquote>
<p>ENINI462</p>
</blockquote></td>
<td>ENINI463</td>
<td><blockquote>
<p>ENINI464</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI465</p>
</blockquote></td>
<td>ENINI466</td>
<td>ENINI467</td>
<td><blockquote>
<p>ENINI468</p>
</blockquote></td>
<td><blockquote>
<p>ENINI469</p>
</blockquote></td>
<td><blockquote>
<p>ENINI470</p>
</blockquote></td>
<td>ENINI471</td>
<td><blockquote>
<p>ENINI472</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI473</p>
</blockquote></td>
<td>ENINI474</td>
<td>ENINI475</td>
<td><blockquote>
<p>ENINI476</p>
</blockquote></td>
<td><blockquote>
<p>ENINI477</p>
</blockquote></td>
<td><blockquote>
<p>ENINI478</p>
</blockquote></td>
<td>ENINI479</td>
<td><blockquote>
<p>ENINI480</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI481</p>
</blockquote></td>
<td>ENINI482</td>
<td>ENINI483</td>
<td><blockquote>
<p>ENINI484</p>
</blockquote></td>
<td><blockquote>
<p>ENINI485</p>
</blockquote></td>
<td><blockquote>
<p>ENINI486</p>
</blockquote></td>
<td>ENINI487</td>
<td><blockquote>
<p>ENINI488</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI489</p>
</blockquote></td>
<td>ENINI490</td>
<td>ENINI491</td>
<td><blockquote>
<p>ENINI492</p>
</blockquote></td>
<td><blockquote>
<p>ENINI493</p>
</blockquote></td>
<td><blockquote>
<p>ENINI494</p>
</blockquote></td>
<td>ENINI495</td>
<td><blockquote>
<p>ENINI496</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI497</p>
</blockquote></td>
<td>ENINI498</td>
<td>ENINI499</td>
<td><blockquote>
<p>ENINI500</p>
</blockquote></td>
<td><blockquote>
<p>ENINI501</p>
</blockquote></td>
<td><blockquote>
<p>ENINI502</p>
</blockquote></td>
<td>ENINI503</td>
<td><blockquote>
<p>ENINI504</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI505</p>
</blockquote></td>
<td>ENINI506</td>
<td>ENINI507</td>
<td><blockquote>
<p>ENINI508</p>
</blockquote></td>
<td><blockquote>
<p>ENINI509</p>
</blockquote></td>
<td><blockquote>
<p>ENINI510</p>
</blockquote></td>
<td>ENINI511</td>
<td><blockquote>
<p>ENINI512</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI513</p>
</blockquote></td>
<td>ENINI514</td>
<td>ENINI515</td>
<td><blockquote>
<p>ENINI516</p>
</blockquote></td>
<td><blockquote>
<p>ENINI517</p>
</blockquote></td>
<td><blockquote>
<p>ENINI518</p>
</blockquote></td>
<td>ENINI519</td>
<td><blockquote>
<p>ENINI520</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI521</p>
</blockquote></td>
<td>ENINI522</td>
<td>ENINI523</td>
<td><blockquote>
<p>ENINI524</p>
</blockquote></td>
<td><blockquote>
<p>ENINI525</p>
</blockquote></td>
<td><blockquote>
<p>ENINI526</p>
</blockquote></td>
<td>ENINI527</td>
<td><blockquote>
<p>ENINI528</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI529</p>
</blockquote></td>
<td>ENINI530</td>
<td>ENINI531</td>
<td><blockquote>
<p>ENINI532</p>
</blockquote></td>
<td><blockquote>
<p>ENINI533</p>
</blockquote></td>
<td><blockquote>
<p>ENINI534</p>
</blockquote></td>
<td>ENINI535</td>
<td><blockquote>
<p>ENINI536</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI537</p>
</blockquote></td>
<td>ENINI538</td>
<td>ENINI539</td>
<td><blockquote>
<p>ENINI540</p>
</blockquote></td>
<td><blockquote>
<p>ENINI541</p>
</blockquote></td>
<td><blockquote>
<p>ENINI542</p>
</blockquote></td>
<td>ENINI543</td>
<td><blockquote>
<p>ENINI544</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI545</p>
</blockquote></td>
<td>ENINI546</td>
<td>ENINI547</td>
<td><blockquote>
<p>ENINI548</p>
</blockquote></td>
<td><blockquote>
<p>ENINI549</p>
</blockquote></td>
<td><blockquote>
<p>ENINI550</p>
</blockquote></td>
<td>ENINI551</td>
<td><blockquote>
<p>ENINI552</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI553</p>
</blockquote></td>
<td>ENINI554</td>
<td>ENINI555</td>
<td><blockquote>
<p>ENINI556</p>
</blockquote></td>
<td><blockquote>
<p>ENINI557</p>
</blockquote></td>
<td><blockquote>
<p>ENINI558</p>
</blockquote></td>
<td>ENINI559</td>
<td><blockquote>
<p>ENINI560</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI561</p>
</blockquote></td>
<td>ENINI562</td>
<td>ENINI563</td>
<td><blockquote>
<p>ENINI564</p>
</blockquote></td>
<td><blockquote>
<p>ENINI565</p>
</blockquote></td>
<td><blockquote>
<p>ENINI566</p>
</blockquote></td>
<td>ENINI567</td>
<td><blockquote>
<p>ENINI568</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI569</p>
</blockquote></td>
<td>ENINI570</td>
<td>ENINI571</td>
<td><blockquote>
<p>ENINI572</p>
</blockquote></td>
<td><blockquote>
<p>ENINI573</p>
</blockquote></td>
<td><blockquote>
<p>ENINI574</p>
</blockquote></td>
<td>ENINI575</td>
<td><blockquote>
<p>ENINI576</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI577</p>
</blockquote></td>
<td>ENINI578</td>
<td>ENINI579</td>
<td><blockquote>
<p>ENINI580</p>
</blockquote></td>
<td><blockquote>
<p>ENINI581</p>
</blockquote></td>
<td><blockquote>
<p>ENINI582</p>
</blockquote></td>
<td>ENINI583</td>
<td><blockquote>
<p>ENINI584</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI585</p>
</blockquote></td>
<td>ENINI586</td>
<td>ENINI587</td>
<td><blockquote>
<p>ENINI588</p>
</blockquote></td>
<td><blockquote>
<p>ENINI589</p>
</blockquote></td>
<td><blockquote>
<p>ENINI590</p>
</blockquote></td>
<td>ENINI591</td>
<td><blockquote>
<p>ENINI592</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI593</p>
</blockquote></td>
<td>ENINI594</td>
<td>ENINI595</td>
<td><blockquote>
<p>ENINI596</p>
</blockquote></td>
<td><blockquote>
<p>ENINI597</p>
</blockquote></td>
<td><blockquote>
<p>ENINI598</p>
</blockquote></td>
<td>ENINI599</td>
<td><blockquote>
<p>ENINI600</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI601</p>
</blockquote></td>
<td>ENINI602</td>
<td>ENINI603</td>
<td><blockquote>
<p>ENINI604</p>
</blockquote></td>
<td><blockquote>
<p>ENINI605</p>
</blockquote></td>
<td><blockquote>
<p>ENINI606</p>
</blockquote></td>
<td>ENINI607</td>
<td><blockquote>
<p>ENINI608</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI609</p>
</blockquote></td>
<td>ENINI610</td>
<td>ENINI611</td>
<td><blockquote>
<p>ENINI612</p>
</blockquote></td>
<td><blockquote>
<p>ENINI613</p>
</blockquote></td>
<td><blockquote>
<p>ENINI614</p>
</blockquote></td>
<td>ENINI615</td>
<td><blockquote>
<p>ENINI616</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI617</p>
</blockquote></td>
<td>ENINI618</td>
<td>ENINI619</td>
<td><blockquote>
<p>ENINI620</p>
</blockquote></td>
<td><blockquote>
<p>ENINI621</p>
</blockquote></td>
<td><blockquote>
<p>ENINI622</p>
</blockquote></td>
<td>ENINI623</td>
<td><blockquote>
<p>ENINI624</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI625</p>
</blockquote></td>
<td>ENINI626</td>
<td>ENINI627</td>
<td><blockquote>
<p>ENINI628</p>
</blockquote></td>
<td><blockquote>
<p>ENINI629</p>
</blockquote></td>
<td><blockquote>
<p>ENINI630</p>
</blockquote></td>
<td>ENINI631</td>
<td><blockquote>
<p>ENINI632</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI633</p>
</blockquote></td>
<td>ENINI634</td>
<td>ENINI635</td>
<td><blockquote>
<p>ENINI636</p>
</blockquote></td>
<td><blockquote>
<p>ENINI637</p>
</blockquote></td>
<td><blockquote>
<p>ENINI638</p>
</blockquote></td>
<td>ENINI639</td>
<td><blockquote>
<p>ENINI640</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI641</p>
</blockquote></td>
<td>ENINI642</td>
<td>ENINI643</td>
<td><blockquote>
<p>ENINI644</p>
</blockquote></td>
<td><blockquote>
<p>ENINI645</p>
</blockquote></td>
<td><blockquote>
<p>ENINI646</p>
</blockquote></td>
<td>ENINI647</td>
<td><blockquote>
<p>ENINI648</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI649</p>
</blockquote></td>
<td>ENINI650</td>
<td>ENINI651</td>
<td><blockquote>
<p>ENINI652</p>
</blockquote></td>
<td><blockquote>
<p>ENINI653</p>
</blockquote></td>
<td><blockquote>
<p>ENINI654</p>
</blockquote></td>
<td>ENINI655</td>
<td><blockquote>
<p>ENINI656</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI657</p>
</blockquote></td>
<td>ENINI658</td>
<td>ENINI659</td>
<td><blockquote>
<p>ENINI660</p>
</blockquote></td>
<td><blockquote>
<p>ENINI661</p>
</blockquote></td>
<td><blockquote>
<p>ENINI662</p>
</blockquote></td>
<td>ENINI663</td>
<td><blockquote>
<p>ENINI664</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI665</p>
</blockquote></td>
<td>ENINI666</td>
<td>ENINI667</td>
<td><blockquote>
<p>ENINI668</p>
</blockquote></td>
<td><blockquote>
<p>ENINI669</p>
</blockquote></td>
<td><blockquote>
<p>ENINI670</p>
</blockquote></td>
<td>ENINI671</td>
<td><blockquote>
<p>ENINI672</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI673</p>
</blockquote></td>
<td>ENINI674</td>
<td>ENINI675</td>
<td><blockquote>
<p>ENINI676</p>
</blockquote></td>
<td><blockquote>
<p>ENINI677</p>
</blockquote></td>
<td><blockquote>
<p>ENINI678</p>
</blockquote></td>
<td>ENINI679</td>
<td><blockquote>
<p>ENINI680</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI681</p>
</blockquote></td>
<td>ENINI682</td>
<td>ENINI683</td>
<td><blockquote>
<p>ENINI684</p>
</blockquote></td>
<td><blockquote>
<p>ENINI685</p>
</blockquote></td>
<td><blockquote>
<p>ENINI686</p>
</blockquote></td>
<td>ENINI687</td>
<td><blockquote>
<p>ENINI688</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI689</p>
</blockquote></td>
<td>ENINI690</td>
<td>ENINI691</td>
<td><blockquote>
<p>ENINI692</p>
</blockquote></td>
<td><blockquote>
<p>ENINI693</p>
</blockquote></td>
<td><blockquote>
<p>ENINI694</p>
</blockquote></td>
<td>ENINI695</td>
<td><blockquote>
<p>ENINI696</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI697</p>
</blockquote></td>
<td>ENINI698</td>
<td>ENINI699</td>
<td><blockquote>
<p>ENINI700</p>
</blockquote></td>
<td><blockquote>
<p>ENINI701</p>
</blockquote></td>
<td><blockquote>
<p>ENINI702</p>
</blockquote></td>
<td>ENINI703</td>
<td><blockquote>
<p>ENINI704</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI705</p>
</blockquote></td>
<td>ENINI706</td>
<td>ENINI707</td>
<td><blockquote>
<p>ENINI708</p>
</blockquote></td>
<td><blockquote>
<p>ENINI709</p>
</blockquote></td>
<td><blockquote>
<p>ENINI710</p>
</blockquote></td>
<td>ENINI711</td>
<td><blockquote>
<p>ENINI712</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI713</p>
</blockquote></td>
<td>ENINI714</td>
<td>ENINI715</td>
<td><blockquote>
<p>ENINI716</p>
</blockquote></td>
<td><blockquote>
<p>ENINI717</p>
</blockquote></td>
<td><blockquote>
<p>ENINI718</p>
</blockquote></td>
<td>ENINI719</td>
<td><blockquote>
<p>ENINI720</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI721</p>
</blockquote></td>
<td>ENINI722</td>
<td>ENINI723</td>
<td><blockquote>
<p>ENINI724</p>
</blockquote></td>
<td><blockquote>
<p>ENINI725</p>
</blockquote></td>
<td><blockquote>
<p>ENINI726</p>
</blockquote></td>
<td>ENINI727</td>
<td><blockquote>
<p>ENINI728</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI729</p>
</blockquote></td>
<td>ENINI730</td>
<td>ENINI731</td>
<td><blockquote>
<p>ENINI732</p>
</blockquote></td>
<td><blockquote>
<p>ENINI733</p>
</blockquote></td>
<td><blockquote>
<p>ENINI734</p>
</blockquote></td>
<td>ENINI735</td>
<td><blockquote>
<p>ENINI736</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI737</p>
</blockquote></td>
<td>ENINI738</td>
<td>ENINI739</td>
<td><blockquote>
<p>ENINI740</p>
</blockquote></td>
<td><blockquote>
<p>ENINI741</p>
</blockquote></td>
<td><blockquote>
<p>ENINI742</p>
</blockquote></td>
<td>ENINI743</td>
<td><blockquote>
<p>ENINI744</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI745</p>
</blockquote></td>
<td>ENINI746</td>
<td>ENINI747</td>
<td><blockquote>
<p>ENINI748</p>
</blockquote></td>
<td><blockquote>
<p>ENINI749</p>
</blockquote></td>
<td><blockquote>
<p>ENINI750</p>
</blockquote></td>
<td>ENINI751</td>
<td><blockquote>
<p>ENINI752</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI753</p>
</blockquote></td>
<td>ENINI754</td>
<td>ENINI755</td>
<td><blockquote>
<p>ENINI756</p>
</blockquote></td>
<td><blockquote>
<p>ENINI757</p>
</blockquote></td>
<td><blockquote>
<p>ENINI758</p>
</blockquote></td>
<td>ENINI759</td>
<td><blockquote>
<p>ENINI760</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI761</p>
</blockquote></td>
<td>ENINI762</td>
<td>ENINI763</td>
<td><blockquote>
<p>ENINI764</p>
</blockquote></td>
<td><blockquote>
<p>ENINI765</p>
</blockquote></td>
<td><blockquote>
<p>ENINI766</p>
</blockquote></td>
<td>ENINI767</td>
<td><blockquote>
<p>ENINI768</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI769</p>
</blockquote></td>
<td>ENINI770</td>
<td>ENINI771</td>
<td><blockquote>
<p>ENINI772</p>
</blockquote></td>
<td><blockquote>
<p>ENINI773</p>
</blockquote></td>
<td><blockquote>
<p>ENINI774</p>
</blockquote></td>
<td>ENINI775</td>
<td><blockquote>
<p>ENINI776</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI777</p>
</blockquote></td>
<td>ENINI778</td>
<td>ENINI779</td>
<td><blockquote>
<p>ENINI780</p>
</blockquote></td>
<td><blockquote>
<p>ENINI781</p>
</blockquote></td>
<td><blockquote>
<p>ENINI782</p>
</blockquote></td>
<td>ENINI783</td>
<td><blockquote>
<p>ENINI784</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI785</p>
</blockquote></td>
<td>ENINI786</td>
<td>ENINI787</td>
<td><blockquote>
<p>ENINI788</p>
</blockquote></td>
<td><blockquote>
<p>ENINI789</p>
</blockquote></td>
<td><blockquote>
<p>ENINI790</p>
</blockquote></td>
<td>ENINI791</td>
<td><blockquote>
<p>ENINI792</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI793</p>
</blockquote></td>
<td>ENINI794</td>
<td>ENINI795</td>
<td><blockquote>
<p>ENINI796</p>
</blockquote></td>
<td><blockquote>
<p>ENINI797</p>
</blockquote></td>
<td><blockquote>
<p>ENINI798</p>
</blockquote></td>
<td>ENINI799</td>
<td><blockquote>
<p>ENINI800</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI801</p>
</blockquote></td>
<td>ENINI802</td>
<td>ENINI803</td>
<td><blockquote>
<p>ENINI804</p>
</blockquote></td>
<td><blockquote>
<p>ENINI805</p>
</blockquote></td>
<td><blockquote>
<p>ENINI806</p>
</blockquote></td>
<td>ENINI807</td>
<td><blockquote>
<p>ENINI808</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI809</p>
</blockquote></td>
<td>ENINI810</td>
<td>ENINI811</td>
<td><blockquote>
<p>ENINI812</p>
</blockquote></td>
<td><blockquote>
<p>ENINI813</p>
</blockquote></td>
<td><blockquote>
<p>ENINI814</p>
</blockquote></td>
<td>ENINI815</td>
<td><blockquote>
<p>ENINI816</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI817</p>
</blockquote></td>
<td>ENINI818</td>
<td>ENINI819</td>
<td><blockquote>
<p>ENINI820</p>
</blockquote></td>
<td><blockquote>
<p>ENINI821</p>
</blockquote></td>
<td><blockquote>
<p>ENINI822</p>
</blockquote></td>
<td>ENINI823</td>
<td><blockquote>
<p>ENINI824</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI825</p>
</blockquote></td>
<td>ENINI826</td>
<td>ENINI827</td>
<td><blockquote>
<p>ENINI828</p>
</blockquote></td>
<td><blockquote>
<p>ENINI829</p>
</blockquote></td>
<td><blockquote>
<p>ENINI830</p>
</blockquote></td>
<td>ENINI831</td>
<td><blockquote>
<p>ENINI832</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI833</p>
</blockquote></td>
<td>ENINI834</td>
<td>ENINI835</td>
<td><blockquote>
<p>ENINI836</p>
</blockquote></td>
<td><blockquote>
<p>ENINI837</p>
</blockquote></td>
<td><blockquote>
<p>ENINI838</p>
</blockquote></td>
<td>ENINI839</td>
<td><blockquote>
<p>ENINI840</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI841</p>
</blockquote></td>
<td>ENINI842</td>
<td>ENINI843</td>
<td><blockquote>
<p>ENINI844</p>
</blockquote></td>
<td><blockquote>
<p>ENINI845</p>
</blockquote></td>
<td><blockquote>
<p>ENINI846</p>
</blockquote></td>
<td>ENINI847</td>
<td><blockquote>
<p>ENINI848</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI849</p>
</blockquote></td>
<td>ENINI850</td>
<td>ENINI851</td>
<td><blockquote>
<p>ENINI852</p>
</blockquote></td>
<td><blockquote>
<p>ENINI853</p>
</blockquote></td>
<td><blockquote>
<p>ENINI854</p>
</blockquote></td>
<td>ENINI855</td>
<td><blockquote>
<p>ENINI856</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI857</p>
</blockquote></td>
<td>ENINI858</td>
<td>ENINI859</td>
<td><blockquote>
<p>ENINI860</p>
</blockquote></td>
<td><blockquote>
<p>ENINI861</p>
</blockquote></td>
<td><blockquote>
<p>ENINI862</p>
</blockquote></td>
<td>ENINI863</td>
<td><blockquote>
<p>ENINI864</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI865</p>
</blockquote></td>
<td>ENINI866</td>
<td>ENINI867</td>
<td><blockquote>
<p>ENINI868</p>
</blockquote></td>
<td><blockquote>
<p>ENINI869</p>
</blockquote></td>
<td><blockquote>
<p>ENINI870</p>
</blockquote></td>
<td>ENINI871</td>
<td><blockquote>
<p>ENINI872</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI873</p>
</blockquote></td>
<td>ENINI874</td>
<td>ENINI875</td>
<td><blockquote>
<p>ENINI876</p>
</blockquote></td>
<td><blockquote>
<p>ENINI877</p>
</blockquote></td>
<td><blockquote>
<p>ENINI878</p>
</blockquote></td>
<td>ENINI879</td>
<td><blockquote>
<p>ENINI880</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI881</p>
</blockquote></td>
<td>ENINI882</td>
<td>ENINI883</td>
<td><blockquote>
<p>ENINI884</p>
</blockquote></td>
<td><blockquote>
<p>ENINI885</p>
</blockquote></td>
<td><blockquote>
<p>ENINI886</p>
</blockquote></td>
<td>ENINI887</td>
<td><blockquote>
<p>ENINI888</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI889</p>
</blockquote></td>
<td>ENINI890</td>
<td>ENINI891</td>
<td><blockquote>
<p>ENINI892</p>
</blockquote></td>
<td><blockquote>
<p>ENINI893</p>
</blockquote></td>
<td><blockquote>
<p>ENINI894</p>
</blockquote></td>
<td>ENINI895</td>
<td><blockquote>
<p>ENINI896</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI897</p>
</blockquote></td>
<td>ENINI898</td>
<td>ENINI899</td>
<td><blockquote>
<p>ENINI900</p>
</blockquote></td>
<td><blockquote>
<p>ENINI901</p>
</blockquote></td>
<td><blockquote>
<p>ENINI902</p>
</blockquote></td>
<td>ENINI903</td>
<td><blockquote>
<p>ENINI904</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI905</p>
</blockquote></td>
<td>ENINI906</td>
<td>ENINI907</td>
<td><blockquote>
<p>ENINI908</p>
</blockquote></td>
<td><blockquote>
<p>ENINI909</p>
</blockquote></td>
<td><blockquote>
<p>ENINI910</p>
</blockquote></td>
<td>ENINI911</td>
<td><blockquote>
<p>ENINI912</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI913</p>
</blockquote></td>
<td>ENINI914</td>
<td>ENINI915</td>
<td><blockquote>
<p>ENINI916</p>
</blockquote></td>
<td><blockquote>
<p>ENINI917</p>
</blockquote></td>
<td><blockquote>
<p>ENINI918</p>
</blockquote></td>
<td>ENINI919</td>
<td><blockquote>
<p>ENINI920</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI921</p>
</blockquote></td>
<td>ENINI922</td>
<td>ENINI923</td>
<td><blockquote>
<p>ENINI924</p>
</blockquote></td>
<td><blockquote>
<p>ENINI925</p>
</blockquote></td>
<td><blockquote>
<p>ENINI926</p>
</blockquote></td>
<td>ENINI927</td>
<td><blockquote>
<p>ENINI928</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI929</p>
</blockquote></td>
<td>ENINI930</td>
<td>ENINI931</td>
<td><blockquote>
<p>ENINI932</p>
</blockquote></td>
<td><blockquote>
<p>ENINI933</p>
</blockquote></td>
<td><blockquote>
<p>ENINI934</p>
</blockquote></td>
<td>ENINI935</td>
<td><blockquote>
<p>ENINI936</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI937</p>
</blockquote></td>
<td>ENINI938</td>
<td>ENINI939</td>
<td><blockquote>
<p>ENINI940</p>
</blockquote></td>
<td><blockquote>
<p>ENINI941</p>
</blockquote></td>
<td><blockquote>
<p>ENINI942</p>
</blockquote></td>
<td>ENINI943</td>
<td><blockquote>
<p>ENINI944</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI945</p>
</blockquote></td>
<td>ENINI946</td>
<td>ENINI947</td>
<td><blockquote>
<p>ENINI948</p>
</blockquote></td>
<td><blockquote>
<p>ENINI949</p>
</blockquote></td>
<td><blockquote>
<p>ENINI950</p>
</blockquote></td>
<td>ENINI951</td>
<td><blockquote>
<p>ENINI952</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI953</p>
</blockquote></td>
<td>ENINI954</td>
<td>ENINI955</td>
<td><blockquote>
<p>ENINI956</p>
</blockquote></td>
<td><blockquote>
<p>ENINI957</p>
</blockquote></td>
<td><blockquote>
<p>ENINI958</p>
</blockquote></td>
<td>ENINI959</td>
<td><blockquote>
<p>ENINI960</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI961</p>
</blockquote></td>
<td>ENINI962</td>
<td>ENINI963</td>
<td><blockquote>
<p>ENINI964</p>
</blockquote></td>
<td><blockquote>
<p>ENINI965</p>
</blockquote></td>
<td><blockquote>
<p>ENINI966</p>
</blockquote></td>
<td>ENINI967</td>
<td><blockquote>
<p>ENINI968</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI969</p>
</blockquote></td>
<td>ENINI970</td>
<td>ENINI971</td>
<td><blockquote>
<p>ENINI972</p>
</blockquote></td>
<td><blockquote>
<p>ENINI973</p>
</blockquote></td>
<td><blockquote>
<p>ENINI974</p>
</blockquote></td>
<td>ENINI975</td>
<td><blockquote>
<p>ENINI976</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI977</p>
</blockquote></td>
<td>ENINI978</td>
<td>ENINI979</td>
<td><blockquote>
<p>ENINI980</p>
</blockquote></td>
<td><blockquote>
<p>ENINI981</p>
</blockquote></td>
<td><blockquote>
<p>ENINI982</p>
</blockquote></td>
<td>ENINI983</td>
<td><blockquote>
<p>ENINI984</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENINI985</p>
</blockquote></td>
<td>ENINI986</td>
<td>ENINI987</td>
<td><blockquote>
<p>ENINI988</p>
</blockquote></td>
<td><blockquote>
<p>ENINI989</p>
</blockquote></td>
<td><blockquote>
<p>ENINI990</p>
</blockquote></td>
<td>ENINI991</td>
<td><blockquote>
<p>ENINI992</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENINI993</p>
</blockquote></td>
<td>ENINI994</td>
<td>ENINI995</td>
<td><blockquote>
<p>ENINI996</p>
</blockquote></td>
<td><blockquote>
<p>ENINI997</p>
</blockquote></td>
<td><blockquote>
<p>ENINI998</p>
</blockquote></td>
<td>ENINI999</td>
<td><blockquote>
<p>ENINIT</p>
</blockquote></td>
</tr>
</tbody>
</table>

ENINIT0 ENINIT1 ENINIT2 ENINIT3 ENINIT4 ENJ ENJC2 ENJDPL ENJINJ ENJINJ1 ENJINJ2 ENJINJ3 ENJINK ENJINQ ENJMUL ENJPARAM ENLBL ENLBL1 ENLBL10

ENLBL11 ENLBL12 ENLBL15 ENLBL16 ENLBL2 ENLBL3 ENLBL4 ENLBL5 ENLBL6 ENLBL7 ENLBL8 ENLBL9 ENLIB ENLIB1 ENLIB2 ENMAN ENNEWPK2 ENNEWPKG ENNTEG ENNTEG0 ENPL1 ENPL10 ENPL11 ENPL1A ENPL2 ENPL3 ENPL3A ENPL3B ENPL4 ENPL5

ENPL5A ENPL5B ENPL5C ENPL6 ENPL7 ENPL7A ENPL7B ENPL7C ENPL8 ENPL8A ENPL9 ENPOST ENPROJ ENPROJ1 ENPROJ2 ENPROJ3 ENPROJ7 ENPROJ8 ENPROJ9 ENPRP ENPRP1 ENPRP2 ENPRP3 ENPRP4 ENPRP5 ENPRP6 ENSA ENSA1 ENSA2 ENSA3 ENSA4 ENSA5 ENSA6 ENSA7 ENSA8 ENSA9 ENSED ENSED0 ENSED1 ENSED2 ENSP ENSP1 ENSP2 ENSP3 ENSP4 ENSP5 ENSP6 ENTEXT ENWARD ENWARD1 ENWARD2 ENWO ENWO1

ENWO2 ENWOCOMP ENWOD ENWOD1 ENWOD2 ENWOD3 ENWOINV ENWONEW ENWONEW1 ENWONEW2 ENWOP ENWOP1 ENWOP2 ENWOP3 ENWOREP ENWOST

\>D ^ENINIT

This version (#7.0) of 'ENINIT' was created on 17-AUG-1993 (at by VA FileMan V.19.0)

I HAVE TO RUN AN ENVIRONMENT CHECK ROUTINE. I AM GOING TO SET UP THE FOLLOWING FILES:

446.4 BARCODE PROGRAM (including data)• Note: You already have the 'BARCODE PROGRAM' File.

Shall I write over the existing Data Definition? YES// NO

- I will OVERWRITE your data with mine.

446.6 SPECIALTY COMMANDS (including data)• Note: You already have the 'SPECIALTY COMMANDS' File.

Shall I write over the existing Data Definition? YES// NO Want my data to overwrite yours? YES// NO

> 6910 ENG INIT PARAMETERS•

> **NOTE:** You already have the 'ENG INIT PARAMETERS' File.

> 6910.1 ENGINEERING COMPUTER PORT•

> **NOTE:** You already have the 'ENGINEERING COMPUTER PORT' File.

6910.2 ENG SOFTWARE OPTIONS (including data)• Note: You already have the 'ENG SOFTWARE OPTIONS' File. Want my data to overwrite yours? YES//

6910.9 ENG DJ SCREEN (including data)• Note: You already have the 'ENG DJ SCREEN' File.

- I will OVERWRITE your data with mine.

> 6911 EQUIPMENT CATEGORY•

> **NOTE:** You already have the 'EQUIPMENT CATEGORY' File.

6912 MANUFACTURER LIST FILE (including data)• Note: You already have the 'MANUFACTURER LIST FILE' File. Want my data to overwrite yours? YES// NO

> 6914 EQUIPMENT INV.•

> **NOTE:** You already have the 'EQUIPMENT INV.' File.

> 6914.1 CMR•

> **NOTE:** You already have the 'CMR' File.

> 6914.2 PM PROCEDURES•

> **NOTE:** You already have the 'PM PROCEDURES' File. Shall I write over the existing Data Definition? YES//

> 6916 BERS SURVEY•

> **NOTE:** You already have the 'BERS SURVEY' File.

6917 CATEGORY STOCK NUMBER (including data)• Note: You already have the 'CATEGORY STOCK NUMBER' File. Want my data to overwrite yours? YES// NO

> 6919 ENG ARCHIVE LOG•

> **NOTE:** You already have the 'ENG ARCHIVE LOG' File.

> 6920 WORK ORDER \#•

> **NOTE:** You already have the 'WORK ORDER \#' File.

6920.1 NEW WORK ACTION (including data)• Note: You already have the 'NEW WORK ACTION' File. Want my data to overwrite yours? YES//

6921 WORK CENTER CODE (including data)• Note: You already have the 'WORK CENTER CODE' File. Shall I write over the existing Data Definition? YES// Want my data to overwrite yours? YES//

> 6922 ENGINEERING SECTION LIST•

> **NOTE:** You already have the 'ENGINEERING SECTION LIST' File. Shall I write over the existing Data Definition? YES//

> 6924 FSA-2162 REPORT•

> **NOTE:** You already have the 'FSA-2162 REPORT' File. Shall I write over the existing Data Definition? YES//

6924.1 FSA-ACCIDENT ACTIVITY (including data)• Note: You already have the 'FSA-ACCIDENT ACTIVITY' File. Shall I write over the existing Data Definition? YES// Want my data merged with yours? YES//

6924.2 FSA-ACCIDENT NATURE (including data)• Note: You already have the 'FSA-ACCIDENT NATURE' File.

- I will OVERWRITE your data with mine.

6924.3 FSA-DIVISION/SERVICE (including data)• Note: You already have the 'FSA-DIVISION/SERVICE' File. Shall I write over the existing Data Definition? YES// Want my data merged with yours? YES//

> 6925 CONSTRUCTION PROJECT•

> **NOTE:** You already have the 'CONSTRUCTION PROJECT' File.

6925.2 PROJECT STATUS (including data)• Note: You already have the 'PROJECT STATUS' File.

- I will OVERWRITE your data with mine.

> 6926 EMPLOYEE(KEYS)•

> **NOTE:** You already have the 'EMPLOYEE(KEYS)' File. Shall I write over the existing Data Definition? YES//

> 6927 LOCKS•

> **NOTE:** You already have the 'LOCKS' File.

Shall I write over the existing Data Definition? YES//

> 6928 ENG SPACE•

> **NOTE:** You already have the 'ENG SPACE' File.

Shall I write over the existing Data Definition? YES//

6928.1 ENG SPACE FUNCTIONS (including data)• Note: You already have the 'ENG SPACE FUNCTIONS' File. Shall I write over the existing Data Definition? YES// Want my data merged with yours? YES//

6928.2 ENG SPACE UTILITIES (including data)• Note: You already have the 'ENG SPACE UTILITIES' File. Shall I write over the existing Data Definition? YES// Want my data merged with yours? YES//

> 6928.3 ENG BUILDING•

> **NOTE:** You already have the 'ENG BUILDING' File.

> 6929 ENG EMPLOYEE•

> **NOTE:** You already have the 'ENG EMPLOYEE' File.

Shall I write over the existing Data Definition? YES// 7335.7 REGULATORY AGENCY (including data)•

> **NOTE:** You already have the 'REGULATORY AGENCY' File.

- I will OVERWRITE your data with mine.

7336.3 OFM SPACE CLASSIFICATION (including data)• Note: You already have the 'OFM SPACE CLASSIFICATION' File.

- I will OVERWRITE your data with mine.

7336.6 OFM H089 CHAPTERS (including data)• Note: You already have the 'OFM H089 CHAPTERS' File.

- I will OVERWRITE your data with mine.

7336.8 OFM PROJ CATEGORY (including data)• Note: You already have the 'OFM PROJ CATEGORY' File.

- I will OVERWRITE your data with mine.

7336.9 OFM BUDGET CATEGORY (including data)• Note: You already have the 'OFM BUDGET CATEGORY' File.

- I will OVERWRITE your data with mine.

SHALL I WRITE OVER FILE SECURITY CODES? NO// Y (YES)

> **NOTE:** This package also contains BULLETINS

> SHALL I WRITE OVER EXISTING BULLETINS OF THE SAME NAME?

YES// (YES)

> **NOTE:** This package also contains SORT TEMPLATES

SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains PRINT TEMPLATES

SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains FUNCTIONS

> SHALL I WRITE OVER EXISTING FUNCTIONS OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains SECURITY KEYS

> SHALL I WRITE OVER EXISTING SECURITY KEYS OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains OPTIONS

> SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// (YES)

ARE YOU SURE EVERYTHING'S OK? NO// Y (YES)

......................

...SORRY, LET ME PUT YOU ON 'HOLD' FOR A SECOND.................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

............................

...('Changes to MCCR AR Tasks' BULLETIN WILL NOT BE TRIGGERED)...

'EN NEW EQUIPMENT' BULLETIN FILED -- Remember to add mail groups for new

bulletins..............................................................................

................................................................................

..........................................

'ENACTUAL' Option Filed 'ENAE' Option Filed 'ENAPPROV' Option Filed 'ENAR' Option Filed

'ENAR-ARCHIVE' Option Filed

'ENAR-ASSEMBLE' Option Filed 'ENAR-DELETE' Option Filed 'ENAR-LOG' Option Filed 'ENAR-RECALL' Option Filed 'ENBCEE ALL' Option Filed 'ENBCEE CAT' Option Filed 'ENBCEE CMR' Option Filed 'ENBCEE LID' Option Filed 'ENBCEE PM' Option Filed 'ENBCEE PMLIST' Option Filed 'ENBCEE PO' Option Filed 'ENBCEE RM' Option Filed 'ENBCEE SD' Option Filed 'ENBCEE SRVC' Option Filed 'ENBCEE WING' Option Filed 'ENBCLBL MGR' Option Filed 'ENBCLBLEE' Option Filed 'ENBCLBLSP' Option Filed 'ENBCNX MGR' Option Filed 'ENBCNXCMR' Option Filed 'ENBCNXDNLD' Option Filed 'ENBCNXMAN' Option Filed 'ENBCNXRES' Option Filed 'ENBCPM MGR' Option Filed 'ENBCPMDNLD' Option Filed 'ENBCPMRES' Option Filed 'ENBCSP ALL' Option Filed 'ENBCSP BLDG' Option Filed 'ENBCSP RM' Option Filed 'ENBCSP WING' Option Filed 'ENBCUPLD' Option Filed 'ENCCLERK' Option Filed 'ENCHANGES' Option Filed 'ENCMR' Option Filed 'ENCONTR' Option Filed 'ENCSN' Option Filed

'ENDSY' Option Filed 'ENEMP' Option Filed 'ENENT' Option Filed

'ENEQ-FAILURE' Option Filed 'ENEQ-INVENTORY' Option Filed 'ENEQ-PLANNER' Option Filed 'ENEQ-REPLACE' Option Filed 'ENEQ-REPORTS' Option Filed 'ENEQ-WARRANTY' Option Filed 'ENEQHID' Option Filed 'ENEQINV1' Option Filed 'ENEQINV2' Option Filed 'ENEQINV3' Option Filed 'ENEQINV4' Option Filed 'ENEQINV5' Option Filed 'ENEQINV6' Option Filed 'ENEQPOST' Option Filed 'ENETRANSFER' Option Filed 'ENEUSER1' Option Filed

'ENFS-2162' Option Filed

'ENFS-2162-ACC. NATURE SUMMARY' Option Filed 'ENFS-2162-DISPLAY' Option Filed

'ENFS-2162-EDIT' Option Filed 'ENFS-2162-ENTER' Option Filed

'ENFS-2162-INJURY SUMMARY' Option Filed 'ENFS-2162-LOCATION SUMMARY' Option Filed 'ENFS-2162-SERVICE SUMMARY' Option Filed

'ENGSADDPRT1' Option Filed 'ENGSCONPRT1' Option Filed 'ENGSGENPRT1' Option Filed 'ENGSMENU' Option Filed 'ENGSSURPRT1' Option Filed 'ENGSSURVEYINPUT' Option Filed 'ENIN-ENTER-MULTI' Option Filed 'ENIN-HIST-GENERIC' Option Filed

'ENIN-HIST-SPECIFIC' Option Filed

'ENINV' Option Filed 'ENINV EDIT' Option Filed 'ENINVINV' Option Filed 'ENINVNEW' Option Filed 'ENMAN' Option Filed 'ENMANUFAC' Option Filed 'ENMGR' Option Filed 'ENMM MGR' Option Filed 'ENMM UTIL' Option Filed 'ENMMBC' Option Filed 'ENMMEE' Option Filed 'ENMMREP' Option Filed 'ENPLM01' Option Filed 'ENPLM02' Option Filed 'ENPLM03' Option Filed 'ENPLM04' Option Filed 'ENPLM05' Option Filed 'ENPLM06' Option Filed 'ENPLM08' Option Filed 'ENPLM09' Option Filed 'ENPLM11' Option Filed 'ENPLM12' Option Filed 'ENPLM13' Option Filed 'ENPLM14' Option Filed 'ENPLM15' Option Filed 'ENPLM16' Option Filed 'ENPLM17' Option Filed 'ENPLM18' Option Filed 'ENPM' Option Filed 'ENPM1' Option Filed 'ENPM10' Option Filed 'ENPM2' Option Filed 'ENPM3' Option Filed 'ENPM4' Option Filed 'ENPM5' Option Filed 'ENPM6' Option Filed 'ENPM7' Option Filed 'ENPM8' Option Filed 'ENPMHOURS' Option Filed 'ENPMINSP' Option Filed 'ENPMR' Option Filed 'ENPMR1' Option Filed 'ENPMR2' Option Filed 'ENPMR3' Option Filed 'ENPMRDEFRL' Option Filed 'ENPMS' Option Filed 'ENPORT' Option Filed 'ENPREL' Option Filed 'ENPROJ' Option Filed 'ENPROJ TKR' Option Filed 'ENPROJ10' Option Filed 'ENPROJSTAT' Option Filed 'ENPROJXMIT' Option Filed 'ENREV' Option Filed 'ENSA1' Option Filed 'ENSCREEN' Option Filed 'ENSEC' Option Filed 'ENSECFORM' Option Filed 'ENSECTION' Option Filed 'ENSITE' Option Filed 'ENSP' Option Filed

'ENSP-137-AMIS' Option Filed 'ENSP-LEASE' Option Filed 'ENSP-LEASE1' Option Filed 'ENSP-LEASE2' Option Filed 'ENSP-LEASE3' Option Filed 'ENSP-PLAN' Option Filed 'ENSP-PLAN1' Option Filed 'ENSP-PLAN2' Option Filed 'ENSP1' Option Filed

'ENSP144' Option Filed 'ENSP2' Option Filed 'ENSP3' Option Filed

'ENSP3-FUNCTION-NSF' Option Filed

'ENSP3-RCS10-0141' Option Filed 'ENSP3-SERVICE-NSF' Option Filed 'ENSP4' Option Filed

'ENSP5' Option Filed 'ENSPBLDG' Option Filed 'ENSPEDKEY' Option Filed 'ENSPEMP' Option Filed 'ENSPFRS1' Option Filed 'ENSPFRS2' Option Filed 'ENSPFRS3' Option Filed 'ENSPFRS4' Option Filed 'ENSPFUNC' Option Filed 'ENSPKEY' Option Filed 'ENSPLOCK' Option Filed 'ENSPRM' Option Filed 'ENSPRMKY' Option Filed 'ENSPROOM' Option Filed 'ENSPROOMD' Option Filed 'ENSPSER' Option Filed 'ENSPSRV' Option Filed 'ENSPUTL' Option Filed 'ENSPUTL-CLEAN' Option Filed 'ENSPUTL1' Option Filed 'ENSPUTL2' Option Filed 'ENSPUTL3' Option Filed 'ENSPUTL4' Option Filed 'ENSWOPT' Option Filed 'ENWCLERK' Option Filed 'ENWO' Option Filed

'ENWO-STATS-DPT' Option Filed 'ENWO-STATS-EMP' Option Filed 'ENWO-STATS-LOC' Option Filed 'ENWO-STATS-SHOP' Option Filed 'ENWO-STATUS-(HC)' Option Filed 'ENWO-STATUS-(XQ)' Option Filed 'ENWO-TRANSFER' Option Filed 'ENWOCLOSE' Option Filed 'ENWODISAP' Option Filed 'ENWOEDIT-WARD' Option Filed 'ENWONEW' Option Filed

'ENWONEW-WARD' Option Filed 'ENWOREP' Option Filed 'ENWORK ACTION' Option Filed 'ENWORK CTR' Option Filed 'ENWOST-WARD' Option Filed

'ENWOSTATUS-WARD' Option Filed

'ENWOWARD' Option Filed.........................................................

.........

Compiling ENPLP005 print template of File 6925..................................

.............................. 'ENPLPC' ROUTINE FILED

'ENPLPC1' ROUTINE FILED............

Compiling ENPLP006 print template of File 6925..................................

.................................................................

...

'ENPLPB' ROUTINE FILED 'ENPLPB1' ROUTINE FILED

'ENPLPB2' ROUTINE FILED....................

Compiling ENPLP008 print template of File 6925..................................

.................................................................

...

'ENPLPA' ROUTINE FILED 'ENPLPA1' ROUTINE FILED

'ENPLPA2' ROUTINE FILED........................

Compiling ENPLP009 print template of File 6925..................................

................................................................ 'ENPLPD' ROUTINE FILED

'ENPLPD1' ROUTINE FILED

'ENPLPD2' ROUTINE FILED..............................

NOTE THAT FILE SECURITY-CODE PROTECTION HAS BEEN MADE...........

Now re-building your Work Order File............................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

........................................

Now re-indexing Work Order File. This could take awhile........................

................................................................................

................................................................................

................................................................................

................................................................................

..........................................................................

Now converting LOCATIONS in your Equipment File.................................

................................................................................

...........................................................................

Now converting Work Order LOCATIONS.............................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

......................................................

Now converting a few data elements in your existing construction projects. This shouldn't take very long....

Now re-indexing

Finished at JUL 29, 1993@18:56.