---
title: "Kernel 8.0 Developerâ€™s Guide: Field Monitoring User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: Field Monitoring"
app_code: XU
app_name: Kernel
section: INF
app_status: active
pkg_ns: XU
patch_ver: 8.0
patch_id: XU*8.0
group_key: "XU:XU:8.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - guide
  - cross
  - kernel
  - style
  - developer
  - span
  - xuhuix
  - table
  - xuhui
  - reference
page_count: 0
word_count: 1192
section_count: 2
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_field_monitoring_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_field_monitoring_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259319" class="anchor"></span>Field Monitoring Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-field-monitoring-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-field-monitoring-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 43%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/28/2025</td>
<td>1.0</td>
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Field Monitoring Developer Tools User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
</tbody>
</table>

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc234301876" class="anchor"></span>List of Figures

<span id="_Ref38421374" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-field-monitoring-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [OPKG^XUHUI(): Monitor New Style Cross-referenced Fields](#opkgxuhui-monitor-new-style-cross-referenced-fields)
    - [Example](#example)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Field Monitoring Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Field Monitoring [OPKG^XUHUI](#opkgxuhui-monitor-new-style-cross-referenced-fields) API is available for developers and is described below.

## OPKG^XUHUI(): Monitor New Style Cross-referenced Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Field Monitoring

ICR \#: 3589

Description: The OPKG^XUHUI API allows other packages to task an option or protocol from a New Style cross-reference. This API can be used to monitor any field or fields in any file using a New Style cross-reference.

Format: OPKG^XUHUI(\[xuhuiop,\]xuhuinm\[,xuhuia\],xuhuixr)

Input Parameters: xuhuiop: (optional) This parameter is a set of NUMERIC codes that tells the Unwinder to use the PROTOCOL (#101) file or the OPTION (#19) file. If this parameter is NULL, the default value is used (that is 101):

- 101 (default)—PROTOCOL (#101) file is used.
- 19—The OPTION (#19) file is used.

xuhuinm: (required) This parameter is the NAME (#.01) value of the protocol or option that is to be launched.

xuhuia: (optional) This parameter is a SET OF CODES. If this input parameter is NULL, the default value is used (that is S):

- S (default)—The data being passed is from the SETting of the cross-reference.
- K—The data being passed is from the KILLing of the cross-reference.

xuhuixr: (required) This parameter is the name of the cross-reference.

Output: See <u>Example</u>: Monitored fields with a New Style cross-reference.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Hui Project needs to monitor the following fields at the top level of the NEW PERSON (#200) file for changes in value, in the order listed:

- NAME (#.01)
- TERMINATION DATE (#9.2)
- DOB (#5)
- SSN (#9)

#### Create New Style Cross-References

Create a MUMPS New Style cross-reference for the fields that are to be monitored for value changes, as shown in <u>Figure 1</u>:

<span id="_Ref499704310" class="anchor"></span>Figure 1: OPKG^XUHUI API—Example of Creating New Style Cross-References

Index Name: AXUHUI (#n)

Short Description: Hui Project Top File Cross-reference

Description: This MUMPS New Style cross-reference is on non-multiple

fields in the NEW PERSON (#200) file that the Hui Project

needs to monitor for changes in value.  The following fields

are being monitored in the order listed:

.01 (NAME)

9.2 (TERMINATION DATE)

5 (DOB)

9 (SSN)

For details on how this cross-reference processes changes,

please refer to the patch description for Kernel Patch XU\*8\*236.

For more detailed information about the MUMPS New Style

cross-reference, please refer to the "VA FileMan V. 22.0 Key 

and Index Tutorial" (see Lessons \#5 and \#6)

Type: MUMPS

EXECUTION: RECORD

Use: ACTION

Set Logic:  D OPKG^XUHUI("","XUHUI FIELD CHANGE EVENT","","AXUHUI") Q

Kill Logic:  Q

Whole Kill:  Q

X(1):  NAME  (200,.01)  (forwards)

X(2):  TERMINATION DATE  (200,9.2)  (forwards)

X(3):  DOB  (200,5)  (forwards)

X(4):  SSN  (200,9)  (forwards)

#### Sample Scenario

Change a monitored (cross-referenced) field value in the NEW PERSON (#200) file, as shown in <u>Figure 2</u>:

<span id="_Ref499704347" class="anchor"></span>Figure 2: OPKG^XUHUI API—Sample Scenario

> INPUT TO WHAT FILE: NEW PERSON// <span class="mark">\<Enter\></span>

> EDIT WHICH FIELD: ALL// <span class="mark">DOB</span>

> THEN EDIT FIELD: <span class="mark">SSN</span>

> THEN EDIT FIELD: <span class="mark">\<Enter\></span>

> Select NEW PERSON NAME: <span class="mark">XUUSER \<Enter\></span> XUUSER,ONE OX

> DOB: JUL 4,1950// <span class="mark">12.24.49 \<Enter\></span> (DEC 24, 1949)

> SSN: 000220000// <span class="mark">000558888</span>

In this example, the ONE XUUSER’s Date of Birth (DOB) was changed from 07/04/50 to 12/24/49 and changed the Social Security Number (SSN) from 000-22-0000 to 000-55-8888. Since these fields are being monitored (that is MUMPS New Style cross-reference, see the “Create Cross-references” previous section), you should see this data passed to the XUHUI FIELD CHANGE EVENT protocol (see the “<u>Internal Results for Developers</u>” section).

#### Internal Results for Developers

The following data is passed to the XUHUI FIELD CHANGE EVENT Protocol through the Kernel OPKG^XUHUI API that is called in the AXUHUI cross-reference (see the “<u>Create New Style Cross-References</u>” section).

<span id="_Toc200269971" class="anchor"></span>Figure 3: OPKG^XUHUI API—Example of Internal Results

-------------------------------------------------------------------------

If executing the Kill logic, then the 'X' array will be equal to the 'X1'

array. If executing the Set logic, then the 'X' array will be equal to

the 'X2' array.

-------------------------------------------------------------------------

X=XUUSER,ONE

X(1)=XUUSER,ONE

X(2)=

X(3)=2491224

X(4)=000558888

-------------------------------------------------------------------------

X1=XUUSER,ONE

X1(1)=XUUSER,ONE

X1(2)=

X1(3)=2500704

X1(4)=000220000

-------------------------------------------------------------------------

X2=XUUSER,ONE

X2(1)=XUUSER,ONE

X2(2)=

X2(3)=2491224

X2(4)=000558888

-------------------------------------------------------------------------

XUHUIA=S

XUHUIDA=70

XUHUIFIL=200

XUHUIFLD=

XUHUINM=XUHUI FIELD CHANGE EVENT

XUHUIOP=101

XUHUIX=XUUSER,ONE

XUHUIX(1)=XUUSER,ONE

XUHUIX(2)=

XUHUIX(3)=2491224

XUHUIX(4)=000558888

XUHUIX1=XUUSER,ONE

XUHUIX1(1)=XUUSER,ONE

XUHUIX1(2)=

XUHUIX1(3)=2500704

XUHUIX1(4)=000220000

XUHUIX2=XUUSER,ONE

XUHUIX2(1)=XUUSER,ONE

XUHUIX2(2)=

XUHUIX2(3)=2491224

XUHUIX2(4)=000558888

XUHUIXR=AXUHUI

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-field-monitoring-user-guide/004.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-field-monitoring-user-guide/005.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-field-monitoring-user-guide/006.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.