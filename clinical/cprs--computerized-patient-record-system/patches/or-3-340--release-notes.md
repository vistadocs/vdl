---
title: OR*3*340 Release Notes CPRS GUI Version
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: CPRS GUI Version
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*340
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: ![](or-3-340-release-notes-cprs-gui-version/001.png)![](or-3-340-release-notes-cprs-gui-version/002.png)
audience: 
keywords: 
  - primary
  - care
  - mhtc
  - span
  - patient
  - cprs
  - treatment
  - health
  - class
  - anchor
page_count: 0
word_count: 785
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_340rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_340rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

![](or-3-340-release-notes-cprs-gui-version/001.png)![](or-3-340-release-notes-cprs-gui-version/002.png)

<span id="_Toc311023151" class="anchor"></span>Table of Contents

<span id="_Toc311023152" class="anchor"></span>Introduction

VistA patch OR\*3.0\*340 provides resolution to a critical need to rapidly identify a patient’s Mental Health (MH) Treatment Coordinator so that veterans with conditions such as depression, suicidal ideation and Post Traumatic Stress Disorder (PSTD) can be treated more quickly and effectively. This project affects nurses, physicians, ward clerks, Primary Care Management Module (PCMM) coordinators and all other mental health professionals. The patch addresses additional needs outlined in the functionality section. Changes will interface over to PCMM, where clinicians will have access to this new functionality. This will make it easier for clinicians to coordinate care between mental health and primary care providers.

This patch is scheduled to be released with SD\*5.3\*575. The purpose of SD\*5.3\*575 is to implement the functionality for displaying the Mental Health Treatment Coordinator (MHTC) in two locations within CPRS, one being the Patient Inquiry display and the other being the Primary Care button detail display.

<span id="_Toc311023153" class="anchor"></span>New Functionality

This patch provides enhancements to CPRS. The sections below outline the changes and fixes that will be applied to the Patient Inquiry Display and the Primary Care Detailed Display.

<span id="_Toc311023154" class="anchor"></span>Changes and Fixes to the Patient Inquiry Display

The Mental Health Treatment Coordinator (MHTC) will be displayed within CPRS GUI as part of the Patient Inquiry display. The MHTC and the MHTC’s position will be shown just after the Primary Practitioner and Primary Care Team as part of the Primary Care Information section of the Patient Inquiry display. The MHTC information will include the MH Treatment Team, MHTC provider’s name and the PCMM position which they were assigned. If a MHTC was not assigned to the patient, no information will be displayed concerning the MHTC. Below is how the Primary Care Information section currently displays:

> Primary Care Information:

> Primary Practitioner:

> Primary Care Team:

- Any user who has permission to view the CPRS GUI will be able to see a patient’s MH treatment coordinator information, if it exists, in the Patient Inquiry display.
- If the patient has a Primary Care Provider, information about his/her MH treatment coordinator will be printed between the first Primary Care section and the Status section and it will be printed between the Second Primary Care section and the Health Insurance section.
- If a MHTC is assigned to the patient, the MH Treatment Team name, the MHTC’s name and position followed by analog pager, phone number, and digital pager will be displayed as below:

  MH Treatment Team:

  MH Treatment Coord: Position:

  Analog Pager: Phone:

  Digital Pager:
- If a MHTC is not assigned to the patient, then the MHTC information will not be displayed within the Patient Inquiry Display.

<span id="_Toc311023155" class="anchor"></span>Changes and Fixes to the Primary Care Display

The MHTC will be displayed within CPRS GUI as part of the Primary Care detailed display. This is accessed by depressing the Primary Care button in the header of CPRS GUI which launches the detailed display. This display will include the MHTC information.

- A user who has permission to view the CPRS GUI will be able to see a patient’s MH treatment coordinator information, if it exists, in the Primary Care display.
- The Mental Health Treatment Team name, the MHTC’s name, analog pager number, digital pager number, and the office phone number will be included on the Primary Care Detailed Display. Below displays the format:

  MH Treatment Team:

  MH Treatment Coordinator:

  Analog Pager:

  Digital Pager:

  Office Phone:
- In the event no MHTC has been assigned to the patient, no MHTC information will be displayed on the Primary Care screen.

<span id="_Toc311023156" class="anchor"></span>Pre-Conditions to Installation

OR\*3.0\*340 is to be released with SD\*5.3\*575, with SD\*5.3\*575 being installed first.

Specific information pertaining to the installation of this patch can be found in the patch description and section referred to as ‘INSTALLATION INSTRUCTIONS’ in patch OR\*3.0\*340 Installation Guide.

<span id="_Toc311023157" class="anchor"></span>Remedy Tickets

- No Remedy tickets are associated with this release.

<span id="_Toc311023158" class="anchor"></span>References

Information in this document is derived from the following documentation on the project’s Technical Services Project Repository (TSPR) site at [<u>http://tspr.vista.med.va.gov/warboard/anotebk.asp?proj=1378&Type=Active</u>](http://tspr.vista.med.va.gov/warboard/anotebk.asp?proj=1378&Type=Active):

- Identification of Principal Mental Health Provider (IPMHP) Requirements Specification Document (RSD), file name: IPMHP Deliverable 1 and 3 RSD v 1.11
- Identification of Principal Mental Health Provider (IPMHP) Computerized Patient Record System (CPRS) Software Design Document (SDD), file name: IPMHP CPRS SDD 340.doc

Additional information can be found in the CPRS GUI User Manual. All documentation can be found on VDL in the CPRS library: [<u>http://www.va.gov/vdl/application.asp?appid=61</u>](http://www.va.gov/vdl/application.asp?appid=61)