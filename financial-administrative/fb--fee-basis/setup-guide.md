---
title: Fee Basis Version 3.5 Package Security Guide
doc_type: SG
doc_label: Security Guide
doc_layer: anchor
doc_subject: Package
app_code: FB
app_name: Fee Basis
section: FIN
app_status: active
pkg_ns: FB
patch_ver: 3.5
patch_id: FB*3.5
group_key: "FB:FB:3.5"
file_numbers: []
security_keys: []
menu_options: 0
description: - [General Security](#general-security) - [Audit Trails](#audit-trails) - [# # Security Keys](#security-keys) - [Legal Requirements](#legal-requirements) - [VA FileMan Access Codes](#va-fileman-access-codes) <u>NOTICE</u> > Per VHA Directive 10-93-142 regarding security of software that affects fina
audience: 
keywords: 
  - basis
  - table
  - contents
  - access
  - security
  - unauthorized
  - audit
  - codes
  - legal
  - fileman
page_count: 0
word_count: 404
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 1995
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Fee_Basis/fb3_5sg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Fee_Basis/fb3_5sg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=40"
---

Decentralized Hospital Computer Program

fee basispackage security guide

January 1995

Information Systems Center

Albany, New York

National Package Security

# General Security


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [General Security](#general-security)
- [Audit Trails](#audit-trails)
- [# # Security Keys](#security-keys)
- [Legal Requirements](#legal-requirements)
- [VA FileMan Access Codes](#va-fileman-access-codes)
<u>NOTICE</u>
> Per VHA Directive 10-93-142 regarding security of software that affects financial systems, none of the Fee Basis routines or data dictionaries may be modified.
> The Fee Basis package deals with activities and data related to the Fiscal and Fee Basis payment processes of your facility. The obvious need for package security has been addressed throughout this software, making every effort to restrict the mishandling of Fee Basis functionality. A significant amount of testing, as well as VA Central Office review, has been conducted on the entire Fee Basis package. Medical Administration Service and the Office of Budget and Finance have requested that each facility utilizing the Fee Basis package appreciate the sensitivity of these issues. It is for these reasons that each facility is reminded that local modification of the program code is expressly prohibited.
> The modification of DHCP National Package software and Data Dictionaries is restricted to the adding of new data elements and to the creation of input/output templates necessary to meet the specific needs of the local facility.
> The concern for package security extends to the menus assigned to the Fee Basis users. No Fee Basis user should have access to all of the options available. While a Fee Medical Clerk should be able to open, close, edit, or reopen a Fee Basis batch by utilizing multiple batch options, the Fiscal Voucher Clerk should only be able to finalize a Fee Basis batch. The standard menus that accompany this package were specifically designed to account for those functions that are performed in Fiscal and MAS. You do have the ability to customize menus for users, but be aware that a conflict of interest might arise.

# Audit Trails

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the FEE NOTIFICATION/REQUEST file (#162.2), the following two fields are sent out with audit turned on if they are changed.

LEGAL ENTITLEMENT (162.2,8)

MEDICAL ENTITLEMENT (162.2,11)

# # # Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FBAA ESTABLISH VENDOR - Allows a user to add vendors to the Fee Basis Vendor file (#161.2).

FBAASUPERVISOR - Provides access to all of the Fee Supervisor options.

XUSPF200 - Used when adding a person to the new person file (#200). Its holders are not required to enter a Social Security Number (SSN) upon input of the person.

# Legal Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Fee Basis software package makes use of Current Procedural Terminology (CPT) codes which is an AMA copyrighted product. Its use is governed by the terms of the agreement between the Department of Veterans Affairs and the American Medical Association.

# VA FileMan Access Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below is a list of recommended VA FileMan Access Codes associated with each file contained in the Fee Basis package.

FILE FILE DD RD WR DEL LAYGO

<u>NUMBER</u> <u>NAME</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u>

161 FEE BASIS PATIENT @ \# \# \# \#

161.2 FEE BASIS VENDOR @ \# \# \# \#

161.21 FEE BASIS CNH CONTRACT @ \# \# \# \#

161.22 FEE BASIS CNH RATE @ \# \# \# \#

161.23 FEE BASIS CNH

AUTHORIZATION RATE @ \# \# \# \#

161.25 FEE BASIS VENDOR

CORRECTION @ \# \# \# \#

161.26 FEE BASIS PATIENT MRA @ \# \# \# \#

161.27 FEE BASIS SUSPENSION @ \# @ @ @

161.3 FEE BASIS LETTER @ \# \# \# \#

161.4 FEE BASIS SITE PARAMETERS @ \# \# \# \#

161.5 FEE CH REPORT OF CONTACT @ \# \# \# \#

161.6 FEE BASIS SPECIALTY CODE @ \# @ @ @

161.7 FEE BASIS BATCH @ \# \# \# \#

161.8 FEE BASIS PROGRAM @ \# @ @ @

161.81 FEE BASIS PARTICIPATION

CODE @ \# @ @ @

161.82 FEE BASIS PURPOSE OF VISIT @ \# @ @ @

161.83 FEE BASIS ID CARD AUDIT @ \# \# @ \#

162 FEE BASIS PAYMENT @ \# \# \# \#

162.1 FEE BASIS PHARMACY INVOICE @ \# \# \# \#

162.2 FEE NOTIFICATION/REQUEST @ \# \# \# \#

162.3 FEE CNH ACTIVITY @ \# \# \# \#

162.4 VA FORM 10-7078 @ \# \# \# \#

162.5 FEE BASIS INVOICE @ \# \#\` \# \#

162.6 FEE BASIS DISPOSITION CODE @ \# @ @ @

162.7 FEE BASIS UNAUTHORIZED

CLAIMS @ \# \# \# \#

162.8 FEE BASIS UNAUTHORIZED

CLAIMS PENDING INFO @ \# \# \# \#

162.91 FEE BASIS UNAUTHORIZED

CLAIMS DISPOSITIONS @ \# @ @ @

162.92 FEE BASIS UNAUTHORIZED

CLAIMS STATUS @ \# @ @ @

162.93 FEE BASIS UNAUTHORIZED

REQUESTED INFORMATION @ \# \# \# \#

162.94 FEE BASIS UNAUTHORIZED

DISAPPROVAL REASONS @ \# @ @ @

162.95 FEE BASIS CHECK

CANCELLATION REASON @ \# @ @ @

163.85 FEE BASIS VA TYPE OF

SERVICE @ \# @ @ @

163.99 FEE BASIS FEE SCHEDULE @ \# \# \# \#