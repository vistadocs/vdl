---
title: TMP Version 2.0 Release 4.8 Requirements
doc_type: RS
doc_label: Requirements Specification
doc_layer: anchor
doc_subject: Release 4.8 Requirements
app_code: TMP
app_name: Telehealth Management Platform
section: CLI
app_status: active
pkg_ns: TMP
patch_ver: 2.0
patch_id: TMP*2.0
group_key: "TMP:TMP:2.0"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - bookmark
  - table
  - contents
  - defect
  - review
  - date
  - reviewed
  - vista
  - fixes
  - show
page_count: 0
word_count: 462
section_count: 2
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Telehealth_Management_Platform/tmp_4-8_requirements_signed.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Telehealth_Management_Platform/tmp_4-8_requirements_signed.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=231"
---

---
title: |
  Telehealth Management Platform (TMP) Phase 3

  4.8.0 Release Requirements Specification
---

Project [TMP (RM)](https://clm.rational.oit.va.gov/rm/process/project-areas/_FhxbEm6fEeSq6-QH2YLx3w)

Prepared by Shannon Utting

June 10, 2020

*[13457 - Group Appointment: 2nd Patient Site booking into 1st Patients Site’s](#_bookmark8)* [Vista IEN *5*](#_bookmark8)

*[12901 - Preventing Alphanumeric characters in Clinic IEN number when clinics](#_bookmark9)* [are created *5*](#_bookmark9)

[*12856 - Intermittent Issues Pulling RTCs and Consults 5*](#_bookmark10)

*[13770 - Account 90 Day report is showing User Type as 'Not Available' even](#_bookmark11)* [though there is a value in the user record *5*](#_bookmark11)

*[13266 - Handle error scenarios while canceling an appointment scheduled with](#_bookmark12)* [TSA (i.e., w/o SP) *5*](#_bookmark12)

*[15561 - Real time clinic updates throws an error when information is missing in](#_bookmark18)* [the VistA inbound message *6*](#_bookmark18)

*[15734 - Error on Appt Cancel Dialog for CVT INTER Group appointment when the](#_bookmark19)* [Reserve Resource is already in Canceled status *6*](#_bookmark19)

*[11197 - Include Hub name and additional text in Hub related Facility Approvals](#_bookmark30)* [emails *8*](#_bookmark30)

*[7981 - Add Participating Sites and Scheduling Resources to VVC Scheduling](#_bookmark41)* [Package *9*](#_bookmark41)

# INTRODUCTION


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [INTRODUCTION](#introduction)
- [TMP 4.8.0 BUSINESS EPICS](#tmp-480-business-epics)
- [TMP 4.8.0 DEFECT FIXES](#tmp-480-defect-fixes)
- [TMP 4.8.0 PRODUCT ENHANCEMENTS](#tmp-480-product-enhancements)
- [Approval Signatures](#approval-signatures)
  - [Harpreet S.](#harpreet-s)
> The purpose of this document is to define the Business Requirements. Telehealth Management Platform (TMP) Phase 3 version 4.8.0 Release will deploy the following functionality:
- Twelve defect fixes to address issues found in TMP Production.
- A yearly review process for Telehealth Service Agreements including a review due date and email reminders prior to expiration.
- Data quality improvements that prevent creation of invalid VistA clinics (missing/invalid IENs) or Scheduling Packages with missing patient side clinics.
- The ability to pass through cancellation remarks to VistA.
- Other efficiencies and defect remediations including: Additional date filter on RTCs/Consults; streamlining of available Patient Technology Types (e.g. COTS/CVT Tablet renamed to SIP Device); Account 90 Day report now has option to display deactivated as well as active users.

# TMP 4.8.0 BUSINESS EPICS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark2" class="anchor"></span>TMP TSA Management

> As a TMP TSA Approver, I need to manage TSA approvals so that agreements are reviewed and approved by staff as required (FTCs, Hub Director, Service Chiefs, Chief of Staff).

> <span id="_bookmark3" class="anchor"></span>TMP Reports & Dashboards

> As a TMP User, I need to view reports and dashboards, so that the application usage and data can be reviewed as required.

> <span id="_bookmark4" class="anchor"></span>TMP Scheduling Package Management

> As a TMP Scheduling Package Manager, I need to manage scheduling packages and associated TSAs.

> <span id="_bookmark5" class="anchor"></span>TMP Efficiencies

> As a TMP User, I need the system to be efficient and streamlined.

> <span id="_bookmark6" class="anchor"></span>TMP Scheduling

> As a TMP Scheduler, I need to schedule and cancel appointments for patients and providers along with any required resources.

# TMP 4.8.0 DEFECT FIXES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark8" class="anchor"></span>13457 - Group Appointment: 2nd Patient Site booking into 1st Patients Site’s Vista IEN

> DEFECT: As a TMP Scheduler, scheduling a group appointment, I need to verify that each VistA clinic IEN is booked into the expected VistA station when multiple patients are booked either within different facilities (inter) or within the same facility (intra).

> <span id="_bookmark9" class="anchor"></span>12901 - Preventing Alphanumeric characters in Clinic IEN number when clinics are created

> DEFECT: Preventing Alphanumeric characters in Clinic IEN number when clinics are created.

> <span id="_bookmark10" class="anchor"></span>12856 - Intermittent Issues Pulling RTCs and Consults

> DEFECT: As a TMP Scheduler scheduling an appointment, I am able to view the patient's RTCs/Consult orders so that one selected can be linked to the appointment and passed through to VistA.

> <span id="_bookmark11" class="anchor"></span>13770 - Account 90 Day report is showing User Type as 'Not Available' even though there is a value in the user record

> DEFECT: Account 90 Day report is showing User Type as 'Not Available' even though there is a value in the user record.

> <span id="_bookmark12" class="anchor"></span>13266 - Handle error scenarios while canceling an appointment scheduled with TSA (i.e., w/o SP)

> DEFECT: As a TMP Scheduler, I need to be prevented from cancelling an appointment that was created prior to 4.6 since the appointment structure has changed and the cancellation will give errors.

> <span id="_bookmark13" class="anchor"></span>16306 - Adding a Non-VA Email on an appointment is not sending the email

> DEFECT: As a TMP Scheduler, I need to be able to add family member/caregiver emails, so that they will also be notified on the VVC appointment.

> <span id="_bookmark14" class="anchor"></span>14133 - TSA 2.0 Provider Preferences Report

> DEFECT: As a TSA Approver, I need the provider preferences to display on the TSA 2.0 report and the Provider Preference report so that the data displays according to the report specs.

> <span id="_bookmark15" class="anchor"></span>13478 - TMP Inventory Screen Doesn't Refresh

> DEFECT: As a TMP Resource Manager I need the Approve and Complete action to refresh so that the status changes without me doing a manual refresh.

> <span id="_bookmark16" class="anchor"></span>8594 - Business Process Error when updating TMP Resource's TMP Site

> DEFECT: TMP Resource Manager is unable to change the TMP Site associated with the Resource and gets a Business Process Error.

> <span id="_bookmark17" class="anchor"></span>14795 - Patient Participating Site - Missing VistA Clinic Message

> DEFECT: As an Scheduling Package Manager or Hub SP Manager, trying to save a participating site with Can Be scheduled flag=Yes, there is a Typo in Business process error message when no VistA clinic was added.

> <span id="_bookmark18" class="anchor"></span>15561 - Real time clinic updates throws an error when information is missing in the VistA inbound message

> DEFECT: As a System Administrator, VistA real time clinic updates aren't processed by TMP if the Station Number is not present in the pay load, which throws an error and TMP doesn't create / update the clinic.

> <span id="_bookmark19" class="anchor"></span>15734 - Error on Appt Cancel Dialog for CVT INTER Group appointment when the Reserve Resource is already in Canceled status

> DEFECT: As a TMP Scheduler scheduling a CVT INTER Group appointment, I am able to cancel from the top level appointment, which cancels all the associated patients on each RR.

# TMP 4.8.0 PRODUCT ENHANCEMENTS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark21" class="anchor"></span>13741 - Update Account 90 Day report

> USER STORY: As a TMP Administrator, I need the Account 90 Day Report updated so that the output can show user's that have logged in in the past 90 days also and are not de-activated.

> <span id="_bookmark22" class="anchor"></span>5107 - Additional facility approval views for records needing review

> USER STORY: As a TSA Manager, I need the ability to view all Facility Approvals(TSAs) reviewed so that I can see any outstanding or completed reviews as follows:

- show what is due to be reviewed this quarter =\> Pending Review
- show what is overdue for review (e.g. based on review due date is past)
- show what was reviewed this quarter as ‘Reviewed and Confirmed’
- show what was reviewed this quarter as ‘Reviewed and Updated’
- user can select the date in a filter option if built as a view

> These additional views are required for Facility Approvals within selected time period:

> TSAs Pending Review This Quarter - any record where FTCs/Hub Director Status is Review Pending

> TSAs Overdue for Review This Quarter - any record where FTCs/Hub Director Status is Review Pending AND current date \> review due date

> TSAs Reviewed and Confirmed This Quarter - any record where (Provider FTC Approval Status=Reviewed and Confirmed) OR Patient (FTC Approval Status=Reviewed and Confirmed) OR Hub Director Approval Status=Reviewed and Confirmed)

> TSAs Reviewed and Updated This Quarter - any record where (Provider FTC Approval Status=Reviewed and Updated) OR Patient (FTC Approval Status=Reviewed and Updated) OR Hub Director Approval Status=Reviewed and Updated)

> <span id="_bookmark23" class="anchor"></span>7925 - Update Participating Site Default Lookup

> USER STORY: As a TMP Scheduling Package Manager, adding a Participating Site to an intrafacility or interfacility Scheduling Package(SP), I need to efficiently view the TMP Sites that are selectable, so that I don’t have to scroll through all TMP sites. On the Participating Site form, the user must specify whether it is a Patient or Provider site, prior to selecting the TMP Site.

> <span id="_bookmark24" class="anchor"></span>11219 - Managing Patient Technology Types

> USER STORY: As TMP Resource Manager I need to update available technology types for a Patient so that obsolete names are removed and device names are streamlined for clarity in the field.

> <span id="_bookmark25" class="anchor"></span>5094 - Reviewed and updated action

> USER STORY: As a member of the TSA Initial Approval Team (FTCs for non-hub, Hub Director for Hub), I need to mark an interfacility Facility Approval(TSA) as 'Reviewed and Confirmed', so that an interfacility Facility Approval(TSA) is re-verified on a periodic basis. This should be for both Provider Side and Patient side FTC Teams for non hub approval process and Hub Director for hub approval process.

> <span id="_bookmark26" class="anchor"></span>8313 - Update participating site views

> USER STORY: As a SP Manager, I need to see the vista clinics associated with a participating site (PS) and audit dates, so that I don't have to click into each record individually.

> <span id="_bookmark27" class="anchor"></span>5093 - Initiate review process

> USER STORY: As a member of the TSA Initial Approval Team (FTCs for non-hub, Hub Director for Hub), I need the system to initiate a review process so that I have a window of time to review previously approved interfacility TSAs according to the yearly review policy. The 'review due date' is calculated as the 1 year anniversary of final approval date +30 calendar days (from Date when Facility Approval Status=Approved).

> <span id="_bookmark28" class="anchor"></span>8027 - Participating site resource subgrid

> USER STORY: As an SP Manager, I need to list out TMP resources under a participating site's associated Paired Resource Group (PRG) so that I don't have to click into each PRG to see what resources are inside of it.

> <span id="_bookmark29" class="anchor"></span>7080 - Appointment screen - cancelation remarks

> USER STORY: As a TMP Scheduler, I need to optionally enter cancel remarks/comments so that these comments can flow to VistA for documentation (into the cancel remarks field).

> <span id="_bookmark30" class="anchor"></span>11197 - Include Hub name and additional text in Hub related Facility Approvals emails

> USER STORY: As a TSA Approver, I need to understand information for Hub related approvals so that I know which Hub and Provider Facilities are requiring my approval.

> <span id="_bookmark31" class="anchor"></span>5092 - Reviewed and confirmed action

> USER STORY: As a member of the TSA Initial Approval Team (FTCs for non-hub, Hub Director for Hub), I need to mark an interfacility Facility Approval(TSA) as 'Reviewed and Confirmed', so that the interfacility Facility Approval(TSA) complies with yearly review policy. This should be for both Provider Side and Patient side FTC Teams for non-hub approval process, Hub Director team for hub approval process. Next Review Due Date will be 1 yr+30 days from this action date.

> <span id="_bookmark32" class="anchor"></span>8020 - Resource Group – Increase Unique ID Character Limit

> USER STORY: As a TMP Resource Manager editing a TMP Resource Group, I need to have a bigger text size for the unique identifier, so that up to 30 characters can be entered.

> <span id="_bookmark33" class="anchor"></span>5090 - Initial review notification email

> USER STORY: As a member of the TSA Initial Approval Team (FTCs for non-hub, Hub Director for Hub), I need to be notified that a previously approved interfacility Facility Approval(TSA) needs to be reviewed by a specific 'review due date', so that I can review and confirm the existing Facility Approval or make updates that trigger required approvals all over again.

> <span id="_bookmark34" class="anchor"></span>7079 - Appointment screen - Consult/RTC table additional filters

> USER STORY: As a TMP Scheduler, I need the RTC and Consult display to allow me to filter on a date range, so that I don't have to scroll through all the RTC/Consults in one single table (given the 2 year+future VistA criteria).

> <span id="_bookmark35" class="anchor"></span>14064 - Scheduling package validation when adding patient side resources

> USER STORY: As a Scheduling Package Manager, adding patient side scheduling resources, I should include a VistA clinic for clinic based type appointments, so that I avoid scheduling errors.

> <span id="_bookmark36" class="anchor"></span>5590 - Final Warning Email Notification

> USER STORY: As a member of the TSA Initial Approval Team (FTCs for non-hub, Hub Director for Hub), I need to get a final reminder that the Facility Approval(TSA) will be deactivated 7 calendar days before the deactivation date (review due date + 1 days), so that I get a final warning to do the overdue review.

> <span id="_bookmark37" class="anchor"></span>14031 - Avoid Linking Inappropriate VistA clinic to a Scheduling Resource

> USER STORY: As a Scheduling Package Manager, adding VistA clinic type scheduling resources to an SP, I shouldn't be allowed to select views that explicitly point to invalid clinics, so that I chose valid clinics for scheduling.

> <span id="_bookmark38" class="anchor"></span>15183 - Update TSA review related views

> USER STORY: As a TSA Approver, I need the TSA review related views updated so that I have better readability and additional columns visible.

> <span id="_bookmark39" class="anchor"></span>5382 - Keep history of all reviewers and approvers

> USER STORY: As a TSA Manager, I need the system to keep a history of all previous approvals and reviews for a Facility Approval (TSA), so that any audit would show the entire history of approvals and reviews including dates and signee information.

> <span id="_bookmark40" class="anchor"></span>5108 - Deactivation/Overdue Email Notification

> USER STORY: As a member of the TSA Initial Approval Team (FTCs for non-hub, Hub Director for Hub), I need to be notified that a previously approved interfacility TSA is still waiting to be reviewed by a specific 'review due date' when the review date is past.

> <span id="_bookmark41" class="anchor"></span>7981 - Add Participating Sites and Scheduling Resources to VVC Scheduling Package

> USER STORY: As a TMP Scheduling Package Manager, I need to add sites and scheduling resources to patient side VVC appointments, so that I can add the appropriate administrative VistA Clinic or other scheduling resources.

# Approval Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Harpreet S.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Digitally signed by Harpreet S. Sodhi 219003

> Date: 2020.06.10

> 18:03:59 -04'00'

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><span id="_bookmark43" class="anchor"></span><strong>VA IT PM Signature</strong></th>
<th><blockquote>
<p><span id="_bookmark44" class="anchor"></span><strong>Date</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| <span id="_bookmark45" class="anchor"></span>Business Owner Signature | <span id="_bookmark46" class="anchor"></span>Date |
|---------------------------------------------------------------------------|-------------------------------------------------------|