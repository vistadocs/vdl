---
title: Blind Rehab Version 5 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: null
app_code: ANRV
app_name: Visual Impairment Service Team (VIST)
section: CLI
app_status: archive
pkg_ns: ANRV
patch_ver: 5
patch_id: ANRV*5
group_key: ANRV:ANRV:5
file_numbers: []
security_keys: []
menu_options: 15
description: For the initial release and other releases of Blind Rehabilitation, refer to the 'Blind Rehabilitation Release Notes
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 2275
section_count: 3
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: August 2011
revision_count: 0
revision_newest: ''
revision_oldest: ''
docx_url: https://www.va.gov/vdl/documents/Clinical/Blind_Rehabilitation_Archive/br_release_notes.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Blind_Rehabilitation_Archive/br_release_notes.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=333
audit_applied: '2026-05-31'
master_source: Blind Rehab Version 5 Release Notes
master_pub_date: August 2011
consolidated_from: 11 versions
prior_versions:
- Blind Rehab Version 5.1.10 Release Notes
- Blind Rehab Version 5.1.12 Release Notes
- Blind Rehab Version 5.1.13 Release Notes
- Blind Rehab Version 5.1.15 Release Notes
- Blind Rehab Version 5.1.16 Release Notes
- Blind Rehab Version 5.1.17 Release Notes
- Blind Rehab Version 5.1.18 Release Notes
- Blind Rehab Version 5.1.3 Release Notes
- Blind Rehab Version 5.1.9 Release Notes
- Blind Rehab Version 5.1 Release Notes
consolidated_title: blind rehab release notes
---

![](blind-rehab-version-5-release-notes/001.png)

BLIND REHABILITATION

RELEASE NOTES

![](blind-rehab-version-5-release-notes/002.png)

Version 5.0.29

August 2011

VistA Health System Design & Development

Revision History

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 55%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><em><strong>Date</strong></em></th>
<th><em><strong>Description</strong></em></th>
<th><em><strong>Author</strong></em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>For the initial release and other releases of Blind Rehabilitation, refer to the '<em>Blind Rehabilitation Release Notes 5.0.28.doc'.</em></td>
<td></td>
</tr>
<tr class="even">
<td>08/2011</td>
<td><p>The following changes have occurred for the version 5.0.29</p>
<p>This BR package addresses specific Remedy tickets</p>
<ul>
<li><p>HD292560 - Users resetting login after AC/VC entered</p></li>
<li><p>HD191284 - Users showing up twice under "Tracked by" option</p></li>
<li><p>HD184543 - Blind Rehab 5.0: Print option/report data</p></li>
<li><p>HD386545 - "Tracked by" list not updated by new staff</p></li>
<li><p>HD386546 - Screen reader not reporting record contents correctly</p></li>
<li><p>HD386547 - Inactive Institution appearing in the Enter/Edit Menus</p></li>
<li><p>HD386600 - Enter/Edit BR Patient - Dependents field does not accept names with apostrophe </p></li>
<li><p>HD386601 - On the Enter/Edit BR Patient screen Prior Rehab Training is accepting past date </p></li>
<li><p>HD386603 - BR Staff task menu Accepting Activation date greater than deactivation date </p></li>
<li><p>HD386604 - Date of Death before Activation Date </p></li>
<li><p>HD386612 - Prevent execution of functionality for a deceased patient</p></li>
<li><p>HD386611 - Wrong Help File displayed on the Converted National Waitlist Records Found - Count Screen</p></li>
<li><p>HD403034 - Institution is added/removed from current user, user will no longer have to logout of 5.0 application</p></li>
<li><p>HD410584- System Operating Extremely Slow</p></li>
<li><p>HD388035-Audit_Trail table vexes DBA</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

Table of Contents

<span id="_Toc153858182" class="anchor"></span>Introduction<u>NOTE</u>: These Release Notes are for Blind Rehabilitation Version 5.0.29.4. For the initial release and other releases of Blind Rehabilitation, refer to the '*Blind Rehabilitation Release Notes 5.0.28.doc'*.

# Documentation Retrieval


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Documentation Retrieval](#documentation-retrieval)
- [VistA Intranet](#vista-intranet)
- [What's New in Blind Rehab v5.0.29](#whats-new-in-blind-rehab-v5029)
  - [General User experience changes](#general-user-experience-changes)
  - [Administrative Users/System Changes](#administrative-userssystem-changes)
- [Appendix](#appendix)
<span class="mark">REDACTED</span>
|                 |                                                                              |                        |     |
|-----------------|------------------------------------------------------------------------------|------------------------|-----|
| *File Name* | *Description*                                                            | *Retrieval Format* |     |
| ANRV5_0CIG.PDF  | \* Blind Rehabilitation Centralized Server Installation/Implementation Guide | Binary                 |     |
| ANRV5_0VIG.PDF  | \*\* Blind Rehabilitation VistA Installation/Implementation Guide            | Binary                 |     |
| ANRV5_0RN.PDF   | Blind Rehabilitation Release Notes                                           | Binary                 |     |
| ANRV5_0TM.PDF   | Blind Rehabilitation Technical Manual/Security Guide                         | Binary                 |     |
| ANRV5_0UM.PDF   | Blind Rehabilitation User Manual                                             | Binary                 |     |
> \* This Installation Guide is only for Centralized Servers, not to be used at the field VistA site.
> \*\* This Installation/Implementation Guide is for field VistA sites.

# VistA Intranet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation for this product is available on the intranet at the following address:

> <http://www.va.gov/vdl/>.

This address takes you to the VistA Documentation Library (VDL), which has a listing of all of the clinical software manuals. Within the Clinical Section, Click on the Blind Rehabilitation link and it will take you to the Blind Rehab documentation.

The link below allows access to the Blind Rehabilitation home page:

> <http://vista.med.va.gov/clinicalspecialties/vist/index.htm>

# What's New in Blind Rehab v5.0.29

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Blind Rehabilitation package (BR-PKG-5.0.29.6) consists of changes to the JAVA components, SDS upgrade from ver.10 to ver. 18 and upgrade to KAAJEE version from 1.0.0.019 to 1.0.1.003

This BR package addresses thirteen specific functionality remedy tickets and two data base performance improvement remedy tickets.

## *General User experience changes*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Reformatted the Login screen by removing the 'Reset' button([HD292560](#HD292560))
- 'Tracked By' changes
  - Controlled by Role (not everyone's staff record will appear in 'Tracked by')
    - VIST Coordinator, BROS, Low Vision([HD191284](#HD191284))
  - Only active staff records will appear in 'Tracked by'
  - New staff added to 'Tracked by' without an application restart([HD386545](#HD386545))
- 508 issue with 'Individual Wait list Records'(<span id="HD388035" class="anchor"></span>[HD386546](\l))
- Help file is corrected for 'Modify Converted National Waitlist Record'([HD386611](#HD386611))
- Enter/Edit:
  - Dependents names that contain an apostrophe will display correctly (O'Brien)([HD386600](#HD386600))
  - Prior Rehab Training (Page4) will not accept future date for any prior training and fields masked for Prior Rehab Training 'NO'.([HD386601](#HD386601))
  - A deceased patient cannot be added to BR application.([HD386604](#HD386604))
  - Execution of functionality is prevented for deceased patients ([HD386612](#HD386612))

## *Administrative Users/System Changes*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Edit BR Staff Screen now accepts Activation date less than or equal to deactivation date. ([HD386603](#HD386603))
- Institution added/removed for a user, the user no longer has to logout of BR 5.0([HD403034](#HD403034))
- BR CO can now manage institutions better via the following changes([HD386547](#HD386547))
  - On Edit BR Institution, a new feature is added to display the number of active users attached to the Institution and the Institution cannot be inactivated when there is staff attached.
- SDS upgrade from v.10 to v.18
- KAAJEE upgrade from 1.0.0.019 to 1.0.1.003
- BR 5.0 application validation against the Internet Explorer 7 ([HD184543](#HD184543))
- Database performance improvement by
- Audit Trail table partitioning([HD388035](#HD388035))
- Dropping indexes on Audit Trail table([HD410584](#HD410584))

# Appendix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 24%" />
<col style="width: 24%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Remedy ID/Defect ID</strong></th>
<th><strong>Issue</strong></th>
<th><strong>Description</strong></th>
<th><strong>Solution</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><span id="HD292560" class="anchor"></span>HD292560/</p>
<p>BLRHB00000512</p></td>
<td>Users resetting login after AC/VC entered</td>
<td>On the Login screen, after entering AV codes press Enter, it should perform Login, not Reset. This is very frustrating, since it forces user to re-enter the AV codes. User must also then either press the login button (further down the page) or tab 4 times and press enter.</td>
<td><p>SDS and KAAJEE upgraded for this feature. The Reset button is removed.</p>
<p>On the Login screen, after entering AV codes press Enter, it performs Login.</p></td>
</tr>
<tr class="even">
<td><p><span id="HD191284" class="anchor"></span>HD191284/</p>
<p>BLRHB00000513 </p></td>
<td>Users showing up twice under "Tracked by" option</td>
<td>Users showing up twice under "Tracked by" option for those who have multiple staff records</td>
<td><p>The 'Tracked by' list would display users with the following three roles:</p>
<p>VIST Coordinator</p>
<p>BROS</p>
<p>Low Vision<strong><br />
</strong></p></td>
</tr>
<tr class="odd">
<td><p><span id="HD184543" class="anchor"></span>HD184543/</p>
<p>BLRHB00000514 </p></td>
<td>Blind Rehab 5.0: Print option/report data</td>
<td>This is an older problem with Blind Rehab 5.0: Print option/report data issues. User was using I.E. 7.0.</td>
<td>Blind Rehab application has been validated /tested the with I.E 7</td>
</tr>
<tr class="even">
<td><p><span id="HD386545" class="anchor"></span>HD386545/</p>
<p>BLRHB00000501 </p></td>
<td>"Tracked by" list not updated by new staff</td>
<td>When a new user is added to the BR application using the BR Staff task menu from the Administrator Menu, the new user is not appearing in the "Tracked By" field.</td>
<td>This issue is occurring due to the Staff being loaded at the time of application is started. Fixed it to reflect the changes in the Staff table dynamically rather than wait for the Application server reboot.</td>
</tr>
<tr class="odd">
<td><p><span id="HD386547" class="anchor"></span>HD386547/</p>
<p>BLRHB00000505 </p></td>
<td>Inactive Institution appearing in the Enter/Edit Menus</td>
<td>Institution whose status in BR Institutions menu of the Administrator menu was changed to inactive is still appearing in the Institutions field of the various Task Menus of the Enter/Edit menu</td>
<td>The fix is based on the enhancement request. The institution cannot inactivate if there is any staff associated with the institution. If there is no staff associated to the institution then that can be inactivated and hence the institution will not appear in the institutions field of the various task menus of the Enter/Edit menu.</td>
</tr>
<tr class="even">
<td><p><span id="HD386600" class="anchor"></span>HD386600/</p>
<p>BLRHB00000506 </p></td>
<td>Enter/Edit BR Patient - Dependents field does not accept names with apostrophe</td>
<td>Enter/Edit BR Patient screen - Dependents field does not accept names with apostrophe</td>
<td>Dependents field can have an apostrophe in their name. Ex: O'Brien</td>
</tr>
<tr class="odd">
<td><p><span id="HD386601" class="anchor"></span>HD386601/</p>
<p>BLRHB00000507 </p></td>
<td>On the Enter/Edit BR Patient screen Prior Rehab Training is accepting past date</td>
<td>On the Enter/Edit BR Patient screen, if there is any prior BR Training it should accept past date instead it is accepting future date and if we select NO for Prior Rehab Training remaining fields are not getting masked.</td>
<td>The fix is applied on Page 4 of the Enter/Edit BR Patient screens where the three fields under "Any Prior Blind Rehab Training?" should not be editable unless that field is set to "YES" and for the Date of training that should allow past and current date</td>
</tr>
<tr class="even">
<td><p><span id="HD386603" class="anchor"></span>HD386603/</p>
<p>BLRHB00000508 </p></td>
<td>BR Staff task menu Accepting Activation date greater than deactivation date</td>
<td>BR Staff task menu is accepting an activation date greater than deactivation date</td>
<td>Edit BR Staff screen is fixed to accept the activation date less than or equal to deactivation date with a user message</td>
</tr>
<tr class="odd">
<td><p><span id="HD386611" class="anchor"></span>HD386611/</p>
<p>BLRHB00000510 </p></td>
<td>Wrong Help File displayed on the Converted National Waitlist Records Found - Count Screen</td>
<td>Wrong help file is displayed on the Converted National Waitlist Records Found - Count screen</td>
<td>Correct Help file "Modify Converted National Waitlist Record" is updated</td>
</tr>
<tr class="even">
<td><p><span id="HD386604" class="anchor"></span>HD386604/</p>
<p>BLRHB00000509 </p></td>
<td>Date of Death before Activation Date </td>
<td>A deceased patient can be added to the Blind Rehabilitation application, and therefore, on the "Additions to VIST Roster" report for some deceased patients the "Enrollment Date" is later than the "Date of Death". Application allows users to make a patient as deceased from the existing patient status screen.</td>
<td>A deceased patient cannot be added to the Blind Rehabilitation application in future. On patient status screen it is fixed by removing the DECEASED from the dropdown. This avoids manual update to patient record as deceased.</td>
</tr>
<tr class="odd">
<td><p><span id="HD386612" class="anchor"></span>HD386612/</p>
<p>BLRHB00000511 </p></td>
<td>Prevent execution of functionality for a deceased patient</td>
<td>Prevent execution of functionality for a deceased patient such as not permitting activation or enrollment of deceased patients throughout the application</td>
<td><p>The below screens fixed to prevent execution of functionality for a deceased patient.</p>
<p>In all the below screens, all the fields have been marked as non-editable for a deceased patient, so no normal functionality can be performed for deceased patient.</p>
<p>Enter/Edit BR Patient</p>
<p>Enter/Edit Low Vision Patient</p>
<p>Enter/Edit Patient Status</p>
<p>Enter/Edit Create Referral</p>
<p>Enter/Edit VARO Claims</p>
<p>Enter/Edit Eye Exam (Eligibility)</p>
<p>Benefits and Service Checklist</p></td>
</tr>
<tr class="even">
<td><p><span id="HD403034" class="anchor"></span>HD403034/</p>
<p>BLRHB00000540</p></td>
<td>Institution is added/removed from current user, user will no longer have to logout of 5.0 application</td>
<td>Staff has to logout of the BR application so that they can see the correct list of institution associated with the staff anytime they make change to the institutions attached to the staff.</td>
<td>when an institution is added or removed from a user, user will no longer have to logout of the 5.0 application</td>
</tr>
<tr class="odd">
<td><span id="HD410584" class="anchor"></span>HD410584</td>
<td>System Operating Extremely Slow</td>
<td>Improve system performance by removing the indexes on the Audit Trail table</td>
<td>This is a Database patch consists of the data scripts for dropping the indexes and creating the indexes on the AUDIT_TRAIL table</td>
</tr>
<tr class="even">
<td>HD388035</td>
<td>AUDIT_TRAIL table vexes DBA</td>
<td>A high volume of audit trail records may cause database performance problems. Improve System Performance by archiving over 2.5 million Audit Trail records to a separate archive table</td>
<td>This is a Database Patch. There are more than 2.5 million records in Audit Trial table and it has become an issue for a DBA in backing up the Audit Trail records. To reduce the backup issue and also to improve the performance of the BR application for audit trial transactions, the Audit trial table records moved to history table. The Audit trail records and Audit trial history records are combined for the AUDIT_TRAIL view</td>
</tr>
<tr class="odd">
<td>HD386546/ BLRHB00000503</td>
<td>Screen reader not reporting record contents correctly</td>
<td>508 compliance issue: Individual Wait List Records-Regular screen shows information on one line. The screen reader shows info on two lines</td>
<td>The fix is validated with the Accessibility team. It is corrected to display the information on one line.</td>
</tr>
</tbody>
</table>

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Blind Rehab Version 5.1.3 Release Notes

## General Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The System Administrator role has undergone an update which allows them to update a user's DUZ code. The Patient Search functionality can now be utilized by entering the first initial of a patient's last name as well as the last four digits of their social security number. When a column sort for Referrals Found is used, and the Edit button is selected, users will now see that patients will match against the data in their respective row. Users will also see that patient records for Additional Medical Treatment Information are displayed correctly. Patient mailing labels will now print correctly on Avery 3x10 label sheets. The VIST Annual Review date on an exported VIST Roster list will be displayed in the correct format. In addition to the forementioned updates, the following new referral types have been added to the application.

- BROS Poly Vision Therapy – 1st Experience
- BROS Poly Vision Therapy – Additional Training
- Vision Therapy – 1st Experience
- Vision Therapy – Additional Training

Changes have also been made for the JAWS screen reader. These improvements include updates towards conveying alert messages and page load completion and the addition of the Alt+K hotkey for the OK button.

### Administration Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

System Administrators can now update a user's DUZ code as depicted in Figure 1.

![](blind-rehab-version-5-1-3-release-notes/002.png)

<span id="_Ref124124733" class="anchor"></span>Figure 1: BR Staff DUZ Code Field

### BR Patient Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Search field now has a bolder outline, allowing users to locate the field with more ease.

![](blind-rehab-version-5-1-3-release-notes/003.png)

<span id="_Toc126321872" class="anchor"></span>Figure 2: Local VistA Site Search

After searching and selecting a patient, the selected patient appears in the Patient Already Selected dialog. To view the selected patient, click OK. A JAWS user can now utilize the Alt+K hotkey to select the OK button.

![](blind-rehab-version-5-1-3-release-notes/004.png)

<span id="_Toc126321873" class="anchor"></span>Figure 3: Patient Already Selected Dialog

When the user clicks the Save and Continue button and required fields are left blank, JAWS will read an alert message for every required field left blank as depicted in Figure 13.

![](blind-rehab-version-5-1-3-release-notes/005.png)

<span id="_Toc126321874" class="anchor"></span>Figure 4: Basic Information with Error Messages

### Create Referrals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New referral types are depicted in Figure 5.

![](blind-rehab-version-5-1-3-release-notes/006.png)

<span id="_Ref124126949" class="anchor"></span>Figure 5: Enter New Referral for this Patient

### Modify Referral (Search)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Modify Referral(Search) reflects the new referral types added as depicted in Figure 6. The referral types will be alphabetized in a future patch.

![](blind-rehab-version-5-1-3-release-notes/007.png)

<span id="_Ref124126592" class="anchor"></span>Figure 6: Referral Types

After the list of referrals found is displayed in a table, it is presented in descending order by Created Date. When clicking on the column headers to sort, the Edit button now correctly reflects the data for the row you wish to edit as depicted in Figure 7.

![](blind-rehab-version-5-1-3-release-notes/008.png)

<span id="_Ref124127679" class="anchor"></span>Figure 7: Referrals Found Table

### Referral Status Save is Read by JAWS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Changes made to a referral status for the Modify Referral(Search) and Modify Referral By Patient functionalities will produce a message stating that the referral status was saved. This message is now read by JAWS.

![](blind-rehab-version-5-1-3-release-notes/009.png)

<span id="_Toc126321878" class="anchor"></span>Figure 8: Change Referral Status

### JAWS Supported Versions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

REDACTED. Figure 9 depicts the supported JAWS versions in a table format.

![](blind-rehab-version-5-1-3-release-notes/010.png)

<span id="_Ref125017630" class="anchor"></span>Figure 9: Supported JAWS Versions

### JAWS 2020 Users Workarounds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When registering a new patient, JAWS will read error messages when pressing the Enter key on the Save and Continue button. JAWS will not read error messages when utilizing the Alt + S hotkey.

![](blind-rehab-version-5-1-3-release-notes/011.png)

<span id="_Toc126321880" class="anchor"></span>Figure 10: Save and Continue Button for Registering New Patient

Once a new patient has been registered, the Edit Blind Patient section will display boxes numbered 1-10 as depicted in Figure 11. JAWS will read these boxes as Tabs.

![](blind-rehab-version-5-1-3-release-notes/012.png)

<span id="_Ref124163889" class="anchor"></span>Figure 11: Edit Blind Patient Tabs

Users that have JAWS 2020 or later versions can use the Tab key to navigate through the 10 Edit Blind Patient tabs. The Space bar can be used to select an Edit Blind Patient tab.

Users that have JAWS 2021 or later versions can utilize the appropriate keystrokes to bring up the JAWS links list. JAWS will read the Edit Blind Patient tabs from the links list.

![](blind-rehab-version-5-1-3-release-notes/013.png)

<span id="_Toc126321882" class="anchor"></span>Figure 12: Edit Blind Patient Tabs Link List

### VIST Annual Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When required fields are left blank, JAWS will read an alert message for every required field left blank as depicted in Figure 13.

![](blind-rehab-version-5-1-3-release-notes/014.png)

<span id="_Ref124126079" class="anchor"></span>Figure 13: Error Messages for Blank Required Fields

A Patient Search can now be performed with the first initial of the patient's last name and the last four digits of their social security number as depicted in Figure 14.

![](blind-rehab-version-5-1-3-release-notes/015.png)

<span id="_Ref124128789" class="anchor"></span>Figure 14: BR Patient Search

### Benefits & Services Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The alert message for a successful save for the Benefits and Services Checklist functionality is now announced by JAWS.

![](blind-rehab-version-5-1-3-release-notes/016.png)

<span id="_Toc126321885" class="anchor"></span>Figure 15:Enter Benefits and Services Checklist

### Letters and Labels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To create a current list, go to Print Patient Mailing Labels and select your desired institution. Click Submit.

    ![](blind-rehab-version-5-1-3-release-notes/017.png)

<span id="_Toc126321886" class="anchor"></span>Figure 16: Patient Mailing Labels – Select Patient Criteria

2.  Click the corresponding Remove button for the labels you do not want as depicted in Figure 17. Once complete, click Continue.

    ![](blind-rehab-version-5-1-3-release-notes/018.png)

<span id="_Ref124129822" class="anchor"></span>Figure 17: Mailing Label Table

3.  Go back to Print Patient Mailing Labels. The option to use the list you edited will be available in the Select Patients Method list as depicted in Figure 18.

    ![](blind-rehab-version-5-1-3-release-notes/019.png)

<span id="_Ref124129885" class="anchor"></span>Figure 18: Patient Mailing Labels – Current List

> **NOTE:** The list you created will not exist after you Logout.

The exported PDF file now prints a sheet of 3x10 labels.

### Print Individual Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The display for patient records was updated to remove the Last Medical Exam date.

REDACTED

<span id="_Toc126321889" class="anchor"></span>Figure 19: Individual Patient Record

### Print Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Exported reports now have the correct date format of MM/DD/YYYY as depicted in Figure 20.

![](blind-rehab-version-5-1-3-release-notes/020.png)

<span id="_Ref124130076" class="anchor"></span>Figure 20: Report Data Download

### Workaround for Referrals Summary Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Navigate to Enter/Edit then Modify Referral (Search).
2.  From the Select Institutionsearch type list, select Referrals From your Institution.
3.  Select All from the Referred To Institutions list.
4.  Select the desired various referral types.
5.  Select the desired date range.

    The example below shows the referrals to all institutions from 01/01/2022 to 12/30/2022 for BRC referral types, referred from Baltimore VAMC institutions, that were Admitted.

    ![](blind-rehab-version-5-1-3-release-notes/021.png)

<span id="_Toc126321891" class="anchor"></span>Figure 21: Modify Referrals

The search yielded 6 referrals of BRC type from Baltimore VMAC that were Admitted for 2022.

![](blind-rehab-version-5-1-3-release-notes/022.png)

<span id="_Toc126321892" class="anchor"></span>Figure 22: Referrals Found

### From: Blind Rehab Version 5.1 Release Notes

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Blind and Visual Impairment Continuum of Care application provides enhanced tracking, and reporting, of the blind rehabilitation services provided to veterans. Features include Electronic referral process to track patient applications for service, notifications feature to alert users of pending referrals, encounters/progress notes will be automatically created, nationwide centralization of BRVS services data to allow nationwide reporting, ad-hoc reporting capabilities, allows the ability to track BRVS patient care access across institutions, and patients can be referred or transferred to other institutions if they move without having to recreate patient data. The VistA namespace is ANRV.

This patch includes many changes and enhancements to Blind Rehabilitation.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These release notes cover the changes to Blind Rehabilitation for this release.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of Blind Rehabilitation and applies to the changes made between this release and any previous release for this software.

## This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide a summary of the new features and functions added, enhancements and modifications to the existing software, and any known issue for Blind Rehabilitation 5.1.

### New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the new features and functions added to the BR 5.1 release.

- Two Factor authentication (2FA) – logon using Personal Identification Verification (PIV) pin.
- A pagination feature was added for search results. The user can select from a dropdown of 5,10,15 or 20 rows displayed per page. The application defaults to 10 rows per a page. Arrows are enabled for moving to the next, previous, or the next set of page results. The previous BR version 5.0 displayed search results in its entirety on a single page.
- The BRS VA TRM/VA Security Standards will be updated. The deployment will be replaced with a VA Enterprise Cloud (VAEC) implementation, using cloud service provider Amazon Web Services (AWS).
- Addition of a SAVE button on each page AND the ability to stay on the page that was saved.
- 508 Compliant changes
  - Ensure that no page element is coded as a table
  - Fixed missing labels and markings of mandatory fields \*
  - Exportable report tables do not have \<th\> header cells
  - Removed verbiage "Select menu item on the left"
  - Error alert message is sent to the screen for BR Patient
  - VIST Annual Review Edit Review buttons have unique labels

#### New Tab – Print VIST Roster Sorts Menu

Previously, the Print VIST Roster Sorts Menu was a submenu under the Print Reports Menu. Now it is a main tab.

The Patient Type drop down box was removed from each report criteria since the low vision patient option was removed throughout the application.

#### BR Patient Submenu Update

BR 5.1 consolidates ALL Mandatory fields onto a preliminary screen that comes up first after selecting the patient. This is highly critical when ADDING a new case to 5.1 as the act of adding the patient is done on one page and then saved before automatically entering the rest of BR Patient option.

The following are Basic Information mandatory field(s):

- Ocular Health
- Patient History
- Living Arrangements
- Blind Rehabilitation Experience

The completion of this page will register the patient after you click Save and Continue. The page(s) following will allow you to skip to different patient information by clicking on any of the boxes as in the sample display below.

Figure 1: BR Patient Page Display

![](blind-rehab-version-5-1-release-notes/002.png)

If data is entered and user clicks on Previous, Save or Next button, the data will be saved. Clicking on the Done button however will not save the data and user will be returned to the home page.

Edit BR patient under Financial /Benefits

- SMC Rating box removed
- Paragraph level box removed
- Annual household income was changed to Monthly Household income

### Enhancements and Modifications to Existing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the enhancements and modifications to the BR 5.1 release.

- Reports were updated from Crystal to Jasper.
- The Help – Application under each submenu was moved to a main menu tab.
- The Logout button was moved to the upper right corner next to the user's login name displayed.
- After a report is displayed, the submenu on the left side remains available on version 5.1 You will not have to click on the main tab at the top of the page after a report is displayed to get back to the list of submenus.

#### Create Referral

Fee Basis was changed to VA funded but this field is slated to be removed.

#### Referral Roster

For all the Referral reports - The ALL option is the default selection whereas previously "All" had to be selected.

#### Modify Referral (Search) Submenu Update

"All" is the default selection for Referred to Institutions, Initiating Areas, Statuses, & Referral Types.

### Removed Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following have been removed for the BR 5.1 release.

- The Waitlist Reporting Menu and Skip to Main Content tabs were removed.
- Entries & Reports related to the following categories: Low Vision Patient, VARO Claims, and Education & In Service Activities were removed.

#### Administration Menu

The following were removed from Administration tab submenu:

- TIU Document Definitions
- MPI Patient Registration
- Patient ICN Lookup
- Patients not registered with MPI
- Visual Acuity Discrepancy

Table 1: Administration Screen Updates

| BR 5.0 Administration                                                                               | BR 5.1 Administration                                                                               |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](blind-rehab-version-5-1-release-notes/003.png) | ![](blind-rehab-version-5-1-release-notes/004.png) |

#### #### #### Enter/Edit Menu

The following submenu items were removed:

- Low Vision Patient
- Education Service Activities
- VARO Claims
- Annual Outcome Survey
- Pre/Post Blind Rehab Survey
- Modify Converted National Waitlist Record
- VIST Visits
- BRC Clinical Assessments
- Create Treatment Plan
- Modify Treatment Plan
- Enter Non-Treatment Plan Training
- Enter Treatment Plan or Training

| BR 5.0 Enter/enter                                                                                  | BR 5.1 Enter/Edit                                                                                  |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| ![](blind-rehab-version-5-1-release-notes/005.png) | ![](blind-rehab-version-5-1-release-notes/006.png) |

#### #### #### Print Individual Records Menu

The following submenus were removed:

- Treatment Plan
- Training History
- Annual Outcome Survey
- Pre/Post Blind Rehab survey

Records can now be exported in different formats (csv, PDF, Word). Previously the records displayed did not have an export option available but had a "Use printer friendly page" option which has since been removed from 5.1 version.

#### Print Reports Menu

The following submenus were removed:

- Low Vision Patients Report
- VARO Claim List
- Education & In Service Activities
- VIST Visits Date List
- BRC Pre-Admission By Priority Level
- BRC Workload Monthly Summary
- BRC Workload Monthly Summary By VISN
- BRC Workload Semi-Annual Summary
- BRC Workload Monthly Summary By VISN
- BROS Workload Summary
- BROS Workload Summary By VISN

### Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Certain patient demographics will not populate until the overnight patient demographics update process runs

1\. Refresh speed in BR Patient Search. Varies from 12 – 30 seconds on average (to bring up the Mandatory Fields). Takes an additional amount of time (usually equal to the 1st delay) to bring up the Basic Information (screen \#1).

2\. Deceased Patient Notification Delete option. Is inconsistent with deletion, sometimes takes 3 tries or more.

3\. Fixing the referrals totals in the VIST Roster Summary Report. This section of the report is currently not working in 5.1.

4\. Fixing the PSD Update for key demographic fields on newly added veterans to 5.1. Currently, address/phone, period of service, race, gender is not updating until the next PSD Update is run (which is now set to nightly). In BR-5.0, this information is updated upon saving the new addition record in 5.0.

5\. Fixing the Print VIST Roster Summary Report issues previously identified (i.e., ICD-10 eye codes, reporting referrals, etc.).

6\. Tweaking the Print Labels feature to better center the printed information near the middle of the Avery Label in each column AND include the 10th row of labels.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*NOTE\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Fixing the PSD Update for newly added Sensitive Record Veterans to 5.1. Currently, Social Security Number (SSN) is not updating until the next PSD Update is run (which is now set to nightly). In BR 5.0, this information is updated upon saving the new addition record in 5.0.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents apply to this release:

- User Manual
- Technical Manual
- Deployment, Installation, Back-out and Rollback Guide

### From: Blind Rehab Version 5.1.18 Release Notes

## Enhancements to the User Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Deceased Patient Notifications were not removed on the first attempt to delete and has been corrected. In addition, the name of the patient has been added to the Deceased Patient Notification link. These notifications will appear for users that were tracking the deceased patient. In addition, if the user had created any referrals for the deceased patient, the patient name and referral number will appear in the Referral Cancellation notification link. This should help increase efficiency as users will not have to open each link to view the patient name and/or referral information to evaluate if the notification is applicable to them.

Any Deceased patient notifications that were created before BR 5.1_14, will not be updated with the patient name. However, any of the links should be removed upon the first attempt to delete the notification.

<span id="_Toc223528799" class="anchor"></span>Figure 1 – Deceased Patient Notifications without patient name

![](blind-rehab-version-5-1-18-release-notes/002.png)

<span id="_Toc223528800" class="anchor"></span>Figure 2 – Deceased Patient Notifications with patient name and referral \#

![](blind-rehab-version-5-1-18-release-notes/003.png)

## Enhancements to Edit Blind Patient page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some enhancements were made to the Edit Blind Patient tabs for the following:

- 2 Ocular Health –  
  the field "Use of Eye Prosthesis" is marked as mandatory
- 3 Patient History –  
  the field "Sight Loss Caused Job Loss?" is marked as mandatory
- 9 Rehabilitation Experience –  
  Vision Therapy types were added to the "Type of Training" drop down list

<span id="_Toc223528801" class="anchor"></span>Figure 3 – "Use of Eye Prothesis" field under Ocular Health

![](blind-rehab-version-5-1-18-release-notes/004.png)

<span id="_Toc223528802" class="anchor"></span>Figure 4 - Vision Therapy types added to Type of Training

![](blind-rehab-version-5-1-18-release-notes/005.png)

## Referrals Information no longer displays previous Admit/Discharged

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following fields were removed from the Referral Information screen since they were not being used.

- Previous Admit Date
- Previous Discharge Date
- Previous Program Type

<span id="_Toc223528803" class="anchor"></span>Figure 5 - Referral Information

> ![](blind-rehab-version-5-1-18-release-notes/006.png)

## VIST Annual Review modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a VIST Annual Review is entered with a Status = COMPLETE, the user can no longer choose "Not Applicable" for Type or Location. For Status = "Could Not Contact", "No Show", or "Declined," Type and Location default to "Not Applicable."

<span id="_Toc223528804" class="anchor"></span>Figure 6 - VIST Annual Reviews

> ![](blind-rehab-version-5-1-18-release-notes/007.png)

## Existing Referrals table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Create Referral Search results table sort by Created Date previously was not sorting chronologically. If you click the sort icon, it will sort by created date in ascending order. If you click it again, it will display it in descending order.

<span id="_Toc223528805" class="anchor"></span>Figure 7 - Sort on Existing Referrals

> ![](blind-rehab-version-5-1-18-release-notes/008.png)

## "Include Deceased patients?" was removed from VIST Roster Sorts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The checkbox to "Include Deceased Patients?" has been removed from all the VIST Roster Sorts report pages. Enabling the checkbox did not include any deceased patients on the reports since deceased patients are removed from the VIST roster when the date of death is entered in VistA.

<span id="_Toc223528806" class="anchor"></span>Figure 8 - "Include Deceased Patients?" on VIST Roster Sorts

![](blind-rehab-version-5-1-18-release-notes/009.png)

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The updates made in this release will most likely need users to do a hard refresh. Some browsers store files in their cache therefore; you may not experience the updates with this software until your cache is cleared. Complete these 2 steps to enable the fixes included in the release.

1.  To refresh CSS, execute: CTRL+F5
2.  To clear your cache, execute the following keystrokes:
    1.  CTRL+ SHIFT + DELETE – Settings window will open
    2.  TAB to the "Cached images" and ensure the box is checked
    3.  TAB to the "Clear Now" button and press ENTER
    4.  CTRL + W to close the Settings window

### From: Blind Rehab Version 5.1.9 Release Notes

### Print Letters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Letters tab has been corrected to allow letters to be printed using the institutions roster list or a trimmed roster list that will persist upon log off.

<span id="_Toc167276016" class="anchor"></span>Figure 1 - Select Patients Method

![](blind-rehab-version-5-1-9-release-notes/002.png)

If the user selects the Load Patient list from Roster, it will load the roster for the institution(s) you have highlighted. A user can begin to edit the list by clicking the Remove button on the row adjacent to the patient's address. This will become your saved patient list after you click the Continue button.

<span id="_Toc167276017" class="anchor"></span>Figure 2 - Remove names from the patient list

![](blind-rehab-version-5-1-9-release-notes/003.png)

The USE CURRENT LIST AND MANUALLY EDIT button will be available if the end user had previously created a unique list by Print Letters – Search Criteria or Print Patient Mailing Labels – Select Patient Criteria. The USE CURRENT LIST AND MANUALLY EDIT - Select Patients Method will not display if prior search criteria were not done. The end user may choose USE CURRENT LIST AND MANUALLY EDIT option; this will become your Saved Patient List. The Saved Patient list persists upon logout.

<span id="_Toc167276018" class="anchor"></span>Figure 3 - Select Patient Criteria - Patient Mailing Labels

![](blind-rehab-version-5-1-9-release-notes/004.png)

The USE BR PATIENT ALREADY SELECTED method will be available if you had executed a BR Patient Search during this log in session. If you had not done any BR patient searches, you will not see it in the Select Patients Method box. Likewise, you will not see the USE YOUR SAVED PATIENT LIST if you have never selected Letters or Mailing Labels to print. If you choose the USE BR PATIENT ALREADY SELECTED option, or the LOAD PATIENT LIST FROM ROSTER, this will become your Saved Patient List. The Saved Patient list persists upon logout.

<span id="_Toc167276019" class="anchor"></span>Figure 4 - Select Patient Criteria for Print Letters

![](blind-rehab-version-5-1-9-release-notes/005.png)

### Print Reports 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reports under the Print Reports tab have been updated to correct the screen reading order when using applications such as JAWS or ZoomText. The reports have also been updated for exported reports in Excel and Word so that they pass the Microsoft Accessibility check.

There is an issue with exporting reports to Word when JAWS is running. This occurs for reports that are larger than 12 pages. Alternate screen reading tools should be used when exporting large reports to Word such as ZoomText or the built in Read Aloud Feature under the Review tab. This issue with JAWS and large Word reports will be fixed in a future release.

<span id="_Toc167276020" class="anchor"></span>Figure 5 - Microsoft Accessibility Check

![](blind-rehab-version-5-1-9-release-notes/006.png)

### Print VIST Roster Sorts Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reports under the Print VIST Roster Sorts Reports tab has been updated to correct the screen reading order when using applications such as JAWS or ZoomText. The reports have also been updated for exported reports in Excel and Word so that they pass the Microsoft Accessibility check.

There is an issue with exporting large reports to Word when JAWS is running. This occurs for reports that are larger than 12 pages. Alternate screen reading tools should be used when exporting reports to Word such as ZoomText or the built in Read Aloud Feature under the Review tab. This issue with JAWS and large Word reports will be fixed in a future release.

<span id="_Toc167276021" class="anchor"></span>Figure 6 - Microsoft Read Aloud

![](blind-rehab-version-5-1-9-release-notes/007.png)

### VIST Roster Summary Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIST Roster Summary Report and VIST Roster Summary Report(by VISN) have been updated to include ICD10 codes. If a patient is still using an ICD9 code on the roster, their ICD9 code will appear in the report and will be marked with an \*. This applies to both Primary and Secondary Cause of Vision Loss.

<span id="_Toc167276022" class="anchor"></span>Figure 7 - ICD10 with some ICD9 codes

![](blind-rehab-version-5-1-9-release-notes/008.png)

The VIST Referrals Applications section have been updated to provide statistics on referrals. For BRC type referrals the quantity of Submitted, Admitted, and Discharged referrals is tracked. For non-BRC type referrals the number of Submitted and Completed referrals is provided for the given reporting period. Vision Therapy type referrals are now included in the report.

<span id="_Toc167276023" class="anchor"></span>Figure 8 - non-BRC VIST Referrals Summary

![](blind-rehab-version-5-1-9-release-notes/009.png)

The VIST Coordinator Encounters and VIST Referrals (VA – Fee for Service) sections have been removed from the VIST Roster Summary Report.

### BR Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enter New Blind Patient has been corrected to make a new staff member's name available in the Tracked By field. Previously, the application would have to be restarted before new staff names could be selected from this drop-down list.

<span id="_Toc167276024" class="anchor"></span>Figure 9 - Tracked By field

![](blind-rehab-version-5-1-9-release-notes/010.png)

### From: Blind Rehab Version 5.1.13 Release Notes

## Enhancements for users requiring use of JAWS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several enhancements were made to help navigating the Blind Rehabilitation application when using JAWS.

1.  The regions on the page are now properly marked so that JAWS users can use keys SHIFT + R to navigate the regions on each page.
2.  After adding patient search criteria and clicking the "Search" button, focus will now move to the patient search results table rather than focus remaining at the Search button.
3.  Previously, JAWS was counting the tab subtask heading as an item in the list when landing on it. For instance, when a user would land on the Enter/Edit subtask, JAWS would say there were 9 in the list when there were only 8 subtasks. The application has now been corrected to only give the number of subtasks in the list.
4.  On the Enter/Edit BR Patient, Edit Blind patient page, there are tabs 1-10 that can be navigated to by using the TAB key. Previously, JAWS would announce the name of the tab and link making it a bit confusing to the user that there may have been 2 items when actually there is only 1 link.

## Patient Search accommodates names that contain an apostrophe

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Previously, the Patient Search or BR Patient Search feature would not recognize a name that contained an apostrophe in VistA. Patient Search will pull in names from VistA if you search with the apostrophe in the search criteria box. However, the patient search results table may or may not display the name with the apostrophe. In this case, the search criteria used for BR Patient Search must be what is shown on their patient record.

<span id="_Toc190421253" class="anchor"></span>Figure 1 - Blind Patient Search results

![](blind-rehab-version-5-1-13-release-notes/002.png)

If the patient's last name displayed an apostrophe in their patient record during enrollment, it must be included in the search criteria for BR Patient Search. Otherwise, it will not find the patient name.

<span id="_Toc190421254" class="anchor"></span>Figure 2 - BR Patient Search result when ' is not included

![](blind-rehab-version-5-1-13-release-notes/003.png)

<span id="_Toc193110428" class="anchor"></span>Figure 3 - BR Patient Search result with ' in last name

![](blind-rehab-version-5-1-13-release-notes/004.png)

## Edit Blind Patient text boxes expand as additional lines of text are entered

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The text boxes for patient history expands as additional lines of text are entered. Previously it was a fixed size and visually limited the lines of text in the display unless you put your cursor in the text box and used your mouse or arrow keys to view additional text.

<span id="_Toc190421255" class="anchor"></span>Figure 4 - Text Area expands with data entered

![](blind-rehab-version-5-1-13-release-notes/005.png)

<span id="_Toc190421256" class="anchor"></span>Figure 5 - Patient Work History

![](blind-rehab-version-5-1-13-release-notes/006.png)

## Field label update for "Gender" to "Sex"

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The field label for "Gender" has been updated to "Sex". This is present in the Current Patient Selected box and on the Patient's Record.

<span id="_Toc193110431" class="anchor"></span>Figure 6 - Current Patient box

![](blind-rehab-version-5-1-13-release-notes/007.png)

## VIST Roster Summary report – Referral Applications summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIST Roster Summary report has been updated for the Referral Applications summary section. Previously, it would show the summary of the BRC & non-BRC referrals that were made from the institution. The change was made to reflect all the VA type referrals that are made to your institution and are completed by the VA. However, the non-VA type referrals statistics are still for those referrals made from a VA institution. The Completions for Non-VA type referrals will be zero unless the VA source choses to complete the non-VA referral. Otherwise, the VA cannot directly receive the referral status from the other agency.

<span id="_Toc190421257" class="anchor"></span>Figure 7 - VIST Referrals Application non-BRC

![](blind-rehab-version-5-1-13-release-notes/008.png)

### From: Blind Rehab Version 5.1.16 Release Notes

## Enhancements for low vision users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The text for User Notifications on the Home page has been enhanced so that the color contrast is stronger when a user hovers on the link. Previously, the text color upon hover did not meet the 508 color contrast criteria.

<span id="_Toc208995463" class="anchor"></span>Figure 1 – User Notifications

![](blind-rehab-version-5-1-16-release-notes/002.png)

## Enhancements for users who require a screen reader

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Application Help contained links that were not understood by users relying on a screen reader for navigation. An icon link for social media sites in the main window for Help was previously reciting incoherent text. This link has been removed since it is not used.

The Page Help link in the main region of each page previously lacked keyboard accessibility for navigation when using a screen reader. Since users do not typically use the page help link, it has been removed from every page. The Application Help tab contains the same Help information and remains available to all users.

<span id="_Toc208995464" class="anchor"></span>Figure 2 – Example of page with Help icon

![](blind-rehab-version-5-1-16-release-notes/003.png)

<span id="_Toc208995465" class="anchor"></span>Figure 3 - Application Help page displaying social media icon

![](blind-rehab-version-5-1-16-release-notes/004.png)

## Pop up modals require confirmation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Previously, pop-up modals would allow users to TAB outside the window and return to the application without closing the pop up. Unsighted users would be unaware that the pop-up modal was still open. The application has been updated so that users cannot continue to use the application without first acknowledging and closing the pop-up window.

These pop-up windows can occur in the following scenarios:

- User attempts to enter/edit data for a patient that is not registered
- User attempts to enter/edit data for a deceased patient
- Warning timeout window opens when a user leaves their session idle

If a user TABs outside the pop-up modal, they will be navigated around the browser window but will not be allowed back to the Blind Rehabilitation application until the pop-up window has been closed.

<span id="_Toc208995466" class="anchor"></span>Figure 4 – Error Encountered for unregistered patient

![](blind-rehab-version-5-1-16-release-notes/005.png)

<span id="_Toc208995467" class="anchor"></span>Figure 5 - Error Encountered for deceased patient

![](blind-rehab-version-5-1-16-release-notes/006.png)

## VIST Roster Summary update for BRC type referrals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIST Roster Summary Report for the VIST Referral Applications (BRC) statistics has been modified. The Submitted column is for all the BRC type referrals that have been <u>referred from</u> your institution. The Admitted and Discharged columns are based on all the BRC type referrals that have been <u>referred to</u> your institution which is unchanged from the previous release.

The section for VIST Referral Applications for non-BRC referrals was not changed.

<span id="_Toc208995468" class="anchor"></span>Figure 6 - VIST Roster Summary Report

![](blind-rehab-version-5-1-16-release-notes/007.png)
