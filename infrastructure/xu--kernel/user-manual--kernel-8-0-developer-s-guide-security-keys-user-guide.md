---
title: "Kernel 8.0 Developerâ€™s Guide: Security Keys User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: Security Keys"
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
  - security
  - table
  - span
  - contents
  - guide
  - keys
  - kernel
  - developer
  - class
  - xpdkey
page_count: 0
word_count: 1430
section_count: 8
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_security_keys_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_security_keys_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259514" class="anchor"></span>Security Keys Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-security-keys-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-security-keys-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Security Keys Developer Tools User Guide</em>.</p>
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

<span id="_Toc207255053" class="anchor"></span>List of Figures

<span id="_Ref38421374" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-security-keys-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [Key Lookup](#key-lookup)
  - [Person Lookup](#person-lookup)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [DEL^XPDKEY(): Delete Security Key](#delxpdkey-delete-security-key)
    - [Example](#example)
  - [\$\$LKUP^XPDKEY(): Look Up Security Key Value](#lkupxpdkey-look-up-security-key-value)
    - [Example](#example-1)
  - [\$\$RENAME^XPDKEY(): Rename Security Key](#renamexpdkey-rename-security-key)
  - [OWNSKEY^XUSRB(): Verify Security Keys Assigned to a User](#ownskeyxusrb-verify-security-keys-assigned-to-a-user)
    - [Examples](#examples)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Security Keys Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As well as locking options, developers can use security keys within options if some part of an option requires special security. One example of this is Kernel’s use of the ZTMQ security key; it restricts functionality within the Dequeue Task, Requeue Tasks, and Delete Tasks options.

## Key Lookup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When writing code that checks whether the current user holds a certain key, do *not* reference the SECURITY KEY (#19.1) file for this information. Instead, check the ^XUSEC global. The most efficient check is:

\>I \$D(^XUSEC(keyname,DUZ))

This is (and continues to be) a supported reference. The ^XUSEC global is built by a cross-reference on the SECURITY KEY (#19.1) file.

## Person Lookup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a key is flagged for Person Lookup, a cross-reference on the NEW PERSON (#200) file is built and maintained to facilitate APIs. It is constructed with the letters AK before the key name. The Provider key is exported with the Person Lookup flag set; as a result, providers can be easily identified in this AK.keyname cross-reference, at ^VA(200,“AK.PROVIDER”,DUZ). Specifically, the lookup would be:

\>S DIC="^VA(200,",DIC(0)="AEQ",D="AK.PROVIDER" D IX^DIC

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Security Keys APIs and Extrinsic Functions are available for developers. These APIs and Extrinsic Functions are described below.

## DEL^XPDKEY(): Delete Security Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Security Keys

ICR \#: 1367

Description: The DEL^XPDKEY API deletes a security key from the SECURITY KEY (#19.1) file. All necessary indexing is performed to maintain the ^XUSEC global. The security key is removed from all holders in the NEW PERSON (#200) file.

Format: DEL^XPDKEY(key_ien)

Input Parameters: key_ien: (required) The internal entry number (IEN) of the security key to delete from the SECURITY KEY (#19.1) file.

Output: none.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950693" class="anchor"></span>Figure 1: DEL^XPDKEY API—Example

\><span class="mark">D DEL^XPDKEY(key_ien)</span>

## \$\$LKUP^XPDKEY(): Look Up Security Key Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Security Keys

ICR \#: 1367

Description: The \$\$LKUP^XPDKEY extrinsic function looks up a security key by name or by Internal Entry Number (IEN) value. It returns the security key:

- Name—If called with a security key number.
- IEN—If called with a security key name.

Format: \$\$LKUP^XPDKEY(key_value)

Input Parameters: key_value: (required) The name or IEN of the security key in question.

Output: returns: Returns the security key:

- Name—If called with a security key number.
- IEN—If called with a security key name.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950694" class="anchor"></span>Figure 2: \$\$LKUP^XPDKEY API—Example

\><span class="mark">S value=\$\$LKUP^XPDKEY(key_value)</span>

## \$\$RENAME^XPDKEY(): Rename Security Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Security Keys

ICR \#: 1367

Description: The \$\$RENAME^XPDKEY extrinsic function renames a security key. All necessary indexing is performed to maintain the ^XUSEC global.

Format: \$\$RENAME^XPDKEY(oldname,newname)

Input Parameters: oldname: (required) Name of security key to be renamed.

newname: (required) New name for security key.

Output: returns: Returns:

- 1—Success.
- 0—Failure.

## OWNSKEY^XUSRB(): Verify Security Keys Assigned to a User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Security Keys

ICR \#: 3277

Description: The XUS KEY CHECK RPC uses the OWNSKEY^XUSRB API to verify if a user has a specified security key assigned. The calling routine sends one or a reference to a subscripted array and the API returns a subscripted array with the following possible values:

- 1—User owns key.
- 0—Key *not* found.

The DUZ variable should be defined before calling this API.

![](kernel-8-0-developer-s-guide-security-keys-user-guide/004.png) NOTE: This was developed as a Broker RPC and all RPCs have as the first parameter the return/output parameter.

Format: OWNSKEY^XUSRB(ret,list\[,ien\])

Input Parameters: ret: (required) Name of the subscripted return array. In every API that is used as an RPC, the first parameter is the return array.

list: (required) A single value or an input subscripted array of security keys to be evaluated.

ien: (optional) The DUZ of a user for whom you want to check if they hold security keys.

Output: ret(): Returns a subscripted output array of the input value/subscripted array (that is list) with the following possible values shown:

- 1—User owns key.
- 0—Key *not* found.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

In <u>Figure 3</u>, the return array is named ZZ and the single security key to be checked is the XUPROG security key:

<span id="_Ref501452353" class="anchor"></span>Figure 3: OWNSKEY^XUSRB API—Example 1

\><span class="mark">K ZZ D OWNSKEY^XUSRB(.ZZ,"XUPROG") ZW ZZ</span>

ZZ(0)=1

#### Example 2

In <u>Figure 4</u>, the return subscripted array is named ZZ and the input array of security keys to be checked is named LST:

<span id="_Ref501452381" class="anchor"></span>Figure 4: OWNSKEY^XUSRB API—Example 2

\><span class="mark">K LST S LST(1)="XUPROG",LST(2)="XUMGR",LST(3)="ABC"</span>

\><span class="mark">K ZZ D OWNSKEY^XUSRB(.ZZ,.LST) ZW ZZ</span>

ZZ(1)=1

ZZ(2)=1

ZZ(3)=0

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-security-keys-user-guide/005.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-security-keys-user-guide/006.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-security-keys-user-guide/007.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.