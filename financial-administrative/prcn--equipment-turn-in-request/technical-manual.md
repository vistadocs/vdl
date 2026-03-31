---
title: PRCN Version 1 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: PRCN
app_name: Equipment / Turn-In Request
section: FIN
app_status: active
pkg_ns: PRCN
patch_ver: 1
patch_id: PRCN*1
group_key: "PRCN:PRCN:1"
file_numbers: []
security_keys: []
menu_options: 12
description: > [Installation Guide/Release Notes (combined or separate documents) User Manual](#table-of-contents)
audience: 
keywords: 
  - blockquote
  - table
  - contents
  - href
  - bookmark
  - equipment
  - turn
  - request
  - class
  - chapter
page_count: 0
word_count: 4925
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 1996
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Equip_Turn-In_Request/prcn_1_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Equip_Turn-In_Request/prcn_1_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=113"
---

> [Department of Veterans Affairs Decentralized Hospital Computer Program](\l)

[EQUIPMENT/TURN-IN REQUEST TECHNICAL MANUAL](#_bookmark0)

> [Version 1.0 June 1996](#_bookmark0)

> [Information Resource Management Field Office Washington, DC](#_bookmark0)

## [PREFACE](\l)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Technical Manual Package Security Guide](#table-of-contents)

> [Installation Guide/Release Notes (combined or separate documents) User Manual](#table-of-contents)

[This document uses a paragraph numbering system that helps the reader understand how the sections of the document relate to each other. For example, suppose this paragraph was section 1.3. Under the numbering system, this paragraph would be the main paragraph for the third section of Chapter 1. If there were two subsections to this section, they would be numbered sections 1.3.1 and](#table-of-contents)

[1.3.2. A paragraph numbered 1.3.5.4.7 would be the seventh subsection of the fourth subsection of the fifth subsection of the third subsection of Chapter 1](#table-of-contents)

> Preface
# [CHAPTER 2 IMPLEMENTATION AND MAINTENANCE](\l)


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [PREFACE](#preface)
- [CHAPTER 2 IMPLEMENTATION AND MAINTENANCE](#chapter-2-implementation-and-maintenance)
- [CHAPTER 3 ROUTINE DESCRIPTIONS](#chapter-3-routine-descriptions)
- [CHAPTER 4 FILE LIST](#chapter-4-file-list)
- [CHAPTER 5 EXPORTED OPTIONS](#chapter-5-exported-options)
    - [Turn-In Menus](#turn-in-menus)
    - [Menu Diagram for PRCN NX EQ COMM MENU](#menu-diagram-for-prcn-nx-eq-comm-menu)
- [CHAPTER 6 CROSS REFERENCES](#chapter-6-cross-references)
- [CHAPTER 7 ARCHIVING AND PURGING](#chapter-7-archiving-and-purging)
- [CHAPTER 8 CALLABLE ROUTINES](#chapter-8-callable-routines)
- [CHAPTER 9 EXTERNAL RELATIONS](#chapter-9-external-relations)
- [CHAPTER 10 INTERNAL RELATIONS](#chapter-10-internal-relations)
- [CHAPTER 11 PACKAGE-WIDE VARIABLES](#chapter-11-package-wide-variables)
- [CHAPTER 12 ON-LINE DOCUMENTATION](#chapter-12-on-line-documentation)
- [GLOSSARY](#glossary)
[This section addresses specific information that is needed to run this module.](#table-of-contents)
> [^PRCS (410) - 1 block per entry (2237 Request)](#table-of-contents)
> [^PRCN(413) - 2 blocks per entry (Equipment Request)](#table-of-contents)
> [^PRCN(413.1) - 2 blocks per entry (Turn-In Request)](#table-of-contents)
[It is recommended that the PRCN global be journaled.](#table-of-contents)
[The PRCN global is created when loading as a virgin install. PRCN should be defined with access privileges; RWD for System, World, Group and UCI, using](#table-of-contents)
[%GLOMAN for DSM and %GCH for MSM. This should be the same access level as the Engineering and IFCAP globals. This global contains all the Equipment/Turn- In Request files used in the package](#table-of-contents)
> Implentation and Maintenance

# [CHAPTER 3 ROUTINE DESCRIPTIONS](\l)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[The Equipment/Turn-In Request routines use the PRCN namespace.](#table-of-contents)

> [Routine Descriptions](#table-of-contents)

> [Routine Descriptions](#_bookmark11)

> [Routine Descriptions](#table-of-contents)

# [CHAPTER 4 FILE LIST](\l)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[This section of the Equipment/Turn-In Request Version 1.0, Technical Manual, provides a listing of all Equipment/Turn-In Request files with their associated VA FileMan security access, and brief descriptions of the type of data stored there.](#table-of-contents)

> [*Warning:* Do NOT use VA FileMan to edit any of the files directly! Using FileMan will compromise system integrity. Use the menu options.](#table-of-contents)

413. [<u>EQUIPMENT REQUEST</u>](#table-of-contents)

[This is the main file containing all non-expendable equipment requests.](#table-of-contents)

1.  [<u>TURN-IN REQUEST</u>](#table-of-contents)

[This file contains all the turn-in equipment requests, both those requests that are for replacement equipment and those requests that are for excess equipment.](#table-of-contents)

2.  [<u>EQUIPMENT COMMITTEE</u>](#table-of-contents)

[This file contains the members of the Equipment Committee who will meet to decide the fate of non-expendable equipment requests.](#table-of-contents)

3.  [<u>CONCURRING OFFICIALS</u>](#table-of-contents)

[This file contains a list of users most frequently used as concurring officials to review, and approve non-expendable equipment requests.](#table-of-contents)

4.  [<u>SPECIAL HANDLING CODES</u>](#table-of-contents)

[This file contains the types of codes for items that may need special handling when ordered.](#table-of-contents)

5.  [<u>NX STATUS</u>](#table-of-contents)

[This file maintains all statuses needed for the equipment and turn-in request process.](#table-of-contents)

> [<u>413.7</u> <u>COUNTER</u>](#table-of-contents)

[This file is used to produce the temporary transaction numbers for both equipment requests and turn-in requests.](#table-of-contents)

> [File List](\l)

[The Equipment/Turn-In Request Version 1.0, package files contain files that are nationally controlled, and generally carry a high level of file protection with regard<span id="_bookmark17" class="anchor"></span> to Delete, Read, Write, and Laygo access, and local data files which do allow Delete, Read, Write, and Laygo access. The data dictionaries for any Equipment/Turn-In file should NOT be altered.](#table-of-contents)

[The package has eight (8) levels of VA FileManager, file protection enabled on its files.](#table-of-contents)

1.  [None - where no special security is enabled](#table-of-contents)
2.  [\# - Site Manager access](#table-of-contents)
3.  [@ - Programmer access to files](#table-of-contents)
4.  [% - Delete Access](#table-of-contents)
5.  [\[ - READ Access](#table-of-contents)
6.  [\] - WRITE Access](#table-of-contents)
7.  [\$ - LAYGO Access](#table-of-contents)
8.  [^ - Cannot be accessed at all](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><a href="#table-of-contents"><strong>4.4 Files with Security Access</strong></a></p>
</blockquote></th>
<th colspan="6"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p><a href="#table-of-contents">DD</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">RD</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">WR</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">DEL</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">LAYGO</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="#table-of-contents">NAME</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">NUMBER</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">ACCESS</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">ACCESS</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">ACCESS</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">ACCESS</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">ACCESS</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="#table-of-contents">---------------------------------</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">-------------</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">------------</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">------------</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">------------</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">------------</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">------------</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="#table-of-contents">EQUIPMENT REQUEST</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">413</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">@</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">[</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">]</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">%</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">$</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="#table-of-contents">TURN-IN REQUEST</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">413.1</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">@</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">[</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">]</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">%</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">$</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="#table-of-contents">EQUIPMENT</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">413.2</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">@</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">[</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">]</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">%</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">$</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="#table-of-contents">COMMITTEE</a></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="#table-of-contents">CONCURRING</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">413.3</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">@</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">[</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">]</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">%</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">$</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="#table-of-contents">OFFICIALS</a></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="#table-of-contents">SPECIAL HANDLING</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">413.4</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">@</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">[</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">]</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">@</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">@</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="#table-of-contents">CODES</a></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="#table-of-contents">NX STATUS</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">413.5</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">@</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">[</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">]</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">@</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">@</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="#table-of-contents">COUNTER</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">413.7</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">@</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">[</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">]</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">@</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">@</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

# [CHAPTER 5 EXPORTED OPTIONS](\l)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[The following chart displays the exported Equipment/Turn-In Request Version 1.0, options listed by primary menu with associated Security Keys that are to be assigned to particular users.](#table-of-contents)

[You will probably want to review the menus and security keys currently assigned to users. The following table shows the menus and associated security keys to be assigned to each type of user.](#table-of-contents)

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><a href="#table-of-contents"><strong>User</strong></a></p>
</blockquote></th>
<th><blockquote>
<p><a href="#table-of-contents"><strong>Menu Text (seen by user)</strong></a></p>
</blockquote></th>
<th><blockquote>
<p><a href="#table-of-contents"><strong>Name (used by computer)</strong></a></p>
</blockquote></th>
<th><blockquote>
<p><a href="#table-of-contents"><strong>Associated Security key(s)</strong></a></p>
</blockquote></th>
<th><blockquote>
<p><a href="#table-of-contents"><strong>Electronic Signature</strong></a></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><a href="#table-of-contents">Requestor</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">Equipment Request Menu</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">PRCN NX MENU</a></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><a href="#table-of-contents">NO</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="#table-of-contents">CMR Official</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">CMR Official Menu</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">PRCN NX CMR MENU</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">PRCNCMR</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">YES</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="#table-of-contents">Personal Property Manager</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">PPM Menu</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">PRCN NX PPM MENU</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">PRCNPPM PRCNRNK</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">YES</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="#table-of-contents">Engineering</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">Engineering Equipment Request Menu</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">PRCN NX ENG MENU</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">PRCNEN</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">YES</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="#table-of-contents">Concurring Officials</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">Equipment Concurring Official Menu</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">PRCN NX CONC MENU</a></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><a href="#table-of-contents">YES</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="#table-of-contents">Equipment Committee Members</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">Equipment Committee Menu</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">PRCN NX EQ COMM</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">PRCNEQP PRCNRNK</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">NO</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

> [Exported Options](#table-of-contents)

### [Turn-In Menus](\l)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><a href="#table-of-contents"><strong>User</strong></a></p>
</blockquote></th>
<th><blockquote>
<p><a href="#table-of-contents"><strong>Menu Text (seen by user)</strong></a></p>
</blockquote></th>
<th><blockquote>
<p><a href="#table-of-contents"><strong>Name (used by computer)</strong></a></p>
</blockquote></th>
<th><blockquote>
<p><a href="#table-of-contents"><strong>Associated Security key(s)</strong></a></p>
</blockquote></th>
<th><blockquote>
<p><a href="#table-of-contents"><strong>Electronic Signature</strong></a></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><a href="#table-of-contents">Requestor</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">Process Turn-Ins</a></p>
<p><a href="#table-of-contents">Menu</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">PRCN TURN</a></p>
<p><a href="#table-of-contents">MENU</a></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><a href="#table-of-contents">NO</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="#table-of-contents">CMR Official</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">Process Turn-Ins Menu</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">PRCN TURN MENU</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">PRCNCMR</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">YES</a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><a href="#table-of-contents">Personal Property Manager</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">Process Turn-In Request</a></p>
<p><a href="#table-of-contents">Disposition Turn-<span id="_bookmark19" class="anchor"></span> in Request</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">PRCN TURN PPM</a></p>
<p><a href="#table-of-contents">PRCN TURN DISP</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">PRCNPPM</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">YES</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="#table-of-contents">Warehouse</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">Process Turn-in Request</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">PRCN TURN WHSE</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">PRCNWHSE</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#table-of-contents">YES</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

[Please note that these are only suggested menus. Individual menus may be customized, provided the appropriate security keys and electronic signature authority have also been included.](#table-of-contents)

> [Enter New Equipment Request PRCN NX NEW](#table-of-contents)

> [Edit Equipment Request PRCN NX EDIT](#table-of-contents)

> [Cancel Equipment Request PRCN NX CANCEL](#table-of-contents)

> [Request Status Report PRCN NX CMR STATUS Display/Print Equipment Request (CMR) PRCN NX CMR DISPLAY Approve Equipment Requests (CMR Official) PRCN NX CMR APP Resubmit Request (CMR) PRCN NX CMR RESUBMIT Process Equipment Turn-Ins Menu ... PRCN TURN MENU](#table-of-contents)

> [June 1996 Equipment/Turn-In Request Version 1.0 13](#table-of-contents)

> [Exported Options](#_bookmark2)

> [Review Equipment Requests (Concurring Official) PRCN NX CONCUR](#_bookmark2)

> [Approve Equipment Request (Engineering) PRCN NX ENG](#_bookmark2)

> [Exported Options](#_bookmark2)

> [Committee review.](#_bookmark2)

> [Enter New Equipment Request Edit Equipment Request Cancel Equipment Request Request Status Report](#_bookmark2)

> [Display/Print Equipment Request Split Equipment Request Resubmit Equipment Requests Process Equipment Turn-Ins Menu](#_bookmark2)

> [Exported Options](#_bookmark2)

> [has been received status.](#_bookmark2)

> [Review Equipment Requests (PPM) PRCN NX PPM](#_bookmark2)

> [Edit Equipment Requests (PPM) PRCN NX PPM EDIT Cancel Equipment Request PRCN NX PPM CANCEL](#_bookmark2)

> [Request Status Report PRCN NX EQ RANK](#_bookmark2)

> [Create 2237 (PPM) PRCN NX PPM 2237](#_bookmark2)

> [Display/Print Equipment Requests (PPM) PRCN NX PPM DISPLAY Equipment Request Reports Menu ... PRCN REPORTS](#_bookmark2)

> [Process Equipment Turn-Ins Menu ... PRCN TURN MENU](#_bookmark2)

> [Exported Options](#_bookmark2)

> [Since the request has already passed all steps, it is not necessary for it to go back through the process.](#_bookmark2)

> [Exported Options](#_bookmark2)

> [Controlled Item Report PRCN NX CONTROLLED ITEM Turn-In Status by CMR Report PRCN NX TURN BY CMR](#_bookmark2)

> [Turn-In Status by Service Report PRCN NX TURN BY SERVICE Turn-In Status Report PRCN NX TURN BY STATUS Turn-In Status by Transaction \# Report PRCN NX TURN BY TRANS Request Status Report PRCN NX STATUS](#_bookmark2)

> [Enter Equipment Turn-In Request PRCN TURN ENTER Edit Equipment Turn-In Request PRCN TURN EDIT](#_bookmark2)

> [Cancel Turn-In Request PRCN TURN CANCEL Approve Equipment Turn-In Request (CMR) PRCN TURN CMR APP Process Equipment Turn-In Request (PPM) PRCN TURN PPM Final Turn-In Request Disposition (PPM PRCN TURN DISP Display/Print Turn-In Request PRCN TURN PRINT](#_bookmark2)

> [Edit Turn-In Transaction (PPM) PRNC TURN PPM EDIT](#_bookmark2)

> [Exported Options](#_bookmark2)

[Exported Options](\l)

[Name: PRCNPURGE](#_bookmark2)

[Type: Run Routine Routine: PRCNPURG Lock:](\l)

[Menu Text: Purge Equipment and Turn-In Requests](\l)

[Description: This option is a TaskMan process to purge completed and cancelled equipment and turn-in requests.](#_bookmark2)

[Equipment Request Menu (Requestor) Enter New Equipment Request Edit Equipment Request Cancel Equipment Request Request Status Report](#_bookmark2)

> [Process Turn-Ins Menu](#_bookmark2)

> [Enter Equipment Turn-In Request Edit Equipment Turn-In Request Cancel Turn-In Request Display/Print Turn-In Request](#_bookmark2)

> [Approve Equipment Turn-In Request (CMR) Process Equipment Turn-In Request (PPM) Final Turn-In Request Disposition (PPM) Edit Turn-In Transaction (PPM)](#_bookmark2)

> [Resubmit Equipment Requests Split Equipment Requests](#_bookmark2)

> [Display/Print Equipment Requests (Requestor)](#_bookmark2)

> [Exported Options](\l)

[CMR Official Equipment Request Menu Enter New Equipment Request Edit Equipment Request](#_bookmark2)

> [Cancel Equipment Request Request Status Report](#_bookmark2)

> [Display/Print Equipment Request (CMR) Approve Equipment Requests (CMR) Resubmit Request (CMR)](#_bookmark2)

> [Process Turn-Ins Menu](#_bookmark2)

> [Enter Equipment Turn-In Request Edit Equipment Turn-In Request Cancel Turn-In Request<span id="_bookmark23" class="anchor"></span> Display/Print Turn-In Request](#_bookmark2)

> [Approve Equipment Turn-In Request (CMR) Process Equipment Turn-In Request (PPM) Final Turn-In Request Disposition (PPM) Edit Turn-In Transaction (PPM)](#_bookmark2)

[Equipment Request Menu (PPM)](#_bookmark2)

> [Review Equipment Requests (PPM) Edit Equipment Requests (PPM) Cancel Equipment Requests](#_bookmark2)

> [Rank Equipment Requests Create 2237 (PPM)](#_bookmark2)

> [Display/Print Equipment Requests (PPM) Equipment Request Reports Menu](#_bookmark2)

> [Controlled Equipment Report Request Status Report](#_bookmark2)

> [Turn-In Status by CMR Official Report Turn-In Status by Service Report](#_bookmark2)

> [Turn-In Status by Transaction Number Report Turn-In Status Report](#_bookmark2)

> [Process Turn-Ins Menu](#_bookmark2)

> [Enter Equipment Turn-In Request Edit Equipment Turn-In Request Cancel Turn-In Request Display/Print Turn-In Request](#_bookmark2)

> [Approve Equipment Turn-In Request (CMR) Process Equipment Turn-In Request (PPM) Final Turn-In Request Disposition (PPM) Edit Turn-In Transaction (PPM)](#_bookmark2)

[Exported Options](\l)

### [Menu Diagram for PRCN NX EQ COMM MENU](\l)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[Equipment Committee Menu Rank Equipment Requests](\l)

> [Equipment Request Summary Report Outstanding Equipment Requests Report Process Equipment Committee Decisions Service Priority Report](#_bookmark2)

[Engineering Equipment Request Menu Approve Equipment Request](#_bookmark2)

[Equipment Concurring Official Menu Review Equipment Requests](#_bookmark2)

[Warehouse Turn-In Menu](#_bookmark2)

> [Process Equipment Turn-In Request Display/Print Turn-In Request](#_bookmark2)

> [Exported Options](#_bookmark2)

# [CHAPTER 6 CROSS REFERENCES](\l)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[(413,.01) TRANSACTION NUMBER 0;1](#_bookmark6)

> [Xref 1: 413^B](#_bookmark6)

> [Set: S ^PRCN(413,"B",\$E(X,1,30),DA)=""](#_bookmark6)

> [Kill: K ^PRCN(413,"B",\$E(X,1,30),DA)](#_bookmark6)

[Desc: This cross-reference is by the generated transaction number. (413,2) REQUESTING SERVICE 0;3](#_bookmark6)

> [Xref 1: Set: Kill: Desc:](#_bookmark6)

> [(413,4.5) CMR](#_bookmark6)

> [Xref 1: Create: Delete: Field Desc:](#_bookmark6)

> [0;16](#_bookmark6)

> [Xref 1: 413^AD](#_bookmark6)

> [Set: S ^PRCN(413,"AD",\$E(X,1,30),DA)=""](#_bookmark6)

> [Kill: K ^PRCN(413,"AD",\$E(X,1,30),DA)](#_bookmark6)

[Desc: This is a cross-reference by the CMR responsible official. (413,6) REQUEST STATUS 0;7](#_bookmark6)

> [Xref 1: Set: Kill: Desc:](#_bookmark6)

> [413^AC](#_bookmark6)

> [S ^PRCN(413,"AC",\$E(X,1,30),DA)=""](#_bookmark6)

> [K ^PRCN(413,"AC",\$E(X,1,30),DA)](#_bookmark6)

> [This is a cross-reference by request status.](#_bookmark6)

<table>
<colgroup>
<col style="width: 62%" />
<col style="width: 21%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><a href="#_bookmark4">Cross References</a></p>
</blockquote></th>
<th colspan="2"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><a href="#_bookmark4">(413,15) LINE ITEM</a></p>
<p><a href="#_bookmark4">(413.015,.01) LINE ITEM NUMBER</a></p>
</blockquote></td>
<td><p><a href="#_bookmark4">1;0</a></p>
<p><a href="#_bookmark4">0;1</a></p></td>
<td><blockquote>
<p><a href="#_bookmark4">(Multiple)</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

> [Xref 1: 413.015^B](#_bookmark4)

> [Set: S ^PRCN(413,DA(1),1,"B",\$E(X,1,30),DA)=""](#_bookmark4)

> [Kill: K ^PRCN(413,DA(1),1,"B",\$E(X,1,30),DA)](#_bookmark4)

> [Desc: This cross-reference is by the Line Item Number.](#_bookmark4)

[(413,28) UTILITIES REQUIRED 3;0 (Multiple)](#_bookmark4)

[(413.028,.01) UTILITIES REQUIRED 0;1](#_bookmark4)

> [Xref 1: 413.028^B](#_bookmark4)

> [Set: S ^PRCN(413,DA(1),3,"B",\$E(X,1,30),DA)=""](#_bookmark4)

> [Kill: K ^PRCN(413,DA(1),3,"B",\$E(X,1,30),DA)](#_bookmark4)

> [Desc: This cross-reference is by utility.](#_bookmark4)

> [(413,30) SERVICE CONTACT 2;14](#_bookmark4)

> [Xref 1: TRIGGER^413^31](#_bookmark4)

> [Create: S X=\$P(\$G(^VA(200,X,.13)),U,2)](#_bookmark4)

> [Delete: @](#_bookmark4)

> [Field: \#31](#_bookmark4)

> [Desc: The Service Contact phone field is triggered from the Office Phone field in the New Person file (.132).](#_bookmark4)

[(413,34) CMR PRIORITY 2;18](#_bookmark4)

> [Xref 1: 413^P^MUMPS](#_bookmark4)

> [Set: S SK=0 D XREF^PRCNCMRP K SK Kill: S SK=1 D XREF^PRCNCMRP K SK](#_bookmark4)

> [Desc: This cross-reference sets the priority by the requestor's service so that all requests are ranked by service.](#_bookmark4)

[(413,46) CONCURRING OFFICIALS 5;0 (Multiple)](#_bookmark4)

[(413.046,.01) CONCURRRING OFFICIALS 0;1](#_bookmark4)

> [Xref 1: 413.046^B](#_bookmark4)

> [Set: S ^PRCN(413,DA(1),5,"B",\$E(X,1,30),DA)=""](#_bookmark4)

> [Kill: K ^PRCN(413,DA(1),5,"B",\$E(X,1,30),DA)](#_bookmark4)

> [Desc: This cross-reference is by concurring official.](#_bookmark4)

[Cross References](#_bookmark3)

[(413,49) EQUIPMENT COMMITTEE RANKING 6;3](#_bookmark3)

> [Xref 1: 413^E](#_bookmark3)

> [Set: S ^PRCN(413,"E",\$E(X,1,30),DA)=""](#_bookmark3)

> [Kill: K ^PRCN(413,"E",\$E(X,1,30),DA)](#_bookmark3)

> [Desc: This is the ranking by importance of requests by the Equipment Committee or their designated surrogate.](#_bookmark3)

[------------------------------------------------------------------------------------------------------------------](#_bookmark3)

[----](#_bookmark3)

[(413.1,.01) TRANSACTION CODE 0;1](#_bookmark3)

> [Xref 1: 413.1^B](#_bookmark3)

> [Set: S ^PRCN(413.1,"B",\$E(X,1,30),DA)=""](#_bookmark3)

> [Kill: K ^PRCN(413.1,"B",\$E(X,1,30),DA)](#_bookmark3)

[Desc: This cross-reference is by the generated transaction number. (413.1,5) CMR RESPONSIBLE OFFICIAL 0;6](#_bookmark3)

> [Xref 1: 413.1^AD](#_bookmark3)

> [Set: S ^PRCN(413.1,"AD",\$E(X,1,30),DA)=""](#_bookmark3)

> [Kill: K ^PRCN(413.1,"AD",\$E(X,1,30),DA)](#_bookmark3)

[Desc: This cross-reference is by the CMR responsible offical. (413.1,6) REQUEST STATUS 0;7](#_bookmark3)

> [Xref 1: Set: Kill: Desc:](#_bookmark3)

[(413.1,15) CMR](#_bookmark3)

> [Xref 1: Create: Delete: Field: Desc:](#_bookmark3)

> [0;16](#_bookmark3)

> [Cross References](#_bookmark5)

[(413.1,20) TURN-IN LINE ITEM 1;0 (Multiple)](#_bookmark5)

[(413.11,.01) REPLACEMENT ITEM NUMBER 0;1](#_bookmark5)

> [Xref 1: 413.11^B](#_bookmark5)

> [Set: S ^PRCN(413.1,DA(1),1,"B",\$E(X,1,30),DA)=""](#_bookmark5)

> [Kill: K ^PRCN(413.1,DA(1),1,"B",\$E(X,1,30),DA)](#_bookmark5)

> [Desc: This is the regular cross-reference by line item.](#_bookmark5)

> [Xref 2: 413.1^AB](#_bookmark5)

> [Set: S ^PRCN(413.1,"AB",\$E(X,1,30),DA(1),DA)=""](#_bookmark5)

> [Kill: K ^PRCN(413.1,"AB",\$E(X,1,30),DA(1),DA)](#_bookmark5)

> [Desc: This cross-reference is used to check to see if an inventoried item already has a turn-in request on file.](#_bookmark5)

> [Xref 3: TRIGGER^413.11^3](#_bookmark5)

> [Create: S X=\$P(^ENG(6914,X,0),U,2)](#_bookmark5)

> [Delete: @](#_bookmark5)

> [Field: \#3](#_bookmark5)

[Desc: This is triggered from the Equipment Inventory file (413.11,2) EQUIP REQUEST LINE ITEM 0;3](#_bookmark5)

> [Xref 1: 413.11^AC](#_bookmark5)

> [Set: S ^PRCN(413.1,DA(1),1,"AC",\$E(X,1,30),DA)=""](#_bookmark5)

> [Kill: K ^PRCN(413.1,DA(1),1,"AC",\$E(X,1,30),DA)](#_bookmark5)

> [Desc: This cross-reference is to be used to check against the quantity of equipment request line item for editing/entering associated replacement items.](#_bookmark5)

[------------------------------------------------------------------------------------------------------------------](#_bookmark5)

[----](#_bookmark5)

[(413.2,.01) MEMBER NAME 0;1](#_bookmark5)

> [Xref 1: 413.2^B](#_bookmark5)

> [Set: S ^PRCN(413.2,"B",\$E(X,1,30),DA)=""](#_bookmark5)

> [Kill: K ^PRCN(413.2,"B",\$E(X,1,30),DA)](#_bookmark5)

> [Desc: This cross-reference by Equipment Committee member.](#_bookmark5)

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 36%" />
<col style="width: 21%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><a href="#_bookmark5">(413.2,3) SCHEDULED MEETINGS</a></p>
<p><a href="#_bookmark5">(413.23,.01) MEETING DATE</a></p>
</blockquote></th>
<th><p><a href="#_bookmark5">1;0</a></p>
<p><a href="#_bookmark5">0;1</a></p></th>
<th><blockquote>
<p><a href="#_bookmark5">(Multiple)</a></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><a href="#_bookmark5">Xref 1:</a></p>
</blockquote></td>
<td colspan="3"><blockquote>
<p><a href="#_bookmark5">413.23^B</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="#_bookmark5">Set:</a></p>
</blockquote></td>
<td colspan="3"><blockquote>
<p><a href="#_bookmark5">S ^PRCN(413.2,DA(1),1,"B",$E(X,1,30),DA)=""</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

[Cross References](#_bookmark2)

> [Kill: K ^PRCN(413.2,DA(1),1,"B",\$E(X,1,30),DA)](#_bookmark2)

> [Desc: This cross-reference is by the scheduled meeting date.](#_bookmark2)

[------------------------------------------------------------------------------------------------------------------](#_bookmark2)

[----](#_bookmark2)

[(413.3,.01) NAME 0;1](#_bookmark2)

> [Xref 1; 413.3^B](#_bookmark2)

> [Set: S ^PRCN(413.3,"B",\$E(X,1,30),DA)=""](#_bookmark2)

> [Kill: K ^PRCN(413.3,"B",\$E(X,1,30),DA)](#_bookmark2)

> [Desc: This cross-reference is by concurring official.](#_bookmark2)

> [Xref 2:TRIGGER^413.3^1](#_bookmark2)

> [Create: S X=\$P(^VA(200,X,0),U,9)](#_bookmark2)

> [Delete: NO EFFECT Field: \#1](#_bookmark2)

[(413.4,.01) CODE 0;1](#_bookmark2)

> [Xref 1: 413.4^B](#_bookmark2)

> [Set: S ^PRCN(413.4,"B",\$E(X,1,30),DA)=""](#_bookmark2)

> [Kill: K ^PRCN(413.4,"B",\$E(X,1,30),DA)](#_bookmark2)

> [Desc: This cross-reference is by the special handling code.](#_bookmark2)

[------------------------------------------------------------------------------------------------------------------](#_bookmark2)

[----](#_bookmark2)

[(413.5,.01) STATUS 0;1](#_bookmark2)

> [Xref 1: 413.5^B](#_bookmark2)

> [Set: S ^PRCN(413.5,"B",\$E(X,1,30),DA)=""](#_bookmark2)

> [Kill: K ^PRCN(413.5,"B",\$E(X,1,30),DA)](#_bookmark2)

> [Desc: This cross-reference is by the status.](#_bookmark2)

[------------------------------------------------------------------------------------------------------------------](#_bookmark2)

[----](#_bookmark2)

[(413.7,.01) CODE 0;1](#_bookmark2)

> [June 1996 Equipment/Turn-In Request Version 1.0 33](#_bookmark2)

> [Cross References](#_bookmark5)

> [Xref 1: 413.7^B](#_bookmark5)

> [Set: S ^PRCN(413.7,"B",\$E(X,1,30),DA)=""](#_bookmark5)

> [Kill: K ^PRCN(413.7,"B",\$E(X,1,30),DA)](#_bookmark5)

> [Desc: This cross-reference is by the counter's identifying code.](#_bookmark5)

[Cross References](#_bookmark6)

> [Archiving and Purging](\l)

# [CHAPTER 7 ARCHIVING AND PURGING](\l)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[Archiving with the Equipment/Turn-In Request Module has not been addressed at this time.](#_bookmark6)

[There is a routine to purge completed equipment, turn-in requests, and cancelled equipment and turn-in requests.](#_bookmark6)

# [CHAPTER 8 CALLABLE ROUTINES](\l)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[Please see Chapter 9 External Relations for information on access to other packages.](#_bookmark6)

> [Callable Routines](#_bookmark6)

# [CHAPTER 9 EXTERNAL RELATIONS](\l)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[Your system must be running KERNEL Version 7 or higher, VA FileMan Version 19 or higher, in order for you to successfully operate Equipment/Turn-In Request Module, Version 1.0. Also, you must have loaded Engineering patch 7\*25 prior to installation of this package.](#_bookmark6)

[Equipment/Turn-In Request package, Version 1.0 has references to other files that are not in the file number range for the package. Turn-ins, in particular, must reference current inventoried items that are maintained by the Engineering Service. Also, the creation of 2237s references other IFCAP routines and files.](#_bookmark6)

> [Integration Reference \#1341](#_bookmark6)

> [NAME: DBIA1341-A ENTRY: 1341 CUSTODIAL PACKAGE: ENGINEERING Washington](#_bookmark6)

[SUBSCRIBING PACKAGE: EQUIPMENT/TURN-IN REQUEST Washington](#_bookmark6)

<table>
<colgroup>
<col style="width: 54%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><a href="#_bookmark6">USAGE: Private</a></p>
</blockquote></th>
<th><blockquote>
<p><a href="#_bookmark6">APPROVED: APPROVED</a></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><a href="#_bookmark6">STATUS: Active</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark6">EXPIRES:</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="#_bookmark6">DURATION: Till Otherwise Agr</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark6">VERSION:</a></p>
<p><a href="#_bookmark6">TYPE: Routine</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

[Version 1.0 of the Non-Expendable Equipment/Turn-In Request Module will call the Engineering Work Order Module in order to create a work order for equipment that must be disconnected before final turn-in can occur.](#_bookmark6)

> [NAME: DBIA1341-B ENTRY: 1342 CUSTODIAL PACKAGE: ENGINEERING Washington](#_bookmark6)

[SUBSCRIBING PACKAGE: EQUIPMENT/TURN-IN REQUEST Washington USAGE: Private APPROVED: APPROVED STATUS: Active EXPIRES:](#_bookmark6)

> [DURATION: Till Otherwise Agr VERSION:](#_bookmark6)

> [FILE: 6914 ROOT: ENG(6914](#_bookmark6)

> [TYPE: File](#_bookmark6)

[The Non-expendable Equipment/Turn-In Request Module requests permission to point to file 6914.](#_bookmark6)

> [External Relations](#_bookmark6)

> [NAME: DBIA1341-C ENTRY: 1343 CUSTODIAL PACKAGE: ENGINEERING Washington](#_bookmark6)

[SUBSCRIBING PACKAGE: EQUIPMENT/TURN-IN REQUEST Washington](#_bookmark6)

<table>
<colgroup>
<col style="width: 54%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><a href="#_bookmark6">USAGE: Private</a></p>
</blockquote></th>
<th><blockquote>
<p><a href="#_bookmark6">APPROVED: APPROVED</a></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><a href="#_bookmark6">STATUS: Active</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark6">EXPIRES:</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="#_bookmark6">DURATION: Till Otherwise Agr FILE: 6914.1</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark6">VERSION:</a></p>
<p><a href="#_bookmark6">ROOT: ENG(6914.1</a></p>
<p><a href="#_bookmark6">TYPE: File</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

[The Non-expendable Equipment/Turn-in Request Module requests permission to point the CMR file, 6914.1.](#_bookmark6)

> [NAME: DBIA1341-D ENTRY: 1344 CUSTODIAL PACKAGE: ENGINEERING Washington](#_bookmark6)

[SUBSCRIBING PACKAGE: EQUIPMENT/TURN-IN Washington USAGE: Private APPROVED: APPROVED STATUS: Active EXPIRES:](#_bookmark6)

> [DURATION: Till Otherwise Agr VERSION:](#_bookmark6)

> [FILE: 6920 ROOT: ENG(6920](#_bookmark6)

> [TYPE: File](#_bookmark6)

[This reference is to the WORK ORDER \# file in Engineering for items which must have a work order created in order to remove or disconnect the item by the Engineering department.](#_bookmark6)

> [NAME: DBIA1341-E ENTRY:1345 CUSTODIAL PACKAGE: ENGINEERING Washington](#_bookmark6)

[SUBSCRIBING PACKAGE: EQUIPMENT/TURN-IN REQUEST Washington USAGE: Private APPROVED: APPROVED STATUS: Active EXPIRES:](#_bookmark6)

> [DURATION: Till Otherwise Agr VERSION:](#_bookmark6)

> [FILE: 6910 ROOT: DIC(6910](#_bookmark6)

> [TYPE: File](#_bookmark6)

[The ENG INIT PARAMETERS file is checked for the entry of the EQUIPMENT TURN-IN SECTION field.](#_bookmark6)

[External Relations](#_bookmark8)

> [NAME: DBIA1341-F ENTRY: 1346 CUSTODIAL PACKAGE: ENGINEERING Washington](#_bookmark8)

[SUBSCRIBING PACKAGE: EQUIPMENT/TURN-IN Washington USAGE: Private APPROVED: APPROVED STATUS: Active EXPIRES:](#_bookmark8)

> [DURATION: Till Otherwise Agr VERSION:](#_bookmark8)

> [TYPE: Routine](#_bookmark8)

[FMS requires FA code sheets on capitalized equipment and FD code sheets when dispositioned. Turn-In items must be sure that the appropriate FA and FD code sheets have been done before finalizing the turn-in.](#_bookmark8)

[ROUTINE: ENFAUTL](#_bookmark8)

> [NAME: DBIA1341-H ENTRY: 1348 CUSTODIAL PACKAGE: ENGINEERING Washington](#_bookmark8)

[SUBSCRIBING PACKAGE: EQUIPMENT/TURN-IN REQUEST Washington](#_bookmark8)

<table>
<colgroup>
<col style="width: 54%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><a href="#_bookmark8">USAGE: Private</a></p>
</blockquote></th>
<th><blockquote>
<p><a href="#_bookmark8">APPROVED: APPROVED</a></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><a href="#_bookmark8">STATUS: Active</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark8">EXPIRES:</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="#_bookmark8">DURATION: Till Otherwise Agr FILE: 6925</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark8">VERSION:</a></p>
<p><a href="#_bookmark8">ROOT: ENG('PROJ',</a></p>
<p><a href="#_bookmark8">TYPE: File</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

[The Equipment/Turn-In module asks permission to display projects, their description and to pull the Chief Engineer Name if exists for inclusion in Equipment Request if necessary.](#_bookmark8)

> [NAME: DBIA1341-I ENTRY: 1349 CUSTODIAL PACKAGE: ENGINEERING Washington](#_bookmark8)

[SUBSCRIBING PACKAGE: EQUIPMENT/TURN-IN REQUEST Washington USAGE: Private APPROVED: APPROVED STATUS: Active EXPIRES:](#_bookmark8)

> [DURATION: Till Otherwise Agr VERSION:](#_bookmark8)

> [FILE: 6928 ROOT: ENG('SP',](#_bookmark8)

[TYPE: File Equipment/Turn-In module asks permission to access the Location file (#6928) to identify where new equipment may be located and where equipment will need to be picked up from when being turned in.](#_bookmark8)

> [External Relations](#_bookmark6)

> [NAME: DBIA1520-A ENTRY: 1520 CUSTODIAL PACKAGE: IFCAP Washington](#_bookmark6)

[SUBSCRIBING PACKAGE: EQUIPMENT/TURN-IN REQUEST Washington](#_bookmark6)

<table>
<colgroup>
<col style="width: 54%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><a href="#_bookmark6">USAGE: Private</a></p>
</blockquote></th>
<th><blockquote>
<p><a href="#_bookmark6">APPROVED: APPROVED</a></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><a href="#_bookmark6">STATUS: Active</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark6">EXPIRES:</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="#_bookmark6">DURATION: Till Otherwise Agr</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark6">VERSION:</a></p>
<p><a href="#_bookmark6">TYPE: Routine</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

[The NX Module (Equipment/Turn-In) requests permission to use IFCAP program PRCFSITE to set special IFCAP variables used in the package.](#_bookmark6)

[ROUTINE: PRCFSITE](#_bookmark6)

> [NAME: DBIA1520-B ENTRY: 1521 CUSTODIAL PACKAGE: IFCAP Washington](#_bookmark6)

[SUBSCRIBING PACKAGE: EQUIPMENT/TURN-IN REQUEST Washington USAGE: Private APPROVED: APPROVED STATUS: Active EXPIRES:](#_bookmark6)

> [DURATION: Till Otherwise Agr VERSION:](#_bookmark6)

[TYPE: Routine The NX module (Equipment/Turn-In) requests permission to reference program PRCSEB when creating 2237s.](#_bookmark6)

[ROUTINE: PRCSEB](#_bookmark6)

> [NAME: DBIA1520-C ENTRY: 1522 CUSTODIAL PACKAGE: IFCAP Washington](#_bookmark6)

[SUBSCRIBING PACKAGE: EQUIPMENT/TURN-IN REQUEST Washington USAGE: Private APPROVED: APPROVED STATUS: Active EXPIRES:](#_bookmark6)

> [DURATION: Till Otherwise Agr VERSION:](#_bookmark6)

> [NAME: DBIA1520-D ENTRY: 1523 CUSTODIAL PACKAGE: IFCAP Washington](#_bookmark6)

[SUBSCRIBING PACKAGE: EQUIPMENT/TURN-IN REQUEST Washington](#_bookmark6)

<table>
<colgroup>
<col style="width: 54%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><a href="#_bookmark6">USAGE: Private</a></p>
</blockquote></th>
<th><blockquote>
<p><a href="#_bookmark6">APPROVED: APPROVED</a></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><a href="#_bookmark6">STATUS: Active</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark6">EXPIRES:</a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><a href="#_bookmark6">DURATION: Till Otherwise Agr</a></p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark6">VERSION:</a></p>
<p><a href="#_bookmark6">TYPE: Routine</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

[This agreement will allow the NX (Equipment/Turn-In) module to call the IFCAP transaction utility program when creating 2237s which will create the record in file 410 and process all checks on creating a 2237.](#_bookmark6)

[ROUTINE: PRCSUT3](#_bookmark6)

> [NAME: DBIA1520-E ENTRY: 1524 CUSTODIAL PACKAGE: IFCAP Washington](#_bookmark6)

[SUBSCRIBING PACKAGE: EQUIPMENT/TURN-IN REQUEST Washington USAGE: Private APPROVED: APPROVED STATUS: Active EXPIRES:](#_bookmark6)

> [DURATION: Till Otherwise Agr VERSION:](#_bookmark6)

> [FILE: 410 ROOT: PRCS(410,](#_bookmark6)

> [TYPE: File](#_bookmark6)

[The NX (Equipment/Turn-In) module requests permission to reference file 410 to create/edit 2237s which are the end product of this module. Includes addition of two templates to file 410, PRCN2237 and PRCN2237E.](#_bookmark6)

> [NAME: DBIA1520-F ENTRY: 1525 CUSTODIAL PACKAGE: IFCAP Washington](#_bookmark6)

[SUBSCRIBING PACKAGE: EQUIPMENT/TURN-IN REQUEST Washington USAGE: Private APPROVED: APPROVED STATUS: Active EXPIRES:](#_bookmark6)

> [DURATION: Till Otherwise Agr VERSION:](#_bookmark6)

> [FILE: 440 ROOT: PRC(440,](#_bookmark6)

> [TYPE: File](#_bookmark6)

[This agreement requests permission for the NX (Equipment/Turn-In) module to point, with read access only, to the Vendor file (440).](#_bookmark6)

> [External Relations](#_bookmark6)

> [NAME: DBIA 1548-A ENTRY: 1548](#_bookmark6)

> [FILE: 3.1 ROOT: DIC(3.1](#_bookmark6)

> [TYPE: File](#_bookmark6)

[The Equipment/Turn-In Request module would like read access to the .01 field of the Title file (#3.1) for identification of other officials which are needed to review and concur with requests.](#_bookmark6)

> [NAME: DBIA1548-B ENTRY: 1549 CUSTODIAL PACKAGE: IFCAP Washington](#_bookmark6)

[SUBSCRIBING PACKAGE: EQUIPMENT/TURN-IN Washington USAGE: Private APPROVED: APPROVED STATUS: Active EXPIRES:](#_bookmark6)

> [DURATION: Till Otherwise Agr VERSION:](#_bookmark6)

> [FILE: 411 ROOT: PRC(411,](#_bookmark6)

> [TYPE: File](#_bookmark6)

[The Equipment/Turn-In Request package would like access to IFCAP's file ADMIN. ACTIVITY SITE PARAMETER (#411) to identify a station for requests and 2237s.](#_bookmark6)

> [NAME: DBIA1548-C ENTRY: 1550 CUSTODIAL PACKAGE: IFCAP Washington](#_bookmark6)

[SUBSCRIBING PACKAGE: EQUIPMENT/TURN-IN Washington USAGE: Private APPROVED: APPROVED STATUS: Active EXPIRES:](#_bookmark6)

> [DURATION: Till Otherwise Agr VERSION:](#_bookmark6)

> [FILE: 410.2 ROOT: PRCS(410.2](#_bookmark6)

> [NAME: DBIA1548-D ENTRY: 1551 CUSTODIAL PACKAGE: IFCAP Washington](#_bookmark9)

[SUBSCRIBING PACKAGE: EQUIPMENT/TURN-IN Washington USAGE: Private APPROVED: APPROVED STATUS: Active EXPIRES:](#_bookmark9)

> [DURATION: Till Otherwise Agr VERSION:](#_bookmark9)

> [FILE: 410.7 ROOT: PRCS(410.7](#_bookmark9)

[TYPE: File The SORT GROUP file (#410.7) is used as a sorting mechanism of requests to categorize their particular cost distribution for 2237s. The Equipment/Turn-In](#_bookmark9)

[Request package would like to prompt for this information early in the request and then pass it on to the 2237.](#_bookmark9)

> [NAME: DBIA1548-E ENTRY: 1552 CUSTODIAL PACKAGE: IFCAP Washington](#_bookmark9)

[SUBSCRIBING PACKAGE: EQUIPMENT/TURN-IN Washington USAGE: Private APPROVED: APPROVED STATUS: Active EXPIRES:](#_bookmark9)

> [DURATION: Till Otherwise Agr VERSION:](#_bookmark9)

[TYPE: Routine The Equipment/Turn-In Request package would like permission to use PRCUSESIG to check for the electronic signature code.](#_bookmark9)

[ROUTINE: PRCUESIG](#_bookmark9)

> [External Relations](#_bookmark6)

# [CHAPTER 10 INTERNAL RELATIONS](\l)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[There are no current internal relations within the Equipment/Turn-In package. All menu options are independent and can stand alone.](#_bookmark6)

> [Internal Relations](#_bookmark6)

# [CHAPTER 11 PACKAGE-WIDE VARIABLES](\l)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[Currently there are no package-wide variables used in the Equipment/Turn-In Request package.](#_bookmark6)

> [Package-Wide Variables](#_bookmark6)

# [CHAPTER 12 ON-LINE DOCUMENTATION](\l)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[Currently there is no special on-line documentation for this package. You may review other information about the package through the Data Dictionary Options in FileMan or through %INDEX.](#_bookmark9)

> On-Line Documentation

# [GLOSSARY](\l)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [AEMS-MERS](#_bookmark10)

> [Category Stock Number](#_bookmark10)

> [Equipment Management](#_bookmark10)

> [Integrated Supply Management System (ISMS)](#_bookmark10)

> [Item Master Number](#_bookmark10)

> [NSN](#_bookmark10)

> [Glossary](#_bookmark10)

> [Purchase Order](#_bookmark10)

> [Short Description](#_bookmark10)

> [VA Form 2237 Vendor File](#_bookmark10)