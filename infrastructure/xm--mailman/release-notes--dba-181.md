---
title: XM*DBA*181 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: XM*DBA*181
app_code: XM
app_name: MailMan
section: INF
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - release
  - domain
  - features
  - mailman
  - notes
  - package
  - introduction
  - purpose
page_count: 0
word_count: 212
section_count: 1
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2017
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Mailman/xm_dba_p181_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Mailman/xm_dba_p181_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=15"
---

---
title: XM\*DBA\*181 Release Notes
---

XMDB - New Package & Domain Release Process

MailMan (XM)

![](xm-dba-181-release-notes/001.png)

June 2017

Office of Information and Technology (OI&T)

Revision History

| Creation Date | Version No. | Description/Comments           | Author(s) | Issue Date |
|---------------|-------------|--------------------------------|-----------|------------|
| 6/16/17       | 1           | Release notes for XM\*DBA\*181 | REDACTED  | 6/16/17    |

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Purpose](#purpose)
- [This Release](#this-release)
- [Features and Functionality](#features-and-functionality)
The Business Owner requested that Domain file updates are automated via a post-install routine.

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This release notes cover the new features provided by patch, XM\*DBA\*181.

# This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide, in brief, the new features and functions added by patch, XM\*DBA\*181. This informational patch, XM\*DBA\*181, informs sites that a new package, 'MailMan Domain Updates' (XMDB), has been created for future MailMan domain releases.

# Features and Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new package was created to allow for automatic installation of MailMan domains by allowing Health Product Support developers to utilize a post-install routine to add the new domains to the Domain (#4.2) file. This will replace the XM\*DBA\*# convention previously used to manually add new domains to the file via FileMan Enter/Edit.