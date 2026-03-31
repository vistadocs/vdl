---
title: "Kernel 8.0 Developerâ€™s Guide: Data Security User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: Data Security"
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
  - returns
  - span
  - table
  - contents
  - guide
  - hash
  - example
  - kernel
  - xushsh
  - string
page_count: 0
word_count: 4035
section_count: 15
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_data_security_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_data_security_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259249" class="anchor"></span>Data Security Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-data-security-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-data-security-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Data Security Developer Tools User Guide</em>.</p>
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

![](kernel-8-0-developer-s-guide-data-security-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [\$\$FILE^XLFSHAN(): Returns SHA Hash for Specified FileMan File or Subfile Entry](#filexlfshan-returns-sha-hash-for-specified-fileman-file-or-subfile-entry)
    - [Example](#example)
  - [\$\$GLOBAL^XLFSHAN(): Returns SHA Hash for a Global](#globalxlfshan-returns-sha-hash-for-a-global)
    - [Example](#example-1)
  - [\$\$HOSTFILE^XLFSHAN(): Returns SHA Hash for Specified Host File](#hostfilexlfshan-returns-sha-hash-for-specified-host-file)
    - [Example](#example-2)
  - [\$\$LSHAN^XLFSHAN(): Returns SHA Hash for a Long Message](#lshanxlfshan-returns-sha-hash-for-a-long-message)
    - [Example](#example-3)
  - [\$\$ROUTINE^XLFSHAN(): Returns SHA Hash for a VistA Routine](#routinexlfshan-returns-sha-hash-for-a-vista-routine)
    - [Example](#example-4)
  - [\$\$SHAN^XLFSHAN(): Returns SHA Hash for a Message](#shanxlfshan-returns-sha-hash-for-a-message)
    - [Example](#example-5)
  - [\$\$AESDECR^XUSHSH(): Returns Plaintext String Value for AES Encrypted Ciphertext Entry](#aesdecrxushsh-returns-plaintext-string-value-for-aes-encrypted-ciphertext-entry)
    - [Example](#example-6)
  - [\$\$AESENCR^XUSHSH(): Returns AES Encrypted Ciphertext for String Entry](#aesencrxushsh-returns-aes-encrypted-ciphertext-for-string-entry)
    - [Example](#example-7)
  - [\$\$B64DECD ^XUSHSH(): Returns Decoded Value for a Base64 String Entry](#b64decd-xushsh-returns-decoded-value-for-a-base64-string-entry)
    - [Example](#example-8)
  - [\$\$B64ENCD^XUSHSH(): Returns Base64 Encoded Value for a String Entry](#b64encdxushsh-returns-base64-encoded-value-for-a-string-entry)
    - [Example](#example-9)
  - [\$\$RSADECR^XUSHSH(): Returns Plaintext String Value for RSA Encrypted Ciphertext Entry](#rsadecrxushsh-returns-plaintext-string-value-for-rsa-encrypted-ciphertext-entry)
    - [Example](#example-10)
  - [\$\$RSAENCR^XUSHSH(): Returns RSA Encrypted Ciphertext for String Entry](#rsaencrxushsh-returns-rsa-encrypted-ciphertext-for-string-entry)
    - [Example](#example-11)
  - [\$\$SHAHASH^XUSHSH(): Returns SHA Hash for a String Entry](#shahashxushsh-returns-sha-hash-for-a-string-entry)
    - [Examples](#examples)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Data Security Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Developers can use data security tools to protect information from unauthorized viewing.

Federal Information Processing Standards Publication 180-4 (FIPS PUB 180-4) specifies secure hash algorithms for computing a condensed representation of electronic data (message). The hash algorithms specified in this Standard are called secure because, for a given algorithm, it is computationally infeasible to find either of the following:

1.  A message that corresponds to a given message digest.
2.  Two different messages that produce the same message digest.

Any change to a message, with a very high probability, results in a different message digest.

Released with Kernel Patch XU\*8.0\*655, the Secure Hash Algorithm (SHA) is a family of one-way cryptographic hash functions. The input data is often called the message, and the hash value is often called the message digest. Cryptographic hash functions are used in the following:

- Digital signatures.
- Message authentication codes.
- Other forms of authentication.

They can also be used to:

- Detect duplicate data.
- Uniquely identify files.
- Detect accidental data corruption as checksums.

In information security contexts, cryptographic hash values are sometimes called digital fingerprints.

Additional SHA utilities were released with Kernel Patch XU\*8.0\*657. These utilities include hashes for the following:

- Specified VA FileMan file or subfile.
- Specified host file.
- Specified routine.
- Message that is too long to be passed as a single string.
- Message that can be passed in a single string.

Encryption is the process of using a mathematical algorithm to transform information so that it becomes unreadable. The information is then available only to those who possess the key that can be used for decryption. Patch XU\*8.0\*655 distributed several encryption utilities, including:

- AES (Advanced Encryption Standard) encryption.
- RSA (Rivest–Shamir–Adleman) encryption.

Binary-to-text encoding schemes are used to represent binary data in an ASCII string format. They are commonly used when there is a need to store or transfer data over media that is designed to deal with textual data to ensure that the data remains intact *without* modification during transport. Patch XU\*8.0\*655 also included Base 64 encoding and decoding utilities.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Data Security APIs and Extrinsic Functions for hashing, encoding/decoding, or encryption/decryption of input of various formats are available for developers. These APIs and Extrinsic Functions are supported under Integration Control Registration (ICR) \#6157 and \#6189 and are described below.

## \$\$FILE^XLFSHAN(): Returns SHA Hash for Specified FileMan File or Subfile Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Data Security

ICR \#: 6157

Description: The \$\$FILE^XLFSHAN extrinsic function returns the SHA hash for a specified file entry. It uses the VA FileMan GETS^DIQ API to extract the data from the file. The input parameters match the input parameters for GETS^DIQ.

![](kernel-8-0-developer-s-guide-data-security-user-guide/004.png) NOTE: The *VA FileMan Developer’s Guide* is located on the [VA Fileman application on the VDL](https://www.va.gov/vdl/application.asp?appid=5).

![](kernel-8-0-developer-s-guide-data-security-user-guide/005.png) NOTE: This API was released with Kernel Patch XU\*8.0\*657.

Format: \$\$FILE^XLFSHAN(hashlen,filenum,iens\[,field\]\[,flags\])

Input Parameters: hashlen: (required) The hash length in bits:

- 160 (SHA-1)
- 224 (SHA-224)
- 256 (SHA-256)
- 384 (SHA-384)
- 512 (SHA-512)filenum: (required) VA FileMan file or subfile number.

iens: (required) Standard VA FileMan IENS indicating internal entry numbers, as documented in the *VA FileMan Developer’s Guide*.

field: (optional) Can be one of the following:

- A single field number.
- A list of field numbers, separated by semicolons.
- A range of field numbers, in the form *M*:*N;* where *M* and *N* are the end points of the inclusive range. All field numbers within this range are retrieved.
- Asterisk (\*) for all fields at the top-level (no sub-Multiple record).
- Double asterisk (\*\*) for all fields including all fields and data in sub-Multiple fields.
- Field number of a multiple followed by an \* to indicate all fields and records in the sub-Multiple for that field.

If this parameter is *not* passed, it defaults to \*\*, which extracts all fields.

flags: (optional) Flags to control processing. The possible values are:

- E—Returns External values in nodes ending with E.
- I—Returns Internal values in nodes ending with I; otherwise, external is returned.
- N—Does *not* return NULL values.
- R—Resolves field numbers to field names in target array subscripts.
- Z—WORD-PROCESSING fields include Zero nodes.
- A#—Audit Trail is used to retrieve the value of "FIELD" at a particular point in time.  
  >   
  > \# is a DATE/TIME in VA FileMan internal format (such as 3021015.08). The values retrieved are the (audited) values of the fields as of that DATE/TIME.

Output: returns: Returns:

- SHA hash—If successful.
- Zero (0)—If the file could *not* be opened or found.
- -1—If an error occurs.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950534" class="anchor"></span>Figure 1: \$\$FILE^XLFSHAN API—Example

\><span class="mark">W \$\$FILE^XLFSHAN(512,200,"10000000407,")</span>

8FE96A435D69989EFC30FC852260990BECB030247657B9CA1CDB9D103097B51792648254770D88E292592CC06C36D22C3E502F790050B8ADBB035C89F59FB8A7

## \$\$GLOBAL^XLFSHAN(): Returns SHA Hash for a Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Data Security

ICR \#: 6157

Description: The \$\$GLOBAL^XLFSHAN extrinsic function returns the SHA hash of a specified global, in contrast with the [\$\$FILE^XLFSHAN](#filexlfshan-returns-sha-hash-for-specified-fileman-file-or-subfile-entry) API, which returns the hash for a particular entry in a global.

![](kernel-8-0-developer-s-guide-data-security-user-guide/006.png) NOTE: This API was released with Kernel Patch XU\*8.0\*657.

Format: \$\$GLOBAL^XLFSHAN(hashlen,filenum,dataonly)

Input Parameters: hashlen: (required) The hash length in bits:

- 160 (SHA-1)
- 224 (SHA-224)
- 256 (SHA-256)
- 384 (SHA-384)
- 512 (SHA-512)

filenum: (required) VA FileMan file number.

dataonly: (required) Scope of the hash:

- 0—Global location of the data is to be included in the hash computation.
- 1—Hash is computed only for the data.

Output: returns: Returns:

- SHA hash—If successful.
- Zero (0)—If there is an error.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950535" class="anchor"></span>Figure 2: \$\$GLOBAL^XLFSHAN API—Example

\><span class="mark">W \$\$GLOBAL^XLFSHAN(256,200,0)</span>

714CE00DE20E30700229F95F69DBAE34262CF30576EA03852CFBE0D0DC2BE611

## \$\$HOSTFILE^XLFSHAN(): Returns SHA Hash for Specified Host File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Data Security

ICR \#: 6157

Description: The \$\$HOSTFILE^XLFSHAN extrinsic function returns the SHA hash for a specified host file. It uses the [\$\$FTG^%ZISH](#ftg_zish) API to load the host file for processing.

![](kernel-8-0-developer-s-guide-data-security-user-guide/007.png) NOTE: This API was released with Kernel Patch XU\*8.0\*657.

Format: \$\$HOSTFILE^XLFSHAN(hashlen,path,filename)

Input Parameters: hashlen: (required) The hash length in bits:

- 160 (SHA-1)
- 224 (SHA-224)
- 256 (SHA-256)
- 384 (SHA-384)
- 512 (SHA-512)

path: (required) Full path, up to but *not* including the filename.

filename: (required) Name of the file.

Output: returns: Returns:

- SHA hash—If successful.
- Zero (0)—If the host file could *not* be opened/found.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950536" class="anchor"></span>Figure 3: \$\$HOSTFILE^XLFSHAN API—Example

\><span class="mark">W \$\$HOSTFILE^XLFSHAN(160,"Z:\Cache2014\\,"cache.cpf")</span>

F11F3595604296A1F8BCF13AA7F2744FB9EB1675

## \$\$LSHAN^XLFSHAN(): Returns SHA Hash for a Long Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Data Security

ICR \#: 6157

Description: The \$\$LSHAN^XLFSHAN extrinsic function returns the SHA hash of a message that is too long to be passed as a single string. The message is passed in ^TMP(\$J,MSUB). The message should be broken into blocks that are exactly 64 bytes/characters long except for the last one. ^TMP(\$J,MSG,N) is the *N*th block of the message; where *N* runs from 1 to NBLOCKS.

![](kernel-8-0-developer-s-guide-data-security-user-guide/008.png) NOTE: This API was released with Kernel Patch XU\*8.0\*657.

Format: \$\$LSHAN^XLFSHAN(hashlen,msub,nblocks)

Input Parameters: hashlen: (required) The hash length in bits:

- 160 (SHA-1)
- 224 (SHA-224)
- 256 (SHA-256)
- 384 (SHA-384)
- 512 (SHA-512)

msub: (required) The ^TMP(\$J,msub) subscript in which the message is passed.

nblocks: (required) The number of blocks in the message.

Output: returns: Returns:

- SHA hash—If successful.
- Zero (0)—If there is an error.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950537" class="anchor"></span>Figure 4: \$\$LSHAN^XLFSHAN API—Example

\><span class="mark">S ^TMP(\$J,"MSG",1)= "test line one"</span>

\><span class="mark">S ^TMP(\$J,"MSG",2)= "test line two"</span>

\><span class="mark">W \$\$LSHAN^XLFSHAN(224,"MSG",2)</span>

42E2C4B559757087BFA5834F43C2C50740984766910C1B4EEC79A350

## \$\$ROUTINE^XLFSHAN(): Returns SHA Hash for a VistA Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Data Security

ICR \#: 6157

Description: The \$\$ROUTINE^XLFSHAN extrinsic function returns the SHA hash for a specified VistA routine.

![](kernel-8-0-developer-s-guide-data-security-user-guide/009.png) NOTE: This API was released with Kernel Patch XU\*8.0\*657.

Format: \$\$ROUTINE^XLFSHAN(hashlen,routine)

Input Parameters: hashlen: (required) The hash length in bits:

- 160 (SHA-1)
- 224 (SHA-224)
- 256 (SHA-256)
- 384 (SHA-384)
- 512 (SHA-512)

routine: (required) The name of the routine.

Output: returns: Returns:

- SHA hash—If successful.
- Zero (0)—If the routine could *not* be opened/found.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950538" class="anchor"></span>Figure 5: \$\$ROUTINE^XLFSHAN API—Example

\><span class="mark">W \$\$ROUTINE^XLFSHAN(384,"XUCERT")</span>

54BA28936CE7CEC515305AE4BBD07FC4FD7620ACF0EAD0AF6A9E5BFBEEF24794DA414C0C33A6C0C3B90005D70A2BFE4D

## \$\$SHAN^XLFSHAN(): Returns SHA Hash for a Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Data Security

ICR \#: 6157

Description: The \$\$SHAN^XLFSHAN extrinsic function returns the SHA hash of a message.

![](kernel-8-0-developer-s-guide-data-security-user-guide/010.png) NOTE: This API was released with Kernel Patch XU\*8.0\*657.

Format: \$\$SHAN^XLFSHAN(hashlen,message)

Input Parameters: hashlen: (required) The hash length in bits:

- 160 (SHA-1)
- 224 (SHA-224)
- 256 (SHA-256)
- 384 (SHA-384)
- 512 (SHA-512)

message: (required) The message string.

Output: returns: Returns:

- SHA hash—If successful.
- Zero (0)—If there is an error.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950539" class="anchor"></span>Figure 6: \$\$SHAN^XLFSHAN API—Example

\><span class="mark">W \$\$SHAN^XLFSHAN(256,"this is a test")</span>

2E99758548972A8E8822AD47FA1017FF72F06F3FF6A016851F45C398732BC50C

## \$\$AESDECR^XUSHSH(): Returns Plaintext String Value for AES Encrypted Ciphertext Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Data Security

ICR \#: 6189

Description: The \$\$AESDECR^XUSHSH extrinsic function returns the string value of an Advanced Encryption Standard (AES) encrypted ciphertext entry. AES is a specification for the encryption of electronic data established by the U.S. National Institute of Standards and Technology (NIST) in 2001.

![](kernel-8-0-developer-s-guide-data-security-user-guide/011.png) NOTE: This API was released with Kernel Patch XU\*8.0\*655.

Format: \$\$AESDECR^XUSHSH(text,key\[,iv\])

Input Parameters: text: (required) The ciphertext string to be decrypted.

key: (required) The input key material 16, 24, or 32 characters long.

iv: (optional) The initialization vector. If this argument is present, it *must* be 16 characters long.

Output: returns: Returns the plaintext value of the AES encrypted ciphertext entry in the text input parameter.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950540" class="anchor"></span>Figure 7: \$\$AESDECR^XUSHSH API—Example

\><span class="mark">W \$\$AESDECR^XUSHSH(\$\$B64DECD^XUSHSH("STbvalBtOxy754eRo15Bkg=="),"Encr4pt10nK3y")</span>

This is a test

## \$\$AESENCR^XUSHSH(): Returns AES Encrypted Ciphertext for String Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Data Security

ICR \#: 6189

Description: The \$\$AESENCR^XUSHSH extrinsic function returns the Advanced Encryption Standard (AES) encrypted ciphertext for a string entry. AES is a specification for the encryption of electronic data established by the U.S. National Institute of Standards and Technology (NIST) in 2001.

![](kernel-8-0-developer-s-guide-data-security-user-guide/012.png) NOTE: This API was released with Kernel Patch XU\*8.0\*655.

Format: \$\$AESENCR^XUSHSH(text,key\[,iv\])

Input Parameters: text: (required) The plaintext string to be encrypted.

key: (required) The input key material 16, 24, or 32 characters long.

iv: (optional) The initialization vector. If this argument is present, it *must* be 16 characters long.

Output: returns: Returns the AES encrypted ciphertext for the string entry in the text input parameter.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](kernel-8-0-developer-s-guide-data-security-user-guide/013.png) NOTE: The AES encryption API returns Unicode ciphertext, which does *not* properly display on an ASCII roll-and-scroll terminal; so, the example demonstrated output is Base64 encoded before display.

<span id="_Toc199950541" class="anchor"></span>Figure 8: \$\$AESENCR^XUSHSH API—Example

\><span class="mark">W \$\$B64ENCD^XUSHSH(\$\$AESENCR^XUSHSH("This is a test","Encr4pt10nK3y"))</span>

STbvalBtOxy754eRo15Bkg==

## \$\$B64DECD ^XUSHSH(): Returns Decoded Value for a Base64 String Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Data Security

ICR \#: 6189

Description: The \$\$B64DECD ^XUSHSH extrinsic function returns the decoded value for a Base64 string entry. Base64 is a binary-to-text encoding scheme that represents binary data in an ASCII string format by translating it into a radix-64 representation. Base64 encoding is commonly used when there is a need to encode binary data that needs to be stored and transferred over media that is designed to deal with textual data.

![](kernel-8-0-developer-s-guide-data-security-user-guide/014.png) NOTE: This API was released with Kernel Patch XU\*8.0\*655.

Format: \$\$B64DECD^XUSHSH(x)

Input Parameters: x: (required) The string to be decoded.

Output: returns: Returns the decoded value for the Base64 input parameter.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950542" class="anchor"></span>Figure 9: \$\$B64DECD ^XUSHSH API—Example

\><span class="mark">W \$\$B64DECD^XUSHSH("VGhpcyBpcyBhIHRlc3Q=")</span>

This is a test

## \$\$B64ENCD^XUSHSH(): Returns Base64 Encoded Value for a String Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Data Security

ICR \#: 6189

Description: The \$\$B64ENCD^XUSHSH extrinsic function returns the Base64 encoded value for a string entry. Base64 is a binary-to-text encoding scheme that represents binary data in an ASCII string format by translating it into a radix-64 representation. Base64 encoding is commonly used when there is a need to encode binary data that needs to be stored and transferred over media that is designed to deal with textual data.

![](kernel-8-0-developer-s-guide-data-security-user-guide/015.png) NOTE: This API was released with Kernel Patch XU\*8.0\*655.

Format: \$\$B64ENCD^XUSHSH(x)

Input Parameters: x: (required) The string to be encoded.

Output: returns: Returns the Base64 encoded value of the input parameter.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950543" class="anchor"></span>Figure 10: \$\$B64ENCD^XUSHSH API—Example

\><span class="mark">W \$\$B64ENCD^XUSHSH("This is a test")</span>

VGhpcyBpcyBhIHRlc3Q=

## \$\$RSADECR^XUSHSH(): Returns Plaintext String Value for RSA Encrypted Ciphertext Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Data Security

ICR \#: 6189

Description: The \$\$RSADECR^XUSHSH extrinsic function returns the plaintext string value for an RSA encrypted ciphertext entry. RSA is a public-key encryption system that is widely used for secure data transmission. The encryption key is public and differs from the decryption key, which is kept secret.

![](kernel-8-0-developer-s-guide-data-security-user-guide/016.png) NOTE: This API was released with Kernel Patch XU\*8.0\*655.

Format: \$\$RSADECR^XUSHSH(text,key\[,pwd\]\[,enc\])

Input Parameters: text: (required) The RSA encrypted ciphertext string to be decrypted.

key: (required) The RSA private key corresponding to the RSA public key that was used for encryption, Privacy Enhanced Mail (PEM) encoded.

pwd: (optional) The private key password.

enc: (optional) Encoding - Public-Key Cryptography Standards (PKCS) \#1 v2.1 encoding method:

- 1—Optimal Asymmetric Encryption Padding (OAEP; default).
- 2—PKCS 1-v1_5.

Output: returns: Returns the plaintext string value for the RSA encrypted ciphertext text input parameter.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](kernel-8-0-developer-s-guide-data-security-user-guide/017.png) NOTE: "hgwds" is the alias of a certificate installed in Caché through the management portal for demonstration purposes. The private key used to decrypt the ciphertext was *not* available, so that function is *not* demonstrated here.

## \$\$RSAENCR^XUSHSH(): Returns RSA Encrypted Ciphertext for String Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Data Security

ICR \#: 6189

Description: The \$\$RSAENCR^XUSHSH extrinsic function returns the RSA encrypted ciphertext for a string entry. RSA is a public-key encryption system that is widely used for secure data transmission. The encryption key is public and differs from the decryption key, which is kept secret.

![](kernel-8-0-developer-s-guide-data-security-user-guide/018.png) NOTE: This API was released with Kernel Patch XU\*8.0\*655.

Format: \$\$RSAENCR^XUSHSH(text,cert\[,cafile\]\[,crlfile\]\[,enc\])

Input Parameters: text: (required) The plaintext string to be encrypted.

cert: (required) An X.509 certificate containing the RSA public key to be used for encryption, in PEM encoded or binary Distinguished Encoding Rules (DER) format. The length of the plaintext *cannot* be greater than the length of the modulus of the RSA public key contained in the certificate minus 42 bytes.

cafile: (optional) The name of a file containing the trusted Certificate Authority X.509 Certificates in PEM-encoded format, one of which was used to sign the certificate.

crlfile: (optional) The name of a file containing X.509 Certificate Revocation Lists in PEM-encoded format that should be checked to verify the status of the certificate.

enc: (optional) Encoding - PKCS \#1 v2.1 encoding method:

- 1—Optimal Asymmetric Encryption Padding (OAEP; default).
- 2—PKCS 1-v1_5.

Output: returns: Returns the RSA encrypted ciphertext value of the text input parameter.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](kernel-8-0-developer-s-guide-data-security-user-guide/019.png) NOTE: The RSA encryption API returns Unicode ciphertext, which does *not* properly display on an ASCII roll-and-scroll terminal; so, the example demonstrated output is Base64 encoded before display.

<span id="_Toc199950544" class="anchor"></span>Figure 11: \$\$RSAENCR^XUSHSH API—Example

\><span class="mark">S TEXT="This is a test"</span>

\><span class="mark">S CREDSET=##class(%SYS.X509Credentials).GetByAlias("hgwds")</span>

\><span class="mark">S CERT=CREDSET.Certificate</span>

\><span class="mark">W \$\$B64ENCD^XUSHSH(\$\$RSAENCR^XUSHSH(TEXT,CERT,,,1))</span>

PbFxIUBA+Mu5F4rtFHVJOusYfqFOm99eyhp3jYTBBIteSMYE1J+dHFqSePGtGXInBIy2f6gVxTvf

WQyy8Le92tbqADftPsGKlBISaA1O3v2r0oxYQkwR6FPub3y/r92b6l/StwAzImMF9EP6vqLt/IOK

1eu4UD+sT5qesGB9zgAmEfQgitT3qhXZJZUAbIi//NZbLiWVtGF+99GSa77VyMXkWqKiSVZZHCLG

yUGgPn8SwFXEsZNs+STuFaQn6jialrn04NOuaqXEDSZu1qGpn5WE3fNcWeLZE5sXJX8rG0uW5R/O

lx/Xlk3L2GhqELELsgzJY0RG5fp8wT58cJKqwQ==

## \$\$SHAHASH^XUSHSH(): Returns SHA Hash for a String Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Data Security

ICR \#: 6189

Description: The \$\$SHAHASH^XUSHSH extrinsic function returns the Secure Hash Algorithm (SHA) hash for a string entry. It uses an input variable to specify the length in bits of the desired hash.

![](kernel-8-0-developer-s-guide-data-security-user-guide/020.png) NOTE: This API was released with Kernel Patch XU\*8.0\*655.

Format: \$\$SHAHASH^XUSHSH(n,x\[,flag\])

Input Parameters: n: (required) Length in bits of the desired hash:

- 160 (SHA-1)
- 224 (SHA-224)
- 256 (SHA-256)
- 384 (SHA-384)
- 512 (SHA-512)

x: (required) String to be hashed.

flag: (optional) Flag to control format of hash:

- H—Hexadecimal (default)
- B—Base64 Encoded

Output: returns: Returns SHA hash for a string entry.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

<span id="_Toc199950545" class="anchor"></span>Figure 12: \$\$SHAHASH^XUSHSH API—Example 1

\><span class="mark">W \$\$SHAHASH^XUSHSH(256,"This is a test")</span>

C7BE1ED902FB8DD4D48997C6452F5D7E509FBCDBE2808B16BCF4EDCE4C07D14E

\>

#### Example 2

<span id="_Toc199950546" class="anchor"></span>Figure 13: \$\$SHAHASH^XUSHSH API—Example 1

\><span class="mark">W \$\$SHAHASH^XUSHSH(256,"This is a test","B")</span>

x74e2QL7jdTUiZfGRS9dflCfvNvigIsWvPTtzkwH0U4=

\>

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-data-security-user-guide/021.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-data-security-user-guide/022.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-data-security-user-guide/023.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.