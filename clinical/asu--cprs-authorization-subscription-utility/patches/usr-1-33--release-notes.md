---
title: USR*1*33 Show User Class Name in ASU Options
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Show User Class Name in ASU Options
app_code: ASU
app_name: "CPRS: Authorization Subscription Utility"
section: CLI
app_status: active
pkg_ns: USR
patch_ver: 1
patch_id: USR*1*33
group_key: "ASU:USR:1"
file_numbers: []
security_keys: []
menu_options: 0
description: Patch USR\1\33 supports the Reminders Polytrauma Marker patch PXRM\2\17. Patches USR\1\33 and PXRM\2\17 are sent out together in a single distribution, with PXRM\2\17 requiring USR\1\33.
audience: 
keywords: 
  - class
  - table
  - contents
  - patch
  - strong
  - names
  - description
  - blockquote
  - style
  - width
page_count: 0
word_count: 659
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2010
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Auth_Subscr_Util_(ASU)/usr_1_33rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Auth_Subscr_Util_(ASU)/usr_1_33rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=58"
---

![](usr-1-33-show-user-class-name-in-asu-options/001.png)

Show User Class Name inASU OptionsRelease Notes

### Patch:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

USR\*1\*33

May 2010

### ### Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Office of Enterprise Development

Computerized Patient Record System Product Line

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [Patch:](#patch)
    - [### Department of Veterans Affairs](#department-of-veterans-affairs)
- [Revision History](#revision-history)
- [Description](#description)
  - [Technical Description](#technical-description)
- [Installation Instructions](#installation-instructions)
The most recent entries in this list are linked to the location in the manual they describe. Click on a link or page number to go to that section.
<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 9%" />
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
<td>May 2010</td>
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
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
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

# Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch USR\*1\*33 supports the Reminders Polytrauma Marker patch PXRM\*2\*17. Patches USR\*1\*33 and PXRM\*2\*17 are sent out together in a single distribution, with PXRM\*2\*17 requiring USR\*1\*33.

 

Patch USR\*1\*33 changes displays of User Class Names in Authorization and Subscription Utility (ASU) options. User Class Names are now shown by the name (field .01) of the entry in the User Class File (File \#8930). Previously they were shown by their Display Names (field .04).

The following example is from a medical center that has populated its User Class File (#8930) with User Class Names in upper case (as in ACCOUNTANT) and Display Names with title capitalization (as in Accountant). Thus in the User Class Definition Option \[USR CLASS DEFINITION\] all names that appear in the list of active user classes are the actual User Class Names and thus are all in upper case:

<u> User Classes Apr 01, 2010@21:40:09 Page: 1 of 44</u>

ACTIVE USER CLASSES 653 Classes

<u>Class Name Abbrev</u>

1 ACCOUNTANT ACC

2 ACCOUNTS PAYABLE EMPLOYEE PAY

3 ACCOUNTS RECEIVABLE EMPLOYEE RCV

4 ACCREDITATION REPRESENTATIVE JCAHO

5 ACTING ASSISTANT CHIEF AAC

6 ACTING ASSISTANT DIRECTOR AAD

7 ACTING CHIEF AC

8 ACTING DIRECTOR AD

9 ADDICTION MEDICINE REHAB

10 ADJUDICATION OFFICER ADJ

11 ADMINISTRATIVE ASSISTANT AA

12 ADMINISTRATIVE INTERN AI

13 ADMINISTRATIVE OFFICER AO

14 ADMINISTRATIVE OFFICER OF THE DAY AOD

15 ADOLESCENT MEDICINE INTERNIST ADOLMD

<span class="mark">+ + Next Screen - Prev Screen ?? More</span>

Find Expand/Collapse Class Change View

Create a Class List Members Quit

Edit User Class

Select OPTION NAME:

The user class options are found under the User Class Management Menu \[USR CLASS MANAGEMENT MENU\], which is found under the TIU Maintenance Menu \[TIU IRM MAINTENANCE MENU\].

 

These changes are necessary because it is the entry name (field .01) of the Class which users see in other applications which involve User Class. Using the same name throughout avoids confusion.

 

## Technical Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For the information of developers: An optional parameter is added to the entry points WHATIS^USRLM and \$\$CLNAME^USRLM. This parameter, NAME01, takes the value 1 if the class entry name is wanted. Otherwise the parameter is left off and the routines work as before.

 

 

# Installation Instructions                       

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch USR\*1\*33 is distributed in a combined build with Reminders Polytrauma Marker Patch PXRM\*2\*17. See the Clinical Reminders Patch 17 Install Guide in the VISTA DOCUMENTATION LIBRARY (file PXRM_2_0_17IG.PDF) for general installation instructions for the host file.

This patch requires USR\*1\*15, USR\*1\*18, and USR\*1\*22.