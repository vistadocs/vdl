---
title: GMRC*3*57 Suicide Hotline Consult Setup
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Suicide Hotline Consult Setup
app_code: GMRC
app_name: "CPRS: Consult/Request Tracking"
section: CLI
app_status: active
pkg_ns: GMRC
patch_ver: 3
patch_id: GMRC*3*57
group_key: "GMRC:GMRC:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - overview
  - example
  - local
  - suicide
  - hotline
  - consult
  - setup
page_count: 0
word_count: 43
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: True
pub_date: August 2007
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking/cons3_p57_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking/cons3_p57_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=62"
---

> ![](gmrc-3-57-suicide-hotline-consult-setup/001.png)

> RELEASE NOTES CONSULTS PATCH GMRC\*3\*57

SUICIDE HOTLINE CONSULT SETUP

> August 2007

> Department of Veterans Affairs Health Provider Systems

> Computerized Patient Record System Product Line

# Overview


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Overview](#overview)
- [Example of local set up.](#example-of-local-set-up)
> The National Suicide Hotline Interfacility Consult process starts on August 15, 2007 and is headquartered at the Canandaigua VAMC using the VISN2 VistA database. Hotline call handlers will order Interfacility Consults (IFCs) to send hotline information to the appropriate location where the caller can receive care.
> This patch installs an entry in every VistA database file \#123.5 REQUEST SERVICES, called SUICIDE HOTLINE. The entry is populated with the NAME (.01) of SUICIDE HOTLINE, SERVICE USAGE (2) of TRACKING ONLY and the IFC SENDING
> FACILITY (134,.01) of UPSTATE NEW YORK HCS. "Tracking Only" is set to prevent this consult service from being ordered directly—it must only be used as an IFC consult generated from the National Suicide Hotline. After the entry is automatically created, it is added to the ALL SERVICES entry as an item in the SUB-SERVICE (10) multiple.
> Additionally, an entry corresponding to SUICIDE HOTLINE is added to the ORDERABLE ITEMS file (101.43).
>  Note: It is extremely critical that the NAME of this service never be changed or edited. For that reason the patch modifies the data dictionary for file 123.5 and the input template used when creating or editing a consult service to prevent deletion and/or editing of this entry. Do not circumvent these precautions.
> For the IFC process to work efficiently, the service needs to always be SUICIDE HOTLINE unless changed nationally by a subsequent patch. After the entry is created via the patch installation process, the associated fields for local consult service tracking and management should be populated with local users, teams, user classes, printers, etc. as with other consult services. Also after the patch is installed, the SUICIDE HOTLINE service can be moved to another location within the site's consult hierarchy system to make local administration more efficient. For example, if sites need to move the SUICIDE HOTLINE service from ALL SERVICES to a grouper for Mental Health or Social Work Service, add SUICIDE HOTLINE as a SUB-SERVICE to the appropriate grouper and remove from the SUB-SERVICE field under ALL SERVICES.
>  CAUTION: Do not remove the SUICIDE HOTLINE from the consult hierarchy!
> Page 2 Suicide Hotline Consult Setup August 2007

# Example of local set up.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This is an example indicating (with arrows) fields that local sites may need to set up according to the needs of the site. The local site may determine that not all fields require an entry but it is important to set up notifications to appropriate staff and to identify those who are authorized to complete this consult.

> Use option GMRC MGR, Consult Management, to access, GMRC SETUP REQUEST SERVICES, Set up Consult Services menu option. Select SUICIDE HOTLINE as the service to edit.

>  Note: Never change or edit the name of this service!

> The entries in the following screen print must be filled in at each site:

> August 2007 Suicide Hotline Consult Setup Page 3

> Page 4 Suicide Hotline Consult Setup August 2007