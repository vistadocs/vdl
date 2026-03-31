---
title: RMPR*3*59 Delayed Order Report (DOR) (GUI) User Manual
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Delayed Order Report (DOR) (GUI)
app_code: RMPR
app_name: Prosthetics
section: CLI
app_status: active
pkg_ns: RMPR
patch_ver: 3
patch_id: RMPR*3*59
group_key: "RMPR:RMPR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: "<table> <colgroup> <col style=\\"width: 18%\\" /> <col style=\\"width: 81%\\" /> </colgroup> <tbody> <tr class=\\"odd\\"> <td><h5 id=\\"introduction\\">Introduction</h5></td> <td><blockquote> <p>The <strong>Delayed Order Report (DOR)</strong> <strong>User Manual</strong> corresponds to Patch RMPR359. This patch pro"
audience: 
keywords: 
  - strong
  - blockquote
  - table
  - colgroup
  - style
  - width
  - tbody
  - class
  - view
  - delayed
page_count: 0
word_count: 9168
section_count: 8
table_count: 20
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: June 2003
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_59um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_59um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=96"
---

## Table of Contents

  - [Table of Contents](#table-of-contents)
  - [## Automated Delayed Order Report (DOR) User Manual](#automated-delayed-order-report-dor-user-manual)
  - [Display the DOR Data](#display-the-dor-data)
  - [View 2319 Information](#view-2319-information)
  - [View and Manage the DOR](#view-and-manage-the-dor)
  - [Appendix A](#appendix-a)
  - [Appendix B](#appendix-b)
![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/001.png)
Prosthetics Patch RMPR\*3\*59Automated Delayed Order Report (DOR)User Manual
June 2003
Health System Design and Development (HSD&D)

## Table of Contents

Automated Delayed Order Report (DOR) User Manual [1](#automated-delayed-order-report-dor-user-manual)
Overview [1](#overview)
Display the DOR Data [3](#display-the-dor-data)
Introduction [3](#introduction-1)
Select a Site(s) [4](#select-a-sites)
Select a Starting Date [5](#select-a-starting-date)
Select a Status [6](#select-a-status)
Select the SSN Range [7](#select-the-ssn-range)
Display the Data [8](#display-the-data)
View DOR Calculation Detail [10](#view-dor-calculation-detail)
View Pending Calculations [14](#view-pending-calculations)
View 2319 Information [15](#view-2319-information)
View 2319 – Patient Demographics [15](#view-2319-patient-demographics)
View 2319 - Clinic Enrollments/Correspondence [16](#view-2319---clinic-enrollmentscorrespondence)
View 2319 - Entitlement Information [17](#view-2319---entitlement-information)
View 2319 – Appliance Transactions [18](#view-2319-appliance-transactions)
View 2319 – Auto Adaptive Info [20](#view-2319-auto-adaptive-info)
View 2319 - Critical Comments [21](#view-2319---critical-comments)
View 2319 – View HISA Information [22](#view-2319-view-hisa-information)
View 2319 – Home Oxygen [23](#view-2319-home-oxygen)
View and Manage the DOR [25](#view-and-manage-the-dor)
View CPRS [25](#view-cprs)
View Request [26](#view-request)
Save as an Excel File [27](#save-as-an-excel-file)
Print the DOR [28](#print-the-dor)
Appendix A [29](#appendix-a)
Using the Menus [29](#using-the-menus)
Appendix B [30](#appendix-b)
Getting Help [30](#getting-help)
Activate Section 508 Assistance [31](#activate-section-508-assistance)

## ## Automated Delayed Order Report (DOR) User Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Overview

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction">Introduction</h5></td>
<td><blockquote>
<p>The <strong>Delayed Order Report (DOR)</strong> <strong>User Manual</strong> corresponds to Patch RMPR*3*59. This patch provides Prosthetics GUI (graphical user interface) windows for the <strong>Delayed Order Report</strong> <strong>(DOR)</strong> feature.</p>
<p><strong>Note</strong>: <em><strong>Using this feature requires basic MS Windows skills.</strong></em></p>
<p><u>The Prosthetics users will be able to do the following with this patch</u>:</p>
</blockquote>
<ul>
<li><p>Search for and display manual suspense entries/electronic consult (CPRS order) data by one or all sites.</p></li>
<li><p>Display data using one or multiple statuses (Open, Pending, Cancelled or Closed).</p></li>
<li><p>Use a starting date for Closed and Cancelled records to display data.</p></li>
<li><p>Sort and rearrange the view; display data in a custom view.</p></li>
<li><p>Print the display.</p></li>
<li><p>Convert the display into a Microsoft Excel file (for more sorting capabilities).</p></li>
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
<td><h5 id="working-days">Working Days</h5></td>
<td><blockquote>
<p>A delayed order is counted in Working days not Calendar days<strong>. This does NOT include Saturdays and Sundays or Holidays!!!</strong></p>
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
<td><h5 id="record-status">Record Status</h5></td>
<td><p>The <em><strong>Status</strong></em> column shows the following status types:</p>
<ol type="1">
<li><p>Open</p></li>
<li><p>Pending</p></li>
<li><p>Closed</p></li>
<li><p>Cancelled</p></li>
</ol></td>
</tr>
</tbody>
</table>

Continued on next page

Overview, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="status-cycle">Status cycle</h5></td>
<td><blockquote>
<p>The <em><strong>Initial Action Date</strong></em> displays the date of the first action taken on the suspense entry/electronic consult (CPRS order) record. This changes the status from OPEN to PENDING. An order remains in PENDING status until it is fulfilled and then changes to a CLOSED status.</p>
<p><strong>Note:</strong> The status can change from OPEN to CLOSED if the order has been fulfilled upon the initial action.</p>
<p>Keep in mind that when creating the first action note, the status changes from OPEN to PENDING and when creating the second or additional action note(s), the status remains PENDING. Only when a record is completed does the status change to CLOSED.</p>
<p>When a complete note is posted, all action has taken place for a requested Prosthetic item or service. When you post the complete note, the status on the record changes from PENDING (if action has previously taken place on the request) or OPEN to a CLOSED status.</p>
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
<td><h5 id="work-days-not-calendar-days">Work Days, not Calendar Days</h5></td>
<td><blockquote>
<p>The <strong>Delayed Order Report</strong> displays the number of “Work“ days (<strong>not</strong> Calendar days) from the original date the order was entered as an electronic consult or a suspense entry to the day it is completed. A “Work” day is defined as Monday through Friday.</p>
<p><strong>Note:</strong> The calculation subtracts Saturdays and Sundays and Holidays from the number of days the order was entered, even if a CPRS order was written over a weekend. <strong><u>Holidays are NOT counted</u>.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Display the DOR Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="general-steps-to-view-dor-data">General steps to view DOR Data</h5></td>
<td><blockquote>
<p>To utilize the <strong>Delayed Order Report (DOR)</strong> data, here is a general set of steps to display DOR data as follows:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Select ALL sites by checking the “<em><strong>Or…All Sites</strong></em>” checkbox (or you can select a specific site from the drop down list).</p>
</blockquote></li>
<li><blockquote>
<p>Enter a Starting Date (defaults to the current date).</p>
</blockquote></li>
<li><blockquote>
<p>Select a Status if you want to change the default statuses. The default statuses are set to <strong>Open</strong>, <strong>Pending</strong>, and <strong>Closed</strong>.</p>
</blockquote></li>
<li><blockquote>
<p>Enter the SSN range of the patient display (mandatory).</p>
</blockquote></li>
<li><blockquote>
<p>Click the <strong>Display</strong> button.</p>
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
<td><h5 id="description">Description</h5></td>
<td><blockquote>
<p>The <em><strong>Description</strong></em> is a free-text field that is manually entered with approximately 15 characters in length. If you can’t view the entire description, you can expand the column by clicking and dragging the borderline to a wider position.</p>
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
<td><h5 id="data-displayed">Data displayed</h5></td>
<td><blockquote>
<p>The data that is displayed with this GUI feature includes the following:</p>
</blockquote>
<p><u>Grid Columns</u>:</p>
<ul>
<li><p>Site</p></li>
<li><p>Delayed column (Yes or No)</p></li>
<li><p>Status of the order</p></li>
<li><p>Type of Order – Manual Suspense or Routine (electronic orders via CPRS including Eyeglass, Contact Lens and Home Oxygen orders)</p></li>
<li><p>Station number</p></li>
<li><p>Create Date (Suspense entry date)</p></li>
<li><p>First Action Date – Date that the order was put into PENDING status</p></li>
<li><p>Number of Days that the order has been delayed including columns for: 0-5, 6-9, 10-29, 30-90, and 90+ columns</p></li>
<li><p>Link information – linked message(s) to the order record</p></li>
<li><p>Brief description</p></li>
<li><p>Patient name</p></li>
<li><p>Social Security Number</p></li>
</ul>
<blockquote>
<p><u>Fields</u>:</p>
</blockquote>
<ul>
<li><p>Selection Result Totals (near bottom of window) include:</p></li>
</ul>
<ul>
<li><p>Total records found</p></li>
<li><p>Total delayed records by calculation</p></li>
<li><p>Percent delayed records by calculation</p></li>
</ul></td>
</tr>
</tbody>
</table>

#### Select a Site(s)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="select-site">Select Site</h5></td>
<td><blockquote>
<p>The first thing you must do to view the DOR is to select a site for the records that you want to display. If you are a multi-site facility, you will be able to select the specific site you want to view via the drop down box. <strong><u>Recommendation</u>:</strong> It is highly recommended that you select the “<em><strong>Or…All Sites</strong></em>” checkbox.</p>
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
<p>To begin the process to display the DOR data, follow this first step:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                          |
|------|--------------------------------------------------------------------------|
| Step | Action                                                                   |
| 1    | Click the “*Or…All Sites*” checkbox to view ALL sites and CBOC data. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="dor-window">DOR window</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/002.png)</p>
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
<td><h5 id="select-all-sites">Select “ALL Sites”</h5></td>
<td><blockquote>
<p>If you want to view all available suspense entries/electronic consult orders including Community Based Outpatient Clinics (CBOC) data, click the <strong>All Sites</strong> checkbox instead of selecting your specific site from the <strong>Site</strong> drop-down list box. This ensures that the display will include all sites. For example, the Kenosha, Wisconsin CBOC will not display when the Milwaukee site is selected only. These records display when the <strong>All Sites</strong> checkbox is selected.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Select a Starting Date

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="datecalendar">Date/Calendar</h5></td>
<td><blockquote>
<p>Note the <em><strong>Starting Date</strong></em> defaults to the current date. You can change this date. Enter a <em><strong>Starting Date</strong></em> by clicking on the drop-down list box. A calendar displays with the current date circled in red and shown at the bottom of the calendar. You can accept the current date by clicking on it.</p>
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
<td><h5 id="steps-1">Steps</h5></td>
<td><blockquote>
<p>To continue to display the DOR data, follow this step:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                       |
|------|-------------------------------------------------------|
| Step | Action                                                |
| 2    | Enter a Starting Date (defaults to the current date). |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="date">Date</h5></td>
<td><blockquote>
<p>You can change the date by the following methods:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|             |                                                                                                                                                                                         |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Change the… | Description                                                                                                                                                                             |
| Day     | Click on the actual day of the week in the calendar.                                                                                                                                    |
| Month   | Click on the month at the top of the calendar to display a list of all months and select one. Or you can decrease or increase one month at a time by clicking the left or right arrows. |
| Year    | Click on the year and an up and down arrow button displays for you to increase or decrease the year.                                                                                    |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="starting-date-calendar">Starting date calendar</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/003.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Select a Status

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="status">Status</h5></td>
<td><blockquote>
<p>You can view <strong>Open</strong>, <strong>Pending</strong>, <strong>Closed</strong> or <strong>Canceled</strong> records by clicking the checkbox for one or all of these options. The default statuses that are already checked are: <strong>Open</strong>, <strong>Pending</strong> and <strong>Closed</strong>. You can click in these boxes to uncheck any status.</p>
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
<td><h5 id="steps-2">Steps</h5></td>
<td><blockquote>
<p>To continue to display the DOR data, follow this step:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                             |
|------|-------------------------------------------------------------|
| Step | Action                                                      |
| 3    | Select a Status if you want to change the default statuses. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="status-scenarios">Status Scenarios</h5></td>
<td><blockquote>
<p>There are a number of combinations that you can choose including the following status scenarios:</p>
<p><strong><u>Scenario 1</u>:</strong> If you select the <strong>Open</strong> and <strong>Pending</strong> statuses, you will view all suspense records/electronic consult records (CPRS orders) available with a status of <strong>Open</strong> and <strong>Pending</strong>.</p>
<p><strong><u>Scenario 2</u>:</strong> The <em><strong>Starting Date</strong></em> field works with the <strong>Closed</strong> and <strong>Canceled</strong> statuses. If you check either one of these statuses, you can then select the <em><strong>Starting Date</strong></em> to display these records. (The <em><strong>Starting Date</strong></em> field that you select plus <strong>Closed</strong> Delayed records for that period does NOT affect the <strong>Open</strong> and <strong>Pending</strong> status record display.)</p>
<p><strong><u>Scenario 3</u>:</strong> If you select all four statuses, you will view ALL <strong>Open</strong> and <strong>Pending</strong> records. You will also view the <strong>Closed</strong> and <strong>Canceled</strong> records beginning with the <em><strong>Starting Date</strong></em> you select ONLY.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Select the SSN Range

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="ssn-fields">SSN fields</h5></td>
<td><blockquote>
<p>You must have an SSN range to view DOR data. There is a <strong>Starting SSN</strong> and an <strong>Ending SSN</strong> field box. This is a range of patient Social Security Numbers by the last two digits. When you enter a range, it will display electronic consults or manual suspense entries within that range.</p>
<p>If your workload is categorized by the SSN for a specific Purchasing Agent, then you can display entries that are assigned by one Purchasing Agent at a time.</p>
<p><strong>Note:</strong> Enter a range of 00 to 99 to view all Purchasing Agents’ SSNs for all patients.</p>
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
<td><h5 id="steps-3">Steps</h5></td>
<td><blockquote>
<p>To continue to display the DOR data, follow this step:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                         |
|------|---------------------------------------------------------|
| Step | Action                                                  |
| 4    | Enter the SSN range of the patient display (mandatory). |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="ssn-range">SSN range</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/004.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Display the Data

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="data-display">Data display</h5></td>
<td><blockquote>
<p>The data displayed are manual suspense and all other consult entries. You’ll notice columns with a breakdown of days of 0-5, 6-9, 10-29, 30-89 and 90+ columns.</p>
<p><u>These columns display the total number of days old by category within the breakdown of the columns. It does NOT display the total number of instances of records (manual suspense entries or electronic consults via CPRS orders)</u>.</p>
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
<td><h5 id="steps-4">Steps</h5></td>
<td><blockquote>
<p>To continue to display the DOR data, follow this step:</p>
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
<td>5</td>
<td><p>Once you have the desired criteria, click the <strong>Display</strong> button. (You can also double click a record to view the <strong>Request</strong> window.)</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;D&gt;</strong> key.</p></td>
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
<td><h5 id="sizing-and-sorting-columns">Sizing and Sorting columns</h5></td>
<td><blockquote>
<p>Columns are sizable on this window, but not movable. To resize a column, you can place the cursor on the column header borderline until you can view the double-headed arrow. Then click and drag the column until it is the size you want.</p>
<p>To sort the columns, click the column header and the data will redisplay in ascending or descending order. <strong>Note:</strong> Due to some records not having a 1<sup>st</sup> Action date, sorting by this column will not sort in date order.</p>
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
<td><h5 id="delayed-order-report-window">Delayed Order Report window</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/005.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

Display the Data, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="menu-refresh-and-clear-buttons">Menu, Refresh and Clear buttons</h5></td>
<td><blockquote>
<p>The <strong>Menu</strong> button returns you to the <strong>Prosthetics Main Menu</strong> window where you can open additional applications at the same time. The <strong>Refresh</strong> button resets (recalls) the data if you had made some column sizing changes. It is the same as clicking the <strong>Display</strong> button again. You can use the <strong>Clear</strong> button to blank out the window and start over with new display criteria.</p>
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
<td><h5 id="column-titles">Column titles</h5></td>
<td><blockquote>
<p>Below are the header titles of each column and a description of each.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Column</td>
<td>Description</td>
</tr>
<tr class="even">
<td><strong>Dlyd</strong></td>
<td>The <strong>Delayed</strong> column will display either a Yes or No as to whether the record is delayed or not. You can sort on this column by all “Yes” records or all “No” records by clicking on the column.</td>
</tr>
<tr class="odd">
<td><strong>Status</strong></td>
<td>The <strong>Status</strong> of the record is either Open, Pending, Closed or Cancelled. Records with an Open status are shown in blue.</td>
</tr>
<tr class="even">
<td><strong>Type</strong></td>
<td>This is the <strong>Type</strong> of record - Manual Suspense entry or Routine Consult (electronic orders via CPRS including Eyeglass, Contact Lens and Home Oxygen orders).</td>
</tr>
<tr class="odd">
<td><strong>Station</strong></td>
<td>This is the <strong>Station Identifying number</strong>.</td>
</tr>
<tr class="even">
<td><strong>Create</strong></td>
<td>The <strong>Create date</strong> is the date that the record was created.</td>
</tr>
<tr class="odd">
<td><strong>1<sup>st</sup> Action</strong></td>
<td>The <strong>First Action date</strong> is the date that initial action was taken on the request and the status changed from Open to Pending.</td>
</tr>
<tr class="even">
<td><strong>0-5</strong></td>
<td>The number of days (0-5) that an order record is <strong>not</strong> delayed.</td>
</tr>
<tr class="odd">
<td><strong>6-9; 10-29; 30-89; 90+</strong></td>
<td><p>These columns of number ranges designate the number of Workdays within these ranges that a request has been delayed. <strong>This does NOT include Saturdays and Sundays nor Holidays.</strong> This also designates that the record is in a Pending status. Any record over 5 days is highlighted in red with yellow numbers.</p>
<p><strong>Note:</strong> The numbers listed in each row for a record designate the <u>number of days NOT the number of record instances</u>.</p></td>
</tr>
<tr class="even">
<td><strong>Lnk</strong></td>
<td><p>The <strong>Link</strong> column designates how many items that were linked to that record. It could be a zero or a number.</p>
<p>Note that if the status is <strong>Closed</strong>, and there is a zero in the Link column, then those records were never linked.</p></td>
</tr>
<tr class="odd">
<td><strong>Description</strong></td>
<td>This is the <strong>description</strong> of the request.</td>
</tr>
<tr class="even">
<td><strong>Patient</strong></td>
<td>The <strong>patient name</strong> is displayed.</td>
</tr>
<tr class="odd">
<td><strong>SSN</strong></td>
<td>The <strong>Social Security Number</strong> for the patient is displayed.</td>
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
<td><h5 id="yellow-and-red-fields">Yellow and Red fields</h5></td>
<td><blockquote>
<p>Records that have a delayed date beyond 5 days will have the number of days in yellow and the block will be highlighted in red.</p>
<p>Records with 0-5 days will have the number shown in bold print.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### View DOR Calculation Detail

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="dor-detail-button">DOR Detail button</h5></td>
<td><blockquote>
<p>You can view the DOR calculation detail for the range of consults and manual suspense entries that you displayed. When you select the <strong>DOR Detail</strong> button, it doesn’t matter what status is checked because the calculation looks at all the <strong>Open</strong>, <strong>Pending</strong> and <strong>Closed</strong> records from the starting date you selected.</p>
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
<td><h5 id="number-of-manuals">Number of MANUALS</h5></td>
<td><blockquote>
<p>You can view the total number of <em>Manual</em> suspense entries that are in <strong>Open</strong>, <strong>Pending</strong> or <strong>Closed</strong> status. Those in the 6-9 or higher columns show the ones that are Delayed.</p>
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
<td><h5 id="number-of-consults">Number of CONSULTS</h5></td>
<td><blockquote>
<p>You can view the total number of electronic Consults (that were not entered manually) that are in <strong>Open,</strong> <strong>Pending</strong> or <strong>Closed</strong> status and have not had any action taken on them. Those in the 6-9 or higher columns show the ones that are Delayed.</p>
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
<td><h5 id="sub-total">SUB TOTAL</h5></td>
<td><blockquote>
<p>The <strong>SUB TOTAL</strong> row totals the number of <em>Manual</em> suspense entries + the total number of all other consults.</p>
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
<td><h5 id="dor-calculation-detail-window">DOR Calculation Detail window</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/006.png)</p>
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
<td><h5 id="minus-pending">Minus PENDING</h5></td>
<td><blockquote>
<p>This row displays the number of consults that have had an initial action taken on it (starting with the date you selected in the calendar for the starting date which is shown here by 1/1/2003) and put into a <strong>Pending</strong> status.</p>
<p>This number is subtracted from the subtotal for the <strong>Total Delayed</strong> row below that.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

View DOR Calculation Detail, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="total-delayed">TOTAL DELAYED</h5></td>
<td><blockquote>
<p>The <strong>TOTAL DELAYED</strong> is calculation that adds the total number of <em>Manual</em> Suspense records + the total number of all other consults and subtracts the number of consults in a <strong>Pending</strong> status (Pending from before the Start Date selected).</p>
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
<td><h5 id="dor-calculation-detail-window-1">DOR Calculation Detail window</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/007.png)</p>
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
<td><h5 id="total-of-sub-total">Total of Sub Total</h5></td>
<td><blockquote>
<p>The <strong>Total of the Sub Total</strong> field includes: 1) the total from the <strong>Sub Total</strong> above (third row), 2) all totals of <em>Manual</em> Suspense entries and 3) all other electronic consults.</p>
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
<td><h5 id="minus-total-pending">Minus Total Pending </h5></td>
<td><blockquote>
<p>The next row shows the calculation for the Total consults minus the <strong>Pending</strong> consults from the starting date that you selected.</p>
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
<td><h5 id="total-delayed-1">TOTAL DELAYED</h5></td>
<td><p>The <strong>TOTAL DELAYED</strong> field is shown.</p>
<p>This displays the Total Delayed from the grid above (any greater than 5 days delayed) divided by (the result of the total Sub Total minus Total Pending as of 1/1/03) and multiplied by 100. This is the percentage delayed.</p></td>
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
<td><h5 id="percent-delayed">Percent Delayed</h5></td>
<td><blockquote>
<p>The final calculations above, this equals the <strong>Percent Delayed</strong> (shown as 95.37%).</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

View DOR Calculation Detail, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="scenarios-below">Scenarios below</h5></td>
<td><blockquote>
<p>The scenarios below describe different timelines when orders are received at different times of the month and if they are delayed. Then it will explain which month’s Calculation Report where the data will appear.</p>
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
<td><h5 id="scenario-1">Scenario 1</h5></td>
<td><blockquote>
<p>An order is received on Tuesday, June 3rd and is changed to <strong>Pending</strong> or <strong>Closed</strong> status on Friday, 6/6. This is <u>not</u> a delayed order and would appear in the June Calculation Report as an order received.</p>
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
<td><h5 id="scenario-2">Scenario 2</h5></td>
<td><blockquote>
<p>An order is received on Tuesday, 6/3 and is changed to <strong>Pending</strong> or <strong>Closed</strong> on Wednesday, 6/20. This is a delayed order and would be included in the June Calculation Report as a delayed order.</p>
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
<td><h5 id="scenario-3">Scenario 3</h5></td>
<td><blockquote>
<p>An order is received on Thursday, 6/26 and is changed to <strong>Pending</strong> or <strong>Closed</strong> on Tuesday, 7/15. This was <u>not</u> a delayed order in June; however the order is included in the June Calculation Report, because it was received in June. Since it took greater than 5 days to change it to <strong>Pending</strong> or <strong>Closed</strong>, it would also be included in the July report as a delayed order and would be included in the calculations.</p>
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
<td><h5 id="scenario-4">Scenario 4</h5></td>
<td><blockquote>
<p>An order is received on Thursday, 6/26 and changed to <strong>Pending</strong> or <strong>Closed</strong> on Monday, August 4<sup>th</sup>. This is <u>not</u> a delayed order in June; however, the order is included in the June Calculation Report, because it was received in June. Since it took greater than 5 days to change it to <strong>Pending</strong> or <strong>Closed</strong>, it would be included in both the July and August report as a delayed order and would also be included in the calculations.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

View DOR Calculation Detail, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="print-button">Print button</h5></td>
<td><blockquote>
<p>You can print the <strong>DOR Calculation Detail</strong> data by clicking the <strong>Print</strong> button. A <strong>Print Preview</strong> pane will display that allows you to zoom in, scroll forward/ backward, print, save the data, or open/load a new report.</p>
<p>Click the <strong>Close</strong> button to return to the <strong>DOR Calculation Detail</strong> window.</p>
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
<td><h5 id="print-preview">Print Preview</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/008.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### View Pending Calculations

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="pending-calc-button">Pending Calc Button</h5></td>
<td><blockquote>
<p>Click on the <strong>Pending Calc</strong> button on the <strong>DOR</strong> window and the window displays based on the selection criteria of this window.</p>
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
<td><h5 id="pending-status-consults">Pending status consults</h5></td>
<td><blockquote>
<p>The <strong>Pending Calculations</strong> window displays the total number of Workdays with the total number of <strong>Pending</strong> records since an initial action was taken on it. These records are categorized into columns by the number of Workdays it has remained in a <strong>Pending</strong> status.</p>
<p>The calculation used to display these <strong>Pending</strong> status records is from the <u>First Action date</u> (not from Creation Date) to the <u>current date</u>. This is a tool to help managers monitor their consults and manual suspense entries that have been <strong>Pending</strong> for an extended period of time.</p>
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
<td><h5 id="pending-calculations">Pending Calculations</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/009.png)</p>
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
<td><h5 id="print-button-1">Print button</h5></td>
<td><blockquote>
<p>The <strong>Print</strong> button allows you to print the Pending Action Calculations and will display the <strong>Print</strong> dialog box.</p>
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
<td><h5 id="excel-button">Excel button</h5></td>
<td><blockquote>
<p>You can send this data to MS Excel by clicking the <strong>Excel</strong> button. It will launch the application and display the data at the same time.</p>
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
<td><h5 id="close-button">Close button</h5></td>
<td><blockquote>
<p>To exit, click the <strong>Close</strong> button or the ![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/010.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## View 2319 Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### View 2319 – Patient Demographics

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction-2">Introduction</h5></td>
<td><blockquote>
<p>The <strong>View 2319</strong> button displays the 10-2319 Prosthetic patient records. The title bar displays the patient name and SSN. Here are the windows of information that you can view from the patient’s 2319:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Patient Demographics</p>
</blockquote></li>
<li><blockquote>
<p>Clinic Enrollments/Correspondence</p>
</blockquote></li>
<li><blockquote>
<p>Entitlement Info</p>
</blockquote></li>
<li><blockquote>
<p>Appliance Transactions</p>
</blockquote></li>
<li><blockquote>
<p>Auto Adaptive Info</p>
</blockquote></li>
<li><blockquote>
<p>Critical Comments</p>
</blockquote></li>
<li><blockquote>
<p>HISA Information</p>
</blockquote></li>
<li><blockquote>
<p>Home Oxygen Items</p>
</blockquote></li>
</ol>
<blockquote>
<p><strong>Note:</strong> Use the <strong>&lt;Alt&gt;</strong> key and the number to toggle to different tabs.</p>
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
<td><h5 id="demographics-data">Demographics data</h5></td>
<td><blockquote>
<p>You can view the patient demographics for the veteran. This includes: Name (in red if deceased with Date of Death listed above the Date of Birth and the age field will not display), address, next of kin, emergency contact information, veteran benefits and eligibility (former Prisoner of War (highlighted in blue if “Yes”), Aid &amp; Attendance, service connected, non-service connected, etc.).</p>
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
<td><h5 id="patient-demographics-window"><u>1</u>. Patient Demographics window</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/011.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### View 2319 - Clinic Enrollments/Correspondence

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="window-description">Window description</h5></td>
<td><blockquote>
<p>This second tab details clinic enrollments and correspondence for the veteran. This includes the following: the last movement actions (i.e., hospital admissions and discharges), clinic enrollments, pending appointments and correspondence letters.</p>
<p><strong>Note:</strong> Due to some records not having a 1<sup>st</sup> Action date, sorting by this column will not sort in date order.</p>
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
<td><h5 id="clinic-enrollments-correspondence"><u>2</u>. Clinic Enrollments/ Correspondence</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/012.png)</p>
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
<td><h5 id="exit">Exit</h5></td>
<td><blockquote>
<p>To exit, click the <strong>Close</strong> button or the ![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/013.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### View 2319 - Entitlement Information

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="window-description-1">Window description</h5></td>
<td><blockquote>
<p>The third tab details entitlement and loan information for the veteran. This includes the following: PSC Issue Card, clothing allowance, items on loan, and items returned.</p>
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
<td><h5 id="entitlement-info"><u>3</u>. Entitlement Info</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/014.png)</p>
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
<td><h5 id="exit-1">Exit</h5></td>
<td><blockquote>
<p>To exit, click the <strong>Close</strong> button or the ![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/015.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### View 2319 – Appliance Transactions

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="appliance-transactions">Appliance Transactions</h5></td>
<td><blockquote>
<p>The <strong>Appliance Transactions</strong> tab of the <strong>View 2319</strong> window displays all transaction history for a veteran. The <em><strong>Date</strong></em> column is the date of the PO. Columns are re-sizable on this window (not movable). The total records found displays at the bottom.</p>
<p><strong>Note:</strong> Due to some records not having a 1<sup>st</sup> Action date, sorting by this column will not sort in date order.</p>
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
<td><h5 id="steps-5">Steps</h5></td>
<td><blockquote>
<p>To view the Appliance Transactions detail, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                        |
|------|----------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                 |
| 1    | Select a transaction by clicking on it to highlight it.                                                                                |
| 2    | Click the ViewDetail button below to display the appliance details. (You can also double click a record to view the details.) |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="appliance-transactions-1"><u>4</u>. Appliance Transactions</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/016.png)</p>
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
<td><h5 id="exit-2">Exit</h5></td>
<td><blockquote>
<p>To exit, click the <strong>Close</strong> button or the ![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/017.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

View 2319 – Appliance Transactions, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="steps-6">Steps</h5></td>
<td><blockquote>
<p>To continue to view the Appliance Transactions detail, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                           |
|------|---------------------------------------------------------------------------|
| Step | Action                                                                    |
| 3    | The Transaction Detail window is shown below.                         |
| 4    | Click the Close button to return to the Appliance Transaction window. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="appliance-transaction-detail">Appliance Transaction Detail</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/018.png)</p>
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
<td><h5 id="exit-3">Exit</h5></td>
<td><blockquote>
<p>To exit, click the <strong>Close</strong> button or the ![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/019.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### View 2319 – Auto Adaptive Info

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="window-description-2">Window description</h5></td>
<td><blockquote>
<p>The fifth tab details the Auto Adaptive information.</p>
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
<td><h5 id="auto-adaptive-info"><u>5</u>. Auto Adaptive Info</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/020.png)</p>
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
<td><h5 id="exit-4">Exit</h5></td>
<td><blockquote>
<p>To exit, click the <strong>Close</strong> button or the ![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/021.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### View 2319 - Critical Comments

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="window-description-3">Window description</h5></td>
<td><blockquote>
<p>The sixth tab details any critical comments recorded for the veteran.</p>
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
<td><h5 id="critical-comments"><u>6</u>. Critical Comments</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/022.png)</p>
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
<td><h5 id="exit-5">Exit</h5></td>
<td><blockquote>
<p>To exit, click the <strong>Close</strong> button or the ![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/023.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### View 2319 – View HISA Information

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="window-description-4">Window description</h5></td>
<td><blockquote>
<p>The seventh tab details the HISA (Home Improvement Structural Alteration) information including the date, quantity, item, type, vendor, station number, serial, HCPCS Code and cost of the item ordered.</p>
<p><strong>Note:</strong> “<em>HISA Information</em>” is the new name for this window; it used to be “<em>Add/Edit Disability Codes</em>.”</p>
<p><strong>Note:</strong> Due to some records not having a 1<sup>st</sup> Action date, sorting by this column will not sort in date order.</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                               |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                        |
| 1    | Select a transaction by clicking on it to highlight it.                                                                                       |
| 2    | Click the ViewDetail button below to display the HISA information details. (You can also double click a record to view the details.) |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="hisa-information"><u>7</u>. HISA Information</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/024.png)</p>
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
<td><h5 id="exit-6">Exit</h5></td>
<td><blockquote>
<p>To exit, click the <strong>Close</strong> button or the ![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/025.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### View 2319 – Home Oxygen

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="window-description-5">Window description</h5></td>
<td><blockquote>
<p>The eighth tab details the <strong>Home Oxygen</strong> information including the date, quantity, item, type, vendor, station, serial, HCPCS Code, and total cost of the item(s).</p>
<p><strong>Note:</strong> Due to some records not having a 1<sup>st</sup> Action date, sorting by this column will not sort in date order.</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                      |
|------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                               |
| 1    | Select a transaction by clicking on it to highlight it.                                                                                              |
| 2    | Click the ViewDetail button below to display the Home Oxygen information details. (You can also double click a record to view the details.) |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="home-oxygen"><u>8</u>. Home Oxygen</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/026.png)</p>
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
<td><h5 id="exit-7">Exit</h5></td>
<td><blockquote>
<p>To exit, click the <strong>Close</strong> button or the ![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/027.png) button in the top right-hand corner.</p>
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
<td><h5 id="view-detail">View Detail</h5></td>
<td><blockquote>
<p>When you select a record and click the <strong>View Detail</strong> button, the following window displays as shown on the next page</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

View 2319 – Home Oxygen, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="view-detail-button">View Detail button</h5></td>
<td><blockquote>
<p>After clicking the <strong>View Detail</strong> button on the <strong>Home Oxygen</strong> window, the following window displays for the patient.</p>
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
<td><h5 id="transaction-detail-window">Transaction Detail window</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/028.png)</p>
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
<td><h5 id="close-button-1">Close button</h5></td>
<td><blockquote>
<p>To exit, click the <strong>Close</strong> button or the ![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/029.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/030.png)![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/031.png)![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/032.png)![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/033.png)

## View and Manage the DOR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### View CPRS

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="function-description">Function description</h5></td>
<td><blockquote>
<p>The <strong>View CPRS</strong> button from the <strong>DOR</strong> window allows you to view all the consult data on the <strong>View CPRS</strong> window as shown below. This is the same data as in the electronic Consult - <strong>Suspense (SU) Menu</strong> feature where you can enter CD for the CPRS Display.</p>
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
<td><h5 id="view-cprs-window">View CPRS window</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/034.png)</p>
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
<td><h5 id="close-button-2">Close button</h5></td>
<td><blockquote>
<p>To exit, click the <strong>Close</strong> button or the ![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/035.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### View Request

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="function-description-1">Function description</h5></td>
<td><blockquote>
<p>When you click the <strong>View Request</strong> button on the <strong>DOR</strong> window, the <strong>View Request</strong> window displays as shown below. This provides the display of the manual suspense entry for the patient.</p>
<p><strong>Note:</strong> You can also double click on a record in the <strong>DOR</strong> window grid to display this <strong>View Request</strong> window.</p>
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
<td><h5 id="view-request-window">View Request window</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/036.png)</p>
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
<td><h5 id="close-button-3">Close button</h5></td>
<td><blockquote>
<p>To exit, click the <strong>Close</strong> button or the ![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/037.png) button in the top right-hand corner.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Save as an Excel File

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="excel-button-1">Excel Button</h5></td>
<td><blockquote>
<p>The <strong><u>E</u>xcel</strong> button on the <strong>DOR</strong> window will automatically launch the Microsoft Excel software program for you. It converts the data that you have selected to display into the Excel file as shown below.</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;X&gt;</strong> key.</p>
<p>This feature creates a temporary Excel <strong>.CSV</strong> file in the C:\NPPDDownLoad folder where the file is temporarily held. The file name is based on the site + the beginning and ending range of the patient’s SSN. You can save this as an Excel file using the <strong>Save As</strong> option from the <strong>File</strong> Menu. <u>When you exit the <strong>Prosthetics Main Menu</strong> window (VISTA suite), the <strong>.CSV</strong> file will be deleted</u>.</p>
<p><strong><u>Example</u>:</strong> The <strong>DOR_9_50_60.csv</strong> filename includes the Site ID # or “ALL” and SSN range.</p>
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
<td><h5 id="ms-excel-data">MS Excel data</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/038.png)</p>
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
<td><h5 id="ms-excel">MS Excel</h5></td>
<td><blockquote>
<p>You can now use any of the features of Microsoft Excel to manipulate your data. Notice that you may need to scroll to the right to view all of the columns.</p>
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
<td><h5 id="print-the-data">Print the data</h5></td>
<td><blockquote>
<p>You can also print the data from Microsoft Excel. Click the <strong>File</strong> Menu and the <strong>Print</strong> option. See next page for more printing information.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Print the DOR

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="print-the-dor-data">Print the DOR data</h5></td>
<td><blockquote>
<p>You can print the <strong>DOR</strong> data using the <strong>Print</strong> button to send this data to your local printer. You can also click the <strong>File</strong> Menu and the <strong>Print-Request Grid</strong> option, and the <strong>Print</strong> dialog box displays. The layout of the print will be the same as the display.</p>
<p><strong><u>Shortcut</u>:</strong> Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;P&gt;</strong> key.</p>
<p><strong>Note:</strong> You can select a different printer that you have setup to print the detail.</p>
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
<td><h5 id="landscape-default">Landscape default</h5></td>
<td><blockquote>
<p>When printing grids, the default is set to print in the <strong>Landscape</strong> format and then returns the printer to the prior state.</p>
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
<td><h5 id="steps-7">Steps</h5></td>
<td><blockquote>
<p>To print the DOR, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                                                                                |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                                                                                         |
| 1    | Click the <u>P</u>rint button on the DOR window.                                                                                                                       |
| 2    | The Print dialog box displays.                                                                                                                                             |
| 3    | Click the <u>P</u>roperties button (to the right of the Name field) on the Print dialog box if you want to change the page orientation of the printout. (Optional) |
| 4    | Click the OK button.                                                                                                                                                       |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="print-dialog-box">Print dialog box</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/039.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Appendix A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Using the Menus

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="menus">Menus</h5></td>
<td><blockquote>
<p>Below are the different menus and menu options that are available to be used instead of the corresponding buttons. You can use these menu options alternatively.</p>
<p>The <strong>Help</strong> Menu is the only menu that does not have a corresponding button. This menu leads you to online help through the <strong>Contents</strong> option. The <strong>Section 508</strong> option is described more in Appendix B.</p>
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
<td><h5 id="file-menu">File Menu</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/040.png)</p>
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
<td><h5 id="select-and-display-menu">Select and Display Menu</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/041.png)</p>
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
<td><h5 id="view-menu">View Menu</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/042.png)</p>
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
<td><h5 id="help-menu">Help Menu</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/043.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Appendix B

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Getting Help

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
<p>Press the <strong>&lt;Alt&gt;</strong> key + <strong>&lt;H&gt;</strong> key. (This activates the <strong>Help</strong> Menu, not the DOR contents.)</p>
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
<td><h5 id="help-menu-1">Help Menu</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/044.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Activate Section 508 Assistance

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction-3">Introduction</h5></td>
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
<td><h5 id="steps-8">Steps </h5></td>
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
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/045.png)</p>
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
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/046.png)</p>
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
<td><h5 id="exitrestart-message">Exit/Restart message</h5></td>
<td><blockquote>
<p>![](rmpr-3-59-delayed-order-report-dor-gui-user-manual/047.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>