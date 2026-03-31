---
title: XQOR Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: plain
doc_subject: 
app_code: XQOR
app_name: Kernel Unwinder
section: INF
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: - [Revision History](#revision-history) - [Preface](#preface) - [Unwinder Installation](#unwinder-installation) This document describes the installation of the XQOR routines. These routines are used in conjunction with the Protocol file to create modular building blocks for applications. The Unwinde
audience: 
keywords: 
  - installation
  - table
  - contents
  - unwinder
  - routines
  - xqor
  - guide
  - revision
  - history
  - preface
page_count: 0
word_count: 191
section_count: 2
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 1994
revision_count: 1
revision_newest: 2/27/15
revision_oldest: 2/27/15
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel_Unwinder/xqorig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel_Unwinder/xqorig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=13"
---

---
title: Kernel Unwinder Installation Guide
---

![](xqor-installation-guide/001.png)

Office of Information and Technology (OI&T)

Original Software Release: August 1994

Revised Documentation Release: February 2015

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Date | Description                                                                                                               | Author                                       |
|----------|-------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| 2/27/15  | Converted document to MS-Word 2007 format and incorporated *<u>some</u>* format changes from the ProPath User Guide Template. | Infrastructure Technical Writer, Oakland, OIFO   |
| 8/1994   | Original release titled “Unwinder (XQOR)”                                                                                     | Information Systems Center, Salt Lake City, Utah |

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
- [Preface](#preface)
- [Unwinder Installation](#unwinder-installation)
This document describes the installation of the XQOR routines. These routines are used in conjunction with the Protocol file to create modular building blocks for applications. The *Unwinder Installation Guide* is intended for DHCP IRM (Information Resource Management) personnel at VAMCs.
Related Manuals:
*Unwinder Technical Manual*

# Unwinder Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

n NO files, options, security keys, etc. are exported with this utility.

n The following XQOR routines are exported:

> XQOR XQOR1 XQOR2 XQOR3 XQOR4 XQORD XQORD1

> XQORI001 XQORINI1 XQORINI2 XQORINI3 XQORINI4 XQORINI5 XQORINIS

> XQORINIT XQORM XQORM1 XQORM2 XQORM3 XQORM4 XQORM5

> XQORM6 XQORMX XQORNTEG XQORO

n Required DHCP packages:

> <u>Package</u> <u>Version</u>

> Kernel 7.1

> Toolkit 7.2 (including patch \# XT\*7.2\*5)

> OE/RR 2.5

1. Run XQORINIT. This init does nothing except create a package file entry. (NO files, options, security keys, etc. are exported with the inits.)

> \><u>D ^XQORINIT</u>

> This version (#7.1) of 'XQORINIT' was created on 18-AUG-1994

> (at SLC, by VA FileMan V.20.0)

> ARE YOU SURE EVERYTHING'S OK? NO// <u>Y</u> (YES)

> ...EXCUSE ME, HOLD ON......

> \>

2. Delete init routines (XQORI\*).
3. On DSM systems, the XQOR routines should be mapped (except for XQOto make for smoother extensively by OE/RR, Problem List, Discharge Summary, Health Summary, etc.