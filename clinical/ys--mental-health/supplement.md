---
title: Veteran's Crisis Line Version 1 Troubleshooting Guide
doc_type: SUP
doc_label: Supplement
doc_layer: anchor
doc_subject: Troubleshooting Guide
app_code: YS
app_name: Mental Health
section: CLI
app_status: active
pkg_ns: YS
patch_ver: 1
patch_id: YS*1
group_key: "YS:YS:1"
file_numbers: []
security_keys: []
menu_options: 0
description: "<table> <colgroup> <col style=\\"width: 5%\\" /> <col style=\\"width: 25%\\" /> <col style=\\"width: 69%\\" /> </colgroup> <thead> <tr class=\\"header\\"> <th></th> <th><blockquote> <p><strong>Problem Description</strong></p> </blockquote></th> <th><blockquote> <p><strong>Resolution</strong></p> </blockquote></th> "
audience: 
keywords: 
  - blockquote
  - strong
  - style
  - width
  - table
  - colgroup
  - thead
  - class
  - tbody
  - reports
page_count: 0
word_count: 710
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/vcl_troubleshooting_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/vcl_troubleshooting_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=78"
---

---
title: Common VCL Problems and their Resolution
---

> Application-side:

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 25%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>Problem Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>1.</strong></p>
</blockquote></td>
<td><blockquote>
<p>User is not able to see the “Custom Reports” link.</p>
</blockquote></td>
<td><blockquote>
<p>Verify that the user has been setup as either “Admin” or “Super Admin” in the application; otherwise they will not be able see the Reports.</p>
<p>Note: Granting users the admin level privilege to a user is a decision handled by the Business Owners, such as Nelson Peck or Dr. Garcia.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Reporting-side:

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 25%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>Problem Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>1.</strong></p>
</blockquote></td>
<td><blockquote>
<p>User is not able to view the Reports page.</p>
</blockquote></td>
<td><blockquote>
<p>The reports home page opens up in a separate tab. Verify whether or not the user is looking at the right tab.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>2.</strong></p>
</blockquote></td>
<td><blockquote>
<p>User is getting the message: “You do not have access to view this page”</p>
</blockquote></td>
<td><blockquote>
<p>The user has not been setup as a member of either VCLREPORTVIEWER or VCLREPORTMANAGER groups.</p>
<p>The business owner will need to follow the AITC 9957 process in order to get the user added to the appropriate group.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>3.</strong></p>
</blockquote></td>
<td><blockquote>
<p>User can view the reports, but is unable to create their own reports.</p>
</blockquote></td>
<td><blockquote>
<p>Only members of the VCLREPORTMANAGER group are authorized to create reports.</p>
<p>The business owner will need to follow the AITC 9957 process in order to get the user added to the appropriate group.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 25%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>3.</strong></p>
</blockquote></th>
<th><blockquote>
<p>While trying to save a report, the user is getting: “Error Access Denied” message.</p>
</blockquote></th>
<th><blockquote>
<p>In example below, User tries to save the report in “Models” folder.</p>
<p>![](veteran-s-crisis-line-version-1-troubleshooting-guide/001.png)</p>
<p>![](veteran-s-crisis-line-version-1-troubleshooting-guide/002.png)</p>
<p>Users can only save reports into the “User Reports” folder. Verify that User is trying to save report into the right folder.</p>
<p>![](veteran-s-crisis-line-version-1-troubleshooting-guide/003.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 25%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>4.</strong></p>
</blockquote></th>
<th><blockquote>
<p>The user account is to be made inactive.</p>
</blockquote></th>
<th><blockquote>
<p>The business needs to initiate the AITC 9957 process in order to get the user removed from VCLREPORTVIEWER / VCLREPORTMANAGER group.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Database-side:

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 25%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>Problem Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Resolution</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>1.</strong></p>
</blockquote></td>
<td><blockquote>
<p>Users typically do not see database related problems, because this is at the “back-end”.</p>
</blockquote></td>
<td><blockquote>
<p>However, in case the application pages are not displaying, or the performance is slow, the DBA may perform checks to verify the health of the database:</p>
<p>Connect to the database using SQL Server Enterprise Manager and verify that it is up and running. Check to see whether there is room in the Tablespaces and in the corresponding File systems.</p>
</blockquote></td>
</tr>
</tbody>
</table>