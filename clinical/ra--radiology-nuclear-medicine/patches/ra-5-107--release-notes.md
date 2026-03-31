---
title: RA*5*107 National Teleradiology Program Phase 2 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: National Teleradiology Program Phase 2
app_code: RA
app_name: Radiology/Nuclear Medicine
section: CLI
app_status: archive
pkg_ns: RA
patch_ver: 5
patch_id: RA*5*107
group_key: "RA:RA:5"
file_numbers: []
security_keys: []
menu_options: 0
description: - [Release Notes for Patch RA\5.0\107](#release-notes-for-patch-ra50107) - [For Present NTP Sites only](#for-present-ntp-sites-only) - [Enhancement for NTP Patch RA\5.0\107](#enhancement-for-ntp-patch-ra50107) - [Prior to Patch Installation](#prior-to-patch-installation) - [After Patch Installation]
audience: 
keywords: 
  - patch
  - table
  - contents
  - gateway
  - query
  - vista
  - notes
  - radiology
  - installation
  - software
page_count: 0
word_count: 904
section_count: 5
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra5_0rn_p107.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra5_0rn_p107.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=384"
---

![](ra-5-107-national-teleradiology-program-phase-2-release-notes/001.png)

Radiology/Nuclear Medicine 5.0

National Teleradiology Program Phase 2

Release Notes

for Patch RA\*5.0\*107

January 2012

Health Systems Design & Development

Provider Systems

# Release Notes for Patch RA\*5.0\*107


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Release Notes for Patch RA\5.0\107](#release-notes-for-patch-ra50107)
  - [For Present NTP Sites only](#for-present-ntp-sites-only)
- [Enhancement for NTP Patch RA\5.0\107](#enhancement-for-ntp-patch-ra50107)
  - [Prior to Patch Installation](#prior-to-patch-installation)
  - [After Patch Installation](#after-patch-installation)
  - [Software and Documentation](#software-and-documentation)
The objective of this project is to provide support for the national implementation of the National Teleradiology Program as the Veterans Affairs Central Office (VACO) has requested.
Patch RA\*5.0\*107 enhances the Veterans Health Information Systems and Technology Architecture (VistA) Radiology/Nuclear Medicine (Rad/Nuc Med) 5.0 Radiology Information System (VistA RIS) package for the functionality used between the NTP and the local VA sites with an HL7 upgrade to v2.4 and VISN configuration enhancements.
The NSR number for this patch is 20080510.
Notes:
- Before you install patch 107, you must install the following patches: RA\*5\*47, MAG\*3\*49, and RA\*5\*78.
- Patch RA\*5.0\*107 patch must be installed with VistA Radiology users off-line.
- The estimated installation time for patch 107 is three minutes.

## For Present NTP Sites only 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When installing RA\*5.0\*107, you must contact the vendor and ask that the NTP Query component of the interface be turned off.

Contact the Outlook mail group:  
VHA NTP CONFIGURATION SUPPORT  
to coordinate the VA facility and vendor implementation and configuration.

# Enhancement for NTP Patch RA\*5.0\*107

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RA\*5.0\*107 has two purposes:

1.  The first is to correct a design issue with RA\*5.0\*78 (v2.3 query/response)
2.  The second is to build the query/response messaging interface to work with v2.4 of HL7

The original NTP Query/Response software (RA\*5.0\*78) was not designed to accommodate multiple legacy facilities, each with their own NTP Gateway, referencing a single VistA production system or VistA instance.

A single VistA instance recognizes only one NTP Gateway: the gateway tied to the RA-SCIMAGE logical link. That query’s responses are being broadcast to the incorrect NTP Gateway.

RA\*5.0\*107 addresses the issue by:

- receiving the NTP gateway query
- identifying the NTP Gateway that receives the query responses
- building the responses to that query
- broadcasting the responses to the correct NTP Gateway

In order to implement this business rule, all relevant NTP Gateways must be identified and logical link records created specifically for those NTP Gateways.

> **NOTE:** The number of NTP Gateways can differ from VISN to VISN. It is up the NTP technical team and the IRM staff responsible for supporting the NTP interface to create the correct logical link records.

The historical information included in the responses to a query serves as a reference for the teleradiologists working for the National Teleradiology Project (NTP).

The client (ScImage) requests results based on the following query parameters:

- A patient within a patient care event date/time window and
- The maximum number of results to be returned.

> **NOTE:** ScImage is a specific vendor. The query was developed to be vendor independent; however, ScImage is the vendor currently contracted by the NTP.

## Prior to Patch Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to operate properly, the following conditions must be met:

1.  Determine the IP address of the HLO multi-threaded listener.
- The multi-threaded listener is set up as a TCP/IP service and is defined to *listen* on port 5001.
- This information is necessary for ScImage to properly communicate with the VistA Radiology/Nuclear Medicine application.
3.  If your VistA instance broadcasts HL7 responses to more than one dedicated NTP Gateway, you must create a new logical links. The following steps must be taken:
1.  The TCP/IP ADDRESS field of these newly created logical links must be entered as the TCP/IP address of the specific NTP Gateway.
2.  The DNS DOMAIN field of these newly created logical links must be entered, in lowercase, as the DNS DOMAIN of the specific NTP Gateway.
4.  Newly created NTP Gateway logical links must have the TCP/IP PORT (OPTIMIZED) field set to a port value of: 21998.

> **NOTE:** The VA facility IRM support staff are responsible for creating and/or editing the NTP Gateway logical links.

## After Patch Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Check for any newly created logical links that are running.

Troubleshooting

- Contact the NTP troubleshooting staff via Outlook at mail group:  
  VHA NTP Support
- Call the NTP troubleshooting staff at:  
  877-780-5559 (select option \#1)

## Software and Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new functionality introduced by this patch is available.

The preferred method is to FTP the files from <span class="mark">REDACTED</span> This transmits the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows:

| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

Rad/Nuc Med Patch RA\*5.0\*107 software and documentation files are available in the following names and formats:

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 30%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>Document File Description</th>
<th>File Names</th>
<th>FTP Mode</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>Radiology/Nuclear Medicine 5.0</em></p>
<p><em>HL7 Interface Specification</em></p></td>
<td><p>RA5_0HL7spec.doc</p>
<p>RA5_0HL7spec.pdf</p></td>
<td>Binary</td>
</tr>
<tr class="even">
<td><p><em>Radiology/Nuclear Medicine 5.0</em></p>
<p><em>National Teleradiology Program Phase 2</em></p>
<p><em>Release Notes</em></p></td>
<td><p>RA5_0RN_P107.doc</p>
<p>RA5_0RN_P107.pdf</p></td>
<td>Binary</td>
</tr>
</tbody>
</table>

Rad/Nuc Med Patch RA\*5.0\*107 manuals are also available in MS Word (.docx) format and the Portable Document Format (.pdf) on the VA Software Documentation Library in the Clinical Section <http://www4.va.gov/vdl/>