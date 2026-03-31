---
title: Primary Care Management Module (PCMM) Mass Discharge Scenarios
doc_type: SUP
doc_label: Supplement
doc_layer: plain
doc_subject: 
app_code: PCMM
app_name: Primary Care Management Module
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: - [Clinic Discharge Rules](#clinic-discharge-rules) PCMM Mass Discharge Scenarios The following is a matrix describing the possible scenarios that can be present when the mass discharge functionality is executed. Also indicated are the actions taken for each scenario. Many scenarios take no action.
audience: 
keywords: 
  - team
  - strong
  - position
  - discharge
  - date
  - class
  - future
  - assignment
  - style
  - width
page_count: 0
word_count: 1979
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pri_Care_Mgmnt_Module_(PCMM)/pcmmugappx.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pri_Care_Mgmnt_Module_(PCMM)/pcmmugappx.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=95"
---

## Table of Contents

  - [Clinic Discharge Rules](#clinic-discharge-rules)
PCMM Mass Discharge Scenarios
The following is a matrix describing the possible scenarios that can be present when the mass discharge functionality is executed. Also indicated are the actions taken for each scenario. Many scenarios take no action. They require business rule definitions that currently do not exist.
<u>Term Definitions</u>
> Effective Date - Date selected by user for discharge date
> Current - Assignment date is on or before the effective mass discharge date
> Future - Assignment or discharge date is after the effective mass discharge date
<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><h1 id="section"></h1>
<h1 id="section-1"></h1>
<h1 id="item">Item</h1></th>
<th><strong>Type</strong></th>
<th><p><strong>Team</strong></p>
<p><strong>Assignment Date</strong></p></th>
<th><p><strong>Team</strong></p>
<p><strong>Unassignment Date</strong></p></th>
<th><strong>Patient Assigned to Position(s)</strong></th>
<th><strong>Position Assignment Date</strong></th>
<th><strong>Position Unassignment Date</strong></th>
<th><strong>Action Taken by New Functionality</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Team</td>
<td>Current</td>
<td>None</td>
<td>No</td>
<td></td>
<td></td>
<td><ol type="a">
<li><p>Discharge from team</p></li>
<li><p>List patient as discharged in message</p></li>
</ol></td>
</tr>
<tr class="even">
<td>2</td>
<td>Team</td>
<td>Current</td>
<td>None</td>
<td>Yes</td>
<td>Current</td>
<td>None</td>
<td><ol type="a">
<li><p>Discharge from positions</p></li>
<li><p>Discharge from team</p></li>
<li><p>List team and position discharges in message</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>3</td>
<td>Team</td>
<td>Current</td>
<td>None</td>
<td>Yes</td>
<td>Current</td>
<td>Future</td>
<td><ol type="a">
<li><p>Change position discharge date to new effective date</p></li>
<li><p>Perform team discharge</p></li>
<li><p>List team, position discharges, and position discharge date change in message</p></li>
</ol></td>
</tr>
<tr class="even">
<td>4</td>
<td>Team</td>
<td>Current</td>
<td>None</td>
<td>Yes</td>
<td>Future</td>
<td>None</td>
<td><ol type="a">
<li><p>Delete position assignment</p></li>
<li><p>Perform team discharge</p></li>
<li><p>List team discharge and position assignment deletion in message</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>5</td>
<td>Team</td>
<td>Current</td>
<td>None</td>
<td>Yes</td>
<td>Future</td>
<td>Future</td>
<td><ol type="a">
<li><p>Delete position assignment</p></li>
<li><p>Perform team discharge</p></li>
<li><p>List team discharge and position assignment deletion in message</p></li>
</ol></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>6</td>
<td>Team</td>
<td>Current</td>
<td>Future</td>
<td>No</td>
<td></td>
<td></td>
<td><ol type="a">
<li><p>Change team discharge date to new effective date</p></li>
<li><p>List team discharge and team discharge date change in message</p></li>
</ol></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 36%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h1 id="section-2"></h1>
<h1 id="section-3"></h1>
<h1 id="item-1">Item</h1></td>
<td><strong>Type</strong></td>
<td><p><strong>Team</strong></p>
<p><strong>Assignment Date</strong></p></td>
<td><p><strong>Team</strong></p>
<p><strong>Unassignment Date</strong></p></td>
<td><strong>Patient Assigned to Position(s)</strong></td>
<td><strong>Position Assignment Date</strong></td>
<td><strong>Position Unassignment Date</strong></td>
<td><strong>Action Taken by New Functionality</strong></td>
</tr>
<tr class="even">
<td>7</td>
<td>Team</td>
<td>Current</td>
<td>Future</td>
<td>Yes</td>
<td>Current</td>
<td>None</td>
<td><ol type="a">
<li><p>Discharge from positions</p></li>
<li><p>Change team discharge date to new effective date</p></li>
<li><p>List team and position discharges and team discharge date change in message</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>8</td>
<td>Team</td>
<td>Current</td>
<td>Future</td>
<td>Yes</td>
<td>Current</td>
<td>Future</td>
<td><ol type="a">
<li><p>Change position discharge date to new effective date</p></li>
<li><p>Change team discharge date to new effective date</p></li>
<li><p>List team and position discharges, as well as team and position discharge date changes in message</p></li>
</ol></td>
</tr>
<tr class="even">
<td>9</td>
<td>Team</td>
<td>Current</td>
<td>Future</td>
<td>Yes</td>
<td>Future</td>
<td>None</td>
<td><ol type="a">
<li><p>Delete position assignment</p></li>
<li><p>Change team discharge date to new effective date</p></li>
<li><p>List team discharge, team discharge date change, and position assignment deletion in message</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>10</td>
<td>Team</td>
<td>Current</td>
<td>Future</td>
<td>Yes</td>
<td>Future</td>
<td>Future</td>
<td><ol type="a">
<li><p>Delete position assignment</p></li>
<li><p>Change team discharge date to new effective date</p></li>
<li><p>List team discharge, team discharge date change and position assignment deletion in message</p></li>
</ol></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>11</td>
<td>Team</td>
<td>Future</td>
<td>None</td>
<td>No</td>
<td></td>
<td></td>
<td><ol type="a">
<li><p>Delete team assignment</p></li>
<li><p>List deleted team assignment in message</p></li>
</ol></td>
</tr>
<tr class="even">
<td>12</td>
<td>Team</td>
<td>Future</td>
<td>None</td>
<td>Yes</td>
<td>Future</td>
<td>None</td>
<td><ol type="a">
<li><p>Delete position assignment</p></li>
<li><p>Delete team assignment</p></li>
<li><p>List deleted team and position assignments in message</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>13</td>
<td>Team</td>
<td>Future</td>
<td>None</td>
<td>Yes</td>
<td>Future</td>
<td>Future</td>
<td><ol type="a">
<li><p>Delete position assignment</p></li>
<li><p>Delete team assignment</p></li>
<li><p>List deleted team and position assignments in message</p></li>
</ol></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>14</td>
<td>Team</td>
<td>Future</td>
<td>Future</td>
<td>No</td>
<td></td>
<td></td>
<td><ol type="a">
<li><p>Delete team assignment</p></li>
<li><p>List deleted team assignment in message</p></li>
</ol></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 36%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h1 id="section-4"></h1>
<h1 id="section-5"></h1>
<h1 id="item-2">Item</h1></td>
<td><strong>Type</strong></td>
<td><p><strong>Team</strong></p>
<p><strong>Assignment Date</strong></p></td>
<td><p><strong>Team</strong></p>
<p><strong>Unassignment Date</strong></p></td>
<td><strong>Patient Assigned to Position(s)</strong></td>
<td><strong>Position Assignment Date</strong></td>
<td><strong>Position Unassignment Date</strong></td>
<td><strong>Action Taken by New Functionality</strong></td>
</tr>
<tr class="even">
<td>15</td>
<td>Team</td>
<td>Future</td>
<td>Future</td>
<td>Yes</td>
<td>Future</td>
<td>None</td>
<td><ol type="a">
<li><p>Delete position assignment</p></li>
<li><p>Delete team assignment</p></li>
<li><p>List deleted team and position assignments in message</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>16</td>
<td>Team</td>
<td>Future</td>
<td>Future</td>
<td>Yes</td>
<td>Future</td>
<td>Future</td>
<td><ol type="a">
<li><p>Delete position assignment</p></li>
<li><p>Delete team assignment</p></li>
<li><p>List deleted team and position assignments in message</p></li>
</ol></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>17</td>
<td>Position</td>
<td></td>
<td></td>
<td>Yes</td>
<td>Current</td>
<td>None</td>
<td><ol type="a">
<li><p>Discharge patient from position</p></li>
<li><p>List position discharge in message</p></li>
</ol></td>
</tr>
<tr class="even">
<td>18</td>
<td>Position</td>
<td></td>
<td></td>
<td>Yes</td>
<td>Current</td>
<td>Future</td>
<td><ol type="a">
<li><p>Change position discharge date to new effective date</p></li>
<li><p>List position discharge and position discharge date change in message</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>19</td>
<td>Position</td>
<td></td>
<td></td>
<td>Yes</td>
<td>Future</td>
<td>None</td>
<td><ol type="a">
<li><p>Delete position assignment</p></li>
<li><p>List deleted position assignment in message</p></li>
</ol></td>
</tr>
<tr class="even">
<td>20</td>
<td>Position</td>
<td></td>
<td></td>
<td>Yes</td>
<td>Future</td>
<td>Future</td>
<td><ol start="3" type="a">
<li><p>Delete position assignment</p></li>
<li><p>List deleted position assignment in message</p></li>
</ol></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
Note on Future Assignments: Any assignment active after the effective date but not active TODAY will not be modified or deleted. This will preserve the history of that assignment. Any modifications to these assignments will need to be accomplished using PCMM GUI. The MailMan message will indicate those assignments falling into this category have not been unassigned.

## Clinic Discharge Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 6%" />
<col style="width: 19%" />
<col style="width: 69%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h1 id="item-3">Item</h1></td>
<td><strong>Type</strong></td>
<td><h1 id="position-associated-with-clinic">Position Associated with Clinic</h1></td>
<td><strong>Action Taken by New Functionality</strong></td>
</tr>
<tr class="even">
<td>1</td>
<td>Team</td>
<td>No</td>
<td><ol type="a">
<li><p>No Action</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>2</td>
<td>Team</td>
<td>Yes</td>
<td><ol type="a">
<li><p>Ask user whether patients enrolled in clinic should be discharged from clinic as part of position discharge.<br />
<br />
This question will be asked for each position associated with a clinic. It will be asked after the user has selected a team and before the list of patient team assignments is presented. In other words, the user will not be prompted with this question for each patient selected.</p></li>
<li><p>List clinic discharge information in message.</p></li>
</ol></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>3</td>
<td>Position</td>
<td>No</td>
<td><ol type="a">
<li><p>No Action</p></li>
</ol></td>
</tr>
<tr class="even">
<td>4</td>
<td>Position</td>
<td>Yes</td>
<td><ol type="a">
<li><p>Ask user whether patients enrolled in clinic should be discharged from clinic as part of position discharge.<br />
<br />
It will be asked after the user has selected a position and before the list of patient position assignments is presented. In other words, the user will not be prompted with this question for each patient selected.</p></li>
<li><p>List clinic discharge information in message.</p></li>
</ol></td>
</tr>
</tbody>
</table>