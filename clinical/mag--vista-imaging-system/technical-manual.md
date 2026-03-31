---
title: VistA Imaging System Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: plain
doc_subject: VistA Imaging System
app_code: MAG
app_name: VistA Imaging System
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: > The VistA Imaging System is based on the use of VA FileMan as an object-oriented database management system to store single or sequential images, and other multimedia object types.
audience: 
keywords: 
  - class
  - imaging
  - table
  - even
  - vista
  - strong
  - blockquote
  - image
  - contents
  - dicom
page_count: 0
word_count: 48084
section_count: 49
table_count: 37
figure_count: 5
appendix_count: 3
has_toc: False
is_stub: False
pub_date: July 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/IMGTECHMAN_F.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/IMGTECHMAN_F.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=105"
---

> ![](vista-imaging-system-technical-manual/001.png)

VistA Imaging System Technical Manual

July 2019 – Revision 46 MAG\*3.0\*204

> Department of Veterans Affairs Product Development

> Health Provider Systems

> VistA Imaging Technical Manual VistA Imaging MAG\*3.0\*204, July 2019

> Property of the US Government

> This is a controlled document. No changes to this document may be made without the express written consent of the VistA Imaging Product Development group.

> While every effort has been made to assure the accuracy of the information provided, this document may include technical inaccuracies and/or typographical errors. Changes are periodically made to the information herein and incorporated into new editions of this document.

> Product names mentioned in this document may be trademarks or registered trademarks of their respective companies, and are hereby acknowledged.

> VistA Imaging Product Development Department of Veterans Affairs Internet: REDACTED

> SharePoint: REDACTED

## Preface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this manual is to provide information about the structure and function of the logical components of the Veterans Health Information Systems and Technology Architecture (VistA) Imaging V. 3.0 package (i.e., files, routines, and configuration that comprise the VistA Imaging System). Although this document describes some security functions, sensitive information regarding the VistA Imaging System can only be found in the Security Guide.

> This document describes…

- How to implement and maintain the VistA Imaging System, its routines and files, options, and cross-references among files.
- How files are archived and purged.
- The established relations among the VistA Imaging System components and other components inside and outside of the Imaging software.

> The VistA Imaging System Technical Manual is part of a suite of manuals that includes a release notes document, security guide, user manuals and installation guides. Information about various VistA Imaging System components (i.e., servers, workstations, and background processors) can be found in the Installation Guide.

> *The Food and Drug Administration classifies this software as a medical device. As such, it may not be changed in any way. Modifications to this software may result in an adulterated medical device under 21CFR820, the use of which is considered to be a violation of US Federal Statutes.*

> *VA Policy states the following:*

> *Those components of a national package (routines, data dictionaries, options, protocols, GUI components, etc.) that implement a controlled procedure, contain a controlled or strictly defined interface or report data to a database external to the local facility, must not be altered except by the Office of Information (OI) Technical Services (TS) staff. A controlled procedure is one that implements requirements that are mandated or governed by law or VA (Department of Veterans Affairs) directive or is subject to governing financial management standards of the Federal Government and VA or that is regulated by oversight groups such as the JCAHO or FDA. A controlled or strictly defined interface is one that adheres to a specific industry standard, will adversely affect a package and/or render the package inoperable if modified or deleted. For national software that is subject to FDA oversight, only the holder of the premarketing clearance (510(k)) is allowed to modify code for the medical device. The holder of a premarketing clearance is restricted to specifically designated TS staff that are located at the registered manufacturing site and operating in the designated production environment.*

> *Modifying FDA regulated software under any other conditions is a severe violation of the Code of Federal Regulations. Local, that is field-based, developers are prohibited from modifying national software that is certified by the FDA.*

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>Revision History</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>16 July 2019</td>
<td><p>MAG*3.0*204 ---<u>REDACTED</u></p>
<p>Update title page, footers, and TOC</p></td>
</tr>
<tr class="even">
<td>2 November 2018</td>
<td><p>MAG*3.0*222 ---<u>REDACTED</u></p>
<p>Updated section 9.4.2</p></td>
</tr>
<tr class="odd">
<td>1 November 2018</td>
<td>MAG*3.0*218 updates --- <u>REDACTED</u> Updated section 6.2.1</td>
</tr>
<tr class="even">
<td>4 October 2018</td>
<td><p>MAG*3.0*178,181,182,184,206 updates --- <u>REDACTED</u></p>
<p>Added chapter 19, sections 19.1, 19.1.1, 19.2</p></td>
</tr>
<tr class="odd">
<td>1 October 2018</td>
<td>MAG*3.0*204 updates --- <u>REDACTED</u> Updated sections 5.1, 6.3.5, 7.2.1</td>
</tr>
<tr class="even">
<td><p>24 September</p>
<p>2018</p></td>
<td><p>MAG*3.0*162,166,174,180 --- <u>REDACTED</u></p>
<p>Updated section 6.2.1</p></td>
</tr>
<tr class="odd">
<td>08 February 2018</td>
<td><p>MAG*3.0*188 , updates(rev 42) ---<u>REDACTED</u> Updated section 7.2.1, Chapter 7 VistA Imaging System M Files VA FileMan Files</p>
<p>- Added two rows to table : ( MUSE TEST TYPES &amp; MUSE FORMAT TABLE</p></td>
</tr>
<tr class="even">
<td>2 Oct 2013</td>
<td><p>MAG*3.0*130, 131, 133, 135, 140 updates (rev 41)— <u>REDACTED</u></p>
<p>Updated for MAG*3.0*130, 131, 133, 135, 140 applying the changes to the proper base document Updated sections 3.5.2, 6.3.1, 6.3.5, 8.7, Chapter 9 (numerous changes throughout the chapter) 12.5,</p>
<blockquote>
<p>12.7, 12.9.2, 12.9.2.2, Index</p>
</blockquote>
<ul>
<li><p>Deleted section A.2 BP Error Messages</p></li>
<li><p>Added section A.2, BP Troubleshooting</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>10 Sep 2013</td>
<td><p>MAG*3.0*130, 131, 133, 135, 140 updates (rev 41)— <u>REDACTED</u></p>
<p>- Updated sections 3.6.2, 6.31 6.3.5, 8.7, 12.15, Index</p>
<ul>
<li><p>Deleted section A.2 BP Error Messages</p></li>
<li><p>Added section A.2, BP Troubleshooting</p></li>
</ul></td>
</tr>
<tr class="even">
<td>26 August 2013</td>
<td><blockquote>
<p>MAG*3.0*127 updates (rev. 40)— <u>REDACTED</u></p>
</blockquote>
<p>- Updated sections 3.3, 6.3.1, 6..3.3, 8.1, A.1 MAG*3.0*34/1116/118 updates (rev. 40)— <u>REDACTED</u></p>
<p><strong>-</strong> Updated sections 1.4, 1.5, 1.7, 3.3, 3.6,, 3.6.1, 3.6.5, 3.9, 4.1, 5.1.1, 5.2.1, 5.3.1.8, 5.3.1.9,5.3.1.10, 6.1,</p>
<p>6.1.1, 6.2.1,6.2.2, 6.3.4, 6.3.9, 7.2.1, 7.7, 7.8, 8.2, 8.5, 8.6, 8.9.1, 8.10.1, 9.1,12.4,12.5, 12.6,15.1, A.3,</p>
<p>- Added sections 7.5, 7.6, 8.3, 8.4, 11.4, 11.4.1, 11.4.2.2,11.4.2.3</p>
<p>MAG*3.0*129 updates (rev. 40)— <u>REDACTED</u></p>
<p>- Updated section 6.3.1</p></td>
</tr>
<tr class="odd">
<td>15 Mar 2013</td>
<td><p>MAG*3.0*124 updates (rev 39)— <u>REDACTED</u></p>
<ul>
<li><p>Updated sections 1.7, 3.1, 8.3: changed title to MAG Reason Edit [Mag Sys Menu]; Index</p></li>
<li><p>Added section 3.6.5, Security Keys for AWIV Web Application</p></li>
</ul></td>
</tr>
<tr class="even">
<td>01 Dec 2012</td>
<td><p>MAG*3.0*122 and MAG*3.0*123 updates (rev 38) – <u>REDACTED</u> .</p>
<p>- Updated sections 3.6.1, 3.11, 6.1.2, 6.3.1, 7.2.1, 7.3.1.</p></td>
</tr>
<tr class="odd">
<td>01 Aug 2012</td>
<td><p>MAG*3.0*120 updates (rev 37) –<u>REDACTED</u></p>
<ul>
<li><p>Added section 1.2, VistARad Product Perspective and Features.</p></li>
<li><p>Added section 1.8, Windows 7 Considerations.</p></li>
</ul>
<p>- Revised sections 2.1; 2.2; 2.3; 3.1.1; 3.2; 3.3; 6.3.1; and 8.12.</p>
<ul>
<li><p>Replaced section 12.7, CCOW Communication, and retitled it as Context Management; added four new subsections.</p></li>
<li><p>Added new section 12.8, CPRS Tools Menu Option for VistARad.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>25 Jan 2012</td>
<td><p>MAG*3.0*121 updates (rev 36) <u>REDACTED</u></p>
<p>- Updated sections 6.3.2, 10.1 and 18.1.5 A.2.2.</p>
<p>- Added new section 12.8.3.</p></td>
</tr>
<tr class="odd">
<td>09 Nov 2011</td>
<td><p>MAG*3.0*104 updates (rev 35) <u>REDACTED</u> r.</p>
<ul>
<li><p>Updated sections 1.6, 3.5 and 12.10</p></li>
<li><p>Added new sections 6.3.8 and 9.9.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>01 Sep 2011</td>
<td><p>MAG*3.0*49,99,117 updates (rev 34) <u>REDACTED</u></p>
<p>MAG*3.0*49 – Updated sections 6.3.4, 8.2, 8.3, 8.4, 8.7, 12.1, 12.4.2.</p>
<blockquote>
<p>Added new sections: 8.2.1, 8.2.1.1, 8.2.1.2, 12.2 12.3, 13.1.3, 13.1.4, 13.1.5.</p>
</blockquote>
<p>MAG*3.0*99 – Updated sections 6.2.1, 6.3.4.</p>
<p>MAG*3.0*117 – Updated sections 3.6.2, 6.3.1, 7.2.1.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>Revision History</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>31 May 2011</td>
<td><p>MAG*3.0*39 updates (rev 33) <u>REDACTED</u></p>
<p>- Updated sections 1.3, 5.1.1, 5.1.2, 5.3.1.5, 5.4, 5.5, 6.3.2, 6.3.3, 7.2.1, 8.2, 8.4, 9.3.2, 9.3.3,</p>
<blockquote>
<p>9.3.3.1.1 to 9.3.3.1.8, and modified Chapter 9 name</p>
</blockquote>
<ul>
<li><p>Added new sections 9.5.5 and 9.5.6 and renumbered existing subheadings affected</p></li>
</ul>
<p>-- Re-organized subheadings in Chapter 9</p>
<ul>
<li><p>Made global corrections listed on page 1 of the Change Pages document</p></li>
</ul></td>
</tr>
<tr class="even">
<td>10 May 2011</td>
<td><p>MAG*3.0*106 updates (rev 32) <u>REDACTED</u></p>
<p>- Updated sections 3.6.3, 6.3.1, and 7.2. Added new section 3.11.</p></td>
</tr>
<tr class="odd">
<td>21 Mar 2011</td>
<td><p>MAG*3.0*115 updates (rev 31) <u>REDACTED</u></p>
<ul>
<li><p>Updated sections 6.3.5 and Appendix A.5 for Patch 115.</p></li>
<li><p>Added sections 12.9 and 13.2 for Patch 115.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>01 Feb 2011</td>
<td><p>MAG*3.0*105 and 98 updates (rev 30) <u>REDACTED</u></p>
<p>- Updated section 1.6 for Patch 105</p>
<p>- Updated sections 5.6, 6.3.7, 9.5.2.2, 9.5.2.3.1 for Patch 98</p></td>
</tr>
<tr class="odd">
<td>01 Dec 2010</td>
<td><p>MAG*3.0*53 and 66 updates (rev 29). <u>REDACTED</u></p>
<p>- Updated sections 3.3, 6.2.1, 6.3.4, 7.2.1, 8.7.1, 8.8.1, and 12.2.2 for Patch 53.</p>
<p>- Updated sections 1. 4, 6.2.1, and 12.2.2 for Patch 66.</p></td>
</tr>
<tr class="even">
<td>05 Oct 2010</td>
<td><p>MAG*3.0*108, 90, 94 and 114 updates (rev 28). <u>REDACTED</u></p>
<ul>
<li><p>Updated sections 3.6.4, 6.3.5, and Appendix 5 for Patch 90.</p></li>
<li><p>Updated sections 3.6.2, 10, and 18.1 for Patches 94 and 108.</p></li>
<li><p>Updated sections 6.3.3 and 15.1 for Patch 114.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>09 Jul 2010</td>
<td><p>MAG*3.0*83 updates, minor corrections (rev 27). <u>REDACTED</u></p>
<p>- Updated sections: 1.4, 3.6.1, and 5.1.1; new sections 1.6, 3.5, and 12.8 for MAG*3.0*83.</p>
<p>- General corrections: 6.1.2, 12.4, 18.1.1, and 18.1.2.</p></td>
</tr>
<tr class="even">
<td>10 Feb 2010</td>
<td><p>Patch 93 and Patch 101 updates, general cleanup (rev 26). <u>REDACTED</u></p>
<p>- Updated sections 3.6.2, 6.3.1, 7.2.1, 7.2.3, 8.2, 11.1.2 for Patch 93.</p>
<p>- New sections: 8.2 subsections, 11.1.3.4, 11.1.3.5, 11.1.3.6 for Patch 93.</p>
<p>- Updated Sections 3.6.4, 6.3.5, 7.2.1, and Appendix A.5 for Patch 101.</p></td>
</tr>
<tr class="odd">
<td>20 Oct 2009</td>
<td><p>Patch 72 and Patch 54 updates; general cleanup (rev 25). <u>REDACTED</u></p>
<ul>
<li><p>Updated sections 3.6.1 and 6.3.1 for Patch 72.</p></li>
<li><p>Revised content in section 6.2.3 (detail moved to Security Guide); removed outdated information from 15.1, 18.1.1, and 18.1.2.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>19 Aug 2008</td>
<td><p>Patch 95 updates and misc. cleanup (rev 24) <u>REDACTED</u></p>
<ul>
<li><p>Updated and formatted patch list in section 3.1</p></li>
<li><p>Updated section 6.3.1 for Patch 95</p></li>
<li><p>Remove obsolete section related to test images and demo mode (6.3.1.1, 6.3.1.2, and 11.3.4.); remove redundant screen shots from Chapter 7; correct outdated content in section 9.5.2.1 (JL)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>29 Feb 2008</td>
<td><p>Patch 59 updates (rev 23) - <u>REDACTED</u></p>
<ul>
<li><p>Updated sections 6.3.1 and 6.3.3 for Patch 59.</p></li>
<li><p>New section Appendix B and B.1 for Means Tests Patch 59.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>14 Jan 2008</td>
<td><p>Patch 76 updates and misc. corrections (rev 22). –<u>REDACTED</u></p>
<ul>
<li><p>Clarify MAG_DECOMPRESSOR content in section 6.3.6.</p></li>
<li><p>Updated sections 3.6.4 and 3.6.5 for p76</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>15 Nov 2007</td>
<td><p>Patch 81 and 69 updates (rev 21) - <u>REDACTED</u> .</p>
<ul>
<li><p>Removed old info from chapter 17, added pointer to new info for p81</p></li>
<li><p>Updated sections 6.2.1, 6.2.2, and 12.2.2; removed section 6.2.4 for p69</p></li>
</ul></td>
</tr>
<tr class="even">
<td>04 May 2007</td>
<td><p>Patch 77, 46 and 65 updates (rev 20) – <u>REDACTED</u></p>
<ul>
<li><p>Added revision # to revision table, title page, and footer, corrected typo in section 9.5.4.4.</p></li>
<li><p>Updated sections 8.2 and 12.5.2 for Patch 77.</p></li>
<li><p>New section 12.6 for Imaging site reports Patch 77.</p></li>
</ul>
<p>- Updated sections 3.1, 3.3, 6.4.1, 6.4.3, 7.2.1, 8.2, 12.3, and 15.1 for Patch 46.</p>
<ul>
<li><p>New section 12.5 for CCOW communication Imaging site reports for Patch 46.</p></li>
<li><p>Updates sections 3.3, 7.2.1, and 8.7 for Patch 65.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>Revision History</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>21 Jul 2006</td>
<td><p>Patch 50 and 20 updates (rev 19) - <u>REDACTED</u>.</p>
<ul>
<li><p>Updated section 12.5.2 for patch 78.</p></li>
</ul>
<p>- Updated the following sections for patch 20: 1.3, 5.1.1, 5.3.1.5, 6.4.2-3, 9.3.2, 9.3.3.1.1-8, 11.1.1 and</p>
<blockquote>
<p>12.5.2.</p>
</blockquote>
<ul>
<li><p>Updated section 7.2.1 for patch 50.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>30 Jun 2006</td>
<td><p>Patch 51 and 18 updates (rev 18) – <u>REDACTED</u>.</p>
<ul>
<li><p>Added new section 6.4.6 and updated section 7.2.1 for patch 51.</p></li>
</ul>
<p>- Updated sections 3.3, 3.6, 5.1.2, 6.4.5, 7.2.1, 8.3, and A.5 for patch 18.</p>
<ul>
<li><p>Updated obsolete information in sections 1.4 and 7.2.3</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>12 Dec 2005</td>
<td><p>Patch 57 updates (rev 17) - <u>REDACTED</u>.</p>
<ul>
<li><p>General typo corrections and formatting cleanup throughout document.</p></li>
<li><p>Removed old operating system references throughout document</p></li>
<li><p>Corrected/updated outdated content in sections 3.1, 3.6, 6.1.1, 6.3, 7.2.1, 8.2, 8.7, 9.5.4.4, and</p></li>
</ul>
<blockquote>
<p>12.5.2.1</p>
</blockquote>
<p>- Removed outdated content from sections: 1.5.3, 3.3, 3.4, 5.2.1, 5.3.2, 5.5, 6.4.4.4.2, 6.4.5, 7.4,</p>
<blockquote>
<p>9.5.4.4, 13.1.2, and A.3</p>
</blockquote>
<ul>
<li><p>Incorporated p45 change page: new chapter 18</p></li>
<li><p>New section 3.10 covering Microsoft patch installation.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>5 April 2005</td>
<td><p>Additional Updates (rev 16):</p>
<p>- Section 6.1.1 Checksums</p></td>
</tr>
<tr class="odd">
<td>28 Mar 2005</td>
<td><p>Additional Updates (rev 15):</p>
<p>- Sections 6.4.1, 7.2.4, 10.2.3.1, 10.2.3.3, and 11.1.2, 16.1.2</p></td>
</tr>
<tr class="even">
<td>9 Mar 2005</td>
<td><p>Patch 48 Updates (rev 14):</p>
<p>- Sections 3.6 Security Keys, 6.1.1 Checksums, 6.4.1 Clinical Workstation Files, 6.4.2 Background</p>
<blockquote>
<p>Processor Files, 7.2.4 Further Information, 10.2.3.1 Input Array Sent to Import API, 10.2.3.3 Results Array Returned to Status Handler, 11.1.2 Delete Images and Pointers</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>30 Sept 2004</td>
<td><p>Patch 8 Updates (rev 13):</p>
<ul>
<li><p>Section 3.3 Site Parameters</p></li>
<li><p>Section 3.6 Security Keys</p></li>
<li><p>Chapter 6 – Section 6.1.1 Routine Descriptions</p></li>
<li><p>Section 6.4.1 Clinical Workstation Files</p></li>
<li><p>Section 7.2.1 VA FileMan Files</p></li>
<li><p>Section 8.2 Imaging System Manager Menu</p></li>
<li><p>Section 10.2.3.1 Input Array Sent to Import API</p></li>
<li><p>Section 11.3.4 VistA Imaging Display, Demo Mode</p></li>
<li><p>Section 11.3.5 VistA Imaging Capture, Test Mode</p></li>
</ul></td>
</tr>
<tr class="even">
<td>23 June 2004</td>
<td><p>Patch 33 Updates (rev 12):</p>
<ul>
<li><p>Section 6.4.1 Clinical Workstation Files</p></li>
<li><p>Appendix A.1 Clinical Workstation Error Messages</p></li>
<li><p>Appendix A.4 Setup Error Messages</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>30 April 2004</td>
<td><p>Patch 11 Updates (rev 11):</p>
<ul>
<li><p>Chapter 6 Routine Descriptions</p></li>
<li><p>Section 7.2.1 VA FileMan Files</p></li>
<li><p>Section 8.9 Access to DICOM Gateway RPCs</p></li>
<li><p>Section 12.2.2 DICOM RPC Broker Calls</p></li>
</ul></td>
</tr>
<tr class="even">
<td>6 April 2004</td>
<td><p>Patch 3 Updates (rev 10):</p>
<ul>
<li><p>Revised sections 8.2, 11.1.1, and 12.5.2.1 to reflect the removal of Edit Image Write Location</p></li>
<li><p>Removed redundant sections 8.2.1-8.2.1.2 (i.e.,MAG ENTERPRISE information already exists in section 12.5).</p></li>
<li><p>Documented revisions for patches 7, 17. 23, 27, 25, 22, and 10.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>9 Dec 2003</td>
<td><p>Patch 10 Updates (rev 9):</p>
<p>- Section 7.2.1 VA FileMan Files</p></td>
</tr>
<tr class="even">
<td>5 Nov 2003</td>
<td><p>Patch 22 Updates (rev 7):</p>
<p>- Appendix A.6 VistARad Error Messages</p></td>
</tr>
<tr class="odd">
<td>30 Sept 2003</td>
<td><p>Patch 25 Updates (rev 8):</p>
<p>- Section 7.2.1 VA FileMan Files</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>Revision History</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>23 July 2003</td>
<td><p>Patch 23 Updates (rev 6):</p>
<ul>
<li><p>Section 8.2 Imaging System Manager Menu</p></li>
<li><p>Section 12.5 MailMan Messaging Patch 27 Updates:</p></li>
<li><p>Section 8.2 Imaging System Manager Menu</p></li>
<li><p>Section 12.5 MailMan Messaging</p></li>
</ul></td>
</tr>
<tr class="even">
<td>7 May 2003</td>
<td><p>Patch 17 Updates (rev 5):</p>
<ul>
<li><p>Section 7.2.1 VA FileMan Files</p></li>
<li><p>Section 7.5 Imaging Entity Relationship Diagram and Detailed Information</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>30 April 2003</td>
<td>Patch 19 Updates (rev 4) to section 8.2 Imaging System Manager Menu</td>
</tr>
<tr class="even">
<td>30 Mar 2003</td>
<td>Patch 16 Updates (rev 3): to Appendix A.5 VistARad Installation Error Messages</td>
</tr>
<tr class="odd">
<td>10 Dec 2002</td>
<td><p>Patch 9 Updates (rev 2):</p>
<p>- Addition of files 2006.035, 2006.036, 2006.59, 2006.5906, 2006.596</p>
<ul>
<li><p>Additional fields for file 2005.2</p></li>
<li><p>Additional security key MAGJ DEMAND ROUTE</p></li>
<li><p>Modification to table 3.3 (collapse line-items for DICOM Gateway)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>6 Sept 2002</td>
<td><p>Patch 7 Updates (rev 1):</p>
<ul>
<li><p>Created changes pages for Sections 3.6, and 7.2.1.</p></li>
<li><p>Chapter 10 – revised</p></li>
</ul></td>
</tr>
</tbody>
</table>

Table of Contents
## Chapter 1 Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Multimedia Patient Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA Imaging System is an extension to the <u>V</u>eterans Health Information <u>S</u>ystem <u>T</u>echnology <u>A</u>rchitecture (VistA) hospital information system that captures clinical images, scanned documents, motion images, and other non-textual data files and makes them part of the patient's electronic medical record. Electrocardiogram (EKG) waveforms can be displayed as part of the electronic medical record. Image and text data are provided in an integrated manner that facilitates the clinician's task of correlating the data and making patient care decisions in a timely, accurate way.

> The system is designed to provide the treating physician with a complete view of patient data and, at the same time, allow consulting physicians to have access to the image and text data. It serves as a tool to aid communication and consultation among physicians -- whether in the same department, in different medical services, or at different sites.

> The VistA Imaging System is unique in that management of the medical images is handled by the hospital information system, allowing very close integration of multimedia data with traditional patient chart information.

> Clinical users can capture images during procedures or images can be added at a later time, for example during the creation of a report or progress note. Automatic image acquisition can be performed by DICOM gateways. Images can be acquired from commercial radiology Picture Archiving and Communications Systems (PACS) or directly from radiology devices. The transfer of patient demographic and order information to the commercial PACS or radiology device plays a key role in the ability to add these images to the patient’s online medical record.

> VistA Imaging workstations located throughout the hospital capture and display a wide variety of medical images including:

- Cardiology
- Endoscopy (GI, pulmonary, cystoscopy, arthroscopy, bronchoscopy, etc.)
- Ultrasound (vascular, echo cardiology)
- Microscopic (Surgical Pathology, Cytology, Autopsy, Hematology)
- Surgery
- Ophthalmology
- Dental
- Dermatology
- Radiology images
- Nursing
- Podiatry
- Scanned advanced directives, consent forms, and other documents

> VistA Imaging VistARad diagnostic workstations are generally located in the Radiology Reading room and are used for softcopy reading of Radiology images. These workstations provide functions for the Radiologist to retrieve and display full-resolution images, associated Radiology reports, and update the Radiology exam status.

### VistARad Product Perspective and Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistARad is a VistA Imaging software component that provides filmless radiology functionality for radiologists and non-radiology clinicians. This maintenance patch (Maintenance VII) addresses various user needs including routine maintenance items, as well as two items described in this document that affect low-level design of certain features already implemented. In addition, support for patient context management is added to the design to eliminate potential safety concerns for those clinicians that require access to VistARad functionality and concurrent use of the VA Computerized Patient Record System (CPRS) and other CCOW-enabled applications.

> The following product features and/or design modifications are included in Patch 120 and described in this document:

- Patch 120 provides support for the Windows 7™ operating system. The client installation file included with this patch will execute on either Windows XP™ or Windows 7. Certain installation details differ according to the target installation environment. These differences are noted elsewhere in this document.

> Note: Some legacy display adapters for high-resolution screens may no longer be supported under Windows 7.

- Changes to the dictation system integration feature reduce potential mismatches between displayed exams and the accession number provided to the dictation system under certain usage scenarios.
- An added feature to the Teaching File interface allows the user to remove Personally Identifiable Information (PII) from images that have PII burned into the image pixel data. Previously, such “burned in” data could not be removed from images used for teaching purposes, raising a patient confidentiality issue. See the *VistARad User Guide*, Teaching Files.
- Patient Context Management Support is discussed. See section [0](\l).

### Automated DICOM Image Acquisition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DICOM is the abbreviation for the Digital Imaging and COmmunications in Medicine standard. DICOM brings open systems technology to the medical imaging marketplace and enables VistA to communicate directly with commercial medical imaging equipment.

> DICOM is a set of networked client/server applications that are implemented on top of TCP/IP. DICOM is part of the VistA networked application suite, along with CPRS, Kernel Broker, MS Exchange, and Windows-based file servers. Similar networking techniques are used for installing and maintaining all of these applications.

### The VistA Imaging DICOM Gateway

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA Imaging DICOM Gateway, referred to as the DICOM Gateway for short, is a suite of VA-developed software that facilitates the transmission of DICOM images between the image acquisition modalities[<sup>1</sup>](#_bookmark6) and the equipment on which these images are permanently stored. The images and information about them are stored in the VistA database as a part of the patient record. Once images have been stored in the system, they are available for viewing from any VistA clinical or diagnostic workstation.

> The VistA Imaging DICOM Gateway can have these functions, depending on its configuration:

- Text Gateway − A gateway that distributes event data from the VistA Hospital Information System to image acquisition modalities and Picture Archiving and Communication Systems (PACS). For more information, see the *VistA Imaging DICOM Gateway User Guide*.
- Image Gateway − A gateway that transfers image files from an acquisition modality or a commercial PACS to VistA, or from VistA to workstations or commercial PACS. For more information, see the *VistA Imaging DICOM Gateway User Guide*.
- Routing Gateway − A gateway that transmits studies acquired at one VistA site to a storage location at another VistA site. For more information, see the *VistA Imaging DICOM Gateway Routing Setup and User Guide*.

### The Hybrid DICOM Image Gateway

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Hybrid DICOM Image Gateway (HDIG) is a component of the DICOM Image Gateway, introduced in MAG\*3.0\*34 to enable the storage of the SOP classes for which support was introduced in MAG\*3.0\*34.

Figure 1: Hybrid DICOM Image Gateway

![](vista-imaging-system-technical-manual/002.png)

> <span id="_bookmark6" class="anchor"></span>Note: The term “modality” is from the DICOM standard and denotes any equipment that produces images.

> The HDIG includes these components:

- DICOM Listener. The DICOM Listener listens on a specific port for incoming DICOM objects from DICOM devices (Application Entities, or AEs) that are pre-defined in the DICOM AE SECURITY MATRIX. It validates all Service Object Pair (SOP) classes for which support was introduced in MAG\*3.0\*34 and stores the DICOM objects that pass the various validation checks in the new database structures. It forwards the SOP classes that were supported before MAG\*3.0\*34 for storage in the old database structures. The DICOM Listener includes:
- The server side of the Query/Retrieve application (Query/Retrieve for short). Query/Retrieve is an application that allows pre-defined application entities to query the VistA database. For more information about Query/Retrieve, see the *VistA Imaging DICOM Gateway User Manual*.
- The server side of the DICOM Importer II. The DICOM Importer II application provides the ability to import studies acquired at external facilities into the VistA database. It also provides a user-friendly graphical user interface for using DICOM Correct to correct errors in the processing flow. For more information about the DICOM Importer II, see the *DICOM Importer II User Manual*.
- Archiver. The Archiver archives the SOP classes for which support was introduced in MAG\*3.0\*34.
- New Abstract Maker. The new Abstract Maker creates abstracts (thumbnail icons) for the SOP classes for which support was introduced in MAG\*3.0\*34.

> The following figure shows the HDIG components. You can select all components during installation, except the server side of the Query/Retrieve application (implemented in MAG\*3.0\*116) and the server side of the DICOM Importer II application (implemented in MAG\*3.0\*118), which are installed with the DICOM Listener.

![](vista-imaging-system-technical-manual/003.png)

Figure 2: HIG components diagram

> For more information about installing the HDIG and its components, see the *VistA Imaging DICOM Gateway Installation Guide*.

> From Patch 204 onward, the HDIG application will only run on 64-bit operating systems (Windows 2008 64-bit, Windows 2012, etc.) This software has not been tested on Windows 2016.

### Background Processor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA Imaging Background Processor is a component in the VistA Imaging System and runs on a Windows file server. The Background Processor ensures the archiving of DICOM and clinical images from short-term storage (RAID groups) onto Tier 2 for long-term storage. These images are stored indefinitely on the archive device.

#### Queue Processor

> The Queue Processor moves image data between Tier 1 and either remote or local Tier 2 storage. This activity is in response to activity from Capture and Display application requests.

#### Purge

> The Purge removes image files from the Tier 1 based on file dates. An automatic purge process can be configured when Tier 1 storage becomes low and a regularly scheduled purge can be configured to operate during off-peak hours.

#### Verifier

> The Verifier maintains and checks data integrity between the VistA Imaging database and the storage network location.

### Typical Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The diagram below shows a typical configuration of a VistA Imaging system.

Figure 3: VistA Imaging Network Topology

![](vista-imaging-system-technical-manual/004.png)

### DICOM Gateway Networking Topology Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA DICOM Gateways may use either one or two networking interfaces depending upon whether the commercial DICOM devices are directly connected to the main network backbone or are located on separate physical networks.

#### Commercial DICOM Devices Connected to Main Network Backbone

> Some sites may choose to have all devices (workstations, main hospital computer, DICOM imaging producing equipment, etc.) connected to a single high-speed switched network backbone. In this case, the VistA Image Servers, VistA DICOM Gateways, and Background Processor will all connect to the same switch on the high-speed backbone. Clinical and capture workstations will be connected to segments that feed into the backbone.

Figure 4: Single High-Speed Switched Network

![](vista-imaging-system-technical-manual/005.png)

#### Commercial DICOM Devices on Separate Physical Networks

> Other sites may choose to have a separate dedicated network for the commercial DICOM devices and DICOM gateways. In this case, the VistA DICOM Gateway must have two network interfaces, one to connect to the main hospital network backbone, and the second to connect to the dedicated network for the commercial DICOM devices. This keeps the traffic on the two networks separate.

Figure 5: Separate Dedicated DICOM Network

![](vista-imaging-system-technical-manual/006.png)

### Cross-Enterprise Image Sharing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Sites that implement the VistA Imaging Exchange (VIX) service get:

- More efficient access to all types of remotely stored images and image-like artifacts (such as scanned documents) from other VA sites that also have a VIX.
- Remote radiology worklist monitoring and access to remotely stored radiology exams, using VistARad, without the need for routing.
- Access to DoD images for shared VA/DoD patients.
- For more information about the VIX, see the *VistA Imaging VIX Administrator’s Guide*. Sites that implement the Advanced Web Image Viewer (AWIV) get:
- The ability for users to view images, progress notes, radiology reports, and other artifacts from within VistAWeb.
- User access to images from any VA site via the Centralized VistA Imaging Exchange (CVIX) service, which is an extension of the VIX service.

> For information about using the AWIV, see the *VistA Imaging AWIV User Manual*. Sites that implement the Advanced Web Image Viewer (AWIV) Web Application get:

- The ability for users to access images using the AWIV through Microsoft Internet Explorer.
- User access to all patient images from all sites at which a patient has been seen, not just the images associated with progress notes or radiology reports.
- User access to DoD artifacts, radiology images, and NCAT reports.

> **NOTE:** The NCAT system must be online and available in order for AWIV users to view NCAT reports.

- User access to images via the AWIV using a thin client.

> For information about using the AWIV WA, see the *VistA Imaging AWIV Web Application User Guide*.

### Windows 7 Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistARad runs successfully under Windows 7. The documentation will point out any differences when necessary, using notes such as the following:

> Note: Restrictions on access to root directories (including C:\\ mean that ordinary users cannot create files in the root directory C:\\

> Some “system” file pathnames (including those for the VistARad application itself) are different on Windows 7 systems. See section [6.3.1](\l) for details.

## Chapter 2 Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following conventions are used in this manual.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 11%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Convention</strong></th>
<th colspan="2"><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Regular Type</td>
<td colspan="2">System-generated menu, dialog, output, etc. (in VistA screenprints)</td>
</tr>
<tr class="even">
<td>Bold Type</td>
<td colspan="2">User Keyboard Entry (in VistA screenprints)</td>
</tr>
<tr class="odd">
<td>[XTSUMBLD- CHECK</td>
<td colspan="2">Routines, VistA Menu options</td>
</tr>
<tr class="even">
<td>&lt;Enter&gt;</td>
<td><blockquote>
<p>![](vista-imaging-system-technical-manual/007.png)</p>
</blockquote></td>
<td>Enter (Return) key</td>
</tr>
<tr class="odd">
<td>&lt;Shift&gt;</td>
<td><blockquote>
<p>![](vista-imaging-system-technical-manual/008.png)</p>
</blockquote></td>
<td>Shift key</td>
</tr>
<tr class="even">
<td>&lt;A&gt;, &lt;2&gt;, &lt;F2&gt;</td>
<td colspan="2">Alpha, numeric or function key</td>
</tr>
<tr class="odd">
<td>&lt;Esc&gt;</td>
<td>![](vista-imaging-system-technical-manual/009.png)</td>
<td>Escape key</td>
</tr>
<tr class="even">
<td rowspan="2">&lt;Num Lock&gt;</td>
<td>![](vista-imaging-system-technical-manual/010.png)</td>
<td>Top left key on the numeric keypad (above the 7); may also be labeled &lt;Numeric Lock&gt;. It is equivalent to the &lt;Caps Lock&gt; used for alphabetic keys.</td>
</tr>
<tr class="odd">
<td colspan="2"><p>If &lt;Num Lock&gt; is on, the keypad key will produce the number shown on its surface.</p>
<p>If &lt;Num Lock&gt; is off, the keypad key moves the cursor as indicated by the label or symbol on the key; for example, the keypad &lt;6&gt; key will move the cursor to the right.</p></td>
</tr>
</tbody>
</table>

### Special Workstation Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Command</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Reboot</td>
<td><ul>
<li><p>Push the RESET button on the front of the workstation.</p></li>
<li><p>If there is no RESET button, power the workstation off and then on; the workstation will reboot.</p></li>
<li><p>The workstation will perform a virus check and load all required software; this takes about 30-60 seconds.</p></li>
<li><p>When the reboot process is complete, you should be able to sign back into the workstation.</p></li>
</ul></td>
</tr>
</tbody>
</table>

### Mouse/Windows Controls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Control</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Mouse button click</td>
<td><ul>
<li><p>The mouse is a device used to point at positions on the screen.</p></li>
<li><p>The mouse may have one, two, or three buttons.</p></li>
<li><p>The mouse should be held at the end opposite the cord so the fingers can press the buttons.</p></li>
<li><p>The buttons are referred to as the "Right Mouse Button," the "Left Mouse Button", and the "Center Mouse Button." One kind of mouse, known as a “wheel mouse,” has a wheel in the center instead of a button. The wheel is normally used for scrolling up and or left to right on a screen. When the mouse is rolled around on a flat surface, the arrow cursor on the screen will move correspondingly.</p></li>
<li><p>Pressing and releasing a button is called "clicking". You may position the arrow over a portion of the window, such as a button or scroll bar, and then click. This will cause the computer to do something such as display an image, depending on the window.</p></li>
<li><p>When the instructions tell you to “press the mouse button,” you can assume that you are to press the left mouse button.</p></li>
<li><p>When it’s necessary to use the right mouse button, you will be told to “right click.” This is used, for example, to select items from a drop-down list or menu.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Select</td>
<td><ul>
<li><p>You may also select a rectangular area on the window, by following these steps:</p></li>
<li><p>Position the arrow cursor so it is over the left upper corner of the area to be selected.</p></li>
<li><p>Press the left mouse button down and hold it down while you move the mouse to the right lower corner of the rectangle to be selected.</p></li>
<li><p>Release the mouse button. You will see a dotted rectangle on the window around the area selected.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Drag</td>
<td><ul>
<li><p>If you want to move a window to another area of the window (e.g., to see something on a window that is underneath), follow these steps:</p></li>
<li><p>Position the cursor over the top colored title area of the window to be moved.</p></li>
<li><p>Press the left mouse button down, hold the mouse button down, and move the mouse until the window is where you want it.</p></li>
<li><p>Release the left mouse button.</p></li>
</ul>
<ul>
<li><p>This is called "clicking and dragging" a window.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>![](vista-imaging-system-technical-manual/011.png)</td>
<td><ul>
<li><p>You may adjust the size of the window by following these steps:</p></li>
<li><p>Place your mouse at the edge of the window that you would like to move.</p></li>
<li><p>When you see the cursor turn into a double headed arrow (![](vista-imaging-system-technical-manual/012.png)), hold the left mouse button down, and move the mouse until the image is the width and/or height that you would like.</p></li>
</ul>
<ul>
<li><p>Release the left mouse button.</p></li>
</ul></td>
</tr>
</tbody>
</table>

Chapter 2 - Orientation

> This page is intentionally left blank.

## Chapter 3 Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VistA Package Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA Imaging System is designed to be used in conjunction with the following VistA packages: Kernel, FileMan and RPC Broker are required packages; other packages depend on the site’s implementation requirements.

#### Packages Used in Conjunction with VistARad

> The VistA Imaging System is designed to be used in conjunction with the following VistA packages. Kernel, FileMan and RPC Broker are required packages. Other packages will depend on the site’s implementation requirements.

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Package Name and Version</strong></th>
<th><strong>Required For</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Kernel V. 8.0</td>
<td>Kernel is a vendor-independent applications development environment, as well as a run-time environment providing standard vendor-independent services to applications software. It is not an operating system, but a set of utilities and associated files that are executed in an M environment.</td>
</tr>
<tr class="even">
<td>FileMan V. 22</td>
<td><p>VA FileMan creates and maintains a database management system that includes features such as:</p>
<ul>
<li><p>A report writer</p></li>
<li><p>A data dictionary manager</p></li>
<li><p>Scrolling and screen-oriented data entry</p></li>
<li><p>Text editors</p></li>
<li><p>Programming utilities</p></li>
<li><p>Tools for sending data to other systems</p></li>
<li><blockquote>
<p>File archiving</p>
</blockquote></li>
</ul>
<blockquote>
<p>VA FileMan can be used as a standalone database, as a set of interactive or "silent" routines, or as a set of application utilities; in all modes, it is used to define, enter, and retrieve information from a set of computer-stored files, each of which is described by a data dictionary.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>RPC Broker 1.1</td>
<td>Interfacing with the hospital database</td>
</tr>
<tr class="even">
<td>Consult/Request Tracking V. 3.0</td>
<td>Capturing images to the Consult/Request Tracking package</td>
</tr>
<tr class="odd">
<td>Medicine V. 2.3</td>
<td>Capturing images to the Medicine package</td>
</tr>
<tr class="even">
<td>Laboratory V. 5.2</td>
<td>Capturing images to the Laboratory package</td>
</tr>
<tr class="odd">
<td>Radiology V. 5.0</td>
<td>Capturing images to the Radiology package</td>
</tr>
<tr class="even">
<td>Surgery V. 3.0</td>
<td>Capturing images to the Surgery package</td>
</tr>
<tr class="odd">
<td>TIU V. 1.0</td>
<td>Capturing images to the Text Integration Utility package</td>
</tr>
<tr class="even">
<td>PIMS V 5.3</td>
<td>Displaying Patient Profile report and patient security lookup</td>
</tr>
<tr class="odd">
<td>Health Summary 2.7</td>
<td>Displaying Health Summary report</td>
</tr>
</tbody>
</table>

### Hardware and Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Contact your Implementation Manager for information about VistA Imaging equipment.

> The VistA Imaging software requires that a network be present with sufficient capacity to transport image files in a reasonable amount of time. All network set-ups must be completed before VistA Imaging workstations can be installed.

### Maintenance of Software on DICOM Gateway Workstations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *This section is obsolete as of the release of Patch 11. Refer to the Imaging DICOM Gateway Installation Guide for information about software installation and maintenance.*

### Changes to IP Addresses or Ports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Any changes to the IP addresses for the VistA servers or changes to the Kernel RPC Broker Listening port(s) will require updating on the VistA Imaging workstations (refer to the Broker Technical and User Manuals).

> The VistA Site Service will also need to be updated with the changes. (If the site service is not updated, remote VA sites will not be able to access locally stored images.) For information about the VistA Site Service, see section [12.11.](\l)

> Sites that have implemented a VIX will need to update their VIX’s configuration to use the new site service values. This is done by re-running the VIX installer. Contact REDACTED for guidance.

> Sites that have implemented a VIX will also need to update their VIX’s configuration after the site service has been updated. This is done by re-running the VIX Installation wizard which will detect the new connection information and reconfigure the VIX accordingly. See the *VIX Installation Guide* for more information.

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are a number of security keys associated with the VistA Imaging system. The following tables summarize security keys and their function.

#### General Security Keys

> Note: Please be cautious when assigning the following keys; the keys are intended for Imaging Support personnel. Review the descriptions before assigning these keys.

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>General Security Keys</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MAG ANNOTATE MGR</td>
<td><blockquote>
<p>This key gives the holder full annotation access at the local site. The holder can add, edit, and delete annotations.</p>
<p>Permissions provided by this key apply only to images at the site where the user has the key. This key also allows users to create annotations regardless of the settings of the user’s account in the PARAMETER DEFINITION (MAG IMAGE ALLOW ANNOTATE) specified at a given site.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>MAGDFIX ALL</td>
<td><blockquote>
<p>Allows the holder to perform DICOM CORRECT functions on any entry in the DICOM FAILED IMAGES file (#2006.575). Users who do not hold this key will only be able to correct entries that were captured on their own site's gateway.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MAG DELETE</td>
<td><blockquote>
<p>This key allows the holder to delete images from the IMAGE file (#2005) and from the new data structures. Pointers in parent packages such as Medicine, Surgery, Lab, Radiology, and TIU will also be deleted for images in file (#2005).</p>
</blockquote></td>
</tr>
<tr class="even">
<td>MAG PREFETCH</td>
<td><blockquote>
<p>This key allows a user to 'PreFetch' or Queue all images for a patient. This means that all images for a patient that are on the jukebox will be copied from the jukebox to the magnetic server cache.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MAG SYSTEM</td>
<td><blockquote>
<p>Given to person(s) managing VistA Imaging Systems. Required to modify site parameters via the Background Processor or to modify workstation parameters via the MAGSYS application. Also enables the display of DICOM header data for radiology images on Clinical Display workstations.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>MAG VIX ADMIN</td>
<td><blockquote>
<p>This key grants access to the VIX transaction log and to update HDIG administration parameters (HDIG service accounts access/verify code and email addresses). This key should be assigned to VIX administrators, to the DICOM service account, and the Imaging System Manager account. For more information, see the <em>VIX Administrator’s Guide</em>.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Security Keys for Clinical Display

> The following keys are used for display of images and should be limited to appropriate personnel:

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>Display-related Security Keys</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MAG RAD SETTINGS</td>
<td>User can edit the CT Presets in the Clinical Imaging Display Radiology Viewer window.</td>
</tr>
<tr class="even">
<td>MAG ROI</td>
<td>User can print, copy images, or make release of information (ROI) requests without having to enter an electronic signature. This key should be assigned only to the HIMS Release of Information Officer.</td>
</tr>
<tr class="odd">
<td>MAGDISP ADMIN</td>
<td>User can display administrative images/documents.</td>
</tr>
<tr class="even">
<td>MAGDISP CLIN</td>
<td>User can display clinical images/documents.</td>
</tr>
<tr class="odd">
<td>MAG EDIT</td>
<td>The MAG EDIT key is used to correct an image field when an index field is incorrect or incomplete, such as correcting a wrong specialty that was selected. Only users assigned the MAG EDIT key can edit an image. The MAG EDIT key is also required to access the QA Review Utility when performing quality assurance reviews of the scanned images. Only the Chief, HIM or authorized designated personnel e.g., VistA Imaging Coordinator, Scanning Supervisor) should be assigned this key.</td>
</tr>
<tr class="even">
<td>MAG PAT PHOTO ONLY</td>
<td>User can view only the patient photo.</td>
</tr>
<tr class="odd">
<td>MAG QA REVIEW</td>
<td>User can access QA Review and QA Review Report from Clinical Display Utilities Menu.</td>
</tr>
<tr class="even">
<td>MAG REVIEW NCAT</td>
<td>User can view NCAT reports.</td>
</tr>
<tr class="odd">
<td>MAG VIEW DOD IMAGES</td>
<td><p>In Patch 72 and 93 versions of Clinical Display, users must have this key to display DoD images.</p>
<p>In newer versions of Clinical Display, this key is not checked.</p></td>
</tr>
</tbody>
</table>

#### Security Keys for Clinical Capture

> Note: If the ‘CAPTURE KEYS’ site parameter has been initialized, the following keys will need to be assigned appropriately.

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>Capture-related Security Keys</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MAG CAPTURE</td>
<td>Allow capture of images without an associated specialty (i.e. 'NONE' on the Imaging Capture configuration window).</td>
</tr>
<tr class="even">
<td>MAG NOTE EFILE</td>
<td><blockquote>
<p>User can electronically file notes without an electronic signature from the Imaging Capture workstation.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MAGCAP ADMIN</td>
<td>Allow capture of images associated with the ‘Admin Document’ specialty.</td>
</tr>
<tr class="even">
<td>MAGCAP CP</td>
<td><blockquote>
<p>Allow capture of Clinical Procedure images.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MAGCAP LAB</td>
<td><blockquote>
<p>User can capture Laboratory images from the Imaging Capture workstation.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>MAGCAP MED C</td>
<td><blockquote>
<p>User can capture Cardiology images from the Imaging Capture workstation.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MAGCAP MED G</td>
<td>User can capture GI images from the Imaging Capture workstation.</td>
</tr>
<tr class="even">
<td>MAGCAP MED GEN</td>
<td>User can capture Generic Medicine images from the Imaging Capture workstation.</td>
</tr>
<tr class="odd">
<td>MAGCAP MED H</td>
<td>User can capture Hematology images from the Imaging Capture workstation.</td>
</tr>
<tr class="even">
<td>MAGCAP MED HI</td>
<td>User can capture Internal Medicine / Hematology images from the Imaging Capture workstation.</td>
</tr>
<tr class="odd">
<td>MAGCAP MED I</td>
<td><blockquote>
<p>User can capture Internal Medicine images from the Imaging Capture workstation.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MAGCAP MED N</p>
</blockquote></td>
<td>User can capture Neurology images from the Imaging Capture workstation.</td>
</tr>
<tr class="odd">
<td>MAGCAP MED P</td>
<td>User can capture Pulmonary / Endoscopy images from the Imaging Capture workstation.</td>
</tr>
<tr class="even">
<td>MAGCAP MED PF</td>
<td><blockquote>
<p>User can capture Pulmonary Function Test images from the Imaging Capture workstation.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MAGCAP MED R</td>
<td>User can capture Rheumatology images from the Imaging Capture workstation.</td>
</tr>
<tr class="even">
<td>MAGCAP MED Z</td>
<td><blockquote>
<p>User can capture Consult images from the Imaging Capture workstation.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MAGCAP PHOTOID</td>
<td>User can capture Photo ID images from the Imaging Capture workstation.</td>
</tr>
<tr class="even">
<td>MAGCAP RAD</td>
<td>User can capture Radiology images from the Imaging Capture workstation.</td>
</tr>
<tr class="odd">
<td>MAGCAP SUR</td>
<td>User can capture Surgery images from the Imaging Capture workstation.</td>
</tr>
<tr class="even">
<td>MAGCAP TIU</td>
<td>User can capture TIU images from the Imaging Capture workstation.</td>
</tr>
<tr class="odd">
<td>MAGCAP TRC</td>
<td>User can capture images associated with a "TeleReader Consult" from the Imaging Capture workstation.</td>
</tr>
</tbody>
</table>

#### Security Keys for VistARad

> The following keys are related to VistARad and should be limited to appropriate personnel:

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>VistARad-related Security Keys</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MAGJ DEMAND ROUTE</p>
</blockquote></td>
<td><blockquote>
<p>User can access VistARad’s on-demand routing capability. On- demand routing can be used to manually send exams to remote sites. For more information, refer to the <em>VistA Imaging Routing User Guide</em>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>MAGJ DEMAND ROUTE DICOM</td>
<td>Allows the user to use the on-demand routing function to queue exam images to be routed to selected remote DICOM destinations. This function only works for sites that have been configured for routing of images. An updated Routing agreement needs to be submitted and approved by the VistA Imaging Group before this function can be used.</td>
</tr>
<tr class="odd">
<td>MAGJ OVERRIDE ANNOTATIONS</td>
<td>Grants to a radiologist user of VistARad access to the menu option ‘Override Annotations’ when viewing an exam whose status is ‘Complete.’ This functionality is detailed in the <em>VistARad User Guide</em>.</td>
</tr>
<tr class="even">
<td>MAGJ REMOTE ACCESS CONTROL</td>
<td>Allows a VistARad user to access the Monitored Sites configuration subset of the VIX Configuration settings tab, and to view exam list data in the Monitored Sites tab of the Manager.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MAGJ SEE BAD IMAGES</p>
</blockquote></td>
<td><blockquote>
<p>User can view images in VistARad that are associated with an exam that has failed the “Patient Safety” database checks.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MAGJ STORE IMAGES</p>
</blockquote></td>
<td><blockquote>
<p>Allows VistARad users to save Voxar images as secondary captures to VistA.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MAGJ SYSTEM MANAGER</p>
</blockquote></td>
<td><p>Allows access to Voxar-related settings in the VistARad Settings dialog. Grants access to additional data in the Imaging Internal Data display window. This functionality is detailed in the VistARad User Guide and Imaging System Installation Guide.</p>
<blockquote>
<p>Should only be assigned to VistARad administrators. Assigned only to VistARad administrators. Grants access to the Local Site VIX configuration subset of the VIX Configuration tab.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MAGJ SYSTEM USER</p>
</blockquote></td>
<td>Allows a user to create and delete site-level hanging protocols, templates, and image presets associated with the VistARad ‘sysAdmin’ user.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MAGJ VOXAR COPYIMAGE</p>
</blockquote></td>
<td>Allows VistARad users to copy images using Voxar (Enables the <strong>Copy to Clipboard</strong> button in the Voxar Reading manager window; refer to Voxar documentation for more information.)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>MAGJ VOXAR EXPORTCAPTURE</p>
</blockquote></td>
<td>Allows VistARad users to export images using Voxar (Enables the three <strong>Export</strong>-related buttons in the Voxar Reading manager window; refer to Voxar documentation for more information.)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MAGJ VOXAR PRINTCOMPOSER</p>
</blockquote></td>
<td>Allows VistARad users to print images using Voxar (Enables the <strong>Print Composer</strong> button in the Voxar Reading manager window; refer to Voxar documentation for more information.)</td>
</tr>
</tbody>
</table>

#### Security Keys for AWIV Web Application

> Users at the medical centers are allowed to view images based on their levels of access and/or user rights. Users must have at least one of the following keys to access images using the AWIV Web Application.

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>AWIV-Related Security Keys</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MAG REVIEW NCAT</td>
<td>User can view NCAT reports.</td>
</tr>
<tr class="even">
<td>MAGDISP ADMIN</td>
<td>User can display administrative images/documents.</td>
</tr>
<tr class="odd">
<td>MAGDISP CLIN</td>
<td>User can display clinical images/documents.</td>
</tr>
<tr class="even">
<td>MAG PAT PHOTO ONLY</td>
<td>User can view only the patient photo.</td>
</tr>
<tr class="odd">
<td>MAG ROI</td>
<td>User can print or copy images without entering an electronic signature; granted only to HIMS Release of Information officer.</td>
</tr>
</tbody>
</table>

> NOTE: The NCAT system must be online and available in order for AWIV users to view NCAT reports.

> Veterans Benefit Administration (VBA) users can view images without security keys, with the exception of NCAT reports.

#### Security Keys for the DICOM Importer II

> The following keys are related to the DICOM Importer II and should be limited to appropriate personnel:

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>Security Keys for the DICOM Importer II</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MAGV IMPORT MEDIA STAGER</td>
<td>Allows DICOM Importer II users to stage (copy) from media to staging persistent storage, where it waits for reconciliation processing.</td>
</tr>
<tr class="even">
<td>MAGV IMPORT STAGE MEDIA ADV</td>
<td><p>Allows DICOM Importer II users to:</p>
<ul>
<li><p>Stage (copy) study level artifacts from media to staging persistent storage and</p></li>
<li><p>View images on the media.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>MAGV IMPORT RECON CONTRACT</td>
<td><p>Allows DICOM Importer II users to:</p>
<ul>
<li><p>Stage media at the study level</p></li>
<li><p>View images on the media</p></li>
<li><p>Associate study DICOM objects with an existing Radiology or Consult order for reconciliation.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>MAGV IMPORT RECON ARTIFACT</td>
<td><p>Allows DICOM Importer II users to:</p>
<ul>
<li><p>Stage media at the study level</p></li>
<li><p>View images on the media</p></li>
<li><p>Associate study DICOM objects with an existing Radiology or Consult order for reconciliation.</p></li>
<li><p>Place new Radiology orders using the Importer II user interface.</p></li>
<li><p>Use DICOM Correct to fix errors in studies in the DICOM Correct queue.</p></li>
<li><p>Manage the DICOM Importer II queue</p></li>
<li><p>Run, view, print and save DICOM Importer II reports</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>MAGV IMPORT REPORTS</td>
<td>Allows DICOM Importer II users to view, print, and save reports to a text file.</td>
</tr>
</tbody>
</table>

### Workstation Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Workstations tend to collect dust inside of the chassis. They should be periodically opened and cleaned. The accumulation of dust can lead to heat damage of workstation components. Only a qualified individual should do further hardware maintenance.

> The monitors used with the VistARad diagnostic workstations require periodic calibration to maintain the proper grayscale luminance display characteristics necessary for accurate image quality. A program of maintenance for these monitors should be established and administered by the Biomedical Engineering staff. A calibration/maintenance log should be kept, as such documentation may be required for review by regulatory bodies.

### Changes to DICOM Modalities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When DICOM Modalities are added, or operational parameters are to be modified, see the *VistA Imaging DICOM Gateway User Manual* for the procedures to record the appropriate new values for the various parameters.

### Changes to Windows Servers and Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Any changes to Image server shares or server security require updates to VistA files. See the

> *VistA Imaging System Installation Guide* for details.

### Microsoft Patch Installation Guidelines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Sites should use the following guidelines for installing Microsoft patches on VistA Imaging Clinical workstations, DICOM gateways, VistARad workstations, DICOM Importer II workstations, and Imaging file servers.

> The nature of the Microsoft patch dictates if it should be installed immediately, after validation, or not at all. For any patch that is installed, use steps detailed in “Procedures for Updates” below.

- Critical security updates - Install immediately after they are released from Microsoft.
- Service Packs - VistA Imaging will verify with solution vendors that there are no known issues and then will field test the service packs at 4 test sites with monitoring. The field test will last approximately 2 weeks. If no issues arise, all sites will be instructed to install the service pack.
- Internet Explorer major version upgrades – Are to be handled the same as service pack updates.

> Note: IE-related critical security updates should be installed immediately after they are released from Microsoft.

- Minor software updates (media player, etc.) – Do not install unless validated by the VistA Imaging team.

#### Procedure for updates (critical components)

> All updates should be applied methodically to critical Imaging components (file servers, gateways, VistARad Workstations).

1.  Ensure that all VistA Imaging components are working properly before installing any updates.
2.  Ensure that service packs, non-critical Internet Explorer upgrades, and minor software updates are validated by VistA Imaging (see above).
3.  Schedule the installation for a time when system usage is low (in case a reboot is required).
4.  Apply each update one at a time.
5.  Apply each update to one critical system. Monitor that system for at least 1 day before updating other systems.
6.  Do not load updates on all critical systems without first testing on a single system of each type.
7.  Report any problems to the National Help Desk immediately.

#### Notes for Clinical Workstations

> For clinical (non-diagnostic) workstations, the following is recommended:

- Microsoft patches should be loaded one at a time, and onto a single workstation only.
- After verifying that the workstation works properly, and that no unexpected issues arise, the patch can be installed on all workstations.

> Any problems should be reported to the National Help Desk.

### Parameter Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MAG TR ALLOW THIN CLIENT

> Sites will be able to configure whether or not TeleReader will be able to access and read images on a workstation that accesses VistA Imaging through a Thin Client.

> MAG IMAGE ALLOW ANNOTATE

> This parameter definition controls the ability of users at a specific site to create annotations based on the following hierarchical levels:

- User
- Service
- Division
- System

> The VistA administrator or Information Resources Management (IRM) personnel can allow users to create annotations by changing the value of the parameter MAG IMAGE ALLOW ANNOTATE for an individual user account, for the users of a specific service at the site, for the user accounts that are part of a division, or for the entire site.

> Authorized users can access the MAG IMAGE ALLOW ANNOTATE parameter through the VistA menu option \[XPAR EDIT PARAMETER\].

> This page is intentionally left blank.

## Chapter 4 Security Software Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Security and Anti-virus Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA workstations are multi-purpose, multi-function medical systems. These workstations usually enable the users to run all of the VA’s application software (including VistA Imaging), the Microsoft Office Suite, e-mail, Internet and other commercial products, as needed by the hospital staff. The workstations should be configured to provide medical information security (as specified by the VA’s security staff), and they must have the latest version of anti-virus software protecting them.

> Additionally, if these workstations will be used to stage or import images from media (CD/DVDs), the media drives must be enabled. Ensure that the anti-virus software is configured to scan all files being staged, imported or copied from media.

> Windows security features should be used to restrict user access and protect system and other areas that should not be accessed by users. For additional information, see the *VistA Imaging Installation Guide* and the *VistA Imaging DICOM Gateway Installation Manual*.

> VistARad Diagnostic workstations must be excluded from automatic software update/inventory tracking packages, and any client software supporting these cannot be installed. For information about removing System Center Configuration Manager (SCCM), please review the *VistA Imaging Installation Guide*.

> This page is intentionally left blank.

## Chapter 5 Space, Staffing, and Standard Operating Procedures for VistA Imaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Infrastructure Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Networking

> VistA Imaging Clinical Workstations run best with at least a 100 mb/s network, however they can be run over a 10 mb/s network.

> The Background Processor (BP) application operates on a Windows-based PC. It is recommended that it operate on a file server that has a minimum of two gigabytes of RAM.

> The VistA Imaging DICOM Gateway requires a hospital network infrastructure having a backbone that will support Ethernet segments with at least 100 megabits per second throughput. It is best to place the servers and Background Processor on the same switch with the gateways. The HDIG runs several services that use several ports to communicate. These ports must be open. It is recommended the HDIG operates on a file server with eight gigabytes of RAM, the minimum is four gigabytes of RAM.

> VistA Imaging VistARad workstations should be on their own separate 1Gb/s network connection to the file servers whenever possible. This is especially important when more than two diagnostic workstations are in use in the radiology department. The VistARad workstations can run acceptably on a 100Mb/s network, but speed of image retrieval and display may be compromised.

> The VistA Imaging Exchange (VIX) service can be set up on the clustered server used for Imaging shares (recommended) or on a dedicated standalone server. If the VIX is set up on a standalone server, the server should have a 4Gb/s network connection to the Imaging cluster. For more information about the VIX, see the *VistA Imaging VIX Administrator’s Guide*.

#### Space

> Each VistA Imaging DICOM Gateway runs on a Windows-based workstation with a monitor having a resolution of 1280x1024 pixels or better. Space is required for the system, its monitor, keyboard and mouse.

> The Background Processor runs on a Windows-based file server and requires similar physical space.

> The VistARad software runs on a Windows-based workstation using one to four monitors having a resolution sufficient for diagnostic reading. An additional workstation running voice dictation software may be present as well. Allow adequate space for the workstation(s), all monitors, keyboards, pointing devices, and dictation devices. In addition, plan for adequate room cooling and for room lighting that is suitable for diagnostic reading requirements.

#### Power

> It is strongly recommended that the power supply to each VistA Imaging server, jukebox, DICOM Gateway, and Background Processor be safeguarded by means of an Uninterruptible Power Supply (UPS). This will reduce line voltage problems as well as protect against power outages.

#### Remote Access

> In order to allow the VistA Imaging Project Support Staff to gain access to the servers and workstations that are running the VistA Imaging, a copy of either PC-Anywhere (preferred) or Remotely Possible (servers) must be installed on each server or workstation. These should be configured as a *host*. These systems should never be hooked up to a modem.

#### Security

> Remote access must be password protected. Be sure to keep the VistA Imaging Project Support Staff updated when any such passwords are changed.

### Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### IRM Support Staff Requirements

> IRM support for VistA Imaging may require one or more staff members, depending on the size of the installation. These staff members must possess knowledge of VistA, Microsoft Windows, networking, and troubleshooting problems with Windows and TCP/IP. These staff members will need administrator privileges and should have a good foundation in Windows to cover troubleshooting, permissions and set-up. Network support will be needed to troubleshoot and maintain routing, wiring and configurations where packet filtering is in use.

> Team members should be comfortable with the following areas:

- *User Manager* for Domains
- Setting permissions
- Shares
- *Server Manager* for setting up shares
- *Event Viewer*
- *Ping*, *TraceRT, NetStat,* and *DICOM_Echo*
- *TCP/IP troubleshooting techniques*

> These staff members will be responsible for supporting Windows-based magnetic and jukebox servers, installing VistA Imaging patches, correcting information in VistA relating to the relationships between patients and images, installing workstations and workstation capture devices, and managing the Background Processor and DICOM gateways. This staff member is responsible for assigning Imaging security keys and menus to the users.

> VistA package support staff should cover the installation of Imaging KIDS patches and issues like translation tables and journaling. In addition, a staff member with experience in M should be available to assist in editing global variables and using FileMan to make corrections as necessary to correct situations such as the incorrect assignment of an image to a patient.

#### Biomedical Engineering Support Staff Requirements

> Someone experienced in Biomedical Engineering and/or network support will be needed to install and troubleshoot modalities, display and capture workstations, capture devices, network and server systems, and to calibrate diagnostic workstation monitors. The amount of time required for these duties will vary with the size and specifics of the installation.

> This staff will be responsible for ensuring that the modalities maintain their connections to the network and are able to communicate with the gateway systems. These staff members should be able to monitor modality traffic and to distribute modality traffic over different gateway processors, depending upon local traffic conditions and circumstances.

#### ADPAC Staff Requirements for Support for All Medical Services

> These staff members will need to know how to use, teach, and support the VistA Imaging system. They should have a close relationship with the IRM staff so that problems may be reported and so that they may be of assistance in the resolution of these problems. The ADPACs will need to assist in implementing and customizing the VistA Imaging System for various specialties. They will need to trouble-shoot issues related to how VistA Imaging System fits into the practice of medicine. They will be the first line of support in the use of the VistA Imaging package and will need to assist the end-users. ADPACs should be able to train key users who can then, in turn, train other users on the VistA Imaging System.

> The ADPACs will be responsible for being key advocates of the VistA Imaging system. It is essential that the ADPACs be proactive people. They will need to “walk the hospital” in the morning to be sure that users are not having problems. They will need to check on the modalities to ensure that they are working properly. These staff members may also be called upon to assist in correcting image header information, so that images are properly assigned to the right patients. The correcting of image headers is an event that does not happen often but one that may occur when the modality does not have an automatic worklist capability but requires end-user interaction to provide the patient name, social security number, and radiology accession number.

### Daily Activities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Standard practices should be followed, including doing complete backups prior to installation of any new software or patches. For every processor in the suite of equipment for the VistA Imaging system, documentation should be maintained indicating what versions of which software are running and when new versions or patches are installed. In addition, this documentation should include information on the dates of installation, and who participated in the installation of software, patches or updates, and any unusual occurrences at the time of installation. Records should be kept of any problems that occur at the site, their cause and resolution.

#### IRM Morning Routine

> Each morning the standard operating procedure should be to perform the tasks listed below in order to ensure the normal daily operation of the system.Check the Imaging Network

> Use Ping and other utilities, such as browsing, to ensure that all servers, gateways and modalities are reachable through the network.

#### Check Tier 2 for Sufficient Platters in the Write Path

> Physically check Tier 2 and its console to see which platters are currently loaded. Ensure that there are sufficient disks loaded to cover the day’s operations and that there are new ones available to be used when needed.

#### Check Current Write Locations for Sufficient Disk Space

> Check the disk space on the servers and gateways. If images are accumulating on the Image Gateway and are not being passed to the VistA Imaging Servers, check for gateway problems. Correct any header information to associate images with the correct patient and allow the gateway to get the images in question moved to the VistA Imaging Servers.

#### Check the Event Viewer Trap on Imaging Network

> Use the *Event Viewer* (under Administrative Tools) to display alerts. These logs may be filtered to show only warnings and alerts. It is a good practice to periodically save these logs to removable media and flush the logs. This will keep disk space usage to a minimum and still allow for old logs to be viewed.

#### Check the Imaging Background Processor

> Failed queues can be noted in the Queue Activity window in the BP Queue Processor window. Active and failed queue status, system wide, can be accessed from the menu option: View\|Purge Re-queue by type.

> Use the Queue Manager on the Background Processor to check for details about failed queues. The Queue Manager should be invoked by using the menu on the BP Queue Processor window. To check the failed queues, select Edit \| QueueManager\| All or Edit \| QueueManager\|

> *{queue}* and browse by queue type. The failed queues are sorted by error status.

![](vista-imaging-system-technical-manual/013.png)

> Alternately select Edit\|QueueManager \| *Queue Type*

> This information will provide some insight as to what processes are failing and why.

> Right-clicking in the message or group level provides a menu to Re-Queue or Purge Queue.

#### Check that the DICOM Image and Text Gateways are Up and Functioning

> Look for any error messages in the open windows. For each processor, make sure that there are windows open for listening and accepting images from those modalities that are assigned to that processor. MSM must be up and running on all gateways, as well as the display windows for the various monitoring sessions. If any of these are not running, restart them. Be sure that the VistA HIS is running.

#### Check that the DICOM Image Gateway Modalities are Sending Images

> The ADPACs and end-users will generally let the IRM know if the modalities are not able to send or store images, however, it is good practice to check on this at the beginning of the day. Check the queue lengths.

#### Review the Image_In Directory for Incomplete DCM Files

> Review the entries in the Dicom\Image_In directory for any files with “\_incomplete” appended to the file name. These are incomplete files received by a modality or a PACS interface that the DICOM image gateway could not process. Research the files to see if the entity resent them at a later time or the images were never received. These files will automatically be purged after one hour.

> On the main hospital system, check to see if the DICOM FAILED IMAGES file (#2006.575) has entries that need correcting. If there are “failed image files”, work with the ADPACs and end-users to correct the information in the image headers and to associate these image files with the correct patients.

#### Review the M Error Traps

> Review the M error traps on all of the DICOM Gateways and the main hospital system. Look for error messages related to the imaging routines (MAG\*). If there are any errors that cannot be resolved by the local IRM staff, log a Remedy call so the VistA Imaging support staff may assist in their resolution. However, local IRM staff can easily address most error conditions.

#### Check the Hybrid Image DICOM Gateway (HDIG) Statistics and Log Files

> For information about accessing the HDIG statistics and logs, see the *VistA Imaging DICOM Gateway User Manual*.

### Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Do an incremental tape backup of all active Imaging Tier 1 shares (for new images captured) or update copy media if doing media copies on the Tier 2 shares. Active Tier 1 shares can be isolated by RAID group configuration.

### Weekly Activities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A RAID Group is a group of one-to-many shares that will be recognized as a unit within the Imaging storage network. Its purpose is to reduce the number of active storage shares in order to facilitate quicker tape backups (both incremental and full). Newly acquired images are distributed evenly among all the shares within a RAID Group.

> Do a full backup of active Imaging Tier 1 shares using the procedures in place at your site. For additional information, refer to Appendixes B and C in the *VistA Imaging Installation Guide*.

### Other Periodic Activities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Support for the VistA Imaging systems includes activities for support of Windows-based servers and the VistA System. Backups should be made for all systems. Current patches should be loaded for VistA. Service Packs for Windows and updates to the VistA Imaging software should be installed as they are released.

- Use the BP Queue Manager to re-queue failed entries and to purge the queues.
- Use the MagUtility program to maintain Tier 1 and Tier 2 storage resources. For details, see the *Storage Utilities User Manual*.
- Review the monthly Image Site Usage mail message to ensure all workstations have latest software installed.
- Before installing any new software or patches, first do a full backup, including the Registry files.
- For the VistARad diagnostic workstation monitors, calibration should be checked on a scheduled basis, at least monthly—more frequently is preferred. Consult the recommendations of the monitor manufacturer. Re-calibration should be performed whenever the calibration check reveals a need to do so. Also, whenever any part of the monitor/video driver hardware configuration is altered, a new calibration must be performed. Examples of configuration changes include: re-setting brightness or contrast controls; removing or replacing a monitor; removing or replacing a video board; replacing the system PC; etc.

### Scheduled Down Time for VistA Servers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> During a VistA System outage, DICOM Gateways will continue to provide modality worklist functionality and to capture images that are temporarily stored on the gateway. This is important to allow the radiology department to continue to perform studies. If you anticipate that the VistA System must be down, it is best to take the following steps:

- Perform all DICOM fixes before the VistA System goes down. This will free the maximum space for temporary image storage.

> During the outage, watch the gateways to be sure they still have adequate space to store images.

> This page is intentionally left blank.

## Chapter 6 Routine Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *The Food and Drug Administration classifies this software as a medical device. As such, it may not be changed in any way. Modifications to this software may result in an adulterated medical device under 21CFR820, the use of which is considered to be a violation of US Federal Statutes.*

> *VA Policy states the following:*

> *Those components of a national package (routines, data dictionaries, options, protocols, GUI components, etc.) that implement a controlled procedure, contain a controlled or strictly defined interface or report data to a database external to the local facility, must not be altered except by the Office of Information (OI) Technical Services (TS) staff. A controlled procedure is one that implements requirements that are mandated or governed by law or VA (Department of Veterans Affairs) directive or is subject to governing financial management standards of the Federal Government and VA or that is regulated by oversight groups such as the JCAHO or FDA. A controlled or strictly defined interface is one that adheres to a specific industry standard, will adversely affect a package and/or render the package inoperable if modified or deleted. For national software that is subject to FDA oversight, only the holder of the premarketing clearance (510(k)) is allowed to modify code for the medical device. The holder of a premarketing clearance is restricted to specifically designated TS staff that are located at the registered manufacturing site and operating in the designated production environment.*

### VistA Imaging Routines on the VistA Hospital Information System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Build Checksums

The Calculate and Show Checksum Values \[XTSUMBLD-CHECK\] menu option can be used as shown below to display a list of checksums for a specified build (KIDS file).

![](vista-imaging-system-technical-manual/014.png)

#### Package Checksums

The Calculate and Show Checksum Values \[XTSUMBLD-CHECK\] menu option can be used as shown below to display a list of checksums for all routines in the Imaging Package. Imaging routines are under the MAG namespace.

![](vista-imaging-system-technical-manual/015.png)

#### Routine Descriptions

To obtain a brief description for all VistA Imaging routines, use the First Line Routine Print \[XU FIRST LINE PRINT\] menu option. Including the second line in the report will show which patches have made changes to the routine. This menu option is part of Programmer Options \[XUPROG\] under sub-menu Routine Tools \[XUPR-ROUTINE-TOOLS\].

VistA Imaging routines are under the MAG namespace. The following is an example:

![](vista-imaging-system-technical-manual/016.png)

### DICOM Gateway Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Imaging DICOM Gateway requires a number of M routines. Most of these are part of the VistA Imaging package. However, because the DICOM gateways run as standalone workstations, they must include some routines from other packages. A few routines must run in the manager UCI.

#### Checksums of VistA Imaging DICOM Gateway Routines

The following listing reflects the VistA Imaging M routines that reside on the VistA Imaging DICOM gateway system.

| Routine | Checksum | Routine | Checksum | Routine | Checksum |
|-------------|--------------|-------------|--------------|-------------|--------------|
| MAG7UP      | 35026309     | MAGDACU     | 9404510      | MAGDAIRM    | 117531807    |
| MAGBRTA4    | 73323436     | MAGDACU0    | 10807003     | MAGDAIRP    | 31922397     |
| MAGBRTA5    | 74916344     | MAGDACU1    | 38544788     | MAGDAIRR    | 91423560     |
| MAGBRTA6    | 10352181     | MAGDACU2    | 7237662      | MAGDAIRS    | 15785148     |
| MAGBRTB1    | 26772420     | MAGDACU3    | 8904229      | MAGDAIRU    | 124794686    |
| MAGBRTB2    | 62448973     | MAGDACW1    | 48007177     | MAGDAIRW    | 28060731     |
| MAGBRTB3    | 21639509     | MAGDACW2    | 26199743     | MAGDAUD1    | 21787487     |
| MAGBRTB4    | 29268889     | MAGDAIR1    | 38225804     | MAGDAUD2    | 11632745     |
| MAGBRTK     | 20097310     | MAGDAIR2    | 174066539    | MAGDAUD3    | 4475591      |
| MAGBRTLR    | 10848658     | MAGDAIR3    | 96391606     | MAGDBB      | 19747360     |
| MAGBRTP1    | 30941600     | MAGDAIR4    | 110325747    | MAGDBB2     | 44540545     |
| MAGDACP1    | 74390040     | MAGDAIR5    | 65081294     | MAGDCIGL    | 22088679     |
| MAGDACP2    | 5612621      | MAGDAIR6    | 179937644    | MAGDCIRL    | 14772888     |
| MAGDACP3    | 46008004     | MAGDAIRA    | 57712921     | MAGDCMPE    | 19614608     |
| MAGDACR1    | 33293963     | MAGDAIRC    | 21720426     | MAGDCST1    | 15269197     |
| MAGDACR2    | 16258693     | MAGDAIRD    | 93443153     | MAGDCST2    | 11326972     |
| MAGDACR3    | 55462381     | MAGDAIRL    | 21354401     | MAGDCST3    | 86034617     |
| MAGDCST4    | 37159893     | MAGDHR5     | 3902302      | MAGDIR7F    | 32599821     |
| MAGDCST5    | 11640174     | MAGDHR9     | 7550226      | MAGDIR7G    | 9410773      |
| MAGDCST6    | 21003965     | MAGDHRC     | 86680704     | MAGDIR7T    | 38613863     |
| MAGDDEL     | 4367093      | MAGDHRC0    | 7768511      | MAGDIRDE    | 8549629      |
| MAGDDEL1    | 7861418      | MAGDHRC1    | 32850852     | MAGDIW2A    | 17353490     |
| MAGDDEL2    | 31000923     | MAGDHRC2    | 25348186     | MAGDIW3     | 20340399     |
| MAGDDEL3    | 7544616      | MAGDHRC3    | 127795528    | MAGDIW3A    | 85967674     |
| MAGDDR0     | 57333954     | MAGDHRC4    | 138693297    | MAGDIW3B    | 39882981     |
| MAGDDR1     | 48401978     | MAGDHRC5    | 109418054    | MAGDIW3C    | 14730954     |
| MAGDDR2     | 33721647     | MAGDHRC6    | 32964204     | MAGDIW4     | 20553707     |
| MAGDDR2A    | 103732840    | MAGDHRC7    | 19766889     | MAGDIW6     | 33599253     |
| MAGDDR3     | 55887980     | MAGDHRCP    | 44418147     | MAGDIWB0    | 5743080      |
| MAGDDR7     | 19337667     | MAGDHRCU    | 4706071      | MAGDIWB1    | 82684636     |
| MAGDDW0     | 18480829     | MAGDIR3     | 32120170     | MAGDIWB2    | 51239563     |
| MAGDDW1     | 33395508     | MAGDIR4A    | 9771049      | MAGDIWB5    | 94186343     |
| MAGDDW2     | 52939670     | MAGDIR5     | 7586177      | MAGDIWB7    | 16107756     |
| MAGDDW3     | 37085878     | MAGDIR6     | 88850067     | MAGDIWBA    | 81638859     |
| MAGDDW4     | 82471058     | MAGDIR6A    | 13107192     | MAGDIWBB    | 69921591     |
| MAGDECHO    | 9429115      | MAGDIR6B    | 21857231     | MAGDIWBC    | 86128746     |
| MAGDEXC1    | 41469390     | MAGDIR6C    | 45366757     | MAGDIWBD    | 30843111     |
| MAGDEXC2    | 53045931     | MAGDIR6D    | 24854094     | MAGDIX      | 5690876      |
| MAGDFCNS    | 89968928     | MAGDIR6E    | 23447535     | MAGDIX1     | 28030316     |
| MAGDFND0    | 23608364     | MAGDIR6F    | 22472350     | MAGDLOGI    | 18187840     |
| MAGDFND1    | 17372953     | MAGDIR6G    | 8628791      | MAGDLOGN    | 67846184     |
| MAGDFND2    | 103160968    | MAGDIR7     | 4535461      | MAGDM2MB    | 16447591     |
| MAGDFND3    | 108714097    | MAGDIR71    | 67975394     | MAGDMENA    | 55414961     |
| MAGDFND4    | 46237039     | MAGDIR72    | 4436051      | MAGDMENL    | 7216238      |
| MAGDFND5    | 11438147     | MAGDIR73    | 5722083      | MAGDMENO    | 39923631     |
| MAGDFND9    | 5028212      | MAGDIR74    | 6275398      | MAGDMENU    | 51445030     |
| MAGDGEX1    | 76377251     | MAGDIR75    | 50725923     | MAGDMFB     | 47598711     |
| MAGDGEX2    | 25589452     | MAGDIR7C    | 89687601     | MAGDMFB1    | 85395849     |
| MAGDGLC     | 36322745     | MAGDIR7D    | 16648443     | MAGDMFB2    | 49214267     |
| MAGDMFB3    | 41066270     | MAGDQUE3    | 28047976     | MAGOSFIL    | 37547909     |
| MAGDMFB4    | 15205941     | MAGDQUE4    | 27764385     | MAGOSMSC    | 51783237     |
| MAGDMFB5    | 25775790     | MAGDRPC0    | 4862620      | MAGOSTCP    | 32979219     |
| MAGDMFB6    | 19405158     | MAGDSSD     | 6477867      | MAGSPID     | 3966944      |
| MAGDMFB7    | 26178773     | MAGDSTA1    | 68354778     | MAGUE       | 75297995     |
| MAGDMFB8    | 13147824     | MAGDSTAT    | 52825843     | MAGVCSTR    | 11185442     |
| MAGDMFB9    | 25588255     | MAGDSTRT    | 14101280     | MAGVDGW1    | 14542314     |
| MAGDMFBA    | 16186541     | MAGDTCP     | 6918159      |             |              |
| MAGDMFBB    | 53824931     | MAGDTCP1    | 69855871     |             |              |
| MAGDMFBC    | 36412183     | MAGDTCP2    | 29403903     |             |              |
| MAGDMFBD    | 38641825     | MAGDTCP3    | 10117098     |             |              |
| MAGDMFBE    | 86462667     | MAGDTGA     | 5398596      |             |              |
| MAGDMFBI    | 29578964     | MAGDTLOG    | 20351436     |             |              |
| MAGDMFBM    | 87591678     | MAGDUID1    | 3785565      |             |              |
| MAGDMFBN    | 5306612      | MAGDUID2    | 6700589      |             |              |
| MAGDMFBP    | 17921307     | MAGDUID4    | 21494340     |             |              |
| MAGDMFBS    | 52098283     | MAGDVRSN    | 3291181      |             |              |
| MAGDMFBT    | 19123785     | MAGDWLKL    | 36028521     |             |              |
| MAGDMFBW    | 97895675     | MAGDWLP2    | 3990165      |             |              |
| MAGDMFCC    | 25444929     | MAGDWLP3    | 78343810     |             |              |
| MAGDMFIC    | 46728636     | MAGDWLPA    | 69861115     |             |              |
| MAGDMLGV    | 76186792     | MAGDWLPB    | 55436315     |             |              |
| MAGDMLOG    | 32785216     | MAGDWLPC    | 16460081     |             |              |
| MAGDMMSG    | 53806690     | MAGDWLU     | 4339594      |             |              |
| MAGDMPPC    | 8533330      | MAGDWLU0    | 38702922     |             |              |
| MAGDMSGT    | 9617440      | MAGDWLU1    | 44796296     |             |              |
| MAGDOS      | 5971106      | MAGDWLU2    | 104897245    |             |              |
| MAGDQR15    | 17707603     | MAGDWLU3    | 5869877      |             |              |
| MAGDQRU0    | 5735145      | MAGDWLU4    | 59848201     |             |              |
| MAGDQUE0    | 30499869     | MAGM2VC     | 89722252     |             |              |
| MAGDQUE1    | 32915712     | MAGM2VCU    | 20477697     |             |              |
| MAGDQUE2    | 21951411     | MAGOSDIR    | 28047976     |             |              |

#### DICOM Gateway Routine Descriptions

> The M routines on the DICOM Gateway can be listed using the FIRST ROUTINE LINE DISPLAY routine (%RFIRST). The following is an example of steps required to use the % RFIRST routine to list Imaging routines.

![](vista-imaging-system-technical-manual/017.png)

> See the previous section for the checksums of the distributed routines.

#### Kernel RPC Broker Routines

> Two RPC Broker routines are incorporated into the DICOM Gateway software. See the *VistA Imaging Security Guide* for more information.

### Non-M Routines Distributed as Executable Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Executable, DLL and other supporting files, which are distributed, include capture device- specific imaging software and executable imaging software. The routine listing below is by function.

#### Clinical Workstation Files

> The following tables list files installed on a Clinical (Display or Capture) workstation.

> Note: Under Windows 7, some “system” files (including executable program files) may be stored in different directories than under Windows XP. Table headings below indicate only the Windows XP pathnames. Windows 7 pathnames are similar, with these changes:

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Windows XP</strong></th>
<th><strong>Windows 7</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>C:\Program Files\...</td>
<td><blockquote>
<p>C:\Program Files (x86)\...</p>
</blockquote></td>
</tr>
<tr class="even">
<td>C:\Windows\system32\...</td>
<td>C:\Windows\SystemWoW64 C:\Windows\System32</td>
</tr>
</tbody>
</table>

> C:\Windows\SystemWoW64 is used for 32-bit files. C:\Windows\System32 is used for 64-bit files. This may sound backward, but it has to do with backward compatibility requirements.

> SysWoW64, standing for Windows 32-bit on Windows 64-bit, contains program files for 32-bit compatibility used on a 64-bit system. A Windows 7 emulator redirects calls for any “System32” files to the SysWoW64 folder.

> Configuration and log file pathnames are changed as follows:

<table>
<colgroup>
<col style="width: 57%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Windows XP</strong></th>
<th><strong>Windows 7</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>C:\Documents and Settings\All Users\Application Data\Vista\Imaging\mag.ini (TeleReader)</p>
<p>C:\Documents and Settings\All Users\Application Data\Vista\Imaging\mag308.ini (Clinical Display and Clinical Capture)</p></td>
<td><p>C:\ProgramData\Vista\Imaging\mag.ini (TeleReader)</p>
<p>C:\ProgramData\Vista\Imaging\mag308.ini (Clinical Display and Clinical Capture)</p></td>
</tr>
<tr class="even">
<td>C:\Documents and Settings\All Users\Application Data\Vista\Imaging \MagTeleReaderConfig.ini</td>
<td>C:\ProgramData\Vista\Imaging\ MagTeleReaderConfig.ini</td>
</tr>
<tr class="odd">
<td>C:\Documents and Settings\All Users\Application Data\Vista\Imaging\Log\MagTeleReaderConfig100420120 34524PM.log*</td>
<td>C:\ProgramData\Vista\Imaging\ Log\MagTeleReaderConfig100420120345 24PM.log*</td>
</tr>
</tbody>
</table>

> \*The name of the log file is based on MagTeleReaderConfig + date time stamp.

> The following tables list files installed on a Clinical (Display or Capture) workstation.

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 34%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p><strong>Clinical Display &amp; Capture files</strong></p>
<p><strong>Windows XP 32-bit -- C:\Program Files\VistA\Imaging Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ABSTRTGA.EXE</td>
<td>HSUMM.TXT</td>
<td rowspan="13"><p>MagScanFilm.EXE MagSCREEN.HLP</p>
<p>Magsys.cnt MAGSYS.EXE</p>
<p>Magsys.hlp MAGSYS.ini MagSysKey.CNT MAGSYSKEY.HLP</p>
<p><strong>MagTeleReader.exe MagTeleReaderConfig.exe</strong> magupdate.ini magwrks.CNT MAGWRKS.EXE</p>
<p>Magwrks.hlp MEANSTEST.HLP</p>
<p>SCNAPI.DLL</p></td>
</tr>
<tr class="even">
<td>ActiveMILDefault.exe</td>
<td>ImagDEMO.DAT</td>
</tr>
<tr class="odd">
<td>Annotation Editor Help.cnt</td>
<td>mag308.ini*</td>
</tr>
<tr class="even">
<td><p>ANNOTATION EDITOR HELP.HLP</p>
<p>demo12.txtDEMO1802.T XT</p></td>
<td><p>MagDemos.TXTMagEKGVi ew.hlp<strong>MagImageCapture.e xe</strong></p>
<p>MAGIMAGEDELETE.HLP</p></td>
</tr>
<tr class="odd">
<td>DEMO2230.TXT</td>
<td><strong>MagImageDisplay.exe</strong></td>
</tr>
<tr class="even">
<td>demo3.txt</td>
<td>magIniPermissions.bat</td>
</tr>
<tr class="odd">
<td>DEMO446.TXT</td>
<td>MagMinibld.EXE</td>
</tr>
<tr class="even">
<td>demolist.txt</td>
<td>magPermissions.bat</td>
</tr>
<tr class="odd">
<td>DocScan.cnt</td>
<td>MagScan150N.BAT</td>
</tr>
<tr class="even">
<td>DOCSCAN.HLP</td>
<td>MagScan75N.BAT</td>
</tr>
<tr class="odd">
<td>ERRLOOK.EXE</td>
<td>MagScanFile.EXE</td>
</tr>
<tr class="even">
<td>ERRLOOK.HLP</td>
<td></td>
</tr>
<tr class="odd">
<td>FRAMGRAB.EXE</td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><p><em>The main application files are shown in bold.</em></p>
<p><em>Files ending in ‘.cnt’ and ‘.hlp’ are contents for help files and help files.</em></p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p><strong>Icons used by Clinical Display &amp; Capture</strong></p>
<p><strong>Windows XP 32-bit -- C:\Program Files\VistA\Imaging Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>abscine.bmp</td>
<td>DoD_PDF.bmp</td>
<td>magrtf.bmp</td>
</tr>
<tr class="even">
<td>absekg.bmp</td>
<td>DoD_PDF.psd</td>
<td>magtext.bmp</td>
</tr>
<tr class="odd">
<td>ABSERROR.BMP</td>
<td>DoD_RTF.bmp</td>
<td>magwav.bmp</td>
</tr>
<tr class="even">
<td>absjbox.bmp</td>
<td>DoD_RTF.psd</td>
<td>MotionVideo.bmp</td>
</tr>
<tr class="odd">
<td>abspacg.bmp</td>
<td>DoD_Unavailable.bmp</td>
<td>Magblack.bmp</td>
</tr>
<tr class="even">
<td>abspaci.bmp</td>
<td>DoD_Unavailable.psd</td>
<td>magdoc.bmp</td>
</tr>
<tr class="odd">
<td>absremote.bmp</td>
<td>DoD_Word.bmp</td>
<td>maghtml.bmp</td>
</tr>
<tr class="even">
<td>AnnotPencilSmall.bmp</td>
<td>DoD_Word.psd</td>
<td>magpdf.bmp</td>
</tr>
<tr class="odd">
<td>AnnotReadOnly.bmp</td>
<td>downarrow1.bmp</td>
<td>magsensitive.bmp</td>
</tr>
<tr class="even">
<td>AnnotReadOnly.psd</td>
<td>ImageQA.bmp</td>
<td>magtext.bmp</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p><strong>Icons used by Clinical Display &amp; Capture</strong></p>
<p><strong>Windows XP 32-bit -- C:\Program Files\VistA\Imaging Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>BLANK2.bmp</p>
<p>BLANK.BMP</p></td>
<td>InternalError.bmp FileOpenError.bmp</td>
<td><p>magwav.bmp</p>
<p>MotionVideo.bmp</p></td>
</tr>
<tr class="even">
<td>Blank.tga</td>
<td>FullResFileNotFound.bmp</td>
<td>MotionVideoAbs.bmp</td>
</tr>
<tr class="odd">
<td>CAPTURE.BMP</td>
<td>FullResFileOpenError.bmp</td>
<td>NOTEXIST.BMP</td>
</tr>
<tr class="even">
<td>DoD_ASCII.bmp</td>
<td>ImageUnavailable.bmp</td>
<td>PRECAP.BMP</td>
</tr>
<tr class="odd">
<td>DoD_ASCII.psd</td>
<td>jboffln.abs</td>
<td>magBlockedImage.bmp</td>
</tr>
<tr class="even">
<td>DoD_Doc.bmp</td>
<td>JBOFFLN.bmp</td>
<td>magsensitive.bmp</td>
</tr>
<tr class="odd">
<td>DoD_Doc.psd</td>
<td>JBOFFLN.tga</td>
<td>uparrow1.bmp</td>
</tr>
<tr class="even">
<td>DoD_JPG.bmp</td>
<td>magavi.bmp</td>
<td></td>
</tr>
<tr class="odd">
<td>DoD_JPG.psd</td>
<td>magBlockedImage.bmp</td>
<td></td>
</tr>
<tr class="even">
<td>DoD_NCAT.bmp</td>
<td>magDeletedGroup.bmp</td>
<td></td>
</tr>
<tr class="odd">
<td>DoD_NCAT.psd</td>
<td>magDeletedImage.bmp</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p><strong>Sample images (obsolete)</strong></p>
<p><strong>Windows XP 32-bit -- C:\Program Files\VistA\Imaging\Image Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging\Image</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><em>These files are no longer distributed as of Patch 8, but may be present on older workstations. These files are no longer used.</em></td>
</tr>
<tr class="even">
<td>BLACKBOX.TGA</td>
<td>DILB3.BMP</td>
<td>Samples.txt</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 30%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p><strong>XP 32-bit -- C:\Program Files\VistA\Imaging\Help\Client</strong></p>
<p><strong>Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging\ Help\Client</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><em>All files in this directory are help files for the VistA Imaging Display and Capture clients.</em></td>
</tr>
<tr class="even">
<td colspan="3"><strong>Windows XP 32-bit -- C:\Program Files\VistA\Imaging\Lib Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging\Lib</strong></td>
</tr>
<tr class="odd">
<td>ACE.dll AGM.dll BIB.dll</td>
<td><p>GEAR32PO.OCX</p>
<p>ig_cmyk_profile.icm ig_rgb_profile.icm</p></td>
<td>igMED15a.ocx igmed15d.dll igmed32s.dll</td>
</tr>
</tbody>
</table>

| Windows XP 32-bit -- C:\Program Files\VistA\Imaging\Lib Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging\Lib |                  |                           |
|-------------------------------------------------------------------------------------------------------------------------|------------------|---------------------------|
| BIBUtils.dll                                                                                                            | igART15a.ocx     | IGMed32x.ocx              |
| DL70ACE.dll                                                                                                             | igartgui15d.dll  | igmult15d.dll             |
| DL70AdobeXMP.dll                                                                                                        | igCORE15a.ocx    | igMULTIMEDIA15a.ocx       |
| DL70AGM.dll                                                                                                             | igCORE15d.dll    | igPDF15a.ocx              |
| DL70ARE.dll                                                                                                             | igDISPLAY15a.ocx | igPROCESSING15a.ocx       |
| DL70AXE8SharedExpat.dll                                                                                                 | igDLGS15a.ocx    | igVECT15a.ocx             |
| DL70AXE16SharedExpat.dll                                                                                                | igEFFECTS15a.ocx | igVIEW15a.ocx             |
| DL70BIB.dll                                                                                                             | igFORMATS15a.ocx | JP2KLib.dll               |
| DL70BIBUtils.dll                                                                                                        | igguidlg15a.dll  | kdu_v52R.dll              |
| DL70CoolType.dll                                                                                                        | igguiwin15a.dll  | MagAnnOCX.ocx             |
| DL70JP2KLib.dll                                                                                                         | igJPEG2K15a.ocx  | MagAnnTool.dllnserver.dll |
| DL70PDFL.dll                                                                                                            | igLZW15a.ocx     | SliceCalc.dll             |
|                                                                                                                         |                  | XRefUtils.dll             |

| Windows XP 32-bit -- C:\Program Files\VistA\Imaging\\ Lib\Accusoft16.2 Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging\\ Lib\Accusoft16.2 |                          |                              |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|------------------------------|
| ACE.dll                                                                                                                                               | ig_cmyk_profile.icm      | igMED16a.ocxigMULTIMEDIA16   |
| AGM.dll                                                                                                                                               | ig_rgb_profile.icm       | a.ocx                        |
| BIB.dll                                                                                                                                               | igART16a.ocx             | igPDF16a.ocxigPROCESSING16a. |
| BIBUtils.dll                                                                                                                                          | igartgui16d.dll          | ocx                          |
| DL81ACE.dll                                                                                                                                           | igArtX16a.ocx            | igtwain16a.ocx               |
| DL81AdobeXMP.dll                                                                                                                                      | igArtX16d.dll            | igtwain16d.dll               |
| DL81AGM.dll                                                                                                                                           | IGArtXGUI16a.ocx         | igVECT16a.ocxigVIEW16a.ocx   |
| DL81ARE.dll                                                                                                                                           | igArtXGUI16d.dll         | JP2KLib.dll                  |
| DL81AXE8SharedExpa                                                                                                                                    | igCORE16a.ocxigDISPLAY16 | kdu_v52R.dll                 |
| t.dll                                                                                                                                                 | a.ocx                    | mfc71.dll                    |
| DL81BIB.dll                                                                                                                                           | igDLGS16a.ocx            | msvcp71.dll                  |
| DL81BIBUtils.dll                                                                                                                                      | igEFFECTS16a.ocx         | msvcr71.dll                  |
| DL81CoolType.dll                                                                                                                                      | igFORMATS16a.ocx         | nserver.dll                  |
| DL81JP2KLib.dll                                                                                                                                       | igguidlg16a.ocx          |                              |
| DL81PDFL.dll                                                                                                                                          | igguidlg16a.dll          |                              |
|                                                                                                                                                       | igguiwin16a.dll          |                              |
|                                                                                                                                                       | igJBIG216a.ocx           |                              |
|                                                                                                                                                       | igJBIG216d.dll           |                              |
|                                                                                                                                                       | igJPEG2K16a.ocx          |                              |
|                                                                                                                                                       | igjpeg2k16d.dll          |                              |
|                                                                                                                                                       | igLZW16a.ocx             |                              |
|                                                                                                                                                       | iglzw16d.dll             |                              |

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 30%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p><strong>PDF support files</strong></p>
<p><strong>Windows XP 32-bit -- C:\Program Files\VistA\Imaging\ Lib\Resource\PDF\CMap Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging\ Lib\Resource\PDF\CMap</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>78-EUC-H</td>
<td>B5pc-H</td>
<td>KSCms-UHC-H</td>
</tr>
<tr class="even">
<td>78-EUC-V</td>
<td>B5pc-UCS2</td>
<td>KSCms-UHC-HW-H</td>
</tr>
<tr class="odd">
<td>78-H</td>
<td>B5pc-UCS2C</td>
<td>KSCms-UHC-HW-V</td>
</tr>
<tr class="even">
<td>78-RKSJ-H</td>
<td>B5pc-V</td>
<td>KSCms-UHC-UCS2</td>
</tr>
<tr class="odd">
<td>78-RKSJ-V</td>
<td>CNS-EUC-H</td>
<td>KSCms-UHC-V</td>
</tr>
<tr class="even">
<td>78-V</td>
<td>CNS-EUC-V</td>
<td>KSCpc-EUC-H</td>
</tr>
<tr class="odd">
<td>78ms-RKSJ-H</td>
<td>CNS1-H</td>
<td>KSCpc-EUC-UCS2</td>
</tr>
<tr class="even">
<td>78ms-RKSJ-V</td>
<td>CNS1-V</td>
<td>KSCpc-EUC-UCS2C</td>
</tr>
<tr class="odd">
<td>83pv-RKSJ-H</td>
<td>CNS2-H</td>
<td>KSCpc-EUC-V</td>
</tr>
<tr class="even">
<td>90ms-RKSJ-H</td>
<td>CNS2-V</td>
<td>NWP-H</td>
</tr>
<tr class="odd">
<td>90ms-RKSJ-UCS2</td>
<td>ETen-B5-H</td>
<td>NWP-V</td>
</tr>
<tr class="even">
<td>90ms-RKSJ-V</td>
<td>ETen-B5-UCS2</td>
<td>RKSJ-H</td>
</tr>
<tr class="odd">
<td>90msp-RKSJ-H</td>
<td>ETen-B5-V</td>
<td>RKSJ-V</td>
</tr>
<tr class="even">
<td>90msp-RKSJ-V</td>
<td>ETenms-B5-H</td>
<td>Roman</td>
</tr>
<tr class="odd">
<td>90pv-RKSJ-H</td>
<td>ETenms-B5-V</td>
<td>UCS2-90ms-RKSJ</td>
</tr>
<tr class="even">
<td>90pv-RKSJ-UCS2</td>
<td>ETHK-B5-H</td>
<td>UCS2-90pv-RKSJ</td>
</tr>
<tr class="odd">
<td>90pv-RKSJ-UCS2C</td>
<td>ETHK-B5-V</td>
<td>UCS2-B5pc</td>
</tr>
<tr class="even">
<td>90pv-RKSJ-V</td>
<td>EUC-H</td>
<td>UCS2-ETen-B5</td>
</tr>
<tr class="odd">
<td>Add-H</td>
<td>EUC-V</td>
<td>UCS2-GBK-EUC</td>
</tr>
<tr class="even">
<td>Add-RKSJ-H</td>
<td>Ext-H</td>
<td>UCS2-GBpc-EUC</td>
</tr>
<tr class="odd">
<td>Add-RKSJ-V</td>
<td>Ext-RKSJ-H</td>
<td>UCS2-KSCms-UHC</td>
</tr>
<tr class="even">
<td>Add-V</td>
<td>Ext-RKSJ-V</td>
<td>UCS2-KSCpc-EUC</td>
</tr>
<tr class="odd">
<td>Adobe-CNS1-0</td>
<td>Ext-V</td>
<td>UniCNS-UCS2-H</td>
</tr>
<tr class="even">
<td>Adobe-CNS1-1</td>
<td>GB-EUC-H</td>
<td>UniCNS-UCS2-V</td>
</tr>
<tr class="odd">
<td>Adobe-CNS1-2</td>
<td>GB-EUC-V</td>
<td>UniCNS-UTF16-H</td>
</tr>
<tr class="even">
<td>Adobe-CNS1-3</td>
<td>GB-H</td>
<td>UniCNS-UTF16-V</td>
</tr>
<tr class="odd">
<td>Adobe-CNS1-4</td>
<td>GB-V</td>
<td>UniCNS-UTF32-H</td>
</tr>
<tr class="even">
<td>Adobe-CNS1-B5pc</td>
<td>GBK-EUC-H</td>
<td>UniCNS-UTF32-V</td>
</tr>
<tr class="odd">
<td>Adobe-CNS1-ETen-B5</td>
<td>GBK-EUC-UCS2</td>
<td>UniCNS-UTF8-H</td>
</tr>
<tr class="even">
<td>Adobe-CNS1-H-CID</td>
<td>GBK-EUC-V</td>
<td>UniCNS-UTF8-V</td>
</tr>
<tr class="odd">
<td>Adobe-CNS1-H-Host</td>
<td>GBK2K-H</td>
<td>UniGB-UCS2-H</td>
</tr>
<tr class="even">
<td>Adobe-CNS1-H-Mac</td>
<td>GBK2K-V</td>
<td>UniGB-UCS2-V</td>
</tr>
<tr class="odd">
<td>Adobe-CNS1-UCS2</td>
<td>GBKp-EUC-H</td>
<td>UniGB-UTF16-H</td>
</tr>
<tr class="even">
<td>Adobe-GB1-0</td>
<td>GBKp-EUC-V</td>
<td>UniGB-UTF16-V</td>
</tr>
<tr class="odd">
<td>Adobe-GB1-1</td>
<td>GBpc-EUC-H</td>
<td>UniGB-UTF32-H</td>
</tr>
<tr class="even">
<td>Adobe-GB1-2</td>
<td>GBpc-EUC-UCS2</td>
<td>UniGB-UTF32-V</td>
</tr>
<tr class="odd">
<td>Adobe-GB1-3</td>
<td>GBpc-EUC-UCS2C</td>
<td>UniGB-UTF8-H</td>
</tr>
<tr class="even">
<td>Adobe-GB1-4</td>
<td>GBpc-EUC-V</td>
<td>UniGB-UTF8-V</td>
</tr>
<tr class="odd">
<td>Adobe-GB1-GBK-EUC</td>
<td>GBT-EUC-H</td>
<td>UniHojo-UCS2-H</td>
</tr>
<tr class="even">
<td>Adobe-GB1-GBpc-EUC</td>
<td>GBT-EUC-V</td>
<td>UniHojo-UCS2-V</td>
</tr>
<tr class="odd">
<td>Adobe-GB1-H-CID</td>
<td>GBT-H</td>
<td>UniHojo-UTF16-H</td>
</tr>
<tr class="even">
<td>Adobe-GB1-H-Host</td>
<td>GBT-V</td>
<td>UniHojo-UTF16-V</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 30%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p><strong>PDF support files</strong></p>
<p><strong>Windows XP 32-bit -- C:\Program Files\VistA\Imaging\ Lib\Resource\PDF\CMap Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging\ Lib\Resource\PDF\CMap</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Adobe-GB1-H-Mac</td>
<td>GBTpc-EUC-H</td>
<td>UniHojo-UTF32-H</td>
</tr>
<tr class="even">
<td>Adobe-GB1-UCS2</td>
<td>GBTpc-EUC-V</td>
<td>UniHojo-UTF32-V</td>
</tr>
<tr class="odd">
<td>Adobe-Japan1-0</td>
<td>H</td>
<td>UniHojo-UTF8-H</td>
</tr>
<tr class="even">
<td>Adobe-Japan1-1</td>
<td>Hankaku</td>
<td>UniHojo-UTF8-V</td>
</tr>
<tr class="odd">
<td>Adobe-Japan1-2</td>
<td>Hiragana</td>
<td>UniJIS-UCS2-H</td>
</tr>
<tr class="even">
<td>Adobe-Japan1-3</td>
<td>HKdla-B5-H</td>
<td>UniJIS-UCS2-HW-H</td>
</tr>
<tr class="odd">
<td>Adobe-Japan1-4</td>
<td>HKdla-B5-V</td>
<td>UniJIS-UCS2-HW-V</td>
</tr>
<tr class="even">
<td>Adobe-Japan1-5</td>
<td>HKdlb-B5-H</td>
<td>UniJIS-UCS2-V</td>
</tr>
<tr class="odd">
<td>Adobe-Japan1-6</td>
<td>HKdlb-B5-V</td>
<td>UniJIS-UTF16-H</td>
</tr>
<tr class="even">
<td>Adobe-Japan1-90ms-RKSJ</td>
<td>HKgccs-B5-H</td>
<td>UniJIS-UTF16-V</td>
</tr>
<tr class="odd">
<td>Adobe-Japan1-90pv-RKSJ</td>
<td>HKgccs-B5-V</td>
<td>UniJIS-UTF32-H</td>
</tr>
<tr class="even">
<td>Adobe-Japan1-H-CID</td>
<td>HKm314-B5-H</td>
<td>UniJIS-UTF32-V</td>
</tr>
<tr class="odd">
<td>Adobe-Japan1-H-Host</td>
<td>HKm314-B5-V</td>
<td>UniJIS-UTF8-H</td>
</tr>
<tr class="even">
<td>Adobe-Japan1-H-Mac</td>
<td>HKm471-B5-H</td>
<td>UniJIS-UTF8-V</td>
</tr>
<tr class="odd">
<td>Adobe-Japan1-PS-H</td>
<td>HKm471-B5-V</td>
<td>UniJISPro-UCS2-HW-V</td>
</tr>
<tr class="even">
<td>Adobe-Japan1-PS-V</td>
<td>HKscs-B5-H</td>
<td>UniJISPro-UCS2-V</td>
</tr>
<tr class="odd">
<td>Adobe-Japan1-UCS2</td>
<td>HKscs-B5-V</td>
<td>UniJISPro-UTF8-V</td>
</tr>
<tr class="even">
<td>Adobe-Japan2-0</td>
<td>Hojo-EUC-H</td>
<td>UniJISX0213-UTF32-H</td>
</tr>
<tr class="odd">
<td>Adobe-Korea1-0</td>
<td>Hojo-EUC-V</td>
<td>UniJISX0213-UTF32-V</td>
</tr>
<tr class="even">
<td>Adobe-Korea1-1</td>
<td>Hojo-H</td>
<td>UniKS-UCS2-H</td>
</tr>
<tr class="odd">
<td>Adobe-Korea1-2</td>
<td>Hojo-V</td>
<td>UniKS-UCS2-V</td>
</tr>
<tr class="even">
<td>Adobe-Korea1-H-CID</td>
<td>Identity-H</td>
<td>UniKS-UTF16-H</td>
</tr>
<tr class="odd">
<td>Adobe-Korea1-H-Host</td>
<td>Identity-V</td>
<td>UniKS-UTF16-V</td>
</tr>
<tr class="even">
<td>Adobe-Korea1-H-Mac</td>
<td>Katakana</td>
<td>UniKS-UTF32-H</td>
</tr>
<tr class="odd">
<td>Adobe-Korea1-KSCms-UHC</td>
<td>KSC-EUC-H</td>
<td>UniKS-UTF32-V</td>
</tr>
<tr class="even">
<td>Adobe-Korea1-KSCpc-EUC</td>
<td>KSC-EUC-V</td>
<td>UniKS-UTF8-H</td>
</tr>
<tr class="odd">
<td>Adobe-Korea1-UCS2</td>
<td>KSC-H</td>
<td>UniKS-UTF8-V</td>
</tr>
<tr class="even">
<td>AdobeFnt09.lst</td>
<td>KSC-Johab-H</td>
<td>V</td>
</tr>
<tr class="odd">
<td>B5-H</td>
<td>KSC-Johab-V</td>
<td>vssver2.scc</td>
</tr>
<tr class="even">
<td>B5-V</td>
<td>KSC-V</td>
<td>WP-Symbol</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 30%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p><strong>PDF support files</strong></p>
<p><strong>Windows XP 32-bit -- C:\Program Files\VistA\Imaging\ Lib\Resource\PDF\Font Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging\ Lib\Resource\PDF\Font</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AdobeFnt09.lst vssver2.scc</td>
<td>zx .mmm</td>
<td>zy .mmm</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 30%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p><strong>MUSE API support files</strong></p>
<p><strong>Windows XP 32-bit -- C:\Program Files\VistA\Imaging\Muse Windows 7 64-bit -- C:\Program Files(x86)\VistA\Imaging\Muse</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Bti.ini</td>
<td>lfmac80n.dll</td>
<td>LTKRN80N.DLL</td>
</tr>
<tr class="even">
<td>BUTIL.EXE</td>
<td>lfmac80w.dll</td>
<td>LTKRN80W.DLL</td>
</tr>
<tr class="odd">
<td>ccalc32.dll</td>
<td>lfmsp80n.dll</td>
<td>LTTHK80W.DLL</td>
</tr>
<tr class="even">
<td>DCMUTL32.DLL</td>
<td>lfmsp80w.dll</td>
<td>LTTWN80N.DLL</td>
</tr>
<tr class="odd">
<td>lfavi80n.dll</td>
<td>lfpcd80n.dll</td>
<td>LTTWN80W.DLL</td>
</tr>
<tr class="even">
<td>lfavi80w.dll</td>
<td>lfpcd80w.dll</td>
<td>LTWND80N.DLL</td>
</tr>
<tr class="odd">
<td>lfawd80n.dll</td>
<td>lfpct80n.dll</td>
<td>LTWND80W.DLL</td>
</tr>
<tr class="even">
<td>lfbmp80n.dll</td>
<td>lfpct80w.dll</td>
<td>museapi.dll</td>
</tr>
<tr class="odd">
<td>lfbmp80w.dll</td>
<td>lfpcx80n.dll</td>
<td>museapi5a.dll</td>
</tr>
<tr class="even">
<td>lfcal80n.dll</td>
<td>lfpcx80w.dll</td>
<td>MUSEAPI5e.dll</td>
</tr>
<tr class="odd">
<td>lfcal80w.dll</td>
<td>lfpng80n.dll</td>
<td>MUSEAPI7.dll</td>
</tr>
<tr class="even">
<td><p>lfcmp80n.dll</p>
<p>lfcmp80w.dll</p></td>
<td><p>lfpng80w.dll</p>
<p>lfras80n.dll</p></td>
<td>museapiFAKE.dll (for non-MUSE sites)</td>
</tr>
<tr class="odd">
<td>lfdic80n.dll</td>
<td>lfras80w.dll</td>
<td>NWLOCALE.DLL</td>
</tr>
<tr class="even">
<td>lfdic80w.dll</td>
<td>lftga80n.dll</td>
<td>PRINTLIB.DLL</td>
</tr>
<tr class="odd">
<td>lfeps80n.dll</td>
<td>lftga80w.dll</td>
<td>Tabctl32.ocx</td>
</tr>
<tr class="even">
<td>lfeps80w.dll</td>
<td>lftif80n.dll</td>
<td>table32.dll</td>
</tr>
<tr class="odd">
<td>lffax80n.dll</td>
<td>lftif80w.dll</td>
<td>W3AIF103.DLL</td>
</tr>
<tr class="even">
<td>lffax80w.dll</td>
<td>lfwfx80n.dll</td>
<td>W3BIF106.DLL</td>
</tr>
<tr class="odd">
<td>lffpx7.dll</td>
<td>lfwfx80w.dll</td>
<td>W3BTRV7.DLL</td>
</tr>
<tr class="even">
<td>lffpx80n.dll</td>
<td>lfwmf80n.dll</td>
<td>W3CRS106.DLL</td>
</tr>
<tr class="odd">
<td>lfgif80n.dll</td>
<td>lfwmf80w.dll</td>
<td>W3MIF109.DLL</td>
</tr>
<tr class="even">
<td>lfgif80w.dll</td>
<td>lfwpg80n.dll</td>
<td>W3NSL105.DLL</td>
</tr>
<tr class="odd">
<td>lfica80n.dll</td>
<td>lfwpg80w.dll</td>
<td>W3NSR103.DLL</td>
</tr>
<tr class="even">
<td>lfica80w.dll</td>
<td>LTANN80N.DLL</td>
<td>W3SCMV7.DLL</td>
</tr>
<tr class="odd">
<td>lfimg80n.dll</td>
<td>LTANN80W.DLL</td>
<td>W3UPI104.DLL</td>
</tr>
<tr class="even">
<td>lfimg80w.dll</td>
<td>LTEFX80N.DLL</td>
<td>WBEXEC.EXE</td>
</tr>
<tr class="odd">
<td>lfkodak.dll</td>
<td>LTEFX80W.DLL</td>
<td>WBTRCALL.DLL</td>
</tr>
<tr class="even">
<td>lflma80n.dll lflma80w.dll</td>
<td>LTFIL80N.DLL LTFIL80W.DLL</td>
<td><p>WBTRV32.DLL</p>
<p>wcalc32.dll</p></td>
</tr>
<tr class="odd">
<td>lflmb80n.dll</td>
<td>LTIMG80N.DLL</td>
<td>zlib32.dll</td>
</tr>
<tr class="even">
<td>lflmb80w.dll</td>
<td>LTIMG80W.DLL</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 30%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><strong>Annotation Editor support files - AccuSoft OCX files Windows XP 32-bit -- C:\windows\system32 Windows 7 64-bit -- C:\windows\SysWoW64</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>igmed32s.dll</p>
</blockquote></td>
<td><blockquote>
<p>imgthumb.ocx</p>
</blockquote></td>
<td><blockquote>
<p>oissq400.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IGMed32x.ocx</p>
</blockquote></td>
<td><blockquote>
<p>jpeg1x32.dll</p>
</blockquote></td>
<td><blockquote>
<p>oitwa400.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>imgadmin.ocx</p>
</blockquote></td>
<td><blockquote>
<p>jpeg2x32.dll</p>
</blockquote></td>
<td><blockquote>
<p>oiui400.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>imgcmn.dll</p>
</blockquote></td>
<td><blockquote>
<p>oieng400.dll</p>
</blockquote></td>
<td><blockquote>
<p>tifflt.dll</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>imgedit.ocx</p>
</blockquote></td>
<td><blockquote>
<p>oiprt400.dll</p>
</blockquote></td>
<td><blockquote>
<p>xiffr3_0.dll</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>imgscan.ocx</p>
</blockquote></td>
<td><blockquote>
<p>oislb400.dll</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>imgshl.dll</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 30%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p><strong>Display CDA Stylesheet support files -</strong></p>
<p><strong>Windows XP 32-bit -- C:\Program Files\Vista\Imaging\stylesheets Windows 7 64-bit -- C:\Program Files (x86)\Vista\Imaging\stylesheets</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CDA.xsl</strong></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>Configuration File MAG.ini</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Windows XP 32-bit</strong></td>
<td><blockquote>
<p>C:\Documents and Settings\All Users\Application Data\Vista\Imaging\MAG.ini</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Windows 7 64-bit</strong></td>
<td><blockquote>
<p>C:\ProgramData\Vista\Imaging\MAG.ini</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Note: The directories in which some “system” files (including executable program files) are stored depend on the operating system on which the software is installed and on whether it is installed on a 32-bit computer or on a 64-bit computer. The following table lists the paths for the currently supported platforms.

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Windows XP 32-bit</strong></th>
<th><strong>Windows 7 64-bit</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>C:\Program Files\...</td>
<td><blockquote>
<p>C:\Program Files (x86)\...</p>
</blockquote></td>
</tr>
<tr class="even">
<td>C:\Windows\system32\...</td>
<td><blockquote>
<p>C:\Windows\SysWoW64</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Configuration and log file pathnames are changed as follows:

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Windows XP</th>
<th><blockquote>
<p>Windows 7</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>C:\Documents and Settings\All Users\Application Data\Vista\Imaging\mag.ini (TeleReader)</p>
<p>C:\Documents and Settings\All Users\Application Data\Vista\Imaging\mag308.ini (Clinical Display and Clinical Capture)</p></td>
<td><blockquote>
<p>C:\ProgramData\Vista\Imaging\mag.ini (TeleReader)</p>
<p>C:\ProgramData\Vista\Imaging\mag308.ini(Cli nical Display and Clinical Capture)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>C:\Documents and Settings\All Users\Application Data\Vista\Imaging</p>
<p>\MagTeleReaderConfig.ini</p></td>
<td><blockquote>
<p>C:\ProgramData\Vista\Imaging\ MagTeleReaderConfig.ini</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>C:\Documents and Settings\All Users\Application Data\Vista\Imaging\Log\MagTeleReaderConf ig10042012034524PM.log*</td>
<td><blockquote>
<p>C:\ProgramData\Vista\Imaging\ Log\MagTeleReaderConfig10042012034524P M.log*</p>
</blockquote></td>
</tr>
</tbody>
</table>

> \*The name of the log file is based on MagTeleReaderConfig + date time stamp.

#### Background Processor Files

| File Name          | Description                                                           |
|------------------------|---------------------------------------------------------------------------|
| GEAR32PO.OCX           | Used by mag_makeabs.exe to create derivative files.                       |
| igmed32s.dll           | Used by mag_makeabs.exe to create derivative files.                       |
| IGMed32x.ocx           | Used by mag_makeabs.exe to create derivative files.                       |
| MagImportXControl1.ocx | Import API Active X control file used by the Background Processor.        |
| mag_makeabs.exe        | Creates derivative files                                                  |
| Magbtm.exe             | Processes queues and configures imaging system files.                     |
| MagHTMLARchive.exe     | Creates HTML output log files                                             |
| MagVerifier.exe        | Performs database integrity checks.                                       |
| MagPurge.exe           | Removes old image files and recovers image files on VistA Imaging shares. |

#### Online Help Files

> Online help files are installed with the Clinical Workstation, Background Processor (BP), and VistARad software.

> All three of the BP applications are documented in MAG_BPUserman.htm and the contents of the MAG_BPUserman_files subdirectory. The MAG_BP_User_Manual.PDF can also be found in the application subdirectory and can be accessed from the Help menu of the BP Queue Processor main window.

> The clinical workstation help system is located in the C:\Program Files\VistA\Imaging\Help

> \Client\index.htm subdirectory. If the workstation is using the Windows 7 (64 bit) operating system, a separate help file for TeleReader is located in C:\Program Files(x86)\VistA\Imaging\Help\TeleReader. The file name is MAGTeleReaderConfig.pdf.

#### DICOM Gateway Files

> The following tables list files that are part of a DICOM Gateway installation. Files are grouped by folder.

> C:\Program Files\VistA\Imaging\DICOM – Primary program files

| File Name             | Description                                                                                                  |
|---------------------------|------------------------------------------------------------------------------------------------------------------|
| BATCH_SEND_IMAGE.BAT      | Batch file that takes a folder of DICOM objects and sends them to a storage provider.                            |
| CTN_VERSION.EXE           | Program that prints the current installed version of the Central Test Node software.                             |
| DCF_LicenseInstaller.bat  | Program that installs the DCF Toolkit license.                                                                   |
| DCM_DIFF.EXE              | Program that compares two DICOM files.                                                                           |
| DCM_DUMP_ELEMENT.EXE      | Program that dumps the content of a DICOM tag into a DICOM file.                                                 |
| DCM_DUMP_FILE.EXE         | Program that dumps the content of a DICOM file.                                                                  |
| DICOM_ECHO.EXE            | Program that can be used to test network connectivity with DICOM modalities.                                     |
| DRIVES.EXE                | Program that provides information on currently mounted disk drives.                                              |
| ERRLOOK.EXE               | Program that can be used to display the meaning of an MS-Windows error code.                                     |
| MAG_AbstrTGA.EXE          | Program that creates thumbnails of images.                                                                       |
| MAG_COMPRESSOR_AWARE.E XE | Program to compress image files before transmission.                                                             |
| MAG_CSTORE.EXE            | Program that runs on the DICOM Gateway to store images.                                                          |
| MAG_DCM_COPY.EXE          | Program that copies parts of DICOM files (used for modifying information in image headers).                      |
| MAG_DCMABSTRACT.EXE       | Program that creates abstracts (thumbnails of images) from DICOM objects.                                        |
| MAG_DCMTOTGA.EXE          | Program that converts DICOM images to Targa Images.                                                              |
| MAG_DCM_COPY.EXE          | Program that copies parts of DICOM files (used for modifying information in image headers).                      |
| MAG_MAKELINK.EXE          | Program to create icons.                                                                                         |
| MAG_RECON.EXE             | Program to reconstruct a DICOM File from an existing DICOM file and a script file containing header-information. |
| MAG_RECON.TXT             | Sample script file to be used with MAG_Recon.exe.                                                                |
| MAG_TELNET.CNT            | Table of contents for Help file.                                                                                 |
| MAG\_ TELNET.EXE          | Help file for Telnet client application.                                                                         |
| MAG\_ TELNET.HLP          | Telnet client application.                                                                                       |
| MAG_TGATODCM.EXE          | Program that converts Targa images to DICOM images.                                                              |
| MAG_VISTA_SEND_IMAGE.EX E | Program that transmits image files.                                                                              |
| MSVCR71.DLL               | Support library for executables compiled with Microsoft C Compiler.                                              |
| OD.EXE                    | Program that produces octal dumps of binary files.                                                               |
| PATHMAN.EXE               | Program that manipulates the default “path” lookup string.                                                       |
| SEND_IMAGE.EXE            | Program that transmits image files.                                                                              |
| SLEEP.EXE                 | Program that allows a batch file to “wait” for a couple of seconds.                                              |

| File Name   | Description                                      |
|-----------------|------------------------------------------------------|
| MAG_DCMVIEW.EXE | DICOM image viewer: Program to display DICOM images. |
| VIEWER1.ICO     | Icon for MAG_DCMView.exe program.                    |

> C:\Program Files\VistA\Imaging\DCMView – DICOM Viewer program files

> C:\Program Files\VistA\Imaging\CVixInstaller – CVIX installer files

> This folder and its subfolders contain the files for the CVIX installer. They should not be modified or deleted.

> C:\Program Files\VistA\Imaging\HDIGInstaller – HDIG installer files

> This folder and its subfolders contain the files for the HDIG installer. They should not be modified or deleted.

> C:\Program Files\VistA\Imaging\VIXInstaller – VIX installer files

> This folder and its subfolders contain the files for the VIX installer. They should not be modified or deleted.

> C:\Program Files\VistA\Imaging\MAG_MakeAbs – Abstract generator files

| File Name        | Description                                                                |
|----------------------|--------------------------------------------------------------------------------|
| MAG_DCMABSTRACT.I CO | Icon for MAG_DCMabstract.exe.                                                  |
| README.TXT           | File, which provides status information about the Abstract Maker installation, |

> C:\DICOM – Icon files

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name</strong></th>
<th><strong>Sample</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MAGCSTORE.ICO</td>
<td><blockquote>
<p>![](vista-imaging-system-technical-manual/018.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>MAGVISTA.ICO</td>
<td><blockquote>
<p>![](vista-imaging-system-technical-manual/019.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> C:\DICOM\Abstract – Files used for generic abstracts for certain image types

| File Name      | Description                                                                             |
|--------------------|---------------------------------------------------------------------------------------------|
| CANNED_IMAGE.JPG   | Canned abstract for JPEG files.                                                             |
| MAG_CANNED_ECG.BMP | Canned abstract for ECG files.                                                              |
| MAG_CANNED_PDF.BMP | Canned abstract for PDF files.                                                              |
| MAG_WHATEVER.BMP   | Canned abstract for other types of files that cannot have abstracts generated “on the fly”. |

> C:\DICOM\Cache – Caché database folder

| File Name      | Description                                                                                            |
|--------------------|------------------------------------------------------------------------------------------------------------|
| CACHE.DAT          | Program that has the Caché database for DICOM Gateways.                                                    |
| CSTORE.OUT         | Startup log file produced by backend M server for the MAG_CSTORE.EXE front end storage provider processes. |
| WORKLIST_60010.OUT | Startup log file produced by backend M server for the Modality Worklist provider processes.                |

> C:\DICOM\Data1 – Text data folder; additional Data2, Data3, folders may exist

> *May be stored in other local drives on older systems*

| File Name  | Description                                                                                  |
|----------------|--------------------------------------------------------------------------------------------------|
| INIT_DICOM.BAT | Program that re-initializes the subdirectories of the directory in which the BAT file is stored. |
| SEARCH.BAT     | Program that scans .TXT files for the occurrence of a specified string.                          |

> \<drive\>:\DICOM\Dict – Dictionary files, typically stored in a network folder

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AE_TITLE.DIC</td>
<td>Dictionary file that maps DICOM Application Entity Titles to well-known aliases and provides descriptions.</td>
</tr>
<tr class="even">
<td>AE_TITLE.SAMPLE</td>
<td>Distributed initial version of AE_TITLE.DIC file.</td>
</tr>
<tr class="odd">
<td>CT_PARAM.DIC</td>
<td>Table containing prior settings for conversion parameters. Imported by ^MAGDMFB7.</td>
</tr>
<tr class="even">
<td>DATA_CR.DIC</td>
<td>Additional data fields to be displayed on DICOM Gateway. Imported by ^MAGDIR4.</td>
</tr>
<tr class="odd">
<td>DATA_MRI.DIC</td>
<td>Additional data fields to be displayed on DICOM Gateway. Imported by ^MAGDIR4.</td>
</tr>
<tr class="even">
<td>DATAGECT.DIC</td>
<td>Additional data fields to be displayed on DICOM Gateway (General Electric). Imported by ^MAGDIR4.</td>
</tr>
<tr class="odd">
<td>DATAMISC.DIC</td>
<td>Additional data fields to be displayed on DICOM Gateway. Imported by ^MAGDIR4.</td>
</tr>
<tr class="even">
<td>ELEMENT.DIC</td>
<td>DICOM Element dictionary. Imported by ^MAGDMFB2.</td>
</tr>
<tr class="odd">
<td>HL7.DIC</td>
<td>VistA HL7 dictionary. Imported by ^MAGDMFB7.</td>
</tr>
<tr class="even">
<td>INSTRUMENT.DIC</td>
<td>List of image producing instruments, distributed as Instrument.Sample. Imported by ^MAGDMFB8</td>
</tr>
<tr class="odd">
<td>INSTRUMENT.SAMPLE</td>
<td>Distributed initial version of INSTRUMENT.DIC.</td>
</tr>
<tr class="even">
<td>MODALITY.DIC</td>
<td><p>Image processing rules for modalities. Imported by</p>
<p>^MAGDMFB8.</p></td>
</tr>
<tr class="odd">
<td>MODALITY.SAMPLE</td>
<td>Distributed initial version of MODALITY.DIC.</td>
</tr>
<tr class="even">
<td>PORTLIST.DIC</td>
<td>Locally edited list of network ports for DICOM services. Imported by ^MAGDMFB9.</td>
</tr>
<tr class="odd">
<td>PORTLIST.SAMPLE</td>
<td>Distributed initial version of PORTLIST.DIC.</td>
</tr>
<tr class="even">
<td>ROUTE.DIC</td>
<td>Locally edited list of image processing rules for automatic routing. Imported by ^MAGBTRB1.</td>
</tr>
<tr class="odd">
<td>ROUTE.SAMPLE</td>
<td>Distributed initial version of ROUTE.DIC.</td>
</tr>
<tr class="even">
<td>SCP_LIST.DIC</td>
<td><p>Provider application parameters. Imported by</p>
<p>^MAGDMFB9.</p></td>
</tr>
<tr class="odd">
<td>SCU_LIST.DIC</td>
<td>List of Service Class User Applications, distributed as SCU_List.Sample. Imported by ^MAGDMFB9.</td>
</tr>
<tr class="even">
<td>TEMPLATE.DIC</td>
<td><p>Macros for event message templates. Imported by</p>
<p>^MAGDMFB3.</p></td>
</tr>
<tr class="odd">
<td>TEMPLATE.TMP</td>
<td>Temporary file created when loading the TEMPLATE.dic dictionary.</td>
</tr>
<tr class="even">
<td>UID.DIC</td>
<td>UID dictionary. Imported by ^MAGDMFB4.</td>
</tr>
<tr class="odd">
<td>WORKLIST.DIC</td>
<td>Locally edited list of the modality Called Application Entity Titles and the corresponding DICOM Modality Worklist database attributes. Imported by ^MAGDMFB8.</td>
</tr>
<tr class="even">
<td>WORKLIST.SAMPLE</td>
<td>Distributed initial version of WORKLIST.DIC.</td>
</tr>
</tbody>
</table>

| File Name       | Description                                  |
|---------------------|--------------------------------------------------|
| MAGDICOM.SETUP.CSP  | Temporary file used in the installation process. |
| MAGDICOM.STATUS.CSP | Temporary file used in the installation process. |
| MAGLOGO1.GIF        | Temporary file used in the installation process. |
| MAGLOGO2.GIF        | Temporary file used in the installation process. |
| MAGMASTERFILE.CSP   | Temporary file used in the installation process. |
| VABKG.JPG           | Temporary file used in the installation process. |

> C:\DICOM\Web – Contains temporary files that are used in the installation process.

#### Sample Files

> For the purpose of testing that the software is properly installed, a number of sample files are included in the distribution kit.

#### Sample DICOM Images

> The sample images that are available for the DICOM gateway can be used to perform trial image transmissions.

| File     | Description                                                                                           |
|--------------|-----------------------------------------------------------------------------------------------------------|
| BabyFace.dcm | Ultrasound image (640x480 pixels)                                                                         |
| BoneScrw.dcm | CR image (2048x2577 pixels)                                                                               |
| Carotid.dcm  | Ultrasound image (640x480 pixels)                                                                         |
| EyeCLens.dcm | (640x560 pixels)                                                                                          |
| EyeClot.dcm  | (640x560 pixels)                                                                                          |
| EyeLens.dcm  | (640x560 pixels)                                                                                          |
| EyeSttch.dcm | (640x560 pixels)                                                                                          |
| Fillings.dcm | IO image (811x644 pixels)                                                                                 |
| GoldGate.dcm | Picture of the Golden Gate Bridge in San Francisco, labeled as modality type OT (other) (640x480 pixels). |
| Implant.dcm  | IO image (811x644 pixels)                                                                                 |
| PaceMkr.dcm  | CR image (1716x1910 pixels)                                                                               |
| Retina.dcm   | (640x480 pixels)                                                                                          |
| Roots.dcm    | IO image (811x644 pixels)                                                                                 |
| Skull.dcm    | CR mage (2048x2577 pixels)                                                                                |
| Spine.dcm    | CR image (2048x2495 pixels)                                                                               |
| test.txt_new | Sample command file, used for modifying information in image headers.                                     |

#### Sample HL7 Data Streams

> The following sample HL7 streams are available.

| File      | Description |
|---------------|-----------------|
| Baltimore.gbl | Small data set  |
| Boston.gbl    | Large data set  |

#### VistARad Workstation Files

> Files that are installed on a VistARad workstation are listed below. Files are grouped by folder.

> Note—the folder locations are different for Windows 7 and Windows XP. Each of the respective folder locations are noted for each of the files listed below.

> Windows 7 – C:\Users\Public\Desktop

> Windows XP – C:\Documents and Settings\All Users\Desktop

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MAG_VistARad_Patch133</td>
<td><blockquote>
<p>desktop shortcut</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Windows 7 – C:\ProgramData\Microsoft\Windows\Start Menu\Programs\VistA Imaging Programs

> Windows XP – C:\Documents and Settings\All Users\Start Menu\Programs\VistA Imaging Programs

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MAG_VistARad_Patch133</td>
<td><blockquote>
<p>start menu shortcut</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Windows 7 – C:\Program Files (x86)\Vista\Imaging\MAG_VistARad

> Windows XP – C:\Program Files\Vista\Imaging\MAG_VistARad

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Bapi32_65_5.dll</td>
<td><blockquote>
<p>DLL for Broker ActiveX control; As part of the VistA Imaging SSOi effort, we will be upgrading this library and BDK, (expected version XWB*1.1*65 currently in development and beta testing), which has built-in integration to the IAM SSOi Secure Token Server (STS) authentication model including PIV/PIN prompt(s).</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CCMBroker.dll</td>
<td><blockquote>
<p>core DLL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DimFileX.ocx</td>
<td><blockquote>
<p>DLL for Dome ActiveX control</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Dimpl8.dll</td>
<td><blockquote>
<p>DLL for Dome ActiveX control</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DimplX.ocx</td>
<td><blockquote>
<p>DLL for Dome ActiveX control</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DXShared.dll</td>
<td><blockquote>
<p>DLL for Dome ActiveX control</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FreeImage.dll</td>
<td><blockquote>
<p>DLL for image processing</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Launcher.exe</td>
<td><blockquote>
<p>utility executable to support monitored site auto-login function</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>LayoutSelect.dll</td>
<td><blockquote>
<p>VistARad core functionality DLL (core DLL)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>MAG_Vistarad.exe</td>
<td><blockquote>
<p>VistARad main executable file</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MAG_Vistarad_Util.exe</td>
<td><blockquote>
<p>VistARad teaching file support executable</p>
</blockquote></td>
</tr>
<tr class="even">
<td>RPCBrokerCom.dll</td>
<td><blockquote>
<p>DLL for Broker ActiveX control</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>RpcDbAccessCom.dll</td>
<td><blockquote>
<p>core DLL</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SliceCalc.dll</td>
<td><blockquote>
<p>core DLL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>TargaFile.dll</td>
<td><blockquote>
<p>core DLL</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VA_CaseManager.dll</td>
<td><blockquote>
<p>core DLL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VA_DelphiUtils.dll</td>
<td><blockquote>
<p>DLL for password decryption to gain access to image share</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VA_DICOM.dll</td>
<td><blockquote>
<p>DLL for accessing DICOM files</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VA_DxShared.dll</td>
<td><blockquote>
<p>core DLL</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VA_GridCtrl.dll</td>
<td><blockquote>
<p>core DLL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VA_HPModule.dll</td>
<td><blockquote>
<p>core DLL</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VA_ImgLdrCtrl.dll</td>
<td><blockquote>
<p>core DLL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VA_Manager.dll</td>
<td><blockquote>
<p>core DLL</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VA_Shared.dll</td>
<td><blockquote>
<p>core DLL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VA_StackViewCtrl.dll</td>
<td><blockquote>
<p>core DLL</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VA_TeachingFiles.dll</td>
<td><blockquote>
<p>core DLL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VA_Vistarad.dll</td>
<td><blockquote>
<p>core DLL</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VergenceContextor.dll</td>
<td><blockquote>
<p>DLL to support context management</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VIXBroker.dll</td>
<td><blockquote>
<p>DLL for VistA Imaging Exchange broker</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Windows 7 – C:\Program Files (x86)\Vista\Imaging\MAG_VistARad\Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Windows XP – C:\Program Files\Vista\Imaging\MAG_VistARad\Help

| File                    | Description                     |
|-----------------------------|-------------------------------------|
| MAG_VistARad_User_Guide.pdf | VistARad help--user guide           |
| MAG_vrad_QSG.pdf            | VistARad help--quick start guide    |
| MAG_Vrad_Quick_Ref.pdf      | VistARad help--quick reference card |
| MAG_vrad_Shortcuts.pdf      | VistARad help--keyboard shortcuts   |

> Windows 7 – C:\ProgramData\VistA\Imaging\MAG_VistARad\Log

> Windows XP – C:\Documents and Settings\All Users\Application Data\VistA\Imaging\MAG_VistARad\Log

| File                                | Description    |
|-----------------------------------------|--------------------|
| MAG_VistARad_mmddyyyy_hhmmss_Lognnn.txt | VistARad log files |

> Windows 7 – C:\ProgramData\VistA\Imaging\MAG_VistARad\Config

> Windows XP – C:\Documents and Settings\All Users\Application Data\VistA\Imaging\MAG_VistARad\Config

| File                   | Description                            |
|----------------------------|--------------------------------------------|
| HPConfig.xml               | used for internal reference                |
| MAG_Dicom_Attributes.lst   | used for internal reference                |
| Mag_DicomTags.txt          | used for internal reference                |
| MAG_Special_Attributes.lst | used for internal reference                |
| Mag_statusdatasettings.txt | used for internal reference                |
| MAGJ.ini                   | VistARad settings                          |
| modality.txt               | used for internal reference                |
| radlextree.xml             | internally used for Teaching Files feature |
| template.dcm               | internally used to create DICOM files      |

> Redistributable packages for necessary runtimes (typically installed in C:\WINDOWS\system32

> and/or C:\WINDOWS\WinSxS)

| Microsoft OLE 2.40 for Windows NT(TM) and Windows 95(TM) Operating Systems |
|----------------------------------------------------------------------------|
| Visual C++ 8.0 ATL (x86) WinSXS MSM                                        |
| Visual C++ 8.0 CRT (x86) WinSXS MSM                                        |
| Visual C++ 8.0 MFC.Policy (x86) WinSXS MSM                                 |
| Visual C++ 8.0 MFC (x86) WinSXS MSM                                        |
| Microsoft GDI+                                                             |
| Microsoft Visual C++ 2005 SP1 Redistributable Package MFC Update (x86)     |
| Windows Installer 3.1 (x86)                                                |

#### MAG_Decompressor Files

> The following files are installed only on systems that are recipients of routed files that use compression. For more information, refer to the *Routing User Guide*.

> Mag_Decompressor files are installed in: C:\Program Files\VistA\Imaging\MAG_Decompressor

> awj2k.dll (not distributed by VistA Imaging; purchased from Aware Inc.) MAG_Decompressor.exe (distributed by Imaging)

#### Storage Site Utilities

> The following are maintenance utilities:

- MagUtility used for various maintenance tasks related to Tier 1, database, and Tier 2
- MagDexter used to provide jukebox platter reports for use with the new MagKat utility
- MagKat, a database maintenance tool used to backfill specific fields in the IMAGE file (#2005).

> For details, see the *Storage Utilities User Manual*.

#### VIX Files

> For a list of the files installed for the VIX (VistA Imaging Exchange) service, see the VIX Reference chapter in the *VIX Administrator’s Guide*.

#### DICOM Importer II Client Files

> The following files are installed on workstations on which the DICOM Importer II client is installed:

- ..\logs\log.txt
- Dicom.dll
- DicomImporter.Common.dll
- DicomImporter.DataSources.dll
- DICOMImporter.unity.config
- DicomImporter.ViewModels.dll
- DicomImporter.Views.dll
- ImagingClient.Infrastructure.dll
- ImagingShell.exe
- ImagingShell.exe.config
- log4net.dll
- log4net.xml
- MAG_DICOM_Importer_II_User_Manual.pdf
- Microsoft.Net.Http.dll
- Microsoft.Practices.Prism.dll
- Microsoft.Practices.Prism.Interactivity.dll
- Microsoft.Practices.Prism.Interactivity.xml
- Microsoft.Practices.Prism.MefExtensions.dll
- Microsoft.Practices.Prism.MefExtensions.xml
- Microsoft.Practices.Prism.UnityExtensions.dll
- Microsoft.Practices.Prism.UnityExtensions.xml
- Microsoft.Practices.Prism.xml
- Microsoft.Practices.ServiceLocation.dll
- Microsoft.Practices.ServiceLocation.xml
- Microsoft.Practices.Unity.Configuration.dll
- Microsoft.Practices.Unity.Configuration.xml
- Microsoft.Practices.Unity.dll
- Microsoft.Practices.Unity.xml
- NLog.dll
- System.Windows.Interactivity.dll
- System.Windows.Interactivity.xml
- VistaCommon.dll
- VistaCommon.XmlSerializers.dll

## Chapter 7 VistA Imaging System M Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *The Food and Drug Administration classifies this software as a medical device. As such, it may not be changed in any way. Modifications to this software may result in an adulterated medical device under 21CFR820, the use of which is considered to be a violation of US Federal Statutes.*

> *VA Policy states the following:*

> *Those components of a national package (routines, data dictionaries, options, protocols, GUI components, etc.) that implement a controlled procedure, contain a controlled or strictly defined interface or report data to a database external to the local facility, must not be altered except by the Office of Information (OI) Technical Services (TS) staff. A controlled procedure is one that implements requirements that are mandated or governed by law or VA (Department of Veterans Affairs) directive or is subject to governing financial management standards of the Federal Government and VA or that is regulated by oversight groups such as the JCAHO or FDA. A controlled or strictly defined interface is one that adheres to a specific industry standard, will adversely affect a package and/or render the package inoperable if modified or deleted. For national software that is subject to FDA oversight, only the holder of the premarketing clearance (510(k)) is allowed to modify code for the medical device. The holder of a premarketing clearance is restricted to specifically designated TS staff that are located at the registered manufacturing site and operating in the designated production environment.*

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA Imaging System is based on the use of VA FileMan as an object-oriented database management system to store single or sequential images, and other multimedia object types.

> This chapter first itemizes the various files that are used by the Imaging System (Clinical Capture/Display, Background Processor, and VistARad) and then describes how to obtain more detailed information about the files. Some of the files are used on the DICOM Image and Text Gateways and will reside on those systems and not on the VistA hospital system.

### VA FileMan Files that are Part of the VistA Imaging System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### VA FileMan Files

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 37%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File</strong></th>
<th><strong>Name</strong></th>
<th><strong>Stored in</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2005</td>
<td>IMAGE</td>
<td>^MAG(2005,D0,...</td>
</tr>
<tr class="even">
<td>2005.01</td>
<td>--&gt;EXPORT LOCATION</td>
<td>--&gt;5,D1,...</td>
</tr>
<tr class="odd">
<td>2005.0106</td>
<td>--&gt;ROUTING TIMESTAMP</td>
<td>--&gt;4,D1,...</td>
</tr>
<tr class="even">
<td>2005.011</td>
<td>--&gt;LONG DESCRIPTION</td>
<td>--&gt;3,D1,...</td>
</tr>
<tr class="odd">
<td>2005.0111</td>
<td>--&gt;ROUTING LOG</td>
<td>--&gt;6,D1,...</td>
</tr>
<tr class="even">
<td>2005.04</td>
<td>--&gt;OBJECT GROUP</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="odd">
<td>2005.210</td>
<td>--&gt; PRESENTATION STATE</td>
<td>--&gt;210,D1,...</td>
</tr>
<tr class="even">
<td>2005.001</td>
<td>IMAGING STUDY</td>
<td>^MAG(2005.001,D0,...</td>
</tr>
<tr class="odd">
<td>2005.002</td>
<td>IMAGING ANNOTATION FILE</td>
<td>^MAG(2005.002,D0,...</td>
</tr>
<tr class="even">
<td>2005.02</td>
<td>OBJECT TYPE</td>
<td>^MAG(2005.02,D0,...</td>
</tr>
<tr class="odd">
<td>2005.21</td>
<td>--&gt;ACTIONS</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="even">
<td>2005.24</td>
<td>--&gt;CHILD CLASS</td>
<td>--&gt;3,D1,...</td>
</tr>
<tr class="odd">
<td>2005.021</td>
<td>IMAGE FILE TYPES</td>
<td>^MAG(2005.021,D0,...</td>
</tr>
<tr class="even">
<td>2005.03</td>
<td>PARENT DATA FILE</td>
<td>^MAG(2005.03,D0,...</td>
</tr>
<tr class="odd">
<td>2005.1</td>
<td>IMAGE AUDIT</td>
<td>^MAG(2005.1,D0,...</td>
</tr>
<tr class="even">
<td>2005.11</td>
<td>--&gt;EXPORT LOCATION</td>
<td>--&gt;5,D1,...</td>
</tr>
<tr class="odd">
<td>2005.1106</td>
<td>--&gt;ROUTING TIMESTAMP</td>
<td>--&gt;4,D1,...</td>
</tr>
<tr class="even">
<td>2005.111</td>
<td>--&gt;LONG DESCRIPTION</td>
<td>--&gt;3,D1,...</td>
</tr>
<tr class="odd">
<td>2005.1111</td>
<td>--&gt; ROUTING LOG</td>
<td>--&gt;6,D1,...</td>
</tr>
<tr class="even">
<td>2005.14</td>
<td>--&gt;OBJECT GROUP</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="odd">
<td>2005.2</td>
<td>NETWORK LOCATION</td>
<td>^MAG(2005.2,D0,...</td>
</tr>
<tr class="even">
<td>2005.201</td>
<td>--&gt;EMAIL</td>
<td>--&gt;5,D1,...</td>
</tr>
<tr class="odd">
<td>2005.4</td>
<td>IMAGE HISTOLOGICAL STAIN</td>
<td>^MAG(2005.4,D0,...</td>
</tr>
<tr class="even">
<td>2005.41</td>
<td>MICROSCOPIC OBJECTIVE</td>
<td>^MAG(2005.41,D0,...</td>
</tr>
<tr class="odd">
<td>2005.6</td>
<td>IMAGING PATIENT REFERENCE</td>
<td>^MAGV(2005.6,D0,...</td>
</tr>
<tr class="even">
<td>2005.61</td>
<td>IMAGING PROCEDURE REFERENCE</td>
<td>^MAGV(2005.61,D0,...</td>
</tr>
<tr class="odd">
<td>2005.62</td>
<td>IMAGE STUDY</td>
<td>^MAGV(2005.62,D0,...</td>
</tr>
<tr class="even">
<td>2005.63</td>
<td>IMAGE SERIES</td>
<td>^MAGV(2005.63,D0,...</td>
</tr>
<tr class="odd">
<td>2005.64</td>
<td>IMAGE SOP INSTANCE</td>
<td>^MAGV(2005.64,D0,...</td>
</tr>
<tr class="even">
<td>2005.65</td>
<td>IMAGE INSTANCE FILE</td>
<td>^MAGV(2005.65,D0,...</td>
</tr>
<tr class="odd">
<td>2005.66</td>
<td>IMAGING DUPLICATE UID LOG</td>
<td>^MAGV(2005.66,DO,...</td>
</tr>
<tr class="even">
<td>2005.71</td>
<td>IMAGING DICOM FIELDS</td>
<td>^MAG(2005.71,D0,...</td>
</tr>
<tr class="odd">
<td>2005.712</td>
<td>MODULE</td>
<td>--&gt;”M”,D1,</td>
</tr>
<tr class="even">
<td>2005.713</td>
<td>ELEMENT TAG</td>
<td>--&gt; “E”,D2,</td>
</tr>
<tr class="odd">
<td>2005.8</td>
<td>IMAGING SERVICE INSTITUTION</td>
<td>^MAGV(2005.8,DO,...</td>
</tr>
<tr class="even">
<td>2005.81</td>
<td>MAG DESCRIPTIVE CATEGORIES</td>
<td>^MAG(2005.81,D0,...</td>
</tr>
<tr class="odd">
<td>2005.82</td>
<td>IMAGE INDEX FOR CLASS</td>
<td>^MAG(2005.82,D0,...</td>
</tr>
<tr class="even">
<td>2005.83</td>
<td>IMAGE INDEX FOR TYPES</td>
<td>^MAG(2005.83,D0,...</td>
</tr>
<tr class="odd">
<td>2005.84</td>
<td>IMAGE INDEX FOR SPECIALTY/SUBSPECIALTY</td>
<td>^MAG(2005.84,D0,...</td>
</tr>
<tr class="even">
<td>2005.85</td>
<td>IMAGE INDEX FOR PROCEDURE/EVENT</td>
<td>^MAG(2005.85,D0,...</td>
</tr>
<tr class="odd">
<td>2005.852</td>
<td>--&gt; SPECIALTY</td>
<td>--&gt; 1,D1,...</td>
</tr>
<tr class="even">
<td>2005.86</td>
<td>IMAGE ACTIONS</td>
<td>^MAG(2005.86.D0,...</td>
</tr>
<tr class="odd">
<td>2005.865</td>
<td>--&gt;TYPE</td>
<td>--&gt;2,D1,...</td>
</tr>
<tr class="even">
<td>2005.87</td>
<td>IMAGE LIST FILTERS</td>
<td>^MAG(2005.87,D0,...</td>
</tr>
<tr class="odd">
<td>2006.911</td>
<td>DICOM GATEWAY INSTRUMENT DICTIONARY</td>
<td>^MAGDICOM(2006.911,D0...</td>
</tr>
<tr class="even">
<td>2006.912</td>
<td>DICOM GATEWAY MODALITY DICTIONARY</td>
<td>^MAGDICOM(2006.912,D0...</td>
</tr>
<tr class="odd">
<td>2006.913</td>
<td>ARTIFACT KEYLIST</td>
<td>^MAGV(2006.913,D0...</td>
</tr>
<tr class="even">
<td>2006.914</td>
<td>RETENTION POLICY</td>
<td>^MAGV(2006.914,D0...</td>
</tr>
<tr class="odd">
<td>2006.915</td>
<td>ARTIFACT DESCRIPTOR</td>
<td>^MAGV(2006.915,D0...</td>
</tr>
<tr class="even">
<td>2006.916</td>
<td>ARTIFACT</td>
<td>^MAGV(2006.916,D0...</td>
</tr>
<tr class="odd">
<td>2006.917</td>
<td>STORAGE PROVIDER</td>
<td>^MAGV(2006.917,D0...</td>
</tr>
<tr class="even">
<td>2006.918</td>
<td>ARTIFACT INSTANCE</td>
<td>^MAGV(2006.918,D0...</td>
</tr>
<tr class="odd">
<td>2006.9191</td>
<td>MAGV GATEWAY CONFIGURATION</td>
<td>^MAGV(2006.9191,D0...</td>
</tr>
<tr class="even">
<td>2006.9192</td>
<td>DICOM AE SECURITY MATRIX</td>
<td>^MAGV(2006.9192,D0,...</td>
</tr>
<tr class="odd">
<td>2006.9193</td>
<td>IMAGING APPLICATION SERVICE</td>
<td>^MAGV(2006.9193,D0,...</td>
</tr>
<tr class="even">
<td>2006.921</td>
<td>ARTIFACT RETENTION POLICY</td>
<td>^MAGV(2006.921,D0,...</td>
</tr>
<tr class="odd">
<td>2006.922</td>
<td>RETENTION POLICY FULFILLMENT</td>
<td>^MAGV(2006.922,D0,...</td>
</tr>
<tr class="even">
<td>2006.923</td>
<td>RETENTION POLICY STORAGE PROVIDER MAP</td>
<td>^MAGV(2006.923,D0,...</td>
</tr>
<tr class="odd">
<td>2006.924</td>
<td>STORAGE PROVIDER AVAILABILITY</td>
<td>^MAGV(2006.924,D0,...</td>
</tr>
<tr class="even">
<td>2006.925</td>
<td>TRANSFER STATISTICS</td>
<td>^MAGV(2006.925,D0,...</td>
</tr>
<tr class="odd">
<td>2006.926</td>
<td>STORAGE TRANSACTION</td>
<td>^MAGV(2006.926,D0,...</td>
</tr>
<tr class="even">
<td>2006.927</td>
<td>QUEUE</td>
<td>^MAGV(2006.927,D0,...</td>
</tr>
<tr class="odd">
<td>2006.928</td>
<td>QUEUE MESSAGE</td>
<td>^MAGV(2006.928,D0,...</td>
</tr>
<tr class="even">
<td>2006.93</td>
<td>IMAGING EVENT AUDIT LOG</td>
<td>^MAGV(2006.93,D0,...</td>
</tr>
<tr class="odd">
<td>2006.931</td>
<td>IMAGING EVENT AUDITABLE ACTION</td>
<td>^MAGV(2006.931,D0,...</td>
</tr>
<tr class="even">
<td>2006.941</td>
<td>MAG WORK ITEM</td>
<td>^MAGV(2006.941,D0,...</td>
</tr>
<tr class="odd">
<td>2006.9412</td>
<td>WORKLIST</td>
<td>^MAGV(2006.9412,D0,...</td>
</tr>
<tr class="even">
<td>2006.9413</td>
<td>MAG WORK ITEM STATUS</td>
<td>^MAGV(2006.9413,D0,...</td>
</tr>
<tr class="odd">
<td>2006.9414</td>
<td>MAG WORK ITEM SUBTYPE</td>
<td>^MAGV(2006.9414,D0,...</td>
</tr>
<tr class="even">
<td>2006.9421</td>
<td>MAGV IMPORT STUDY LOG</td>
<td>^MAGV(2006.9421,D0,...</td>
</tr>
<tr class="odd">
<td>2006.9422</td>
<td>MAGV IMPORT MEDIA LOG</td>
<td>^MAGV(2006.9422,D0,...</td>
</tr>
<tr class="even">
<td>2005.88</td>
<td>MAG REASON FILE</td>
<td>^MAG(2005.88</td>
</tr>
<tr class="odd">
<td>2005.99</td>
<td>IMAGE INDEX FOR BODY PART</td>
<td>^MAG(2005.99,D0,…</td>
</tr>
<tr class="even">
<td>2006.03</td>
<td>IMAGE BACKGROUND QUEUE</td>
<td>^MAGQUEUE(2006.03,D0,...</td>
</tr>
<tr class="odd">
<td>2006.031</td>
<td>IMAGE BACKGROUND QUEUE POINTER</td>
<td>^MAGQUEUE(2006.031,D0,...</td>
</tr>
<tr class="even">
<td>2006.033</td>
<td>OFFLINE IMAGES</td>
<td>^MAGQUEUE(2006.033,D0,...</td>
</tr>
<tr class="odd">
<td>2006.034</td>
<td>IMPORT QUEUE</td>
<td>^MAG(2006.034,D0,...</td>
</tr>
<tr class="even">
<td>2006.0341</td>
<td>--&gt;IMAGE DATA</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="odd">
<td>2006.035</td>
<td>SEND QUEUE</td>
<td>^MAGQUEUE(2006.035,D0,...</td>
</tr>
<tr class="even">
<td>2006.036</td>
<td>ROUTING STATISTICS</td>
<td>^MAGQUEUE(2006.036,D0,...</td>
</tr>
<tr class="odd">
<td>2006.03601</td>
<td>--&gt;DETAILS</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="even">
<td>2006.04</td>
<td>ACQUISITION DEVICE</td>
<td>^MAG(2006.04,D0,...</td>
</tr>
<tr class="odd">
<td>2006.041</td>
<td>ACQUISITION SESSION</td>
<td>^MAG(2007.041,D0,...</td>
</tr>
<tr class="even">
<td>2006.1</td>
<td>IMAGING SITE PARAMETERS</td>
<td>^MAG(2006.1,D0,...</td>
</tr>
<tr class="odd">
<td>2006.11</td>
<td>--&gt;MULTI NAMESPACE</td>
<td>--&gt;4,D1,...</td>
</tr>
<tr class="even">
<td>2006.112</td>
<td>--&gt;FILE TYPES</td>
<td>--&gt;2,D1,...</td>
</tr>
<tr class="odd">
<td>2006.12</td>
<td>--&gt; ASSOCIATED INSTITUTIONS</td>
<td>--&gt; INSTS,D1,...</td>
</tr>
<tr class="even">
<td>2006.15</td>
<td>DICOM UID ROOT</td>
<td>^MAG(2006.15,D0,…</td>
</tr>
<tr class="odd">
<td>2006.166</td>
<td>--&gt; BP MAIL MESSAGE</td>
<td>--&gt;6,D1,...</td>
</tr>
<tr class="even">
<td>2006.1662</td>
<td>--&gt;--&gt; Mail Group</td>
<td>--&gt;1,D2,...</td>
</tr>
<tr class="odd">
<td>2006.1664</td>
<td>--&gt;--&gt; MESSAGE RECIPIENTS</td>
<td>--&gt;3,D2,...</td>
</tr>
<tr class="even">
<td>2006.1665</td>
<td>--&gt;--&gt; SECURITY KEYS</td>
<td>--&gt;4,D2,...</td>
</tr>
<tr class="odd">
<td>2006.17</td>
<td>MUSE VERSIONS</td>
<td>^MAG(2006.17,D0,...</td>
</tr>
<tr class="even">
<td>2006.171</td>
<td>MUSE TEST TYPES</td>
<td>^MAG(2006.171,D0,…</td>
</tr>
<tr class="odd">
<td>2006.172</td>
<td>MUSE FORMAT TABLE</td>
<td>^MAG(2006.172,D0,…</td>
</tr>
<tr class="even">
<td>2006.18</td>
<td>IMAGING USER PREFERENCE</td>
<td>^MAG(2006.18,D0,...</td>
</tr>
<tr class="odd">
<td>2006.1867</td>
<td>--&gt;PATIENT LIST</td>
<td>--&gt;”PATLIST”,D1,...</td>
</tr>
<tr class="even">
<td>2006.19</td>
<td>IMAGING USERS</td>
<td>^MAG(2006.19,D0,...</td>
</tr>
<tr class="odd">
<td>2006.191</td>
<td>--&gt;ADDITIONAL NAMESPACE</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="even">
<td>2006.5</td>
<td>PACS MESSAGE</td>
<td>^MAGDHL7(2006.5,D0,...</td>
</tr>
<tr class="odd">
<td>2006.502</td>
<td>--&gt;MESSAGE SEGMENTS</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="even">
<td>2006.51</td>
<td>DICOM DATA ELEMENT DICTIONARY</td>
<td>^MAGDICOM(2006.51,D0,...</td>
</tr>
<tr class="odd">
<td>2006.514</td>
<td>--&gt;ENUMERATED VALUE</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="even">
<td>2006.511</td>
<td>DIAGNOSTIC INFO FIELD</td>
<td>^MAGDICOM(2006.511,D0,...</td>
</tr>
<tr class="odd">
<td>2006.5112</td>
<td>--&gt;TAG</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="even">
<td>2006.52</td>
<td>DICOM MESSAGE TEMPLATE DICTIONARY</td>
<td>^MAGDICOM(2006.52,D0,...</td>
</tr>
<tr class="odd">
<td>2006.5204</td>
<td>--&gt;MESSAGE</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="even">
<td>2006.53</td>
<td>DICOM UID DICTIONARY</td>
<td>^MAGDICOM(2006.53,D0,...</td>
</tr>
<tr class="odd">
<td>2006.5305</td>
<td>--&gt;UID</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="even">
<td>2006.531</td>
<td>EXTENDED SOP NEGOTIATION</td>
<td>^MAGDICOM(2006.531,D0,..</td>
</tr>
<tr class="odd">
<td>2006.532</td>
<td>DICOM SOP CLASS</td>
<td>^MAG(2006.532,D0,...</td>
</tr>
<tr class="even">
<td>2006.539</td>
<td>DICOM UID SPECIFIC ACTION</td>
<td>^MAGDICOM(2006.539,D0,...</td>
</tr>
<tr class="odd">
<td>2006.5391</td>
<td>--&gt;PURPOSE</td>
<td>--&gt;1,...</td>
</tr>
<tr class="even">
<td>2006.54</td>
<td>PDU TYPE</td>
<td>^MAGDICOM(2006.54,D0,...</td>
</tr>
<tr class="odd">
<td>2006.55</td>
<td>DICOM WORKLIST PATIENT</td>
<td>^MAGDWLST(2006.55,D0,...</td>
</tr>
<tr class="even">
<td>2006.552</td>
<td>--&gt;PATIENT</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="odd">
<td>2006.5522</td>
<td>--&gt;--&gt;MEDICAL ALERT</td>
<td>--&gt;--&gt;1,D2,...</td>
</tr>
<tr class="even">
<td>2006.56</td>
<td>DICOM WORKLIST STUDY</td>
<td>^MAGDWLST(2006.56,D0,...</td>
</tr>
<tr class="odd">
<td>2006.562</td>
<td>--&gt;STUDY</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="even">
<td>2006.5621</td>
<td>--&gt;--&gt;PATIENT HISTORY</td>
<td>--&gt;--&gt;2,D2,...</td>
</tr>
<tr class="odd">
<td>2006.5622</td>
<td>--&gt;--&gt;APPOINTMENT SCHEDULE</td>
<td>--&gt;--&gt;1,D2,...</td>
</tr>
<tr class="even">
<td>2006.563</td>
<td>DICOM GATEWAY PARAMETER</td>
<td>^MAGDICOM(2006.563,D0,...</td>
</tr>
<tr class="odd">
<td>2006.5631</td>
<td>--&gt;DATA PATH</td>
<td>--&gt;“DATA PATH”,D1...</td>
</tr>
<tr class="even">
<td>2006.5632</td>
<td>--&gt;PROFILE</td>
<td>--&gt;“PROFILE”,D1...</td>
</tr>
<tr class="odd">
<td>2006.5634</td>
<td>--&gt;INSTALLATION</td>
<td>--&gt;“INSTALL”,D1...</td>
</tr>
<tr class="even">
<td>2006.564</td>
<td>DICOM QUEUE</td>
<td>^MAGDICOM(2006.564,D0,...</td>
</tr>
<tr class="odd">
<td>2006.5641</td>
<td>DICOM GATEWAY MACHINE ID</td>
<td>^MAGDICOM(2006.5641,D0,...</td>
</tr>
<tr class="even">
<td>2006.565</td>
<td>EXPORT DICOM RUN FILE</td>
<td>^MAGDICOM(2006.565,D0,...</td>
</tr>
<tr class="odd">
<td>2006.57</td>
<td>DICOM HL7 SEGMENT</td>
<td>^MAGDICOM("HL7",D0,...</td>
</tr>
<tr class="even">
<td>2006.5701</td>
<td>--&gt;ELEMENT</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="odd">
<td>2006.571</td>
<td>DICOM RAW IMAGE</td>
<td>^MAGDICOM(2006.571,D0,..</td>
</tr>
<tr class="even">
<td>2006.5711</td>
<td>DICOM M2MB RPC QUEUE</td>
<td>^MAGDINPT(2006.5711,D0,..</td>
</tr>
<tr class="odd">
<td>2006.5712</td>
<td>DICOM FIXED QUEUE</td>
<td>^MAGDINPT(2006.5712,D0,..</td>
</tr>
<tr class="even">
<td>2006.5713</td>
<td>DICOM UNKNOWN MODALITY</td>
<td>^MAGDINPT(2006.5713,D0,..</td>
</tr>
<tr class="odd">
<td>2006.5757</td>
<td>DICOM RADIOLOGY PROCEDURE MODIFIIERS</td>
<td>^MAGDICOM(2006.5757,D0,...</td>
</tr>
<tr class="even">
<td>2006.5758</td>
<td>DICOM RADIOLOGY PROCEDURES</td>
<td>^MAGDICOM(2006.5758,D0,...</td>
</tr>
<tr class="odd">
<td>2006.5759</td>
<td>OUTSIDE IMAGING LOCATION</td>
<td>^MAGD(2006.5759,D0,...</td>
</tr>
<tr class="even">
<td>2006.5761</td>
<td>DICOM MESSAGE STATISTISTICS</td>
<td>^MAGDAUDT(2006.5761,D0,...</td>
</tr>
<tr class="odd">
<td>2006.57611</td>
<td>--&gt;MESSAGE</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="even">
<td>2006.5762</td>
<td>DICOM INSTRUMENT STATISTICS</td>
<td>^MAGDAUDT(2006.5762,D0,...</td>
</tr>
<tr class="odd">
<td>2006.57621</td>
<td>--&gt;LOCATION</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="even">
<td>2006.5762111</td>
<td>--&gt;--&gt;INSTRUMENT</td>
<td><p>--&gt;--&gt;1,D2,...</p>
<p>CONSNON&gt;</p></td>
</tr>
<tr class="odd">
<td>2006.57621</td>
<td>--&gt;INSTRUMENT</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="even">
<td>2006.5763</td>
<td>DICOM PACS STATISTICS</td>
<td>^MAGDAUDT(2006.5763,D0,...</td>
</tr>
<tr class="odd">
<td>2006.57631</td>
<td>--&gt;ACCESSION NUMBER</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="even">
<td>2006.576311</td>
<td>--&gt;--&gt;EVENT</td>
<td>--&gt;--&gt;1,D2,...</td>
</tr>
<tr class="odd">
<td>2006.5764</td>
<td>DICOM LOCAL INSTRUMENT STATISTICS</td>
<td>^MAGDICOM(2006.5764,D0,...</td>
</tr>
<tr class="even">
<td>2006.57641</td>
<td>--&gt;DATE</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="odd">
<td>2006.577</td>
<td>DICOM FIFO QUEUE</td>
<td>^MAGDICOM(2006.577,D0,...</td>
</tr>
<tr class="even">
<td>2006.5771</td>
<td>--&gt;QUEUE LETTER</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="odd">
<td>2006.58</td>
<td>DICOM LOG</td>
<td>^MAGDMLOG(D0,...</td>
</tr>
<tr class="even">
<td>2006.5801</td>
<td>--&gt;TEXT</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="odd">
<td>2006.5802</td>
<td>--&gt;LINE</td>
<td>--&gt;2,D1,...</td>
</tr>
<tr class="even">
<td>2006.581</td>
<td>INSTRUMENT DICTIONARY</td>
<td>^MAGDICOM(2006.581,D0,...</td>
</tr>
<tr class="odd">
<td>2006.582</td>
<td>MODALITY TYPE DICTIONARY</td>
<td>^MAGDICOM(2006.582,D0,...</td>
</tr>
<tr class="even">
<td>2006.5821</td>
<td>CT CONVERSION PARAMETERS</td>
<td>^MAGDICOM(2006.5821,D0,...</td>
</tr>
<tr class="odd">
<td>2006.583</td>
<td>MODALITY WORKLIST DICTIONARY</td>
<td>^MAGDICOM(2006.583,D0,...</td>
</tr>
<tr class="even">
<td>2006.5831</td>
<td>DICOM HEALTHCARE PROVIDER SERVICE</td>
<td>^MAGDICOM(2006.5831,D0,...</td>
</tr>
<tr class="odd">
<td>2006.5839</td>
<td>DICOM GMRC TEMP LIST</td>
<td>^MAGDICOM(2006.5839,D0,...</td>
</tr>
<tr class="even">
<td>2006.584</td>
<td>TCP/IP PROVIDER PORT LIST</td>
<td>^MAGDICOM(2006.584,D0,...</td>
</tr>
<tr class="odd">
<td>2006.5841</td>
<td>TELEREADER ACQUISITION SERVICE</td>
<td>^MAG(2006.5841,D0,...</td>
</tr>
<tr class="even">
<td>2006.5842</td>
<td>TELEREADER ACQUISITION SITE</td>
<td>^MAG(2006.5842,D0,...</td>
</tr>
<tr class="odd">
<td>2006.5843</td>
<td>TELEREADER READER</td>
<td>^MAG(2006.5843,D0,...</td>
</tr>
<tr class="even">
<td>2006.5849</td>
<td>TELEREADER READ/UNREAD LIST</td>
<td>^MAG(2006.5849,D0,...</td>
</tr>
<tr class="odd">
<td>2006.585</td>
<td>USER APPLICATION</td>
<td>^MAGDICOM(2006.585,D0,...</td>
</tr>
<tr class="even">
<td>2006.5852</td>
<td>--&gt;SOP CLASS</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="odd">
<td>2006.58522</td>
<td>--&gt;--&gt;TRANSFER SYNTAX</td>
<td>--&gt;--&gt;1,D2,...</td>
</tr>
<tr class="even">
<td>2006.586</td>
<td>PROVIDER APPLICATION</td>
<td>^MAGDICOM(2006.586,D0,...</td>
</tr>
<tr class="odd">
<td>2006.5863</td>
<td>--&gt;SOP</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="even">
<td>2006.58633</td>
<td>--&gt;--&gt;TRANSFER SYNTAX UID</td>
<td>--&gt;--&gt;1,D2,...</td>
</tr>
<tr class="odd">
<td>2006.587</td>
<td>DICOM TRANSMIT DESTINATION</td>
<td>^MAG(2006, 587,...</td>
</tr>
<tr class="even">
<td>2006.588</td>
<td>APPLICATION ENTITY TITLE</td>
<td>^MAGDICOM(2006.588,D0,...</td>
</tr>
<tr class="odd">
<td>2006.59</td>
<td>ROUTING RULE</td>
<td>^MAGDICOM(2006.59,D0,...</td>
</tr>
<tr class="even">
<td>2006.5901</td>
<td>--&gt;RAW TEXT</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="odd">
<td>2006.5902</td>
<td>--&gt;ACTION</td>
<td>--&gt;ACTION,D1,...</td>
</tr>
<tr class="even">
<td>2006.5903</td>
<td>--&gt; --&gt;PARAMETER</td>
<td>--&gt; --&gt;1,D2,...</td>
</tr>
<tr class="odd">
<td>2006.5904</td>
<td>--&gt;CONDITION</td>
<td>--&gt; --&gt;1,D2,...</td>
</tr>
<tr class="even">
<td>2006.5905</td>
<td>--&gt; --&gt;TIMEFRAME</td>
<td>--&gt; --&gt;1,D2,...</td>
</tr>
<tr class="odd">
<td>2006.5906</td>
<td>ROUTE LOAD BALANCE</td>
<td>^MAGRT(2006.5906,D0,...</td>
</tr>
<tr class="even">
<td>2006.59061</td>
<td>--&gt;PARENT</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="odd">
<td>2006.596</td>
<td>ACTION QUEUE STATUS</td>
<td>^MAGDICOM(2006.596,D0,...</td>
</tr>
<tr class="even">
<td>2006.5961</td>
<td>--&gt;THREAD</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="odd">
<td>2006.598</td>
<td>DICOM ERROR MESSAGE QUEUE</td>
<td>^MAGD(2006.598,D0,...</td>
</tr>
<tr class="even">
<td>2006.599</td>
<td>DICOM Error Log</td>
<td>^MAGD(2006.599,D0,...</td>
</tr>
<tr class="odd">
<td>2006.621</td>
<td>MAG CT PARAMETER</td>
<td>^MAG(2006.621,D0,...</td>
</tr>
<tr class="even">
<td>2006.623</td>
<td>MAG CR PARAMETER</td>
<td>^MAG(2006.623,D0,...</td>
</tr>
<tr class="odd">
<td>2006.63</td>
<td>MAG RAD LIST DATA ELEMENTS</td>
<td>^MAG(2006.63,D0,...</td>
</tr>
<tr class="even">
<td>2006.631</td>
<td>MAG RAD LISTS DEFINITION</td>
<td>^MAG(2006.631,D0,...</td>
</tr>
<tr class="odd">
<td>2006.6311</td>
<td>--&gt;COLUMNS</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="even">
<td>2006.6312</td>
<td>--&gt;SORT</td>
<td>--&gt;2,D1,...</td>
</tr>
<tr class="odd">
<td>2006.634</td>
<td>MAGJ ZLIST SEARCH FILE</td>
<td>^MAG(2006.634,D0,...</td>
</tr>
<tr class="even">
<td>2006.65</td>
<td>MAG RAD PRIOR EXAM LOGIC</td>
<td>^MAG(2006.65,D0,...</td>
</tr>
<tr class="odd">
<td>2006.66</td>
<td>--&gt;PRIOR CASE MATCHING CPT GROUP</td>
<td>--&gt;1,D1,...</td>
</tr>
<tr class="even">
<td>2006.67</td>
<td>MAG RAD CPT MATCHING</td>
<td>^MAG(2006.67,D0,...</td>
</tr>
<tr class="odd">
<td>2006.674</td>
<td>--&gt;BODY PART</td>
<td>--&gt;1,...</td>
</tr>
<tr class="even">
<td>2006.675</td>
<td>--&gt;MODALITY</td>
<td>--&gt;2,...</td>
</tr>
<tr class="odd">
<td>2006.68</td>
<td>MAGJ USER DATA</td>
<td>^MAG(2006.68,D0,...</td>
</tr>
<tr class="even">
<td>2006.682</td>
<td>--&gt;VR-WS</td>
<td>--&gt;VR-WS,D1,...</td>
</tr>
<tr class="odd">
<td>2006.6821</td>
<td>--&gt;--&gt;DATA</td>
<td>--&gt;--&gt;VR-WS,D1,1,...</td>
</tr>
<tr class="even">
<td>2006.6823</td>
<td>--&gt;--&gt;KEYS</td>
<td>--&gt;--&gt;VR-WS,D1,2,...</td>
</tr>
<tr class="odd">
<td>2006.683</td>
<td>--&gt;VR-HP</td>
<td>--&gt;VR-HP...</td>
</tr>
<tr class="even">
<td>2006.6831</td>
<td>--&gt;--&gt;DATA</td>
<td>--&gt;--&gt;VR-HP,D1,1,...</td>
</tr>
<tr class="odd">
<td>2006.6832</td>
<td>--&gt;--&gt;KEYS</td>
<td>--&gt;--&gt;VR-HP,D1,2,...</td>
</tr>
<tr class="even">
<td>2006.69</td>
<td>MAG VISTARAD SITE PARAMETERS FILE</td>
<td>^MAG(2006.69,D0,...</td>
</tr>
<tr class="odd">
<td>2006.8</td>
<td>BP WORKSTATIONS</td>
<td>^MAG(2006.8,D0,...</td>
</tr>
<tr class="even">
<td>2006.81</td>
<td>IMAGING WINDOWS WORKSTATIONS</td>
<td>^MAG(2006.81,D0,...</td>
</tr>
<tr class="odd">
<td>2006.82</td>
<td>IMAGING WINDOWS SESSIONS</td>
<td>^MAG(2006.82,D0,...</td>
</tr>
<tr class="even">
<td>2006.821</td>
<td>--&gt;ACTIONS</td>
<td>--&gt;"ACT",D1,...</td>
</tr>
<tr class="odd">
<td>2006.823</td>
<td>--&gt;ERRORS</td>
<td>--&gt;"ERR",D1,...</td>
</tr>
<tr class="even">
<td>2006.83</td>
<td>DICOM WORKSTATION</td>
<td>^MAG(2006.83,D0,...</td>
</tr>
<tr class="odd">
<td>2006.87</td>
<td>DICOM GATEWAY INFORMATION</td>
<td>^MAG(2006.87,D0,...</td>
</tr>
<tr class="even">
<td>2006.95</td>
<td>IMAGE ACCESS LOG</td>
<td>^MAG(2006.95,D0,...</td>
</tr>
<tr class="odd">
<td>2006.96</td>
<td>IMAGE INDEX CONVERSION</td>
<td>^MAGIXCVT (2006.96,D0...</td>
</tr>
<tr class="even">
<td>2006.961</td>
<td>MULTI IMAGE PRINT FILE</td>
<td>^MAG(2006.961,</td>
</tr>
<tr class="odd">
<td>2006.9613</td>
<td>--&gt;IMAGES PRINTED SUB- FILE</td>
<td>^MAG(2006.961,D0,"IMG",</td>
</tr>
</tbody>
</table>

#### More Detailed Information

> More detailed information about these files can be obtained using the FileMan option LIST FILE ATTRIBUTES. The Data Dictionaries are considered part of the online documentation for this software application. It may be necessary to print the Data Dictionaries in order to support the package at your site.

> The Data Dictionaries for VistA Imaging files may be printed using the VA FileManager’s option LIST FILE ATTRIBUTES under the DATA DICTIONARY UTILITIES menu as follows:

![](vista-imaging-system-technical-manual/020.png)

> The Data Dictionary will now print on the user's specified device.

### Input Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The distribution contains the following input templates:

> FILE \#2005 MAG IMAGE INDEX EDIT FILE \#2006.1: MAG PURGE PARAMETERS FILE \#2006.1: MAG SITE PARAMETERS FILE \#2006.1: MAG MUSE PARAMETERS

> FILE \#2005.2: MAG ENTER/EDIT NETWORK LOC FILE \#2005.2: MAG ENTER/EDIT MUSE NETWORK FILE \#2005.575: MAGD-ENTRY

> FILE \#2005.575: MAGD-UPDT

> FILE \#2005.88: MAG REASON EDIT

> FILE \#2006.8: MAG EDIT BACKGRND WORKSTA FILE \#2006.631: MAGJ LIST EDIT

> FILE \#2006.65: MAGJ PRIOR EDIT

#### Further Information

> Every individual object (i.e., an image, audio clip, waveform, or scanned document) is an entry in the IMAGE file (#2005), where the object's attributes are managed. In addition, three auxiliary files are used:

- Object Type
- Network Location
- Parent Data

> The objects are then related to the patient's VistA text data (medicine, surgery, laboratory, radiology reports or progress notes) through the use of pointers, both forward from the VistA PACKAGE file (#9.4) to the IMAGE file (#2005), and backwards from the IMAGE file (#2005) to the VistA PACKAGE file (#9.4). Software allows new objects to be added and displayed.

> Several additional files are used by the system. These include:

- IMAGING WINDOWS WORKSTATIONS file (#2006.81), which contains information about every workstation on the network.
- IMAGE HISTOLOGICAL STAIN file (#2005.4), and the MICROSCOPIC OBJECTIVE file

> (#2005.41) used by anatomic pathology.

- IMAGING SITE PARAMETERS file (#2006.1).
- Background Queue files, which are necessary to manage abstract creation, automatic file migration (movement of image/object files between optical disk jukebox and magnetic disk), file copies.
- IMAGE ACCESS LOG file (#2006.95) used to track system utilization.
- User preferences files, which store personal preferences for the software configuration of the workstation.
- IMAGE LIST FILTERS file (#2005.87), which stores personal filters for each user, and public filters for all users.
- IMAGE FILE TYPES file (#2005.021), which lists all image formats that VistA Imaging supports.
- IMAGING ANNOTATION file (#2005.002), which stores annotation information that is associated with an image.
- Parameters that are specific for each individual DICOM Gateway Computer.
- Master files that drive the operation of the DICOM Gateway.
- Modality Worklist file that contains the scheduled activities for the various modalities that acquire images.
- Incoming Images.
- Images that need manual intervention before they can be entered into the VistA HIS.

### File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA Imaging System files are in the 2005 through the 2006.999 numbering space. Full file and field documented attributes on any Imaging files can be obtained using the LIST FILE ATTRIBUTES sub-menu option located in the ‘Data Dictionary Utilities menu.

![](vista-imaging-system-technical-manual/021.png)

### Files Introduced in MAG\*3.0\*34

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The new data structure introduced in MAG\*3.0\*34 includes these files:

- IMAGING PATIENT REFERENCE file (#2005.6)

> The file contains information about each patient with which imaging procedures and studies are associated within VistA.

- IMAGING PROCEDURE REFERENCE file (#2005.61)

> The file contains information about each procedure corresponding to an entry in the IMAGING PATIENT REFERENCE file (#2005.6).

- IMAGE STUDY file (#2005.62)

> The file contains information about each study corresponding to an entry in the IMAGING PROCEDURE REFERENCE file (#2005.61).

- IMAGE SERIES file (#2005.63)

> The file contains information about each series corresponding to an entry in the IMAGE STUDY file (#2005.62).

- IMAGE SOP INSTANCE file (#2005.64)

> The file contains information about each SOP instance in the IMAGE SERIES file (#2005.63).

- IMAGE INSTANCE FILE file (#2005.65)

> The file contains information about each physical file instance corresponding to an entry on the IMAGE SOP INSTANCE file (#2005.64).

- IMAGING DUPLICATE UID LOG file (#2005.66)

> The file contains information about duplicate UIDs.

- IMAGING SERVICE INSTITUTION file (#2005.8)

> The file contains entries indicating the Imaging institution associated with an action performed on an Imaging file entry.

- DICOM GATEWAY INSTRUMENT DICTIONARY file (#2006.911)

> The file contains information about the instruments that communicate with the DICOM Gateway.

- DICOM GATEWAY MODALITY DICTIONARY file (#2006.912)

> The file contains information about the various types of image acquisition devices that are present at a site. Note that a modality is a class of devices; an instrument is a specific device or an instance of such a class.

- ARTIFACT KEYLIST file (#2006.913)

> The file includes information that allows clients of the storage system, such as display clients and the Query/Retrieve application to retrieve artifacts (images) stored in the VistA system at the site.

- RETENTION POLICY file (#2006.914)

> The file contains information about the various retention policies available to the storage system. Retention policies can be user-definable or business.

- ARTIFACT DESCRIPTOR file (#2006.915)

> The file acts as the entry point into the storage system. It holds information about a particular type of artifact (such as the artifact type MedicalImage, which is an image in DICOM format) and maps this type of artifact to its intrinsic retention policy. The file also stores the file extension that is used for files of the given type. Artifact descriptors records are created when the patch is installed. Users cannot delete or modify these records or create new ones.

- ARTIFACT file (#2006.916)

> The file holds records with information about the artifact: CRC, size, who the artifact was created by, a link back to the artifact descriptor, and so on. (An artifact is an object that the storage system stores, such as an image, a text file, a report, an abstract.)

- STORAGE PROVIDER file (#2006.917)

> The file includes information about the devices used at the site. It contains one record for each device. For example, if there is a consolidated site with a RAID in place A, a RAID in place B, and an archive in place B, there would be 3 entries in the file. The information in the file is used to determine whether a particular configuration is valid at configuration and at runtime.

- ARTIFACT INSTANCE file (#2006.918)

> The file holds the details of a particular instance of the binary data for an artifact. Each record is owned by a specific provider and has a reference to its parent artifact record, as well as a URL that the given provider can understand and that can be used to return a stream for the artifact. The file also includes properties related to when the file was created, when it was last accessed, and so on.

- MAGV GATEWAY CONFIGURATION file (#2006.9191)

> The file contains configuration parameters of the DICOM Gateways connected to the VistA system at the specific site.

- DICOM AE SECURITY MATRIX file (#2006.9192)

> The file contains a list of the devices (application entities) that can connect to the VistA system and their parameters, which include the type of access they have to the system (defined as the DICOM service and role).

- IMAGING APPLICATION SERVICE file (#2006.9193)

> The file contains VistA Imaging applications or services, such as HDIG, DICOM Importer II, and VI DICOM Storage SCP.

- ARTIFACT RETENTION POLICY file (#2006.921)

> The file maps an artifact to the set of retention policies currently and also historically in effect for that artifact.

- RETENTION POLICY FULFILLMENT file (#2006.922)

> The file maps a running history of how particular retention policies caused artifacts to be written to specific storage providers. It is also used by asynchronous archiving to determine which retention policies have not yet been satisfied and which storage providers still need to be written to.

- RETENTION POLICY STORAGE PROVIDER MAP file (#2006.923)

> The file maps retention policies, through an acquisition location, to the storage providers that should be used to satisfy the retention policies. It also contains a flag indicating whether a particular storage provider should be called synchronously or asynchronously.

- STORAGE PROVIDER AVAILABILITY file (#2006.924)

> The file contains information about the availability of a connection between an acquisition place and a particular storage (archive) provider. If there is a record for a particular storage provider/acquisition location pair, the connection is only available between the start and end times indicated in the record. If there is no record, the connection is always available.

- TRANSFER STATISTICS file (#2006.925)

> The file contains statistics about network transfers between a storage provider and a client endpoint, including the time of day the transfer occurred, the duration of the transfer, and the size of the artifact.

- STORAGE TRANSACTION file (#2006.926)

> The file records the actions for a particular artifact, such as: storing the artifact successfully in a specific storage provider; failed attempts to store the artifact in a storage provider; retrieving the artifact from a particular storage provider; failed attempts to retrieve the artifact from a storage provider.

- QUEUE file (#2006.927)

> The file is a list of Queues (queue types). It contains the queue for asynchronous storage requests, the queue for failed asynchronous storage requests, the Abstract Maker queue and the queue for sending email notifications.

- QUEUE MESSAGE file (#2006.928)

> The file stores the messages for the requests for all queues defined in the QUEUE file. Each record in the file contains information about the queued request: the message itself, a reference to the queue, the priority of the request, the minimum delivery date/time, and expiration date/time of the message. The file is used by internal processes to carry out the actions for all queued requests.

- IMAGING EVENT AUDIT LOG file (#2006.93)

> The file contains a list of all audited events.

- IMAGING EVENT AUDITABLE ACTION file (#2006.931)

> The file contains the list of VistA Imaging events that can be audited.

- MAG WORK ITEM file (#2006.941)

> The file contains a queue of work items for worklists in the WORKLIST file (#2006.9412).

- WORKLIST file (#2006.9412)

> The file contains entries for worklists and their current activity status.

- MAG WORK ITEM STATUS file (#2006.9413)

> This file contains work item statuses.

- MAG WORK ITEM SUBTYPE file (#2006.9414)

> This file contains work item subtypes.

- MAGV IMPORT STUDY LOG file (#2006.9421)

> The file contains a log of import events carried out by the DICOM Importer II at the study level. These include user and study information, and counts of the total number of series and objects imported, the number of objects that failed to import, and of the number of objects imported for each modality contained within the study. This information allows generation of reports covering importer activity for a user-specified time period.

- MAGV IMPORT MEDIA LOG file (#2006.9422)

> The file holds a log of import events carried out by the DICOM Importer II at the media bundle level. A media bundle is a group of studies under a single Importer II work item. A media bundle may or may not represent a single piece of media or a single network transaction. This file includes information about media validity, the user who reconciled the associated studies, the workstation, as well as the source of the imported media.

### Sort and Print Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Sort and Print Templates for the IMAGING PATIENT REFERENCE File (#2005.6)

- MAGV-PAT-QUERY – This sort template enables users to retrieve study, series, image, and file information for a single patient or a range of patients, based on the value of the ENTERPRISE PATIENT ID field (#.01).
- MAGV-PAT-QUERY – This print template returns a report with the following Binformation:

Sort and Print Templates for the IMAGING PROCEDURE REFERENCE File (#2005.61)

<table>
<colgroup>
<col style="width: 53%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>For each requested patient:</p>
</blockquote></th>
<th>Name and social security number</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>For each of the patient’s procedures:</p>
</blockquote></td>
<td>Procedure ID</td>
</tr>
<tr class="even">
<td><blockquote>
<p>For each study within the procedure:</p>
</blockquote></td>
<td><p>Study instance UID</p>
<p>Description Modalities in study</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>For each series within the study:</p>
</blockquote></td>
<td><p>Series instance UID</p>
<p>Description Modality</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p>For each SOP instance within the series:</p>
</blockquote></td>
<td><p>SOP instance UID</p>
<p>SOP class UID</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>For each file within the SOP instance:</p>
</blockquote></td>
<td>Fileref</td>
</tr>
</tbody>
</table>

- MAGV-PROC-QUERY – This sort template enables users to retrieve study and series information for a single procedure or a range of procedures, based on the value of the PROCEDURE ID field (#.01).
- MAGV-PROC-QUERY – This print template returns a report with the following information:

Sort and Print Templates for the ARTIFACT INSTANCE File (#2006.918)

<table>
<colgroup>
<col style="width: 53%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>For each requested procedure:</p>
</blockquote></th>
<th>Procedure ID</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>For the associated patient:</p>
</blockquote></td>
<td><p>Social security number Name</p>
<p>Date of birth</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p>For each study within the procedure:</p>
</blockquote></td>
<td><p>Study instance UID</p>
<p>Description Modalities in study</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>For each study within the procedure:</p>
</blockquote></td>
<td>Study instance UID</td>
</tr>
<tr class="even">
<td><blockquote>
<p>For each series within the study:</p>
</blockquote></td>
<td>Series instance UID</td>
</tr>
</tbody>
</table>

- MAGV-FILEREF-QUERY – This sort template enables users to retrieve patient, study, and series information for a single file or a range of files based on the value of the FILEREF field (#6).
- MAGV-FILEREF-QUERY – This print template returns the following information:

Sort Template for the QUEUE MESSAGE File (#2006.928)

<table>
<colgroup>
<col style="width: 53%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>For each requested file:</p>
</blockquote></th>
<th>File name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>For the associated patient:</p>
</blockquote></td>
<td><p>Social security number Name</p>
<p>Sex</p>
<p>Date of birth</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p>For each study within the procedure:</p>
</blockquote></td>
<td><p>Study instance UID Description</p>
<p>Modalities in study</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>For each study within the procedure:</p>
</blockquote></td>
<td>Study instance UID</td>
</tr>
<tr class="even">
<td><blockquote>
<p>For each series within the study:</p>
</blockquote></td>
<td>Series instance UID</td>
</tr>
</tbody>
</table>

- MAGVA-ASYNC-STORAGE-ERRORS – This sort template is for system use only. It is used by Hybrid DICOM Gateway Menu \[MAGV HDIG MENU\] Option Find Async Storage Request Errors \[MAGVA ASYNC STORAGE ERR QURY\] to store results of a query for Asynchronous Storage Request Error Queue entries in the QUEUE MESSAGE file (#2006.928), and by Option List Async Storage Request Errors \[MAGVA ASYNC STORAGE ERR LIST\] to display information about the entries.

### File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA Imaging System files are in the 2005 through the 2006.999 numbering space. Full file and field documented attributes on any Imaging files can be obtained using the LIST FILE ATTRIBUTES sub-menu option located in the ‘Data Dictionary’ Utilities menu.

![](vista-imaging-system-technical-manual/022.png)

### File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA Imaging recommends no access to any Imaging files by any end-user other than IRM personnel. Please review the Security manual to get a detail listing of all FileMan protections on all Imaging files. All updating of Imaging files is done via the GUI interface or by the Imaging System Manager menu (locked by the MAG SYSTEM security key) on the VistA hospital system. However, the recommended method is to use the VistA Imaging Background Processor application (GUI).

> The following imaging entity relationship diagram shows the data structures that existed before the release of MAG\*3.0\*34.

Imaging Entity Relationship Diagram and Detailed Information

![](vista-imaging-system-technical-manual/023.png)

> A detailed File Diagram can be obtained using the FileMan’s menu option ‘MAP POINTER RELATIONS’.

- Select ‘DATA DICTIONARIES UTILITIES’ from the FileMan menu.
- Select ‘MAP POINTER RELATIONS’ menu option.
- Respond to the ‘PACKAGE NAME’ prompt with IMAGING.

> The following imaging entity relationship diagram shows the data structures that were introduced in MAG\*3.0\*34. The diagram includes key fields for each table, It also shows the pointers to other data structures: the old data structures and non-VistA Imaging data tables.

Imaging Entity Relationship Diagram: Data Structures Introduced in MAG\*3.0\*34

![](vista-imaging-system-technical-manual/024.png)

> A detailed and current File Diagram can be obtained using the FileMan’s menu option ‘MAP POINTER RELATIONS’.

- Select ‘DATA DICTIONARIES UTILITIES’ from the FileMan menu.
- Select ‘MAP POINTER RELATIONS’ menu option.
- Respond to the ‘PACKAGE NAME’ prompt with IMAGING.

### Global Journaling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Journaling of the VistA Imaging global is mandatory. MAG\* should be journaled.

> During a scheduled VistA (hospital) server downtime, it is highly recommended to coordinate any data restore activities related to the VistA Imaging System with the IRM staff.

### VistA System Outages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> During a VistA System outage, DICOM Gateways will continue to provide modality worklist functionality and to capture images that are temporarily stored on the gateway. This is important to allow the radiology department to continue to perform studies. If you anticipate that the VistA System must be down, it is best to take the following steps:

- Perform all DICOM fixes before the VistA System goes down. This will free the maximum space for temporary image storage.
- During the outage, watch the gateways to be sure they still have adequate space to store images.

> This page is intentionally blank.

## Chapter 8 Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction: INI File Setup and Configuration of Workstations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> INI files are DOS files with the extension .ini (such as win.ini and mouse.ini) that contain initialization information for programs. Initialization refers to the parameters that control the way a program is initially launched. They also customize the application to accommodate workstation-specific characteristics, such as the type of capture hardware installed (Refer to *VistA Imaging System Installation Guide* for further details). The INI files are set up initially when the software is first installed on the workstation.

### Imaging System Manager Menu \[MAG SYS MENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Imaging System Manager Menu \[MAG SYS MENU\] contains system manager functions. Access to these menu options requires the MAG SYSTEM security key.

> Menu Diagram for Imaging System Manager Menu \[MAG SYS MENU\]

![](vista-imaging-system-technical-manual/025.png)

> Editing the Network Location Status should be performed by using the Network Location Manager in the Background Processor.

> Imaging Database Integrity checking should be performed in the Background Processor using the Verifier application.

> Note: You can enter ??? at the Select Imaging System Manager Menu Option prompt for a description of each menu option.

> See the *Background Processor User Manual* for more information.

> For detailed information about the ‘Telereader Menu …’ option, refer to the TeleReader Configuration document.

> For detailed information about the “Ad hoc Enterprise Site Report” option and the “Imaging Site Reports” option, refer to Chapter 12.

#### Imaging Hl7 Messaging Maintenance \[Mag Hl7 Maint\]

> This option contains sub-options that allow you to modify parameters relating to the transmission of HL7 ADT messages to commercial PACS (cPACS) and to select the version of HL7 order messages that should be sent from VistA Radiology to cPACS and to the VistA Text Gateway.

> Note: If you need help with the sub-options of this option, consult the designated HL7 specialist within the IRM department at your site.

> Menu Diagram for Imaging HL7 Messaging Maintenance \[MAG HL7 MAINT\]

![](vista-imaging-system-technical-manual/026.png)

#### Maintain Subscriptions to Radiology Hl7 Drivers \[Magd Maint Rad Hl7 Subs\]

> This option allows you to select the version of HL7 order messages that should be sent from VistA Radiology to cPACS and to the VistA Text Gateway.

> From the Imaging System Manager Menu, select HL7:

![](vista-imaging-system-technical-manual/027.png)

> From the Imaging HL7 Messaging Maintenance Menu, select RHL7:

![](vista-imaging-system-technical-manual/028.png)

> VistA Imaging first verifies that all applicable HL7 protocols are available. There are two Imaging subscriber protocols and eight Radiology event driver protocols – four for HL7 Version 2.1 messages and four for HL7 Version 2.4 messages.

![](vista-imaging-system-technical-manual/029.png)

> VistA Imaging then asks which version of HL7 you wish to be used to generate Radiology messages. Enter 2.1 or 2.4.

![](vista-imaging-system-technical-manual/030.png)

> If the desired HL7 version is not currently in use, VistA Imaging adjusts protocol subscriptions to cause the desired version to come into use.

![](vista-imaging-system-technical-manual/031.png)

If the desired HL7 version is already in use, the system will take no action.

![](vista-imaging-system-technical-manual/032.png)

#### Configure Ihe-Based Hl7 Adt Interface To Pacs

> This option allows you to modify parameters relating to the transmission of HL7 version 2.4 ADT messages to commercial PACS (if used) and the DICOM Text Gateway.

> From the Imaging System Manager Menu, select HL7:

![](vista-imaging-system-technical-manual/033.png)

> From the Imaging HL7 Messaging Maintenance Menu, select IHE:

![](vista-imaging-system-technical-manual/034.png)

> VistA Imaging first asks you to verify the name of the sending application and the receiving application. These are the applications in the HL7 APPLICATION PARAMETER File (#771) whose NAME Field values are associated with the entries in field 3 and 5 respectively, and whose FACILITY NAME Field values are associated with the entries in fields 4 and 6 respectively, of the Message Header (MSH) segments of the outbound HL7 messages

> Note: This option only changes the names of the sending and receiving applications. To change the names of the sending and receiving facilities, get help from the designated HL7 specialist within the IRM department at your site.

![](vista-imaging-system-technical-manual/035.png)

> If you wish to accept the application names that are presented, enter N. Otherwise, enter Y and enter the desired new application names at the prompts:

![](vista-imaging-system-technical-manual/036.png)

> VistA Imaging next asks you to enter the TCP/IP address and port number of the logical link over which the outbound VistA HL7 stream will be transmitted to cPACS.

![](vista-imaging-system-technical-manual/037.png)

> Finally, you are asked whether you wish to turn on the IHE-based PACS interface, which will transmit IHE-conformant ADT HL7 messages from VistA HIS to cPACS (if used) and to the DICOM Text Gateway.

![](vista-imaging-system-technical-manual/038.png)

> Enter Y to turn the interface on or N to turn it off.

### Configure AE Security Matrix Settings \[MAGV AE SEC MX SETTINGS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This menu lets users edit the DICOM AE SECURITY MATRIX file (#2006.9192). The file contains a list of application entity (AE) titles: all remote devices that can connect to the local VistA system and its components. It also determines which devices can connect to the VistA system and the type of access that they are allowed (a combination of DICOM service and the DICOM role associated with this service). For example, a device that is a Service Class User (SCU) of the Storage Service Class (C-STORE) can send DICOM objects to a DICOM Gateway that is defined as a Service Class Provider (SCP) of the Storage Service Class. If a device is not listed in the DICOM AE Security Matrix, it cannot access the VistA system or its components.

> VistA Imaging system administrators use the menu option Configure AE Security Matrix Settings \[MAGV AE SEC MX SETTINGS\] after initial installation to define the remote devices that can connect to the local VistA system and its components. They will also use the menu option to remove devices, or to change device properties.

> The Configure AE Security Matrix Settings \[MAGV AE SEC MX SETTINGS\] menu option is accessed from the Imaging System Manager Menu \[MAG SYS MENU\].

![](vista-imaging-system-technical-manual/039.png)

> For information about the AE Security Matrix and about using the Configure AE Security Matrix Settings to configure the AE Security Matrix, see the *VistA Imaging DICOM Gateway Installation Guide*.

### Delete Study by Accession Number \[MAG SYS-DELETE STUDY\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This menu allows a user with the MAG DELETE key to delete studies by accession number. In the data structures introduced in MAG\*3.0\*34, each study has a different accession number. The Delete Study by Accession Number is useful for deleting studies from the new data structures.

> For deleting studies from the old data structures, you can still use the Delete Image Group option. This option deletes all images in the group, regardless if they are in the new or in the old data structures.

> The \[MAG SYS-DELETE STUDY\] menu option is accessed from the Imaging System Manager Menu \[MAG SYS MENU\].

![](vista-imaging-system-technical-manual/040.png)

> To delete a study by accession number:

1.  From the Imaging System Manager Menu, select Delete Study by Accession Number:

![](vista-imaging-system-technical-manual/041.png)

2.  Enter the accession number of the study you want to delete.

![](vista-imaging-system-technical-manual/042.png)

3.  Select a reason for deleting the study.

![](vista-imaging-system-technical-manual/043.png)

4.  Type Yes to confirm you want to delete the study.

![](vista-imaging-system-technical-manual/044.png)

> The system displays a message that the study has been deleted. The study is marked for deletion in the database. It will no longer be available for viewing, queries or any other operations.

![](vista-imaging-system-technical-manual/045.png)

### Enter/Edit Reason \[MAG REASON EDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This menu option allows adding/editing of reasons for actions performed on images (copying, printing, etc.) stored in the MAG REASON file (#2005.88). The Reason codes and definitions shown are samples only.

![](vista-imaging-system-technical-manual/046.png)

> From the System Manager menu \[MAG SYS MENU\] select Enter/edit Reason.

![](vista-imaging-system-technical-manual/047.png)

> At the prompt Select MAG REASON: enter a reason number to display an existing reason; or a ? to display a list of all MAG REASON numbers currently stored.

![](vista-imaging-system-technical-manual/048.png)

> A new MAG REASON is added by entering the name of a new MAG REASON at the prompt.

![](vista-imaging-system-technical-manual/049.png)

> Because new MAG REASON codes can be created either by the national VistA team, or by local site administrators, the MAG REASON code list varies from site to site. In some cases, the same reason appears on different site lists with different code numbers. For example, the latest nationally created reason—For use in Veterans Benefits Administration claims processing, which was created as part of the VIX maintenance Patch 124—is number 16 on the list of nationally created reasons. But if a site used the 16th place in its MAG REASON code list for a local reason before Patch 124, that local reason appears as L16 on that site’s MAG REASON list, and the new national code takes the next number in line. In that hypothetical case, For use in Veterans Benefits Administration claims processing would appear as code 17 on the site’s MAG REASON list.

> The national MAG Reason Code list now contains 16 codes (see table). It contained 15 reason codes before site administrators were given the capability to create local reason codes. These 15 reasons are uniform across all VistA sites.

| Number | Reason                                                                                          | Type | Code |
|------------|-----------------------------------------------------------------------------------------------------|----------|----------|
| 1          | Clinical care for the patient whose images are being downloaded                                     | CP       | 1        |
| 2          | Clinical care for other VA patients                                                                 | CP       | 2        |
| 3          | For use in approved research by VA staff                                                            | CP       | 3        |
| 4          | For approved teaching purposes by VA staff                                                          | CP       | 4        |
| 5          | For use in approved VA publications                                                                 | CP       | 5        |
| 6          | Authorized release of medical records or health information (ROI)                                   | CP       | 6        |
| 7          | Corrupt image                                                                                       | D        | 7        |
| 8          | Low quality image                                                                                   | DS       | 8        |
| 9          | Wrong case/exam/accession number                                                                    | DS       | 9        |
| 10         | Wrong note title                                                                                    | D        | 10       |
| 11         | Wrong patient                                                                                       | D        | 11       |
| 12         | Image is incorrectly included in an image group                                                     | D        | 12       |
| 13         | All images were removed from the group                                                              | D        | 13       |
| 14         | HIMS document correction When a document or image needs to have the patient or image data corrected | DS       | 14       |
| 15         | Rescinded TIU Note                                                                                  | SD       | 15       |
| 16         | For use in Veterans Benefits Administration claims processing.                                      | CP       | 16       |

> Note: The transaction log/report lists actions on images by type and reason. For an accurate understanding of the logs from any VA site, complete the steps in the first two paragraphs of this section to retrieve a list of all MAG REASON codes currently being used at the site. Locate the MAG REASON number on the site list. Each MAG REASON number on this list is paired with the text of the reason for the action.

### MAG Client Version Report \[MAG CLIENT VERSION REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Imaging Clients Version Report \[MAG CLIENT VERSION REPORT\]. This option prints the list of workstations and clients that need updates. When the new version of the VistA server code is distributed, those clients may continue, but they are not supported.

> From the Imaging System Menu \[MAG SYS MENU\], enter "Imaging Site Reports" at the prompt.

![](vista-imaging-system-technical-manual/050.png)

> At the prompt, enter "Imaging Clients Version Report".

![](vista-imaging-system-technical-manual/051.png)

![](vista-imaging-system-technical-manual/052.png)

### Imaging VistARad System Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistARad System Options Menu is used to set site parameters that control VistARad’s basic behaviors and performance, to create custom exam lists, and to review and manage VistARad’s prefetch and CPT (Current Procedural Terminology) code matching capabilities.

> Menu Diagram for MAGJ MAIN

![](vista-imaging-system-technical-manual/053.png)

### Imaging MAG WINDOWS Menu Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The menu option MAG WINDOWS should be assigned as a secondary menu option to end-users who need access to VistA Imaging, and to all users and operators of the DICOM Gateways and Background Processor applications. This menu outlines enables:

- Access to all the RPCs used by VistA Imaging
- An automated log-on to applications experiencing service interrupted by network and host system outages

### Imaging VistARad MAGJ VISTARAD WINDOWS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The menu option MAGJ VISTARAD WINDOWS should be assigned as a secondary menu option to end-users who need access to VistA Imaging VistARad. This menu outlines all the RPCs used by VistARad.Imaging MAG JB OFFLINE Menu option

> This menu option is not part of any menu and is discussed in Chapter 9 of this manual; section Removing Jukebox Media - Offline Images.

### Imaging DICOM Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA Imaging DICOM Gateway itself does not use VA Kernel software, and as a result, does not use any Options. However, on the VistA hospital system the following menu does relate to the DICOM Gateways. See the *Imaging DICOM User Manual* for full instructions on using this menu.

> Menu Diagram for MAGD DICOM MENU

![](vista-imaging-system-technical-manual/054.png)

### Imaging Menu Options Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A full description for all of the Imaging’s VistA menu options can be obtained by using FileMan print menu option.

![](vista-imaging-system-technical-manual/055.png)

### Access to DICOM Gateway RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA system grants access to Remote Procedures based on a relation between certain menu options and the RPCs in question. The DICOM Gateway uses two classes of RPCs: those that can be called by any user of the DICOM Gateway (“view-only access”) and those that can only be called by end-users with “full access”. In order to support this distribution of privileges, the following two menu options are present in the VistA system and should be assigned to the appropriate personnel:

> MAG DICOM GATEWAY VIEW MAG DICOM GATEWAY FULL

### Imaging Menu Options Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A full description for all of the Imaging VistA menu options can be obtained by using the FileMan print menu option.

![](vista-imaging-system-technical-manual/056.png)

> Note: The output displayed by the option, Inquire VistARad CPT Matching Set \[MAGJ INQUIRE CPT MATCHING SET\], has been modified to display attributes defined for the entered CPT code, and also the matching CPT code values for its related "Similar CPT" and "Modality/Body Part" combinations.

> Note: This change as implemented does not require any KIDS component, so no new or modified Menu options will be apparent in the KIDS definition or installation files.

> This page is intentionally blank.

## Chapter 9 Archiving, Purging, Verifying, and Backup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter explains how to archive, purge, and verify VistA Imaging files and VistA Imaging FileMan entries. Image files are part of the patient’s record and must be preserved for the required number of years. Image files may be kept online indefinitely. As image files get older and have not been accessed recently, they reside on the optical disk jukeboxes where they are still accessible to users, but access is less rapid. Some sites have taken platters out of jukeboxes for shelf storage, but these are reloaded when needed by a user. The state of the images on the storage devices and their relationship (through file references) to the VistA database require periodic verification.

> Most of the information in this chapter describes archiving, purging, and backup using the Background Processor and refers to the data that is stored in the data structures that were used before MAG\*3.0\*34 (also referred to as the “old” data structures). This data includes the SOP classes that were supported before MAG\*3.0\*34.

> DICOM objects and studies from the SOP classes for which support was introduced in MAG\*3.0\*34 are stored in the data structures that were introduced in MAG\*3.0\*34 (also referred to as the “new” data structures). The Archiver, which is installed with the HDIG, manages the archiving and data aging in the new data structures. For information about handling processing and storage errors in the new data structures, see section *11.4 Handling Processing and Storage Errors in the New Data Structures.*

### Archiving and Purging of Image FileMan Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Entries in the IMAGE file (#2005) should not be purged or archived.

### Archiving and Purging of Image Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Automatic Image File Migration

> The imaging workstation stores the full-size image file on the server when the image is captured. An abstract may be created by the capture workstation, or by placing an entry in the Abstract queue. An entry is placed in the JUKEBOX queue. The background processor then copies the images to Tier 2.

> After a period of time during which an image is not accessed:

1.  The full-size image will be deleted from the magnetic file server. It will still be accessible to users from Tier 2.
2.  Next, the abstract will be deleted from the magnetic file server. If a subsequent request is made to display the full-size image or the abstract, that file will be copied back to the magnetic file server.

> Because images are stored temporarily on the magnetic servers, these are referred to as VistA magnetic cache.

#### Purging Tier 1 Shares

> The Background Processor’s Purge application clears disk space within the VistA Imaging shares. This space is necessary for newly captured files from Imaging modalities and the DICOM gateways. Space is also needed for files that are copied from Tier 2 when images are viewed on Imaging display workstations.

> Each file on every VistA Imaging shares is evaluated to determine if it should be purged, as follows:

- The file name must consist of the local namespace followed by the number which coincides with its IMAGE file (#2005) internal entry number. If the corresponding IMAGE file (#2005) entry does not exist, the image file is unconditionally purged from the VistA Imaging shares.
- The file location is checked against the IMAGE file (#2005) settings. If the IMAGE file (#2005) entry has no current magnetic cache pointers set for this image, then the IMAGE file (#2005) entry is updated, and the file is not purged. If no Tier 2 pointer is set, then a Tier 2 copy (JUKEBOX queue) is queued.
- If the image file in the VistA Imaging shares is not where the IMAGE file (#2005) specifies it to be, then the location pointed to by the IMAGE file (#2005) is checked. If a proper image file is found, then the redundant image will be otherwise purged.
- The image is next characterized as Patient Photo or non-Photo image for a patient by checking its image type. If so, the Photo ID/Advance Directive’s purge criteria parameters will be used in evaluating this image.
- If the image (a) is found to be at a Tier 1 location other than that specified by the IMAGE file (#2005) entry, or (b) is not found at an IMAGE file (#2005) alternate site, or (c) is confirmed of size non-zero on Tier 2, then the file will be removed from the VistA Imaging Tier 1 according to the purge criteria.

### Queue Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Failed and unprocessed queues are purged during the install procedures of the VistA Imaging System. Using the BP Edit\|Queue Manager\| *Queue Type* option on the main Background Processor form, one can update and manage queue file growth. After selecting a queue type and a queue status value, a list of the queues from eldest to most current will be shown with their status. The list will end at the current queue pointer. These reflect unprocessed (nil) and failed queues.

> The user has the option of requeuing, purging or saving them to a file. These records reflect requests to move files to and from Tier 2 with the exception of Abstract and Delete queues

> Normally, a site would not consider requeuing jukebox-to-hard disk copies (JBTOHD queue) as these files usually reflect old requests that, for the most part, will no longer be useful. The Tier 2 copies (JUKEBOX queue) may be requeued, however, the Purge process will automatically requeue those that are not currently archived on Tier 2

> Each queue task has an active queue pointer that designates the next entry to be processed. This queue pointer can be manually moved forward to begin processing at another location in the queue by using the Set Queue Partition context menu option within the BP Queue Manager. A typical situation may be when a queue entry is corrupted. Then the active queue pointer can be moved to the next entry where processing will continue with the rest of the queue entries for that task. (See the *Background Processor User Manual* for more details).

#### Server Size

Select View \| Server Size from the BP Queue Processor menu bar.

BP Queue Processor Server Size Submenu

![](vista-imaging-system-technical-manual/057.png)

> This window shows the amount of total space, free space and % Server Reserve space for Tier 1 and Tier 2 shares as well as RAID Groups.

GO Vista Storage Graphs

![](vista-imaging-system-technical-manual/058.png)

> The VistA Storage area on the Queue Processor GUI can be refreshed with the most current storage utilization statistics for RAID Groups and Tier 1 shares by clicking the buttons Refresh Current Write Group or Refresh All (Tier 1 Shares).

#### Background Processor: Open Log Functions Log Files

> New log files are created as HTML files at the beginning of every session. HTML files are viewable, printable, and searchable. By default, the BP Queue Processor log files reside in the following subdirectories:

- Queue Processor - C:\Program Files\VistA\Imaging\BackProc\log\BackProc
- Purge - C:\Program Files\VistA\Imaging\BackProc\log\purge
- Verifier - C:\Program Files\VistA\Imaging\BackProc\log\verifier

> You can access these files by selecting File \| Open Log on the BP Queue Processor menu bar and double-clicking the desired file.

> Note: The log files can also be imported into an Excel spreadsheet.

> Important: These files should be kept for historical/troubleshooting reasons and added to the tape backup process to safeguard the files. (See *Appendix B: Backups* in the *VistA Imaging System Installation Guide.*)

> <u>Log File Format</u>

> BP Queue Processor log files are archived as HTML files and have the year-month-day and sequence number imbedded in the file name, as shown in the right pane of the window in this example.

BP Queue Processor Log Files

![](vista-imaging-system-technical-manual/059.png)

> If more than one log file is created on the same day, the system appends a sequence number to the file name.

#### Queue Processor Log Files

> The Queue Processor produces multiple log files for a processing run. Each file contains different information.

- BackProc Log

> The BackProc.log file records all activity in the Event Log section in the Queue Processor window.

BackProc.log File Records

![](vista-imaging-system-technical-manual/060.png)

| Name        | Description                                               |
|-----------------|---------------------------------------------------------------|
| Date/Time       | Actual time when the IMAGE file (#2005) was processed         |
| Event_Queue_Ref | Queue name and entry number and status check info             |
| Message/Path    | Description of action taken (or statistics for status checks) |

- BP Error Log

> The BPError.log file records error conditions with the operating system and Broker.

BPError.log File Records

![](vista-imaging-system-technical-manual/061.png)

| Name        | Description                                       |
|-----------------|-------------------------------------------------------|
| Date/Time       | Actual time when the IMAGE file (#2005) was processed |
| Event_Queue_Ref | Error category                                        |
| Message/Path    | Description of error condition                        |

#### Verifier Log Files

> BP Verifier produces the following types of log files. For details on each log file, see the Verifier chapter in the *Background Processor User Manual*.

- Scan Log

> The Scan log file lists entries with potential file integrity problems. The log records the operational events that take place to correct a particular problem. They are used to determine if and how the Verifier corrected the faulty condition. The IENs that the Verifier could not fix are listed in the ScanError log file.

- NoArchive Log

> The NoArchive log file contains image file names that are missing on the jukebox and could not be created from existing files and/or could not be found on the RAID. The Verifier examines both the IMAGE file (#2005) and the IMAGE AUDIT file (#2005.1) for missing files. The 2005.1 column shown below indicates those missing files that have been deleted and the IMAGE file (#2005) record has been moved to the IMAGE AUDIT file (#2005.1).

- ScanError Log

> The ScanError log file lists problems with IENs that could not be corrected. When a Verifier scan is completed, the contents of this file are sent as a mail message to the MAG SERVER mail group.

- DFNError Log

> The DFNError log file displays integrity issues with patient data.

- VerifierdebugLog

> The Verifier debug information is only logged when an error occurs. After 30 errors, debug mode is turned off. By turning off debug mode, the size of the Debug Log is restricted to limit overwhelming the local hard drive with repetitive data.

#### Purge Log Files

> BP Purge produces the following types of log files. For details on each log file, see the Purge chapter in the Background Processor User Manual.

- Purge Log

> The Purge.html log file records the current share being purged as well as all of the successful deletions and the reason they were deleted.

- PurgeError Log

> The PurgeError.html log file records the current share being purged as well as all of the files that were not deleted and the reason they were not deleted.

#### Check Status of the JBTOHD Report

1.  On the Background Processor main menu, select the View \| JBTOHD Report option.
2.  Select File \| Refresh in the report window.

JBTOHD Report

![](vista-imaging-system-technical-manual/062.png)

> The JBTOHD queue display is sorted by the individual that queued the entry. It displays the number and types of queues. It displays the patient along with the queue Internal Entry Number (IEN) to facilitate advancing the queue pointer.

### Background Processor Configuration Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Configuring BP Servers Guidelines

- At least one BP Server must be present to perform utility functions such as copying image files to and from Imaging servers (the Tier 1 shares) and Tier 2.
- The software does not permit redundant task assignments of BP activities. For example, you cannot specify that more than one BP Server perform the JUKEBOX queue task.
- The JUKEBOX and DELETE queue tasks should run on the same BP server. If not, the DELETE queue may be processed in advance of the image being written to the Tier 2, and the DELETE queue will eventually fail. These failed queues must be re-queued.
- The IMPORT and ABSTRACT tasks must run on the same server. There will be occasional archived FULL files that do not have abstracts. If you see these ABSTRACT tasks failing, the JBTOHD task should be added to server running the IMPORT/ABSTRACT task. Please note the IMPORT can execute on a single server.
- If the Verifier and Purge are to be run on servers other than those running the Queue Processor tasks, a new BP Server must be configured for those tasks.
- When the PREFET task is added to the VistA Imaging Display workstation configuration, this activity task must be checked assigned on the BP Server configuration window in order to have these queue types processed.
- A directory can be created on the Tier 1 shares or remote storage location to archive BP log files for later reference.

#### Adding a BP Server to the VistA Imaging System

> Running multiple BP servers improves performance and redundancy by allowing the distribution of tasks, and allowing queues to be quickly reassigned in the event of a failure. Therefore, it is recommended that at least two BP servers be up and running. Though the facility may choose any server to host the BP (as long as the server meets the minimum requirements), an ideal location is directly on the two Image Cluster nodes.

#### To Set Up a BP Server Application

1.  From the BP Queue Processor menu bar, select Edit \| BP Servers.

BP Server

![](vista-imaging-system-technical-manual/063.png)

> The BP Server Parameters window enables you to create a unique server name for a server and assign tasks to that server. The properties on these servers enable you to specify the location of the log files for all applications on each BP Server and the file’s size limit (described in “*Specifying the Log File Location and* Size” in the *BP User Manual.)*

BP Server Parameters

> ![](vista-imaging-system-technical-manual/064.png)

2.  Click the Add New BP Server button at the bottom of the tree pane.
3.  In the BP Server Add dialog box displayed, enter a logical name for the BP Server such as BP1.

> Note: The name must be at least three characters in length and can contain alpha and numeric characters and must be unique. Once the name is saved, it cannot be renamed. It can only be deleted when all the tasks assigned to it are removed.

BP Server Add

![](vista-imaging-system-technical-manual/065.png)

> If the name is not valid, an error message is displayed. You can correct the name and repeat the steps.

#### Assigning Tasks (Queues) to a BP Server

> By default, no tasks are assigned to BP Servers. The tasks will need to be assigned in order for that function of the BP software to operate. You can assign tasks based on the needs of your facility. As previously mentioned, a queue name identifies the task that the Queue Processor performs. All queues are available for you to assign to a BP Server, except EVAL.

> Note: You should assign Purge as well as the Scheduled Verify to BP Servers. These features help maintain the system’s free-space and integrity without operator intervention.

> Drag and drop a task from the Unassigned Tasks in the tree pane (shown) to the server that is designated to run that task.

BP Server Parameters

![](vista-imaging-system-technical-manual/066.png)

> Note: The priority of tasks running on the same server is set internally and cannot be changed. The functions of each task are:

1.  JBTOHD - populates the Tier 1 shares with images that have been deleted from Tier 1 through the Purge function.
2.  PREFET - populates Tier 1 with images that were requested based on VistA Imaging Display workstation configuration parameters.
3.  ABSTRACT - creates ABS derivative thumbnail files from FULL/BIG files when the file type is missing on Tier 1 and Tier 2.
4.  IMPORT - provides a means for external applications to archive images in the VistA Imaging environment.
5.  JUKEBOX - copies images to the long-term archival storage device
6.  DELETE - removes images from Tier 1.
7.  GCC - exports images to a share that is external to the local VistA Imaging network.
8.  PURGE – This assignment includes both the auto purge and the scheduled purge tasks. Refer to the purge section of this document for more details.
9.  SCHEDULED VERIFY – automatically runs the Verifier at the assigned time to check the integrity of the Image records in VistA with the file locations on Tier 1 and Tier 2 storage. Only the most recent unchecked IENs are verified.

> Click Apply to save the changes or OK to save the changes and exit.

#### Removing a BP Server from the VistA Imaging System

1.  From the Queue Processor menu bar, select Edit \| BP Servers.
2.  In the tree pane, right-click the server name and select Delete BP Server from the popup menu displayed.

> Note: This popup menu can also be accessed from the keyboard by using Shift + F10.

BP Servers

![](vista-imaging-system-technical-manual/067.png)

> The selected BP Server is removed from the tree pane.

> Note: This same name can be added later.

#### Specifying the Log File Location and Size

1.  Click a BP Server name in the tree pane and select Server Properties from the popup menu displayed.

> Note: This popup menu can also be accessed from the keyboard by using Shift + F10.

BP Servers

![](vista-imaging-system-technical-manual/068.png)

> The BP Server Properties dialog box is displayed.

BP Server Properties

![](vista-imaging-system-technical-manual/069.png)

2.  Enter the size in megabytes in the Log File Size field. The default log file size limit is 2 MB.
3.  Specify the Network Log file location on a local machine or a remote network location.

> Note: By default, the log files are created on the local drive in the directory Program Files\VistA\Imaging\BackProc\Log. If a remote network location is entered, the Background Processor must have Read and Write access to it. Use the \\computer name\share name format and do not use a letter drive for the remote network location.

4.  Click OK to save the information and close the window.

#### Background Processor Purge Configuration

> The BP Purge / Verifier / RAID Group Advance Settings window is used for setting up the Scheduled Verifier, Scheduled Purge, and RAID Group Advance activities. In addition, the parameters for the Purge activity are set up through this window.

> Selecting the Edit \| Purge / Verifier / RG Settings menu in the Queue Processor window opens the BP Purge / Verifier / RAID Group Advance Settings window.

BP Purge/ Verifier /RAID Group Advance Settings

> ![](vista-imaging-system-technical-manual/070.png)

#### Purge Settings

> The Purge process is used to remove image files from Tier 1when the free space is low or when older and/or not recently viewed image files can be purged to allow room for newly acquired images. It is important to note that no file is purged from Tier 1 shares if it has not been verified and confirmed as saved on Tier 2.

> The Purge can be run manually in standalone mode or as a part of the Queue Processor. The Purge Parameters are used to control the purge activities in auto, manual and scheduled modes.

#### Guidelines for Setting Retention Days on Files for the Purge

> General guidelines:

- Determine the span of dates of images that will be preserved on the Imaging shares.
- The shorter the timeframe, the more space will be free on Tier 1 when the purge completes.
- Multiple purges may be required to determine the retention days. It is advisable to start with one share with a large retention days value.
- Not all sites capture all the file types specified in the parameter list (e.g. BIG, Photo ID).
- If the frequency and the results of purging are acceptable, then it is not advisable to change the Purge values.
- If there is still not enough free space after the purge, decrease the Retention Days in Purge Parameters (BIG and FULL files, in particular) and repeat the purge until the desired free space is obtained.

> Factors that determine the best set of purge parameters for an individual site are:

- The frequency of purges
- The volume of image acquisition rate
- The volume of image file retrieval
- The use of Pre-Fetch
- The capacity of disk space for VistA Imaging Tier 1 shares

> Some sites have extended their Tier 1 capacities and are able to maintain five or more years of images on the shares. These sites may only need to purge once per year to purge off the latest year of images (year 6). Others who have smaller Tier 1 sets have to purge more frequently and can only have a limited amount of images on their shares.

> For your site, strive to keep the shares between 80% and 90% full (or between 10% and 20% free space). When the Purge process completes and the resulting free space is in excess of this values, then adjust the parameters accordingly.

#### Configuring the Retention Days Settings

Retention Days Configuration Settings

![](vista-imaging-system-technical-manual/071.png)

Retention Days and Retention Dates box

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field or Checkbox</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Full Files</td>
<td><p>Source: Images from the DICOM Gateways, Clinical Capture workstations and Imports</p>
<p>File extensions: 756,ASC,AVI, BMP,BW,DCM, DOC, HTM, HTML, JPG, MHT, MHTML, MP3, MP4, MPEG, MPG, PAC, PDF, RTF, TGA, TIF, WAV</p>
<p>Range: 0 - 99,999 (number of days back from the current date that files should be retained)</p></td>
</tr>
<tr class="even">
<td>Big Files</td>
<td><p>Source: Images from the DICOM gateway and Clinical Capture workstations.</p>
<p>File extensions: BIG</p>
<p>Range: 0 - 99,999 (number of days back from the current date that files should be retained)</p></td>
</tr>
<tr class="odd">
<td>Abstract Files</td>
<td><p>Source: Images from the DICOM gateways, Clinical Capture workstations and Imports. Abstract files are derivatives of the TGA/BIG format files.</p>
<p>File extensions: ABS</p>
<p>Range: 0 - 99,999 (number of days back from the current date that files should be retained)</p></td>
</tr>
<tr class="even">
<td>Photo IDs/Ad Direct</td>
<td><p>Source: Source: Patient photo images and Advance Directives from the Clinical Capture workstations.</p>
<p>File extension: JPG</p>
<p>Range: 0 - 99,999 (number of days back from the current date that files should be retained)</p></td>
</tr>
</tbody>
</table>

1.  Enter the number of days that each of the four file types above should remain on the shares based on the purge date criteria in the section *Configuring Purge Date Criteria Settings.*

> Note: The FULL and BIG files are typically larger file sizes and consume more free space on the shares than the abstracts and photo IDs and Advance Directives.

2.  As a result of different file type sizes, set fewer retention days for the larger file to free more space.
3.  Because the abstracts and photo IDs are smaller files, set the retention days for purging these two types of files to a higher value than the values for the FULL/BIG file retention days. Also, the availability of Photo IDs and Advance Directives on Tier 1 has a great impact on patient care.
4.  Because the abstract files are viewed as thumbnails on the Clinical Display workstation, set the retention days to retain a minimum of 5 years (1,825 days) on the shares regardless of the capacity of the Tier 1 to make viewing on the Clinical Display workstations more efficient.

#### Configuring Purge Date Criteria Settings

Purge Criteria Selection

![](vista-imaging-system-technical-manual/072.png)

| Purge Criteria |                                                                                                                   |
|--------------------|-------------------------------------------------------------------------------------------------------------------|
| Date Accessed      | Date when the file (image) was last viewed on a VI workstation                                                    |
| Date Created       | Date when the file was copied to the current disk share                                                           |
| Date Modified      | Date when the file was last changed. On the initial save, the Date Created will be the same as the Date Modified. |

> Any of the three file date/times can be used (date accessed, date modified, date created) to purge the shares. There have been instances where third party utilities have changed the access dates on all the files it “touched” to the same recent date.

> When the purge is activated, no files are deleted as none of the file access dates are purge candidates. It is recommended that the Date Modified be used. This date is retained when files are moved across storage media and is a reliable date for purging.

Configuring Scheduled/Express Purge Settings

![](vista-imaging-system-technical-manual/073.png)

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field or Checkbox</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Auto Purge</td>
<td><p>Enables the Purge to run when the high water mark is reached on a RAID Group.</p>
<p><strong>Important</strong>: Auto Purge should always be enabled.</p></td>
</tr>
<tr class="even">
<td>Last Purge BP Server</td>
<td>BP Server on which the last purge was run</td>
</tr>
<tr class="odd">
<td>Purge Factor</td>
<td>Multiple of the % Server Reserve (found on the Imaging Site Parameters window). When the free space falls below value of the % Server Reserve times the purge factor, a purge is initiated on the next available online RAID Group. The default value of the purge factor is 2.</td>
</tr>
</tbody>
</table>

> Express Purge Section

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field or Checkbox</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Active</td>
<td>Enables an Express Purge</td>
</tr>
<tr class="even">
<td>Purge Rate</td>
<td><p>When the number of image entries that have been evaluated for purging (based on the date criterion), without deletion, the purge process for that share will cease.</p>
<p>The default Purge Rate value is 100,000.</p></td>
</tr>
</tbody>
</table>

> Scheduled Purge Section

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field or Checkbox</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Active</td>
<td>Enable scheduled purges</td>
</tr>
<tr class="even">
<td>Last Purge Date:</td>
<td>Date when the last purge was run</td>
</tr>
<tr class="odd">
<td>Frequency (in days)</td>
<td><p>The number of days added to the Last Purge Date to determine the next Scheduled Purge Date.</p>
<p>If this field is left blank, the Scheduled Purge can be scheduled for a single event. When the event takes place, the Next Purge Date is cleared.</p></td>
</tr>
<tr class="even">
<td>Next Purge Date</td>
<td>Next scheduled Purge date</td>
</tr>
<tr class="odd">
<td>Purge Time</td>
<td>Time of day for the next scheduled Purge</td>
</tr>
</tbody>
</table>

> Note: Before an automatic purge is set up, a manual purge should be run on a share to make sure the Purge Parameters are set properly.

> The automatic purge will use these same Purge Parameters and if not set properly, will result in unsatisfactory results. As the volume of images increases from the gateways, etc., these parameters should be adjusted to compensate for the increase.

> Scheduled purges typically are set up on a monthly basis, but this will vary per site. The goal is to keep the shares between 80% and 90% full. Some adjustments in scheduling will need to be made after a scheduled purge cycle has completed.

> Enabling Express Purge will greatly enhance the purging process by eliminating unnecessary file traversals that are not candidates for purging and thus significantly decrease the time to purge a share. The Purge Factor is set to control when the purge on a share is terminated.

> When the number of files that are traversed and not deleted has exceeded the number in the Purge Factor, the purge stops on that share and begins purging the next share (automatic mode).

#### Network Location Manager: Adding a New Tier 1 or Tier 2 Storage Location and other Storage Types

> Note: The following procedure applies to all the tabs in the Network Location Manager window.

1.  From the Queue Processor menu bar, select Edit \| Network Location Manager to open the following window.

Network Location Manager

![](vista-imaging-system-technical-manual/074.png)

> The Tier 1 tab is automatically selected.

2.  To add a new network location, click the New button at the bottom. The Network Location Properties window will be displayed.

Network Location Properties Blank

![](vista-imaging-system-technical-manual/075.png)

3.  Type the Share Name.
4.  At the Network Share field, either type the path to the location where images are to be stored, or click the browse (…) button and specify the path.
5.  Select the appropriate option at the Storage Type field.
6.  Click Apply.

> Additional fields relevant to the storage type are displayed. The example below is for Storage Type RAID only.

> Note: The STORAGE TYPE field is preselected depending on the Network Location tab selected. If the EKG tab is selected, then the STORAGE TYPE will be set to EKG, and so forth. However, the preselected value can be modified.

Network Location Properties Filled In

![](vista-imaging-system-technical-manual/076.png)

7.  Leave the Operational Status check box selected by default setting, or clear it.
8.  Leave the Read Only check box cleared by default setting or select it.
9.  Click Apply to add the changes to the database or click OK to add the changes and exit.

#### Background Processor Imaging Site Parameters Edit Functions Imaging Site Parameters Window

> The Edit \| Imaging Site Parameters menu on the Queue Processor menu bar opens the Imaging Site Parameters window used to modify and save parameters in the VistA database. Each of the boxed areas in the window is described below.

Imaging Site Parameters

![](vista-imaging-system-technical-manual/077.png)

Administrative Settings

![](vista-imaging-system-technical-manual/078.png)

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field or Checkbox</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Current Namespace</td>
<td><blockquote>
<p>Each VHA facility has its own unique 3-character designator. The Current Namespace file is used to store this 3 letter facility designator. It is used in Imaging as the first 3 characters of the 14-character name given to image files captured at this site. The VistA Imaging development and support teams maintain a central database with each sites 3 letter designator. The Current Namespace field is not configurable. This is necessary to ensure that image file names across VHA are unique.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Tier 1 Write Location</td>
<td>All images from the gateways, Capture, etc. will be written to this share. The selected Current RAID Group determines which shares are listed on this dropdown list.</td>
</tr>
<tr class="odd">
<td>Generic Carbon Copy</td>
<td>Remote share where files will be exported. The share permissions must match the login credentials for the BP Server.</td>
</tr>
<tr class="even">
<td>Current RAID Group</td>
<td>The current active RAID Group includes the Tier 1 Write Location (described above). When new images are processed, they are stored on the Tier 1 Write Location share within this group. The RAID Groups are set up with the Network Location Manager.</td>
</tr>
<tr class="odd">
<td>Import Queue Security</td>
<td>Checks users Imaging security keys for permission to capture images</td>
</tr>
<tr class="even">
<td>Site Code</td>
<td>Three-letter acronym for the site location. This is used for AutoRouting and MUSE.</td>
</tr>
<tr class="odd">
<td>Associated Institutions</td>
<td><p>This set of institution values will allow users from other institutions to access local images.</p>
<p><strong>Note</strong>: Right-clicking this field displays an Add/Delete popup menu that can also be accessed from the keyboard by using Shift + F10.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field or Checkbox</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VistARad Grouping</td>
<td><p>The radiologist can lock/interpret exams for other divisions (including the Parent Institution or other Associated Institutions), when those divisions are included in this set of institutions. Note that this setting controls exam locking and updating, as well as filtering of the UNREAD Exams lists to show only the Institutions that are defined here.</p>
<p><strong>Note</strong>: Right-clicking this field displays an Add/Delete popup menu that can also be accessed from the keyboard by using Shift + F10.</p></td>
</tr>
</tbody>
</table>

Storage Functions Settings

![](vista-imaging-system-technical-manual/079.png)

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field or Checkbox</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Tier 2 Write Location</td>
<td>Tier 2 share where newly acquired images are currently being written.</td>
</tr>
<tr class="even">
<td>% Tier 1 Reserve</td>
<td>The purpose of the reserve is to provide a significant amount of reserved primary storage to allow time for corrective action to create more space on the shares. Enter an integer between 1 and 50.</td>
</tr>
<tr class="odd">
<td>% Tier 2 Reserve</td>
<td>The default value is 5%. The values can be set in the range 0- 50%. When the allocated space does not meet this watermark, then no JUKEBOX queues will be processed and Tier 2 retrieval requests may be compromised, depending on the Tier 2 technology.</td>
</tr>
<tr class="even">
<td>Auto Write Location Update</td>
<td><p>At the interval of every 20 minutes or 100 images written to a share, the Queue Processor will determine which share within a group has the most space and will use that share as the current write location for newly acquired images.</p>
<p>To manually select a Tier 1 Write Location, uncheck the Auto Write Location Update box. Images will be written to the selected Tier 1 share until it is filled or manually changed to another share.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field or Checkbox</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Multiple Namespace</td>
<td><p>List of all the legacy namespaces that have been used at a site and are reflected in the filenames on the Tier 1 and Tier 2 shares. <strong>Note</strong>: Right-clicking this field displays an Add/Delete popup menu that can also be accessed from the keyboard by using Shift</p>
<p>+ F10.</p></td>
</tr>
<tr class="even">
<td>File Types</td>
<td><p>File extensions outside of the standard extensions that the BP products will recognize and treat as a standard extension file. <strong>Note</strong>: Right-clicking this field displays an Add/Delete popup menu that can also be accessed from the keyboard by using Shift</p>
<p>+ F10.</p></td>
</tr>
</tbody>
</table>

TeleReader

![](vista-imaging-system-technical-manual/080.png)

| Field or Checkbox | Description                                                                                                                                                                                                    |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NET SITE SERVICE      | The web service used by Remote Image Views to gain access to remote sites                                                                                                                                          |
| Timeout TeleReader    | The number of minutes that the TeleReader application will remain active before closing due to inactivity. If this field is undefined, the application will not timeout. Max value is 999999, no decimals allowed. |

Clinical Workstation Settings

![](vista-imaging-system-technical-manual/081.png)

| Field or Checkbox   | Description                                                                                                                            |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Use Capture Keys        | Check users’ Imaging security keys for permission to capture images.                                                                       |
| Timeout Windows Display | Number of minutes until the Imaging Display application will close due to inactivity. The default setting is 120 minutes (Range 6 to 600). |

| Field or Checkbox   | Description                                                                                                                                     |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Timeout Windows Capture | Number of minutes until the Imaging Capture application will close due to inactivity. The default setting is 120 minutes (Range 6 to 600).          |
| Timeout VistARad        | Number of minutes until the Imaging VistARad application will close due to inactivity. There is no default setting.                                 |
| Default MUSE Site       | MUSE site number that the Imaging Display application will connect to. Site numbers are usually 1, 2, 3, …. If left empty, the field defaults to 1. |
| Default User Preference | A specified user’s parameter settings will be used for first-time users of the Imaging system.                                                      |

Service Accounts Settings

![](vista-imaging-system-technical-manual/082.png)

> These credentials are shared between the DICOM Gateway, Image cluster, Jukebox Server, and Background Processor.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field or Checkbox</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Windows Username</td>
<td>Imaging Administrator domain Service Account (IA Account) used to access the Imaging shares on the RAID and archive (jukebox) share. Both the RAID and archive (jukebox) shares must have READ/WRITE permission to this account.</td>
</tr>
<tr class="even">
<td>Windows Password</td>
<td>Domain password used to access the Imaging shares on the RAID and archive (jukebox) share.</td>
</tr>
<tr class="odd">
<td>VistA Access</td>
<td><p>Encrypted access code for the Imaging Service Account in VistA. This account will be used to automatically re-log into the application when there is a loss of connectivity between the BP product and the Broker (VistA).</p>
<p><strong>Note</strong>: The Imaging Service Account must have the MAG SYSTEM security key and secondary menu option MAG WINDOWS. The VERIFY CODE never expires. This user must have a single division designation.</p></td>
</tr>
<tr class="even">
<td>VistA Verify</td>
<td>Encrypted verify code for the Imaging Service Account in VistA. This account will be used to automatically re- log into the application when there is a loss of connectivity between the BP product and the Broker (VistA).</td>
</tr>
</tbody>
</table>

DICOM Interface Settings

![](vista-imaging-system-technical-manual/083.png)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field or Checkbox</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DICOM Gateway Write Location</td>
<td>RAID share where newly acquired images are currently being written.</td>
</tr>
<tr class="even">
<td>DICOM Gateway Interface Switch Update</td>
<td>Indicates presence of a DICOM Gateway on the system.</td>
</tr>
<tr class="odd">
<td>Retention Days HL7 – Modality Work Lists</td>
<td><p>This field is used as the default value, in days, by the DICOM Text Gateway for three different user menu driven purges:</p>
<ul>
<li><p>This field is used by the Purge Old Modality Worklist Entries menu option to determine the number of retention days from the date of creation of Modality Worklist Entries.</p></li>
<li><p>This field is used by the Purge Old DICOM Message Files menu option to determine the number of retention days from the date of creation of DICOM messages that were sent to commercial PACS.</p></li>
<li><p>This field is used by the Purge Old HL7 Transaction Global Nodes menu option to determine the number of retention days from the date of creation of HL7 messages sent from VistA to the DICOM Text Gateway.</p></li>
</ul>
<p><strong>Note</strong>: This value may be overridden by the user when executing any of these menu options.</p></td>
</tr>
<tr class="even">
<td>% Free Space DICOM Messages</td>
<td>Minimum percentage of free disk space for DICOM HL7 messages on the text gateway. A typical value is 25%.</td>
</tr>
<tr class="odd">
<td>Retention Days DICOM Messages</td>
<td>Number of days to retain DICOM HL7 messages on the text gateway, 30 days is recommended.</td>
</tr>
</tbody>
</table>

#### Scheduled BP Verifier

> The Scheduled Verifier should be set up to run nightly. It will verify the integrity of any image records not validated since the previous Verifier run (Manual or Scheduled). It is suggested that the Verifier be run manually over the entire range of image records before incremental Verifier runs are started. The application that runs for the Scheduled Verifier is the same as the Manual Verifier. Reference the Manual Verifier in the BP User Manual for specific information about the GUI and log files.

#### Guidelines for Setting Parameters for the Scheduled Verifier

> The following guidelines for using the Scheduled Verifier will help maintain the integrity of the Imaging records in the VistA database.

> Important: If the PC that has Scheduled or Auto events is not a server class, the task will not start.

- Set the Active check box to enable scheduled runs of the BP Verifier. The scheduled runs of the Verifier will only check the most recent VistA records of new images that have been created since the last Scheduled Verifier run.
- Do not select the Check Text Files check box. The contents of the text files on Tier 1 will be compared to the information in VistA. This processing will slow down the Verifier processing and utilities are not available at the present time to correct any issues that surface.
- The Last Verifier Date field is set by the system and cannot be set by the user.
- When the Active parameter is checked, the Frequency (in days) field setting should be 1 so that the Verifier runs daily.
- Initially set the Next Verifier Date to today’s date. The scheduling frequency will be based on this date.
- Set the Verifier Time to an inactive period of the day –typically after hours when image creation activity is low.

Description of the Scheduled Verifier Settings

![](vista-imaging-system-technical-manual/084.png)

| Field or Checkbox | Description                                                                 |
|-----------------------|---------------------------------------------------------------------------------|
| Last Verify BP Server | BP Server on which the Verifier was last run (Display only, set by application) |

#### Scheduled Verifier

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field or Checkbox</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Active</td>
<td>Enables scheduling the Verifier</td>
</tr>
<tr class="even">
<td>Check Text Files</td>
<td><p>Read text files on Tier 1 and determine if:</p>
<ol type="1">
<li><blockquote>
<p>the file is binary or unreadable</p>
</blockquote></li>
<li><blockquote>
<p>there are unprintable characters in the file</p>
</blockquote></li>
<li><blockquote>
<p>The SSN does not match the one in VistA</p>
</blockquote></li>
<li><blockquote>
<p>SOP Instance UID mismatch with VistA</p>
</blockquote></li>
<li><blockquote>
<p>Study Instance UID mismatch with VistA</p>
</blockquote></li>
<li><blockquote>
<p>SOP Instance UID and/or Study Instance UID are blank</p>
</blockquote></li>
<li><p>SSN in the top part of the text file does not match the bottom.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>Frequency (in days)</td>
<td>Number of days added to the date of the last time the Verifier application ran to determine the next time the Scheduled Verifier should be run.</td>
</tr>
<tr class="even">
<td>Last Verifier Date</td>
<td>Date when the Verifier was last run</td>
</tr>
<tr class="odd">
<td>Next Verifier Date</td>
<td>Date of the next scheduled Verifier will run based on the Frequency (in days) parameter</td>
</tr>
<tr class="even">
<td>Verifier Time</td>
<td>Time of day when the Verifier will run</td>
</tr>
</tbody>
</table>

#### Setting Up the Scheduled Verifier

> Use the guidelines above to set up the Scheduled Verifier.

1.  Select Edit \| BP Servers.
2.  Drag the SCHEDULED VERIFY task on the BP Server to the location where the Verifier is to be run.
3.  Click OK to close the window.
4.  Select the Edit \| Purge / Verifier /RG Settings tab.
5.  Set the following fields in the Scheduled Verifier box:

| Field           | Setting                                               |
|---------------------|-----------------------------------------------------------|
| Active              | Checked                                                   |
| Check Text Files    | Unchecked                                                 |
| Frequency (in days) | 1                                                         |
| Next Verifier Date  | (starting date)                                           |
| Verifier Time       | (time of day the Verifier will run – after hours is best) |

#### Scheduled RAID Group Advance

> The RAID Group Advance is configured on the Imaging Site Parameters window. RAID groups are used to organize Tier 1 shares into logical groups for easy tape backup and restore processing. During the install, all existing online Imaging shares are placed into the first RAID Group, RG-XXX1. This configuration is the same and has been in existence for past years. The Auto Update functionality is also the same. At regular intervals, the current write location will change to the share with the most free space. The Auto-Write function will reset the current write location to provide load balancing within the RAID group. When the % Server Reserve within the group has been reached, the Auto-Write will set the next RAID group as the current write group. In addition, when the used space in that RAID group has reached the high water mark, the next RAID Group that has online shares will become the current RAID group.

#### Guidelines for Setting Parameters for the Scheduled RAID Group Advance

> Sites can choose a configuration that suits them best, as follows:

- Use the initial configuration where all the shares are in the same RAID Group. The new images will be evenly distributed among all the shares.
- Nightly incremental tape backups, as well as monthly/quarterly tape backups, must be done on a regular basis on all the shares.
- Distribute the shares among multiple RAID Groups. Fill the shares in each group to the Server Size, and then switch the current write group to the next. New image files will be distributed over all the shares assigned to that group.
- Nightly incremental tape backups, as well as monthly/quarterly tape backups, must be done only on that RAID Group.
- When the RAID group has reached capacity, a final full backup should be done on all of that RAID group’s shares. Nightly incremental tape backups and monthly/quarterly tape backups should be started on the next current write group.

Scheduled RAID Group Advance Settings

![](vista-imaging-system-technical-manual/085.png)

| Field or Checkbox | Description                                                                                                                                                                                                                                                                              |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Active                | Enable RAID Group Advance scheduling                                                                                                                                                                                                                                                         |
| Last RAID Advance     | Date when the last scheduled RAID Group Advance occurred                                                                                                                                                                                                                                     |
| Frequency (in days)   | Number of days added to the date of the last RAID Group Advance to determine the next time the RAID Group Advance will run. If the Frequency parameter is set, the next RAID Group Advance will be scheduled automatically. If the frequency is not set, no automatic scheduling will occur. |
| Next Advance Date     | Date of the next scheduled RAID Group Advance                                                                                                                                                                                                                                                |
| Advance Time          | Required. Time of day of the next scheduled RAID Group Advance                                                                                                                                                                                                                               |

#### Setting Up the Scheduled RAID Group Advance

> This option is applicable when the there are multiple active RAID Groups. Use the guidelines above to set up the Scheduled RAID Group Advance.

1.  Select the Edit \| Purge / Verifier /RG Settings tab.
2.  Set the following fields in the Scheduled RAID Group Advance box:

| Field           | Setting                                                                                      |
|---------------------|--------------------------------------------------------------------------------------------------|
| Active              | Checked                                                                                          |
| Frequency (in days) | Set by determining how long a span of time images will be written to a set of shares in a Group. |
| Next Advance Date   | Set the starting date when the system will move to the next RAID Group.                          |
| Advance Time        | Set the starting time of day when the system will move to the next RAID Group.                   |

3.  Click OK to close the window.
4.  Click Start on the Queue Processor main window.

> (A Queue Processor must be in the running state in order for the RAID Group Advance to run on the designated server.)

### Background Processor Image and File Entry Verifier

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Background Processor Image and File Entry Verifier submenu

![](vista-imaging-system-technical-manual/086.png)

> As a separate executable, it is necessary to launch the Verifier application from the Programs menu, unless you set up a desktop shortcut. The executable is installed by default in the program files/vista/imaging/backproc subdirectory.

> The process examines each non-group entry within the selected range of IMAGE file (#2005) entries. It searches each network magnetic and jukebox share indicated by each IMAGE file (#2005) entry for all extensions of the indicated filename. For each, it does the following:

- When more than one Tier 2 share contains images of the same file name, the Verifier will aggregate those files on a current Tier 2 Write location. It will update the JB references in the IMAGE file (#2005) entry and IMAGE AUDIT file (#2005.1) entry. The Activity column of the Verifier will display this activity as “Aggregate”.
- If any extension of the image file is missing from the referenced Tier 2 share and is both referenced and available on the VistA Imaging Shares, then the Verifier will copy it to Tier 2 and update the appropriate Tier 2 IMAGE file (#2005) references.
- If the VistA Imaging Shares references in the IMAGE file (#2005) entry are not accurate and the appropriate files are available at another network location, then the VistA Imaging Shares references are updated.
- If there is no TGA or ABS file on the network, but a BIG file exists, then the Verifier will create the missing file(s) at the current network write location, aggregate it to the Tier 2, and update the image file jukebox references.

### Imaging Server and Jukebox Backup Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Sites should establish weekly and daily schedules for backing up images from the VistA Imaging network servers and Tier 2 unit(s). A copy of the backed up media should be kept off site. Full backups and incremental backups are recommended. For further information, refer to the “Backups” section of Appendix B of the *VistA Imaging System Installation Guide*.

### DICOM-related Backup and Purge

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> As the software in the VistA Imaging DICOM Gateway is being used, information is created and stored. If left alone, this information would accumulate in an unbounded fashion and would eventually exceed any reasonable storage capability.

> A number of entities are purged automatically as the software is being used, based on retention parameters that can be set using the software itself.

> The storage of images takes a lot of space, and, as a result, images are typically only stored temporarily on the magnetic disks that are connected to the various workstations and servers. For long-term storage, images are typically copied to a jukebox, and then removed from their temporary cache storage.

#### Growing entities

> The VistA Imaging software creates the following entities:

- Image files (pixel data) temporarily stored on VistA magnetic cache servers
- Image Background Queue (^MAGQUEUE(2006.03,i,…))
- Modality Worklist Entries (^MAGDWLST(2006.56, i, …) )
- DICOM and PACS Messages (^MAGDHL7(2006.5,i,…))
- DICOM Failed Images (^MAGD(2006.575,i,…))
- DICOM Incomplete Images (^MAGD(2006.593,i,…))
- DICOM Error Log (^MAGD(2006.599,i,…))
- Error log on DICOM Gateways

#### Tier 2 Archive

#### File Migration

> As a part of normal procedure, captured images are copied to long term storage. The process that copies these files observes the following rules:

- Long-term storage media should be non-rewritable optical media.
- Overwrites are not allowed.
- All image-related files (“Full”, “Big”, and “Abstract”) are copied to Tier 2.
- Site-specified additional file types are copied to Tier 2. (“TXT” is part of the default install setting).
- If a file copy fails, additional attempts are made to copy the file. This is controlled by a site parameter whose default is three attempts.

#### Removing Jukebox Media - Offline Images

> The VistA Imaging System is capable of tracking images on platters that have been removed from the jukebox. This is sometimes necessary when all platters in all of slots in the jukebox are full, and a new jukebox has not been purchased or installed. Some sites use this option to archive platters on a first in, first out manner instead of buying additional hardware. By removing a platter, the images on the platter are marked offline. The clinical display software will display an “Archived Image” abstract (thumbnail) for any offline images. If the user clicks on the abstract, a message-box will appear with offline image and associated platter information. If the user chooses to view that image, they can notify an imaging system manager so the platter can be put back into the jukebox. System Managers can also be notified automatically with an email message whenever an offline image is accessed. The OFFLINE IMAGE TRACKERS mail group is installed on the system during the VistA Imaging KIDS installation. System managers that would like to receive notifications should add themselves to the mail group. The procedure below outlines the steps necessary to track offline images.

> Note: See the *Storage Utilities User Manual* for the procedure to remove jukebox media.

#### Taking Images Offline

1.  Go to DEX Administrator.
2.  Click on View \| Reports, then choose Media Files.
3.  Click Next.
4.  Select the media (platter) that will be taken offline. (Multiple select is allowed)
5.  Click Finish.
6.  When the report is available, save it to a file (use Save As) - Be sure to save as type Text (\*.txt)
7.  Move file to VistA System (ftp; use ASCII mode, not binary mode)
8.  Run M option MAG JB OFFLINE (shown below); this procedure will require a FileMan access of “@”.

To Check Which Platters are Offline

![](vista-imaging-system-technical-manual/087.png)

![](vista-imaging-system-technical-manual/088.png)

To Put Images Back Online

![](vista-imaging-system-technical-manual/089.png)

#### Purge Image Files from VistA Magnetic Cache Manually

> The Background Processor Purge software purges image files from the VistA Magnetic Cache, depending upon certain criteria set by the site.

> To manually operate this software:

1.  From the Windows Start \| All Programs menu, select VistA Imaging Programs \| Background Processor \| Purge.

Background Processor Purge software

![](vista-imaging-system-technical-manual/090.png)

> The display box in the upper left quadrant shows the files that will be purged and the date of last access by user application. All listed items are captured in the current Purge.log file. The display is cleared after every 50 items to conserve application memory.

2.  To select a subset of image shares for purging, select Edit \| Select Shares. The Purge Share Select window displays the shares.

Purge Share Select Window

![](vista-imaging-system-technical-manual/091.png)

3.  Select the share(s) to be purged and click OK.
4.  Review the Purge parameters and share selection on the Purge window.
5.  In the Purge application, click Start and OK in the confirmation message displayed.

> The Activities display (immediately below the start button) shows the time of execution and gives running totals for the VMC files evaluated, the number purged, and the number that were queued to be copied to the Jukebox (JB) because they could not be confirmed on the jukebox.

> The Share Processing display lists each online, non-routed, magnetic type share in the NETWORK LOCATION file (#2005.2). These are input values for each step of the purge process and they are appended with a Purged status as they are successfully processed.

> The two graphical displays reflect the runtime categorization of image files evaluated and purged as the purge process progresses. Note that the vertical axis units change over the processing period. Also, the units tend to differ between the two graphs.

> Steps in the purge process are:

1.  The processor initially gets the information from VistA including site parameters governing file aging criteria and online magnetic file server shares.
2.  The hierarchical directory structures on each imaging server share are traversed. For each file in each directory, the date of last access is compared against the VistA site file aging criteria for that file type.
3.  Files meeting VistA purge criteria are removed from the Imaging magnetic server share, and the IMAGE file (#2005) is updated in the VistA database to indicate the current Tier 2 Write location of the files on the Tier 2.
4.  If the image file being evaluated resides on an imaging server share other than the one indicated in the IMAGE file (#2005) in the VistA database, then the file on the unreferenced share is purged regardless of the date of last access as long as the file is present at its referenced location.
5.  If there is no corresponding IMAGE file (#2005) entry in the VistA database for this file, the file is purged regardless of age criteria.
6.  If the IMAGE file (#2005) in the VistA database is synchronized with the Tier 1, but there is no reference to the file’s location on the Tier 2 then a Tier 2 copy is queued and the file is left in place on the Tier 1 share.
7.  A site parameter exists for evaluating radiology image files to be held regardless of age if the specific file is related to a radiology package entry with the “NOPURGE” node set.

> Note: A monthly verification process may be added to validate the file server references in the IMAGE file (#2005) in the VistA database.

#### Entities That Are Purged at the Discretion of the Site Supervisor

#### Purge Old Modality Worklist Entries

> Old entries may be purged by selecting the option “Purge old Modality Worklist Entries” from the “Text Gateway” menu.

> The subroutine that is called for this menu-option (ENTRY^MAGDDEL1) removes entries in

> ^MAGDWLST(2006.55,…) that were time-stamped more than a certain number of days (the default is the number of days specified in ^MAGDICOM(2006.563,1,"DELETE DAYS")) before the current date.

#### Purge Old DICOM Message Files

> Old files and directories may be purged by selecting the option “Purge old DICOM message files” from the “Text Gateway” menu.

> The subroutine that is called for this menu-option (DICOM^MAGDDEL2) removes files and directories that were time-stamped more than a certain number of days (the default is the number of days specified in ^MAGDICOM(2006.563,1,"DELETE DAYS")) before the current date.

> Names of directories that may play a role in this context are stored in

> ^MAGDICOM(2006.563,1,"DATA PATH",…).

#### Purge PACS Messages

> Old messages may be purged by selecting the option “Purge old HL7 transaction global nodes” from the “Text Gateway” menu; these messages are stored in global

> ^MAGDHL7(2006.5.

> The subroutine that is called for this menu-option (HL7^MAGDDEL3) removes entries in

> ^MAGDHL7(2006.5,…) that were time-stamped more than the number of days specified in

> ^MAGDICOM(2006.563,1,"DELETE DAYS") before the current date.

#### Process DICOM Failed Images

> Entries are removed from this file by using the Correct RAD-DICOM File Entries \[MAGD FIX DICOM FILE\] or the Correct Clinical Specialties DICOM File Entries \[MAGD FIX CLINSPEC DICOM FILE\] menu options. Using this menu will mark the entries as corrected and will be reprocessed by the VistA DICOM Image Gateway. Entries are stored in global

> ^MAGD(2006.575).

#### Removal of DICOM Incomplete Images

> Entries in this file will automatically be removed after an hour’s time span; entries are temporary stored in global ^MAGD(2006.593).

#### DICOM Error Log

> This file should not be purged. It records incomplete files received and images requested to be deleted from the DICOM FAILED IMAGES file (#2006.575). Entries are stored in global ^MAGD(2006.599.

#### MSM Error log

> See the *VistA Imaging DICOM Gateway User Manual* for instructions on how to view and purge entries from the MSM Error Log located in global ^UTILITY(“%ER”,+\$H.

### VIX-related Backups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No special backup processes are needed for the VIX (VistA Image Exchange) service.

- Metadata and images stored on the VIX’s dedicated cache are considered transitory copies and are not a part of the patient record. The site from which the data originates is the official custodian of the data, not the VIX.
- The VIX transaction log, which is the primary record of VIX activities, is retained on the server where the VIX is installed for 90 days. A permanent remote backup of the VIX transaction log is also made by the VIX Log Collector service; this is a remote automated service that requires no site configuration or activation.

> For more information about the VIX cache and the VIX Log Collector service, refer to the *VIX Administrator’s Guide.*

> This page is intentionally blank.

## Chapter 10 Callable Routines/Application Programmer Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Import API

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Import API (Application Programming Interface) was built in VistA Imaging patches 15 and 38 and is used to allow non-imaging VA and commercial vendors to build applications that import images into the VistA database and connect them to the patient record. The Import API was modified in VistA Imaging Patch 108.

> The Import API is used by the VA Veteran's ID Card (VIC) and Clinical Procedures applications, as well as commercial applications such as iMed consent and DocManager. The VIC software is used to acquire photographic images of patients. These images are sent to the National Card Management Directory (NCMD).A copy of these photo images are also automatically sent to VistA Imaging through the VistA Imaging Import API.

> The Import API also has the following capabilities:

- To check VistA Imaging and verify if a patient has a photo ID on file in VistA Imaging.
- To retrieve a current list of indexing terms.
- To create a new TIU Note stub and attach an image to it.
- To watermark images associated with a Rescinded Advance Directive with the text “Rescinded”.

> For more details on the Import API reference the *VistA Imaging System Import API Programmer Guide*. The Import API Programmer Guide can be requested from the VistA Imaging Development Team.

> The Import API cannot be used without a written agreement between the VistA Imaging group and the party wishing to use the Import API. All imported images must meet image quality and documentation requirements of VistA Imaging. In addition to the written agreement the VA Policy in section 10.1.1 and FDA Policy in section 10.1.2 must be followed.

### VA Policy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *<u>VA Policy states the following</u>:*

> Those components of a national package (routines, data dictionaries, options, protocols, GUI components, etc.) that implement a controlled procedure contain a controlled or strictly defined interface or report data to a database external to the local facility must not be altered except by the VistA Imaging OED staff. A controlled procedure is one that implements requirements that are mandated or governed by law or VA (Department of Veterans Affairs) directive or is subject to governing financial management standards of the Federal Government and VA or that is regulated by oversight groups such as the JCAHO or FDA. A controlled or strictly defined interface is one that adheres to a specific industry standard, will adversely affect a package and/or render the package inoperable if modified or deleted. For national software that is subject to FDA oversight, only the holder of the premarketing clearance (510(k)) is allowed to modify code for the medical device. The holder of a premarketing clearance is restricted to specifically designated VistA Imaging OED staff that are located at the registered manufacturing site and operating in the designated production environment.Note: Any party interested in interfacing with the VistA Imaging software will need to contact the VistA Imaging development team to get an integration agreement in place.

### FDA Policy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *<u>FDA Policy states the following</u>:*

> The Food and Drug Administration (FDA) classifies this software as a medical device. As such, it may not be changed in any way. Modifications to this software may result in an adulterated medical device under 21CFR820, the use of which is considered to be a violation of US Federal Statutes.

## VistA Imaging Import API

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Terms of Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: The Import API, as a part of the VistA Imaging software, is regulated as a medical device. The Import API cannot be used without a written agreement between the VistA Imaging HSD&D group and the party wishing to use the Import API.

> To secure an agreement for the use of the Import API, the following criteria must be met:

1.  Any products built or interfaced using the VistA Imaging Import API must be tested with VistA Imaging. Testing will be performed by the VistA Imaging team with assistance from field sites and the calling package. This testing must demonstrate that there are no adverse interactions affecting the safety, efficacy or performance of the VistA Imaging software or the devices interfaced to VistA Imaging.
2.  Any changes to packages/product(s) using the VistA Imaging Import API must be reported to the VistA Imaging Project Office for review and testing before release. Retesting of VistA Imaging with the product(s) is required with any change.
3.  Documentation that imported reports/objects meet VHA, regulatory, and quality requirements must be on file with the Vista Imaging Project Office prior to any clinical use. Sample imported reports/objects shall be provided initially to the VistA Imaging Project Office by the package using the API. Sites installing the VistA Imaging API must comply with all VistA Imaging requirements and are responsible for filing all required documentation with the VistA Imaging Project Office, including image quality and data forms and sample reports/objects from any interfaced device.
4.  Additional requirements may apply to non-VA software using the Import API.

## Chapter 11 Error Recovery, Troubleshooting, and Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Error Recovery

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Server or Disk Drive Failure

> When a server or disk drive fails, the VistA Imaging System allows immediate action to be taken so that system operation may continue. The following steps should be taken when a server or drive has failed:

- Use the Network Location Manager menu option on the Background Processor and place the share(s) “OFFLINE”. If these are magnetic drives, their images will be automatically pulled from Tier 2.
- If the Image Network Write Location or PACS Image Write Location field in the IMAGING SITE PARAMETERS file (#2006.1) points to a device that is down, edit it to point to a location that is operational. Use the Edit/Site Parameters menu option on the Background Processor.
- When your server or disk drive has been repaired, edit the Operational Status field (#5) of the NETWORK LOCATION file (#2005.2) to “ONLINE”.
- Run the Verifier software on your magnetic shares to synchronize any pointers changed during the failure, and archive unprocessed files to Tier 2.

#### Delete Image and Pointers

> Images can be deleted using the VistA Imaging Display application. When an image is deleted, the image itself and all "derivative" images (such as abstracts) are deleted from the image servers. Additionally, the IMAGE file (#2005) entry for the image, and any pointers to applications (Laboratory, Medicine, etc.) for that image, are deleted as well. To delete images, a user must have the MAG DELETE security key. For Clinical Display users with this key, there will be a Delete in the main menu of the Image List and Radiology Viewer windows. The Delete option will also be available in pop-up menus for images and abstracts.

> The following occurs once an image has been flagged for deletion:

1.  An entry is made in the Background Queue file and will be processed on a first-in-first-out basis by the Background Processor.
2.  The IMAGE AUDIT file (#2005.1) will record the information on the deleted image entry.
3.  An entry will be made in the IMAGE ACCESS LOG file (#2006.95) to indicate that an image was deleted.
4.  The image entry will be deleted from the IMAGE file (#2005) and any pointed to entries will also be updated.
5.  All DOS files relating to the image will be deleted from the Imaging server(s), but not from the jukebox.

#### ATTENTION: Caution Must Be Taken when Granting the Image Deletion Key.

> Note: Anyone who holds the Image Deletion Key is allowed to delete any image, regardless of who created the image in question.

> When images are deleted, a reason code must be entered to note why the image was deleted. Sites can optionally add site-specific reason codes by using the MAG REASON EDIT System Manager Menu option, which is explained in Section 8.2 of this document.

#### Correcting Image Capture Errors

> When an image is captured under the wrong patient, it is strongly recommended that you use the following procedure to make the needed correction—provided that the images still reside on the Radiology modality, or a hard copy of the image is still available:

1.  Correct the patient information on the modality, then resend the image; or, if a hard copy (X- Ray film) of the image is available, digitize the image
2.  Review the new images acquired
3.  Follow the instructions in the section above to delete the incorrect images

> If the above approach is not feasible then contact the Imaging Support staff to assist in correcting the images. The steps they will use are covered below.

> Two (2) types of errors can be made during image capture:

- An image is captured that the user did not want to save. This type of error is corrected by the image and pointer deletion procedure described above.
- The user identified the patient incorrectly and therefore saved patient B's images with patient A's text record. Presently, this second type of error must be corrected manually by imaging system manager staff using the following procedure.

#### Delete Incorrect Image Pointers from Incorrect Patient's Record

1.  Use the edit option of File Manager to access the image field of the parent package (e.g., radiology, cardiology, laboratory, etc.) for the incorrect patient.
2.  Identify and write down the names of the images that were incorrectly placed in this file.
3.  Delete these entries.

#### Add Correct Image Pointers to Correct Patient's Record

1.  Use the edit option to select the correct patient's report file.
2.  Edit the image field and enter the exact same image names that were deleted from the incorrect patient.

#### Verify Correction

> Ask the user to examine the image of the correct and incorrect patients, and determine whether the correction was done properly.

#### QA Review Utility

> In Clinical Display or Clinical Capture, users who have the MAG SYSTEM or MAG EDIT security keys have access to the QA Review Utility. This utility allows users with the appropriate security key to specify date ranges and perform quality assurance checks on captured images from specified users.

> The QA Review Utility also allows the reviewers of the images to change the image indexes by using the Image Index Edit Utility.

#### Image Index Edit Utility

> The Image Index Edit Utility is available to users who have the MAG SYSTEM or MAG EDIT security keys. Through this utility, an authorized user can select an image and modify the indexing terms for the image.

#### QA Review Reports

> The QA Review Reports are available to users who have the MAG SYSTEM or MAG EDIT security keys. The reports are run for a specified date range and for specific users. The reports give details for users to scan for the date range, status, number of entries and pages, and a percentage representing the total number of images reviewed.

### Troubleshooting / Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Users may encounter several types of errors as they use the VistA Imaging System. Some of these errors are…

- Processing errors: which means that the VistA Imaging System failed to complete a processing task.
- Data errors: which means that the VistA Imaging System attempted to use data that was incomplete or formatted incorrectly.
- Command errors: which means that users and other programs that interact with Imaging issued commands that conflicted with other commands or with the VistA Imaging System processing state.

> A table of error messages, descriptions and causes or solutions is provided in Appendix A of this document and in the *VistA Imaging Error Message Guide*.

### Test Software Available for Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

> When setting up a workstation, it is often necessary to use software to test isolated workstation functions. A number of executables are available for testing:

- Network connectivity
- Connectivity to the Kernel RPC Broker
- Ability to display images
- Connectivity to image servers
- Network timing tests

> These exetables are described in the following sections.

#### PING, TRACERT

> The PING and TRACERT commands are available in the DOS directory on the workstations. Using these commands can help determine if the IP address supplied in the HOSTS or LMHOST file is reachable, or if a possible routing problem exists. The local PC support person in IRM can assist with the usage of these commands and the local network IP addressing scheme.

#### RPCTEST.EXE

> The RPCTEST.EXE file is located in the Program Files\VISTA\BROKER directory. This file can be used to test the Broker Client Manager connection to the VistA servers. Once this file is executed, the VistA Access/Verify Code Window should display. If it does not, one or a combination of the following could be happening:

- The TCP Listener is not running on the VistA hospital system.
- An invalid IP address or listening port number was configured during the Broker Client Manager software installation on the workstation.

> Note: Please review the Kernel RPC documentation on the usage of this executable file and installation of the RPC Client Manager software.

#### VistA Imaging Capture, Test Mode

> The VistA Imaging Capture software has a Test mode that allows testing of input devices (scanners, video capture boards, etc.). The Test mode features…

- Testing of the capture functions without a connection to the VistA servers.
- No requirement to identify patients.

> In addition, the image test file will not be saved. This mode is helpful when interfacing and testing new equipment.

> To set the application to test mode, select Test Mode from the Configuration \| Configuration Settings \| All Settings menu.

> Note: See the Capture online help for additional information.

### Handling Processing and Storage Errors in the New Data Structures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The HDIG and the Archiver handle errors in storing the SOP classes for which support was introduced in MAG\*3.0\*34. These SOP classes are stored in the data structures that were introduced in MAG\*3.0\*34.

> The section does not apply to processing and storage errors of the SOP classes that were supported before the release of MAG\*3.0\*34.

#### How the HDIG and the Archiver Handle Processing and Storage Errors

> The HDIG uses the DICOM Gateway notification mechanism to send notifications about processing and storage errors to the email group defined in its configuration. It also sends information about such errors to the modality that sent the DICOM object.

> When the HDIG stores an image, it uses two queues defined in the QUEUE file (#2006.927). The Archiver uses the Async Storage Request Queue to archive the objects in long term storage asynchronously. It uses the Async Storage Request Error Queue to record failed storage attempts. Both queues operate through entries made in the QUEUE MESSAGE file (#2006.928). The Archiver attempts to process storage requests from QUEUE MESSAGE file (#2006.928) entries for the Async Storage Request Queue. If the Archiver is not able to store the object, it waits for 20 minutes before trying again. The Archiver will try to store an object five times. After five unsuccessful attempts to store the object, the Archiver deletes the Async Storage Request Queue entry in the QUEUE MESSAGE file (#2006.928) and creates a corresponding entry for the Async Storage Request Error Queue.

> After the error queue message is created, the Archiver cannot make further attempts to store the object until a user examines the failed attempts, resolves the source of the error, and re-enters an Async Storage Request Queue entry in the QUEUE MESSAGE file (#2006.928) for the object.

> You can identify and view Async Storage Request Error Queue entries in the QUEUE MESSAGE file (#2006.928) using VistA options on the Hybrid DICOM Gateway Menu \[MAGV HDIG MENU\] as described in <span id="_bookmark152" class="anchor"></span>*[Using Hybrid DICOM Gateway \[MAGV HDIG MENU\]](\l) [Options to Get Information About Asynchronous Storage Error Queue Entries in the QUEUE](#_bookmark152) [MESSAGE File (#2006.928) .](#_bookmark152)* After correcting the problem, you can return the archive request back to the Async Storage Request Queue. For information about the procedure, see *[Retrying](#retrying-failed-archive-requests)* [*Failed Archive Requests*.](#retrying-failed-archive-requests)

#### Getting Information About Processing and Storage Errors

> There are two ways to get information about processing and storage errors:

- Getting emails from the DICOM Gateway notification mechanism
- Using the Hybrid DICOM Gateway Menu \[MAGV HDIG MENU\] Options

#### Getting Emails from the DICOM Gateway Notification Mechanism

> The HDIG saves processing and storage errors. It sends messages with all processing and storage errors to the email address defined in the configuration of the DICOM Gateway. The HDIG sends an email immediately for processing or storage errors. Image RESENDs and IOD violation errors accumulate during the day and are sent either in groups of 25 or at the end of the day (if fewer than 25).

> If you get information about storage and processing errors, you need to identify the cause of the error and correct it. This typically involves identifying the object that caused the error, the cause of the error, and correcting the problem.

#### Using Hybrid DICOM Gateway \[MAGV HDIG MENU\] Options to Get Information About Asynchronous Storage Error Queue Entries in the QUEUE MESSAGE File (#2006.928)

> You can view the information for Async Storage Request Error Queue entries in the QUEUE MESSAGE file (#2006.928) using the Find and List options on the Hybrid DICOM Gateway Menu \[MAGV HDIG MENU\].

1.  Log into your VistA account and select the Imaging System Manager Menu \[MAG SYS MENU\].

![](vista-imaging-system-technical-manual/092.png)

2.  Select Find Async Storage Request Errors \[MAGVA ASYNC STORAGE ERR QURY\]. This option selects QUEUE MESSAGE file (#2006.928) entries with a QUEUE field value of Async Storage Request Error Queue, and stores them in the MAGV-ASYNC- STORAGE-ERRORS Template.

![](vista-imaging-system-technical-manual/093.png)

3.  Select List Async Storage Request Errors \[MAGVA ASYNC STORAGE ERR LIST\].

> This option lists detailed information about the QUEUE MESSAGE file (#2006.928) entries selected in the preceding step. The following shows the sample output for the first three of 18 error messages in the Async Storage Request Error Queue.

![](vista-imaging-system-technical-manual/094.png)

> The Async Storage Request Error Queue entries in the QUEUE MESSAGE file (#2006.928) provide information about the type of object that is stored and about its token. The listing displays the logged storage error(s) for an artifact resolved using its token. The sequence in the preceding sample was generated following these steps.

- Uses the artifactToken to look up the artifact identifier (IEN of the artifact) from the ARTIFACT file (#2006.916).
- Retrieves the storage transactions for the artifact from the STORAGE TRANSACTION file (#2006.926), filtering for failed transactions. (Those with a STATUS field value of F).
- Displays the MESSAGE field (#7) of the STORAGE TRANSACTION file (#2006.926) entry, which is likely to contain an error.
- Displays the lastError item from the MESSAGE field (#6) in the QUEUE MESSAGE file (#2006.928).

#### Retrying Failed Archive Requests

> The Archiver makes five attempts to archive a file before moving it to the Async Storage Request Error Queue. After correcting the cause of the error, a site administrator must manually move the messages from the error queue to the Async Storage Request Queue. This notifies the Archiver to try and store the record again.

> This section demonstrates how to move all the messages from the Async Storage Request Error Queue to the Async Storage Request Queue.

> From the Hybrid DICOM Gateway Menu, \[MAGV HDIG MENU\], select Requeue Async Storage Request Errors \[MAGVA ASYNC STORAGE ERR REQU\].

> In this first example, all of the entries are requeued.

![](vista-imaging-system-technical-manual/095.png)

> In this example, the entries have previously been requeued, but the sort template has not been refreshed (with a subsequent Find operation).

![](vista-imaging-system-technical-manual/096.png)

> You should run the menu options in this order:

- Find Async Storage Request Errors
- List Async Storage Request Errors
- Requeue Async Storage Request Errors

> A List operation displays the current contents of the sort template.

> Before running the Requeue option, you must resolve the cause of the storage error.

> If the entries have already been requeued when you attempt to requeue them, you should initiate a new Find operation to re-initialize the sort template.

> If a situation, such as a server power outage, is the cause of many archive failure errors, it is more efficient to verify a representative sample of the error messages and then requeue the entire set with the Requeue option after the event that has caused the storage failures is corrected.

## Chapter 12 External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### HL7 Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Text gateway processes the following HL7 message types to construct and maintain the Modality Worklist Database:

ADT Admission, Discharge, Transfer

SCH Patient Appointment and Scheduling Segment MFN Master File Notification

ORM Order Message

ORU Observational Result – Unsolicited

### HL7 Application Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Imaging includes the following HL7 application parameters:

- MAG COMRCL PACS

This application name represents the destination for HL7 messages, and will appear in field 5 of the Message Header segment (MSH-5) of the HL7 message generated by VistA. The value in its FACILITY NAME Field will appear in MSH-6.

- MAG VISTA IMGNG

This application name represents the origin for HL7 messages, and will appear in MSH-

3\. The value in its FACILITY NAME Field will appear in MSH-4.

These entries are added to the HL7 APPLICATION PARAMETER File (#771) during installation.

![](vista-imaging-system-technical-manual/097.png)

You can change the value of the NAME or FACILITY NAME attributes through VistA option HL EDIT APPL PARAM.

### HL7 Logical Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Imaging includes the HL7 logical link MAG CPACS.

This entry will be added to the HL7 LOGICAL LINK File (#870) during installation:

![](vista-imaging-system-technical-manual/098.png)

This logical link contains information about the commercial PACS destination, including its TCP/IP parameters (IP address and port number). The VistA HL7 package uses the IP address and port number to route messages to their destination over the network. You can change the value of the IP address and port number using VistA option HL EDIT LOGICAL LINKS.

### Imaging Broker Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Imaging Broker Calls

All VistA Imaging remote procedure calls are documented in the REMOTE PROCEDURE file (#8994) and can be viewed using FileMan Print File Entries \[DIPRINT\] or Inquire to File Entries \[DIINQUIRY\] menu options. VistA Imaging remote procedures use the MAG namespace.

![](vista-imaging-system-technical-manual/099.png)

### Windows Messaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to communicate with CPRS, windows messages are exchanged on the workstation. The VistA Imaging display clients must be launched from the CPRS menu option to enable the exchange of these messages.

If CCOW is enabled, VistA Imaging Clinical Display and VistA Imaging Clinical Capture will synchronize patient and user context with other CCOW applications (such as CPRS) using CCOW. If CCOW is unavailable, VistA Imaging Clinical Display and VistA Imaging Clinical Capture will continue to synchronize with CPRS when launched from CPRS using Windows messages.

### Integration Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Integration Agreements (IAs) describe how one VistA application uses routines that belong to another VistA application.

To display the ICRs that cover non-Imaging routines used by Imaging, perform the steps below.

1.  Sign on to the FORUM system.
2.  Select the DBA menu.
3.  Select the INTEGRATION CONTROL REGISTRATIONS \[IAs\] menu.
4.  Select the Subscriber Package Menu \[SUBS\].
5.  Choose the “Print ACTIVE by Subscribing Package” option.
6.  Enter “IMAGING” at the “START WITH SUBSCRIBING PACKAGE: FIRST//”

> prompt.

7.  Enter “IMAGINGZ” at the “GO TO SUBSCRIBING PACKAGE: LAST//’ prompt.
8.  Select the device for printing.

To display the IAs that cover Imaging routines used by other applications, perform the steps below.

1.  Sign on to the FORUM system.
2.  Select the DBA menu.
3.  Select the INTEGRATION CONTROL REGISTRATIONS \[IAs\] menu.
4.  Select the Custodial Package Menu \[CUST\].
5.  Choose the “ACTIVE ICRs by Custodial Package” option.
6.  Enter “IMAGING” for the package prompt.

### Select the Context Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section includes:

- Context Management
- The Clinical Context Object Workgroup Protocol
- The Context Management Settings Tab
- Context Changes
- CPRS Tools Menu for VistARad

#### Context Management

Context Management (CM) allows users to choose a subject once in one application, and have all applications containing information on that same subject “tune” to the data they contain. This eliminates the need for the user to redundantly select the subject in the varying applications. In the healthcare industry, for example, multiple applications operating “in context” through use of a context manager would allow a user to select a patient (*that is,* the subject) in one application. See the expanded discussion for end users in the *VistARad User Guide*, under Context Management.

Context Management is gaining in prominence in healthcare due to the creation of a standardized protocol, the Clinical Context Object Workgroup (CCOW) Protocol, enabling applications to function in a “context-aware” state.

#### The Clinical Context Object Workgroup Protocol

> CCOW is a Health Level 7 (HL7) standard protocol designed to enable dissimilar healthcare software applications to synchronize in real-time, and at the user-interface level. It is vendor independent and allows applications to present information at the desktop and/or portal level in a unified way.

> CCOW is the primary standard protocol used in healthcare to facilitate the Context Management process. Although both CCOW and non-CCOW compliant applications can use CM, the CCOW standard helps facilitate a more robust and near “plug-and-play” interoperability across applications.

> When CCOW is available, the VistARad client uses CCOW to synchronize patient and user context management with the Computerized Patient Record System (CPRS) and other CCOW-enabled applications. A new Settings tab, Context Management, is used to enable context management; the setting Enable Context Management must be checked to use the context management functionality.

> The TeleReader application requires CCOW to synchronize patient and user context with other applications such as CPRS and VistA Imaging Display. TeleReader cannot work if CCOW is unavailable. TeleReader will close if CCOW is not functioning properly.

#### The Context Management Settings Tab

> The Context Management settings tab allows the user to manage how CM operates on the individual workstation. The user must check the Enable Context Management in order to use CM capability.

#### Context Changes

> A context indicator (icon) appears at the top of the various VistARad windows to the left of the Patient Name and demographics. A Context menu item appears on the Manager and Viewer menu bars for options to Suspend/Resume context, etc. The application also automatically changes the displayed icon to reflect the change in context. See the expanded discussion for end users in the VistARad User Guide, under Context Management.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Icon</strong></th>
<th><strong>Title</strong></th>
<th><strong>Meaning</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>![](vista-imaging-system-technical-manual/100.png)</p>
</blockquote></td>
<td rowspan="2"><strong>Changing</strong></td>
<td>Displayed when the Clinical Link is changing. This icon may appear so briefly that the user may not see it. It is displayed when the common (linked) patient is changing. For example, if VistARad is linked with CPRS and CPRS changes from one patient to another, this icon will display during the change process.</td>
</tr>
<tr class="even">
<td><strong>Patient Context is Changing</strong></td>
</tr>
<tr class="odd">
<td rowspan="2">![](vista-imaging-system-technical-manual/101.png)</td>
<td rowspan="2"><strong>Broken</strong></td>
<td>Displayed when an application is not linked or the application is “out of patient context.” For example, if CPRS is linked and displaying one patient and VistARad is displaying a different patient, then VistARad is said to be “out of patient context” and will display this icon.</td>
</tr>
<tr class="even">
<td><strong>Patient Context is Broken</strong></td>
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>![](vista-imaging-system-technical-manual/102.png)</p>
</blockquote></td>
<td rowspan="2"><strong>Linked</strong></td>
<td>Displayed when an application is utilizing CCOW to maintain patient context with the CCOW server. For example, if VistARad is open and displaying the same patient (as defined by the CCOW server) for all linked applications, then VistARad will display this icon.</td>
</tr>
<tr class="even">
<td><strong>Patient Context is Joined</strong></td>
</tr>
</tbody>
</table>

### CPRS Tools Menu Option for VistARad

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Sites may also configure a new CPRS Tools menu option for launching VistARad from CPRS. Refer to the *VistA Imaging Installation Guide*, under Associating Display and Capture with CPRS, for background information on this configuration step. To configure for launching VistARad, add a Sequence, then enter this line of text exactly as shown (no line breaks, no extra spaces):

![](vista-imaging-system-technical-manual/103.png)

### Mailman Messaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes the types of MailMan messages that are sent to a site’s MAG SERVER mail group.

> The MAG SERVER mail group is established when VistA Imaging is installed. MAG SERVER initially contains the addresses of the person that installed VistA Imaging and of the VistA Imaging development team.

- Typical members of this group should be key IRM support staff, radiology managers, and/or ADPACS.
- Text pagers can be added to the MAG SERVER mail group as a “Remote Member”, provided that the domain portion of the remote mail member address is defined in the DOMAIN file (#4.2).

> Note: The “<u>REDACTED</u>” is a required member of this group.

> The members of the MAG SERVER mail group (aka the Local Imaging Mail Group) can be edited as described in Chapter 6 of the Background Processor User Manual.

#### “Image Cache Critically Low” Messages

> The Image Cache Critically Low message is generated automatically when the Background Processor is unable to update the network write location within the VistA Magnetic Cache. This happens when the low level mark has been reached and the current location has only 5% (default value) of its capacity available at the time this message is generated.

> The following is a sample Image Cache Critically Low Message:

![](vista-imaging-system-technical-manual/104.png)

> This mechanism ensures that the remaining cache locations can be manually referenced during the free space recovery process (BP Purge) that the VistA Imaging System Manager MUST initiate. It is advised that while the purge is running the Auto Write Location update process be turned off, and that the Network Write Location and the PACS Write Location be manually updated to different locations. For more information, see Chapter 6 in the *Background Processor User Manual*.

#### “Image Site Usage” Messages

> When VistA Imaging is installed, a process used to generate monthly Image Site Usage messages is established. Image Site Usage messages contain information about VistA Imaging statistics (images displayed, images captured, etc.) and the software and patch versions installed. The information in these messages is used for the VistA Imaging VISN (Veterans Integrated Service Network) Performance Monitor Report.

> Image Site Usage messages are automatically generated at 4:01 AM (VistA System time) on the first day of each month, and will be sent to the MAG SERVER mail group. They can also be generated on demand as described on the next page.

> A sample monthly Image Site Usage message is shown below.

![](vista-imaging-system-technical-manual/105.png)

![](vista-imaging-system-technical-manual/106.png)![](vista-imaging-system-technical-manual/107.png)

> The following sections explain how an Ad Hoc (on demand) version of an Image Site Usage message can be generated, describe the contents of a typical Site Usage message, and outline how automatic Image Site Usage message generation can be disabled.

#### Ad Hoc Image Site Usage Messages

> To generate an on-demand version of the Imaging Site Usage message, perform the following steps.

1.  Access the Imaging System Manager Menu \[MAG SYS MENU\] and run the Ad Hoc Enterprise Site Report option.

![](vista-imaging-system-technical-manual/108.png)![](vista-imaging-system-technical-manual/109.png)

2.  At the next two prompts, enter the date range that you want the report to cover. The prompts will default to the previous month.

![](vista-imaging-system-technical-manual/110.png)

3.  After the report is generated, it will be sent in a MailMan message to the MAG SERVER mail group. The subject of the message will be “Ad Hoc Image Site Usage.”

#### Contents of an Image Site Usage Message

> The contents of the Image Site Usage message are described in the following table. Note that some entries in the message are dependent on the Imaging components and patches installed— for example, entries specific to VistARad workstations will not be present at sites that do not use VistARad.

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Entry Name</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Site</td>
<td>The name of the medical center for which the message was generated.</td>
</tr>
<tr class="even">
<td>Reporting Period</td>
<td>The time period covered by the report. Note that for Ad-Hoc reports, the date range specified by the user is indicated (which may be greater than the date range of the available data).</td>
</tr>
<tr class="odd">
<td>Date</td>
<td>The date the message was generated.</td>
</tr>
<tr class="even">
<td>Domain</td>
<td>The VistA mail domain name where the message was generated.</td>
</tr>
<tr class="odd">
<td>2005 Entries</td>
<td>The number of entries in the IMAGE file (#2005), based on the value in the IMAGE File header.</td>
</tr>
<tr class="even">
<td>2006.81 Entries</td>
<td>The total number of Clinical Display and Clinical Capture workstations, as indicated in the IMAGING WINDOWS WORKSTATIONS file (#2006.81).</td>
</tr>
<tr class="odd">
<td>Production Account</td>
<td>The value is equal to "1" if the message is generated from the site's production database environment.</td>
</tr>
<tr class="even">
<td>WS DIS VERS</td>
<td><p>An array showing installations of the VistA Imaging Clinical Display software. The array contains the following values:</p>
<blockquote>
<p>VERSION ^ OPERATING_SYSTEM ^ #INSTALLED</p>
</blockquote>
<p>An entry will be generated for each unique combination of VERSION and OPERATING_SYSTEM, for all Display workstations that have been accessed in the last 180 days.</p></td>
</tr>
<tr class="odd">
<td>WS CAP VERS</td>
<td><p>An array showing installations of the VistA Imaging Clinical Capture software. The array contains the following values:</p>
<blockquote>
<p>VERSION ^ OPERATING_SYSTEM ^ #INSTALLED</p>
</blockquote>
<p>An entry will be generated for each unique combination of VERSION and OPERATING_SYSTEM, for all Capture workstations that have been accessed in the last 180 days.</p></td>
</tr>
<tr class="even">
<td>WS VR VERS</td>
<td><p>An array showing installations of the VistARad workstation software. The array contains the following values:</p>
<blockquote>
<p>VERSION ^ OPERATING_SYSTEM ^ #INSTALLED</p>
</blockquote>
<p>An entry will be generated for each unique combination of VERSION and OPERATING_SYSTEM, for all VistARad workstation that have been accessed in the last 180 days.</p></td>
</tr>
<tr class="odd">
<td>VistARad Version</td>
<td>The most recently installed version of VistARad. For the installation history of all instances of VistARad, refer to the “Imaging Package Installation HX” field.</td>
</tr>
<tr class="even">
<td>DICOM Error Log</td>
<td>The total number of unresolved DICOM errors present in the DICOM Error Log (#2006.599) on the date the report was generated.</td>
</tr>
<tr class="odd">
<td>DICOM Failed Images</td>
<td>The total number of entries in the DICOM FAILED IMAGES file (#2006.575) on the date the report was generated.</td>
</tr>
<tr class="even">
<td>Queue File Count</td>
<td>The total number of entries in the IMAGE BACKGROUND QUEUE file (#2006.03), including failed entries that will not be processed without user intervention. (Successfully processed entries are deleted from the file.)</td>
</tr>
<tr class="odd">
<td>Unprocessed Queue Entries</td>
<td>The total number of unprocessed entries currently in the IMAGE BACKGROUND QUEUE file (#2006.03).</td>
</tr>
<tr class="even">
<td><em>N</em> day Image Workstation Sessions</td>
<td>The number of login sessions that occurred on all workstations (Display, Capture, and VistARad) for the period of the report.</td>
</tr>
<tr class="odd">
<td><em>N</em> day Image Workstation Patients</td>
<td>The number of patient lookups performed on Display and Capture workstations for the period of the report.</td>
</tr>
<tr class="even">
<td><em>N</em> day Image Workstation Images</td>
<td>The total number of images accessed from all Clinical Display and Capture workstations for the period of the report.</td>
</tr>
<tr class="odd">
<td><em>N</em> day Image Workstation Captures</td>
<td>The number of images acquired using Capture workstations for the period of the report.</td>
</tr>
<tr class="even">
<td><em>N</em> day VistARad WS Display</td>
<td><p>An array containing information for studies displayed on all VistARad workstations for the period of the report. The array contains the following values:</p>
<p>STUDIES ^ IMAGES ^ PATIENTS ^ RAD/NONRAD ^ ROUTED/LOCAL ^</p>
<p>STUDIES_PER_MODALITY</p>
<blockquote>
<p>STUDIES: The number of studies displayed.</p>
<p>IMAGES: The number of images displayed.</p>
<p>PATIENTS: The number of patient records accessed.</p>
<p>RAD/NONRAD: The number of studies displayed by radiologists and non-radiologists, respectively.</p>
<p>ROUTED/LOCAL: The number of routed and non-routed exams displayed, respectively.</p>
</blockquote>
<p>STUDIES_PER_MODALITY: An array of modalities and the numbers of displayed studies for each modality.</p></td>
</tr>
<tr class="odd">
<td><em>N</em> day VistARad WS Interpretations</td>
<td><p>An array containing information for studies interpreted using all VistARad workstations for the period of the report. The array contains the following values:</p>
<p>STUDIES ^ IMAGES ^ PATIENTS ^ RAD/NONRAD ^ ROUTED/LOCAL ^</p>
<p>STUDIES_PER_MODALITY</p>
<blockquote>
<p>STUDIES: The number of studies interpreted. IMAGES: The number of images interpreted. PATIENTS: The number of patient records accessed.</p>
<p>RAD/NONRAD: The number of studies interpreted by radiologists and non-radiologists, respectively (the value for non-radiologist interpretations should always be 0).</p>
<p>ROUTED/LOCAL: The number of routed and non-routed exams interpreted, respectively.</p>
</blockquote>
<p>STUDIES_PER_MODALITY: An array of modalities and the numbers of interpreted studies for each modality.</p></td>
</tr>
<tr class="even">
<td><em>N</em> day average daily routed images</td>
<td>The average number of studies routed per day.</td>
</tr>
<tr class="odd">
<td>BP Vers. Num. Date</td>
<td><p>An array showing installations of the Background Processor client software. The array contains the following values:</p>
<blockquote>
<p>CLIENT_VERSION ^ OPERATING_SYSTEM ^ #INSTALLED ^</p>
<p>BUILD_DATE</p>
</blockquote>
<p>An entry will be generated for each unique combination of VERSION and OPERATING_SYSTEM for all Background Processor workstations.</p></td>
</tr>
<tr class="even">
<td>VistA Image Version/Build</td>
<td><p>The most recent VistA Imaging KIDS installation, presented in an array with the following values:</p>
<p>RELEASE ^ PATCH ^ INSTALL_DATE</p></td>
</tr>
<tr class="odd">
<td>DICOM Gateway Version</td>
<td><p>An array showing installations of the DICOM Gateway workstation software. The array is based on the contents of the DICOM WORKSTATION file (#2006.83), and contains the following values:</p>
<p>VERSION;PACKAGE_NAME;PATCHES;BUILD_DATE ^ #_INSTALLED</p></td>
</tr>
<tr class="even">
<td>Image file namespace(s)</td>
<td>The unique 1-, 2-, or 3-character filename prefix used for images stored at this site. If multiple prefixes are used by a site, each prefix will be shown.</td>
</tr>
<tr class="odd">
<td>From FileMan Date Until FileMan Date</td>
<td>Fields that provide information which may be helpful to support staff when the report contains unexpected values.</td>
</tr>
<tr class="even">
<td>Resolution</td>
<td><p>Reports the number of workstations and the resolutions being used by their monitors.</p>
<blockquote>
<p>CLASS ^ COLUMNS ^ ROWS ^ BITS ^ TYPE ^ COUNT</p>
</blockquote>
<p>CLASS: Indicates if the monitors in this group have acceptable or unacceptable display capabilities.</p>
<p>COLUMNS^ROWS: The number or vertical and horizontal pixels.</p>
<p>BITS: The bit-depth.</p>
<p>TYPE : The workstation type (PC or Thin Client (TC)).</p>
<p>COUNT: The number of workstations.</p></td>
</tr>
<tr class="odd">
<td>DICOM Capture</td>
<td><p>An array showing the modality and number of images acquired by all DICOM Image Gateways during the reporting period. The array contains the following values.</p>
<blockquote>
<p>MODALITY_ABBR ^ IMAGES_ACQUIRED ^ MODALITY_NAME ^</p>
<p>GROUPS_ACQUIRED</p>
</blockquote>
<p>An entry will be generated for each modality that images are acquired from.</p></td>
</tr>
<tr class="even">
<td>Import API</td>
<td><p>Provides a count of images and image groups that were acquired by the Import API, broken down by sending application (origin).</p>
<blockquote>
<p>SOURCE_APP ^ #IMAGES ^ #GROUPS</p>
</blockquote>
<p>Only present for sites that use the Import API.</p></td>
</tr>
<tr class="odd">
<td>Clin Capture</td>
<td><p>An array showing the PROCEDURE Field (#2005,6) and number of images acquired by all Capture workstations during the reporting period. The array contains the following values.</p>
<blockquote>
<p>PROC_FIELD ^ IMAGES_CAPTURED</p>
</blockquote>
<p>An entry will be generated for each procedure field entry that images are captured for.</p></td>
</tr>
<tr class="even">
<td>Other Consents</td>
<td><p>An array showing the number of captured consent forms , based on the contents of the SHORT DESCRIPTION field (#2005,10) for the report period.</p>
<blockquote>
<p>SHORT_DESC_FIELD^ IMAGES</p>
</blockquote>
<p>An entry will be generated for each SHORT DESCRIPTION field value containing the word “consent”. (For example, CONSENT and INFORMED CONSENT would be shown in two different entries).</p></td>
</tr>
<tr class="odd">
<td>Consent Forms</td>
<td>The number of consent forms captured for the report period.</td>
</tr>
<tr class="even">
<td>Image file group parents</td>
<td><p>The number of image group parent entries added to the IMAGE</p>
<p>file (#2005) during the report period.</p></td>
</tr>
<tr class="odd">
<td>Image file objects</td>
<td>The number of entries (excluding group parent entries) added to the IMAGE file (#2005) during the report period.</td>
</tr>
<tr class="even">
<td>Image file deletes</td>
<td>The number of entries deleted from the IMAGE file (#2005) during the report period. Note that this value indicates only those entries that were both added AND deleted within the report period.</td>
</tr>
<tr class="odd">
<td>Document Images (TIF)</td>
<td>The number of scanned document images acquired during the reporting period.</td>
</tr>
<tr class="even">
<td>Document Groups (TIF)</td>
<td>The number of scanned document groups acquired during the reporting period.</td>
</tr>
<tr class="odd">
<td>Total Image Objects for Place</td>
<td>The count for entire institutional database</td>
</tr>
<tr class="even">
<td>Total Group Parents for Place</td>
<td>The count for entire institutional database</td>
</tr>
<tr class="odd">
<td>Total Image Entry Deletes for Place</td>
<td>The count for entire institutional database</td>
</tr>
<tr class="even">
<td>Unique Image Patients Captured</td>
<td>The number of individual patients that had new images added (using VistA Imaging) during the report period.</td>
</tr>
<tr class="odd">
<td>Unique Image Patients Display</td>
<td>The number of individual patients that had images displayed using Clinical Display or VistARad during the report period.</td>
</tr>
<tr class="even">
<td>Unique Image Patients All</td>
<td>The total number of individual patients that had images displayed or captured during the report period.</td>
</tr>
<tr class="odd">
<td>Total Non-Verified Images for Place</td>
<td>Count for reporting period</td>
</tr>
<tr class="even">
<td>Total Verified Images for Place</td>
<td>Count for reporting period</td>
</tr>
<tr class="odd">
<td>Total Duplicate Images for Place</td>
<td>Count for reporting period</td>
</tr>
<tr class="even">
<td>TLR SPECIALITY</td>
<td>TeleReader reporting period count</td>
</tr>
<tr class="odd">
<td>TLR PROCEDURE</td>
<td>TeleReader reporting period count</td>
</tr>
<tr class="even">
<td>TLR LOCAL STUDIES</td>
<td>TeleReader reporting period count</td>
</tr>
<tr class="odd">
<td>TLR REMOTE STUDIES</td>
<td>TeleReader reporting period count</td>
</tr>
<tr class="even">
<td>TLR LOCAL IMAGES</td>
<td>TeleReader reporting period count</td>
</tr>
<tr class="odd">
<td>TLR REMOTE IMAGES</td>
<td>TeleReader reporting period count</td>
</tr>
<tr class="even">
<td>TLR LOCAL READING TIME</td>
<td>TeleReader reporting period count</td>
</tr>
<tr class="odd">
<td>TLR REMOTE READING TIME</td>
<td>TeleReader reporting period count</td>
</tr>
<tr class="even">
<td>TLR RESULTED LOCALLY BY TELEREADER</td>
<td>TeleReader reporting period count</td>
</tr>
<tr class="odd">
<td>TLR RESULTED LOCALLY BY CPRS</td>
<td>TeleReader reporting period count</td>
</tr>
<tr class="even">
<td>TLR RESULTED REMOTELY BY TELEREADER</td>
<td>TeleReader reporting period count</td>
</tr>
<tr class="odd">
<td>TLR RESULTED REMOTELY BY CPRS</td>
<td>TeleReader reporting period count</td>
</tr>
<tr class="even">
<td>TLR LOCAL ACQUISITION TIME</td>
<td>TeleReader reporting period count</td>
</tr>
<tr class="odd">
<td>TLR REMOTE ACQUISITION TIME</td>
<td>TeleReader reporting period count</td>
</tr>
<tr class="even">
<td>Advance Directive Scanned Administrative Closure</td>
<td>&lt;for future use&gt;</td>
</tr>
<tr class="odd">
<td>Advance Directive Unscanned Manual Closure</td>
<td>The number of signed Advance Directive notes that do not have attached scanned documents.</td>
</tr>
<tr class="even">
<td><p>Advance Directive – UNC</p>
<p>- <em>title</em></p></td>
<td>The number of Advance Directive notes without attached scanned documents, broken down by TIU note title.</td>
</tr>
<tr class="odd">
<td>Advance Directive Scanned Manual Closure</td>
<td>The number of signed Advance Directive notes that have attached scanned documents.</td>
</tr>
<tr class="even">
<td><p>Advance Directive – SMC</p>
<p>- <em>title</em></p></td>
<td>The number of Advance Directive notes with attached scanned documents, broken down by TIU note title.</td>
</tr>
<tr class="odd">
<td>Imaging Package Installation HX</td>
<td><p>An array showing the installation history of the VistA Imaging KIDS software. The array is based on the PACKAGE file (#9.4), and contains the following values:</p>
<p>SEQ_NUM ^ PACKAGE ^ VERSION ^ DATE ^ INSTALLER</p>
<blockquote>
<p>SEQ_NUM: Installation sequence.</p>
<p>PACKAGE: The package being installed. “Imaging” is used for the VistA Imaging KIDS packages; “MAGJ Radiology” refers to pre-3.0 Imaging installations of the VistARad software.</p>
<p>VERSION: The version number of the software.</p>
<p>DATE: The date the software was installed.</p>
<p>INSTALLER: The user account used to install the software.</p>
</blockquote>
<p>Entries will be generated both for current and pre-existing software versions.</p></td>
</tr>
<tr class="even">
<td>Local Network Locations</td>
<td><p>Each line shows information about a NETWORK LOCATION file (#2005.2) entry defined at the site. The first line (the one that begins with 0) is a header line that show the names of the values reported in subsequent lines. Subsequent lines show 2005.2 entries that:</p>
<ul>
<li><p>Have a Storage Type other than ‘Export’ or ‘Diagram’</p></li>
<li><p>Are on-line</p></li>
</ul>
<p>Are not ‘Routing’ shares.</p></td>
</tr>
<tr class="odd">
<td>Associated Institutions</td>
<td>This is the list of institutions whose designated users will use the imaging resources, Images, and shares associated with this this Imaging configuration while logged in to the primary host system. This is a function of the multiple platform design necessary to implement the consolidated Imaging system.</td>
</tr>
<tr class="even">
<td>ACCESS TYPE(1)</td>
<td>Clinical care for the patient whose images are being downloaded</td>
</tr>
<tr class="odd">
<td>ACCESS TYPE(2) ACCESS TYPE(B)</td>
<td>Clinical care for other VA patients</td>
</tr>
<tr class="even">
<td>ACCESS TYPE(A)</td>
<td>DICOM transmit to SITE_NAME for reason 1,Clinical care for the patient whose images are being transmitted</td>
</tr>
<tr class="odd">
<td>ACCESS TYPE(3) ACCESS TYPE(C)</td>
<td>For use in approved research by VA staff</td>
</tr>
<tr class="even">
<td>ACCESS TYPE(4)</td>
<td>For approved teaching purposes by VA staff</td>
</tr>
<tr class="odd">
<td>ACCESS TYPE(D)</td>
<td>DICOM transmit to SITE_NAME for reason 4,Approved teaching purposes by VA staff</td>
</tr>
<tr class="even">
<td>ACCESS TYPE(5) ACCESS TYPE(E)</td>
<td>For use in approved VA publications</td>
</tr>
<tr class="odd">
<td>ACCESS TYPE(6) ACCESS TYPE(R)</td>
<td>Authorized release of medical records or health information</td>
</tr>
<tr class="even">
<td>ACCESS TYPE(F)</td>
<td>DICOM transmit to SITE for reason 6: Copy to HIPAA Compliant Storage</td>
</tr>
<tr class="odd">
<td>ACCESS TYPE(16)</td>
<td>For use in Veterans Benefits Administration claims processing</td>
</tr>
<tr class="even">
<td>ACCESS TYPE(17)</td>
<td>Prints from a Display Client.</td>
</tr>
<tr class="odd">
<td>ACCESS TYPE(18)</td>
<td>Prints from a Display Client.</td>
</tr>
<tr class="even">
<td>ACCESS TYPE(AWIVTC)</td>
<td>VistA Web Sessions</td>
</tr>
<tr class="odd">
<td>ACCESS TYPE(CAP)</td>
<td>Clinical Captures</td>
</tr>
<tr class="even">
<td>ACCESS TYPE(DELETE)</td>
<td>Clinical Display Deletes</td>
</tr>
<tr class="odd">
<td>ACCESS TYPE(EXPORT-&gt;..)</td>
<td>GCC queue export events</td>
</tr>
<tr class="even">
<td>ACCESS TYPE(IMGVW)</td>
<td>Imaging Displays</td>
</tr>
<tr class="odd">
<td>ACCESS TYPE(IMGMM)</td>
<td>?? We may need to examine the Windows Session file entry</td>
</tr>
<tr class="even">
<td>ACCESS TYPE(INDEX- 42)</td>
<td>IMAGE INDEX field sets</td>
</tr>
<tr class="odd">
<td>ACCESS TYPE(INDEX- ALL)</td>
<td>All INDEX type field sets</td>
</tr>
<tr class="even">
<td>ACCESS TYPE(INDEX- 45)</td>
<td>Package Index updates</td>
</tr>
<tr class="odd">
<td>ACCESS TYPE(INDEX- CR)</td>
<td>Procedure/ Event Index updates</td>
</tr>
<tr class="even">
<td>ACCESS TYPE(INDXCHG)</td>
<td>Image Index fields updates</td>
</tr>
<tr class="odd">
<td>ACCESS TYPE(LABRPT)</td>
<td>Lab Reports</td>
</tr>
<tr class="even">
<td>ACCESS TYPE(LONGDES)</td>
<td>Parent Record Descriptions</td>
</tr>
<tr class="odd">
<td>ACCESS TYPE(MAG ANNOT)</td>
<td>Imaging Annotation using CLINICAL_DISPLAY</td>
</tr>
<tr class="even">
<td>ACCESS TYPE(MAG UTIL)</td>
<td>Storage Utility Updates</td>
</tr>
<tr class="odd">
<td>ACCESS TYPE(MEDRPT)</td>
<td>Medicine Reports</td>
</tr>
<tr class="even">
<td>ACCESS TYPE(NOIMAGE)</td>
<td>Capture failure/corrupt records</td>
</tr>
<tr class="odd">
<td>ACCESS TYPE(QFAIL)</td>
<td>Failed Setting JukeBox Queues</td>
</tr>
<tr class="even">
<td>ACCESS TYPE(P17CV)</td>
<td>Image Index Commits</td>
</tr>
<tr class="odd">
<td>ACCESS TYPE(RADRPT)</td>
<td>Radiology reports</td>
</tr>
<tr class="even">
<td>ACCESS TYPE(RESCIND)</td>
<td>Rescinded IMPORT Images</td>
</tr>
<tr class="odd">
<td>ACCESS TYPE(RVDODVA)</td>
<td>VIX / VistA Rad Remote View DOD view of VA images</td>
</tr>
<tr class="even">
<td>ACCESS TYPE(RVVADOD)</td>
<td>VIX / VistA Rad Remote View VA view of DOD images</td>
</tr>
<tr class="odd">
<td>ACCESS TYPE(RVVAVA)</td>
<td>VIX / VistA Rad Remote View VA view of VA image</td>
</tr>
<tr class="even">
<td>ACCESS TYPE(SURGRPT)</td>
<td>Surgical Reports</td>
</tr>
<tr class="odd">
<td>ACCESS TYPE(TIURPT)</td>
<td>TIU Reports</td>
</tr>
<tr class="even">
<td>ACCESS TYPE(VR-INT)</td>
<td>VistA Rad Interpretation</td>
</tr>
<tr class="odd">
<td>ACCESS TYPE(VR-VW)</td>
<td>VistARad Display</td>
</tr>
<tr class="even">
<td>ACCESS TYPE(VR- VW/REM)</td>
<td>Remote VistARad Displays</td>
</tr>
</tbody>
</table>

#### MAGREPSTART and MAGREPSTOP

> The MAGREPSTART and MAGREPSTOP options can be run to stop and restart the generation of monthly Image Site Usage messages. MAGREPSTART and MAGREPSTOP are not part of any menu, and should be assigned to a system manager or IRM before they need to be executed.

> Note: Image Site Usage messages are used to fulfill FDA requirements related to medical device monitoring MAGREPSTART and MAGREPSTOP should only be run at the direction of the VistA Imaging Group. Use of these options is not necessary under normal conditions.

> Note: If the generation of monthly Image Site Usage messages is suspended using MAGREPSTOP, no monthly messages will be generated until the process is restarted using MAGREPSTART.

#### Watermarking Messages

> When a patient’s Advance Directive Note is rescinded, the images that are attached to that note are queued for watermarking with the text “Rescinded”. As part of the watermarking process, the subscribers of the G.MAG SERVER mail group will receive an email with information about the status of the operation when:

- Watermarking is successful
- Watermarking fails

#### “Rescinded” Watermarking Succeeded

> Following is an example of the email message generated when the image was watermarked with “Rescinded”:

> Subj: Import API Report \[#31292\] 06/22/11@08:14 8 lines From: PROVIDER, ONE In 'IN' basket. Page 1

1.  1^1 Image(s) Copied OK. 0 Errors.
2.  MAGRSND;3110622.081451.3
3.  31
4.  RESCINDED IMAGE FILE^\\SERVER1\IMAGE1\$\SLA0\00\00\02\05\SLA00000020542.TIF

> The preceding array was generated by the VistA Imaging Import API while processing a 'RESCIND' Image action.

> Enter message action (in IN basket): Ignore//

#### “Rescinded” Watermarking Failed

> Following is an example of the email message generated if the image could not be watermarked with “Rescinded”.

> Subj: Import API Report \[#31341\] 06/23/11@09:52 9 lines From: PROVIDER, ONE In 'IN' basket. Page 1

5.  0^Image is already Rescinded.
6.  Image(1) 0^\<*error message for rescind failure*\>
7.  Image(1) RESCIND Action is Canceled.
8.  Image(1) IEN: 20924
9.  TIU Note: 697

> The preceding array was generated by the VistA Imaging Import API while processing a 'RESCIND' Image action.

> Enter message action (in IN basket): Ignore//

### Imaging Site Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Imaging Site Reports is an ad hoc reporting tool used to evaluate user productivity and details of the variety of images being created by the VistA Imaging application. The audience for these reports will be the managers of the VistA Imaging application.

#### Document Counts Report

> This is a report of the IMAGE file (#2005) of Image Types for an ‘Acquisition Site’ and a 'From' and 'To' Date/Time Image Saved date range. The report will give totals for each Acquisition Site, Object Type, for each user, within the Acquisition Site and date range. A grand total of images within the Acquisition Site and date range are given at the end of the report.

![](vista-imaging-system-technical-manual/111.png)

![](vista-imaging-system-technical-manual/112.png)

#### Image Count by User Report

> This is a report of the IMAGE file (#2005) of Image Types for an ‘Acquisition Site’ and a 'From' and 'To' Date/Time Image Saved date range. The report will give totals for each Acquisition Site, Object Type, for each user, within the Acquisition Site and date range. A grand total of images within the Acquisition Site and date range are given at the end of the report.

![](vista-imaging-system-technical-manual/113.png)

![](vista-imaging-system-technical-manual/114.png)

![](vista-imaging-system-technical-manual/115.png)

![](vista-imaging-system-technical-manual/116.png)

#### Means Test Report

> This is a report of the IMAGE file (#2005) sorted by ‘Acquisition Site’, 'From' and 'To' Date/Time Image Saved date range, Export Location = ALL (including null), and Index Type From ‘MEANS’ to ‘MEANSZ’. Report detail will include: Acquisition Site, Patient Name, SSN, Index Type, Date/Time Image Saved, and Export Location.

![](vista-imaging-system-technical-manual/117.png)

#### Package Index Contains ‘Note’ Report

> This is a report of the IMAGE file (#2005) sorted by ‘Acquisition Site, 'From' and 'To' Date/Time Image Saved date range, Short Description, and Package index containing ‘NOTE’. Report detail will include: Acquisition Site, Patient Name, SSN, Short Description, Date/Time Image Saved, and Image Saved by. Sub-counts and counts are given per Scanned By, with Short Description, within Patient.

![](vista-imaging-system-technical-manual/118.png)

![](vista-imaging-system-technical-manual/119.png)

![](vista-imaging-system-technical-manual/120.png)

![](vista-imaging-system-technical-manual/121.png)

![](vista-imaging-system-technical-manual/122.png)

### VistA Site Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA Site Service is a central repository of information used by Imaging components (such as Clinical Display) to connect to other sites. Using the site service eliminates the need to store other sites’ connection information locally. Local Imaging components access the site service using a special entry in the NETWORK LOCATION file (#2005.2) as described in Chapter 18.

> The site service stores the following information for each site:

- Three-digit site number
- Site name
- Region ID (VISN number)
- Station number (field \#99 in the INSTITUTION file (#4))
- VistA server hostname
- VistA server port number
- VIX server hostname
- VIX server port number

> The last two values in the preceding list only apply at sites that have implemented the VistA Imaging Exchange (VIX) service. See the *VIX Administrator’s Guide* for details.

> Note: If any of the information above changes, you must contact the VistA Imaging development group to have the site service updated. Incorrect or outdated information will interfere with remote image access.

> Sites that have implemented a VIX will also need to update their VIX’s configuration after the site service has been updated. This is done by re-running the VIX Installation wizard which will detect the new connection information and reconfigure the VIX accordingly. See the *VIX Installation Guide* for more information.

### VistARad External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistARad is able, optionally, to interface with the following types of non-VistA Imaging applications.

#### Voice Dictation Software

> VistARad can be configured to interface with voice dictation software on the same diagnostic workstation, or elsewhere on the network. When a voice dictation interface is configured, VistARad sends identifying information for the current exam to the dictation software. Currently, Talk and PowerScribe are supported.

#### Medical Visualization/3D Reconstruction Software

> VistARad can be configured to interface with medical visualization/3D reconstruction software on the same diagnostic workstation. When a medical visualization interface is configured, VistARad can send an exam to the visualization software for various manipulations such as multi-planar reconstruction, 3D reconstruction, and PET/CT Fusion. Currently, Toshiba’s Voxar 3D software is supported.

#### Medical Imaging Resource Center (MIRC) “Teaching File” server

> VistARad can be configured to interface with a Medical Imaging Resource Center (MIRC) server. When this interface is configured, VistARad can send an image, an image set, or an entire exam of interest to the server as a “teaching file”. Additionally, VistARad can launch a web browser to the same server, making its teaching file contents available. Only one MIRC server interface can be configured, at any given time, per diagnostic workstation. The MIRC server will not be hosted on the diagnostic workstation.

> More information on setting up the interfaces is available from Chapter 3 of the *VistA Imaging Installation Guide*.

## Chapter 13 Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Entry/Exit Logic

The VistA Imaging System contains no options that rely on entry or exit logic from other options.

#### Synchronization

#### Clinical, Diagnostic, and Background Processor Workstations

The VistA Imaging software installed on the VistA Hospital Information System must be synchronized with compatible versions of the software installed on the individual workstations.

#### DICOM Modalities and PACS

The main purpose of the VistA Imaging DICOM Gateway is to act as an interface between external equipment and the VistA Hospital Information System. For each gateway function, in order for that function to be operational, the equipment on both sides of the interface must be up- and-running. In order to test and verify the operational status of equipment, see the *VistA Imaging DICOM Gateway User Manual* for a description of the programs Ping and DICOM_Echo.

#### Radiology HL7 v2.1 Protocols

The VistA Imaging DICOM Gateway is dependent on Radiology protocols being active. VistA Imaging must be a subscriber to these protocols. Review the following protocols; the highlighted protocol is the VistA Imaging protocol subscriber. Please review the DICOM Installation manual in the section *VistA - PACS Radiology Interface Setup Instructions* for a step-by-step procedure to setup the protocols.

![](vista-imaging-system-technical-manual/123.png)

#### Radiology HL7 v2.4 Protocols

Currently HL7 Version 2.4 is the version of HL7 sanctioned for use in the VA enterprise and the version against which commercial PACS have been tested for conformance. Therefore, the v2.4 protocols will ordinarily be subscribed to by VistA Imaging in preference to the v2.1 protocols described in the previous section.

![](vista-imaging-system-technical-manual/124.png)

![](vista-imaging-system-technical-manual/125.png)

#### VistA Imaging ADT Protocols

> Beginning with the release of Patch MAG\*3.0\*49, VistA Imaging uses HL7 messages to communicate ADT (admission / discharge / transfer) events directly to commercial PACS. ADT information had formerly been sent from the VistA DICOM Gateway using customized DICOM protocols, which have since been deprecated.

> VistA Imaging generates and sends these messages through the VistA HL7 package using the following protocols.

![](vista-imaging-system-technical-manual/126.png)

![](vista-imaging-system-technical-manual/127.png)

#### Radiology Protocols (VistARad)

> VistA Imaging VistARad can be set to automatically prefetch archived images for prior radiology exams. Prefetch is activated by subscribing to the RA REG protocol—the VistARad client protocol is MAGJ PREFETCH SEND/ORM. Review the example RA REG protocol below; the bolded protocol is the VistARad protocol subscriber. The Installation Guide has a step-by-step procedure to set up the protocol.

Patient Movement Protocol (DICOM)

![](vista-imaging-system-technical-manual/128.png)

> The VistA Imaging DICOM gateway is dependent on the Patient Movement (DGPM MOVEMENT EVENTS) protocol being active. VistA Imaging must be a subscriber to this event protocol. The following is an example of this event protocol; the highlighted protocol is the Imaging protocol subscriber. ATTENTION: This is only pertinent if a VistA Imaging DICOM gateway configuration has been defined. Please review the DICOM Installation manual under section *VistA - PACS Radiology Interface Setup Instructions* for a step-by-step procedure to setup the protocols.

![](vista-imaging-system-technical-manual/129.png)

![](vista-imaging-system-technical-manual/130.png)

### VistARad Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistARad interfaces with the following components of VistA Imaging.

#### VistA Site Service

> VistARad will query the VistA Site Service if VistARad is configured to detect a local VistA Imaging Exchange (VIX) server. It may do this even if there is no local VIX available.

#### VistA Imaging Exchange (VIX) servers

> If a local VIX server is accessible, VistARad will query the local VIX for relevant patient exams & ancillary information from other remote sites, including those in the DoD. If configured for remote site monitoring, VistARad will also periodically query the VIX for exam list information from the configured monitored sites. Additional information on configuring VistARad for VIX- enabled reading and list monitoring is available in the “VistARad Settings” and “Monitoring Exam Lists of Remote Sites” sections of the VistARad User Guide.

This page is intentionally blank.

## Chapter 14 Package-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Imaging System does not contain any package-wide variables.

This page is intentionally blank.

## Chapter 15 Online Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Online Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Online help is available from the Help menu for Clinical Display, Clinical Capture, MagSys (clinical workstation configuration manager), Background Processor, Verifier, VistARad, TeleReader, TeleReader Configurator, and DICOM Importer II.

This page is intentionally blank.

## Chapter 16 Site-Specific Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Site-Specific Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Radiology Report Transcription Service

> Local routines that automatically upload radiology reports from a transcription service should be reviewed and/or modified to ensure that proper consideration has been made for VistA Imaging. When an image is captured via the DICOM Image Gateway and the radiology case number does not have an existing radiology report entry (in file \#74), then the VistA Imaging software creates a report stub entry for that case number with limited information. (See box below -- example of radiology report stub entry made by Imaging.) Please note that the stub report entry has an image pointer stored in the IMAGE field, no report status is on file and the activity log indicates that images were collected. The VistA Imaging System executes a Radiology Package API called CREATE^RARIC to create this entry. The RAD/NUC MED PATIENT file (#70) is also updated with the report pointer in the Report Text field.

> Imaging has experienced problems when the auto-upload routine updates the REPORT TEXT field (#17) in the RAD/NUC MED PATIENT file (#70). Often the problems result from the program not expecting the Report file entry to exist at the time of the upload. However, the DICOM image capture process guarantees that at the time the transcribed reports are uploaded to the system, a Report file entry already exists, although no Report <u>text</u> nodes exist. Differences in implementations of the local upload programs at various sites have led to other problems as well. Therefore, if your site uses such a program for uploading and/or updating the Radiology report, you must carefully review all aspects of its functionality in light of the changes introduced by the VistA Imaging System.

Example: Radiology Report stub entry made by the VistA Imaging application.

![](vista-imaging-system-technical-manual/131.png)

#### HL7 MESSAGE TEXT File (#772)

> VistA Imaging is a subscriber to the Radiology protocols that create HL7 messages. When Radiology protocols are executed, entries are created in the HL7 MESSAGE TEXT file (#772). The purging of this file is handled by the menu option for this application. Sites are requested to review the purging parameters for this file. Use menu option ‘Purge Message Text File Entries’ under the HL7 Main menu.

#### Incomplete DICOM Files Received on the DICOM Image Gateway

> During the processing of DICOM files on the DICOM image gateway, it is possible for a modality or a PACS interface to send an incomplete file (possibly just header information without the image information). The image processing routine will log these entries in a temporary file (M global) and check periodically to see if the entire file has been received. If, after an hour’s time span, the file is still incomplete, the entry is removed from the temporary file (M global) and the file is renamed by appending “\_incomplete” to the filename. These files do remain in the DICOM\IMAGE_IN directory and will require site personnel to research the possible failure. In addition, these files will require manual intervention for file maintenance (deletion). Please see the *VistA Imaging DICOM User Manual* for additional information.

## Chapter 17 Database Integrity Checking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA Imaging System performs database integrity checking at the system level and within various applications.

### VistA Imaging MAG SYS MENU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In the VistA Imaging system, the MAG SYS MENU has an Integrity Checker Menu with the following submenus:

- GM Global Move Inconsistency Report
- QA Pointer Inconsistency Report
- SC Scan Database for Integrity Issues

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Where</strong></th>
<th><strong>Means</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>GM</td>
<td><p>Global Move Inconsistency Report [MAG_IC_RPT_GM]</p>
<p>DESCRIPTION: Report from Imaging Integrity Check, limited to items required for Central Office</p>
<p>ROUTINE: RPT^MAGCRPT("CO")</p>
<p>UPPERCASE MENU TEXT: GLOBAL MOVE INCONSISTENCY REPO</p></td>
</tr>
<tr class="even">
<td>QA</td>
<td><p>Pointer Inconsistency Report [MAG_IC_RPT_QA]</p>
<p>DESCRIPTION: Report from Imaging Integrity Check, including all items required for Quality Assurance</p>
<p>ROUTINE: RPT^MAGCRPT("QA")</p>
<p>UPPERCASE MENU TEXT: POINTER INCONSISTENCY REPORT</p></td>
</tr>
<tr class="odd">
<td>SC</td>
<td><p>Scan Database for Integrity Issues [MAG_IC_SCAN] DESCRIPTION: Menu option to scan the Imaging database</p>
<p>EXIT ACTION: K MAGN100,MAGZ,VALID,Z ROUTINE: RPT^MAGGSQI(.Z,1E11)</p>
<p>UPPERCASE MENU TEXT: SCAN DATABASE FOR INTEGRITY IS</p></td>
</tr>
</tbody>
</table>

### Clinical Display Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Clinical Display Workstation User Manual* contains two references to Questionable Integrity (QI):

- A “Not Viewable” icon is displayed if the user attempts to view an image that has internal references that suggest some degree of integrity risk. For details, see the section Images That Are Not Viewable Due to an Error.
- An image that is blocked from view can be attributed to a number of reasons. One is if the image data does not pass the QI check, then the image is marked as QI. For details, see the section Blocked Images in the Abstracts Window.

> Additionally, see the *Clinical Display Workstation User Manual* section *Deleting Images with Questionable Integrity (QI Issues)* in *Appendix C: Deleting Images*.

### VistARad Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *VistARad User Guide* contains a reference to a “Severe Alert” icon that is displayed when a user attempts to view an exam and the system detects a data integrity problem with the exam. For details, see the section *Opening Exams*.

### Verifier Application in the Background Processor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The BP Verifier provides a report called the Imaging Patient Integrity Issues in the DFNError Log file, which displays integrity issues with patient data. For details, see Section *5.7.1.4 DFN Log File* in the *Background Processor User Manual*.

## Chapter 18 Remote Image Views

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Configuration for Remote Image Views

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Remote Image Views functionality uses a Network Location entry that points to the VistA Site Service to determine the server and port of remote VistA databases. This Network Location entry is present at all sites running Patch 45 or later. By default, this Network Location is enabled.

> The URL defined in the VistA Site Service Network Location must be accessible to all clients attempting to access remote images.

> Patch 111 provides the availability of the Broker Security Enhancement (BSE) for VistA Imaging clients. BSE is a token based authentication method that provides enhanced security over the previously used CAPRI login method.

> Patch 94 modifies remote image view functionality in Display and TeleReader to make use of BSE. The client will first use BSE when attempting to connect to remote sites. If BSE fails, the client will use the CAPRI remote site login. When CAPRI is used, the system will generate a log entry to track the usage of the CAPRI authentication method. Using the BSE or CAPRI remote login method does not affect the usability of the applications, and it is transparent to the user.

> The Kernel Team will release a patch to disable the CAPRI authentication method after Patch 94 is released. When the Kernel Team disables the CAPRI authentication method, only clients 94 and later will be able to connect to sites for remote image viewing.

#### Enabling/Disabling Remote Image Views for Site

> To enable/disable Remote Image Views for your entire site, you may do so by changing the Operational Status of the NETWORK LOCATION file (#2005.2). Setting the Operational Status to On-Line enables Remote Image Views for your entire site. Setting the Operational Status to Off-Line disables Remote Image Views for your entire site. Enabling and disabling this option does not prevent remote sites from accessing your data. This only prevents users at your local site from accessing remote data.

![](vista-imaging-system-technical-manual/132.png)

![](vista-imaging-system-technical-manual/133.png)

#### Updating VistA Site Service URL

> The remote image viewing capability uses a VistA Site Service to determine the server details of remote VistA0 systems. The following describes how to change the URL for this service if necessary.

![](vista-imaging-system-technical-manual/134.png)

## Chapter 19 Two-Facto Authentication (2FA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Two-Factor Authentication (2FA) Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> SSOi implemented by replacing the existing RPC Broker for those VistA Imaging applications that require VistA login credentials to access. The VistA Imaging login interface and workflow has changed from username and password to PIV card and PIN entry as part of the 2FA mandate. VistA Imaging components currently consume and reference a Delphi RPC Broker Development Kit (BDK) including a compiled BAPI32.DLL library. This RPC library exposes several procedure calls used to authenticate a user within a VistA application. As part of the VistA Imaging SSOi effort, we will be upgrading this library and BDK, (expected version XWB\*1.1\*65 currently in development and beta testing), which will have built-in integration to the IAM SSOi Secure Token Server (STS) authentication model including PIV/PIN prompt(s).

#### PIV/PIN Login

> Figures 1 and 2 represent the screens that will display during login with 2FA SSOi integration. The user must have a valid PIV card attached to their computer, select the corresponding identity certificate, and enter their PIN.

PIV Identity Certificate Selection Display![](vista-imaging-system-technical-manual/135.png)

PIV PIN Entry Display

![](vista-imaging-system-technical-manual/136.png)

### Implementation History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MAG\*3.0\*178 introduced 2FA for the Clinical Capture application, replacing username and password login process.

> MAG\*3.0\*181 introduced 2FA for the Clinical Display application, replacing username and password login process.

> MAG\*3.0\*182 introduced 2FA for the Telereader application, replacing username and password login process.

> MAG\*3.0\*184 introduced 2FA for the VistARAD application, replacing username and password login process.

> MAG\*3.0\*206 introduced 2FA for the Importer application, replacing username and password login process.

## Appendix A Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Clinical Workstation Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Error Message</strong></p>
</blockquote></th>
<th><strong>Cause(s)/Solutions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>You don’t have the proper Security Keys to capture LAB images.</p>
</blockquote></td>
<td><blockquote>
<p>The USE CAPTURE KEY field in the IMAGING SITE PARAMETERS file (#2006.1) has been turned on and the user has not been assigned the proper key. Please review the Security Key section in the <em>VistA Imaging Security Guide.</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Error in connecting to Server</p>
<p>\\servername\image\</p>
</blockquote></td>
<td><blockquote>
<p>Possible causes:</p>
</blockquote>
<ul>
<li><p>The workstation has not been set up properly.</p></li>
<li><p>The account used to access the server has not been given the proper security level or has not been set up properly.</p></li>
<li><p>The listed server is down.</p></li>
</ul>
<blockquote>
<p>Find the associated error number and use the Help | Error Code Lookup option in Imaging Display.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AutoUpdating is disabled. Network Configuration file doesn’t exist.</p>
</blockquote></td>
<td><blockquote>
<p>The MAGNET.ini file is not on the Network Update directory. Auto Update is not configured properly.</p>
</blockquote>
<ol type="1">
<li><p>Contact network administrator and request that a copy of the MAGNET.ini file be placed in the Network Update directory.</p></li>
<li><p>Review the VistA Imaging System Installation Guide for proper configuration of Auto Update.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AutoUpdating disabled. The network update directory doesn’t exist.</p>
</blockquote></td>
<td><blockquote>
<p>Cannot connect to the directory or it does not exist.</p>
</blockquote>
<ul>
<li><p>User does not have privileges to the distribution directory.</p></li>
<li><p>Workstation log-on profile does not connect to Network Update directory.</p></li>
<li><p>Contact network administrator.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AutoUpdating disabled. Workstation isn’t configured for Auto Updating.</p>
</blockquote></td>
<td><blockquote>
<p>No update directory in the MAG308.ini file under section SYS_AUTOUPDATE for variable DIRECTORY.</p>
<p>Run MAGASET.EXE from the Network Update directory. This will automatically define the DIRECTORY entry in the MAG308.ini file for the current workstation.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Error Message</strong></p>
</blockquote></th>
<th><strong>Cause(s)/Solutions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AutoUpdating canceled. No Updates available.</p>
</blockquote></td>
<td><blockquote>
<p>The MAGSETUP.EXE file does not reside in the Network Update directory.</p>
<p>Contact the network administrator and request a copy of the MAGSETUP.EXE file be placed on the Network Update directory.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Abstract not found.</p>
</blockquote></td>
<td><blockquote>
<p>Possible causes:</p>
</blockquote>
<ul>
<li><p>The abstract was removed from the server.</p></li>
<li><p>The abstract was not generated, or could not be written to the share.</p></li>
<li><p>Network problems.</p></li>
<li><p>Mapped Image share</p></li>
<li><blockquote>
<p>Permission to access the share is not granted. Diagnostic process and corrective action:</p>
</blockquote></li>
<li><p>Check file and folder permissions for the image shares.</p></li>
<li><p>Check to see if the files exist on the shares.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ERROR_ACCESS_ DENIED</p>
</blockquote></td>
<td><blockquote>
<p>Possible causes:</p>
</blockquote>
<ul>
<li><p>Account or share permissions are not set up properly.</p></li>
<li><p>Account password was changed on the server, but not updated in the IMAGING SITE PARAMETERS file (#2006.1).</p></li>
</ul></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Error connecting to server.</p>
</blockquote></td>
<td><blockquote>
<p>Possible causes:</p>
</blockquote>
<ul>
<li><p>Incorrect configuration. Diagnostic process and corrective action:</p></li>
<li><blockquote>
<p>Check for error number in the message history window. Look it up using the Error Lookup option on the Imaging Display help menu.</p>
</blockquote></li>
<li><blockquote>
<p>Use ping or tracert to check the availability of the file server.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Error Message</strong></p>
</blockquote></th>
<th><strong>Cause(s)/Solutions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>0 Images on file.</p>
</blockquote></td>
<td><blockquote>
<p>Possible causes:</p>
</blockquote>
<ul>
<li><p>Normal condition.</p></li>
</ul>
<blockquote>
<p>Diagnostic process and corrective action:</p>
</blockquote>
<ul>
<li><p>This refers to images, not EKGs! A patient can have one without the other. Check "user preferences" to see if "always display EKG window" is selected. Click the EKG button to display the EKGs.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><blockquote>
<p>The File Does Not Exist - Notify IRM.</p>
</blockquote></td>
<td><blockquote>
<p>Possible causes:</p>
</blockquote>
<ul>
<li><p>Missing or inaccessible file. Diagnostic process and corrective action:</p></li>
<li><blockquote>
<p>Check to see if the file pointed by the database exist and is accessible.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Launching Imaging from CPRS causes RPC Broker dialog for access/verify code.</p>
</blockquote></td>
<td><blockquote>
<p>Possible Causes:</p>
</blockquote>
<ul>
<li><p>Incorrect configuration. Diagnostic process and corrective action:</p></li>
<li><blockquote>
<p>AutoSignon or multiple signon is not enabled for the site (KERNEL SYSTEM PARAMETERS file (#8989.3)) or</p>
</blockquote></li>
</ul>
<blockquote>
<p>the user (NEW PERSON file (#200)).</p>
</blockquote>
<ul>
<li><blockquote>
<p>DEFAULT AUTO SIGN-ON cannot be set to “Disabled” in Kernel site parameters file.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Error Accessing Group Image - See VistA Error Log.</p>
</blockquote></td>
<td><blockquote>
<p>Possible causes:</p>
</blockquote>
<ul>
<li><p>Database inconsistency. Diagnostic process and corrective action:</p></li>
<li><blockquote>
<p>This error is found on the clinical display when you try to delete an "Abstract not Found" entry. The software identifies this entry as a group image and because you cannot expand the group, it cannot be deleted.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Error Message</strong></p>
</blockquote></th>
<th><strong>Cause(s)/Solutions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>No MUSE Servers available.</p>
</blockquote></td>
<td><blockquote>
<p>Possible causes:</p>
</blockquote>
<ul>
<li><p>No MUSE servers are configured in the Network Location file (#2005.2).</p></li>
<li><p>All MUSE servers in the Network Location file are configured as off-line.</p></li>
</ul>
<blockquote>
<p>Diagnostic process and corrective action:</p>
</blockquote>
<ul>
<li><p>Add the MUSE Servers to the Network Location file.</p></li>
<li><p>Bring the MUSE servers back On-Line in the Network Location file.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><blockquote>
<p>No MUSE Servers available. Select a failed connection to see the error code.</p>
</blockquote></td>
<td><blockquote>
<p>Possible causes:</p>
</blockquote>
<ul>
<li><p>The application failed to connect to the all of the MUSE Servers.</p></li>
<li><blockquote>
<p>MUSE servers are down. Diagnostic process and corrective action:</p>
</blockquote></li>
<li><p>Click on a specific connection to see the error details.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>No Muse EKGs on File for this patient</p>
</blockquote></td>
<td><blockquote>
<p>Possible causes:</p>
</blockquote>
<ul>
<li><p>Patient ID (SSN) entered does not match MUSE patient ID.</p></li>
<li><blockquote>
<p>The Patient has no Muse EKGs on file. Diagnostic process and corrective action:</p>
</blockquote></li>
<li><p>Verify that the entered patient ID (SSN) is identical in the MUSE and VistA databases.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Error connecting to MUSE Server</p>
<p>\\&lt;ServerName&gt;\</p>
<p>&lt;ServerShare&gt;: status =53</p>
</blockquote></td>
<td><blockquote>
<p>Possible causes:</p>
</blockquote>
<ul>
<li><p>The network path was not found.</p></li>
<li><p>Permission problem on share.</p></li>
<li><p>MUSE server down.</p></li>
</ul>
<blockquote>
<p>Diagnostic process and corrective action:</p>
</blockquote>
<ul>
<li><p>Be sure you can ping the server.</p></li>
<li><p>Ensure that the Physical Reference field in the Network Location file (#2005.2) is defined correctly.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Error Message</strong></p>
</blockquote></th>
<th><strong>Cause(s)/Solutions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Error connecting to MUSE Server</p>
<p>\\&lt;ServerName&gt;\</p>
<p>&lt;ServerShare&gt;: status =104</p>
</blockquote></td>
<td><blockquote>
<p>Possible causes:</p>
</blockquote>
<ul>
<li><p>Error message displayed when user selects a failed connection in the EKG selection list. The MUSE API flag is not enabled.</p></li>
</ul>
<blockquote>
<p>Diagnostic process and corrective action:</p>
</blockquote>
<ul>
<li><p>This requires a call to GE so they can enable the API by installing a VOL000\system\sysinf\MUSEAPI.FIX file.</p></li>
<li><p>If this file was created with Notepad, be sure that it is not named MUSEAPI.FIX.TXT. Notepad adds a .txt extension when it creates a file.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Invalid File : MUSEAPI.DLL Call IRM</p>
<p>to get an updated file.</p>
</blockquote></td>
<td><blockquote>
<p>Possible causes:</p>
</blockquote>
<ul>
<li><blockquote>
<p>The MUSE API files were not installed correctly.</p>
</blockquote></li>
<li><p>The MUSE API files are not installed. Diagnostic process and corrective action:</p></li>
<li><blockquote>
<p>Call IRM for help</p>
</blockquote></li>
<li><blockquote>
<p>Reinstall VistA Imaging.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

### Troubleshooting General Startup Network Connection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Check all the online VistA Imaging Tier 1 shares and Tier 2 shares by one of the following means to determine if the BP has access to the folders/files on the shares. There are several methods to test the connectivity:

1.  From the Main BP window, select the View \> Server Size option. The free space should display for each share.

Main BP Window “View” Menu Options

![](vista-imaging-system-technical-manual/137.png)

2.  Using Windows Explorer on the destination device (Image cluster or Windows-based Jukebox server), show the properties of the VistA Imaging Tier 1 shares and Tier 2 shares.

The VHAxxxIA account that is used to log into the BP Server should have READ/WRITE access to both the shares and folders/files on those shares.

> **NOTE:** For sites using the Archive Appliance (AA), contact the HP Expert Center.

3.  Open a DOS window. At the command prompt type *dir [<u>\\server\share</u>](file://server/share)* (the server could be a cluster server or the jukebox server). Traverse down a couple folders under the main level the folders/files should be visible
4.  If any of these methods fail, open a DOS window and use the DOS *ping* command to see if the server is accessible on the network.
5.  If the server is accessible, try mapping the share thru Windows Explorer. Explorer will display any error messages. If the server is not accessible, contact the network admin to troubleshoot.

#### Broker Failures

When the connection to the Broker fails:

- Verify the PORT and Server are correct in the registry
- Close and restart the application.
- Open a DOS window and use the *ping* command to see if the VistA server is available
- Verify that the listener is running in VistA
- Validate that the Access/Verify codes have not expired.
- Check the security on the Access/Verify account. Make sure:
  - The MAG SYSTEM security key is assigned
  - The All MAG\* RPC's \[MAG WINDOWS\]menu option is assigned

#### Not Enough Server Cache

This message indicates that:

- The share on the server is not accessible. Follow the steps in section *[0](#troubleshooting-general-startup-network-connection) [Network Connection](#troubleshooting-general-startup-network-connection)* to troubleshoot.
- The free space on the Image shares is below the % Server Reserve.
- Disable the Auto Write Location Update option.
- Set the write location manually to a share with cache space available.
- If no share has adequate free space, create a second BP Server and manually launch a Purge (in Error! Reference source not found. Error! Reference source not found.) to run on all shares. When the Purge has run and generated free space on a share, set the Write location manually to that share.

#### Not Enough Process Memory

Close all the applications and reboot the server. If the problem persists, contact the National Helpdesk.

#### Not Enough Write Cache Available

This message refers to the DiskXtender cache on the jukebox and indicates there is no free space on the jukebox share, or for Archive Appliance sites a possible space issue exists.

- Verify the share is accessible. Follow the steps in section *[0](#troubleshooting-general-startup-network-connection) [Network](#troubleshooting-general-startup-network-connection) [Connection](#troubleshooting-general-startup-network-connection)* to troubleshoot.
- Click the Extended Drive in DiskXtender to see if there is free space available. Also, use Windows Explorer on the JB server to see if Windows is properly reporting free space.
- Check the Move Group within the DiskXtender application to see if there are platters with available space. If not, add additional optical platters to the Move Group. See the *DiskXtender User Manual*.
- Run a Drive Scan on the share. See the *DiskXtender User Manual*.

#### Queue Processor Startup

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 30%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Create Process failed'+ProgramName</td>
<td>A system error occurred staring the process</td>
<td>Follow your local, VISN, or regional procedures for problem resolution/escalation</td>
</tr>
<tr class="even">
<td><p>Increment <em>queue_name</em></p>
<p>Ptr^Failed</p></td>
<td><p>The QUEUE POINTER (#1) in the IMAGE BACKGROUND QUEUE POINTER file</p>
<p>(#2006.031) in VistA could not be updated</p></td>
<td>On the main BP window, use the Edit &gt; Refresh Queue Counts to correct the current counts. Close the BP and restart the application.</td>
</tr>
<tr class="odd">
<td>Initialization Failure^Log Files at: C:\Program Files\Vista\Imaging\BackprocLo g\BackProc\BPError.log</td>
<td>Log file could not be created</td>
<td>Check permissions on the log folder</td>
</tr>
<tr class="even">
<td>RAID groups not properly configured</td>
<td>An active RAID Group has no online shares</td>
<td><p>Make sure online RAID Group has online shares.</p>
<p>Use the Network Location Manager to reset your RAID groups</p></td>
</tr>
<tr class="odd">
<td>Requeue Failure trying to Requeue:</td>
<td>An attempt to re-queue a failed queue entry failed</td>
<td>Use the Queue Manager and step past the queue entry. Determine the problem with the entry that would not re-queue.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 30%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>SetTime Handle – Destin: C:\Program Files\Vista\Imaging\BackprocLo g\BackProc\BPError.log</p>
<p>Access is Denied</p></td>
<td>Could not write the Access Date on the log file</td>
<td>Check the file permissions on the log folder listed.</td>
</tr>
<tr class="even">
<td><p>The Background Processor client software is version <em>n.n.n.n</em>.</p>
<p>VistA Imaging Host system has version <em>m</em> installed. Please update to compatible client and host software. Shutting down the Background Processor...</p></td>
<td>The client software that is installed does not match the KIDS version installed on VistA.</td>
<td>Install the correction version of the KIDS and client software.</td>
</tr>
<tr class="odd">
<td>The Patch 135 KIDS install on the VistA host system is required for this Version of the: <em>site name</em> BP Queue Processor</td>
<td>The KIDS file for this most recent patch has not been installed in VistA.</td>
<td>Install the KIDS file on VistA.</td>
</tr>
<tr class="even">
<td>The Site parameter context could not be determined. The application will terminate.</td>
<td>The PLACE global is corrupt</td>
<td>Follow your local, VISN, or regional procedures for problem resolution/escalation.</td>
</tr>
<tr class="odd">
<td>![](vista-imaging-system-technical-manual/138.png)</td>
<td>The Broker is not properly configured in the registry of this server.</td>
<td><p>Edit the registry on this server to meet the connection requirements on the host server with proper host server name and port number.</p>
<p>Note: on 64 bit OS the hive is [HKEY_LOCAL_MACHINE\SO</p>
<p>FTWARE\Wow6432Node\Vista\B roker\Servers]</p></td>
</tr>
<tr class="even">
<td>This server is not yet configured for BP queue task processing!</td>
<td>There is either no BP Server name with this network name in the BP Server file (#2006.8) or there are no task(s) assigned to this server</td>
<td>Create a BP Server through the GUI and assign tasks to it BP Servers menu/tab</td>
</tr>
<tr class="odd">
<td>InitLogFile: procedure NewCreationDate | SetFileTime Failed <em>WIN32_Error</em></td>
<td>Log File Initialization error</td>
<td>See above The log files should not have a local drive in the BP Server Parameters. The designated path should be a network share. Note: The Computer name is automatically set by the application software. Setting the server name in the parameter will create a confusing duplicate descendant server tree on the Network share.</td>
</tr>
</tbody>
</table>

### Runtime

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 30%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0^Accusoft Control creation error : &lt; <em>error message</em> &gt;</td>
<td>The Import API uses the AccuSoft Image Gear Toolkit to create the watermarked image. If an error occurs during the creation of AccuSoft controls, the error message displays describing the error.</td>
<td>The AccuSoft controls are installed during MAG*3.0*135 installation. If this error message occurs, contact the VistA Imaging system manager.</td>
</tr>
<tr class="even">
<td>0^Image is missing from input data.</td>
<td>The image to be watermarked is not in the Import Queue Data.</td>
<td>Check the IMAGE file (#2005) to see if the data is corrupt.</td>
</tr>
<tr class="odd">
<td>0^Watermark failure : &lt;<em>error message</em>&gt;</td>
<td>The process of burning the “Rescinded” watermark onto the image file failed.</td>
<td><p>The AccuSoft ToolKit could not create the watermarked image.</p>
<p>Check if the rescinded bitmap exists in the image directory <strong>C:\Program Files\vista\Imaging\Bmp\MagRe scinded.bmp</strong>.</p>
<p>You may need to reinstall MAG*3.0*135 to correct AccuSoft ImageGear problems.</p></td>
</tr>
<tr class="even">
<td>An Abstract for this file is on the Jukebox, a JBTOHD is being queued</td>
<td>ABSTRACT - The abstract pointer on the Tier 1 is empty. The abstract will be copied from the jukebox</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Could not complete</td>
<td>DELETE - file could not be deleted</td>
<td><p>Check permissions on Tier 1</p>
<p>share</p></td>
</tr>
<tr class="even">
<td>Could not complete/Requeued</td>
<td>DELETE - file could not be deleted</td>
<td><p>Check permissions on Tier 1</p>
<p>share</p></td>
</tr>
<tr class="odd">
<td>Current Tier 1 Shares^Exception: No RAID group Assigned</td>
<td>The Tier 1 share must be assigned to a RAID Group</td>
<td><p>On the BP main window, use Edit</p>
<p>&gt; Network Location Manager to assign the Tier 1 share(s) to a RAID Group.</p></td>
</tr>
<tr class="even">
<td><p>False Positive Copy f<em>ilename(Source)</em>,</p>
<p><em>filenames source file size</em>, <em>file size(jukebox)</em></p></td>
<td>File sizes on source and destination don’t match. File not copied.</td>
<td>Determine if images are for different patients</td>
</tr>
<tr class="odd">
<td>File copied was of size zero</td>
<td>IMPORT - The file size is zero</td>
<td>Resend image from import source</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>File of size zero created then deleted</td>
<td>MAKEABS - file of zero length was created by Mag_MakeAbs.exe. It was deleted.</td>
<td>Follow your local, VISN, or regional procedures for problem resolution/escalation</td>
</tr>
<tr class="even">
<td>File was not found</td>
<td>IMPORT - file does not exist on the image share</td>
<td>Resend image from import source</td>
</tr>
<tr class="odd">
<td><em>filename</em> Source file does not exist.</td>
<td>Could not find source file</td>
<td>Run Verifier to correct VistA pointers</td>
</tr>
<tr class="even">
<td><em>fileshare</em>: Cannot connect to the Export Share.</td>
<td>EXPORT - Cannot map to the remote share</td>
<td>Check for network connectivity. Check permissions..</td>
</tr>
<tr class="odd">
<td>ForceDirectories failed:</td>
<td>DELETE - could not create directory on jukebox share</td>
<td>Check permissions on jukebox share</td>
</tr>
<tr class="even">
<td>Image File type: <em>filename.ext</em> is an Unsupported Format</td>
<td>ABSTRACT - The Full file is not a supported Imaging file type. So the abstract cannot be created.</td>
<td>Examine the "foreign" file and determine if the extension was misnamed.</td>
</tr>
<tr class="odd">
<td>Invalid Imaging Network Username or Password.</td>
<td>The BP processor operator does not have write permissions on Tier 1, Tier 2, the Network Log file share, or the IMPORT share.</td>
<td>Check permissions on the share the write share associated with this error.</td>
</tr>
<tr class="even">
<td>Jukebox is not available: <em>filepath Volume label</em></td>
<td>Tier 2- the jukebox share is not available</td>
<td>Ping the jukebox server. Check the jukebox share permissions.</td>
</tr>
<tr class="odd">
<td>Jukebox sourcefile unavailable</td>
<td>JBTOHD - There is no abstract file on the jukebox. The abstract pointer in VistA is not set.</td>
<td>None</td>
</tr>
<tr class="even">
<td><p>JUKEBOX: <em>queue _pointer</em></p>
<p>^f<em>ile_extension</em> Not copied</p></td>
<td>JUKEBOX - Alternate file extension (i.e. .TXT) was not copied</td>
<td>Check file permissions</td>
</tr>
<tr class="odd">
<td>Login Message^Pausing 3 minutes and will then retry</td>
<td>AUTOLOGIN - could not relog into the Broker</td>
<td>Check for network connectivity.</td>
</tr>
<tr class="even">
<td>Login Message^Silent Login attempt failed!</td>
<td>AUTOLOGIN - could not relog into the Broker</td>
<td>Check for network connectivity.</td>
</tr>
<tr class="odd">
<td>Make AbstractError / abs is already present</td>
<td>ABSTRACT- file already exists at the Tier 1 location specified in VistA</td>
<td>None</td>
</tr>
<tr class="even">
<td>Make AbstractError / f<em>ilename</em></td>
<td><p>MAKEABS- the</p>
<p>Mag_MakeAbs.exe could not create the abstract file</p></td>
<td>Follow your local, VISN, or regional procedures for problem resolution/escalation</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NetConError Using User credentials <em>WIN32_Error</em></td>
<td>GCC - Could not logon to the remote location with the Username/Password in VistA</td>
<td><p>Correct the Username/Password for the</p>
<p>GCC location in VistA</p></td>
</tr>
<tr class="even">
<td>NetConError,'There is no password associated with this Network Location: <em>share_name</em></td>
<td>GCC - The password field is empty for this Network Location</td>
<td>Enter a password for this GCC location</td>
</tr>
<tr class="odd">
<td>No Image file entry was created!</td>
<td>IMPORT - an IEN was not created in the image file</td>
<td>Resend image from import source</td>
</tr>
<tr class="even">
<td><p>No Jukebox sourcefile available</p>
<p>/ Attempting Abstract Queue</p></td>
<td>JBTOHD - There is no abstract file on the jukebox. The abstract pointer in VistA is set. The Queue Processor will attempt to make on from the Full or BIG file.</td>
<td>None</td>
</tr>
<tr class="odd">
<td>No Tracking ID IMPORT failed</td>
<td>IMPORT - unique Tracking ID parameter is missing from IMPORT</td>
<td><p>Resend image from import source.</p>
<p>Use the Queue Manager to check the Import queue Properties for failed IMPORTS.</p></td>
</tr>
<tr class="even">
<td><p>Problem renaming log file:</p>
<p><em>filename</em></p></td>
<td>Could not rename log file to a versioned copy</td>
<td>Check permissions on the existing folder/files</td>
</tr>
<tr class="odd">
<td><em>queue_pointer</em> '^Size Mismatch <em>queue_type</em> copy not overwritten.</td>
<td>File sizes on source and destination don’t match. File not copied.</td>
<td>Determine if images are for different patients</td>
</tr>
<tr class="even">
<td>SetFileTime Failed</td>
<td>Could not set Access date on the log file.</td>
<td>None</td>
</tr>
<tr class="odd">
<td>The BP Queue executed a scheduled RAID Group Advance</td>
<td>The Queue Processor performed a the scheduled RAID Group Advance to the next group with adequate free space per the site parameter configuration</td>
<td>Verify that the tape backup schedule are synchronized with this Tier 1 write location update</td>
</tr>
<tr class="even">
<td>The BP Queue executed an automatic RAID Group Advance</td>
<td>The Queue Processor performed an automatic RAID Group to the next group with adequate free space per the site parameter watermark configuration</td>
<td>Verify that the tape backup schedule are synchronized with this Tier 1 write location update</td>
</tr>
<tr class="odd">
<td>The jukebox copy: <em>filename</em> does not exist -- attempting a copy...</td>
<td>DELETE -Could not find the file on jukebox shares. Try to copy from Tier 1 shares to jukebox</td>
<td>None</td>
</tr>
<tr class="even">
<td>The RAID share is not on-line</td>
<td>IMPORT - The Tier 1 share is not available</td>
<td>Check the permissions on the image share indicated</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>The <em>src_filename</em> to</p>
<p><em>dest_filename</em> copy failed.</p></td>
<td>EXPORT - file could not be copied</td>
<td>Check for network connectivity. Check permissions.</td>
</tr>
<tr class="even">
<td><p>The VistA cache file: <em>filename</em></p>
<p>not found</p></td>
<td>DELETE -Could not find the file on Tier 1share to delete</td>
<td>None</td>
</tr>
<tr class="odd">
<td>This Server is not yet configured!</td>
<td>A BP Server has not been associated with this server.</td>
<td>Create a BP Server for this processor</td>
</tr>
<tr class="even">
<td>Unable to copy to the Jukebox: Not enough write cache available</td>
<td>JUKEBOX - The Tier 2 share is not available or is full</td>
<td>Add new platters to the jukebox. Determine why the Tier 2share is full. Possibly add new platters to the jukebox.</td>
</tr>
<tr class="odd">
<td>Zero size <em>queue_type</em> copy NOT overwritten</td>
<td>Zero size file on the destination could not be overwritten</td>
<td>Remove zero size file</td>
</tr>
<tr class="even">
<td>No Connection to VISTA</td>
<td>The VistA Access and Verify codes of the user or service account are invalid.</td>
<td>Update the Access and Verify codes on the BP Site parameter window.</td>
</tr>
</tbody>
</table>

#### #### Verifier Start/Run

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>About to exit without processing: 0</td>
<td>There are no IEN records within the range.</td>
<td>Choose another IEN range</td>
</tr>
<tr class="even">
<td>Broker Connection to server could not be established!</td>
<td>VistA RPC Broker is not currently in a listening state OR the application has timed out.</td>
<td>Close the application and restart. Check with the VistA system manager for the status of the Broker listener.</td>
</tr>
<tr class="odd">
<td><p>CC:createcontext</p>
<p>("MAG WINDOWS") could not be established!</p></td>
<td><p>The user does not have All MAG* RPC's [MAG</p>
<p>WINDOWS] menu option assigned.</p></td>
<td>Assign the user this menu option.</td>
</tr>
<tr class="even">
<td>lbCacheShare.items.Count &lt; 1: MAGQ SHARES</td>
<td>There are no online, non-router VMC shares.</td>
<td>Use the Queue Processor’s Network Location Manager to check/add the shares.</td>
</tr>
<tr class="odd">
<td>Invalid Input Range</td>
<td>The From and To values entered in the Range are not correct (e.g. Start: 0 End: 0).</td>
<td>Enter a valid <em>From</em> and <em>To</em> range.</td>
</tr>
<tr class="even">
<td>jukebox shares are not setup</td>
<td>The Tier 2 share(s) are offline or don’t exist in the NETWORK LOCATION file (#2005.2).</td>
<td>Create/Edit the Tier 2 shares in the Network Location Manager on the Queue Processor.</td>
</tr>
<tr class="odd">
<td>This workstation is not currently setup as a Background Processor.</td>
<td>There is no BP Server set up for this machine.</td>
<td>Use the option <em>BP Servers</em> on the Queue Processor to register this server.</td>
</tr>
<tr class="even">
<td>Verifier client software is version nnn. VistA Imaging Host software is version mmm. Please update to compatible client and host software. Shutting down Verifier...</td>
<td>The version of the KIDS file installed on VistA does not match the executable version on the workstation.</td>
<td>Install the latest KIDS and client software.</td>
</tr>
<tr class="odd">
<td>VistA shares are not setup</td>
<td>The image share(s) are offline or don’t exist in the NETWORK LOCATION file (#2005.2).</td>
<td>Create/Edit the shares in the Network Location Manager on the Queue Processor.</td>
</tr>
</tbody>
</table>

#### Output HTML Messages

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Aggregate JB Copy Error:</td>
<td>Could not copy from alternate Tier 2 to the current Tier 2 Write location.</td>
<td>Check permissions</td>
</tr>
<tr class="even">
<td>Abs to JB:</td>
<td>Abstract has been created and copied to the jukebox</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Aggregate Function - Enabled</td>
<td>Software is enabled to copy files from secondary jukebox, if necessary</td>
<td>None</td>
</tr>
<tr class="even">
<td>BIG Aggregate Failed</td>
<td>Could not copy BIG file from secondary jukebox</td>
<td>Check file existence/permissions</td>
</tr>
<tr class="odd">
<td>Create Process failed</td>
<td>Could not create process on VistA for Verifier</td>
<td>Check Error Trap</td>
</tr>
<tr class="even">
<td>Empty FBIG node</td>
<td>"FBIG" node has no pointers set in IMAGE file (#2005) record.</td>
<td>Check shares for existence of BIG file. If not found, restore BIG file from backup tapes.</td>
</tr>
<tr class="odd">
<td>File of size zero created then deleted</td>
<td><p>Abstract file created of size zero. Then it is deleted.</p>
<p>(Likely corruption of BIG and/or TGA file)</p></td>
<td>None</td>
</tr>
<tr class="even">
<td>FULL Aggregate Failed</td>
<td>Could not copy FULL file from secondary Tier 2.</td>
<td>Check file existence/permissions</td>
</tr>
<tr class="odd">
<td>FULL Aggregate Failed</td>
<td>Could not copy FULL file from secondary Tier 2.</td>
<td>Check file existence/permissions</td>
</tr>
<tr class="even">
<td>Images JB share is OFF-LINE:</td>
<td>Tier 2 is offline</td>
<td>Set Tier 2 back ONLINE</td>
</tr>
<tr class="odd">
<td>Make AbstractError</td>
<td><p>Abstract file could not be created from TGA/BIG</p>
<p>(BIG/TGA not found or image file corruption).</p></td>
<td>Check shares for existence of BIG/TGA file. If not found, restore BIG/TGA file from backup tapes.</td>
</tr>
<tr class="even">
<td>New Abs to CWL</td>
<td>An abstract file has been created and copied to the current write image share</td>
<td>None</td>
</tr>
<tr class="odd">
<td>No ABS file VC Ptr Cleared</td>
<td>Abstract file not found on the Image share</td>
<td>None</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>No ABS file VC Share OFF- Line</td>
<td>Image share is offline at location of abstract file</td>
<td>Set share back online and re-run Verifier</td>
</tr>
<tr class="even">
<td>No ABS JB Files</td>
<td>No abstract file found on Tier 2</td>
<td>Check shares for existence of ABS file. If not found, restore ABS file from backup tapes</td>
</tr>
<tr class="odd">
<td>No Acquisition Site in Image file</td>
<td>The ACQUISITION SITE field #100 in the IMAGE file (#2005) is missing. This is a required field.</td>
<td><p>Contact IRM</p>
<p>Update the field with the proper site ID.</p></td>
</tr>
<tr class="even">
<td>No FULL JB Files</td>
<td>FULL file not found on the Tier 2</td>
<td>Check shares for existence of Full file. If not found, restore Full file from backup tapes</td>
</tr>
<tr class="odd">
<td>No FULL VC Files</td>
<td>FULL file not found on the Tier 1 share</td>
<td>None</td>
</tr>
<tr class="even">
<td>No jukebox BIG Files</td>
<td>BIG file not found on the Tier 2</td>
<td>Check shares for existence of BIG file. If not found, restore BIG file from backup tapes.</td>
</tr>
<tr class="odd">
<td>No jukebox FULL Files</td>
<td>FULL file not found on the Tier 2</td>
<td>Check shares for existence of Full file. If not found, restore Full file from backup tapes.</td>
</tr>
<tr class="even">
<td>No Network References</td>
<td>No IMAGE file (#2005) record exists for this image</td>
<td>Re-import image thru the Capture client</td>
</tr>
<tr class="odd">
<td>No Network References: Archived Image</td>
<td>Image has been archived, resides in the IMAGE AUDIT file (#2005.1)</td>
<td>None</td>
</tr>
<tr class="even">
<td>No VC BIG Files</td>
<td>Could not find the BIG file on the Tier 1 share</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Not Certed</td>
<td><p>Could not find/create file type on</p>
<p>Tier 2</p></td>
<td>Check shares for existence of BIG file. If not found, restore BIG file from backup tapes.</td>
</tr>
<tr class="even">
<td>Problem rename log file:</td>
<td>Permission problem with log file</td>
<td>Set WRITE permissions set on share/folder/file for Windows login account.</td>
</tr>
<tr class="odd">
<td>Text file Patient ID not in VistA</td>
<td>Could not locate patient ID in VistA</td>
<td>Contact IRM</td>
</tr>
<tr class="even">
<td>TXT to BIG VC</td>
<td>Copy TXT file to same share as BIG file</td>
<td>None</td>
</tr>
<tr class="odd">
<td>TXT to FULL VC</td>
<td>Copy TXT file to same share as FULL file</td>
<td>None</td>
</tr>
<tr class="even">
<td colspan="3"><strong>"Check Text" Option Messages</strong></td>
</tr>
<tr class="odd">
<td>Text File Corruption Error Type 1:</td>
<td>Text file is binary or unreadable</td>
<td>Restore file from Tier 2/backup tapes</td>
</tr>
<tr class="even">
<td>Cannot determine Text file type:</td>
<td>Foreign text file was not likely generated on the image gateway</td>
<td>Restore file from Tier 2/backup tapes</td>
</tr>
<tr class="odd">
<td>Text File Corruption Error Type 2:</td>
<td>Text file is ASCII but has unprintable characters or truncated</td>
<td>Restore file from Tier 2/backup tapes</td>
</tr>
<tr class="even">
<td>Text/Image DFN Mismatch:</td>
<td>Patient ID in text file does not match that in VistA</td>
<td>Future utility patch</td>
</tr>
</tbody>
</table>

| Message                   | Explanation                                                          | Action                              |
|-------------------------------|--------------------------------------------------------------------------|-----------------------------------------|
| Text/Image SOP/UID Mismatch   | The Series Instance UID in the text file does not match the one in VistA | Future utility patch                    |
| Text/Image Study/UID Mismatch | The Study Instance UID in the text file does not match the one in VistA  | Future utility patch                    |
| Text/Image UID Mismatch       | SOP and/or Study UID are/is blank in text file                           | Future utility patch                    |
| Updated Text file             | Text file has been edited                                                | Validate file has been copied to Tier 2 |
| No SSN Found                  | Patient ID field missing in text file                                    | Future utility patch                    |

#### Integrity Messages on Patient Data

There are integrity issues that will prevent their respective images from being displayed and others that will not impact the viewing. See Appendix C for sample output.

#### Conditions Preventing Viewing

An integrity error message will be generated when the image is retrieved for viewing on these conditions and the patient image will not be viewable until the condition is corrected or the user has the proper key to view these images.

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>No Image Ptr in AP</td>
<td><blockquote>
<p>The Clinical Association Report (AP) for this image does not contain an image entry that points back to this image.</p>
</blockquote></td>
<td>Future utility patch</td>
</tr>
<tr class="even">
<td>GP has no images</td>
<td>Image series that does not contain any images. Group Parents (GP) are containers for an Image series. A group parent with NO group objects (GO) is an invalid condition.</td>
<td>Future utility patch</td>
</tr>
<tr class="odd">
<td>Conflicting AP &amp; Image DFNs</td>
<td>The patient file reference (DFN) in the Clinical Association Report (AP) does not match the DFN in the IMAGE file (#2005).</td>
<td>Future utility patch</td>
</tr>
<tr class="even">
<td>Invalid Image Ptr to AP</td>
<td>The Clinical Association Report (AP) has image references that are not in the IMAGE file (#2005).</td>
<td>Future utility patch</td>
</tr>
<tr class="odd">
<td>Conflicting GP and GO DFN</td>
<td>The patient file reference (DFN) in the Group Parent (GP) is not the same as the DFN in the Image entry.</td>
<td>Future utility patch</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>GP &amp; GO AP Mismatch</td>
<td>The Group Parent and Group Object pointer references to a Clinical Association Report (AP) do not match.</td>
<td>Future utility patch</td>
</tr>
<tr class="even">
<td>GP Missing GO Ptr</td>
<td>The Group Object multiple of the referenced Group Parent does not reference this group object.</td>
<td>Future utility patch</td>
</tr>
<tr class="odd">
<td>No AP Mult Ptr</td>
<td><p>This Image entry does not have the clinical application (AP) image multiple entry number specified. The IMAGE file (#2005).record is missing the <em>PARENT DATA FILE IMAGE</em></p>
<p><em>POINTER</em> (#17) for a Clinical Association Report (AP).</p></td>
<td>Future utility patch</td>
</tr>
<tr class="even">
<td>GO DFN mismatches</td>
<td>Some image file Group Objects have different PATIENT references (DFN).</td>
<td>Future utility patch</td>
</tr>
<tr class="odd">
<td>Image entry is structurally abnormal</td>
<td>The normal structure that distinguishes Image entry Group Parents (GP), Group Objects (GO), and Non-Group image (NG) is corrupt.</td>
<td>Future utility patch</td>
</tr>
<tr class="even">
<td>Missing Group Objects</td>
<td>The Group Parent has Group Object references that are missing.</td>
<td>Future utility patch</td>
</tr>
<tr class="odd">
<td>DFN Mismatches in AP Image Mult</td>
<td>The Clinical Association Report (AP) references a Group Parent that has image files with a different PATIENT reference (DFN) than the report.</td>
<td>Future utility patch</td>
</tr>
</tbody>
</table>

#### Conditions Allowing Viewing

The following integrity issues will not prevent their respective images from being displayed. These are informational messages.

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>No AP Ptr</td>
<td>The IMAGE file (#2005) record is missing the PARENT DATA FILE# (#16) for a Clinical Association Report (AP). This Image does not have the entry in the clinical application (AP) specified.</td>
<td>Future utility patch</td>
</tr>
<tr class="even">
<td>No AP entry Ptr</td>
<td><p>This Image does not have the entry in the clinical application (AP) specified. The IMAGE file (#2005) record is missing the <em>PARENT GLOBAL ROOT DO</em></p>
<p><em>(#17)</em> for a Clinical Association Report (AP).</p></td>
<td>Future utility patch</td>
</tr>
</tbody>
</table>

#### Purge

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Broker Reconnection failed</td>
<td>Auto login after a Broker disconnect failed</td>
<td>Check network. Contact IRM</td>
</tr>
<tr class="even">
<td><p>Create Process failed</p>
<p><em>ProgramName</em>,</p></td>
<td>Windows failed to create a process.</td>
<td>Reboot the server.</td>
</tr>
<tr class="odd">
<td>Express Purge Rate limit reached: <em>PurgeRate</em> on share: <em>CurrentShare</em></td>
<td>The purge terminated on the given share because Express Purge was active and the Purge process exceeded the user defined purge rate.</td>
<td>None</td>
</tr>
<tr class="even">
<td>File Delete failure: <em>filename</em></td>
<td>The file listed could not be deleted.</td>
<td>Check permissions on the share/folder/file</td>
</tr>
<tr class="odd">
<td>File in use: <em>filename</em></td>
<td>The log file is in use</td>
<td>Exit from the Purge and restart</td>
</tr>
<tr class="even">
<td>File purged: <em>filename</em>. 'The Image file (#2005) was not updated'</td>
<td>The file was deleted on Tier 1, but the pointer in VistA could not be updated.</td>
<td>Validate the IEN record exists in VistA.</td>
</tr>
<tr class="odd">
<td>Findfirst failed <em>filename</em></td>
<td>The directory traversal failed</td>
<td>Exit from the Purge and restart</td>
</tr>
<tr class="even">
<td><p>Log File Archival reset to:</p>
<p><em>FilePath2</em> instead of: <em>FilePath1</em></p></td>
<td>The logs files are now being stored at another location.</td>
<td>None</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Login Message^Broker Reconnection Successful</td>
<td>After a Broker disconnect, the application was able to reconnect to VistA.</td>
<td>None</td>
</tr>
<tr class="even">
<td>Login Message^Pausing 3 minutes and will then retry</td>
<td>After a Broker disconnect, the application tries 3 times to reconnect to VistA</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Login Message^Silent Login attempt failed!</td>
<td>After a Broker disconnect, the application was not able to reconnect to VistA.</td>
<td>Check network connections.</td>
</tr>
<tr class="even">
<td>NewCreationDate^SetFileTime Failed <em>filename</em></td>
<td>Could not set the date of last Access on filename</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Non-Connection related Broker error</td>
<td>Broker disconnected</td>
<td>Check VistA for error trap</td>
</tr>
<tr class="even">
<td>NOT Purged criteria: <em>EvalCriteria</em> NOT PURGED- JUKEBOX QUEUED <em>filename date</em></td>
<td><p>File was not deleted. See Section</p>
<p>6.4 Purge Criteria.</p></td>
<td>None</td>
</tr>
<tr class="odd">
<td><p>Problem renaming log file</p>
<p><em>filename1</em> -&gt; <em>filename2</em></p></td>
<td>Could not rename log file to versioned log file name</td>
<td>Check permissions.</td>
</tr>
<tr class="even">
<td>Purge Criteria: <em>EvalCriteria filename filedate</em></td>
<td>See Section 6.4 Purge Criteria</td>
<td>None</td>
</tr>
<tr class="odd">
<td><p>Purge Criteria: <em>EvalCriteria</em></p>
<p>NOT PURGED <em>filename filedate</em></p></td>
<td>File was deleted. See Section 6.4 Purge Criteria</td>
<td>None</td>
</tr>
<tr class="even">
<td>Silent Login attempt</td>
<td>Broker was disconnected. Auto login is initiated.</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Start Date failure</td>
<td>Problem with Date of Last Purge on Scheduled Purge</td>
<td>Contact IRM to clear the record in the Imaging Site Parameter file (#2006.1).</td>
</tr>
</tbody>
</table>

#### Import API

The Import API OCX (IAPI OCX) traps System Error Codes in all of the Windows function calls that are made during Import processing. When an Error occurs, the Error Code and Error Description are listed in the Result Array that is returned by the Import API.

Descriptions of the error codes are returned using the Windows function: GetLastError.

> **NOTE:** The System Error Codes are very broad. Each one can occur in one of many hundreds of locations in the system. Consequently the descriptions of these codes cannot be very specific. Use of these codes requires some amount of investigation and analysis. Make note of the run- time context in which these errors occur.

Along with the System Error code and description, the values of other IAPI parameters will also be listed in the Result Array when an error occurs. The other values will help determine the exact cause of the error.

Not all of the values listed below will be returned in the Result Array. Depending on the type of error, some values will be listed while others may or may not exist at the point in the process when the error occurred.

An example of this is the Access Verify codes. These values will be listed if an error occurs during login to the dabatase only.

Other values include:

- Import Queue number
- Image Share File Path
- Password
- Tracking ID
- Server\Share Name
- Access Code
- File to Import Full Patch
- Username
- Verify Code

#### Example

The following is an example of returned Error array

(0): 0~ERROR: 0 Images copied

1)  : MAG135;20130122 12:31:21-43 \<\< Tracking ID
2)  : 21 \<\< Import Queue Number
3)  : Image Security for Filename: \\vhaiswclu4\User1\$\TestImages\CardioMR.jpg
4)  : ParseServerShare: Input= \\vhaiswclu4\User1\$\TestImages\CardioMR.jpg
5)  : ------ ExtractFilePath : \\vhaiswclu4\User1\$\TestImages\\
6)  : ------ Result \\Server\Share: \\vhaiswclu4\User1\$
7)  : ------ Confirming UserName and Password...
8)  : ------ Username: vhamaster\vhaiswIU Password Access1.
9)  : OSConnectToServer Start : 1/22/2013 12:32:35 PM
10) : GetLastError: 1219 - Multiple connections to a server or shared resource by the

same user, using more than one user name, are not allowed. Disconnect all previous connections to the server or shared resource and try again

11) : ------ Credential conflict, continuing as current User...
12) : OSConnectToServer Success: 1/22/2013 12:32:35 PM
13) : Success: Image Directory is accessible. \\vhaiswclu4\User1\$
14) : Error copying \\vhaiswclu4\User1\$\TestImages\CardioMR.jpg

> to Server : 30168~\\isw-kirin-lt\image1\$\GFB0\00\00\03\01\\GFB00000030168.JPG

15) : :File doesn't exist : \\vhaiswclu4\User1\$\TestImages\CardioMR.jpg
16) : 1~VistA Image Entry deleted: 30168
17) : 1~Status Callback was called

The most common types of errors that will occur in the IAPI OCX are network connection errors and network read/write errors.

The exact errors that may occur at a site are unknown, but the most probable are listed below:

> 2: The system cannot find the file specified

> 3: The system cannot find the path specified

> 4: The system cannot open the file

> 5: Access is denied

> 8: Not enough storage is available to process this command

> 1: The access code is invalid

> 14: Not enough storage is available to complete this operation

> 15: The system cannot find the drive specified

19: The media is write protected

20: The system cannot find the device specified

21: The device is not ready

25: The drive cannot locate a specific area or track on the disk

26: The specified disk or diskette cannot be accessed

> 29: The system cannot write to the specified device

> 30: The system cannot read from the specified device

> 31: A device attached to the system is not functioning

> 32: The process cannot access the file because it is being used by another process

> 33: The process cannot access the file because another process has locked a portion of the file

> 36: Too many files opened for sharing

> 39: The disk is full

> 51: Windows cannot find the network path. Verify that the network path is correct and the destination computer is not busy or turned off. If Windows still cannot find the network path, contact your network administrator

> 52: You were not connected because a duplicate name exists on the network. Go to System in Control Panel to change the computer name and try again

> 53: The network path was not found

> 54: The network is busy

> 57: A network adapter hardware error occurred

> 59: An unexpected network error occurred

> 64: The specified network name is no longer available

> 65: Network access is denied

> 67: The network name cannot be found

> 70: The remote server has been paused or is in the process of being started

> 71: No more connections can be made to this remote computer at this time because there are already as many connections as the computer can accept

> 80: The file exists

> 82: The directory or file cannot be created

> 86: The specified network password is not correct

88: A write fault occurred on the network

89: The system cannot start another process at this time Import API : System Error Codes

#### Queue Processor Application Error Messages Startup

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0^Accusoft Control creation error : &lt; <em>error message</em> &gt;</td>
<td>The Import API uses the AccuSoft Image Gear Toolkit to create the watermarked image. If an error occurs during the creation of AccuSoft controls, the error message displays describing the error.</td>
<td><p>The AccuSoft controls are installed during MAG*3.0*121</p>
<p>installation. If this error message occurs, contact the VistA Imaging system manager.</p>
<p>You may need to reinstall MAG*3.0*121 to correct AccuSoft ImageGear problems.</p></td>
</tr>
<tr class="even">
<td>0^Image is missing from input data.</td>
<td>The image to be watermarked is not in the Import Queue Data.</td>
<td>Check the IMAGE file (#2005) to see if the data is corrupt.</td>
</tr>
<tr class="odd">
<td><p>0^Watermark failure :</p>
<p>&lt;<em>error message</em>&gt;</p></td>
<td>The process of burning the “Rescinded” watermark onto the image file failed.</td>
<td><p>The AccuSoft ToolKit could not create the watermarked image.</p>
<p>Check if the rescinded bitmap exists in the image directory <strong>C:\Program Files\vista\Imaging\Bmp\ MagRescinded.bmp</strong>.</p>
<p>You may need to reinstall MAG*3.0*121 to correct AccuSoft ImageGear problems.</p></td>
</tr>
<tr class="even">
<td>Create Process failed'+ProgramName</td>
<td>A system error occurred staring the process</td>
<td>Log a Remedy ticket</td>
</tr>
<tr class="odd">
<td><p>Increment <em>queue_name</em></p>
<p>Ptr^Failed</p></td>
<td><p>The QUEUE POINTER</p>
<p>(#1) in the IMAGE BACKGROUND QUEUE</p>
<p>POINTER file (#2006.031) in VistA</p>
<p>could not be updated</p></td>
<td>On the main BP window, use the Edit | Refresh Queue Counts to correct the current counts. Close the BP and restart the application.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Initialization Failure^Log Files at: C:\Program Files\Vista\Imaging\Backp rocLog\BackProc\BPError.log</td>
<td>Log file could not be created</td>
<td>Check permissions on the log folder</td>
</tr>
<tr class="even">
<td><p>RAID groups not properly configured</p>
<p>Use the Network Location Manager to reset your RAID groups</p></td>
<td>An active RAID Group has no online shares</td>
<td>Make sure online RAID Group has online shares</td>
</tr>
<tr class="odd">
<td>Requeue Failure trying to Requeue:</td>
<td>An attempt to re-queue a failed queue entry failed</td>
<td>Use the Queue Manager and step past the queue entry. Determine the problem with the entry that would not re-queue.</td>
</tr>
<tr class="even">
<td><p>SetTime Handle – Destin: C:\Program Files\Vista\Imaging\Backp rocLog\BackProc\BPError</p>
<p>.log Access is Denied</p></td>
<td>Could not write the Access Date on the log file</td>
<td>Check the file permissions on the log folder listed.</td>
</tr>
<tr class="odd">
<td><p>The Background Processor client software is version <em>n.n.n.n</em>. VistA Imaging Host system has version <em>m</em> installed. Please update to compatible client and host software.</p>
<p>Shutting down the Background Processor...</p></td>
<td>The client software that is installed does not match the KIDS version installed on VistA.</td>
<td>Install the correction version of the KIDS and client software.</td>
</tr>
<tr class="even">
<td>The Patch 39 KIDS install on the VistA host system is required for this Version of the: <em>site name</em> BP Queue Processor</td>
<td>The KIDS file for this most recent patch has not been installed in VistA.</td>
<td>Install the KIDS file on VistA.</td>
</tr>
<tr class="odd">
<td>The Site parameter context could not be determined. The application will terminate.</td>
<td>The PLACE global is corrupt</td>
<td>Log a Remedy ticket</td>
</tr>
</tbody>
</table>

| Message                                                     | Explanation                                    | Action                                                 |
|-----------------------------------------------------------------|----------------------------------------------------|------------------------------------------------------------|
| This server is not yet configured for BP queue task processing! | There is no BP Server name assigned to this server | Create a BP Server through the GUI and assign tasks to it. |

#### Runtime

| Message                                                                              | Explanation                                                                                    | Action                                                                                               |
|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| An Abstract for this file is on the Jukebox, a JBTOHD is being queued                    | ABSTRACT - The abstract pointer on the RAID is empty. The abstract will be copied from the jukebox | None                                                                                                     |
| Could not complete                                                                       | DELETE - file could not be deleted                                                                 | Check permissions on RAID share                                                                          |
| Could not complete/Requeued                                                              | DELETE - file could not be deleted                                                                 | Check permissions on RAID share                                                                          |
| Current RAID Shares^Exception: No RAID group Assigned                                    | The RAID share must be assigned to a RAID Group                                                    | On the BP main window, use Edit \| Network Location Manager to assign the RAID share(s) to a RAID Group. |
| False Positive Copy f*ilename(Source)*, *filenames source filesize*, *filesize(jukebox)* | File sizes on source and destination don’t match. File not copied.                                 | Determine if images are for different patients                                                           |
| File copied was of size zero                                                             | IMPORT - The file size is zero                                                                     | Resend image from import source                                                                          |
| File of size zero created then deleted                                                   | MAKEABS - file of zero length was created by Mag_MakeAbs.exe. It was deleted.                      | Log a Remedy ticket                                                                                      |
| File was not found                                                                       | IMPORT - file does not exist on the image share                                                    | Resend image from import source                                                                          |
| *filename* Source file does not exist.                                                   | Could not find source file                                                                         | Run Verifier to correct VistA pointers                                                                   |

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>fileshare</em>: Cannot connect to the Export Share.</td>
<td>EXPORT - Cannot map to the remote share</td>
<td><p>Check for network connectivity.</p>
<p>Check permissions..</p></td>
</tr>
<tr class="even">
<td>ForceDirectories failed:</td>
<td>DELETE - could not create directory on jukebox share</td>
<td>Check permissions on jukebox share</td>
</tr>
<tr class="odd">
<td>Image File type: <em>filename.ext</em> is an Unsupported Format</td>
<td>ABSTRACT - The Full file is not a supported Imaging file type. So the abstract cannot be created.</td>
<td>Examine the "foreign" file and determine if the extension was misnamed.</td>
</tr>
<tr class="even">
<td><p>Jukebox is not available:</p>
<p><em>filepath Volume label</em></p></td>
<td>JUKEBOX - the jukebox share is not available</td>
<td>Ping the jukebox server. Check the jukebox share permissions.</td>
</tr>
<tr class="odd">
<td>Jukebox sourcefile unavailable</td>
<td>JBTOHD - There is no abstract file on the jukebox. The abstract pointer in VistA is not set.</td>
<td>None</td>
</tr>
<tr class="even">
<td><p>JUKEBOX: <em>queue</em></p>
<p><em>_pointer</em> ^f<em>ile_extension</em> Not copied</p></td>
<td>JUKEBOX - Alternate file extension (i.e. .TXT) was not copied</td>
<td>Check file permissions</td>
</tr>
<tr class="odd">
<td>Login Message^Pausing 3 minutes and will then retry</td>
<td>AUTOLOGIN - could not relog into the Broker</td>
<td>Check for network connectivity.</td>
</tr>
<tr class="even">
<td>Login Message^Silent Login attempt failed!</td>
<td>AUTOLOGIN - could not relog into the Broker</td>
<td>Check for network connectivity.</td>
</tr>
<tr class="odd">
<td>Make AbstractError / abs is already present</td>
<td>ABSTRACT- file already exists at the RAID location specified in VistA</td>
<td>None</td>
</tr>
<tr class="even">
<td>Make AbstractError / f<em>ilename</em></td>
<td><p>MAKEABS- the</p>
<p>Mag_MakeAbs.exe could not create the abstract file</p></td>
<td>Log a Remedy ticket</td>
</tr>
<tr class="odd">
<td>NetConError Using User credentials <em>WIN32_Error</em></td>
<td>GCC - Could not logon to the remote location with the Username/Password in VistA</td>
<td>Correct the Username/Password for the GCC location in VistA</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NetConError,'There is no password associated with this Network Location: <em>share_name</em></td>
<td>GCC - The password field is empty for this Network Location</td>
<td>Enter a password for this GCC location</td>
</tr>
<tr class="even">
<td>No Image file entry was created!</td>
<td>IMPORT - an IEN was not created in the image file</td>
<td>Resend image from import source</td>
</tr>
<tr class="odd">
<td>No Jukebox sourcefile available / Attempting Abstract Queue</td>
<td>JBTOHD - There is no abstract file on the jukebox. The abstract pointer in VistA is set. The Queue Processor will attempt to make on from the Full or BIG file.</td>
<td>None</td>
</tr>
<tr class="even">
<td>No Tracking ID IMPORT failed</td>
<td>IMPORT - unique Tracking ID parameter is missing from IMPORT</td>
<td>Resend image from import source</td>
</tr>
<tr class="odd">
<td>No valid RAID share found</td>
<td><p>IMPORT - no RAID</p>
<p>pointer is set in VistA for the image</p></td>
<td>Resend image from import source</td>
</tr>
<tr class="even">
<td><p>Problem renaming log file:</p>
<p><em>filename</em></p></td>
<td>Could not rename log file to a versioned copy</td>
<td>Check permissions on the existing folder/files</td>
</tr>
<tr class="odd">
<td><em>queue_pointer</em> '^Size Mismatch <em>queue_type</em> copy not overwritten.</td>
<td>File sizes on source and destination don’t match. File not copied.</td>
<td>Determine if images are for different patients</td>
</tr>
<tr class="even">
<td>SetFileTime Failed</td>
<td>Could not set Access date on the log file.</td>
<td>None</td>
</tr>
<tr class="odd">
<td>The jukebox copy: <em>filename</em> does not exist -- attempting a copy...</td>
<td>DELETE -Could not find the file on jukebox shares. Try to copy from RAID shares to jukebox</td>
<td>None</td>
</tr>
<tr class="even">
<td>The RAID share is not on- line</td>
<td>IMPORT - The Image share is not available</td>
<td>Check the permissions on the image share indicated</td>
</tr>
<tr class="odd">
<td><p>The <em>src_filename</em> to</p>
<p><em>dest_filename</em> copy failed.</p></td>
<td>EXPORT - file could not be copied</td>
<td><p>Check for network connectivity.</p>
<p>Check permissions.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>The VistA cache file:</p>
<p><em>filename</em> not found</p></td>
<td>DELETE -Could not find the file on RAID shares to delete</td>
<td>None</td>
</tr>
<tr class="even">
<td>This Server is not yet configured!</td>
<td>A BP Server has not been associated with this server.</td>
<td>Create a BP Server for this processor</td>
</tr>
<tr class="odd">
<td>Unable to copy to the Jukebox: Not enough write cache available</td>
<td>JUKEBOX - The jukebox share is not available or is full</td>
<td><p>Add new platters to the jukebox. Determine why the jukebox share is full.</p>
<p>Possibly add new platters to the jukebox.</p></td>
</tr>
<tr class="even">
<td>Zero size <em>queue_type</em> copy NOT overwritten</td>
<td>Zero size file on the destination could not be overwritten</td>
<td>Remove zero size file</td>
</tr>
</tbody>
</table>

#### Verifier Application Error Messages Start/Run

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>About to exit without processing: 0</td>
<td>There are no IEN records within the range.</td>
<td>Choose another IEN range</td>
</tr>
<tr class="even">
<td>Broker Connection to server could not be established!</td>
<td>VistA RPC Broker is not currently in a listening state OR the application has timed out.</td>
<td>Close the application and restart. Check with the VistA system manager for the status of the Broker listener.</td>
</tr>
<tr class="odd">
<td><p>CC:createcontext ("MAG WINDOWS")</p>
<p>could not be established!</p></td>
<td><p>The user does not have the MAG WINDOWS menu</p>
<p>option assigned.</p></td>
<td>Assign the user this menu option.</td>
</tr>
<tr class="even">
<td><p>lbCacheShare.items.Count</p>
<p>&lt; 1: MAGQ SHARES</p></td>
<td>There are no online, non- router VMC shares.</td>
<td>Use the Queue Processor’s Network Location Manager to check/add the shares.</td>
</tr>
<tr class="odd">
<td>Invalid Input Range</td>
<td>The From and To values entered in the Range are not correct (e.g. Start: 0 End: 0).</td>
<td><p>Enter a valid <em>From</em> and <em>To</em></p>
<p>range.</p></td>
</tr>
<tr class="even">
<td>jukebox shares are not setup</td>
<td>The jukebox share(s) are offline or don’t exist in the NETWORK LOCATION file (#2005.2).</td>
<td>Create/Edit the jukebox shares in the Network Location Manager on the Queue Processor.</td>
</tr>
</tbody>
</table>

| Message                                                                                                                                                          | Explanation                                                                                           | Action                                                                     |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| This workstation is not currently setup as a Background Processor.                                                                                                   | There is no BP Server set up for this machine.                                                            | Use the option *BP Servers* on the Queue Processor to register this server.    |
| Verifier client software is version nnn. VistA Imaging Host software is version mmm. Please update to compatible client and host software. Shutting down Verifier... | The version of the KIDS file installed on VistA does not match the executable version on the workstation. | Install the latest KIDS and client software.                                   |
| VistA shares are not setup                                                                                                                                           | The image share(s) are offline or don’t exist in the NETWORK LOCATION file (#2005.2).                     | Create/Edit the shares in the Network Location Manager on the Queue Processor. |

#### Output HTML Messages

| Message                            | Explanation                                                                                    | Action                                                                                |
|----------------------------------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| Aggregate JB Copy Error:               | Could not copy from alternate jukebox to current jukebox                                           | Check permissions                                                                         |
| Abs to JB:                             | Abstract has been created and copied to the jukebox                                                | None                                                                                      |
| Aggregate Function - Enabled           | Software is enabled to copy files from secondary jukebox, if necessary                             | None                                                                                      |
| BIG Aggregate Failed                   | Could not copy BIG file from secondary jukebox                                                     | Check file existence/permissions                                                          |
| Create Process failed                  | Could not create process on VistA for Verifier                                                     | Check Error Trap                                                                          |
| Empty FBIG node                        | "FBIG" node has no pointers set in 2005 record.                                                    | Check shares for existence of BIG file. If not found, restore BIG file from backup tapes. |
| File of size zero created then deleted | Abstract file created of size zero. Then it is deleted. (Likely corruption of BIG and/or TGA file) | None                                                                                      |
| FULL Aggregate Failed                  | Could not copy FULL file from secondary jukebox                                                    | Check file existence/permissions                                                          |
| FULL Aggregate Failed                  | Could not copy FULL file from secondary jukebox                                                    | Check file existence/permissions                                                          |

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Images JB share is OFF- LINE:</td>
<td>jukebox is offline</td>
<td>Set jukebox back ONLINE</td>
</tr>
<tr class="even">
<td>Make AbstractError</td>
<td>Abstract file could not be created from TGA/BIG (BIG/TGA not found or image file corruption).</td>
<td>Check shares for existence of BIG/TGA file. If not found, restore BIG/TGA file from backup tapes.</td>
</tr>
<tr class="odd">
<td>New Abs to CWL</td>
<td>An abstract file has been created and copied to the current write image share</td>
<td>None</td>
</tr>
<tr class="even">
<td>No ABS file VC Ptr Cleared</td>
<td>Abstract file not found on the Image share</td>
<td>None</td>
</tr>
<tr class="odd">
<td>No ABS file VC Share OFF-Line</td>
<td>Image share is offline at location of abstract file</td>
<td>Set share back online and re- run Verifier</td>
</tr>
<tr class="even">
<td>No ABS JB Files</td>
<td>No abstract file found on the jukebox</td>
<td>Check shares for existence of ABS file. If not found, restore ABS file from backup tapes</td>
</tr>
<tr class="odd">
<td>No Acquisition Site in Image file</td>
<td><p>The ACQUISITION SITE</p>
<p>field #100 in the IMAGE file (#2005) is missing. This is a required field.</p></td>
<td><p>Contact IRM</p>
<p>Update the field with the proper site ID.</p></td>
</tr>
<tr class="even">
<td>No FULL JB Files</td>
<td>FULL file not found on the jukebox</td>
<td>Check shares for existence of Full file. If not found, restore Full file from backup tapes</td>
</tr>
<tr class="odd">
<td>No FULL VC Files</td>
<td>FULL file not found on the Image share</td>
<td>None</td>
</tr>
<tr class="even">
<td>No jukebox BIG Files</td>
<td>BIG file not found on the jukebox</td>
<td>Check shares for existence of BIG file. If not found, restore BIG file from backup tapes.</td>
</tr>
<tr class="odd">
<td>No jukebox FULL Files</td>
<td>FULL file not found on the jukebox</td>
<td>Check shares for existence of Full file. If not found, restore Full file from backup tapes.</td>
</tr>
<tr class="even">
<td>No Network References</td>
<td><p>No IMAGE file (#2005)</p>
<p>record exists for this image</p></td>
<td>Re-import image thru the Capture client</td>
</tr>
<tr class="odd">
<td>No Network References: Archived Image</td>
<td>Image has been archived, resides in the IMAGE AUDIT file (#2005.1)</td>
<td>None</td>
</tr>
<tr class="even">
<td>No VC BIG Files</td>
<td>Could not find the BIG file on the image share</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Not Certed</td>
<td>Could not find/create file type on jukebox</td>
<td>Check shares for existence of BIG file. If not found, restore BIG file from backup tapes.</td>
</tr>
</tbody>
</table>

| Message                       | Explanation                          | Action                                                                |
|-----------------------------------|------------------------------------------|---------------------------------------------------------------------------|
| Problem rename log file:          | Permission problem with log file         | Set WRITE permissions set on share/folder/file for Windows login account. |
| Text file Patient ID not in VistA | Could not locate patient ID in VistA     | Contact IRM                                                               |
| TXT to BIG VC                     | Copy TXT file to same share as BIG file  | None                                                                      |
| TXT to FULL VC                    | Copy TXT file to same share as FULL file | None                                                                      |

"Check Text" Option Messages

| Message                        | Explanation                                                          | Action                                   |
|------------------------------------|--------------------------------------------------------------------------|----------------------------------------------|
| Text File Corruption Error Type 1: | Text file is binary or unreadable                                        | Restore file from jukebox/backup tapes       |
| Cannot determine Text file type:   | Foreign text file was not likely generated on the image gateway          | Restore file from jukebox/backup tapes       |
| Text File Corruption Error Type 2: | Text file is ASCII but has unprintable characters or truncated           | Restore file from jukebox/backup tapes       |
| Text/Image DFN Mismatch:           | Patient ID in text file does not match that in VistA                     | Future utility patch                         |
| Text/Image SOP/UID Mismatch        | The Series Instance UID in the text file does not match the one in VistA | Future utility patch                         |
| Text/Image Study/UID Mismatch      | The Study Instance UID in the text file does not match the one in VistA  | Future utility patch                         |
| Text/Image UID Mismatch            | SOP and/or Study UID are/is blank in text file                           | Future utility patch                         |
| Updated Text file                  | Text file has been edited                                                | Validate file has been copied to the jukebox |
| No SSN Found                       | Patient ID field missing in text file                                    | Future utility patch                         |

#### Integrity Messages on Patient Data

There are integrity issues that will prevent their respective images from being displayed and others that will not impact the viewing. See Appendix C in the *Background Processor User Manual* for sample output.

#### Conditions Preventing Viewing

An integrity error message will be generated when the image is retrieved for viewing on these conditions and the patient image will not be viewable until the condition is corrected or the user has the proper key to view these images.

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>No Image Ptr in AP</td>
<td><blockquote>
<p>The Clinical Association Report (AP for this image does not contain an image entry that points back to this image.</p>
</blockquote></td>
<td>Future utility patch</td>
</tr>
<tr class="even">
<td>GP has no images</td>
<td>Image series that does not contain any images. Group Parents (GP) are containers for an Image series. A group parent with NO group objects (GO) is an invalid condition.</td>
<td>Future utility patch</td>
</tr>
<tr class="odd">
<td>Conflicting AP &amp; Image DFNs</td>
<td>The patient file reference (DFN) in the Clinical Association Report (AP does not match the DFN in the IMAGE file (#2005).</td>
<td>Future utility patch</td>
</tr>
<tr class="even">
<td>Invalid Image Ptr to AP</td>
<td>The Clinical Association Report (AP) has image references that are not in the IMAGE file (#2005).</td>
<td>Future utility patch</td>
</tr>
<tr class="odd">
<td>Conflicting GP and GO DFN</td>
<td>The patient file reference (DFN) in the Group Parent (GP) is not the same as the DFN in the Image entry.</td>
<td>Future utility patch</td>
</tr>
<tr class="even">
<td>GP &amp; GO AP Mismatch</td>
<td>The Group Parent and Group Object pointer references to a Clinical Association Report (AP) do not match.</td>
<td>Future utility patch</td>
</tr>
<tr class="odd">
<td>GP Missing GO Ptr</td>
<td>The Group Object multiple of the referenced Group Parent does not reference this group object.</td>
<td>Future utility patch</td>
</tr>
<tr class="even">
<td><strong>Message</strong></td>
<td><strong>Explanation</strong></td>
<td><strong>Action</strong></td>
</tr>
<tr class="odd">
<td>No AP Mult Ptr</td>
<td><p>This Image entry does not have the clinical application (AP) image multiple entry number specified. The IMAGE file (#2005).record is missing the <em>PARENT DATA FILE IMAGE POINTER</em> (#17)</p>
<p>for a Clinical Association Report (AP).</p></td>
<td>Future utility patch</td>
</tr>
<tr class="even">
<td>GO DFN mismatches</td>
<td>Some image file Group Objects have different PATIENT references (DFN).</td>
<td>Future utility patch</td>
</tr>
<tr class="odd">
<td>Image entry is structurally abnormal</td>
<td>The normal structure that distinguishes Image entry Group Parents (GP), Group Objects (GO), and Non- Group image (NG) is corrupt.</td>
<td>Future utility patch</td>
</tr>
<tr class="even">
<td>Missing Group Objects</td>
<td>The Group Parent has Group Object references that are missing.</td>
<td>Future utility patch</td>
</tr>
<tr class="odd">
<td>DFN Mismatches in AP Image Mult</td>
<td>The Clinical Association Report (AP) references a Group Parent that has image files with a different PATIENT reference (DFN) than the report.</td>
<td>Future utility patch</td>
</tr>
</tbody>
</table>

#### Conditions Allowing Viewing

The following integrity issues will not prevent their respective images from being displayed. These are informational messages.

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>No AP Ptr</td>
<td><p>The IMAGE file (#2005) record is missing the PARENT DATA FILE#</p>
<p>(#16) for a Clinical Association Report (AP). This Image does not have the entry in the clinical application (AP) specified.</p></td>
<td>Future utility patch</td>
</tr>
<tr class="even">
<td>No AP entry Ptr</td>
<td><p>This Image does not have the entry in the clinical application (AP) specified. The IMAGE file (#2005) record is missing the <em>PARENT GLOBAL ROOT</em></p>
<p><em>DO (#17)</em> for a Clinical Association Report (AP).</p></td>
<td>Future utility patch</td>
</tr>
</tbody>
</table>

#### Purge Application Error Messages

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
<tr class="odd">
<th><strong>Message</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Broker Reconnection failed</td>
<td>Auto login after a Broker disconnect failed</td>
<td>Check network. Contact IRM</td>
</tr>
<tr class="even">
<td><p>Create Process failed</p>
<p><em>ProgramName</em>,</p></td>
<td>Windows failed to create a process.</td>
<td>Reboot the server.</td>
</tr>
<tr class="odd">
<td>Express Purge Rate limit reached: <em>PurgeRate</em> on share: <em>CurrentShare</em></td>
<td>The purge terminated on the given share because Express Purge was active and the Purge process exceeded the user defined purge rate.</td>
<td>None</td>
</tr>
<tr class="even">
<td><p>File Delete failure:</p>
<p><em>filename</em></p></td>
<td>The file listed could not be deleted.</td>
<td>Check permissions on the share/folder/file</td>
</tr>
<tr class="odd">
<td>File in use: <em>filename</em></td>
<td>The log file is in use</td>
<td>Exit from the Purge and restart</td>
</tr>
<tr class="even">
<td>File purged: <em>filename</em>. 'The Image file (#2005) was not updated'</td>
<td>The file was deleted on the RAID, but the pointer in VistA could not be updated.</td>
<td>Validate the IEN record exists in VistA.</td>
</tr>
<tr class="odd">
<td>Findfirst failed <em>filename</em></td>
<td>The directory traversal failed</td>
<td>Exit from the Purge and restart</td>
</tr>
<tr class="even">
<td>Log File Archival reset to: <em>FilePath2</em> instead of: <em>FilePath1</em></td>
<td>The logs files are now being stored at another location.</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Login Message^Broker Reconnection Successful</td>
<td>After a Broker disconnect, the application was able to reconnect to VistA.</td>
<td>None</td>
</tr>
<tr class="even">
<td>Login Message^Pausing 3 minutes and will then retry</td>
<td>After a Broker disconnect, the application tries 3 times to reconnect to VistA</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Login Message^Silent Login attempt failed!</td>
<td>After a Broker disconnect, the application was not able to reconnect to VistA.</td>
<td>Check network connections.</td>
</tr>
<tr class="even">
<td>NewCreationDate^SetFile Time Failed <em>filename</em></td>
<td>Could not set the date of last Accesses on filename</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Non-Connection related Broker error</td>
<td>Broker disconnected</td>
<td>Check VistA for error trap</td>
</tr>
<tr class="even">
<td><p>NOT Purged criteria: <em>EvalCriteria</em> NOT PURGED-JUKEBOX</p>
<p>QUEUED <em>filename date</em></p></td>
<td>File was not deleted. See Section 6.4 Purge Criteria.</td>
<td>None</td>
</tr>
<tr class="odd">
<td><p>Problem renaming log file</p>
<p><em>filename1</em> -&gt; <em>filename2</em></p></td>
<td>Could not rename log file to versioned log file name</td>
<td>Check permissions.</td>
</tr>
<tr class="even">
<td>Purge Criteria: <em>EvalCriteria filename filedate</em></td>
<td>See Section 6.4 Purge Criteria</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Purge Criteria: <em>EvalCriteria</em> NOT PURGED <em>filename filedate</em></td>
<td>File was deleted. See Section 6.4 Purge Criteria</td>
<td>None</td>
</tr>
<tr class="even">
<td>Silent Login attempt</td>
<td>Broker was disconnected. Auto login is initiated.</td>
<td>None</td>
</tr>
<tr class="odd">
<td>Start Date failure</td>
<td>Problem with Date of Last Purge on Scheduled Purge</td>
<td>Contact IRM to clear the record in the Imaging Site Parameter file.</td>
</tr>
</tbody>
</table>

### DICOM Gateway Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Information about DICOM Gateway Error messages is available in the *VistA Imaging Error Message Guide.*

### Clinical Display/Capture Setup Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following errors are possible during the MAGINSTALL.EXE file execution. When the MAGINSTALL file is transported via FTP, it should be in binary format (or possible file corruption may occur).

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Error Message</strong></p>
</blockquote></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Incorrect Windows version.</td>
<td>Review the installation manual regarding the application’s Windows compatibility.</td>
</tr>
<tr class="even">
<td>Invalid executable file.</td>
<td>Possible corrupted MAGINSTALL.EXE file.</td>
</tr>
<tr class="odd">
<td>Type of executable file was unknown.</td>
<td>Possible corrupted MAGINSTALL.EXE file.</td>
</tr>
<tr class="even">
<td>Attempt was made to load a second instance of an executable file containing multiple data segments that were not marked for read-only.</td>
<td>Possible corrupted MAGINSTALL.EXE file.</td>
</tr>
<tr class="odd">
<td>Dynamic Link Library (DLL) file was invalid.</td>
<td>One of the DLLs required to run this application was corrupt.</td>
</tr>
<tr class="even">
<td>[2] Imaging Display</td>
<td>The Imaging Display application is open. Close the application and click retry.</td>
</tr>
<tr class="odd">
<td>[1] Imaging Capture</td>
<td>The Imaging Capture application is open. Close the application and click retry.</td>
</tr>
</tbody>
</table>

### VistARad Error Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error messages associated with the VistARad application are listed below. Messages are listed alphabetically. This list is not exhaustive. It omits some messages which are informational, supply their own remediation instruction, or are otherwise self-evident. If a message not on this list appears and requires further explanation, please contact the National Help Desk.

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Error Message</strong></th>
<th><strong>Cause(s)/Solutions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Case #nnn is already locked by you, perhaps at another workstation.</td>
<td>A user has attempted to lock an exam that is already locked in their name. This could occur from two different logons from different workstations; or, it could result from a failed connection that left a process hanging without a connected client.</td>
</tr>
<tr class="even">
<td>Case %s: all images failed to load.</td>
<td><p>No images for the selected case could be found. If any valid headers are located, one or more “dummy” thumbnails may be displayed in the Preview window, but no actual images are available.</p>
<p>Close the exam, then attempt to re-open it. If the problem persists, contact the local Imaging Coordinator.</p></td>
</tr>
<tr class="odd">
<td>Case #nnn is Locked by [Name/Unknown]; Status Update will NOT be allowed.</td>
<td>Between the time that the exam was opened and locked, and the time the exam was closed for update, the Exam lock information had changed, making the exam not updateable. If this occurs, check for problems in the lock table or with the Broker connection.</td>
</tr>
<tr class="even">
<td>Case #nnn locked by [name], not locked by [user]--No Status update performed</td>
<td>Between the time that the exam was opened and locked, and the time the exam was closed for update, the lock information either was killed, or over-written with another user’s information.</td>
</tr>
<tr class="odd">
<td>Case #nnn was previously locked by [Radiologist]. The lock is now assigned to you.</td>
<td>The radiologist that previously had the lock likely had the M session abnormally terminated.</td>
</tr>
<tr class="even">
<td>Case %s: no valid headers found.</td>
<td><p>Images in the exam do not have valid headers and cannot be processed properly. The exam load is considered successful.</p>
<p>You can display images by loading the “IMG_INVALID_TEXT” stack in the Preview window into the Viewer; the exam can be locked for interpretation.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Error Message</strong></th>
<th><strong>Cause(s)/Solutions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Case %s: some image(s) are missing.</td>
<td><p>Some images and/or headers could not be found. The exam load is considered incomplete.</p>
<p>Depending on what is missing, one or more placeholders will be used in the Preview and Viewer windows. The exam cannot be locked or interpreted.</p>
<p>Close the exam, then attempt to re-open it. If the problem persists, contact the local Imaging Coordinator.</p></td>
</tr>
<tr class="even">
<td>Case %s: some image(s) have invalid or missing headers.</td>
<td><p>The headers for some images in the case could not be found. Images that can be processed properly will be displayed normally; images that could not be processed due to missing header data will be loaded into the Preview window only with an “IMG_INVALID_TEXT” label.</p>
<p>The exam can be locked and interpreted.</p></td>
</tr>
<tr class="odd">
<td>Case with number xxx will not be loaded, Error 0x %x.</td>
<td>A VistARad internal error occurred while opening the exam.</td>
</tr>
<tr class="even">
<td><p>Could not send files to MIRC Server at</p>
<p>&lt;Host Name&gt; and Port &lt;Port Number&gt; with AE Title &lt;AE Title&gt;.</p></td>
<td>Ensure that the MIRC server configuration information is correct, that the MIRC server is online, and that it can receive messages.</td>
</tr>
<tr class="odd">
<td>Current Case Not Accessible for Updating</td>
<td>A user request to close an exam cannot be processed because the data does not have valid information that correctly identifies a Radiology study. Check the exam data stored in the Radiology database.</td>
</tr>
<tr class="even">
<td>Current Case not accessible to close--no action taken</td>
<td>A user request to close an exam cannot be processed because the data does not have valid information for the Radiology study. Check the exam data stored in the Radiology database.</td>
</tr>
<tr class="odd">
<td>Don't know how to read this image element.</td>
<td>An unexpected value was found in the last DICOM tag listed in the Viewport Info tab of the Hanging Protocol Definition dialog. The hanging protocol definition cannot be saved. Verify that the image header is populated properly for the DICOM tag in question.</td>
</tr>
</tbody>
</table>

| Error Message                                                           | Cause(s)/Solutions                                                                                                                                                                                                                                            |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Error getting shared CPT-HP association info.                               | VistARad was unable to read information from the VistA host. Check the VistA error trap & contact your Imaging Coordinator or the National Help Desk.                                                                                                             |
| Error Initializing HP module.                                               | VistARad was unable to read information from the VistA host. Check the VistA error trap & contact your Imaging Coordinator or the National Help Desk.                                                                                                             |
| Error occurred while performing search.                                     | The VistARad client was not able to contact the VistARad host. Check for status details at the bottom of the manager window.                                                                                                                                      |
| Error Reading File MAGJ.ini                                                 | MAGJ.ini not present in expected location (C:\Program Files\Vista\Imaging\MAG\_ VistARad). The software will start, but users will not be able to display local copies of routed exams or use integrated voice dictation functions until the problem is resolved. |
| Error reading settings. VistARad will exit.                                 | The client was unable to retrieve monitor information from the VistARad back end on the VistA Host. Verify that the VistA Host is accessible and running.                                                                                                         |
| Error retrieving monitor information (Error:%d). VistARad will exit.        | The VistARad client could not retrieve monitor information stored on the VistARad back end. System queried back end for monitor information but gets no response. Verify that a connection is present and that the VistA system is up and running.                |
| Exam is for Station (nnn); you are logged on to \#mmm". Exam is NOT Locked. | The exam being opened is exam registered at a consolidated site that is a not the user’s logon site (division). The exam can be displayed but its status cannot be updated.                                                                                       |
| Exam Manager failed to Initialize. VistARad will exit.                      | The client was unable contact VistARad back end on the VistA Host. Verify that the VistA Host is accessible and running, and that the correct KIDS version is installed.                                                                                          |

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Error Message</strong></th>
<th><strong>Cause(s)/Solutions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Exam Status for Case #nnn CANNOT be updated; current status remains: [Status]</td>
<td><p>The status update cannot proceed because there is insufficient information in the radiology record to allow the status to advance.</p>
<p>If this occurs frequently, then the site has not properly performed VistARad system setup regarding Radiology Exam Status codes definition—refer to Chapter 3 in the <em>VistA Imaging Installation Guide</em>.</p></td>
</tr>
<tr class="even">
<td>Failed to get HP info from the backend for default system user. Error code 0x80004005.</td>
<td>VistARad was unable to read information from the VistA host. Check the VistA error trap &amp; contact your Imaging Coordinator or the National Help Desk.</td>
</tr>
<tr class="odd">
<td>Failed to import user profile. Click OK to exit VistARad.</td>
<td>VistARad was unable to read information from the VistA host. Check the VistA error trap &amp; contact your Imaging Coordinator or the National Help Desk.</td>
</tr>
<tr class="even">
<td>Failed to read in xxx preset definition of the current or system user correctly.</td>
<td>There was a problem processing the specified image preset definition. Do not use the specified image preset until the problem is resolved.</td>
</tr>
<tr class="odd">
<td>Failed to read in xxx template definition of the current or system user correctly.</td>
<td>There was a problem processing the specified template definition. Do not use the specified template until the problem is resolved.</td>
</tr>
<tr class="even">
<td>Failed to retrieve a preset xxx for user xxx</td>
<td>There was a problem retrieving preset information from the VistARad back end. Verify that a connection is present and that the VistA system is up and running.</td>
</tr>
<tr class="odd">
<td>For Case #nnn, current Status is [status]; Stats Update will NOT be allowed</td>
<td><p>Between the time the exam list indicated an exam was lockable and the time the exam was opened, the exam status had changed, making the exam not lockable. If this happens frequently, exam list compile intervals specified in the MAG VISTARAD SITE PARAMETERS file</p>
<p>(#2006.69) may need to be adjusted.</p></td>
</tr>
<tr class="even">
<td><p>For MAGJ STUDYDATA</p>
<p>(TX="_TXID_") invalid params passed to rpc call.</p></td>
<td>Invalid request for key image and/or presentation state data was received on the VistA host; could indicate a database problem with the exam or images in the exam being looked at.</td>
</tr>
</tbody>
</table>

| Error Message                                                                                            | Cause(s)/Solutions                                                                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HP creation failed, error code xxxx                                                                          | An application error prevented creation of the hanging protocol; record the error code and contact Customer Support.                                                                                                                                                              |
| HP named xxx could not be read in correctly.                                                                 | There was a problem processing the specified hanging protocol definition. Do not use the specified hanging protocol until the problem is resolved.                                                                                                                                |
| Insufficient memory; cannot load all text files, thumbnails and/or key images. Load aborted for case(s) XXX. | Exit and restart VistARad to clear any potential memory issues. Attempt to reload the exam in question. Contact your Imaging Coordinator if the error persists.                                                                                                                   |
| Invalid Request (ListType=xxx)                                                                               | An attempt to compile an exam list failed. The exam list definition in MAG RAD LISTS DEFINITION file (#2006.631) may be corrupted. The exam list definition should be fixed or disabled.                                                                                          |
| Invalid transaction (TX="\_TXID\_") requested by MAGJ STUDYDATA RPC call.                                    | Invalid request for key image and/or presentation state data was received on the VistA host; could indicate a database problem with the exam or images in the exam being looked at.                                                                                               |
| Modality type xxx not found in the configuration file.                                                       | hpconfig.xml does not contain information for the modality associated with the active exam. Verify that modality for the exam in question is being correctly identified and that hpconfig.xml file stored in the VistARad application folder is present and not corrupt.          |
| Modality xxx not found. Please contact your system administrator"                                            | The hpconfig.xml file does not contain information for the modality associated with the active exam. Verify that modality for the exam in question is being correctly identified and that hpconfig.xml file stored in the VistARad application folder is present and not corrupt. |
| No data supplied for History List update/delete.                                                             | The client software performed an invalid request to update the History list.                                                                                                                                                                                                      |
| No modality in this stack of images                                                                          | The exam being opened does not contain modality information.                                                                                                                                                                                                                      |

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Error Message</strong></th>
<th><strong>Cause(s)/Solutions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>No Update Allowed for Case #nnn-- current status is [Status]</td>
<td>Between the time that the exam was opened and locked, and the time the exam was closed for update, the Exam Status information had changed, making the exam not updateable. This can occur if a data entry operation was performed in Radiology package while the exam was being read.</td>
</tr>
<tr class="even">
<td><p>Image loading has been paused: not enough memory to load all images at once.</p>
<p>Use the Preview window's List view mode to load and/or purge selected image sets.</p></td>
<td>Using the Preview window in List View mode, click “Purge” on one or more (partially) loaded series to free their memory. Then click “Resume” on the series of interest that was paused.</td>
</tr>
<tr class="odd">
<td>Request Contains Invalid Case Pointer (nnn^nnn^nnn^nnn).</td>
<td>A user request to open an exam cannot be processed because the data does not have valid information that correctly identifies a Radiology study. Check the exam data stored in the Radiology database.</td>
</tr>
<tr class="even">
<td>Resource limit exceeded! Close some images</td>
<td>The maximum number of DIMPLX controls allowed by the operating system has been exceeded. Use the layout controls in VistARad to reduce the number of visible viewports.</td>
</tr>
<tr class="odd">
<td><p>Startup problem: cannot launch background case loader.</p>
<p>Startup problem: cannot launch background cleaner.</p>
<p>Startup problem: cannot create image load/display objects.</p></td>
<td>Exit and restart VistARad; contact customer support if this error persists.</td>
</tr>
<tr class="even">
<td>The current History List may not be updated by the current user.</td>
<td>The client software performed an invalid request to update the History list.</td>
</tr>
<tr class="odd">
<td>The Exam file for this exam has patient [Pat1]; the corresponding Report file has patient [Pat2]. This is a serious problem, immediately report it to Radiology management and Imaging support!</td>
<td>The exam failed a “Patient Safety” check.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Error Message</strong></th>
<th><strong>Cause(s)/Solutions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>This exam has no report entry for associating images; no images can be accessed.</td>
<td>There is no Radiology Report link for the images in the exam being opened. Could be normal; or, a database problem (e.g., induced by deleting a Report without first correcting images).</td>
</tr>
<tr class="even">
<td><p>This exam has problems in the Radiology files, with two different Case Numbers referenced Ref1 and Ref2.</p>
<p>This is a potentially serious problem— immediately report it to Radiology management and Imaging support staff!</p></td>
<td>The exam failed a “Patient Safety” check.</td>
</tr>
<tr class="odd">
<td>This exam has problems in the Radiology Report file, with two different report entries referenced Ref1 and Ref2. This is a potentially serious problem--immediately report it to Radiology management and Imaging support staff!</td>
<td>The exam failed a “Patient Safety” check.</td>
</tr>
<tr class="even">
<td>This exam is linked to Report entry #nnn, but some of its images may be linked to Report entry #mmm. This is a potentially serious problem-- immediately report it to Radiology management and Imaging support staff!</td>
<td>The exam failed a “Patient Safety” check.</td>
</tr>
<tr class="odd">
<td>This exam is registered for [Pat1]; however, it is linked to images for patient [Pat2]. This is a serious problem, immediately report it to Radiology management and Imaging support staff!</td>
<td>The exam failed a “Patient Safety” check.</td>
</tr>
<tr class="even">
<td>The resolution of the display is not suitable for displaying diagnostic quality images. VistARad will exit.</td>
<td>This message appears if monitor resolution width is less than 1024, or if monitor resolution height is less than 700, or if monitor bit depth is less than 8.</td>
</tr>
<tr class="odd">
<td>Unable to access HISTORY File for deleting records; try again later.</td>
<td>A delete or other update operation cannot be performed because the current M process cannot lock the file for the user.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Error Message</strong></th>
<th><strong>Cause(s)/Solutions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Unable to connect to specified host/port</p>
<p>or</p>
<p>Unable to obtain VIX connection information for the specified Site code</p></td>
<td>VistARad cannot establish a connection to the specified remote VIX server. Verify correct data entry. If necessary, consult your local ADPAC to confirm that the specified VIX server is on-line and the Site Service is configured properly.</td>
</tr>
<tr class="even">
<td>Unable to get/update user data (USER_name) for MAGJ USER DATA RPC call.</td>
<td>The system could not retrieve data from the MAGJ USER DATA file (#2006.68).</td>
</tr>
<tr class="odd">
<td>Unable to open device 'IMAGING WORKSTATION'</td>
<td><p>Attempt to display a VistARad report fails because the host system cannot open the device for host file output.</p>
<p>Fix the device file entry.</p></td>
</tr>
<tr class="even">
<td>Unable to retrieve images for Case #nnn</td>
<td>Probably a database problem; the system expected to find images, but did not find any.</td>
</tr>
<tr class="odd">
<td>Unable to update Interpreting Radiologist:[Explanation provided ]</td>
<td>The Status Update cannot proceed because the user fails Radiology package user security checks.</td>
</tr>
<tr class="even">
<td>Update failed</td>
<td>There was a problem saving preset information to the VistARad back end. Verify that a connection is present and that the VistA system is up and running.</td>
</tr>
<tr class="odd">
<td>Updates not allowed at this site--no action taken</td>
<td>After the exam was closed and locked, the back end “Enable Status Update” setting has been disabled.</td>
</tr>
<tr class="even">
<td>VistARad cannot run in a terminal services client environment. VistARad will exit.</td>
<td>VistARad cannot be launched using a remote desktop connection or terminal services client.</td>
</tr>
<tr class="odd">
<td>VistARad is already running. Exiting application.</td>
<td><p>Another instance of VistARad is running on the workstation. If that instance cannot be accessed from the Windows Taskbar, you may need to kill the process named “VistARad Viewer” using the Windows Task Manager; you may need to end the MAG_Vistarad.exe process from within the Processes tab of the Windows Task Manager.</p>
<p>Then re-launch VistARad.</p></td>
</tr>
</tbody>
</table>

This page intentionally left blank.

## Appendix B: Means Tests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Sending Means Tests to the HEC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is the current list of ‘Image Types’ that need to be sent to the HEC (Health Eligibility Center):

- MEANS TEST (10-10EZ)
- MEANS TEST (10-10EZR)\*
- MEANS TEST (10-10F)

\* The (HEC) has requested that a third type of Means Test (EZR) be copied to them. Sites need to add the MEANS TEST (10-10EZR) Image Index Type to the IMAGE ACTIONS file (#2005.86) to allow the transfer of this type of Means Test.

- A qualified person at the site needs to use FileMan to edit the IMAGE ACTIONS file (#2005.86); select the TYPE field (#5); and choose HEC COPY at the Image Action name field prompt.
- You can also log a Remedy ticket and have VistA Support guide you through this process.

An example of adding a new Index Type to be sent to HEC is shown below. User entries are shown in bold.

![](vista-imaging-system-technical-manual/139.png)

![](vista-imaging-system-technical-manual/140.png)

> Appendix B – Means Tests

> **NOTE:** Sites would only want to add/expand on what gets sent to the Health Eligibility Center (HEC) upon a direct request from the Health Eligibility Center (HEC) to do so. This is usually a rare occurrence, and all sites will be notified if this occurs.

This page intentionally left blank.

## Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AE_Title The unique name assigned to a DICOM application to identify the application to other DICOM applications on the network. AE_Title will be used to log machine-to-machine communication within this patch.
CD Compact Disc
cPACS Commercial PACS
DICOM Correct The name assigned to the software routine used to correct DICOM Objects that fail processing on the DICOM Gateway.
DICOM Gateway Interface between VistA and external DICOM application entities.
> See *VistA Imaging DICOM Gateway*.
DICOM Importer II Refers to the software that performs the automated DICOM import process from outside facilities.
DICOMDIR A file that is a unique and mandatory DICOM Directory file that
contains the Media Storage Directory SOP Class as described in DICOM PS 3.10 2008.
DoD Department of Defense
DUZ The internal entry number of a VistA user’s entry in the NEW PERSON file (#200).
DVD Digital Versatile Disc
GUI Graphical User Interface
HDIG Hybrid DICOM Image Gateway: An image gateway that combines the legacy DICOM Gateway and the new VISA Gateway. It implements DICOM services.
HIPAA Health Insurance Portability and Accountability Act
IA Integration Agreement
IHE Integrating the Healthcare Enterprise
IHS Indian Health Services
KIDS Kernel Installation and Distribution System
PACS Picture Archiving and Communications System
Partial Study A study where only a subset of the available images have been
staged or imported.
PHI Protected health information: Individually identifiable health information transmitted by electronic media, maintained in electronic media, or transmitted or maintained in any other form or medium.
RPC Remote Procedure Call
SCP Service Class Provider
SCU Service Class User
SOP Service Object Pair
SOP Class Unique identifier assigned by the DICOM Standard to identify
DICOM objects.
Staging Copying study data from either media or an authorized network location into temporary persistent storage for later reconciliation. There are two
> types of staging (controlled by Security Keys):
> Basic Staging: An authorized user copies all study data from an authorized source to Importer II Persistent Storage.
Advanced Staging: An authorized user can view source data by study and copy data by study to Importer II Persistent Storage.
Storage media The physical device onto which data is recorded.
Supported SOP Class A DICOM Object that can be processed by the DICOM Gateway
and delivered to other VistA Imaging applications for use within VistA Imaging.
TWAIN An interface standard for scanners, cameras and other input devices.
A TWAIN driver is generally supplied by the equipment vendor.
UID DICOM unique identifier
VA US Department of Veterans Affairs
VISA VistA Imaging Services Architecture
VISN Veterans Integrated Service Network
VIX VistA Imaging eXchange – Software platform for managing site service and other VISA services.

# Index


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Preface](#preface)
  - [Chapter 1 Introduction](#chapter-1-introduction)
    - [Multimedia Patient Record](#multimedia-patient-record)
    - [VistARad Product Perspective and Features](#vistarad-product-perspective-and-features)
    - [Automated DICOM Image Acquisition](#automated-dicom-image-acquisition)
    - [The VistA Imaging DICOM Gateway](#the-vista-imaging-dicom-gateway)
    - [The Hybrid DICOM Image Gateway](#the-hybrid-dicom-image-gateway)
    - [Background Processor](#background-processor)
    - [Typical Configuration](#typical-configuration)
    - [DICOM Gateway Networking Topology Options](#dicom-gateway-networking-topology-options)
    - [Cross-Enterprise Image Sharing](#cross-enterprise-image-sharing)
    - [Windows 7 Considerations](#windows-7-considerations)
  - [Chapter 2 Orientation](#chapter-2-orientation)
    - [Documentation Conventions](#documentation-conventions)
    - [Special Workstation Procedures](#special-workstation-procedures)
    - [Mouse/Windows Controls](#mousewindows-controls)
  - [Chapter 3 Implementation and Maintenance](#chapter-3-implementation-and-maintenance)
    - [VistA Package Requirements](#vista-package-requirements)
    - [Hardware and Software Requirements](#hardware-and-software-requirements)
    - [Maintenance of Software on DICOM Gateway Workstations](#maintenance-of-software-on-dicom-gateway-workstations)
    - [Changes to IP Addresses or Ports](#changes-to-ip-addresses-or-ports)
    - [Security Keys](#security-keys)
    - [Workstation Hardware](#workstation-hardware)
    - [Changes to DICOM Modalities](#changes-to-dicom-modalities)
    - [Changes to Windows Servers and Security](#changes-to-windows-servers-and-security)
    - [Microsoft Patch Installation Guidelines](#microsoft-patch-installation-guidelines)
    - [Parameter Definitions](#parameter-definitions)
  - [Chapter 4 Security Software Maintenance](#chapter-4-security-software-maintenance)
    - [Security and Anti-virus Considerations](#security-and-anti-virus-considerations)
  - [Chapter 5 Space, Staffing, and Standard Operating Procedures for VistA Imaging](#chapter-5-space-staffing-and-standard-operating-procedures-for-vista-imaging)
    - [Infrastructure Resources](#infrastructure-resources)
    - [Support](#support)
    - [Daily Activities](#daily-activities)
    - [Maintenance](#maintenance)
    - [Weekly Activities](#weekly-activities)
    - [Other Periodic Activities](#other-periodic-activities)
    - [Scheduled Down Time for VistA Servers](#scheduled-down-time-for-vista-servers)
  - [Chapter 6 Routine Descriptions](#chapter-6-routine-descriptions)
    - [VistA Imaging Routines on the VistA Hospital Information System](#vista-imaging-routines-on-the-vista-hospital-information-system)
    - [DICOM Gateway Routines](#dicom-gateway-routines)
    - [Non-M Routines Distributed as Executable Files](#non-m-routines-distributed-as-executable-files)
  - [Windows 7 – C:\Program Files (x86)\Vista\Imaging\MAGVistARad\Help](#windows-7-cprogram-files-x86vistaimagingmagvistaradhelp)
  - [Chapter 7 VistA Imaging System M Files](#chapter-7-vista-imaging-system-m-files)
    - [Introduction](#introduction)
    - [VA FileMan Files that are Part of the VistA Imaging System](#va-fileman-files-that-are-part-of-the-vista-imaging-system)
    - [Input Templates](#input-templates)
    - [File List](#file-list)
    - [Files Introduced in MAG\3.0\34](#files-introduced-in-mag3034)
    - [Sort and Print Templates](#sort-and-print-templates)
    - [File List](#file-list-1)
    - [File Security](#file-security)
    - [Global Journaling](#global-journaling)
    - [VistA System Outages](#vista-system-outages)
  - [Chapter 8 Exported Options](#chapter-8-exported-options)
    - [Introduction: INI File Setup and Configuration of Workstations](#introduction-ini-file-setup-and-configuration-of-workstations)
    - [Imaging System Manager Menu \[MAG SYS MENU\]](#imaging-system-manager-menu-mag-sys-menu)
    - [Configure AE Security Matrix Settings \[MAGV AE SEC MX SETTINGS\]](#configure-ae-security-matrix-settings-magv-ae-sec-mx-settings)
    - [Delete Study by Accession Number \[MAG SYS-DELETE STUDY\]](#delete-study-by-accession-number-mag-sys-delete-study)
    - [Enter/Edit Reason \[MAG REASON EDIT\]](#enteredit-reason-mag-reason-edit)
    - [MAG Client Version Report \[MAG CLIENT VERSION REPORT\]](#mag-client-version-report-mag-client-version-report)
    - [Imaging VistARad System Options](#imaging-vistarad-system-options)
    - [Imaging MAG WINDOWS Menu Option](#imaging-mag-windows-menu-option)
    - [Imaging VistARad MAGJ VISTARAD WINDOWS](#imaging-vistarad-magj-vistarad-windows)
    - [Imaging DICOM Menu](#imaging-dicom-menu)
    - [Imaging Menu Options Documentation](#imaging-menu-options-documentation)
    - [Access to DICOM Gateway RPCs](#access-to-dicom-gateway-rpcs)
    - [Imaging Menu Options Documentation](#imaging-menu-options-documentation-1)
  - [Chapter 9 Archiving, Purging, Verifying, and Backup](#chapter-9-archiving-purging-verifying-and-backup)
    - [Introduction](#introduction-1)
    - [Archiving and Purging of Image FileMan Entries](#archiving-and-purging-of-image-fileman-entries)
    - [Archiving and Purging of Image Files](#archiving-and-purging-of-image-files)
    - [Queue Management](#queue-management)
    - [Background Processor Configuration Tools](#background-processor-configuration-tools)
    - [Background Processor Image and File Entry Verifier](#background-processor-image-and-file-entry-verifier)
    - [Imaging Server and Jukebox Backup Information](#imaging-server-and-jukebox-backup-information)
    - [DICOM-related Backup and Purge](#dicom-related-backup-and-purge)
    - [VIX-related Backups](#vix-related-backups)
  - [Chapter 10 Callable Routines/Application Programmer Interfaces (APIs)](#chapter-10-callable-routinesapplication-programmer-interfaces-apis)
  - [Import API](#import-api)
    - [VA Policy](#va-policy)
    - [FDA Policy](#fda-policy)
  - [VistA Imaging Import API](#vista-imaging-import-api)
    - [Terms of Use](#terms-of-use)
  - [Chapter 11 Error Recovery, Troubleshooting, and Testing](#chapter-11-error-recovery-troubleshooting-and-testing)
    - [Error Recovery](#error-recovery)
    - [Troubleshooting / Error Messages](#troubleshooting-error-messages)
    - [Test Software Available for Troubleshooting](#test-software-available-for-troubleshooting)
    - [Handling Processing and Storage Errors in the New Data Structures](#handling-processing-and-storage-errors-in-the-new-data-structures)
  - [Chapter 12 External Relations](#chapter-12-external-relations)
    - [HL7 Messages](#hl7-messages)
    - [HL7 Application Parameters](#hl7-application-parameters)
    - [HL7 Logical Link](#hl7-logical-link)
    - [Imaging Broker Calls](#imaging-broker-calls)
    - [Windows Messaging](#windows-messaging)
    - [Integration Agreements](#integration-agreements)
    - [Select the Context Management](#select-the-context-management)
    - [CPRS Tools Menu Option for VistARad](#cprs-tools-menu-option-for-vistarad)
    - [Mailman Messaging](#mailman-messaging)
    - [Imaging Site Reports](#imaging-site-reports)
    - [VistA Site Service](#vista-site-service)
    - [VistARad External Relations](#vistarad-external-relations)
  - [Chapter 13 Internal Relations](#chapter-13-internal-relations)
    - [Dependencies](#dependencies)
    - [VistARad Internal Relations](#vistarad-internal-relations)
  - [Chapter 14 Package-Wide Variables](#chapter-14-package-wide-variables)
  - [Chapter 15 Online Documentation](#chapter-15-online-documentation)
    - [Online Help](#online-help)
  - [Chapter 16 Site-Specific Implementation](#chapter-16-site-specific-implementation)
    - [Site-Specific Implementation](#site-specific-implementation)
  - [Chapter 17 Database Integrity Checking](#chapter-17-database-integrity-checking)
    - [VistA Imaging MAG SYS MENU](#vista-imaging-mag-sys-menu)
    - [Clinical Display Application](#clinical-display-application)
    - [VistARad Application](#vistarad-application)
    - [Verifier Application in the Background Processor](#verifier-application-in-the-background-processor)
  - [Chapter 18 Remote Image Views](#chapter-18-remote-image-views)
    - [Configuration for Remote Image Views](#configuration-for-remote-image-views)
  - [Chapter 19 Two-Facto Authentication (2FA)](#chapter-19-two-facto-authentication-2fa)
    - [Two-Factor Authentication (2FA) Overview](#two-factor-authentication-2fa-overview)
    - [Implementation History](#implementation-history)
  - [Appendix A Error Messages](#appendix-a-error-messages)
    - [Clinical Workstation Error Messages](#clinical-workstation-error-messages)
    - [Troubleshooting General Startup Network Connection](#troubleshooting-general-startup-network-connection)
    - [Runtime](#runtime)
    - [DICOM Gateway Error Messages](#dicom-gateway-error-messages)
    - [Clinical Display/Capture Setup Error Messages](#clinical-displaycapture-setup-error-messages)
    - [VistARad Error Messages](#vistarad-error-messages)
  - [Appendix B: Means Tests](#appendix-b-means-tests)
    - [Sending Means Tests to the HEC](#sending-means-tests-to-the-hec)
  - [Glossary](#glossary)
- [Index](#index)
  - [A](#a)
  - [B](#b)
  - [C](#c)
  - [D](#d)
  - [F](#f)
  - [G](#g)
  - [H](#h)
  - [I](#i)
  - [J](#j)
  - [K](#k)
  - [L](#l)
  - [M](#m)
  - [N](#n)
  - [O](#o)
  - [P](#p)
  - [Q](#q)
  - [R](#r)
  - [S](#s)
  - [T](#t)
  - [U](#u)
  - [V](#v)
  - [W](#w)
%
% Server Reserve, 123

## A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ad hoc reporting, 157
ADPAC staff requirements, 29 ADT protocols, 171
archiving, 97
Auto-Write function, 123

## B

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Background Processor configuration guidelines, 104 files installed on, 50 overview, 5
BackProc.log file, 101, 102
backward compatibility, 169 biomedical staff requirements, 29

## C

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CCOW, iv, v, 2, 144, 145, 146
Check text files, 122 Clinical Workstation
files installed on, 42
CONFIGURE IHE-BASED HL7 ADT
INTERFACE TO PACS menu option, 87 Context Management, iv, 2, 145, 146
CPRS, iv, 2, 144, 145, 146, 147, 155, 189

## D

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DFNError log file, 103 DICOM error log, 131 DICOM Gateway, 125
and PACS, 169
HL7 messages and, 143 DICOM overview, 2
DICOM_Echo, 28 document counts report, 157 drag, 11
E
error log DICOM, 131
MSM, 131
Error messages, 214
event viewer, 28, 30
exported options, 85

## F

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

failed images, processing, 130 file migration, 126
file security, 79
FileMan files, 63

## G

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

global journaling, 83

## H

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

hardware maintenance, 21
HEC, sending means tests to, 223 HL7 application parameters, 143 HL7 logical link, 143
HL7 MESSAGE TEXT file (#772), 181
HL7 messages, 143 HL7 protocols
Radiology v.2.1, 169
Radiology v.2.4, 170

## I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ICRs (integration control registrations), 144 Image Cache, 147
image count by user report, 158 IMAGE file (#2005)
deletion, 98
migration, 97
IMAGE file (#2005)
archiving or purging, 97 images
taking offline, 126
viewing remotely, 185
IMAGING HL7 MESSAGING MAINTENANCE, 85
Imaging package requirements, 13 Imaging Site parameters, 115 Imaging system
general maintenance, 29
overview, 1
RPC calls, 144
Import API, 134
input templates, 72
Integration Agreement, 144, 225
Integration Agreements, 144
Internal Relations, 169 IRM staff requirements, 28

## J

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

journaling, 83
jukebox backups, 125

## K

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel, 2, 13, 14, 41, 94, 137, 138, 185, 189
KIDS, 28, 36, 95, 126, 152, 155, 202, 203,
207, 217

## L

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Log files
Background Processor, 100
BackProc.log, 101, 102
DFNError log, 103
NoArchive log, 102
Purge.html log, 103
PurgeError.html log, 103
Queue Processor, 101
Scan log, 102
ScanError log, 103 Verifier log files, 102

## M

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MAG CLIENT VERSION REPORT menu
option, 92
MAG CPACS, 143
MAG HL7 MAINT menu option, 85 MAG REASON EDIT menu option, iv, 90 MAG SERVER mail group, 147, 148
MAG_Decompressor, 60
MAGD MAINT RAD HL7 SUBS menu
option, 86
MAGREPSTART, 156
MailMan messages, 147 MAINTAIN SUBSCRIPTIONS TO
RADIOLOGY HL7 DRIVERS menu
option, 86 maintenance
general, 29
hardware, 21
security software, 25 means test report, 161 means tests, 223 Menus
Imaging System Manager, 85 VistARad System Options, 93
messages HL7, 143
Image Cache, 147
MailMan, 147
site usage, 148
Windows, 144
Microsoft patches, installing, 21 modalities, changes to, 21 mouse, 10
MSM error log, 131

## N

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Network Location Manager, using, 113 network resources, 27
NoArchive log file, 102

## O

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

offline images, 126
online help, 179

## P

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

package index contains ‘note’ report, 162 package requirements, 13
package-wide variables, 177 patches, Microsoft, installing, 21 patient movement protocol, 174 PII, 2
ping, 28
power requirements, 28 processing failed images, 130
productivity reports, 157 protocols
patient movement, 174
radiology, 169, 173
Purge configuration, 108 Purge log files, 103 Purge.html log file, 103 PurgeError.html log file, 103 purging, 97, 98
image shares, 128
message files, 130
modality worklist, 130
PACS messages, 130

## Q

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Queue Processor overview, 5

## R

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Radiology HL7 v2.1 protocols, 169 Radiology HL7 v2.4 protocols, 170 radiology protocols
DICOM, 169
VistARad, 173
radiology report transcription service, 181 RAID Group Advance, 123
reboot, 9
remote access requirements, 28 Remote Image Views, 185 reports, imaging site, 157 routines
non-M, 41 RPC calls
VistA Imaging, 144

## S

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Scan log file, 102 ScanError log file, 103 Scheduled Verifier, 121
security, 25
file, 79
security keys, 15
server manager, 28
site parameters for Imaging, 115 site usage messages, 148
space requirements, 27 staff requirements
ADPAC, 29
biomedical, 29
IRM, 28
system outages, 83

## T

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TeleReader, 18, 22, 51, 118, 146, 154, 155,
185
TraceRT, 28
Two-Factor Authentication (2FA), 189

## U

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

user manage*r*, 28

## V

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verifier overview, 6
Verifier, using, 125
VistA Imaging ADT protocols, 171 VistA Site Service, 14, 166, 186
VIX, 7, 27, 61, 131, 166

## W

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

window controls, 10
Windows 7, iv, 2, 8, 41, 42, 49
Windows messaging, 144 Windows servers, changes to, 21 Workstations, 9
