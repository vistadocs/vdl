---
title: "Kernel 8.0 Developerâ€™s Guide: Electronic Signature User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: Electronic Signature"
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
  - span
  - electronic
  - class
  - xusesig
  - smallcaps
  - table
  - contents
  - string
  - signature
  - guide
page_count: 0
word_count: 1848
section_count: 11
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_esig_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_esig_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259297" class="anchor"></span>Electronic Signatures Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-electronic-signature-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-electronic-signature-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Electronic Signatures Developer Tools User Guide</em>.</p>
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

![](kernel-8-0-developer-s-guide-electronic-signature-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [^XUSESIG: Set Up Electronic Signature Code](#xusesig-set-up-electronic-signature-code)
  - [SIG^XUSESIG(): Verify Electronic Signature Code](#sigxusesig-verify-electronic-signature-code)
  - [<span class="smallcaps">\$\$CHKSUM</span>^XUSESIG1(): Build Checksum for Global Root](#span-classsmallcapschksumspanxusesig1-build-checksum-for-global-root)
  - [<span class="smallcaps">\$\$CMP</span>^XUSESIG1(): Compare Checksum to \$NameValue](#span-classsmallcapscmpspanxusesig1-compare-checksum-to-namevalue)
  - [<span class="smallcaps">\$\$DE</span>^XUSESIG1(): Decode String](#span-classsmallcapsdespanxusesig1-decode-string)
  - [<span class="smallcaps">\$\$E</span>N^XUSESIG1(): Encode ESBLOCK](#span-classsmallcapsespannxusesig1-encode-esblock)
  - [<span class="smallcaps">\$\$E</span>SBLOCK^XUSESIG1(): E-Sig Fields Required for Hash](#span-classsmallcapsespansblockxusesig1-e-sig-fields-required-for-hash)
  - [<span class="smallcaps">D</span>E^XUSHSHP: Decrypt Data String](#span-classsmallcapsdspanexushshp-decrypt-data-string)
  - [<span class="smallcaps">E</span>N^XUSHSHP: Encrypt Data String](#span-classsmallcapsespannxushshp-encrypt-data-string)
  - [<span class="smallcaps">H</span>ASH^XUSHSHP: Hash Electronic Signature Code](#span-classsmallcapshspanashxushshp-hash-electronic-signature-code)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Electronic Signatures Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Electronic Signatures APIs and Extrinsic Functions are available for developers. These APIs and Extrinsic Functions are described below.

## ^XUSESIG: Set Up Electronic Signature Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Electronic Signatures

ICR \#: 936

Description: The ^XUSESIG API, when called from the top, allows the user to set up a personal electronic signature code. It is used within application code to allow the user immediate on-the-fly access to set up the electronic signature, rather than force the user to leave the application and enter a different option to do the same.

Format: ^XUSESIG

Input Parameters: none.

Output: none.

## SIG^XUSESIG(): Verify Electronic Signature Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Electronic Signatures

ICR \#: 10050

Description: The SIG^XUSESIG API requests and verifies the electronic signature code of the current user.

Format: SIG^XUSESIG(duz,x1)

Input Parameters: duz: (required) User number.

Output Parameters: x1: If the user entered the correct electronic signature code, the encrypted electronic signature code as stored in the NEW PERSON (#200) file is returned in x1. Otherwise, x1 is returned as NULL.

## <span class="smallcaps">\$\$CHKSUM</span>^XUSESIG1(): Build Checksum for Global Root

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Electronic Signatures

ICR \#: 1557

Description: The <span class="smallcaps">\$\$CHKSUM</span>^XUSESIG1 extrinsic function takes a global root (\$name_value) and builds a checksum for all data in the root.

![](kernel-8-0-developer-s-guide-electronic-signature-user-guide/004.png) NOTE: The flag input parameter is no longer used. Previously, It was used when there was more than one checksum algorithm.

Format: \$\$CHKSUM^XUSESIG1(\$name_value\[,flag\])

Input Parameters: \$name_value: (required) This is a global root as would be returned from \$NAME.

flag: (obsolete) Not used at this time.

Output: returns: Returns the checksum for the global root.

## <span class="smallcaps">\$\$CMP</span>^XUSESIG1(): Compare Checksum to \$Name_Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Electronic Signatures

ICR \#: 1557

Description: The <span class="smallcaps">\$\$CMP</span>^XUSESIG1 extrinsic function compares the checksum passed in to the calculated value from the \$name_value input parameter. It Returns the following:

- 1—Match.
- 0—No match.

Format: \$\$CMP^XUSESIG1(checksum,\$name_value)

Input Parameters: checksum: (required) The output from the <u>\$\$CHKSUM^XUSESIG1(): Build Checksum for Global Root</u> API.

\$name_value: (required) This is a global root as would be returned from \$NAME.

Output: returns: Returns:

- 1—Match.
- 0—No match.

## <span class="smallcaps">\$\$DE</span>^XUSESIG1(): Decode String

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Electronic Signatures

ICR \#: 1557

Description: The <span class="smallcaps">\$\$DE</span>^XUSESIG1 extrinsic function decodes the input string using the checksum as the key.

Format: \$\$DE^XUSESIG1(checksum,encoded_string)

Input Parameters: checksum: (required) The output from the <u>\$\$CHKSUM^XUSESIG1(): Build Checksum for Global Root</u> API.

encoded_string: (required) The output from the <u><span class="smallcaps">\$\$EN</span>^XUSESIG1(): Encode ESBLOCK</u> API.

Output: returns: Returns the decoded string.

## <span class="smallcaps">\$\$E</span>N^XUSESIG1(): Encode ESBLOCK

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Electronic Signatures

ICR \#: 1557

Description: The <span class="smallcaps">\$\$E</span>N^XUSESIG1 extrinsic function encodes the ESBLOCK using the checksum as the key.

Format: \$\$EN^XUSESIG1(checksum,esblock)

Input Parameters: checksum: (required) A number that reveals if the data in the root has been changed.

esblock: (optional) This should be the data returned from the <u><span class="smallcaps">\$\$ESBLOCK</span>^XUSESIG1(): E-Sig Fields Required for Hash</u> API.

Output: returns: Returns encoded ESBLOCK.

## <span class="smallcaps">\$\$E</span>SBLOCK^XUSESIG1(): E-Sig Fields Required for Hash

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Electronic Signatures

ICR \#: 1557

Description: The <span class="smallcaps">\$\$E</span>SBLOCK^XUSESIG1 extrinsic function returns the set of fields from the NEW PERSON (#200) file that are needed as part of the hash for an acceptable electronic signature (E-Sig). These fields include the following:

- E-Sig Block
- E-Sig Title
- Degree
- Current DATE/TIME

If the Internal Entry Number (IEN) is *not* passed in, then it uses the DUZ.

Format: \$\$ESBLOCK^XUSESIG1(\[ien\])

Input Parameters: ien: (optional) This is the Internal Entry Number (IEN) of the NEW PERSON (#200) file entry for which data is requested. The default is to use the DUZ of the current user.

Output: returns: Returns the following fields:

- E-Sig Block
- E-Sig Title
- Degree
- Current DATE/TIME

## <span class="smallcaps">D</span>E^XUSHSHP: Decrypt Data String

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Electronic Signatures

ICR \#: 10045

Description: The <span class="smallcaps">D</span>E^XUSHSHP API decrypts a string encrypted by a call to the <u><span class="smallcaps">EN^XUSHSHP: Encrypt</span> Data String</u> API. Typically, this API would be used to decrypt strings when printing a document containing encrypted strings.

Format: DE^XUSHSHP

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
2.  Set all input variables.
3.  Call the API.

Input Variables: X: (required) Encrypted string generated by a call to the <u><span class="smallcaps">EN^XUSHSHP:</span> Encrypt Data String</u> API.

X1: (required) Identification number used as the X1 input variable in the <u><span class="smallcaps">EN^XUSHSHP:</span> Encrypt Data String</u> API.

X2: (required) Number used as the X2 input variable in the <u><span class="smallcaps">EN^XUSHSHP:</span> Encrypt Data String</u> API.

Output Variables: X: The decrypted string (can be printed).

## <span class="smallcaps">E</span>N^XUSHSHP: Encrypt Data String

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Electronic Signatures

ICR \#: 10045

Description: The <span class="smallcaps">E</span>N^XUSHSHP API encrypts a string and associates the encrypted string with an identification number and a document number. To decrypt the string, a call *must* be made to the <u><span class="smallcaps">DE^XUSHSHP:</span> Decrypt Data String</u> API, with the encrypted string, identification number, and document number as input variables. Typically, this API would be used to encrypt strings within a document.

Format: EN^XUSHSHP

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
4.  Set all input variables.
5.  Call the API.

Input Variables: X: (required) The string to be encrypted (such as the contents of the SIGNATURE BLOCK PRINTED NAME field in the NEW PERSON \[#200\] file).

X1: (required) An identification number (such as DUZ).

X2: (required) A document number (or the number one).

Output Variables: X: Encrypted string.

## <span class="smallcaps">H</span>ASH^XUSHSHP: Hash Electronic Signature Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Electronic Signatures

ICR \#: 10045

Description: The <span class="smallcaps">H</span>ASH^XUSHSHP API uses as input the text string (signature) entered by the user. The routine then hashes the string. The hashed result can then be used to verify the user’s identity by comparison with the stored electronic signature code (in the NEW PERSON \[#200\] file).

Format: HASH^XUSHSHP

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
6.  Set all input variables.
7.  Call the API.

Input Variables: X: (required) Electronic Signature code as entered by the user.

Output Variables: X: Hashed form of the electronic signature code submitted as input to function.

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-electronic-signature-user-guide/005.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-electronic-signature-user-guide/006.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-electronic-signature-user-guide/007.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.