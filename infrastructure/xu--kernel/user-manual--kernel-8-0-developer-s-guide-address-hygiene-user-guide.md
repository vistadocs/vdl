---
title: "Kernel 8.0 Developerâ€™s Guide: Address Hygiene User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: Address Hygiene"
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
  - ztmp
  - span
  - code
  - fips
  - class
  - xiputil
  - city
  - table
  - contents
  - county
page_count: 0
word_count: 1700
section_count: 6
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_address_hygiene_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_address_hygiene_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  Address Hygiene Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-address-hygiene-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-address-hygiene-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Address Hygiene Developer Tools User Guide</em>.</p>
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

![](kernel-8-0-developer-s-guide-address-hygiene-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [CCODE^XIPUTIL(): FIPS Code Data](#ccodexiputil-fips-code-data)
    - [Example](#example)
  - [\$\$FIPS^XIPUTIL(): FIPS Code for ZIP Code](#fipsxiputil-fips-code-for-zip-code)
    - [Example](#example-1)
  - [\$\$FIPSCHK^XIPUTIL(): Check for FIPS Code](#fipschkxiputil-check-for-fips-code)
    - [Examples](#examples)
  - [POSTAL^XIPUTIL(): ZIP Code Information](#postalxiputil-zip-code-information)
    - [Examples](#examples-1)
  - [POSTALB^XIPUTIL(): Active ZIP Codes](#postalbxiputil-active-zip-codes)
    - [Example](#example-2)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Address Hygiene Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.
The VA’s Address Hygiene software validates and corrects address data as necessary.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Address Hygiene APIs and Extrinsic Functions are available for developers to work with Address Hygiene. These APIs and Extrinsic Functions are described below.

## CCODE^XIPUTIL(): FIPS Code Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Address Hygiene

ICR \#: 3618

Description: The CCODE^XIPUTIL API returns all the data associated for a Federal Information Processing Standards (FIPS) code.

Format: CCODE^XIPUTIL(fips,.xipc)

Input Parameters: fips: (required) FIPS Code.

Output Parameters: xipc: An array containing the following:

- XIPC(“COUNTY”)—County associated with this FIPS code
- XIPC(“FIPS CODE”)—5-digit FIPS county code
- XIPC(“INACTIVE DATE”)—Date the FIPS code was inactivated
- XIPC(“LATITUDE”)—Estimated Latitude of the county
- XIPC(“LONGITUDE”)—Estimated Longitude of the county
- XIPC(“STATE”)—State associated with this FIPS code
- XIPC(“STATE POINTER”)—POINTER to the state in the STATE (#5) file
- XIPC(“ERROR”)—Errors encountered during lookup

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950503" class="anchor"></span>Figure 1: CCODE^XIPUTIL API—Example

\><span class="mark">S ZFIPS=54041</span>

\><span class="mark">S ZTMP=""</span>

\><span class="mark">D CCODE^XIPUTIL(ZFIPS,.ZTMP)</span>

\><span class="mark">ZW ZTMP,ZFIPS</span>

ZFIPS=54041

ZTMP=

ZTMP("COUNTY")=LEWIS

ZTMP("FIPS CODE")=54041

ZTMP("INACTIVE DATE")=

ZTMP("LATITUDE")=39:00N

ZTMP("LONGITUDE")=80:28W

ZTMP("STATE")=WEST VIRGINIA

ZTMP("STATE POINTER")=54

## \$\$FIPS^XIPUTIL(): FIPS Code for ZIP Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Address Hygiene

ICR \#: 3618

Description: The \$\$FIPS^XIPUTIL extrinsic function returns the Federal Information Processing Standard (FIPS) Code associated with the Postal Code.

Format: \$\$FIPS^XIPUTIL(pcode)

Input Parameters: pcode: (required) Postal Code for which the FIPS Code is returned.

Output: returns: Returns the FIPS Code.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950504" class="anchor"></span>Figure 2: \$\$FIPS^XIPUTIL API—Example

\><span class="mark">S X=\$\$FIPS^XIPUTIL("26452")</span>

\><span class="mark">W X</span>

54041

## \$\$FIPSCHK^XIPUTIL(): Check for FIPS Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Address Hygiene

ICR \#: 3618

Description: The \$\$FIPSCHK^XIPUTIL extrinsic function answers the question as to whether a Federal Information Processing Standard (FIPS) code exists. It returns the following:

- IEN—Internal Entry Number, if the FIPS code exists.
- Zero (0)—FIPS Code does *not* exist.

Format: \$\$FIPSCHK^XIPUTIL(fips)

Input Parameters:fips: (required) FIPS Code.

Output: returns: Returns:

- IEN—Internal Entry Number, if the FIPS code exists.
- Zero (0)—FIPS Code does *not* exist.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

<span id="_Toc199950505" class="anchor"></span>Figure 3: \$\$FIPSCHK^XIPUTIL API—Example 1

\><span class="mark">S X=\$\$FIPSCHK^XIPUTIL("54041")</span>

\><span class="mark">W X</span>

335

#### Example 2

<span id="_Toc199950506" class="anchor"></span>Figure 4: \$\$FIPSCHK^XIPUTIL API—Example 2

\><span class="mark">S X=\$\$FIPSCHK^XIPUTIL("54999")</span>

\><span class="mark">W X</span>

0

## POSTAL^XIPUTIL(): ZIP Code Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Address Hygiene

ICR \#: 3618

Description: The POSTAL^XIPUTIL API returns United States Postal Service (USPS)-related data/information in an output array (see “Output Parameters”) for the preferred (default) ZIP Code.

Format: POSTAL^XIPUTIL(pcode,.xip)

Input Parameters:pcode: (required) Postal Code for which data is returned.

Output Parameters:.xip: An array containing the following:

- XIP(“CITY”)—City that the United States Postal Service (USPS) assigned to this PCODE.
- XIP(“CITY ABBREVIATION”)—USPS assigned abbreviation.
- XIP(“CITY KEY”)—USPS assigned city key.
- XIP(“COUNTY”)—County associated with this PCODE.
- XIP(“COUNTY POINTER”)—POINTER to the county in the COUNTY CODE (#5.13) file.
- XIP(“FIPS CODE”)—5-digit FIPS code associated with the county.
- XIP(“INACTIVE DATE”)—Date FIPS Code inactive.
- XIP(“LATITUDE”)—Latitude.
- XIP(“LONGITUDE”)—Longitude.
- XIP(“POSTAL CODE”)—Value used to look up postal data.
- XIP(“PREFERRED CITY KEY”)—USPS preferred (DEFAULT) city key.
- XIP(“STATE”)—State associated with this PCODE.
- XIP(“STATE POINTER”)—POINTER to the state in the STATE (#5) file.
- XIP(“UNIQUE KEY”)—Unique lookup value.
- XIP(“ERROR”)—Errors encountered during lookup.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

<span id="_Toc199950507" class="anchor"></span>Figure 5: POSTAL^XIPUTIL API—Example 1

\><span class="mark">S ZCODE=99991</span>

\><span class="mark">S ZTMP=""</span>

\><span class="mark">D POSTAL^XIPUTIL(ZCODE,.ZTMP)</span>

\><span class="mark">ZW ZTMP,ZCODE</span>

ZCODE=99991

ZTMP=

ZTMP("CITY")=ANYCITY1

ZTMP("CITY ABBREVIATION")=

ZTMP("CITY KEY")=Z22802

ZTMP("COUNTY")=ANYCOUNTY1

ZTMP("COUNTY POINTER")=2910

ZTMP("FIPS CODE")=06075

ZTMP("INACTIVE DATE")=

ZTMP("LATITUDE")=39:00N

ZTMP("LONGITUDE")=80:28W

ZTMP("POSTAL CODE")=99991

ZTMP("PREFERRED CITY KEY")=Z22802

ZTMP("STATE")=ANYSTATE1

ZTMP("STATE POINTER")=6

ZTMP("UNIQUE KEY")=999919Z22802

#### Example 2

<span id="_Toc199950508" class="anchor"></span>Figure 6: POSTAL^XIPUTIL API—Example 2

\><span class="mark">S ZCODE=99992</span>

\><span class="mark">S ZTMP=</span>

\><span class="mark">D POSTAL^XIPUTIL(ZCODE,.ZTMP)</span>

\><span class="mark">ZW ZTMP,ZCODE</span>

ZCODE=99992

ZTMP=

ZTMP("CITY")=ANYCITY2

ZTMP("CITY ABBREVIATION")=

ZTMP("CITY KEY")=Z22296

ZTMP("COUNTY")=ANYCOUNTY2

ZTMP("COUNTY POINTER")=2912

ZTMP("FIPS CODE")=06001

ZTMP("INACTIVE DATE")=

ZTMP("POSTAL CODE")=99992

ZTMP("PREFERRED CITY KEY")=Z22296

ZTMP("STATE")=ANYSTATE2

ZTMP("STATE POINTER")=6

ZTMP("UNIQUE KEY")=999929Z22296

## POSTALB^XIPUTIL(): Active ZIP Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Address Hygiene

ICR \#: 3618

Description: The POSTALB^XIPUTIL API returns all active ZIP codes for a single ZIP code.

Format: POSTALB^XIPUTIL(pcode,.xip)

Input Parameters:pcode: (required) Postal code for which the data is being requested.

Output Parameters:.xip(*n*): The number of primary subscripts in an array:

- XIP(*n*,“CITY”)—City that the United States Postal Service (USPS) assigned to this pcode. An asterisk (\*) indicates which city is PREFERRED (DEFAULT).
- XIP(*n,*“CITY KEY”)—USPS’s assigned city key.
- XIP(*n*, “CITY ABBREVIATION”)—USPS’s assigned abbreviation.
- XIP(*n*,“COUNTY”)—County associated with this pcode.
- XIP(*n*,“COUNTY POINTER”)—POINTER to the county in the COUNTY CODE (#5.13) file.
- XIP(*n*,“FIPS CODE”)—5-digit FIPS code associated with the county
- XIP(*n*,“POSTAL CODE”)—Value used to look up postal data
- XIP(*n*,“PREFERRED CITY KEY”)—USPS PREFERRED (DEFAULT) city key.
- XIP(*n*,“STATE”)—State associated with this pcode.
- XIP(*n*,“STATE POINTER”)—POINTER to the state in the STATE (#5) file.
- XIP(*n*,“UNIQUE KEY”)—Unique lookup value.
- XIP(“ERROR”)—Errors encountered during lookup.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950509" class="anchor"></span>Figure 7: POSTALB^XIPUTIL API—Example

\><span class="mark">S ZCODE=26452</span>

\><span class="mark">S ZTMP=""</span>

\><span class="mark">D POSTALB^XIPUTIL(ZCODE,.ZTMP)</span>

\><span class="mark">ZW ZTMP,ZCODE</span>

ZCODE=26452

ZTMP=2

ZTMP(1,"CITY")=WESTON\*

ZTMP(1,"CITY ABBREVIATION")=

ZTMP(1,"CITY KEY")=X29362

ZTMP(1,"COUNTY")=LEWIS

ZTMP(1,"COUNTY POINTER")=335

ZTMP(1,"FIPS CODE")=54041

ZTMP(1,"POSTAL CODE")=26452

ZTMP(1,"PREFERRED CITY KEY")=X29362

ZTMP(1,"STATE")=WEST VIRGINIA

ZTMP(1,"STATE POINTER")=54

ZTMP(1,"UNIQUE KEY")=26452X29362

ZTMP(2,"CITY")=VALLEY CHEL

ZTMP(2,"CITY ABBREVIATION")=

ZTMP(2,"CITY KEY")=X2A444

ZTMP(2,"COUNTY")=LEWIS

ZTMP(2,"COUNTY POINTER")=335

ZTMP(2,"FIPS CODE")=54041

ZTMP(2,"POSTAL CODE")=26452

ZTMP(2,"PREFERRED CITY KEY")=X29362

ZTMP(2,"STATE")=WEST VIRGINIA

ZTMP(2,"STATE POINTER")=54

ZTMP(2,"UNIQUE KEY")=26452X2A444

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-address-hygiene-user-guide/004.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-address-hygiene-user-guide/005.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-address-hygiene-user-guide/006.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.