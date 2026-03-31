---
title: NUR*4*45 Nursing Technical Manual and Package Security Guide Change Pages
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: Nursing  and Package Security Guide Change Pages
app_code: NUR
app_name: Nursing
section: CLI
app_status: active
pkg_ns: NUR
patch_ver: 4
patch_id: NUR*4*45
group_key: "NUR:NUR:4"
file_numbers: []
security_keys: []
menu_options: 0
description: "--- title: | <span id=\\"_Toc205632711\\" class=\\"anchor\\"></span>Nursing Technical Manual and"
audience: 
keywords: 
  - table
  - nursing
  - contents
  - security
  - guide
  - patch
  - strong
  - technical
  - manual
  - package
page_count: 0
word_count: 506
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2018
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Nursing/nurs_4_p45_tm_cp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Nursing/nurs_4_p45_tm_cp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=80"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Nursing Technical Manual and

  Package Security Guide Version 4.0

  Change Pages for Patch NUR\*4.0\*45
---

VistA Health  
Systems Design & Development

![](nur-4-45-nursing-technical-manual-and-package-security-guide-change-pages/001.png)

May 2018
# Document Purpose


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Document Purpose](#document-purpose)
- [Scope of Patch NUR\4.0\45](#scope-of-patch-nur4045)
- [Updates to Nursing Technical Manual and Package Security Guide Version 4.0](#updates-to-nursing-technical-manual-and-package-security-guide-version-40)
  - [Chapter 1: Implementation and Maintenance](#chapter-1-implementation-and-maintenance)
This document presents the new functionality provided by Patch NUR\*4.0\*45 and should be considered an update to the content contained in the existing Nursing Technical Manual and Package Security Guide Version 4.0 (1997, updated 2000) PDF file. The new material presented in this document is provided in lieu of inserting revisions directly into the text of the existing Technical Manual and Package Security Guide Version 4.0 because no editable (MS Word) document can be located.

# Scope of Patch NUR\*4.0\*45

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch NUR\*4.0\*45 modifies the Nursing Patient Care Assignment Worksheet to display only the last four digits of each patient’s Social Security Number (SSN) and to remove the admitting diagnosis from the worksheet and replace it with the text “ON FILE.” Additionally, the Nursing End-of-Shift Report is modified to display oxygen levels with the patient’s vital signs, add a line of header information to clarify the purpose of the report sections, include new assessment categories that guide clinical staff when documenting patient problems, and hide contact information for the Attending Physician.

# Updates to Nursing Technical Manual and Package Security Guide Version 4.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The enhancements provided by patch NUR\*4.0\*45 impact Chapter 1: Implementation and Maintenance, Site Configurable Files and Fields (pages 1.15 – 1.16).

## Chapter 1: Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch NUR\*4.0\*45 adds the PRINT ATT NUMS ON EOS RPT field (#10.6) to the NURS PARAMETERS file (#213.9) to act as a parameter that controls the display of the Attending Physician contact numbers on the Nursing End-of-Shift report.

Initially, the value is set to NO and Attending Physician contact numbers are not displayed on the report. Users at each site can display the Attending Physician contact numbers by setting the value to YES.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 20%" />
<col style="width: 28%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><strong><u>Field</u></strong></th>
<th><strong><u>Name</u></strong></th>
<th><strong><u>Data Contained</u></strong></th>
<th><strong><u>Purpose</u></strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>10.6</td>
<td>PRINT ATT NUMS ON EOS RPT</td>
<td><p>Attending Physician contact numbers</p>
<p>Display flag:</p>
<p>NO (Do not display)</p>
<p>YES (Display)</p></td>
<td><p>Display or hide Attending Physician Contact Numbers on Nursing End-of-Shift Report.</p>
<p>The Default is NO (Do not display).</p></td>
</tr>
</tbody>
</table>