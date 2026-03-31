---
title: "Kernel 8.0 Developerâ€™s Guide: Name Standardization User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: Name Standardization"
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
  - xlfname
  - mark
  - myname
  - xuuser
  - components
  - table
  - contents
  - family
page_count: 0
word_count: 6768
section_count: 10
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_name_standardization_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_name_standardization_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259474" class="anchor"></span>Name Standardization Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-name-standardization-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-name-standardization-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Name Standardization Developer Tools User Guide</em>.</p>
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

![](kernel-8-0-developer-s-guide-name-standardization-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [\$\$BLDNAME^XLFNAME(): Build Name from Component Parts](#bldnamexlfname-build-name-from-component-parts)
    - [Details](#details)
    - [Examples](#examples)
  - [\$\$CLEANC^XLFNAME(): Name Component Standardization Routine](#cleancxlfname-name-component-standardization-routine)
    - [Examples](#examples-1)
  - [\$\$FMNAME^XLFNAME(): Convert HL7 Formatted Name to Name](#fmnamexlfname-convert-hl7-formatted-name-to-name)
    - [Details](#details-1)
    - [Examples](#examples-2)
  - [\$\$HLNAME^XLFNAME(): Convert Name to HL7 Formatted Name](#hlnamexlfname-convert-name-to-hl7-formatted-name)
    - [Details](#details-2)
    - [Examples](#examples-3)
  - [NAMECOMP^XLFNAME(): Component Parts from Standard Name](#namecompxlfname-component-parts-from-standard-name)
    - [Example](#example)
  - [\$\$NAMEFMT^XLFNAME(): Formatted Name from Name Components](#namefmtxlfname-formatted-name-from-name-components)
    - [Details](#details-3)
    - [Examples](#examples-4)
  - [STDNAME^XLFNAME(): Name Standardization Routine](#stdnamexlfname-name-standardization-routine)
    - [Details](#details-4)
    - [Example](#example-1)
  - [DELCOMP^XLFNAME2(): Delete Name Components Entry](#delcompxlfname2-delete-name-components-entry)
    - [Example](#example-2)
  - [UPDCOMP^XLFNAME2(): Update Name Components Entry](#updcompxlfname2-update-name-components-entry)
    - [Example](#example-3)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Name Standardization Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Name Standardization APIs and Extrinsic Functions are available for developers. These APIs and Extrinsic Functions are described below.

## \$\$BLDNAME^XLFNAME(): Build Name from Component Parts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Name Standardization

ICR \#: 3065

Description: The \$\$BLDNAME^XLFNAME extrinsic function takes the component parts of a name and returns the name, truncated if necessary, in the following format:

Family_name,Given_name\<space\>Middle_name\<space\>Suffix(es)

Format: \$\$BLDNAME^XLFNAME(.name\[,max\])

Input Parameters: .name: (required) The component parts of the name:

NAME("FAMILY") = Family (Last) Name

NAME("GIVEN") = Given (First) Name(s)

NAME("MIDDLE") = Middle Name(s)

NAME("SUFFIX") = Suffix(es)

Alternatively, this array can contain the file number, IENS, and field number of the field that contains the name. If the name has a corresponding entry in the NAME COMPONENTS (#20) file, then the name components are obtained from that entry. Otherwise, the name is obtained directly from the file, record, and field specified, and the name components are obtained by making a call to the <u>STDNAME^XLFNAME(): Name Standardization Routine</u> API.

> NAME("FILE") = Source file number (required)

> NAME("IENS") = IENS of entry in the source file (required)

NAME("FIELD") = Source field number (required)

max: (optional) The maximum length of the Name to be returned (default = 256).

![](kernel-8-0-developer-s-guide-name-standardization-user-guide/004.png) REF: For a description of the pruning algorithm, see the “<u>Details</u>” section.

Output: returns: Returns the name, truncated if necessary, in the following format:

Family_name,Given_name\<space\>Middle_name\<space\>Suffix(es)

### Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the max input parameter is used, and the resulting name is longer than max, the following pruning algorithm is performed to shorten the name:

1.  Truncate Middle Name from the right-most position until only the initial character is left.
2.  Drop suffix.
3.  Truncate Given Name from the right-most position until only the initial character is left.
4.  Truncate Family Name from the right-most position.
5.  Truncate the name from the right.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

Suppose the MYNAME array contains the following elements:

MYNAME("FAMILY")="XUUSER"

MYNAME("GIVEN")="SIXTY"

MYNAME("MIDDLE")="K."

MYNAME("SUFFIX")="JR"

Calls to \$\$BLDNAME^XLFNAME returns the name as follows:

<span id="_Toc199950661" class="anchor"></span>Figure 1: \$\$BLDNAME^XLFNAME API—Example 1: All Characters

\><span class="mark">S X=\$\$BLDNAME^XLFNAME(.MYNAME)</span>

\><span class="mark">W X</span>

XUUSER,SIXTY K JR

“Pruning” the name to 12 characters total:

<span id="_Toc199950662" class="anchor"></span>Figure 2: \$\$BLDNAME^XLFNAME API—Example 1: Only 12 Characters

\><span class="mark">S X=\$\$BLDNAME^XLFNAME(.MYNAME,12)</span>

\><span class="mark">W X</span>

XUUSER,SI K

#### Example 2

If an entry in the NAME COMPONENTS (#20) file stores the components of a name stored in the NAME (#.01) field of record number 32 in the NEW PERSON (#200) file, and the data in the corresponding record in the NAME COMPONENTS (#20) file is:

FILE=200

FIELD=.01

IENS="32,"

GIVEN NAME="SIXTY"

MIDDLE NAME="K."

FAMILY NAME="XUUSER"

SUFFIX="JR"

You can set:

MYNAME("FILE")=200

MYNAME("FIELD")=.01

MYNAME("IENS")="32,"

Then call \$\$BLDNAME^XLFNAME as in <u>Example 1</u>:

<span id="_Toc199950663" class="anchor"></span>Figure 3: \$\$BLDNAME^XLFNAME API—Example 2: All Characters

\><span class="mark">S X=\$\$BLDNAME^XLFNAME(.MYNAME)</span>

\><span class="mark">W X</span>

XUUSER,SIXTY K JR

“Pruning” the name to 12 characters total:

<span id="_Toc199950664" class="anchor"></span>Figure 4: \$\$BLDNAME^XLFNAME API—Example 2: Only 12 Characters

\><span class="mark">S X=\$\$BLDNAME^XLFNAME(.MYNAME,12)</span>

\><span class="mark">W X</span>

XUUSER,SI K

## \$\$CLEANC^XLFNAME(): Name Component Standardization Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Name Standardization

ICR \#: 3065

Description: The \$\$CLEANC^XLFNAME extrinsic function takes a single name component and returns that name in standard format.

Format: \$\$CLEANC^XLFNAME(comp\[,flags\])

Input Parameters: comp: (required) The name component to be converted to standard format.

flags: (optional) Flag to control processing. Possible values are:

- F—If the name component to be converted is the FAMILY (LAST) NAME, pass the F flag. With the F flag:
- Colons (:), semicolons (;), and commas (,) are converted to hyphens (-).
- Spaces and all punctuation except hyphens are removed.
- Two or more consecutive spaces or hyphens are replaced with a single space or hyphen.
- Birth position indicators 1ST through 10TH are changed to their Roman numeral equivalents.
- NULL—Without the F flag:
- The component is converted to uppercase.
- Colons (:), semicolons (;), commas (,), and periods (.) are converted to spaces.
- All punctuation except for hyphens and spaces are removed.
- Two or more consecutive spaces or hyphens are replaced with a single space or hyphen.
- Birth position indicators 1ST through 10TH are changed to their Roman numeral equivalents.

Output: returns: Returns the standard formatted name.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

Standardize family (last) name:

<span id="_Toc199950665" class="anchor"></span>Figure 5: \$\$CLEANC^XLFNAME API—Example 1

\><span class="mark">Set X=\$\$CLEANC^XLFNAME("XUUSER-XU U SER","F")</span>

\><span class="mark">W X</span>

XUUSER-XUUSER

\><span class="mark">Set X=\$\$CLEANC^XLFNAME("XUUSER-XU U SER 2ND","F")</span>

\><span class="mark">W X</span>

XUUSER-XUUSERII

\><span class="mark">Set X=\$\$CLEANC^XLFNAME("XUUSER-XU U SER")</span>

\><span class="mark">W X</span>

XUUSER-XU U SER

\><span class="mark">Set X=\$\$CLEANC^XLFNAME("ST. USER","F")</span>

\><span class="mark">W X</span>

STUSER

#### Example 2

Standardize other (*non*-family) name components:

<span id="_Toc199950666" class="anchor"></span>Figure 6: \$\$CLEANC^XLFNAME API—Example 2

\><span class="mark">S X=\$\$CLEANC^XLFNAME("F.O.")</span>

\><span class="mark">W X</span>

F O

\><span class="mark">S X=\$\$CLEANC^XLFNAME("FORTY'")</span>

\><span class="mark">W X</span>

FORTY

\><span class="mark">S X=\$\$CLEANC^XLFNAME("FORTY ONE")</span>

\><span class="mark">W X</span>

FORTY ONE

\><span class="mark">S X=\$\$CLEANC^XLFNAME("FORTY-ONE")</span>

\><span class="mark">W X</span>

FORTY-ONE

## \$\$FMNAME^XLFNAME(): Convert HL7 Formatted Name to Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Name Standardization

ICR \#: 3065

Description: The \$\$FMNAME^XLFNAME extrinsic function converts an HL7 formatted input name to a VistA formatted name.

Format: \$\$FMNAME^XLFNAME(\[.\]name\[,flags\]\[,delim\])

Input Parameters: \[.\]name: (required) This is the HL7 name to be converted; it can be passed by reference. If the C flag is used, the name components are returned in nodes descendent from this parameter (see the “[Output Parameters](#fmname_xlfname_output_parameters)” section).

flags: (optional) Flags to controls processing. Possible values are:

- C—Return name components in the NAME array (see the “[Output Parameters](#fmname_xlfname_output_parameters)” section).
- L#—Truncate the returned name to a maximum Length of \# characters; where \# is an integer between 1 and 256.
- M—Return the name in mixed case, with the first letter of each name component capitalized.
- S—Return the name in standardized form.

delim: (optional) The delimiter used in the HL7 formatted name (default = ^).

<span id="fmname_xlfname_output_parameters" class="anchor"></span>Output Parameters: name: If the flags input parameter contains a C, the component parts of the name are returned in the NAME array:

NAME("FAMILY) = Family (Last) Name  
NAME("GIVEN") = Given (First) Name(s)  
NAME("MIDDLE") = Middle Name(s)  
NAME("SUFFIX") = Suffix(es)

### Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the L# flag is used, and the resulting name is longer than \#, the following pruning algorithm is performed to shorten the name:

1.  Truncate Middle Name from the right-most position until only the initial character is left.
6.  Drop suffix.
7.  Truncate Given Name from the right-most position until only the initial character is left.
8.  Truncate Family Name from the right-most position.
9.  Truncate the name from the right.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

Convert an HL7 formatted name to a VistA name:

<span id="_Ref204333053" class="anchor"></span>Figure 7: \$\$FMNAME^XLFNAME API—Example 1

\><span class="mark">S X=\$\$FMNAME^XLFNAME("XUUSER^SIXTY^K.^JR^MR.^PHD")</span>

\><span class="mark">W X</span>

XUUSER,SIXTY K. JR

\><span class="mark">S X=\$\$FMNAME^XLFNAME("XUUSER^SIXTY^K.^JR^MR.^PHD","S")</span>

\><span class="mark">W X</span>

XUUSER,SIXTY K JR

\><span class="mark">S X=\$\$FMNAME^XLFNAME("XUUSER^SIXTY^K.^JR^MR.^PHD","M")</span>

\><span class="mark">W X</span>

Xuuser,Sixty K. Jr

\><span class="mark">S X=\$\$FMNAME^XLFNAME("XUUSER^SIXTY^K.^JR^MR.^PHD","SL12")</span>

\><span class="mark">W X</span>

XUUSER,SI K

#### Example 2

Convert an HL7 formatted name where the tilde character (~) is the delimiter to a standard name:

<span id="_Ref204339307" class="anchor"></span>Figure 8: \$\$FMNAME^XLFNAME API—Example 2

\><span class="mark">S X=\$\$FMNAME^XLFNAME("XUUSER~SIXTY~K.~JR~MR","S","~")</span>

\><span class="mark">W X</span>

XUUSER,SIXTY K JR

#### Example 3

Convert an HL7 formatted name to a standard name, and return the components of that name in the MYNAME array:

<span id="_Ref204339398" class="anchor"></span>Figure 9: \$\$FMNAME^XLFNAME API—Example 3: Converting an HL7 Formatted Name to a Standard Name, and Returning the Components in an Array

\><span class="mark">S MYNAME="XUUSER^SIXTY^K.^JR^MR.^PHD"</span>

\><span class="mark">W \$\$FMNAME^XLFNAME(.MYNAME,"CS")</span>

XUUSER,SIXTY K JR

\><span class="mark">ZW MYNAME</span>

MYNAME=XUUSER^SIXTY^K.^JR^MR.^PHD

MYNAME("DEGREE")=PHD

MYNAME("FAMILY")=XUUSER

MYNAME("GIVEN")=SIXTY

MYNAME("MIDDLE")=K.

MYNAME("PREFIX")=MR.

MYNAME("SUFFIX")=JR

## \$\$HLNAME^XLFNAME(): Convert Name to HL7 Formatted Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Name Standardization

ICR \#: 3065

Description: The \$\$HLNAME^XLFNAME extrinsic function converts an input name to an HL7 formatted name.

Format: \$\$HLNAME^XLFNAME(\[.\]name\[,flags\]\[,delim\])

Input Parameters: \[.\]name: (required) The component parts of the name to be converted:

NAME("FAMILY) = Family (Last) Name (required)  
NAME("GIVEN") = Given (First) Name(s) (optional)  
NAME("MIDDLE") = Middle Name(s) (optional)  
NAME("SUFFIX") = Suffix(es) (optional)  
NAME("PREFIX") = Prefix (optional)  
NAME("DEGREE") = Degree (optional)

Alternatively, this array can contain the file number, IENS, and field number of the field that contains the name. If the name has a corresponding entry in the NAME COMPONENTS (#20) file, then the name components are obtained from that entry. Otherwise, the name is obtained directly from the file, record, and field specified, and the name components are obtained by making a call to the <u>STDNAME^XLFNAME(): Name Standardization Routine</u> API.

NAME("FILE") = Source file number (required)  
NAME("IENS") = IENS of entry in the source file (required)  
NAME("FIELD") = Source field number (required)

Another alternative is to pass in the unsubscripted NAME parameter the name to be converted. \$\$HLNAME^XLFNAME obtains the components parts of that name by making a call to the <u>STDNAME^XLFNAME(): Name Standardization Routine</u> API. This alternative is recommended only for names that do *not* have associated entries on the NAME COMPONENTS (#20) file.

flags: (optional) Flags to controls processing. Possible values are:

- L#—Truncate the returned name to a maximum Length of \# characters; where \# is an integer between 1 and 256.
- S—Return the name components in the HL7 formatted name in Standardized form.

delim: (optional) The delimiter to use in the HL7 string  
(default is ^).

Output: returns: Returns the converted name in HL7 format.

### Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the L# flag is used, and the resulting name is longer than \#, the following pruning algorithm is performed to shorten the name:

1.  Truncate Middle Name from the right-most position until only the initial character is left.
10. Drop suffix.
11. Truncate Given Name from the right-most position until only the initial character is left.
12. Truncate Family Name from the right-most position.
13. Truncate the name from the right.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

Suppose the MYNAME array contains the following elements:

MYNAME("PREFIX")="MR."  
MYNAME("GIVEN")="SIXTY"  
MYNAME("MIDDLE")="K."  
MYNAME("FAMILY")="XUUSER"  
MYNAME("SUFFIX")="JR"  
MYNAME("DEGREE")="PHD"

Then calls to the \$\$HLNAME^XLFNAME API returns the name, as shown in <u>Figure 10</u>:

<span id="_Ref499804952" class="anchor"></span>Figure 10: \$\$HLNAME^XLFNAME API—Example 1

\><span class="mark">S X=\$\$HLNAME^XLFNAME(.MYNAME)</span>

\><span class="mark">W X</span>

XUUSER^SIXTY^K.^JR^MR.^PHD

\><span class="mark">S X=\$\$HLNAME^XLFNAME(.MYNAME,"","~")</span>

\><span class="mark">W X</span>

XUUSER~SIXTY~K.~JR~MR.~PHD

\><span class="mark">S X=\$\$HLNAME^XLFNAME(.MYNAME,"S","~")</span>

\><span class="mark">W X</span>

XUUSER~SIXTY~K~JR~MR~PHD

\><span class="mark">S X=\$\$HLNAME^XLFNAME(.MYNAME,"L12S")</span>

\><span class="mark">W X</span>

XUUSER^SI^K

#### Example 2

If an entry in the NAME COMPONENTS (#20) file stores the components of a name stored in the NAME (#.01) field of record number 32 in the NEW PERSON (#200) file, and the data in the corresponding record in the NAME COMPONENTS (#20) file is:

FILE = 200  
FIELD = .01  
IENS = "32,"  
PREFIX = "MR."  
GIVEN NAME = "SIXTY"  
MIDDLE NAME = "K."  
FAMILY NAME = "XUUSER"  
SUFFIX = "JR"  
DEGREE = "PHD"

You can set:

MYNAME("FILE") = 200  
MYNAME("FIELD") = .01  
MYNAME("IENS") = "32,"

Then call the \$\$HLNAME^XLFNAME API, as in [Example 1](#example-1-3), to return the name in various formats.

#### Example 3

Convert a name passed by value to HL7 format:

<span id="_Toc199950671" class="anchor"></span>Figure 11: \$\$HLNAME^XLFNAME API—Example 3

\><span class="mark">S X=\$\$HLNAME^XLFNAME("XUUSER,SIXTY HOWARD II")</span>

\><span class="mark">W X</span>

XUUSER^SIXTY^HOWARD^II

\><span class="mark">S X=\$\$HLNAME^XLFNAME("XUUSER,SIXTY HOWARD II","S")</span>

\><span class="mark">W X</span>

XUUSER^SIXTY^HOWARD^II

\><span class="mark">S X=\$\$HLNAME^XLFNAME("XUUSER,SIXTY HOWARD II","SL10","~")</span>

\><span class="mark">W X</span>

XUUSE~S~H

## NAMECOMP^XLFNAME(): Component Parts from Standard Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Name Standardization

ICR \#: 3065

Description: The NAMECOMP^XLFNAME API takes a name in standard format and returns in an array the component parts of that name.

Format: NAMECOMP^XLFNAME(.name)

Input Parameters: .name: (required) This parameter is the name in standard format to be parsed. NAMECOMP^XLFNAME returns the component parts of the name in nodes descendent from NAME.  
(See “Output Parameters.”)

Output Parameters: .name: The component parts of the name are returned in the NAME array passed in.

NAME("FAMILY) = Family (last) Name  
NAME("GIVEN") = Given (first) Name  
NAME("MIDDLE") = Middle Name  
NAME("SUFFIX") = Suffix(es)

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In <u>Figure 12</u>, the MYNAME variable is set to the standard name. The NAMECOMP^XLFNAME call is made to return in the MYNAME array the component parts of that name:

<span id="_Ref501446529" class="anchor"></span>Figure 12: NAMECOMP^XLFNAME API—Example

\><span class="mark">S MYNAME="XUUSER-XUUSER,FORTY ONE S MD"</span>

\><span class="mark">D NAMECOMP^XLFNAME(.MYNAME)</span>

\><span class="mark">ZW MYNAME</span>

MYNAME=XUUSER-XUUSER,FORTY ONE S MD

MYNAME("FAMILY")=XUUSER-XUUSER

MYNAME("GIVEN")=FORTY ONE

MYNAME("MIDDLE")=S

MYNAME("SUFFIX")=MD

## \$\$NAMEFMT^XLFNAME(): Formatted Name from Name Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Name Standardization

ICR \#: 3065

Description: The \$\$NAMEFMT^XLFNAME extrinsic function returns a name converted to a form useful for display.

Format: \$\$NAMEFMT^XLFNAME(.name\[,format\]\[,flags\])

Input Parameters: .name: (required) An array that contains the component parts of the name:

NAME("FAMILY) = Family (Last) Name (required)  
NAME("GIVEN") = Given (First) Name(s) (optional)  
NAME("MIDDLE") = Middle Name(s) (optional)  
NAME("SUFFIX") = Suffix(es) (optional)  
NAME("PREFIX") = Prefix (optional)  
NAME("DEGREE") = Degree (optional)

Alternatively, this array can contain the file number, IENS, and field number of the field that contains the name. If the name has a corresponding entry in the NAME COMPONENTS (#20) file, then the name components are obtained from that entry. Otherwise, the name is obtained directly from the file, record, and field specified, and the name components are obtained by making a call to the <u>STDNAME^XLFNAME(): Name Standardization Routine</u> API.

NAME("FILE") = Source file number (required)  
NAME("IENS") = IENS of entry in the source file (required)  
NAME("FIELD") = Source field number (required)

format: (optional) Controls the general formatting of the output (default = G). Possible values are:

- F—Return Family (Last) Name first.
- G—Return Given (First) Name first.
- O—Return Only the Family (Last) Name.

flags: (optional) Flags to controls processing. Possible values are:

- C—If the F format is used, return a Comma between the Family (Last) and Given (First) Names. Otherwise, the Family (Last) Name and the Given (First) Name are separated by a space. (Ignored if the F format is *not* used.)
- D—Return the Degree.
- Dc—Return the Degree preceded by a comma and space.
- L#—Truncate the returned name to a maximum Length of \# characters; where \# is an integer between 1 and 256. See the “<u>Details</u>” section for a description of the pruning algorithm.
- M—Return the name in Mixed case, with the first letter of each name component capitalized.
- P—Return the Prefix.
- S—Standardize the name components before building formatted name.
- Xc—Precede the SuffiX with a comma and space.

Output: returns: Returns the formatted name.

### Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the L# flag is used, and the resulting name is longer than \#, the following pruning algorithm is performed to shorten the name:

1.  Drop Degree.
14. Drop Prefix.
15. Truncate Middle Name from the right-most position until only the initial character is left.
16. Drop suffix.
17. Truncate Given Name from the right-most position until only the initial character is left.
18. Truncate Family Name from the right-most position.
19. Truncate the name from the right.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

Suppose the MYNAME array contains the following elements:

MYNAME("PREFIX")="MR."

MYNAME("GIVEN")="SIXTY"

MYNAME("MIDDLE")="K."

MYNAME("FAMILY")="XUUSER"

MYNAME("SUFFIX")="JR"

MYNAME("DEGREE")="PHD"

Then calls to the \$\$NAMEFMT^XLFNAME API returns the name as follows:

<span id="_Toc199950673" class="anchor"></span>Figure 13: \$\$NAMEFMT^XLFNAME API—Example 1

\><span class="mark">S X=\$\$NAMEFMT^XLFNAME(.MYNAME,"F")</span>

\><span class="mark">W X</span>

XUUSER SIXTY K. JR

\><span class="mark">S X=\$\$NAMEFMT^XLFNAME(.MYNAME,"F","C")</span>

\><span class="mark">W X</span>

XUUSER,SIXTY K. JR

\><span class="mark">S X=\$\$NAMEFMT^XLFNAME(.MYNAME,"F","CS")</span>

\><span class="mark">W X</span>

XUUSER,SIXTY K JR

\><span class="mark">S X=\$\$NAMEFMT^XLFNAME(.MYNAME,"F","CSD")</span>

\><span class="mark">W X</span>

XUUSER,SIXTY K JR PHD

\><span class="mark">S X=\$\$NAMEFMT^XLFNAME(.MYNAME,"F","CDcXc")</span>

\><span class="mark">W X</span>

XUUSER,SIXTY K., JR, PHD

\><span class="mark">S X=\$\$NAMEFMT^XLFNAME(.MYNAME,"F","CSL12")</span>

\><span class="mark">W X</span>

XUUSER,SI K

\><span class="mark">S X=\$\$NAMEFMT^XLFNAME(.MYNAME,"F","CMD")</span>

\><span class="mark">W X</span>

Xuuser,Sixty K. Jr PhD

\><span class="mark">S X=\$\$NAMEFMT^XLFNAME(.MYNAME,"G")</span>

\><span class="mark">W X</span>

SIXTY K. XUUSER JR

\><span class="mark">S X=\$\$NAMEFMT^XLFNAME(.MYNAME,"G","D")</span>

\><span class="mark">W X</span>

SIXTY K. XUUSER JR PHD

\><span class="mark">S X=\$\$NAMEFMT^XLFNAME(.MYNAME,"G","Dc")</span>

\><span class="mark">W X</span>

SIXTY K. XUUSER JR, PHD

\><span class="mark">S X=\$\$NAMEFMT^XLFNAME(.MYNAME,"G","P")</span>

\><span class="mark">W X</span>

MR. SIXTY K. XUUSER JR

\><span class="mark">S X=\$\$NAMEFMT^XLFNAME(.MYNAME,"G","Xc")</span>

\><span class="mark">W X</span>

SIXTY K. XUUSER, JR

\><span class="mark">S X=\$\$NAMEFMT^XLFNAME(.MYNAME,"G","PDcXc")</span>

\><span class="mark">W X</span>

MR. SIXTY K. XUUSER, JR, PHD

\><span class="mark">S X=\$\$NAMEFMT^XLFNAME(.MYNAME,"G","PDcXcM")</span>

\><span class="mark">W X</span>

Mr. Sixty K. Xuuser, Jr, PhD

\><span class="mark">S X=\$\$NAMEFMT^XLFNAME(.MYNAME,"G","S")</span>

\><span class="mark">W X</span>

SIXTY K XUUSER JR

\><span class="mark">S X=\$\$NAMEFMT^XLFNAME(.MYNAME,"G","SL12")</span>

\><span class="mark">W X</span>

SI K XUUSER

\><span class="mark">S X=\$\$NAMEFMT^XLFNAME(.MYNAME,"O")</span>

\><span class="mark">W X</span>

XUUSER

\><span class="mark">S X=\$\$NAMEFMT^XLFNAME(.MYNAME,"O","S")</span>

\><span class="mark">W X</span>

XUUSER

\><span class="mark">S X=\$\$NAMEFMT^XLFNAME(.MYNAME,"O","M")</span>

\><span class="mark">W X</span>

Xuuser

\><span class="mark">S X=\$\$NAMEFMT^XLFNAME(.MYNAME,"O","L3")</span>

\><span class="mark">W X</span>

XU

#### Example 2

If an entry in the NAME COMPONENTS (#20) file stores the components of a name stored in the NAME (#.01) field of record number 32 in the NEW PERSON (#200) file, and the data in the corresponding record in the NAME COMPONENTS (#20) file is:

FILE = 200

FIELD = .01

IENS = "32,"

PREFIX = "MR."

GIVEN NAME = "SIXTY"

MIDDLE NAME = "K."

FAMILY NAME = "XUUSER"

SUFFIX = "JR"

DEGREE = "PHD"

You can set:

MYNAME("FILE")=200

MYNAME("FIELD")=.01

MYNAME("IENS")="32,"

Then call the \$\$NAMEFMT^XLFNAME API, as in [Example 1](#example-1-4), to return the name in various formats.

## STDNAME^XLFNAME(): Name Standardization Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Name Standardization

ICR \#: 3065

Description: The STDNAME^XLFNAME API parses a name and converts it into the following standard format:

Family_name,Given_name\<space\>Middle_name\<space\>Suffix(es)

A name in standard format is entirely in uppercase and contains no Arabic numerals. The Family_name (last name) portion of a standard name appears to the left of the comma and contains no spaces and no punctuation except hyphens (-). The other parts of a standard name (the portion to the right of the comma) contain no punctuation except for hyphens and spaces. NMI and NMN are *not* used for the Middle_name.

STDNAME^XLFNAME optionally returns in an array the component parts of the name. It also optionally returns information in an array about possible problems encountered during the conversion of the name to standard form and the parsing of the name into its component parts.

Format: STDNAME^XLFNAME(.name\[,flags\]\[,.audit\])

Input Parameters: .name: (required) The name to be converted to standard format. It is assumed that the name is in the general format:

Family_name,Given_name(s) Middle_name Suffix(es)

If the F flag is *not* used, and the name contains no comma, it is assumed the name is in the general format:

Given_name(s) Middle_name Family_name Suffix(es)

The standard form of the name is returned in the NAME variable. If the C flag is passed in, the components of the name are returned in nodes descendent from NAME. (See the “Output Parameters” section.)

flags: (optional) Flags to control processing. Possible values are:

- C—Return name components in the NAME array. (See the “Output Parameters” section.)
- F—If the name passed in the name input parameter does *not* contain a comma, assume it is the Family Name only. For example, if the name input is “ST USER”, return the name as “STUSER” instead of “USER,ST”.
- G—Do *not* return AUDIT(“GIVEN”) even if the Given Name is missing.
- P—Remove text in parentheses ( ), brackets \[ \], or braces { } from the name. If such text is removed, return AUDIT(“STRIP”).

.audit: (optional) If provided, this is an array that STDNAME^XLFNAME returns if there are any ambiguities or possible problems in standardizing the name or parsing the name into component parts. (See the “Output Parameters” section.)

> Output Parameters: name: This parameter is set to the name that was input converted to standard format.

> If the flags input parameter contains a C, the component parts of the name are returned in the NAME array:

NAME("FAMILY) = Family (Last) Name  
NAME("GIVEN") = Given (First) Name(s)  
NAME("MIDDLE") = Middle Name  
NAME("SUFFIX") = Suffix(es)

audit: If this parameter is set to the original name that was passed in the name parameter. In addition, if there were any problems in the interpretation of the name being standardized, descendants of audit are set:

AUDIT(“*SUBSCRIPT*”) = “”

Where “*SUBSCRIPT*” can be any one of the following:

- AUDIT(“FAMILY”)—The Family Name starts with ST. (The period and space are removed from the Family Name. For example, the name “ST. USER” is converted to “STUSER”.)
- AUDIT(“GIVEN”)—Returned if there is no Given Name and the G flag is *not* passed.
- AUDIT(“MIDDLE”)—Returned if there are three or more names between the first comma and the Suffix(es). (All name parts except the last are assumed to be part of the Given Name. Only the last part is assumed to be the Middle Name.)
- AUDIT(“NM”)—Returned if NMI or NMN appears to be used as the Middle Name. (NMI and NMN are removed from the standard name, and the Middle Name component is returned as NULL.)
- AUDIT(“NOTE”)—Returned if the name appears to contain a note or flag that may *not* actually be part of the name. For example, the name starts with C- or EEE or has FEE at the end.
- AUDIT(“NUMBER”)—Returned if a name part (other than a valid numeric Suffix) contains a number.
- AUDIT(“PERIOD”)—Returned if periods were removed.
- AUDIT(“PUNC”)—Returned if punctuation was removed.
- AUDIT(“SPACE”)—Returned if spaces were removed from the Family Name.
- AUDIT(“STRIP”)—Returned if text in parentheses ( ), brackets \[ \], or braces { } were removed from the Name. (This is done only if the P flag is passed.)
- AUDIT(“SUFFIX”)—Returned if:
- Suffix(es) are found immediately to the left of the 1st comma.
- I, V, or X, and nothing else except valid suffixes, appear immediately after the Given Name. (It is interpreted as the Middle Name.)
- The name immediately after the Given Name appears to be a *non*-numeric suffix (except I, V, and X), and everything after that also appear to be suffixes. (It is assumed there are a Given Name and Suffix(es), but no Middle Name.)
- M.D. or M D is found at the end of the name, or before any valid suffixes at the end of the name. (It is assumed that M and D are initials in the Given or Middle Name rather than a Suffix.)
- The name part before any recognizable suffixes is more than one character in length and does *not* contain any vowels or Y. It is interpreted as a suffix.
- Suffix is found between commas immediately after the Family Name.

### Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Standard Name

In forming the standard name, the following changes are made:

1.  The name is converted to uppercase.
20. In the Family Name:
1.  Semicolons (;) and colons (:) are converted to hyphens (-).  
      
    Spaces and all other punctuation except hyphens are removed.
2.  Spaces and all other punctuation except hyphens are removed.
21. In the other name parts (Given Name, Middle Name, and Suffix).
1.  Semicolon, colons, commas (,), and periods (.) are converted to spaces.  
      
    Spaces and all other punctuation except hyphens are removed.
3.  All punctuation except hyphens and spaces are removed.
22. Hyphens and spaces at the beginning and end of the name are removed.
23. Two or more consecutive hyphens/spaces are replaced with a single hyphen/space.
24. Any suffixes immediate preceding the comma are moved to the end.
25. The suffixes indicating birth positions 1st, 2nd, 3rd, ..., 10th are converted to their Roman numeral equivalents I, II, III, … X.
26. DR immediately after the comma (or if there is no comma, at the beginning of the name), is assumed to be a suffix and moved to the end of the name.
27. Any suffixes between two commas immediate after the Family Name are moved to the end of the name.
28. NMI or NMN used as a Middle Name is deleted.

#### Component Parts Name

In forming the component parts of the name, only the following changes are made:

1.  The name component is converted to uppercase.
29. In the Family Name, semicolons (;) and colons (:) are converted to hyphens (-).
30. In the other name parts (Given Name, Middle Name, and Suffix), semicolons, colons, and commas (,) are converted to spaces.
31. Hyphens and spaces at the beginning and end of the name are removed.
32. Two or more consecutive hyphens/spaces are replaced with a single hyphen/space.
33. A Middle Name of NMI or NMN is changed to NULL.
34. Spaces after periods are removed.
35. Accent graves (\`) and carets (^) are removed.

In parsing the name into its component parts, if the name contains a comma or the F flag is passed, STDNAME^XLFNAME looks for suffixes immediately to the left of the first comma, and at the very end of the name. The suffixes it recognizes are 1ST through 10TH, JR, SR, DR, MD, ESQ, DDS, RN, ARNP, DO, PA, and Roman numerals I through X.

![](kernel-8-0-developer-s-guide-name-standardization-user-guide/005.png) NOTE: The ARNP, DO, and PA suffixes were added with Kernel Patch XU\*8.0\*535.

If a name part before any recognizable suffixes is more than one character in length, and contains no vowel or Y, it is also assumed to be a suffix. The Name Standardization looks for the DR suffix immediately after the first comma, and for any suffix between two commas immediately after the Family Name. The portion of the name to the left of the comma, less any suffixes, is assumed to be the Family Name.

After STDNAME^XLFNAME accounts for all Suffixes, it looks at the portion of the name after the comma. It assumes that the first space-delimited piece is the Given Name. If any other pieces are left, the last one (rightmost) is assumed to be the Middle Name, and anything else is appended to the end of the Given Name.

If the name contains no comma, and the F flag is *not* passed, STDNAME^XLFNAME looks for suffixes at the very end of the name. The last space-delimited piece before any suffixes is assumed to be the Family Name. The first space-delimited piece is assumed to be the Given Name. If any other pieces are left, the last one (rightmost) is assumed to be the Middle Name, and anything else is appended to the end of the Given Name.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In this example, the MYNAME variable is set to the name to be standardized. The C flag indicates that the name components should be returned in the MYNAME array, and the P flag indicates that parenthetical text should be removed from the name. STDNAME^XLFNAME sets MYAUD to original name passed in and sets nodes in the MYAUD array to flag changes and possible problems.

<span id="_Toc199950674" class="anchor"></span>Figure 14: STDNAME^XLFNAME API—Example

\><span class="mark">S MYNAME="XUUSER,FIFTY A. B. 2ND (TEST)"</span>

\><span class="mark">D STDNAME^XLFNAME(.MYNAME,"CP",.MYAUD)</span>

\><span class="mark">ZW MYNAME</span>

MYNAME=XUUSER,FIFTY A B II

MYNAME("FAMILY")=XUUSER

MYNAME("GIVEN")=FIFTY A.

MYNAME("MIDDLE")=B.

MYNAME("SUFFIX")=2ND

\><span class="mark">ZW MYAUD</span>

MYAUD=XUUSER,FIFTY A. B. 2ND (TEST)

MYAUD("MIDDLE")=""

MYAUD("PERIOD")=""

MYAUD("SPACE")=""

MYAUD("STRIP")=""

STDNAME^XLFNAME returned the standard form of the name in MYNAME as XUUSER,FIFTY A B II. It interpreted FIFTY A. as the given (first) name and B. as the middle name. Since this may *not* be correct, MYAUD(“MIDDLE”) is set. Periods were removed and spaces were removed to form the standard name, therefore MYAUD(“PERIOD”) and MYAUD(“SPACE”) were set. Finally, since the parenthetical text (TEST) was removed, MYAUD(“STRIP”) was set.

## DELCOMP^XLFNAME2(): Delete Name Components Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Name Standardization

ICR \#: 3066

Description: The DELCOMP^XLFNAME2 API deletes an entry in the NAME COMPONENTS (#20) file, and optionally, the value of the POINTER in the source file that points to the name components entry.

![](kernel-8-0-developer-s-guide-name-standardization-user-guide/006.png) NOTE: The DELCOMP^XLFNAME2 API is designed to be used in the KILL logic for the MUMPS cross-reference mentioned in the <u>UPDCOMP^XLFNAME2(): Update Name Components Entry</u> API.

Format: DELCOMP^XLFNAME2(file,\[.\]record,field\[,ptrfield\])

Input Parameters: file: (required) The number of the file or Multiple (the “source file”) that contains the name.

\[.\]record: (required) The IENS or the Internal Entry Number array (that looks like the DA array) of the record in the source file that contains the name.

field: (required) The number of the field in the source file that contains the name.

ptrfield: (optional) The number of the POINTER field in the source file that points to the NAME COMPONENTS (#20) file. Only if this parameter is passed is the value of this POINTER field deleted.

Output: none. Deletes record.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Suppose that you have a NAME COMPONENTS (#20) file entry that contains the components of a name stored in File \#1000, Record \#132, Field \#.01. The POINTER Field \#1.1 of that File \#1000 is a POINTER to the NAME COMPONENTS (#20) file. To delete the entry in the NAME COMPONENTS (#20) file, and the value of the POINTER field, you can do the following:

<span id="_Toc199950675" class="anchor"></span>Figure 15: DELCOMP^XLFNAME2 API—Example

\><span class="mark">D DELCOMP^XLFNAME(1000,132,.01,1.1)</span>

## UPDCOMP^XLFNAME2(): Update Name Components Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: Name Standardization

ICR \#: 3066

Description: The UPDCOMP^XLFNAME2 API updates an entry in the NAME COMPONENTS (#20) file. Optionally, the POINTER in the source file that points to the name components entry is also updated.

This API is designed to be used in the SET logic of a MUMPS cross-reference on the NAME field in a source file, to keep the NAME field and the associated name components in sync. For an example of its use, see the ANAME index in the INDEX (#.11) file. The ANAME index is a MUMPS cross-reference on the NAME (#.01) field of the NEW PERSON (#200) file. If an entry’s NAME field is edited, the ANAME cross-reference updates the associated entry in the NAME COMPONENTS (#20) file.

![](kernel-8-0-developer-s-guide-name-standardization-user-guide/007.png) NOTE: Existing MUMPS cross-references on the NAME COMPONENTS (#20) file already exist to update the associated NAME field on the source file if the components are edited.

Format: UPDCOMP^XLFNAME2(file,\[.\]record,field,\[.\]name\[,ptrfield\]  
\[,ptrval\])

Input Parameters: file: (required) The number of the file or Multiple (the “source file”) that contains the name.

\[.\]record: (required) The IENS or the Internal Entry Number array (that looks like the DA array) of the record in the source file that contains the name.

field: (required) The number of the field in the source file that contains the name.

\[.\]name: (required) An array that contains the component parts of the name to store in the NAME COMPONENTS (#20) file entry:

NAME("FAMILY) = Family Name (required)  
NAME("GIVEN") = Given Name(s) (optional)  
NAME("MIDDLE") = Middle Name(s) (optional)  
NAME("SUFFIX") = Suffix(es) (optional)  
NAME("PREFIX") = Prefix (optional)  
NAME("NOTES") = optional free text string

Alternatively, a name in standard format can be passed in the name input parameter. If the name input parameter has no descendants \[that is \$D(NAME)=1\], UPDCOMP^XLFNAME2 makes a call to the <u>NAMECOMP^XLFNAME(): Component Parts from Standard Name</u> API to build the NAME array for you.

ptrfield: (optional) The number of the POINTER field in the source file that points to the NAME COMPONENTS (#20) file. Only if this parameter is passed is the value of this POINTER field updated with the entry number of the record in the NAME COMPONENTS (#20) file that was added or edited.

ptrval: (optional) The current value of the POINTER field specified by the ptrfield input parameter. This parameter can be used to save processing time. If both ptrfield and ptrval are passed, the POINTER field is updated only if this value is different from the entry number of the record in the NAME COMPONENTS (#20) file that was added or edited.

Output: returns: Updated entry in the NAME COMPONENTS (#20) file.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Suppose the .01 field of File \#1000 contains a person’s name, and the component parts of the name in entry 132 should be updated as follows:

- Family (last) name: XUUSER
- Given (first) name: FIFTY HENRY
- Middle name: A.
- Suffix: JR.

Field \#1.1 is defined as a POINTER to the NAME COMPONENTS (#20) file and has a value of 42, the IEN of a record in the NAME COMPONENTS (#20) file. To update the NAME COMPONENTS (#20) file with this name, you can do the following:

<span id="_Toc199950676" class="anchor"></span>Figure 16: UPDCOMP^XLFNAME2 API—Example

\><span class="mark">S MYNAME("FAMILY")="XUUSER"</span>

\><span class="mark">S MYNAME("GIVEN")="FIFTY HENRY"</span>

\><span class="mark">S MYNAME("MIDDLE")="A."</span>

\><span class="mark">S MYNAME("SUFFIX")="JR."</span>

\><span class="mark">D UPDCOMP^XLFNAME2(1000,132,.01,.MYNAME,1.1,42)</span>

If there is an entry in the NAME COMPONENTS (#20) file that corresponds to File \#1000, Field \#.01, IEN \#132, that entry is updated with the name components passed in the MYNAME array. Otherwise, a new entry is added to the name components with this information.

If the entry in the name components that was updated or added is record \#42, no change is made to the value of the POINTER field \#1.1, since 42 was passed in the 6th parameter.

MUMPS cross-references on the NAME COMPONENTS (#20) file updates the name in the Field \#.01 of File \#1000 to “XUUSER,FIFTY HENRY A JR” if it does *not* already contain that name.

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-name-standardization-user-guide/008.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-name-standardization-user-guide/009.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-name-standardization-user-guide/010.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.