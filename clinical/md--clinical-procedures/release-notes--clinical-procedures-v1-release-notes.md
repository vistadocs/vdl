---
title: Clinical Procedures Version 1 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
app_code: MD
app_name: Clinical Procedures
section: CLI
app_status: active
pkg_ns: MD
patch_ver: 1
patch_id: MD*1
group_key: "MD:MD:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - issue
  - imaging
  - considerations
  - vista
  - reports
  - resolution
  - table
  - contents
  - introduction
  - implementation
page_count: 0
word_count: 529
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2004
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/ClinProc/clinproc1_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/ClinProc/clinproc1_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=139"
---

![](clinical-procedures-version-1-release-notes/001.png)

Clinical Procedures  
  
Release Notes

April 2004

V*ist*A Health Systems Design and Development

Table of Contents

[Introduction [1](#introduction)](#introduction)

[Implementation Considerations [1](#implementation-considerations)](#implementation-considerations)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Implementation Considerations](#implementation-considerations)
Clinical Procedures (CP) passes final patient results, using Health Level 7 (HL7) messaging, between vendor clinical information systems (CIS) and VistA.   Patients' test results or reports are displayed through the Computerized Patient Record System (CPRS).  The report data is stored on long-term and short-term Imaging storage. It’s important for all providers to understand how CP works with other VistA applications, such as VistA Imaging (VI). For example, providers must use the VI Display Client to displays reports and results.
These release notes describe considerations to keep in mind about how CP works with other VistA applications.

## Implementation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Here is a list of considerations to remember when you are working with CP.

- Issue: CP stores all instrument reports in the VistA Imaging Juke Box. All clinicians must have access to the VI software and training on how to use it. IRM will also have to provide access to the VI software on any workstation that can be used to access reports.
- Issue: Some instruments require a clinician to sign-off on a report before sending it to CP. TIU will then require another signature to make the report official. This process may impose a high workload for high volume tests, such as EKGs.  
  Resolution: CP is considering a future enhancement.
- Issue: CP imaging files are not being deleted properly from the device or temporary folder.  
  Resolution: This is a known issue and is being addressed in a future Imaging patch.
- Issue: Some sites are finding it cumbersome to use CP because images can only be viewed one at a time.  
  Resolution: Imaging is working on a new viewer that will be available in a future patch.
- Issue: Sites cannot use Remote Data Views to see CP reports. The reason for this issue is that VistA Imaging and CPRS do not support Remote Data Views.  
  Resolution: Imaging is developing an Imaging Remote Data View that will display CP results.
- Issue: For some departments, printing reports is time-consuming. Images linked to CP reports must be printed one at a time.  
  Resolution: An Imaging patch is planned that will allow multiple images to be printed at the same time.
- Issue: You must have the MD Manager key to delete studies. (The MD Manager key is also used to set up CP parameters.)  
  Resolution: A new security key, the MD Delete key, will be available in a future CP patch.
- Issue: The TIU note created by CP does not include an author or interpreter’s name. Therefore the user must designate an author, call a separate screen to designate the co-signer, enter the encounter information, and then author the note. At this time CP cannot provide the provider’s name because of issues in getting an accurate match from an instrument.  
  Resolution: This issue will be addressed in a future CP enhancement.