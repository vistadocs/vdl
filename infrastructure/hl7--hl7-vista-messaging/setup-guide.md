---
title: HL7 V. 1.6 Package Security Guide
doc_type: SG
doc_label: Security Guide
doc_layer: anchor
doc_subject: Package
app_code: HL7
app_name: HL7 (VistA Messaging)
section: INF
app_status: active
pkg_ns: 
patch_ver: 1.6
patch_id: 
group_key: "HL7::1.6"
file_numbers: []
security_keys: []
menu_options: 0
description: - [Security Keys](#security-keys) - [Legal Requirements](#legal-requirements) - [VA FileMan Access Codes](#va-fileman-access-codes) No security keys are provided with the HL7 V. 1.6 software package.
audience: 
keywords: 
  - access
  - table
  - contents
  - security
  - message
  - package
  - keys
  - legal
  - requirements
  - fileman
page_count: 0
word_count: 243
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 1995
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Health_Level_7_(HL7)/hl71_6sg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Health_Level_7_(HL7)/hl71_6sg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=8"
---

Decentralized Hospital Computer Program

DHCPhealth level seven(HL7)package security guide

October 1995

sensitive information

IRM Field Office

Albany, New York

National Package Security

# Security Keys


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Security Keys](#security-keys)
- [Legal Requirements](#legal-requirements)
- [VA FileMan Access Codes](#va-fileman-access-codes)
No security keys are provided with the HL7 V. 1.6 software package.

# Legal Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no unique legal requirements for this version of HL7.

# VA FileMan Access Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of recommended VA FileMan Access Codes associated with each file contained in the DHCP HL7 package.

FILE FILE DD RD WR DEL LAYGO

<u>NAME</u> <u>NUMBER</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u>

HL7 NON-DHCP

APPLICATION

PARAMETER 770 @ @ @ @ @

HL7 APPLICATION

PARAMETER 771 @ @ @ @ @

HL7 FIELD 771.1 @ @ @ @ @

HL7 MESSAGE TYPE 771.2 @ @ @ @ @

HL7 SEGMENT TYPE 771.3 @ @ @ @ @

HL7 DATA TYPE 771.4 @ @ @ @ @

HL7 VERSION 771.5 @ @ @ @ @

HL7 MESSAGE

STATUS 771.6 @ @ @ @ @

HL7 ERROR

MESSAGE 771.7 @ @ @ @ @

HL7 STANDARD 771.8 @ @ @ @ @

HL7 MESSAGE

TEXT 772 @ @ @ @ @

FILE FILE DD RD WR DEL LAYGO

<u>NAME</u> <u>NUMBER</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u> <u>ACCESS</u>

HL7 MESSAGE

ADMINISTRATION 773 @ @ @ @ @

HL7 EVENT TYPE

CODE 779.001 @ @ @ @ @

HL7 ACKNOWLEDGE-

MENT CODE 779.002 @ @ @ @ @

HL7 ACCEPT/

APPLICATION ACK

CONDITION 779.003 @ @ @ @ @

COUNTRY CODE 779.004 @ @ @ @ @

HL LOWER LEVEL

PROTOCOL TYPE 869.1 @ @ @ @ @

HL LOWER LEVEL

PROTOCOL

PARAMETER 869.2 @ @ @ @ @

HL COMMUNICATION

SERVER PARAMETERS 869.3 @ @ @ @ @

HL LOGICAL LINK 870 @ @ @ @ @