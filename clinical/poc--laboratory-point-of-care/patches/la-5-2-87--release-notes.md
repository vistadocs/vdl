---
title: "LA*5.2*87 Laboratory: POC VHIC Card Update Release Notes"
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: "Laboratory: POC VHIC Card Update"
app_code: POC
app_name: "Laboratory: Point of Care"
section: CLI
app_status: active
pkg_ns: LA
patch_ver: 5.2
patch_id: LA*5.2*87
group_key: "POC:LA:5.2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - installation
  - vhic
  - transport
  - global
  - patient
  - release
  - instructions
  - patch
page_count: 0
word_count: 646
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2018
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Point_of_Care/LA_87_VHIC_Card_Update.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Point_of_Care/LA_87_VHIC_Card_Update.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=149"
---

---
title: |
  LABORATORY (LA\*5.2\*87)

  Veterans Health Identification Card (VHIC) Update

  Release Notes
---

![](la-5-2-87-laboratory-poc-vhic-card-update-release-notes/001.png)

June 2018

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Table Of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Purpose](#purpose)
- [This Release](#this-release)
- [Known Issues](#known-issues)
- [Pre-Installation Instructions](#pre-installation-instructions)
- [Installation Instructions](#installation-instructions)
Before LA\*5.2\*87 was released, Lab Point of Care functionality did not allow the use of VHIC. With the release of this patch, VistA will recognize the patient when the complete VHIC identification string is transmitted by the Point of Care (POC) Health Level (HL) 7 interface.

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to communicate possible limitations when using VHIC.

# This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A patient’s VHIC may be used on a POC device if (1) the site’s HL7 interface sends the patient identifier on the barcode without removing trailing spaces from the VHIC ID and (2) the interface is not dependent on an Automated Data Transfer (ADT) HL7 interface feed.

# Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some POC vendors do not send the complete patient identifier when a VHIC card is scanned. Trailing spaces on the barcode may be deleted by the vendor before sending the transaction to VistA, or the vendor may not be able to send all of the 15 to 18 characters which are required by VistA to identify the patient.

Other vendors are dependent on the Social Security Number (SSN) of the patient which must be sent to an ADT HL7 feed to determine patient identity. ADT HL7 interfaces cannot accept a VHIC card identifier. Sites can check if they are using the ADT feed for POC testing by using the LA7 MESSAGE PARAMETER (#62.48) option from the Lab POC setup menu:

Select Lab Universal Interface Menu Option: PCS Lab Point of Care Setup

Select one of the following:

1 LA7 MESSAGE PARAMETER (#62.48)

2 LOAD/WORK LIST (#68.2)

3 AUTO INSTRUMENT (#62.4)

4 Print POC Test Code Mapping

Select which file to setup: 1 LA7 MESSAGE PARAMETER (#62.48)

Select LA7 MESSAGE PARAMETER CONFIGURATION: LA7POC3

Does this POC interface want to receive VistA ADT messages? YES// \<\<\< if YES here, and the HL7 logical link LA7POC3A is running, the ADT feed is being used.Note: VHIC may not be used when the ADT feed is in use.

# Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LA\*5.2\*88 must be installed before LA\*5.2\*87.

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be loaded with users on the system. Install during non-peak hours. Installation will take less than one (1) minute.

> **NOTE:** Kernel patches must be current on the target system to avoid problems loading and/or installing this patch.

1.  Use the 'INSTALL/CHECK MESSAGE' option of the PackMan menu. This option will load the KIDS patch onto the system.
2.  The patch has now been loaded into a Transport global on the system. Now use KIDS to install the transport global.
3.  On the 'Kernel Installation & Distribution System' Menu (KIDS), select the 'Installation' menu.
4.  Use the 'Verify Checksum in Transport Global' option and verify that all routines have the correct checksums.
5.  On the KIDS menu, under the 'Installation' menu, use the following options:
- Print Transport Global
- Compare Transport Global to Current System
- Backup a Transport Global

  Preserve a copy of the routines exported in this patch prior to installation. The 'Backup a Transport Global' option should be used. Compare the routines in the production account to the routines in the patch by using the 'Compare a Transport Global to Current System' option.
6.  Use the 'Install Package(s)' option under the 'Installation' menu and select the package 'LA\*5.2\*87'.

    If prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//, choose 'NO'.

    When prompted 'Want to DISABLE Scheduled Options, Menu Options, and

    Protocols? NO//', choose 'NO'.