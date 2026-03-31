---
title: Shift Handoff Tool Version 1 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
app_code: CRHD
app_name: Shift Handoff Tool
section: CLI
app_status: active
pkg_ns: CRHD
patch_ver: 1
patch_id: CRHD*1
group_key: "CRHD:CRHD:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - shift
  - handoff
  - tool
  - vamc
  - release
  - table
  - notes
  - contents
  - class
  - version
page_count: 0
word_count: 653
section_count: 1
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2008
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Shift_Handoff_Tool/crhdrn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Shift_Handoff_Tool/crhdrn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=175"
---

---
title: |
  <span id="_Toc495855387" class="anchor"></span>Shift Handoff Tool

  Release Notes
---

![](shift-handoff-tool-version-1-release-notes/001.png)

Release Date: June 2008

Clinician Desktop Service

Veterans Health Information Technology

Version 1

Revision History

| Date      | Description of Change | Author Information                 |
|-----------|-----------------------|------------------------------------|
| June 2008 | Initial Release       | <span class="mark">REDACTED</span> |
|           |                       |                                    |
|           |                       |                                    |

# Overview


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Overview](#overview)
- [Installation Requirements](#installation-requirements)
- [Shift Handoff Tool at a Glance](#shift-handoff-tool-at-a-glance)
The Shift Handoff Tool is part of the Class III to Class I initiative. It was originally developed under the project name CAIRO by the Indianapolis VAMC Development Group with input and testing from: Washington DC VAMC, Dallas VAMC, Loma Linda VAMC, Central Iowa (Des Moines), Iowa City VAMC, White River Junction VAMC, Denver VAMC, Ann Arbor VAMC, San Antonio VAMC, and the Altoona VAMC .
There has been a great deal of variability in Physician to Physician communication recorded in the medical literature. The design and development of the Shift Handoff Tool seeks to address this variability.
Standard data elements such as Allergies, Medications, Problems, History and Physical, Admitting Diagnosis, Labs, and Consults are routinely communicated Physician to Physician at shift handoff. By providing a tool to do this, we hoped that errors in care are prevented because the information is communicated in a clear, readable, standardized format.
The information can be printed out and carried with the Physician during rounds. Notes can be written on the paper copy and re-entered into the Shift Handoff Tool for the providers on the next shift.

# Installation Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is an M component (server) and a GUI component (client) to this application.

Sites have the option to implement this software. However, the M component (CRHD_1.KID) is mandated to be installed within sixty days of its release per VHA Directive 2001-023. Complete install instructions for the M component are included in the Shift Handoff Tool Install Guide (CRHDIG.PDF).

There are no required patches before installing this application.

GUI installation and implementation is detailed in the Shift Handoff Tool Implementation Guide and Technical Manual (CRHDIGTM.PDF).

Complete user instructions are found in the Shift Handoff Tool User Manual (CRHDUM.PDF).

All manuals and guides mentioned in this section are available as part of the SHIFTHANDOFF.ZIP file on the download.vista.med.va.gov FTP site and on the VHA Software Document Library (VDL) at http://www.va.gov/vdl/ after of the release date.

# Shift Handoff Tool at a Glance 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](shift-handoff-tool-version-1-release-notes/002.png)</p>
<p>1. Start the Shift Handoff Tool from the CPRS Tools drop-down menu. Auto Sign-on will occur if your site uses CLAGENT (Broker Single Sign-on) otherwise you will need to enter your CPRS Access and Verify codes to log into the application.</p></th>
<th><p>![](shift-handoff-tool-version-1-release-notes/003.png)</p>
<p>2. Select List to print: Double click list or hit Submit button.</p>
<p>Right click patient name in ‘Patient Box’ to delete patient from list.</p>
<p>Personal List only – Right click on selected Personal list to delete a Personal List.</p>
<p>HOT List – if you hold the manager key you are allowed to delete a HOT list.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>![](shift-handoff-tool-version-1-release-notes/004.png)</p>
<p>3. Enter/Edit data.</p>
<p>Yellow boxes: Editable fields. (data in these fields have a expiration date)</p>
<p>White boxes: Uneditable fields, data comes from Vista.</p>
<p>SAVE DATA, by moving from one field to another initiates the save field or hit the SAVE button at top of screen.</p></td>
<td><p>![](shift-handoff-tool-version-1-release-notes/005.png)</p>
<p>4. Print or Preview Report.</p></td>
</tr>
</tbody>
</table>