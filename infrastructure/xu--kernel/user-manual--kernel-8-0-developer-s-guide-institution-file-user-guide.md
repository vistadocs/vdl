---
title: "Kernel 8.0 Developerâ€™s Guide: Institution File User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: Institution File"
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
  - institution
  - xuaf
  - number
  - table
  - span
  - contents
  - station
  - returns
  - param
  - xumf
page_count: 0
word_count: 5639
section_count: 30
table_count: 7
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_institution_file_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_institution_file_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259348" class="anchor"></span>Institution File Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-institution-file-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-institution-file-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
<caption><p><span id="_Toc199951036" class="anchor"></span>Table 1: MAIN^XUMFP(): Master File Parameters API—QRD: Query Definition</p></caption>
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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Institution File Developer Tools User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
</tbody>
</table>

<span id="_Toc199951036" class="anchor"></span>Table 1: MAIN^XUMFP(): Master File Parameters API—QRD: Query Definition

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc234301876" class="anchor"></span>List of Figures

<span id="_Toc206924658" class="anchor"></span>List of Tables

<span id="_Hlt412359042" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-institution-file-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [\$\$ACTIVE^XUAF4(): Institution Active Facility (True/False)](#activexuaf4-institution-active-facility-truefalse)
  - [CDSYS^XUAF4(): Coding System Name](#cdsysxuaf4-coding-system-name)
  - [\$\$CERNER^XUAF4(): Check if Site Converted to Cerner](#cernerxuaf4-check-if-site-converted-to-cerner)
  - [CHILDREN^XUAF4(): List of Child Institutions for a Parent](#childrenxuaf4-list-of-child-institutions-for-a-parent)
  - [\$\$CIRN^XUAF4(): Institution CIRN-enabled Field Value](#cirnxuaf4-institution-cirn-enabled-field-value)
  - [F4^XUAF4(): Institution Data for a Station Number](#f4xuaf4-institution-data-for-a-station-number)
    - [Example](#example)
  - [\$\$ID^XUAF4(): Institution Identifier](#idxuaf4-institution-identifier)
  - [\$\$IDX^XUAF4(): Institution IEN (Using Coding System and ID)](#idxxuaf4-institution-ien-using-coding-system-and-id)
  - [\$\$IEN^XUAF4(): IEN for Station Number](#ienxuaf4-ien-for-station-number)
    - [Example](#example-1)
  - [\$\$LEGACY^XUAF4(): Institution Realigned/Legacy (True/False)](#legacyxuaf4-institution-realignedlegacy-truefalse)
  - [\$\$LKUP^XUAF4(): Institution Lookup](#lkupxuaf4-institution-lookup)
  - [LOOKUP^XUAF4(): Look Up Institution Identifier](#lookupxuaf4-look-up-institution-identifier)
    - [Example](#example-2)
  - [\$\$MADD^XUAF4(): Institution Mailing Address](#maddxuaf4-institution-mailing-address)
  - [\$\$NAME^XUAF4(): Institution Official Name](#namexuaf4-institution-official-name)
  - [\$\$NNT^XUAF4(): Institution Station Name, Number, and Type](#nntxuaf4-institution-station-name-number-and-type)
  - [\$\$NS^XUAF4(): Institution Name and Station Number](#nsxuaf4-institution-name-and-station-number)
  - [\$\$O99^XUAF4(): IEN of Merged Station Number](#o99xuaf4-ien-of-merged-station-number)
    - [Example](#example-3)
  - [\$\$PADD^ XUAF4(): Institution Physical Address](#padd-xuaf4-institution-physical-address)
  - [PARENT^XUAF4(): Parent Institution Lookup](#parentxuaf4-parent-institution-lookup)
  - [\$\$PRNT^XUAF4(): Institution Parent Facility](#prntxuaf4-institution-parent-facility)
  - [\$\$RF^XUAF4(): Realigned From Institution Information](#rfxuaf4-realigned-from-institution-information)
    - [Example](#example-4)
  - [\$\$RT^XUAF4(): Realigned To Institution Information](#rtxuaf4-realigned-to-institution-information)
    - [Example](#example-5)
  - [SIBLING^XUAF4(): Sibling Institution Lookup](#siblingxuaf4-sibling-institution-lookup)
  - [\$\$STA^XUAF4(): Station Number for IEN](#staxuaf4-station-number-for-ien)
    - [Example](#example-6)
  - [\$\$TF^XUAF4(): Treating Facility (True/False)](#tfxuaf4-treating-facility-truefalse)
    - [Example](#example-7)
  - [\$\$WHAT^XUAF4(): Institution Single Field Information](#whatxuaf4-institution-single-field-information)
  - [\$\$IEN^XUMF(): Institution IEN (Using IFN, Coding System, and ID)](#ienxumf-institution-ien-using-ifn-coding-system-and-id)
  - [MAIN^XUMFI(): HL7 Master File Message Builder](#mainxumfi-hl7-master-file-message-builder)
    - [Details](#details)
    - [Example](#example-8)
  - [MAIN^XUMFP(): Master File Parameters](#mainxumfp-master-file-parameters)
    - [Details](#details-1)
    - [Example](#example-9)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Institution File Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Institution File APIs and Extrinsic Functions are available for developers to work with the INSTITUTION (#4) file. These APIs and Extrinsic Functions are described below.

## \$\$ACTIVE^XUAF4(): Institution Active Facility (True/False)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The \$\$ACTIVE^XUAF4 extrinsic function, given the Internal Entry Number (IEN) in the INSTITUTION (#4) file, returns the Boolean value for the question—is this an active facility? It checks to see if the INACTIVE FACILITY FLAG (#101) field is *not* set.

Format: \$\$ACTIVE^XUAF4(ien)

Input Parameters: ien: (required) Internal Entry Number (IEN) of the institution in question.

Output: returns: Returns a Boolean value:

- True (*non*-Zero)—Station Number is an active facility.
- False (Zero)—Station Number is *not* an active facility. The INACTIVE FACILITY FLAG (#101) field has a value indicating it is inactive.

## CDSYS^XUAF4(): Coding System Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The CDSYS^XUAF4 API returns the Coding System name.

Format: CDSYS^XUAF4(y)

Input Parameters: y: (required) Pass by reference, returns:

Y(coding_system) = \$D_of_local_system^ coding_system name

Output Parameters: y: Passed by reference, returns:

Y(coding_system) = \$D_of_local_system^ coding_system name

## \$\$CERNER^XUAF4(): Check if Site Converted to Cerner

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The \$\$CERNER^XUAF4 extrinsic function checks if a VA facility (site) has been converted to Cerner (aka Oracle Health).

Format: \$\$CERNER^XUAF4(sta)

Input Parameters: sta: (required) The site’s station number.

Output: returns: Returns:

- 1—Cerner-converted site.
- -1—Invalid station number; *not* a Cerner-converted site.

## CHILDREN^XUAF4(): List of Child Institutions for a Parent

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The CHILDREN^XUAF4 API returns a list of all institutions that make up a given Veterans Integrated Service Network (VISN), parent institution entered in the parent input parameter.

Format: CHILDREN^XUAF4(array,parent)

Input Parameters: array: (required) \$NAME reference to store the list of institutions that make up the parent VISN institution for the parent input parameter.

parent: (required) Parent (VISN) institution lookup value, any of the following:

- Internal Entry Number (IEN); has the grave accent (\`) in front of it.
- Station Number.
- Station Name.

Output: returns: Returns the array populated with the list of institutions that make up the parent VISN.

Variable array ("c",ien)=station_name^station_number

## \$\$CIRN^XUAF4(): Institution CIRN-enabled Field Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The \$\$CIRN^XUAF4 extrinsic function returns the value of the CIRN-enabled field from the INSTITUTION (#4) file.

Format: \$\$CIRN^XUAF4(inst\[,value\])

Input Parameters: inst: (required) Institution lookup value, any of the following:

- Internal Entry Number (IEN); has the grave accent (\`) in front of it.
- Station Number.
- Station Name.

value: (optional) Restricted to use by CIRN. This input parameter allows the setting of the field to a new value.

Output: returns: Returns the CIRN-enabled field value.

## F4^XUAF4(): Institution Data for a Station Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The F4^XUAF4 API returns the Internal Entry Number (IEN) and other institution data, including historical information, for a given STATION NUMBER (#99) in the INSTITUTION (#4) file.

Format: F4^XUAF4(sta,\[.\]array\[,flag\]\[,date\])

Input Parameters: sta: (required) Station Number.

\[.\]array: (required) \$NAME reference for return values.

flag: (optional) Flags that represent the Station Number Status. Possible values are:

- A—Active entries only.
- M—Medical treating facilities only.

date: (optional) Return name on this VA FileMan internal date.

> Output: ARRAY: IEN or 0^error message.

> ARRAY(“NAME”): Name.

> ARRAY(“VA NAME”): Official VA Name.

> ARRAY(“STATION NUMBER”): Station Number.

> ARRAY(“TYPE”): Facility Type Name.

> ARRAY(“INACTIVE”): Inactive Date (0=*not* inactive).

> ![](kernel-8-0-developer-s-guide-institution-file-user-guide/004.png) NOTE: If inactive date *not* available, then 1.

> ARRAY(“REALIGNED TO”): IEN^station number^date.

> ARRAY(“REALIGNED FROM”): IEN^station number^date.

> ARRAY(“MERGE”,IEN”): Merged Records.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950585" class="anchor"></span>Figure 1: F4^XUAF4 API—Example

\><span class="mark">D F4^XUAF4("528A8",.ARRAY)</span>

\><span class="mark">ZW ARRAY</span>

ARRAY=7020

ARRAY("INACTIVE")=0

ARRAY("NAME")=\<REDACTED\>

ARRAY("REALIGNED FROM")=500^500^3000701

ARRAY("STATION NUMBER")=528A8

ARRAY("TYPE")=VAMC

ARRAY("VA NAME")=\<REDACTED\> - \<REDACTED\> DIVISION

## \$\$ID^XUAF4(): Institution Identifier

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The \$\$ID^XUAF4 extrinsic function returns the Identifier (ID) of an INSTITUTION (#4) file entry for a given Coding System and Internal Entry Number (IEN).

Format: \$\$ID^XUAF4(cdsys,ien)

Input Parameters: cdsys: (required) CDSYS is an existing coding system of the INSTITUTION (#4) file. To see the existing coding system in the file:

\>D CDSYS^XUAF4(.Y)ien: (required) Internal Entry Number (IEN) of the institution in question.

Output: returns: Returns the INSTITUTION (#4) file Identifier (ID) associated with the given Coding System and IEN.

## \$\$IDX^XUAF4(): Institution IEN (Using Coding System and ID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The \$\$IDX^XUAF4 extrinsic function returns the Internal Entry Number (IEN) of an INSTITUTION (#4) file entry for a given Coding System and Identifier (ID) pair.

Format: \$\$IDX^XUAF4(cdsys,id)

Input Parameters: cdsys: (required) CDSYS is an existing coding system of the INSTITUTION (#4) file. To see the existing coding system in the file:

\>D CDSYS^XUAF4(.Y)id: (required) ID is the identifier associated with the coding system. The station number, for example, is the identifier for the VASTANUM coding system and NPI number is the ID for the NPI coding system.

Output: returns: Returns the INSTITUTION (#4) file Internal Entry Number (IEN) associated with the given Coding System and Identifier (ID).

## \$\$IEN^XUAF4(): IEN for Station Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The \$\$IEN^XUAF4 extrinsic function returns the Internal Entry Number (IEN) of the entry for a given STATION NUMBER (#99) field in the INSTITUTION (#4) file.

Format: \$\$IEN^XUAF4(sta)

Input Parameters: sta: (required) Station Number.

Output: returns: Returns:

- IEN—Internal Entry Number.
- NULL—Error.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950586" class="anchor"></span>Figure 2: \$\$IEN^XUAF4 API—Example

\><span class="mark">S X=\$\$IEN^XUAF4("528A5")</span>

\><span class="mark">W X</span>

532

## \$\$LEGACY^XUAF4(): Institution Realigned/Legacy (True/False)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The \$\$LEGACY^XUAF4 extrinsic function, given the STATION NUMBER (#99) field in the INSTITUTION (#4) file, returns the Boolean value for the question—has this station number been realigned? Is it a legacy Station Number?

Format: \$\$LEGACY^XUAF4(sta)

Input Parameters: sta: (required) The STATION NUMBER (#99) field value in the INSTITUTION (#4) file for the Station Number in question

Output: returns: Returns a Boolean value:

- True (*non*-Zero)—Station Number has been realigned; it is a legacy Station Number.
- False (Zero)—Station Number has *not* been realigned; it is *not* a legacy Station Number.

## \$\$LKUP^XUAF4(): Institution Lookup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The \$\$LKUP^XUAF4 extrinsic function returns the IEN or Zero (0) when doing a lookup on the INSTITUTION (#4) file.

Format: \$\$LKUP^XUAF4(inst)

Input Parameters: inst: (required) Institution lookup value, any of the following:

- Internal Entry Number (IEN); has the grave accent (\`) in front of it.
- Station Number.
- Station Name.

Output: returns: Returns:

- IEN—Internal Entry Number.
- Zero (0).

## LOOKUP^XUAF4(): Look Up Institution Identifier

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The LOOKUP^XUAF4 API lookup utility allows a user to select an Institution by Coding System and ID. It prompts a user for a Coding System and then prompts for an Identifier—it’s an IX^DIC API call on a New Style cross-reference of the ID (#.02) field of the IDENTIFIER (#9999) Multiple field in the INSTITUTION (#4) file.

Format: LOOKUP^XUAF4()

Input Parameters: See IX^DIC For input information, see the IX^DIC documentation in the *VA FileMan Developer’s Guide*.

Output: See IX^DIC For output information, see the IX^DIC documentation in the *VA FileMan Developer’s Guide*.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950587" class="anchor"></span>Figure 3: LOOKUP^XUAF4 API—Example

Select INSTITUTION CODING SYSTEM: <span class="mark">DMIS</span>

ID: <span class="mark">0037</span>

DMIS 0037 WALTER REED DC USAH 688CN

## \$\$MADD^XUAF4(): Institution Mailing Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The \$\$MADD^XUAF4 extrinsic function returns the mailing address information for an institution in a caret-delimited string (that is streetaddr^city^state^zip) for a given Internal Entry Number (IEN) in the INSTITUTION (#4) file.

Format: \$\$MADD^XUAF4(ien)

Input Parameters: ien: (required) Internal Entry Number (IEN) of the institution in question.

Output: returns: Returns the institution mailing address in a caret-delimited string:

streetaddr^city^state^zip

## \$\$NAME^XUAF4(): Institution Official Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The \$\$NAME^XUAF4 extrinsic function returns the OFFICIAL NAME (#100) field value in the INSTITUTION (#4) file for an institution given its Internal Entry Number (IEN). However, if Field \#100 is NULL, the NAME (#.01) field in the INSTITUTION (#4) file is returned.

Format: \$\$NAME^XUAF4(ien)

Input Parameters: ien: (required) Internal Entry Number (IEN) of the institution in question.

Output: returns: Returns either of the following:

- OFFICIAL NAME (#100) field value in the INSTITUTION (#4) file—If Field \#100 is *not*NULL.
- NAME (#.01) field value in the INSTITUTION (#4) file—If Field \#100 is NULL.

## \$\$NNT^XUAF4(): Institution Station Name, Number, and Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The \$\$NNT^XUAF4 extrinsic function returns the station information for an institution in a caret-delimited string (that is station_name^station_number^station_type) for a given Internal Entry Number (IEN) in the INSTITUTION (#4) file.

Format: \$\$NNT^XUAF4(ien)

Input Parameters: ien: (required) Internal Entry Number (IEN) of the institution in question.

Output: returns: Returns the institution station information in a caret-delimited string:

station_name^station_number^station_type

## \$\$NS^XUAF4(): Institution Name and Station Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The \$\$NS^XUAF4 extrinsic function returns the institution information in a caret-delimited string (that is institution_name^station_number) for a given Internal Entry Number (IEN) in the INSTITUTION (#4) file.

Format: \$\$NS^XUAF4(ien)

Input Parameters: ien: (required) Internal Entry Number (IEN) of the institution in question.

Output: returns: Returns the institution information in a caret-delimited string:

institution_name^station_number

## \$\$O99^XUAF4(): IEN of Merged Station Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The \$\$O99^XUAF4 extrinsic function returns the Internal Entry Number (IEN) of the valid STATION NUMBER field (#99) in the INSTITUTION (#4) file, if this entry was merged during the INSTITUTION (#4) file cleanup process (such as due to a duplicate STATION NUMBER \[#99\] field). This function may be used by application developers to re-point their INSTITUTION (#4) file references to a valid entry complete with Station Number.

Format: \$\$O99^XUAF4(ien)

Input Parameters: ien: (required) Internal Entry Number (IEN) of the institution in question.

Output: returns: Returns the Internal Entry Number (IEN) of the INSTITUTION (#4) file entry with a valid STATION NUMBER field (#99)—the Station Number deleted from the input IEN during the cleanup process (that is Kernel Patch XU\*8.0\*206).

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950588" class="anchor"></span>Figure 4: \$\$O99^XUAF4 API—Example

\><span class="mark">S NEWIEN=\$\$O99^XUAF4(6538)</span>

\><span class="mark">W NEWIEN</span>

6164

\><span class="mark">W ^DIC(4,6164,99)</span>

519HB^^^

## \$\$PADD^ XUAF4(): Institution Physical Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The \$\$PADD^ XUAF4 extrinsic function returns the physical address information for an institution in a caret-delimited string (streetaddr^city^state^zip) for a given Internal Entry Number (IEN) in the INSTITUTION (#4) file.

Format: \$\$PADD^XUAF4(ien)

Input Parameters: ien: (required) Internal Entry Number (IEN) of the institution in question.

Output: returns: Returns the institution physical address in a caret-delimited string:

streetaddr^city^state^zip

## PARENT^XUAF4(): Parent Institution Lookup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The PARENT^XUAF4 API returns a list of all institutions that make up a given Veterans Integrated Service Network (VISN), parent institution entered in the lookup input parameter.

Format: PARENT^XUAF4(array,lookup\[,type\])

Input Parameters: array: (required) \$NAME reference to store the list of the parent (VISN) institution for the lookup input parameter institution.

lookup: (required) Parent (VISN) institution lookup value, any of the following:

- Internal Entry Number (IEN); has the grave accent (\`) in front of it.
- Station Number.
- Station Name.

type: (optional) Type of institution from the INSTITUTION ASSOCIATION TYPES (#4.05) file, default is VISN.

Output: returns: Returns the array populated with the list of parent (VISN) institutions.

Variable array ("P",PIEN)=STATION_NAME^STATION_NUMBER

![](kernel-8-0-developer-s-guide-institution-file-user-guide/005.png) NOTE: With the business rule that institutions can only have one parent per type, if you specify the type input parameter, you get an array that only has one PIEN in it. If the type parameter is left blank, it finds *all* parents for the institution and lists them in the array.

## \$\$PRNT^XUAF4(): Institution Parent Facility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The \$\$PRNT^XUAF4 extrinsic function returns the parent facility institution information in a caret-delimited string (ien^station_number^name) for a given child facility STATION NUMBER (#99) field in the INSTITUTION (#4) file.

Format: \$\$PRNT^XUAF4(sta)

Input Parameters: sta: (required) The STATION NUMBER (#99) field value in the INSTITUTION (#4) file for the child facility whose parent facility information is being requested.

Output: returns: Returns the parent facility institution information in a caret-delimited string:

ien^station_number^name

## \$\$RF^XUAF4(): Realigned From Institution Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#:Description: The \$\$RF^XUAF4 extrinsic function returns the information that is pointed to in the REALIGNED FROM (#.06) field in the HISTORY (#999) Multiple field in a caret-delimited string (ien^station_number^effective_date) for a given Internal Entry Number (IEN) in the INSTITUTION (#4) file.

Format: \$\$RF^XUAF4(ien)

Input Parameters: ien: (required) Internal Entry Number (IEN) of the institution in question.

Output: returns: Returns the realigned from institution information in a caret-delimited string:

ien^station_number^effective_date

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950589" class="anchor"></span>Figure 5: \$\$RF^XUAF4 API—Example

\><span class="mark">S IEN=\$\$RF^XUAF4(7020)</span>

\><span class="mark">W IEN</span>

500^500^3000701

## \$\$RT^XUAF4(): Realigned To Institution Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#:Description: The \$\$RT^XUAF4 extrinsic function returns the information that is pointed to in the REALIGNED TO (#.05) field in the HISTORY (#999) Multiple field in a caret-delimited string (ien^station_number^effective_date) for a given Internal Entry Number (IEN) in the INSTITUTION (#4) file.

Format: \$\$RT^XUAF4(ien)

Input Parameters: ien: (required) Internal Entry Number (IEN) of the institution in question.

Output: returns: Returns the realigned to institution information in a caret-delimited string:

ien^station_number^effective_date

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950590" class="anchor"></span>Figure 6: \$\$RT^XUAF4 API—Example

\><span class="mark">S IEN=\$\$RT^XUAF4(500)</span>

\><span class="mark">W IEN</span>

7020^528A8^3000701

## SIBLING^XUAF4(): Sibling Institution Lookup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The SIBLING^XUAF4 API returns a list of all institutions that make up a given Veterans Integrated Service Network (VISN), parent institution entered in the child input parameter.

Format: SIBLING^XUAF4(array,child\[,type\])

Input Parameters: array: (required) \$NAME reference to store the list of all institutions of a parent (VISN) institution for the child input parameter institution.

child: (required) Child institution lookup value, any of the following:

- Internal Entry Number (IEN); has the grave accent (\`) in front of it.
- Station Number.
- Station Name.

type: (optional) Type of institution from the INSTITUTION ASSOCIATION TYPES (#4.05) file (default is VISN).

Output: returns: Returns the array populated with the list of all institutions of the parent (VISN) institution.

Variable array  
("P",PIEN, "C",CIEN)=STATION_NAME^STATION_NUMBER

![](kernel-8-0-developer-s-guide-institution-file-user-guide/006.png) NOTE: With the business rule that institutions can only have one parent per type, if you specify the type input parameter, you get an array that only has one PIEN in it. If the type parameter is left blank, it finds *all* parents for the institution and lists them in the array. Also, the input site (that is child input parameter) is included in the list.

## \$\$STA^XUAF4(): Station Number for IEN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The \$\$STA^XUAF4 extrinsic function returns the STATION NUMBER (#99) field for the entry of a given Internal Entry Number (IEN) in the INSTITUTION (#4) file.

Format: \$\$STA^XUAF4(ien)

Input Parameters: ien: (required) Internal Entry Number (IEN) of the institution in question.

Output: returns: Returns the Station Number.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950591" class="anchor"></span>Figure 7: \$\$STA^XUAF4 API—Example

\><span class="mark">S STA=\$\$STA^XUAF4(7020)</span>

\><span class="mark">W STA</span>

528A8

## \$\$TF^XUAF4(): Treating Facility (True/False)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The \$\$TF^XUAF4 extrinsic function, given the Internal Entry Number (IEN) in the INSTITUTION (#4) file, returns the Boolean value for the question—is this a medical treating facility?

Format: \$\$TF^XUAF4(ien)

Input Parameters: ien: (required) Internal Entry Number (IEN) of the institution in question.

Output: returns: Returns a Boolean value:

- True (*non*-Zero)—Treating facility.
- False (Zero)—Not a Treating facility.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950592" class="anchor"></span>Figure 8: \$\$TF^XUAF4 API—Example

\><span class="mark">S TF=\$\$TF^XUAF4(7020)</span>

\><span class="mark">W TF</span>

1

## \$\$WHAT^XUAF4(): Institution Single Field Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 2171

Description: The \$\$WHAT^XUAF4 extrinsic function returns the data from a single field given the Internal Entry Number (IEN) and the specific field requested in the INSTITUTION (#4) file.

Format: \$\$WHAT^XUAF4(ien,field)

Input Parameters: ien: (required) Internal Entry Number (IEN) of the institution in question (POINTER value to the INSTITUTION (#4) file.

field: (required) field number of the field in question.

Output: returns: Returns the value in the specified field.

## \$\$IEN^XUMF(): Institution IEN (Using IFN, Coding System, and ID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Institution File

ICR \#: 3795

Description: The \$\$IEN^XUMF extrinsic function returns the Internal Entry Number (IEN) for a given Internal File Number (IFN), Coding System, and Identifier (ID).

Format: \$\$IEN^XUMF(ifn,cdsys,id)

Input Parameters: ifn: (required) Internal File Number (IFN).

cdsys: (required) CDSYS is an existing coding system of the INSTITUTION (#4) file. To see the existing coding system in the file:

\>D CDSYS^XUAF4(.Y)id: (required) ID is the identifier associated with the coding system. The station number, for example, is the identifier for the VASTANUM coding system and NPI number is the ID for the NPI coding system.

Output: returns: Returns the Internal Entry Number (IEN) of the institution requested.

## MAIN^XUMFI(): HL7 Master File Message Builder

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Institution File

ICR \#: 2171

Description: The MAIN^XUMFI API implements an HL7 Master File Message Builder Interface that dynamically maps a VA FileMan field to an HL7 Master File sequence within a segment. The interface implements functionality to build the following segments:

- Master File Notification (MFN)
- Master File Query (MFQ)
- Master File Response (MFR)

The interface calls applicable VISTA HL7 GENERATE and GENACK interfaces to send/reply/broadcast an appropriate HL7 Master File message.

Format: MAIN^XUMFI(ifn,ien,type,param,error)

Input Parameters: See MAIN^XUMFP For a description of the Input parameters for this API, see the “<u>MAIN^XUMFP(): Master File Parameters</u>" API.

Output ParametersOutput: See MAIN^XUMFP For a description of the Output Parameters and Output for this API, see the “<u>MAIN^XUMFP(): Master File Parameters</u>" API.

### Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This interface should be called after the Master File Parameter API. The Master File Parameter API sets up the required parameters in the PARAM array.

The Institution File Redesign (IFR) patch (that is XU\*8.0\*206) implemented several Application Programming Interfaces (APIs). After the IFR patch was installed and the cleanup performed, the STATION NUMBER (#99) field was a unique key to the INSTITUTION (#4) file.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950593" class="anchor"></span>Figure 9: MAIN^XUMFI API—Example

\><span class="mark">D MAIN^XUMFI(4,18723,1,.PARAM,.ERROR)</span>

From the HL7 MESSAGE TEXT (#772) file, you will see the following:

<span id="_Toc199950594" class="anchor"></span>Figure 10: MAIN^XUMFI API—Sample Output

DATE/TIME ENTERED: JAN 12, 2001@09:17:29

SERVER APPLICATION: XUMF MFN TRANSMISSION TYPE: OUTGOING

MESSAGE ID: 0259 PARENT MESSAGE: JAN 12, 2001@09:17:29

PRIORITY: DEFERRED RELATED EVENT PROTOCOL: XUMF MFN

MESSAGE TYPE: SINGLE MESSAGE

MESSAGE TEXT:  

MFI^Z04^MFS^REP^20010112091729^20010112091729^NE

MFE^MUP^^19001011^631GD~STATION NUMBER~D

ZIN^GREENFIELD^631GD^National^CBOC~FACILITY TYPE~VA^^^MASSACHUSETTS^^^^^^

STATUS: SUCCESSFULLY COMPLETED

DATE/TIME PROCESSED: JAN 12, 2001@09:17:29

NO. OF CHARACTERS IN MESSAGE: 161     NO. OF EVENTS IN MESSAGE: 1

## MAIN^XUMFP(): Master File Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Institution File

ICR \#: 3354

Description: The MAIN^XUMFP API sets up required parameters used by the HL7 Master File Message Builder Interface and the HL7 Master File message handler. The interface defines required parameters and serves as a common interface for parameter initialization. This interface is the enabling component of the Master File Server (MFS) mechanism allowing VA FileMan Master Files to be maintained by the server, including files with Multiple fields and extended references.

The developer can set any param parameter before or after the interface call and override the default value.

Format: MAIN^XUMFP(ifn,ien,type,param,error)

Input Parameters: ifn: (required) Internal File Number (IFN).

ien: (required) Internal Entry Number (IEN).

Single entry (pass by value).

Example:

IEN=1

Multiple entries (pass by reference).

Example:

- IEN(1)=“”
- IEN(2)=“”

ALL national entries (pass by value).

> Example:

IEN=“ALL”

NEW entry (pass by value).

> Example:

IEN=“NEW”

type: (required) Message TYPE. Possible values are:

- 0—MFN: Unsolicited update.
- 1—MFQ: Query particular record and file.
- 3—MFQ: Query particular record in array.
- 5—MFQ: Query group records file.
- 7—MFQ: Query group records array.
- 11—MFR: Query response particular record file.
- 13—MFR: Query response particular record array.
- 15—MFR: Query response group records file.
- 17—MFR: Query response group records array.

> Input / Output Parameters:

> param: Parameter array:

- PARAM(“PROTOCOL”): IEN PROTOCOL (#101) file.
- PARAM(“BROADCAST”): Broadcast message to all VistA sites.
- PARAM(“LLNK”): Logical link in HLL(“LINKS”,*n*) format.

For more param array options, see the “<u>Details</u>” section.

Output: error: Returns:

1^Error message text

### Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Parameter          | HL7 Sequence                    | HL7 Data Type |
|--------------------|---------------------------------|---------------|
| PARAM(“QDT”)   | Query DATE/TIME             | TS        |
| PARAM(“QFC”)   | Query Format Code               | ID        |
| PARAM(“QP”)    | Query Priority                  | ID        |
| PARAM(“QID”)   | Query ID                        | ST        |
| PARAM(“DRT”)   | Deferred Response Type          | ID        |
| PARAM(“DRDT”)  | Deferred Response DATE/TIME | TS        |
| PARAM(“QLR”)   | Quantity Limited Request        | CQ        |
| PARAM(“WHO”)   | Who Subject Filter              | XCN       |
| PARAM(“WHAT”)  | What Subject Filter             | CE        |
| PARAM(“WDDC”)  | What Department Data Code       | CE        |
| PARAM(“WDCVQ”) | What Data Code Value Qual.      | CM        |
| PARAM(“QRL”)   | Query Results Level             | ID        |

<span id="_Toc199951037" class="anchor"></span>Table 2: MAIN^XUMFP(): Master File Parameters API—XCN Data Type of QRD WHO Parameter

<table>
<caption><p><span id="_Toc199951038" class="anchor"></span>Table 3: MAIN^XUMFP(): Master File Parameters API—CE Data Type of QRD WHAT Parameter</p></caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 14%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th>Component</th>
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1<sup>ST</sup> component</td>
<td></td>
<td>One of the following:</td>
</tr>
<tr class="even">
<td>NAME</td>
<td></td>
<td><blockquote>
<p>Value of NAME (#.01) field for Internal Entry Number (IEN).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>ALL</td>
<td></td>
<td><blockquote>
<p>String represents all national entries.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IEN ARRAY</td>
<td></td>
<td><blockquote>
<p>String represents entries passed in IEN array.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9<sup>th</sup> component</td>
<td><strong>D</strong></td>
<td>Source table (VA FileMan cross-reference).</td>
</tr>
<tr class="even">
<td>10<sup>th</sup> component</td>
<td><strong>045A4</strong></td>
<td>Assigning authority.</td>
</tr>
</tbody>
</table>

<span id="_Toc199951038" class="anchor"></span>Table 3: MAIN^XUMFP(): Master File Parameters API—CE Data Type of QRD WHAT Parameter

| Component                | Value     | Description           |
|--------------------------|-----------|-----------------------|
| 1<sup>ST</sup> component | 4     | Identifier            |
| 2<sup>nd</sup> component | IFN   | Text                  |
| 3<sup>rd</sup> component | VA FM | Name of Coding System |

<span id="_Toc199951039" class="anchor"></span>Table 4: MAIN^XUMFP(): Master File Parameters API—MFI: Master File Identification

| Parameter           | Description                        |
|---------------------|------------------------------------|
| PARAM(“MFI”)    | Master File Identifier             |
| PARAM(“MFAI”)   | Master File Application Identifier |
| PARAM(“FLEC”)   | File-Level Event Code              |
| PARAM(“ENDT”)   | Entered Data/Time                  |
| PARAM(“MFIEDT”) | Effective DATE/TIME            |
| PARAM(“RLC”)    | Response Level Code                |

<span id="_Toc199951040" class="anchor"></span>Table 5: MAIN^XUMFP(): Master File Parameters API—MFE: Master File Entry

| Parameter           | Description             |
|---------------------|-------------------------|
| PARAM(“RLEC”)   | Record-Level Event Code |
| PARAM(“MFNCID”) | MFN Control ID      |
| PARAM(“MFEEDT”) | Effective DATE/TIME |
| PARAM(“PKV”)    | Primary Key Value       |

<span id="_Toc199951041" class="anchor"></span>Table 6: MAIN^XUMFP(): Master File Parameters API—\[Z...\] Segments Parameters

| Parameter                           | Description                   |
|-------------------------------------|-------------------------------|
| PARAM(“SEG”,SEG)=“”             | HL7 segment name              |
| PARAM(“SEG”,SEG,“SEQ”,SEQ,FLD#) | segment sequence \# and field |

<span id="_Toc199951042" class="anchor"></span>Table 7: MAIN^XUMFP(): Master File Parameters API—Files Involving Sub-Records and Extended Reference

![](kernel-8-0-developer-s-guide-institution-file-user-guide/007.png) NOTE: If any special processing is required, in addition to the external value passed by VA FileMan, set the FLD# node equal to a formatting function:

*n*^\$\$TAG^RTN(*X*)

Where:

- *n* is the component sequence number.
- *X* is the external value from VA FileMan.

P(segment_sequence,HLCS,n)=FM_external_value

| Parameter                               | Description                   |
|-----------------------------------------|-------------------------------|
| PARAM(“SEG”,SEG,“SEQ”,SEQ,“FILE”)   | See VA FileMan documentation. |
| PARAM(“SEG”,SEG,“SEQ”,SEQ,“IENS”)   | \$\$GET1^DIQ() for value. |
| PARAM(“SEG”,SEG,“SEQ”,SEQ,“FIELD”)  | of FILE, IENS, and FIELD.     |
| PARAM(“SEG”,SEG,“SEQ”,SEQ,“KEY”)    | .01 value.                |
| PARAM(“SEG”,SEG,“SEQ”,SEQ,“FORMAT”) | format non ST data types. |

![](kernel-8-0-developer-s-guide-institution-file-user-guide/008.png) NOTE: Query group records store PARAM in the ^TMP global with the following root:

^TMP(“XUMF MFS”,\$J,“PARAM”,IEN)

For Example, MFE PKV node is:

^TMP(“XUMF MFS”,\$J,“PARAM”,IEN,“PKV”)

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Figure 11</u> is an example of a query (MFQ) for a group records array:

<span id="_Ref62625905" class="anchor"></span>Figure 11: MAIN^XUMFP API—Example

\><span class="mark">D MAIN^XUMFP(4,"ALL",7,.PARAM,.ERROR)</span>

Since query group records store PARAM in the ^TMP global, display the ^TMP global to see the PARAM values:

<span id="_Toc199950596" class="anchor"></span>Figure 12: MAIN^XUMFP API—Displaying ^TMP Global for PARAM Values

\><span class="mark">D ^%G</span>

Global ^TMP("XUMF MFS",\$J

TMP("XUMF MFS",\$J

^TMP("XUMF MFS",539017563,"PARAM","DRDT") =

^TMP("XUMF MFS",539017563,"PARAM","DRT") =

^TMP("XUMF MFS",539017563,"PARAM","ENDT") =

^TMP("XUMF MFS",539017563,"PARAM","FLEC") = UPD

^TMP("XUMF MFS",539017563,"PARAM","MFAI") =

^TMP("XUMF MFS",539017563,"PARAM","MFEEDT") = 20010212110654

^TMP("XUMF MFS",539017563,"PARAM","MFI") = Z04

^TMP("XUMF MFS",539017563,"PARAM","MFIEDT") =

^TMP("XUMF MFS",539017563,"PARAM","MFNCID") =

^TMP("XUMF MFS",539017563,"PARAM","POST") = POST^XUMFP4C

^TMP("XUMF MFS",539017563,"PARAM","PRE") = PRE^XUMFP4C

^TMP("XUMF MFS",539017563,"PARAM","PROTOCOL") = 2233

^TMP("XUMF MFS",539017563,"PARAM","QDT") = 20010212110654

^TMP("XUMF MFS",539017563,"PARAM","QFC") = R

^TMP("XUMF MFS",539017563,"PARAM","QID") = Z04 ARRAY

^TMP("XUMF MFS",539017563,"PARAM","QLR") = RD~999

^TMP("XUMF MFS",539017563,"PARAM","QP") = I

^TMP("XUMF MFS",539017563,"PARAM","QRL") =

^TMP("XUMF MFS",539017563,"PARAM","RLC") = NE

^TMP("XUMF MFS",539017563,"PARAM","RLEC") = MUP

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",1,.01) = ST

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",2,99) = ST

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",3,11) = ID

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",4,13) = CE^~FACILITY TYPE~VA

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",5,100) = ST

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",6,101) = ST

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",7,.02) = ST

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",8,"DTYP") = CE^~VISN~VA

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",8,"FIELD") = 1

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",8,"FILE") = 4.014

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",8,"IENS") = 1,?+1,

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",9,"DTYP") = ST

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",9,"FIELD") = 1:99

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",9,"FILE") = 4.014

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",9,"IENS") = 2,?+1,

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",10,"DTYP") = DT

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",10,"FIELD") = .01

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",10,"FILE") = 4.999

^TMP("XUMF MFS",539017563, PARAM","SEG","ZIN","SEQ",11,"DTYP") = ST

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",11,"FIELD") = .06:99

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",11,"FILE") = 4.999

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",12,"DTYP") = DT

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",12,"FIELD") = .01

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",12,"FILE") = 4.999

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",13,"DTYP") = ST

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",13,"FIELD") = .05:99

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",13,"FILE") = 4.999

^TMP("XUMF MFS",539017563,"PARAM","SEGMENT") = ZIN

^TMP("XUMF MFS",539017563,"PARAM","WDCVQ") =

^TMP("XUMF MFS",539017563,"PARAM","WDDC") = INFRASTRUCTURE~INFORMATION INFRASTRUCTURE ~VA TS

^TMP("XUMF MFS",539017563,"PARAM","WHAT") = 4~IFN~VA FM

^TMP("XUMF MFS",539017563,"PARAM","WHO") = ALL\~\~\~\~\~\~\~~D~045A4

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-institution-file-user-guide/009.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-institution-file-user-guide/010.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-institution-file-user-guide/011.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.