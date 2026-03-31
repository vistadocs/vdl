---
title: Beneficiary Travel  Version 1 Dashboard Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: Dashboard
app_code: DGBT
app_name: Beneficiary Travel
section: CLI
app_status: active
pkg_ns: DGBT
patch_ver: 1
patch_id: DGBT*1
group_key: "DGBT:DGBT:1"
file_numbers: []
security_keys: []
menu_options: 0
description: - [Release Notes for Beneficiary Travel (BT) Dashboard Version 1.0](#release-notes-for-beneficiary-travel-bt-dashboard-version-10) - [Beneficiary Travel Patch DGBT\1\19](#beneficiary-travel-patch-dgbt119) - [Web Servers](#web-servers) - [New Service Requests (NSRs)](#new-service-requests-nsrs) - [Co
audience: 
keywords: 
  - travel
  - beneficiary
  - table
  - contents
  - dashboard
  - dgbt
  - notes
  - vista
  - address
  - version
page_count: 0
word_count: 580
section_count: 6
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Beneficiary_Travel/dgbt1_0_dash_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Beneficiary_Travel/dgbt1_0_dash_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=123"
---

---
title: |
  Beneficiary Travel (BT) Dashboard

  Version 1.0
---

C3-C1 Conversion Project

Release Notes

![](beneficiary-travel-version-1-dashboard-release-notes/001.png)

Beneficiary Travel Patch DGBT\*1\*19

July 2012

# Release Notes for Beneficiary Travel (BT) Dashboard Version 1.0


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Release Notes for Beneficiary Travel (BT) Dashboard Version 1.0](#release-notes-for-beneficiary-travel-bt-dashboard-version-10)
  - [Beneficiary Travel Patch DGBT\1\19](#beneficiary-travel-patch-dgbt119)
  - [Web Servers](#web-servers)
  - [New Service Requests (NSRs)](#new-service-requests-nsrs)
- [Components](#components)
  - [Files and Associated Fields](#files-and-associated-fields)
  - [New Option](#new-option)
The Beneficiary Travel Dashboard (BTD) web application assists Veterans Health Administration (VHA) Travel Office users who create travel claims, make faster, more accurate decisions on mileage reimbursement.
BT Dashboard features:
- Displays a configurable list of the closest VHA facilities, as well as the clinical specialties offered at each facility, based on configuration in the new VistA BENEFICIARY TRAVEL DASHBOARD CONFIG file (#392.5)
- When configured, the clinical specialties can be viewed by selecting the facility name
- Displays patient appointments, notes, orders, consults, and past claims
- Calculates driving mileage from patient's address to a configured set of VHA institutions
- Automatically synchronizes with travel claims as they are entered through the VistA Beneficiary Travel Menu \[DGBT BENE TRAVEL\] Claim Enter/Edit \[DGBT BENE TRAVEL SCREEN\] option
- Extracts the patient’s address from VistA, and calculates the distance between the patient’s home address and each VAMC and CBOC in the area using the Bing Maps API
- Generates a report of claims for a specified date range, including patient name, claim date/time, and who entered the claim, and saves the report in a Microsoft<sup>®</sup> Excel spreadsheet
- Generates a running total of claims for the current day at the user’s facility
- Travel clerks may go directly to the Bing™ Map site when working with a destination address not configured within the Dashboard
- Portal to VA Intranet site with a comprehensive list of facilities that can be used to find treatment centers that may be closer to the veteran
- No data is entered through BT Dashboard. All data displayed in BT Dashboard is obtained from the VistA Beneficiary Travel application

## Beneficiary Travel Patch DGBT\*1\*19

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This VistA patch provides the infrastructure for the BT Dashboard web application.

## Web Servers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Facilities within a region will share a single regional web server
- Installation of the web and MUMPS components will be coordinated by the regional Service Line Manager (SLM), between the Information Resource Manager (IRM), local system managers and local Beneficiary Travel staff

## New Service Requests (NSRs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

20070411

Beneficiary Travel Package provides changes to the VistA Beneficiary Travel Package as Congress makes legislative changes to benefits rules and reimbursement amounts.

# Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Files and Associated Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

File Name (Number) Field Name (Number) New/Modified/Deleted

------------------ ------------------- --------------------

BENEFICIARY TRAVEL

DASHBOARD CONFIG FILE

(#392.5)

NAME (392.5,.01) NEW

VA INSTITUTION (392.5,1) NEW

VA INSTITUTION (392.52,.01) NEW

ACTIVE (392.52,1) NEW

ALTERNATE ADDRESS (392.52,2) NEW

SPECIALTY(392.52,3) NEW

SPECIALTY (392.523,.01) NEW

NON-VA INSTITUTION (392.5,2) NEW

NON-VA INSTITUTION (392.53,.01) NEW

ACTIVE (392.53,1) NEW

ADDRESS (392.53,2) NEW

SPECIALTY (392.53,3) NEW

SPECIALTY (392.533,.01) NEW

BENEFICIARY TRAVEL

DASHBOARD AUDIT FILE

(#392.51)

AUDIT (.01) NEW

NAME (1) NEW

ACTION (2) NEW

## New Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Option Name Type New/Modified/Deleted

----------- ---- --------------------

DGBT BENE TRAVEL CONFIG EDIT Edit NEW