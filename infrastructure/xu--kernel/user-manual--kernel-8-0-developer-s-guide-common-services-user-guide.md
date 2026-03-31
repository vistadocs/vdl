---
title: "Kernel 8.0 Developerâ€™s Guide: Common Services User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: Common Services"
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
  - kernel
  - vpid
  - developer
  - services
  - common
  - table
  - person
  - contents
  - xupsqry
page_count: 0
word_count: 1240
section_count: 4
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_common_services_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_common_services_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  Common Services Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-common-services-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-common-services-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Common Services Developer Tools User Guide</em>.</p>
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

<span id="_Ref38421374" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-common-services-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [\$\$IEN^XUPS(): Get IEN Using VPID in File \#200](#ienxups-get-ien-using-vpid-in-file-200)
  - [\$\$VPID^XUPS(): Get VPID Using IEN in File \#200](#vpidxups-get-vpid-using-ien-in-file-200)
  - [EN1^XUPSQRY(): Query New Person File](#en1xupsqry-query-new-person-file)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Common Services Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Common Services APIs and Extrinsic Functions are available for developers. These APIs and Extrinsic Functions are described below.

## \$\$IEN^XUPS(): Get IEN Using VPID in File \#200

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Common Services

ICR \#: 4574

Description: The \$\$IEN^XUPS extrinsic function accepts the VA Person ID (VPID) of an entry in the NEW PERSON (#200) file and returns the Internal Entry Number (IEN)/DUZ.

![](kernel-8-0-developer-s-guide-common-services-user-guide/004.png) CAUTION: VPID has *not* been fully implemented in the VA. VPID was the user identifier within the *canceled* Enterprise Single Sign-On (ESSO) project. The current Identity and Access Management (IAM) 2-Factor Authentication (2FA) project uses Security ID (SecID) as the unique identifier. VPID APIs and fields will be deprecated in a *future* Kernel patch. Developers are encouraged to remove all references to these APIs in their code.

![](kernel-8-0-developer-s-guide-common-services-user-guide/005.png) NOTE: This API was released with Kernel Patch XU\*8.0\*309.

Format: \$\$IEN^XUPS(vpid)

Input Parameters: vpid: (required) The VA Person ID (VPID).

Output: returns: Returns the Internal Entry Number (IEN)/DUZ of the NEW PERSON (#200) file.

## \$\$VPID^XUPS(): Get VPID Using IEN in File \#200

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Common Services

ICR \#: 4574

Description: The \$\$VPID^XUPS extrinsic function accepts the internal entry number (IEN)/DUZ of an entry in the NEW PERSON (#200) file and returns the VA Person ID (VPID) for the selected user.

![](kernel-8-0-developer-s-guide-common-services-user-guide/006.png) NOTE: This API was released with Kernel Patch XU\*8.0\*309.

![](kernel-8-0-developer-s-guide-common-services-user-guide/007.png) CAUTION: VPID has *not* been fully implemented in the VA. VPID was the user identifier within the *canceled* Enterprise Single Sign-On (ESSO) project. The current Identity and Access Management (IAM) 2-Factor Authentication (2FA) project uses Security ID (SecID) as the unique identifier. VPID APIs and fields will be deprecated in a *future* Kernel patch. Developers are encouraged to remove all references to these APIs in their code.

Format: \$\$VPID^XUPS(duz)

Input Parameters: duz: (required) The Internal Entry Number (IEN) in the NEW PERSON (#200) file.

Output: returns: Returns the VA Person ID (VPID) for the entry found in the NEW PERSON (#200) file.

## EN1^XUPSQRY(): Query New Person File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Common Services

ICR \#: 4575

Description: The XUPS PERSONQUERY RPC uses the EN1^XUPSQRY API. This API provides the functionality to query the NEW PERSON (#200) file. The calling application can query the NEW PERSON (#200) file by using either the Security ID (SECID) of the requested entry or part/all of a last name. Other optional parameters can be passed to the call as additional filters.

![](kernel-8-0-developer-s-guide-common-services-user-guide/008.png) NOTE: This API was released with Kernel Patch XU\*8.0\*325.

Format:

EN1^XUPSQRY(result,xupsecid,xupslnam\[,xupsfnam\]\[,xupsssn\]\[,xupsprov\]\[,xupsstn\]\[,xupsmnm\]\[,xupsdate\])

Input Parameters: result: (required) Name of the subscripted return array. In every API that is used as an RPC, the first parameter is the return array.

xupsecid: (required) This parameter contains the SECID for the requested user. Either the SECID or last name is required.

xupslnam: (required) This parameter contains all or part of a last name. A last name or SECID are required input variables.

xupsfnam: (optional) This parameter is set to NULL or the full or partial first name.

xupsssn: (optional) This parameter is set to NULL or contains the 9 digits of the Social Security Number (SSN).

xupsprov: (optional) This parameter is set to NULL or P. If set to P, it screens for providers (person with active user class).

xupsstn: (optional) This parameter is set to NULL or the Station Number.

xupsmnm: (optional) This parameter is set to the maximum number of entries (1-50) to be returned. Defaults to 50.

xupsdate: (optional) This parameter contains the date used to determine if person class is active. Defaults to current date.

Output Parameters: result(): Returns a subscripted output array of the input value/subscripted array (that is list) with the following possible values shown:

- ^TMP(\$J,“XUPSQRY”,1)—1 if found, 0 if *not* found
- ^TMP(\$J,“XUPSQRY”,n,0)—VPID^IEN^LastName~First Name~Middle Name^SSN^DOB^SEX^
- ^TMP(\$J,“XUPSQRY”,n,1)—Provider Type^
- ^TMP(\$J,“XUPSQRY”,n,2)—Provider Classification^
- ^TMP(\$J,“XUPSQRY”,n,3)—Provider Area of Specialization^
- ^TMP(\$J,“XUPSQRY”,n,4)—VA CODE^X12 CODE^Specialty Code^end-of-record character “\|”\|

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-common-services-user-guide/009.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-common-services-user-guide/010.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-common-services-user-guide/011.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.