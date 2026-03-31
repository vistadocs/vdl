---
title: "Kernel 8.0 Developerâ€™s Guide: XLF Function Library User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: XLF Function Library"
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
  - class
  - example
  - mark
  - returns
  - table
  - contents
  - xlfmth
  - format
  - date
page_count: 0
word_count: 18599
section_count: 12
table_count: 5
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_xlf_fl_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_xlf_fl_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259769" class="anchor"></span>XLF Function Library Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
<caption><blockquote>
<p><span id="_Ref200268660" class="anchor"></span>Table 1: $$LENGTH^XLFMSMT API—Valid Units</p>
</blockquote></caption>
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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: XLF Function Library Developer Tools User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref200268660" class="anchor"></span>Table 1: \$\$LENGTH^XLFMSMT API—Valid Units

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc207256229" class="anchor"></span>List of Figures

<span id="_Toc207256230" class="anchor"></span>List of Tables

<span id="_Hlt412359042" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [Bitwise Logic Functions—XLFSHAN](#bitwise-logic-functionsxlfshan)
    - [\$\$AND^XLFSHAN(): Bitwise Logical AND](#andxlfshan-bitwise-logical-and)
    - [\$\$OR^XLFSHAN(): Bitwise Logical OR](#orxlfshan-bitwise-logical-or)
    - [\$\$XOR^XLFSHAN(): Bitwise Logical XOR](#xorxlfshan-bitwise-logical-xor)
  - [CRC Functions—XLFCRC](#crc-functionsxlfcrc)
    - [\$\$CRC16^XLFCRC(): Cyclic Redundancy Code 16](#crc16xlfcrc-cyclic-redundancy-code-16)
    - [\$\$CRC32^XLFCRC(): Cyclic Redundancy Code 32](#crc32xlfcrc-cyclic-redundancy-code-32)
  - [Date Functions—XLFDT](#date-functionsxlfdt)
    - [\$\$%H^XLFDT(): Convert Seconds to \$H](#hxlfdt-convert-seconds-to-h)
    - [\$\$DOW^XLFDT(): Day of Week](#dowxlfdt-day-of-week)
    - [\$\$DT^XLFDT: Current Date (VA FileMan Date Format)](#dtxlfdt-current-date-va-fileman-date-format)
    - [\$\$FMADD^XLFDT(): VA FileMan Date Add](#fmaddxlfdt-va-fileman-date-add)
    - [\$\$FMDIFF^XLFDT(): VA FileMan Date Difference](#fmdiffxlfdt-va-fileman-date-difference)
    - [\$\$FMTE^XLFDT(): Convert VA FileMan Date to External Format](#fmtexlfdt-convert-va-fileman-date-to-external-format)
    - [\$\$FMTH^XLFDT(): Convert VA FileMan Date to \$H](#fmthxlfdt-convert-va-fileman-date-to-h)
    - [\$\$FMTHL7^XLFDT(): Convert VA FileMan Date to HL7 Date](#fmthl7xlfdt-convert-va-fileman-date-to-hl7-date)
    - [\$\$HADD^XLFDT(): \$H Add](#haddxlfdt-h-add)
    - [\$\$HDIFF^XLFDT(): \$H Difference](#hdiffxlfdt-h-difference)
    - [\$\$HL7TFM^XLFDT(): Convert HL7 Date to VA FileMan Date](#hl7tfmxlfdt-convert-hl7-date-to-va-fileman-date)
    - [\$\$HTE^XLFDT(): Convert \$H to External Format](#htexlfdt-convert-h-to-external-format)
    - [\$\$HTFM^XLFDT(): Convert \$H to VA FileMan Date Format](#htfmxlfdt-convert-h-to-va-fileman-date-format)
    - [\$\$NOW^XLFDT: Current Date and Time (VA FileMan Format)](#nowxlfdt-current-date-and-time-va-fileman-format)
    - [\$\$SCH^XLFDT(): Next Scheduled Runtime](#schxlfdt-next-scheduled-runtime)
    - [\$\$SEC^XLFDT(): Convert \$H/VA FileMan date to Seconds](#secxlfdt-convert-hva-fileman-date-to-seconds)
    - [\$\$TZ^XLFDT: Time Zone Offset (GMT)](#tzxlfdt-time-zone-offset-gmt)
    - [\$\$WITHIN^XLFDT(): Checks Dates/Times within Schedule](#withinxlfdt-checks-datestimes-within-schedule)
  - [Hyperbolic Trigonometric Functions—XLFHYPER](#hyperbolic-trigonometric-functionsxlfhyper)
    - [\$\$ACOSH^XLFHYPER(): Hyperbolic Arc-Cosine](#acoshxlfhyper-hyperbolic-arc-cosine)
    - [\$\$ACOTH^XLFHYPER(): Hyperbolic Arc-Cotangent](#acothxlfhyper-hyperbolic-arc-cotangent)
    - [\$\$ACSCH^XLFHYPER(): Hyperbolic Arc-Cosecant](#acschxlfhyper-hyperbolic-arc-cosecant)
    - [\$\$ASECH^XLFHYPER(): Hyperbolic Arc-Secant](#asechxlfhyper-hyperbolic-arc-secant)
    - [\$\$ASINH^XLFHYPER(): Hyperbolic Arc-Sine](#asinhxlfhyper-hyperbolic-arc-sine)
    - [\$\$ATANH^XLFHYPER(): Hyperbolic Arc-Tangent](#atanhxlfhyper-hyperbolic-arc-tangent)
    - [\$\$COSH^XLFHYPER(): Hyperbolic Cosine](#coshxlfhyper-hyperbolic-cosine)
    - [\$\$COTH^XLFHYPER(): Hyperbolic Cotangent](#cothxlfhyper-hyperbolic-cotangent)
    - [\$\$CSCH^XLFHYPER(): Hyperbolic Cosecant](#cschxlfhyper-hyperbolic-cosecant)
    - [\$\$SECH^XLFHYPER(): Hyperbolic Secant](#sechxlfhyper-hyperbolic-secant)
    - [\$\$SINH^XLFHYPER(): Hyperbolic Sine](#sinhxlfhyper-hyperbolic-sine)
    - [\$\$TANH^XLFHYPER(): Hyperbolic Tangent](#tanhxlfhyper-hyperbolic-tangent)
  - [Mathematical Functions—XLFMTH](#mathematical-functionsxlfmth)
    - [\$\$ABS^XLFMTH(): Absolute Value](#absxlfmth-absolute-value)
    - [\$\$ACOS^XLFMTH(): Arc-Cosine (Radians)](#acosxlfmth-arc-cosine-radians)
    - [\$\$ACOSDEG^XLFMTH(): Arc-Cosine (Degrees)](#acosdegxlfmth-arc-cosine-degrees)
    - [\$\$ACOT^XLFMTH(): Arc-Cotangent (Radians)](#acotxlfmth-arc-cotangent-radians)
    - [\$\$ACOTDEG^XLFMTH(): Arc-Cotangent (Degrees)](#acotdegxlfmth-arc-cotangent-degrees)
    - [\$\$ACSC^XLFMTH(): Arc-Cosecant (Radians)](#acscxlfmth-arc-cosecant-radians)
    - [\$\$ACSCDEG^XLFMTH(): Arc-Cosecant (Degrees)](#acscdegxlfmth-arc-cosecant-degrees)
    - [\$\$ASEC^XLFMTH(): Arc-Secant (Radians)](#asecxlfmth-arc-secant-radians)
    - [\$\$ASECDEG^XLFMTH(): Arc-Secant (Degrees)](#asecdegxlfmth-arc-secant-degrees)
    - [\$\$ASIN^XLFMTH(): Arc-Sine (Radians)](#asinxlfmth-arc-sine-radians)
    - [\$\$ASINDEG^XLFMTH(): Arc-Sine (Degrees)](#asindegxlfmth-arc-sine-degrees)
    - [\$\$ATAN^XLFMTH(): Arc-Tangent (Radians)](#atanxlfmth-arc-tangent-radians)
    - [\$\$ATANDEG^XLFMTH(): Arc-Tangent (Degrees)](#atandegxlfmth-arc-tangent-degrees)
    - [\$\$COS^XLFMTH(): Cosine (Radians)](#cosxlfmth-cosine-radians)
    - [\$\$COSDEG^XLFMTH(): Cosine (Degrees)](#cosdegxlfmth-cosine-degrees)
    - [\$\$COT^XLFMTH(): Cotangent (Radians)](#cotxlfmth-cotangent-radians)
    - [\$\$COTDEG^XLFMTH(): Cotangent (Degrees)](#cotdegxlfmth-cotangent-degrees)
    - [\$\$CSC^XLFMTH(): Cosecant (Radians)](#cscxlfmth-cosecant-radians)
    - [\$\$CSCDEG^XLFMTH(): Cosecant (Degrees)](#cscdegxlfmth-cosecant-degrees)
    - [\$\$DECDMS^XLFMTH(): Convert Decimals to Degrees:Minutes:Seconds](#decdmsxlfmth-convert-decimals-to-degreesminutesseconds)
    - [\$\$DMSDEC^XLFMTH(): Convert Degrees:Minutes:Seconds to Decimal](#dmsdecxlfmth-convert-degreesminutesseconds-to-decimal)
    - [\$\$DTR^XLFMTH(): Convert Degrees to Radians](#dtrxlfmth-convert-degrees-to-radians)
    - [\$\$E^XLFMTH(): e—Natural Logarithm](#exlfmth-enatural-logarithm)
    - [\$\$EXP^XLFMTH(): e—Natural Logarithm to the Nth Power](#expxlfmth-enatural-logarithm-to-the-nth-power)
    - [\$\$LN^XLFMTH(): Natural Log (Base e)](#lnxlfmth-natural-log-base-e)
    - [\$\$LOG^XLFMTH(): Logarithm (Base 10)](#logxlfmth-logarithm-base-10)
    - [\$\$MAX^XLFMTH(): Maximum of Two Numbers](#maxxlfmth-maximum-of-two-numbers)
    - [\$\$MIN^XLFMTH(): Minimum of Two Numbers](#minxlfmth-minimum-of-two-numbers)
    - [\$\$PI^XLFMTH(): PI](#pixlfmth-pi)
    - [\$\$PWR^XLFMTH(): X to the Y Power](#pwrxlfmth-x-to-the-y-power)
    - [\$\$RTD^XLFMTH(): Convert Radians to Degrees](#rtdxlfmth-convert-radians-to-degrees)
    - [\$\$SD^XLFMTH(): Standard Deviation](#sdxlfmth-standard-deviation)
    - [\$\$SEC^XLFMTH(): Secant (Radians)](#secxlfmth-secant-radians)
    - [\$\$SECDEG^XLFMTH(): Secant (Degrees)](#secdegxlfmth-secant-degrees)
    - [\$\$SIN^XLFMTH(): Sine (Radians)](#sinxlfmth-sine-radians)
    - [\$\$SINDEG^XLFMTH(): Sine (Degrees)](#sindegxlfmth-sine-degrees)
    - [\$\$SQRT^XLFMTH(): Square Root](#sqrtxlfmth-square-root)
    - [\$\$TAN^XLFMTH(): Tangent (Radians)](#tanxlfmth-tangent-radians)
    - [\$\$TANDEG^XLFMTH(): Tangent (Degrees)](#tandegxlfmth-tangent-degrees)
  - [Measurement Functions—XLFMSMT](#measurement-functionsxlfmsmt)
    - [\$\$BSA^XLFMSMT(): Body Surface Area Measurement](#bsaxlfmsmt-body-surface-area-measurement)
    - [\$\$LENGTH^XLFMSMT(): Convert Length Measurement](#lengthxlfmsmt-convert-length-measurement)
    - [\$\$TEMP^XLFMSMT(): Convert Temperature Measurement](#tempxlfmsmt-convert-temperature-measurement)
    - [\$\$VOLUME^XLFMSMT(): Convert Volume Measurement](#volumexlfmsmt-convert-volume-measurement)
    - [\$\$WEIGHT^XLFMSMT(): Convert Weight Measurement](#weightxlfmsmt-convert-weight-measurement)
  - [String Functions—XLFSTR](#string-functionsxlfstr)
    - [\$\$CJ^XLFSTR(): Center Justify String](#cjxlfstr-center-justify-string)
    - [\$\$INVERT^XLFSTR(): Invert String](#invertxlfstr-invert-string)
    - [\$\$LJ^XLFSTR(): Left Justify String](#ljxlfstr-left-justify-string)
    - [\$\$LOW^XLFSTR(): Convert String to Lowercase](#lowxlfstr-convert-string-to-lowercase)
    - [\$\$REPEAT^XLFSTR(): Repeat String](#repeatxlfstr-repeat-string)
    - [\$\$REPLACE^XLFSTR(): Replace Strings](#replacexlfstr-replace-strings)
    - [\$\$RJ^XLFSTR(): Right Justify String](#rjxlfstr-right-justify-string)
    - [\$\$SENTENCE^XLFSTR(): Convert String to Sentence Case](#sentencexlfstr-convert-string-to-sentence-case)
    - [\$\$STRIP^XLFSTR(): Strip a String](#stripxlfstr-strip-a-string)
    - [\$\$TITLE^XLFSTR(): Convert String to Title Case](#titlexlfstr-convert-string-to-title-case)
    - [\$\$TRIM^XLFSTR(): Trim String](#trimxlfstr-trim-string)
    - [\$\$UP^XLFSTR(): Convert String to Uppercase](#upxlfstr-convert-string-to-uppercase)
  - [Utility Functions—XLFUTL](#utility-functionsxlfutl)
    - [\$\$BASE^XLFUTL(): Convert Between Two Bases](#basexlfutl-convert-between-two-bases)
    - [\$\$CCD^XLFUTL(): Append Check Digit](#ccdxlfutl-append-check-digit)
    - [\$\$CNV^XLFUTL(): Convert Base 10 to Another Base](#cnvxlfutl-convert-base-10-to-another-base)
    - [\$\$DEC^XLFUTL(): Convert Another Base to Base 10](#decxlfutl-convert-another-base-to-base-10)
    - [\$\$VCD^XLFUTL(): Verify Integrity](#vcdxlfutl-verify-integrity)
  - [IP Address Functions—XLFIPV](#ip-address-functionsxlfipv)
    - [\$\$CONVERT^XLFIPV(): Convert any IP Address to Standardized IP Address Format](#convertxlfipv-convert-any-ip-address-to-standardized-ip-address-format)
    - [\$\$FORCEIP4^XLFIPV(): Convert any IP Address to IPv4](#forceip4xlfipv-convert-any-ip-address-to-ipv4)
    - [\$\$FORCEIP6^XLFIPV(): Convert any IP Address to IPv6](#forceip6xlfipv-convert-any-ip-address-to-ipv6)
    - [\$\$VALIDATE^XLFIPV(): Validate IP Address Format](#validatexlfipv-validate-ip-address-format)
    - [\$\$VERSION^XLFIPV: Show System Settings for IPv6](#versionxlfipv-show-system-settings-for-ipv6)
  - [JSON Conversion Functions—XLFJSON](#json-conversion-functionsxlfjson)
    - [DECODE^XLFJSON(): Convert a JSON Object into a Closed Array Reference](#decodexlfjson-convert-a-json-object-into-a-closed-array-reference)
    - [ENCODE^XLFJSON(): Convert Closed Array or Global Reference to a JSON Object](#encodexlfjson-convert-closed-array-or-global-reference-to-a-json-object)
    - [\$\$ESC^XLFJSON(): Escape String to JSON](#escxlfjson-escape-string-to-json)
    - [\$\$UES^XLFJSON(): Unescape JSON to a String](#uesxlfjson-unescape-json-to-a-string)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: XLF Function Library Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several APIs are available for developers to work with the XLF Function Library. These APIs are described in the sections that follow.

The XLF Function Library provides the following functions:

- <u>Bitwise Logic Functions—XLFSHAN</u>
- <u>CRC Functions—XLFCRC</u>
- <u>Date Functions—XLFDT</u>
- <u>Hyperbolic Trigonometric Functions—XLFHYPER</u>
- <u>Mathematical Functions—XLFMTH</u>
- <u>Measurement Functions—XLFMSMT</u>
- <u>String Functions—XLFSTR</u>
- <u>Utility Functions—XLFUTL</u>
- <u>IP Address Functions—XLFIPV</u>
- <u>JSON Conversion Functions—XLFJSON</u>

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Bitwise Logic Functions—XLFSHAN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These functions help process bitwise logic[^1].

### \$\$AND^XLFSHAN(): Bitwise Logical AND

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Bitwise Logic Functions

ICR \#: 6157

Description: The \$\$AND^XLFSHAN extrinsic function performs a bitwise logical AND of two 32 bit integers.

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/004.png) NOTE: This API was released with Kernel Patch XU\*8.0\*657.

Format: \$\$AND^XLFSHAN(x,y)

Input Parameters: x: (required) An integer of 32 bits or less.

y: (required) An integer of 32 bits or less.

Output: returns: Returns the bitwise logical AND.

#### Example

<span id="_Toc199950834" class="anchor"></span>Figure 1: \$\$AND^XLFSHAN API—Example

\><span class="mark">W \$\$AND^XLFSHAN(345,123)</span>

89

### \$\$OR^XLFSHAN(): Bitwise Logical OR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Bitwise Logic Functions

ICR \#: 6157

Description: The \$\$OR^XLFSHAN extrinsic function performs a bitwise logical OR of two 32 bit integers.

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/005.png) NOTE: This API was released with Kernel Patch XU\*8.0\*657.

Format: \$\$OR^XLFSHAN(x,y)

Input Parameters: x: (required) An integer of 32 bits or less.

y: (required) An integer of 32 bits or less.

Output: returns: Returns the bitwise logical OR.

#### Example

<span id="_Toc199950835" class="anchor"></span>Figure 2: \$\$OR^XLFSHAN API—Example

\><span class="mark">W \$\$OR^XLFSHAN(345,123)</span>

379

### \$\$XOR^XLFSHAN(): Bitwise Logical XOR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Bitwise Logic Functions

ICR \#: 6157

Description: The \$\$XOR^XLFSHAN extrinsic function performs a bitwise logical XOR of two 32 bit integers.

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/006.png) NOTE: This API was released with Kernel Patch XU\*8.0\*657.

Format: \$\$XOR^XLFSHAN(x,y)

Input Parameters: x: (required) An integer of 32 bits or less.

y: (required) An integer of 32 bits or less.

Output: returns: Returns the bitwise logical XOR.

#### Example

<span id="_Toc199950836" class="anchor"></span>Figure 3: \$\$XOR^XLFSHAN API—Example

\><span class="mark">W \$\$XOR^XLFSHAN(345,123)</span>

290

## CRC Functions—XLFCRC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These functions are provided to help process strings.

### \$\$CRC16^XLFCRC(): Cyclic Redundancy Code 16

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: CRC Functions

ICR \#: 3156

Description: The \$\$CRC16^XLFCRC extrinsic function computes a Cyclic Redundancy Code (CRC) of the 8-bit character string, using the following as the polynomial:

X^16 + X^15 + X^2 + 1

The optional seed input parameter can supply an initial value, which allows for running CRC calculations on multiple strings. If the seed input parameter is *not* specified, a default value of Zero (0) is assumed. The seed value is limited to 0 \<= seed \<= 2^16. The function value is between 0 and 2^16.

Format: \$\$CRC16^XLFCRC(string\[,seed\])

Input Parameters: string: (required) String upon which to compute the CRC16.

seed: (optional) Seed value. Needed to compute the CRC16 over multiple strings.

Output: returns: Returns the Cyclic Redundancy Code (CRC) 16 value.

#### Examples

#### Example 1

SET CRC=\$\$CRC16^XLFCRC(string)

A checksum can also be calculated over multiple strings.

<span id="_Toc199950837" class="anchor"></span>Figure 4: \$\$CRC16^XLFCRC API—Example 1: Calculating a Checksum over Multiple Strings (1 of 2)

SET (I,C)=0FOR SET I=\$ORDER(X(I)) QUIT:'I DO. SET C=\$\$CRC16^XLFCRC(X(I),C)

Or:

<span id="_Toc199950838" class="anchor"></span>Figure 5: \$\$CRC16^XLFCRC API—Example 1: Calculating a Checksum over Multiple Strings (2 of 2)

SET I=0,C=4294967295FOR SET I=\$ORDER(X(I)) QUIT:'I DO. SET C=\$\$CRC16^XLFCRC(X(I),C)

If the save method is used all the time.

#### Example 2

<span id="_Toc199950839" class="anchor"></span>Figure 6: \$\$CRC16^XLFCRC API—Example 2

CRC162 ;Test call CRC16^XLFCRC multiple timesS TEXT="Now is the time for all good children",TEXT2="to come to the aid of their country."S CRC=0,CRC=\$\$CRC16^XLFCRC(TEXT,CRC)If 23166=\$\$CRC16^XLFCRC(TEXT2,CRC) WRITE !,"CRC16 OK"Q

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/007.png) NOTE: These have been approved for inclusion in a future ANSI M language standard as part of the library.

### \$\$CRC32^XLFCRC(): Cyclic Redundancy Code 32

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: CRC Functions

ICR \#: 3156

Description: The \$\$CRC32^XLFCRC extrinsic function computes a Cyclic Redundancy Code (CRC) of the 8-bit character string, using the following as the polynomial:

X^32 + X^26 + X^23 + X^22 + X^16 + X^12 + X^11 + X^10 + X^8 + X^7 + X^5 + X^4 + X^2 + X + 1

The optional seed input parameter can supply an initial value, which allows for running CRC calculations on multiple strings. If the seed input parameter is *not* specified, a default value of 4,294,967,295 (2^32-1) is assumed. The seed value is limited to 0 \<= seed \<= 2^32. The function value is between 0 and 2^32.

Format: \$\$CRC32^XLFCRC(string\[,seed\])

Input Parameters: string: (required) String upon which to compute the CRC32.

seed: (optional) Seed value. Needed to compute the CRC32 over multiple strings.

Output: returns: Returns the Cyclic Redundancy Code (CRC) 32 value.

#### Examples

#### Example 1

SET CRC=\$\$CRC32^XLFCRC(string)

A checksum can also be calculated over multiple strings.

<span id="_Toc199950840" class="anchor"></span>Figure 7: \$\$CRC32^XLFCRC API—Example 1: Calculating a Checksum over Multiple Strings (1 of 2)

SET (I,C)=0FOR SET I=\$ORDER(X(I)) QUIT:'I DO. SET C=\$\$CRC32^XLFCRC(X(I),C)

Or:

<span id="_Toc199950841" class="anchor"></span>Figure 8: \$\$CRC32^XLFCRC API—Example 1: Calculating a Checksum over Multiple Strings (2 of 2)

SET I=0,C=4294967295FOR SET I=\$ORDER(X(I)) QUIT:'I DO. SET C=\$\$CRC32^XLFCRC(X(I),C)

If the save method is used all the time.

#### Example 2

<span id="_Toc199950842" class="anchor"></span>Figure 9: \$\$CRC32^XLFCRC API—Example 2

CRC322 ;Test call CRC32^XLFCRC multiple timesS TEXT="Now is the time for all good children",TEXT2="to come to the aid of their country."S CRC=0,CRC=\$\$CRC32^XLFCRC(TEXT,CRC)If 715820230=\$\$CRC32^XLFCRC(TEXT2,CRC) WRITE !,"CRC32 OK"Q

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/008.png) NOTE: These have been approved for inclusion in a future ANSI M language standard as part of the library.

## Date Functions—XLFDT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \$\$%H^XLFDT(): Convert Seconds to \$H

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Date Functions

ICR \#: 10103

Description: The \$\$%H^XLFDT extrinsic function converts the number of seconds input to a \$H formatted date. It converts the output of the <u>\$\$SEC^XLFDT(): Convert \$H/VA FileMan date to Seconds</u> API back to a \$H value.

Format: \$\$%H^XLFDT(seconds)

Input Parameters: seconds: (required) Input seconds.

Output: returns: Returns seconds in \$H date format.

#### Example

<span id="_Toc199950843" class="anchor"></span>Figure 10: \$\$%H^XLFDT API—Example

\><span class="mark">S X=\$\$%H^XLFDT(5108536020)</span>

\><span class="mark">W X</span>

59126,49620

### \$\$DOW^XLFDT(): Day of Week

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Date Functions

ICR \#: 10103

Description: The \$\$DOW^XLFDT extrinsic function returns the corresponding day of the week from a date in VA FileMan format.

Format: \$\$DOW^XLFD(x\[,y\])

Input Parameters: x: (required) VA FileMan date.

y: (optional) 1 to return a day-of-week number.

Output: returns: Returns the day of the week.

#### Examples

#### Example 1

<span id="_Toc199950844" class="anchor"></span>Figure 11: \$\$DOW^XLFDT API—Example 1

\><span class="mark">S X=\$\$DOW^XLFDT(2901231.111523)</span>

\><span class="mark">W X</span>

Monday

#### Example 2

<span id="_Toc199950845" class="anchor"></span>Figure 12: \$\$DOW^XLFDT API—Example 2

\><span class="mark">S X=\$\$DOW^XLFDT(2901231.111523,1)</span>

\><span class="mark">W X</span>

1

### \$\$DT^XLFDT: Current Date (VA FileMan Date Format)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Date Functions

ICR \#: 10103

Description: The \$\$DT^XLFDT extrinsic function returns the current date in VA FileMan format.

Format: \$\$DT^XLFDT

Input Parameters: none.

Output: returns: Returns the current date in VA FileMan format.

#### Example

<span id="_Toc199950846" class="anchor"></span>Figure 13: \$\$DT^XLFDT API—Example

\><span class="mark">S X=\$\$DT^XLFDT</span>

\><span class="mark">W X</span>

3040126

### \$\$FMADD^XLFDT(): VA FileMan Date Add

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Date Functions

ICR \#: 10103

Description: The \$\$FMADD^XLFDT extrinsic function returns the result of adding days, hours, minutes, and seconds to a date in VA FileMan format.

Format: \$\$FMADD^XLFDT(x,d,h,m,s)

Input Parameters: x: (required) VA FileMan date (in quotes).

d: (required) Days.

h: (required) Hours.

m: (required) Minutes.

s: (required) Seconds.

Output: returns: Returns the updated date and time in VA FileMan format.

#### Example

<span id="_Toc199950847" class="anchor"></span>Figure 14: \$\$FMADD^XLFDT API—Example

\><span class="mark">S X=\$\$FMADD^XLFDT(2901231.01,2,2,20,15)</span>

\><span class="mark">W X</span>

2910102.032015

### \$\$FMDIFF^XLFDT(): VA FileMan Date Difference

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Date Functions

ICR \#: 10103

Description: The \$\$FMDIFF^XLFDT extrinsic function returns the difference between two VA FileMan format dates.

Format: \$\$FMDIFF^XLFDT(x1,x2\[,x3\])

Input Parameters: x1: (required) VA FileMan date.

x2: (required) VA FileMan date, to subtract from the x1 date.

x3: (optional) If NULL,\`\$D(x3), return the difference in days. Otherwise:

- If x3 = 1, return the difference in days.
- If x3 = 2, return the difference in seconds.
- If x3 = 3, return the difference in days hours:minutes:seconds format (DD HH:MM:SS).

Output: returns: Returns the date and/or time difference.

#### Examples

#### Example 1

<u>Figure 15</u> returns the difference between two dates/times in days (x3 = NULL or 1). In this example, the first date is 2 days less than the second date:

<span id="_Ref500773432" class="anchor"></span>Figure 15: \$\$FMDIFF^XLFDT API—Example 1

\><span class="mark">S X=\$\$FMDIFF^XLFDT(2901229,2901231.111523)</span>

\><span class="mark">W X</span>

-2

\><span class="mark">S X=\$\$FMDIFF^XLFDT(2901229,2901231.111523,1)</span>

\><span class="mark">W X</span>

-2

#### Example 2

<u>Figure 16</u> returns the difference between two dates/times in seconds (x3 = 2). In this example, the first date is 150,079 seconds greater than the second date:

<span id="_Ref500773457" class="anchor"></span>Figure 16: \$\$FMDIFF^XLFDT API—Example 2

\><span class="mark">S X=\$\$FMDIFF^XLFDT(2901231.111523,2901229.173404,2)</span>

\><span class="mark">W X</span>

150079

#### Example 3

<u>Figure 17</u> returns the difference between two dates/times in DD HH:MM:SS (x3 = 3). In this example, the first date is 1 day, 1 hour, 24minutes, and 2 seconds greater than the second date:

<span id="_Ref500773478" class="anchor"></span>Figure 17: \$\$FMDIFF^XLFDT API—Example 3

\><span class="mark">S X=\$\$FMDIFF^XLFDT(2901231.024703,2901230.012301,3)</span>

\><span class="mark">W X</span>

1 1:24:2

### \$\$FMTE^XLFDT(): Convert VA FileMan Date to External Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Date Functions

ICR \#: 10103

Description: The \$\$FMTE^XLFDT extrinsic function converts a VA FileMan formatted input date to an external formatted date.

Format: \$\$FMTE^XLFDT(x\[,y\])

Input Parameters: x: (required) VA FileMan date.

y: (optional) Affects output as follows:

- If NULL, \`\$D(y), return the written-out format.
- If \`\$D(y) then return standard VA FileMan format.
- If +y = 1 then return standard VA FileMan format.
- If +y = 2 then return MM/DD/YY@HH:MM:SS format.
- If +y = 3 then return DD/MM/YY@HH:MM:SS format.
- If +y = 4 then return YY/MM/DD@HH:MM:SS format.
- If +y = 5 then return MM/DD/YYYY@HH:MM:SS format.
- If +y = 6 then return DD/MM/YYYY@HH:MM:SS format.
- If +y = 7 then return YYYY/MM/DD@HH:MM:SS format.
- If y contains a D then date only.
- If y contains an F then output date with leading spaces.
- If y contains an M then only output HH:MM.
- If y contains a P then output HH:MM:SS am/pm.
- If y contains an S then force seconds in the output.
- If y contains a Z then output date with leading Zeroes.

Output: returns: Returns the external formatted date.

#### Examples

#### Example 1

Return the date in the following format: Standard VA FileMan date format.

<span id="_Toc199950851" class="anchor"></span>Figure 18: \$\$FMTE^XLFDT API—Example 1: Standard VA FileMan Date Format

\><span class="mark">S X=\$\$FMTE^XLFDT(2940629.105744,1)</span>

\><span class="mark">W X</span>

Jun 29, 1994@10:57:44

#### Example 2

Return the date in the following format: Standard VA FileMan date format and include am/pm.

<span id="_Toc199950852" class="anchor"></span>Figure 19: \$\$FMTE^XLFDT API—Example 2: Standard VA FileMan Date Format and Including am/pm

\><span class="mark">S X=\$\$FMTE^XLFDT(2940629.1057,"1P")</span>

\><span class="mark">W X</span>

Jun 29, 1994 10:57 am

#### Example 3

Return the date in the following format: MM/DD/YY@HH:MM:SS.

<span id="_Toc199950853" class="anchor"></span>Figure 20: \$\$FMTE^XLFDT API—Example 3: MM/DD/YY@HH:MM:SS Format

\><span class="mark">S X=\$\$FMTE^XLFDT(2940629.105744,2)</span>

\><span class="mark">W X</span>

6/29/94@10:57:44

#### Example 4

Return the date in the following format: MM/DD/YY@HH:MM.

<span id="_Toc199950854" class="anchor"></span>Figure 21: \$\$FMTE^XLFDT API—Example 4: MM/DD/YY@HH:MM Format

\><span class="mark">S X=\$\$FMTE^XLFDT(2940629.105744,"2M")</span>

\><span class="mark">W X</span>

6/29/94@10:57

#### Example 5

Return the date in the following format: MM/DD/YY@HH:MM:SS and include am/pm.

<span id="_Toc199950855" class="anchor"></span>Figure 22: \$\$FMTE^XLFDT API—Example 5: MM/DD/YY@HH:MM:SS Format and Including am/pm

\><span class="mark">S X=\$\$FMTE^XLFDT(2940629.105744,"2P")</span>

\><span class="mark">W X</span>

6/29/94 10:57:44 am

#### Example 6

Return the date in the following format: MM/DD/YY@HH:MM:SS, forcing seconds to display when no seconds were included in the input parameter.

<span id="_Toc199950856" class="anchor"></span>Figure 23: \$\$FMTE^XLFDT API—Example 6: MM/DD/YY@HH:MM:SS Format with Forced Seconds Displayed

\><span class="mark">S X=\$\$FMTE^XLFDT(2940629.1057,"2S")</span>

\><span class="mark">W X</span>

6/29/94@10:57:00

#### Example 7

Return the date in the following format: MM/DD/YY@HH:MM:SS, forcing seconds to display when no seconds were included in the input parameter, and include leading spaces.

<span id="_Toc199950857" class="anchor"></span>Figure 24: \$\$FMTE^XLFDT API—Example 7: MM/DD/YY@HH:MM:SS Format Including Leading Spaces and with Forced Seconds Displayed

\><span class="mark">S X=\$\$FMTE^XLFDT(2940629.1057,"2SF")</span>

\><span class="mark">W X</span>

6/29/94@10:57:00

#### Example 8

Return the date in the following format: DD/MM/YY@HH:MM:SS and include leading spaces.

<span id="_Toc199950858" class="anchor"></span>Figure 25: \$\$FMTE^XLFDT API—Example 8: DD/MM/YY@HH:MM:SS Format Including Leading Spaces

\><span class="mark">S X=\$\$FMTE^XLFDT(2940629.105744,"3F")</span>

\><span class="mark">W X</span>

29/ 6/94@10:57:44

#### Example 9

Return the date in the following format: YY/MM/DD, ignore the time values entered and only display the date.

<span id="_Toc199950859" class="anchor"></span>Figure 26: \$\$FMTE^XLFDT API—Example 9: YY/MM/DD Format Ignoring Time Values

\><span class="mark">S X=\$\$FMTE^XLFDT(2940629.1057,"4D")</span>

\><span class="mark">W X</span>

94/6/29

#### Example 10

To output a short DATE/TIME try the following, convert space to Zero and remove slash, as shown in <u>Figure 27</u>:

<span id="_Ref499704278" class="anchor"></span>Figure 27: \$\$FMTE^XLFDT API—Example 10: Short Date/Time Format Converting Spaces to Zeroes and Removing Slashes

\><span class="mark">S X=\$TR(\$\$FMTE^XLFDT(2940629.1057,"4F")," /","0")</span>

\><span class="mark">W X</span>

940629@10:57

#### Example 11

Return the date in the following format: MM/DD/YYYY@HH:MM:SS.

<span id="_Toc199950861" class="anchor"></span>Figure 28: \$\$FMTE^XLFDT API—Example 11: MM/DD/YYYY@HH:MM:SS Format

\><span class="mark">S X=\$\$FMTE^XLFDT(3000229.110520,5)</span>

\><span class="mark">W X</span>

2/29/2000@11:05:20

#### Example 12

Return the date in the following format: MM/DD/YYYY@HH:MM:SS and include leading spaces.

<span id="_Toc199950862" class="anchor"></span>Figure 29: \$\$FMTE^XLFDT API—Example 12: MM/DD/YYYY@HH:MM:SS Format Including Leading Spaces

\><span class="mark">S X=\$\$FMTE^XLFDT(3000229.110520,"5F")</span>

\><span class="mark">W X</span>

2/29/2000@11:05:20

#### Example 13

Return the date in the following format: MM/DD/YYYY@HH:MM:SS, forcing seconds.

<span id="_Toc199950863" class="anchor"></span>Figure 30: \$\$FMTE^XLFDT API—Example 13: MM/DD/YYYY@HH:MM:SS Format Forcing Seconds

\><span class="mark">S X=\$\$FMTE^XLFDT(3000229.1105,"5S")</span>

\><span class="mark">W X</span>

2/29/2000@11:05:00

#### Example 14

Return the date in the following format: MM/DD/YYYY HH:MM:SS, include leading Zeroes and am/pm.

<span id="_Toc199950864" class="anchor"></span>Figure 31: \$\$FMTE^XLFDT API—Example 14: MM/DD/YYYY HH:MM:SS Format Including Leading Zeroes and am/pm

\><span class="mark">S X=\$\$FMTE^XLFDT(3000229.110520,"5ZP")</span>\><span class="mark">W X</span>

02/29/2000 11:05:20 am

#### Example 15

Return the date in the following format: DD/MM/YYYY@HH:MM:SS, with leading spaces.

<span id="_Toc199950865" class="anchor"></span>Figure 32: \$\$FMTE^XLFDT API—Example 15: DD/MM/YYYY@HH:MM:SS Format with Leading Spaces

\><span class="mark">S X=\$\$FMTE^XLFDT(3000229.110520,"6F")</span>

\><span class="mark">W X</span>

29/ 2/2000@11:05:20

#### Example 16

Return the date in the following format: DD/MM/YYYY@HH:MM:SS, with leading Zeroes.

<span id="_Toc199950866" class="anchor"></span>Figure 33: \$\$FMTE^XLFDT API—Example 16: DD/MM/YYYY@HH:MM:SS Format with Leading Zeroes

\><span class="mark">S X=\$\$FMTE^XLFDT(3000229.1105,"6Z")</span>

\><span class="mark">W X</span>

29/02/2000@11:05

#### Example 17

Return the date in the following format: YYYY/MM/DD@HH:MM:SS.

<span id="_Toc199950867" class="anchor"></span>Figure 34: \$\$FMTE^XLFDT API—Example 17: YYYY/MM/DD@HH:MM:SS Format

\><span class="mark">S X=\$\$FMTE^XLFDT(3000301.1105,7)</span>

\><span class="mark">W X</span>

2000/3/1@11:05

#### Example 18

Return the date in the following format: YYYY/MM/DD, ignore the time values entered and only display the date.

<span id="_Toc199950868" class="anchor"></span>Figure 35: \$\$FMTE^XLFDT API—Example 18: YYYY/MM/DD Format Ignoring Time Values

\><span class="mark">S X=\$\$FMTE^XLFDT(3000301.1105,"7D")</span>

\><span class="mark">W X</span>

2000/3/1

### \$\$FMTH^XLFDT(): Convert VA FileMan Date to \$H

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Date Functions

ICR \#: 10103

Description: The \$\$FMTH^XLFDT extrinsic function converts a VA FileMan formatted input date to a \$H formatted date.

Format: \$\$FMTH^XLFDT(x\[,y\])

Input Parameters: x: (required) VA FileMan date.

y: (optional) 1 to return the date portion only (no seconds).

Output: returns: Returns the converted date in \$H format.

#### Examples

#### Example 1

<span id="_Toc199950869" class="anchor"></span>Figure 36: \$\$FMTH^XLFDT API—Example 1

\><span class="mark">S X=\$\$FMTH^XLFDT(2901231.111523)</span>

\><span class="mark">W X</span>

54786,40523

#### Example 2

<span id="_Toc199950870" class="anchor"></span>Figure 37: \$\$FMTH^XLFDT API—Example 2

\><span class="mark">S X=\$\$FMTH^XLFDT(2901231.111523,1)</span>

\><span class="mark">W X</span>

54786

### \$\$FMTHL7^XLFDT(): Convert VA FileMan Date to HL7 Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Date Functions

ICR \#: 10103

Description: The \$\$FMTHL7^XLFDT extrinsic function converts a VA FileMan formatted input DATE/TIME into a Health Level Seven (HL7) formatted date, including the time offset.

Format: \$\$FMTHL7^XLFDT(fm_date_time)

Input Parameters: fm_date_time: (required) VA FileMan date.

Output: returns: Returns the converted date in HL7 format.

#### Example

<span id="_Toc199950871" class="anchor"></span>Figure 38: \$\$FMTHL7^XLFDT API—Example

\><span class="mark">S X=\$\$FMTHL7^XLFDT(3001127.1525)</span>

\><span class="mark">W X</span>

200011271525-0800

### \$\$HADD^XLFDT(): \$H Add

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Date Functions

ICR \#: 10103

Description: The \$\$HADD^XLFDT extrinsic function returns the result of adding days, hours, minutes, and seconds to a date in \$H format.

Format: \$\$HADD^XLFDT(x,d,h,m,s)

Input Parameters: x: (required) \$H date (in quotes).

d: (required) Days.

h: (required) Hours.

m: (required) Minutes.

s: (required) Seconds.

Output: returns: Returns the resultant date in \$H format.

#### Example

<span id="_Toc199950872" class="anchor"></span>Figure 39: \$\$HADD^XLFDT API—Example

\><span class="mark">S X=\$\$HADD^XLFDT("54786,3600",2,2,20,15)</span>

\><span class="mark">W X</span>

54788,12015

### \$\$HDIFF^XLFDT(): \$H Difference

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Date Functions

ICR \#: 10103

Description: The \$\$HDIFF^XLFDT extrinsic function returns the difference between two \$H formatted dates.

Format: \$\$HDIFF^XLFDT(x1,x2\[,x3\])

Input Parameters: x1: (required) \$H date (in quotes).

x2: (required) \$H date (in quotes) to subtract from the x1 date.

x3: (optional) If NULL, \`\$D(x3), return the difference in days. Otherwise:

- If x3 = 1, return the difference in days.
- If x3 = 2, return the difference in seconds.
- If x3 = 3, return the difference in  
  > days hours:minutes:seconds format  
  > (DD HH:MM:SS).

Output: returns: Returns the \$H difference.

#### Examples

#### Example 1

Return the \$H difference in days.

<span id="_Toc199950873" class="anchor"></span>Figure 40: \$\$HDIFF^XLFDT API—Example 1

\><span class="mark">S X=\$\$HDIFF^XLFDT("54789,40523","54786,25983",1)</span>

\><span class="mark">W X</span>

3

#### Example 2

Return the \$H difference in seconds.

<span id="_Toc199950874" class="anchor"></span>Figure 41: \$\$HDIFF^XLFDT API—Example 2

\><span class="mark">S X=\$\$HDIFF^XLFDT("54789,40523","54786,25983",2)</span>

\><span class="mark">W X</span>

273740

#### Example 3

Return the \$H difference in days hours:minutes:seconds format (DD HH:MM:SS).

<span id="_Toc199950875" class="anchor"></span>Figure 42: \$\$HDIFF^XLFDT API—Example 3

\><span class="mark">S X=\$\$HDIFF^XLFDT("54789,40523","54786,25983",3)</span>

\><span class="mark">W X</span>

3 4:02:20

### \$\$HL7TFM^XLFDT(): Convert HL7 Date to VA FileMan Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Date Functions

ICR \#: 10103

Description: The \$\$HL7TFM^XLFDT extrinsic function converts an HL7 formatted input DATE/TIME into a VA FileMan formatted DATE/TIME.

Format: \$\$HL7TFM^XLFDT(hl7_date_time\[,local_uct\]\[,time_flag\])

Input Parameters: hl7_date_time: (required) HL7 formatted date and time.

local_uct: (optional) This parameter controls if any time offset is applied to the time. If a time offset is included, then time offset can be applied to give Local time or Coordinated Universal Time (UTC, aka GMT, or Greenwich Mean Time) time offset from the MAILMAN TIME ZONE (#4.4) file. The default is to return Local time. Valid values are:

- L (default)—Local time.
- U—UTC time.

time_flag: (optional) This parameter is set to 1 if the value in the hl7_date_time input parameter is just a time value. The default assumes that the hl7_date_time input parameter is a date and time value.

Output: returns: Returns the converted date in VA FileMan format.

#### Examples

#### Example 1

To get date with no offset:

<span id="_Toc199950876" class="anchor"></span>Figure 43: \$\$HL7TFM^XLFDT API—Example 1

\><span class="mark">S X=\$\$HL7TFM^XLFDT("200011271525-0700")</span>

\><span class="mark">W X</span>

3001127.1525

#### Example 2

To get UTC time offset:

<span id="_Toc199950877" class="anchor"></span>Figure 44: \$\$HL7TFM^XLFDT API—Example 2

\><span class="mark">S X=\$\$HL7TFM^XLFDT("200011271525-0700","U")</span>

\><span class="mark">W X</span>

3001127.2225

#### Example 3

To get Local time in PST offset:

<span id="_Toc199950878" class="anchor"></span>Figure 45: \$\$HL7TFM^XLFDT API—Example 3

\><span class="mark">S X=\$\$HL7TFM^XLFDT("200011271525-0700","L")</span>

\><span class="mark">W X</span>

3001127.1425

#### Example 4

To get Local time when only providing a time (no date) as the input parameter:

<span id="_Toc199950879" class="anchor"></span>Figure 46: \$\$HL7TFM^XLFDT API—Example 4

\><span class="mark">S X=\$\$HL7TFM^XLFDT("1525-0700","L",1)</span>

\><span class="mark">W X</span>

.1525

### \$\$HTE^XLFDT(): Convert \$H to External Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Date Functions

ICR \#: 10103

Description: The \$\$HTE^XLFDT extrinsic function converts a \$H formatted input date to an external formatted date.

Format: \$\$HTE^XLFDT(x\[,y\])

Input Parameters: x: (required) \$H date (in quotes).

y: (optional) Affects output as follows:

- If NULL,\`\$D(y), return the written-out format.
- If \`\$D(y) then return standard VA FileMan format.
- If +y = 1 then return standard VA FileMan format.
- If +y = 2 then return MM/DD/YY@HH:MM:SS format.
- If +y = 3 then return DD/MM/YY@HH:MM:SS format.
- If +y = 4 then return YY/MM/DD@HH:MM:SS format.
- If +y = 5 then return MM/DD/YYYY@HH:MM:SS format.
- If +y = 6 then return DD/MM/YYYY@HH:MM:SS format.
- If +y = 7 then return YYYY/MM/DD@HH:MM:SS format.
- If y contains a D then date only.
- If y contains an F then output date with leading spaces.
- If y contains an M then output HH:MM only.
- If y contains a P then output HH:MM:SS am/pm.
- If y contains an S then force seconds in the output.
- If y contains a Z then output date with leading Zeroes.

Output: returns: Returns the external format of a \$H date.

#### Examples

#### Example 1

Return the date in the following format: Standard external format.

<span id="_Toc199950880" class="anchor"></span>Figure 47: \$\$HTE^XLFDT API—Example 1

\><span class="mark">S X=\$\$HTE^XLFDT("54786,40523")</span>

\><span class="mark">W X</span>

Dec 31, 1990@11:15:23

#### Example 2

Return the date in the following format: MM/DD/YY@HH:MM:SS.

<span id="_Toc199950881" class="anchor"></span>Figure 48: \$\$HTE^XLFDT API—Example 2

\><span class="mark">S X=\$\$HTE^XLFDT("54786,40523",2)</span>

\><span class="mark">W X</span>

12/31/90@11:15:23

#### Example 3

Return the date in the following format: MM/DD/YY@HH:MM:SS, omitting the seconds.

<span id="_Toc199950882" class="anchor"></span>Figure 49: \$\$HTE^XLFDT API—Example 3

\><span class="mark">S X=\$\$HTE^XLFDT("57386,33723","2M")</span>

\><span class="mark">W X</span>

2/12/98@09:22

#### Example 4

Return the date in the following format: MM/DD/YYYY@HH:MM:SS.

<span id="_Toc199950883" class="anchor"></span>Figure 50: \$\$HTE^XLFDT API—Example 4

\><span class="mark">S X=\$\$HTE^XLFDT("57351,27199",5)</span>

\><span class="mark">W X</span>

1/8/1998@07:33:19

#### Example 5

Return the date in the following format: DD/MM/YYYY@HH:MM:SS.

<span id="_Toc199950884" class="anchor"></span>Figure 51: \$\$HTE^XLFDT API—Example 5

\><span class="mark">S X=\$\$HTE^XLFDT("57351,27199",6)</span>

\><span class="mark">W X</span>

8/1/1998@07:33:19

#### Example 6

Return the date in the following format: YYYY/MM/DD@HH:MM:SS.

<span id="_Toc199950885" class="anchor"></span>Figure 52: \$\$HTE^XLFDT API—Example 6

\><span class="mark">S X=\$\$HTE^XLFDT("57351,27199",7)</span>

\><span class="mark">W X</span>

1998/1/8@07:33:19

### \$\$HTFM^XLFDT(): Convert \$H to VA FileMan Date Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Date Functions

ICR \#: 10103

Description: The \$\$HTFM^XLFDT extrinsic function converts a \$H formatted input date to a VA FileMan formatted date.

Format: \$\$HTFM^XLFDT(x\[,y\])

Input Parameters: x: (required) \$H date (in quotes).

y: (optional) 1 to return the date portion only (no seconds).

Output: returns: Returns the converted \$H date in VA FileMan format.

#### Examples

#### Example 1

<span id="_Toc199950886" class="anchor"></span>Figure 53: \$\$HTFM^XLFDT API—Example 1

\><span class="mark">S X=\$\$HTFM^XLFDT("54786,40523")</span>

\><span class="mark">W X</span>

2901231.111523

#### Example 2

<span id="_Toc199950887" class="anchor"></span>Figure 54: \$\$HTFM^XLFDT API—Example 2

\><span class="mark">S X=\$\$HTFM^XLFDT("54786,40523",1)</span>

\><span class="mark">W X</span>

2901231

### \$\$NOW^XLFDT: Current Date and Time (VA FileMan Format)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Date Functions

ICR \#: 10103

Description: The \$\$NOW^XLFDT extrinsic function returns the current date and time in VA FileMan format.

Format: \$\$NOW^XLFDT

Input Parameters: none.

Output: returns: Returns the current date and time in VA FileMan format.

#### Example

<span id="_Toc199950888" class="anchor"></span>Figure 55: \$\$NOW^XLFDT API—Example

\>S X=\$\$NOW^XLFDT

\>W X

3040126.103044

### \$\$SCH^XLFDT(): Next Scheduled Runtime

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Date Functions

ICR \#: 10103

Description: The \$\$SCH^XLFDT extrinsic function returns the next run-time based on Schedule code.

Format: \$\$SCH^XLFDT(schedule_string,base_date\[,force_future_flag\])

Input Parameters: schedule_string: (required) Interval to add to base_date, as follows:

- *n*S—Add *n* seconds to base_date.
- *n*H—Add *n* hours to base_date.
- *n*D—Add *n* days to base_date.
- *n*M—Add *n* months to base_date.
- \$H;\$H;\$H—List of \$H dates.
- *n*M(list)—Complex month increment. For example: 1M(15,L), which means schedule it to run every month (1M) on the 15 and last day of the month (15,L).
- dd\[@time\]—Day of month (such as 12).
- *n*Day\[@time\]—day of week in month (such as 1M, first Monday); (see “[Day Code](#day_code)” list that follows).
- Day.
- L—Last day of month.
- LDay—Last specific day in month (such as LM \[last Monday\], LT \[last Tuesday\], LW \[last Wednesday\]...).
- Day\[@time\]—Day of week (see “[Day Code](#day_code)” list that follows).
- Day.
- D—Every weekday.
- E—Every weekend day (Saturday, Sunday).
- <span id="day_code" class="anchor"></span>Day Code (used in schedule codes above):
- M—Monday
- T—Tuesday
- W—Wednesday
- R—Thursday
- F—Friday
- S—Saturday
- U—Sunday

base_date: (required) VA FileMan date to which the interval is added.

force_future_flag: (optional) If passed with a value of:

- 1—Forces returned date to be in future, by repeatedly adding interval to base_date until a future date is produced.
- Otherwise—Interval is added once.

Output: returns: Returns the next run-time.

#### Examples

#### Example 1

To schedule something to run every month on the 15<sup>th</sup> of the month at 2:00 p.m. and on the last day of every month at 6:00 p.m., you would enter the following:

- Middle of the Month:

> <span id="_Toc199950889" class="anchor"></span>Figure 56: \$\$SCH^XLFDT API\$\$SCH^XLFDT API—Example 1: Middle of the Month

> \><span class="mark">S X=\$\$SCH^XLFDT("1M(15@2PM,L@6PM)",2931003)</span>

> \><span class="mark">W X</span>

> 2931015.14

- End of the Month:

> <span id="_Toc199950890" class="anchor"></span>Figure 57: \$\$SCH^XLFDT API\$\$SCH^XLFDT API—Example 1: End of the Month

> \><span class="mark">S X=\$\$SCH^XLFDT("1M(15@2PM,L@6PM)",X)</span>

> \><span class="mark">W X</span>

> 2931031.18

#### Example 2

To schedule something to run every month on the 15<sup>th</sup> of the month at 11:00 p.m. and on the last day of every month at 8:00 p.m., you would enter the following:

- Middle of the Month:

> <span id="_Toc199950891" class="anchor"></span>Figure 58: \$\$SCH^XLFDT API\$\$SCH^XLFDT API—Example 2: Middle of the Month

> \><span class="mark">S X=\$\$SCH^XLFDT("1M(15@11PM,L@8PM)",2931028)</span>

> \><span class="mark">W X</span>

> 2931031.2

- End of the Month:

> <span id="_Toc199950892" class="anchor"></span>Figure 59: \$\$SCH^XLFDT API\$\$SCH^XLFDT API—Example 2: End of the Month

> \><span class="mark">S X=\$\$SCH^XLFDT("1M(15@11PM,L@8PM)",X)</span>

> \><span class="mark">W X</span>

> 2931115.23

#### Example 3

To schedule something to run every 3 months on the last day of the month at 6:00 p.m., you would enter the following:

- Middle of the Month:

> <span id="_Toc199950893" class="anchor"></span>Figure 60: \$\$SCH^XLFDT API\$\$SCH^XLFDT API—Example 3: Middle of the Month

> \><span class="mark">S X=\$\$SCH^XLFDT("3M(L@6PM)",2930927)</span>

> \><span class="mark">W X</span>

> 2930930.18

- End of the Month:

> <span id="_Toc199950894" class="anchor"></span>Figure 61: \$\$SCH^XLFDT API\$\$SCH^XLFDT API—Example 3: End of the Month

> \><span class="mark">S X=\$\$SCH^XLFDT("3M(L@6PM)",X)</span>

> \><span class="mark">W X</span>

> 2931231.18

#### Example 4

The \$\$SCH^XLFDT API can return a date that is closer to the date the API is run if the user does *not* use the force_future_flag parameter and the base_date parameter is set to a date in the past. In this example, the base_date parameter is set to a date in the past, 11/17/2014 at 8:00, and the interval is set to find the date 2 months out on the second Monday of the month. The date that is returned is the date that the API was run, 1/12/2015, which happens to be the second Monday of the month and two months out from the base_date.

<span id="_Toc199950895" class="anchor"></span>Figure 62: \$\$SCH^XLFDT API—Example 4: Not Using Future flag

\><span class="mark">S X=\$\$SCH^XLFDT("2M(2M@0800)",3141117.0800)</span>

\><span class="mark">W X</span>

3150112.08

If using the force_future_flag parameter to the API, using the same interval as above, the API forces the return date to be a date in the future from the date the API is run.

<span id="_Toc199950896" class="anchor"></span>Figure 63: \$\$SCH^XLFDT API—Example 4: Using Future Flag

\><span class="mark">S X=\$\$SCH^XLFDT("2M(2M@0800)",3141117.0800,1)</span>

\><span class="mark">W X</span>

3150309.08

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/009.png) NOTE: The base_date *must* be passed correctly. The base_date parameter is compared to the schedule_string parameter in the interval to return the correct output.

### \$\$SEC^XLFDT(): Convert \$H/VA FileMan date to Seconds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Date Functions

ICR \#: 10103

Description: The \$\$SEC^XLFDT extrinsic function converts a \$H or VA FileMan formatted input date to the number of seconds. The input date can be entered as either a VA FileMan date or a \$H date. If entered as a VA FileMan date, the date is first converted to \$H through the <u>\$\$FMTH^XLFDT(): Convert VA FileMan Date to \$H</u> API.

Format: \$\$SEC^XLFDT(x)

Input Parameters: x: (required) VA FileMan or \$H date.

Output: returns: Returns the \$H date in seconds.

#### Examples

#### Example 1

Inputting a VA FileMan DATE/TIME:

<span id="_Toc199950897" class="anchor"></span>Figure 64: \$\$SEC^XLFDT—Example 1

\><span class="mark">S X=\$\$SEC^XLFDT(3021118.1347)</span>

\><span class="mark">W X</span>

5108536020

#### Example 2

Inputting a \$H date:

<span id="_Toc199950898" class="anchor"></span>Figure 65: \$\$SEC^XLFDT—Example 2

\><span class="mark">S X=\$\$SEC^XLFDT(\$H)</span>

\><span class="mark">W X</span>

5146022146

### \$\$TZ^XLFDT: Time Zone Offset (GMT)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Date Functions

ICR \#: 10103

Description: The \$\$TZ^XLFDT extrinsic function returns the Time Zone offset from Greenwich mean time (GMT) based on a POINTER from the TIME ZONE (#1) field in the MAILMAN SITE PARAMETERS (#4.3) file to the MAILMAN TIME ZONE (#4.4) file.

The accuracy of this value is dependent on system administrators updating the TIME ZONE (#1) field in the MAILMAN SITE PARAMETERS (#4.3) file to accurately point to the site’s correct time zone, including whether it is standard time (ST) or daylight savings time (DST).

Format: \$\$TZ^XLFDT

Input Parameters: none.

Output: returns: Returns the Time Zone offset from GMT.

#### Example

For Pacific Daylight Savings Time (PDT), the offset from GMT is:

<span id="_Toc199950899" class="anchor"></span>Figure 66: \$\$TZ^XLFDT—Example

\><span class="mark">S X = \$\$TZ^XLFDT</span>

\><span class="mark">W X</span>

-0700

### \$\$WITHIN^XLFDT(): Checks Dates/Times within Schedule

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Date Functions

ICR \#:Description: The \$\$WITHIN^XLFDT extrinsic function returns whether a DATE/TIME is within a specified schedule string.

Format: \$\$WITHIN^XLFDT(schedule_string,base_date)

Input Parameters: schedule_string: (required) Interval to add to base_date.

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/010.png) REF: For alternate values, see the <u>\$\$SCH^XLFDT(): Next Scheduled Runtime</u> API.

base_date: (required) VA FileMan date checked to determine if it is within the input schedule_string.

Output: returns: Returns whether a DATE/TIME is within a specified schedule string.

## Hyperbolic Trigonometric Functions—XLFHYPER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following hyperbolic trigonometric functions provide an additional set of mathematical operations beyond the math functions in XLFMTH.

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/011.png) NOTE: The optional second parameter in brackets \[ \] denotes the precision for the function. Precision means the detail of the result, in terms of number of digits.

### \$\$ACOSH^XLFHYPER(): Hyperbolic Arc-Cosine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Hyperbolic Trigonometric Functions

ICR \#: 10144

Description: The \$\$ACOSH^XLFHYPER extrinsic function returns the hyperbolic arc cosine, with radians output.

Format: \$\$ACOSH^XLFHYPER(x\[,n\])

Input Parameters: x: (required) Number for which you want the hyperbolic arc cosine.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the hyperbolic arc cosine.

#### Example

<span id="_Toc199950900" class="anchor"></span>Figure 67: \$\$ACOSH^XLFHYPER API—Example

\><span class="mark">S X=\$\$ACOSH^XLFHYPER(3,12)</span>

\><span class="mark">W X</span>

1.762747174

### \$\$ACOTH^XLFHYPER(): Hyperbolic Arc-Cotangent

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Hyperbolic Trigonometric Functions

ICR \#: 10144

Description: The \$\$ACOTH^XLFHYPER extrinsic function returns the hyperbolic arc cotangent, with radians output.

Format: \$\$ACOTH^XLFHYPER(x\[,n\])

Input Parameters: x: (required) Number for which you want the hyperbolic arc cotangent.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the hyperbolic arc cotangent.

#### Example

<span id="_Toc199950901" class="anchor"></span>Figure 68: \$\$ACOTH^XLFHYPER API—Example

\><span class="mark">S X=\$\$ACOTH^XLFHYPER(3,12)</span>

\><span class="mark">W X</span>

.34657359025

### \$\$ACSCH^XLFHYPER(): Hyperbolic Arc-Cosecant

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Hyperbolic Trigonometric Functions

ICR \#: 10144

Description: The \$\$ACSCH^XLFHYPER extrinsic function returns the hyperbolic arc cosecant, with radians output.

Format: \$\$ACSCH^XLFHYPER(x\[,n\])

Input Parameters: x: (required) Number for which you want the hyperbolic arc cosecant.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the hyperbolic arc cosecant.

#### Example

<span id="_Toc199950902" class="anchor"></span>Figure 69: \$\$ACSCH^XLFHYPER API—Example

\><span class="mark">S X=\$\$ACSCH^XLFHYPER(3,12)</span>

\><span class="mark">W X</span>

.3274501502

### \$\$ASECH^XLFHYPER(): Hyperbolic Arc-Secant

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Hyperbolic Trigonometric Functions

ICR \#: 10144

Description: The \$\$ASECH^XLFHYPER extrinsic function returns the hyperbolic arc secant, with radians output.

Format: \$\$ASECH^XLFHYPER(x\[,n\])

Input Parameters: x: (required) Number for which you want the hyperbolic arc secant.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the hyperbolic arc secant.

#### Example

<span id="_Toc199950903" class="anchor"></span>Figure 70: \$\$ASECH^XLFHYPER API—Example

\><span class="mark">S X=\$\$ASECH^XLFHYPER(.3,12)</span>

\><span class="mark">W X</span>

1.8738202425

### \$\$ASINH^XLFHYPER(): Hyperbolic Arc-Sine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Hyperbolic Trigonometric Functions

ICR \#: 10144

Description: The \$\$ASINH^XLFHYPER extrinsic function returns the hyperbolic arc sine, with radians output.

Format: \$\$SINH^XLFHYPER(x\[,n\])

Input Parameters: x: (required) Number for which you want the hyperbolic arc sine.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the hyperbolic arc sine.

#### Example

<span id="_Toc199950904" class="anchor"></span>Figure 71: \$\$ASINH^XLFHYPER API—Example

\><span class="mark">S X=\$\$SINH^XLFHYPER(3,12)</span>

\><span class="mark">W X</span>

10.0178749273

### \$\$ATANH^XLFHYPER(): Hyperbolic Arc-Tangent

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Hyperbolic Trigonometric Functions

ICR \#: 10144

Description: The \$\$ATANH^XLFHYPER extrinsic function returns the hyperbolic arc tangent, with radians output.

Format: \$\$ATANH^XLFHYPER(x\[,n\])

Input Parameters: x: (required) Number for which you want the hyperbolic arc tangent.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the hyperbolic arc tangent.

#### Example

<span id="_Toc199950905" class="anchor"></span>Figure 72: \$\$ATANH^XLFHYPER API—Example

\><span class="mark">S X=\$\$ATANH^XLFHYPER(.3,12)</span>

\><span class="mark">W X</span>

.3095196042

### \$\$COSH^XLFHYPER(): Hyperbolic Cosine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Hyperbolic Trigonometric Functions

ICR \#: 10144

Description: The \$\$COSH^XLFHYPER extrinsic function returns the hyperbolic arc cosine, with radians output.

Format: \$\$COSH^XLFHYPER(x\[,n\])

Input Parameters: x: (required) Number for which you want the hyperbolic cosine.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the hyperbolic cosine.

#### Example

<span id="_Toc199950906" class="anchor"></span>Figure 73: \$\$COSH ^XLFHYPER API—Example

\><span class="mark">S X=\$\$COSH^XLFHYPER(3,12)</span>

\><span class="mark">W X</span>

10.0676619957

### \$\$COTH^XLFHYPER(): Hyperbolic Cotangent

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Hyperbolic Trigonometric Functions

ICR \#: 10144

Description: The \$\$COTH^XLFHYPER extrinsic function returns the hyperbolic cotangent, with radians output.

Format: \$\$COTH^XLFHYPER(x\[,n\])

Input Parameters: x: (required) Number for which you want the hyperbolic cotangent.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the hyperbolic cotangent.

#### Example

<span id="_Toc199950907" class="anchor"></span>Figure 74: \$\$COTH^XLFHYPER API—Example

\><span class="mark">S X=\$\$COTH^XLFHYPER(3,12)</span>

\><span class="mark">W X</span>

1.00496982332

### \$\$CSCH^XLFHYPER(): Hyperbolic Cosecant

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Hyperbolic Trigonometric Functions

ICR \#: 10144

Description: The \$\$CSCH^XLFHYPER extrinsic function returns the hyperbolic cosecant, with radians output.

Format: \$\$CSCH^XLFHYPER(x\[,n\])

Input Parameters: x: (required) Number for which you want the hyperbolic cosecant.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the hyperbolic cosecant.

#### Example

<span id="_Toc199950908" class="anchor"></span>Figure 75: \$\$CSCH^XLFHYPER API—Example

\><span class="mark">S X=\$\$CSCH^XLFHYPER(3,12)</span>

\><span class="mark">W X</span>

.09982156967

### \$\$SECH^XLFHYPER(): Hyperbolic Secant

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Hyperbolic Trigonometric Functions

ICR \#: 10144

Description: The \$\$SECH^XLFHYPER extrinsic function returns the hyperbolic secant, with radians output.

Format: \$\$SECH^XLFHYPER(x\[,n\])

Input Parameters: x: (required) Number for which you want the hyperbolic secant.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the hyperbolic secant.

#### Example

<span id="_Toc199950909" class="anchor"></span>Figure 76: \$\$SECH^XLFHYPER API—Example

\><span class="mark">S X=\$\$SECH^XLFHYPER(3,12)</span>

\><span class="mark">W X</span>

.09932792742

### \$\$SINH^XLFHYPER(): Hyperbolic Sine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Hyperbolic Trigonometric Functions

ICR \#: 10144

Description: The \$\$SINH^XLFHYPER extrinsic function returns the hyperbolic sine, with radians output.

Format: \$\$SINH^XLFHYPER(x\[,n\])

Input Parameters: x: (required) Number for which you want the hyperbolic sine.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the hyperbolic sine.

#### Examples

#### Example 1

<span id="_Toc199950910" class="anchor"></span>Figure 77: \$\$SINH^XLFHYPER API—Example 1

\><span class="mark">S X=\$\$SINH^XLFHYPER(.707)</span>

\><span class="mark">W X</span>

.767388542

#### Example 2

<span id="_Toc199950911" class="anchor"></span>Figure 78: \$\$SINH^XLFHYPER API—Example 2

\><span class="mark">S X=\$\$SINH^XLFHYPER(.3,12)</span>

\><span class="mark">W X</span>

.30452029345

### \$\$TANH^XLFHYPER(): Hyperbolic Tangent

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Hyperbolic Trigonometric Functions

ICR \#: 10144

Description: The \$\$TANH^XLFHYPER extrinsic function returns the hyperbolic tangent of x (TAN x = SIN x/COS x), with radians output.

Format: \$\$TANH^XLFHYPER(x\[,n\])

Input Parameters: x: (required) Number for which you want the hyperbolic tangent.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the hyperbolic tangent.

#### Example

<span id="_Toc199950912" class="anchor"></span>Figure 79: \$\$TANH^XLFHYPER API—Example

\><span class="mark">S X=\$\$TANH^XLFHYPER(3,12)</span>

\><span class="mark">W X</span>

.99505475368

## Mathematical Functions—XLFMTH

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These calls are provided as an enhancement to what is offered in standard M. In addition, extended math functions provide mathematical operations with adjustable and higher precision. Additional trigonometric functions are available. Angles can be specified either in decimal format or in degrees:minutes:seconds.

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/012.png) NOTE: Each optional parameter in brackets \[ \] denotes the maximum and default precision for the function. Precision means the detail of the result, in terms of number of digits.

### \$\$ABS^XLFMTH(): Absolute Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$ABS^XLFMTH extrinsic function returns the absolute value of the number in x.

Format: \$\$ABS^XLFMTH(x)

Input Parameters: x: (required) Number for which you want the absolute value.

Output: returns: Returns the absolute value of a number.

#### Example

<span id="_Toc199950913" class="anchor"></span>Figure 80: \$\$ABS^XLFMTH API—Example

\><span class="mark">S X=\$\$ABS^XLFMTH(-42.45)</span>

\><span class="mark">W X</span>

42.45

### \$\$ACOS^XLFMTH(): Arc-Cosine (Radians)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$ACOS^XLFMTH extrinsic function returns the arc cosine, with radians output.

Format: \$\$ACOS^XLFMTH(x\[,n\])

Input Parameters: x: (required) Number for which you want the arc cosine in radians.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the arc cosine of a number output in radians.

#### Example

<span id="_Toc199950914" class="anchor"></span>Figure 81: \$\$ACOS^XLFMTH API—Example

\><span class="mark">S X=\$\$ACOS^XLFMTH(.5)</span>

\><span class="mark">W X</span>

1.047197551

### \$\$ACOSDEG^XLFMTH(): Arc-Cosine (Degrees)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$ACOSDEG^XLFMTH extrinsic function returns the arc cosine, with degrees output.

Format: \$\$ACOSDEG^XLFMTH(x\[,n\])

Input Parameters: x: (required) Number for which you want the arc cosine in degrees.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the arc cosine of a number output in degrees.

#### Example

<span id="_Toc199950915" class="anchor"></span>Figure 82: \$\$ACOSDEG^XLFMTH API—Example

\><span class="mark">S X=\$\$ACOSDEG^XLFMTH(.5)</span>

\><span class="mark">W X</span>

60

### \$\$ACOT^XLFMTH(): Arc-Cotangent (Radians)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$ACOT^XLFMTH extrinsic function returns the arc cotangent, with radians output.

Format: \$\$ACOT^XLFMTH(x\[,n\])

Input Parameters: x: (required) Number for which you want the arc cotangent in radians.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the arc cotangent of a number output in radians.

#### Example

<span id="_Toc199950916" class="anchor"></span>Figure 83: \$\$ACOT^XLFMTH API—Example

\><span class="mark">S X=\$\$ACOT^XLFMTH(.5)</span>

\><span class="mark">W X</span>

1.107148718

### \$\$ACOTDEG^XLFMTH(): Arc-Cotangent (Degrees)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$ACOTDEG^XLFMTH extrinsic function returns the arc cotangent, with degrees output.

Format: \$\$ACOTDEG^XLFMTH(x\[,n\])

Input Parameters: x: (required) Number for which you want the arc cotangent in degrees.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the arc cotangent of a number output in degrees.

#### Example

<span id="_Toc199950917" class="anchor"></span>Figure 84: \$\$ACOTDEG^XLFMTH API—Example

\><span class="mark">S X=\$\$ACOTDEG^XLFMTH(.5)</span>

\><span class="mark">W X</span>

63.43494882

### \$\$ACSC^XLFMTH(): Arc-Cosecant (Radians)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$ACSC^XLFMTH extrinsic function returns the arc cosecant, with radians output.

Format: \$\$ACSC^XLFMTH(x\[,n\])

Input Parameters: x: (required) Number for which you want the arc cosecant in radians.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the arc cosecant of a number output in radians.

#### Example

<span id="_Toc199950918" class="anchor"></span>Figure 85: \$\$ACSC^XLFMTH API—Example

\><span class="mark">S X=\$\$ACSC^XLFMTH(1.5)</span>

\><span class="mark">W X</span>

.729727656

### \$\$ACSCDEG^XLFMTH(): Arc-Cosecant (Degrees)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$ACSCDEG^XLFMTH extrinsic function returns the arc cosecant, with degrees output.

Format: \$\$ACSCDEG^XLFMTH(x\[,n\])

Input Parameters: x: (required) Number for which you want the arc cosecant in degrees.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the arc cosecant of a number output in degrees.

#### Example

<span id="_Toc199950919" class="anchor"></span>Figure 86: \$\$ACSCDEG^XLFMTH API—Example

\><span class="mark">S X=\$\$ACSCDEG^XLFMTH(1.5)</span>

\><span class="mark">W X</span>

41.8103149

### \$\$ASEC^XLFMTH(): Arc-Secant (Radians)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$ASEC^XLFMTH extrinsic function returns the arc secant, with radians output.

Format: \$\$ASEC^XLFMTH(x\[,n\])

Input Parameters: x: (required) Number for which you want the arc secant in radians.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the arc secant of a number output in radians.

#### Example

<span id="_Toc199950920" class="anchor"></span>Figure 87: \$\$ASEC^XLFMTH API—Example

\><span class="mark">S X=\$\$ASEC^XLFMTH(1.5)</span>

\><span class="mark">W X</span>

.841068671

### \$\$ASECDEG^XLFMTH(): Arc-Secant (Degrees)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$ASECDEG^XLFMTH extrinsic function returns the arc secant, with degrees output.

Format: \$\$ASECDEG^XLFMTH(x\[,n\])

Input Parameters: x: (required) Number for which you want the arc secant in degrees.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the arc secant of a number output in degrees.

#### Example

<span id="_Toc199950921" class="anchor"></span>Figure 88: \$\$ASECDEG^XLFMTH API—Example

\><span class="mark">S X=\$\$ASECDEG^XLFMTH(1.5)</span>

\><span class="mark">W X</span>

48.1896851

### \$\$ASIN^XLFMTH(): Arc-Sine (Radians)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$ASIN^XLFMTH extrinsic function returns the arc sine, with radians output.

Format: \$\$ASIN^XLFMTH(x\[,n\])

Input Parameters: x: (required) Number for which you want the arc sine in radians.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the arc sine of a number output in radians.

#### Example

<span id="_Toc199950922" class="anchor"></span>Figure 89: \$\$ASIN^XLFMTH API—Example

\><span class="mark">S X=\$\$ASIN^XLFMTH(.5)</span>

\><span class="mark">W X</span>

.523598776

### \$\$ASINDEG^XLFMTH(): Arc-Sine (Degrees)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$ASINDEG^XLFMTH extrinsic function returns the arc sine, with degrees output.

Format: \$\$ASINDEG^XLFMTH(x\[,n\])

Input Parameters: x: (required) Number for which you want the arc sine in degrees.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the arc sine of a number output in degrees.

#### Example

<span id="_Toc199950923" class="anchor"></span>Figure 90: \$\$ASINDEG^XLFMTH API—Example

\><span class="mark">S X=\$\$ASINDEG^XLFMTH(.5)</span>

\><span class="mark">W X</span>

30

### \$\$ATAN^XLFMTH(): Arc-Tangent (Radians)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$ATAN^XLFMTH extrinsic function returns the arc tangent, with radians output.

Format: \$\$ATAN^XLFMTH(x\[,n\])

Input Parameters: x: (required) Number for which you want the arc tangent in radians.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the arc tangent of a number output in radians.

#### Example

<span id="_Toc199950924" class="anchor"></span>Figure 91: \$\$ATAN^XLFMTH API—Example

\><span class="mark">S X=\$\$ATAN^XLFMTH(.5)</span>

\><span class="mark">W X</span>

.463647609

### \$\$ATANDEG^XLFMTH(): Arc-Tangent (Degrees)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$ATANDEG^XLFMTH extrinsic function returns the arc tangent, with degrees output.

Format: \$\$ATANDEG^XLFMTH(x\[,n\])

Input Parameters: x: (required) Number for which you want the arc tangent in degrees.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the arc tangent of a number output in degrees.

#### Example

<span id="_Toc199950925" class="anchor"></span>Figure 92: \$\$ATANDEG^XLFMTH API—Example

\><span class="mark">S X=\$\$ATANDEG^XLFMTH(.5)</span>

\><span class="mark">W X</span>

26.56505118

### \$\$COS^XLFMTH(): Cosine (Radians)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$COS^XLFMTH extrinsic function returns the cosine, with radians input.

Format: \$\$COS^XLFMTH(x\[,n\])

Input Parameters: x: (required) Radians input number for which you want the cosine.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the cosine of radians input number.

#### Example

<span id="_Toc199950926" class="anchor"></span>Figure 93: \$\$COS^XLFMTH API—Example

\><span class="mark">S X=\$\$COS^XLFMTH(1.5)</span>

\><span class="mark">W X</span>

.070737202

### \$\$COSDEG^XLFMTH(): Cosine (Degrees)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$COSDEG^XLFMTH extrinsic function returns the cosine, with degrees input.

Format: \$\$COSDEG^XLFMTH(x\[,n\])

Input Parameters: x: (required) Degrees input number for which you want the cosine.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the cosine of degrees input number.

#### Example

<span id="_Toc199950927" class="anchor"></span>Figure 94: \$\$COSDEG^XLFMTH API—Example

\><span class="mark">S X=\$\$COSDEG^XLFMTH(45)</span>

\><span class="mark">W X</span>

.707106781

### \$\$COT^XLFMTH(): Cotangent (Radians)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$COT^XLFMTH extrinsic function returns the cotangent, with radians input.

Format: \$\$COT^XLFMTH(x\[,n\])

Input Parameters: x: (required) Radians input number for which you want the cotangent.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the cotangent of radians input number.

#### Example

<span id="_Toc199950928" class="anchor"></span>Figure 95: \$\$COT^XLFMTH API—Example

\><span class="mark">S X=\$\$COT^XLFMTH(1.5)</span>

\><span class="mark">W X</span>

.070914844

### \$\$COTDEG^XLFMTH(): Cotangent (Degrees)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$COTDEG^XLFMTH extrinsic function returns the cotangent, with degrees input.

Format: \$\$COTDEG^XLFMTH(x\[,n\])

Input Parameters: x: (required) Degrees input number for which you want the cotangent.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the cotangent of degrees input number.

#### Example

<span id="_Toc199950929" class="anchor"></span>Figure 96: \$\$COTDEG^XLFMTH API—Example

\><span class="mark">S X=\$\$COTDEG^XLFMTH(45)</span>

\><span class="mark">W X</span>

1

### \$\$CSC^XLFMTH(): Cosecant (Radians)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$CSC^XLFMTH extrinsic function returns the cosecant, with radians input.

Format: \$\$CSC^XLFMTH(x\[,n\])

Input Parameters: x: (required) Radians input number for which you want the cosecant.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the cosecant of radians input number.

#### Example

<span id="_Toc199950930" class="anchor"></span>Figure 97: \$\$CSC^XLFMTH API—Example

\><span class="mark">S X=\$\$CSC^XLFMTH(1.5)</span>

\><span class="mark">W X</span>

1.002511304

### \$\$CSCDEG^XLFMTH(): Cosecant (Degrees)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$CSCDEG^XLFMTH extrinsic function returns the cosecant, with degrees input.

Format: \$\$CSCDEG^XLFMTH(x\[,n\])

Input Parameters: x: (required) Degrees input number for which you want the cosecant.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the cosecant of degrees input number.

#### Example

<span id="_Toc199950931" class="anchor"></span>Figure 98: \$\$CSCDEG^XLFMTH API—Example

\><span class="mark">S X=\$\$CSCDEG^XLFMTH(45)</span>

\><span class="mark">W X</span>

1.414213562

### \$\$DECDMS^XLFMTH(): Convert Decimals to Degrees:Minutes:Seconds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$DECDMS^XLFMTH extrinsic function converts a number from decimal to degrees:minutes:seconds.

Format: \$\$DECDMS^XLFMTH(x\[,n\])

Input Parameters: x: (required) Decimal number to be converted to degree:minutes:seconds.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the converted decimal input number to degrees:minutes:seconds.

#### Example

<span id="_Toc199950932" class="anchor"></span>Figure 99: \$\$DECDMS^XLFMTH API—Example

\><span class="mark">S X=\$\$DECDMS^XLFMTH(30.7)</span>

\><span class="mark">W X</span>

30:42:0

### \$\$DMSDEC^XLFMTH(): Convert Degrees:Minutes:Seconds to Decimal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$DMSDEC^XLFMTH extrinsic function converts a number from degrees:minutes:seconds to a decimal.

Format: \$\$DMSDEC^XLFMTH(x\[,n\])

Input Parameters: x: (required) Degrees:minutes:seconds input number to be converted to decimal.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the converted degrees:minutes:seconds input number to decimal.

#### Example

<span id="_Toc199950933" class="anchor"></span>Figure 100: \$\$DMSDEC^XLFMTH API—Example

\><span class="mark">S X=\$\$DMSDEC^XLFMTH("30:42:0")</span>

\><span class="mark">W X</span>

30.7

### \$\$DTR^XLFMTH(): Convert Degrees to Radians

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$DTR^XLFMTH extrinsic function converts degrees to radians.

Format: \$\$DTR^XLFMTH(x\[,n\])

Input Parameters: x: (required) Degrees input number to be converted to radians.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the converted degrees input number to radians.

#### Example

<span id="_Toc199950934" class="anchor"></span>Figure 101: \$\$DTR^XLFMTH API—Example

\><span class="mark">S X=\$\$DTR^XLFMTH(45)</span>

\><span class="mark">W X</span>

.7853981634

### \$\$E^XLFMTH(): e—Natural Logarithm

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$E^XLFMTH extrinsic function returns e (natural logarithm).

Format: \$\$E^XLFMTH(\[n\])

Input Parameters: n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns e, natural logarithm.

#### Example

<span id="_Toc199950935" class="anchor"></span>Figure 102: \$\$E^XLFMTH API—Example

\><span class="mark">S X=\$\$E^XLFMTH(12)</span>

\><span class="mark">W X</span>

2.71828182846

### \$\$EXP^XLFMTH(): e—Natural Logarithm to the Nth Power

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$EXP^XLFMTH extrinsic function returns e (natural logarithm) to the x power (exponent).

Format: \$\$EXP^XLFMTH(x\[,n\])

Input Parameters: x: (required) The power to which you want e raised.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the value of e to the specified power.

#### Example

<span id="_Toc199950936" class="anchor"></span>Figure 103: \$\$EXP^XLFMTH API—Example

\><span class="mark">S X=\$\$EXP^XLFMTH(1.532)</span>

\><span class="mark">W X</span>

4.6274224185

### \$\$LN^XLFMTH(): Natural Log (Base e)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$LN^XLFMTH extrinsic function returns the natural log of x (Base e).

Format: \$\$LN^XLFMTH(x\[,n\])

Input Parameters: x: (required) Number for which you want the natural log.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the natural log of a number.

#### Example

<span id="_Toc199950937" class="anchor"></span>Figure 104: \$\$LN^XLFMTH API—Example

\><span class="mark">S X=\$\$LN^XLFMTH(4.627426)</span>

\><span class="mark">W X</span>

1.532000774

### \$\$LOG^XLFMTH(): Logarithm (Base 10)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$LOG^XLFMTH extrinsic function returns the logarithm (Base 10) of x.

Format: \$\$LOG^XLFMTH(x\[,n\])

Input Parameters: x: (required) Number for which you want the logarithm.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the logarithm (Base 10) of input number.

#### Example

<span id="_Toc199950938" class="anchor"></span>Figure 105: \$\$LOG^XLFMTH API—Example

\><span class="mark">S X=\$\$LOG^XLFMTH(3.1415)</span>

\><span class="mark">W X</span>

.4971370641

### \$\$MAX^XLFMTH(): Maximum of Two Numbers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$MAX^XLFMTH extrinsic function returns the maximum value by comparing the number in x with the number in y.

Format: \$\$MAX^XLFMTH(x,y)

Input Parameters: x: (required) First number to compare with second number in y to determine which is higher in value.

y: (required) Second number to compare with first number in x to determine which is higher in value.

Output: returns: Returns the highest number.

#### Example

<span id="_Toc199950939" class="anchor"></span>Figure 106: \$\$MAX^XLFMTH API—Example

\><span class="mark">S X=\$\$MAX^XLFMTH(53,24)</span>

\><span class="mark">W X</span>

53

### \$\$MIN^XLFMTH(): Minimum of Two Numbers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$MIN^XLFMTH extrinsic function returns the minimum value by comparing the number in x with the number in y.

Format: \$\$MIN^XLFMTH(x,y)

Input Parameters: x: (required) First number to compare with second number in y to determine which is lower in value.

y: (required) Second number to compare with first number in x to determine which is lower in value.

Output: returns: Returns the lowest number.

#### Example

<span id="_Toc199950940" class="anchor"></span>Figure 107: \$\$MIN^XLFMTH API—Example

\><span class="mark">S X=\$\$MIN^XLFMTH(53,24)</span>

\><span class="mark">W X</span>

24

### \$\$PI^XLFMTH(): PI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$PI^XLFMTH extrinsic function returns pi.

Format: \$\$PI^XLFMTH(\[n\])

Input Parameters: n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns pi.

#### Example

<span id="_Toc199950941" class="anchor"></span>Figure 108: \$\$PI^XLFMTH API—Example

\><span class="mark">S X=\$\$PI^XLFMTH(12)</span>

\><span class="mark">W X</span>

3.14159265359

### \$\$PWR^XLFMTH(): X to the Y Power

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$PWR^XLFMTH extrinsic function returns x to the y power. This function makes use of LN and EXP.

Format: \$\$PWR^XLFMTH(x,y\[,n\])

Input Parameters: x: (required) Number for which you want the exponent value.

y: (required) The exponent to which the input number (x) should be raised.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the exponent value.

#### Example

<span id="_Toc199950942" class="anchor"></span>Figure 109: \$\$PWR^XLFMTH API—Example

\><span class="mark">S X=\$\$PWR^XLFMTH(3.2,1.5)</span>

\><span class="mark">W X</span>

5.7243340224

### \$\$RTD^XLFMTH(): Convert Radians to Degrees

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$RTD^XLFMTH extrinsic function converts radians to degrees.

Format: \$\$RTD^XLFMTH(x\[,n\])

Input Parameters: x: (required) Radians input number to be converted to degrees.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the converted radians input number to degrees.

#### Example

<span id="_Toc199950943" class="anchor"></span>Figure 110: \$\$RTD^XLFMTH API—Example

\><span class="mark">S X=\$\$RTD^XLFMTH(1.5,12)</span>

\><span class="mark">W X</span>

85.9436692696

### \$\$SD^XLFMTH(): Standard Deviation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$SD^XLFMTH extrinsic function returns the standard deviation. Standard deviation is defined as:

“A measure of variability equal to the square root of the arithmetic average of the squares of the deviations from the mean in a frequency distribution.”[^2]

Format: \$\$SD^XLFMTH(%s1,%s2,%n)

Input Parameters: %s1: (required) Sum.

%s2: (required) Sum of squares.

%n: (required) Count.

Output: returns: Returns the standard deviation.

#### Example

<span id="_Toc199950944" class="anchor"></span>Figure 111: \$\$SD^XLFMTH API—Example

\><span class="mark">S X=\$\$SD^XLFMTH(5,25,2)</span>

\><span class="mark">W X</span>

3.53553390593

### \$\$SEC^XLFMTH(): Secant (Radians)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$SEC^XLFMTH extrinsic function returns the secant of a number, with radians input.

Format: \$\$SEC^XLFMTH(x\[,n\])

Input Parameters: x: (required) Number in radians for which you want the secant.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the secant of radians input number.

#### Example

<span id="_Toc199950945" class="anchor"></span>Figure 112: \$\$SEC^XLFMTH API—Example

\><span class="mark">S X=\$\$SEC^XLFMTH(1.5)</span>

\><span class="mark">W X</span>

14.1368329

### \$\$SECDEG^XLFMTH(): Secant (Degrees)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$SECDEG^XLFMTH extrinsic function returns the secant of a number, with degrees input.

Format: \$\$SECDEG^XLFMTH(x\[,n\])

Input Parameters: x: (required) Number in degrees for which you want the secant.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the secant of degrees input number.

#### Example

<span id="_Toc199950946" class="anchor"></span>Figure 113: \$\$SECDEG^XLFMTH API—Example

\><span class="mark">S X=\$\$SECDEG^XLFMTH(45)</span>

\><span class="mark">W X</span>

1.414213562

### \$\$SIN^XLFMTH(): Sine (Radians)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$SIN^XLFMTH extrinsic function returns the sine of a number, with radians input.

Format: \$\$SIN^XLFMTH(x\[,n\])

Input Parameters: x: (required) Number in radians for which you want the sine.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the sine of radians input number.

#### Example

<span id="_Toc199950947" class="anchor"></span>Figure 114: \$\$SIN^XLFMTH API—Example

\><span class="mark">S X=\$\$SIN^XLFMTH(.7853982)</span>

\><span class="mark">W X</span>

.707106807

### \$\$SINDEG^XLFMTH(): Sine (Degrees)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$SINDEG^XLFMTH extrinsic function returns the sine of a number, with degrees input.

Format: \$\$SINDEG^XLFMTH(x\[,n\])

Input Parameters: x: (required) Number in degrees for which you want the sine.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the sine of degrees input number.

#### Example

<span id="_Toc199950948" class="anchor"></span>Figure 115: \$\$SINDEG^XLFMTH API—Example

\><span class="mark">S X=\$\$SINDEG^XLFMTH(45)</span>

\><span class="mark">W X</span>

.707106781

### \$\$SQRT^XLFMTH(): Square Root

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$SQRT^XLFMTH extrinsic function returns the square root of a number.

Format: \$\$SQRT^XLFMTH(x\[,n\])

Input Parameters: x: (required) Number for which you want the square root.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the square root of input number.

#### Example

<span id="_Toc199950949" class="anchor"></span>Figure 116: \$\$SQRT^XLFMTH API—Example

\><span class="mark">S X=\$\$SQRT^XLFMTH(153)</span>

\><span class="mark">W X</span>

12.3693168769

### \$\$TAN^XLFMTH(): Tangent (Radians)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$TAN^XLFMTH extrinsic function returns the tangent of a number  
(TAN x = SIN x/COS x), with radians input.

Format: \$\$TAN^XLFMTH(x\[,n\])

Input Parameters: x: (required) Number in radians for which you want the tangent.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the tangent of radians input number.

#### Example

<span id="_Toc199950950" class="anchor"></span>Figure 117: \$\$TAN^XLFMTH API—Example

\><span class="mark">S X=\$\$TAN^XLFMTH(.7853982)</span>

\><span class="mark">W X</span>

1.000000073

### \$\$TANDEG^XLFMTH(): Tangent (Degrees)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Math Functions

ICR \#: 10105

Description: The \$\$TANDEG^XLFMTH extrinsic function returns the tangent of a number, with degrees input.

Format: \$\$TANDEG^XLFMTH(x\[,n\])

Input Parameters: x: (required) Number in degrees for which you want the tangent.

n: (optional) The precision for the function. Precision means the detail of the result, in terms of number of digits.

Output: returns: Returns the tangent of degrees input number.

#### Example

<span id="_Toc199950951" class="anchor"></span>Figure 118: \$\$TANDEG^XLFMTH API—Example

\><span class="mark">S X=\$\$TANDEG^XLFMTH(45)</span>

\><span class="mark">W X</span>

1

## Measurement Functions—XLFMSMT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine contains APIs to allow conversion between U.S. (English) and Metric units.

### \$\$BSA^XLFMSMT(): Body Surface Area Measurement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Measurement Functions

ICR \#: 3175 and 10143

Description: The \$\$BSA^XLFMSMT extrinsic function returns the body surface area.

Format: \$\$BSA^XLFMSMT(ht,wt)

Input Parameters: ht: (required) Height in centimeters.

wt: (required) Weight in kilograms.

Output: returns: Returns the body surface area measurement.

#### Examples

#### Example 1

<span id="_Toc199950952" class="anchor"></span>Figure 119: \$\$BSA^XLFMSMT API—Example 1

\><span class="mark">S X=\$\$BSA^XLFMSMT(175,86)</span>

\><span class="mark">W X</span>

2.02

#### Example 2

<span id="_Toc199950953" class="anchor"></span>Figure 120: \$\$BSA^XLFMSMT API—Example 2

\><span class="mark">S X=\$\$BSA^XLFMSMT(\$\$LENGTH^XLFMSMT(69,"IN","CM"),\$\$WEIGHT^XLFMSMT(180,"LB","KG"))</span>

\><span class="mark">W X</span>

1.98

### \$\$LENGTH^XLFMSMT(): Convert Length Measurement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Measurement Functions

ICR \#: 3175 and 10143

Description: The \$\$LENGTH^XLFMSMT extrinsic function converts U.S. length to Metric length and vice versa. It returns the equivalent value with units.

Format: \$\$LENGTH^XLFMSMT(value,from,to)

Input Parameters: value: (required) A positive NUMERIC value.

from: (required) Unit of measure of the value input parameter (see <u>Table 1</u>).

to: (required) Unit of measure to which the value input parameter is converted (see <u>Table 1</u>).

Valid units in either uppercase or lowercase are:

| Metric             | US            |
|--------------------|---------------|
| km—kilometers  | mi—miles  |
| m—meters       | yd—yards  |
| cm—centimeters | ft—feet   |
| mm—millimeters | in—inches |

<span id="_Ref200268653" class="anchor"></span>Table 2: \$\$TEMP^XLFMSMT API—Valid Units

Output: returns: Returns the length measurement.

#### Examples

#### Example 1

Converting U.S. length to Metric length:

<span id="_Toc199950954" class="anchor"></span>Figure 121: \$\$LENGTH^XLFMSMT API—Example 1

\><span class="mark">S X=\$\$LENGTH^XLFMSMT(12,"IN","CM")</span>

\><span class="mark">W X</span>

30.48 CM

#### Example 2

Converting Metric length to U.S. length:

<span id="_Toc199950955" class="anchor"></span>Figure 122: \$\$LENGTH^XLFMSMT API—Example 2

\><span class="mark">S X=\$\$LENGTH^XLFMSMT(30.48,"cm","in")</span><span class="mark">\>W X</span>

12 IN

### \$\$TEMP^XLFMSMT(): Convert Temperature Measurement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Measurement Functions

ICR \#: 3175 and 10143

Description: The \$\$TEMP^XLFMSMT extrinsic function converts U.S. temperature to Metric temperature and vice versa. It returns the equivalent value with units.

Format: \$\$TEMP^XLFMSMT(value,from,to)

Input Parameters: value: (required) A positive NUMERIC value.

from: (required) Unit of measure of the value input parameter (see <u>Table 2</u>).

to: (required) Unit of measure to which the value input parameter is converted (see <u>Table 2</u>).

Valid units in either uppercase or lowercase are:

| Metric    | US           |
|-----------|--------------|
| C—Celsius | F—Fahrenheit |

<span id="_Ref200270071" class="anchor"></span>Table 3: \$\$VOLUME^XLFMSMT API—Valid Units

Output: returns: Returns the temperature measurement.

#### Examples

#### Example 1

Converting Fahrenheit to Celsius:

<span id="_Toc199950956" class="anchor"></span>Figure 123: \$\$TEMP^XLFMSMT API—Example 1: Converting Fahrenheit to Celsius

\><span class="mark">S X=\$\$TEMP^XLFMSMT(72,"F","C")</span>

\><span class="mark">W X</span>

22.222 C

#### Example 2

Converting Celsius to Fahrenheit:

<span id="_Toc199950957" class="anchor"></span>Figure 124: \$\$TEMP^XLFMSMT API—Example 2: Converting Celsius to Fahrenheit

\><span class="mark">S X=\$\$TEMP^XLFMSMT(0,"c","f")</span>

\><span class="mark">W X</span>

32 F

### \$\$VOLUME^XLFMSMT(): Convert Volume Measurement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Measurement Functions

ICR \#: 3175 and 10143

Description: The \$\$VOLUME^XLFMSMT extrinsic function converts U.S. volume to Metric volume and vice versa. Converts milliliters to cubic inches or quarts or ounces. It returns the equivalent value with units.

Format: \$\$VOLUME^XLFMSMT(value,from,to)

Input Parameters: value: (required) A positive NUMERIC value.

from: (required) Unit of measure of the value input parameter (see <u>Table 3</u>).

to: (required) Unit of measure to which the value input parameter is converted (see <u>Table 3</u>).

Valid units in either uppercase or lowercase are:

| Metric        | US            |
|---------------|---------------|
| kl— kiloliter | cf—cubic feet |
| hl—hectoliter | ci—cubic inch |
| dal—dekaliter | gal—gallon    |
| l—liters      | qt—quart      |
| dl—deciliter  | pt—pint       |
| cl—centiliter | c—cup         |
| ml—milliliter | oz— ounce     |

<span id="_Ref200269373" class="anchor"></span>Table 4: \$\$WEIGHT^XLFMSMT API—Valid Units

Output: returns: Returns the volume measurement.

#### Examples

#### Example 1

Converting U.S. volume to Metric volume:

<span id="_Toc199950958" class="anchor"></span>Figure 125: \$\$VOLUME^XLFMSMT API—Example 1

\><span class="mark">S X=\$\$VOLUME^XLFMSMT(12,"CF","ML")</span>

\><span class="mark">W X</span>

339800.832 ML

#### Example 2

Converting Metric volume to U.S. volume:

<span id="_Toc199950959" class="anchor"></span>Figure 126: \$\$VOLUME^XLFMSMT API—Example 2

\><span class="mark">S X=\$\$VOLUME^XLFMSMT(339800.832,"ml","cf")</span>

\><span class="mark">W X</span>

11.998 CF

### \$\$WEIGHT^XLFMSMT(): Convert Weight Measurement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Measurement Functions

ICR \#: 3175 and 10143

Description: The \$\$WEIGHT^XLFMSMT extrinsic function converts U.S. weights to proximate Metric weights and vice versa. It returns the equivalent value with units.

Format: \$\$WEIGHT^XLFMSMT(value,from,to)

Input Parameters: value: (required) A positive NUMERIC value.

from: (required) Unit of measure of the value input parameter (see <u>Table 4</u>).

to: (required) Unit of measure to which the value input parameter is converted (see <u>Table 4</u>).

Valid units in either uppercase or lowercase are:

| Metric        | US        |
|---------------|-----------|
| t—metric tons | tn— tons  |
| kg—kilograms  | lb—pounds |
| g—grams       | oz—ounces |
| mg—milligram  | gr—grain  |

Output: returns: Returns the weight measurement.

#### Examples

#### Example 1

Converting U.S. weight to Metric weight:

<span id="_Toc199950960" class="anchor"></span>Figure 127: \$\$WEIGHT^XLFMSMT API—Example 1

\><span class="mark">S X=\$\$WEIGHT^XLFMSMT(12,"LB","G")</span>

\><span class="mark">W X</span>

5448 G

#### Example 2

Converting Metric weight to U.S. weight:

<span id="_Toc199950961" class="anchor"></span>Figure 128: \$\$WEIGHT^XLFMSMT API—Example 2

\><span class="mark">S X=\$\$WEIGHT^XLFMSMT(5448,"g","lb")</span>

\><span class="mark">W X</span>

12.011 LB

## String Functions—XLFSTR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These functions are provided to help process strings.

### \$\$CJ^XLFSTR(): Center Justify String

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: String Functions

ICR \#: 10104

Description: The \$\$CJ^XLFSTR extrinsic function returns a center justified character string.

Format: \$\$CJ^XLFSTR(s,i\[,p\])

Input Parameters: s: (required) Character string.

i: (required) Field size. If this second parameter contains a trailing T, this extrinsic function returns the output truncated to the field size specified.

p: (optional) Pad character.

Output: returns: Returns the Center justified string.

#### Examples

#### Example 1

<span id="_Toc199950962" class="anchor"></span>Figure 129: \$\$CJ^XLFSTR API—Example 1

\><span class="mark">W "\[",\$\$CJ^XLFSTR("SUE",10),"\]"</span>

\[ SUE \]

#### Example 2

<span id="_Toc199950963" class="anchor"></span>Figure 130: \$\$CJ^XLFSTR API—Example 2

\><span class="mark">W "\[",\$\$CJ^XLFSTR("SUE",10,"-"),"\]"</span>

\[---SUE----\]

#### Example 3

<span id="_Toc199950964" class="anchor"></span>Figure 131: \$\$CJ^XLFSTR API—Example 3

\><span class="mark">W \$\$CJ^XLFSTR("123456789",5)</span>

123456789

#### Example 4

<span id="_Toc199950965" class="anchor"></span>Figure 132: \$\$CJ^XLFSTR API—Example 4

\><span class="mark">W \$\$CJ^XLFSTR(123456789,"5T")</span>

12345

### \$\$INVERT^XLFSTR(): Invert String

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: String Functions

ICR \#: 10104

Description: The \$\$INVERT^XLFSTR extrinsic function returns an inverted string. It inverts the order of the characters in a string.

Format: \$\$INVERT^XLFSTR(x)

Input Parameters: x: (required) Character string.

Output: returns: Returns the inverted string.

#### Example

<span id="_Toc199950966" class="anchor"></span>Figure 133: \$\$INVERT^XLFSTR API—Example

\><span class="mark">S X=\$\$INVERT^XLFSTR("ABC")</span>

\><span class="mark">W X</span>

CBA

### \$\$LJ^XLFSTR(): Left Justify String

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: String Functions

ICR \#: 10104

Description: The \$\$LJ^XLFSTR extrinsic function returns a left justified character string.

Format: \$\$LJ^XLFSTR(s,i\[,p\])

Input Parameters: s: (required) Character string.

i: (required) Field size. If this second parameter contains a trailing T, this extrinsic function returns the output truncated to the field size specified.

p: (optional) Pad character.

Output: returns: Returns the left justified string.

#### Examples

#### Example 1

<span id="_Toc199950967" class="anchor"></span>Figure 134: \$\$LJ^XLFSTR API—Example 1

\><span class="mark">W "\[",\$\$LJ^XLFSTR("TOM",10),"\]"</span>

\[TOM \]

#### Example 2

<span id="_Toc199950968" class="anchor"></span>Figure 135: \$\$LJ^XLFSTR API—Example 2

\><span class="mark">W "\[",\$\$LJ^XLFSTR("TOM",10,"-"),"\]"</span>

\[TOM-------\]

#### Example 3

<span id="_Toc199950969" class="anchor"></span>Figure 136: \$\$LJ^XLFSTR API—Example 3

\><span class="mark">W \$\$LJ^XLFSTR("123456789",5)</span>

123456789

#### Example 4

<span id="_Toc199950970" class="anchor"></span>Figure 137: \$\$LJ^XLFSTR API—Example 4

\><span class="mark">W \$\$LJ^XLFSTR(123456789,"5T")</span>

12345

### \$\$LOW^XLFSTR(): Convert String to Lowercase

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: String Functions

ICR \#: 10104

Description: The \$\$LOW^XLFSTR extrinsic function returns an input string converted to all lowercase.

Format: \$\$LOW^XLFSTR(x)

Input Parameters: x: (required) Character string.

Output: returns: Returns the input string converted to all lowercase.

#### Example

<span id="_Toc199950971" class="anchor"></span>Figure 138: \$\$LOW^XLFSTR API—Example

\><span class="mark">S X=\$\$LOW^XLFSTR("JUSTICE")</span>

\><span class="mark">W X</span>

justice

### \$\$REPEAT^XLFSTR(): Repeat String

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: String Functions

ICR \#: 10104

Description: The \$\$REPEAT^XLFSTR extrinsic function returns a string that repeats the value of x for y number of times.

Format: \$\$REPEAT^XLFSTR(x\[,y\])

Input Parameters: x: (required) Character string to be repeated.

y: (optional) Number of times to repeat the string in x.

Output: returns: Returns the repeated string.

#### Examples

#### Example 1

<span id="_Toc199950972" class="anchor"></span>Figure 139: \$\$REPEAT^XLFSTR API—Example 1

\><span class="mark">S X=\$\$REPEAT^XLFSTR("-",10)</span>

<span class="mark">\>W X</span>

----------

#### Example 2

<span id="_Toc199950973" class="anchor"></span>Figure 140: \$\$REPEAT^XLFSTR API—Example 2

\><span class="mark">S X=\$\$REPEAT^XLFSTR("blue water ",5)</span>

\><span class="mark">W X</span>

blue water blue water blue water blue water blue water

### \$\$REPLACE^XLFSTR(): Replace Strings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: String Functions

ICR \#: 10104

Description: The \$\$REPLACE^XLFSTR extrinsic function uses a multi-character \$Translate to return a string with the specified string replaced.

Format: \$\$REPLACE^XLFSTR(in,.spec)

Input Parameters: in: (required) Input string.

.spec: (required) An array passed by reference.

Output: returns: Returns the replaced string.

#### Examples

#### Example 1

<span id="_Toc199950974" class="anchor"></span>Figure 141: \$\$REPLACE^XLFSTR API—Example 1

\><span class="mark">SET spec("aa")="a",spec("pqr")="alabama"</span>

\><span class="mark">S X=\$\$REPLACE^XLFSTR("aaaaaaqraaaaaaa",.spec)</span>

\><span class="mark">W X</span>

aaaaalabamaaaaa

#### Example 2

<span id="_Toc199950975" class="anchor"></span>Figure 142: \$\$REPLACE^XLFSTR API—Example 2

\><span class="mark">SET spec("F")="VA File",spec("M")="Man"</span>

\><span class="mark">S X=\$\$REPLACE^XLFSTR("FM",.spec)</span>

\><span class="mark">W X</span>

VA FileMan

### \$\$RJ^XLFSTR(): Right Justify String

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: String Functions

ICR \#: 10104

Description: The \$\$RJ^XLFSTR extrinsic function returns a right justified character string.

Format: \$\$RJ^XLFSTR(s,i\[,p\])

Input Parameters: s: (required) Character string.

i: (required) Field size. If this second parameter contains a trailing T, this extrinsic function returns the output truncated to the field size specified.

p: (optional) Pad character.

Output: returns: Returns the right justified string.

#### Examples

#### Example 1

<span id="_Toc199950976" class="anchor"></span>Figure 143: \$\$RJ^XLFSTR API—Example 1

\><span class="mark">W "\[",\$\$RJ^XLFSTR("TOM",10),"\]"</span>

\[ TOM\]

#### Example 2

<span id="_Toc199950977" class="anchor"></span>Figure 144: \$\$RJ^XLFSTR API—Example 2

\><span class="mark">W "\[",\$\$RJ^XLFSTR("TOM",10,"-"),"\]"</span>

\[-------TOM\]

#### Example 3

<span id="_Toc199950978" class="anchor"></span>Figure 145: \$\$RJ^XLFSTR API—Example 3

\><span class="mark">W \$\$RJ^XLFSTR("123456789",5)</span>

123456789

#### Example 4

<span id="_Toc199950979" class="anchor"></span>Figure 146: \$\$RJ^XLFSTR API—Example 4

\><span class="mark">W \$\$RJ^XLFSTR(123456789,"5T")</span>

12345

### \$\$SENTENCE^XLFSTR(): Convert String to Sentence Case

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: String Functions

ICR \#: 10104

Description: The \$\$SENTENCE^XLFSTR extrinsic function returns an input string converted to Sentence case. The initial character of each sentence in the input string is capitalized and the remaining characters in that sentence are returned as all lowercase. The first character of the string begins a sentence. Subsequent sentences are identified as beginning after any of the following:

- Period (.)
- Exclamation point (!)
- Question mark (?)

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/013.png) NOTE: This API was released with Kernel Patch XU\*8.0\*400.

Format: \$\$SENTENCE^XLFSTR(x)

Input Parameters: x: (required) Character string.

Output: returns: Returns the string converted to Sentence case format.

#### Example

<span id="_Toc199950980" class="anchor"></span>Figure 147: \$\$SENTENCE^XLFSTR API—Example

\><span class="mark">S X=\$\$SENTENCE^XLFSTR("HELLO WORLD!!! THIS IS A CAPITALIZED SENTENCE. this is not.")</span>

\><span class="mark">W X</span>

Hello world!!! This is a capitalized sentence. This is not.

### \$\$STRIP^XLFSTR(): Strip a String

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: String Functions

ICR \#: 10104

Description: The \$\$STRIP^XLFSTR extrinsic function returns a string stripped of all instances of a specified character.

Format: \$\$STRIP^XLFSTR(x,y)

Input Parameters: x: (required) Character string.

y: (required) The character to strip out of the string.

Output: returns: Returns the string stripped of specified character.

#### Examples

#### Example 1

<span id="_Toc199950981" class="anchor"></span>Figure 148: \$\$STRIP^XLFSTR API—Example 1

\><span class="mark">S X=\$\$STRIP^XLFSTR("hello","e")</span>

\><span class="mark">W X</span>

hllo

#### Example 2

<span id="_Toc199950982" class="anchor"></span>Figure 149: \$\$STRIP^XLFSTR API—Example 2

\><span class="mark">S X=\$\$STRIP^XLFSTR("Mississippi","i")</span>

\><span class="mark">W X</span>

Msssspp

### \$\$TITLE^XLFSTR(): Convert String to Title Case

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: String Functions

ICR \#: 10104

Description: The \$\$TITLE^XLFSTR extrinsic function returns an input string converted to Title case:

- The initial letter of the first block of characters (that is word) in the input string is capitalized and the remaining characters of that first word are returned as all lowercase.
- Also, the initial letter of any subsequent word in the input string is capitalized and the remaining characters in that word are returned as all lowercase.
- A word is identified when it is preceded by at least one space, except for the first word in the string.

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/014.png) NOTE: This API was released with Kernel Patch XU\*8.0\*400.

Format: \$\$TITLE^XLFSTR(x)

Input Parameters: x: (required) Character string.

Output: returns: Returns the string converted to Title case format.

#### Example

<span id="_Toc199950983" class="anchor"></span>Figure 150: \$\$TITLE^XLFSTR API—Example

\><span class="mark">S X=\$\$TITLE^XLFSTR("HELLO WORLD!!! THIS IS A title-form SENTENCE. so is this.")</span>

\><span class="mark">W X</span>

Hello World!!! This Is A Title-form Sentence. So Is This.

### \$\$TRIM^XLFSTR(): Trim String

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: String Functions

ICR \#: 10104

Description: The \$\$TRIM^XLFSTR extrinsic function trims spaces or other specified characters from the left, right, or both ends of an input string.

Format: \$\$TRIM^XLFSTR(s\[,f\]\[,c\])

Input Parameters: s: (required) Character string.

f: (optional) This flag can have the following value:

- LR (default)—Trim characters from both ends of the string.
- L—Trim characters from the left/beginning of the string.
- R—Trim characters from the right/end of the string.

c: (optional) Set this parameter to the character to trim from the input string. This parameter defaults to a space.

Output: returns: Returns the trimmed string.

#### Examples

#### Example 1

In <u>Figure 151</u>, we are trimming the spaces from both the left and right end of the string (the brackets are added to more clearly display the trimmed string):

<span id="_Ref501035587" class="anchor"></span>Figure 151: \$\$TRIM^XLFSTR API—Example 1

\><span class="mark">S X="\["\_\$\$TRIM^XLFSTR(" A B C ")\_"\]"</span>

<span class="mark">\>W X</span>

\[A B C\]

The second input parameter defaults to LR and the third input parameter defaults to spaces.

#### Example 2

In <u>Figure 152</u>, we are trimming the slashes from both the left and right end of the string (the brackets are added to more clearly display the trimmed string):

<span id="_Ref501035601" class="anchor"></span>Figure 152: \$\$TRIM^XLFSTR API—Example 2

\><span class="mark">S X="\["\_\$\$TRIM^XLFSTR("//A B C//",,"/")\_"\]"</span>

\><span class="mark">W X</span>

\[A B C\]

The second input parameter defaults to LR.

#### Example 3

In <u>Figure 153</u>, we are trimming the slashes from the left end of the string (the brackets are added to more clearly display the trimmed string):

<span id="_Ref501035612" class="anchor"></span>Figure 153: \$\$TRIM^XLFSTR API—Example 3

\><span class="mark">S X="\["\_\$\$TRIM^XLFSTR("//A B C//","L","/")\_"\]"</span>

\><span class="mark">W X</span>

\[A B C//\]

#### Example 4

In <u>Figure 154</u>, we are trimming the slashes from the right end of the string (the brackets are added to more clearly display the trimmed string):

<span id="_Ref501035623" class="anchor"></span>Figure 154: \$\$TRIM^XLFSTR API—Example 4

\><span class="mark">S X="\["\_\$\$TRIM^XLFSTR("//A B C//","r","/")\_"\]"</span>

\><span class="mark">W X</span>

\[//A B C\]

### \$\$UP^XLFSTR(): Convert String to Uppercase

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: String Functions

ICR \#: 10104

Description: The \$\$UP^XLFSTR extrinsic function returns an input string converted to all uppercase.

Format: \$\$UP^XLFSTR(x)

Input Parameters: x: (required) Character string.

Output: returns: Returns the string converted to all uppercase.

#### Example

<span id="_Toc199950988" class="anchor"></span>Figure 155: \$\$UP^XLFSTR API—Example

\><span class="mark">S X=\$\$UP^XLFSTR("freedom")</span>

\><span class="mark">W X</span>

FREEDOM

## Utility Functions—XLFUTL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These functions are provided to help with a variety of tasks.

### \$\$BASE^XLFUTL(): Convert Between Two Bases

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Utility Functions

ICR \#: 2622

Description: The \$\$BASE^XLFUTL extrinsic function converts a number from one base to another. The base *must* be between 2 and 16, both from and to parameters.

Format: \$\$B ASE^XLFUTL(n,from,to)

Input Parameters: n: (required) Number to convert.

from: (required) Base of number being converted.

to: (required) Base to which the number is to be converted.

Output: returns: Returns the converted number from one base to another.

#### Examples

#### Example 1

<span id="_Toc199950989" class="anchor"></span>Figure 156: \$\$BASE^XLFUTL API—Example 1

\><span class="mark">S X=\$\$BASE^XLFUTL(1111,2,16)</span>

\><span class="mark">W X</span>

F

#### Example 2

<span id="_Toc199950990" class="anchor"></span>Figure 157: \$\$BASE^XLFUTL API—Example 2

\><span class="mark">S X=\$\$BASE^XLFUTL(15,10,16)</span>

\><span class="mark">W X</span>

F

#### Example 3

<span id="_Toc199950991" class="anchor"></span>Figure 158: \$\$BASE^XLFUTL API—Example 3

\><span class="mark">S X=\$\$BASE^XLFUTL("FF",16,10)</span>

\><span class="mark">W X</span>

255

### \$\$CCD^XLFUTL(): Append Check Digit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Utility Functions

ICR \#: 2622

Description: The \$\$CCD^XLFUTL extrinsic function returns a number appended with a computed check digit. To check if the original number corresponds with the appended check digit, use the <u>\$\$VCD^XLFUTL(): Verify Integrity</u> API.

Format: \$\$CCD^XLFUTL(x)

Input Parameters: x: (required) Integer for which the check digit is computed.

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/015.png) REF: See “The Taylor Report” in Computerworld magazine, 1975, for the algorithm.

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/016.png) NOTE: This Check Digit algorithm is considered obsolete. Developers are advised to consider other alternatives to validate data integrity. Alternatives include using:

- AES Encryption/Decryption: [\$\$AESENCR^XUSHSH](#aesencr_xushsh) and [\$\$AESDECR^XUSHSH](#aesdecr_xushsh).
- Secure Hash Algorithm (SHA) hashing: [\$\$SHAHASH^XUSHSH](#shahash_xushsh) or [\$\$SHAN^XLFSHAN](#shan_xlfshan) for strings.
- Other SHA hash APIs can be used to validate data integrity for:  
  files: [\$\$FILE^XLFSHAN](#file_xlfshan) or [\$\$HOSTFILE^XLFSHAN](#hostfile_xlfshan);  
  routines: [\$\$ROUTINE^XLFSHAN](#routine_xlfshan); globals: [\$\$GLOBAL^XLFSHAN](#global_xlfshan);  
  and messages: [\$\$LSHAN^XLFSHAN](#lshan_xlfshan).

Output: returns: Returns the number with appended check digit.

#### Examples

#### Example 1

<span id="_Toc199950992" class="anchor"></span>Figure 159: \$\$CCD^XLFUTL API—Example 1

\><span class="mark">S X=\$\$CCD^XLFUTL(99889)</span>

\><span class="mark">W X</span>

998898

#### Example 2

<span id="_Toc199950993" class="anchor"></span>Figure 160: \$\$CCD^XLFUTL API—Example 2

\><span class="mark">S X=\$\$CCD^XLFUTL(7654321)</span>

\><span class="mark">W X</span>

76543214

### \$\$CNV^XLFUTL(): Convert Base 10 to Another Base

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Utility Functions

ICR \#: 2622

Description: The \$\$CNV^XLFUTL extrinsic function converts a number from Base 10 to another base, which *must* be between 2 and 16.

Format: \$\$CNV^XLFUTL(n,base)

Input Parameters: n: (required) Base 10 number to convert.

base: (required) The base to which the number is to be converted.

Output: returns: Returns the converted number to specified base.

#### Examples

#### Example 1

<span id="_Toc199950994" class="anchor"></span>Figure 161: \$\$CNV^XLFUTL API—Example 1

\><span class="mark">S X=\$\$CNV^XLFUTL(15,2)</span>

\><span class="mark">W X</span>

1111

#### Example 2

<span id="_Toc199950995" class="anchor"></span>Figure 162: \$\$CNV^XLFUTL API—Example 2

\><span class="mark">S X=\$\$CNV^XLFUTL(255,2)</span>

\><span class="mark">W X</span>

11111111

#### Example 3

<span id="_Toc199950996" class="anchor"></span>Figure 163: \$\$CNV^XLFUTL API—Example 3

\><span class="mark">S X=\$\$CNV^XLFUTL(255,8)</span>

\><span class="mark">W X</span>

377

### \$\$DEC^XLFUTL(): Convert Another Base to Base 10

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Utility Functions

ICR \#: 2622

Description: The \$\$DEC^XLFUTL extrinsic function converts a number from a specified base, which *must* be between 2 and 16, to Base 10.

Format: \$\$DEC^XLFUTL(n,base)

Input Parameters: n: (required) Number to convert.

base: (required) Base of number being converted.

Output: returns: Returns the converted number in Base 10.

#### Example

<span id="_Toc199950997" class="anchor"></span>Figure 164: \$\$DEC^XLFUTL API—Example

\><span class="mark">S X=\$\$DEC^XLFUTL("FF",16)</span>

\><span class="mark">W X</span>

255

### \$\$VCD^XLFUTL(): Verify Integrity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Utility Functions

ICR \#: 2622

Description: The \$\$VCD^XLFUTL extrinsic function verifies the integrity of a number with an appended check digit. The check digit *must* be appended by the <u>\$\$CCD^XLFUTL(): Append Check Digit</u> API.

Format: \$\$VCD^XLFUTL(number)

Input Parameters: number: (required) Number to verify, including appended check digit.

Output: returns: Returns:

- 1—Number corresponds to check digit.
- 0—Number does *not* correspond to check digit.

#### Examples

#### Example 1

<span id="_Toc199950998" class="anchor"></span>Figure 165: \$\$VCD^XLFUTL API—Example 1

\><span class="mark">S X=\$\$VCD^XLFUTL(76543214)</span>

\><span class="mark">W X</span>

1

#### Example 2

Transposing “32” to “23”:

<span id="_Toc199950999" class="anchor"></span>Figure 166: \$\$VCD^XLFUTL API—Example 2

\><span class="mark">S X=\$\$VCD^XLFUTL(76542314)</span>

\><span class="mark">W X</span>

0

## IP Address Functions—XLFIPV

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These calls are provided to standardize the storage and processing of Internet Protocol (IP) addresses. Storing addresses in a standardized format simplifies VA FileMan search and sort functions. It also simplifies the processing of addresses in M routines. When VistA is used in an IPv4/IPv6 dual-stack environment, some performance degradation can occur due to the need to try multiple IP address combinations when making network connections. Therefore, it is important to simplify and standardize this process whenever possible.

### \$\$CONVERT^XLFIPV(): Convert any IP Address to Standardized IP Address Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: IP Address Functions

ICR \#: 5844

Description: The \$\$CONVERT^XLFIPV extrinsic function converts an Internet Protocol (IP) address (either IPv4 or IPv6) into an IP address in a standardized format, depending upon the system settings:

- IPv4—<u>\$\$FORCEIP4^XLFIPV(): Convert any IP Address to IPv4</u> API.
- IPv6—<u>\$\$FORCEIP6^XLFIPV(): Convert any IP Address to IPv6</u> API.

Format: \$\$CONVERT^XLFIPV(ip)

Input Parameters: ip: (required) IPv4 or IPv6 address (string; in quotes) to be converted.

Output: returns: Returns:

- An IPv4 address if IPv6 is disabled on the system.
- An IPv6 address if IPv6 is enabled on the system.
- An IPv4 or IPv6NULL address if the input *cannot* be converted.

#### Examples

#### Example 1—IPv4 Enabled

<span id="_Toc199951000" class="anchor"></span>Figure 167: \$\$CONVERT^XLFIPV API—Example 1: IP4 Input and IPv6 Enabled

\><span class="mark">S X=\$\$CONVERT^XLFIPV("\<REDACTED\>")</span>

\><span class="mark">W X</span>

\<REDACTED\>

#### Example 2—IPv4 Disabled

<span id="_Toc199951001" class="anchor"></span>Figure 168: \$\$CONVERT^XLFIPV API—Example 2: IP4 Input and IPv6 Disabled

\><span class="mark">S X=\$\$CONVERT^XLFIPV("\<REDACTED\>")</span>

\><span class="mark">W X</span>

\<REDACTED\>

#### Example 3—IPv6 Enabled

<span id="_Toc199951002" class="anchor"></span>Figure 169: \$\$CONVERT^XLFIPV API—Example 3: IP6 Input and IPv6 Enabled

\><span class="mark">S X=\$\$CONVERT^XLFIPV("\<REDACTED\>")</span>

\><span class="mark">W X</span>

\<REDACTED\>

#### Example 4—IPv6 Disabled

<span id="_Toc199951003" class="anchor"></span>Figure 170: \$\$CONVERT^XLFIPV API—Example 4: IP6 Input and IPv6 Disabled

\><span class="mark">S X=\$\$CONVERT^XLFIPV("\<REDACTED\>")</span>

\><span class="mark">W X</span>

0.0.0.0

### \$\$FORCEIP4^XLFIPV(): Convert any IP Address to IPv4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: IP Address Functions

ICR \#: 5844

Description: The \$\$FORCEIP4^XLFIPV extrinsic function converts an IP address (either IPv4 or IPv6) into an IPv4 address in a standardized format consisting of four decimal numbers, each in the range 0 to 255. For example:

001.99.001.9

Format: \$\$FORCEIP4^XLFIPV(ip)

Input Parameters: ip: (required) IPv4 or IPv6 address (string; in quotes) to be converted.

Output: returns: Returns:

- An IPv4 address in “*nnn.nnn.nnn.nnn*” notation if the input address is valid and has an IPv4 equivalent.
- The NULL address “0.0.0.0” if the input address is invalid.
- The NULL address “0.0.0.0” if an IPv6 address is input that does *not* have an IPv4 equivalent.

#### Examples

#### Example 1

<span id="_Toc199951004" class="anchor"></span>Figure 171: \$\$FORCEIP4^XLFIPV API—Example 1

\><span class="mark">S X=\$\$FORCEIP4^XLFIPV("\<REDACTED\>")</span>

\><span class="mark">W X</span>

\<REDACTED\>

#### Example 2

<span id="_Toc199951005" class="anchor"></span>Figure 172: \$\$FORCEIP4^XLFIPV API—Example 2

\><span class="mark">S X=\$\$FORCEIP4^XLFIPV("\<REDACTED\>")</span>

\><span class="mark">W X</span>

0.0.0.0

#### Example 3

<span id="_Toc199951006" class="anchor"></span>Figure 173: \$\$FORCEIP4^XLFIPV API—Example 3

\><span class="mark">S X=\$\$FORCEIP4^XLFIPV("\<REDACTED\>")</span>

\><span class="mark">W X</span>

0.0.0.0

#### Example 4

<span id="_Toc199951007" class="anchor"></span>Figure 174: \$\$FORCEIP4^XLFIPV API—Example 4

\><span class="mark">S X=\$\$FORCEIP4^XLFIPV("\<REDACTED\>")</span>

\><span class="mark">W X</span>

\<REDACTED\>

#### Example 5

<span id="_Toc199951008" class="anchor"></span>Figure 175: \$\$FORCEIP4^XLFIPV API—Example 5

\><span class="mark">S X=\$\$FORCEIP4^XLFIPV("\<REDACTED\>")</span>

\><span class="mark">W X</span>

\<REDACTED\>

### \$\$FORCEIP6^XLFIPV(): Convert any IP Address to IPv6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: IP Address Functions

ICR \#: 5844

Description: The \$\$FORCEIP6^XLFIPV extrinsic function converts an IP address (either IPv4 or IPv6) into an IPv6 address in a standardized format consisting of eight groups of hexadecimal numbers separated by colons. For example:

2001:0DB8:85A3:0042:0000:8A2E:0370:7334

Format: \$\$FORCEIP6^XLFIPV(ip)

Input Parameters: ip: (required) IPv4 or IPv6 address (string; in quotes) to be converted.

Output: returns: Returns:

- An IPv6 address in “*hhhh:hhhh:hhhh:hhhh:hhhh:hhhh:hhhh:hhhh*” notation if the input address is valid and has an IPv6 equivalent.
- The NULL address “0000:0000:0000:0000:0000:0000:0000:0000” if the input address is invalid.

#### Examples

#### Example 1

<span id="_Toc199951009" class="anchor"></span>Figure 176: \$\$FORCEIP6^XLFIPV API—Example 1

\><span class="mark">S X=\$\$FORCEIP6^XLFIPV("10.126.3.1")</span>

\><span class="mark">W X</span>

0000:0000:0000:0000:0000:FFFF:0A7E:0301

#### Example 2

<span id="_Toc199951010" class="anchor"></span>Figure 177: \$\$FORCEIP6^XLFIPV API—Example 2

\><span class="mark">S X=\$\$FORCEIP6^XLFIPV("10.999.3.1")</span>

\><span class="mark">W X</span>

0000:0000:0000:0000:0000:0000:0000:0000

#### Example 3

<span id="_Toc199951011" class="anchor"></span>Figure 178: \$\$FORCEIP6^XLFIPV API—Example 3

\><span class="mark">S X=\$\$FORCEIP6^XLFIPV("2001:db8::8a2e:370:7334")</span>

\><span class="mark">W X</span>

2001:0DB8:0000:0000:0000:8A2E:0370:7334

#### Example 4

<span id="_Toc199951012" class="anchor"></span>Figure 179: \$\$FORCEIP6^XLFIPV API—Example 4

\><span class="mark">S X=\$\$FORCEIP6^XLFIPV("::ffff:10.126.3.1")</span>

\><span class="mark">W X</span>

0000:0000:0000:0000:0000:FFFF:0A7E:0301

#### Example 5

<span id="_Toc199951013" class="anchor"></span>Figure 180: \$\$FORCEIP6^XLFIPV API—Example 5

\><span class="mark">S X=\$\$FORCEIP6^XLFIPV("127.0.0.1")</span>

\><span class="mark">W X</span>

0000:0000:0000:0000:0000:0000:0000:0001

### \$\$VALIDATE^XLFIPV(): Validate IP Address Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: IP Address Functions

ICR \#: 5844

Description: The \$\$VALIDATE^XLFIPV extrinsic function validates the format of an IP address (either IPv4 or IPv6).

Format: \$\$VALIDATE^XLFIPV(ip)

Input Parameters: ip: (required) IPv4 or IPv6 address (string) to be validated.

Output: returns: Returns:

- 1—If the IP address is in a valid format.
- 0—If the format is invalid or NULL input.

#### Examples

#### Example 1

<span id="_Toc199951014" class="anchor"></span>Figure 181: \$\$VALIDATE^XLFIPV API—Example 1

\><span class="mark">S X=\$\$VALIDATE^XLFIPV(10.126.3.1)</span>

\><span class="mark">W X</span>

1

#### Example 2

<span id="_Toc199951015" class="anchor"></span>Figure 182: \$\$VALIDATE^XLFIPV API—Example 2

\><span class="mark">S X=\$\$VALIDATE^XLFIPV(10.999.3.1)</span>

\><span class="mark">W X</span>

0

#### Example 3

<span id="_Toc199951016" class="anchor"></span>Figure 183: \$\$VALIDATE^XLFIPV API—Example 3

\><span class="mark">S X=\$\$VALIDATE^XLFIPV(2001:db8::8a2e:370:7334)</span>

\><span class="mark">W X</span>

1

#### Example 4

<span id="_Toc199951017" class="anchor"></span>Figure 184: \$\$VALIDATE^XLFIPV API—Example 4

\><span class="mark">S X=\$\$VALIDATE^XLFIPV(2001:db8::8g2h:370:7334)</span>

\><span class="mark">W X</span>

0

### \$\$VERSION^XLFIPV: Show System Settings for IPv6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: IP Address Functions

ICR \#: 5844

Description: The \$\$VERSION^XLFIPV extrinsic function determines the system settings for IPv6.

Format: \$\$VERSION^XLFIPV

Input Parameters: none.

Output: returns: Returns:

- 1—If IPv6 is enabled.
- 0—If IPv6 is disabled.

#### Examples

#### Example 1: IPv6 Enabled

<span id="_Toc199951018" class="anchor"></span>Figure 185: \$\$VERSION^XLFIPV API—Example 1: IPv6 Enabled

\><span class="mark">S X=\$\$VERSION^XLFIPV</span>

\><span class="mark">W X</span>

1

#### Example 2: IPv6 Disabled

<span id="_Toc199951019" class="anchor"></span>Figure 186: \$\$VERSION^XLFIPV API—Example 2: IPv6 Disabled

\><span class="mark">S X=\$\$VERSION^XLFIPV</span>

\><span class="mark">W X</span>

0

## JSON Conversion Functions—XLFJSON

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These calls are provided to standardize the conversion of a global or array to the JavaScript Object Notation (JSON) format, and JSON to a global or array format. They also include extrinsic functions to prepare strings for the JSON conversion process, by escaping (making JSON compliant) or unescaping (making code compliant) strings.

### DECODE^XLFJSON(): Convert a JSON Object into a Closed Array Reference

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: JSON Conversion Functions

ICR \#: 6682

Description: The DECODE^XLFJSON API converts a JSON object into a closed array reference.

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/017.png) NOTE: This API was released with Kernel Patch XU\*8.0\*680.

Format: DECODE^XLFJSON (xujson,xuroot\[,xuerr\])

Input Parameters: xujson: (required) A string or array containing a serialized JSON object.

Output Parameters: xuroot: (required) A closed array reference for M representation of the object.

xuerr: (optional) This contains error messages. If *not* defined, defaults to ^TMP(“XLFJERR”,\$J).

#### Example

<span id="_Toc199951020" class="anchor"></span>Figure 187: DECODE^XLFJSON API—Example

\><span class="mark">S INJSON(1)="{""menu"":{""id"":""file"",""popup"":{""menuitem"":\[{""value</span><span class="mark">"": ""New"",""onclick"":""CreateNewDoc()""},"</span>

\><span class="mark">S INJSON(2)="{""value"": ""Open"",""onclick"": ""OpenDoc()""},{""value"":</span><span class="mark">""Close"",""onclick"": ""CloseDoc()""}\]} ,"</span>

\><span class="mark">S INJSON(3)="""value"":""File""}}"</span>

\><span class="mark">D DECODE^XLFJSON("INJSON","OUTJSON","ERRORS")</span>

\><span class="mark">ZW OUTJSON</span>

OUTJSON("menu","id")="file"

OUTJSON("menu","popup","menuitem",1,"onclick")="CreateNewDoc()"

OUTJSON("menu","popup","menuitem",1,"value")="New"

OUTJSON("menu","popup","menuitem",2,"onclick")="OpenDoc()"

OUTJSON("menu","popup","menuitem",2,"value")="Open"

OUTJSON("menu","popup","menuitem",3,"onclick")="CloseDoc()"

OUTJSON("menu","popup","menuitem",3,"value")="Close"

OUTJSON("menu","value")="File"

### ENCODE^XLFJSON(): Convert Closed Array or Global Reference to a JSON Object

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: JSON Conversion Functions

ICR \#: 6682

Description: The ENCODE^XLFJSON API converts a closed array or global reference to a JSON object.

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/018.png) NOTE: This API was released with Kernel Patch XU\*8.0\*680.

Format: ENCODE^XLFJSON(xuroot,xujson\[,xuerr\])

Input Parameters: xuroot: (required) A closed array reference for M representation of the object.

Output Parameters: xujson: (required) A string or array containing a serialized JSON object.

xuerr: (optional) This contains error messages. If *not* defined, defaults to ^TMP(“XLFJERR”,\$J).

#### Example

<span id="_Toc199951021" class="anchor"></span>Figure 188: ENCODE^XLFJSON API—Example

\><span class="mark">S Y("menu","id")="file"</span>

\><span class="mark">S Y("menu","popup","menuitem",1,"onclick")="CreateNewDoc()"</span>

\><span class="mark">S Y("menu","popup","menuitem",1,"value")="New"</span>

\><span class="mark">S Y("menu","popup","menuitem",2,"onclick")="OpenDoc()"</span>

\><span class="mark">S Y("menu","popup","menuitem",2,"value")="Open"</span>

\><span class="mark">S Y("menu","popup","menuitem",3,"onclick")="CloseDoc()"</span>

\><span class="mark">S Y("menu","popup","menuitem",3,"value")="Close"</span>

\><span class="mark">S Y("menu","value")="File"</span>

\><span class="mark">D ENCODE^XLFJSON("Y","OUTJSON","ERRORS")</span>

\><span class="mark">W OUTJSON(1)</span>

{"menu":{"id":"file","popup":{"menuitem":\[{"onclick":"CreateNewDoc()","value":"N

ew"},{"onclick":"OpenDoc()","value":"Open"},{"onclick":"CloseDoc()","value":"Clo

se"}\]},"value":"File"}}

### \$\$ESC^XLFJSON(): Escape String to JSON

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: JSON Conversion Functions

ICR \#: 6682

Description: The \$\$ESC^XLFJSON extrinsic function returns an escaped string in a JSON format.

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/019.png) NOTE: This API was released with Kernel Patch XU\*8.0\*680.

Format: \$\$ESC^XLFJSON(x)

Input Parameters: x: (required) A string to be escaped to a JSON format.

Output: returns: Returns a JSON escaped string.

#### Example

<span id="_Toc199951022" class="anchor"></span>Figure 189: \$\$ESC^XLFJSON API—Example

\><span class="mark">W \$\$ESC^XLFJSON("\one\two\three\\)</span>

\\one\\two\\three\\

### \$\$UES^XLFJSON(): Unescape JSON to a String

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: JSON Conversion Functions

ICR \#: 6682

Description: The \$\$UES^XLFJSON extrinsic function returns a unescaped string from a JSON format.

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/020.png) NOTE: This API was released with Kernel Patch XU\*8.0\*680.

Format: \$\$UES^XLFJSON(x)

Input Parameters: x: (required) A JSON escaped string to be unescaped.

Output: returns: Returns a unescaped string representation of the escaped JSON input string.

#### Example

<span id="_Toc199951023" class="anchor"></span>Figure 190: \$\$UES^XLFJSON API—Example

\><span class="mark">W \$\$UES^XLFJSON("\\one\\two\\three\\")</span>

\one\two\three\\

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/021.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/022.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-xlf-function-library-user-guide/023.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.

[^1]: Wikipedia Definition for “Bitwise operation:” <https://en.wikipedia.org/wiki/Bitwise_operation>

[^2]: Definition as taken from: *Webster’s New World College Dictionary*, Fourth Edition; Michael Agnes, Editor in Chief; David B. Guralink, Editor in Chief Emeritus; Copyright 2001, 2000, 1999 by IDG Books Worldwide, Inc.; ISBN 0-02-863118-8.