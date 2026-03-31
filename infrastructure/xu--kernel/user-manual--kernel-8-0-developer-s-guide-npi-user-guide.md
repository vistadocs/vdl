---
title: "Kernel 8.0 Developerâ€™s Guide: NPI User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: NPI"
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
  - xusnpi
  - guide
  - provider
  - example
  - table
  - class
  - kernel
  - contents
  - developer
page_count: 0
word_count: 2066
section_count: 7
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_npi_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_npi_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259485" class="anchor"></span>National Provider Identifier (NPI) Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-npi-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-npi-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: National Provider Identifier (NPI) Developer Tools User Guide</em>.</p>
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

<span id="_Toc207304615" class="anchor"></span>List of Figures

<span id="_Ref38421374" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-npi-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [\$\$CHKDGT^XUSNPI(): Validate NPI Format](#chkdgtxusnpi-validate-npi-format)
    - [Examples](#examples)
  - [\$\$NPI^XUSNPI(): Get NPI from Files \#200, \#4, or \#355.93](#npixusnpi-get-npi-from-files-200-4-or-35593)
    - [Examples](#examples-1)
  - [\$\$QI^XUSNPI(): Get Provider Entities](#qixusnpi-get-provider-entities)
    - [Examples](#examples-2)
  - [\$\$NPIUSED^XUSNPI1(): Returns an Error or Warning if an NPI is in Use](#npiusedxusnpi1-returns-an-error-or-warning-if-an-npi-is-in-use)
  - [\$\$TAXIND^XUSTAX(): Get Taxonomy Code from File \#200](#taxindxustax-get-taxonomy-code-from-file-200)
    - [Example](#example)
  - [\$\$TAXORG^XUSTAX(): Get Taxonomy Code from File \#4](#taxorgxustax-get-taxonomy-code-from-file-4)
    - [Example](#example-1)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: National Provider Identifier (NPI) Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following National Provider Identifier (NPI) APIs and Extrinsic Functions are available for developers. These APIs and Extrinsic Functions are described below.

## \$\$CHKDGT^XUSNPI(): Validate NPI Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: National Provider Identifier (NPI)

ICR \#: 4532

Description: The \$\$CHKDGT^XUSNPI extrinsic function validates the format of a National Provider Identifier (NPI) number. It checks the following:

- NPI is numeric.
- Length of the Number (*must* be 10-digits).
- Check Digit is Valid.

![](kernel-8-0-developer-s-guide-npi-user-guide/004.png) NOTE: This API was released with Kernel Patch XU\*8.0\*410.

Format: \$\$CHKDGT^XUSNPI(xusnpi)

Input Parameters: xusnpi: (required) The 10-digit National Provider Identifier (NPI) number to validate. No default.

Output: returns: Returns:

- 1—If check digit is valid. The NPI number *must* be 10-digits long.
- 0—If check digit is *not* valid.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

Figure 1 shows the result when checking a valid NPI:

<span id="_Ref500752448" class="anchor"></span>Figure 1: \$\$CHKDGT^XUSNPI API—Example 1

\><span class="mark">W \$\$CHKDGT^XUSNPI(1234567893)</span>

1

#### Example 2

Figure 2 shows the result when checking an invalid NPI (*not*10 digits):

<span id="_Ref500752484" class="anchor"></span>Figure 2: \$\$CHKDGT^XUSNPI API—Example 2

\><span class="mark">W \$\$CHKDGT^XUSNPI(123456789)</span>

0

#### Example 3

<u>Figure 3</u> shows the result when checking an invalid NPI (*invalid* digit):

<span id="_Ref508717628" class="anchor"></span>Figure 3: \$\$CHKDGT^XUSNPI API—Example 3

\><span class="mark">W \$\$CHKDGT^XUSNPI(1234567892)</span>

0

## \$\$NPI^XUSNPI(): Get NPI from Files \#200, \#4, or \#355.93

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: National Provider Identifier (NPI)

ICR \#: 4532

Description: The \$\$NPI^XUSNPI extrinsic function retrieves the National Provider Identifier (NPI) and related utilities from any of the following files:

- NEW PERSON (#200)
- INSTITUTION (#4)
- IB NON/OTHER VA BILLING PROVIDER (#355.93)

![](kernel-8-0-developer-s-guide-npi-user-guide/005.png) NOTE: This API was released with Kernel Patch XU\*8.0\*410.

Format: \$\$NPI^XUSNPI(xusqi,xusien\[,xusdate\])

Input Parameters: xusqi: (required) The Qualified Identifier for the NPI. For example:

Individual_ID, Organization_ID, or Non_VA_Provider_ID

No default.

xusien: (required) The Internal Entry Number (IEN) from any of the following files:

- NEW PERSON (#200)
- INSTITUTION (#4)
- IB NON/OTHER VA BILLING PROVIDER (#355.93)

No default.

xusdate: (optional) A date of interest. Defaults to “Today”.

Output: returns: Returns any of the following strings:

- NPI^EffectiveDate^Status—If National Provider Identifier (NPI) exists.
- 0—If NPI does *not* exist.
- -1^ErrorMessage—If invalid xusqi or xusien input parameters.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

The example in Figure 4 uses the following file data:

- Individual_ID = NEW PERSON (#200) file
- NPI = 9876543213
- EffectiveDate = 3061108.123651
- Status = Active

<span id="_Ref499807975" class="anchor"></span>Figure 4: \$\$NPI^XUSNPI API—Example 1

\><span class="mark">W \$\$NPI^XUSNPI("Individual_ID",82)</span>

9876543213^3061108.123651^Active

#### Example 2

The example in <u>Figure 5</u> uses the following file data:

- Organization_ID = INSTITUTION (#4) file
- NPI = 1111111112
- EffectiveDate = 3070122
- Status = Active

<span id="_Ref499807999" class="anchor"></span>Figure 5: \$\$NPI^XUSNPI API—Example 2

\><span class="mark">W \$\$NPI^XUSNPI("Organization_ID",1)</span>

1111111112^3070122^Active

#### Example 3

The example in <u>Figure 6</u> uses the following file data:

- Non_VA_Provider_ID = IB NON/OTHER VA BILLING PROVIDER (#355.93) file
- NPI = 2222222228
- EffectiveDate = 3070122
- Status = Active

<span id="_Ref508718906" class="anchor"></span>Figure 6: \$\$NPI^XUSNPI API—Example 3

\><span class="mark">W \$\$NPI^XUSNPI("Non_VA_Provider_ID ",1)</span>

2222222228 ^3070122^Active

## \$\$QI^XUSNPI(): Get Provider Entities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: National Provider Identifier (NPI)

ICR \#: 4532

Description: The \$\$QI^XUSNPI extrinsic function retrieves all qualified provider entities for a National Provider Identifier (NPI) identifier.

![](kernel-8-0-developer-s-guide-npi-user-guide/006.png) NOTE: This API was released with Kernel Patch XU\*8.0\*410.

Format: \$\$QI^XUSNPI(xusnpi)

Input Parameters: xusnpi: (required) The National Provider Identifier (NPI) identifier. No default.

Output: returns: Returns either of the following strings:

- QualifiedIdentifier^IEN^EffectiveDate^Status—National Provider Identifier (NPI) exists. If more than one record is found, they are separated by a semi-colon (;).
- 0—Qualified NPI does *not* exist.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

The example in Figure 7 uses the following file data:

- Individual_ID = NEW PERSON (#200) file
- IEN = 82
- EffectiveDate = 3061108.123651
- Status = Active

<span id="_Ref508720189" class="anchor"></span>Figure 7: \$\$QI^XUSNPI API—Example 1

\><span class="mark">W \$\$QI^XUSNPI(9876543213)</span>

Individual_ID^82^3061108.123651^Active;

#### Example 2

The example in <u>Figure 8</u> uses the following file data:

- Organization_ID = INSTITUTION (#4) file
- IEN = 1
- EffectiveDate = 3070122
- Status = Active

<span id="_Ref508720188" class="anchor"></span>Figure 8: \$\$QI^XUSNPI API—Example 2

\><span class="mark">W \$\$QI^XUSNPI(1111111112)</span>

Organization_ID^1^3070122^Active;

#### Example 3

The example in [Figure 183](#_Ref508720187) uses the following file data:

- Non_VA_Provider_ID = IB NON/OTHER VA BILLING PROVIDER (#355.93) file
- IEN = 3
- EffectiveDate = 3070122
- Status = Active

<span id="_Ref508720187" class="anchor"></span>Figure 9: \$\$QI^XUSNPI API—Example 3

\><span class="mark">W \$\$QI^XUSNPI(2222222228)</span>

Non_VA_Provider_ID^3^3070122^Active;

## \$\$NPIUSED^XUSNPI1(): Returns an Error or Warning if an NPI is in Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: National Provider Identifier (NPI)

ICR \#: 6888

Description: The \$\$NPIUSED^XUSNPI1 extrinsic function returns an error or warning if an NPI is in use.

Call this API from code where a new NPI is being added to a provider. It evaluates whether the NPI is currently or previously used by any entity on any of the following files:

- NEW PERSON (#200)
- INSTITUTION (4)
- IB NON/OTHER VA BILLING PROVIDER (#355.93)

If the API returns:

- Error—NPI should *not* be assigned to the provider.
- Warning—Warning should be displayed to the end user, but they should be allowed to add the NPI to the new provider.

![](kernel-8-0-developer-s-guide-npi-user-guide/007.png) NOTE: This API was released with Kernel Patch XU\*8.0\*480.

Format: \$\$NPIUSED^XUSNPI1(xusnpi,xusqid,xusqil,xusrslt\[,xusien\])

Input Parameters: xusnpi: (required) The NPI being checked. No default.

xusqid: (required) The Qualified Identifier for the NPI (such as "Individual_ID"). No default.

xusqil: (required) The delimited list of entities already using that NPI. No default. This is the output from [\$\$QI^XUSNPI](#qixusnpi-get-provider-entities) in the following format:

Qualified_Identifier^IEN^Effective_date/time^Active/Inactive;xusien: (optional) This input parameter is *only* set if this routine is being called from the Input transform of the NPI field in any of the following files:

- NEW PERSON (#200)
- INSTITUTION (4)
- IB NON/OTHER VA BILLING PROVIDER (#355.93)

It is set to the IEN of the entity being edited. No Default.

![](kernel-8-0-developer-s-guide-npi-user-guide/008.png) CAUTION: This input parameter should *only* be set if the routine is being called from an Input transform. It suppresses return of the error or warning message.

Output Parameter: xusrslt: An array containing either an error or warning message (if any).

Output: returns: Returns:

- 0 (Zero; No Error)—If the NPI is *not* being used, or if the API is called from the Input transform and the NPI was previously used by the current user.
- 1 (Error)—If an error was found, an *error* message is returned in xusrslt.
- 2 (Warning)—If the current file is the NEW PERSON (#200) or IB NON/OTHER VA BILLING PROVIDER (#355.93), and if a provider on the other file has the NPI, a *warning* message is returned in xusrslt.

> ![](kernel-8-0-developer-s-guide-npi-user-guide/009.png) NOTE: A provider can be both a VA and a *non*-VA provider at the same time.

## \$\$TAXIND^XUSTAX(): Get Taxonomy Code from File \#200

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: National Provider Identifier (NPI)

ICR \#: 4911

Description: The \$\$TAXIND^XUSTAX extrinsic function retrieves the taxonomy code for a given record in the NEW PERSON (#200) file.

![](kernel-8-0-developer-s-guide-npi-user-guide/010.png) NOTE: This API was released with Kernel Patch XU\*8.0\*410.

Format: \$\$TAXIND^XUSTAX(xuien)

Input Parameters: xuien: (required) This is the Internal Entry Number (IEN) of the record in the NEW PERSON (#200) file. No default.

Output: returns: Returns either of the following strings:

- TaxonomyX12Code^TaxonomyIEN—Taxonomy exists.
- ^—Taxonomy does *not* exist.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following example uses the following file data:

- Taxonomy X12 code of the record in the NEW PERSON (#200) file = 2086S0105
- Taxonomy IEN from the PERSON CLASS (#8932.1) file = 900

<span id="_Toc199950686" class="anchor"></span>Figure 10: \$\$TAXIND^XUSTAX API—Example

\><span class="mark">W \$\$TAXIND^XUSTAX(82)</span>

2086S0105X^900

## \$\$TAXORG^XUSTAX(): Get Taxonomy Code from File \#4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: National Provider Identifier (NPI)

ICR \#: 4911

Description: The \$\$TAXORG^XUSTAX extrinsic function retrieves the taxonomy code for a given record in the INSTITUTION (#4) file.

![](kernel-8-0-developer-s-guide-npi-user-guide/011.png) NOTE: This API was released with Kernel Patch XU\*8.0\*410.

Format: \$\$TAXORG^XUSTAX(xuien)

Input Parameters: xuien: (required) This is the Internal Entry Number (IEN) of the record in the INSTITUTION (#4) file. No default.

Output: returns: Returns either of the following strings:

- TaxonomyX12Code^TaxonomyIEN—Taxonomy exists.
- ^—Taxonomy does *not* exist.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following example uses the following file data:

- Taxonomy X12 code of the record in the INSTITUTION (#4) file = 390200000X
- Taxonomy IEN from the PERSON CLASS (#8932.1) file = 144

<span id="_Toc199950687" class="anchor"></span>Figure 11: \$\$TAXORG^XUSTAX API—Example

\><span class="mark">W \$\$TAXORG^XUSTAX(2)</span>

390200000X^144

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-npi-user-guide/012.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-npi-user-guide/013.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-npi-user-guide/014.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.