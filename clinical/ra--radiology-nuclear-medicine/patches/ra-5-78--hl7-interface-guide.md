---
title: RA*5*78 HL7 Interface Spec for Voice Recognition Release Notes
doc_type: INT
doc_label: Interface Specification
doc_layer: patch
doc_subject: HL7 Interface Spec for Voice Recognition Release Notes
app_code: RA
app_name: Radiology/Nuclear Medicine
section: CLI
app_status: archive
pkg_ns: RA
patch_ver: 5
patch_id: RA*5*78
group_key: "RA:RA:5"
file_numbers: []
security_keys: []
menu_options: 0
description: RA\5.0\78 allows the VistA Radiology/Nuclear Medicine application to accept an inbound query from ScImage and return radiology results back to ScImage. This historical information serves as a reference for the teleradiologists working for the NTP project.
audience: 
keywords: 
  - patch
  - table
  - contents
  - group
  - mail
  - radiology
  - scimage
  - port
  - query
  - notes
page_count: 0
word_count: 985
section_count: 1
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2009
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra5_0rn_p78.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra5_0rn_p78.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=384"
---

![](ra-5-78-hl7-interface-spec-for-voice-recognition-release-notes/001.png)

Radiology/Nuclear Medicine  
Release Notes

Patch RA\*5.0\*78  
May 2009

Health Systems Design & Development

Provider Systems

# # # # # Release Notes for Patch RA\*5.0\*78


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# # # # Release Notes for Patch RA\5.0\78](#release-notes-for-patch-ra5078)
- [Overview](#overview)
- [HL7 Report Query Patch](#hl7-report-query-patch)
    - [Sort Criteria](#sort-criteria)
    - [Conditions for Patch 78](#conditions-for-patch-78)
    - [Exported Components](#exported-components)
- [During Installation](#during-installation)
- [After Installation](#after-installation)
Patch RA\*5.0\*78 is an enhancement patch in support of the VHA National Radiology Program office initiative to integrate teleradiology (remote-read) reports into VistA.
A new National Teleradiology Program (NTP) reading center is established in California and staffed by VHA radiologists. VA medical centers may contract with the NTP to provide daytime or after-hours interpretation of imaging studies.

# Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RA\*5.0\*78 allows the VistA Radiology/Nuclear Medicine application to accept an inbound query from ScImage and return radiology results back to ScImage. This historical information serves as a reference for the teleradiologists working for the NTP project.

Notes: Associated patch RA\*5.0\*84 must be installed before you install RA\*5.0\*78.  
Patch 78 can be installed with Radiology users on the system.  
Install time for Patch 78 is less than two minutes.

# HL7 Report Query Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch RA\*5.0\*78 allows ScImage to query the VistA Radiology/Nuclear Medicine 5.0.

Application for results.

> **NOTE:** ScImage is a specific vendor. The query was developed to be vendor independent; however, ScImage is the vendor currently contracted by the NTP.  
\*\*\*ATTENTION–for present NTP sites only–when installing RA\*5.0\*78, it is critical that this vendor be contacted to turn off the NTP Query component of the interface. Contact the Outlook mail group, VHA NTP CONFIGURATION SUPPORT, to coordinate VA facility and vendor implementation and configuration.\*\*\*

### Sort Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two different sort criteria for the query. The client (ScImage) can request results based on:

1.  A single accession number (one patient/one result), or
2.  A patient record number, within a patient care event date/time window, and maximum number of results to be returned on that patient.

### Conditions for Patch 78

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order for the patch to work as intended, there is a dependency on properly setting up HLO.

> **NOTE:** Sites must refer to *Patch HL\*1.6\*126 Installation Manual/Release Notes* (HL_1_6_126.ig) on the VDL. 

- Cache/VMS sites must review section 5.2
- Cache/NT sites must review section 5.4[^1]

In order for the patch to operate properly, two conditions must be met.

1.  Determine the IP address of the HLO multi-threaded listener.
1.  The listener is setup as a TCP/IP service and is defined to *listen* on port 5001.
2.  This information is necessary for ScImage to properly communicate with the VistA Radiology/Nuclear Medicine application.
3.  For first time NTP integration at VA facilities, the RA-SCIMAGE logical link must have the following fields defined with specific values.

| Field Name          | Field Number | Field Value |
|-------------------------|------------------|-----------------|
| TCP/IP PORT             | 400.02           | 21999           |
| TCP/IP PORT (OPTIMIZED) | 400.08           | 21998           |

> **NOTE:** Some facilities went on-line with NTP when they installed RA\*5.0\*84.

- Coordinate with the NTP troubleshooting staff to change the value of the TCP/IP PORT to 21999 on the VistA-side of the interface, so that the same TCP/IP PORT value of 21999 is applied to the NTP server.
- A number of facilities acted as test sites for RA\*5.0\*78. These test sites may have a value in the TCP/IP PORT (OPTIMIZED) field different than the suggested value of 21998. The sites must not change the TCP/IP PORT (OPTIMIZED) value.
- Contact the NTP troubleshooting staff via Outlook at mail group: VHA NTP ERROR or call: 650-615-6063 or 650-814-3660.

### Exported Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  HLO Application Registry
- RA-NTP-QUERY
- RA-NTP-RSP
2.  Mail Group

> RAD HL7 MESSAGES

# During Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You are asked to identify the coordinator of the RAD HL7 MESSAGES mail group during installation.

Enter the Coordinator for Mail Group 'RAD HL7 MESSAGES':

> **NOTE:** Use the RAD HL7 MESSAGES mail group to identify a core set of radiology support staff that can monitor Health Level Seven (HL7) broadcasts between the Vista Radiology/Nuclear Medicine application and the Commercial Off The Shelf (COTS) products. Email messages are specifically sent to the members of this mail group whenever a COTS inbound HL7 message is received by VistA provided the VistA-side business rules find the HL7 message *deficient*.

- Identify the Radiology ADPAC as the coordinator of the mail group, if your site has a Radiology ADPAC.
- To add additional recipients (Members) of the message, edit the mail group using the option Mail Group Edit.  
  (Menu path: Manage Mailman -\> Group/Distribution Management -\> Mail Group Edit)
- The backup Radiology ADPAC and the software support personnel responsible for the VistA Radiology/Nuclear Medicine application at your facility can be additional members of this mail group.

Notes: You must add POSTMASTER as a member of the RAD HL7 MESSAGES mail group in order to broadcast messages to the RAD HL7 MESSAGES mail group.  
When prompted to enter an additional member, set TYPE to INFO.  
INFO indicates that the message is transmitted to all members as an informational message. Members cannot reply to informational messages.  
  
The MEMBER subfile of the RAD HL7 MESSAGES mail group must be populated with *active* facility personnel in addition to Postmaster.

# After Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After you install Patch RA\*5.0\*78, follow this menu path to edit the RA-SCIMAGE logical link.

Select OPTION NAME: HLO MAIN MENU HL7 (Optimized) MAIN MENU

SM HLO SYSTEM MONITOR

MV HLO MESSAGE VIEWER

APPS HLO APPPLICATION REGISTRY

STAT HLO MESSAGE STATISTICS

ES HLO ERROR STATISTICS

EL Link Edit \<-- this is the option

Select HL7 (Optimized) MAIN MENU Option: Link Edit

Select HL LOGICAL LINK NODE: RA-SCIMAGE \<-- this is the logical link

Edit the two fields: DNS DOMAIN (#.08) and TCP/IP PORT (OPTIMIZED) (#400.08).

1.  Ask the network manager the Domain Name Server (DNS) value for the local NTP Gateway Server.  
    The DNS value is the translation of the IP Address value of the RA-SCIMAGE logical link into a human-readable domain name value.
4.  Enter the DNS value of the NTP Gateway Server into the DNS DOMAIN field.
5.  Sites installing this patch for the first time, enter <span class="mark">REDACTED</span> into the TCP/IP PORT (OPTIMIZED) field.

> **NOTE:** VistA port table assignments are reserved in the TCP Port Registry as follows:  
Port <span class="mark">REDACTED</span> is reserved for NTP/Patch RA\*5.0\*78  
Port <span class="mark">REDACTED</span> is reserved for NTP/Patch RA\*5.0\*84

[^1]: July 2009: Added information about the dependence of Patch 78 on the proper set up of HLO.