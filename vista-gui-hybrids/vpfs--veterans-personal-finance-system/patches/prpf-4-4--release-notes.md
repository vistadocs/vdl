---
title: PRPF*4*4 VPFS Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 
app_code: VPFS
app_name: Veterans Personal Finance System
section: GUI
app_status: active
pkg_ns: PRPF
patch_ver: 4
patch_id: PRPF*4*4
group_key: "VPFS:PRPF:4"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - vpfs
  - access
  - parent
  - multiple
  - stations
  - station
  - functionality
  - prpf
page_count: 0
word_count: 410
section_count: 2
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2020
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VPFS/prpf_4_4_release_notes.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VPFS/prpf_4_4_release_notes.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=170"
---

---
title: <span id="_Toc205632711" class="anchor"></span>
---

Veterans Personal Finance System (VPFS)PRPF\*4\*4Release Notes

![](prpf-4-4-vpfs-release-notes/001.png)

Office of Information and Technology (OI&T)

Product Development

Version: 1.0July 2020

Revision History

| Date      | Version | Description                        | Author                       |
|-----------|---------|------------------------------------|------------------------------|
| July 2020 | 1.0     | Document Creation. Technical Edit. | VPFS Tier 3 Sustainment Team |

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Current functionality for users with access to multiple parent stations](#current-functionality-for-users-with-access-to-multiple-parent-stations)
- [New functionality for users with access to multiple parent stations](#new-functionality-for-users-with-access-to-multiple-parent-stations)
- [How to access VPFS](#how-to-access-vpfs)
  - [Additional Documentation](#additional-documentation)
Veterans Personal Finance System (VPFS) patch PRPF\*4\*4, will implement two-factor authentication (2FA).
Also upgraded are the following: the application server from WebLogic 8 to WebLogic 10.3.6, the operating system (OS) to enterprise Linux 6/7+, Technical Reference Model (TRM)-driven application and database upgrades (Log4j 2.10, Oracle 11g), Fortify-identified security and code quality fixes to the VPFS codebase.
This is an informational only patch and is bundled with the Kernel Authentication & Authorization for Java 2 Enterprise Edition (KAAJEE) patches XU\*8.0\*694 and XU\*8.0\*696, and the VistALink patch XOBV\*1.6\*5.
> **NOTE:** This implementation of 2FA authentication upgrades VPFS from Access and Verify codes to use the new Single Sign-On Internal (SSOI) Personal Identification Verification (PIV) login. All current VPFS users \*MUST\* be appropriately provisioned with the SSOI system for each of their corresponding VPFS VistA stations.

# Current functionality for users with access to multiple parent stations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VPFS patch introduces a change for users who have access to multiple parent stations. Prior to patch PRPF\*4\*4, when the user clicks the Logout option inside VPFS, it takes them to the Login landing page with a dropdown to select the station.

# New functionality for users with access to multiple parent stations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduced with PRPF\*4\*4, if a user is currently logged into one station, and they want to login into a different parent station or child station of a different parent station, the user will need to logout of VPFS and close all instances of the web browser, then reopen a new web browser, and login again. They need to both logout of the application and close the web browser. If the user does not close the web browser then they will be taken to the same station they accessed prior to logout, without being able to choose a different parent station.

# How to access VPFS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Production URL:  <span class="mark">REDACTED</span>

## Additional Documentation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Additional documentation can be found on the VA Software Document Library at: <https://www.va.gov/vdl/application.asp?appid=170>