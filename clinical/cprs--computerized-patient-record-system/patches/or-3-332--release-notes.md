---
title: OR*3*332 VBECS Fixes Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: VBECS Fixes
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*332
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: The most recent entries in this list are linked to the location in the manual they describe. Click on a link or page number to go to that section.
audience: 
keywords: 
  - vbecs
  - report
  - span
  - blood
  - order
  - class
  - line
  - horizontal
  - bank
  - blockquote
page_count: 0
word_count: 1585
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2011
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_332rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_332rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

![](or-3-332-vbecs-fixes-release-notes/001.png)

CPRS-VBECS Fixes (OR\*3.0\*332) Release Notes

N<span class="smallcaps">ovember</span> 2011

Office of Enterprise Development

Computerized Patient Record System Product Line

<span id="_Toc107371093" class="anchor"></span>Revision History

The most recent entries in this list are linked to the location in the manual they describe. Click on a link or page number to go to that section.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 30%" />
<col style="width: 21%" />
<col style="width: 18%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Page</strong></td>
<td><strong>Change</strong></td>
<td><strong>Project Manager</strong></td>
<td><strong>Technical Writer</strong></td>
</tr>
<tr class="even">
<td>March 2011</td>
<td>All</td>
<td><blockquote>
<p>Initial Release</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>November 2011</td>
<td>various</td>
<td><blockquote>
<p>Revisions from review</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc308093238" class="anchor"></span>Table of Contents

<span id="_Toc308093239" class="anchor"></span>Introduction

OR\*3.0\*332 is the third patch released to address features of CPRS blood component and diagnostic test ordering changes. It also deals with several display issues, including how reports are formatted. The patch introduces several parameter changes or new parameters.

<span id="_Toc308093240" class="anchor"></span>Functionality

This patch makes changes to the Blood Bank report in CPRS, with several items that sites have requested. Some of these changes are hard-coded, while others are controlled by parameter. Patch OR\*3.0\*332 also adds some parameters and changes others to add some flexibility for sites using the VBECS dialog and Blood Bank report in CPRS.

<span id="_Toc308093241" class="anchor"></span>Pre-Conditions to Installation

OR\*3\*332 requires the following:

- OR\*3\*109
- OR\*3\*309

<span id="_Toc308093242" class="anchor"></span>Changes and Fixes to the Blood Bank Report

- CQ 18632 – The Blood Bank report has been changed to display the Division name instead of the number in the last column of the Units Available section. This change was made to the display only. The printed version of the report will continue to print the Division number due to limited space on the line.
- CQ 18634 - Blood Bank Report displays warning: “ABO Rh: 1^Not able to open port”.  This warning message comes back from VBECS when the VistALink is down. Test sites indicated that this message was confusing.

Resolution: Developers changed CPRS to display the user-defined error message in the parameter OR VBECS ERROR MESSAGE.

- CQ 18708 - There are two places that display an error message when the VBECS VistALink port is down. Previously, the error message was inconsistent.

Resolution: Now, the same text defined in the OR VBECS ERROR MESSAGE parameter is displayed in these two places:

- Patient Info Tab on the Blood Component and Diagnostic Test Order Form Dialog
- The Blood Bank report
- CQ 19330, 19467, 20038, Remedy 366911 – The AVAILABLE/ISSUED UNITS section of the Blood Bank report has been reformatted to make room for larger data fields and more columns. A new column Product ID has been added to fix a problem with missing data when a patient had more than one Product with the same Unit ID. To give further flexibility, a new parameter (OR VBECS AVAIL UNITS FORMAT) is included with this patch:

This parameter determines the format for how AVAILABLE/ISSUED UNITS display on the Blood Bank Report and the Patient Information screen on the Blood Bank Order Dialog.

The possible choices are:

- 0 (zero) or horizontal
- 1 or vertical
- 2 or split

What each choice will do to the display and printed report is explained below

- 0:HORIZONTAL
  - Horizontal displays fields across the page, one line per date/time.

![](or-3-332-vbecs-fixes-release-notes/002.png)

- Horizontal printed reports split the line if it is longer than 79 characters as shown below.

![](or-3-332-vbecs-fixes-release-notes/003.png)

1:VERTICAL

- Vertical displays fields down the page in sections per date/time.

![](or-3-332-vbecs-fixes-release-notes/004.png)

- The Vertical printed report looks the same.
-   
  2:SPLIT HORIZONTAL
  - Split Horizontal keeps the Patient Information Screen the same as the HORIZONTAL format as shown below:

![](or-3-332-vbecs-fixes-release-notes/005.png)

- The Blood Bank Report splits the line if it is longer than 79 characters.

![](or-3-332-vbecs-fixes-release-notes/006.png)

- The Split Horizontal printed report splits the line if it is longer than 79 characters.

![](or-3-332-vbecs-fixes-release-notes/007.png)

The OR VBECS AVAIL UNITS FORMAT parameter was created to address issues found when printing the Blood Bank report in the horizontal format. The option of displaying/printing AVAILABLE/ISSUED UNITS vertically has been created.

As more fields with variable lengths are added to this report, the length of the line may go beyond the 80 character limit for printing. This is not an issue with the Windows display. The information from the Patient Information tab on the Blood Component and Diagnostic Test Order Form dialog cannot be printed, so no attempt has been made to split the line when it goes beyond 79 characters. It functions the same when either HORIZONTAL or SPLIT HORIZONTAL is selected.

For both HORIZONTAL display formats the length of the line expands or contracts depending on the column width of each field and the length of the longest line. Because of this it is possible, though not likely, that the line will not split even if SPLIT HORIZONTAL is selected.

Each site can further customize the Blood Bank Report and Patient information display on the Blood Component and Diagnostic Test Order Form dialog by shortening the length of each line on the Horizontal formats by using the Location abbreviation instead of the Location Name. To do this, edit the parameter OR VBECS LOC ABBREV BB REPORT.

This parameter is new with this patch and only affects the display of the report. The printed report will display the Location abbreviation due to space Limitations.

- CQ 19246: Blood Bank Report DAT Comment Is Missing the Last Line–Previously, the comment for a Direct Antiglobulin Test (DAT) was missing the last line of the comment.

Resolution: This has been fixed so the entire comment is visible.

<span id="_Toc308093243" class="anchor"></span>Changes and Fixes to the Blood Order Dialog

- CQ 18512 – The field requested the ability to alphabetically sort the items in the Reason for Request field.

Resolution: Developers added the new parameter OR VBECS REASON SORT ALPHA to enable sites to alphabetically sort the list of reasons in the Reason for Request field on the Blood Component and Diagnostic Test Order Form dialog.

-   
  CQ 19070 – With the VBECS 1.6.1.0 update, VBECS sends CPRS a ‘no blood required’ flag for some surgical procedures. 

Resolution: This patch adds the CPRS logic to recognize this flag so that CPRS will no longer require a specimen for those orders.

> **NOTE:** Both patch OR\*3.0\*332 and VBECS 1.6.1.0 must be installed before users will see this functionality.

- CQ 19259, 19139, Remedy 382825, 383708, 408643, 464652 – Previously, CPRS saved the specimen unique identifier (UID) with the order and transmitted it to VBECS even if the Date/Time Wanted was past the specimen’s expiration date or if the order was delayed, which could cause confusion.

Resolution: If the order’s Date/Time Wanted is past the specimen’s expiration date or if the order is a delayed order, CPRS will no longer save the specimen UID with the order nor transmit the specimen UID.

- CQ 19265: Display Reason for Request with All Child Orders –The Reason for Request had previously only been saved with component orders.

Resolution: The Reason for Request will now be saved with all VBECS child orders, so it can be transmitted to VBECS. The Reason for Request displays in VBECS on the “VBECS – Order Details” screen.

- CQ 19696, Remedy Ticket 429909, 471985, 424381 –Developers discovered that component requests with the same date/time were overwriting each other and ended up missing on the report.

Resolution: Developers corrected the problem and all of the data should now display.

- CQ 19845 – Previously, there was a problem with the Item Ordered field of lab child orders. Although it did not affect the ordering functions, the field was inadvertently being stuffed with the Orderable Item pointer, which was incorrect. Because the Orderable Item and the Item Ordered point to completely different files, a FileMan Inquiry of the order appeared to be incorrect. Item Ordered was meant to be used by developers to troubleshoot problems, not to build the order. Item Ordered stored which item was selected off the Write Orders menu. For child orders, this item the Item Ordered? should be empty because the child orders came from the parent order, not from a selection on the Write Orders menu.

Resolution: Developers added some code to ensure the Item Ordered field is empty for child orders, which is correct.

- CQ 20073, Remedy 457551 – Add Division Level to OR VBECS REASON FOR REQUEST

Resolution: Developers added DIVISION level settings to the parameter OR VBECS REASON FOR REQUEST. This parameter is being updated in this patch.

<span id="_Toc308093244" class="anchor"></span>Miscellaneous Fixes

- Unnecessary code removed from routine ORWLR that displays the Lab Cumulative in CPRS Reports. This change may improve the speed that the report displays.
- HL7 Review–New codes have been added to STATUS^ORMVBEC for compliance with HL7 standards; pre-existing codes will continue to be respected for backwards compatibility.

<span id="_Toc308093245" class="anchor"></span>Remedy Tickets Resolved by This Patch

- 366911
- 408643
- 382825
- 383708
- 429909
- 457551
- 366886
- 461972
- 464652
- 424381
- 471985