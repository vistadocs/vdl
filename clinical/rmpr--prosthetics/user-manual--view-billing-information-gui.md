---
title: View Billing Information (GUI) User Manual (Updated RMPR*3*178)
doc_type: UM
doc_label: User Manual
doc_layer: plain
doc_subject: View Billing Information (GUI)  (Updated RMPR*3*178)
app_code: RMPR
app_name: Prosthetics
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: Version 3.0January 2005(Revised August 2014)Department of Veterans AffairsOffice of Information and TechnologyProduct DevelopmentRevision History
audience: 
keywords: 
  - strong
  - blockquote
  - style
  - width
  - table
  - colgroup
  - tbody
  - class
  - view
  - billing
page_count: 0
word_count: 6546
section_count: 0
table_count: 6
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: August 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_pvbi_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_pvbi_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=96"
---

Prosthetics View Billing Information (GUI)User Manual

![](view-billing-information-gui-user-manual-updated-rmpr-3-178/001.png)

Version 3.0January 2005(Revised August 2014)Department of Veterans AffairsOffice of Information and TechnologyProduct DevelopmentRevision History

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>GUI User Manual</td>
<td><blockquote>
<p>Below are the development phases and dates of this <strong>Prosthetics - View Billing Information (GUI) User Manual.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 11%" />
<col style="width: 18%" />
<col style="width: 17%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Section</strong></th>
<th><strong>Date</strong></th>
<th><strong>Patch</strong></th>
<th><strong>Page/Author</strong></th>
<th><strong>Change</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Throughout</td>
<td>08/2014</td>
<td>RMPR*3.0*168</td>
<td><p>Pages <a href="#ICDp3">3</a>, <a href="#ICDupdates1">5</a>, <a href="#screen6">15</a></p>
<p>Pages <a href="#screen1">8</a>, <a href="#calendar-for-date-range-selection">9</a>, <a href="#view-prosthetics-billing-information">11</a>, <a href="#screen4">13</a>, <a href="#screen5">14</a>, <a href="#screen6">15</a>, <a href="#screen7">16</a>, <a href="#screen8">17</a>, <a href="#screen9">18</a>, <a href="#screen10">19</a>, <a href="#screen11">20</a>, <a href="#help-menu">28</a><br />
<mark>REDACTED</mark></p></td>
<td><p>Changed ICD-9 reference to ICD</p>
<p>New ICD-10 Billing screen shots</p></td>
</tr>
<tr class="even">
<td>Section 5</td>
<td>03/2009</td>
<td>RMPR*3.0*149</td>
<td><p>Pages 23-26</p>
<p><mark>REDACTED</mark></p></td>
<td>To reflect change in GUI</td>
</tr>
</tbody>
</table>

Table of Contents

View Prosthetics Billing Information User Manual [5](#_Toc346873979)

Overview [5](#_Toc346873980)

Section 1 - For Billing Users [6](#_Toc346873981)

Billing Main Menu Window [6](#_Toc346873982)

Section 2 – For Prosthetics Users [7](#_Toc346873983)

Prosthetics Main Menu Window [7](#_Toc346873984)

Section 3 – View Billing Information Package [8](#_Toc346873985)

View Billing Information Window [8](#_Toc346873986)

Enter a Date Range [9](#_Toc24938077)

Display the Prosthetics Data [11](#_Toc24938078)

Change Data Display [12](#_Toc346873989)

View Column Descriptions - Site, Dates and Patient Data [13](#_Toc346873990)

View Column Description - Insurance Information [15](#_Toc346873991)

View Column Descriptions - Coding Errors [17](#_Toc346873992)

View Column Descriptions - Item Information [18](#_Toc346873993)

View Column Descriptions - Quantity and Total Cost Data [19](#_Toc346873994)

View Column Descriptions - HCPCS and HCPCS Description Data [20](#_Toc346873995)

<span id="ICDp3" class="anchor"></span>View Column Descriptions - ICD and ICD Description [22](#_Toc346873996)

View Column Descriptions - Disability Information [23](#_Toc346873997)

Section 4 - Printing [24](#_Toc346873998)

Print the View Prosthetics Billing Information Window [24](#_Toc346873999)

Section 5 – Saving [26](#_Toc172537396)

Save as an Excel File [26](#_Toc172537397)

Section 6 - Closing and Exiting [30](#_Toc346874002)

Exit the View Prosthetics Billing Information Window [30](#_Toc346874003)

Appendix A [31](#_Toc346874004)

Getting Help [31](#_Toc346874005)

Appendix B [32](#_Toc346874006)

Activate Section 508 Assistance [32](#_Toc346874007)

<span id="_Toc346873979" class="anchor"></span>View Prosthetics Billing Information User Manual

<span id="_Toc346873980" class="anchor"></span>Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Introduction</td>
<td><blockquote>
<p>This <strong>View Prosthetics Billing Information</strong> <strong>User Manual</strong> is for Patch RMPR*3*96. This patch provides Prosthetics GUI (graphical user interface) windows for the <strong>View Prosthetics</strong> <strong>Billing Information</strong> feature.</p>
<p>The Prosthetics and Billing users will be able to do the following with this patch:</p>
</blockquote>
<ul>
<li><p>Search for data and display data by a range of dates.</p></li>
<li><p>Sort and rearrange the view; display data in a custom view.</p></li>
<li><p>Print the display.</p></li>
<li><blockquote>
<p>Convert the display into a Microsoft Excel file (for more complex sorting capabilities).</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Audience</td>
<td><blockquote>
<p>These Release Notes are geared towards two audiences. The <strong>Vista Sign-on</strong> window will appear with different functions according to which type of user is accessing the Billing information. The two audiences for this document and the <strong>Vista Sign-on</strong> window include:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Billing users – Section 1</p>
</blockquote></li>
<li><blockquote>
<p>Prosthetics users – Section 2</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Data displayed<span id="ICDupdates1" class="anchor"></span></td>
<td><blockquote>
<p>The data that is displayed on the <strong>View Prosthetics Billing Information</strong> window includes the following:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Site</p>
</blockquote></li>
<li><blockquote>
<p>Create Date</p>
</blockquote></li>
<li><blockquote>
<p>Delivery Date</p>
</blockquote></li>
<li><blockquote>
<p>Patient name</p>
</blockquote></li>
<li><blockquote>
<p>Social Security Number</p>
</blockquote></li>
<li><blockquote>
<p>Insurance</p>
</blockquote></li>
<li><blockquote>
<p>Coding Errors</p>
</blockquote></li>
<li><blockquote>
<p>Item Description</p>
</blockquote></li>
<li><blockquote>
<p>Quantity</p>
</blockquote></li>
<li><blockquote>
<p>Total Cost</p>
</blockquote></li>
<li><blockquote>
<p>HCPCS</p>
</blockquote></li>
<li><blockquote>
<p>HCPCS Description</p>
</blockquote></li>
<li><blockquote>
<p>ICD</p>
</blockquote></li>
<li><blockquote>
<p>ICD Description</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc346873981" class="anchor"></span>Section 1 - For Billing Users

<span id="_Toc346873982" class="anchor"></span>Billing Main Menu Window

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Billing Main windows</td>
<td><blockquote>
<p>Below is the <strong>Prosthetics Main Menu</strong> window where Billing users can first sign-on to VISTA (using the <strong>Vista Sign-On</strong> button) and then access the <strong>View Prosthetics Billing Information</strong> window. The Billing users will see a “<em>green dollar sign</em>” icon on the desktop to select the Prosthetics feature.</p>
<p><strong>Note:</strong> Please see the <strong>Prosthetics Main Menu User Manual</strong> for more detail information regarding VISTA Sign-On instructions.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Prosthetics Main Menu</td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/002.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Billing button</td>
<td><blockquote>
<p>Click the <strong>View Prosthetics Billing Information</strong> button and proceed to Section 3.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc346873983" class="anchor"></span>Section 2 – For Prosthetics Users

<span id="_Toc346873984" class="anchor"></span>Prosthetics Main Menu Window

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Prosthetics Main Menu Window</td>
<td><blockquote>
<p>Below is the <strong>Prosthetics Main Menu</strong> window where Prosthetics users can sign-on to VISTA and then access the <strong>View Prosthetics Billing Information</strong> window. These users also have access to other Prosthetics features.</p>
<p><strong>Note:</strong> To access this application, you will double click on the <strong>Prosthetics VISTA Suite</strong> (<em>medicine bag)</em> icon on desktop. Please see the <strong>Prosthetics Main Menu User Manual</strong> for more detailed VISTA Sign-on instructions.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Prosthetics Main Menu</td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/003.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Billing button</td>
<td><blockquote>
<p>Click the <strong>View Prosthetics Billing Information</strong> button and proceed to Section 3.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc346873985" class="anchor"></span>Section 3 – View Billing Information Package

<span id="_Toc346873986" class="anchor"></span>View Billing Information Window

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Purpose</td>
<td><blockquote>
<p>You can view Prosthetics billing information, insurance information and disability information for specific veteran using the <strong>View Prosthetics Billing Information</strong> window.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>View Prosthetics Billing Information main window<span id="screen1" class="anchor"></span></td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/004.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Menu button</td>
<td><blockquote>
<p>The <strong>Menu</strong> button will close the <strong>View Prosthetic Billing Information</strong> window and return you to the <strong>Prosthetics Main Menu</strong> window.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc24938077" class="anchor"></span>Enter a Date Range

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="datecalendars">Date/Calendars</h5></td>
<td><blockquote>
<p>After you have successfully signed on to VISTA, and the <strong>View Prosthetic Billing Information</strong> window appears, you must select the date range that you want to view.</p>
<p>Enter a <strong>Beginning Date</strong> and an <strong>Ending Date</strong> by clicking on the drop-down list boxes next to the respective fields. A calendar displays as shown below.</p>
<p><strong>Note:</strong> The software will sort by the <strong>Create Date</strong> field of the Prosthetics Purchase Order or Stock Issue. It does <strong>not</strong> sort by the <strong>Delivery Date</strong> field (the date paid).</p>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/005.png)</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Ctrl&gt;</strong> key <strong>+ &lt;B&gt;</strong> key for the Beginning Date and the<br />
<strong>&lt;Ctrl&gt;</strong> key + <strong>&lt;E&gt;</strong> key for the Ending Date to display the respective calendars. You can also click the <strong>File</strong> Menu and the <strong>Select</strong> <strong>Beginning Date</strong> or <strong>Select</strong> <strong>Ending Date</strong> option from the list.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="calendar-for-date-range-selection">Calendar for date range selection</h5></td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/006.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Enter a Date Range, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="selecting-a-date-range">Selecting a date range</h5></td>
<td><blockquote>
<p>The calendars display with the current date circled in red shown at the bottom of the calendar. You can accept the current date by clicking on it. You can also change the date by the following methods:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|             |                                                                                                                                                                                                 |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Change the… | Description                                                                                                                                                                                     |
| Day     | Click on the actual day of the week in the calendar.                                                                                                                                            |
| Month   | Click on the month at the top of the calendar to display a list of all months and select one from there. You can decrease or increase one month at a time by clicking the left or right arrows. |
| Year    | Click on the year and an up and down arrow button displays for you to increase or decrease the year.                                                                                            |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="number-of-day-restrictions">Number of Day Restrictions</h5></td>
<td><blockquote>
<p>You are restricted to a date range of less than 100 days. If you select a date range outside of this 100 day parameter, the following dialog message box displays:</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="date-range-message-box">Date Range Message box</h5></td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/007.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="start-date-before-end-date">Start Date before End Date</h5></td>
<td><blockquote>
<p>If you accidentally entered an incorrect date range, you will receive a warning message. For instance, if you enter a start date that is after the end date, the message below will display. Click the <strong>OK</strong> button and reselect your date range.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="startend-date-message">Start/End Date Message</h5></td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/008.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc24938078" class="anchor"></span>Display the Prosthetics Data

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="display-the-data">Display the data</h5></td>
<td><blockquote>
<p>Once you have selected the date ranges, click the <strong>Display</strong> button to reveal the data within that date range. (You can also click the <strong>File Menu</strong> and the <strong>Display</strong> option.)</p>
<p>A progress bar activates, and the button name changes to “<em>Searching</em>” while the system is retrieving records. (A long date range may result in a long search time.)</p>
<p><strong>Recommendation:</strong> The larger the date range selected, the greater time it will take to search, sort, and display the data. We recommend that you sort by a short date range (5-10 days) and perform the sort early in the morning or later in the day when your VISTA system is less active.</p>
<p><strong>Shortcut:</strong> Press the &lt;<strong>Ctrl</strong>&gt; key + &lt;<strong>D</strong>&gt; key.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="view-prosthetics-billing-information">View Prosthetics Billing Information</h5></td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/009.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc346873989" class="anchor"></span>Change Data Display

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="changing-the-display-of-the-data">Changing the display of the data…</h5></td>
<td><blockquote>
<p>You can manipulate the layout of the view in the <strong>View Prosthetics Billing Information</strong> window for both viewing as well as printing purposes as follows:.</p>
</blockquote>
<ul>
<li><p>To enlarge a column, click and drag a cell border.</p></li>
<li><p>To sort on any column, click on the header to sort it in <u>ascending order</u>.</p></li>
<li><p>If you click on the same column again, it will sort it in <u>descending order</u>.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="refresh-data">Refresh data</h5></td>
<td><blockquote>
<p>If you have changed the sort order, you can refresh your data by clicking the <strong><u>D</u>isplay</strong> button again.</p>
<p><strong><u>Note</u>:</strong> Refresh does not reset any column resizing that has been done.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc346873990" class="anchor"></span>View Column Descriptions - Site, Dates and Patient Data

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Site</td>
<td><blockquote>
<p>The <strong>Site</strong> column displays the VA facility where the veteran was treated and where the Prosthetics transaction was created.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Create Date</td>
<td><blockquote>
<p>The <strong>Create Date</strong> is the date the transaction (Purchase Order or Stock Issue) was created and posted to the Prosthetic veteran’s record (2319).</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Delivery Date</td>
<td><blockquote>
<p>If the <strong>Delivery Date</strong> field is blank, this indicates that Prosthetics has <strong>NOT</strong> paid the item; therefore an assumption is made that the veteran may not have received the item.</p>
<p>The <strong>Delivery Date</strong> is <strong>not</strong> the date the veteran received the item; it is technically the date the Purchase Order was closed or the date the Stock Issue transaction was posted to the 2319.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Patient</td>
<td><blockquote>
<p>The <strong>Patient</strong> column contains the veteran’s last name and first name. Only Non-Service Connected transactions display for the requested date range.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>SSN</td>
<td><blockquote>
<p>The <strong>SSN</strong> column displays the patient’s Social Security Number (SSN).</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Column Headers<span id="screen4" class="anchor"></span></td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/010.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc346873991" class="anchor"></span>View Column Description - Insurance Information

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Insurance for a patient</td>
<td><blockquote>
<p>The <strong>Insurance</strong> column displays health insurance information from the patient’s VISTA record.</p>
<p>If there is no health insurance information in the patient’s VISTA record, it displays “<em>Nothing Found</em>” in the <strong>Insurance</strong> column.</p>
<p>If health insurance displays, then the <u>most recent</u> insurance entered into the patient’s VISTA record will display.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Insurance column<span id="screen5" class="anchor"></span></td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/011.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Asterisk</td>
<td><blockquote>
<p>If there is an asterisk (*) in the <strong>Insurance</strong> column, this indicates that there is more than one insurance listed for the patient. If there is no asterisk (*), then there is only ONE insurance listed for the patient in the VISTA record.</p>
<p>Click on that line item to display the insurance information in the box below.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Sorting Tip</td>
<td><blockquote>
<p>You can sort on the column headers within the <strong>Insurance Information</strong> box to group items together for easier review. For instance, you can click on the <strong>Effective date</strong> column or <strong>Expires date</strong> column headers, and this will group items for reviewing the most recent insurance.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Effective date column sorted</td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/012.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc346873992" class="anchor"></span>View Column Descriptions - Coding Errors

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Coding Errors</td>
<td><blockquote>
<p>The <strong>Coding Errors</strong> column is to alert Billing users of a <em>possible</em> error. Errors could be any of the following:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Inactive HCPCS</p>
</blockquote></li>
<li><blockquote>
<p>Inactive ICD codes</p>
</blockquote></li>
<li><blockquote>
<p>Use of VA unique HCPCS codes.</p>
</blockquote></li>
</ul>
<blockquote>
<p>The <strong>Coding</strong> <strong>Errors</strong> column checks the HCPCS code to see if it was valid at the time of service, and if not, then the word “HCPCS” is shown in red as well as the “HCPCS Description” is shown in red. This also applies to the inactive ICD Codes.</p>
<p><strong><u>Example</u>:</strong> If there is a red HCPCS displayed in the <strong>HCPCS</strong> column, then the <strong>Coding Errors</strong> column will display “<strong>Alert HCPCS</strong>” for Prosthetics or Billing users. This will provide a mechanism to alert users to review this billing information.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Coding Column<span id="screen6" class="anchor"></span></td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/013.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Sorting Tip</td>
<td><blockquote>
<p>You can sort on the <strong>Coding Errors</strong> column by clicking the column header to group items for review.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc346873993" class="anchor"></span>View Column Descriptions - Item Information

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Item definition</td>
<td><blockquote>
<p>The <strong>Item</strong> column displays an Item or appliance kept in the Pros Master Item file. This column displays the IFCAP Item description of the Item issued to the Veteran.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>~R~ in the Item column</td>
<td><blockquote>
<p>An “<strong>~R~</strong>” displayed in the <strong>Item</strong> column represents a <strong>Repair</strong> item. The <strong>HCPCS Description</strong> column should explain what was being repaired.</p>
<p>The <strong>Item</strong> column is the “<em>Brief Description</em>” entry that is printed on the purchase order transaction and appears on the 2319 record. The <em>Brief Description</em> is entered to define the item.</p>
<p><strong>Tip:</strong> You can sort on the Item column by clicking the column header to group items to review all Repair items together.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Item column sorted – Repair items grouped together<span id="screen7" class="anchor"></span></td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/014.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc346873994" class="anchor"></span>View Column Descriptions - Quantity and Total Cost Data

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Qty column</td>
<td><blockquote>
<p>The <strong>Quantity</strong> column provides the number issued of that Item to the veteran. This is the quantity based on purchasing (not units).</p>
<p><strong>Note:</strong> For Home Oxygen, it is a payment unit not a billing unit.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Column headers<span id="screen8" class="anchor"></span></td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/015.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Total Cost column</td>
<td><blockquote>
<p>The <strong>Total Cost</strong> column represents the cost of the issue.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc346873995" class="anchor"></span>View Column Descriptions - HCPCS and HCPCS Description Data

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>HCPCS definition</td>
<td><blockquote>
<p>The HCPCS acronym stands for Healthcare Financing Administration Common Procedure Coding System. The HCPCS code represents an item or service. The Prosthetics staff selects the HCPCS code when the transaction was created.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Red HCPCS</td>
<td><p>If the HCPC Code and HCPCS Description in the <strong>HCPCS</strong> and <strong>HPCPS Description</strong> columns are red, that represents a HCPCS Code that has a coding error as defined by an Inactive HCPCS.</p>
<blockquote>
<p>This provides an alert to Prosthetics and Billing users as this will affect billing information.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Column headers<span id="screen9" class="anchor"></span></td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/016.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Asterisk in HCPCS column and Calculation Flag</td>
<td><blockquote>
<p>If there is an asterisk in the <strong>HCPCS</strong> column, this indicates that there is a calculation flag.</p>
</blockquote>
<p>A calculation flag determines whether or not a HCPCS is used as a Main Component to display the entire cost of a purchase, when multiple items within the purchase make up a whole (e.g., when purchasing a limb or surgical implants).</p></td>
</tr>
</tbody>
</table>

<span id="_Toc346873996" class="anchor"></span>View Column Descriptions - ICD and ICD Description

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>ICD definition</td>
<td><blockquote>
<p>International Classification of Diseases (Ninth Revision) <strong>-</strong>A coding system designed by WHO, (World Health Organization). ICD is the official system of assigning codes to diagnoses and procedures associated with hospital utilization in the United States.</p>
<p>The ICD is used to code and classify mortality data from death certificates. VOLUMES 1-2 contain diagnosis and procedures. VOLUME 3 is used for statistical, research and re-imbursement purposes.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Column headers<span id="screen10" class="anchor"></span></td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/017.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>ICD Code Selection</td>
<td><blockquote>
<p>This code is selected by the prescribing clinician when the Prosthetic consult is created.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc346873997" class="anchor"></span>View Column Descriptions - Disability Information

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Disability Information</td>
<td><blockquote>
<p>If the patient has disability information, it will automatically be displayed in the <strong>Disability Information</strong> box in the bottom of the window.</p>
<p>If a patient is selected without any disability information, the <strong>Disability Information</strong> box at the bottom of the window will display “<em>Nothing Found</em>.”</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Disability sample<span id="screen11" class="anchor"></span></td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/018.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc346873998" class="anchor"></span>Section 4 - Printing

<span id="_Toc346873999" class="anchor"></span>Print the View Prosthetics Billing Information Window

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="print-the-data">Print the data</h5></td>
<td><blockquote>
<p>You can print the <strong>View Prosthetics</strong> <strong>Billing Information</strong> data after you have finished your sort by column heading. Click the <strong><u>P</u>rint</strong> button to send this information to your local printer, and click <strong>OK</strong> on the <strong>Print</strong> dialog box. (You can also click the <strong>File</strong> Menu and the <strong>Print</strong> option.)</p>
<p><strong>Note:</strong> The layout of the print will be the same as the display. You can select a specific printer to print the <strong>View Prosthetics Billing</strong> <strong>Information</strong> window.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="change-to-landscape">Change to Landscape</h5></td>
<td><blockquote>
<p><strong><u>Recommendation</u>:</strong> You should change the format of the printout from <em>Portrait</em> to <em>Landscape</em> to print all the columns on the same page.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="steps">Steps</h5></td>
<td><blockquote>
<p>To change the print format, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Step</td>
<td>Action</td>
</tr>
<tr class="even">
<td>1</td>
<td>Click the <strong><u>P</u>rint</strong> button on the <strong>View Prosthetics</strong> <strong>Billing Information</strong> window.</td>
</tr>
<tr class="odd">
<td>2</td>
<td><p>Click the <strong><u>P</u>roperties</strong> button (to the right of the <strong>Name</strong> field) on the <strong>Print</strong> dialog box. Continue to the next page.</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;P&gt;</strong> key.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="print-dialog-box">Print dialog box</h5></td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/019.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="layout-tab">Layout Tab</h5></td>
<td><blockquote>
<p>You can change the format of the printout from the standard <em>Portrait</em> format to <em>Landscape</em> on the <strong>Layout</strong> tab.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="steps-continued">Steps (continued)</h5></td>
<td><blockquote>
<p>To continue to change to the Landscape format, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Step</td>
<td>Action</td>
</tr>
<tr class="even">
<td>3</td>
<td>Click the <strong>Layout</strong> tab on the <strong>Properties</strong> dialog box (usually shown as a default view).</td>
</tr>
<tr class="odd">
<td>4</td>
<td><p>Click the <strong><u>L</u>andscape</strong> radio button to change the format.</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;L&gt;</strong> key.</p></td>
</tr>
<tr class="even">
<td>5</td>
<td>Click <strong>OK</strong> or press <strong>&lt;Enter.&gt;</strong></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="landscape-radio-button">Landscape Radio button</h5></td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/020.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="last-step">Last step</h5></td>
<td><blockquote>
<p>When you return to the <strong>Print</strong> dialog box, click <strong>OK</strong> again, and it will print your output. You can print multiple copies if necessary.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc172537396" class="anchor"></span>Section 5 – Saving

<span id="_Toc172537397" class="anchor"></span>Save as an Excel File

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Excel Button</td>
<td><blockquote>
<p>Click the <strong><u>E</u>xcel</strong> button on the <strong>View Prosthetics Billing Information</strong> window to launch Excel and display the current data. (You can also click the <strong>File</strong> menu and select the <strong>Excel</strong> option.)</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;X&gt;</strong> key to launch MS Excel.</p>
<p><strong>Note:</strong> This feature creates a temporary Excel .CSV file in the folder selected. The default folder is C:\ViewBillingDownload (which is automatically created). The file name is based on the date range.</p>
<p><strong><u>Example</u>:</strong> Jul 02, 2006_Aug 10, 2006.csv</p>
</blockquote>
<p>Prior to the display, you are notified that the information about to be exported may contain Patient Identifiable Information.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Steps</td>
<td><blockquote>
<p>To export data to Excel:</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Step</td>
<td>Action</td>
</tr>
<tr class="even">
<td>1</td>
<td><p>Click the <strong><u>E</u>xcel</strong> button on the <strong>View Prosthetics Billing Information</strong> window.</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;X&gt;</strong> key.</p></td>
</tr>
<tr class="odd">
<td>2</td>
<td>Click the <strong><u>O</u>K</strong> button on the security reminder.</td>
</tr>
<tr class="even">
<td>3</td>
<td>Continue to the <strong>Select Directory</strong> window.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Security Reminder</td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/021.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                     |
|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                              |
| 4    | Navigate to the desired directory and select <u>O</u>K .(Click Cancel to exit or <u>H</u>elp to view the help pages associated with this functionality) |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Select Directory</td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/022.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                          |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                   |
| 5    | Navigate to a secure location where the temporary Excel (.csv) file will be stored and then select <u>O</u>K . Excel will open and display the data. |

Cont’d.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>MS Excel data</td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/023.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Step</td>
<td>Action</td>
</tr>
<tr class="even">
<td>6</td>
<td><p>This is only a temporary file so if you wish to save the data you must select <strong><u>F</u>ile,</strong> then <strong>Save <u>A</u>s,</strong> then change the name of the file.</p>
<p><strong>Note:</strong> To save the file, you <strong>must</strong> change the filename from the default. If you accept the default file name, it will be deleted when you close the NPPD window.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Temp file location</td>
<td><blockquote>
<p>Should you wish to check the location of the temp file, it displays on the View Prosthetic Billing window right above the Excel button.</p>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/024.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Note</td>
<td><blockquote>
<p>You will be unable to export another report to Excel or navigate away from the View Prosthetic Billing Information window until the current Excel (.csv) file is closed. Attempting to do so without first closing the file will result in one of the following errors depending on what action has taken place. If you do save a file with Patient Identifiable Info in it, don’t forget to delete it when you no longer need it.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Attempting to Open another report with temp file still open</td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/025.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Attempting to navigate away from the View Prosthetic Billing Information window with temp file still open</td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/026.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc346874002" class="anchor"></span>Section 6 - Closing and Exiting

<span id="_Toc346874003" class="anchor"></span>Exit the View Prosthetics Billing Information Window

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Exit the Application</td>
<td><blockquote>
<p>You can exit the application by first clicking the <strong>Menu</strong> button on the <strong>View Prosthetics Billing Information</strong> window. Then click the <strong>Close</strong> button on the <strong>Main Prosthetics</strong> window:</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Confirmation window</td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/027.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Cancel button</td>
<td><blockquote>
<p>If you click the <strong>Cancel</strong> button, you will remain in the application and can continue to work.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc346874004" class="anchor"></span>Appendix A

<span id="_Toc346874005" class="anchor"></span>Getting Help

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="f1-key">F1 Key</h5></td>
<td><blockquote>
<p>Online Help can be accessed in three methods:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Click the <strong>Help</strong> Menu (located in the upper left corner of the menu bar) and the <strong>Contents</strong> option.</p>
</blockquote></li>
<li><blockquote>
<p>Press the <strong>&lt;F1&gt;</strong> key.</p>
</blockquote></li>
<li><blockquote>
<p>Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;H&gt;</strong> key. (This activates the <strong>Help</strong> Menu, not the Billing contents.)</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="help-menu">Help Menu</h5></td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/028.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc346874006" class="anchor"></span>Appendix B

<span id="_Toc346874007" class="anchor"></span>Activate Section 508 Assistance

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction">Introduction</h5></td>
<td><blockquote>
<p>You can change the colors of the screen to black/white, which is required for Section 508 requirements to be read by visually and hearing impaired veterans.</p>
<p>This feature can be updated from the <strong>Help</strong> Menu. It provides a toggle to go back and forth between using the colors or the black/white screens depending on your needs.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="steps-1">Steps </h5></td>
<td><blockquote>
<p>To activate the Section 508 assistance, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Step</td>
<td>Action</td>
</tr>
<tr class="even">
<td>1</td>
<td><p>Click the <strong>Help</strong> Menu, and click the <strong>Section 508</strong> option.</p>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/029.png)</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Ctrl&gt;</strong> key + <strong>&lt;S&gt;</strong> key.</p></td>
</tr>
<tr class="odd">
<td>2</td>
<td>Click <strong>OK</strong> on the confirmation message dialog box as shown below.</td>
</tr>
<tr class="even">
<td>3</td>
<td>Click <strong>OK</strong> again to exit out of the system and restart to activate the changes.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="confirmation-message">Confirmation message</h5></td>
<td><blockquote>
<p>![](view-billing-information-gui-user-manual-updated-rmpr-3-178/030.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>