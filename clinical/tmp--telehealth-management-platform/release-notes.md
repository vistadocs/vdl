---
consolidated_title: "tmp release notes"
app_code: TMP
doc_type: RN
master_source: "TMP Version 2.0 Release 4.8 Release Notes"
master_pub_date: October 2021
consolidated_from: 2 versions
prior_versions:
  - "TMP Version 1.5 Release 4.6 Release Notes"
---

Department of Veterans AffairsTelehealth Management Platform (TMP)  
  
  
4.8.0 Release Notes  

![](tmp-version-2-0-release-4-8-release-notes/001.png)

June 2020Version 1.0

*Prepared for*

VA

*19 October 2021*

*Prepared By*MCS

MICROSOFT MAKES NO WARRANTIES, EXPRESS OR IMPLIED, IN THIS DOCUMENT.

Complying with all applicable copyright laws is the responsibility of the user.  Without limiting the rights under copyright, no part of this document may be reproduced, stored in or introduced into a retrieval system, or transmitted in any form or by any means (electronic, mechanical, photocopying, recording, or otherwise), or for any purpose, without the express written permission of Microsoft Corporation.

Microsoft may have patents, patent applications, trademarks, copyrights, or other intellectual property rights covering subject matter in this document.  Except as expressly provided in any written license agreement from Microsoft, our provision of this document does not give you any license to these patents, trademarks, copyrights, or other intellectual property.

The descriptions of other companies’ products in this document, if any, are provided only as a convenience to you.  Any such references should not consider an endorsement or support by Microsoft.  Microsoft cannot guarantee their accuracy, and the products may change over time. In addition, the descriptions are intended as brief highlights to aid understanding, rather than as thorough coverage. For authoritative descriptions of these products, please consult their respective manufacturers.

© 2016 Microsoft Corporation. All rights reserved. Any use or distribution of these materials without express authorization of Microsoft Corp. is strictly prohibited.

Microsoft and Windows are either registered trademarks or trademarks of Microsoft Corporation in the United States and/or other countries.

The names of actual companies and products mentioned herein may be the trademarks of their respective owners.

Change Record

| Date       | Author   | Version | Change Reference |
|------------|----------|---------|------------------|
| 06/24/2020 | REDACTED | 1.0     | Initial Version  |
|            |          |         |                  |

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
- [Release Detail](#release-detail)
  - [New Enhancements Implemented](#new-enhancements-implemented)
  - [Defects Resolved](#defects-resolved)
  - [Data Migrations/Updates](#data-migrationsupdates)
  - [Considerations/Known Issues](#considerationsknown-issues)
  - [Key Screenshots Updated](#key-screenshots-updated)
    - [Yearly TSA Review](#yearly-tsa-review)
    - [Scheduling Package Management – VVC Case](#scheduling-package-management-vvc-case)
    - [Appointment screen – VVC case/Patient Side Resources](#appointment-screen-vvc-casepatient-side-resources)
    - [Appointment screen – Cancellation Remarks](#appointment-screen-cancellation-remarks)
    - [Appointment screen – RTC/Consults additional date filter:](#appointment-screen-rtcconsults-additional-date-filter)
    - [Patient Technology Types Streamlined](#patient-technology-types-streamlined)
    - [Resource Group Unique ID field increased to 30 character limit](#resource-group-unique-id-field-increased-to-30-character-limit)
    - [Account 90 Day Report](#account-90-day-report)
This document provides the details of the Telehealth Management Platform(TMP) 4.8 Release including user enhancements and defect remediations implemented. The 4.8 Release builds on the TMP functionality by adding the following updates:
<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th>TMP 4.8 Update </th>
<th><strong>Description</strong> </th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>TSA Yearly Review and</strong>  <br />
<strong>Re-Approval</strong> </p>
<p> </p></td>
<td><p>Definition of a process and timeline for reviewing Telehealth Service Agreements (TSAs) to ensure they are reviewed and re-approved yearly for compliance purposes.  Timeline: <br />
![](tmp-version-2-0-release-4-8-release-notes/002.png) <br />
 </p>
<ul>
<li><blockquote>
<p>5093 Initiate Review Process</p>
</blockquote></li>
<li><blockquote>
<p>5090 Initial review notification email </p>
</blockquote></li>
<li><blockquote>
<p>5092 Reviewed and confirmed action  </p>
</blockquote></li>
<li><blockquote>
<p>5094 Reviewed and updated action  </p>
</blockquote></li>
<li><blockquote>
<p>5107,15183 Additional facility approval views for records needing review </p>
</blockquote></li>
<li><blockquote>
<p>5108 Deactivation/Overdue Email Notification </p>
</blockquote></li>
<li><blockquote>
<p>5382 Keep history of all reviewers and approvers </p>
</blockquote></li>
<li><blockquote>
<p>5590 Final warning email notification </p>
</blockquote></li>
</ul>
<p> </p>
<p>This functionality introduces a Review Due Date on TSAs, such that if the review is not done within the time range, the TSA becomes inactivated and the approval status is EXPIRED. The yearly review due dates of existing TSAs are also calculated as part of the deployment.</p></td>
</tr>
<tr class="even">
<td><strong>TMP Scheduling Enhancements</strong> </td>
<td><p>Addition of key enhancements to allow the field to enter cancellation remarks when an appointment is cancelled as well as add patient side resources for VVC type scheduling packages/appointments. <br />
 </p>
<ul>
<li><blockquote>
<p>7080 Appointment Screen – Cancellation Remarks  </p>
</blockquote></li>
<li><blockquote>
<p>7981 Scheduling packaging – VVC case </p>
</blockquote></li>
<li><blockquote>
<p>7079 Appointment screen - Consult/RTC table additional filters </p>
</blockquote></li>
</ul>
<p> </p></td>
</tr>
<tr class="odd">
<td><strong>TMP Efficiencies</strong> </td>
<td><p>Additional updates to streamline the TMP interface experience and validations. </p>
<ul>
<li><blockquote>
<p>7925 Update Participating Site Default Lookup </p>
</blockquote></li>
<li><blockquote>
<p>8313 Update Participating Site Views  </p>
</blockquote></li>
<li><blockquote>
<p>11219 Managing Patient Technology Types </p>
</blockquote></li>
<li><blockquote>
<p>8027 Participating Site Resource Subgrid  </p>
</blockquote></li>
<li><blockquote>
<p>13741,13770 Update Account 90 Day Report </p>
</blockquote></li>
<li><blockquote>
<p>11197 Include Hub name and additional text in Hub related Facility Approvals emails </p>
</blockquote></li>
<li><blockquote>
<p>8020 Resource Group – Increase Unique ID Character Limit </p>
</blockquote></li>
<li><blockquote>
<p>12901 Preventing AlphaNumeric characters in Clinic IEN number when clinics are created </p>
</blockquote></li>
<li><blockquote>
<p>11197 Include Hub name and additional text in Hub related Facility Approvals emails </p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>TMP Defect Remediations</strong> </td>
<td><p>Identified issues were remediated:</p>
<ul>
<li><p>7854 - Technology with no Refresh Date - "Last Equipment Refresh Date" column has data</p></li>
<li><p>8594 - Prod: Business Process Error when updating TMP Resource's TMP Site - INC6311634 (RTC ticket #987319)</p></li>
<li><p>12549 - Production - Appointment - Forward Email messages are not showing under email messages</p></li>
<li><p>12856 - Production - TMP Intermittent Issues Pulling RTCs and Consults</p></li>
<li><p>12901 - Pre-Prod- Preventing AlphaNumeric characters in Clinic IEN number when clinics are created</p></li>
<li><p>13266 - [Internal] Handle error scenarios while canceling an appointment scheduled with TSA (i.e., w/o SP)</p></li>
<li><p>13457 - Prod: Group Appointment: 2nd Patient Site booking into 1st Patients Site’s Vista IEN</p></li>
<li><p>13478 - Prod: INC7581991 - TMP Inventory | Screen doesn't refresh</p></li>
<li><p>14795 - Patient Participating Site - Missing VistA Clinic Message</p></li>
<li><p>15561 - Prod - Real time clinic updates throws an error when information is missing in the VistA inbound message</p></li>
<li><p>15734 - QA: Error on Appt Cancel Dialog for CVT INTER Group appointment when the Reserve Resource is already in Canceled status</p></li>
<li><p>16306 - DEV - Internal - Adding a Non-VA Email on an appointment is not sending the email</p></li>
</ul></td>
</tr>
</tbody>
</table>
For additional detail and history of any of the items, please refer to the Azure DevOps environment that details the discussion/item history. If given access the repository can be found at this [link](https://va-crmprojects.visualstudio.com/TMP), which is:  
<https://va-crmprojects.visualstudio.com/TMP>

# Release Detail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Enhancements Implemented

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the list of all the user stories implemented for new functional enhancements:

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 17%" />
<col style="width: 5%" />
<col style="width: 28%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th>ID</th>
<th>Title</th>
<th>Work Item Type</th>
<th>Description</th>
<th>Acceptance Criteria</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F5090&amp;data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088128971&amp;sdata=SW6ds%2FGFxqPTbin1UAfbClTJR5y%2BAHhe%2BQQhOoqPk1E%3D&amp;reserved=0">5090</a></td>
<td>Initial review notification email</td>
<td>User Story</td>
<td>As a member of the TSA Initial Approval Team (FTCs for non-hub, Hub Director for Hub), I need to be notified that a previously approved interfacility Facility Approval(TSA) needs to be reviewed by a specific 'review due date', so that I can review and confirm the existing Facility Approval or make updates that trigger required approvals all over again.</td>
<td><ul>
<li><p>notification email is sent to both Provider and Patient side Initial Approval team with the below wording - At 60 days prior to the review due date<br />
if hub: [Initial Approval Team Text] = Hub Director<br />
if non hub: [Initial Approval Team Text]= Provider and Patient FTCs</p></li>
<li><p>clicking on the link included in the email takes user to the appropriate Facility approval record</p></li>
</ul>
<blockquote>
<p>Subject: [Provider Facility Name] and [Patient Facility Name] agreement needs yearly review</p>
<p>[Provider Facility Name] and [Patient Facility Name] agreement needs review by [Initial Approval Team Text], [Specialty, Specialty Sub-Type] telehealth service.</p>
<p>To review, please click here [link to Facility Approval record].  <strong>This review is due by [review due date] or the associated record will be inactivated.</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><a href="https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F5092&amp;data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088138968&amp;sdata=yROX7gGTGjxyCW5l6iIX%2FsMcLpPhvnrqEZb7Sk6%2Bg9c%3D&amp;reserved=0">5092</a></td>
<td>Reviewed and confirmed action</td>
<td>User Story</td>
<td>As a member of the TSA Initial Approval Team (FTCs for non-hub, Hub Director for Hub), I need to mark an interfacility Facility Approval(TSA) as 'Reviewed and Confirmed', so that the interfacility Facility Approval(TSA) complies with yearly review policy.  This should be for both Provider Side and Patient side FTC Teams for non hub approval process, Hub Director team for hub approval process.<br />
<br />
Next Review Due Date will be 1 yr+30 days from this action date.</td>
<td><ul>
<li><p>FTC Approval team member can mark a Facility Approval(TSA) as 'Reviewed and Confirmed' where system keeps the signee and date associated with this review action</p></li>
<li><p>Audit history shows this review action</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><a href="https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F5093&amp;data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088138968&amp;sdata=sR1kFdpIiF5HCsQdd0Xi1C30TTur68u1izqMvxr6%2FQs%3D&amp;reserved=0">5093</a></td>
<td>Initiate review process</td>
<td>User Story</td>
<td>As a member of the TSA Initial Approval Team (FTCs for non-hub, Hub Director for Hub), I need the system to initiate a review process so that I have a window of time to review previously approved interfacility TSAs according to the yearly review policy. The 'review due date' is calculated as the 1 year anniversary of final approval date +30 calendar days (from Date when Facility Approval Status=Approved).</td>
<td><ul>
<li><p>review due date is visible and calculated correctly as the 1 year anniversary of final approval date +30 calendar days (11:59pm/10:59pm EST depending on daylight savings adjustment )</p></li>
<li><p>Review due date is read only (on the TSA approval screen, signature page), visible in the page Header to the left of Approval status.</p></li>
<li><p>60 calendar days prior to the review due date, the review process begins and the initial Approval Team Statuses are updated:<br />
non hub: FTC Approval Status on Patient and Provider side = Review Pending<br />
hub: Hub Director Approval Status = Review Pending</p></li>
<li><p>Approval Status can only go forward to 'Reviewed and Confirmed' or 'Reviewed and Updated' =&gt; cannot go back to Approve (Approve is no longer an option).  Additionally prior to the review process Reviewed and Update do not appear</p></li>
</ul></td>
</tr>
<tr class="even">
<td><a href="https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F5094&amp;data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088148964&amp;sdata=VygC9em79%2F52JOkVuxdy28Wibq9qJwytN3P%2FcxAW1kY%3D&amp;reserved=0">5094</a></td>
<td>Reviewed and updated action</td>
<td>User Story</td>
<td>As a member of the TSA Initial Approval Team (FTCs for non-hub, Hub Director for Hub), I need to mark an interfacility Facility Approval(TSA) as 'Reviewed and Confirmed', so that an interfacility Facility Approval(TSA) is re-verified on a periodic basis.  This should be for both Provider Side and Patient side FTC Teams for non hub approval process and Hub Director for hub approval process.</td>
<td><ul>
<li><p>TSA Initial Approval Team member (FTCs for non-hub, Hub Director for Hub) can set the Approval Status as 'Reviewed and Updated' where system keeps the signee and date associated with this review action</p></li>
<li><p>Audit history shows this review action​ and any previous signatures</p></li>
<li><p>New approval notifications sent to Service Chief and Chiefs of Staff as required based on Hub vs. non Hub approval process</p></li>
<li><p>non-hub: Both FTC Initial Approval Teams must take action before any Service Chief and Chief of Staffs are notified</p></li>
</ul>
<blockquote>
<p>(Emails will not be sent out until both FTC teams have changed their Approval Statuses”). If either FTC changes their status to Reviewed and updated then both patient and provider side Service Chiefs and Chiefs of Staff will be notified.</p>
</blockquote>
<ul>
<li><p>Service Chief and Chiefs of Staff Approval Status's reset to blank awaiting their new approvals (also the signee and signee date fields also go to blank)</p></li>
<li><p>User is prompted with a popup prompt to continue or cancel this status update: <br />
Title: Warning<br />
Text: This TSA has been Reviewed and Updated.  Clicking okay will clear all signatures and dates. Are you sure you want to proceed?</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><a href="https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F5107&amp;data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088148964&amp;sdata=NNePDJFzlrGRjGBPlBR0vbVGMx5Ol68xiftW5KHByEg%3D&amp;reserved=0">5107</a></td>
<td>Additional facility approval views for records needing review</td>
<td>User Story</td>
<td><p>As a TSA Manager, I need the ability to view all Facility Approvals(TSAs) reviewed so that I can see any outstanding or completed reviews as follows:</p>
<p>- show what is due to be reviewed this quarter =&gt; Pending Review</p>
<p>- show what is overdue for review (e.g. based on review due date is past)</p>
<p>- show what was reviewed this quarter as ‘Reviewed and Confirmed’ ​</p>
<p>- show what was reviewed this quarter as ‘Reviewed and Updated’ ​</p>
<p>- user can select the date in a filter option if built as a view</p>
<p>These 8 additional views are required for Facility Approvals within selected time period</p>
<p>non hub:</p>
<p><strong>TSAs Pending Review This Quarter</strong> - any record where FTCs Status is Review Pending</p>
<p><strong>TSAs Overdue for Review This Quarter</strong> - any record where FTCs Status is Review Pending AND</p>
<p> current date &gt; review due date</p>
<p><strong>TSAs Reviewed and Confirmed This Quarter</strong> - any record where (Provider FTC Approval Status=Reviewed and Confirmed) OR Patient (FTC Approval Status=Reviewed and Confirmed)</p>
<p><strong>TSAs Reviewed and Updated This Quarter</strong> - any record where (Provider FTC Approval Status=Reviewed and Updated) OR Patient (FTC Approval Status=Reviewed and Updated)</p>
<p>Hub:</p>
<p><strong>Hub TSAs Pending Review This Quarter</strong> - any record where Hub Director Status is Review Pending</p>
<p><strong>Hub TSAs Overdue for Review This Quarter</strong> - any record where Hub Director Status is Review Pending AND</p>
<p> current date &gt; review due date</p>
<p><strong>Hub TSAs Reviewed and Confirmed This Quarter</strong> - any record where Hub Director Approval Status=Reviewed and Confirmed)</p>
<p><strong>Hub TSAs Reviewed and Updated This Quarter</strong> - any record where Hub Director Approval Status=Reviewed and Updated)</p></td>
<td><p>User has additional view options that lists records with the matching criteria with columns as follows:</p>
<p>For non Hub:</p>
<p>Name</p>
<p>Provider Facility</p>
<p>Patient Facility</p>
<p>Scheduling Package Name</p>
<p>Created On</p>
<p>Created By</p>
<p>Last Modified On</p>
<p>Modified By</p>
<p>Review Due Date</p>
<p>Patient FTC Approval Status</p>
<p>Patient FTC Date Signed</p>
<p>Provider FTC Approval Status</p>
<p>Provider FTC Date Signed</p>
<p>Status Reason</p>
<p>For Hub:</p>
<p>Name</p>
<p>Provider Facility</p>
<p>Patient Facility</p>
<p>Scheduling Package Name</p>
<p>Scheduling Package.Hub</p>
<p>Created On</p>
<p>Created By</p>
<p>Last Modified On</p>
<p>Modified By</p>
<p>Review Due Date</p>
<p>Hub Director Approval Status</p>
<p>Hub Director Date Signed</p>
<p>Status Reason</p></td>
</tr>
<tr class="even">
<td><a href="https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F5108&amp;data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088148964&amp;sdata=XUUQRzUMsIm%2B3H5hgbHKhsfBqhx8gkf7ERAOQwJ%2F8II%3D&amp;reserved=0">5108</a></td>
<td>Deactivation/Overdue Email Notification</td>
<td>User Story</td>
<td>As a member of the TSA Initial Approval Team (FTCs for non-hub, Hub Director for Hub), I need to be notified that a previously approved interfacility TSA is still waiting to be reviewed by a specific 'review due date' when the review date is past</td>
<td><ul>
<li><p>current date is the day after the review due date + 1 day</p></li>
<li><p>non hub: notification email is sent to either or both Provider and Patient side FTC Approval team with the below wording - depending who is still outstanding (FTC Approval Status=Pending Review)<br />
Initial Approver Text = Provider and/or Patient FTCs<br />
hub: notification email is sent to Hub Director, Initial Approver Text = Hub Director</p></li>
<li><p>clicking on the link included in the email takes user to the appropriate Facility approval record</p></li>
</ul>
<blockquote>
<p>Subject: [Provider Facility Name] and [Patient Facility Name] agreement’s yearly review is overdue and service is deactivated &lt;=Subject ends here.   </p>
<p>[Provider Facility Name] and [Patient Facility Name] It has been more than a year since this Telehealth service agreement has been reviewed and signed by [Initial Approver Text], [Specialty, Specialty Sub-Type] Telehealth service.<br />
To review, please click here [link to TSA].  <strong>This review was due by [review due date] and the associated TSA is no longer active.</strong></p>
</blockquote>
<ul>
<li><p>Facility Approval record is de-activated and the overall status = EXPIRED</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><a href="https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F5382&amp;data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088158960&amp;sdata=z0c7kmW1YWllY0rSBXiFn3FDFC438sew4N6LiFKM%2Blw%3D&amp;reserved=0">5382</a></td>
<td>Keep history of all reviewers and approvers</td>
<td>User Story</td>
<td>As a TSA Manager, I need the system to keep a history of all previous approvals and reviews for a Facility Approval(TSA), so that any audit would show the entire history of approvals and reviews including dates and signee information.</td>
<td>system shows all history of approvals and reviews, including date and signee information of when the action occurred</td>
</tr>
<tr class="even">
<td><a href="https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F5590&amp;data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088158960&amp;sdata=Ze%2Frqa07QRT4GhxaAmaNa9vqDhRHhj%2B1x16VGKZhwXE%3D&amp;reserved=0">5590</a></td>
<td>Final Warning Email Notification</td>
<td>User Story</td>
<td>As a member of the TSA Initial Approval Team (FTCs for non-hub, Hub Director for Hub), I need to get a final reminder that the Facility Approval(TSA) will be deactivated 7 calendar days before the deactivation date (review due date), so that I get a final warning to do the overdue review.</td>
<td><p>    non hub: Initial Approver Text= Provider and Patient FTCs<br />
     hub: Initial Approver Text = Hub Director </p>
<p>Subject: [Provider Facility Name] and [Patient Facility Name] agreement needs yearly review ASAP</p>
<p>[Provider Facility Name] and [Patient Facility Name] agreement needs review by [Initial Approver Text], [Specialty, Specialty Sub-Type] telehealth service.</p>
<p>To review, please click here [link to Facility Approval].  <strong>This review was due by [review due date] and the associated TSA will be inactivated 7 days from this message.</strong></p></td>
</tr>
<tr class="odd">
<td><a href="https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F7079&amp;data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088168951&amp;sdata=BhyL8wZMuoR%2FnN3WkuusGRN422myxZucr5TMWWLoEi0%3D&amp;reserved=0">7079</a></td>
<td>Appointment screen - Consult/RTC table additional filters</td>
<td>User Story</td>
<td>As a TMP Scheduler, I need the RTC and Consult display to allow me to filter on a date range, so that I don't have to scroll through all the RTC/Consults in one single table (given the 2 year+future VistA criteria).</td>
<td><p>-user can filter by RTCs/Consults from 30 days past through the future</p>
<p>-user can filter by RTCs/Consults from 90 days past through the future<br />
<br />
-user can filter by all RTCs/Consults in the past through the future<br />
<br />
-date filter is on RTC/Consult Created Date</p></td>
</tr>
<tr class="even">
<td><a href="https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F7080&amp;data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088168951&amp;sdata=UH24WUFQ7467UcBCPR5nOmIygNxaekq8%2FXLFLUvyHNo%3D&amp;reserved=0">7080</a></td>
<td>Appointment screen - cancellation remarks</td>
<td>User Story</td>
<td>As a TMP Scheduler, I need to optionally enter cancel remarks/comments so that these comments can flow to VistA for documentation  (into the cancel remarks field)</td>
<td>The following updates to the Appointment form:<br />
- Cancel Comments entered on TMP are passed through to VistA when an appointment is cancelled<br />
<br />
- Cancel comments text field added with a max size of 160 is optional and not required<br />
<br />
-Cancel comments field is shown on Appointment Information section below scheduling package name (only when the whole appointment has been canceled and is read only). Field title is Cancellation Remarks.<br />
<br />
-Existing 'Scheduling Comments' field is moved to above the Scheduling Package Name on the form<br />
<br />
-for a group appointment, the 'reserve resource' cancellation comments field will be visible on the Reserve Resource if (and only if) it is canceled.  NOT on the parent appointment.</td>
</tr>
<tr class="odd">
<td><a href="https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F7925&amp;data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088178942&amp;sdata=OMuQEguEpxuk1hOC%2FhWgOyRKMenF%2BJbkB8GtuODJ4ok%3D&amp;reserved=0">7925</a></td>
<td>Update Participating Site Default Lookup</td>
<td>User Story</td>
<td><p>As a TMP Scheduling Package Manager, adding a Participating Site to an intrafacility or interfacility Scheduling Package(SP), I need to efficiently view the TMP Sites that are selectable, so that I don’t have to scroll through all TMP sites.</p>
<p>On the Participating Site form, the user must specify whether it is a Patient or Provider site, prior to selecting the TMP Site.</p>
<ul>
<li><p><strong>Location Type</strong> must be placed above <strong>TMP Site</strong></p></li>
<li><p><strong>TMP Site</strong> must be disabled until the <strong>Location Type</strong> is selected, as that will help knowing whether the user selected Patient Site or Provider Site and the filtering/non-filtering of <strong>TMP Site</strong> can be appropriately controlled<strong>.</strong></p></li>
</ul>
<p>Filtering Rules =&gt; See Devops</p></td>
<td>The TMP Sites listed in the default lookup are specific to the selected SP Facility (Provider Facility and Patient Facility)</td>
</tr>
<tr class="even">
<td><a href="https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F7981&amp;data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088178942&amp;sdata=9G8X8sJmadXcgxaDENsX35NEv3AhjQx2mu%2B9oyrQe6o%3D&amp;reserved=0">7981</a></td>
<td>Add Participating Sites and Scheduling Resources to VVC Scheduling Package</td>
<td>User Story</td>
<td>As a TMP Scheduling Package Manager, I need to add sites and scheduling resources to patient side VVC appointments, so that I can add the appropriate administrative VistA Clinic or other scheduling resources</td>
<td>-User has ability to add participating sites and scheduled resources to VVC patient location types on a scheduling package (both Intrafacility and Interfacility).<br />
<br />
-Same business rules apply when participating sites are added<br />
<br />
-only 1 or zero VistA Clinic scheduling resources allowed. That is:<br />
- Interfacility VVC is required to have 1 Vista Clinic on the patient participating site, when a participating site is added<br />
<br />
-Intrafacility VVC must have a provider participating site, and may have a patient participating site but a patient participating site is not required. <br />
<br />
-if scheduling resources are added and Can Be Scheduled=Yes, they get scheduled as part of the appointment creation for SPs with Scheduling Usage type of Scheduling.<br />
<br />
-In order for an Intrafacility VVC Patient Participating Site ‘CanBe Scheduled’ field to be set to ‘Yes’, the Patient Participating Site must have a scheduling resource (when a patient participating site is added).<br />
<br />
-If scheduling resources are added and its a TSA usage type, facility approvals would get initiated as required as well.<br />
<br />
-User has option to have zero participating sites on the patient side also (as is today for intrafacility only).<br />
<br />
-Assumption is that TCT Staff team exists even for non-VA site would exist with members (e.g. admin person would get the scheduling emails)<br />
<br />
-When creating a VVC appointment, user can select a checkbox indicating if Patient Site Resources Required?</td>
</tr>
<tr class="odd">
<td><a href="https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F8020&amp;data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088188938&amp;sdata=Nqat6IJVo4XjbOgvp93gmjYOcdIvg9p44gm0yfuMi9Q%3D&amp;reserved=0">8020</a></td>
<td>Resource Group – Increase Unique ID Character Limit</td>
<td>User Story</td>
<td>Asa TMP Resource Manager editing a TMP Resource Group, I need to have a bigger text size for the unique identifier, so that up to 30 characters can be entered</td>
<td>User can enter up to 30 characters in the Unique ID field</td>
</tr>
<tr class="even">
<td><a href="https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F8027&amp;data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088188938&amp;sdata=wBJGUN1SmYAl9tN9XYPdtAIZDtAEFTIFVqxjelhTzR4%3D&amp;reserved=0">8027</a></td>
<td>Participating site resource subgrid</td>
<td>User Story</td>
<td>As an SP Manager, I need to list out TMP resources under a participating site's associated Paired Resource Group (PRG) so that I don't have to click into each PRG to see what resources are inside of it.</td>
<td>Resources subgrid includes Resources column with concatenation of all included resources when item is a PRG. A redundant TMP Resource Group column is removed since Name is already listed.</td>
</tr>
<tr class="odd">
<td><a href="https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F8313&amp;data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088198937&amp;sdata=mLNtFVvZ9SvvhdKZqAE7kK22FBqsUts99kFjzesovt0%3D&amp;reserved=0">8313</a></td>
<td>Update participating site views</td>
<td>User Story</td>
<td>As a SP Manager, I need to see the vista clinics associated with a participating site (PS) and audit dates, so that I don't have to click into each record individually</td>
<td><p>Following updates on the PS views are visible:</p>
<p>For views:</p>
<p>All Patient Participating Sites</p>
<p>My Site's Patient Participating Sites</p>
<p>Patient Participating Sites @ my Facility</p>
<p>All Provider Participating Sites</p>
<p>My Site's Provider Participating Sites</p>
<p>Provider Participating Sites @ my Facility</p>
<p>Non-Schedulable Participating Sites @ my Facility</p>
<p>Schedulable Participating Sites @ my Facility</p>
<p>- Increase TMP Sites to 300 px</p>
<p>- Scheduling Package to 300 px,</p>
<p>- Remove Name column (Not Needed) or reposition to be column 3,</p>
<p>- Added Columns - Modified By and Modified On,</p>
<p>- Added Columns - Created By, and Created On</p>
<p>==</p>
<p>The following changes specifically to the following views:</p>
<p>All Patient Participating Sites</p>
<p>My Site's Patient Participating Sites</p>
<p>Patient Participating Sites @ my Facility</p>
<p>- Added Column - Patient Side Vista Clinics</p>
<p>==</p>
<p>All Provider Participating Sites</p>
<p>My Site's Provider Participating Sites</p>
<p>Provider Participating Sites @ my Facility</p>
<p>- Added Column - Provider Side Vista Clinics,</p>
<p>==</p>
<p>Non-Schedulable Participating Sites @ my Facility</p>
<p>Schedulable Participating Sites @ my Facility</p>
<p>- Added Column - Provider Side Vista Clinics,</p>
<p>- Added Column - Patient Side Vista Clinics</p></td>
</tr>
<tr class="even">
<td><a href="https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F11197&amp;data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088198937&amp;sdata=5AWfbRGjQQETB7c%2BoVEyqFh1EQR0vil6t2%2BNxczreHg%3D&amp;reserved=0">11197</a></td>
<td>Include Hub name and additional text in Hub related Facility Approvals emails</td>
<td>User Story</td>
<td>As a TSA Approver, I need to understand information for Hub related approvals so that I know which Hub and Provider Facilities are requiring my approval</td>
<td>The 2 Hub related Facility Approval email templates have the attached text (highlighted text describes the field values inserted/substituted).</td>
</tr>
</tbody>
</table>

| ID  | Title | Work Item Type | Description | Acceptance Criteria |
|-----|-------|----------------|-------------|---------------------|

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 13%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F11219&amp;data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088208924&amp;sdata=%2B2BM9J8sKIRlZNkqmStHpeuQcBUz2RF5n1hj46kEakg%3D&amp;reserved=0">11219</a></th>
<th>Managing Patient Technology Types</th>
<th>User Story</th>
<th>As TMP Resource Manager I need to update available technology types for a Patient so that obsolete names are removed and device names are streamlined for clarity in the field</th>
<th><p>Patient Form is updated for Technology Type:</p>
<p>Please change CVT Tablet and COTS Tablet value to one value, “SIP Device”.</p>
<p>Please leave SIP Address field. Make all fields visible for the Technology type, but gray out and lock the ones that are not pertinent to the Technology Type in question.</p>
<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><strong><u>Fields Accessible</u></strong></th>
<th colspan="5"><strong><u>Technology Type</u></strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><u>Fields</u></strong></td>
<td><strong><u>CVT Tablet <br />
(Sip Device)</u></strong></td>
<td><strong><u>COTS Tablet<br />
(Sip Device)</u></strong></td>
<td><u>VA Issued Device</u></td>
<td><strong><u>VA Issued Device</u></strong></td>
<td><strong><u>Personal Device</u></strong></td>
</tr>
<tr class="even">
<td><strong>Tablet SIP Address</strong></td>
<td>Available</td>
<td>Available</td>
<td>Read-only</td>
<td>Read-only</td>
<td>Read-only</td>
</tr>
<tr class="odd">
<td><strong>Do Not Allow Emails</strong></td>
<td>Read-only</td>
<td>Read-only</td>
<td><strong>If Allow</strong></td>
<td><strong>If Do Not Allow</strong></td>
<td>Automatically set it to "Allow" and disable the fiel<strong>d</strong></td>
</tr>
<tr class="even">
<td><strong>Email</strong></td>
<td>Read-only</td>
<td>Read-only</td>
<td>Available</td>
<td>Read-only</td>
<td>Available</td>
</tr>
</tbody>
</table>
<p>  Static VMR Link</p>
<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 18%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>Read-only</th>
<th>Read-only</th>
<th>Read-only</th>
<th>Available</th>
<th>Read-only</th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<p>                       </p>
<p>- VA Issued iOS Device replaced with VA Issued Device</p>
<p>- Static VMR Link, Do Not Allow Emails, would continue to be associated with VA Issued Device (i.e. renamed from VA Issued IOS Device) </p>
<p>- Personal VA Video Connect Device replaced with Personal Device</p>
<p>For Personal VA Video Connect Device – the field that are accessible are based off of the Do Not Allow<br />
- Email address would still be associated with Personal Device (i.e. renamed from Personal VA Video Connect Device). Email Address field needs to be present and accessible to this Technology Type.</p>
<p>Ensure that after the merge of the options sets to SIP Address,<br />
the following table logic holds true:</p>
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong><u>Emails Sent</u></strong></th>
<th colspan="5"><strong><u>Technology Type</u></strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><u>Emails</u></strong></td>
<td><strong><u>CVT Tablet (Sip Device)</u></strong></td>
<td><strong><u>COTS Tablet<br />
(Sip Device)</u></strong></td>
<td><p><strong><u>VA Issued Device</u></strong></p>
<p><strong><u>(Allow)</u></strong></p></td>
<td><p><strong><u>VA Issue Device</u></strong></p>
<p><strong><u>(Do Not Allow)</u></strong></p></td>
<td><strong><u>Personal Device</u></strong></td>
</tr>
<tr class="even">
<td><p><strong>Provider Site</strong></p>
<p><strong>Provider &amp; TCT/Staff</strong></p></td>
<td>YES</td>
<td>YES</td>
<td>YES</td>
<td>YES</td>
<td>YES</td>
</tr>
<tr class="odd">
<td><p><strong>Patient Email</strong></p>
<p><strong> </strong></p></td>
<td>NO EMAIL SENT</td>
<td>NO EMAIL SENT</td>
<td><strong>YES</strong></td>
<td>NO EMAIL SENT</td>
<td><strong>YES</strong></td>
</tr>
<tr class="even">
<td><p><strong>Scheduler Action</strong></p>
<p><strong> </strong></p></td>
<td>YES</td>
<td>YES</td>
<td>YES</td>
<td>YES</td>
<td>YES</td>
</tr>
</tbody>
</table></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| ID  | Title | Work Item Type | Description | Acceptance Criteria |
|-----|-------|----------------|-------------|---------------------|

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 11%" />
<col style="width: 7%" />
<col style="width: 26%" />
<col style="width: 46%" />
</colgroup>
<tbody>
<tr class="odd">
<td><a href="https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F13741&amp;data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088208924&amp;sdata=1edCMIbfuvHmhi3YzGyFB9R492fH5NzQOQHUZjf6p8I%3D&amp;reserved=0">13741</a></td>
<td>Update Account 90 Day report</td>
<td>User Story</td>
<td>As a TMP Administrator, I need the Account 90 Day Report updated so that the output can show user's that have logged in in the past 90 days also and are not de-activated.</td>
<td>Report has additional filter: Active<br />
-If Active selected then the date being filtered is LoginDate<br />
<br />
-if Disabled selected then the date being filtered is the Disabled Date<br />
<br />
-if All is selected all users are listed -report accurately shows User Type value<br />
<br />
-Start/End Date filter defaults to 90 Day date range</td>
</tr>
<tr class="even">
<td><a href="https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F14031&amp;data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088208924&amp;sdata=AsHW3yqnPTXcpAGUJLwC7sthyHc0D2Fv6rUGTXBTnEw%3D&amp;reserved=0">14031</a></td>
<td>Avoid Linking Inappropriate VistA clinic to a Scheduling Resource</td>
<td>User Story</td>
<td>As a Scheduling Package Manager, adding VistA clinic type scheduling resources to an SP, I  shouldn't be allowed to select views that explicitly point to invalid clinics, so that I chose valid clinics for scheduling</td>
<td><p>The following views no longer appear as selections under the Resource Lookup</p>
<p>Patient clinics without IEN (Group Resources)</p>
<p>Patient clinics without IEN (TSA)</p>
<p>Provider clinics without IEN (Group Resources)</p>
<p>Provider clinics without IEN (TSA)</p>
<p>Scheduled Vista Clinics Missing IENs Update<br />
<br />
'Type - Vista Clinic' view to omit clinics without an IEN</p></td>
</tr>
<tr class="odd">
<td><a href="https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F14064&amp;data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088218922&amp;sdata=Wk%2BhWXbhcjp89F3YhpVvy2kyEMCFX6ax7Zzw8tdbKIs%3D&amp;reserved=0">14064</a></td>
<td>Scheduling package validation when adding patient side resources</td>
<td>User Story</td>
<td>As an SchedulingPackage Manager, adding patient side scheduling resources, I should include a VistA clinic for clinic based type appointments, so that I avoid scheduling errors</td>
<td>-When a user doesn’t add a patient side vista clinic type resource for clinic based type appointments and tries to change the Can Be Scheduled to Yes, they get a validation error</td>
</tr>
<tr class="even">
<td><a href="https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F15183&amp;data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088218922&amp;sdata=Pil9wymhxmPh2ukfR1L4lqydJzYQrMwp0UGu9EEgGgI%3D&amp;reserved=0">15183</a></td>
<td>Update TSA review related views</td>
<td>User Story</td>
<td>As a TSA Approver, I need the TSA review related views updated so that I have better readability and additional columns visible</td>
<td><p>-The following views are updated with below column order and column widths:</p>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>TSAs Overdue for Review This Quarter - Hub</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TSAs Overdue for Review This Quarter - Non-Hub</td>
</tr>
<tr class="even">
<td>TSAs Pending Review This Quarter - Hub</td>
</tr>
<tr class="odd">
<td>TSAs Pending Review This Quarter - Non-Hub</td>
</tr>
<tr class="even">
<td>TSAs Reviewed and Confirmed This Quarter - Hub</td>
</tr>
<tr class="odd">
<td>TSAs Reviewed and Confirmed This Quarter - Non-Hub</td>
</tr>
<tr class="even">
<td>TSAs Reviewed and Updated This Quarter - Hub</td>
</tr>
<tr class="odd">
<td><p>TSAs Reviewed and Updated This Quarter - Non-Hub</p>
<p>-Hub views no longer use the Scheduling Package.Hub column and instead include the TSA.Hub Facility column</p>
<p>-the listed records sort alphabetically on the first column  (i.e. Name is the default sort, A-Z)</p>
<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 57%" />
<col style="width: 22%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>For Hub TSA Views</strong></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><u>Order</u></strong></td>
<td><strong><u>Column Name</u></strong></td>
<td><strong><u>Column Width</u></strong></td>
<td> </td>
</tr>
<tr class="even">
<td>1</td>
<td><strong>Name</strong></td>
<td>300</td>
<td>px</td>
</tr>
<tr class="odd">
<td>2</td>
<td><strong>Hub Facility</strong></td>
<td>200</td>
<td>px</td>
</tr>
<tr class="even">
<td>3</td>
<td><strong>Scheduling Package</strong></td>
<td><strong>300</strong></td>
<td>px</td>
</tr>
<tr class="odd">
<td>4</td>
<td><strong>Review Due Date</strong></td>
<td>150</td>
<td>px</td>
</tr>
<tr class="even">
<td>5</td>
<td><strong>Approval Status Hub Director</strong></td>
<td><strong>200</strong></td>
<td>px</td>
</tr>
<tr class="odd">
<td>6</td>
<td><strong>Date Signed Hub Director</strong></td>
<td>150</td>
<td>px</td>
</tr>
<tr class="even">
<td>7</td>
<td><strong>Status Reason</strong></td>
<td>150</td>
<td>px</td>
</tr>
<tr class="odd">
<td>8</td>
<td><strong>Provider Facility</strong></td>
<td>200</td>
<td>px</td>
</tr>
<tr class="even">
<td>9</td>
<td><strong>Patient Facility</strong></td>
<td>200</td>
<td>px</td>
</tr>
<tr class="odd">
<td>10</td>
<td><strong>Modified By</strong></td>
<td>150</td>
<td>px</td>
</tr>
<tr class="even">
<td>11</td>
<td><strong>Modified On</strong></td>
<td>150</td>
<td>px</td>
</tr>
<tr class="odd">
<td>12</td>
<td><strong>Created By</strong></td>
<td>150</td>
<td>px</td>
</tr>
<tr class="even">
<td>13</td>
<td><strong>Created On</strong></td>
<td>150</td>
<td>px</td>
</tr>
<tr class="odd">
<td> </td>
<td> </td>
<td>2300</td>
<td>px</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><strong>For Non-Hub TSA Views:</strong></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong><u>Order</u></strong></td>
<td><strong><u>Column Name</u></strong></td>
<td><strong><u>Column Width</u></strong></td>
<td> </td>
</tr>
<tr class="odd">
<td>1</td>
<td><strong>Name</strong></td>
<td>300</td>
<td>px</td>
</tr>
<tr class="even">
<td>2</td>
<td><strong>Scheduling Package</strong></td>
<td>300</td>
<td>px</td>
</tr>
<tr class="odd">
<td>3</td>
<td><strong>Review Due Date</strong></td>
<td>150</td>
<td>px</td>
</tr>
<tr class="even">
<td>4</td>
<td><strong>Approval Status (Provider FTC)</strong></td>
<td>200</td>
<td>px</td>
</tr>
<tr class="odd">
<td>5</td>
<td><strong>Date Signed (Provider FTC)</strong></td>
<td>150</td>
<td>px</td>
</tr>
<tr class="even">
<td>6</td>
<td><strong>Approval Status (Patient FTC)</strong></td>
<td>200</td>
<td>px</td>
</tr>
<tr class="odd">
<td>7</td>
<td><strong>Date Signed (Patient FTC)</strong></td>
<td>150</td>
<td>px</td>
</tr>
<tr class="even">
<td>8</td>
<td><strong>Status Reason</strong></td>
<td>150</td>
<td>px</td>
</tr>
<tr class="odd">
<td>9</td>
<td><strong>Provider Facility</strong></td>
<td>200</td>
<td>px</td>
</tr>
<tr class="even">
<td>10</td>
<td><strong>Patient Facility</strong></td>
<td>200</td>
<td>px</td>
</tr>
<tr class="odd">
<td>11</td>
<td><strong>Modified By</strong></td>
<td>150</td>
<td>px</td>
</tr>
<tr class="even">
<td>12</td>
<td><strong>Modified On</strong></td>
<td>150</td>
<td>px</td>
</tr>
<tr class="odd">
<td>13</td>
<td><strong>Created By</strong></td>
<td>150</td>
<td>px</td>
</tr>
<tr class="even">
<td>14</td>
<td><strong>Created On</strong></td>
<td>150</td>
<td>px</td>
</tr>
<tr class="odd">
<td> </td>
<td> </td>
<td>2600</td>
<td>px</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

## Defects Resolved

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the defects that have been resolved in this release:

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 26%" />
<col style="width: 9%" />
<col style="width: 27%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>ID</th>
<th>Title</th>
<th>Work Item Type</th>
<th>Description</th>
<th>Acceptance Criteria</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="https://va-crmprojects.visualstudio.com/813c42f7-7b2c-4815-ba8f-afd87e914f66/_workitems/edit/7854">7854</a></td>
<td>Technology with no Refresh Date - "Last Equipment Refresh Date" column has data</td>
<td>Bug</td>
<td>As a TMP Resource Manager, I need to see the technologies with no refresh date in a view so that I know which items need to be modified.</td>
<td>View displays with: Filters: VISN, Facility, Site, System Type, Last Equipment Refresh Date DOES NOT contain data Rows: TMP Resource where Type=Technology​ AND Last Equipment Refresh Date DOES NOT contain data Columns: Name, System Type, Cart Type, Master Serial Number, Room/CEVN, Last Equipment Refresh Date, POC, TMP Site, Facility, VISN​</td>
</tr>
<tr class="even">
<td><a href="https://va-crmprojects.visualstudio.com/813c42f7-7b2c-4815-ba8f-afd87e914f66/_workitems/edit/8594">8594</a></td>
<td>Prod: Business Process Error when updating TMP Resource's TMP Site - INC6311634 (RTC ticket #987319)</td>
<td>Bug</td>
<td>TMP Resource Manager is unable to change the TMP Site associated with the Resource and gets a Business Process Error</td>
<td>-TMP Resource Manager can change the TMP Site of a TMP Resource to another TMP Site within the same facility</td>
</tr>
<tr class="odd">
<td><a href="https://va-crmprojects.visualstudio.com/813c42f7-7b2c-4815-ba8f-afd87e914f66/_workitems/edit/12549">12549</a></td>
<td>Production - Appointment - Forward Email messages are not showing under email messages</td>
<td>Bug</td>
<td>As a TMP scheduler, I need to be able to forward a scheduling email so that it can be resent or forwarded in cases where a recipient may have lost track of the original email</td>
<td>-emails on an appointment can be forwarded (user enters email addresses)</td>
</tr>
<tr class="even">
<td><a href="https://va-crmprojects.visualstudio.com/813c42f7-7b2c-4815-ba8f-afd87e914f66/_workitems/edit/12856">12856</a></td>
<td>Production - TMP Intermittent Issues Pulling RTCs and Consults</td>
<td>Bug</td>
<td>As a TMP Scheduler scheduling an appointment, I am able to view the patient's RTCs/Consult orders so that one selected can be linked to the appointment and passed through to VistA</td>
<td>RTCs and Consults consistently are displayed when available</td>
</tr>
<tr class="odd">
<td><a href="https://va-crmprojects.visualstudio.com/813c42f7-7b2c-4815-ba8f-afd87e914f66/_workitems/edit/12901">12901</a></td>
<td>Pre-Prod- Preventing AlphaNumeric characters in Clinic IEN number when clinics are created</td>
<td>Bug</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="https://va-crmprojects.visualstudio.com/813c42f7-7b2c-4815-ba8f-afd87e914f66/_workitems/edit/13266">13266</a></td>
<td>[Internal] Handle error scenarios while canceling an appointment scheduled with TSA (i.e., w/o SP)</td>
<td>Bug</td>
<td>As a TMP Scheduler, I need to be prevented from cancelling an appointment that was created prior to 4.6 since the appointment structure has changed and the cancellation will give errors</td>
<td>-when user tries to cancel an appointment created with the prior 4.4 structure that isn't linked to a scheduling package, the user gets an error indicating that this appointment needs to be cancelled in VistA</td>
</tr>
<tr class="odd">
<td><a href="https://va-crmprojects.visualstudio.com/813c42f7-7b2c-4815-ba8f-afd87e914f66/_workitems/edit/13457">13457</a></td>
<td>Prod: Group Appointment: 2nd Patient Site booking into 1st Patients Site’s Vista IEN</td>
<td>Bug</td>
<td>-the appointment books into the wrong clinic (IEN) ------ As a TMP Scheduler, scheduling a group appointment, I need to verify that each VistA clinic IEN is booked into the expected VistA station when multiple patients are booked either within different facilities (inter) or within the same facility (intra).</td>
<td><p>-when there are multiple Reserve Resources (RRs) on a CVT group appointment, even if from different patient sites/facilities</p>
<p>- each VistA clinic IEN is booked into the correct facility based on where the Patient was booked (specific RRs patient site)</p></td>
</tr>
<tr class="even">
<td><a href="https://va-crmprojects.visualstudio.com/813c42f7-7b2c-4815-ba8f-afd87e914f66/_workitems/edit/13478">13478</a></td>
<td>Prod: INC7581991 - TMP Inventory | Screen doesn't refresh</td>
<td>Bug</td>
<td>As a TMP Resource Manager I need the Approve and Complete action to refresh so that the status changes without me doing a manual refresh</td>
<td>-inventory status changes to Inactive after the Approve and Complete action is done without the user doing a manual refresh</td>
</tr>
<tr class="odd">
<td><a href="https://va-crmprojects.visualstudio.com/813c42f7-7b2c-4815-ba8f-afd87e914f66/_workitems/edit/14133">14133</a></td>
<td>Prod - TSA 2.0 Provider Preferences report not showing on TSA or preference report the provider preferences (RTC - 1173733/INC7765921)</td>
<td>Bug</td>
<td>As a TSA Approver, I need the provider preferences to display on the TSA 2.0 report and the Provider Preference report so that the data displays according to the report specs</td>
<td>-provider preferences that are on the associated user records on the SP are shown on those sections of the reports</td>
</tr>
<tr class="even">
<td><a href="https://va-crmprojects.visualstudio.com/813c42f7-7b2c-4815-ba8f-afd87e914f66/_workitems/edit/14795">14795</a></td>
<td>Patient Participating Site - Missing VistA Clinic Message</td>
<td>Bug</td>
<td>As an Scheduling Package Manager or Hub SP Manager, trying to save a participating site with Can Be scheduled flag=Yes, there is a Typo in Business process error message when no VistA clinic was added</td>
<td>-error displays with typo corrected: using singular VistA Clinic instead of plural VistA Clinics</td>
</tr>
<tr class="odd">
<td><a href="https://va-crmprojects.visualstudio.com/813c42f7-7b2c-4815-ba8f-afd87e914f66/_workitems/edit/15561">15561</a></td>
<td>Prod - Real time clinic updates throws an error when information is missing in the VistA inbound message</td>
<td>Bug</td>
<td>As a System Administrator, VistA real time clinic updates aren't processed by TMP if the Station Number is not present in the pay load, which throws an error and TMP doesn't create / update the clinic. Approved by Pauline to include it as part of TMP 4.8.</td>
<td>-​when the station number is not found in the incoming clinic update message, default to the station number of the associated site</td>
</tr>
<tr class="even">
<td><a href="https://va-crmprojects.visualstudio.com/813c42f7-7b2c-4815-ba8f-afd87e914f66/_workitems/edit/15734">15734</a></td>
<td>QA: Error on Appt Cancel Dialog for CVT INTER Group appointment when the Reserve Resource is already in Canceled status</td>
<td>Bug</td>
<td>As a TMP Scheduler scheduling a CVT INTER Group appointment, I am able to cancel from the top level appointment, which cancels all the associated patients on each RR</td>
<td>-entire appointment is cancelled including individual RRs when cancellation is from the top level appointment (successfully with no error)</td>
</tr>
<tr class="odd">
<td><a href="https://va-crmprojects.visualstudio.com/813c42f7-7b2c-4815-ba8f-afd87e914f66/_workitems/edit/16306">16306</a></td>
<td>DEV - Internal - Adding a Non-VA Email on an appointment is not sending the email</td>
<td>Bug</td>
<td>As a TMP Scheduler, I need to be able to add family member/caregiver emails, so that they will also be notified on the VVC appointment</td>
<td>Assumption is that user is on the appropriate scheduling team:<br />
<br />
-additional email notifications sent to requested emails (1 or more)</td>
</tr>
</tbody>
</table>

## Data Migrations/Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following data updates were included:  
  
1. 4.6 implementation had a Patient Technology type field with possible values including COTS Tablet, CVT Tablet. This 4.8 release removes those values as options while also updating any existing patients with those values to SIP Address instead (see deployment guide and above user story detail for \#[11219](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F11219&data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088208924&sdata=%2B2BM9J8sKIRlZNkqmStHpeuQcBUz2RF5n1hj46kEakg%3D&reserved=0)).  
2. Any existing TSAs that were approved prior to 4.8 will be updated with a Review Due Date (1 year+30 days from the final approval). This is also part of the deployment guide steps.

## Considerations/Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please be advised of the following considerations and known issues for this release:

1.  Although Scheduling Packages (SPs) can now include patient side scheduling resources for VVC type SPs, Patient Side Resources for a VVC group appointment is not fully supported from the scheduling aspect. User should not create a VVC group appointment with Patient Side Resources as checked. This is fully supported for Individual style VVC appointments however. The VVC Group feature will be further enhanced in the future based on backlog priorities and refinements.
2.  For Group Appointments, cancellation remarks entered when doing a cancellation from the main appointment screen are not passed to VistA (user must do the cancellation at the Reserve Resource level instead so that the comments are passed).

## Key Screenshots Updated

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Yearly TSA Review 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Review Due Date is calculated and included on a TSA record (1year + 30 days after final approval):  
  
![](tmp-version-2-0-release-4-8-release-notes/003.png)

Additional approval Status as part of the process (in addition to previous Approve and Deny):  
Review Pending

Reviewed and Confirmed

Reviewed and Updated

![](tmp-version-2-0-release-4-8-release-notes/004.png)

TSA record will be inactivated and the Status reason will change to EXPIRED when the re-approvals are not done in time:  
![](tmp-version-2-0-release-4-8-release-notes/005.png)

> Sample approval flow non-hub data example:

|                                                                                 |                    |                    |       |                                                                                                                |                            |                             |                           |                            |                    |                 |                     |
|---------------------------------------------------------------------------------|--------------------|--------------------|-------|----------------------------------------------------------------------------------------------------------------|----------------------------|-----------------------------|---------------------------|----------------------------|--------------------|-----------------|---------------------|
| <u>Normal expected flow non hub example: FTCs agree on Review & Updated</u> |                    |                    |       |                                                                                                                |                            |                             |                           |                            |                    |                 |                     |
| Date                                                                        | Provider FTC   | Patient FTC    |  | Comment                                                                                                    | Provider Service Chief | Provider Chief of Staff | Patient Service Chief | Patient Chief of Staff | Overall Status | Status Date | Review Due Date |
| 1-Jan                                                                           | Approve            | Approve            |       | Initial TSA approved                                                                                           | Approve                    | Approve                     | Approve                   | Approve                    | Approved           | 1-Jan           | 31-Jan              |
| 1-Dec                                                                           | Review Pending     | Review Pending     |       | 60 day Review window begins, FTCs are notified, both FTC statuses are Review Pending                           | Approve                    | Approve                     | Approve                   | Approve                    | Approved           | 1-Jan           | 31-Jan              |
| 5-Dec                                                                           | Review Pending     | Reviewed & Updated |       | One FTC updates to Reviewed & Updated, Service Chiefs still not notified, since other FTC has not taken action | Blanked out                | Blanked out                 | Blanked out               | Blanked out                | Approved           | 1-Jan           | 31-Jan              |
| 10-Dec                                                                          | Reviewed & Updated | Reviewed & Updated |       | Both FTCS have taken action, Service Chiefs and Chiefs of Staff notified                                       | Blanked out                | Blanked out                 | Blanked out               | Blanked out                | Approved           | 1-Jan           | 31-Jan              |

Additional TSA views:  
  
![](tmp-version-2-0-release-4-8-release-notes/006.png)

### Scheduling Package Management – VVC Case 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VVC scheduling packages now support addition of patient side resources (optional)

![](tmp-version-2-0-release-4-8-release-notes/007.png)

1.  
2.  

### Appointment screen – VVC case/Patient Side Resources 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is also a patient side resource checkbox when scheduling (optional). When this is selected, the user is required to enter a Patient Site instead of Provider site.  
  
![](tmp-version-2-0-release-4-8-release-notes/008.png)

1.  
2.  
3.  

### Appointment screen – Cancellation Remarks 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User can enter cancellation remarks as part of the cancellation dialog:  
![](tmp-version-2-0-release-4-8-release-notes/009.png)  
  
For an individual appointment this is also shown on the main appointment screen once cancelled:  
![](tmp-version-2-0-release-4-8-release-notes/010.png)  
  
Note for group appointments – the cancel remarks are on the Reserve Resource Level in order for the remarks to flow to VistA as part of the cancellation.

1.  
2.  
3.  
4.  

### Appointment screen – RTC/Consults additional date filter: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User can filter by date range when viewing RTCs/Consults to attach to an appointment for an individual.  
  
![](tmp-version-2-0-release-4-8-release-notes/011.png)

5.  
6.  
7.  
8.  

### Patient Technology Types Streamlined 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The list of values for Patient Technology types have been streamlined/renamed:  
COTS Tablet, CVT Tablet =\> SIP Address  
  
All related fields are now visible though not enterable depending on the selection (locked as read only). Please see the relationship details in the [11219](https://nam06.safelinks.protection.outlook.com/?url=https%3A%2F%2Fva-crmprojects.visualstudio.com%2F813c42f7-7b2c-4815-ba8f-afd87e914f66%2F_workitems%2Fedit%2F11219&data=02%7C01%7CGina.Dominique%40microsoft.com%7C8b10121f7d634fc513a208d816b7219d%7C72f988bf86f141af91ab2d7cd011db47%7C1%7C0%7C637284323088208924&sdata=%2B2BM9J8sKIRlZNkqmStHpeuQcBUz2RF5n1hj46kEakg%3D&reserved=0) user story.

![](tmp-version-2-0-release-4-8-release-notes/012.png)

9.  
10. 
11. 
12. 

### Resource Group Unique ID field increased to 30 character limit 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User can now enter additional characters:  
  
![](tmp-version-2-0-release-4-8-release-notes/013.png)

13. 
14. 
15. 
16. 

### Account 90 Day Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report was enhanced to show Disabled as well as Active users. The User Type in the output was also fixed.  
  
![](tmp-version-2-0-release-4-8-release-notes/014.png)