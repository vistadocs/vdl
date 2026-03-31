---
title: HBPC Security Guide
doc_type: SG
doc_label: Security Guide
doc_layer: plain
doc_subject: 
app_code: HBPC
app_name: Home Based Primary Care
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: Version 1.0November 1993Revised August 2021Department of Veterans AffairsOffice of Information Technology
audience: 
keywords: 
  - blockquote
  - hbhc
  - class
  - strong
  - table
  - style
  - width
  - contents
  - even
  - mail
page_count: 0
word_count: 1195
section_count: 4
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Home_Based_Pri_Care_(HBPC)/hbh_sg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Home_Based_Pri_Care_(HBPC)/hbh_sg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=68"
---

---
title: |
  HOME BASED PRIMARY CARE

  SECURITY GUIDE
---

![](hbpc-security-guide/001.png)

SENSITIVE INFORMATION

Version 1.0November 1993Revised August 2021Department of Veterans AffairsOffice of Information Technology

> Revision History

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 10%" />
<col style="width: 7%" />
<col style="width: 26%" />
<col style="width: 23%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Patch</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Page</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Project Manager</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Technical</strong></p>
<p><strong>Writer</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>August 2021</p>
</blockquote></td>
<td><blockquote>
<p>32</p>
</blockquote></td>
<td><blockquote>
<p>Title, 2, 4</p>
</blockquote></td>
<td><blockquote>
<p>HBH*1.0*32</p>
</blockquote>
<ul>
<li><p>Updated HBHC to <strong><u>HBPC</u></strong> for the note in the Security Keys section</p></li>
<li><p>Updated HBHC to <strong><u>HBPC</u></strong> in the Legal Requirements section</p></li>
<li><p>Updated Title page, Revision History, and Footers</p></li>
</ul></td>
<td><blockquote>
<p>Liberty ITS</p>
</blockquote></td>
<td><blockquote>
<p>Liberty ITS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>August 2009</p>
</blockquote></td>
<td><blockquote>
<p>24</p>
</blockquote></td>
<td><blockquote>
<p><a href="#mail-groups"><u>4</u></a></p>
</blockquote></td>
<td><blockquote>
<p>Patch HBH*1*24 August 2009 – Bookmark added</p>
<p>and bookmarks described.</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
</tbody>
</table>

# File Security


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [File Security](#file-security)
- [Security Keys](#security-keys)
  - [Legal Requirements](#legal-requirements)
- [Mail Groups](#mail-groups)
  - [HBH Mail Group](#hbh-mail-group)
  - [HBHC MEDICAL FOSTER HOME Mail Group](#hbhc-medical-foster-home-mail-group)
> All HBHC files are exported with FileMan security codes set to "@" for Data Dictionary, Read, Write, Delete, LAYGO, & Audit file access. Each of the files listed below will need the FileMan security code changed from "@" to an appropriate code for the HBHC service. Each service will need to determine the proper access level for their users.
> Data Dictionary and Audit access are reserved for the IRMS staff. Delete access should NOT be allowed on any HBHC files since these files point to or are referenced by other files. Read and/or Write Access is granted by virtue of the menu options that reference each file.
> NUMBER NAME DD RD WR DEL LAYGO AUDIT
<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 32%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>631</th>
<th><blockquote>
<p>HBHC</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT</p>
</blockquote></th>
<th><blockquote>
<p>@</p>
</blockquote></th>
<th>@</th>
<th>@</th>
<th>@</th>
<th>@</th>
<th><blockquote>
<p>@</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>631.1</td>
<td><blockquote>
<p>HBHC</p>
</blockquote></td>
<td><blockquote>
<p>REJECT/WITHDRAWEL REASON</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>631.2</td>
<td><blockquote>
<p>HBHC</p>
</blockquote></td>
<td><blockquote>
<p>EXPRESSIVE COMMUNICATION</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>631.3</td>
<td><blockquote>
<p>HBHC</p>
</blockquote></td>
<td><blockquote>
<p>RECEPTIVE COMMUNICATION</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>631.4</td>
<td><blockquote>
<p>HBHC</p>
</blockquote></td>
<td><blockquote>
<p>PROVIDER</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>631.5</td>
<td><blockquote>
<p>HBHC</p>
</blockquote></td>
<td><blockquote>
<p>TYPE OF VISIT</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>631.6</td>
<td><blockquote>
<p>HBHC</p>
</blockquote></td>
<td><blockquote>
<p>CLINIC</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>631.7</td>
<td><blockquote>
<p>HBHC</p>
</blockquote></td>
<td><blockquote>
<p>PERIOD OF SERVICE</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>631.8</td>
<td><blockquote>
<p>HBHC</p>
</blockquote></td>
<td><blockquote>
<p>VALID STATE CODE</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>631.9</td>
<td><blockquote>
<p>HBHC</p>
</blockquote></td>
<td><blockquote>
<p>SYSTEM PARAMETER</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>632</td>
<td><blockquote>
<p>HBHC</p>
</blockquote></td>
<td><blockquote>
<p>VISIT</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>633</td>
<td><blockquote>
<p>HBHC</p>
</blockquote></td>
<td><blockquote>
<p>TEAM</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>633.2</td>
<td><blockquote>
<p>HBHC</p>
</blockquote></td>
<td><blockquote>
<p>MEDICAL FOSTER HOME</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>634</td>
<td><blockquote>
<p>HBHC</p>
</blockquote></td>
<td><blockquote>
<p>TRANSMIT</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>634.1</td>
<td><blockquote>
<p>HBHC</p>
</blockquote></td>
<td><blockquote>
<p>EVALUATION/ADMISSION ERRORS</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>634.2</td>
<td><blockquote>
<p>HBHC</p>
</blockquote></td>
<td><blockquote>
<p>VISIT ERRORS</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>634.3</td>
<td><blockquote>
<p>HBHC</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE ERROR(S)</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>634.4</td>
<td><blockquote>
<p>HBHC</p>
</blockquote></td>
<td><blockquote>
<p>FORM 6 CORRECTIONS</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>634.7</td>
<td><blockquote>
<p>HBHC</p>
</blockquote></td>
<td><blockquote>
<p>MEDICAL FOSTER HOME</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td>@</td>
<td>@</td>
<td>@</td>
<td>@</td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
</tbody>
</table>
> ERROR(S)

# Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> HBHC TRANSMIT

> This key locks the HBHC Transmission Menu option and should be assigned to users responsible for data transmission to Austin.

> HBHC MANAGER

> This key locks the HBHC Manager Menu option and should be assigned to the Application Coordinator.

> Note: ONLY sites that have received Medical Foster Home (MFH) sanction status approval from the Director of Home & Community-Based Care in the Office of Geriatrics and Extended Care, VA Central Office (VACO), should be utilizing the MFH portion of the Home Based Primary Care (HBPC) Information System software. The MFH functionality is dormant for sites without an approved MFH sanction status.

> HBHC MEDICAL FOSTER HOME

> This security key locks the Medical Foster Home (MFH) Menu \[HBHC MFH MENU\] option.

## Legal Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no known legal requirements associated with the HBPC package.

# Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## HBH Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Members of the HBH mail group receive data error messages after visit data is scanned. This group also receives any messages pertaining to the transmission of the data to Austin. Assign users to this mail group that will be responsible for correcting data errors or receiving transmission/confirmation messages.

## HBHC MEDICAL FOSTER HOME Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: ONLY sites who have received MFH sanction status approval from VACO should assign anyone to the HBHC MEDICAL FOSTER HOME.

> Members of the HBHC MEDICAL FOSTER HOME mail group receive mail messages on the first of each month for inspections, training sessions, or licenses due for the MFH.