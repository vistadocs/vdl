---
title: GCS Version 2 Package Security Guide
doc_type: SG
doc_label: Security Guide
doc_layer: anchor
doc_subject: Package
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
description: 
audience: 
keywords: 
  - code
  - sheet
  - generic
  - table
  - contents
  - sheets
  - security
  - files
  - package
  - stack
page_count: 0
word_count: 901
section_count: 6
table_count: 31
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 1995
revision_count: 2
revision_newest: 12/22/04
revision_oldest: 12/22/04
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Generic_Code_Sheet_(GCS)/gcs2sec.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Generic_Code_Sheet_(GCS)/gcs2sec.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=7"
---

Decentralized Hospital Computer Program

GENERIC CODE SHEETPACKAGE SECURITY GUIDE

March 1995

Information Systems Center

Washington, D.C.

Preface

This Package Security Guide is designed to provide the Information Security Officer with information necessary to maintain security with Version 2.0 of the Generic Code Sheet package.

Table of Contents

Introduction

Security Information

A. Naming Conventions
B. Files
C. File Security
D. Description of Files
E. Overwriting Data
F. Globals
G. Resource Requirements
H. Security Keys
I. Mail Groups
J. Menu Options
K. Archiving and Purging

Glossary

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

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Security Information](#security-information)
  - [A. Naming Conventions](#a-naming-conventions)
  - [B. Files](#b-files)
  - [C. File Security](#c-file-security)
  - [D. Description of Files](#d-description-of-files)
*The SF CIO Field Office added hard page breaks to this document to keep the paging the same when the document was transferred and converted to a different version of MS Word. The TOC was also adjusted to coincide with the original version of this document. No other text/content changes were made.*
The Generic Code Sheet package is a Decentralized Hospital Computer Program (DHCP) software module which manages the input, editing, deletion, and transmission of code sheets from a local hospital computer system to a centralized computer system as defined by the code sheet.
The Generic Code Sheet package contains a code sheet file, GENERIC CODE SHEET (#2100), to be used to define field definitions to support the code sheets. The field definitions describe the type of data to be stored in the actual code sheet. The fields can be arranged in an input template in the order they will be used to create the code sheet.
Once the code sheet data has been created, the code sheets can be marked for batching. Batching the code sheets will group like code sheets together for transmission. When the code sheets are transmitted, all code sheets within the batch will be transmitted in the same VA MailMan message. The exception to this is the Financial Management System (FMS) code sheets. When the FMS code sheets are created they are queued for transmission using the GENERIC CODE SHEET STACK file (#2100.1), thus bypassing the batching process. The code sheets are transmitted from the stack file by a background VA TaskManager job which can be run every 2 hours, 3 hours, etc. as specified by the systems manager.

# Security Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## A. Naming Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The namespace assigned to the Generic Code Sheet package is GEC. All routines are located in the GECS namespace except for the initialization routines which begin with GECI. The only global exported as part of the Generic Code Sheet package is GECS. Namespaced variables of special note are listed in the Package-wide Variable section of the manual.

## B. Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Generic Code Sheet package exports and uses the following files:

2100 GENERIC CODE SHEET

2100.1 GENERIC CODE SHEET STACK

2101.1 GENERIC CODE SHEET BATCH TYPE

2101.2 GENERIC CODE SHEET TRANSACTION

TYPE/SEGMENT

2101.3 GENERIC CODE SHEET TRANSMISSION RECORD

2101.4 GENERIC CODE SHEET TEMPLATE MAPS (not used)

2101.5 GENERIC CODE SHEET COUNTER

2101.6 GENERIC CODE SHEET LOCK

2101.7 GENERIC CODE SHEET SITE

## C. File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All files exported with the Generic Code Sheet package Version 2.0 have the following security codes:

Data Dictionary (DD) Access: @

Read (RD) Access: @

Write (WR) Access: @

Delete (DEL) Access: @

LAYGO Access: @

## D. Description of Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The GENERIC CODE SHEET file (#2100) is used to store the actual code sheets which have been automatically created by the system (except for the Financial Management (FMS) code sheets which are placed in the GENERIC CODE SHEET STACK file (#2100.1)) or manually created by the user. This file contains all the  
fields and input templates which are used to create the code sheets. The fields are used to define the data which appears on the code sheet. The input templates define the order the fields should appear on the code sheets and the order the fields should be asked to the user.

The GENERIC CODE SHEET STACK file (#2100.1) is used to store the Financial Management System (FMS) code sheets which are ready for transmission. When a user manually creates and marks an FMS code sheet for transmission, it is moved to the GENERIC CODE SHEET STACK file (#2100.1). When the system automatically creates an FMS code sheet, it is automatically entered into the GENERIC CODE SHEET STACK file (#2100.1) bypassing the GENERIC CODE SHEET file (#2100). The code sheets are transmitted from the stack file and the STATUS field (#3) is used to monitor the code sheet's progress.

The GENERIC CODE SHEET BATCH TYPE file (#2101.1) is used to store the name of the application, service, or code sheet type, for example Dental, MAS, Financial Management, etc. The GENERIC CODE SHEET TRANSACTION TYPE/SEGMENT file (#2101.2) is used to store the name of each individual code sheet. The two files are linked using the BATCH TYPE Field (#.7) in the GENERIC CODE SHEET TRANSACTION TYPE/SEGMENT file (#2101.2). This allows each individual code sheet to be grouped under an application, service, or code sheet type. Both of these files are exported with data.

The GENERIC CODE SHEET TRANSMISSION RECORD

## ## ## ## ## ## ## # |     |     |
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|-----|-----|
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |

|     |     |
|-----|-----|
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |
|     |     |

|     |     |
|-----|-----|
|     |     |