---
consolidated_title: "install guide"
app_code: IB
doc_type: IG
master_source: "IB*2*499 Install Guide"
master_pub_date: revision_count: 0
consolidated_from: 2 versions
prior_versions:
  - "IB*2*476 Install Guide"
---

NEWBORN DG FB IB PATCH BUNDLEINSTALLATION GUIDE

![](ib-2-499-install-guide/001.png)

Patches DG\*5.3\*867, FB\*3.5\*146, IB\*2.0\*499September 2013

Office of Information and Technology

Product Development

# # Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Revision History](#revision-history)
- [Installation](#installation)
  - [Overview](#overview)
    - [Document Retrieval](#document-retrieval)
  - [Prerequisites](#prerequisites)
  - [Pre/Post-Installation Overview](#prepost-installation-overview)
  - [Pre-Installation Instructions](#pre-installation-instructions)
- [Post-Installation Instructions](#post-installation-instructions)
- [Technical Guide](#technical-guide)
  - [Post-Install Routine Summary](#post-install-routine-summary)
Table i. Revision History
<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 55%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Description</strong></th>
<th><strong>Project Mgr/Technical Writer</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>9/2013</td>
<td><p>NEWBORN DG FB IB BUNDLE 1.0 multi-build Installation Instructions.</p>
<p>This patch supports changes that allow the Electronic Filing of Newborn claims.</p></td>
<td><ul>
<li><blockquote>
<p>Project Manager<br />
REDACTED</p>
</blockquote></li>
<li><blockquote>
<p>Lead Developer<br />
REDACTED</p>
</blockquote></li>
<li><blockquote>
<p>Technical Writer<br />
REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>
Contents

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Users should be made aware that processing of Newborn claims must ONLY be entered in VistA. No entry in FBCS should be performed.Note: This bundle will automatically install three patches (FB\*3.5\*146, DG\*5.3\*867, IB\*2.0\*499) in the correct order.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This bundle has enhancements that extend the capabilities of the Veterans Health Information Systems and Technology Architecture (VistA) Patient Registration system (DG), Fee Basis System (FB), and Integrated Billing (IB). Below is a list of all the applications involved in this project along with their patch number:

| Application/Version             | Patch        |
|---------------------------------|--------------|
| PATIENT REGISTRATION (DG) V 5.3 | DG\*5.3\*867 |
| FEE BASIS (FB) V 3.5            | FB\*3.5\*146 |
| INTEGRATED BILLING (IB) 2.0     | IB\*2.0\*499 |

The patches (DG\*5.3\*867, FB\*3.5\*146, and IB\*2.0\*499) are being released in the Kernel Installation and Distribution System (KIDS) multi-build distribution NEWBORN DG FB IB BUNDLE 1.0.

The purpose of the Caregivers: Newborn Claims Processing Enhancement Project is to enhance VistA Fee Basis application in support of compliance with Public Law 111-163, the Caregiver and Veterans Omnibus Health Services Act of 2010. This law makes changes to sections of Title 38, United States Code to furnish health care services to a newborn child of a Woman Veteran who is receiving maternity care furnished by the Department of Veterans Affairs (VA) for not more than seven days after the birth of the child.

The scope of these enhancements is to capture information on healthcare services provided to newborn children of Women Veterans. Affected functions include eligibility determination, enrollment and registration, documentation of referrals and authorization for care, claims processing, and payment. Only modification to the Fee Basis (FB) and the Registration (DG) packages are necessary to meet the requirements of this enhancement. The Integrated Billing (IB) Patch is included to provide required data for the Fee Basis install to reference.

This enhancement's primary purpose is to allow the Electronic Filing of Newborn claims.

### Document Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new functionality introduced by this bundle is available.

The preferred method is to FTP the files from REDACTED. This transmits the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows:

Albany REDACTED \<REDACTED\>

Hines REDACTED \<REDACTED\>

Salt Lake City REDACTED \<REDACTED\>

The documentation will be in the form of Adobe Acrobat files.

Documentation can also be found on the VA Software Documentation Library at: <http://www.va.gov/vdl/>

File Description File Name FTP Mode

-----------------------------------------------------------------------------------------------

Fee Basis User Manual fb3_5um.pdf Binary

PIMS v5.3 ADT User Manual Registration dg_5_3_reg_um.pdf Binary

The procedure guide, Care for Newborn of Women Veterans, located at REDACTD should be distributed to those personnel registering newborns and/or processing newborn claims.

## Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This bundle may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This bundle should take less than 5 minutes to install.

FB\*3.5\*147 is a required patch and must be installed before this bundle.

## Pre/Post-Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three post installation routines associated with this bundle: ^DG867PO, ^FB146PO, and ^IB499PO. These routines primarily serve as filters for the data transmitted to the appropriate files listed above, so that only the intended data is delivered. The only exception is the ^IB499PO routine which programmatically makes an addition to the help text of the FAMILY PREFIX field (#.03) in the file SPONSOR RELATIONSHIP file (#355.81). The post-installation routines may be deleted after successful installation of the NEWBORN DG FB IB BUNDLE 1.0.

## Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  OBTAIN PATCHES

Obtain the host file NEWBORN_1_2_DG_FB_IB.KID which contains the following patches:

DG\*5.3\*867

FB\*3.5\*146

IB\*2.0\*499

Sites can retrieve VistA software from the following FTP addresses. The preferred method is to FTP the files from:

REDACTED

This will transmit the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows:

> Albany REDACTED

Hines REDACTED

Salt Lake City REDACTED

The NEWBORN_1_2_DG_FB_IB.KID host file is located in the anonymous.software directory. Use ASCII Mode when downloading the file.

2.  START UP KIDS

Start up the Kernel Installation and Distribution System Menu option \[XPD MAIN\]:

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: Installation

Load a Distribution

Print Transport Global

Compare Transport Global to Current System

Verify Checksums in Transport Global

Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Backup a Transport Global

Select Installation Option:

3.  LOAD TRANSPORT GLOBAL FOR MULTI-BUILD

From the Installation menu, select the Load a Distribution option.

When prompted for "Enter a Host File:" Enter the full directory path where you saved the host file NEWBORN_1_2_DG_FB_IB.KID (e.g., SYS\$SYSDEVICE:\[ANONYMOUS\]NEWBORN_1_2_DG_FB_IB.KID).

When prompted for "OK to continue with Load? NO//", Enter "YES."

The following will display:

Loading Distribution...

NEWBORN DG FB IB BUNDLE 1.0

DG\*5.3\*867

FB\*3.5\*146

IB\*2.0\*499

Use INSTALL NAME: NEWBORN DG FB IB BUNDLE 1.0 to install this distribution.

4.  RUN OPTIONAL INSTALLATION OPTIONS FOR MULTI-BUILD

From the Installation menu, you may select to use the following options (when prompted for the INSTALL NAME, enter NEWBORN DG FB IB BUNDLE 1.0

1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as data dictionaries or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, data dictionaries, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
5.  INSTALL MULTI-BUILD

This is the step to start the installation of this KIDS patch. This will need to be run for the NEWBORN DG FB IB BUNDLE 1.0

1.  Choose the Install Package(s) option to start the patch install.
2.  When prompted for the "Select INSTALL NAME:", enter NEWBORN DG FB IB BUNDLE 1.0
3.  When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//", answer NO.
4.  When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//", answer NO.
5.  When prompted "Device: HOME//", enter HOME to display the Install message on the screen (or enter the device you want to print the Install message). You may queue the install if you wish.

# Post-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The FB146PO Post-Install Routine creates the following four additional routines:

- FBCTAU
- FBCTAU1
- FBCTAU2
- FBCTAU3Note: Also, please note there are three post installation routines that may be deleted after successful installation of the NEWBORN DG FB IB BUNDLE 1.0. These are:
- DG867PO
- FB146PO
- IB499PO

# Technical Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Post-Install Routine Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

^IB499PO

^DG867PO

^FB146PO

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: IB*2*476 Install Guide

## IB\*2.0\*476

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## December 2012

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Version 1.3 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Office of Information and Technology (OIT) Product Development

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 11%" />
<col style="width: 43%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>July 2, 2012</p>
</blockquote></td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td><blockquote>
<p>Initial document creation</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>November 7, 2012</p>
</blockquote></td>
<td><blockquote>
<p>1.1</p>
</blockquote></td>
<td><blockquote>
<p>Added Prerequisites section and Updated post-installation instructions section</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>November 30,2012</p>
</blockquote></td>
<td><blockquote>
<p>1.2</p>
</blockquote></td>
<td><blockquote>
<p>Updated Prerequisites information</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>December</p>
</blockquote></td>
<td><blockquote>
<p>1.3</p>
</blockquote></td>
<td><blockquote>
<p>Updated from patch return</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> ii IB\*2.0\*476 Installation Guide December 2012
