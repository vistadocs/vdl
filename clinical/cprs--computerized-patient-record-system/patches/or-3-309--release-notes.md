---
title: OR*3*309 Release Notes VBECS Interface Follow-Up Fixes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: VBECS Interface Follow-Up Fixes
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*309
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: The most recent entries in this list are linked to the location in the manual they describe. Click on a link or page number to go to that section.
audience: 
keywords: 
  - vbecs
  - span
  - cprs
  - class
  - order
  - blood
  - report
  - strong
  - orders
  - anchor
page_count: 0
word_count: 987
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2010
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_309rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_309rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

![](or-3-309-release-notes-vbecs-interface-follow-up-fixes/001.png)

CPRS-VBECS Interface Follow-Up Fixes (OR\*3.0\*309) Release Notes

March 2010

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
<td>March 2010</td>
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

<span id="_Toc257115272" class="anchor"></span>Table of Contents

<span id="_Toc257115273" class="anchor"></span>Introduction

VistA Blood Establishment Computer System (VBECS) was released with many known problems and open issues. VistA patch OR\*3.0\*212 provides the interface between the (Computerized Patient Record System) CPRS and VBECS. OR\*3.0\*309 was conceived to help resolve some of the known problems and increase the value of VBECS to the customer base.

<span id="_Toc257115274" class="anchor"></span>Functionality

This patch enhances the Blood Bank report to display Blood Bank orders with the newest date on the top and going subsequent down to the oldest date at the bottom of the report. The results display horizontally with “Canned” comments marked by with an asterisk next to the test and displayed at the bottom of the testing results. The components are being returned to total components/day. Test sites also requested the Unit section on the Patient Information Tab be move closer to the top allowing provider to see the units without scrolling down. Multidivisons, have no way to know what site performed the tests, thus CPRS is adding the division code next to the test results. Added a default parameter, OR VBECS Legacy to turn the on the Legacy Blood Bank report. CPRS added code to remove the duplicate blood bank data.

The functionality allows Reason for Request and Surgery prompts for any kind of order. The collection type was moved next to the diagnostic test or component on the Active Orders on the Orders Tab. CPRS/VBECS contains Discontinue information in the Activity Section from backdoor discontinued orders. Unsigned orders were removed from the duplicate Type and Screen order check. It is now possible to add VBECS to auto-dc rule in the CPRS rule editor option.

<span id="_Toc257115275" class="anchor"></span>Pre-Conditions to Installation

OR\*3\*309 requires VBECS and OR\*3\*212 and CPRS 27 or CPRS 27.N.

<span id="_Toc257115276" class="anchor"></span>Changes and Fixes to the Blood Bank Report

The Blood Bank report found on the Labs and Reports tabs was showing data coming from VBECS twice (the entire report was being duplicated) when the parameter OR VBECS LEGACY REPORT was set to yes. (ORWRP2)

- Changed sort order of results displayed on reports to reverse chronologic order. (CQ 17823)
- Changed results to display horizontally rather than vertically (CQ 17824)
- Changed the VBECS canned comments display to once (CQ 17825)
- VBECS component transfusions were totaled per day in CPRS V26, changed functionality to match. (CQ 17976)
- Moved the UNITS section of the report on the Patient Info tab of the Blood order dialog up higher in the report so that it can be seen without having to scroll down. (CQ 17731)
- Multi Division Potential Problem - Unable to differentiate where testing is performed. (CQ 18484)
- Changed OR VBECS LEGACY parameter default to Yes, but allow sites that have it set to remain the way it is set. (CQ 18101)
- VBECS changes to ^LROSBR by VBECS team (VBECS Legacy report) Resolution – Added code to stop the duplicate Blood Bank Report displaying. (CQ 18044)

<span id="_Toc257115277" class="anchor"></span>Changes and Fixes to the Blood Order Dialog

- Removed the Ask on Condition value for the Reason for Request and Surgery prompts, allowing them to be answered for any blood order. (CQ 18033)
- Moved the collection type earlier in the order text. (CQ 17687)
- Added DC information to the Activity Section of the parent order when child orders are dc’d from VBECS. (CQ 18196)
- Prior to this patch the check for a current Type & Screen during the ordering process was including unreleased/unsigned orders; with this patch, unreleased/unsigned orders will no longer be included in the check for Type & Screen. (CQ 18227)
- Displayed Lab results were not saving correctly with the order, when the first item returned by Lab was a comment rather than a result value; this caused a System Exception error in VBECS when the “PR” lab result message was sent from CPRS. The lab results are now being saved correctly with the order, eliminating the exception error. (CQ 18448)
- Prior to this patch, CPRS did not allow auto-DC of VBECS orders; this patch updates the package screen in the OE/RR Auto-DC Rules file to accept VBECS. (CQ 18494)
- VBECS date/time is changing request date when a second, third units are order, when testing completes. (CQ 18644)
- VBECS Remedy HD 340648 Unit Request Date changes the previous order when  adding a component (CQ 18655)
- VBECS Manually expired specimens not recognized by CPRS, allows ordering RBC w/o T&S. (CQ 18690)

<span id="_Toc257115278" class="anchor"></span>Remedy Tickets

- OR\*3\*309 Remedy ticket \#286113, the VBECS patient information tab has the number of units available at the bottom of screen. The preferred placement is on the top.
- OR\*3\*309 Remedy ticket \#325289, the CPRS HL7 Parser caught a System Exception Error.