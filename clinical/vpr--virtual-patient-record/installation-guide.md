---
title: Virtual Patient Record (VPR) Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: plain
doc_subject: Virtual Patient Record (VPR)
app_code: VPR
app_name: Virtual Patient Record
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: This document provides instructions for installing Virtual Patient Record (VPR) version 1.0. VPR is a foundation software package component of the Health Management Platform architecture. This architecture is part of the scope of the Health Informatics Initiative. VPR extracts patient data from doma
audience: 
keywords: 
  - contents
  - table
  - installation
  - patient
  - package
  - remote
  - extract
  - proxy
  - version
  - routines
page_count: 0
word_count: 780
section_count: 3
table_count: 9
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 2
revision_newest: 05/14/2012
revision_oldest: 08/08/11
docx_url: "https://www.va.gov/vdl/documents/Clinical/virtual_patient_record/vpr_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/virtual_patient_record/vpr_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=197"
---

![](virtual-patient-record-vpr-installation-guide/001.png)![](virtual-patient-record-vpr-installation-guide/002.png)

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Contents](#contents)
- [Overview](#overview)
- [Installation Guide](#installation-guide)
  - [Instructions](#instructions)
  - [Verification](#verification)
- [Checksums](#checksums)
- [Uninstalling VPR](#uninstalling-vpr)
|            |                  |      |                                                                                                                                                       |                                      |                                      |
|------------|------------------|------|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------|--------------------------------------|
| Date       | Patch or Version | Page | Description                                                                                                                                           | Project Manager                      | Author                               |
| 05/14/2012 | 1.0              | 4    | Added section for uninstalling VPR software as required by the National Release Checklist; corrected minor formatting issues; updated date in footer; | <span class="mark">*REDACTED*</span> | <span class="mark">*REDACTED*</span> |
| 08/08/11   | 1.0              |      | VPR version 1.0 Release                                                                                                                               | <span class="mark">*REDACTED*</span> | <span class="mark">*REDACTED*</span> |
|            |                  |      |                                                                                                                                                       |                                      |                                      |
|            |                  |      |                                                                                                                                                       |                                      |                                      |

# Contents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document provides instructions for installing Virtual Patient Record (VPR) version 1.0. VPR is a foundation software package component of the Health Management Platform architecture. This architecture is part of the scope of the Health Informatics Initiative. VPR extracts patient data from domains at local and remote VistA sites to provide a cached view of patient charts. It provides normalized fields with common field names and data structures across domains. VPR includes two remote procedure calls (RPCs), one comprised of routines that extract data from VistA and the other that returns the current version number for VPR.

The VPR RPC for data extraction was initially installed in the Nationwide Health Information Network (NwHIN) namespace, which was called NHIN, and the NwHIN client has been using most of the extract routines in production to get and share data.

With this product release, the VPR RPCs will be installed in its own VPR namespace and renumbered as VPR version 1.0. NwHIN can continue to use the extract routines in its NHIN namespace, but will need to access VPR v1.0, or subsequent versions as they are released, in order to take advantage of future enhancements to the extract routines.

Four routines in this release are new, have not previously been released to NHIN:

VPRDGMRC Consults extract  
VPRDGPF Patient Record Flags extract  
VPRDOR Orders extract  
VPRDPXHF Health Factors extract

# Installation Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VPR RPC package consists of the following three files:

|               |                        |                          |
|---------------|------------------------|--------------------------|
| File Name | Contents           | FTP Retrieval Format |
| VPR1_0.KID    | KIDS build             | ASCII                    |
| VPR_TM.PDF    | Technical manual       | Binary                   |
| VPR_IG.PDF    | VPR Installation guide | Binary                   |

Retrieve these files via FTP from <span class="mark">*REDACTED*</span>, which transmits the files from the first available FTP server (preferred method). You can also retrieve the files directly from one of the following FTP sites:

|                                      |                                      |                                      |
|--------------------------------------|--------------------------------------|--------------------------------------|
| OI Field Office                  | FTP Address                      | Directory                        |
| <span class="mark">*REDACTED*</span> | <span class="mark">*REDACTED*</span> | <span class="mark">*REDACTED*</span> |
| <span class="mark">*REDACTED*</span> | <span class="mark">*REDACTED*</span> | <span class="mark">*REDACTED*</span> |
| <span class="mark">*REDACTED*</span> | <span class="mark">*REDACTED*</span> | <span class="mark">*REDACTED*</span> |

You can install this package release with users on the system; however, to minimize disruption to users, you should install it at a non-peak time. Installation should take less than one minute.

This package release adds the following file entries:

- VPR APPLICATION PROXY—OPTION file(#19)
- VPR GET PATIENT DATA—REMOTE PROCEDURE file (#8994)
- VPR DATA VERSION—REMOTE PROCEDURE file (#8994)

## Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the VistA Kernel Installation & Distribution System (KIDS) menu:

1.  Using ASCII format, retrieve the KIDS file VPR1_0.KID
2.  Select the Load a Distribution option and enter VPR1_0.KID when prompted at the host file prompt. You may need to prefix a directory name.  
    Example: VA16\$:\[SMAVISTA.IRMPERSON\]VPR1_0.KID
3.  Select any or all of the following options (KIDS Installation Menu) as desired:
    - Print Transport Global
    - Compare Transport Global to Current System
    - Verify Checksums in Transport Global
    - Backup a Transport Global
4.  Use the Install Package(s) option, which is located under the KIDS menu’s INSTALLATION submenu. At the Select INSTALL NAME: Prompt, respond: VPR 1.0
5.  At the Want KIDS to Rebuild Menu Trees Upon Completion of Install? Prompt, respond: NO.
6.  At the Want KIDS to INHIBIT LOGONs during the install? Prompt, respond: NO.
7.  At the Want to DISABLE Scheduled Options, Menu Options, and Protocols? Prompt, respond: NO.
8.  When the installation is completed, use the Kernel Delete Routines option \[XTRDEL\] to delete the VPRPI initialization routine.

## Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the FileMan Inquiry option to verify the VPR 1.0 package’s M-VistA installation.

Verify that:

1.  The VPR package entry exists in the PACKAGE file (# 9.4).
2.  The VPR GET PATIENT DATA and VPR DATA VERSION remote procedure entries exist in the REMOTE PROCEDURE file (#8994).
3.  The APP PROXY ALLOWED field is set to *Yes* for VPR GET PATIENT DATA and VPR DATA VERSION in the REMOTE PROCEDURE file (#8994)
4.  The VPR APPLICATION PROXY option exists in the OPTION file (#19) and

    the VPR GET PATIENT DATA and VPR DATA VERSION remote procedures are attached to this option.
5.  The installation process created the VPR, APPLICATION PROXY entry in the NEW PERSON file (file \#200) and the entry has the VPR APPLICATION PROXY option assigned as a secondary menu.  
      
    Example FileMan Inquire from file 200:  
      
    NAME: VPR,APPLICATION PROXY DATE ENTERED: JUL 13, 2011

    CREATOR: IRM,PERSON

    SECONDARY MENU OPTIONS: VPR APPLICATION PROXY

    User Class: APPLICATION PROXY ISPRIMARY: Yes

    PROVIDER KEY (c): 0

# Checksums

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table contains checksums for the VPR routines VPR GET PATIENT DATA:

| \# | Routine                     | Checksum |
|--------|---------------------------------|--------------|
| 1      | VPRD                            | 24278674     |
| 2      | VPRDGMPL                        | 20610705     |
| 3      | VPRDGMRA                        | 21412184     |
| 4      | VPRDGMRC                        | 10314726     |
| 5      | VPRDGMV                         | 39440303     |
| 6      | VPRDGPF                         | 5569926      |
| 7      | VPRDLR                          | 24712747     |
| 8      | VPRDLRA                         | 69605973     |
| 9      | VPRDLRO                         | 27350157     |
| 10     | VPRDOR                          | 9187731      |
| 11     | VPRDPROC                        | 8662758      |
| 12     | VPRDPS                          | 14378656     |
| 13     | VPRDPSI                         | 41960179     |
| 14     | VPRDPSO                         | 68282901     |
| 15     | VPRDPT                          | 65865871     |
| 16     | VPRDPXHF                        | 9504608      |
| 17     | VPRDPXIM                        | 15857859     |
| 18     | VPRDRA                          | 39795192     |
| 19     | VPRDSDAM                        | 9762566      |
| 20     | VPRDSR                          | 29738621     |
| 21     | VPRDTIU                         | 61120410     |
| 22     | VPRDVSIT                        | 71801802     |
|        | VPRPI \<\< post install routine | 300624       |

# Uninstalling VPR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VPR consists of two RPCs, a few options, and the supporting routines that can simply be deleted if a site would ever want to remove the package from their system.  Backing out VPR only requires deleting any items in the VPR namespace.