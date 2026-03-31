---
title: VES Version 5.3 Release Notes  07001 (Emergency Release)
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 07001 (Emergency Release)
app_code: VES
app_name: VA Enrollment System
section: GUI
app_status: archive
pkg_ns: VES
patch_ver: 5.3
patch_id: VES*5.3*7001
group_key: "VES:VES:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - table
  - release
  - contents
  - health
  - fixes
  - veterans
  - enrollment
  - defects
  - benefits
  - care
page_count: 0
word_count: 895
section_count: 3
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2018
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VA_Enrollment_System_Archive/es_5_3_0_07001_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VA_Enrollment_System_Archive/es_5_3_0_07001_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=293"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Enrollment System (ES)

  Emergency Release for ES 5.3.0.07001

  Release Notes
---

![](ves-version-5-3-release-notes-07001-emergency-release/001.png)

August 2018

Office of Information and Technology (OIT)

Table of Contents

Table of Figure

[Table 1: Defects and Fixes in ES 5.3.0.07001 [2](#_Toc522886001)](#_Toc522886001)

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
The mission of the Department of Veterans Affairs (VA) Office of Information and Technology (OIT), Enterprise Program Management Office (EPMO) is to provide benefits to Veterans and their families. To meet this overarching goal, OIT is charged with providing high quality, effective, and efficient IT services and Operations and Maintenance (O&M) to persons and organizations that provide point-of-care services to our Veterans.
The VA’s goals for its Veterans and families include:
- Make it easier for Veterans and their families to receive the right benefits, and meeting their expectations for quality, timeliness, and responsiveness.
- Improve the quality and accessibility of health care, benefits, and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing State-of-the-art disease management.
- Ensure awareness and understanding of the personalized, proactive, and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice, and ongoing support needed to make informed health decisions and successfully implement the Veteran’s personal health plans.
- Receive timely, high quality, personalized, safe, effective, and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates, and other service organizations.
To assist in meeting these goals, the Enterprise Health Benefits Determination (EHBD) program provides enterprise-wide enhancements and sustainment for the following systems/applications:
- The Enrollment System (ES) assists Veterans to enroll for VA healthcare benefits and is the core application that feeds other VA systems with Enrollment and Eligibility (E&E) data.
- Income Verification Match (IVM) assists in determining priority grouping for healthcare eligibility.
- Veterans Information Systems and Technology Architecture (VistA) Registration, Eligibility & Enrollment (REE) shares information with other VistA applications and enables registration and eligibility determinations and enrollment at VA Medical Centers (VAMC).
- Veteran’s On-Line Application (VOA) is re-purposed for the online Veterans Health Benefits Handbook (VHB). VHB provides each enrolled Veteran on-demand online access to a personalized and dynamic health benefits-related Handbook.
Enrollment System Modernization (ESM) defines Health Benefit Plans (HBP) for which a client (Veteran, service member, or beneficiary) is eligible and ties them to the authority for care. Key enhancements to be completed include Pending Eligibility Determination, fixes to the Enrollment System, Date of Death, Internal Controls, Workflow, Veterans Financial Assessment, converting of Military Service Data Sharing (MSDS) to Enterprise Military Information Service (eMIS), Manage Relationships, Veteran Contact Service, and support for Enrollment System Community Care (ESCC).

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Release Notes document is to announce the release of the emergency release build ES 5.3.0.07001. This release, developed in Java technology, contains ESM P2 development and upgrade efforts, including enhancements to support Community Care (CC) and ES Sustainment.

# Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of ES and applies to the changes made between this release and any previous release for this software.

# This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ES 5.3.0 will be updated with build 5.3.0.07001 and hosted at the Austin Information Technology Center (AITC).

The following sections provide a summary of the defects and fixes to the existing software.

## Defects and Fixes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1 lists the defects and fixes and corresponding Rational Team Concert (RTC) Change and Configuration Management (CM) numbers included in ES 5.3.0.07001

<table>
<caption><p><span id="_Toc522886001" class="anchor"></span>Table : Defects and Fixes in ES 5.3.0.07001</p></caption>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th>RTC<br />
CM #</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>810016</td>
<td><p><strong>Defect:</strong> Production defect: A ORUZ10 transmission failure occurs due to the Social Security Number (SSN) data stripped from the ZDP segment. Sites are recording &lt;SUBSCRIPT&gt;IX+1^DIE1 errors when attempting to process HL7 ORUZ10 financial updates sent from ES.</p>
<p><strong>Fix:</strong> Code changes to remove the following method and method calls that was removing the SSN from the ZDP segment and setting it to an empty string:</p>
<p>cleanupSensitiveData(message.getSegments()).</p></td>
</tr>
</tbody>
</table>

<span id="_Toc522886001" class="anchor"></span>Table : Defects and Fixes in ES 5.3.0.07001

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No known or open issues were identified in this release.

# Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents apply to this release:

- ES 5.3.0.07001 Release Notes are uploaded to the [VA Software Document Library](http://www.va.gov/vdl/) (VDL).
- Additional reference documentation related to this release is stored in RTC.