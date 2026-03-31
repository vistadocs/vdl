---
title: Release Notes ES 6_2_2_06001_rn
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: ES 6_2_2_06001_rn
app_code: VES
app_name: VA Enrollment System
section: GUI
app_status: active
pkg_ns: VES
patch_ver: 6.2
patch_id: VES*6.2*6001
group_key: "VES:VES:6.2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - table
  - contents
  - health
  - release
  - care
  - enrollment
  - fixes
  - eligibility
  - veterans
  - defects
page_count: 0
word_count: 892
section_count: 3
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2022
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VA_Enrollment_System/ves_6_2_2_06001_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VA_Enrollment_System/ves_6_2_2_06001_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=183"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Eligibility and Enrollment (E&E)

  Veterans Health Administration (VHA) Enrollment System (VES) 6.2.2.06001

  Release Notes
---

![](release-notes-es-6-2-2-06001-rn/001.png)

October 2022

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Table of Contents

List of Tables

[Table 1: Defects and Fixes in VES 6.2.2.06001 [2](#_Ref99965903)](#_Ref99965903)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Purpose](#purpose)
- [Audience](#audience)
- [This Release](#this-release)
  - [Defects and Fixes](#defects-and-fixes)
  - [Known Issues](#known-issues)
- [Product Documentation](#product-documentation)
The mission of the VA OIT Development, Security, and Operations is to provide benefits to Veterans and their families. In order to meet this overarching goal, OIT is charged with providing high quality, effective and efficient IT services and Operations and Maintenance (O&M) to persons and organizations that provide point-of-care services to our Veterans.
The VA’s goals for its Veterans and families include:
- Make it easier for Veterans and their families to receive the right benefits and meeting their expectations for quality, timeliness and responsiveness.
- Improve the quality and accessibility of health care, benefits and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing state of the art disease management.
- Ensure awareness and understanding of the personalized, proactive and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice and ongoing support needed to make informed health decisions and successfully implement the Veteran’s personal health plans.
- Receive timely, high quality, personalized, safe, effective and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates and other service organizations.
To assist in meeting these goals, the Eligibility and Enrollment (E&E) program will provide enterprise wide enhancements and sustainment for the following systems/applications:
- The VHA Enrollment System (VES) is the authoritative system for VA enrollment and Community Care static eligibility determinations.
- Income Verification Match (IVM)/Enrollment Database (EDB) assists in determining priority grouping for health care eligibility.
- Veterans Information Systems and Technology Architecture (VistA) Registration, Eligibility & Enrollment (REE) shares information with other VistA applications and enables registration and preliminary eligibility determinations and enrollment at VA Medical Centers (VAMC). VES makes the final eligibility determinations.
- The Veteran’s On-Line Application (VOA), now referred to as Health Care Application (HCA), enables Veterans to self-enroll in VA health care and is another entry point for records to be added to VES.
E&E defines VHA Profiles (VHAP) for which a client (Veteran, Service Member, or beneficiary) is eligible and ties them to the authority for care. Key enhancements to be completed include Pending Eligibility Determination, fixes to the VHA Enrollment System, Date of Death, Internal Controls, Workflow, Veterans Financial Assessment, converting of Military Service Data Sharing (MSDS) to Enterprise Military Information Service (eMIS), Manage Relationships, Veteran Contact Service and support for VES Integrated Veteran Care (IVC) Systems Impact (VES/IVC SI).

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Release Notes document is to announce the release of the VES 6.2.2.06001. This release, developed in Java technology, contains E&E development and upgrade efforts. This release includes defect fixes to support Enrollment System Modernization (ESM), VES/IVC SI and VES Sustainment.

# Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of VES 6.2.2.06001 and applies to the changes made between this release and any previous release for this software.

# This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VES will be upgraded from Version 6.2.2 to Version 6.2.2.06001 and hosted by Amazon Web Services.

The following sections provide a summary of the defects and fixes to the existing software.

## Defects and Fixes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1 lists the defects and fixes and corresponding Jira issue numbers included in VES 6.2.2.06001.

<table>
<caption><p><span id="_Ref99965903" class="anchor"></span>Table 1: Defects and Fixes in VES 6.2.2.06001</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Jira Issue #</strong></th>
<th><strong>Summary</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VES-25714</td>
<td><p><strong>Defect:</strong> The Community Care eligibility (VCE) recalculation job is not setting the “vce_recalc_required_ind” flag back to “N” after it finishes updating the record and publishing the Health Level 7 (HL7) messages; this causes the job to reprocess the same records continuously and will never complete all of the required recalculations.</p>
<p><strong>Fix</strong>: Modified the VCE recalculation job to set the flag back to “N” upon completion.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref99965903" class="anchor"></span>Table 1: Defects and Fixes in VES 6.2.2.06001

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No known or open issues were identified in this release.

# Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents apply to this release:

- VES 6.2.2.06001 Release Notes are uploaded to the [VA Software Document Library](http://www.va.gov/vdl/).
- Additional reference documentation related to this release is stored in GitHub.