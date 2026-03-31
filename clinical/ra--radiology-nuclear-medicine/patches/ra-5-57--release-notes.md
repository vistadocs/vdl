---
title: RA*5*57 (PFSS) Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: (PFSS)
app_code: RA
app_name: Radiology/Nuclear Medicine
section: CLI
app_status: archive
pkg_ns: RA
patch_ver: 5
patch_id: RA*5*57
group_key: "RA:RA:5"
file_numbers: 
  - 79
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - pfss
  - table
  - contents
  - account
  - radiology
  - reference
  - patch
  - routines
  - class
  - door
page_count: 0
word_count: 1274
section_count: 7
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra5_0rn_p57.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra5_0rn_p57.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=384"
---

![](ra-5-57-pfss-release-notes/001.png)

RADIOLOGY/NUCLEAR MEDICINE

RELEASE NOTES

Patch RA\*5.0\*57

March 2006

Health Systems Design & Development

Provider Systems

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Patient Financial Services System](#patient-financial-services-system)
  - [Patch Overview](#patch-overview)
  - [Software Interfaces](#software-interfaces)
- [Radiology RA\5\57 Enhancements](#radiology-ra557-enhancements)
  - [New Fields](#new-fields)
    - [RAD/NUC MED ORDERS File (#75.1)](#radnuc-med-orders-file-751)
    - [IMAGING TYPE File (#79.2)](#imaging-type-file-792)
- [Radiology RA\5\57 Routines](#radiology-ra557-routines)
  - [New Routines](#new-routines)
  - [Modified Routines](#modified-routines)

## Patient Financial Services System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch is part of the Patient Financial Services System (PFSS) project. PFSS patches are being released on various schedules. Some patch functionality will not be active until a new PFSS switch is activated during final implementation. PFSS will initially be implemented at select pilot sites ONLY.

The purpose of the PFSS project is to prepare the Veterans Health Information Systems and Technology Architecture (VistA) environment for the implementation of a commercial off-the-shelf (COTS) billing replacement system. The project consists of the implementation of the billing replacement system, business process improvements, and enhancements to VistA to support integration with the COTS billing replacement system. Significant changes to VistA legacy systems and ancillary packages are necessary.

Some of the PFSS software components are not operational until the PFSS On/Off Switch, distributed with patch IB\*2\*260, is set to “ON”. The ability for the local site to set the switch to “ON” will be provided at the appropriate time with the release of a subsequent Integrated Billing patch.

For more information about the PFSS project, review the documentation accompanying this patch and refer to the following website:

> <http://vista.med.va.gov/billreplace/>

These release notes provide a brief description of the enhancements to the Radiology project provided in Patch RA\*5\*57.

## Patch Overview 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The COTS billing system handles the billing functionality by incorporating a patient account number for all billable patient activity. The Radiology package does not currently support the use of a patient “account number.” The RA\*5\*57 patch supplies the modifications and enhancements necessary to provide this “account awareness.” All outpatient appointments or encounters created within a PFSS-enabled system will generate a PFSS Account Reference through an IBB API.

The enhancements in this patch will ensure that all orders have:

- A PFSS Account Reference that is associated to the order
- A valid Current Procedural Terminology (CPT) code, service date, and department code for sending to Patient Care Encounter (PCE) for proper charge of Radiology procedures

No changes will be noticeable to the user community because of the modifications made for this project. Neither new prompts nor any changes to report output or formatting will occur. No additional processing time should be noticed as a result of these modifications.

The functionality installed by this patch will be invisible to users of the Radiology menus. The menus will call an IBB API in the background that will generate the PFSS Account Reference and return it for storage in the PFSS ACCOUNT file (#375).

For the new functionality to request and store the account number reference during appointment management, three conditions must be met:

1.  Patch IB\*2\*286 must be installed (these are the new IBB utilities and files).
2.  Clinical Indicator Data Capture (CIDC) Patch RA\*5\*41 must be installed.
3.  The PFSS On/Off Switch must be enabled at the site.

If these three conditions are not met, the Radiology functionality will continue to operate as it does currently.

> NOTE: IB\*2\*286 does not need to be installed for this patch to be installed. Until the PFSS switch is activated, the Radiology package will ignore any of the installed modifications.

## Software Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Radiology/Nuclear Medicine V. 5.0 is required to be installed prior to these enhancements. Radiology/Nuclear Medicine V. 5.0 relies, at a minimum, on the following external packages:

> Kernel V. 8.0

> VA FileMan V. 22.0

> MailMan V. 8.0

> VistA Health Level 7 (HL7) V. 1.6

> CPRS V. 26

> IB V. 2.0

> PCE V. 1.0

# Radiology RA\*5\*57 Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two new fields have been added, in the RAD/NUC MED ORDERS file and the IMAGING TYPE file. The new fields are described in detail below.

### RAD/NUC MED ORDERS File (#75.1)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PFSS ACCOUNT REFERENCE field (#90) contains information associated with the account reference obtained from IBB. This is a pointer to the PFSS ACCOUNT file (#375).

### IMAGING TYPE File (#79.2)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PFSS Dept. Code field (#90) contains information representing the department code used by the PFSS project.

# Radiology RA\*5\*57 Routines 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new routines provided by RA\*5\*57 are listed in the table below.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routine Name</strong></th>
<th><strong>Routine Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>RA57PST</td>
<td>The post installation routine that will loop through file #79.2 and insert the appropriate Department Code. This routine may be deleted after RA*5*57 is installed.</td>
</tr>
<tr class="even">
<td>RABWIBB</td>
<td><ul>
<li><p>Checks the switch status, to initialize some input variables for an IBB API</p></li>
<li><p>Gets a PFSS Account Reference for both CPRS (front door) and Radiology (back door) orders</p></li>
<li><p>Cancels a PFSS Account Reference</p></li>
<li><p>Retrieves the Department Code and PFSS Account Reference</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>RABWIBB2</td>
<td><ul>
<li><p>Sets up the remaining variables required by an IBB API</p></li>
<li><p>Then calls the IBB API to collect the new PFSS Account Reference that is passed back to the calling routines</p></li>
<li><p>Stores the PFSS Account Reference in the RAD/NUC MED ORDERS file (#75.1)</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Modified Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The modified routines provided by RA\*5\*57 are listed in the table below.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routine Name</strong></th>
<th><strong>Routine Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>RABWORD</td>
<td>Triggers the process of retrieving a new PFSS Account Reference when a new order is placed, from both CPRS (front door) and from Radiology (back door). It will not trigger this process if a back door order was updated from CPRS.</td>
</tr>
<tr class="even">
<td>RABWORD1</td>
<td>Flags that Radiology is processing a CPRS update to the ordering Diagnosis (Dx) and ordering clinical indicators of a back door order.</td>
</tr>
<tr class="odd">
<td>RAO7OKS</td>
<td><ul>
<li><p>Gets a new PFSS Account Reference for a new order placed from CPRS (front door). This number will be passed back to CPRS in a new PV1 segment of the pseudo HL7 message and will be stored in the Radiology application</p></li>
<li><p>Cancels an existing PFSS Account Reference when an order is discontinued from CPRS (front door)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>RAO7UTL</td>
<td>Includes the PFSS Account Reference in the PV1 segment of the pseudo HL7 message to CPRS, for a Radiology (back door) order.</td>
</tr>
<tr class="odd">
<td>RAORDU</td>
<td>Checks if the Request Status is DISCONTINUE, and if it is, sends a “Delete” event to IBB.</td>
</tr>
<tr class="even">
<td>RAPCE</td>
<td>Checks the PFSS status switch and if it is active will send the Department Code and PFSS Account Reference to PCE.</td>
</tr>
</tbody>
</table>