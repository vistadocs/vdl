---
title: VPFS VistAMigrate Data Migration Version 1.2 Users Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: Users Guide
app_code: VPFS
app_name: Veterans Personal Finance System
section: GUI
app_status: active
pkg_ns: VPFS
patch_ver: 1.2
patch_id: VPFS*1.2
group_key: "VPFS:VPFS:1.2"
file_numbers: []
security_keys: []
menu_options: 0
description: > VPFS is the mini-banking system used to manage the accounts of VHA patients in the VHA hospital system. VPFS replaces the Personal Funds of Patients (PFOP) system that was used previously. VPFS looks different from PFOP because it is a web-based application; however, its design and functionality a
audience: 
keywords: 
  - blockquote
  - class
  - style
  - width
  - strong
  - colspan
  - even
  - table
  - colgroup
  - thead
page_count: 0
word_count: 39126
section_count: 7
table_count: 3
figure_count: 0
appendix_count: 6
has_toc: False
is_stub: False
pub_date: July 2020
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VPFS/vistamigrate_1_datamigrationguide.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VPFS/vistamigrate_1_datamigrationguide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=170"
---

## Veterans Personal Finance System (VPFS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistAMigrate Data Migration Guide

> Version 1.2.0

![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/001.png)

> July 2020

> U.S. Department of Veterans Affairs Health Systems Design & Development

#### Document Approval Signatures

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 33%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>VPFS Project</p>
<p>Title: Project Manager</p>
</blockquote></th>
<th><blockquote>
<p>Signed: [signature on file] Typed <mark>redacted</mark></p>
</blockquote></th>
<th><blockquote>
<p>Date:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SQA Group</p>
<p>Title: SQA Manager</p>
</blockquote></td>
<td><blockquote>
<p>Signed: [signature on file] Typed: <mark>redacted</mark></p>
</blockquote></td>
<td><blockquote>
<p>Date:</p>
</blockquote></td>
</tr>
</tbody>
</table>

> History of Revisions

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 22%" />
<col style="width: 35%" />
<col style="width: 11%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section Changed</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description of Change</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Effective Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Contacts</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Initial release of document</p>
</blockquote></td>
<td><blockquote>
<p>12/01/06</p>
</blockquote></td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td><blockquote>
<p>Section 4.9.1</p>
</blockquote></td>
<td><blockquote>
<p>Added note about the removal of PRPF_DATA_MIGRATION_USERS</p>
<p>security key</p>
</blockquote></td>
<td><blockquote>
<p>01/18/07</p>
</blockquote></td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1.2.0</p>
</blockquote></td>
<td><blockquote>
<p>Footer sections</p>
</blockquote></td>
<td><blockquote>
<p>Updated footer sections with updated date and version number.</p>
</blockquote></td>
<td><blockquote>
<p>01/15/18</p>
</blockquote></td>
<td><mark>redacted</mark></td>
</tr>
</tbody>
</table>

#### Table of Contents

[About This Document 1](#about-this-document)
> [Document Purpose. 1](#document-purpose)
> [Document Audience 1](#document-audience)
[Conventions Used in this Document 1](#conventions-used-in-this-document)
> [Additional Resources 1](#additional-resources)
1.  [Overview of VistAMigrate 2](#overview-of-vistamigrate)
2.  [Preparing to Migrate Data from PFOP to VPFS. 3](#preparing-to-migrate-data-from-pfop-to-vpfs)
    1.  [Overview. 3 2.2](#overview)
Flow of Data through VistAMigrate 4 2.3
Groups/Roles in Data Migration 5 2.4
> Preparation Checklist. 6 2.5
Patient Funds Data Migration Process 8 2.6
Data Migration Task Assignments 9 2.7
Overview of Steps in the M Environment. 10 2.8
> Overview of Steps in Reengineered Environment. 11
[2.9 Data Migration Success Criteria. 11](#data-migration-success-criteria)
3.  [Performing Diagnostics and Data Cleanup in the M Environment 12](#performing-diagnostics-and-data-cleanup-in-the-m-environment)
    1.  [Patient Funds Diagnostic Summary Report. 12](#patient-funds-diagnostic-summary-report)
    2.  [Patient Funds Diagnostic Detail Report 13](#patient-funds-diagnostic-detail-report)
    3.  [Correcting Patient Funds Errors 14](#correcting-patient-funds-errors)
4.  [Migrating Data Using VistAMigrate. 15](#migrating-data-using-vistamigrate)
    1.  [Accessing VistAMigrate 15](#accessing-vistamigrate)
    2.  [VistAMigrate Welcome Page. 16](#vistamigrate-welcome-page)
        1.  [Banner 17](#banner)
        2.  [Navigation Bar 18](#navigation-bar)
        3.  [Description of Steps 18](#description-of-steps)
        4.  [Process Running Indicator 19](#process-running-indicator)
    3.  [M Diagnostics 19](#m-diagnostics)
    4.  [M Extract. 22](#m-extract)
    5.  [Stage Data 24](#stage-data)
    6.  [Analyze Data 27](#analyze-data)
    7.  [Convert Data. 30](#convert-data)
    8.  [Verify Data 32](#verify-data)
    9.  [Final Steps 34](#final-steps)
        1.  [Finalizing Data Migration 35](#finalizing-data-migration)
        2.  [Resetting VistAMigrate to Start Over 36](#resetting-vistamigrate-to-start-over)
[Appendix A. Frequently Asked Questions 37](#appendix-a.-frequently-asked-questions)
[Appendix B. Migration Business Rules 39](#appendix-b.-migration-business-rules)
> [Migration Business Rules. 39](#migration-business-rules)
iii List of Figures
> [M Extract Results 69](#m-extract-results)
> [Stage Data Log File. 71](#stage-data-log-file)
> List of Figures
> Figure 2-1. Flow of Data. 4
> Figure 2-2. The Data Migration Process. 8
> Figure 4-1. VistAMigrate Login Page 15
> Figure 4-2. VistAMigrate Pick Project page 16
> Figure 4-3. VistAMigrate Welcome page. 17
> Figure 4-4. Process Running Indicator 19
> Figure 4-5. M Diagnostics page 20
> Figure 4-6. M Diagnostics Page with Sample Diagnostic Summary Report 21
> Figure 4-7. M Diagnostics Page with Detail Report 22
> Figure 4-8. M Extract Page 23
> Figure 4-9. M Extract Page with Extract Results. 24
> Figure 4-10. Stage Data page. 25
> Figure 4-11. Stage Data Page with Log File 26
> Figure 4-12. Stage Data Page with Bad File Data 27
> Figure 4-13. Analyze Data Page. 28
> Figure 4-14. Analyze Data Page with VPFS – Analyze Report 29
> Figure 4-15. Convert Data Page. 30
> Figure 4-16. Convert Data Page with Results. 31
> Figure 4-17. Convert Data Page with Errors. 32
> Figure 4-18. Verify Data Page 33
> Figure 4-19. Verify Data Page with Log. 33
> Figure 4-20. Final Steps Page. 35
> iv July 2020 List of Tables

#### List of Tables

> Table 2-1. Groups and Roles 5
> Table 2-2. Preparation Checklist 6
> Table 2-3. Data Migration Task Assignments 9
> Table A-1. Frequently Asked Questions. 37
> Table B-1. Migration Business Rules 39
> Table C-1. PFOP Extraction File Layout, VPFS Mapping 50
> Table D-1. Description of Diagnostic Summary Report 66
> Table E-1. VistA Files Owned by the PRPF Namespace 104
> This page is left blank intentionally

## About This Document

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Document Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of the VistAMigrate Data Migration Guide is to provide a step-by-step guide to the data migration process. The document provides instructions for the entire migration process from installing any MUMPS (M) patches required for running data diagnostics to finalizing the migration on the Java side.

### Document Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The audience for this document includes:

- All stakeholders with a role to play in data migration
- Local Information Resource Management (IRM) and Automated Data Processing Application Coordinator (ADPAC)
- Enterprise Management Center (EMC), Enterprise VistA Support (EVS) and National Training and Education Office (NT&EO)

### Conventions Used in this Document

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Format</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Indicates…</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>bold</strong></p>
</blockquote></td>
<td><blockquote>
<p>A control that you click, such as a button, icon, or link, or a field label.</p>
<p>Example: Click <strong>Deploy</strong>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Courier - normal</p>
</blockquote></td>
<td><blockquote>
<p>Text that appears on the screen or in a log file.</p>
<p>Example: Table created.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Courier - <strong>bold</strong></p>
</blockquote></td>
<td><blockquote>
<p>Text that you type.</p>
<p>SQL&gt; <strong>quit</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>&lt;<em>Courier&gt;</em> italic and enclosed in angle brackets</p>
</blockquote></td>
<td><blockquote>
<p>A variable that you replace with the specified text</p>
<p>Enter password: &lt;<em>SYSDBA password</em>&gt;</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Additional Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For additional documentation, go to the VHA Application Modernization website: <span class="mark">redacted</span>

#### Overview of VistAMigrate

## Overview of VistAMigrate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Department of Veterans Health Administration (VHA) is in the process of reengineering a number of legacy applications, moving from the MUMPS-based Veterans Health Information Systems and Technology Architecture (VistA) environment to the Veterans Affairs (VA’s) standard modern environment, which includes Oracle for the database environment and The Java 2 Platform, Enterprise Edition (J2EE) for the application software environment. The redesigned applications will use the Oracle database and the BEA WebLogic Application Server, built using the J2EE open source platform running on Red Hat Linux servers. The database will be centralized for all facilities at the VAEMC, and applications will be accessible via a secure, 508-compliant Web browser front end.

> VistAMigrate is the tool that VPFS (Veterans Personal Funds System) can use to migrate current demographic data from VistA legacy to reengineering applications. VistAMigrate includes reports that you use to analyze your production data in preparation for migration. After you have thoroughly analyzed and cleaned your data, you can cut over to the production environment. After cutover, you will still be able to access VistA legacy for reporting purposes and to view historical information; but you will not be able to make changes to data in the legacy system.

## Preparing to Migrate Data from PFOP to VPFS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VPFS is the mini-banking system used to manage the accounts of VHA patients in the VHA hospital system. VPFS replaces the Personal Funds of Patients (PFOP) system that was used previously. VPFS looks different from PFOP because it is a web-based application; however, its design and functionality are modeled after PFOP. You can perform all the functions in VPFS that were available in PFOP, with the exception of a few functions that are no longer needed because of the new built-in security controls.

> One of the major changes is that VPFS is a centralized system. With PFOP, each site used a stand-alone copy of the software and there were differences between local versions, such as data structures, business rules, etc. With VPFS, all sites access the same centralized application using a web browser over the VHA secure Intranet. VPFS stores all data for all sites in one centralized database. Access to the data in the database is controlled by security software that limits access according to your VistA site and user role.

> Data that is migrated from the PFOP to the VPFS include: patient name and identifying information, patient type and status, account limits, balance, and other related information. The balance from each existing PFOP account will be carried forward as a single transaction (BALCARFWD) to start each new VPFS account. All deferred transactions will also be migrated.

> To get the balance information, the migration process will automatically insert a record based on an extract of current balance and associated data. If the migration is being performed from a manual system, the Patient Funds Clerk (PFC) can perform a deposit transaction (using the defined process for moving from a manual system to VPFS). From this point of view, it is not necessary to migrate more than current data. However, since at the time of cutover there may be transactions with deferral dates (so that their amounts are not included in the Total Available until these deferral dates are reached), all deferred transactions will be brought over.

> Note: Go to PFOP to review past transaction history. The transaction history in VPFS will begin with the migrated transactions and the initial balance carried forward.

> Some of the data that is displayed in VPFS comes from other files and cannot be updated through VPFS:

- Patient File Data: Address, Guardian information, date of birth, SSN, Claim Number, etc. are provided by the Patient File and refreshed with the most current information each time you access VPFS. Changes to patient file data must be made at the source in the Patient File.
- Standard Data Service (SDS): The standard State list, Country list, and Institution list are provided by SDS. Changes to these standard lists must be made by the SDS group.

### Flow of Data through VistAMigrate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following diagram shows the flow of the data from M through VistAMigrate and into the Oracle production tables.

> is data clean?

> Figure 2-1. Flow of Data

### Groups/Roles in Data Migration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Individuals from a number of different groups have roles in the data migration, both for field testing and for the national rollout. These groups and roles are described in the following table:

> Table 2-1. Groups and Roles

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Group</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Role</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Field Test Site</p>
</blockquote></td>
<td><blockquote>
<p>Various resources:</p>
</blockquote>
<ul>
<li><p>Champion (site “owner”: supervise local activities)</p></li>
<li><p>Business users (cleanup data)</p></li>
<li><p>Local IRM / Site Manager (set up VistA User Accounts for use by Authentication and Authorization service)</p></li>
<li><p>Local fiscal staff (participate in evaluation of migrated data)</p></li>
</ul></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Project team</p>
</blockquote></td>
<td><blockquote>
<p>Development owners of the application:</p>
</blockquote>
<ul>
<li><p>Responsible for support through field testing</p></li>
<li><p>Drive field testing</p></li>
<li><p>Responsible for all preparations for implementation through field testing</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Project Implementation Office (PIO)</p>
</blockquote></td>
<td><ul>
<li><p>Provide coordination between the EMC hosting site, EVS, Health Systems Design &amp; Development (HSD&amp;D), and the local sites.</p></li>
<li><p>Notify the hosting site of scheduled deployment dates.</p></li>
<li><p>Work with the NT&amp;EO</p></li>
<li><p>Participate in pre-testing activities in order to provide advice and get familiar with the project to plan for post testing activities.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Hosting Site and EMC</p>
</blockquote></td>
<td><ul>
<li><p>Provide and maintain the hardware.</p></li>
<li><p>Provide and maintain the software environment.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EVS</p>
</blockquote></td>
<td><ul>
<li><p>Provide advice and support in pre-testing activities (e.g. candidate site contacts)</p></li>
<li><p>Ongoing support of the post-testing project</p></li>
<li><p>Participate in pre-testing activities in order to provide advice and get familiar with the project so as to plan for post-testing activities</p></li>
</ul></td>
</tr>
<tr class="even">
<td><blockquote>
<p>National Training and Education Office (NT&amp;EO)</p>
</blockquote></td>
<td><ul>
<li><p>Training oversight</p></li>
<li><p>Training plan and materials oversight</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Technical Support Office (TSO)</p>
</blockquote></td>
<td><ul>
<li><p>Technical assistance for data cleanup</p></li>
<li><p>Provide training for VistAMigrate</p></li>
<li><p>Coordinate with the sites to complete the migration</p></li>
</ul></td>
</tr>
</tbody>
</table>

### Preparation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The data migration process involves a number of steps that begin well before the actual cutover. Tasks to perform prior to the beginning of data cleanup are listed in the table below, which can be filled in for each site and used as a checklist.

> Table 2-2. Preparation Checklist

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 17%" />
<col style="width: 13%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Task</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Assigned To</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Due Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comments</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Identify roles:</p>
</blockquote>
<ul>
<li><p>Who is the data owner for the site?</p></li>
<li><p>Who will be responsible for the data cleanup?</p></li>
<li><p>Who will participate in the data cleanup?</p></li>
<li><p>Who will support data cleanup?</p></li>
<li><p>Who will ensure that the appropriate staff members have access to the Diagnostic Routine on the PFOP Menu?</p></li>
</ul></td>
<td></td>
<td></td>
<td><blockquote>
<p>Although one person will be primarily responsible for ensuring that the data is properly cleansed, many others may participate in the actual cleanup. These people should be subject matter experts who are familiar with what data is valid, and who know the business rules.</p>
<p>Since there is one centralized database and one centralized application server, local IRM do not have to support the actual application. But, they will be critical in supporting the M patch that runs the diagnostic routine and in providing access to it.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Identify staff filling each of the above roles.</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>The person performing this task must have the authority to commit staff resources to specific data cleanup tasks.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Hold a site stakeholders’ meeting, including all above staff.</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>This meeting is to explain what each role is supposed to do, to provide training in the process and tool, and to review the data migration schedule for the site.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Train participating site staff.</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>Training includes how to perform the data cleanup.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 19%" />
<col style="width: 13%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Review the current state of the data.</p>
</blockquote></th>
<th></th>
<th></th>
<th rowspan="2"><blockquote>
<p>Identify any special problems or issues that will have to be resolved during cleanup.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Task</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Assigned To</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Due Date</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Comments</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>Review the detailed schedule for cleanup.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Determine how normal functioning will be affected by the data migration dates.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>For example: Will this affect the reconciliation process?</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Perform detailed contingency planning in the event of a data migration failure.</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Decide on the site’s data migration error reporting and notification process.</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Install Diagnostic Patch 15 on the local VistA legacy application to be used to perform data cleanup.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>This step must be performed by local IRM or the ADPAC staff.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Install Migration Patch 16 on the local VistA legacy application to be used to perform the data extract when cleanup is complete.</p>
</blockquote></td>
<td></td>
<td></td>
<td rowspan="2"><blockquote>
<p>The Extract will be executed from the VistAMigrate tool, not from the local VistA application menu.</p>
<p>This step must be performed by local IRM or the ADPAC staff.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>Install Patch 17, which locks down the VistA legacy application.</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>This step must be performed by local IRM or the ADPAC staff.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 17%" />
<col style="width: 13%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>It is highly recommended that you set up a Data Migration binder for your site and ensure that all persons involved understand the use of the binder.</p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p>This binder is very important because it will contain the history of your data migration (such as the Diagnostic reports and documentation of error corrections).</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Patient Funds Data Migration Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before deploying reengineered applications, each site cycles through the data migration steps shown in Figure 2-2:

- The diagnosis / cleanup process (shown in yellow) is performed in the M environment a number of times to ensure that data is clean and ready for migration.
- The steps in the reengineered environment (shown in white) are performed using the VistAMigrate software tool. You can restart the data migration process at any point and go back to the M environment to clean up data as long as you have not performed the final step.
- The final step (shown in blue) moves the data into the production tables in the new environment. At this point the site begins to use the reengineered application for all data entry. Patch 17 is installed in the M environment to lock data entry in the legacy application. Reporting functions remain available for auditing purposes.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 34%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Steps in M environment</p>
</blockquote></th>
<th><blockquote>
<p><strong>Diagnose data in M database</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Cleanup data in M database</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Steps in New</p>
</blockquote></td>
<td><blockquote>
<p><strong>Extract</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Stage Data</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Environment</p>
</blockquote></td>
<td><blockquote>
<p>Extract data</p>
</blockquote></td>
<td>Move extracted</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Using</p>
</blockquote></td>
<td><blockquote>
<p>from M</p>
</blockquote></td>
<td><blockquote>
<p>data into</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistAMigrate</p>
</blockquote></td>
<td><blockquote>
<p>database.</p>
</blockquote></td>
<td><blockquote>
<p>staging</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p><strong>Analyze Data</strong></p>
</blockquote></td>
<td><strong>Convert Data</strong></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Diagnose data</p>
</blockquote></td>
<td>Move data from</td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>in staging</p>
</blockquote></td>
<td><blockquote>
<p>staging to</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>database.</p>
</blockquote></td>
<td><blockquote>
<p>production.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p><strong>Verify Data</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Finalize</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Diagnose data in</p>
</blockquote></td>
<td>Finalize data in</td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>production</p>
</blockquote></td>
<td><blockquote>
<p>production</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>database.</p>
</blockquote></td>
<td><blockquote>
<p>database</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Figure 2-2. The Data Migration Process

### Data Migration Task Assignments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You may want to use the following table to record data migration task assignments, due dates, and comments.

> Table 2-3. Data Migration Task Assignments

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 19%" />
<col style="width: 14%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Task</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Assigned To</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Due Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comments</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Run the Diagnostic routine and perform data cleanup in the M environment.</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Document results of each run and store results in a binder.</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 16%" />
<col style="width: 14%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>When data is sufficiently clean, obtain sign-off on readiness to migrate the data.</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Run the M Diagnostic step.</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Run the M Extract step</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Run the Stage Data step.</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Run the Analyze Data step.</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Using the Analyze report, verify that the data is sufficiently clean to migrate.</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>If data is not sufficiently clean, you can perform one of the following steps:</p>
</blockquote>
<ul>
<li><p>Re-run the Diagnostic routine and perform data cleanup in the M environment. After data is cleaned up, re-run the migration process again.</p></li>
</ul>
<blockquote>
<p>(OR)</p>
</blockquote>
<ul>
<li><p>Run the Convert Data step.</p></li>
</ul></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Run the Verify Data step to verify that there is no data loss or corruption.</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Run the M Diagnostic Summary and Detail reports again <em>in the VistA legacy application</em>.</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Task</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Assigned To</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Due Date</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Comments</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>Compare the M Diagnostic reports from before and after the migration to ensure the data has not changed.</p>
</blockquote></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td colspan="3"></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Evaluate the migration results to ensure that they meet the Data Migration Success Criteria. (See <u>2.9. Data Migration Success Criteria</u>)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Obtain sign-off on the results of the data migration.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Finalize the data migration.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>In production, continue to monitor the application and the data.</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Overview of Steps in the M Environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before You Begin: Complete all the preparation tasks in section 2.4 Preparation Checklist before you begin the data migration process.

> For descriptions and instructions for installing Patches 15, 16, and 17, see the documentation bundled with the patches or see Appendix E of this document.

> For assistance using Patch 15 to diagnose and clean up data in the M environment, see the *PRPF Data Diagnostic Patch User Guide*.

> Staff at the local site complete the following data migration steps in the M environment as shown in yellow (shaded) shapes in the Figure 2-2. This is an iterative process. Cycle through these steps repeatedly until you are confident that your data will migrate successfully.

1.  Diagnostics: Run the diagnostic routine in the M environment to check for errors, such as invalid date format or missing social security number (SSN).
2.  Review: Review the summary and detailed error reports that are produced by the diagnostic routine to identify errors that need to be corrected before migrating data to the reengineered application.
3.  Cleanup: Use the M-system menu options to clean data by correcting any data errors found in the summary and detailed error reports produced by the diagnostic routine.

> Notes: Cleanup should be performed by staff members who understand the data and the business rules. If necessary, authorized users can clean up the data by going into the M code using standard processes and documenting changes. It is important to correct any data that violates the rules imposed by the FileMan data dictionary’s input transform for a field. Such data errors could cause the migration process to fail.

4.  Repeat steps 1 through 3 to diagnose, review, and clean up data until you are satisfied that the data is clean enough to migrate to the new database.

### Overview of Steps in Reengineered Environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once staff at the local site determine that data is clean and that it meets migration standards, the designated VistAMigrate user completes the data migration steps in the reengineered environment as shown in the un-shaded shapes in Figure 2-2. For details about using VistAMigrate, see Chapter 4. Migrating Data Using VistAMigrate.

> Complete these steps in VistAMigrate:

1.  Run M Diagnostics to verify that the data is clean and ready for migration.
2.  Run M Extract to extract the data from the M environment and view the extract results.
3.  Run Stage Data to move the extracted data into the Oracle staging database.
4.  Run Analyze Data to run diagnostics on the staged data to check for errors in the Oracle staging environment.
5.  Run Convert Data to move the data from the Oracle staging database to the Oracle production database.
6.  Run Verify Data to run diagnostics on the production data to check for errors in the Oracle production environment.
7.  Final Steps: Business owners and other stakeholders determine whether the results look accurate and whether the site is ready to finalize the migration:
    - Start Over: If the site is not ready to finalize the migration, restart the process.
    - Finalize: If the site is ready, finalize the migration, begin using the reengineered application, and use M Patch 17 to disable data entry in the legacy application.

### Data Migration Success Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The data migration success criteria must be met in order to proceed with using the reengineered application in a production environment.

- No records failed to load or were unaccounted for.
- None of the data was corrupted.
- None of the data (individual field values) was lost.
- All transformations to the data can be traced to a business rule.
- All fields derived from calculations are accurate.

> Note: If some records fail to load, it is expected that users will re-enter identified missing records in the VPFS system. For related information in Business Rules, refer to <u>Appendix B Business Rules.</u>

#### Performing Diagnostics and Data Cleanup in the M Environment

## Performing Diagnostics and Data Cleanup in the M Environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Diagnostics and data cleanup is an iterative process that typically requires several cycles of error checking and correcting before data for the site can be migrated. The Diagnostic routine checks all of the data for a number of identified errors that may prevent the data from migrating successfully. The Data Diagnostic Report produces both a summary and a detailed report, that you use as a reference to locate and correct data errors. You can print or view the reports online.

> Generally, you use the VistA menu options to correct errors. However, if this is not feasible, ask your local ADPAC representative to coordinate the cleanup of data owned by other groups.

> Note: All data cleanup cycles must be completed 2 weeks prior to the beginning of the actual data migration for the site. Several days before cutover, there will be one more run of the Diagnostic routine to check the data quality prior to beginning the data migration process.

> To access the Patient Funds Diagnostic reports:

1.  Log on to PFOP as PRPF Supervisor.
2.  Open the Patient Funds Supervisor Menu \[PRPF SUPERVISOR\].
3.  Select PRPF DATA DIAGNOSTIC REPORT.

> After a short period, dots appear to indicate that the report is running, the Patient Funds Diagnostic Summary report is displayed. The DEVICE: prompt appears.

4.  Do any of the following:
    - Let the report print to the screen using ;132;999, then copy and paste the report to a text editor.
    - Turn on capture to file in KEA.
    - Enter a printer name to print both the summary and detail versions of the Patient Funds Diagnostic Summary report.

> DEVICE: \<*your_printer*\>

> Both reports are printed on the printer you specified. File the reports in the site’s data migration binder.

- Enter a file name to save both the reports to file.

> DEVICE: \<*folder*/*file_name*\>

> A file containing both versions of the report is saved to the location and file name that you specified.

- To exit without saving or printing the reports, enter the caret symbol (^).

> Note: For additional information, refer to the *PRPF Data Migration Patch User Guide.*

### Patient Funds Diagnostic Summary Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Patient Funds Diagnostic Summary report is designed to be a quick and easy way for you to validate all data that will be involved with the migration of the Patient Funds package to the new VPFS application.

> 3\. Performing Diagnostics and Data Cleanup in the M Environment

> The diagnostic report generates a Summary Report, which is intended to be a quick reference to the amount of data elements that are not validating correctly. The Summary Report contains the total number of patient accounts processed and the total balance of all patient accounts at the time the summary was generated. For a sample of this report, see Appendix D.

### Patient Funds Diagnostic Detail Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> At the end of the summary report a prompt appears asking if you would like to generate the detail report. Typically, the error count in the summary report provides all the information that you need to view your progress in cleaning up data and generating the detail report is not necessary.

> Note: The detail report can be quite large. Before you generate the detail report, check the notation at the end of the summary report indicating how many lines will be in the detail report. (See the highlighted text in the sample below.)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* NOTE: In addition to the summary report there is an available detail report, this report can be sent to any device or flat file if required.

> \>\>\>\>\> The detail diagnostic report will contain 2550 lines.

> If you still desire the detail report, then please input the name of the device that the report will be sent to.

> If the detail report is not desired then input "^" at the device prompt and the detail report will not print.

> DEVICE:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> To access the detail report, at the DEVICE prompt, do one of the following:

- To display the report on the screen, accept the defaults.
- To print the report, enter the name of a printer.
- To save the report to a flat file, enter a file name.
- To return to the Supervisor's Menu without displaying, printing, or saving the report, enter ^.

> The detail report records consist of a series of data fields (STATION ID,ERR#,NAME,DESC,VALUE). Each field is separated by the delimiter “^”. All detail records can be imported into a spreadsheet and sorted or generated into other reports. The detail report is sorted by default in the order of Station-id then by error number and then by patient name. For a sample of this report, see Appendix D.

- PFOP data: If an asterisk (\*) appears by the error number on the summary report, the data for the field is owned by PFOP and can be edited by PFOP. Patient Funds staff can use the appropriate VistA Patient Funds menu options to correct the data for each patient.
- Non- PFOP data: If no asterisk (\*) appears by the error number on the summary report, the data for the field is not editable by Patient Funds staff. Contact your ADPAC to coordinate changes to data that is owned by other packages.
3.  Performing Diagnostics and Data Cleanup in the M Environment

### Correcting Patient Funds Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section provides tips for correcting errors in the M environment.

> Note: If you cannot correct the error through the local VistA legacy application, or if there are too many of a certain type of error to correct easily manually, follow the appropriate chain of command to escalate the issue. This may include asking the EVS team for assistance.

- Use the appropriate VistA Patient Funds menu options to make your corrections.
- It is highly recommended that you keep a log of the corrections you make and store the log in your site’s Data Migration binder. The log should note what the errors were, who corrected them, and the date corrected.
- Decide how to handle cases where required data is missing. You may decide to replace missing data with a default value. For example: If a date field is missing the day part of the date, provide a default day value such as “01.” Be sure to document your decisions and document any data that you will need if you decide to re-enter any records or data after cutover.
- Repeat the Diagnosis and Data Cleanup process until the Summary Report shows a count of 0 for any actual errors, or until the site data owners have decided that the data is sufficiently clean to migrate even if it still contains errors that will not stop the automated migration process.
- It is recommended that you hold a weekly data cleanup review to share findings with other sites to improve the process and to ensure successful migration for all sites. Sites can work together to:
- Develop consistent approaches for specific kinds of errors. For example: In the case of missing data in the day field, sites may decide to make the correction the same way, such as entering 1 for a missing day.
- Share frequently asked questions (FAQs).
- Recommend modifications to diagnostic routines.

## Migrating Data Using VistAMigrate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once your site data owners have approved data for migration to the reengineered environment, you are ready to proceed with the migration steps in the reengineered environment. Use the VistAMigrate software tool to migrate data.

> Note: Contact the system administrator for your site to gain access to VistAMigrate. This application uses the same access and verify codes that you use to access your VistA system, however an additional security key (PRPF_DATA_MIGRATION_USERS) is required.

### Accessing VistAMigrate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To access VistAMigrate:

1.  Open a web browser and go to http://\<*host\>*:\<*port\>*/vistaMigrate/

> The VistAMigrate Login page opens.

![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/002.png)

> Figure 4-1. VistAMigrate Login Page

2.  Enter your VistAMigrate login information:
    1.  Enter access code: Enter the VistAMigrate access code for the site.
    2.  Enter verify code: Enter the VistAMigrate verify code for the site.
3.  Institution: Select the site from the dropdown list of institutions.
4.  Click Login.

> The Pick Project page opens.

> ![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/003.png)

> Figure 4-2. VistAMigrate Pick Project page

5.  Select from the dropdown list, the reengineered application to which you want to migrate data.
6.  Click OK.

> Loading… flashes on the page while the application loads, then one of the following occurs:

- If this is the first or a restarted VistAMigrate session for the site, the Welcome page opens. Continue with the next section.
- If the data migration process was previously started for the site, the page opens for the last step accessed. Continue with the section for that step.

### VistAMigrate Welcome Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistAMigrate Welcome page provides the following:

- A banner across the top of the page displays migration status information for your site. This banner appears on all VistAMigrate pages and is refreshed with current information as you move through the data migration steps. See Section 1. Banner for more information.
- A navigation bar in the left panel of the page provides access to steps in the data migration process. This navigation bar appears on all VistAMigrate pages and displays your progress through the data migration steps. See Section 4.2.2 Navigation Bar for more information.
- Overview text appears in the main panel of the Welcome page providing an overview of the data migration steps. This area of the page will display logs and reports as you move through the migration steps. See Section 4.2.3 Description of Steps for more information.

> ![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/004.png)

> Figure 4-3. VistAMigrate Welcome page

#### Banner

> The Banner at the top of each VistAMigrate page displays migration status information for the site that you are logged into. Status information is updated as you move through the data migration steps:

- User Name: The name of the user associated with the Access Code used to log in.
- Station: A code identifying the site/institution.
- Project: The name of the reengineered application to which you are migrating data.
- Extracted:
  - Main Records: Total number of patient funds accounts extracted from the VistA legacy database.
  - Total Records: Total number of data records in the extract file. This number includes records of all types (patient demographics, patient account information, income source information, transactions, remarks, suspense data, etc.). Each patient will have multiple data records in the extract file; the number of records is determined by the data for that patient.
- Staged: Total number of records moved using structure query language (SQL)\*Loader to the Oracle staging tables for analysis. The number of Main Records should match the number of Main Records extracted. The number of Total Records includes a header record and will, therefore, be one greater than the total number of records extracted.
- Converted: Total number of records converted and moved from the Oracle staging tables to the Oracle production tables. After you complete the data migration, this number may be less than the total number of Staged records because records with errors will have been removed.

#### Navigation Bar

> Use the navigation bar in the left panel to access the steps in the VistAMigrate data migration process. The steps must be performed in sequence from top to bottom. For example: You must perform the M Diagnostics step within the VistA Migrate application before you can perform the M Extract step, and the M Extract step before you can perform the Stage Data step. You can, however, start over at any point.

> Note: Selecting a step will not automatically run that step. You need to click the Run button for that step to run it.

> Selecting a step that has already been run will display the report for the previous run and give you the option to re-run that step.

#### Starting Over

> The steps of the data migration process are iterative. Repeat the steps as many times as necessary to make sure the data is clean for a successful migration. When you repeat a step, data that was previously reported is cleared. For example: If you repeat step 2 M Diagnostics, any data reported from previous routines in steps 3-7 will be cleared. Another way to clear data is to click the Start Over button on the Final Steps page. You can go to the Final Steps page and start over any time during the data migration process as long as the migration has not been finalized.

> The steps on the navigation bar are color coded as follows:

- Green: Indicates that no action is required. The Welcome step is always green.
- Blue: Indicates that the task is enabled and available for use.
- Yellow: During processing, yellow swirls in the blue circle on the navigation bar indicating that the system is working on the task. When the system is done, the navigation circle becomes solid yellow until you complete the step.
- Gray: Indicates that the task is disabled until predecessor actions are performed.
- Red: Indicates that an error was returned and displayed. You cannot go on to the next step until the error is corrected.

#### Description of Steps

- Welcome: Read the overview provided on the VistAMigrate Welcome page.
- M Diagnostics: Perform this step to check data in the M environment for errors. Repeat this step each time you correct data.
- M Extract: Perform this step to extract your clean data from the M environment. Repeat this step each time you correct data.
- Stage Data: Perform this step to move extracted data to the staging database. Repeat this step each time you extract data.
- Analyze Data: Perform this step to run diagnostics on the data that you moved to the staging database to determine whether your data is clean enough to move to production. Repeat this step each time you stage data.
- Convert Data: Perform this step to move data from the staging database to the production database.
- Verify Data: Perform this step to run Oracle-side diagnostics to determine whether the data was migrated successfully into the production database.
- Final Steps: After you have determined whether the data was migrated successfully, use this step to do one of the following:
  - Start Over: If you determine that data was not migrated successfully, reset VistAMigrate and start the entire process over.
  - Finalize: Once you determine that data was migrated successfully, finalize the data migration.

> Note: This step will prevent any future data migration.

#### Process Running Indicator

> When you click the Run button to run a step in VistAMigrate, the process running indicator appears until the process is completed.

![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/005.png)

> Figure 4-4. Process Running Indicator

> To stop the process and reload the previous results, click the button on the right of the indicator.

### M Diagnostics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In this step you run the M diagnostic routine to check for errors in the data in the VistA legacy database.

> This step produces diagnostic reports that list errors based on the business rules in Appendix B. As previously noted, this generates the same reports as the new VistA option released with patch PRPF\*3.0\*15. See Appendix D for sample reports.

> Use the diagnostic summary and detail reports that are produced by this routine:

- During data cleanup, to evaluate the state of a site’s data. The goal is that each time you run the report after data cleanup, the error count will change to reflect the error correction.
- After data cleanup, to determine whether the data can be successfully migrated and cutover can take place.

> Important: M Diagnostics does not modify data; it is a reporting tool only.

> Any changes to be made for data cleanup must be made to the data in VistA. Refer to the Minimum Requirements to Migrate listed in the business rules for the criteria each field must meet to successfully migrate. The business rules are located in Appendix B in this document, or in the PRPF Data Diagnostic Patch User Guide that accompanies patch PRPF\*3.0\*15.

> To run M Diagnostics:

1.  In the navigation bar in the left panel, click 2 M Diagnostics. The M Diagnostics page opens.
    - If Run Diagnostics has *not* been run on this site before or if you are starting over, no reports will be shown.
    - ![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/006.png)If Run Diagnostics has been run on this site before, the most current diagnostic reports are shown from a previous or the current VistAMigrate session.

> Figure 4-5. M Diagnostics page

2.  Click the Run Diagnostics button.

> The M diagnostic routines run. Once complete, the Summary and Detail tabs appear on the page with the Patient Funds Diagnostic Summary Report displayed.

> ![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/007.png)

> Figure 4-6. M Diagnostics Page with Sample Diagnostic Summary Report

3.  Do the following:
    - Review the Diagnostic Summary Report. This report shows counts for each of the error conditions identified.
    - Click the Detail tab to review the Detail report. This report shows selected data for each record containing an error.
    - Optional: Click Download Reports to download a zip file containing both reports. Save the file to an appropriate location, naming it so that it is identifiable as a Diagnostic Summary and Detail report.

> Note: These reports are UNIX-formatted text files. They will not appear correctly in NotePad. Use WordPad or another application such as Excel that can display UNIX-formatted text correctly.

> Before you print the reports, change the page orientation to landscape.

> ![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/008.png)

> Figure 4-7. M Diagnostics Page with Detail Report

### M Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In this step you execute the M Extract routine that extracts a copy of the data to be migrated from the VistA legacy environment to an extract file that will be used by the Stage Data step.

> The report for this step shows the contents of this extract file exactly as it was transferred from VistA. In most cases you would only need to review this report to validate specific data values after completing the migration process, or to determine the cause of an error found during migration.

> Important: M Extract does not modify data.

> To run M Extract:

1.  In the navigation bar in the left panel, click 3 M Extract. The M Extract page opens.
    - If M Extract has *not* been run on this site before or if you started over, no data will be shown.
    - If M Extract has been run on this site before, the most current data are shown from a previous or the current VistAMigrate session.

> ![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/009.png)

> Figure 4-8. M Extract Page

2.  Click Run Extract.

> The M extract routines run. Once complete, the extract results appear on the page.

> Use the vertical scroll bar to view the full list of results on the page. If a large amount of data has been extracted, there may be left and right arrows at the bottom of the page you can use to move through the pages of data (use the right arrow to go to the next page of data, or the left arrow to go to the previous page).

> ![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/010.png)

> Figure 4-9. M Extract Page with Extract Results

3.  Do the following:
    - Review the Extract results.

> The fields in the Extract report are delimited by the circumflex character (^). If a record has null values in the field(s) at the end of the record, the ^ is not necessarily repeated. For a sample of this report, see Appendix D.

- Optional: Click Download Reports to download a zip file containing the report. Save the file to an appropriate location, naming it so that it is identifiable as an Extracts report.

> Note: This report is a UNIX-formatted text file. It will not appear correctly in NotePad. Use WordPad or another application such as Excel that can display UNIX-formatted text correctly.

> Before you print the report, change the page orientation to landscape.

### Stage Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In the Stage Data step, you execute the Run Data Staging process, which uses Oracle SQL\*Loader to read the data from the file generated by the M Extract routine and load the data into temporary (staging) tables in the Oracle database. These tables correspond to the record types in the extract file. No records are excluded by validation requirements at this point, since the aim is to bring all of the data into the Oracle environment for analysis.

> Run Data Staging generates two files that appear on the Stage Data page:

- The Log file: SQL\*Loader generates this file, which lists the number of records that loaded or failed to load in each table, including the conditions applied to each. This is a critical step in the verification of the migration as it ensures that no records are lost.
- The Bad file: SQL\*Loader generates this file if any records were rejected from the load because they contained errors. These errors may be caused by data that is too long for a particular field, or data that contains control characters (such as new line, etc.). Do not edit the extract file to try to fix any rejected records! Instead, site owners must correct the data in PFOP and repeat the data migration process.

> To move migrated data to the staging tables:

1.  In the navigation bar in the left panel, click 4 Stage Data. The Stage Data page opens.
    - If Stage Data has *not* been run on this site before or if you started over, no data will be shown.
    - If Stage Data has been run on this site before, the most current data are shown from a previous or the current VistAMigrate session.

> ![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/011.png)

> Figure 4-10. Stage Data page

2.  Click Run Data Staging.

> The Stage Data routines run. Once complete, the Log tab and log file appear. If any records with errors were present, the Bad tab also appears.

> ![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/012.png)

> Figure 4-11. Stage Data Page with Log File

3.  Do the following:
- Review the Stage Data Log file.
  - The first part of this report shows a list of all the staging tables, including the column names, position, maximum length and data type.
  - Following this is a list of records that were rejected or discarded from the staging tables, along with an explanation of the error that caused the record to be rejected. If any records were rejected, those records need to be reviewed and the reason they were rejected should be understood. You may need to look at the Extract report, or back in the VistA files.
  - Rejected records are typically caused by a particular piece of data exceeding the maximum length for that field.
  - Discarded records are those that do not fit the record format for any of the known record types. This is typically caused by a line-feed or other control character in the data.
  - Next, the report shows a table-by-table summary of how many rows were loaded or rejected from each table.
  - At the bottom of the log, there are 4 lines summarizing the total logical records skipped, read, rejected, or discarded. Rows not loaded due to data errors will be counted in the total records rejected.
- If the Bad tab is displayed, click the Bad tab to view the list of records containing errors. Information in this report can help you find the reason that records were rejected.
- Optional: Click Download Reports to download a zip file containing both of the reports.

> Note: These reports are UNIX-formatted text files. They will not appear correctly in NotePad. Use WordPad or another application such as Excel that can display UNIX-formatted text correctly.

> Before you print the reports, change the page orientation to landscape.

![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/013.png)

> Figure 4-12. Stage Data Page with Bad File Data

> For samples of these reports, see Appendix D.

### Analyze Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After you run Stage Data to load the extracted data into the temporary staging tables in the Oracle database, use the Analyze Data step to check the staged data to make sure it meets the Minimum Requirements to Migrate detailed in the business rules listed in Appendix B. This process produces a report listing each business rule and errors or warnings for any records violating that rule.

> To analyze the staged data:

1.  In the navigation bar in the left panel, click 5 Analyze Data. The Analyze Data page opens.
    - If Analyze Data has *not* been run on this site before or if you started over, no data will be shown.
    - If Analyze Data has been run on this site before, the most current data are shown from a previous or the current VistAMigrate session.

> ![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/014.png)

> Figure 4-13. Analyze Data Page

2.  Click Run Data Analysis.

> The Data Analysis routines run. Once completed, the Log tab and VPFS – Analyze Report appear.

> ![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/015.png)

> Figure 4-14. Analyze Data Page with VPFS – Analyze Report

3.  Do the following:
    - Review the Analyze Report.
      - Each section of this report checks a different data validation criteria or business rule. The report will display both error and warning conditions. Errors will prevent a patient from being migrated, warnings are informational. If there are any records listed for a given item, those records need to be reviewed and the reason they appear in the report should be understood. Refer to the business rules in Appendix B for a description of each item. This report can also be compared against the M Diagnostics reports that were generated in the first step of the migration.
      - At the end of the report are some informational sections providing a higher level view of the data being migrated. Compare the Total Account Balance (under Total for All Accounts) against the Total balance of accounts for migration line at the top of the M Diagnostic Summary. Also compare the number of deferred transactions (under Total for All Accounts) against the number of deferred transactions (line item 46) in the Diagnostic Summary. These values should be equal.
    - Optional: Click Download Reports to download a zip file containing the report.

> Note: This report is a UNIX-formatted text file. It will not appear correctly in NotePad. Use WordPad or another application such as Excel that can display UNIX-formatted text correctly.

> Before you print the report, change the page orientation to landscape.

> For a sample of the Analyze Data report, see Appendix D.

### Convert Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This step populates the Oracle production tables with converted data from the temporary staging tables. The conversion procedure will format the data as needed by VPFS, converting VistA dates to Oracle dates, assigning default values to replace blanks, etc., according to the business rules listed in Appendix

> B. After you are satisfied that there are no errors in the Oracle staging environment, use the Convert Data step to move the data to the Oracle production environment.

> Important: Any patients identified as having data with errors during the Analyze Data step will be removed from the staging tables and will not be migrated during the Convert Data routine or appear in the Convert Data log. A file containing the extracted data records for the rejected patients will be available after you run this step. Be sure to use the Download Reports option to save a copy of this log at that time.

> To move data to the Oracle production environment:

1.  In the navigation bar in the left panel, click 6 Convert Data. The Convert Data page opens.
    - If Convert Data has *not* been run on this site before or if you started over, no data will be shown.
    - If Convert Data has been run on this site before, the most current data are shown from a previous or the current VistAMigrate session.

![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/016.png)

> Figure 4-15. Convert Data Page

2.  Click Run Data Conversion.

> The Data Conversion routines run. Once complete, the Results tab and Results file appear. If any records with errors were present, the Errors tab also appears.

> ![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/017.png)

> Figure 4-16. Convert Data Page with Results

3.  Do the following:
    - Review the Convert Data Results.

> This shows a “progress report” as each type of data is processed. Verify that each process completed successfully. If any process failed, the Errors tab will contain a technical description of any errors. Contact the EMC technical representative.

- If the Errors tab is displayed, click the Errors tab to view the list of records containing errors.
- Optional: Click Download Reports to download a zip file containing the reports and the file containing the patient records that had errors during the Analyze Step.

> Note: These reports are UNIX-formatted text files. They will not appear correctly in NotePad. Use WordPad or another application such as Excel that can display UNIX-formatted text correctly.

> Before you print the reports, change the page orientation to landscape.

> ![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/018.png)

> Figure 4-17. Convert Data Page with Errors

> The Errors report displays each error and identifies the procedure in which it occurred. For samples of the Convert Data reports, see Appendix D.

### Verify Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This step executes a script that checks the migrated production data for a variety of potential migration and conversion errors. The log that is produced by this step provides all of the following data:

- Non-migrated patient account list • Migrated totals check
- Patient account list • Income source check
- Inactive accounts with non-zero balances • Remarks count check
- Transactions list • Non-converted special remarks list
- Deferred transactions list • Non-converted general remarks list
- Account balances check

> To verify data in the Oracle production environment:

1.  In the navigation bar in the left panel, click 7 Verify Data. The Verify Data page opens.
    - If Verify Data has *not* been run on this site before or if you started over, no data will be shown.
    - If Verify Data has been run on this site before, the most current data are shown from a previous or the current VistAMigrate session.

> ![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/019.png)

> Figure 4-18. Verify Data Page

2.  Click Run Data Verification.

> The Data Verification routines run. Once complete, the Log tab and Log file appear.

![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/020.png)

> Figure 4-19. Verify Data Page with Log

3.  Do the following:
    - Review the Verify Report. This report is intended to allow you to verify that the patient data was migrated as expected.
      - The list of patients that were not migrated is shown in the Non-migrated Patient Account List section. This list should match the Patient Accounts with Errors section of the Analyze report.
      - The list of patients that migrated successfully is shown in the Patient Account List section.
      - Compare the Total of Account Balances, Number of Deferred Transactions, and Total of Deferred Amounts in the Migrated Totals Check section against the values in the Total for Migrated Accounts section in the Analyze report.
    - Optional: Click Download Reports to download a zip file containing the report.

> Note: This report is a UNIX-formatted text file. It will not appear correctly in NotePad. Use WordPad or another application such as Excel that can display UNIX-formatted text correctly.

> Before you print the report, change the page orientation to landscape.

> For samples of the VPFS Verify Data Report produced by Verify Data, see Appendix D.

### Final Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This step provides two options:

- Finalize: Choose the Finalize option only if you are ready for final cutover.
- Start Over: Choose the Start Over option if you need to clear all previous runs and start the VistAMigrate data migration process over with M Diagnostics.

> Prior to choosing Finalize, re-run the M Diagnostic reports from the VistA legacy application. Compare the M Diagnostic reports from before and after the migration process to verify that additional deferred transactions have not been created in PFOP during the migration process and that data has not been corrupted during the conversion. Some of the data values may not be identical. Analyze any discrepancies and verify that the changes are due to documented business rules. See Appendix B for business rules.

> To perform the final steps:

1.  In the navigation bar in the left panel, click 8 Final Steps. The Final Steps page opens.

> ![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/021.png)

> Figure 4-20. Final Steps Page

#### Finalizing Data Migration

> To finalize data migration and cut over to VPFS:

> Caution: You will no longer be able to run/re-run migration if you choose the Finalize option!

- Click Finalize.

> The Finalize routines run. When complete:

- A message is displayed indicating that the data migration is finalized.
- The reengineered application is available for your site to register patients and manage accounts.
- VistAMigrate routines are disabled for this institution. The circles for the steps in the navigation bar become green. You will be able to access the step pages, to view and download the final reports.
- Contact your local IRM staff to install Patch 17. Data entry in the VistA legacy application is disabled for this institution. Legacy data is available for viewing and reporting only.

> Note: When a site has finalized the migration in step 8 of the data migration process, VistAMigrate will disallow any further migrations of PFOP data into VPFS for that site. At this point, the PRPF_DATA_MIGRATION_USERS security key should be removed

> from the legacy VistA accounts for all users at that site to disable user access to VistAMigrate.

- Click Download Reports. This will download a zip file containing all reports and files generated during the migration process.

> Note: These files are UNIX-formatted text files. They will not appear correctly in NotePad. Use WordPad or another application such as Excel that can display UNIX-formatted text correctly.

#### Resetting VistAMigrate to Start Over

> To clear all previous data migration runs for this institution and start over:

> Important! Be sure to click Download Reports to download a zip file containing all reports and files generated during the migration process.

> Note: These files are UNIX-formatted text files. They will not appear correctly in NotePad. Use WordPad or another application such as Excel that can display UNIX-formatted text correctly.

- Click Start Over.

> The Start Over routines run. The system clears any data from prior runs, including files and database data, and resets the counts.

#### <u>Appendix A. Frequently Asked Questions</u>

# Appendix A. Frequently Asked Questions


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Veterans Personal Finance System (VPFS)](#veterans-personal-finance-system-vpfs)
  - [About This Document](#about-this-document)
    - [Document Purpose](#document-purpose)
    - [Document Audience](#document-audience)
    - [Conventions Used in this Document](#conventions-used-in-this-document)
    - [Additional Resources](#additional-resources)
  - [Overview of VistAMigrate](#overview-of-vistamigrate)
  - [Preparing to Migrate Data from PFOP to VPFS](#preparing-to-migrate-data-from-pfop-to-vpfs)
    - [Overview](#overview)
    - [Flow of Data through VistAMigrate](#flow-of-data-through-vistamigrate)
    - [Groups/Roles in Data Migration](#groupsroles-in-data-migration)
    - [Preparation Checklist](#preparation-checklist)
    - [Patient Funds Data Migration Process](#patient-funds-data-migration-process)
    - [Data Migration Task Assignments](#data-migration-task-assignments)
    - [Overview of Steps in the M Environment](#overview-of-steps-in-the-m-environment)
    - [Overview of Steps in Reengineered Environment](#overview-of-steps-in-reengineered-environment)
    - [Data Migration Success Criteria](#data-migration-success-criteria)
  - [Performing Diagnostics and Data Cleanup in the M Environment](#performing-diagnostics-and-data-cleanup-in-the-m-environment)
    - [Patient Funds Diagnostic Summary Report](#patient-funds-diagnostic-summary-report)
    - [Patient Funds Diagnostic Detail Report](#patient-funds-diagnostic-detail-report)
    - [Correcting Patient Funds Errors](#correcting-patient-funds-errors)
  - [Migrating Data Using VistAMigrate](#migrating-data-using-vistamigrate)
    - [Accessing VistAMigrate](#accessing-vistamigrate)
    - [VistAMigrate Welcome Page](#vistamigrate-welcome-page)
    - [M Diagnostics](#m-diagnostics)
    - [M Extract](#m-extract)
    - [Stage Data](#stage-data)
    - [Analyze Data](#analyze-data)
    - [Convert Data](#convert-data)
    - [Verify Data](#verify-data)
    - [Final Steps](#final-steps)
- [Appendix A. Frequently Asked Questions](#appendix-a-frequently-asked-questions)
- [Appendix B. Migration Business Rules](#appendix-b-migration-business-rules)
    - [Migration Business Rules](#migration-business-rules)
- [Appendix C. Extraction File Layouts](#appendix-c-extraction-file-layouts)
    - [PFOP Extraction File Layout, VPFS Mapping](#pfop-extraction-file-layout-vpfs-mapping)
- [Appendix D. VistAMigrate Report Samples](#appendix-d-vistamigrate-report-samples)
    - [Diagnostic Summary Report](#diagnostic-summary-report)
    - [M Extract Results](#m-extract-results)
    - [Stage Data Log File](#stage-data-log-file)
    - [Analyze Report](#analyze-report)
    - [Convert Data Results](#convert-data-results)
    - [Verify Report](#verify-report)
- [Appendix E. Acronyms and Abbreviations](#appendix-e-acronyms-and-abbreviations)
> The following table provides answers to the most frequently asked questions about data migration.
> Table A-1. Frequently Asked Questions
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Question</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Answer</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Will I be able to use the VistA legacy application after cutover?</p>
</blockquote></td>
<td><blockquote>
<p>After cutover, the VistA legacy application will be available for viewing data and running reports, but data entry will be disabled.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>What happens to the legacy data if the migration fails at cutover?</p>
</blockquote></td>
<td><blockquote>
<p>If the actual migration <em>cutover</em> fails, the VistA legacy application will be turned back on with all of its current functionality.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>If we use the reengineered application for a while and then something goes wrong, can we go back to the legacy application?</p>
</blockquote></td>
<td><blockquote>
<p>No. Once you start using the reengineered application, the legacy data becomes out of sync with the new data. Moving between the two systems would make reconciliation of data difficult.</p>
<p>You may be asked to perform functions manually while the problem is being fixed and tested. Once the reengineered application is made available to you again, you will need to enter your manual records into the system.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>How will we regain the data we entered in the reengineered application in the event of a failure?</p>
</blockquote></td>
<td><blockquote>
<p>The database will be backed up on a nightly basis. If either the database or the application goes down, the last database backup can be restored and the data extracted.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>After cutover, will dual / parallel systems be run until it is determined that the reengineered application is stable?</p>
</blockquote></td>
<td><blockquote>
<p>No. However, the reengineered application will be closely monitored through several business cycles (e.g. reconciliations) to determine that it is stable.</p>
<p>It is recommended that you print reports frequently so that you can track the data you have entered.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>How should I report defects I discover during field testing?</p>
</blockquote></td>
<td><blockquote>
<p>Remedy will be used in field testing and reported to the VPFS team and tracked also in ClearQuest. A process is being developed which will be followed.</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>What support is provided during field testing?</p>
</blockquote></th>
<th><blockquote>
<p>During field testing, the Rapid Response Team will provide help during business hours nationwide.</p>
<p>Plans for support of the production system after cutover are TBD.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>What are the criteria for deciding to go ahead in production?</p>
</blockquote></td>
<td><blockquote>
<p>See Section 2.9 Data Migration Success Criteria.</p>
</blockquote></td>
</tr>
</tbody>
</table>
> Appendix B.
> This page is intentionally left blank.

# Appendix B. Migration Business Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The table in this appendix is intended for users who are ready to attempt to migrate their data to the reengineered environment. It lists the minimum requirements that each data element must meet for a record to be migrated to the new database.

> Unless otherwise stated, blank values are allowed.

> Note: The diagnostic routine that you run via the new menu option Database Diagnostic Report \[PRPF DATA DIAGNOSTIC REPORT\] and in VistAMigrate will identify invalid or missing data. Data not meeting the Minimum Requirements to Migrate in the table below needs to be corrected because records not meeting these requirements will *not* be migrated to VPFS.

### Migration Business Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Table B-1. Migration Business Rules

<table style="width:100%;">
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>PFOP / M Diagnostic Business Rule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Business Rule (Minimum Requirements to Migrate)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>NAME, #.01</p>
</blockquote></td>
<td><blockquote>
<p>Patient name cannot be blank.</p>
</blockquote></td>
<td><blockquote>
<p>Patient name cannot be blank.</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to File 2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>NAME, #.01</p>
</blockquote></td>
<td><blockquote>
<p>Patient name cannot contain values other than alpha characters, one comma, apostrophe, and space after first name. Must be 3-30 characters,</p>
</blockquote></td>
<td><blockquote>
<p>Patient name must be 3-30 characters.</p>
</blockquote></td>
<td><blockquote>
<p>Some names being migrated will contain data that is considered invalid now (special characters) but was valid in the past.</p>
<p>Pointer to File 2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>SSN, #50</p>
</blockquote></td>
<td><blockquote>
<p>SSN cannot be blank.</p>
</blockquote></td>
<td><blockquote>
<p>SSN cannot be blank.</p>
</blockquote></td>
<td><blockquote>
<p>Computed from File 2, #.09</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>SSN, #50</p>
</blockquote></td>
<td><blockquote>
<p>SSN must be 9 digits.</p>
</blockquote></td>
<td><blockquote>
<p>SSN must be 9 digits or 9 digits followed by a ‘P’ to allow for pseudo-SSN.</p>
</blockquote></td>
<td><blockquote>
<p>Allow ‘P’ as an optional 10th character for pseudo-SSN. Computed from File 2, #.09</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>PFOP / M Diagnostic Business Rule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Business Rule (Minimum Requirements to Migrate)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>SSN, #50</p>
</blockquote></td>
<td><blockquote>
<p>SSN cannot be a duplicate.</p>
</blockquote></td>
<td><blockquote>
<p>SSN cannot be a duplicate at <em>any</em></p>
<p>station.</p>
</blockquote></td>
<td><blockquote>
<p>Computed from File 2, #.09</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>SSN, #50</p>
</blockquote></td>
<td><blockquote>
<p>SSN contains pseudo SSN value.</p>
</blockquote></td>
<td><blockquote>
<p>Not an error; pseudo-SSN values are allowed.</p>
</blockquote></td>
<td><blockquote>
<p>Computed from File 2, #.09</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>DOB, #51</p>
</blockquote></td>
<td><blockquote>
<p>DOB cannot be blank.</p>
</blockquote></td>
<td><blockquote>
<p>DOB cannot be blank.</p>
</blockquote></td>
<td><blockquote>
<p>Computed from File 2, #.03</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>DOB, #51</p>
</blockquote></td>
<td><blockquote>
<p>DOB must be a valid VistA date.</p>
</blockquote></td>
<td><blockquote>
<p>DOB must be 7 digits, in VistA date format.</p>
<p>Imprecise dates will be defaulted to the first of the month or year during migration.</p>
</blockquote></td>
<td><blockquote>
<p>Imprecise dates having a ‘00’ for the month and/or day will be defaulted to ‘01’.</p>
<p>Computed from File 2, #.03</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>WARD, #52</p>
</blockquote></td>
<td><blockquote>
<p>Ward must be 2-30 characters.</p>
</blockquote></td>
<td><blockquote>
<p>Ward must be 2-30 characters.</p>
</blockquote></td>
<td><blockquote>
<p>Computed from File 2, #.1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>CLAIM NUMBER, #53</p>
</blockquote></td>
<td><blockquote>
<p>Claim Number must be ‘SS’ or 7-9 digits.</p>
</blockquote></td>
<td><blockquote>
<p>Claim Number must be 'SS' or 7-9 digits.</p>
</blockquote></td>
<td><blockquote>
<p>Computed from File 2, #.313</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>ZIP CODE, #59</p>
</blockquote></td>
<td><blockquote>
<p>ZIP Code must be 5 digits.</p>
</blockquote></td>
<td><blockquote>
<p>Not migrated.</p>
</blockquote></td>
<td><blockquote>
<p>Computed from File 2, #.116</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12</td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>REGIONAL OFFICE, #8</p>
</blockquote></td>
<td><blockquote>
<p>NA</p>
</blockquote></td>
<td><blockquote>
<p>Not migrated.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>13</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>INTEGRATION CONTROL NUMBER (ICN), #991.01</p>
</blockquote></td>
<td><blockquote>
<p>ICN cannot be a duplicate.</p>
</blockquote></td>
<td><blockquote>
<p>ICN cannot be duplicate at <em>any</em></p>
<p>station.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>14</p>
</blockquote></th>
<th><blockquote>
<p>2</p>
</blockquote></th>
<th><blockquote>
<p>ICN, #991.01</p>
</blockquote></th>
<th><blockquote>
<p>ICN must be at least 1 character.</p>
</blockquote></th>
<th><blockquote>
<p>ICN must be 1-10 digits, optionally followed by a ‘V’ and a 6 digit checksum. An additional 6 digit prefix and 6 digit suffix are allowed for future use.</p>
</blockquote></th>
<th><blockquote>
<p>Allows current ICN format (10V6), with or without the checksum, and future ICN format (16V12).</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>PFOP / M Diagnostic Business Rule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Business Rule (Minimum Requirements to Migrate)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>PROVIDER AUTH RESTRICT, #10.7</p>
</blockquote></td>
<td><blockquote>
<p>Provider Name cannot contain values other than alpha characters, one comma, apostrophe, and space. (Must meet VistA standard naming requirements.)</p>
</blockquote></td>
<td><blockquote>
<p>Provider Name must be 3-30 characters.</p>
</blockquote></td>
<td><blockquote>
<p>M Diagnostic Summary: item only validates name if present. This field can be blank. It is not associated with item #20 and will not increment the report counter if an error is registered on item #20.</p>
<p>Pointer to File 200 source.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>DATE OF CURRENT RESTRICTION, #10.5</p>
</blockquote></td>
<td><blockquote>
<p>Date of Current Restriction must be a valid VistA date.</p>
</blockquote></td>
<td><blockquote>
<p>Date of Current Restriction must be 7 digits in VistA date format.</p>
<p>Imprecise dates are not allowed. Cannot be blank if patient type is restricted (R) or limited unrestricted</p>
<p>(L).</p>
</blockquote></td>
<td><blockquote>
<p>Month or day cannot be 00.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>17</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Demographic record</p>
</blockquote></td>
<td><blockquote>
<p>Missing demographic record for account. Record must be present.</p>
</blockquote></td>
<td><blockquote>
<p>Demographic record must exist for account.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>18</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>ACCOUNT STATUS, #1</p>
</blockquote></td>
<td><blockquote>
<p>Account Status must be A, I or blank.</p>
</blockquote></td>
<td><blockquote>
<p>Account Status must be A, I, or blank. Blanks will be defaulted to A during migration.</p>
</blockquote></td>
<td><blockquote>
<p>A nightly update process will set active/inactive: if zero balance &amp; no transactions for 30+ days, set to I.</p>
<p>The number of blank entries will be displayed in the M Diagnostic Summary and Analyze Report.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>19</p>
</blockquote></th>
<th><blockquote>
<p>470</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT TYPE, #2</p>
</blockquote></th>
<th><blockquote>
<p>Patient Type must be L, R, U, X or blank.</p>
</blockquote></th>
<th><blockquote>
<p>Patient Type must be L, R, U, X, or blank. Blanks will be defaulted to U during migration.</p>
</blockquote></th>
<th><blockquote>
<p>The number of blank entries will be displayed in the M Diagnostic Summary and Analyze Report.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>PROVIDER AUTH RESTRICT, #10.7</p>
</blockquote></td>
<td><blockquote>
<p>Provider Name cannot be blank if the Patient Type is restricted or limited unrestricted.</p>
</blockquote></td>
<td><blockquote>
<p>Provider Name cannot be blank if the Patient Type is restricted (R) or limited unrestricted (L).</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>PFOP / M Diagnostic Business Rule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Business Rule (Minimum Requirements to Migrate)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>21</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT STATUS, #3</p>
</blockquote></td>
<td><blockquote>
<p>Patient Status must be A, R, C, N, X or blank.</p>
</blockquote></td>
<td><blockquote>
<p>Patient Status must be A, R, C, N, X, or blank. Blanks will be defaulted to X during migration.</p>
</blockquote></td>
<td><blockquote>
<p>The number of blank entries will be displayed in the M Diagnostic Summary and Analyze Report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>INDIGENT, #4</p>
</blockquote></td>
<td><blockquote>
<p>Indigent indicator must be Y, N or blank.</p>
</blockquote></td>
<td><blockquote>
<p>Indigent must be Y, N, or blank. Blanks will be defaulted to N during migration.</p>
</blockquote></td>
<td><blockquote>
<p>The number of blank entries will be displayed in the M Diagnostic Summary and Analyze Report.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>23</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>APPORTIONEE $, #5</p>
</blockquote></td>
<td><blockquote>
<p>Apportionee $ cannot be less than 0 or greater than 99,999.00.</p>
</blockquote></td>
<td><blockquote>
<p>Apportionee $ must be a number greater than or equal to 0, or blank. A warning will be displayed if value is greater than 99,999.</p>
</blockquote></td>
<td><blockquote>
<p>Populates income source type and amount during conversion.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>24</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>GUARDIAN $, #6</p>
</blockquote></td>
<td><blockquote>
<p>Guardian $ cannot be less than 0 or greater than 99,999.00.</p>
</blockquote></td>
<td><blockquote>
<p>Guardian $ must be a number greater than or equal to 0, or blank. A warning will be displayed if value is greater than 99,999.</p>
</blockquote></td>
<td><blockquote>
<p>Populates income source type and amount during conversion.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>25</p>
</blockquote></th>
<th><blockquote>
<p>470</p>
</blockquote></th>
<th><blockquote>
<p>INSTITUTION AWARD, #7</p>
</blockquote></th>
<th><blockquote>
<p>Institutional Award $ cannot be less than 0 or greater than 99,999.00.</p>
</blockquote></th>
<th><blockquote>
<p>Institutional Award $ must be a number greater than or equal to 0, or blank.</p>
<p>A warning will be displayed if value is greater than 99,999.</p>
</blockquote></th>
<th><blockquote>
<p>Populates income source type and amount during conversion.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>OTHER ASSETS, #9</p>
</blockquote></td>
<td><blockquote>
<p>Other Assets $ cannot be less than 0 or greater than 99,999.00.</p>
</blockquote></td>
<td><blockquote>
<p>Other Assets $ must be a number greater than or equal to 0, or blank. A warning will be displayed if value is greater than 99,999.</p>
</blockquote></td>
<td><blockquote>
<p>Populates income source type and amount during conversion.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>PFOP / M Diagnostic Business Rule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Business Rule (Minimum Requirements to Migrate)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>27</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>STORED BALANCE, #14</p>
</blockquote></td>
<td><blockquote>
<p>Stored Balance cannot be less than 0 or greater than 99,999.</p>
</blockquote></td>
<td><blockquote>
<p>Stored Balance must be a number must be a number greater than or equal to 0, or blank. If blank, will default to 0.</p>
<p>A warning will be displayed if value is greater than 99,999.</p>
<p>Must equal sum of Stored Private Source Balance and Gratuitous Source Balance.</p>
</blockquote></td>
<td><blockquote>
<p>Blank value will default to 0.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>STORED PRIVATE SOURCE, #15</p>
</blockquote></td>
<td><blockquote>
<p>Stored Private Source Balance cannot be less than 0 or greater than 99,999.</p>
</blockquote></td>
<td><blockquote>
<p>Stored Private Source Balance must be a number greater than or equal to 0, or blank. If blank, will default to 0.</p>
<p>A warning will be displayed if value is greater than 99,999.</p>
</blockquote></td>
<td><blockquote>
<p>Blank value will default to 0.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>29</p>
</blockquote></th>
<th><blockquote>
<p>470</p>
</blockquote></th>
<th><blockquote>
<p>STORED GRATUITOUS, #16</p>
</blockquote></th>
<th><blockquote>
<p>Stored Gratuitous Balance cannot be less than 0 or greater than 99,999.</p>
</blockquote></th>
<th><blockquote>
<p>Stored Gratuitous Balance must be a number greater than or equal to 0, or blank. If blank, will default to 0.</p>
<p>A warning will be displayed if value is greater than 99,999.</p>
</blockquote></th>
<th><blockquote>
<p>Blank value will default to 0.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>AMOUNT RESTRICTED PER MONTH, #17</p>
</blockquote></td>
<td><blockquote>
<p>Amount Restricted / Month cannot be less than 0 or greater than 99,999.</p>
</blockquote></td>
<td><blockquote>
<p>Amount Restricted / Month must be a number between 0 and 99,999.</p>
</blockquote></td>
<td><blockquote>
<p>Blank value means no restriction limit.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>31</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>AMOUNT RESTRICTED PER WEEK, #18</p>
</blockquote></td>
<td><blockquote>
<p>Amount Restricted / Week cannot be less than 0 or greater than 99,999.</p>
</blockquote></td>
<td><blockquote>
<p>Amount Restricted / Week must be a number between 0 and 99,999.</p>
</blockquote></td>
<td><blockquote>
<p>Blank value means no restriction limit.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>32</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>AMOUNT RESTRICTED PER MONTH / WEEK, #17, 18</p>
</blockquote></td>
<td><blockquote>
<p>Restricted Monthly Amount cannot be less than 5 times the Weekly Amount.</p>
</blockquote></td>
<td><blockquote>
<p>Display a warning if the Restricted Monthly Amount is less than 5 times the Weekly Amount.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>PFOP / M Diagnostic Business Rule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Business Rule (Minimum Requirements to Migrate)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>33</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>AMOUNT RESTRICTED PER MONTH / WEEK, #17, 18</p>
</blockquote></td>
<td><blockquote>
<p>Restricted Monthly Amount cannot be less than the Weekly Amount.</p>
</blockquote></td>
<td><blockquote>
<p>Restricted Monthly Amount cannot be less than the Weekly Amount.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>MONTHLY RESTRICTION BALANCE 1, #21</p>
</blockquote></td>
<td><blockquote>
<p>NA</p>
</blockquote></td>
<td><blockquote>
<p>Monthly Restricted Balance cannot be less than 0 or greater than 99,999.</p>
</blockquote></td>
<td><blockquote>
<p>Not checked in M Diagnostic.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>WEEKLY RESTRICTION BALANCE 1, #22</p>
</blockquote></td>
<td><blockquote>
<p>NA</p>
</blockquote></td>
<td><blockquote>
<p>Weekly Restricted Balance cannot be less than 0 or greater than 99,999.</p>
</blockquote></td>
<td><blockquote>
<p>Not checked in M Diagnostic.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>34</p>
</blockquote></th>
<th><blockquote>
<p>470</p>
</blockquote></th>
<th><blockquote>
<p>MINIMUM BALANCE #1;#23</p>
</blockquote></th>
<th><blockquote>
<p>Minimum Balance cannot be less than 0 or greater than 99,999.</p>
</blockquote></th>
<th><blockquote>
<p>Minimum Balance must be a number greater than or equal to 0, or blank.</p>
<p>A warning will be displayed if value is greater than 99,999.</p>
</blockquote></th>
<th><blockquote>
<p>Blank value means no minimum balance.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>35</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>MAXIMUM BALANCE #1, #24</p>
</blockquote></td>
<td><blockquote>
<p>Maximum Balance cannot be less than 0 or greater than 99,999</p>
</blockquote></td>
<td><blockquote>
<p>Maximum Balance must be a number greater than or equal to 0, or blank.</p>
<p>A warning will be displayed if value is greater than 99,999.</p>
</blockquote></td>
<td><blockquote>
<p>Blank value means no maximum balance.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>36</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>Balance record</p>
</blockquote></td>
<td><blockquote>
<p>Missing balance record for account. Record must be present.</p>
</blockquote></td>
<td><blockquote>
<p>Balance record must exist for account.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>37</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>PAYEE, #1 of SubFile INCOME SOURCE #470.05</p>
</blockquote></td>
<td><blockquote>
<p>Income source Payee cannot be blank.</p>
</blockquote></td>
<td><blockquote>
<p>Income source Payee cannot be blank.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>38</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>AMOUNT, #2 of</p>
<p>SubFIle INCOME SOURCE, #470.05</p>
</blockquote></td>
<td><blockquote>
<p>Income source Amount cannot be blank.</p>
</blockquote></td>
<td><blockquote>
<p>Income source Amount cannot be blank.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>PFOP / M Diagnostic Business Rule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Business Rule (Minimum Requirements to Migrate)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>39</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>AMOUNT, #2 of</p>
<p>SubFIle INCOME SOURCE, #470.05</p>
</blockquote></td>
<td><blockquote>
<p>Income Amount cannot be less than 1 or greater than 99,999.00.</p>
</blockquote></td>
<td><blockquote>
<p>Income Amount must be a number greater than or equal to 0.</p>
<p>A warning will be displayed if value is greater than 99,999.</p>
</blockquote></td>
<td><blockquote>
<p>PFOP does not allow values less than 1 but checks for values less than 1 are possible.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>40</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>FREQUENCY, #3 of</p>
<p>SubFile INCOME SOURCE, #470.05</p>
</blockquote></td>
<td><blockquote>
<p>Income source Frequency must be D, W, M, Y, X, V, O or blank.</p>
</blockquote></td>
<td><blockquote>
<p>Income source Frequency must be D, W, M, Y, X, V, O or blank.</p>
</blockquote></td>
<td><blockquote>
<p>M Diagnostic Summary: The number of blank entries will be displayed in the summary.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>41</p>
</blockquote></th>
<th><blockquote>
<p>470</p>
</blockquote></th>
<th><blockquote>
<p>STATION NAME, #73</p>
</blockquote></th>
<th><blockquote>
<p>Station ID cannot be blank or unassigned.</p>
</blockquote></th>
<th><blockquote>
<p>Station ID must be a valid station ID*.</p>
</blockquote></th>
<th><blockquote>
<p>* If blank, parent station ID will be inserted as the default station ID during migration. M Diagnostic: Although the Summary Report does count these errors, they are not displayed in the Detail Report to save space.</p>
<p>Pointer to File 4.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>42</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>STATION NAME, #73</p>
</blockquote></td>
<td><blockquote>
<p>Station ID must be valid. (Must exist in File 4, Institution table.)</p>
</blockquote></td>
<td><blockquote>
<p>Station ID must be a valid station ID*. Station ID must be the division ID being migrated or a child of that station.</p>
<p>(Must exist in the SDS Institution table.)</p>
</blockquote></td>
<td><blockquote>
<p>* If blank, parent station ID will be inserted as the default station ID during extraction.</p>
<p>Pointer to File 4.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL INFORMATION/ REMARKS, #34</p>
</blockquote></td>
<td><blockquote>
<p>NA</p>
</blockquote></td>
<td><blockquote>
<p>General Remarks cannot be more than 2000 characters.</p>
</blockquote></td>
<td><blockquote>
<p>Not checked by M Diagnostic A Description that is too long will be truncated to 2000 characters during migration.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>PFOP / M Diagnostic Business Rule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Business Rule (Minimum Requirements to Migrate)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>SPECIAL REMARKS, #35</p>
</blockquote></td>
<td><blockquote>
<p>NA</p>
</blockquote></td>
<td><blockquote>
<p>Special Remarks cannot be more than 2000 characters.</p>
</blockquote></td>
<td><blockquote>
<p>Not checked by M Diagnostic A Description that is too long will be truncated to 2000 characters during migration.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>43</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>SUSPENSE DATE,</p>
<p>#.01 of SubFile SUSPENSE DATE, #32</p>
</blockquote></td>
<td><blockquote>
<p>Suspense Date must be a valid VistA date.</p>
</blockquote></td>
<td><blockquote>
<p>Suspense Date must be 7 digits in VistA date format.</p>
<p>Imprecise dates are not allowed. Cannot be blank.</p>
</blockquote></td>
<td><blockquote>
<p>Detail report contains two types of errors reported: 43.1</p>
<p>- Suspense date is blank</p>
<p>43.2 - Suspense date is not valid</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>44</p>
</blockquote></th>
<th><blockquote>
<p>470</p>
</blockquote></th>
<th><blockquote>
<p>ITEM ID, #.01 of SubFile ID, #470.04,</p>
<p>of SubFile SUSPENSE DATE, #32</p>
</blockquote></th>
<th><blockquote>
<p>Suspense ID cannot be blank or more than 40 characters.</p>
</blockquote></th>
<th><blockquote>
<p>Suspense ID cannot be blank or more than 50 characters.</p>
</blockquote></th>
<th><blockquote>
<p>Detail report contains two types of errors reported:</p>
</blockquote>
<ol type="1">
<li><p>- Suspense ID is blank</p></li>
<li><blockquote>
<p>- Suspense ID &lt; 1 or &gt; 40 characters</p>
</blockquote></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>45</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>FULL DESCRIPTION,</p>
<p>#1, of SubFile ID, #470.04, of SubFile SUSPENSE DATE, #32</p>
</blockquote></td>
<td><blockquote>
<p>Suspense Text cannot be blank or more than 255 characters.</p>
</blockquote></td>
<td><blockquote>
<p>Suspense Text cannot be blank or more than 255 characters.</p>
</blockquote></td>
<td><blockquote>
<p>Detail report contains two types of errors reported:</p>
</blockquote>
<ol type="1">
<li><p>- Suspense description is blank</p></li>
<li><p>- Suspense description &lt; 1 or &gt; 255 characters</p></li>
</ol>
<blockquote>
<p>Maximum length cannot be verified in the Analyze Report. A Description that is too long will be truncated to 255 characters during migration.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>Invalid suspense item</p>
</blockquote></td>
<td><blockquote>
<p>NA</p>
</blockquote></td>
<td><blockquote>
<p>Cannot have a Suspense Item record (S2) without a corresponding Suspense Date record (S1).</p>
</blockquote></td>
<td><blockquote>
<p>Not checked by M Diagnostic. Verify the integrity of the suspense records in the extraction file.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>PFOP / M Diagnostic Business Rule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Business Rule (Minimum Requirements to Migrate)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>46</p>
</blockquote></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>DEFERRED CREDIT REF #, #31</p>
</blockquote></td>
<td><blockquote>
<p>Display a count of the deferred transactions.</p>
</blockquote></td>
<td><blockquote>
<p>NA</p>
</blockquote></td>
<td><blockquote>
<p>M Diagnostic Summary: Shows count of deferred transactions. Is not an error and does not display in the Detail Report.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>47</p>
</blockquote></th>
<th><blockquote>
<p>470.1</p>
</blockquote></th>
<th><blockquote>
<p>Transaction record</p>
</blockquote></th>
<th><blockquote>
<p>Missing transaction record or record is blank. Record must be present.</p>
<p>Deferred Credit Reference Number must match the Transaction ID.</p>
</blockquote></th>
<th><blockquote>
<p>NA</p>
</blockquote></th>
<th><blockquote>
<p>See comment below:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="6"><blockquote>
<p>47 - Comment</p>
<p>Master Transaction IDs should always be the same as the Deferred Credit Reference Number with an ‘M’ appended to the end. The ‘M’ is stripped off when doing this check.</p>
<p>Important Note: If you find that there are deferred transactions that have Master Transaction IDs (.01 field of file 470.1) that do not match the Deferred Credit Reference number (the .01 field of an entry in file 470 field 31, which is also the IEN of file 470.1) this indicates:</p>
</blockquote>
<ol type="1">
<li><p>The Master transaction counter in file 470.3 is out of sync. This must be corrected or the counter will continue to be incorrect for all future transactions in Patient Funds. Each site has the following two options for resolving this matter:</p>
<ol type="a">
<li><p>Correct the transaction counter by contacting IRM to register a Remedy ticket. This is recommended so transactions will be in sync for future transactions.</p></li>
<li><p>Leave the transaction counter out of sync. This option is not recommended but is acceptable. If transactions are not corrected, transactions will be out of sync in VistA but will have no negative effect on VPFS data or the Patient Funds migration.</p></li>
</ol></li>
<li><p>Master Transaction IDs do not match the Deferred Credit Reference Numbers. Each site has the following three options for resolving this matter:</p>
<ol type="a">
<li><p>Let the deferred transaction clear or move up the deferred date so the transaction will clear sooner.</p></li>
<li><p>Correct the transactions that do not have a matching Master Transaction ID by contacting IRM to register a Remedy ticket. This is recommended so transactions in the past will be in sync.</p></li>
<li><p>Leave the transactions that do not have matching Master Transaction IDs unchanged. This option is not recommended but is acceptable. If transactions are not corrected transactions will be out of sync in VistA but this will have no negative effect on VPFS data or the Patient Funds migration.</p></li>
</ol></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>PFOP / M Diagnostic Business Rule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Business Rule (Minimum Requirements to Migrate)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>48</p>
</blockquote></td>
<td><blockquote>
<p>470.1</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT NAME, #1</p>
</blockquote></td>
<td><blockquote>
<p>Patient name must match the deferred transaction name.</p>
</blockquote></td>
<td><blockquote>
<p>NA</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to PATIENT FUNDS FILE, #470 which is a pointer to PATIENT FILE, #2</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>49</p>
</blockquote></th>
<th><blockquote>
<p>470.1</p>
</blockquote></th>
<th><blockquote>
<p>TRANSACTION ID, #.01</p>
</blockquote></th>
<th><blockquote>
<p>Transaction ID cannot be blank. Transaction ID must match the transaction ID for the patient account.</p>
</blockquote></th>
<th><blockquote>
<p>NA</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>50</p>
</blockquote></td>
<td><blockquote>
<p>470.1</p>
</blockquote></td>
<td><blockquote>
<p>AMOUNT, #3</p>
</blockquote></td>
<td><blockquote>
<p>Transaction Amount cannot be blank, less than .01 or greater than 99,999.</p>
</blockquote></td>
<td><blockquote>
<p>Transaction Amount must be a number between 0 and 99,999 and cannot be blank.</p>
<p>Must equal sum of Private Source Amount and Gratuitous Source Amount.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>470</p>
</blockquote></td>
<td><blockquote>
<p>LAST TRANSACTION DATE, #</p>
</blockquote></td>
<td><blockquote>
<p>NA</p>
</blockquote></td>
<td><blockquote>
<p>Last Transaction Date must be 7 digits, in VistA date format.</p>
<p>Imprecise dates are not allowed.</p>
</blockquote></td>
<td><blockquote>
<p>Not checked in M Diagnostic.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>470.1</p>
</blockquote></td>
<td><blockquote>
<p>DEFERRAL DATE, #19</p>
</blockquote></td>
<td><blockquote>
<p>NA</p>
</blockquote></td>
<td><blockquote>
<p>Deferral Date must be 7 digits, in VistA date format and cannot be blank. Imprecise dates are not allowed.</p>
</blockquote></td>
<td><blockquote>
<p>Not checked in M Diagnostic.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>51</p>
</blockquote></td>
<td><blockquote>
<p>470.1</p>
</blockquote></td>
<td><blockquote>
<p>TRANSACTION DATE, #4</p>
</blockquote></td>
<td><blockquote>
<p>Transaction Date must be a valid VistA date and cannot be blank.</p>
</blockquote></td>
<td><blockquote>
<p>Transaction Date must be 7 digits, in VistA date format and cannot be blank. Imprecise dates are not allowed.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>52</p>
</blockquote></td>
<td><blockquote>
<p>470.1</p>
</blockquote></td>
<td><blockquote>
<p>DATE TRANSACTION ENTERED, #5</p>
</blockquote></td>
<td><blockquote>
<p>Transaction Entered Date must be a valid VistA date and cannot be blank.</p>
</blockquote></td>
<td><blockquote>
<p>Transaction Entered Date must be 7 digits, in VistA date format and cannot be blank. Imprecise dates are not allowed.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>53</p>
</blockquote></td>
<td><blockquote>
<p>470.1</p>
</blockquote></td>
<td><blockquote>
<p>REFERENCE, #6</p>
</blockquote></td>
<td><blockquote>
<p>Reference must be 1-10 characters and cannot be blank.</p>
</blockquote></td>
<td><blockquote>
<p>Reference must be 1-10 characters and cannot be blank.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ID</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>PFOP / M Diagnostic Business Rule</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VPFS Business Rule (Minimum Requirements to Migrate)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comment</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>54</p>
</blockquote></th>
<th><blockquote>
<p>470.1</p>
</blockquote></th>
<th><blockquote>
<p>DEPOSIT/ WITHDRAWAL, #7</p>
</blockquote></th>
<th><blockquote>
<p>Deposit/Withdrawal field must be D or W and cannot be blank.</p>
</blockquote></th>
<th><blockquote>
<p>Deposit/Withdrawal field must be D or W and cannot be blank.</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>55</p>
</blockquote></td>
<td><blockquote>
<p>470.1</p>
</blockquote></td>
<td><blockquote>
<p>CASH/CHECK/ OTHER, #8</p>
</blockquote></td>
<td><blockquote>
<p>Cash/Check/Other field must be 1, 2, or 3 and cannot be blank.</p>
</blockquote></td>
<td><blockquote>
<p>Cash/Check/Other field must be 1, 2, or 3 and cannot be blank.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>56</p>
</blockquote></td>
<td><blockquote>
<p>470.1</p>
</blockquote></td>
<td><blockquote>
<p>SOURCE, #9</p>
</blockquote></td>
<td><blockquote>
<p>Transaction Income Source must be P, G, or B and cannot be blank.</p>
</blockquote></td>
<td><blockquote>
<p>Transaction Income Source must be P, G, or B and cannot be blank.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>57</p>
</blockquote></td>
<td><blockquote>
<p>470.1</p>
</blockquote></td>
<td><blockquote>
<p>FORM, #10</p>
</blockquote></td>
<td><blockquote>
<p>Form cannot be blank and must be a value in the standard Form list (user-maintained, in table).</p>
</blockquote></td>
<td><blockquote>
<p>Form cannot be blank.</p>
<p>Display warning if Form value is not in the standard Form list in VPFS.</p>
</blockquote></td>
<td><blockquote>
<p>Form is a pointer to File 470.2.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>58</p>
</blockquote></td>
<td><blockquote>
<p>470.1</p>
</blockquote></td>
<td><blockquote>
<p>PRIVATE SOURCE AMT, #11</p>
</blockquote></td>
<td><blockquote>
<p>Private Source Amount cannot be less than .01 or greater than 99,999 but can be blank.</p>
</blockquote></td>
<td><blockquote>
<p>Private Source Amount must be between 0 and 99,999.</p>
<p>Either the Private or Gratuitous Amount must <em>not</em> be blank.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>59</p>
</blockquote></td>
<td><blockquote>
<p>470.1</p>
</blockquote></td>
<td><blockquote>
<p>GRATUITOUS AMOUNT, #12</p>
</blockquote></td>
<td><blockquote>
<p>Gratuitous Source Amount cannot be less than .01 or greater than 99,999 but can be blank.</p>
</blockquote></td>
<td><blockquote>
<p>Gratuitous Amount must be between 0 and 99,999.</p>
<p>Either Private or Gratuitous Amount must <em>not</em> be blank.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>470.1</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT FUNDS CLERK, #13</p>
</blockquote></td>
<td><blockquote>
<p>Patient Funds Clerk cannot be blank and must exist in File 200.</p>
</blockquote></td>
<td><blockquote>
<p>Patient Funds Clerk must be 3-35 characters and cannot be blank.</p>
</blockquote></td>
<td><blockquote>
<p>Pointer to NEW PERSON FILE, #200</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Appendix C. Extraction File Layouts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PFOP Extraction File Layout, VPFS Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Table C-1. PFOP Extraction File Layout, VPFS Mapping

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 22%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="11"><blockquote>
<p><strong>PFOP EXTRACTION FILE LAYOUT - VPFS MAPPING</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>KEY</strong></p>
</blockquote></td>
<td><strong>:</strong></td>
<td><blockquote>
<p>A1 - header</p>
<p>D1 - demographics 1 D2 - demographics 2 B1 - balance 1</p>
<p>B2 - balance 2</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>T1 - transaction 1 S1 - suspense 1 S2 - suspense 2 S3 - suspense 3 I1 - income 1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>R1 - general remarks 1 R2 - general remarks 2 X1 - special remarks 1 X2 - special remarks 2</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p><strong>M Extr Field</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p><strong>V Table</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>V Field</strong></p>
</blockquote></td>
<td><blockquote>
<p>![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/022.png)</p>
</blockquote></td>
<td><blockquote>
<p><strong>Conversion Rules</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>A1</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>"VPFS"</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td><blockquote>
<p>Station ID</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td><blockquote>
<p>version and run date</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>4</td>
<td><blockquote>
<p>filler</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td><blockquote>
<p>filler</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>6</td>
<td><blockquote>
<p>rec #</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td><blockquote>
<p>“0”</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>7</td>
<td><blockquote>
<p>rec type</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td><blockquote>
<p>“A1”</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>8</td>
<td><blockquote>
<p># patient accounts processed</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>9</td>
<td><blockquote>
<p>total # recs in file</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th><blockquote>
<p>VistA job #</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>(internal VistAMigrat</p>
</blockquote></th>
<th><blockquote>
<p>use only)</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>D1</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>"VPFS"</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td><blockquote>
<p>Station ID</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>All records include S IEN, SSN, and ICN f</p>
</blockquote></td>
<td>tation ID, or inking.</td>
<td><blockquote>
<p>y</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td><blockquote>
<p>IEN</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>person</p>
</blockquote></td>
<td><blockquote>
<p>ien_id</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="12"><blockquote>
<p><strong>PFOP EXTRACTION FILE LAYOUT - VPFS MAPPING</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>KEY</strong></p>
</blockquote></td>
<td><strong>:</strong></td>
<td><blockquote>
<p>A1 - header</p>
<p>D1 - demographics 1 D2 - demographics 2 B1 - balance 1</p>
<p>B2 - balance 2</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>T1 - transaction 1 S1 - suspense 1 S2 - suspense 2 S3 - suspense 3 I1 - income 1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>R1 - general remarks 1 R2 - general remarks 2 X1 - special remarks 1 X2 - special remarks 2</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p><strong>M Extr Field</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p><strong>V Table</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>V Field</strong></p>
</blockquote></td>
<td><blockquote>
<p>![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/023.png)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p><strong>Conversion Rules</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>person</p>
</blockquote></td>
<td><blockquote>
<p>ssn_nbr</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td><blockquote>
<p>ICN</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>person</p>
</blockquote></td>
<td><blockquote>
<p>icn</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>6</td>
<td><blockquote>
<p>rec #</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>7</td>
<td><blockquote>
<p>rec type</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>“D1”</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>8</td>
<td><blockquote>
<p>name</p>
</blockquote></td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>person, patient_account</p>
</blockquote></td>
<td><blockquote>
<p>full_nm</p>
</blockquote></td>
<td><blockquote>
<p>vc 150</p>
</blockquote></td>
<td><blockquote>
<p>Uppercase Populate patient_ac patient_upper_last_</p>
<p>patient_account.pati</p>
<p>(first character of las last 4 digits of SSN n the ‘P’).</p>
</blockquote></td>
<td><blockquote>
<p>ount. nm nd</p>
<p>nt_cd name,</p>
<p>ot counting</p>
</blockquote></td>
<td><blockquote>
<p>y</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>9</p>
</blockquote></th>
<th><blockquote>
<p>SSN</p>
</blockquote></th>
<th>11</th>
<th><blockquote>
<p>y</p>
</blockquote></th>
<th><blockquote>
<p>person</p>
</blockquote></th>
<th><blockquote>
<p>ssn_nbr</p>
</blockquote></th>
<th><blockquote>
<p>vc 9</p>
</blockquote></th>
<th><blockquote>
<p>Change to 10. Accommodate pseu which have a P on</p>
<p>th Digits 1-9</p>
<p>numeric, d</p>
</blockquote></th>
<th><blockquote>
<p>o-SSNs, e end.</p>
<p>git 10 = 'P'</p>
</blockquote></th>
<th><blockquote>
<p>y</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>DOB</p>
</blockquote></td>
<td>7</td>
<td></td>
<td><blockquote>
<p>patient_account</p>
</blockquote></td>
<td><blockquote>
<p>birth_dt</p>
</blockquote></td>
<td><blockquote>
<p>date</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Standard M date for at.</p>
<p>For example: 22103 3 (03/03/1921) where first digit indicates century (1=18, 2=19,</p>
<p>3=20) date."</p>
<p>Check for "imprecise</p>
</blockquote></td>
<td><blockquote>
<p>y</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>ward</p>
</blockquote></td>
<td>30</td>
<td></td>
<td><blockquote>
<p>patient_account</p>
</blockquote></td>
<td><blockquote>
<p>ward_nm</p>
</blockquote></td>
<td><blockquote>
<p>vc 30</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Uppercase 2-30 chars</p>
</blockquote></td>
<td><blockquote>
<p>y</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 22%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="11"><blockquote>
<p><strong>PFOP EXTRACTION FILE LAYOUT - VPFS MAPPING</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>KEY</strong></p>
</blockquote></td>
<td><strong>:</strong></td>
<td><blockquote>
<p>A1 - header</p>
<p>D1 - demographics 1 D2 - demographics 2 B1 - balance 1</p>
<p>B2 - balance 2</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>T1 - transaction 1 S1 - suspense 1 S2 - suspense 2 S3 - suspense 3 I1 - income 1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>R1 - general remarks 1 R2 - general remarks 2 X1 - special remarks 1 X2 - special remarks 2</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p><strong>M Extr Field</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p><strong>V Table</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>V Field</strong></p>
</blockquote></td>
<td><blockquote>
<p>![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/024.png)</p>
</blockquote></td>
<td><blockquote>
<p><strong>Conversion Rules</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>12</td>
<td><blockquote>
<p>claim #</p>
</blockquote></td>
<td>9</td>
<td></td>
<td colspan="2"><blockquote>
<p>person</p>
</blockquote></td>
<td><blockquote>
<p>claim_nbr</p>
</blockquote></td>
<td><blockquote>
<p>vc 11</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>y</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>13</td>
<td><blockquote>
<p>address 1</p>
</blockquote></td>
<td>35</td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td><blockquote>
<p>Address fields are n t migrated (address 1-3, city, st te, zip) since these will be rereshed on first use and/or the fi st night.</p>
</blockquote></td>
<td><blockquote>
<p>y</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>14</td>
<td><blockquote>
<p>address 2</p>
</blockquote></td>
<td>30</td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>y</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>15</p>
</blockquote></th>
<th><blockquote>
<p>address 3</p>
</blockquote></th>
<th>30</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th colspan="2"></th>
<th><blockquote>
<p>y</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>16</p>
</blockquote></td>
<td><blockquote>
<p>city</p>
</blockquote></td>
<td>15</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td><blockquote>
<p>y</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>17</p>
</blockquote></td>
<td><blockquote>
<p>state</p>
</blockquote></td>
<td>30</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td><blockquote>
<p>y</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>18</p>
</blockquote></td>
<td><blockquote>
<p>zip</p>
</blockquote></td>
<td>10</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td><blockquote>
<p>y</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>19</p>
</blockquote></td>
<td><blockquote>
<p>prov name</p>
</blockquote></td>
<td>30</td>
<td></td>
<td><blockquote>
<p>patient_account</p>
</blockquote></td>
<td><blockquote>
<p>physician_nm</p>
</blockquote></td>
<td><blockquote>
<p>vc 100</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>division id</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>patient_account</p>
</blockquote></td>
<td><blockquote>
<p>station_cd</p>
</blockquote></td>
<td><blockquote>
<p>vc 10</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Also converted to instn_id via institution table, set in person, patient_account, etc.instn_id field.</p>
</blockquote></td>
<td><blockquote>
<p>y</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>n/a</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>patient_account</p>
</blockquote></td>
<td><blockquote>
<p>patient_cd</p>
</blockquote></td>
<td><blockquote>
<p>vc 5</p>
</blockquote></td>
<td><blockquote>
<p>First char of last na digits of SSN (exclud in position 10 of SS</p>
</blockquote></td>
<td><blockquote>
<p>e, last 4</p>
<p>g the P N).</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>D2</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>"VPFS"</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Station ID</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>All records include S IEN, SSN, and ICN f</p>
</blockquote></td>
<td>ation ID, or linking.</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>IEN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 17%" />
<col style="width: 15%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"><blockquote>
<p><strong>PFOP EXTRACTION FILE LAYOUT - VPFS MAPPING</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>KEY:</strong></p>
</blockquote></td>
<td><blockquote>
<p>A1 - header</p>
<p>D1 - demographics 1 D2 - demographics 2 B1 - balance 1</p>
<p>B2 - balance 2</p>
</blockquote></td>
<td><blockquote>
<p>T1 - transaction 1 S1 - suspense 1 S2 - suspense 2 S3 - suspense 3 I1 - income 1</p>
</blockquote></td>
<td><blockquote>
<p>R1 - general remarks 1 R2 - general remarks 2 X1 - special remarks 1 X2 - special remarks 2</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th><blockquote>
<p><strong>M Extr Field</strong></p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p><strong>V Table</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>V Field</strong></p>
</blockquote></th>
<th><blockquote>
<p>![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/025.png)</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Conversion Rules</strong></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>ICN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>rec #</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>rec type</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>“D2”</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>patient IEN</p>
</blockquote></td>
<td></td>
<td>y</td>
<td><blockquote>
<p>person</p>
</blockquote></td>
<td><blockquote>
<p>ien_id</p>
</blockquote></td>
<td><blockquote>
<p>n 18</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>account status</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>y</td>
<td><blockquote>
<p>patient_account</p>
</blockquote></td>
<td><blockquote>
<p>acct_status_ind</p>
</blockquote></td>
<td><blockquote>
<p>vc 1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Upper: I, A Default</p>
<p>= A</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>patient type</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>patient_account</p>
</blockquote></td>
<td><blockquote>
<p>patient_type_cd</p>
</blockquote></td>
<td><blockquote>
<p>vc 1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Upper: L, R, U, X Default = U</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>patient status</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>patient_account</p>
</blockquote></td>
<td><blockquote>
<p>patient_status_cd</p>
</blockquote></td>
<td><blockquote>
<p>vc 1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Upper: A, R, C, N, X</p>
<p>Default = X</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>indigent</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>patient_account</p>
</blockquote></td>
<td><blockquote>
<p>indigent_ind</p>
</blockquote></td>
<td><blockquote>
<p>vc 1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Upper: Y, N Default</p>
<p>= N</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>apportionee $</p>
</blockquote></td>
<td><blockquote>
<p>9,2</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>income_source</p>
</blockquote></td>
<td><blockquote>
<p>income_source_amt</p>
</blockquote></td>
<td><blockquote>
<p>n 18,2</p>
</blockquote></td>
<td><blockquote>
<p>income_source.inco</p>
<p>_txt = 'APPORTION</p>
<p>income_source.inco</p>
<p>_amt = appor$</p>
</blockquote></td>
<td><blockquote>
<p>e_source E' and e_source</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>guardian $</p>
</blockquote></td>
<td><blockquote>
<p>9,2</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>income_source</p>
</blockquote></td>
<td><blockquote>
<p>income_source_amt</p>
</blockquote></td>
<td><blockquote>
<p>n 18,2</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>income_source.inco e_source</p>
<p>_txt = 'GUARDIAN' and income_source.inco e_source</p>
<p>_amt = guard$</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="12"><blockquote>
<p><strong>PFOP EXTRACTION FILE LAYOUT - VPFS MAPPING</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>KEY</strong></p>
</blockquote></td>
<td><strong>:</strong></td>
<td><blockquote>
<p>A1 - header</p>
<p>D1 - demographics 1 D2 - demographics 2 B1 - balance 1</p>
<p>B2 - balance 2</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>T1 - transaction 1 S1 - suspense 1 S2 - suspense 2 S3 - suspense 3 I1 - income 1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>R1 - general remarks 1 R2 - general remarks 2 X1 - special remarks 1 X2 - special remarks 2</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p><strong>M Extr Field</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p><strong>V Table</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>V Field</strong></p>
</blockquote></td>
<td><blockquote>
<p>![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/026.png)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p><strong>Conversion Rules</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>15</td>
<td><blockquote>
<p>institut award $</p>
</blockquote></td>
<td><blockquote>
<p>9,2</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>income_source</p>
</blockquote></td>
<td><blockquote>
<p>income_source_amt</p>
</blockquote></td>
<td><blockquote>
<p>n 18,2</p>
</blockquote></td>
<td><blockquote>
<p>income_source.inco</p>
<p>_txt = 'OTHER ASS</p>
<p>income_source.inco</p>
<p>_amt = other assets$</p>
</blockquote></td>
<td><blockquote>
<p>e_source TS' and e_source</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>16</td>
<td><blockquote>
<p>regional office</p>
</blockquote></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>patient_account</p>
</blockquote></td>
<td><blockquote>
<p>patient_ro_cd</p>
</blockquote></td>
<td><blockquote>
<p>vc 5</p>
</blockquote></td>
<td><blockquote>
<p>Corresponds to institution.station_cd</p>
</blockquote></td>
<td><blockquote>
<p>but no FK</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>17</td>
<td><blockquote>
<p>other assets $</p>
</blockquote></td>
<td><blockquote>
<p>9,2</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>income_source</p>
</blockquote></td>
<td><blockquote>
<p>income_source_amt</p>
</blockquote></td>
<td><blockquote>
<p>n 18,2</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>income_source.inco e_source</p>
<p>_txt = 'INSTITUTIONAL</p>
<p>AWARD' and</p>
<p>income_source.inco e_source</p>
<p>_amt = institut award$</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>18</td>
<td><blockquote>
<p>date of last trans</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>patient_account</p>
</blockquote></td>
<td><blockquote>
<p>last_trans_entered_dt</p>
</blockquote></td>
<td><blockquote>
<p>date</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>M date conversion, imprecise date check</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>19</td>
<td><blockquote>
<p>date of current restr</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>patient_account</p>
</blockquote></td>
<td><blockquote>
<p>current_restriction_dt</p>
</blockquote></td>
<td><blockquote>
<p>date</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>M date conversion, imprecise date check</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>20</td>
<td><blockquote>
<p>prov IEN</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Do not migrate.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>21</td>
<td><blockquote>
<p>prov converted</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Do not migrate.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>B1</p>
</blockquote></th>
<th>1</th>
<th><blockquote>
<p>"VPFS"</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th colspan="2"></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>2</td>
<td><blockquote>
<p>Station ID</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>All records include S IEN, SSN, and ICN f</p>
</blockquote></td>
<td><blockquote>
<p>ation ID, or linking.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td><blockquote>
<p>IEN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 22%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="11"><blockquote>
<p><strong>PFOP EXTRACTION FILE LAYOUT - VPFS MAPPING</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>KEY</strong></p>
</blockquote></td>
<td><strong>:</strong></td>
<td><blockquote>
<p>A1 - header</p>
<p>D1 - demographics 1 D2 - demographics 2 B1 - balance 1</p>
<p>B2 - balance 2</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>T1 - transaction 1 S1 - suspense 1 S2 - suspense 2 S3 - suspense 3 I1 - income 1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>R1 - general remarks 1 R2 - general remarks 2 X1 - special remarks 1 X2 - special remarks 2</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p><strong>M Extr Field</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p><strong>V Table</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>V Field</strong></p>
</blockquote></td>
<td><blockquote>
<p>![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/027.png)</p>
</blockquote></td>
<td><blockquote>
<p><strong>Conversion Rules</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td><blockquote>
<p>ICN</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>6</td>
<td><blockquote>
<p>rec #</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>7</td>
<td><blockquote>
<p>rec type</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td><blockquote>
<p>“B1”</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>8</td>
<td><blockquote>
<p>bal carr fwd</p>
</blockquote></td>
<td>10,2</td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td><blockquote>
<p>Do not migrate.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>9</td>
<td><blockquote>
<p>priv carr fwd</p>
</blockquote></td>
<td>10,2</td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td><blockquote>
<p>Do not migrate.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>10</td>
<td><blockquote>
<p>grat carr fwd</p>
</blockquote></td>
<td>10,2</td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td><blockquote>
<p>Do not migrate.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>11</p>
</blockquote></th>
<th><blockquote>
<p>stored bal</p>
</blockquote></th>
<th>10,2</th>
<th>y</th>
<th><blockquote>
<p>patient_account</p>
</blockquote></th>
<th><blockquote>
<p>total_balance_amt</p>
</blockquote></th>
<th>18,2</th>
<th><blockquote>
<p>Default = 0</p>
<p>Use to create initial bal - deferred that is migrated separately) Can use to check: V bal should be same amount (chk in temp</p>
</blockquote></th>
<th><blockquote>
<p>/w: (stored being</p>
<p>FS stored s this able).</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>stored priv</p>
</blockquote></td>
<td>10,2</td>
<td>y</td>
<td><blockquote>
<p>patient_account</p>
</blockquote></td>
<td><blockquote>
<p>private_source_balan ce_amt</p>
</blockquote></td>
<td>18,2</td>
<td colspan="2"><blockquote>
<p>Default = 0 as above for private.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>stored grat</p>
</blockquote></td>
<td>10,2</td>
<td>y</td>
<td><blockquote>
<p>patient_account</p>
</blockquote></td>
<td><blockquote>
<p>gratuitous_balance_a mt</p>
</blockquote></td>
<td>18,2</td>
<td><blockquote>
<p>Default = 0 as above for gratuito</p>
</blockquote></td>
<td><blockquote>
<p>us.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>amt restr per month</p>
</blockquote></td>
<td>8,2</td>
<td></td>
<td><blockquote>
<p>patient_account</p>
</blockquote></td>
<td><blockquote>
<p>monthly_restriction_li mit_amt</p>
</blockquote></td>
<td>18,2</td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
<td><blockquote>
<p>amt restr per week</p>
</blockquote></td>
<td>8,2</td>
<td></td>
<td><blockquote>
<p>patient_account</p>
</blockquote></td>
<td><blockquote>
<p>weekly_restriction_li mit_amt</p>
</blockquote></td>
<td>18,2</td>
<td colspan="2"></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 22%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="11"><blockquote>
<p><strong>PFOP EXTRACTION FILE LAYOUT - VPFS MAPPING</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>KEY</strong></p>
</blockquote></td>
<td><strong>:</strong></td>
<td><blockquote>
<p>A1 - header</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>T1 - transaction 1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>R1 - general remarks 1</p>
</blockquote></td>
<td rowspan="5"></td>
<td rowspan="5"></td>
<td rowspan="5"></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>D1 - demographics 1</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>S1 - suspense 1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>R2 - general remarks 2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>D2 - demographics 2</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>S2 - suspense 2</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>X1 - special remarks 1</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>B1 - balance 1</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>S3 - suspense 3</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>X2 - special remarks 2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>B2 - balance 2</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>I1 - income 1</p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p><strong>M Extr Field</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p><strong>V Table</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>V Field</strong></p>
</blockquote></td>
<td><blockquote>
<p>![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/028.png)</p>
</blockquote></td>
<td><blockquote>
<p><strong>Conversion Rules</strong></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>16</p>
</blockquote></th>
<th><blockquote>
<p>restriction month</p>
</blockquote></th>
<th><blockquote>
<p>9</p>
<p>(date</p>
<p>)</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th colspan="2"><blockquote>
<p>Do not migrate.</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>17</p>
</blockquote></td>
<td><blockquote>
<p>restriction week #</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Do not migrate.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>18</p>
</blockquote></td>
<td><blockquote>
<p>monthly restr balance</p>
</blockquote></td>
<td><blockquote>
<p>8,2</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>patient_account</p>
</blockquote></td>
<td><blockquote>
<p>actual_monthly_restri ction_amt</p>
</blockquote></td>
<td>18,2</td>
<td colspan="2"><blockquote>
<p>Default = 0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>19</p>
</blockquote></td>
<td><blockquote>
<p>weekly restr balance</p>
</blockquote></td>
<td><blockquote>
<p>8,2</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>patient_account</p>
</blockquote></td>
<td><blockquote>
<p>actual_weekly_restric tion_amt</p>
</blockquote></td>
<td>18,2</td>
<td colspan="2"><blockquote>
<p>Default = 0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>B2</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>"VPFS"</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Station ID</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>All records include S IEN, SSN, and ICN f</p>
</blockquote></td>
<td><blockquote>
<p>ation ID, or inking.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>IEN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>ICN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>rec #</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>rec type</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>“B2”</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>min bal 1</p>
</blockquote></td>
<td><blockquote>
<p>9,2</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>patient_account</p>
</blockquote></td>
<td><blockquote>
<p>min_one_limit_amt</p>
</blockquote></td>
<td>18,2</td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>max bal 1</p>
</blockquote></td>
<td><blockquote>
<p>9,2</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>patient_account</p>
</blockquote></td>
<td><blockquote>
<p>max_one_limit_amt</p>
</blockquote></td>
<td>18,2</td>
<td colspan="2"></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>KEY</strong></p>
</blockquote></th>
<th><strong>:</strong></th>
<th><blockquote>
<p>A1 - header</p>
<p>D1 - demographics 1 D2 - demographics 2 B1 - balance 1</p>
<p>B2 - balance 2</p>
</blockquote></th>
<th colspan="3"><blockquote>
<p>T1 - transaction 1 S1 - suspense 1 S2 - suspense 2 S3 - suspense 3 I1 - income 1</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>R1 - general remarks 1 R2 - general remarks 2 X1 - special remarks 1 X2 - special remarks 2</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p><strong>M Extr Field</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p><strong>V Table</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>V Field</strong></p>
</blockquote></td>
<td><blockquote>
<p>![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/029.png)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p><strong>Conversion Rules</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>10</td>
<td><blockquote>
<p>min bal 2</p>
</blockquote></td>
<td><blockquote>
<p>9,2</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Do not migrate</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>11</td>
<td><blockquote>
<p>max bal 2</p>
</blockquote></td>
<td><blockquote>
<p>9,2</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Do not migrate</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>T1</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>"VPFS"</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td><blockquote>
<p>Station ID</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td><blockquote>
<p>All records include S IEN, SSN, and ICN f</p>
</blockquote></td>
<td><blockquote>
<p>ation ID, or linking.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td><blockquote>
<p>IEN</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td><blockquote>
<p>ICN</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>6</td>
<td><blockquote>
<p>rec #</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>7</td>
<td><blockquote>
<p>rec type</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>“T1”</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>8</td>
<td><blockquote>
<p>deferred date</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Same as deferral date at end of record.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>9</td>
<td><blockquote>
<p>trans id</p>
</blockquote></td>
<td><blockquote>
<p>12</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>account_transaction</p>
</blockquote></td>
<td><blockquote>
<p>master_trans_cd</p>
</blockquote></td>
<td><blockquote>
<p>vc 20</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>10</td>
<td><blockquote>
<p>patient IEN</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 22%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>11</p>
</blockquote></th>
<th><blockquote>
<p>patient trans #</p>
</blockquote></th>
<th>5,0</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>Do not migrate.</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>amount</p>
</blockquote></td>
<td>10,2</td>
<td></td>
<td><blockquote>
<p>account_transaction</p>
</blockquote></td>
<td><blockquote>
<p>trans_amt</p>
</blockquote></td>
<td>18,2</td>
<td><blockquote>
<p>Default = 0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>trans date</p>
</blockquote></td>
<td>date</td>
<td></td>
<td><blockquote>
<p>account_transaction</p>
</blockquote></td>
<td><blockquote>
<p>trans_dt</p>
</blockquote></td>
<td>date</td>
<td><blockquote>
<p>M date conversion, imprecise date check</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="12"><blockquote>
<p><strong>PFOP EXTRACTION FILE LAYOUT - VPFS MAPPING</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>KEY</strong></p>
</blockquote></td>
<td><strong>:</strong></td>
<td><blockquote>
<p>A1 - header</p>
<p>D1 - demographics 1 D2 - demographics 2 B1 - balance 1</p>
<p>B2 - balance 2</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>T1 - transaction 1 S1 - suspense 1 S2 - suspense 2 S3 - suspense 3 I1 - income 1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>R1 - general remarks 1 R2 - general remarks 2 X1 - special remarks 1 X2 - special remarks 2</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p><strong>M Extr Field</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p><strong>V Table</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>V Field</strong></p>
</blockquote></td>
<td><blockquote>
<p>![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/030.png)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p><strong>Conversion Rules</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>14</td>
<td><blockquote>
<p>date trans entered</p>
</blockquote></td>
<td><blockquote>
<p>date</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>account_transaction</p>
</blockquote></td>
<td><blockquote>
<p>trans_entered_dt</p>
</blockquote></td>
<td><blockquote>
<p>date</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>M date conversion, imprecise date check</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>15</td>
<td><blockquote>
<p>ref</p>
</blockquote></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>account_transaction</p>
</blockquote></td>
<td><blockquote>
<p>reference_txt</p>
</blockquote></td>
<td><blockquote>
<p>vc 35</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>16</td>
<td><blockquote>
<p>d/w</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>account_transaction</p>
</blockquote></td>
<td><blockquote>
<p>trans_type_ind</p>
</blockquote></td>
<td><blockquote>
<p>vc 1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Upper: D, W</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>17</td>
<td><blockquote>
<p>c/c/o</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>y</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>account_transaction</p>
</blockquote></td>
<td><blockquote>
<p>payment_type_cd</p>
</blockquote></td>
<td><blockquote>
<p>vc 1</p>
</blockquote></td>
<td><blockquote>
<p>1, 2, 3 (= cash, chec but store number)</p>
</blockquote></td>
<td><blockquote>
<p>, other,</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>18</td>
<td><blockquote>
<p>source</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>account_transaction</p>
</blockquote></td>
<td><blockquote>
<p>source_type_ind</p>
</blockquote></td>
<td><blockquote>
<p>vc 1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Upper: P, G, B</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>19</td>
<td><blockquote>
<p>form</p>
</blockquote></td>
<td><blockquote>
<p>11</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>account_transaction</p>
</blockquote></td>
<td><blockquote>
<p>form_nbr</p>
</blockquote></td>
<td><blockquote>
<p>vc 12</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 7%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>20</p>
</blockquote></th>
<th><blockquote>
<p>priv amt</p>
</blockquote></th>
<th><blockquote>
<p>7</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>account_transaction</p>
</blockquote></th>
<th><blockquote>
<p>private_source_amt</p>
</blockquote></th>
<th><blockquote>
<p>18,2</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>Default = 0</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>21</p>
</blockquote></td>
<td><blockquote>
<p>grat amt</p>
</blockquote></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>account_transaction</p>
</blockquote></td>
<td><blockquote>
<p>gratuitous_amt</p>
</blockquote></td>
<td><blockquote>
<p>18,2</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Default = 0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>pfc</p>
</blockquote></td>
<td><blockquote>
<p>14</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>account_transaction</p>
</blockquote></td>
<td><blockquote>
<p>user_id</p>
</blockquote></td>
<td><blockquote>
<p>vc 12</p>
</blockquote></td>
<td><blockquote>
<p>Turn off any trigger ( "sys").</p>
</blockquote></td>
<td><blockquote>
<p>uch as to</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>23</p>
</blockquote></td>
<td><blockquote>
<p>e-sig</p>
</blockquote></td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Do not migrate.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>24</p>
</blockquote></td>
<td><blockquote>
<p>rmks</p>
</blockquote></td>
<td><blockquote>
<p>35</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>account_transaction</p>
</blockquote></td>
<td><blockquote>
<p>trans_rmks_txt</p>
</blockquote></td>
<td><blockquote>
<p>vc 255</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>25</p>
</blockquote></td>
<td><blockquote>
<p>validation code</p>
</blockquote></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Do not migrate.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>bal carr fwd</p>
</blockquote></td>
<td><blockquote>
<p>10,2</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Do not migrate.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 22%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="11"><blockquote>
<p><strong>PFOP EXTRACTION FILE LAYOUT - VPFS MAPPING</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>KEY</strong></p>
</blockquote></td>
<td><strong>:</strong></td>
<td><blockquote>
<p>A1 - header</p>
<p>D1 - demographics 1 D2 - demographics 2 B1 - balance 1</p>
<p>B2 - balance 2</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>T1 - transaction 1 S1 - suspense 1 S2 - suspense 2 S3 - suspense 3 I1 - income 1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>R1 - general remarks 1 R2 - general remarks 2 X1 - special remarks 1 X2 - special remarks 2</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p><strong>M Extr Field</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p><strong>V Table</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>V Field</strong></p>
</blockquote></td>
<td><blockquote>
<p>![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/031.png)</p>
</blockquote></td>
<td><blockquote>
<p><strong>Conversion Rules</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>27</td>
<td><blockquote>
<p>priv bal carr fwd</p>
</blockquote></td>
<td>10,2</td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td><blockquote>
<p>Do not migrate.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>28</td>
<td><blockquote>
<p>grat bal carr fwd</p>
</blockquote></td>
<td>10,2</td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td><blockquote>
<p>Do not migrate.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>29</p>
</blockquote></th>
<th><blockquote>
<p>deferral date</p>
</blockquote></th>
<th><blockquote>
<p>date</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>account_transaction</p>
</blockquote></th>
<th><blockquote>
<p>deferral_dt</p>
</blockquote></th>
<th>date</th>
<th colspan="2"><blockquote>
<p>M date conversion, imprecise date check</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>signature conversion completed</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Do not migrate.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td rowspan="4"></td>
<td><blockquote>
<p>31</p>
</blockquote></td>
<td><blockquote>
<p>signature code</p>
</blockquote></td>
<td><blockquote>
<p>date/</p>
</blockquote></td>
<td rowspan="4"></td>
<td rowspan="4"></td>
<td rowspan="4"></td>
<td rowspan="4"></td>
<td colspan="2"><blockquote>
<p>Do not migrate.</p>
</blockquote></td>
<td rowspan="4"></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>date/time</p>
</blockquote></td>
<td><blockquote>
<p>time</p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>(char</p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>20)</p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>account_transaction</p>
</blockquote></td>
<td><blockquote>
<p>countin_deferred_bal ance_ind</p>
</blockquote></td>
<td>vc 1</td>
<td colspan="2"><blockquote>
<p>Default = Y for migration only (since we have only deferred recs)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="3"></td>
<td rowspan="3"></td>
<td rowspan="3"></td>
<td rowspan="3"></td>
<td rowspan="3"></td>
<td><blockquote>
<p>account_transaction</p>
</blockquote></td>
<td><blockquote>
<p>countin_restricted_ba</p>
</blockquote></td>
<td>vc 1</td>
<td><blockquote>
<p>No default.</p>
</blockquote></td>
<td></td>
<td rowspan="3"></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>lance_ind</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Will be used as user do withdrawals.</p>
</blockquote></td>
<td><blockquote>
<p>start to</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Only deposits being (deferred, and store</p>
</blockquote></td>
<td><blockquote>
<p>migrated balance)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>account_transaction</p>
</blockquote></td>
<td><blockquote>
<p>running_balance_amt</p>
</blockquote></td>
<td>18,2</td>
<td colspan="2"><blockquote>
<p>Populated by trigger.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>S1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>"VPFS"</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Each suspense date record (S1) can have multip e suspense items (S2)associated with that date.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 17%" />
<col style="width: 15%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"><blockquote>
<p><strong>PFOP EXTRACTION FILE LAYOUT - VPFS MAPPING</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>KEY:</strong></p>
</blockquote></td>
<td><blockquote>
<p>A1 - header</p>
<p>D1 - demographics 1 D2 - demographics 2 B1 - balance 1</p>
<p>B2 - balance 2</p>
</blockquote></td>
<td><blockquote>
<p>T1 - transaction 1 S1 - suspense 1 S2 - suspense 2 S3 - suspense 3 I1 - income 1</p>
</blockquote></td>
<td><blockquote>
<p>R1 - general remarks 1 R2 - general remarks 2 X1 - special remarks 1 X2 - special remarks 2</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th><blockquote>
<p><strong>M Extr Field</strong></p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p><strong>V Table</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>V Field</strong></p>
</blockquote></th>
<th><blockquote>
<p>![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/032.png)</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Conversion Rules</strong></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>2</td>
<td><blockquote>
<p>Station ID</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>All records include S IEN, SSN, and ICN f</p>
</blockquote></td>
<td><blockquote>
<p>ation ID, or linking.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td><blockquote>
<p>IEN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td><blockquote>
<p>ICN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>6</td>
<td><blockquote>
<p>rec #</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>7</td>
<td><blockquote>
<p>rec type</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>“S1”</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>8</td>
<td><blockquote>
<p>suspense date</p>
</blockquote></td>
<td><blockquote>
<p>date</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>suspense</p>
</blockquote></td>
<td><blockquote>
<p>suspense_dt</p>
</blockquote></td>
<td><blockquote>
<p>date</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>M date conversion, imprecise date check</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>S2</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>"VPFS"</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td><blockquote>
<p>Station ID</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>All records include S IEN, SSN, and ICN f</p>
</blockquote></td>
<td><blockquote>
<p>ation ID, or inking.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td><blockquote>
<p>IEN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td><blockquote>
<p>ICN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>6</td>
<td><blockquote>
<p>rec #</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>7</td>
<td><blockquote>
<p>rec type</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>“S2”</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>8</td>
<td><blockquote>
<p>item ID</p>
</blockquote></td>
<td><blockquote>
<p>40</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>suspense</p>
</blockquote></td>
<td><blockquote>
<p>item_nm</p>
</blockquote></td>
<td><blockquote>
<p>vc 50</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Must be unique within IEN and suspense date.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>9</th>
<th><blockquote>
<p>full descr</p>
</blockquote></th>
<th><blockquote>
<p>127</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>suspense</p>
</blockquote></th>
<th><blockquote>
<p>item_desc_txt</p>
</blockquote></th>
<th><blockquote>
<p>vc 255</p>
</blockquote></th>
<th><blockquote>
<p>Suspense item desc may be split to creat</p>
</blockquote></th>
<th><blockquote>
<p>iptions e uspense</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="12"><blockquote>
<p><strong>PFOP EXTRACTION FILE LAYOUT - VPFS MAPPING</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>KEY</strong></p>
</blockquote></td>
<td><strong>:</strong></td>
<td><blockquote>
<p>A1 - header</p>
<p>D1 - demographics 1 D2 - demographics 2 B1 - balance 1</p>
<p>B2 - balance 2</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>T1 - transaction 1 S1 - suspense 1 S2 - suspense 2 S3 - suspense 3 I1 - income 1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>R1 - general remarks 1 R2 - general remarks 2 X1 - special remarks 1 X2 - special remarks 2</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p><strong>M Extr Field</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p><strong>V Table</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>V Field</strong></p>
</blockquote></td>
<td><blockquote>
<p>![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/033.png)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p><strong>Conversion Rules</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>description extensio (S3) records if they are too long. Concatenate with .</p>
<p>S3</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>S3</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>"VPFS"</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td><blockquote>
<p>Station ID</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td><blockquote>
<p>All records include S IEN, SSN, and ICN f</p>
</blockquote></td>
<td><blockquote>
<p>ation ID, or inking.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td><blockquote>
<p>IEN</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td><blockquote>
<p>ICN</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>6</td>
<td><blockquote>
<p>rec #</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>7</td>
<td><blockquote>
<p>rec type</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>“S3”</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>8</td>
<td><blockquote>
<p>item ID</p>
</blockquote></td>
<td><blockquote>
<p>40</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>suspense</p>
</blockquote></td>
<td><blockquote>
<p>item_nm</p>
</blockquote></td>
<td><blockquote>
<p>vc 50</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Match with S2.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>9</td>
<td><blockquote>
<p>full descr</p>
</blockquote></td>
<td><blockquote>
<p>127</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>suspense</p>
</blockquote></td>
<td><blockquote>
<p>item_desc_txt</p>
</blockquote></td>
<td><blockquote>
<p>vc 255</p>
</blockquote></td>
<td><blockquote>
<p>Concatenate with S2</p>
</blockquote></td>
<td><blockquote>
<p>.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>I1</p>
</blockquote></th>
<th>1</th>
<th><blockquote>
<p>"VPFS"</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th colspan="2"></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>2</td>
<td><blockquote>
<p>Station ID</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>All recs include stati ssn, for linking.</p>
</blockquote></td>
<td><blockquote>
<p>n id, ien,</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td><blockquote>
<p>IEN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td><blockquote>
<p>ICN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>6</td>
<td><blockquote>
<p>rec #</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="12"><blockquote>
<p><strong>PFOP EXTRACTION FILE LAYOUT - VPFS MAPPING</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>KEY</strong></p>
</blockquote></td>
<td><strong>:</strong></td>
<td><blockquote>
<p>A1 - header</p>
<p>D1 - demographics 1 D2 - demographics 2 B1 - balance 1</p>
<p>B2 - balance 2</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>T1 - transaction 1 S1 - suspense 1 S2 - suspense 2 S3 - suspense 3 I1 - income 1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>R1 - general remarks 1 R2 - general remarks 2 X1 - special remarks 1 X2 - special remarks 2</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p><strong>M Extr Field</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p><strong>V Table</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>V Field</strong></p>
</blockquote></td>
<td><blockquote>
<p>![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/034.png)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p><strong>Conversion Rules</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>7</td>
<td><blockquote>
<p>rec type</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>“I1”</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>8</td>
<td><blockquote>
<p>income source</p>
</blockquote></td>
<td><blockquote>
<p>25</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>income_source</p>
</blockquote></td>
<td><blockquote>
<p>income_source_txt</p>
</blockquote></td>
<td><blockquote>
<p>vc 50</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>9</td>
<td><blockquote>
<p>payee</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>income_source</p>
</blockquote></td>
<td><blockquote>
<p>payee_nm</p>
</blockquote></td>
<td><blockquote>
<p>vc 50</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>10</td>
<td><blockquote>
<p>amount</p>
</blockquote></td>
<td><blockquote>
<p>8,2</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>income_source</p>
</blockquote></td>
<td><blockquote>
<p>income_souce_amt</p>
</blockquote></td>
<td><blockquote>
<p>18,2</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Default = 0.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>11</td>
<td><blockquote>
<p>freq</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>income_source</p>
</blockquote></td>
<td><blockquote>
<p>freq_cd</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>Upper: D, W, M, Y, X</p>
</blockquote></td>
<td><blockquote>
<p>, V, O</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>R1</p>
</blockquote></th>
<th>1</th>
<th><blockquote>
<p>"VPFS"</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th colspan="2"></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>2</td>
<td><blockquote>
<p>Station ID</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>All records include S IEN, SSN, and ICN f</p>
</blockquote></td>
<td><blockquote>
<p>ation ID, or linking.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td><blockquote>
<p>IEN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td><blockquote>
<p>ICN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>6</td>
<td><blockquote>
<p>rec #</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>7</td>
<td><blockquote>
<p>rec type</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>“R1”</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>8</td>
<td><blockquote>
<p>gen rmks</p>
</blockquote></td>
<td><blockquote>
<p>127</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>patient_account</p>
</blockquote></td>
<td><blockquote>
<p>general_rmks_txt</p>
</blockquote></td>
<td><blockquote>
<p>255</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Remarks may be spl t to create extension (R2) records if they are too long.</p>
<p>Concatenate with R2.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>R2</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>"VPFS"</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td><blockquote>
<p>Station ID</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>All recs include stati ssn, for linking.</p>
</blockquote></td>
<td><blockquote>
<p>n id, ien,</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 22%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="11"><blockquote>
<p><strong>PFOP EXTRACTION FILE LAYOUT - VPFS MAPPING</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>KEY</strong></p>
</blockquote></td>
<td><strong>:</strong></td>
<td><blockquote>
<p>A1 - header</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>T1 - transaction 1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>R1 - general remarks 1</p>
</blockquote></td>
<td rowspan="5"></td>
<td rowspan="5"></td>
<td rowspan="5"></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>D1 - demographics 1</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>S1 - suspense 1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>R2 - general remarks 2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>D2 - demographics 2</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>S2 - suspense 2</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>X1 - special remarks 1</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>B1 - balance 1</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>S3 - suspense 3</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>X2 - special remarks 2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>B2 - balance 2</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>I1 - income 1</p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p><strong>M Extr Field</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p><strong>V Table</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>V Field</strong></p>
</blockquote></td>
<td><blockquote>
<p>![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/035.png)</p>
</blockquote></td>
<td><blockquote>
<p><strong>Conversion Rules</strong></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>3</th>
<th><blockquote>
<p>IEN</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th colspan="2"></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>4</td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td><blockquote>
<p>ICN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>6</td>
<td><blockquote>
<p>rec #</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>7</td>
<td><blockquote>
<p>rec type</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>“R2”</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>8</td>
<td><blockquote>
<p>gen rmks</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Multiple remarks ext nsion (R2) records can exist for each R1. Concatenate with R1.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>X1</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>"VPFS"</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td><blockquote>
<p>Station ID</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>All records include S IEN, SSN, and ICN f</p>
</blockquote></td>
<td><blockquote>
<p>ation ID, or inking.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td><blockquote>
<p>IEN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td><blockquote>
<p>ICN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>6</td>
<td><blockquote>
<p>rec #</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>7</td>
<td><blockquote>
<p>rec type</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>“X1”</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>8</td>
<td><blockquote>
<p>spec rmks</p>
</blockquote></td>
<td><blockquote>
<p>127</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>patient_account</p>
</blockquote></td>
<td><blockquote>
<p>special_rmks_txt</p>
</blockquote></td>
<td><blockquote>
<p>2000</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Remarks may be spl t to create extension (X2) recor s if they are too long.</p>
<p>Concatenate with X2.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>X2</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>"VPFS"</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
</tbody>
</table>

#### Appendix C. Extraction File Layouts

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="12"><blockquote>
<p><strong>PFOP EXTRACTION FILE LAYOUT - VPFS MAPPING</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>KEY</strong></p>
</blockquote></td>
<td><strong>:</strong></td>
<td><blockquote>
<p>A1 - header</p>
<p>D1 - demographics 1 D2 - demographics 2 B1 - balance 1</p>
<p>B2 - balance 2</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>T1 - transaction 1 S1 - suspense 1 S2 - suspense 2 S3 - suspense 3 I1 - income 1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>R1 - general remarks 1 R2 - general remarks 2 X1 - special remarks 1 X2 - special remarks 2</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p><strong>M Extr Field</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p><strong>V Table</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>V Field</strong></p>
</blockquote></td>
<td><blockquote>
<p>![](vpfs-vistamigrate-data-migration-version-1-2-users-guide/036.png)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p><strong>Conversion Rules</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td><blockquote>
<p>Station ID</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td><blockquote>
<p>All records include S IEN, SSN, and ICN f</p>
</blockquote></td>
<td><blockquote>
<p>ation ID, or linking.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td><blockquote>
<p>IEN</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td><blockquote>
<p>ICN</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>6</td>
<td><blockquote>
<p>rec #</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>7</td>
<td><blockquote>
<p>rec type</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>“X2”</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>8</td>
<td><blockquote>
<p>spec rmks</p>
</blockquote></td>
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>Multiple remarks ext nsion (X2) records can exist for each X1. Concatenate with X1.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

Appendix D.

> This page is intentionally left blank.

> July 2020 65 Appendix D. VistAMigrate Report Samples

# Appendix D. VistAMigrate Report Samples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This appendix contains sample portions of the reports, logs, and error files produced by the routines that you perform while moving through the data migration process in VistAMigrate.

### Diagnostic Summary Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report is accessed in both of the following ways:

- In the VistA legacy application: Select the function Database Diagnostic Report.
- In VistAMigrate: Select step 2 M Diagnostics

> The Diagnostic Summary Report lists the number of occurrences for each type of error, and also lists how many deferred transactions are to be migrated (this is not an error). The following table lists descriptions of the information in the fields on the Diagnostic Summary Report.

> Table D-1. Description of Diagnostic Summary Report

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Error #</strong></p>
</blockquote></td>
<td><blockquote>
<p>Code assigned to the error type.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></td>
<td><blockquote>
<p>Name of the field where the error occurred.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Error Description</strong></p>
</blockquote></td>
<td><blockquote>
<p>Description of the error.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Total Count</strong></p>
</blockquote></td>
<td><blockquote>
<p>Number of occurrences of the specific type of error.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Total Accounts processed =</strong></p>
</blockquote></td>
<td><blockquote>
<p>Total number of patient records processed by the M diagnostics routine.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> VPFS^442^^^^0^A1^1006^155^000666625

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*\* Patient Funds Diagnostic Summary LEGACY RPC (version 5.9) \*\*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Run Date: FEB 27, 2006 Run Time: 10:30:01 \*\*

> Total accounts processed = 1006 \*\*

> Total balance of accounts for migration =\$1,085,425.00 \*\*

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 22%" />
<col style="width: 57%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Err#</td>
<td><blockquote>
<p>Field</p>
</blockquote></td>
<td><blockquote>
<p>Error</p>
</blockquote></td>
<td>Total</td>
</tr>
<tr class="even">
<td><blockquote>
<p>#</p>
</blockquote></td>
<td><blockquote>
<p>Name</p>
</blockquote></td>
<td><blockquote>
<p>Description</p>
</blockquote></td>
<td>Count</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>#1</p>
</blockquote></td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td><blockquote>
<p>Name is blank</p>
</blockquote></td>
<td>1</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>#2</p>
</blockquote></td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td><blockquote>
<p>Name contains invalid data</p>
</blockquote></td>
<td>3</td>
</tr>
<tr class="even">
<td><blockquote>
<p>#3</p>
</blockquote></td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td><blockquote>
<p>SSN is blank</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>#4</p>
</blockquote></td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td><blockquote>
<p>SSN contains invalid data</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>#5</p>
</blockquote></td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td><blockquote>
<p>SSN contains duplicate value</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>#6</p>
</blockquote></td>
<td><blockquote>
<p>SSN</p>
</blockquote></td>
<td><blockquote>
<p>SSN contains Pseudo SSN value</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>#7</p>
</blockquote></td>
<td><blockquote>
<p>DOB</p>
</blockquote></td>
<td><blockquote>
<p>DOB is blank</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>#8</p>
</blockquote></td>
<td><blockquote>
<p>DOB</p>
</blockquote></td>
<td><blockquote>
<p>DOB contains invalid date</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>#9</p>
</blockquote></td>
<td><blockquote>
<p>WARD</p>
</blockquote></td>
<td><blockquote>
<p>Ward loc invalid length</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="odd">
<td>#10</td>
<td><blockquote>
<p>CLAIM</p>
</blockquote></td>
<td><blockquote>
<p>Claim # contains invalid data</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="even">
<td>#11</td>
<td><blockquote>
<p>ZIP</p>
</blockquote></td>
<td><blockquote>
<p>Zipcode contains invalid data</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="odd">
<td>#12</td>
<td><blockquote>
<p>REGION OFFICE</p>
</blockquote></td>
<td><blockquote>
<p>Regional Office ID invalid data</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="even">
<td>#13</td>
<td><blockquote>
<p>ICN</p>
</blockquote></td>
<td><blockquote>
<p>ICN Duplicate</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="odd">
<td>#14</td>
<td><blockquote>
<p>ICN</p>
</blockquote></td>
<td><blockquote>
<p>ICN invalid or blank</p>
</blockquote></td>
<td>1</td>
</tr>
<tr class="even">
<td>#15</td>
<td><blockquote>
<p>PROVIDER AUTHR</p>
</blockquote></td>
<td><blockquote>
<p>Provider Name contains invalid data</p>
</blockquote></td>
<td>15</td>
</tr>
<tr class="odd">
<td>*#16</td>
<td><blockquote>
<p>PROVID AUTH DT</p>
</blockquote></td>
<td><blockquote>
<p>Date of current restriction invalid date</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="even">
<td>*#17</td>
<td><blockquote>
<p>NO BALANCE REC</p>
</blockquote></td>
<td><blockquote>
<p>Balance record data missing</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="odd">
<td>*#18</td>
<td><blockquote>
<p>ACCOUNT STATUS</p>
</blockquote></td>
<td><blockquote>
<p>Account status not (A),I,Blank=0</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="even">
<td>*#19</td>
<td><blockquote>
<p>PATIENT TYPE</p>
</blockquote></td>
<td><blockquote>
<p>Patient type not L,R,(U),X,Blank=197</p>
</blockquote></td>
<td>0</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 17%" />
<col style="width: 49%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>*#20</p>
</blockquote></th>
<th><blockquote>
<p>PAT TYPE/PHY</p>
</blockquote></th>
<th><blockquote>
<p>Patient type L or R without Phy name</p>
</blockquote></th>
<th><blockquote>
<p>5</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>*#21</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT STATUS</p>
</blockquote></td>
<td><blockquote>
<p>Patient Status not A,R,C,N,(X),Blank=722</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*#22</p>
</blockquote></td>
<td><blockquote>
<p>INDIGENT</p>
</blockquote></td>
<td><blockquote>
<p>Indigent status not (N),Y,Blank=722</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*#23</p>
</blockquote></td>
<td><blockquote>
<p>APPORTIONEE $</p>
</blockquote></td>
<td><blockquote>
<p>Apportionee amount &lt; $0 or &gt; $99,999</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*#24</p>
</blockquote></td>
<td><blockquote>
<p>GUARDIAN $</p>
</blockquote></td>
<td><blockquote>
<p>Guardian amount &lt; $0 or &gt; $99,999</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*#25</p>
</blockquote></td>
<td><blockquote>
<p>INSTITUT AWARD</p>
</blockquote></td>
<td><blockquote>
<p>Institutional award &lt; $0 or &gt; $99,999</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*#26</p>
</blockquote></td>
<td><blockquote>
<p>OTHER ASSETS</p>
</blockquote></td>
<td><blockquote>
<p>Other assets &lt; $0 or &gt; $99,999</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>66</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>January 18, 2007 <u>Appendix D. VistAMigrate Report Samples</u></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*#27</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>STORED BALANCE Stored balance &lt; $0 or &gt; $99,999</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*#28</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>STORED PRIVATE Stored private &lt; $0 or &gt; $99,999</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*#29</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>STORED GRATUIT Stored gratuitous &lt; $0 or &gt; $99,999</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*#30</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>RESTRCT MONTH Restricted Monthly &lt; $0 or &gt; $99,999</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*#31</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>RESTRCT WEEKLY Restricted Weekly &lt; $0 or &gt; $99,999</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*#32</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>RESTRCT AMT ER Restrict Mnthly amount &gt; (5X) weekly amt</p>
</blockquote></td>
<td><blockquote>
<p>32</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*#33</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>RESTRCT AMT ER Restrict Mnthly amount &lt; weekly amt</p>
</blockquote></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*#34</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>MINIMUM BAL Minimum balance #1 &lt; $0 or &gt; $99,999</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*#35</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>MAXIMUM BAL Maximum balance #1 &lt; $0 or &gt; $99,999</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*#36</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NO BALANCE REC Balance record missing for account</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*#37</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>INCOME PAYEE Income payee blank, Income source present</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*#38</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>INCOME AMOUNT Invalid income amount, Income source present</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*#39</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>INCOME AMOUNT Income amount &lt; $1 or &gt; $99,999</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*#40</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>INCOME FREQCY Income frequency not D,W,M,Y,X,V,O,Blank=5</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*#41</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>STATION ID Station ID blank or unassigned</p>
</blockquote></td>
<td><blockquote>
<p>863</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>#42</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>STATION ID Station ID invalid</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*#43</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SUSPENSE DATE Suspense date has invalid date</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*#44</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SUSPENSE ID Suspense ID has Invalid data</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*#45</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SUSPENSE TEXT Suspense text is &lt; 1 or &gt; 255 characters</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*#46</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DEFERRED TRANS There are 2 deferred transactions</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*#47</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>TRANSACTION ID Transaction ID mis-match with IEN</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*#48</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PATIENT NAME Patient name does not match deferred trans</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*#49</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PATIENT TRANS # Patient transaction # invalid</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*#50</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DEFR AMOUNT Deferred amount invalid</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*#51</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>TRANSACTN DATE Transaction date Invalid</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*#52</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DT TRAN ENTD Date transaction entered Invalid</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*#53</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>REFERENCE Reference Invalid &lt; 1 or &gt; 10 in length</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*#54</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DEPOSIT/WTHDRWL Deposit/Withdrawal status Invalid</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*#55</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CASH/CHECK/OTR Cash/Check/Other status Invalid</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*#56</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SOURCE Transaction source invalid</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*#57</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FORM Form does not match</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*#58</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PRVT SOURCE AMT Private source amount invalid or &lt; 0 or &gt; 99999</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*#59</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>GRATUITOUS AMT Gratuitous amount invalid or &lt; 0 or &gt; 99999</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>*#60</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PFUNDS CLERK PFunds clerk invalid</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
</tbody>
</table>

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

#### Detail

> The Detail report provides detail of each record in the Diagnostic Summary Report that contains an error. Use this information to diagnose the problem and locate the record containing the error so that you can correct it. The following is a sample portion of the M Diagnostic Detail report. For more information about the fields that are in the patient record, see Appendix C – Extraction File Layouts.

> STATION ID=442^ERR#=2^NAME=AAA_X,CXTHW_16481^DESC=Patient Name contains invalid data^VALUE=\>AAA_X,CXTHW\<

> STATION ID=442^ERR#=15^NAME=AAA_X,CXTHW_16481^DESC=Provider name contains invalid data^VALUE=\>:TUXRS,AHXYLUI H III\<

> STATION ID=442^ERR#=15^NAME=FAXEU,AHTADH GUHI_7184376^DESC=Provider name contains invalid data^VALUE=\>:TUXRS,AHXYLUI H III\<

> STATION ID=442^ERR#=15^NAME=SLWW,CDZZDH Y_2159^DESC=Provider name contains invalid data^VALUE=\>:TUXRS,AHXYLUI H III\<

> STATION ID=442^ERR#=20^NAME=LLBH,UDJELUI Q_11296^DESC=No Physician name for L or R^VALUE=\>R\<

> STATION ID=442^ERR#=23^NAME=LLBH,UDJELUI Q_11296^DESC=Apportionee \$ out of range either \< 0 or \>

> \$99,999.00^VALUE=\>110000\<

> STATION ID=442^ERR#=24^NAME=LLBH,UDJELUI Q_11296^DESC=Guardian \$ out of range either \< 0 or \>

> \$99,999.00^VALUE=\>120000\<

> STATION ID=442^ERR#=25^NAME=LLBH,UDJELUI Q_11296^DESC=Institutional award out of range either \< 0 or \> \$99,999.00^VALUE=\>130000\<

> (truncated)

> This page is intentionally blank.

### M Extract Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After you run the M Extract routine, the results of the extract routine are displayed in a flat file on the M Extract page as shown below. This flat file contains the following record types. The structure of each of these records is listed in Appendix C – Extraction File Layouts.

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 33%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>A1 - header</p>
<p>D1 - demographics 1 D2 - demographics 2 B1 - balance 1</p>
<p>B2 - balance 2</p>
</blockquote></th>
<th><blockquote>
<p>T1 - transaction 1 S1</p>
<p>- suspense 1</p>
<p>S2 - suspense 2 S3 - suspense 3 I1 - income 1</p>
</blockquote></th>
<th><blockquote>
<p>R1 - general remarks 1 R2 - general remarks 2 X1 - special remarks 1 X2 - special remarks 2</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> VPFS^442^(VER#4.9) RUN-DATE@TIME=FEB 27, 2006@10:30:18^^^0^A1^1006^3184^548539125 VPFS^442^22^666019138^1002052393V697258^1^D1^BLEU,CXEY P^666019138^2196665^^SS^123 EASY ST^BUILDING 1^Apartment 101^BOOMTOWN^27^54321^BRUIHSS,UXKHUS Z JR^442 VPFS^442^22^666019138^1002052393V697258^2^D2^22^I^L^N^N^999^888^777^6010^200^3000822^^1728 VPFS^442^22^666019138^1002052393V697258^3^B1^^^^0^0^0^100^25^3050600^964^0^0 VPFS^442^22^666019138^1002052393V697258^4^B2^20^10000^25^9999

> VPFS^442^22^666019138^1002052393V697258^5^I1^BOB JONES^JIM JONES^5^W VPFS^442^22^666019138^1002052393V697258^6^R1^GENERAL REMARKS LINE 1. AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA VPFS^442^22^666019138^1002052393V697258^7^R1^BBBBBBBBBBBBBBBBBBBBBBBBBBBB CCCCCCCCCCCCCCCCCC VPFS^442^22^666019138^1002052393V697258^8^R1^DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD VPFS^442^22^666019138^1002052393V697258^9^R1^GENERAL REMARKS LINE 2 FFFFFFFF FFFFFFFF GGGGGGG HHHHHHHH VPFS^442^22^666019138^1002052393V697258^10^R1^IIIIIIIIII JJJJJJJJ VPFS^442^22^666019138^1002052393V697258^11^X1^SPECIAL REMARKS AAAAAAAAAAAAAAAAAAAAAAAAAA BBBBBBBBB CCCCCCCCCCC

> VPFS^442^22^666019138^1002052393V697258^12^X1^DDDDDDDD EEEEEEEEEEEEEEE FFFFFFFFFFFFFFFFFFFFFFFFFF GGGGGGGGGGG HHHHHHHHHH VPFS^442^22^666019138^1002052393V697258^13^X1^

> VPFS^442^22^666019138^1002052393V697258^14^X1^SPECIALS REMARKS LINE 2 .............. MMMMMMMMMMMMM ,,,,,,,,,,,,

> VPFS^442^22^666019138^1002052393V697258^15^X1^DFDSFSDFSADF DFDFDFDFS

> (truncated)

> Appendix D. VistAMigrate Report Samples

> This page is intentionally blank.

### Stage Data Log File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Stage Data log file is generated by Oracle SQL\*Loader. This log will provide detail about any records that were rejected. (The middle of the log file has been truncated in this example.)

#### Top Portion

> SQL\*Loader: Release 10.2.0.1.0 - Production on Mon Feb 27 10:30:55 2006 Copyright (c) 1982, 2005, Oracle. All rights reserved.

> Control File: D:\vmdata\VPFS\CODE\vpfs_load_temp.ctl Data File: D:\vmdata\VPFS\442\vpfs_extraction.txt

> Bad File: D:\vmdata\VPFS\442\vpfs_stage.bad Discard File: none specified

> (Allow all discards)

> Number to load: ALL Number to skip: 0 Errors allowed: 50

> Bind array: 64 rows, maximum of 256000 bytes Continuation: none specified

> Path used: Conventional

> Table DM_A1, loaded when REC_TYPE = 0X4131(character 'A1') Insert option in effect for this table: APPEND

> TRAILING NULLCOLS option in effect

> Column Name Position Len Term Encl Datatype

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 13%" />
<col style="width: 1%" />
<col style="width: 11%" />
<col style="width: 1%" />
<col style="width: 5%" />
<col style="width: 1%" />
<col style="width: 4%" />
<col style="width: 1%" />
<col style="width: 4%" />
<col style="width: 1%" />
<col style="width: 24%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>APPLICATION_NM</p>
</blockquote></th>
<th></th>
<th></th>
<th>FIRST</th>
<th></th>
<th>10</th>
<th></th>
<th>^</th>
<th></th>
<th></th>
<th></th>
<th>CHARACTER</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>STATION_ID</p>
</blockquote></td>
<td></td>
<td></td>
<td>NEXT</td>
<td></td>
<td>10</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
<td><blockquote>
<p>EMPTY1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NEXT * ^</p>
</blockquote></td>
<td><blockquote>
<p>CHARACTER</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
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
<td><blockquote>
<p>(FILLER FIELD)</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EMPTY2</p>
</blockquote></td>
<td colspan="3">NEXT</td>
<td colspan="2">*</td>
<td colspan="2"><blockquote>
<p>^</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>CHARACTER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>(FILLER FIELD)</p>
</blockquote></td>
<td colspan="3"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="5"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EMPTY3</p>
</blockquote></td>
<td colspan="3">NEXT</td>
<td colspan="2">*</td>
<td colspan="2"><blockquote>
<p>^</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>CHARACTER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>(FILLER FIELD)</p>
</blockquote></td>
<td colspan="3"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="5"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>REC_NUM</p>
</blockquote></td>
<td colspan="3">NEXT</td>
<td colspan="2"><blockquote>
<p>10</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>^</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>CHARACTER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>REC_TYPE</p>
</blockquote></td>
<td colspan="3">NEXT</td>
<td colspan="2">2</td>
<td colspan="2"><blockquote>
<p>^</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>CHARACTER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NUM_PAT_ACCNTS</p>
</blockquote></td>
<td colspan="3">NEXT</td>
<td colspan="2"><blockquote>
<p>10</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>^</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>CHARACTER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NUM_RECS_IN_FILE</p>
</blockquote></td>
<td colspan="3">NEXT</td>
<td colspan="2">10</td>
<td colspan="2"><blockquote>
<p>^</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>CHARACTER</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Table DM_D1, loaded when REC_TYPE = 0X4431(character 'D1') Insert option in effect for this table: APPEND

> TRAILING NULLCOLS option in effect

> Column Name Position Len Term Encl Datatype

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 1%" />
<col style="width: 12%" />
<col style="width: 1%" />
<col style="width: 6%" />
<col style="width: 1%" />
<col style="width: 5%" />
<col style="width: 1%" />
<col style="width: 5%" />
<col style="width: 1%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>APPLICATION_NM</th>
<th></th>
<th>1</th>
<th></th>
<th>10</th>
<th></th>
<th>^</th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>CHARACTER</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>STATION_ID</td>
<td></td>
<td>NEXT</td>
<td></td>
<td>10</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
</tr>
<tr class="even">
<td>PAT_IEN</td>
<td></td>
<td>NEXT</td>
<td></td>
<td>15</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
</tr>
<tr class="odd">
<td>SSN</td>
<td></td>
<td>NEXT</td>
<td></td>
<td>10</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
</tr>
<tr class="even">
<td>PAT_ICN</td>
<td></td>
<td>NEXT</td>
<td></td>
<td>30</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
</tr>
<tr class="odd">
<td>REC_NUM</td>
<td></td>
<td>NEXT</td>
<td></td>
<td>10</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
</tr>
<tr class="even">
<td>REC_TYPE</td>
<td></td>
<td>NEXT</td>
<td></td>
<td>2</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
</tr>
<tr class="odd">
<td>FULL_NAME</td>
<td></td>
<td>NEXT</td>
<td></td>
<td>150</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
</tr>
<tr class="even">
<td>SSN1</td>
<td></td>
<td>NEXT</td>
<td></td>
<td>10</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
</tr>
<tr class="odd">
<td>DOB</td>
<td></td>
<td>NEXT</td>
<td></td>
<td>10</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
</tr>
<tr class="even">
<td>WARD</td>
<td></td>
<td>NEXT</td>
<td></td>
<td>30</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
</tr>
<tr class="odd">
<td>CLAIM_NBR</td>
<td></td>
<td>NEXT</td>
<td></td>
<td>11</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
</tr>
<tr class="even">
<td>ADDR1</td>
<td></td>
<td>NEXT</td>
<td></td>
<td>35</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
</tr>
<tr class="odd">
<td>ADDR2</td>
<td></td>
<td>NEXT</td>
<td></td>
<td>35</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
</tr>
<tr class="even">
<td>ADDR3</td>
<td></td>
<td>NEXT</td>
<td></td>
<td>35</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
</tr>
<tr class="odd">
<td>CITY</td>
<td></td>
<td>NEXT</td>
<td></td>
<td>50</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
</tr>
<tr class="even">
<td>STATE</td>
<td></td>
<td>NEXT</td>
<td></td>
<td>2</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
</tr>
<tr class="odd">
<td>ZIP</td>
<td></td>
<td>NEXT</td>
<td></td>
<td>35</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
</tr>
<tr class="even">
<td>PROV_NAME</td>
<td></td>
<td>NEXT</td>
<td></td>
<td>100</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
</tr>
</tbody>
</table>

> DIVISION_ID NEXT 10 ^ CHARACTER

> …………………………………………………………………………………………………………

> July 2020 71 Appendix D. VistAMigrate Report Samples

#### Bottom Portion

> …………………………………………………………………………………………………………………

> Table DM_S123, loaded when REC_TYPE = 0X5333(character 'S3') Insert option in effect for this table: APPEND

> TRAILING NULLCOLS option in effect

> Column Name Position Len Term Encl Datatype

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 13%" />
<col style="width: 1%" />
<col style="width: 11%" />
<col style="width: 1%" />
<col style="width: 5%" />
<col style="width: 1%" />
<col style="width: 4%" />
<col style="width: 1%" />
<col style="width: 4%" />
<col style="width: 1%" />
<col style="width: 23%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th>APPLICATION_NM</th>
<th></th>
<th></th>
<th>1</th>
<th></th>
<th>10</th>
<th></th>
<th>^</th>
<th></th>
<th></th>
<th></th>
<th>CHARACTER</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>STATION_ID</td>
<td></td>
<td></td>
<td>NEXT</td>
<td></td>
<td>10</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
<td></td>
</tr>
<tr class="even">
<td>PAT_IEN</td>
<td></td>
<td></td>
<td>NEXT</td>
<td></td>
<td>15</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
<td></td>
</tr>
<tr class="odd">
<td>SSN</td>
<td></td>
<td></td>
<td>NEXT</td>
<td></td>
<td>10</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
<td></td>
</tr>
<tr class="even">
<td>PAT_ICN</td>
<td></td>
<td></td>
<td>NEXT</td>
<td></td>
<td>30</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
<td></td>
</tr>
<tr class="odd">
<td>REC_NUM</td>
<td></td>
<td></td>
<td>NEXT</td>
<td></td>
<td>10</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
<td></td>
</tr>
<tr class="even">
<td>REC_TYPE</td>
<td></td>
<td></td>
<td>NEXT</td>
<td></td>
<td>2</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
<td></td>
</tr>
<tr class="odd">
<td><p>ITEM_ID</p>
<blockquote>
<p>NEXT 255 ^</p>
</blockquote></td>
<td><blockquote>
<p>CHARACTER</p>
</blockquote></td>
<td></td>
<td>NEXT</td>
<td></td>
<td>50</td>
<td></td>
<td>^</td>
<td></td>
<td></td>
<td></td>
<td>CHARACTER</td>
<td><blockquote>
<p>ITEM_DESC</p>
</blockquote></td>
</tr>
</tbody>
</table>

> value used for ROWS parameter changed from 64 to 49

> Record 42: Rejected - Error on table DM_S123, column STATION_ID. Field in data file exceeds maximum length

> Record 43: Rejected - Error on table DM_S123, column APPLICATION_NM. Field in data file exceeds maximum length

> Record 45: Discarded - failed all WHEN clauses.

> Record 47: Rejected - Error on table DM_S123, column STATION_ID. Field in data file exceeds maximum length

> Record 49: Discarded - failed all WHEN clauses. Record 51: Discarded - failed all WHEN clauses.

> Record 53: Rejected - Error on table DM_S123, column STATION_ID. Field in data file exceeds maximum length

> Table DM_A1:

> 1 Row successfully loaded.

> 0 Rows not loaded due to data errors.

> 3191 Rows not loaded because all WHEN clauses were failed.

> 0 Rows not loaded because all fields were null.

> Table DM_D1:

> 1006 Rows successfully loaded.

> 0 Rows not loaded due to data errors.

> 2186 Rows not loaded because all WHEN clauses were failed.

> 0 Rows not loaded because all fields were null.

> Table DM_D2:

> 1006 Rows successfully loaded.

> 0 Rows not loaded due to data errors.

> 2186 Rows not loaded because all WHEN clauses were failed.

> 0 Rows not loaded because all fields were null.

> Table DM_B1:

> 1006 Rows successfully loaded.

> 0 Rows not loaded due to data errors.

> 2186 Rows not loaded because all WHEN clauses were failed.

> 0 Rows not loaded because all fields were null.

> Table DM_B2:

> 15 Rows successfully loaded.

> 0 Rows not loaded due to data errors.

> 3177 Rows not loaded because all WHEN clauses were failed.

> 0 Rows not loaded because all fields were null.

> Table DM_I1:

> 15 Rows successfully loaded.

> 0 Rows not loaded due to data errors.

> 3177 Rows not loaded because all WHEN clauses were failed.

> 0 Rows not loaded because all fields were null.

> Table DM_R1_R2:

> 72 Rows successfully loaded.

> 0 Rows not loaded due to data errors.

> 3120 Rows not loaded because all WHEN clauses were failed.

> 0 Rows not loaded because all fields were null.

> Table DM_R1_R2:

#### July 2020 Appendix D. VistAMigrate Report Samples

> 0 Rows successfully loaded.

> 0 Rows not loaded due to data errors.

> 3192 Rows not loaded because all WHEN clauses were failed.

> 0 Rows not loaded because all fields were null.

> Table DM_X1_X2:

> 24 Rows successfully loaded.

> 0 Rows not loaded due to data errors.

> 3168 Rows not loaded because all WHEN clauses were failed.

> 0 Rows not loaded because all fields were null.

> Table DM_X1_X2:

> 0 Rows successfully loaded.

> 0 Rows not loaded due to data errors.

> 3192 Rows not loaded because all WHEN clauses were failed.

> 0 Rows not loaded because all fields were null.

> Table DM_T1:

> 2 Rows successfully loaded.

> 0 Rows not loaded due to data errors.

> 3190 Rows not loaded because all WHEN clauses were failed.

> 0 Rows not loaded because all fields were null.

> Table DM_S123:

> 9 Rows successfully loaded.

> 0 Rows not loaded due to data errors.

> 3183 Rows not loaded because all WHEN clauses were failed.

> 0 Rows not loaded because all fields were null.

> Table DM_S123:

> 29 Rows successfully loaded.

> 4 Rows not loaded due to data errors.

> 3159 Rows not loaded because all WHEN clauses were failed.

> 0 Rows not loaded because all fields were null.

> Table DM_S123:

> 0 Rows successfully loaded.

> 0 Rows not loaded due to data errors.

> 3192 Rows not loaded because all WHEN clauses were failed.

> 0 Rows not loaded because all fields were null.

> Space allocated for bind array: 255094 bytes(49 rows) Read buffer bytes: 1048576

> Total logical records skipped: 0

> Total logical records read: 3192

> Total logical records rejected: 4

> Total logical records discarded: 3

> Run began on Mon Feb 27 10:30:55 2006

> Run ended on Mon Feb 27 10:30:56 2006

> Elapsed time was: 00:00:01.24 CPU time was: 00:00:00.32

#### Stage Data Bad File

> The Stage Data “Bad” file contains the raw records from the extract file that could not be staged. Use this file in conjunction with the Stage Data log file to determine what data is causing any rejected records.

> IF ITEM^THIS IS TEXT FO R A SEPERATE ITEM

> IF ITEM^THERE IS A BLANK LINE BEFORE THIS ONE

> IF ITEM^THIS IS A SEPERATE ITEM TEXT ENTERY WITH 2 BLANK LINES BEFORE IT.

> Appendix D*.* VistAMigrate Report Samples

> This page is intentionally blank.

### Analyze Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Analyze Data Report contains detail for any patient records containing warnings or errors.

> ================== VPFS - Analyze Report for Station 442 on 02/27/2006 10:02 AM ===================

> ===================================================================================================

> =========================================== BLANK NAME ============================================

> ===================================================================================================

> Rule: The Patient Name field cannot be blank.

> SSN FULL NAME IEN REC_NUM

> ---------- ------------------------------ --------------- -------- 666024936

> NAME-MISSING-SSN#666024936 39665 2886

> 1 row created.

> ===================================================================================================

> ========================================== INVALID NAME ===========================================

> ===================================================================================================

> Rule: The Patient Name field must be between 3 and 30 characters. no rows selected

> 0 rows created.

> ===================================================================================================

> ============================================ BLANK SSN ============================================

> ===================================================================================================

> Rule: The SSN field cannot be blank. no rows selected

> 0 rows created.

> ===================================================================================================

> =========================================== INVALID SSN ===========================================

> ===================================================================================================

> Rule: The SSN field must be 9 digits. An optional 10th character 'P' is allowed (for pseudo-SSN). no rows selected

> 0 rows created.

> ================

> ================

> ================

> ================

> ================

> ================

> ===

> ================================== DUPLICATE SSN (THIS STATION) ===================================

> ===================================================================================================

> Rule: Duplicate SSNs are not allowed. (Check within data for this station.) no rows selected

> 0 rows created.

> ===================================================================================================

> =================================== DUPLICATE SSN (ANY STATION) ===================================

> ===================================================================================================

> Rule: Duplicate SSNs are not allowed. (Check within data at any station.) no rows selected

1.  rows created.

> ===================================================================================================

> ====================================== PSEUDO SSN (WARNING) =======================================

> ===================================================================================================

> Rule: The SSN field contains a pseudo-SSN value (10th character is a 'P'). no rows selected

> ===================================================================================================

> =========================================== INVALID ICN ===========================================

> ===================================================================================================

> Rule: The ICN field must be between 1 to 10 digits, optionally followed by a 'V' and a 6 digit checksum. An additional 6 digit prefix and 6 digit suffix are also allowed for future use.

> SSN IEN REC_NUM PAT_ICN

> ---------- -------- -------- ------------------------------ 666000363 29534 2393 -1

2.  row created.

> ===================================================================================================

> ================================== DUPLICATE ICN (THIS STATION) ===================================

> ===================================================================================================

> Rule: Duplicate ICNs are not allowed. (Check within data for this station.) no rows selected

> 0 rows created.

> ===================================================================================================

> =================================== DUPLICATE ICN (ANY STATION) ===================================

> ===================================================================================================

> Rule: Duplicate ICNs are not allowed. (Check within data at any station.) no rows selected

> 0 rows created.

> ===================================================================================================

> ======================================== BLANK BIRTH DATE =========================================

> ===================================================================================================

> Rule: The DOB field cannot be blank. no rows selected

> 0 rows created.

> ===================================================================================================

> ======================================= INVALID BIRTH DATE ========================================

> ===================================================================================================

> Rule: The DOB field must be a valid VistA date. (Imprecise dates are allowed.) no rows selected

> 0 rows created.

> \>\> 0 records with an imprecise date of birth will be set to the first day of the month/year.

> ===================================================================================================

> ======================================= INVALID WARD LENGTH =======================================

> ===================================================================================================

> Rule: The Ward field must be between 2 and 30 characters. no rows selected

> 0 rows created.

> ===================================================================================================

> ====================================== INVALID CLAIM NUMBER =======================================

> ===================================================================================================

> Rule: The Claim Number field must be between 7 and 9 digits or 'SS'. no rows selected

> 0 rows created.

> ===================================================================================================

> =================================== INVALID ACCOUNT STATUS TYPE ===================================

> ===================================================================================================

> Rule: The Account Status field must be an 'A' or 'I'. (Blanks will be set to 'A'.) no rows selected

> 0 rows created.

> \>\> 0 records with a blank account status will be set to A (Active).

> ===================================================================================================

> ====================================== INVALID PATIENT TYPE =======================================

> ===================================================================================================

> Rule: The Patient Type field must be 'L', 'R', 'U', or 'X'. (Blanks will be set to 'U'.) no rows selected

> 0 rows created.

> \>\> 197 records with a blank patient type will be set to U (Unknown).

> ===================================================================================================

> ================================ BLANK PROVIDER (FOR L/R PATIENTS) ================================

> ===================================================================================================

> Rule: The Provider Name field cannot be blank for type 'L' or 'R' patients.

666046008

> 5 rows created.

> ===================================================================================================

> ====================================== INVALID PROVIDER NAME ======================================

> ===================================================================================================

> Rule: The Provider Name field must be between 3 and 30 characters. no rows selected

> 0 rows created.

> ===================================================================================================

> ======================== BLANK CURRENT RESTRICTION DATE (FOR L/R PATIENTS) ========================

> ===================================================================================================

> Rule: The Current Restriction Date field cannot be blank for type 'L' or 'R' patients.

> CURRENT RESTR

| SSN       |     | IEN   |     | REC_NUM |     | PAT TYPE DATE |
|-----------|-----|-------|-----|---------|-----|---------------|
| 666019008 |     | 22    |     | 1       |     | L             |
| 666023064 |     | 16481 |     | 1338    |     | R             |
| 666026702 |     | 24966 |     | 1975    |     | R             |
| 666026849 |     | 20598 |     | 1625    |     | R             |
| 666028954 |     | 16490 |     | 1346    |     | R             |
| 666035039 |     | 23846 |     | 1914    |     | R             |

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 28%" />
<col style="width: 24%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>666046598</p>
</blockquote></th>
<th><blockquote>
<p>37939</p>
</blockquote></th>
<th><blockquote>
<p>2852</p>
</blockquote></th>
<th>R</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>666054826</p>
</blockquote></td>
<td><blockquote>
<p>11081</p>
</blockquote></td>
<td><blockquote>
<p>981</p>
</blockquote></td>
<td>R</td>
</tr>
<tr class="even">
<td><blockquote>
<p>666067730</p>
</blockquote></td>
<td><blockquote>
<p>29192</p>
</blockquote></td>
<td><blockquote>
<p>2348</p>
</blockquote></td>
<td>R</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666067760</p>
</blockquote></td>
<td><blockquote>
<p>7174481</p>
</blockquote></td>
<td><blockquote>
<p>3106</p>
</blockquote></td>
<td>R</td>
</tr>
</tbody>
</table>

> 10 rows selected.

> 10 rows created.

> ===================================================================================================

> ================================ INVALID CURRENT RESTRICTION DATE =================================

> ===================================================================================================

> Rule: The Current Restriction Date field must be a valid VistA date. (Imprecise dates are NOT allowed.) no rows selected

> 0 rows created.

> ===================================================================================================

> ===================================== INVALID PATIENT STATUS ======================================

> ===================================================================================================

> Rule: The Patient Type field must be 'A', 'N', 'R', 'C', or 'X'. (Blanks will be set to 'X'.) no rows selected

> 0 rows created.

> \>\> 722 records with a blank patient status will be set to X (Unknown).

> ===================================================================================================

> ========================================= INDIGENT CHECK ==========================================

> ===================================================================================================

> Rule: The Indigent field must be 'Y', or 'N'. (Blanks will be set to 'N'.) no rows selected

> 0 rows created.

> \>\> 722 records with a blank indigent status will be set to N (No).

> ===================================================================================================

> =================================== INVALID APPORTIONEE AMOUNT ====================================

> ===================================================================================================

> Rule: The Apportionee Amount cannot be less than 0. Amounts over 99,999 are displayed as warnings.

> APPORTIONEE SSN IEN REC_NUM AMOUNT

> 666010001 11296 995 110000 666010004

> 2236 347 110000

> 0 rows created.

> ===================================================================================================

> ===================================== INVALID GUARDIAN AMOUNT =====================================

> ===================================================================================================

> Rule: The Guardian Amount cannot be less than 0. Amounts over 99,999 are displayed as warnings.

> GUARDIAN SSN IEN REC_NUM AMOUNT

> 666010001 11296 995 120000 666000024

> 2236 347 110000

> 0 rows created.

> ================

> ================

> ================

> ================

> ================

> ================

> ===

> =============================== INVALID INSTITUTIONAL AWARD AMOUNT ================================

> ===================================================================================================

> Rule: The Inst. Award Amount cannot be less than 0. Amounts over 99,999 are displayed as warnings.

> INSTITUTIONAL SSN IEN REC_NUM AWARD AMOUNT

> 666012000 11296 995 130000 666010000

> 2236 347 141000

> 0 rows created.

> ===================================================================================================

> =================================== INVALID OTHER ASSETS AMOUNT ===================================

> ===================================================================================================

> Rule: The Other Assets Amount cannot be less than 0. Amounts over 99,999 are displayed as warnings.

> OTHER ASSETS SSN IEN REC_NUM AMOUNT

> ---------- -------- -------- ------------ 666066664

> 2236 347 140000

1.  rows created.

> ===================================================================================================

> ======================================== INVALID BALANCES =========================================

> ===================================================================================================

> Rule: The Account Balances cannot be less than 0. Balances over 99,999 are displayed as warnings. The Stored Balance must also equal the sum of the Private and Gratuitous Balances.

666066683

2.  row created.

> 0 rows created.

1.  rows created.
2.  row created.

> ==============================================================================

> =====================

> =============================== INVALID RESTRICTED BALANCES/LIMITS ================================

> ===================================================================================================

> Rule: The Restriction Balances or Limits cannot be less than 0 or more than 99,999. The Monthly Limit cannot be less than the Weekly Limit.

> Monthly Limits less than 5x the Weekly Limits are displayed as warnings.

> MONTHLY WEEKLY MONTHLY WEEKLY RESTRICTION RESTRICTION RESTRICTED RESTRICTED

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 1%" />
<col style="width: 9%" />
<col style="width: 1%" />
<col style="width: 9%" />
<col style="width: 1%" />
<col style="width: 14%" />
<col style="width: 1%" />
<col style="width: 14%" />
<col style="width: 1%" />
<col style="width: 14%" />
<col style="width: 1%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SSN</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>IEN</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>REC_NUM</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>BALANCE</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>BALANCE</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>LIMIT</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>LIMIT</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>666010666</p>
</blockquote></td>
<td></td>
<td>367</td>
<td></td>
<td>88</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>50</td>
<td></td>
<td>250</td>
</tr>
<tr class="even">
<td><blockquote>
<p>666010009</p>
</blockquote></td>
<td></td>
<td>1647</td>
<td></td>
<td>249</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>20</td>
<td></td>
<td>5</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666010537</p>
</blockquote></td>
<td></td>
<td>3959</td>
<td></td>
<td>562</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>60.00</td>
<td></td>
<td>15.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>666010008</p>
</blockquote></td>
<td></td>
<td>2254</td>
<td></td>
<td>354</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>60</td>
<td></td>
<td>15</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666011007</p>
</blockquote></td>
<td></td>
<td>330</td>
<td></td>
<td>76</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>60.00</td>
<td></td>
<td>15.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>666010011</p>
</blockquote></td>
<td></td>
<td>11296</td>
<td></td>
<td>996</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>200</td>
<td></td>
<td>500</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666018770</p>
</blockquote></td>
<td></td>
<td>3402</td>
<td></td>
<td>484</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>100</td>
<td></td>
<td>25</td>
</tr>
<tr class="even">
<td><blockquote>
<p>666015802</p>
</blockquote></td>
<td></td>
<td>3008</td>
<td></td>
<td>451</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>125</td>
<td></td>
<td>30</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666015870</p>
</blockquote></td>
<td></td>
<td>3590</td>
<td></td>
<td>502</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>60.00</td>
<td></td>
<td>15.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>666015888</p>
</blockquote></td>
<td></td>
<td>578</td>
<td></td>
<td>126</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>200</td>
<td></td>
<td>250</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666019102</p>
</blockquote></td>
<td></td>
<td>2320</td>
<td></td>
<td>361</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>60.00</td>
<td></td>
<td>15.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>666019198</p>
</blockquote></td>
<td></td>
<td>2812</td>
<td></td>
<td>423</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>200</td>
<td></td>
<td>50</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666019889</p>
</blockquote></td>
<td></td>
<td>22</td>
<td></td>
<td>3</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>100</td>
<td></td>
<td>25</td>
</tr>
<tr class="even">
<td><blockquote>
<p>666019624</p>
</blockquote></td>
<td></td>
<td>2236</td>
<td></td>
<td>348</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>5000</td>
<td></td>
<td>9000</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666022222</p>
</blockquote></td>
<td></td>
<td>17685</td>
<td></td>
<td>1425</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>60.00</td>
<td></td>
<td>15.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>666022238</p>
</blockquote></td>
<td></td>
<td>3600</td>
<td></td>
<td>510</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>60.00</td>
<td></td>
<td>15.00</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666023331</p>
</blockquote></td>
<td></td>
<td>2159</td>
<td></td>
<td>332</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>100</td>
<td></td>
<td>25</td>
</tr>
<tr class="even">
<td><blockquote>
<p>666024444</p>
</blockquote></td>
<td></td>
<td>16481</td>
<td></td>
<td>1340</td>
<td></td>
<td>75</td>
<td></td>
<td>75</td>
<td></td>
<td>200</td>
<td></td>
<td>50</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666025515</p>
</blockquote></td>
<td></td>
<td>2244</td>
<td></td>
<td>351</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>100</td>
<td></td>
<td>500</td>
</tr>
<tr class="even">
<td><blockquote>
<p>666026766</p>
</blockquote></td>
<td></td>
<td>24966</td>
<td></td>
<td>1977</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>120</td>
<td></td>
<td>30</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666026665</p>
</blockquote></td>
<td></td>
<td>20598</td>
<td></td>
<td>1627</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>60</td>
<td></td>
<td>15</td>
</tr>
<tr class="even">
<td><blockquote>
<p>666035556</p>
</blockquote></td>
<td></td>
<td>23846</td>
<td></td>
<td>1916</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>20</td>
<td></td>
<td>35</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666040665</p>
</blockquote></td>
<td></td>
<td>13246</td>
<td></td>
<td>1123</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>60.00</td>
<td></td>
<td>15.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>666045445</p>
</blockquote></td>
<td></td>
<td>27228</td>
<td></td>
<td>2094</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>100</td>
<td></td>
<td>25</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666044562</p>
</blockquote></td>
<td></td>
<td>13021</td>
<td></td>
<td>1092</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>200</td>
<td></td>
<td>50</td>
</tr>
<tr class="even">
<td><blockquote>
<p>666049766</p>
</blockquote></td>
<td></td>
<td>19138</td>
<td></td>
<td>1524</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>60.00</td>
<td></td>
<td>15.00</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666054826</p>
</blockquote></td>
<td></td>
<td>11081</td>
<td></td>
<td>983</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>100</td>
<td></td>
<td>25</td>
</tr>
<tr class="even">
<td><blockquote>
<p>666058514</p>
</blockquote></td>
<td></td>
<td>25391</td>
<td></td>
<td>2000</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>60.00</td>
<td></td>
<td>15.00</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666065772</p>
</blockquote></td>
<td></td>
<td>30958</td>
<td></td>
<td>2520</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>60.00</td>
<td></td>
<td>15.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>666067430</p>
</blockquote></td>
<td></td>
<td>29192</td>
<td></td>
<td>2350</td>
<td></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td>100</td>
<td></td>
<td>25</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666067760</p>
</blockquote></td>
<td></td>
<td>7174481</td>
<td></td>
<td>3108</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>20</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>25</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="5"><blockquote>
<p>666085822 7184376 3176</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>0</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>0</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>100</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>25</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 32 rows selected.

> 0 rows created.

> 0 rows created.

> 0 rows created.

> 0 rows created.

> 7 rows created.

> ===================================================================================================

> ==================================== INVALID MIN/MAX BALANCES =====================================

> ===================================================================================================

> Rule: The Min / Max Balances cannot be less than 0. Balances over 99,999 are displayed as warnings.

MIN MAX

BALANCE BALANCE

SSN IEN REC_NUM ONE ONE

> 27625 2140 110000 190000

> 0 rows created.

> 0 rows created.

> ===================================================================================================

> ===================================== MISSING BALANCE RECORD ======================================

> ===================================================================================================

> Rule: The Balance Record (B1) is missing. no rows selected

1.  rows created.

> ===================================================================================================

> ======================================= BLANK INCOME PAYEE ========================================

> ===================================================================================================

> Rule: The Income Source Payee field cannot be blank.

> SSN IEN REC_NUM INCOME_SOURCE PAYEE 7174481 3111 new

> 666051920

> 666067760

2.  row created.

> ===================================================================================================

> ======================================= BLANK INCOME AMOUNT =======================================

> ===================================================================================================

> Rule: The Income Amount field cannot be blank.

INCOME

SSN IEN REC_NUM INCOME_SOURCE AMOUNT

> 666013608 5531 685 SELF 1 row created.

> ===================================================================================================

> ====================================== INVALID INCOME AMOUNT ======================================

> ===================================================================================================

> Rule: The Income Amount cannot be less than 0. Amounts over 99,999 are displayed as warnings. no rows selected

> 0 rows created.

> ===================================================================================================

> ===================================== INVALID FREQUENCY CODE ======================================

> ===================================================================================================

> Rule: The Frequency Code field must be 'D', 'W', 'M', 'Y', 'X', 'V', 'O', or blank. no rows selected

> 0 rows created.

> ===================================================================================================

> ======================================== BLANK STATION ID =========================================

> ===================================================================================================

> Rule: The Station ID field cannot be blank. no rows selected

> 0 rows created.

> ===================================================================================================

> ======================================= INVALID STATION ID ========================================

> ===================================================================================================

> Rule: The Station ID field must be the station being migrated (e.g. 442) or a child of that station (e.g. 4429AA).

666049465

> 27228 VPFSPATIENT,4 656

> 4 rows created.

> =================================================================================================== =============================== PATIENT COUNTS BY STATION ID (INFO) ===============================

> ===================================================================================================

> Information Only: Display the number of patients at each station present in this migration.

<table>
<colgroup>
<col style="width: 74%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>STATION ID</th>
<th>COUNT</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>442</td>
<td>995</td>
</tr>
<tr class="even">
<td>4429AA</td>
<td>7</td>
</tr>
<tr class="odd">
<td>512</td>
<td>1</td>
</tr>
<tr class="even">
<td>656</td>
<td>1</td>
</tr>
<tr class="odd">
<td>6569AA</td>
<td>1</td>
</tr>
<tr class="even">
<td><blockquote>
<p>679</p>
</blockquote>
<p>6 rows selected.</p></td>
<td>1</td>
</tr>
</tbody>
</table>

> ===================================================================================================

> ===================================== INVALID GENERAL REMARKS =====================================

> ===================================================================================================

> Rule: The General Remarks field cannot be more than 2000 characters (will be truncated to 2000 char.). no rows selected

> ===================================================================================================

> ===================================== INVALID SPECIAL REMARKS =====================================

> ===================================================================================================

> Rule: The Special Remarks field cannot be more than 2000 characters (will be truncated to 2000 char.). no rows selected

> ===================================================================================================

> ====================================== INVALID SUSPENSE DATE ======================================

> ===================================================================================================

> Rule: The Suspense Date field must be a valid VistA date. (Imprecise dates and blanks are NOT allowed.) no rows selected

> 0 rows created.

> ===================================================================================================

> ======================================== BLANK SUSPENSE ID ========================================

> ===================================================================================================

> Rule: The Suspense ID field cannot be blank. no rows selected

> 0 rows created.

> ===================================================================================================

> ======================================= BLANK SUSPENSE TEXT =======================================

> ===================================================================================================

> Rule: The Suspense Text field cannot be blank.

> SUSPENSE SUSPENSE SUSPENSE

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 1%" />
<col style="width: 8%" />
<col style="width: 1%" />
<col style="width: 8%" />
<col style="width: 1%" />
<col style="width: 33%" />
<col style="width: 1%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>SSN</th>
<th></th>
<th>IEN</th>
<th></th>
<th>DATE</th>
<th></th>
<th>ID</th>
<th></th>
<th>TEXT</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>666017673</td>
<td></td>
<td>148</td>
<td></td>
<td></td>
<td></td>
<td>HERE IS A D</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>666017673</td>
<td></td>
<td>148</td>
<td></td>
<td></td>
<td></td>
<td>HERE IS A D</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>666017673</td>
<td></td>
<td>148</td>
<td></td>
<td></td>
<td></td>
<td>HERE IS A D</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>666017673</td>
<td></td>
<td>148</td>
<td></td>
<td></td>
<td></td>
<td>HERE IS A D</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>666017673</td>
<td></td>
<td>148</td>
<td></td>
<td></td>
<td></td>
<td>HERE IS A D</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>666017673</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>148</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>HERE IS A D</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> 6 rows selected.

> 1 row created.

> ===================================================================================================

> ====================================== INVALID SUSPENSE ITEM ======================================

> ===================================================================================================

> Rule: Ensure the necessary records exist to build a complete suspense item (minimum of 1 S1 and 1 S2). Suspense Items (S2) without a corresponding Suspense Date (S1)

> no rows selected

> Suspense Text (S3) without a corresponding Suspense Item (S2) no rows selected

> 0 rows created.

> 0 rows created.

> ===================================================================================================

> =================================== INVALID TRANSACTION AMOUNTS ===================================

> ===================================================================================================

> Rule: The Transaction Amounts cannot be less than 0 or more than 99,999. The Transaction Amount cannot be blank, and one of either the Private Amount or Gratuitous Amount must not be blank.

> The Transaction Amount must also equal the sum of the Private Source and Gratuitous Amounts. no rows selected

> 0 rows created.

> 0 rows created.

> 0 rows created.

> 0 rows created.

> 0 rows created.

> ===================================================================================================

> ================================== INVALID LAST TRANSACTION DATE ==================================

> ===================================================================================================

> Rule: The Last Transaction Date field must be a valid VistA date. (Imprecise dates are NOT allowed.) no rows selected

> 0 rows created.

> ===================================================================================================

> ====================================== INVALID DEFERRAL DATE ======================================

> ===================================================================================================

> Rule: The Deferral Date field must be a valid VistA date. (Imprecise dates and blanks are NOT allowed.) no rows selected

> 0 rows created.

> ===================================================================================================

> ==================================== INVALID TRANSACTION DATE =====================================

> ===================================================================================================

> Rule: The Transaction Date field must be a valid VistA date. (Imprecise dates and blanks are NOT allowed.) no rows selected

> 0 rows created.

> ===================================================================================================

> ================================ INVALID TRANSACTION ENTERED DATE =================================

> ===================================================================================================

> Rule: The Transaction Entered Date field must be a valid VistA date. (Imprecise dates and blanks are NOT allowed.) no rows selected

> 0 rows created.

> =================================================================================================== ======================================== INVALID REFERENCE ========================================

> ===================================================================================================

> Rule: The Reference field must be between 1 and 10 characters and cannot be blank. no rows selected

> 0 rows created.

> ===================================================================================================

> ================================= INVALID DEPOSIT/WITHDRAWAL CODE =================================

> ===================================================================================================

> Rule: The Deposit/Withdrawal Code field must be 'D' or 'W'.

> no rows selected

> 0 rows created.

> ===================================================================================================

> ================================= INVALID CASH/CHECK/OTHER STATUS =================================

> ===================================================================================================

> Rule: The Cash/Check/Other Code field must be '1', '2', or '3'. no rows selected

> 0 rows created.

> ===================================================================================================

> ========================================= INVALID SOURCE ==========================================

> ===================================================================================================

> Rule: The Source Code field must be 'P', 'G', or 'B'. no rows selected

> 0 rows created.

> ===================================================================================================

> ========================================== INVALID FORM ===========================================

> ===================================================================================================

> Rule: The Form field cannot be blank. Form values not in the standard Forms list are displayed as warnings. no rows selected

> 0 rows created.

> ================

> ================

> ================

> ================

> ================

> ================

> ===

> =================================== INVALID PATIENT FUNDS CLERK ===================================

> ===================================================================================================

> Rule: The Patient Funds Clerk field must be between 3 and 35 characters and cannot be blank.

> no rows selected

> 0 rows created.

> ===================================================================================================

> ================================= NON-DEPOSIT TRANSACTIONS (INFO) =================================

> ===================================================================================================

> Information Only:

> no rows selected

> ===================================================================================================

> =================================== ACTIVE ZERO BALANCES (INFO) ===================================

> ===================================================================================================

> Information Only:

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 1%" />
<col style="width: 11%" />
<col style="width: 1%" />
<col style="width: 14%" />
<col style="width: 1%" />
<col style="width: 17%" />
<col style="width: 1%" />
<col style="width: 17%" />
<col style="width: 1%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th>SSN</th>
<th></th>
<th>IEN</th>
<th></th>
<th>ACCOUNT STATUS</th>
<th></th>
<th><blockquote>
<p>STORED BALANCE</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>PRIVATE SOURCE STORED BALANCE</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>GRATUITOUS</p>
<p>SOURCE STORED BALANCE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>666011585</td>
<td></td>
<td>32300</td>
<td></td>
<td>A</td>
<td></td>
<td>$.00</td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td>666015806</td>
<td></td>
<td>1186</td>
<td></td>
<td>A</td>
<td></td>
<td>$.00</td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>666017673</td>
<td></td>
<td>148</td>
<td></td>
<td>A</td>
<td></td>
<td>NaN</td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$1,400.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td>666019238</td>
<td></td>
<td>507</td>
<td></td>
<td>A</td>
<td></td>
<td>$.00</td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>666019624</td>
<td></td>
<td>2236</td>
<td></td>
<td>A</td>
<td></td>
<td>$.00</td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td>666022238</td>
<td></td>
<td>3600</td>
<td></td>
<td>A</td>
<td></td>
<td>$.00</td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>666039076</td>
<td></td>
<td>24254</td>
<td></td>
<td>A</td>
<td></td>
<td>$.00</td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td>666047363</td>
<td></td>
<td>29534</td>
<td></td>
<td>A</td>
<td></td>
<td>$.00</td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>666048128</td>
<td></td>
<td>22668</td>
<td></td>
<td>A</td>
<td></td>
<td>$.00</td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td>666048595</td>
<td></td>
<td>16528</td>
<td></td>
<td>A</td>
<td></td>
<td>$.00</td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>666049742</td>
<td></td>
<td>19138</td>
<td></td>
<td>A</td>
<td></td>
<td>$.00</td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td>666051920</td>
<td></td>
<td>27625</td>
<td></td>
<td>A</td>
<td></td>
<td>$.00</td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>666052928</td>
<td></td>
<td>28582</td>
<td></td>
<td>A</td>
<td></td>
<td>$.00</td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 666061997 27972 A \$.00 \$.00 \$.00

> 14 rows selected.

> ===================================================================================================

> ============================ DEFERRED TRANSACTIONS BALANCE LIST (INFO) ============================

> ===================================================================================================

> Information Only:

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 34%" />
<col style="width: 29%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>PRIVATE</th>
<th>GRATUITOUS</th>
<th colspan="2"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SOURCE</td>
<td>SOURCE</td>
<td><blockquote>
<p>PRIVATE</p>
</blockquote></td>
<td><blockquote>
<p>GRATUITOUS</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 24%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>BALANCE</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>BALANCE</p>
</blockquote></th>
<th><blockquote>
<p>STORED BALANCE</p>
</blockquote></th>
<th><blockquote>
<p>STORED</p>
<p>AMT</p>
</blockquote></th>
<th><blockquote>
<p>STORED</p>
<p>AMT</p>
</blockquote></th>
<th><blockquote>
<p>TRANS</p>
<p>AMT</p>
</blockquote></th>
<th><blockquote>
<p>TRANS</p>
</blockquote></th>
<th>TRANS</th>
<th>SSN</th>
<th><blockquote>
<p>IEN</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>666035039</p>
</blockquote></td>
<td></td>
<td>23846</td>
<td><blockquote>
<p>$200.00</p>
</blockquote></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td><blockquote>
<p>$200.00</p>
</blockquote></td>
<td><blockquote>
<p>$200.00</p>
</blockquote></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td>$200.00</td>
<td colspan="2"><blockquote>
<p>666084319</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7179975</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$10.00</p>
</blockquote></td>
<td><blockquote>
<p>$10.00</p>
</blockquote></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td><blockquote>
<p>$10.00</p>
</blockquote></td>
<td><blockquote>
<p>$10.00</p>
</blockquote></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
</tbody>
</table>

> ===================================================================================================

> ====================== NON-ZERO BALANCE WITH NO DEFERRED TRANSACTIONS (INFO) ======================

> ===================================================================================================

> Information Only:

<table style="width:100%;">
<colgroup>
<col style="width: 17%" />
<col style="width: 15%" />
<col style="width: 1%" />
<col style="width: 20%" />
<col style="width: 1%" />
<col style="width: 20%" />
<col style="width: 1%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>SSN</th>
<th><blockquote>
<p>IEN</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>STORED BALANCE</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>PRIVATE SOURCE STORED BALANCE</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>GRATUITOUS</p>
<p>SOURCE STORED BALANCE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>666010088</td>
<td><blockquote>
<p>367</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$190.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$190.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td>666010653</td>
<td><blockquote>
<p>8339</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$809,000.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$809,000.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>666017766</td>
<td><blockquote>
<p>2344</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$275.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$275.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td>666012511</td>
<td><blockquote>
<p>11296</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$10.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$10.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>666016543</td>
<td><blockquote>
<p>201</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$100.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$100.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td>666014577</td>
<td><blockquote>
<p>3402</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$64.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$14.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$50.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>666022277</td>
<td>16683</td>
<td></td>
<td><blockquote>
<p>$110.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$110.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td>666028791</td>
<td><blockquote>
<p>2159</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$805.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$805.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>666098000</td>
<td><blockquote>
<p>16481</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$35.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$35.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td>666020000</td>
<td>7173155</td>
<td></td>
<td><blockquote>
<p>$90.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$90.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>666024315</td>
<td><blockquote>
<p>2244</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$130.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$130.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td>666025116</td>
<td><blockquote>
<p>19626</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$120.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$120.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>666026849</td>
<td><blockquote>
<p>20598</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$10.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$10.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td>666028954</td>
<td><blockquote>
<p>16490</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$450.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$300.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$150.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>666032555</td>
<td><blockquote>
<p>31754</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$3.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$3.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td>666049465</td>
<td><blockquote>
<p>27228</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$123,123.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$123,123.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>666051958</td>
<td><blockquote>
<p>40556</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$160.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$160.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td>666053711</td>
<td><blockquote>
<p>37168</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$100.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$100.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>666063555</td>
<td><blockquote>
<p>36880</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$110.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$110.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td>666067490</td>
<td>7178549</td>
<td></td>
<td><blockquote>
<p>$310.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$110.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$200.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>666067760</td>
<td>7174481</td>
<td></td>
<td><blockquote>
<p>$20.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$20.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 666071083 27068 \$150,000.00 \$.00 \$150,000.00

> 22 rows selected.

> ===================================================================================================

> =================================== TOTAL CHECKS (ALL ACCOUNTS) ===================================

> =================================================================================================== TOTAL FOR ALL ACCOUNTS:

> TOTAL DEFERRED TOTAL

> ACCOUNT BALANCE TRANSACTIONS DEFERRED AMOUNT

> \$1,085,425.00 2 \$210.00

> TOTAL FOR MIGRATED ACCOUNTS (EXCLUDING PATIENT ACCOUNTS WITH ERRORS):

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 16%" />
<col style="width: 26%" />
<col style="width: 11%" />
<col style="width: 18%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>TOTAL</p>
</blockquote></th>
<th><blockquote>
<p>DEFERRED</p>
</blockquote></th>
<th><blockquote>
<p>TOTAL</p>
</blockquote></th>
<th colspan="2"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ACCOUNT</p>
</blockquote></td>
<td><blockquote>
<p>BALANCE</p>
</blockquote></td>
<td><blockquote>
<p>TRANSACTIONS</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>DEFERRED</p>
</blockquote></td>
<td><blockquote>
<p>AMOUNT</p>
</blockquote></td>
</tr>
</tbody>
</table>

> \$961,093.00 1 \$10.00

> ===================================================================================================

> ================================== PATIENT ACCOUNTS WITH ERRORS ===================================

> ===================================================================================================

> \>\>\> \>\>\> NOTE: THE FOLLOWING PATIENT ACCOUNTS HAVE ERRORS AND WILL NOT BE MIGRATED! \<\<\< \<\<\<

> 33 rows updated.

| SSN       |     | IEN     |     | FULL NAME      |
|-----------|-----|---------|-----|----------------|
| 666010088 |     | 367     |     | VPFSPATIENT,1  |
| 666010259 |     | 1647    |     | VPFSPATIENT,2  |
| 666012511 |     | 11296   |     | VPFSPATIENT,3  |
| 666012546 |     | 201     |     | VPFSPATIENT,4  |
| 666013608 |     | 5531    |     | VPFSPATIENT,5  |
| 666014270 |     | 3402    |     | VPFSPATIENT,6  |
| 666015802 |     | 3008    |     | VPFSPATIENT,7  |
| 666015888 |     | 578     |     | VPFSPATIENT,8  |
| 666017673 |     | 148     |     | VPFSPATIENT,9  |
| 666019138 |     | 22      |     | VPFSPATIENT,10 |
| 666019624 |     | 2236    |     | VPFSPATIENT,12 |
| 666023064 |     | 16481   |     | VPFSPATIENT,13 |
| 666024315 |     | 2244    |     | VPFSPATIENT,14 |
| 666024936 |     | 39665   |     | VPFSPATIENT,15 |
| 666026702 |     | 24966   |     | VPFSPATIENT,16 |
| 666026849 |     | 20598   |     | VPFSPATIENT,17 |
| 666028954 |     | 16490   |     | VPFSPATIENT,18 |
| 666035039 |     | 23846   |     | VPFSPATIENT,19 |
| 666046598 |     | 37939   |     | VPFSPATIENT,20 |
| 666047363 |     | 29534   |     | VPFSPATIENT,21 |
| 666049465 |     | 27228   |     | VPFSPATIENT,22 |
| 666054826 |     | 11081   |     | VPFSPATIENT,23 |
| 666067730 |     | 29192   |     | VPFSPATIENT,24 |
| 666067760 |     | 7174481 |     | VPFSPATIENT,25 |

> 24 rows selected.

> This page is intentionally blank.

### Convert Data Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Convert Data results file contains a log of the steps performed while converting the patient data.

> mainVPFS Process Started on 02/27/2006 10:33:28.) preConversionCheck Process Started on 02/27/2006 10:33:28.)

> preConversionCheck Institution record check completed on 02/27/2006 10:33:28.) preConversionCheck Blank name check completed on 02/27/2006 10:33:28. 0 Records converted.)

> preConversionCheck Blank SSN check completed on 02/27/2006 10:33:28. 0 Records converted.) preConversionCheck Duplicate SSN check completed on 02/27/2006 10:33:28. 0 Records converted.) preConversionCheck Duplicate IEN/DFN check completed on 02/27/2006 10:33:29. 0 Records converted.) preConversionCheck Blank division id check completed on 02/27/2006 10:33:29. 0 Records converted.) preConversionCheck Invalid division id check completed on 02/27/2006 10:33:29. 0 Records converted.)

> preConversionCheck L/R patient type with no physician name check completed on 02/27/2006 10:33:29. 0 Records converted.) preConversionCheck Invalid indigent code check completed on 02/27/2006 10:33:29. 0 Records converted.)

> preConversionCheck Income source present but blank payee check completed on 02/27/2006 10:33:29. 0 Records converted.) preConversionCheck Income source present but blank amount check completed on 02/27/2006 10:33:29. 0 Records converted.) preConversionCheck Valid income amount check completed on 02/27/2006 10:33:29. 0 Records converted.) preConversionCheck Invalid frequency check completed on 02/27/2006 10:33:29. 0 Records converted.) preConversionCheck Invalid account status type check completed on 02/27/2006 10:33:29. 0 Records converted.) preConversionCheck Invalid patient type check completed on 02/27/2006 10:33:29. 0 Records converted.) preConversionCheck Invalid patient status check completed on 02/27/2006 10:33:29. 0 Records converted.) preConversionCheck Invalid deposit/withdraw check completed on 02/27/2006 10:33:29. 0 Records converted.) preConversionCheck Invalid cash/check/other status check completed on 02/27/2006 10:33:29. 0 Records converted.) preConversionCheck Invalid transaction source check completed on 02/27/2006 10:33:29. 0 Records converted.) preConversionCheck Invalid transaction amount check completed on 02/27/2006 10:33:29. 0 Records converted.) preConversionCheck Record counts check completed on 02/27/2006 10:33:29.) preConversionCheck Process Completed on 02/27/2006 10:33:29. 982 Records converted.) prepDates Process Started on 02/27/2006 10:33:29.) prepDates dm_d1.dob conversion completed on 02/27/2006 10:33:29.) prepDates dm_d2.date_last_trans conversion completed on 02/27/2006 10:33:29.) prepDates dm_d2.date_curr_restr conversion completed on 02/27/2006 10:33:30.) prepDates dm_t1.deferral_dt conversion completed on 02/27/2006 10:33:30.) prepDates dm_t1.trans_date conversion completed on 02/27/2006 10:33:30.) prepDates dm_t1.date_trans_entered conversion completed on 02/27/2006 10:33:30.) prepDates dm_d1.division_id match completed on 02/27/2006 10:33:30.) prepDates Process Completed on 02/27/2006 10:33:30.) insertPerson Process Started on 02/27/2006 10:33:30. 982 Records converted.) insertPerson

> Process Completed on 02/27/2006 10:33:31. 982 Records converted.) insertPatientAccount Process Started on 02/27/2006 10:33:31.)

> insertPatientAccount Process Completed on 02/27/2006 10:33:34. 982 Records converted.) insertIncomeSource Process Started on 02/27/2006 10:33:34.) insertIncomeSource Insert from DM_I1 completed on 02/27/2006 10:33:35.)

> insertIncomeSource Insert from DM_D2, apportionee\$ completed on 02/27/2006 10:33:35.) insertIncomeSource Insert from DM_D2, guardian\$ completed on 02/27/2006 10:33:35.) insertIncomeSource Insert from DM_D2, institut_award\$ completed on 02/27/2006 10:33:35.) insertIncomeSource Insert from DM_D2, other_assets\$ completed on 02/27/2006 10:33:35.) insertIncomeSource Process Completed on 02/27/2006 10:33:35. 17 Records converted.) insertAccountTransaction Process Started on 02/27/2006 10:33:35.) insertAccountTransaction Insert from DM_T1 completed on 02/27/2006 10:33:36.) insertAccountTransaction Insert for BALCARFWD, private source amount w/ no corresponding deferred trans completed on 02/27/2006 10:33:36.) insertAccountTransaction Insert for BALCARFWD, gratuitous amount w/ no corresponding deferred trans completed on 02/27/2006 10:33:36.) insertAccountTransaction Insert for BALCARFWD, private amount \> private deferred trans sum completed on 02/27/2006 10:33:36.) insertAccountTransaction Insert for BALCARFWD, gratuitous amount \> gratuitous deferred trans sum completed on 02/27/2006 10:33:36.) insertAccountTransaction Update of verification status completed on 02/27/2006 10:33:37.) insertAccountTransaction Update of child institution id completed on 02/27/2006 10:33:37.)

> insertAccountTransaction Process Completed on 02/27/2006 10:33:37. 14 Records converted.) updateRunningBalance Process Started on 02/27/2006 10:33:37.) updateRunningBalance Process Completed on 02/27/2006 10:33:37.) updateDeferredAvailableBalance Process Started on 02/27/2006 10:33:37.) updateDeferredAvailableBalance Process Completed on 02/27/2006 10:33:37.) updateGeneralRemarks Process Started on 02/27/2006 10:33:37.) updateGeneralRemarks Process Completed on 02/27/2006 10:33:40.) updateSpecialRemarks Process Started on 02/27/2006 10:33:40.) updateSpecialRemarks Process Completed on 02/27/2006 10:33:41.) insertSuspense Process Started on 02/27/2006 10:33:41.)

> insertSuspense Process Completed on 02/27/2006 10:33:42. 4 Records converted.) postConversionCheck Process Started on 02/27/2006 10:33:42.)

> postConversionCheck Process Completed on 02/27/2006 10:33:42. 982 Records converted.) mainVPFS Process Completed on 02/27/2006 10:33:42.)

#### Errors

> If there were any errors encountered during conversion, those will be detailed in a separate Errors log file.

> 04/07/2005 17:40:00 Error in preConversionCheck: 1 records found with patient type L or R without provider name.

> This page is intentionally blank.

### Verify Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Verify Data Report contains data that will assist in determining whether the migration was successful. By comparing the Verify Report against the Analyze Report, you can determine that there were no patients unexpectedly dropped during data conversion. (Some data portions of the report have been truncated in this example.)

> ==================== VPFS - Verify Report for Station 442 on 02/27/2006 10:02 AM ==================

> ===================================================================================================

> ================================ RECORD COUNT CHECK ===============================================

> ===================================================================================================

> PERSON_CNT PAT_ACCT_CNT ACCT_TRANS_CNT INCOME_SOURCE_CNT DM_D1_CNT DM_D2_CNT DM_B1_CNT DM_B2_CNT DM_I1_CNT DM_T1_CNT

> 982 982 14 17 982 982 982 8 7 1

> ===================================================================================================

> ================================ NOT NULL COUNT CHECK =============================================

> ===================================================================================================

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2" rowspan="2"></th>
<th>PAT_ACCT</th>
<th></th>
<th>PAT_ACCT</th>
<th></th>
<th></th>
<th></th>
<th>DM_D2</th>
<th></th>
<th>DM_D2</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th>DM_T1</th>
</tr>
<tr class="odd">
<th>CURRENT</th>
<th></th>
<th>LAST</th>
<th></th>
<th></th>
<th></th>
<th>CURRENT</th>
<th></th>
<th>LAST</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th>DM_D2</th>
<th></th>
<th>DM_D2</th>
<th></th>
<th>DM_T1</th>
<th></th>
<th>DM_T1</th>
<th></th>
<th>TRANS</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PAT_ACCT</td>
<td></td>
<td>RESTRICTN</td>
<td></td>
<td>TRANS</td>
<td></td>
<td>DM_D1</td>
<td></td>
<td>RESTRICTN</td>
<td></td>
<td>TRANS</td>
<td></td>
<td>DM_D2</td>
<td></td>
<td>DM_D2</td>
<td></td>
<td>INSTN</td>
<td></td>
<td>OTHER</td>
<td></td>
<td>DEFERRAL</td>
<td></td>
<td>TRANS</td>
<td></td>
<td>ENTERED</td>
</tr>
<tr class="even">
<td>DOB</td>
<td></td>
<td>DATE</td>
<td></td>
<td>ENTERED</td>
<td></td>
<td>DOB</td>
<td></td>
<td>DATE</td>
<td></td>
<td>ENTERED</td>
<td></td>
<td>APPORTN$</td>
<td></td>
<td>GUARDN$</td>
<td></td>
<td>AWARD$</td>
<td></td>
<td>ASSETS$</td>
<td></td>
<td>DATE</td>
<td></td>
<td>DATE</td>
<td></td>
<td>DATE</td>
</tr>
<tr class="odd">
<td>NOT NULL</td>
<td></td>
<td>NOT NULL</td>
<td></td>
<td>NOT NULL</td>
<td></td>
<td>NOT NULL</td>
<td></td>
<td>NOT NULL</td>
<td></td>
<td>NOT NULL</td>
<td></td>
<td>NOT NULL</td>
<td></td>
<td>NOT NULL</td>
<td></td>
<td>NOT NULL</td>
<td></td>
<td>NOT NULL</td>
<td></td>
<td>NOT NULL</td>
<td></td>
<td>NOT NULL</td>
<td></td>
<td>NOT NULL</td>
</tr>
<tr class="even">
<td><blockquote>
<p>982</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>24</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>970</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>982</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>24</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>970</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ===================================================================================================

> ================================ NON-MIGRATED PATIENT ACCOUNT LIST ================================

> ===================================================================================================

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 1%" />
<col style="width: 24%" />
<col style="width: 33%" />
<col style="width: 1%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th>SSN</th>
<th></th>
<th>FULL NAME</th>
<th></th>
<th></th>
<th>IEN</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>666010088</td>
<td></td>
<td>VPFSPATIENT,</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
<td>367</td>
</tr>
<tr class="even">
<td>666010259</td>
<td></td>
<td>VPFSPATIENT,</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td></td>
<td>1647</td>
</tr>
<tr class="odd">
<td>666012511</td>
<td></td>
<td>VPFSPATIENT,</td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td></td>
<td>11296</td>
</tr>
<tr class="even">
<td>666012546</td>
<td></td>
<td>VPFSPATIENT,</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td></td>
<td>201</td>
</tr>
<tr class="odd">
<td>666013608</td>
<td></td>
<td>VPFSPATIENT,</td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td></td>
<td>5531</td>
</tr>
<tr class="even">
<td>666014270</td>
<td></td>
<td>VPFSPATIENT,</td>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td></td>
<td>3402</td>
</tr>
<tr class="odd">
<td>666015802</td>
<td></td>
<td>VPFSPATIENT,</td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td></td>
<td>3008</td>
</tr>
<tr class="even">
<td>666015888</td>
<td></td>
<td>VPFSPATIENT,</td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td></td>
<td>578</td>
</tr>
<tr class="odd">
<td>666017673</td>
<td></td>
<td>VPFSPATIENT,</td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td></td>
<td>148</td>
</tr>
<tr class="even">
<td>666019138</td>
<td></td>
<td>VPFSPATIENT,</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td></td>
<td>22</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 50%" />
<col style="width: 13%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>666019624</p>
</blockquote></th>
<th><blockquote>
<p>VPFSPATIENT, 11</p>
</blockquote></th>
<th><blockquote>
<p>2236</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>666023064</p>
</blockquote></td>
<td><blockquote>
<p>VPFSPATIENT, 12</p>
</blockquote></td>
<td><blockquote>
<p>16481</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>666024315</p>
</blockquote></td>
<td><blockquote>
<p>VPFSPATIENT, 13</p>
</blockquote></td>
<td><blockquote>
<p>2244</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666024936</p>
</blockquote></td>
<td><blockquote>
<p>NAME-MISSING-SSN#666024936</p>
</blockquote></td>
<td><blockquote>
<p>39665</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>666026702</p>
</blockquote></td>
<td><blockquote>
<p>VPFSPATIENT, 14</p>
</blockquote></td>
<td><blockquote>
<p>24966</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666026849</p>
</blockquote></td>
<td><blockquote>
<p>VPFSPATIENT, 15</p>
</blockquote></td>
<td><blockquote>
<p>20598</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>666028954</p>
</blockquote></td>
<td><blockquote>
<p>VPFSPATIENT, 16</p>
</blockquote></td>
<td><blockquote>
<p>16490</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666035039</p>
</blockquote></td>
<td><blockquote>
<p>VPFSPATIENT, 17</p>
</blockquote></td>
<td><blockquote>
<p>23846</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>666046598</p>
</blockquote></td>
<td><blockquote>
<p>VPFSPATIENT, 18</p>
</blockquote></td>
<td><blockquote>
<p>37939</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666047363</p>
</blockquote></td>
<td><blockquote>
<p>VPFSPATIENT, 19</p>
</blockquote></td>
<td><blockquote>
<p>29534</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>666049465</p>
</blockquote></td>
<td><blockquote>
<p>VPFSPATIENT, 20</p>
</blockquote></td>
<td><blockquote>
<p>27228</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666054826</p>
</blockquote></td>
<td><blockquote>
<p>VPFSPATIENT, 21</p>
</blockquote></td>
<td><blockquote>
<p>11081</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>666067730</p>
</blockquote></td>
<td><blockquote>
<p>VPFSPATIENT, 22</p>
</blockquote></td>
<td><blockquote>
<p>29192</p>
</blockquote></td>
<td><blockquote>
<p>666067760</p>
</blockquote></td>
</tr>
</tbody>
</table>

> VPFSPATIENT, 23 7174481

> 24 rows selected.

> ===================================================================================================

> ================================ PATIENT ACCOUNT LIST =============================================

> ===================================================================================================

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 20%" />
<col style="width: 0%" />
<col style="width: 8%" />
<col style="width: 0%" />
<col style="width: 6%" />
<col style="width: 0%" />
<col style="width: 8%" />
<col style="width: 0%" />
<col style="width: 4%" />
<col style="width: 0%" />
<col style="width: 3%" />
<col style="width: 0%" />
<col style="width: 4%" />
<col style="width: 0%" />
<col style="width: 6%" />
<col style="width: 0%" />
<col style="width: 4%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SSN</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>FULL NAME</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>PAT</p>
<p>CODE STATION</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>CLAIM NBR</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>WARD</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>ACCT STATUS</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>PAT TYPE</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>PAT STATUS</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>CURRENT RESTRICTN DATE</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>DOB</p>
</blockquote></th>
<th><blockquote>
<p>LAST TRANS ENTERED DATE</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>TOTAL BALANCE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>666063555</p>
</blockquote></td>
<td></td>
<td>VPFSPATIENT, 1</td>
<td></td>
<td>A3555 4429AA</td>
<td></td>
<td>SS</td>
<td></td>
<td></td>
<td></td>
<td>A</td>
<td></td>
<td>U</td>
<td></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>12/29/1924 06/21/2005</p>
</blockquote></td>
<td></td>
<td>$110.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>666025116</p>
</blockquote></td>
<td></td>
<td>VPFSPATIENT, 2</td>
<td></td>
<td>A5116 4429AA</td>
<td></td>
<td>SS</td>
<td></td>
<td></td>
<td></td>
<td>A</td>
<td></td>
<td>U</td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>01/07/1941 06/21/2005</p>
</blockquote></td>
<td></td>
<td>$120.00</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666045322</p>
</blockquote></td>
<td></td>
<td>VPFSPATIENT, 3</td>
<td></td>
<td>A5322 442</td>
<td></td>
<td>SS</td>
<td></td>
<td></td>
<td></td>
<td>I</td>
<td></td>
<td>U</td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>12/23/1938 08/25/1997</p>
</blockquote></td>
<td></td>
<td>$.00</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 4%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 8%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>666035810</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>VPFSPATIENT, 6</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>A5810 442</p>
</blockquote></th>
<th>SS</th>
<th><blockquote>
<p>$.00</p>
</blockquote></th>
<th>I</th>
<th>U</th>
<th><blockquote>
<p>X</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>03/18/1920 06/01/1993</p>
</blockquote></th>
<th>$.00</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>666056812</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>VPFSPATIENT, 7</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>A6812 442</p>
</blockquote></td>
<td>SS</td>
<td></td>
<td>I</td>
<td>U</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>12/06/1920 03/17/1995</p>
</blockquote></td>
<td>$.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>666072494</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>VPFSPATIENT, 8</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>A2494 442</p>
</blockquote></td>
<td>SS</td>
<td></td>
<td>I</td>
<td>U</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>08/28/1929 12/17/2001</p>
</blockquote></td>
<td>$.00</td>
</tr>
<tr class="odd">
<td colspan="13"><blockquote>
<p>…………………………………………………………………………………………………………………</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>666030099</p>
</blockquote></td>
<td>VPFSPATIENT,</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>Y0099</td>
<td><blockquote>
<p>442</p>
</blockquote></td>
<td><blockquote>
<p>SS</p>
</blockquote></td>
<td colspan="2">I</td>
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>04/12/1930</td>
<td><blockquote>
<p>09/27/1996</p>
</blockquote></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666051696</p>
</blockquote></td>
<td>VPFSPATIENT,</td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td>Y1696</td>
<td><blockquote>
<p>442</p>
</blockquote></td>
<td><blockquote>
<p>SS</p>
</blockquote></td>
<td colspan="2">I</td>
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>03/03/1923</td>
<td><blockquote>
<p>02/22/2002</p>
</blockquote></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>666014535</p>
</blockquote></td>
<td>VPFSPATIENT,</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td>Y4535</td>
<td><blockquote>
<p>442</p>
</blockquote></td>
<td><blockquote>
<p>SS</p>
</blockquote></td>
<td colspan="2">I</td>
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>11/29/1899</td>
<td><blockquote>
<p>05/13/1999</p>
</blockquote></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666035862</p>
</blockquote></td>
<td>VPFSPATIENT,</td>
<td><blockquote>
<p>11</p>
</blockquote></td>
<td>Y5862</td>
<td><blockquote>
<p>442</p>
</blockquote></td>
<td><blockquote>
<p>SS</p>
</blockquote></td>
<td colspan="2">I</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>08/04/1948</td>
<td><blockquote>
<p>10/15/2003</p>
</blockquote></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>666072044</p>
</blockquote></td>
<td>VPFSPATIENT,</td>
<td><blockquote>
<p>12</p>
</blockquote></td>
<td>Z2044</td>
<td><blockquote>
<p>442</p>
</blockquote></td>
<td><blockquote>
<p>SS</p>
</blockquote></td>
<td colspan="2">I</td>
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>10/29/1922</td>
<td><blockquote>
<p>01/05/2004</p>
</blockquote></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666016895</p>
</blockquote></td>
<td>VPFSPATIENT,</td>
<td><blockquote>
<p>13</p>
</blockquote></td>
<td>Z6895</td>
<td><blockquote>
<p>442</p>
</blockquote></td>
<td><blockquote>
<p>SS</p>
</blockquote></td>
<td colspan="2">I</td>
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
<td>06/19/1912</td>
<td><blockquote>
<p>06/29/2000</p>
</blockquote></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>666038798</p>
</blockquote></td>
<td>VPFSPATIENT,</td>
<td><blockquote>
<p>14</p>
</blockquote></td>
<td>Z8798</td>
<td><blockquote>
<p>442</p>
</blockquote></td>
<td><blockquote>
<p>SS</p>
</blockquote></td>
<td colspan="2">I</td>
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>06/18/1921</td>
<td><blockquote>
<p>05/18/1992</p>
</blockquote></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666075939</p>
</blockquote></td>
<td>VPFSPATIENT,</td>
<td><blockquote>
<p>15</p>
</blockquote></td>
<td>Z5939</td>
<td><blockquote>
<p>442</p>
</blockquote></td>
<td><blockquote>
<p>SS</p>
</blockquote></td>
<td colspan="2">I</td>
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>06/29/1956</td>
<td><blockquote>
<p>02/10/2003</p>
</blockquote></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>666031719</p>
</blockquote></td>
<td>VPFSPATIENT,</td>
<td><blockquote>
<p>16</p>
</blockquote></td>
<td>Z1719</td>
<td><blockquote>
<p>442</p>
</blockquote></td>
<td></td>
<td colspan="2">I</td>
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>06/06/1953</td>
<td><blockquote>
<p>07/20/1992</p>
</blockquote></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666027197</p>
</blockquote></td>
<td>VPFSPATIENT,</td>
<td><blockquote>
<p>17</p>
</blockquote></td>
<td>Z7197</td>
<td><blockquote>
<p>442</p>
</blockquote></td>
<td><blockquote>
<p>SS</p>
</blockquote></td>
<td colspan="2">I</td>
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>12/15/1920</td>
<td><blockquote>
<p>08/16/1993</p>
</blockquote></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
</tr>
</tbody>
</table>

\- TOTAL

\$961,093.00

> 982 rows selected.

> ===================================================================================================

> ================================ INACTIVE ACCOUNTS WITH NON-ZERO BALANCES =========================

> =================================================================================================== SSN FULL NAME ACCOUNT STATUS TOTAL BALANCE

> TOTAL

> no rows selected

> ===================================================================================================

> ================================ TRANSACTIONS LIST ================================================

> ===================================================================================================

TOTAL

> \$961,093.00

> 14 rows selected.

> ===================================================================================================

> ================================ DEFERRED TRANSACTIONS LIST =======================================

> ===================================================================================================

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 23%" />
<col style="width: 0%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 0%" />
<col style="width: 8%" />
<col style="width: 0%" />
<col style="width: 8%" />
<col style="width: 0%" />
<col style="width: 8%" />
<col style="width: 0%" />
<col style="width: 14%" />
<col style="width: 0%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SSN</p>
</blockquote></th>
<th><blockquote>
<p>FULL NAME</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>TRANS NUMBER TRANS</p>
</blockquote></th>
<th><blockquote>
<p>DEFERRAL DATE DATE</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>PATIENT TOTAL BALANCE</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>PATIENT DEFERRED BALANCE</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>PATIENT AVAILABLE BALANCE</p>
</blockquote></th>
<th colspan="4"><blockquote>
<p>MASTER TRANS TRANS</p>
<p>TRANS AMT TYPE CODE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>666084319 VPFSPATIENT, 65</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>176 01/27/2006 02/06/2006</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$10.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$10.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$.00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>$10.00 D</p>
<p>TOTAL</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>6392M</p>
</blockquote></td>
</tr>
</tbody>
</table>

> \$10.00

> ===================================================================================================

> ================================ ACCOUNT BALANCES CHECK ===========================================

> ===================================================================================================

TOTAL

> \$961,093.00 \$810,783.00 \$150,310.00

> 14 rows selected.

> ===================================================================================================

> ================================ MIGRATED TOTALS CHECK ============================================

> =================================================================================================== NUMBER OF TOTAL OF NUMBER OF TOTAL OF

> PATIENT ACCOUNTS ACCOUNT BALANCES DEFERRED TRANSACTIONS DEFERRED AMOUNTS

> 982 \$961,093.00 1 \$10.00

> ================================ INCOME SOURCE CHECK =============================================

> ===================================================================================================

| SSN       |     | FULL NAME       |     | INCOME SOURCE       |     | INCOME SOURCE AMT |     | FREQ      |
|-----------|-----|-----------------|-----|---------------------|-----|-------------------|-----|-----------|
| 666039856 |     | VPFSPATIENT, 44 |     | GUARDIAN            |     | \$.00             |     |           |
| 666039856 |     | VPFSPATIENT, 42 |     | INSTITUTIONAL AWARD |     | \$50.00           |     |           |
| 666039856 |     | VPFSPATIENT, 43 |     | APPORTIONEE         |     | \$100.00          |     |           |
| 666019127 |     | VPFSPATIENT, 44 |     | APPORTIONEE         |     | \$600.00          |     |           |
| 666019127 |     | VPFSPATIENT, 45 |     | INSTITUTIONAL AWARD |     | \$600.00          |     |           |
| 666012561 |     | VPFSPATIENT, 46 |     | INSTITUTIONAL AWARD |     | \$9,228.00        |     |           |
| 666024180 |     | VPFSPATIENT, 47 |     | INSTITUTIONAL AWARD |     | \$26,736.00       |     |           |
| 666035137 |     | VPFSPATIENT, 48 |     | APPORTIONEE         |     | \$178.00          |     |           |
| 666019865 |     | VPFSPATIENT, 49 |     | APPORTIONEE         |     | \$100.00          |     | 666019865 |

> VPFSPATIENT, 50 GUARDIAN \$100.00

> 10 rows selected.

> ===================================================================================================

> ================================ REMARKS COUNT CHECK ==============================================

> ===================================================================================================

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 19%" />
<col style="width: 15%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th>PAT_ACCT</th>
<th></th>
<th>DM_X1_X2</th>
<th>PAT_ACCT</th>
<th></th>
<th>DM_R1_R2</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SPECIAL RMKS</td>
<td><blockquote>
<p>DM_X1_X2</p>
</blockquote></td>
<td>TOTAL</td>
<td>GENERAL RMKS</td>
<td><blockquote>
<p>DM_R1_R2</p>
</blockquote></td>
<td>TOTAL</td>
</tr>
<tr class="even">
<td>NOT NULL</td>
<td><blockquote>
<p>NOT NULL</p>
</blockquote></td>
<td>COUNT</td>
<td>NOT NULL</td>
<td><blockquote>
<p>NOT NULL</p>
</blockquote></td>
<td>COUNT</td>
</tr>
</tbody>
</table>

> 16 16 18 53 53 54

> ===================================================================================================

> ================================ NON-CONVERTED SPECIAL REMARKS LIST ===============================

> ===================================================================================================

> no rows selected

#### Appendix D

> ===================================================================================================

> ================================ NON-CONVERTED GENERAL REMARKS LIST ===============================

> ===================================================================================================

> no rows selected

> This page intentionally blank.

#### Appendix E. Acronyms and Abbreviations

# Appendix E. Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ADPAC</p>
</blockquote></td>
<td><blockquote>
<p>Automated Data Processing Application Coordinator</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>API</p>
</blockquote></td>
<td><blockquote>
<p>Application Program Interface</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ASIS</p>
</blockquote></td>
<td><blockquote>
<p>Application Structure and Integration Services</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>C&amp;A</p>
</blockquote></td>
<td><blockquote>
<p>Certification and Accreditation</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CHISS</p>
</blockquote></td>
<td><blockquote>
<p>Common Health Information Security Services</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CI</p>
</blockquote></td>
<td><blockquote>
<p>Configuration Item</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>COTS</p>
</blockquote></td>
<td><blockquote>
<p>Commercial Off The Shelf</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CPU</p>
</blockquote></td>
<td><blockquote>
<p>Central Processing Unit</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CRUD</p>
</blockquote></td>
<td><blockquote>
<p>Create, Read, Update, Delete</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CSS</p>
</blockquote></td>
<td><blockquote>
<p>Cascading Style Sheets</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DAS</p>
</blockquote></td>
<td><blockquote>
<p>Delegated Administration Service</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DBMS</p>
</blockquote></td>
<td><blockquote>
<p>Database Management System</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DHTML</p>
</blockquote></td>
<td><blockquote>
<p>Dynamic HyperText Markup Language</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DN</p>
</blockquote></td>
<td><blockquote>
<p>Distinguished Name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DOS</p>
</blockquote></td>
<td><blockquote>
<p>Disk Operating System</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DSS</p>
</blockquote></td>
<td><blockquote>
<p>Decision Support System</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EAR</p>
</blockquote></td>
<td><blockquote>
<p>Enterprise Archive</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EJB</p>
</blockquote></td>
<td><blockquote>
<p>Enterprise Java Bean</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EIS</p>
</blockquote></td>
<td><blockquote>
<p>Enterprise Information System</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ERD</p>
</blockquote></td>
<td><blockquote>
<p>Entity Relationship Diagram</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ETL</p>
</blockquote></td>
<td><blockquote>
<p>Extract, Transform, Load</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FK</p>
</blockquote></td>
<td><blockquote>
<p>Foreign Key</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FTP</p>
</blockquote></td>
<td><blockquote>
<p>File Transfer Protocol</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HIPAA</p>
</blockquote></td>
<td><blockquote>
<p>Health Insurance Portability and Accountability Act</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HIS</p>
</blockquote></td>
<td><blockquote>
<p>Health Information System</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>HL7</p>
</blockquote></th>
<th><blockquote>
<p>Health Level 7</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HTML</p>
</blockquote></td>
<td><blockquote>
<p>HyperText Markup Language</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HTTP</p>
</blockquote></td>
<td><blockquote>
<p>HyperText Transfer Protocol</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HTTPS</p>
</blockquote></td>
<td><blockquote>
<p>HyperText Transfer Protocol Secure</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ICN</p>
</blockquote></td>
<td><blockquote>
<p>Integration Control Number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IIG</p>
</blockquote></td>
<td><blockquote>
<p>Impact Innovations Group</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IP</p>
</blockquote></td>
<td><blockquote>
<p>Internet Protocol</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IFCAP</p>
</blockquote></td>
<td><blockquote>
<p>Integrated Patient Funds Distribution, Control Point Activity, Accounting and</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Appendix F. Acronyms and Abbreviations

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Procurement</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IPF</p>
</blockquote></td>
<td><blockquote>
<p>Integrated Patient Funds</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>J2EE</p>
</blockquote></td>
<td><blockquote>
<p>Java TM 2 Platform, Enterprise Edition</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>JAAS</p>
</blockquote></td>
<td><blockquote>
<p>Java Authentication and Authorization Service</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>JCA</p>
</blockquote></td>
<td><blockquote>
<p>Java Connector Architecture</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>JDBC</p>
</blockquote></td>
<td><blockquote>
<p>Java Database Connectivity</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>JDK</p>
</blockquote></td>
<td><blockquote>
<p>Java Development Kit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>JMS</p>
</blockquote></td>
<td><blockquote>
<p>Java Message Service</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>JNDI</p>
</blockquote></td>
<td><blockquote>
<p>Java Naming Directory Interface</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>JSP</p>
</blockquote></td>
<td><blockquote>
<p>Java Server Page</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>JSTL</p>
</blockquote></td>
<td><blockquote>
<p>Java Standard Tag Library</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>JTA</p>
</blockquote></td>
<td><blockquote>
<p>Java Transaction API</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>JVM</p>
</blockquote></td>
<td><blockquote>
<p>Java Virtual Machine</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>KAAJEE</p>
</blockquote></td>
<td><blockquote>
<p>Kernel Authentication and Authorization for J2EE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LAN</p>
</blockquote></td>
<td><blockquote>
<p>Local Area Network</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LDAP</p>
</blockquote></td>
<td><blockquote>
<p>Lightweight Directory Access Protocol</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LLC</p>
</blockquote></td>
<td><blockquote>
<p>Limited Liability Corporation</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>MUMPS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MAC</p>
</blockquote></td>
<td><blockquote>
<p>Media Access Controller</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MUMPS</p>
</blockquote></td>
<td><blockquote>
<p>Massachusetts Universal Multi Programming System</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MVC</p>
</blockquote></td>
<td><blockquote>
<p>Model View Controller</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>OCI</p>
</blockquote></th>
<th><blockquote>
<p>Oracle Call Interface</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>OCS</p>
</blockquote></td>
<td><blockquote>
<p>Office of Cyber Security</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PFC</p>
</blockquote></td>
<td><blockquote>
<p>Patient Funds Clerk</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PFCS</p>
</blockquote></td>
<td><blockquote>
<p>Patient Funds Clerk Supervisor</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PATS</p>
</blockquote></td>
<td><blockquote>
<p>Patient Advocate Tracking System</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PFOP</p>
</blockquote></td>
<td><blockquote>
<p>Personal Funds of Patients</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PK</p>
</blockquote></td>
<td><blockquote>
<p>Primary Key</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PKI</p>
</blockquote></td>
<td><blockquote>
<p>Public Key Infrastructure</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PM</p>
</blockquote></td>
<td><blockquote>
<p>Project Manager</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PSD</p>
</blockquote></td>
<td><blockquote>
<p>Person Service Demographics</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PSL</p>
</blockquote></td>
<td><blockquote>
<p>Person Service Lookup</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>QA</p>
</blockquote></td>
<td><blockquote>
<p>Quality Assurance</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>QCI</p>
</blockquote></td>
<td><blockquote>
<p>Quality Control Inspector</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Appendix F. Acronyms and Abbreviations

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>QCP</p>
</blockquote></td>
<td><blockquote>
<p>Quality Control Plan</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RBAC</p>
</blockquote></td>
<td><blockquote>
<p>Role Based Access Control</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RDBMS</p>
</blockquote></td>
<td><blockquote>
<p>Relational Database Management System</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RO</p>
</blockquote></td>
<td><blockquote>
<p>Regional Office</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RPC</p>
</blockquote></td>
<td><blockquote>
<p>Remote Procedure Call</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SCM</p>
</blockquote></td>
<td><blockquote>
<p>Software Configuration Management</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SCMP</p>
</blockquote></td>
<td><blockquote>
<p>Software Configuration Management Plan</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SD&amp;D</p>
</blockquote></td>
<td><blockquote>
<p>System Design &amp; Development</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SDD</p>
</blockquote></td>
<td><blockquote>
<p>System Design Document</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SDK</p>
</blockquote></td>
<td><blockquote>
<p>Software Development Kit</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SDL</p>
</blockquote></td>
<td><blockquote>
<p>Software Development Library</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SDLC</p>
</blockquote></td>
<td><blockquote>
<p>Software Development Life Cycle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SEPG</p>
</blockquote></td>
<td><blockquote>
<p>Software Engineering Process Group</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SI</p>
</blockquote></td>
<td><blockquote>
<p>System Implementation</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SME</p>
</blockquote></td>
<td><blockquote>
<p>Subject Matter Expert</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SOAP</p>
</blockquote></td>
<td><blockquote>
<p>Simple Object Access Protocol</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SOW</p>
</blockquote></th>
<th><blockquote>
<p>Statement of Work</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SQA</p>
</blockquote></td>
<td><blockquote>
<p>Software Quality Assurance</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SQAP</p>
</blockquote></td>
<td><blockquote>
<p>Software Quality Assurance Plan</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SQL</p>
</blockquote></td>
<td><blockquote>
<p>Standard Query Language</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SRS</p>
</blockquote></td>
<td><blockquote>
<p>Software Requirements Specification</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SSL</p>
</blockquote></td>
<td><blockquote>
<p>Secure Sockets Layer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TBD</p>
</blockquote></td>
<td><blockquote>
<p>To Be Determined</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TLD</p>
</blockquote></td>
<td><blockquote>
<p>Tag Descriptor Library</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>URI</p>
</blockquote></td>
<td><blockquote>
<p>Uniform Resource Identifier</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>URL</p>
</blockquote></td>
<td><blockquote>
<p>Uniform Resource Locator</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Affairs</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VAX</p>
</blockquote></td>
<td><blockquote>
<p>VAX (Virtual Address eXtension) is an established line of mid-range server computers from the Digital Equipment Corporation (DEC).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VHA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Health Administration</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Information Systems Technology Architecture</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VMS</p>
</blockquote></td>
<td><blockquote>
<p>Virtual Machine System (operating system for VAX computers)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VPFS</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Personal Finance System</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WAN</p>
</blockquote></td>
<td><blockquote>
<p>Wide Area Network</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WAR</p>
</blockquote></td>
<td><blockquote>
<p>Web Archive</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Appendix F. Acronyms and Abbreviations

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>XDE</p>
</blockquote></td>
<td><blockquote>
<p>Extensible Development Environment</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>XHTML</p>
</blockquote></td>
<td><blockquote>
<p>Extensible HyperText Markup Language</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>XML</p>
</blockquote></td>
<td><blockquote>
<p>Extensible Markup Language</p>
</blockquote></td>
</tr>
</tbody>
</table>