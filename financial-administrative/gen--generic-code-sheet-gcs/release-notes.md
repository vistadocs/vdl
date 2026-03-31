---
title: GCS Version 2 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
app_code: GEN
app_name: Generic Code Sheet (GCS)
section: FIN
app_status: active
pkg_ns: GEN
patch_ver: 2
patch_id: GEN*2
group_key: "GEN:GEN:2"
file_numbers: []
security_keys: []
menu_options: 0
description: - [# Release Notes](#release-notes) The Generic Code Sheet package is a Decentralized Hospital Computer Program (DHCP) software module which manages the input, editing, deletion, and transmission of code sheets from a local hospital computer system to a centralized computer system as defined by the
audience: 
keywords: 
  - code
  - sheet
  - sheets
  - generic
  - notes
  - locks
  - computer
  - table
  - contents
  - release
page_count: 0
word_count: 347
section_count: 1
table_count: 10
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 1995
revision_count: 2
revision_newest: 12/22/04
revision_oldest: 12/22/04
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Generic_Code_Sheet_(GCS)/gcs2rel.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Generic_Code_Sheet_(GCS)/gcs2rel.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=7"
---

Department of Veterans Affair

Decentralized Hospital Computer System

GENERIC CODE SHEETRELEASE NOTES

March 1995

Information Systems Center

Table of Contents

Release Notes

Revision History

Initiated on 12/22/04

|          |                                                                  |                 |                  |
|----------|------------------------------------------------------------------|-----------------|------------------|
| Date     | Description (Patch \# if applic.)                                | Project Manager | Technical Writer |
| 12/22/04 | Updated to comply with SOP 192-352 Displaying Sensitive Data.    |                 | REDACTED         |
| 12/22/04 | Pdf file checked for accessibility to readers with disabilities. |                 | REDACTED         |
|          |                                                                  |                 |                  |
|          |                                                                  |                 |                  |
|          |                                                                  |                 |                  |
|          |                                                                  |                 |                  |
|          |                                                                  |                 |                  |
|          |                                                                  |                 |                  |
|          |                                                                  |                 |                  |
|          |                                                                  |                 |                  |

# # Release Notes


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Release Notes](#release-notes)
The Generic Code Sheet package is a Decentralized Hospital Computer Program (DHCP) software module which manages the input, editing, deletion, and transmission of code sheets from a local hospital computer system to a centralized computer system as defined by the code sheet.
Generic Code Sheet V 2.0 was developed to meet the new DHCP programming standards. The software in V. 2.0 is now using incremental and decremental locks, the TMP global versus the UTILITY global, and has pointers to the NEW PERSON file 200 instead of the USER file 3. The use of incremental and decremental locks eliminates the use of the GENERIC CODE SHEET LOCK file 2101.6 to control the locking process. In V. 1.5 this file was used to manage the locks for building, batching, and transmitting code sheets. If a process failed, the GENERIC CODE SHEET LOCK file would have to be cleared by the IRM Service. With the use of incremental and decremental locks, this file is no longer used to manage the locks, but is used to give users information on why a process is locked. The file no longer has to be cleared by the IRM Service.
Generic Code Sheet V 2.0 also includes new functionality to build, transmit, and manage the Financial Management System (FMS) code sheets. The transmission and management of the FMS code sheets is accomplished by the new GENERIC CODE SHEET STACK file 2100.1. This new file stores the FMS code sheets waiting to be transmitted. At a recurring time as set by the IRM Service, a TaskManager job will start up and transmit the FMS code sheets to Austin. The code sheets are grouped in MailMan messages using a “best-fit” strategy. One MailMan message may include 20 or 30 code sheets. This strategy eliminates the overhead associated with having one code sheet per MailMan message saving in disk space and network overhead.
