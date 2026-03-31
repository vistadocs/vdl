---
title: OR*3*153 CPRS Query Hepatitis C Reports User Manual
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: CPRS Query Hepatitis C Reports
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*153
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: > The Hepatitis C Case Registry contains important demographic and clinical data on all VHA patients identified with Hepatitis C infection. The registry extracts VISTA pharmacy, laboratory, and pathology databases in order to provide the key clinical information needed to track disease stage, diseas
audience: 
keywords: 
  - table
  - contents
  - query
  - strong
  - cprs
  - report
  - reports
  - hepatitis
  - class
  - manual
page_count: 0
word_count: 4711
section_count: 15
table_count: 3
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: APRIL 2003
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_30_153um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_30_153um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/001.png)

> CPRS QUERY

> (HEPATITIS C REPORTS)

> USER MANUAL

> APRIL 2003

> Department of Veterans Affairs

> V*IST*A System Design & Development

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
    - [Recommended Users](#recommended-users)
    - [Related Manuals](#related-manuals)
    - [Section 508 Compliance](#section-508-compliance)
- [Introduction](#introduction)
- [Signing on to the CPRS Query Tool](#signing-on-to-the-cprs-query-tool)
- [Security, Keys, and Restrictions](#security-keys-and-restrictions)
    - [PARAMETER:](#parameter)
- [Using the CPRS Query Tool](#using-the-cprs-query-tool)
  - [Creating Standard Predefined Queries/Reports](#creating-standard-predefined-queriesreports)
    - [Patient Lists](#patient-lists)
  - [Example 1: Abnormal Results Query](#example-1-abnormal-results-query)
  - [Example 2: Consult Status Report](#example-2-consult-status-report)
  - [Example 3: Incomplete Orders Query](#example-3-incomplete-orders-query)
  - [Example 4: Recent Activity Query](#example-4-recent-activity-query)
  - [Example 5: Scheduled/Due Activity Query](#example-5-scheduleddue-activity-query)
  - [Creating Custom Reports](#creating-custom-reports)
    - [Criteria for Custom Queries/Reports](#criteria-for-custom-queriesreports)
    - [Patient List](#patient-list)
    - [Sources](#sources)
    - [Filters](#filters)
    - [Date/Time](#datetime)
    - [Search Criteria](#search-criteria)
    - [Displayable Fields](#displayable-fields)
    - [Patient Information](#patient-information)
    - [Orders and Consults](#orders-and-consults)
    - [Documents](#documents)
    - [Visits/Appointments](#visitsappointments)
  - [Example 1: Steps to Create a Custom Query or Report](#example-1-steps-to-create-a-custom-query-or-report)
  - [Example 2: Creating a Custom Report – by Orderable Item](#example-2-creating-a-custom-report-by-orderable-item)
  - [Editing an Existing Report](#editing-an-existing-report)
  - [Exporting a Report](#exporting-a-report)
    - [To export a report, follow these steps:](#to-export-a-report-follow-these-steps)
- [Appendix A: Creating a Query to Use Multiple Times](#appendix-a-creating-a-query-to-use-multiple-times)
- [Appendix B: Accessibility for Individuals with Disabilities](#appendix-b-accessibility-for-individuals-with-disabilities)
  - [Changing the Font Size](#changing-the-font-size)
    - [CPRS Menus and Windows Alert Boxes](#cprs-menus-and-windows-alert-boxes)
  - [Changing the Window Background Color](#changing-the-window-background-color)
  - [Keyboard Shortcuts for Common CPRS Query Tool Commands](#keyboard-shortcuts-for-common-cprs-query-tool-commands)
    - [Navigation](#navigation)
    - [Keyboard shortcuts on the buttons](#keyboard-shortcuts-on-the-buttons)
    - [Download the Configuration File from the FTP Site](#download-the-configuration-file-from-the-ftp-site)
    - [Cut and Paste Information into the Existing Configuration File](#cut-and-paste-information-into-the-existing-configuration-file)
    - [Create a New Configuration File Manually](#create-a-new-configuration-file-manually)
    - [Create the Configuration File while Running JAWS](#create-the-configuration-file-while-running-jaws)
> The CPRS Query Tool User Guide provides detailed instructions for using the CPRS Query Tool software.

### Recommended Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CPRS Query Tool software is designed for use by designated Local Coordinators, Managers, and Clinicians who are responsible for and provide care to VA patients with hepatitis C infection or wish to use the reports functionality for other purposes.

### Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CPRS Query Tool– Installation Guide Version 1.0 Clinical Case Registries – Installation Guide Version 1.0 Clinical Case Registries – Technical Manual Version 1.0 Clinical Case Registries – User Manual Version 1.0

### Section 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Veterans Health Administration (VHA) fully supports Section 508 of The Rehabilitation Act and is committed to equal access for all users. While every effort has been made to ensure Section 508 compliance, we realize that there may be other issues.
> See Appendix A for Accessibility Instructions.

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Hepatitis C Case Registry contains important demographic and clinical data on all VHA patients identified with Hepatitis C infection. The registry extracts V*IST*A pharmacy, laboratory, and pathology databases in order to provide the key clinical information needed to track disease stage, disease progression, and response to treatment on a regional and national level.

> In order to improve the utility of the local Hepatitis C registry lists, the CPRS Query tool has been developed. This tool allows local clinicians to take advantage of the greater range of clinical information within the local CPRS system. This tool allows clinicians to use the list of patients in the local Hepatitis C Registry and other lists of patients to query for clinical data related to appointments, orders, notes, and results across multiple patients at once.

> ☞NOTE: This manual includes some specific examples of how to use the CPRS Query tool. The basic operations of the tool use “point and click” actions familiar to most users. In the first example, we include images of all pop-up boxes the user sees. For efficiency, we

> do not include this level of detail in subsequent examples, when the operations are the same as those previously described.

# Signing on to the CPRS Query Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once the CPRS Query Tool (Hepatitis C Reports) has been installed on your workstation, you can sign on – either through an icon or through the Tools menu, depending on how your site sets it up.

> To start the Query tool:

1.  Double-click on the CPRS Query icon on your desktop, or open CPRS Query from the Tools menu.
2.  When the Connect To dialog appears, click on the down-arrow, select the appropriate account (if more than one exists), and click OK.

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/002.png)

> After you connect to the appropriate account, the Sign- on window appears.

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/003.png)

1.  Type your access code into the Access Code field and press the Tab key.
2.  Type your verify code into the Verify Code field and press the Enter key or click on

> OK.

> ☞ Shortcut: You can also type the access code, followed by a semicolon (;), and the verify code in the access code box. Once you have done this, press the Enter key or click OK.

# Security, Keys, and Restrictions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ORRCM REPORTING Required Menu Option

> To use CPRS Query, a user must be assigned the menu option ORRCM REPORTING.

> ROR VA HEPC USER Required key to see the “Registry” tab.

> To see the Registry tab when selecting patients, a user must be assigned the ROR VA HEPC USER key.

> TIU/ASU Business Rules Business Rules in TIU/ASU authorize specific users or groups of

> users to perform specified actions on documents in particular statuses. A set of business rules is exported with TIU/ASU; sites can edit or add to these.

> When you search for documents in CPRS Query, the TIU business rules are applied. Users may not see a document on their list or the content of the document in the detailed display if the business rules do not allow access to the document.

### PARAMETER:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ORHEPC ABNORMAL Abnormal Result Enabled Date

> START Upon installation, this parameter is set at the PACKAGE level to the date the patch was installed. It may also be set at the SYSTEM level locally. Sites can change this parameter by using the General Parameter Tools, available on the CPRS Configuration (IRM) menu, or from programmer mode: XPAR MENU TOOLS/EP (Edit Parameter Values) option.

> The Abnormal Results (field 72) field is added to the Orders file

> \(100\) with this patch. This field will be defined as YES for any order that is identified as an abnormal result, as defined by the following criteria:

> Consults = Existence of Significant Findings Lab = Critical high or low value

> Radiology = Primary Diagnostic Code assigned to the exam report has 'Generate Abnormal Alert' set to YES in file \#78.3

> When a user queries the abnormal result report, the available abnormal report start date will refer to the value of this parameter. Therefore, any data prior to the date set in the ORHEPC ABNORMAL START parameter will NOT be included in the report query.

# Using the CPRS Query Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After you log in to the CPRS Query Tool (Hepatitis C Reports), a warning window for confidentiality appears to ask you whether to continue or not:

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/004.png)

> Then a window similar to the following appears:

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/005.png)

- You can choose an existing report, or create a customized query.
- The bottom part of the window shows the criteria used for building the query. If any of these criteria are highlighted with blue text, you must enter more details. Otherwise, you can edit any of the criteria.
- You can then display the report, based on the criteria selected.

## Creating Standard Predefined Queries/Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You can obtain predefined reports of activities by designating a patient list and time period. Default time periods are provided

### Patient Lists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The initial list of patients is constructed from the following list sources:

- CPRS Patient Lists (Provider, Personal, Team)
- PCMM Team Lists
- Ward and Specialty Lists
- Local Registry (i.e., Hepatitis C Registry)

> The following predefined queries are available. You can use the default time criteria, or specify some other time period.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Report</strong></th>
<th><blockquote>
<p><strong>Criteria</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Abnormal Results</td>
<td><ul>
<li><p>Patients with abnormal results or significant findings.</p></li>
<li><p>Default Time range: Past six months.</p></li>
<li><p>A selected time range.</p></li>
<li><p>A specific patient list.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Consult Status Report</td>
<td><ul>
<li><p>A specific patient list.</p></li>
<li><p>Default Time range: Past six months.</p></li>
<li><p>A selected time range.</p></li>
<li><p>A selected consulting service.</p></li>
<li><p>Default service: ALL SERVICES</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Incomplete Orders</td>
<td><ul>
<li><p>Orders with a specified status.</p></li>
<li><p>Default Time range: Past six months.</p></li>
<li><p>Orders placed during a specific time range.</p></li>
<li><p>A specific patient list.</p></li>
<li><p>Specified service.</p></li>
<li><p>Default Status: PARTIAL RESULTS OR PENDING</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Recent Activity</td>
<td><ul>
<li><p>Patients on a specific ward or any patient list.</p></li>
<li><p>Default Time range: Past 24 hours.</p></li>
<li><p>Last order activity for a specific time range.</p></li>
<li><p>Notes for a specific time range</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Scheduled/Due Activity</td>
<td><ul>
<li><p>Orders where the order status is pending or scheduled.</p></li>
<li><p>Default Time range: Past six months through tomorrow.</p></li>
<li><p>A specific patient list.</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Example 1: Abnormal Results Query

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See the “Security, Keys, and Restrictions” section for information on setting the Abnormal Result Enabled Date parameter. Any abnormal results prior to the installation date will NOT be included on the Abnormal report (there is no historical flagging or population of the field).

> ☞NOTE: CPRS Query gets its abnormal results information from related VISTA applications via HL7 messages, based on existing package/service processing rules:

> Consults = existence of Significant Findings Lab = critical high or low value

> Radiology = Primary Diagnostic Code assigned to the exam report has 'Generate Abnormal Alert' set to YES in file \#78.3

> In this example, we’ll look for all the patients on the Hepatitis C local registry with abnormal results or significant findings within the date range of the past six months.

#### Steps to create query

1.  Open the query tool.
2.  In the main window, click Abnormal Results.

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/006.png)

3.  Click the \<select patient list\> link.

> Patient List window

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/007.png)

4.  Add the Local Hepatitis C Registry to the selected lists panel by clicking on the name and clicking the Add button, or by double-clicking the name.
5.  Click the OK button.
6.  Modify the date range, if desired, by clicking on the date range link under Find Orders.

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/008.png)

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/009.png)

7.  Click the Show Report button. A screen with available reports appears. Note the advisory statement in yellow.

> NOTE: In the following steps you will be able to view individual patient findings and store the report for additional review or future reference. These options are available for all reports produced with the CPRS Query tool.

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/010.png)

8.  Select an Order/Request from the list to display, print, or export by clicking on the name. More information appears in the bottom pane. You can adjust the two panes by dragging on the bar in between.

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/011.png)

> Print: Contact your CPRS support person if you need to install a new network printer. Since the report contains confidential patient information, the printer should be one appropriate to handle this type of information (e.g., not in a public area).

> Export: See page 46 for instructions about Exporting Queries/Reports.

> Exit: Note that reports are not stored. If you click on \<Exit\> without printing or exporting your report, processing will stop and you will need to run the report again. Also, information in reports is based on what data are in the system at the time a report is run. Thus, running a report with the same criteria at two different times may produce different results, as new information may have been added when you run the second report.

## Example 2: Consult Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In this example, we create a list of all consults for all services for the past six months for all the patients on a personal/team list called New List 1.

#### Steps to create query

1.  Open the CPRS Query tool.
2.  In the main window, click Consult Status Report.

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/012.png)

3.  Click the \<select patient list\> link.

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/013.png)

4.  Select the Personal/Team tab and click on New List1 and the Add button to add it to the list of selected lists.
5.  Click the OK button.
6.  Click the date range link under “Find Consults” if you wish to change the date range.
7.  The default value is \<ALL SERVICES\>. If you wish to change this, click on it and you will be able to select specific services to include in your search. In the left side of Consult Services window, click on a service and then click \<Add\> to include the service in your search. To remove a service from your search, click on it in the right window, then click on \<Remove\>.

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/014.png)

8.  Click the OK button.
9.  Click the Show Report button.
10. Select an Order/Request.
11. You will be able to select an Order/Request to display, print, or export

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/015.png)

> 04/28/20003 CPRS Query User Manual 14

## Example 3: Incomplete Orders Query

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In this example, we create a list of all orders with a partial or pending status for the past six months for patients on a Medical Observation Specialty List

#### Steps to create query

> 1\. In the main window, click Incomplete Orders.

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/016.png)

1.  Click the\<select patient list\> link.
2.  Click the Specialty tab and add Medical Observation to the list of selected lists.

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/017.png)

3.  Click the OK button.
4.  Click the \<PARTIAL RESULTS or PENDING\> link if you wish to change order statuses. In the order status, click on the box to the left of the order status you wish to include in your search. A checkmark appears in the box of any order status that will be included in the report. To remove an order status from the search, click the box again to remove the check mark.

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/018.png)

5.  Click the Show Report button. You can then select an Order/Request to display, print, or export.

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/019.png)

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/020.png)

## Example 4: Recent Activity Query

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In this example, we create a list of recent activity for orders and documents (Clinical Procedures, Consults, Discharge Summaries, and Progress Notes) during the past month for patients on the local Hepatitis C Registry.

#### Steps to create query

1.  In the main window, click Recent Activity.

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/021.png)

2.  Click the \<select patient list\> link.
3.  Add the Local Hepatitis C Registry to the list of selected lists.
4.  Click the OK button.
5.  Change the time period from “during the Past 24 Hours” by clicking on the date link.
6.  Click the \<Consults or Discharge Summaries or Progress Notes\> link if you wish to modify the document classes.
7.  In the Document Class window click to check or uncheck the document class(es) you want to include in your search..

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/022.png)

8.  Click the Show Report button. A list of orders and requests during the past week for patients on the Hepatitis C Registry is displayed.

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/023.png)

9.  Select a record, and the details are displayed. You can then print or export the report.

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/024.png)

## Example 5: Scheduled/Due Activity Query

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In this example, we create a list of all pending or scheduled Imaging orders and pending or scheduled consults for the past six months for patients on the local Hepatitis C Registry.

#### Steps to create query

1.  In the main window, click Scheduled/Due Activity

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/025.png)

2.  Click the \<select patient list\> link.
3.  Add the Local Hepatitis C Registry to the list of selected lists.
4.  Modify any of the other criteria listed in the bottom pane by clicking on the underlined text and making your choices in the windows that appear.
5.  Click the OK button.
6.  Click the Show Report button.
7.  Select an Order or Request, and the details are displayed. You can then print or export the report.

> NOTE: Some sites do not mark consults as scheduled, so in order to view consults that have been received by the service but not completed, you may need to search for statuses of PENDING, ACTIVE, SCHEDULED, and RECEIVED.

## Creating Custom Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After you log in to CPRS Query, you can create a customized search/report. As with predefined reports, the bottom part of the window shows the criteria used for building the search. If any of these criteria are highlighted with blue text, you must enter more details. Otherwise, you can edit any of the criteria. You can then display the report, based on the criteria selected.

### Criteria for Custom Queries/Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You can construct reports of activities for patients according to many criteria. Begin by selecting an initial list of patients. Applying a filter further refines the list and restricts the patients that appear in the report. Once the patient set is specified, search criteria are set that will retrieve matching data items for each patient. These data items include orders, documents, and appointments. You can then specify which fields are displayed for each data item returned. The query is then executed and a columnar report is generated.

### Patient List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Each query begins with a list of patients.

### Sources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The initial list of patients is constructed from the following list sources: o CPRS Patient Lists (Provider, Personal, Team)

- PCMM Team Lists
- Ward and Specialty Lists
- Local Registry (i.e., Hepatitis C Registry)

### Filters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Filters can then be applied to the list of patients, if desired. These filters determine whether a particular patient appears in the report. The following filters are available:

- Patient currently admitted to the hospital
- Clinic stop at any location
- Visit to specific clinic(s) within a time frame.

### Date/Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Pick one of the following date criteria on your query definition:

- ORDERS: looks for the date entered.
- ORDERS queries that involve the signature status: look at the date of the various actions as well.
- DOCUMENTS: looks for the reference date.
- VISITS: looks for the visit date.

### Search Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For each patient, the query retrieves data items that meet preset criteria. These data items include orders, clinical documents, and appointments. For each type of data item, the user selects criteria that the item must possess for inclusion in the report. Only orders that match all the criteria are returned. None of the criteria are specifically required— most reports would use only a few of the available criteria. You can also query by orders that meet none of the specified criteria.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 23%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Query Type</strong></th>
<th><blockquote>
<p><strong>Criteria</strong></p>
</blockquote></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Orders and Consults</td>
<td>Service Category</td>
<td><p>Identifies which service the order was sent to. This criterion is based on the Display Group, which is arranged in a hierarchy. Selecting one display group automatically includes any group that is subordinate to it. For example, selecting “Laboratory” will automatically include the various types of lab tests (chemistry, hematology, etc.) subordinate to it. You can also select only one or some of the subordinate services in a Display Group. To do this, click on the plus sign to the left of the Display Group to get a list of all the subordinate services for that group, then choose the subordinate services you</p>
<p>wish to include in your search.</p></td>
</tr>
<tr class="even">
<td></td>
<td>Order Status</td>
<td>Identifies the state of the order (pending, active, complete, etc.)</td>
</tr>
<tr class="odd">
<td></td>
<td>Signature Status</td>
<td><p>Identifies the status of the signature</p>
<p>(electronically signed, on the chart, etc.)</p></td>
</tr>
<tr class="even">
<td></td>
<td>Abnormal Results</td>
<td><p>Allows you to search for items related to</p>
<p>abnormal results or significant findings associated with a result.</p></td>
</tr>
<tr class="odd">
<td></td>
<td>Requesting Clinician</td>
<td>Identifies the clinician who initially wrote the order.</td>
</tr>
<tr class="even">
<td></td>
<td>Order Text</td>
<td><p>Text that was displayed when the order was signed or the order was updated by a receiving</p>
<p>service</p></td>
</tr>
<tr class="odd">
<td>Documents</td>
<td>Title</td>
<td><p>Specifies a particular type of document, such as progress notes in general to a specific note title used in a particular clinic. You can search by</p>
<p>BOTH title and class</p></td>
</tr>
<tr class="even">
<td></td>
<td>Class</td>
<td>Document Class refers to Progress Notes, Consults, Procedures, etc.</td>
</tr>
<tr class="odd">
<td></td>
<td>Status</td>
<td><blockquote>
<p>Status of note: unsigned, uncosigned, etc.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>Author</td>
<td>Author of document</td>
</tr>
<tr class="odd">
<td></td>
<td>Visit Location</td>
<td><blockquote>
<p>Location of visit</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>Visits/Appointments</td>
<td><strong>Clinic</strong> narrows the search to a specific clinic or clinics.</td>
</tr>
</tbody>
</table>

### Displayable Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once the query criteria have been set up, you can select which fields will be displayed for each data item. The following fields are available:

### Patient Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Name
- SSN (last four digits only)
- Age
- Ward Location

### Orders and Consults

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Order Date/Time
- Ordering Provider
- Order Text
- Order Status
- Signature Status
- Service (Display Group)
- Result Flag (abnormal, critical, significant)
- Significant Finding Text

### Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Reference Date/Time
- Title
- Author
- Status
- Expected Cosigner

### Visits/Appointments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Date/Time
- Location
- Visit Status

> NOTE: These fields are only available when they’re appropriate. For example, if you’re only querying based on Orders criteria, the Documents fields are not available. If you’re doing a negative query (only records where none of the specified criteria are met), then only the patient information fields are available.

## Example 1: Steps to Create a Custom Query or Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In this example, we want to look for Hepatitis C Registry patients seen by Dr. Anderson since January 5, 2003.

1.  After opening the CPRS Report Tool application, click on Create Custom Search. The following window appears:

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/026.png)

2.  Click in the box for Primary Outpatient Provider.
3.  In this example, check the box for “Clinic Appointments / Visits.”

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/027.png)

4.  Select blue-highlighted items in the bottom box to further specify values.

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/028.png)

5.  Click “\<Select patient list\>”; the following window appears:

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/029.png)

6.  Click Local HepC Registry and click Add, then OK. (Or, simply double-click on Local HepC Registry to add it.)
7.  Click on \< during the date range\> to enter the time frame. This screen appears.

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/030.png)

8.  After date selections are made, click OK.
9.  Click \<select providers\>. When the Provider window opens, click on ANDERSON, DOCTOR, then click the Add button (or double-click on the provider). Click OK.

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/031.png)

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/032.png)

10. When you click Next, the following window appears. Check Clinic Location if you want to limit the report to a specific clinic. If you do not select a specific clinic, the report will contain visits with the selected provider(s) in all clinics in which they schedule patients.

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/033.png)

11. If you do choose to limit the search to specific clinic(s), the lower portion of the window will now include a blue link for \<select clinic(s)\>. Click on this to see a screen in which you specify the clinics to include. After selecting the desired clinics, click OK to return to the main query window.

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/034.png)

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/035.png)

12. Select each of the fields you wish to display in your report, and then click the Add button (or double click on the field) to include the field in your report.
13. Click Next to name and save your Custom Report. Click to put a check in the box to the left of “Save the report for future use” then click in the white space under \<Report Name\> and type in a name for the report that will describe what criteria are used.

> Note 1: If you don’t give the report a name, the system will simply name it “Custom Report \#x”

> Note 2: If you don’t save the report, you will need to reconstruct the criteria for future queries.

> Note 3: Because the system uses the data currently in the system, running a custom report with the same criteria on two different occasions may produce slightly different results.

> .

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/036.png)

14. Click the Show Report button to display the report.

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/037.png)

## Example 2: Creating a Custom Report – by Orderable Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In this example, we create a list all patients on the Registry list who had an abnormal Hepatitis profile test during the last month.

1.  Open the query tool.
2.  In the top pane, select Create Custom Search...
3.  Check the box for Orders/Results

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/038.png)

3.  On the bottom pane, click the \<select patient list\> link.

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/039.png)

4.  On the Patients form, select the Registry tab.
5.  On the left pane, select "Local HepC Registry" and then click the Add button.
6.  Select Active in the Registry Status option group at the bottom of the form, and then click the OK button.

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/040.png)

7.  On the bottom pane, click the \<during the date range\> link.
8.  Select Past Month, then click OK.

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/041.png)

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/042.png)

9.  Click the Next button.
10. When you click Next, this Orders screen appears:

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/043.png)

11. On the top pane, click the “Specific Items Ordered” option in the Type of Order option group. The words "where the order is for \<select orderable item\> appear in the Find Orders section.
12. Click the \<select orderable item\> link. The Orderable Items form opens.

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/044.png)

13. Select HEPATITIS PROFILE from the list of orderable items and click the Add button. NOTE: lab test names may vary among facilities. Choose the appropriate name at your facility.

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/045.png)

14. Click the OK button. The Orderable Item form closes and returns you to the Orders page.

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/046.png)

15. Click Abnormal Results Flag under “Find orders with specific statuses or flags.” A window similar to the following will appear; click OK, then click Next.

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/047.png)

16. The Field Selection page opens. Select each of the fields below, and then click the Add button to add the field to the report.
    - Patient Name,
    - Patient SSN,
    - Patient Ward,
    - Order /Consult Date,
    - Order /Consult Status, and
    - Order/Consult Abnormal Results.

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/048.png)

17. After adding the fields, click the Finish button.
18. Give a name to the report (the default name is "New Custom Report \#.")

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/049.png)

19. Click the Show Report button. Note the caveat in the yellow panel at the top: “Reports are compiled for groups of patients and do not replace the need for clinical judgment in individual patient care.”

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/050.png)

## Editing an Existing Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In this example, we will edit the report we just created, to include patients with any visits during the current quarter.

1.  In the first window of the CPRS Query Tool, click on the report you just created, New Custom Report \#1, then click the Edit button at the bottom of the screen.

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/051.png)

2.  Select an item you wish to edit, such as the time period.

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/052.png)

3.  Click the Finish button. Click the Yes button on the pop-up window.
4.  Click the Rename button and rename the report.

> NOTE: You can view your current list of reports by clicking the button “Click to view your current review list.”

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/053.png)

5.  Click in the Save the report for later reuse, if desired, then click the Finish button.

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/054.png)

## Exporting a Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You can export any report generated by the CPRS Query Tool as a text file.

### To export a report, follow these steps:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Generate a report, following directions for any of the previous queries.
2.  Click Export on the Show Reports screen. A warning box appears:

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/055.png)

3.  Click Yes, and the “Save CPRS Report Data as” dialog box appears.

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/056.png)

4.  Type a name for the file.
5.  Browse to the location where you would like to store the file.
6.  Click Save.

> By default, reports are stored as text (.txt) files. Once you have stored a report, you can import it into other programs, such as Excel. Remember that reports contain confidential patient information and must be treated as any other confidential patient information.

# Appendix A: Creating a Query to Use Multiple Times

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Thanks to Northern California HCS for this site example.

> This example shows how to create a query to use multiple times by storing the template with the date range to be filled in each time.

1.  Select Create Custom Report (of Hepatitis C Registry patients). Choose to view orders in the Search Items window.

![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/057.png)

2.  Choose to limit items to laboratory tests and choose the list of specific tests to view. In this example, the Hepatitis C viral loads (qual and quant) and the Hepatitis C Genotypes are chosen from the list as the orderable items to view.

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/058.png)

3.  Fill in all the blue underlined items except for the date range. Save the report template.

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/059.png)

> The report is now saved without the date range – the date range can be filled in each time the user wants to run this saved report.

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/060.png)

> The results give a list of all 382 patients in the registry (4100 patients) who had these tests ordered during this time period

# Appendix B: Accessibility for Individuals with Disabilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section discusses the features of the CPRS Query Tool that allow people who are blind, who have limited vision, or who have limited dexterity to use the software effectively. The features discussed include changing the font and window sizes, changing the background color, configuring a screen reader, and keyboard equivalents for common CPRS Query Tool commands.

## Changing the Font Size

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTE: enlarging fonts may cause distortion to the screen, or make parts not visible, so it may be preferable to use screen magnifiers.

### CPRS Menus and Windows Alert Boxes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To change the font size used for CPRS menus and Windows alert boxes, follow these steps:

> ☞ NOTE: The steps below will change the font used in menus and Windows boxes for ALL of the applications on your computer. Also, enlarging fonts may cause distortion to the screen, or make parts not visible, so it may be preferable to use screen magnifiers.

1.  Click Start \| Settings \| Control Panel.
2.  Double-click on the Display icon.
3.  Click the Appearance tab.

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/061.png)

4.  From the Item drop-down list box, select either Menu or Message Box.
5.  Select a font from the Font drop-down list.
6.  Select a size from the Size drop-down list.
7.  Select a color from the Color drop-down list.
8.  Click Apply.
9.  If necessary, repeat steps 4-8 to change the display settings for another item.
10. Press OK.

## Changing the Window Background Color

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To change the background color of CPRS Query Tool windows and dialog boxes, follow these steps:

> ☞ NOTE: The steps below will change the background color of windows and dialog boxes for ALL applications on your computer.

1.  Click Start \| Settings \| Control Panel.
2.  Double-click on the Display icon.

> The *Display Properties* dialog box will appear.

3.  Click the Appearance tab.
4.  From the Item drop-down list box, select Window.
5.  Select a color from the Color drop-down list box.
6.  Click Apply.

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/062.png)

7.  If necessary, repeat steps 4-6 to change the display settings for another item.
8.  Press OK.

> ![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/063.png)

> In this example, the Window color has been changed to blue.

## Keyboard Shortcuts for Common CPRS Query Tool Commands

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Navigation</strong></th>
<th><strong>Keystroke</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>To advance to the next field, button, or control (left-right).</td>
<td><strong>Tab</strong></td>
</tr>
<tr class="even">
<td><p>To exit a field that accepts tabs (e.g. the details pane of the Notes tab) and move to the next</p>
<p>control (left-right)</p></td>
<td><strong>Control</strong> + <strong>Tab</strong></td>
</tr>
<tr class="odd">
<td>To exit a field that accepts tabs and move to the previous control (right-left)</td>
<td><strong>Shift</strong> + <strong>Control</strong> + <strong>Tab</strong></td>
</tr>
<tr class="even">
<td>Pull down a list box</td>
<td><strong>Down Arrow</strong></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Navigation</strong></th>
<th><strong>Keystroke</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Navigate a list box</td>
<td><strong>Up Arrow</strong> or <strong>Down Arrow</strong></td>
</tr>
<tr class="even">
<td>Select an item in a list box</td>
<td><strong>Return</strong> or <strong>Enter</strong></td>
</tr>
<tr class="odd">
<td>Expand a tree view</td>
<td><strong>Right Arrow</strong></td>
</tr>
<tr class="even">
<td>Collapse a tree view</td>
<td><strong>Left Arrow</strong></td>
</tr>
<tr class="odd">
<td>To advance (left-right) to the next tabbed page of a dialog box</td>
<td><p><strong>Right arrow</strong></p>
<p>![](or-3-153-cprs-query-hepatitis-c-reports-user-manual/064.png)</p>
<p>Example of a dialog box with tabbed pages. Press <strong>Control</strong> + <strong>Tab</strong> to move from left to right. Press <strong>Shift</strong> + <strong>Control</strong> + <strong>Tab</strong> to move from right to left</p></td>
</tr>
<tr class="even">
<td>To move backwards (right- left) between tabbed pages of a dialog box</td>
<td><strong>Shift</strong> + <strong>Control</strong> + <strong>Tab</strong></td>
</tr>
<tr class="odd">
<td><p>To toggle a check box on or</p>
<p>off</p></td>
<td><strong>Spacebar</strong></td>
</tr>
</tbody>
</table>

> Common Commands

- To open a form from a hyperlink: navigate to the link, and press the space bar.
- To display a record on the bottom pane, use the keyboard to navigate to it, and then press the Enter key. it doesn’t automatically update when you change which record is highlighted.

### Keyboard shortcuts on the buttons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Keyboard shortcut | Action     |
|-----------------------|----------------|
| alt-x                 | to exit        |
| alt-r                 | to show report |
|                       |                |
|                       |                |

> <u>JAWS Configuration Files</u>

> Users can create a JAWS custom configuration file for any application. The configuration file tells JAWS how to behave for certain elements in the application, including elements it may not know how to process. The configuration file will also help JAWS recognize many of the custom screen elements in CPRS Query.

> Screen elements in Windows are commonly called “screen controls” or just “controls.” Several custom controls were developed to make CPRS Query more functional and easier to program. Most of these controls were built on predefined Windows controls (like buttons and drop-down lists.) The instructions in this appendix tell you how to update the JAWS configuration file to tell JAWS to treat these custom controls like the standard Windows controls.

> There are 4 ways to set up the JAWS configuration file for CPRS Query.

1.  The first, and easiest, option is to download a ready-made configuration file from one of the ANONYMOUS FTP directories.
2.  The second is to cut and paste text into an existing configuration file.
3.  The third to create a new file and cut and paste the text into it.
4.  The fourth method, creating the file while running the JAWS application, is in case you have difficulty with the first three.

### Download the Configuration File from the FTP Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Download a file named QUERY.JCF from the ANONYMOUS directory. The preferred method is to FTP the files from:

> download.vista.med.va.gov.

> This transmits the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows:

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 39%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>CIO Field Office</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>FTP Address</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Directory</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Albany</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td><blockquote>
<p>[anonymous.software]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Hines</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td><blockquote>
<p>[anonymous.software]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Salt Lake City</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td><blockquote>
<p>[anonymous.software]</p>
</blockquote></td>
</tr>
</tbody>
</table>

2.  On your workstation, navigate to the appropriate directory. (The standard location for JAWS version 3.7 is C:\JAWS37U\SETTINGS\ENU and for the new JAWS version 4.0, it is C:\JAWS40\SETTINGS\ENU.)
3.  If there is no QUERY.JCF file in the directory, save the file.

### Cut and Paste Information into the Existing Configuration File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Open QUERY.JCF using Notepad. (The standard location for JAWS version

> 3.7 is C:\JAWS37U\SETTINGS\ENU and for the new JAWS version 4.0, it is C:\JAWS40\SETTINGS\ENU.)

2.  Copy and paste the following text at the end of the Notepad document:

> \[WindowClasses\] TORComboEdit=EditCombo TORListBox=ListBox TORAlignButton=Button TORTreeView=TreeView TORAlignEdit=Edit TORListView=ListView TORCheckBox=CheckBox

3.  Save the document.

### Create a New Configuration File Manually

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Start Notepad.
2.  Select the following text and Copy and paste it into the Notepad document:

> \[WindowClasses\] TORComboEdit=EditCombo TORListBox=ListBox TORAlignButton=Button TORTreeView=TreeView TORAlignEdit=Edit TORListView=ListView TORCheckBox=CheckBox

3.  Save the document as “QUERY.JCF” in the appropriate JAWS folder.

> Note: Use the quotes when entering the file name in Notepad; otherwise Notepad will try to save it with a .txt extension.

> (The standard location for JAWS version 3.7 is C:\JAWS37U\SETTINGS\ENU and for the new JAWS version 4.0, it is C:\JAWS40\SETTINGS\ENU.)

### Create the Configuration File while Running JAWS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Start JAWS and CPRS Query.
2.  On the patient selection list box, place the cursor in the edit box where you type the patient name.
3.  Press Insert + F2 to open a dialog called “Run JAWS Manager.”
4.  Cursor down to “Window Class Reassign,” and select the OK button. JAWS then opens the “JAWS Configuration Manager” and a “Window Classes” dialog.
5.  Ensure that in the Window Classes dialog, the New Class edit box reads “TORComboEdit.”
6.  Go to the Assign to: list box, and select EditCombo. Then, select the Add Class button.

> The assignment should show up in the "Assigned Classes" list box.

7.  Repeat the above two steps, each time substituting the values below for the “New Class” and “Assign to” entries:

> TORListBox Assign to: ListBox TORAlignButton Assign to: Button TORTreeView Assign to: TreeView

> TORAlignEdit Assign to: Edit TORListView Assign to: ListView TORCheckBox Assign to: CheckBox

8.  When the entire list is entered, select the OK button.

> JAWS will now use this configuration file when using CPRS Query, and will recognize the custom controls in CPRS Query.