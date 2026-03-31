---
title: MPI/PD Version 1 VISTA Programmer Manual
doc_type: API
doc_label: API Manual
doc_layer: anchor
doc_subject: VISTA Programmer Manual
app_code: MPIF
app_name: Master Patient Index
section: INF
app_status: active
pkg_ns: MPIF
patch_ver: 1
patch_id: MPIF*1
group_key: "MPIF:MPIF:1"
file_numbers: 
  - 985
  - 991
security_keys: []
menu_options: 24
description: 
audience: 
keywords: 
  - strong
  - patient
  - class
  - colspan
  - view
  - vista
  - primary
  - even
  - identity
  - blockquote
page_count: 0
word_count: 40703
section_count: 42
table_count: 60
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: April 1999
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Master_Patient_Index_(MPI)/rg1_0_pm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Master_Patient_Index_(MPI)/rg1_0_pm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=16"
---

---
title: |
  Master Patient Index  
  Patient Demographics (MPI/PD)

  Version 1.0

  Programmer Manual
---

![](mpi-pd-version-1-vista-programmer-manual/001.png)

April 1999

Office of Information and Technology (OI&T)

Revision History

<span id="_Toc510587527" class="anchor"></span>Table i. Documentation Revision History

<table>
<caption><p><span id="_Toc510587531" class="anchor"></span>Table . Supported MPI/PD APIs for which an IA is required</p></caption>
<colgroup>
<col style="width: 10%" />
<col style="width: 69%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11/2018</td>
<td><p>Documentation updates are listed by patch designation and RTC Story.</p>
<p>Software enhancements for this release comprise Patch MPI*1.0*123/Story #782858 (VETS360).</p>
<p>Field added to “Table 1. Primary View Identity Traits stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file)”</p>
<ul>
<li><p>EMAIL ADDRESS (#36.1)</p></li>
</ul></td>
<td>Identity and Security Services/Master Veteran Index team</td>
</tr>
<tr class="even">
<td>4/2018</td>
<td>Corrected references to Self Identified Gender identity in MPI-PD VistA Manuals and HC IdM Manuals based on feedback from the VA Lesbian, Gay, Bisexual, and Transgender (LGBT) Health Program.</td>
<td>Identity and Security Services/Master Veteran Index team</td>
</tr>
<tr class="odd">
<td>10/2017</td>
<td><p>Documentation updates are listed by VistA patch designation and RTC Story.</p>
<p>Software enhancements for this release comprise companion VistA Patch DG*5.3*944/RTC Story 504382 (Sub-Story: 513042): “Add new fields (POB Country and POB Province [not Person Type]) to the PATIENT file, Add trigger to the new fields in the PATIENT file, Enable Auditing on fields in PATIENT file (#2) new fields.”</p>
<p>Fields added to “Section 1.2.2 Primary View Identity Traits”</p>
<ul>
<li><blockquote>
<p>PLACE OF BIRTH COUNTRY (#9.1)</p>
</blockquote></li>
<li><blockquote>
<p>PLACE OF BIRTH PROVINCE (#9.2)</p>
</blockquote></li>
<li><blockquote>
<p>PERSON TYPE (#150)</p>
</blockquote></li>
<li><blockquote>
<p>PERSON TYPE (#.054, .01)</p>
</blockquote></li>
</ul>
<p>Fields added to “Table 4. Data elements monitored in the PATIENT file (#2) for changes”</p>
<ul>
<li><blockquote>
<p>PLACE OF BIRTH COUNTRY (2,.0931)</p>
</blockquote></li>
<li><blockquote>
<p>PLACE OF BIRTH PROVINCE (2,.0932)</p>
</blockquote></li>
</ul></td>
<td>Identity and Security Services/Master Veteran Index team</td>
</tr>
<tr class="even">
<td>5/2017</td>
<td><p>Documentation updates are listed by VistA patch designation and RTC Story. Software enhancements for this release comprise companion VistA Patches DG*5.3*937, RG*1.0*67 and MPIF*1.0*65.</p>
<p>RTC Story 445457/Sub-Stories:</p>
<ul>
<li><blockquote>
<p>455445: “Add new field at the Primary View level #985, Enable audit on new field at the Primary View level #985”</p>
</blockquote></li>
</ul>
<blockquote>
<p>The following fields have been added to the Primary View of the MPI (see “Table 1. Primary View Identity Traits stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file)”):</p>
</blockquote>
<ul>
<li><blockquote>
<p>DEATH STATUS (#118)</p>
</blockquote></li>
<li><blockquote>
<p>PREFERRED NAME (#300)</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>455414: “Add new field to the PATIENT file, Add trigger to the new field in the PATIENT file, Enable Auditing on field in PATIENT file (#2) new field”</p>
</blockquote></li>
</ul>
<blockquote>
<p>The new PREFERRED NAME field (#.2405) been added to the PATIENT (#2) file and are utilized by the MPI. (See “Table 4. Data elements monitored in the PATIENT file (#2) for changes”)</p>
</blockquote></td>
<td>Identity and Security Services/Master Veteran Index team</td>
</tr>
<tr class="odd">
<td>12/2016</td>
<td><p>Documentation updates are listed by VistA patch designation and RTC Story. Software enhancements for this release comprise companion VistA Patches DG*5.3*926, MPIF*1.0*64 and RG*1.0*65. Patch DG*5.3*926 documentation updates:</p>
<p>RTC Story 323008: Enhance VistA Source of Notification field in the PATIENT file (#2):</p>
<ul>
<li><blockquote>
<p>The following fields have been added to the “Table 1. Primary View Identity Traits stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file),” stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file):</p>
</blockquote></li>
</ul>
<ul>
<li><p>SSA VERIFICATION STATUS (#108)</p></li>
<li><p>ID INTEROPERABLTY PERSON TYPE (#109)</p></li>
<li><p>LEVEL OF ASSURANCE (#110)</p></li>
<li><p>DEATH INDICATOR (Y/N)? (#111)</p></li>
<li><p>NOTIFICATION PROVIDER (#113)</p></li>
<li><p>SUPPORTING DOCUMENT TYPE (#114)</p></li>
<li><p>DATE OF DEATH OPTION USED (#115)</p></li>
<li><p>DISCHARGED DATE/TIME (#116)</p></li>
<li><p>DATE OF DEATH OVERRIDE REASON (#117)</p></li>
</ul>
<ul>
<li><blockquote>
<p>The following new field has been added to the PATIENT (#2) file and is utilized by the MPI. (See “Table 4. Data elements monitored in the PATIENT file (#2) for changes”):</p>
</blockquote></li>
</ul>
<ul>
<li><p>SUPPORTING DOCUMENT TYPE (#.357)</p></li>
</ul></td>
<td>Identity Services project/Master Veteran Index team</td>
</tr>
<tr class="even">
<td>12/2015</td>
<td>Patch DG*5.3*915 documentation update, only. Updated glossary entry for Registration Process.</td>
<td>Identity Services project/Master Veteran Index team</td>
</tr>
<tr class="odd">
<td>9/2015</td>
<td><p>Patch RG*1.0*62 documentation updates:</p>
<ul>
<li><blockquote>
<p>Healthcare Identity Management (HC IdM) has requested the removal/deletion of Primary View Rejects (PVRs) and PVR functionality. As of Patch RG*1.0*62:</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Exception #234 (Primary View Reject) are no longer being logged.</p>
</blockquote></li>
<li><blockquote>
<p>A post-init process executed and marked all existing unresolved 234 exceptions as Resolved.</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>In support of the new Date of Death (DOD) requirements to the MPI, the following fields from the PATIENT (#2) file will be added to the OBX message segment of the ADT-A08 HL7 message (See “Table 4. Data elements monitored in the PATIENT file (#2) for changes.”):</p>
</blockquote></li>
</ul>
<ul>
<li><p>DEATH ENTERED BY (#.352)</p></li>
<li><p>SOURCE OF NOTIFICATION (#.353)</p></li>
<li><p>DATE OF DEATH LAST UPDATED (#.354)</p></li>
<li><p>LAST EDITED BY (#.355)</p></li>
</ul>
<p>These fields have been enabled for auditing.</p>
<p>Patch DG*5.3*902 documentation updates:</p>
<ul>
<li><blockquote>
<p>The following new fields have been added to the PATIENT (#2) file and are utilized by the MPI. (See “Table 4. Data elements monitored in the PATIENT file (#2) for changes.”):</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>FULL ICN (#991.1)</p>
</blockquote></li>
<li><blockquote>
<p>FULL ICN HISTORY (#991.91)</p>
</blockquote></li>
</ul>
<blockquote>
<p>Both fields contain the complete Integration Control Number (ICN) value, which includes the Identifier, Delimiter, Checksum, and optional Encryption Scheme.</p>
</blockquote>
<ul>
<li><blockquote>
<p>Additional changes for Increment 13:</p>
</blockquote></li>
</ul>
<ul>
<li><p>Updated Index and Glossary.</p></li>
</ul></td>
<td>Identity Services project/Master Veteran Index team</td>
</tr>
<tr class="even">
<td>7/2013</td>
<td><p>Documentation updates:</p>
<ul>
<li><blockquote>
<p>Organization references and links were updated this manual to reflect the most current changes in the Dept of Veterans Affairs with the release of Patches DG*5.3*863, RG*1.0*60, MPIF*1.0*57.</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>7/2012</td>
<td><p>Patch DG*5.3*837 updates:</p>
<ul>
<li><blockquote>
<p>Replaced VistA Logo w/VA Seal on title page.</p>
</blockquote></li>
<li><blockquote>
<p>Updated appendix titled: "Data Stored on the MPI in Austin" to reflect current MPI VETERAN/CLIENT file (#985).</p>
</blockquote></li>
<li><blockquote>
<p>Updated appendix and table titled: "Primary View Identity Traits" to reflect Primary View of the MPI.</p>
</blockquote></li>
<li><blockquote>
<p>Updated Glossary based on HC IdM feedback.</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>08/02/11</td>
<td><p>Two updates <em><u>not</u></em> generated from a patch release:</p>
<ul>
<li><blockquote>
<p>The appendix titled: <em>“MPI/PD Business Rules”</em> has been updated to remove the CMOR references and renamed to <em>“MPI Glossary of Working Concepts.</em></p>
</blockquote></li>
<li><blockquote>
<p>Reviewed documentation to update for current organizational references and standards.</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>07/2010</td>
<td><p>Patch DG*5.3*821 updates to support the James A Lovell Joint VA/DOD Medical Center in North Chicago:</p>
<ul>
<li><blockquote>
<p>New Treating Facility updates. The SOURCE ID (#20) multiple has been added to the TREATING FACILITY LIST file (#391.91) in VistA.  The SOURCE ID (#.01) and IDENTIFIER STATUS (#1) fields are updated by a Treating Facility update from the Master Patient Index (MPI).</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>11/2009</td>
<td>Final updates to documentation implementing feedback from Product Support (PS) for national release.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>8/2009</td>
<td>Updates based on developer feedback.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>7/2009</td>
<td>MPI_CodeCR1713: Identity Management Data Quality (IMDQ) name change to Healthcare Identity Management (HC IdM).</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>6/2008</td>
<td><p>Patch RG*1*52 makes the following changes in the MPI/PD software:</p>
<ul>
<li><blockquote>
<p>MPI/PD Patient Admin User Menu Removed</p>
</blockquote></li>
</ul>
<blockquote>
<p>The MPI/PD Patient Admin User Menu [RG ADMIN USER MENU] was distributed with patch RG*1.0*49 (released 4/10/08) as obsolete with an Out of Order message. This option is being distributed in this build as DELETE AT SITE in order to remove it from the menu structure. There are other MPI/PD options in the MPIF* and VAFC* namespaces that are also obsolete that will be removed in future MPIF* and DG* patches.</p>
</blockquote>
<ul>
<li><blockquote>
<p>The following Date of Death exceptions in the MPI/PD Exception Handler have been made obsolete:</p>
</blockquote></li>
</ul>
<blockquote>
<p><strong>-</strong> <strong>Exception Type:</strong> Death Entry on MPI not in VISTA.<br />
<strong>Description:</strong> MPI had Date of Death field populated. Vista did not have Date of Death.<br />
<strong>Exception number:</strong> 215.</p>
<p><strong>-</strong> <strong>Exception Type:</strong> Death Entry on Vista not in MPI.<br />
<strong>Description:</strong> VISTA had Date of Death field populated. MPI did not have Date of Death.<br />
<strong>Exception number</strong>: 216.</p>
<p><strong>-</strong> <strong>Exception Type:</strong> Death Entries on MPI and Vista DO NOT Match.<br />
<strong>Description:</strong> MPI and VistA had different dates of death for this patient.<br />
<strong>Exception number:</strong> 217.</p>
</blockquote>
<ul>
<li><blockquote>
<p>REMOTE DATE OF DEATH INDICATED Bulletin Made Obsolete:</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>The Remote Date of Death Indicated notification message generated from the MPI has been made obsolete. This bulletin indicated that the patient had a date of death entered from the sending site but not at the receiving site.</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Obsolete Data Removed from the Unresolved Exception Summary report:</p>
</blockquote></li>
</ul>
<blockquote>
<p>Data referencing the Patient Data Review and CMOR Requests Status has been removed from the Unresolved Exception Summary report. Those issues were made obsolete in earlier patches.</p>
</blockquote></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>3/2008</td>
<td><p>As of Patch DG*5.3*756, the ALIAS [#1] multiple in the PATIENT (#2) file will be updated in VistA resulting from the edits made to that information on the MPI by the IMDQ team. The VistA data will be synchronized to match the MPI values. Additionally, when a facility revises their local ALIAS data, the information will be transmitted to the MPI, which in turn will update all treating facilities where the patient is known.</p>
<p>NOTE: Patch DG*5.3*756 was released on September 6, 2007.</p></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>8/2007</td>
<td><p>Documentation updates for the Patches RG*1*48 and MPIF*1*48, including functionality from Patch DG*5.3*756, which is part of the Master Patient Index (MPI) Changes Project, Iteration 4.</p>
<ul>
<li><blockquote>
<p>VA facilities now have the ability to remotely view Primary View patient identity fields on the Master Patient Index (MPI). This information is available on the MPI in the MPI Patient Data Inquiry [MPI DATA MGT PDAT MPI] option. The report generated by this option displays the current activity scores for individual patient identity fields (i.e., Primary View of the MPI).</p>
</blockquote></li>
<li><blockquote>
<p>In the Primary View of the MPI, the ALIAS multiple (#50) is stored in the MPI VETERAN/CLIENT file (#985). In VistA, the ALIAS multiple (#1) is stored in the PATIENT file (#2). All edits made by Identity Management Data Quality (IMDQ) staff to any of the fields in the ALIAS multiple on the MPI via the Edit PV Alias Values [MPI DATA MGT EDIT PV ALIAS] option, including any pre-existing alias data in that same patient entry that was not edited, is sent to the Primary View of the MPI and now synchronized out to all systems of interest (e.g., VistA treating facilities) for that patient. Site updates to the ALIAS multiple (#1) in the VistA PATIENT file (#2) will be updated in VistA and synchronized to match the MPI values. Additionally, when a VA facility updates their local ALIAS data, the information is sent to the Primary View of the MPI and synchronized back out to all other treating facilities (systems of interest) in which that patient has been seen for care.</p>
</blockquote></li>
<li><blockquote>
<p>The CIRN HL7 EXCEPTION LOG file (#991.1) has been modified to record VA facility personnel who use the MPI/PD Exception Handling option to resolved exceptions and the date/time the resolution occurred. Patch RG*1*48 adds the following new fields to File #991.1:</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>DATE/TIME PROCESSED field (#7)</p>
</blockquote></li>
<li><blockquote>
<p>WHO MARKED PROCESSED field (#8)</p>
</blockquote></li>
</ul>
<blockquote>
<p>This data is now being captured and Identity Management Data Quality (IMDQ) staff will have the capability to view this information.</p>
</blockquote>
<ul>
<li><blockquote>
<p>A change has been made in the MPI/PD EXCEPTION HANDLING [RG EXCEPTION HANDLING] option. Upon selecting the MPI/PD Exception Handling option, instead of being prompted to run the exception purge, you are now notified when the last purge took place. The purge process runs automatically if it has not run within the past two hours; however, the MPI/PD EXCEPTION PURGE [RG EXCEPTION PURGE] option should be scheduled to run once an hour via Taskman. It can take a few minutes to run, but once the job is finished, you can go back to the Message Exception Menu and choose MPI/PD Exception Handling to view the results of the purge process.</p>
</blockquote></li>
<li><blockquote>
<p>A stand-alone option named View VistA Exceptions for Patient [MPI DATA MGT VISTA EXCEPTION] has been implemented on the MPI in Austin for the Identity Management Data Quality (IMDQ) team allowing them to query a VistA site for a selected patient and view all the existing VistA exceptions for a given date range. The VistA side support for this new MPI option came in as part of Patch RG*1*48.</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>3/2007</td>
<td><p>As of Patches MPIF*1*46 and RG*1*44, this documentation has been updated to reflect the following:</p>
<p>Patch MPIF*1*46:</p>
<ul>
<li><blockquote>
<p>Processing to account for the HL7 PID segment message being greater than 245 characters.</p>
</blockquote></li>
<li><blockquote>
<p>Resume correct prompting for identity fields in the first part of PIMS Registration options for new patients.</p>
</blockquote></li>
<li><blockquote>
<p>Updated screening to prevent Primary View Reject exceptions from entering the Potential Matches Returned logic.</p>
</blockquote></li>
<li><blockquote>
<p>Changed exception text for the new Primary View Reject exception.</p>
</blockquote></li>
</ul>
<p>Patch RG*1*44:</p>
<ul>
<li><blockquote>
<p>Functionality incorporated into the MPI/PD Exception Handling RG EXCEPTION HANDLING option to automatically process the "Primary View Reject" exceptions. Name change for exception action that processes reject exceptions "PVR View PV Rej Detail."</p>
</blockquote></li>
<li><blockquote>
<p>MPI/PD Exception Purge process updated. For every date that an exception occurs for a patient, the exception occurs in the Exception Handler for review. However, if more than one active Primary View Reject exception occurs during the same day for the same patient, the purge will remove the duplicate occurrences, leaving only the most recent.</p>
</blockquote></li>
<li><blockquote>
<p>Alias Social Security Numbers included in the HL7 ADT-A31 update message.</p>
</blockquote></li>
<li><blockquote>
<p>Processing to ensure that pending updates to the Primary View waiting in the ADT/HL7 PIVOT file (#391.71) are not lost in IMDQ override process.</p>
</blockquote></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>1/2007</td>
<td><p>As of Patches MPIF*1*44 and RG*1*45, this documentation has been updated to reflect the following:</p>
<ul>
<li><p>The concept of a "CMOR facility" is being phased out and will be replaced by the Primary View when Patch MPI*1*40 is installed on the Austin MPI. VistA Patch MPIF*1*44 sets all VistA options related to "CMOR" out of order, rendering them obsolete. The OUT OF ORDER MESSAGE field for these options is marked as "Obsolete with Patch MPIF*1*44."</p></li>
<li><p>As of Patch MPIF*1*44, the Site Parameters Edit for CMOR [MPIF SITE PARAMETER] option, located on the MPI/PD Patient Admin Coordinator Menu, is obsolete and has been placed out of order.</p></li>
<li><p>As of Patch MPIF*1*44, the AUTO CHANGE CMOR NIGHT JOB [MPIF CMOR REQUEST AUTO JOB] option is obsolete. Sites that have this option scheduled to run via TaskMan, should unschedule it.</p></li>
<li><p>SSN VERIFICATION STATUS field (#.0907) is now synchronized out to Sites when updated by Enrollment System Redesign (ESR) as of Patch RG*1*45.</p></li>
</ul></td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>4/2006</td>
<td>Updates to documentation based on Patches MPIF*1*43 and RG*1*43, which comprise the changes to the MPI/PD software resulting from the Health Eligibility Center (HEC) Enumeration to the Master Patient Index (MPI).</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="odd">
<td>1/2005</td>
<td>Changed references to ICNs to include that they follow the ASTM e1714-95 standard for a universal health identifier, edited/clarified description references to ICNs, and provided new example for the 29 character ICNs as described in the standard.</td>
<td>Identity Services project/Master Patient Index team</td>
</tr>
<tr class="even">
<td>12/2004</td>
<td>Implemented new conventions for displaying TEST data. See Orientation section for details.</td>
<td>Master Patient Index team</td>
</tr>
<tr class="odd">
<td>5/2004</td>
<td>Updates to the MPI/PD VistA Version 1.0 Programmer Manual release based on Patches MPIF*1*33, RG*1*35 and DG*5.3*589 to support the MPI Changes Iteration 2 project</td>
<td>Master Patient Index team</td>
</tr>
<tr class="even">
<td>6/2003</td>
<td>MPI/PD VistA Version 1.0 Programmer Manual released in conjunction with patches DG*5.3*505, and MPIF*1*28 of the MPI Changes Iteration I project</td>
<td>Master Patient Index team</td>
</tr>
<tr class="odd">
<td>4/1999</td>
<td>Initial MPI/PD and MPI VistA User Manuals were created for release with the MPI/PD V.1.0 software in April 1999.</td>
<td>Master Patient Index team</td>
</tr>
</tbody>
</table>

<span id="_Toc510587531" class="anchor"></span>Table . Supported MPI/PD APIs for which an IA is required

Patch History

For the current patch history related to this software, please refer to the Patch Module (i.e., Patch User Menu \[A1AE USER\]) on FORUM.

Contents

Tables and Figures

Orientation

How to Use this Manual

This manual uses several methods to highlight different aspects of the material.

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

Table ii. Documentation Symbol Descriptions

| Symbol                                                                                                     | Description                                                                                                |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/002.png) | NOTE: Used to inform the reader of general information including references to additional reading material |
| ![](mpi-pd-version-1-vista-programmer-manual/003.png)                                                              | CAUTION: Used to caution the reader to take special notice of critical information                         |

<span id="_Toc510587532" class="anchor"></span>Table . Supported APIs to which MPI/PD subscribes

- Descriptive text is presented in a proportional font (as represented by this font).
- "Snapshots" of computer online displays (i.e., character-based screen captures/dialogs) and computer source code are shown in a non-proportional font and enclosed within a box.
- User's responses to online prompts will be boldface type.
- The "\<Enter\>" found within these snapshots indicate that the user should press the Enter or Return key on their keyboard.
- Author's comments are displayed in italics or as "callout" boxes.

|                                                                                                                |                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/004.png) | NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

<span id="_Ref408234376" class="anchor"></span>Table . Data elements monitored in the PATIENT file (#2) for changes

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the XUPROGMODE key).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) will begin with either "000" or "666."
- Person, patient, and user names will be formatted as follows:

> \[application name\]PERSON,\[fictitious given name\]; \[application name\]PATIENT,\[fictitious given name\]; and \[application name\]USER,\[fictitious given name\] respectively.

> The "fictitious given name" represents a fabricated given name for the patient, person or user. Using a name (rather a number) more clearly represents test data when it’s used in descriptive text in this documentation to convey a concept or comparison. For example: MVIPERSON,SAM; MVIPATIENT,NANCY; MVIUSER,DEBRA, etc.

> **NOTE:** The business owner, Healthcare Identity Management (HC IdM), requested we use the following nomenclature to represent test data for HC IdM Caseworkers: “HC IdM,CASE WORKER.

Intended Audience/Assumptions

This manual is written with the assumption that the reader is familiar with the VistA computing environment. It is written with the assumption that the reader is familiar with the VistA computing environment. No attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere.

Reference Material

Readers who wish to learn more about the Master Patient Index/Patient Demographic (MPI/PD) software should consult the following VA Web sites:

- VA Software Document Library (VDL) Web site:

> [MPI/PD documentation on the VA Software Document Library (VDL)](http://www.va.gov/vdl/application.asp?appid=16)

- The MPI/PD product documentation, as found at the link above, includes the following manuals:
- Master Patient Index/Patient Demographics (MPI/PD) VistA User Manual
- Master Patient Index/Patient Demographics (MPI/PD) VistA HL7 Interface Specifications
- Master Patient Index/Patient Demographics (MPI/PD) VistA Technical Manual
- Master Patient Index/Patient Demographics (MPI/PD) VistA Programmer Manual
- Master Patient Index (MPI) VistA Monograph
- Also see the VistA Duplicate Record Merge manuals listed below, which can be found on the VA Web site:

> [Duplicate Record Merge: Patient Merge documentation on the VA Software Document Library (VDL)](http://www.va.gov/vdl/application.asp?appid=2)

- *Duplicate Record Merge: Patient Merge Release Notes for Kernel Toolkit Patch XT\*7.3\*113.*
- *Duplicate Record Merge: Patient Merge User Manual, Version 7.3, Patch XT\*7.3\*113*
- *Duplicate Record Merge: Patient Merge Technical Manual, Version 7.3, Patch XT\*7.3\*113*Installation Information and Procedures

The Master Patient Index and Patient Demographics were distributed and installed together. All installation information and procedures involved with the MPI is included in the *CIRN Patient Demographics (CIRN-PD) Pre-Installation and Implementation Guide v.5* document on the VA Software Document Library Web site:

> [MPI/PD documentation on the VA Software Document Library (VDL)](http://www.va.gov/vdl/application.asp?appid=16)

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/005.png) | NOTE: One of the major pre-implementation tasks is the merging of duplicate patient records at a site. The *"Duplicate Record Merge: Patient Merge (Patch XT\*7.3\*23) User Manual"* is required for this task. Patches XT\*7.3\*49, RG\*1\*6, and RG\*1\*10 allow sites with MPI/PD to resolve duplicate records. If you do not have these patches installed, it is recommended that the option to merge patient records be placed out of order. |

Interaction Between MPI/PD and Other Packages

Because of the close interaction between MPI/PD and other packages, you may also find it helpful to review the documentation for the following VistA software:

- VistA HL7 V. 1.6
- PIMS V. 5.3 Admission, Discharge and Transfer (ADT)

VistA documentation is made available online in Microsoft Word format and in Adobe Acrobat Portable Document Format (PDF).

How to Obtain Technical Information Online

Exported VistA M-based file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

|                                                                                                                |                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/006.png) | NOTE: Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. |

Help at Prompts

VistA M-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA software.

To retrieve online documentation in the form of Help in VistA character-based software:

- Enter a single question mark ("?") at a field/prompt to obtain a brief description. If a field is a pointer, entering one question mark ("?") displays the HELP PROMPT field contents and a list of choices, if the list is short. If the list is long, the user will be asked if the entire list should be displayed. A YES response will invoke the display. The display can be given a starting point by prefacing the starting point with an up-arrow ("^") as a response. For example, ^M would start an alphabetic listing at the letter M instead of the letter A, while ^127 would start any listing at the 127th entry.
- Enter two question marks ("??") at a field/prompt for a more detailed description. Also, if a field is a pointer, entering two question marks displays the HELP PROMPT field contents and the list of choices.
- Enter three question marks ("???") at a field/prompt to invoke any additional Help text that may be stored in Help Frames.

Obtaining Data Dictionary Listings

Technical information about VistA M-based files and their associated fields is stored in data dictionaries. You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

|                                                                                                                |                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/007.png) | REF: For details about obtaining data dictionaries and about the formats available, please refer to the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User Manual*. |

Legal DisclaimersSoftware

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

Documentation

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Product Description―What Comprises the Master Patient Index?](#product-descriptionwhat-comprises-the-master-patient-index)
    - [Master Patient Index (Austin)](#master-patient-index-austin)
    - [Master Patient Index/Patient Demographics (VistA)](#master-patient-indexpatient-demographics-vista)
    - [Primary View Replaces Obsolete CMOR View](#primary-view-replaces-obsolete-cmor-view)
    - [Systems of Interest to the MVI—Treating Facilities and Non-VistA Systems](#systems-of-interest-to-the-mvitreating-facilities-and-non-vista-systems)
  - [Primary View—How are VistA Sites Affected by this Change to the MPI?](#primary-viewhow-are-vista-sites-affected-by-this-change-to-the-mpi)
    - [Primary View Auto-Updates Person Identity Fields in the VistA Patient File (#2)](#primary-view-auto-updates-person-identity-fields-in-the-vista-patient-file-2)
    - [Primary View Identity Traits](#primary-view-identity-traits)
- [MPI/PD Frequently Asked Questions (FAQ)](#mpipd-frequently-asked-questions-faq)
  - [What is the Master Patient Index (MPI)?](#what-is-the-master-patient-index-mpi)
  - [How do I Get Primary View Data?](#how-do-i-get-primary-view-data)
  - [How do I Get Correlation Data?](#how-do-i-get-correlation-data)
  - [Is the MPI the Authoritative Source for this Information?](#is-the-mpi-the-authoritative-source-for-this-information)
  - [What is an Integration Control Number (ICN)?](#what-is-an-integration-control-number-icn)
  - [What Does an ICN Look Like?](#what-does-an-icn-look-like)
  - [How Does a Patient Get an ICN?](#how-does-a-patient-get-an-icn)
  - [Where is the ICN Stored?](#where-is-the-icn-stored)
  - [What is a Local ICN?](#what-is-a-local-icn)
  - [Under What Conditions are Local ICNs Assigned to Patient Records?](#under-what-conditions-are-local-icns-assigned-to-patient-records)
  - [How Can I Retrieve a Patient's ICN as a VistA Developer/Application?](#how-can-i-retrieve-a-patients-icn-as-a-vista-developerapplication)
  - [What Causes a Patient Record Not to Have a National ICN Assignment?](#what-causes-a-patient-record-not-to-have-a-national-icn-assignment)
  - [What Causes a Patient Record to Have Only a Local ICN Assignment?](#what-causes-a-patient-record-to-have-only-a-local-icn-assignment)
  - [Can a Patient's ICN Change?](#can-a-patients-icn-change)
  - [How Can I Tell if an ICN has Change?](#how-can-i-tell-if-an-icn-has-change)
  - [Can a Vendor Use an ICN to Identify a Patient?](#can-a-vendor-use-an-icn-to-identify-a-patient)
  - [How Can My VistA Application Get an ICN Assignment for a Patient?](#how-can-my-vista-application-get-an-icn-assignment-for-a-patient)
  - [What is the Communication Procedure with the MPI?](#what-is-the-communication-procedure-with-the-mpi)
  - [How Do I Ensure Test System Data is Not Sent to the MPI?](#how-do-i-ensure-test-system-data-is-not-sent-to-the-mpi)
  - [How Do I Block Automatic Calls to a Patient if Other Treating Facilities Don’t Use the Same Characters?](#how-do-i-block-automatic-calls-to-a-patient-if-other-treating-facilities-dont-use-the-same-characters)
  - [How/Where Do We Find the Correct Patient DFN Used in Exception Messages?](#howwhere-do-we-find-the-correct-patient-dfn-used-in-exception-messages)
  - [Should Sensitive Patients be Shared Between Sites?](#should-sensitive-patients-be-shared-between-sites)
- [MPI/PD FAQ—HL7, Links, Background Jobs, Etc.](#mpipd-faqhl7-links-background-jobs-etc)
  - [Re-enable MPIVA DIR Link?](#re-enable-mpiva-dir-link)
  - [Are TCP/IP Links Managed Differently Than Other Links?](#are-tcpip-links-managed-differently-than-other-links)
  - [How Do I Interpret a DNS Address?](#how-do-i-interpret-a-dns-address)
  - [How Do I Interpret the HL7 Systems Monitor?](#how-do-i-interpret-the-hl7-systems-monitor)
  - [How Do I Correctly Shutdown the UCX Service For My Listener?](#how-do-i-correctly-shutdown-the-ucx-service-for-my-listener)
  - [How Do I Resolve Links in ERROR or SHUTDOWN State?](#how-do-i-resolve-links-in-error-or-shutdown-state)
  - [How Do I Restart MPIVA DI if in SHUTDOWN State?](#how-do-i-restart-mpiva-di-if-in-shutdown-state)
  - [How Do I Resolve a Link in an ERROR State?](#how-do-i-resolve-a-link-in-an-error-state)
  - [What is the INACTIVE State?](#what-is-the-inactive-state)
  - [Purging the HL7 Globals?](#purging-the-hl7-globals)
- [Callable Routines](#callable-routines)
  - [Supported APIs](#supported-apis)
  - [Supported APIs (IA Required)](#supported-apis-ia-required)
  - [Supported APIs (IA Required) to Which MPI/PD is a Subscriber](#supported-apis-ia-required-to-which-mpipd-is-a-subscriber)
  - [MPI Direct Connect](#mpi-direct-connect)
- [Background Jobs](#background-jobs)
  - [LOCAL/MISSING ICN RESOLUTION](#localmissing-icn-resolution)
  - [UPDATE BATCH JOB FOR HL7 v2.3](#update-batch-job-for-hl7-v23)
- [Glossary](#glossary)
  - [# Index](#index)
This is the Programmer Manual for the Master Patient Index/Patient Demographics (MPI/PD) VistA. It is designed to provide you, the Veterans Health Information Systems and Technology Architecture (VistA) developer, with information about the programming functions of MPI/PD. This manual covers the Application Programming Interfaces (APIs) involved with MPI/PD. It provides information on which call(s) to use to perform a particular task, how to use the call(s), and if applicable, which messages to subscribe to. This manual also dedicates a chapter to MPI/PD Frequently Asked Questions (FAQ). It provides an overview of the technical aspects of this software and how VistA developers use the APIs to and get ICN assignments and retrieve patient data for patients. This is among other pertinent topics geared for a technical audience.
Overview of Master Veteran Index (MVI)
The Master Veteran Index (MVI) is the authoritative source for *<u>person identity data</u>*. It maintains identity data for persons across VA systems, provides a unique universal identifier for each person, stores identity data as correlations for each system where a person is known, provides a probabilistic matching algorithm, and includes the Master Patient Index (MPI), Person Service Identity Management (PSIM), and Toolkit (TK). It maintains a “gold copy” known as a “Primary View” of the person’s identity data. Broadcasts identity trait updates to systems of interest.
The MPI Austin is the data store of person records and one of the component pieces of the Master Veteran Index. It is a cross-reference or index of persons that includes the person's related identifiers and other patient identifying information. The MVI is used to associate a person's identifiers among multiple ID-assigning entities, possibly including a Health Data Repository, to support the consolidation and sharing of a patient’s health care information across VHA. The MVI is the authoritative source for *<u>patient identity</u>*.
Overview of Master Patient Index/Patient Demographics
This is the documentation for the Master Patient Index/Patient Demographics (MPI/PD) software.
MPI/PD was developed to initialize active persons to the Master Veteran Index (MVI) and to establish the framework for the sharing of person information between sites. During the process of initialization to the Master Veteran Index, each active person received:
- An Integration Control Number (ICN)
- A Coordinating Master of Record (CMOR) – no longer utilized
- A Treating Facility List of sites where the person is also known by this ICN
Each site becomes part of the network of sites that share key demographic data for patients via HL7 messaging. Master Patient Index VistA (MPI) and Patient Demographics (PD) were distributed and installed together. This manual covers the functionality of both packages.
The objectives of the MPI/PD are to:
- Create an index that uniquely identifies each active person treated by the Veterans Administration.
- Identify the sites where a person is receiving care.
This is crucial to the sharing of person information across sites.
Master Patient Index Patch MPI\*1\*40 constituted a change in the business process that updates the person identity fields across VA facilities. As of Patch MPI\*1\*40, the Primary View methodology was introduced, phasing out the use of the facility Coordinating Master of Record (CMOR) concept. Primary View is an enterprise view of the most current data for a person based on authority scoring and the latest data rules.
Distinguishing MPI (Austin) from MPI/PD at the VA Facilities
The actual index referred to as the *<u>Master Patient Index (MPI)</u>* is located at the Austin Information Technology Center (AITC). *<u>Master Patient Index/Patient Demographics (MPI/PD)</u>* refers to the software that resides at the VA facilities, which sends patient data to the MPI (Austin). These terms \[i.e., MPI (Austin) and MPI/PD\] are used throughout this manual only when it is not obvious which component of the MPI the documentation is referring. Otherwise, the reader should assume the information is referring to MPI/PD.
MPI Identity Hub for the Healthcare Identity Management (HC IdM) Team
As of the release of MPI/PD Patches MPIF\*1\*52 and RG\*1\*54, the MPI Identity Hub for Healthcare Identity Management (HC IdM) was implemented enabling the change from the current MVI person deterministic lookup to an Identity Hub based probabilistic patient lookup.
Initiate was purchased to be integrated with the MPI and Person Service Identity Management (PSIM) for the purpose of improving the matching of patients and persons across VHA. PSIM will serve as the interface to the commercial Identity Management system and the MPI will interact with PSIM.
The Initiate centralized probabilistic search algorithm will replace the local VistA KERNEL DUPLICATE RECORD MERGE search process for identifying local potential duplicate PATIENT file (#2) records. When the search algorithm identifies potential duplicates, they are automatically added to the VistA DUPLICATE RECORD file (#15).
|                                                                                                                |                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/008.png) | REF: For more information on the VistA DUPLICATE RECORD MERGE release, please refer to Kernel Toolkit Patch XT\*7.3\*113. |

## Product Description―What Comprises the Master Patient Index?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Master Patient Index (Austin)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Master Patient Index (MPI) is located at the Austin Information Technology Center (AITC). It is composed of a unique list of persons and an associated list of VAMCs (Veterans Affairs Medical Centers) and other systems of interest where each person has been seen. This enables the sharing of person data between operationally diverse systems. Each person record (or index entry) on the MVI contains multiple demographic fields which are updated to the Primary View.

When a person is first presented into the MVI for an Integration Control Number (ICN) assignment, that person's identifying information (i.e., name, Social Security Number (SSN), date of birth, gender, mother's maiden name, multiple birth indicator, place of birth city and state) is passed to the MVI.

The MVI checks to see if an exact match on Name (first and last), SSN, date of birth, and gender is found. A check is also made to see if the person's internal entry number (DFN) from the querying site is already known to the MVI. If so, this is also considered an exact match. If an exact match is found, the ICN, and ICN Checksum are returned to the requesting site. The requesting site is added to the list of treating facilities (TF) in which this person has been seen and the updated list is broadcasted to all systems of interest, including VAMCs.

If a match is not found, the MVI returns a message indicating this. The patient entry is then added to the MVI. If a potential match is found, a potential match exception is logged for the HC IdM group to review, the person is still added to the MVI.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/009.png) | NOTE: The term "systems of interest" refers to VA facilities that have seen persons and entered them as entries onto the MVI. This also refers to non-VistA systems that have a registered interest in a person (e.g., Federal Health Information Exchange \[FHIE\], HomeTeleHealth, Person Service Identity Management \[PSIM\], Health Data Repository \[HDR\], etc.). |

#### HC IdM Team is Data Steward for the Master Veteran Index (MVI)

The Healthcare Identity Management (HC IdM) team is the Data Steward for the Master Veteran Index (MVI). The HC IdM team is comprised of analysts who have considerable experience working with the MVI and person data updates. They have the ability to perform the following functions on the Primary View of the MVI:

- View and/or edit the authority values for the Primary View business rules criterion.
- Override Primary View identity traits for selected identity fields in the MPI VETERAN/CLIENT file (#985) and broadcast the new Primary View out to the systems of interest.
- View the Primary View Reject Report from the data in the MPI REJECTED UPDATE file (#985.65).

### Master Patient Index/Patient Demographics (VistA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Master Patient Index/Patient Demographics (MPI/PD) software resides in VistA enabling sites to:

- Request an ICN assignment
- Resolve a potential duplicate on the MVI.
- Query the MVI for known data.
- Update MVI MPI when changes occur to demographic fields stored on the MVI or of interest to other facilities/systems of interest.

#### Requesting an ICN Assignment

During the initialization of the MVI, each VA Medical Center sent batch HL7 messages to the MVI requesting ICNs for all persons whose records reflected activity in the past three fiscal years (i.e., active patient records).

In day-to-day operations, persons are presented to the MVI via:

- PIMS options:
  - Load/Edit Patient Data \[DG LOAD PATIENT DATA\]
  - Register a Patient \[DG REGISTER PATIENT\]
  - Electronic 10-10EZ Processing \[EAS EZ 1010EZ PROCESSING\]
- Local/Missing ICN Resolution \[MPIF LOC/MIS ICN RES\] background job

When a new patent record is created via the PIMS options, a real-time connection is established to the MVI requesting an ICN assignment. If communication cannot be established or is lost with the MVI before the ICN assignment process has completed, a local ICN is assigned. Otherwise, a national ICN is assigned to the person. The ICN can either be newly created or already on the MMVIPI for that person. The ICN, ICN checksum, and list of facilities, including other systems of interest (e.g., FHIE and HDR), are updated in the site's VistA system.

If an existing person record is edited via the PIMS options, and if this person does not have an ICN (national or local), the same process occurs as was illustrated for a newly created person.

If a person record is edited or created outside of the PIMS options, they are presented to the MVI for ICN assignment via the Local/Missing ICN Resolution background job.

If a match is not found the MVI returns a message indicating this and that the person is being added to the MVI. If potential matches are found, a new ICN is assigned to the person, and an exception is logged for the Health Care Identify Management (HC IdM) group to review and provide the appropriate action.  If the persons are truly the same person, then the records will be linked together with one ICN becoming the primary ICN that all records will be linked under and the other will be deactivated.  The sites that had the deactivated ICN will be updated to the primary ICN.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 89%" />
<col style="width: 2%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">![](mpi-pd-version-1-vista-programmer-manual/010.png)</td>
<td><strong>NOTE:</strong> As of MPI/PD Patch MPIF*1*52, all screens and actions associated with the MPI/PD Exception Handler functionality for resolving Potential Match Exceptions have been removed from MPI/PD. This functionality is now supported in the Identity Management Toolkit.</td>
<td></td>
</tr>
<tr class="even">
<td>![](mpi-pd-version-1-vista-programmer-manual/011.png)</td>
<td colspan="3"><p><strong>NOTE</strong>: MPI/PD updates as of VistA Patches MPIF*1*43 and RG*1*43:</p>
<ul>
<li><blockquote>
<p>The only times local ICNs are assigned to person records are when:</p>
</blockquote>
<ul>
<li><blockquote>
<p>The connection to the MVI cannot be established, or has been lost before the ICN assignment was completed.</p>
</blockquote></li>
</ul></li>
</ul>
<blockquote>
<p>This happens regardless of which process is used to present the person to the MVI for ICN assignment (i.e., Register a Patient, Load/Edit Patient Data, Electronic 10-10EZ Processing, and/or the Local/Missing ICN Resolution Background Job).</p>
</blockquote>
<ul>
<li><blockquote>
<p>The site edits an existing person or adds a new person using an option that doesn't directly interact with the MVI (e.g., VistA Lab or VA FileMan). </p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>All existing exceptions that were active in the CIRN HL7 EXCEPTION LOG file (#991.1) of the types listed below, were marked with a status of PROCESSED:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Required field(s) missing for person sent to MVI</p>
</blockquote></li>
<li><blockquote>
<p>SSN Match Failed</p>
</blockquote></li>
<li><blockquote>
<p>Name Doesn't Match</p>
</blockquote></li>
</ul></li>
</ul>
<blockquote>
<p>These three exceptions listed are no longer generated. </p>
</blockquote>
<ul>
<li><blockquote>
<p>As part of RG*1*43, the View Potential Match Patient [RG EXCEPTION POTENTIAL MATCH] option has been removed from the Message Exception Menu [RG EXCEPTION MENU] as it is obsolete.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

The Display Only Query option allows the site to query the MVI to see what the MVI would return if the person was presented for ICN assignment without actually making the request. The person can be an existing person or the user can choose to enter the name, date of birth and SSN (not required) and see what the MVI returns.

|                                                                                                                |                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/012.png) | REF: More information about the "Potential Duplicate PATIENT records found by MPI" message is available via the installation of VistA Kernel Toolkit Patch XT\*7.3\*113. |

### Primary View Replaces Obsolete CMOR View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As part of the MPI Changes Project, Iteration 4, the concept of a "CMOR facility" is being phased out and will be replaced by the Primary View when Patch MPI\*1\*40 is installed on the Austin MPI. VistA Patch MPIF\*1\*44 sets all VistA options related to "CMOR" out of order, rendering them obsolete. The OUT OF ORDER MESSAGE field for these options is marked as "Obsolete with Patch MPIF\*1\*44." Obsolete options will be removed from the Coordinating Master of Record (CMOR) Request \[MPIF CMOR MGR\] menu at a future date.

### Systems of Interest to the MVI—Treating Facilities and Non-VistA Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The term "systems of interest" refers to VA facilities that have seen persons and entered them as entries onto the MVI. This also refers to non-VistA systems that have a registered interest in a person (e.g., Federal Health Information Exchange \[FHIE\], HomeTeleHealth, Person Service Identity Management \[PSIM\], Health Data Repository \[HDR\], etc.).

A facility's relationship to a person determines what information it receives and sends. MPI/PD stores this information.

Any facility where a person is identified by the same ICN (regardless of VISN) is placed on the Treating Facility List. The list may contain other systems of interest that are not VAMCs (e.g., FHIE and HDR).

|                                                                                                                |                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/013.png) | NOTE: The Treating Facility List is utilized by several other VistA applications, including Inter-facility Consults and Remote Data Views in CPRS. |

## Primary View—How are VistA Sites Affected by this Change to the MPI?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the Primary View?

Patch MPI\*1\*40 constitutes a change in the business process that updates the patient identity fields across VA facilities referred to as the Primary View of the MVI, overview as follows:

- Primary View is an update to the patient identity fields across VA facilities.
- Primary View creates a centralized view of the patient data aka a Primary View
- Primary View has the best data from any combination of sites for the patient
- Synchronizing the patient identity fields becomes centralized under a new set of business rules on the MVI.
- Primary View is a transition from and *disassociated* with the Coordinating Master of Record (CMOR) view of the MPI.
- Primary View allows for:
- VistA sites to continue to edit patient data at their site.
- Patient data is sent to a central system (i.e., the Master Patient Index) to determine validity and quality

This is an enterprise view of the most current data for a person based on authority scoring and the latest data rules. Edits to patient identity traits (listed below) are evaluated based on the same. The highest score achieves the best quality of data updates to the Primary View*.* These values are stored in the MPI VETERAN/CLIENT file (#985) on the MVI (*<u>not</u>* a VistA file).

- Name
- Social Security Number
- Date of Birth
- Gender
- Mother's Maiden Name
- Multiple Birth Indicator (Sent and updated to Primary View as of Patch RG\*1\*45. Added to the list of fields auto-updated \[synchronized\] in VistA as of Patch RG\*1\*47.)
- Place of Birth, City and State
- SSN Verification Status (Verified, Invalid Per SSA, and Null) (Added to File \#985 as of Patch MPI\*1\*40. Populated to the Primary View of the MVI and systems of interest to the MVI as of DG\*5.3\*688 \[EVC R2\].)
- Pseudo SSN Reason (Added to File \#985 as of Patch MPI\*1\*40. Populated to the Primary View of the MVI and systems of interest to the MVI as of RG\*1\*47 and DG\*5.3\*653 \[EVC R1\].)

How Does the Primary View Work?

Before Patch MPI\*1\*40, person data reviews were done at the CMOR sites. All VA facilities nation-wide had responsibility to manage and maintain their set of person. With the release of Patch MPI\*1.0\*40, person updates are controlled by centralized business rules and Primary View scoring on the MVI. HC IdM staff have the ability to override the rejection process of any valid edits.

In the transition to Primary View*,* when a patient is new to the NVI or an existing patient is initialized under the latest business rule changes, the CMOR process for resolving Patient Data Reviews no longer exists. Instead, edits are processed against the centralized data rules and Primary View scoring on the MVI. If the data update is rejected, it will not be updated in the primary view.  If this field is a synchronized field, the primary view will be sent to that system attempting to make the update to reject the data and changing it to the current primary view. This took the burden off CMOR sites to review other sites’ edits for acceptance or rejection.

Business Rules for Data Validity and Integrity

The Healthcare Identity Management (HC IdM) team has developed two spreadsheets that dictate business rules for the Primary View:

- "Business Processes That Update Person Identity"—Authority score
- "Primary View Data Rules"—Data rules

Person identity fields in the Primary View of the MVI are evaluated and updated based on scoring and data rules. The Primary View score is evaluated based on criteria captured from person encounters at VA facilities (e.g., active prescriptions, admission or registration in the last year, lab test, or radiology exam in the last year) that are sending the inbound update (i.e., data entered by users or sent from a system of interest) to the MVI. The score is calculated from data updates coming from the site. Data is weighed on a field-by-field basis against any differences on the MVI to determine if the score for the inbound edits is equal to or greater than the score for the existing Primary View*.* Next, the inbound edit is evaluated against Primary View data rules.

Edits to key person identity fields accepted for the update to the Primary View are broadcasted out to all systems of interest that subscribe to updates for that person that do not already have the updated data. Data that does not meet or exceed the current score and pass the data rules will not be updated in the primary view.  If this field is a synchronized field, the primary view will be sent to that system attempting to make the update to reject the data and changing it to the current primary view.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                              |     |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| ![](mpi-pd-version-1-vista-programmer-manual/014.png) | NOTE: The term "systems of interest" refers to VA facilities that have seen persons and entered them as entries onto the MVI. This also refers to non-VistA systems that have a registered interest in a person (e.g., Federal Health Information Exchange \[FHIE\], HomeTeleHealth, Person Service Identity Management \[PSIM\], Health Data Repository \[HDR\], etc.). |     |
| ![](mpi-pd-version-1-vista-programmer-manual/015.png) | REF: For a list of the patient identity fields that make up the Primary View on the MVI, see the section’s titled "Primary View Auto-Updates Person Identity Fields in the VistA Patient File (#2)" and "Primary View Identity Traits" in this document.                                                                                                                 |     |
| ![](mpi-pd-version-1-vista-programmer-manual/016.png) | NOTE: The MPI VETERAN/CLIENT file (#985) comprises the Primary View and is resident on the Austin MPI.                                                                                                                                                                                                                                                                   |     |

### Primary View Auto-Updates Person Identity Fields in the VistA Patient File (#2)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following fields, stored in the MPI VETERAN/CLIENT file (#985), are auto-updated from the MVI to the VistA PATIENT file (#2) and broadcast by the MVI to systems of interest:

- Name
- Social Security Number
- Date of Birth
- Gender
- Mother's Maiden Name
- Multiple birth indicator (Sent and updated to Primary View as of Patch RG\*1\*45. Added to the list of fields auto-updated \[synchronized\] in VistA as of Patch RG\*1\*47.)
- SSN Verification Status (Verified, Invalid Per SSA, and null) (Added to File \#985 as of Patch MPI\*1\*40. Populated to the Primary View of the MVI and systems of interest to the MVI as of DG\*5.3\*688 \[EVC R2\].)
- Pseudo SSN Reason (Added to File \#985 as of Patch MPI\*1\*40. Populated to the Primary View of the MVI and systems of interest to the MVI as of RG\*1\*47 and DG\*5.3\*653 \[EVC R1\].)
- Alias (As of Patch DG\*5.3\*756, the ALIAS \[#1\] multiple in the PATIENT (#2) file is updated in VistA resulting from the edits made to that information on the MVI by the HC IdM team. The VistA data is synchronized to match the MPI values. Additionally, when a facility revises their local ALIAS data, the information is transmitted to the MVI, which in turn updates all treating facilities where the patient is known.)

The concept of the Primary View was introduced with Patch MPI\*1\*40*,* which utilizes central business rules and removes the manual review process (Patient Data Review) from the sites. This allows for faster updates and the ability to have the best data from multiple locations. The site-to-HC IdM communication happens when there is a need for an override of a valid edit that the site had rejected do to the centralized business rules.

Site edits to person identity fields *must* pass the Primary View data rules as well as meet or exceed the current authority score value for that field *before* updating the Primary View on the MVI. If local data fails because the authority score has not weighed in high enough, the edit is rejected.

|                                                                                                                |                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/017.png) | NOTE: The term "auto-update" refers to fields that are updated from a central database (i.e., the Master Veteran Index). |

### Primary View Identity Traits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is the list of fields that are stored in the Primary View of the MPI.

|                                                                                                                |                                                                                    |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/018.png) | NOTE: Not all Primary View fields are synchronized to the systems of interest. |

Table . Primary View Identity Traits stored in the MPI VETERAN/CLIENT file (#985) on the MVI (not a VistA file)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name and Number</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>INTEGRATION CONTROL NUMBER (ICN) (#.01)</td>
<td><p>Based on ASTM E-1714 format is 16 digits, delimiter character, 6 checksum digits.</p>
<p>When the ICN is displayed in the MVI, it appears as 10 digits followed by the delimiter character (“V”) followed by the 6 checksum digits.</p></td>
</tr>
<tr class="even">
<td>SURNAME (#1)</td>
<td>Family name, also known as last name.</td>
</tr>
<tr class="odd">
<td>FIRST NAME (#2)</td>
<td>Person's first given name.</td>
</tr>
<tr class="even">
<td>MIDDLE NAME (#3)</td>
<td>Person's middle name or middle initial.</td>
</tr>
<tr class="odd">
<td>NAME PREFIX (#4)</td>
<td><p>Commonly, Dr., Ms., Sir, or other appropriate titles.</p>
<p>NOTE: Not currently populated on the MPI.</p></td>
</tr>
<tr class="even">
<td>NAME SUFFIX (#5)</td>
<td>Examples are Jr., Sr., PhD, etc.</td>
</tr>
<tr class="odd">
<td>MOTHERS MAIDEN NAME (#6)</td>
<td>Mother’s Surname at her birth.</td>
</tr>
<tr class="even">
<td>DATE OF BIRTH (#7)</td>
<td>Date of person's birth.</td>
</tr>
<tr class="odd">
<td>PLACE OF BIRTH CITY (#8)</td>
<td><p>Name of the city or town (or nearest) where the person was born.</p>
<p>NOTE: Not synchronized to the systems of interest.</p></td>
</tr>
<tr class="even">
<td>PLACE OF BIRTH STATE (#9)</td>
<td><p>If USA, 2 character state abbreviation. If not USA, the country state. Pointer to the STATE file (#5).</p>
<p>NOTE: Not synchronized to the systems of interest.</p></td>
</tr>
<tr class="odd">
<td>PLACE OF BIRTH COUNTRY (#9.1)</td>
<td><p>The PLACE OF BIRTH COUNTRY field identifies the Country that was selected from the available COUNTRY CODE list for where the individual was  born.</p>
<p>NOTE: Not synchronized to the systems of interest.</p></td>
</tr>
<tr class="even">
<td>PLACE OF BIRTH PROVINCE (#9.2)</td>
<td><p>The PLACE OF BIRTH PROVINCE field identifies the location within certain countries containing additional divisions of where the individual was born.</p>
<p>NOTE: Not synchronized to the systems of interest.</p></td>
</tr>
<tr class="odd">
<td>DATE OF DEATH (#10)</td>
<td><p>The date of the person's death.</p>
<p>As of Patch MPI*1*90, Increment 7, Date of Death will be on the Primary View when supplied from one of NCA’s systems, BOSS, or AMAS. Date of Death <em><u>will not</u></em> be synched from PV to the correlations for Increment 8.</p></td>
</tr>
<tr class="even">
<td>DEATH VERIFICATION STATUS (#11)</td>
<td><p>One of four criteria must exist to flag this as Verified:</p>
<ul>
<li><blockquote>
<p>Patient death under VA auspices</p>
</blockquote></li>
<li><blockquote>
<p>DoD casualty report</p>
</blockquote></li>
<li><blockquote>
<p>Receipt of certified death certificate</p>
</blockquote></li>
<li><blockquote>
<p>Burial benefits by NCS</p>
</blockquote></li>
</ul>
<p>NOTE: Not currently populated on the MPI.</p></td>
</tr>
<tr class="odd">
<td>GENDER (#12)</td>
<td><ul>
<li><blockquote>
<p>M = MALE</p>
</blockquote></li>
<li><blockquote>
<p>F = FEMALE</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>SOCIAL SECURITY NUMBER (#13)</td>
<td><p>Patient’s Social Security Number (SSN)</p>
<p>NOTE: Pseudo SSNs aren't stored on the MPI.</p></td>
</tr>
<tr class="odd">
<td><p>SSN VERIFICATION STATUS (#14)</p>
<p>NOTE: Added to File #985 as of Patch MPI*1*40. Populated to the Primary View of the MPI and systems of interest to the MPI as of DG*5.3*688 [EVC R2].</p></td>
<td><p>Status of the verification of a person's SSN. This value is stored on the MVI, derived from an update from the ESR application after interaction with SSA (Social Security Administration). Possible values synchronized to sites are:</p>
<ul>
<li><blockquote>
<p>Null</p>
</blockquote></li>
<li><blockquote>
<p>INVALID PER SSA</p>
</blockquote></li>
<li><blockquote>
<p>VERIFIED</p>
</blockquote></li>
</ul>
<p>Possible values used on the MVI for the ESR correlation are:</p>
<ul>
<li><blockquote>
<p>NEW RECORD</p>
</blockquote></li>
<li><blockquote>
<p>IN-PROCESS</p>
</blockquote></li>
<li><blockquote>
<p>INVALID PER SSA</p>
</blockquote></li>
<li><blockquote>
<p>RESEND TO SSA</p>
</blockquote></li>
<li><blockquote>
<p>VERIFIED</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><p>PSEUDO SSN REASON (#14.1)</p>
<p>NOTE: Added to File #985 as of Patch MPI*1*40. Populated to the Primary View of the MPI and systems of interest to the MPI as of RG*1*47 and DG*5.3*653 [EVC R1].)</p></td>
<td><p>Used to document the reason an individual was assigned a pseudo SSN. Available reasons are:</p>
<ul>
<li><blockquote>
<p>(R) Refused to Provide—Individual was asked for his/her SSN but refused to provide the number.</p>
</blockquote></li>
<li><blockquote>
<p>(S) SSN Unknown/Follow-up required—Individual is not available to ask/answer the request for SSN. The facility should initiate follow-up activity to obtain the SSN.</p>
</blockquote></li>
<li><blockquote>
<p>(N) No SSN Assigned—Individual has not been assigned an SSN. This generally applies to spouse or dependents of veterans who are not US citizens, and infrequently, non-citizen beneficiaries.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>CLAIM NUMBER (#15)</td>
<td>VBA assigned claim number.  Used to assist confirming ID.</td>
</tr>
<tr class="even">
<td>COORDINATING MASTER OF RECORD (#16)</td>
<td>Pre-Primary View Coordinating Site for patient. POINTER TO INSTITUTION file (#4).</td>
</tr>
<tr class="odd">
<td>SENSITIVITY (#17)</td>
<td><p>Sensitivity is used to assist in sensitive management audit reports for unusual activity.</p>
<p>NOTE:  This field is not utilized.</p></td>
</tr>
<tr class="even">
<td>PRIMARY ICN (#18)</td>
<td>As of patch MPI*1.0*40, this field will be used as the value of the Primary ICN for a deactivated ICN. The field will only be populated for an entry that has an ID STATE of deactivated. It is basically telling which ICN should be used instead.</td>
</tr>
<tr class="odd">
<td>DATE/TIME OF ORIGINAL CREATION (#19)</td>
<td>Date/time that the person was added to the MPI VETERAN/CLIENT (#985) file.  This information will be used for reports and analysis by the Healthcare Identity Management (HC IdM) team.</td>
</tr>
<tr class="even">
<td>FACILITY OF ORIGINAL CREATION (#20)</td>
<td>Facility that originally added the person to the MPI VETERAN/CLIENT (#985) file.  This information will be used for reports and analysis by the Healthcare Identity Management (HC IdM) team.</td>
</tr>
<tr class="odd">
<td>CREATED BY (#21)</td>
<td>The CREATED BY field identifies the person at the FACILITY OF ORIGINAL CREATION who added the person to the MPI VETERAN/CLIENT (#985) file. This information will be used for reports and analysis by the Healthcare Identity Management (HC IdM) team.</td>
</tr>
<tr class="even">
<td>RESOLUTION JOURNAL CASE NUMBER (#22)</td>
<td>If a case exists in the MPI DATA MGT RESOLUTION JOURNAL file (#985.2) for this ICN it will be stored in this field regardless of the status of the case.  Resolution Journal cases hold the history of any resolution work done by the Healthcare Identity Management (HC IdM) on this ICN.</td>
</tr>
<tr class="odd">
<td>PRIMARY VIEW DATE LAST UPDATED (#23)</td>
<td>The PRIMARY VIEW DATE LAST UPDATED field is the date/time that any of the person's identity element fields were last updated in the MPI VETERAN/CLIENT (#985) file.</td>
</tr>
<tr class="even">
<td>IDENTITY THEFT (#24)</td>
<td>The IDENTITY THEFT field is used to designate that a specific record has been confirmed by Health Care Identity Management (HC IdM) staff to be involved in an identity theft occurrence. Once it has been marked, the IDENTITY THEFT field will prevent good records from being linked or matched to the identify theft record.</td>
</tr>
<tr class="odd">
<td>TEMPORARY ID NUMBER (#25)</td>
<td>The Department of Defense (DoD) Defense Eligibility Enrollment Reporting System (DEERS) uses a Temporary Identification Number for individuals (e.g., babies) who do not have or have not provided a Social Security Number (SSN) when the record is added to DEERS.  It is used for military dependents only. </td>
</tr>
<tr class="even">
<td>FOREIGN ID NUMBER (#26)</td>
<td>The Department of Defense (DoD) Defense Eligibility Enrollment Reporting System (DEERS) uses a Foreign Identification Number for foreign military and foreign nationals when the record is added to DEERS.</td>
</tr>
<tr class="odd">
<td>SELF IDENTIFIED GENDER field (#27)</td>
<td><p>The value of Self Identified Gender specifies the patient’s self-identified gender identity.</p>
<p>NOTE<strong>:</strong> The PV value will be synched to VHA correlations only. This new field will not be shared to NCA, VBA, DoD or any outside agency/company at this time.</p>
<p>NOTE: As of Patch DG*5.3*902, the menu text display for the field named SELF-IDENTIFIED GENDER was changed to “Self-Identified Gender Identity” in the following MPI/PD options:</p>
<ul>
<li><blockquote>
<p>Patient MPI/PD Data Inquiry</p>
</blockquote></li>
<li><blockquote>
<p>Remote Patient Data Query Menu ...</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>STREET ADDRESS [LINE 1] (#31)</td>
<td><p>First line of person’s residence street address (3-35 characters).</p>
<p>NOTE: Not part of the Primary View originally. As of Patch MPI*1*90, this field will begin being populated from ESR.</p></td>
</tr>
<tr class="odd">
<td>STREET ADDRESS [LINE 2] (32#)</td>
<td><p>Second line of person’s residence street address (3-30 characters) if the space provided in "street address" was not sufficient.</p>
<p>NOTE: Not part of the Primary View originally. As of Patch MPI*1*90, this field will begin being populated from ESR.</p></td>
</tr>
<tr class="even">
<td>STREET ADDRESS [LINE 3] (33#)</td>
<td><p>Third line of person’s residence street address (3-30 characters) if the space provided in "street address" and "street address 2" was not sufficient.</p>
<p>NOTE: Not part of the Primary View originally. As of Patch MPI*1*90, this field will begin being populated from ESR.</p></td>
</tr>
<tr class="odd">
<td>CITY [RESIDENCE] (#34)</td>
<td><p>City in which person resides (3-28 characters).</p>
<p>NOTE: Not part of the Primary View originally. As of Patch MPI*1*90, this field will begin being populated from ESR.</p></td>
</tr>
<tr class="even">
<td>STATE [RESIDENCE] (#35)</td>
<td><p>State in which person resides.</p>
<p>NOTE: Not part of the Primary View originally. As of Patch MPI*1*90, this field will begin being populated from ESR.</p></td>
</tr>
<tr class="odd">
<td>ZIP+4 [RESIDENCE] (#36)</td>
<td><p>Five or Nine digit Zip Code.</p>
<p>NOTE: Not part of the Primary View originally. As of Patch MPI*1*90, this field will begin being populated from ESR.</p></td>
</tr>
<tr class="even">
<td>EMAIL ADDRESS (#36.1)</td>
<td>The Email Address (3-50 characters) for receiving electronic correspondence on.</td>
</tr>
<tr class="odd">
<td>PHONE NUMBER [RESIDENCE] (#37)</td>
<td><p>Telephone number (4-23 characters) to person’s place of residence.</p>
<p>NOTE: Not part of the Primary View originally. As of Patch MPI*1*90, this field will begin being populated from ESR.</p></td>
</tr>
<tr class="even">
<td><p>MULTIPLE BIRTH INDICATOR (#39)</p>
<p>NOTE: Added to the list of fields auto-updated in VistA as of Patch RG*1*47.</p></td>
<td><p>The MULTIPLE BIRTH INDICATOR will designate whether or not the person is part of a multiple birth (i.e. to identify twins, etc.). Possible values are:</p>
<ul>
<li><blockquote>
<p>N = NO</p>
</blockquote></li>
<li><blockquote>
<p>Y = MULTIPLE BIRTH</p>
</blockquote></li>
<li><blockquote>
<p>Null (not the same as No)</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>PROVINCE (#40)</td>
<td><p>Enter a PROVINCE if the patient has provided one for his/her foreign address. The entry can be alphanumeric and up to 20 characters in length.</p>
<p>NOTE: As of Patch MPI*1*90, this field was added to the Primary View and is populated from ESR.</p></td>
</tr>
<tr class="even">
<td>POSTAL CODE (#41)</td>
<td><p>Enter the person’s POSTAL CODE if the patient has provided one for his/her foreign address. The entry can be alphanumeric and up to 10 characters in length.  </p>
<p>NOTE: As of Patch MPI*1*90, this field was added to the Primary View and is populated from ESR.</p></td>
</tr>
<tr class="odd">
<td>COUNTRY (#42)</td>
<td><p>Enter the COUNTRY where the person’s permanent address is located.  If entering an Army/Air Force Post Office (APO) or a Fleet Post Office (FPO) address, select United States as the country.</p>
<p>NOTE: As of Patch MPI*1*90, this field was added to the Primary View and is populated from ESR.</p></td>
</tr>
<tr class="even">
<td>ALIAS (#50)</td>
<td>If this person is known by any name other than that entered in the name field enter that/those other name(s) here. (Multiple field)</td>
</tr>
<tr class="odd">
<td>ALIAS SURNAME (#02,.01)</td>
<td><p>Person’s last name (aka family name). If this patient is known by any name other than that entered in the Name field, enter the other name(s) here.</p>
<p>NOTE: Once in Primary View, will be an aggregated list from all treating facilities.</p></td>
</tr>
<tr class="even">
<td>ALIAS FIRST NAME (#.02,1)</td>
<td><p>Person’s first name.</p>
<p>NOTE: Once in Primary View, will be an aggregated list from all treating facilities.</p></td>
</tr>
<tr class="odd">
<td>ALIAS MIDDLE NAME (#.02,2)</td>
<td><p>Person’s middle name or middle initial.</p>
<p>NOTE: Once in Primary View, will be an aggregated list from all treating facilities.</p></td>
</tr>
<tr class="even">
<td>ALIAS PREFIX (#.02,3)</td>
<td><p>Commonly, Dr., Ms., Sir, or other appropriate titles.</p>
<p>NOTE: Not currently populated on the MVI. Once in Primary View, will be an aggregated list from all treating facilities.</p></td>
</tr>
<tr class="odd">
<td>ALIAS SUFFIX (#.02,4)</td>
<td><p>Examples are Jr., Sr., PhD, etc.</p>
<p>NOTE: Once in Primary View, will be an aggregated list from all treating facilities.</p></td>
</tr>
<tr class="even">
<td>ALIAS SSN (#.02,5)</td>
<td><p>If the person was also known under a name other than that listed in the NAME field of the PATIENT file (#2), enter the social security number used if different when the person used this alias. Include any different SSNs used by person even if names are the same.</p>
<p>NOTE: Alias SSNs that are Pseudo SSNs will not be stored on the MVI. Alias SSN is paired with an Alias Name.  There can't be just an alias SSN. Once in Primary View, will be an aggregated list from all treating facilities.</p></td>
</tr>
<tr class="odd">
<td>ALIAS DATE LAST UPDATED (#.02,6)</td>
<td>The ALIAS DATE LAST UPDATED field is the date/time that the ALIAS field was last updated in the MPI VETERAN/CLIENT (#985) file.</td>
</tr>
<tr class="even">
<td>RACE INFORMATION (#60)</td>
<td><p>Enter the race that best identifies this person.</p>
<p>NOTE: Not synchronized to the systems of interest. Once in Primary View, will be an aggregated list from all treating facilities. (Multiple field)</p>
<p>NOTE: As of Patch MPI*1*91, this field is no longer populated in the Primary View (File #985); however, it continues to be populated in the correlation view (File #985.5).</p></td>
</tr>
<tr class="odd">
<td>RACE INFORMATION (#.03,.01)</td>
<td><p>Enter the races which best identify this patient.</p>
<p>NOTE: As of Patch MPI*1*91, this field is no longer populated in the Primary View (File #985); however, it continues to be populated in the correlation view (File #985.5).</p></td>
</tr>
<tr class="even">
<td>RACE DATE LAST UPDATED (#.03,1)</td>
<td><p>The RACE DATE LAST UPDATED field is the date/time that the RACE field was last updated in the MPI VETERAN/CLIENT (#985) file.</p>
<p>NOTE: As of Patch MPI*1*91, this field is no longer populated in the Primary View (File #985); however, it continues to be populated in the correlation view (File #985.5).</p></td>
</tr>
<tr class="odd">
<td>ETHNICITY INFORMATION (#70)</td>
<td><p>Enter the ethnicity that best identifies this person.</p>
<p>NOTE: Not synchronized to the systems of interest. Once in Primary View, will be an aggregated list from all treating facilities. (Multiple field setup but only one value stored)</p>
<p>NOTE: As of Patch MPI*1*91, this field is no longer populated in the Primary View (File #985); however, it continues to be populated in the correlation view (File #985.5).</p></td>
</tr>
<tr class="even">
<td>ETHNICITY INFORMATION (#.04,.01)</td>
<td><p>Enter the ethnicity which best identifies this person.</p>
<p>NOTE: As of Patch MPI*1*91, this field is no longer populated in the Primary View (File #985); however, it continues to be populated in the correlation view (File #985.5).</p></td>
</tr>
<tr class="odd">
<td>ETHNICITY DATE LAST UPDATED (#.04,1)</td>
<td><p>The ETHNICITY DATE LAST UPDATED field is the date/time that the ETHNICITY field was last updated in the MPI VETERAN/CLIENT (#985) file.</p>
<p>NOTE: As of Patch MPI*1*91, this field is no longer populated in the Primary View (File #985); however, it continues to be populated in the correlation view (File #985.5).</p></td>
</tr>
<tr class="even">
<td>ID STATE (#80)</td>
<td><p>The following ID STATE definitions are from the Object Management Group (OMG) Person Identification Service (PIDS) Specification. ID STATE designates the status of the entry in the MPI VETERAN/CLIENT (#985) file in accordance with business rules and standards. Values for the patient are:</p>
<ul>
<li><p>P = Permanent</p></li>
<li><p>T = Temporary</p></li>
<li><p>D = Deactivated</p></li>
</ul>
<p>PERMANENT: This ID State specifies that all required fields are entered and a national ICN is established. When an ID is created as permanent all mandatory traits <em>must</em> be provided. A permanent ID can be deactivated but <em>cannot</em> be made temporary except for when HC IdM uses the OVR function.</p>
<p>TEMPORARY: This ID State specifies that there are not enough fields to make an entry permanent (as defined further in the business rules). An ID can be created as temporary without indicating any mandatory traits. A common usage is to create an ID that data can be bound to a patient before that patient is identified with an appropriate confidence. A temporary ID can be made permanent or deactivated.</p>
<p>DEACTIVATED: This ID State specifies that the ICN is no longer used. Once an ID is expected not to be needed any more it can be deactivated (merged or deprecated), which keeps it around for historical purposes. A deactivated ID is in its final state and <em>cannot</em> be transitioned to any other state by PIDS operations.</p>
<p>NOTE: Not synchronized to the systems of interest.</p></td>
</tr>
<tr class="odd">
<td>DATE OF ID STATE (#81)</td>
<td>The DATE OF ID STATE field identifies when the ID STATE field was last updated.</td>
</tr>
<tr class="even">
<td>SURNAME PRIMARY VIEW SCORE (#85)</td>
<td>The SURNAME PRIMARY VIEW SCORE field contains the Primary View Authority Score for the SURNAME (#1) identity element.</td>
</tr>
<tr class="odd">
<td>FIRST NAME PRIMARY VIEW SCORE (#86)</td>
<td>The FIRST NAME PRIMARY VIEW SCORE field contains the Primary View Authority Score for the FIRST NAME (#2) identity element.</td>
</tr>
<tr class="even">
<td>MIDDLE NAME PRIMARY VIEW SCORE (#87)</td>
<td>The MIDDLE NAME PRIMARY VIEW SCORE field contains the Primary View Authority Score for the MIDDLE NAME (#3) identity element.</td>
</tr>
<tr class="odd">
<td>PREFIX PRIMARY VIEW SCORE (#88)</td>
<td>The PREFIX PRIMARY VIEW SCORE field contains the Primary View Authority Score for the NAME PREFIX (#4) identity element. Not currently populated on the MVI.</td>
</tr>
<tr class="even">
<td>SUFFIX PRIMARY VIEW SCORE (#89)</td>
<td>The SUFFIX PRIMARY VIEW SCORE field contains the Primary View Authority Score for the NAME SUFFIX (#5) identity element</td>
</tr>
<tr class="odd">
<td>DOB PRIMARY VIEW SCORE (#90)</td>
<td>The DOB PRIMARY VIEW SCORE field contains the Primary View Authority Score for the DATE OF BIRTH (#7) identity element.</td>
</tr>
<tr class="even">
<td>GENDER PRIMARY VIEW SCORE (#91)</td>
<td>The GENDER PRIMARY VIEW SCORE field contains the Primary View Authority Score for the GENDER (#12) identity element.</td>
</tr>
<tr class="odd">
<td>SSN PRIMARY VIEW SCORE (#92)</td>
<td>The SSN PRIMARY VIEW SCORE field contains the Primary View Authority Score for the SOCIAL SECURITY NUMBER (#13) identity element.</td>
</tr>
<tr class="even">
<td>MMN PRIMARY VIEW SCORE (#95)</td>
<td>The MMN PRIMARY VIEW SCORE field contains the Primary View Authority Score for the MOTHER'S MAIDEN NAME (#6) identity element.</td>
</tr>
<tr class="odd">
<td>MULT BIRTH PRIMARY VIEW SCORE (#96)</td>
<td>The MULT BIRTH PRIMARY VIEW SCORE field contains the Primary View Authority Score for the MULTIPLE BIRTH INDICATOR (#39) identity element.</td>
</tr>
<tr class="even">
<td>POB CITY PRIMARY VIEW SCORE (#97)</td>
<td>The POB CITY PRIMARY VIEW SCORE field contains the Primary View Authority Score for the PLACE OF BIRTH CITY (#8) identity element.</td>
</tr>
<tr class="odd">
<td>POB STATE PRIMARY VIEW SCORE (#98)</td>
<td>The POB STATE PRIMARY VIEW SCORE field contains the Primary View Authority Score for the PLACE OF BIRTH STATE (#9) identity element.</td>
</tr>
<tr class="even">
<td>IDENTITY THEFT ACTIVATION (#102)</td>
<td>The IDENTITY THEFT ACTIVATION field is used to determine when a specific record has been confirmed by the Health Care Identity Management (HC IdM) staff to have been involved in an identity theft occurrence.</td>
</tr>
<tr class="odd">
<td>IDENTITY THEFT DEACTIVATION (#103)</td>
<td>The IDENTITY THEFT DEACTIVATION field is used to determine when a specific record has been removed/cleared by the Health Care Identity Management (HC IdM) staff as having been involved in an identity theft occurrence.</td>
</tr>
<tr class="even">
<td>DEATH ENTERED BY (#104)</td>
<td><p>Name of the individual who entered the DATE OF DEATH.</p>
<p>DEATH ENTERED BY is identified and populated at the VAMC level and updated on the Master Patient Index (MPI). This information will be used for reports and analysis by the Healthcare Identity Management (HC IdM) team.</p></td>
</tr>
<tr class="odd">
<td>SOURCE OF NOTIFICATION (#105)</td>
<td><p>Specifies who first notified the VA of the patient’s death.</p>
<p>SOURCE OF NOTIFICATION is identified and populated at the VAMC level and updated on the Master Patient Index (MPI). This information will be used for reports and analysis by the Healthcare Identity Management (HC IdM) team.</p></td>
</tr>
<tr class="even">
<td>DATE OF DEATH LAST UPDATED (#106)</td>
<td><p>Date/Time the DATE OF DEATH was last updated for the patient.</p>
<p>DATE OF DEATH LAST UPDATED is identified and populated at the VAMC level and updated on the Master Patient Index (MPI). This information will be used for reports and analysis by the Healthcare Identity Management (HC IdM) team.</p></td>
</tr>
<tr class="odd">
<td>DEATH LAST EDITED BY (#107)</td>
<td><p>Name of the individual who last edited the DATE OF DEATH.</p>
<p>DEATH LAST EDITED BY is identified and populated at the VAMC level and updated on the Master Patient Index (MPI). This information will be used for reports and analysis by the Healthcare Identity Management (HC IdM) team.</p></td>
</tr>
<tr class="even">
<td>SSA VERIFICATION STATUS (#108)</td>
<td>The SSA VERIFICATION STATUS field identifies the current state of the record.</td>
</tr>
<tr class="odd">
<td>ID INTEROPERABLTY PERSON TYPE (#109)</td>
<td>The ID INTEROPERABLTY PERSON TYPE field identifies the current interoperability person type of the record.</td>
</tr>
<tr class="even">
<td>LEVEL OF ASSURANCE (#110)</td>
<td><p>The LEVEL OF ASSURANCE field identifies the confidence level of the record as determined by the MyHealtheVet (MHV) application.</p>
<p>The LEVEL OF ASSURANCE values refer to the four identity authentication assurance levels for E-Government transactions, described in “E-Authentication Guidance for Federal Agencies” [OMB 04-04]. The four assurance levels are:</p>
<ul>
<li><p>Level1 : Little or no confidence in the asserted identity’s validity.</p></li>
<li><p>Level2 : Some confidence in the asserted identity’s validity.</p></li>
<li><p>Level3 : High confidence in the asserted identity’s validity.</p></li>
<li><p>Level4 : Very high confidence in the asserted identity’s validity.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>DEATH INDICATOR (Y/N)? (#111)</td>
<td><p>The DEATH INDICATOR (Y/N)? field identifies whether or not an individual has been identified as deceased.</p>
<p>Note: Initially this field will only be identified and populated by site 200IVT (Identity Verify Tool), which correlates to the ‘Experian’ integration work.</p></td>
</tr>
<tr class="even">
<td>NOTIFICATION PROVIDER (#113)</td>
<td>The NOTIFICATION PROVIDER field identifies the current Line of Business (LOB) system that correlated a patient’s date of death.</td>
</tr>
<tr class="odd">
<td>SUPPORTING DOCUMENT TYPE (#114)</td>
<td>The SUPPORTING DOCUMENT TYPE field identifies the current document used to inform of a patient’s date of death from the Line of Business (LOB) system.</td>
</tr>
<tr class="even">
<td>DATE OF DEATH OPTION USED (#115)</td>
<td><p>The DATE OF DEATH OPTION USED field specifies the option used on the Line of Business (LOB) system when editing (adding/updating) a patient’s date of death. Option values include the following:</p>
<ul>
<li><p>JRN_OBJ</p></li>
<li><p>JRN_APP</p></li>
<li><p>JRN_STN</p></li>
<li><p>DEATH ENTRY</p></li>
<li><p>DISCHARGE A PATIENT</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>DISCHARGED DATE/TIME (#116)</td>
<td><p>The DISCHARGED DATE/TIME field identifies the date (time is optional) when a patient was last discharged from the Veteran Affairs Medical Center (VAMC).</p>
<p>DISCHARGED DATE/TIME is identified and populated at the VAMC level and updated on the Master Veteran Index (MVI).</p></td>
</tr>
<tr class="even">
<td>DATE OF DEATH OVERRIDE REASON (#117)</td>
<td><p>The DATE OF DEATH OVERRIDE REASON field specifies the reason for making a change to the date of death on a patient’s record. Reason values included the following:</p>
<ul>
<li><p>DECEASED WHILE INPATIENT</p></li>
<li><p>DEATH CERTIFICATE</p></li>
<li><p>NCA</p></li>
<li><p>VERIFIED VIA BIRLS</p></li>
<li><p>VERIFIED VIA SSA</p></li>
<li><p>DATE OF DEATH CORRECTION</p></li>
<li><p>ENTERED IN ERROR</p></li>
<li><p>IDENTITY THEFT</p></li>
</ul>
<p>NOTE: Not synchronized to the systems of interest.</p></td>
</tr>
<tr class="odd">
<td>DEATH STATUS (#118)</td>
<td><p>The DEATH STATUS field specifies whether the DATE OF DEATH (#20) value in the correlation [MPI FACILITY ASSOCIATION file #985.5] has successfully passed all of the Primary View (PV business rules to get promoted into PV. Status values include the following:</p>
<ul>
<li><p>PENDING</p></li>
<li><p>VERIFIED</p></li>
</ul></td>
</tr>
<tr class="even">
<td>PERSON TYPE (#150)</td>
<td>The person types that this person is identified by. (Multiple field)</td>
</tr>
<tr class="odd">
<td>PERSON TYPE<br />
(#.054, .01)</td>
<td>The Person Type(s) selected from the available list [MPI PERSON TYPES FILE #985.72] that identifies the current person type(s) of the record.</td>
</tr>
<tr class="even">
<td>PREFERRED NAME (#300)</td>
<td>Specifies the name on how the patient would prefer to be referenced by during interactions at the medical facility.</td>
</tr>
</tbody>
</table>

  
Enhanced MPI-to-VistA Synchronization—Additional Patient Identity FieldsSSN Verification Status Synchronized to Systems of Interest

The SSN Verification Status is populated on the MVI and broadcast to treating facilities and systems of interest. The field values VERIFIED and INVALID PER SSA are triggered as a result of an update from the ESR application and subsequent update to the Primary View.

The SSN Verification Status is an existing field on the MVI with the current values listed below. In order to bring these values in line with the Enrollment VistA Changes (EVC) requirements and Standard Data Services (SDS) tables as well as support the later migration of data into the Administrative Data Repository (ADR), a change is needed to the internal and external value on the MVI. The current values are listed below; however, only the values of Null, Verified and Invalid Per SSA are synchronized with the sites.

- Null
- New Record
- In-Process
- Invalid Per SSA
- Resend to SSA
- Verified

SSN and Pseudo SSN Reason Synchronized to Systems of Interest

When a VistA instance or Enrollment System Redesign (ESR) updates the Pseudo SSN Reason, the MVI updates the MPI FACILITY ASSOCIATION file (#985.5). If the VistA instance is the Primary View, that value is updated in File \#985 and broadcasted out to all sites.

Multiple Birth Indicator Synchronized to Systems of Interest

As of Patch RG\*1\*45, the MULTIPLE BIRTH INDICATOR field is sent and stored on the MVI; however, it is not synchronized to all of the "systems of interest" (i.e., Treating Facilities). As of Patch RG\*1\*47, the MULTIPLE BIRTH INDICATOR is included in the list of patient identity fields that are synchronized from the MPI out to all systems of interest.

If synchronization of the MULTIPLE BIRTH INDICATOR field fails, an exception is logged on the MVI. This functionality is in support of the Patient Safety Office's effort to reduce the number of local duplicate record merges on records that are related to patients with similar trait values to their siblings.

|                                                                                                                |                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/019.png) | NOTE: The Duplicate Record Merge: Patient Merge software has already been modified to display the MULTIPLE BIRTH INDICATOR field value if present. |

The ALIAS Multiple Stored on MVI and Synchronized to VistA

In the Primary View of the MVI, the ALIAS multiple (#50) is stored in the MPI VETERAN/CLIENT file (#985) as an aggregated list from all the treating facilities associated with that ICN. In VistA, the ALIAS multiple (#1) is stored in the PATIENT file (#2). All edits made by Healthcare Identity Management (HC IdM) staff to the ALIAS multiple on the MVI via the Edit PV Alias Values \[MPI DATA MGT EDIT PV ALIAS\] option are updated in the Primary View on the MVI and synchronized out to all systems of interest (e.g., VistA treating facilities) for that patient. Site edits to the ALIAS multiple (#1) in the VistA PATIENT file (#2) are updated in VistA and sent to the MVI for updates to the Primary View. The updates are then synchronized back out to all other treating facilities (systems of interest) associated with that ICN.

Process Sequence for Inbound Edits

In the process for updating the Primary View of the MVI, the first check is for potential catastrophic edits to person identity, which is defined as an edit to two or more of the following identity traits:

- Name (First, Last)
- Date Of Birth
- Social Security Number (SSN)
- Gender

If the potential catastrophic edit affects two or more identity traits, an exception is generated that becomes a manual HC IdM catastrophic edit review process. HC IdM processes potential catastrophic edits as follows:

- Accept All
- Reject All
- Partial Accept

If there are no catastrophic edits:

- All fields in Primary View are compared to the inbound data sent for that correlation.
- If there are differences, a series of computations begin to "score" the data to determine if it meets the criteria for acceptance. The Primary View score is based on data captured from a patient encounter with a Veterans Affairs facility (e.g., active prescriptions, admission or registration in the last year, lab test, or radiology exam in the last year).
- The score is then calculated from the data update coming from the site.
- Each field is then evaluated against any fields that are different in the current Primary View to see if the score is equal to or greater than the existing Primary View field's score and that the data update meets the business rules for data validity and integrity.
- Any of the fields, all of the fields, or none of the fields may be updated based upon the scoring and the business rules.

|                                                                                                                |                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/020.png) | NOTE: The MPI FACILITY ASSOCIATION file (#985.5) contains the sites' last update. This correlation should be a duplicate of the same data in the PATIENT file (#2) at the sites. |

Primary View Reject

When person identity fields are edited at VA facilities and sent to the MVI, those edits *must* meet or exceed the existing authority score and pass the Primary View Data Rules on a field-by-field basis. If an edit fails to pass both of these tests, the edit to that person identity field is rejected.

If a site determines that the rejected data is a legitimate edit, the only way to get that data updated on the MVI is to contact the Healthcare Identity Management (HC IdM) team and have them make the edit. HC IdM has the ability to overwrite Primary View data.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-programmer-manual/021.png)</td>
<td><p><strong>NOTE:</strong> Healthcare Identity Management (HC IdM) has requested the removal/deletion of Primary View Rejects (PVRs) and PVR functionality. As of Patch RG*1.0*62:</p>
<ul>
<li><p>Exception #234 (Primary View Reject) were no longer be logged.</p></li>
<li><p>A post-init process executed and marked all existing unresolved 234 exceptions as Resolved.</p></li>
<li><p>The menu option MPI/PD Exception Handling [RG EXCEPTION HANDLING] was removed, since it is no longer needed.</p></li>
</ul></td>
</tr>
</tbody>
</table>

HC IdM View/Edit Authority Values for Business Rules Criterion

Healthcare Identity Management (HC IdM) staff can view or edit the current authority values for the Primary View business rules criterion. These authority values weigh and score inbound edits to the person entries on the MVI based on person activity at the site.

# MPI/PD Frequently Asked Questions (FAQ)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## What is the Master Patient Index (MPI)?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Master Patient Index (MPI) is located at the Austin Information Technology Center (AITC). It is composed of a unique list of persons and an associated list of VAMCs (Veterans Affairs Medical Centers) and other systems of interest where each person has been seen. This enables the sharing of person data between operationally diverse systems. Each person record (or index entry) on the MVI contains multiple demographic fields which are updated to the Primary View.

The Master Patient Index/Patient Demographics (MPI/PD) software resides in VistA enabling sites to:

- Request an ICN assignment.
- Resolve a potential duplicate on the MPI.
- Review and process exceptions received from MPI including Primary View Reject exceptions.
- Query the MPI (Austin) for known data.
- Update the MPI when changes occur to demographic fields stored on the MPI or of interest to other facilities/systems of interest.

|                                                                                                                |                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/022.png) | REF: For more information see the section titled: "Product Description―" in this manual.                                                                                                                                                                                                   |
| ![](mpi-pd-version-1-vista-programmer-manual/023.png) | NOTE: The MPI/PD software (i.e., routines in the MPIF\* and RG\* namespace) SHOULD NOT reside/run on Legacy systems. Any VistA applications utilizing APIs in the MPIF and RG namespace on Legacy systems should check for the existence of these routine(s) before trying to access them. |

## How do I Get Primary View Data?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To get Primary View data, use the menu options on the Message Exception Menu, located on the MPI/PD Patient Admin Coordinator Menu.

Select MPI/PD Patient Admin Coordinator Menu Option: Message Exception Menu

          Patient MPI/PD Data Inquiry

          Remote Patient Data Query Menu...

          Display Only Query

          Primary View Display from MPI

Select Message Exception Menu Option:

|                                                                                                                |                                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/024.png) | REF: For more information on using the MPI/PD Message Exception Menu options to get Primary View data for a person, see the *Master Patient Index/Patient Demographics (MPI/PD) v1.0 User Manual*, section titled: *“Message Exception Menu,”* in the chapter titled: *“MPI/PD Menus and Options.”* |

## How do I Get Correlation Data?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To get correlation data for a person, use the menu options on the Message Exception Menu, located on the MPI/PD Patient Admin Coordinator Menu.

Select MPI/PD Patient Admin Coordinator Menu Option: Message Exception Menu

          Patient MPI/PD Data Inquiry

          Remote Patient Data Query Menu...

          Display Only Query

          Primary View Display from MPI

Select Message Exception Menu Option:

|                                                                                                                |                                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/025.png) | REF: For more information on using the MPI/PD Message Exception Menu options to get Primary View data for a person, see the *Master Patient Index/Patient Demographics (MPI/PD) v1.0 User Manual*, section titled: *“Message Exception Menu,”* in the chapter titled: *“MPI/PD Menus and Options.”* |

## Is the MPI the Authoritative Source for this Information?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MPI is the authoritative source for the ICN and the following five identity fields:

- Name (all components),
- SSN,
- Date of Birth,
- Gender,
- Mother's Maiden Name,

and the correlated domains (treating facilities/systems of interest) that know that ICN.

## What is an Integration Control Number (ICN)?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Integration Control Number (ICN) follows the ASTM e1714-95 standard for a universal health identifier. This standard describes the identifier as 29 characters (i.e., 16-digit sequence + 'V' delimiter + 6-digit checksum + 6-digit encryption). The short version of the ICN/VPID can be 17 characters (i.e., 10-digit sequence + 'V' delimiter + 6-digit checksum), with the leading zeros of the sequence and trailing zeros encryption trimmed off.

An Integration Control Number (ICN) is a unique identifier assigned to each patient entry in the Master Patient Index linking patients to their records across VA systems

ICNs fall under two categories: national and local. Both are described as follows:

National ICNs

During the initialization of the MPI database in Austin, each VA Medical Center sent batch HL7 messages to the MPI (Austin) requesting ICNs for all of its patients whose records reflected activity in the past three fiscal years (i.e., active patient records).

In day-to-day operations, patients are presented to the MPI via:

- PIMS options:
  - Load/Edit Patient Data \[DG LOAD PATIENT DATA\]
  - Register a Patient \[DG REGISTER PATIENT\]
  - Electronic 10-10EZ Processing \[EAS EZ 1010EZ PROCESSING\]
- Local/Missing ICN Resolution \[MPIF LOC/MIS ICN RES\] background job

When a new patent record is created via the PIMS options, a real-time connection is established to the MPI requesting an ICN assignment. If communication cannot be established or is lost with the MPI before the ICN assignment process has completed, a local ICN is assigned. Otherwise, a national ICN is assigned to the patient. The MPI uses patient traits to determine whether this patient is already known to the MPI and thus already has an ICN, or whether this is a new patient which causes a new ICN to be created. The ICN, ICN checksum, CMOR, and list of facilities, including other systems of interest (e.g., FHIE and HDR), are updated in the site's VistA system.

If an existing patient record is edited via the PIMS options, and if this patient does not have an ICN (national or local), the same process occurs as was illustrated for a newly created patient.

If a patient record is edited or created outside of the PIMS options, they are presented to the MPI for ICN assignment via the Local/Missing ICN Resolution background job.

If an exact match is not found the MPI returns a message indicating this and that the patient is being added to the MPI. If potential matches are found, a new ICN is assigned to the patient, but an exception is logged for the Health Care Identify Management (HC IdM) group to review and provide the appropriate action.  If the patients are truly the same person then the records will be linked together with one ICN becoming the primary ICN that all records will be linked under and the other will be deactivated.  The sites that had the deactivated ICN will be updated to the primary ICN.

Local ICNs

ICNs are created for new patients locally at the site when the MPI is unavailable or when the connection is lost prior to the assignment an ICN (e.g., the Direct Connect could not be established). A local ICN is also assigned as a placeholder when a patient has been sent to be added to the MPI. This is to ensure identification of these patients as these records await a response from the MPI. Local ICNs look like a national ICN. They contain the same number of digits as a national ICN. The only difference is that the first three digits are the VAMCs station number.

|                                                                                                                |                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/026.png) | NOTE: It is not recommended that Local ICNs be sent to remote databases as they will only be known at the local facility that assigned them. |

A background job named Local/Missing ICN Resolution will find all patients in the local PATIENT file (#2) with either a Local ICN or that have been flagged as missing an ICN and send these patients to the MPI for a national ICN assignment.

Missing ICNs

Missing ICNs result from patient records which have been added to the PATIENT file (#2) via other means than through the PIMS options that establish the real-time connection with the MPI (Load/Edit Patient Data, Register a Patient, and Electronic 10-10EZ Processing). These records are flagged internally for inclusion in the Local/Missing ICN Resolution job.

## What Does an ICN Look Like?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ICN follows the ASTM e1714-95 standard for a universal health identifier. This standard describes the identifier as 29 characters (i.e., 16-digit sequence + 'V' delimiter + 6-digit checksum + 6-digit encryption). For example:

> 0000001000720100V271387000000

The short version of the ICN/VPID can be 17 characters (i.e., 10-digit sequence + 'V' delimiter + 6-digit checksum), with the leading zeros of the sequence and trailing zeros encryption trimmed off. For example:

> 1000720100V271387

## How Does a Patient Get an ICN?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In day-to-day operations, a patient record can get an ICN assignment by one of the following ways:

1.  Through a real-time TCP/IP connection (i.e. Direct Connect) via one of the following PIMS options:
- Load/Edit Patient Data \[DG LOAD PATIENT DATA\]
- Register a Patient \[DG REGISTER PATIENT\]
- Electronic 10-10EZ Processing \[EAS EZ 1010EZ PROCESSING\]

When a new patent record is created via the PIMS options, a real-time connection is established to the MPI requesting an ICN assignment. If communication cannot be established or is lost with the MPI before the ICN assignment process has completed, a local ICN is assigned. Otherwise, a national ICN is assigned to the patient. The ICN can either be newly created or already on the MPI for that patient. The ICN, ICN checksum, and list of facilities, including other systems of interest (e.g., FHIE and HDR), are updated in the site's VistA system.

2.  If an existing patient record is edited via the PIMS options, and if this patient does not have an ICN (national or local), the same process occurs as was illustrated for a newly created patient.
3.  If a patient record is edited or created outside of the PIMS options, they are presented to the MPI for ICN assignment via the Local/Missing ICN Resolution background job.
4.  If an exact match is not found the MPI returns a message indicating this and that the patient is being added to the MPI. If potential matches are found, a new ICN is assigned to the patient, and an exception is logged for the Health Care Identify Management (HC IdM) group to review and provide the appropriate action.  If the patients are truly the same person, then the records will be linked together with one ICN becoming the primary ICN that all records will be linked under and the other will be deactivated.  The sites that had the deactivated ICN will be updated to the primary ICN.

## Where is the ICN Stored?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Besides being stored on the MPI, the ICN is also stored in the following fields in the PATIENT file (#2) in VistA:

- INTEGRATION CONTROL NUMBER, field (#991.01).
- ICN CHECKSUM, field (#991.02).
- FULL ICN, field (#991.1), which contains both the identifier and checksum values.

|                                                                                                                |                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/027.png) | NOTE: The FULL ICN field will eventually replace Fields \#991.01 and \#991.02. The FULL ICN HISTORY multiple (#2.0991) mirrors the existing ICN HISTORY multiple (#2.0992), except contains the single full ICN value. |

All three of these fields, above, are stored on the "MPI" node, ^DPT(DFN,"MPI").

FULL ICN HISTORY multiple (Field \#2.0991): ICNs found in the FULL ICN HISTORY multiple are ones that have previously been assigned to the patient, but are not the current ICN. Stored in the FULL ICN History multiple is the following field: FULL ICN HISTORY (#.01).

The FULL ICN HISTORY multiple is stored in ^DPT(\<DFN\>,”MPIFICNHIS”,\<IEN\>,0).

ICN HISTORY multiple (#2.0992): ICNs found in the ICN HISTORY multiple are ones that have previously been assigned to the patient, but are not the current ICN. Stored in the ICN HISTORY multiple are the following fields: ICN (#.01), ICN CHECKSUM (#1), CMOR (#2) and DATE/TIME OF CHANGE (#3).

The ICN HISTORY multiple (#2.0992) is stored in ^DPT(\<DFN\>,"MPIFHIS",\<IEN\>,0).

|                                                                                                                   |                                                                        |
|-------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/028.png) | CAUTION: Direct access to ICNs in the PATIENT file is not allowed. |

## What is a Local ICN?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Local ICN is created by a local VistA system, and not the MPI. A Local ICN is assigned when: 

- the site edits an existing patient or adds a new patient using an option that doesn't directly interact with the MPI (e.g., VistA Lab or VA FileMan).
- communication can't be established or is lost with the MPI before the ICN assignment process has completed, a local ICN is assigned.

Each facility is currently responsible for appropriately resolving their local exceptions on a daily basis. These requirements are stated in [VHA DIRECTIVE 1906](http://vaww1.va.gov/vhapublications/ViewPublication.asp?pub_ID=2880) (NOTE: This is an internal VA Web site and is not available to the public.).

All Local ICNs created in a given day are sent up to the MPI via the LOCAL/MISSING ICN RESOLUTION JOB that runs every 600 seconds. The result of this job will be a national ICN.

## Under What Conditions are Local ICNs Assigned to Patient Records?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are conditions in which local ICNs are assigned to patient records:

- The site's VistA system can't connect to the MPI.
- The site edits an existing patient or adds a new patient using an option that doesn't directly interact with the MPI (e.g., VistA Lab or VA FileMan).
- The site attempts to add a patient; however, something happens to hold up transmission to the MPI causing a delay in national ICN assignment. In this instance, a local ICN is assigned as an interim placeholder to the patient entry until a national ICN is returned. Local ICN assignments made in this situation facilitate these types of patient entries to be easily identifiable.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-programmer-manual/029.png)</td>
<td><p><strong>NOTE: Local ICN Assignment as Placeholders</strong></p>
<p>When a patient is sent to the MPI, a local ICN is assigned as placeholder to that entry until a national ICN is returned. In addition, if the patient sent to the MPI is an existing patient that doesn't have a national ICN assignment, and if that record has been edited outside the PIMS options that interact directly with the MPI, when the UPDATE BATCH JOB FOR HL7 v2.3 [VAFC BATCH UPDATE] job runs it will create a local ICN for that patient. This ensures that patient records of this nature are sent to the MPI for national ICN assignment when the Local/Missing ICN Resolution background job [MPIF LOC/MIS ICN RES] is run at the site.</p></td>
</tr>
<tr class="even">
<td>![](mpi-pd-version-1-vista-programmer-manual/030.png)</td>
<td><strong>NOTE:</strong> When Local ICNs are assigned to patient records, they continue to be resolved through the Local/Missing ICN Resolution Background Job [MPIF LOC/MIS ICN RES].</td>
</tr>
</tbody>
</table>

## How Can I Retrieve a Patient's ICN as a VistA Developer/Application?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/031.png) | NOTE: The ICN follows the ASTM e1714-95 standard for a universal health identifier. The standard describes the identifier to be 29 characters (i.e., 16-digit sequence + 'V' delimiter + 6-digit checksum + 6-digit encryption). The short version of the ICN/VPID may be 17 characters (i.e., 10-digit sequence + 'V' delimiter + 6-digit checksum), with the leading zeros of the sequence and trailing zeros encryption trimmed off. |

The API \$\$GETICN^MPIF001(DFN) will return a complete ICN. This function call is passed the IEN for the patient in the PATIENT file (#2). Returned is a -1^error message or the ICN. For example:

> Function call: S ICN=\$\$GETICN^MPIF001(3404040)  
> Returned value: 1000720100V271387

|                                                                                                                |                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/032.png) | NOTE: This API returns the active ICN for the patient. If there was an ICN assigned, which is no longer active, no ICN will be returned. |

Use the API \$\$GETDFN^MPIF001(ICN) if you have the ICN and need to find the patient's entry in the PATIENT file (#2). This function call is passed the ICN of the patient you are looking for in the PATIENT file (#2). You can pass the ICN either with or without the checksum and “V”. Returned is a –1^error message or the IEN for the patient in this site's PATIENT file (#2).

> Function call: S DFN=\$\$GETDFN^MPIF001("1000720100V271387")  
> Returned value: 3404040

## What Causes a Patient Record Not to Have a National ICN Assignment?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- If the patient record was not included as part of the initial seeding process to the MPI. When the MPI was first initialized, patient records showing no activity in the last three fiscal years prior to the initialization were not enumerated with an ICN.
- If the patient record has not been edited or has not had clinical activity since approximately 1989, it would not have been sent up to the MPI for an ICN and CMOR assignment during the initial seeding of the index.
- If the patient record has not been processed into the system via any of the following PIMS options: Load/Edit, Register a Patient, or Electronic 10-10EZ Processing since the initial seeding of the index.
- Prior to this patch MPIF\*1\*33, the following criteria were not sent to the Master Patient Index (MPI) for national ICN assignment:
- Patient records with last names beginning with ZZ
- Patient records that have 5 leading zeros for the Social Security Number (SSN)
- Patients records with last names beginning with "EEE"
- Patients records with last names beginning with the word "Merging" (This applies to patients in the process of being merged via the Duplicate Record Merge software.)

> Patient records having met these criteria were either prevented from being sent to the MPI or were removed. Thus, these records currently exist in sites’ PATIENT file (#2) without a national ICN assignment.

- If the patient record had been merged with another.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/033.png) | NOTE: VistA Patch MPIF\*1\*33 removed the Inactivate Patient from MPI \[MPIF PAT INACT\] option from the Master Patient Index Menu \[MPIF VISTA MENU\]. This option allowed users to inactivate patient records for any reason as long as they were not shared by another VistA system. Patient records having no activity since inactivation do not have national ICN assignments. |                                                                                                                                                                                                                                                                                                                                                |
| ![](mpi-pd-version-1-vista-programmer-manual/034.png) |                                                                                                                                                                                                                                                                                                                                                                                         | NOTE: As of Patch DG\*5.3\*589, the AMPIZZ and ATSSN cross-references have been removed from the PATIENT file (#2). These cross-references were used to automatically inactivate patient entries from the MPI if records were found to be ZZ'd and/or if the first five digits of patient Social Security Numbers were replace with zeros. |

## What Causes a Patient Record to Have Only a Local ICN Assignment?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Answer:

- If communication can't be established or is lost with the MPI before the ICN assignment process has completed.
- If the site edits an existing or adds a new patient using an option that doesn't directly interact with the MPI (e.g., VistA Lab or VA FileMan).
- If the patient is being added to the MPI (via the HL7 ADT-A28 message) as a placeholder until a National ICN is assigned. A local ICN is assigned to prevent processing the patient again on the MPI during that interim period.

## Can a Patient's ICN Change?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Yes. A patient’s ICN can change in any of the following two ways:

1.  An ICN will change when the patient has a local ICN assigned and the patient traits are sent to the MPI for a national ICN assignment. All previously assigned ICNs are stored in the ICN History Multiple in the PATIENT file (#2) . The GETDFN Application Programmer Interface will return the patient given a passed ICN.
2.  When a patient is presented to the MPI and there are potential matches found for that patient, the patient is added to the MPI and assigned a new national ICN. A Potential Matches Returned exception is generated in Person Service Identity Management (PSIM). The HC IdM team will review and resolve Potential Matches Returned exceptions. If HC IdM determines that two potential match patients are the same person, one of the two national ICNs will be selected as the prime ICN, and that ICN will be assigned to both patients. So the old national ICN for one of the patients will be replaced with the prime ICN selected by HC IdM, both on the MPI records, and on the PATIENT record in VistA. This is referred to as “linking” the existing patient to a new ICN.

## How Can I Tell if an ICN has Change?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All VistA systems are subscribers to MPI messaging automatically. You will be notified via the ADT-A24 message of a change in National ICN for a given patient.  If the patient's ICN changed from a local to a national, there isn't a message generated specifically for that change.  If the subscribing system has requested to be notified about a change to a DFN/SITE pair then they would get the ADT-A24 message.  

Please feel free to consult the MPI development team and/or Healthcare Identity Management (HC IdM) if you any further questions.

## Can a Vendor Use an ICN to Identify a Patient?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a vendor application requires an ICN and would like to attempt to get one as part of the processing, a request needs to be sent to the MPI development team for evaluation. The development staff will review the request and if approved, provide the appropriate APIs and code to accomplish this task.

## How Can My VistA Application Get an ICN Assignment for a Patient?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your application requires an ICN and would like to attempt to get one as part of your processing, a request needs to be sent to the development team for evaluation. The development staff will review the request and if approved, provide the appropriate APIs and code to accomplish this task.

## What is the Communication Procedure with the MPI?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the [<u>MPI/PD HL7 Interface Specifications</u>](http://www.va.gov/vdl/application.asp?appid=16) (*NOTE: This is an internal VA Web site and is not available to the public.*) on the Master Patient Index (MPI) section of the VA Software Documentation Library.

## How Do I Ensure Test System Data is Not Sent to the MPI?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*"I remember there was some discussion among the MPI Development Team regarding mirroring the test account and implementing a special process to ensure that test data was not sent to the MPI. Do you know who I could contact about that?"*

The routine is the Test Account Reset Utility, NVSTAR, created by EIE Health Systems Technical Support, distributed via KIDS build, and is platform independent. The software and all the supporting documentation are available at all the CIOFO FTP servers in the test system directory (just below the root). See Error! Reference source not found., for an example of how to use the NVSTAR Test Account Reset Utility.

<span id="_Toc510587528" class="anchor"></span>Figure 1. How to use the NVSTAR Test Account Reset Utility

ES40A2\$ ftp REDACTED *  User Input—Start File Transfer.*

220 ISC4A1.REDACTED FTP Server (Version 5.6) Ready.

Connected to REDACTED.

Name (REDACTED:system): anonymous

331 Guest login OK, send ident as password.

Password: * User Input—Not echoed. Usually just your email address.*

230 Guest login OK, access restrictions apply.

FTP\> pwd  * User Input—Find out where you are.*

257 "ANON\$:\[ANONYMOUS\]" is current directory.

FTP\> cd \[.cache.mirtestacct\]  *User Input—Get to proper target directory.*

250-CWD command successful.

250 New default directory is ANON\$:\[ANONYMOUS.CACHE.MIRTESTACCT\]

FTP\> ls   *User Input—List directory.*

200 PORT command successful.

150 Opening data connection for ANON\$:\[ANONYMOUS.CACHE.MIRTESTACCT\]\*.\*;\* (10.6.21.15,55719)

NVSTAR7.KID;1

NVSTAR7_CACHE_MIRTEST.DOC;1

NVSTAR7_XQ_XU273_CACHE.RSA;1

ZSTU_TEST521.RSA;1

ZSTU_TEST523.RSA;1

226 NLST Directory transfer complete

114 bytes received in 00:00:00.03 seconds (2.85 Kbytes/s)

FTP\> hash   *User Input—Turn on hash marks.*

Hash mark printing on (1024/hash mark).

FTP\> ascii   *User Input—ASCII files being retrieved.*

200 TYPE set to ASCII.

FTP\> mget \*   *User Input—\[mget \* transfers all of the files in this directory into the default directory  
at your site that FTP was started.  You might like to create a directory locally on your  
machine and set that as your default before the transfer.\]*

\#200 TYPE set to IMAGE.

200 PORT command successful.

150 Opening data connection for ANON\$:\[ANONYMOUS.CACHE.MIRTESTACCT\]NVSTAR7.KID;1

 (10.6.21.15,55771) (269695 bytes)

\############################################################################

\############################################################################

\############################################################################

\#######################

226 Transfer complete.

local: SYS\$COMMON:\[SYSMGR\]NVSTAR7.KID;2  remote: NVSTAR7.KID;1

269695 bytes received in 00:00:00.50 seconds (523.69 Kbytes/s)

200 PORT command successful.

150 Opening data connection for ANON\$:\[ANONYMOUS.CACHE.MIRTESTACCT\]NVSTAR7_CACHE

\_MIRTEST.DOC;1 (10.6.21.15,55772) (454656 bytes)

\############################################################################

\############################################################################

\############################################################################

\############################################################################

\############################################################################

\############################################

226 Transfer complete.

local: SYS\$COMMON:\[SYSMGR\]NVSTAR7_CACHE_MIRTEST.DOC;2  remote: NVSTAR7_CACHE_MIR

TEST.DOC;1

454656 bytes received in 00:00:00.72 seconds (614.43 Kbytes/s)

200 PORT command successful.

150 Opening data connection for ANON\$:\[ANONYMOUS.CACHE.MIRTESTACCT\]NVSTAR7_XQ_XU

273_CACHE.RSA;1 (10.6.21.15,55773) (19868 bytes)

\###################

226 Transfer complete.

local: SYS\$COMMON:\[SYSMGR\]NVSTAR7_XQ_XU273_CACHE.RSA;2  remote: NVSTAR7_XQ_XU273

\_CACHE.RSA;1

19868 bytes received in 00:00:00.17 seconds (110.38 Kbytes/s)

200 PORT command successful.

150 Opening data connection for ANON\$:\[ANONYMOUS.CACHE.MIRTESTACCT\]ZSTU_TEST521.

RSA;1 (10.6.21.15,55774) (3765 bytes)

\###

226 Transfer complete.

local: SYS\$COMMON:\[SYSMGR\]ZSTU_TEST521.RSA;2  remote: ZSTU_TEST521.RSA;1

3765 bytes received in 00:00:00.05 seconds (72.41 Kbytes/s)

200 PORT command successful.

150 Opening data connection for ANON\$:\[ANONYMOUS.CACHE.MIRTESTACCT\]ZSTU_TEST523.

RSA;1 (10.6.21.15,55775) (6773 bytes)

\######

226 Transfer complete.

local: SYS\$COMMON:\[SYSMGR\]ZSTU_TEST523.RSA;2  remote: ZSTU_TEST523.RSA;1

6773 bytes received in 00:00:00.11 seconds (57.40 Kbytes/s)

FTP\> exit   *User Input—Everything successfully transferred. So, let's Exit.*

221 Goodbye.

|                                                                                                                |                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/035.png) | NOTE: HL7 cleanup is only one of the rather large lists of cleanup/reset procedures the software does now. |

If you have further questions about, or need help with getting and using the NVSTAR, contact the VA Service Desk at REDACTED or log a Remedy ticket to SystemsVistA/VMSCache/General.

## How Do I Block Automatic Calls to a Patient if Other Treating Facilities Don’t Use the Same Characters?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MUMPS Audio Fax, Figure , allows you to place a site-specified non-numeric character in the phone number to block automatic calls to a patient. This value is overwritten if the patient's treating facilities don't use the same character. Is there another way to block the calls? 

Mumps AudioFax outbound calling applications will look for an identified character in the patient phone number and will also look for an entry in the VEXM APPOINTMENT CALLS EXCLUDED PATIENTS file as a basis for excluding the patient from calls. Use EXCLUDE PATIENT FROM CALLING option on the MAF APPOINTMENT SYSTEM MENU to correct this.

> <span id="_Ref93118821" class="anchor"></span>Figure 2. Exclude Patient From Calling Option Blocks Automatic Calls to a Patient

> Select MAF APPOINTMENT SYSTEM MENU Option: 8\<Enter\> EXCLUDE PATIENT FROM CALLING 

Select PATIENT NAME: DEMONSTRATION

1 MVIPATIENT,ROE 12-24-19 000008888 NO NSC VETERAN

2 MVIPATIENT,GIL 01-01-25 000001333 NO NON-VETERAN (OTHER)

3 MVIPATIENT,DEVIN 07-04-53 000006666 NO NSC VETERAN

4 MVIPATIENT,RYAN 02-14-01 000007777 YES SC VETERAN

5 MVIPATIENT,SAGE 06-06-60 000000606 NO NSC VETERAN

ENTER '^' TO STOP, OR CHOOSE 1-5: 2\<Enter\> MVIPATIENT,GIL 01-01-25 000001333 NO NON-VETERAN (OTHER)

Select PATIENT NAME: DEMONSTRATION*\<\<\<--- Need to enter the name again.*

1 MVIPATIENT,ROE 12-24-19 000008888 NO NSC VETERAN

2 MVIPATIENT,GIL 01-01-25 000001333 NO NON-VETERAN (OTHER)

3 MVIPATIENT,DEVIN 07-04-53 000006666 NO NSC VETERAN

4 MVIPATIENT,RYAN 02-14-01 000007777 YES SC VETERAN

5 MVIPATIENT,SAGE 06-06-60 000000606 NO NSC VETERAN

ENTER '^' TO STOP, OR CHOOSE 1-5: 2\<Enter\> MVIPATIENT,GIL 01-01-25 000001333 NO NON-VETERAN (OTHER)

Warning : You have selected a test patient.

 Enrollment Priority: Category: NOT ENROLLED End Date:

Select PATIENT NAME: DEMONSTRATION

1 MVIPATIENT,ROE 12-24-19 000008888 NO NSC VETERAN

2 MVIPATIENT,GIL 01-01-25 000001333 NO NON-VETERAN (OTHER)

3 MVIPATIENT,DEVIN 07-04-53 000006666 NO NSC VETERAN

4 MVIPATIENT,RYAN 02-14-01 000007777 YES SC VETERAN

5 MVIPATIENT,SAGE 06-06-60 000000606 NO NSC VETERAN

ENTER '^' TO STOP, OR CHOOSE 1-5: 5\<Enter\> MVIPATIENT,SAGE 06-06-60 000000606 NO NSC VETERAN

Warning : You have selected a test patient.

 Enrollment Priority: GROUP 5 Category: IN PROCESS End Date:

Select PATIENT NAME: DEMONSTRATION*\<\<\<--- Need to enter the name again*.

1 MVIPATIENT,ROE 12-24-19 000008888 NO NSC VETERAN

2 MVIPATIENT,GIL 01-01-25 000001333 NO NON-VETERAN (OTHER)

3 MVIPATIENT,DEVIN 07-04-53 000006666 NO NSC VETERAN

4 MVIPATIENT,RYAN 02-14-01 000007777 YES SC VETERAN

5 MVIPATIENT,SAGE 06-06-60 000000606 NO NSC VETERAN

ENTER '^' TO STOP, OR CHOOSE 1-5: 5 \<Enter\> MVIPATIENT,SAGE 06-06-60 000000606 NO NSC VETERAN

Warning : You have selected a test patient.

Enrollment Priority: GROUP 5 Category: IN PROCESS End Date:

Select PATIENT NAME: \<Enter\>

Select MAF APPOINTMENT SYSTEM MENU Option: \<Enter\>

Select MAF APPOINTMENT SYSTEM MENU Option: FM \<Enter\> VA FileMan

VA FileMan Version 22.0 

Select VA FileMan Option: Inquire to File Entries 

OUTPUT FROM WHAT FILE: VA PHONE// VEX

1 VEXM APPOINTMENT CALLS CLINIC IDENTIFIERS (0 entries)

2 VEXM APPOINTMENT CALLS EXCLUDED PATIENTS   (0 entries)

CHOOSE 1-2: 2\<Enter\> VEXM APPOINTMENT CALLS EXCLUDED PATIENTS (0 entries)

Select VEXM APPOINTMENT CALLS EXCLUDED PATIENTS PATIENT NAME: ?

Answer with VEXM APPOINTMENT CALLS EXCLUDED PATIENTS PATIENT NAME

Choose from:

MVIPATIENT,GIL

MVIPATIENT,SAGE 

There are two other "don't call" control parameters both on the client system located on the DHCP-Appointment Options screen. The first one, "Exclude Phone \#s With", is on the VistA-Appointment Parameters screen. It allows the user to define the character. If that character is in the phone number string, the system will not make the call. The second one is named "Excluded \#s." It allows the user to enter the exact telephone \# for a patient and not be called by the system.

## How/Where Do We Find the Correct Patient DFN Used in Exception Messages?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*"We're having difficultyfinding the correct patient with the DFN used in the exception messages? "*

Using FileMan Inquiry in your PATIENT file (#2), you can find the patient by entering the backwards apostrophe (\`) and the DFN at the "Select Patient" prompt.

## Should Sensitive Patients be Shared Between Sites?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

"If a patients is flagged as sensitive at another site, should we make them sensitive at our site? We received a Remote Sensitivity Indicated message stating that the patient was flagged as sensitive at another site but not at our site. Who in the receiving facility should act on this message?"

REMOTE SENSITIVITY INDICATED is an informational bulletin where the patient is marked as sensitive at the sending site but not at receiving site; the site can act or not. There are at least two schools of thought on the issue:

1.  A patient that is sensitive at one site should be sensitive at all sites where seen.
2.  The patient is sensitive at a site for a particular reason that may not be valid at another site. 

Forward the message to the person at your facility that normally evaluates whether or not a patient is sensitive. That person may contact the other facility to determine why the patient is sensitive there and decide if the patient meets the criteria for sensitivity at your facility.

# MPI/PD FAQ—HL7, Links, Background Jobs, Etc.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Re-enable MPIVA DIR Link?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*"When I checked the HL7 links yesterday I noticed a link I don't remember seeing before - MPIVA DIR. It was in a "shutdown" state, supposedly shutdown on 12/20/00 (we installed MPI/PD last weekend). On the HL7 Monitor there is no "type of  link" displayed; there are messages "received", none "processed", some "to send" and an equal number "sent". Should this link be re-enabled?"*

The MPIVA DIR is the MPI direct connect which is the interactive connection with the Austin MPI and it should always be in a shutdown state. The field values you reported are normal for this link. The differences in the messages To Send, Sent, To Be Processed, and Processed are normal and can be ignored.

## Are TCP/IP Links Managed Differently Than Other Links?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*"I've seen some links with "read errors" and "openfail."  From reading the documentation, it appears that "openfail" would indicate some problem with the remote site's listener or UCX service; correct?  What does a "read error" signify, and how can it be corrected?  I tried shutting down and restarting the problem link. I was able to once; however it didn't correct the problem. When I tried to do it again, the HL7 Monitor reported that the link was already running and didn't offer a prompt to shut it down. Are TCP/IP links managed differently than other types of links?"*

The following info was pulled from the HL7 documentation file hl71_6p56_p66.pdf:

3.2.2 Operational Link States (Normal)

|                |                                                                                                                                                                                                                                 |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| State      | Explanation                                                                                                                                                                                                                 |
| Bidding    | X3.28 links: Switching roles, server to sender                                                                                                                                                                                  |
| Check Out  | Checking the "Out" queue for messages to send.                                                                                                                                                                                  |
| Disconnect | X3.28: Line is disconnected.                                                                                                                                                                                                    |
| Done       | HLLP: Message was validated.                                                                                                                                                                                                    |
| Enabled    | Non-persistent TCP links: Link has been started.                                                                                                                                                                                |
| Idle       | No messages are waiting to be sent or received. Idle cycle time is 3 seconds.                                                                                                                                                   |
| Inactive   | Non-persistent TCP links: Link has been started and has delivered messages, but because there are no messages to deliver currently, the background job has been inactivated. The TCP Link Manager will reactivate it as needed. |
| Open       | Link is attempting to open a connection.                                                                                                                                                                                        |
| Polling    | X3.28: Link is checking if there is a message to send.                                                                                                                                                                          |
| Reading    | Link is reading a new message from the connected system.                                                                                                                                                                        |
| Retention  | Non-persistent TCP: Link has delivered messages, but has no more to send; the background process is waiting until either the retention time expires or new messages show up that need to be delivered.                          |
| Send       | Link is transmitting a message.                                                                                                                                                                                                 |
| Validate   | HLLP: Link is calculating a checksum and verifying the value.                                                                                                                                                                   |
| Wait ACK   | X3.28: Link is waiting for an acknowledgment.                                                                                                                                                                                   |
| Writing    | HLLP: Link is sending a message.                                                                                                                                                                                                |

3.2.3 Abnormal or Non-Operational Link States

|              |                                                                                 |
|--------------|---------------------------------------------------------------------------------|
| State    | Explanation                                                                 |
| Error    | Link encountered an error.                                                      |
| Halting  | Link has been asked to shut down.                                               |
| NAK      | HLLP: A negative acknowledgment has been sent.                                  |
| OpenFail | Link could not open a connection to its associated device or target system.     |
| Send NAK | X3.28: Link is sending a negative acknowledgment.                               |
| Shutdown | Link has been shut down.                                                        |
| Timeout  | HLLP: When trying to read from the connected system, a timeout was encountered. |

## How Do I Interpret a DNS Address?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*"Interpreting Ping of HL7 link: I tried to ping a site; the dialog stated "DNS returned:  ..." with an IP address, tried that address, then failed with an error of "DNS lookup failed". How could the DNS lookup fail when it said that DNS returned an address?  Is the DNS address it referred to the one it found in File \#870?"*

The ping first tries to make a successful connection to the TCP/IP address and Port number associated with that link in the HL LOGICAL LINK file (#870). If the ping is unsuccessful, the message "DNS returned" is returned from the KERNEL call \$\$ADDRESS^XLFNSLK("HL7.domain.REDACTED"). Next, it tries to make a successful connection to that address. If unsuccessful, the message "DNS lookup failed" is returned. I know this is somewhat confusing because it isn't the lookup that failed, but the value that was returned from the lookup that failed.

## How Do I Interpret the HL7 Systems Monitor?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*"Whenever I look at this in the HL7 Systems Monitor, the "messages sent" count is usually at least 250 behind the "messages to send". Is this normal, or does something need to be adjusted?  We currently have 2 incoming and 1 outgoing filer running."*

Typically, the number of "messages sent" should equal the number of "messages to send.". If these numbers do not equal, this might be an indication that you’ve had too many retransmissions of the same message. Check the ^RGMTUT98 call and see if there are any backlogged messages. If not, there isn't really a problem. You can always use the HL7 option, Clear a Queue of all Entries, to reset the numbers. If this situation continues, you can log an HL7 NOIS to resolve the issue.

VAWNY  44887  44887  44727  44467  MS  0 server  
\>D ^RGMTUT98  
 \<\<[<u>Run - Jan 19, 2001@14:53:20</u>](mailto:Run%20-%20Jan%2019,%202001@14:53:20)\>\>  
 Outgoing messages:  
 VAMAN - 1 messages.         STATE: Open  
 VALEB - 1 messages.         STATE: Openfail  
 VACMO - 2 messages.         STATE: Open  
 ZZDGRUBATH - 3 messages.    STATE: Halting  
 

 Incoming messages:  
 VAWNY - 1 messages.         STATE: 0 server

## How Do I Correctly Shutdown the UCX Service For My Listener?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*"Shutting down UCX service (VAWNY):  How do you correctly shutdown this link?  Do you only disable the UCX service, or do you also have to shutdown the link in the HL7 menu?"*

Disabling the service will stop the inbound message, so yes you only have to disable the service. Disabling the service won’t stop a connection that has already been established and is sending messages. To be sure that the listener is shutdown, set the SHUTDOWN LLP? field to Yes via VA FileMan. Remember to set this field back to NO before you restart the UCX service.

## How Do I Resolve Links in ERROR or SHUTDOWN State?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These links (for sites that have installed), need to be restarted. For all sites up and running on MPI/PD, all the VA\* and MPIVA links need to be monitored and kept running.

If you see that a link keeps going into ERROR state and staying there, or if you notice a link in OPENFAIL state, contact the National Help Desk at REDACTED and log a Remedy ticket.

HL7 Patch 49 will start up TaskMan jobs when the links have messages to send, but will not remove the link from an error state. It will also not start if the link has not been "enabled" via Patch 49.

If a link remains down for seven days or more, the messages waiting on that link may be purged by the HL7 purge, and will be lost. If possible, the MPI Team would like to avoid this happening. 

## How Do I Restart MPIVA DI if in SHUTDOWN State?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*"MPIVA DI is in a shutdown state. Should I restart the link?  In addition, we have VABOS in a shutdown state until they come up. We are a LEDI site and VABOS link came up when we installed MPI/PD."*

MPIVA DI - does not need to be started. This link is not like typical HL7 links. It is used for the real-time connections. If the shutdown state is confusing, you can change it via VA FileMan to something else.

## How Do I Resolve a Link in an ERROR State?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*"We have VAWPB is in an error state, and also received an alert HL7 Message IEN 672808 exceeded retries for LL VAWPB. VADET is in an openfailed state."*

Stop and restart VAWPB; this should take care of it. The excessive retries are to alert you to go check out the link. If restarting the link doesn’t solve the problem and you can successfully PING via HL7 the VAWPB link, you should contact the National Help Desk at REDACTED and log a NOIS to the HL7 team for assistance. There may be a message stuck at the top of the queue that needs to be manually removed from the queue.

## What is the INACTIVE State?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inactive state means that the link has been enabled under HL7 patch 49 and currently has no messages to send. It is just waiting for something to do. There isn't a TaskMan job until the link is actually sending messages (this is a good thing).

## Purging the HL7 Globals?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*"Can we begin topurge some of the LLP nodes? We installed phase II of CIRN on February 4th. On our SAGG report that was run on 1/28/2000 the HLMA global size was 16,033. The SAGG report run on 3/24/00, HLMA has grown to 165,530."*

You should be running the HL7 purge on a weekly basis, at least. Be sure to schedule it to run via TaskMan and in the off hours. There are parameters that also can be set, at least take the default. That should give you back some disk space.

|                                                                                                                |                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/036.png) | NOTE: Be sure to keep successfully completed messages at least two days. Some messages require that the original message still be in the HLMA global in order to be processed successfully. |

# Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section documents the following categories of supported calls as they relate to the MPI/PD package.

1.  The first category is titled "Supported APIs." This section lists and describes the callable routines, which are supported for general use in interacting with the MPI/PD software (MPIF and RG namespaces).
2.  The second category is titled "Supported APIs (IA Required)." This section lists and describes the MPI/PD callable routines, for which you must obtain an IA in to use.
3.  The third category is titled "Supported APIs (IA Required) to Which MPI/PD is a Subscriber." This section lists and describes the callable routines that the MPI/PD package subscribes to, for which IAs were obtained.

The forth category is the section titled "MPI Direct Connect." You must also obtain an IA for adding the MPI Direct Connect functionality to your VistA package.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/037.png) | NOTE: The list of Integration Agreements (IAs) in which the MPI/PD software (MPIF and RG namespaces) is either custodian or subscriber to can be found on FORUM. For information on how to access these Integration Agreements, see the chapter titled "Callable Routines" in the *Master Patient Index/Patient Demographics (MPI/PD) VistA Technical Manual*. |
| ![](mpi-pd-version-1-vista-programmer-manual/038.png) | NOTE: The MPI/PD software (i.e., routines in the MPIF\* and RG\* namespaces) SHOULD NOT reside/run on Legacy systems. Any VistA applications utilizing APIs in the MPIF and RG namespaces on Legacy systems should check for the existence of these routines before trying to access them.                                                                     |

## Supported APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section documents all the supported APIs belonging to the MPI/PD package for retrieving information from the MPI node in the PATIENT file (#2) or MPI /PD related information. They are sorted by routine name within Integration Agreement (IA) number. The following information is provided for each API listed:

1.  API name (highlighted in boldface) and description
4.  Associated IA

<span id="_Toc510587530" class="anchor"></span>Table 1. MPI/PD Supported APIs

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 25%" />
<col style="width: 23%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>API and Description</strong></th>
<th><strong>Input Parameter(s)</strong></th>
<th><strong>Output Parameter(s)</strong></th>
<th><strong>IA</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>$$CMOR2^MPIF001(DFN)</strong></p>
<p>This API returns the CMOR (Coordinating Master Of Record) Site Name for any given patient.</p></td>
<td>DFN (i.e., The DFN is the IEN entry of the patient from the PATIENT file [#2].)</td>
<td><p>CMOR Site Name</p>
<p>Or</p>
<p>-1^error message</p></td>
<td>2701</td>
</tr>
<tr class="even">
<td><p><strong>$$CMORNAME^MPIF001(CIEN)</strong></p>
<p>This API returns the CMOR Site Name for any given Institution IEN.</p></td>
<td>CIEN (i.e., The CIEN is the IEN entry from the INSTITUTION file [#4].)</td>
<td><p>CMOR Site Name</p>
<p>Or</p>
<p>-1^error message</p></td>
<td>2701</td>
</tr>
<tr class="odd">
<td><p><strong>$$EN2^MPIFAPI()</strong></p>
<p>This API creates and returns the next local ICN and ICN Checksum.</p></td>
<td>None</td>
<td>Local ICN_V_ICN Checksum</td>
<td>2702</td>
</tr>
<tr class="even">
<td><p><strong>$$GETDFN^MPIF001(ICN)</strong></p>
<p>This is the supported API for retrieving the IEN from the PATIENT file (#2) for any given ICN passed as the input parameter. The ICN should be passed without the V or its checksum. Returned is a –1^error message or the IEN for the patient in this site's PATIENT file (#2).</p>
<p><strong>Function call:</strong></p>
<p>S DFN=$$GETDFN^MPIF001(1000720100V271387)</p>
<p><strong>Returned value:</strong></p>
<p>3404040</p></td>
<td>ICN (i.e., Integration Control Number without the checksum or V separator.)</td>
<td>PATIENT file (#2) IEN (i.e., IEN of the patient found to have the passed ICN)</td>
<td>2701</td>
</tr>
<tr class="odd">
<td><p><strong>$$GETICN^MPIF001(DFN)</strong></p>
<p>This API returns the ICN and ICN checksum for the patient passed.</p>
<p>ICN is a 10-digit number followed by the capital letter V and a six-digit checksum. This API returns the complete ICN. It is passed the IEN for the patient in the PATIENT file (#2) . Returned is a -1^error message or the ICN, include the ICN Checksum. For example:</p>
<p><strong>Function call:</strong></p>
<p>S ICN=$$GETICN^MPIF001(3404040)</p>
<p><strong>Returned value:</strong></p>
<p>1000720100V271387</p>
<p>![](mpi-pd-version-1-vista-programmer-manual/039.png) <strong>NOTE:</strong> This will return only the active ICN for the patient. If there was an ICN assigned, but is no longer active, NO ICN will be returned.</p></td>
<td>DFN (i.e., The DFN is the IEN entry of the patient from the PATIENT file [#2].)</td>
<td>ICN_V_ICN CHECKSUM</td>
<td>2701</td>
</tr>
<tr class="even">
<td><p><strong>$$GETVCCI^MPIF001(DFN)</strong></p>
<p>This API returns the CMOR Station Number for the patient who was passed.</p></td>
<td>DFN (i.e., The DFN is the IEN entry of the patient from the PATIENT file [#2].)</td>
<td>Station Number of the CMOR for the given patient.</td>
<td>2701</td>
</tr>
<tr class="odd">
<td><p><strong>$$HL7CMOR^MPIF001(DFN,SEP)</strong></p>
<p>This API returns the CMORs Station Number and Institution Name for any given patient.</p></td>
<td><p>DFN (i.e., The DFN is the IEN entry of the patient from the PATIENT file [#2].)</p>
<p>SEP is the delimiter used to separate Station Number and Name. This is not a required field. Default value is ^.</p></td>
<td>Station Number SEP Institution Name or -1^error message</td>
<td>2701</td>
</tr>
<tr class="even">
<td><p><strong>$$IFLOCAL^MPIF001(DFN)</strong></p>
<p>This API is used to check if a patient has a Local ICN.</p></td>
<td>DFN (i.e., The DFN is the IEN entry of the patient from the PATIENT file [#2].)</td>
<td><p>0 (zero) or 1</p>
<p>The returned value of 0 (zero) means that:</p>
<blockquote>
<p>1. the patient does not exist,</p>
<p>2. the DFN (i.e., The DFN is the IEN entry from the PATIENT file [#2].) is not defined,</p>
<p>3. the MPI node does not exist, or</p>
<p>4. the patient does not have a local ICN.</p>
</blockquote>
<p>The returned value of 1 means that the patient has a Local ICN.</p></td>
<td>2701</td>
</tr>
<tr class="odd">
<td><p><strong>$$IFVCCI^MPIF001(DFN)</strong></p>
<p>This API is used to determine if your site is the CMOR for the given patient.</p></td>
<td>DFN (i.e., The DFN is the IEN entry of the patient from the PATIENT file [#2].)</td>
<td><p>If the number 1 is returned, your site is the CMOR for the given patient.</p>
<p>If a minus number 1 (–1) is returned, your site is NOT the CMOR for the given patient.</p></td>
<td>2701</td>
</tr>
<tr class="even">
<td><p><strong>$$MPILINK^MPIFAPI()</strong></p>
<p>This API returns the name of the HL7 Logical Link that is used to send messages to the MPI. If you are sending a message to the MPI, this is the call to make to get the name of the link.</p></td>
<td>none</td>
<td>HL7 Logical Link name</td>
<td>2702</td>
</tr>
<tr class="odd">
<td><p><strong>$$MPINODE^MPIFAPI(DFN)</strong></p>
<p>This API returns the MPI node for any given patient from the PATIENT file (#2).</p></td>
<td>DFN (i.e., The DFN is the IEN entry of the patient from the PATIENT file [#2].)</td>
<td>MPI node or -1^error message.</td>
<td>2702</td>
</tr>
<tr class="even">
<td><p><strong>$$SUBNUM^MPIFAPI(DFN)</strong></p>
<p>This API returns the Subscription Control Number from the MPI node for any given patient in the PATIENT file (#2).</p></td>
<td>DFN (i.e., The DFN is the IEN entry of the patient from the PATIENT file [#2].)</td>
<td>Subscription Control Number or -1^error message</td>
<td>2702</td>
</tr>
<tr class="odd">
<td><p><strong>GETADFN^MPIFAPI(ICN,DFN)</strong></p>
<p>This API returns the DFN for a given ICN ONLY if the ICN is the active ICN for a patient.</p></td>
<td>ICN (i.e., Integration Control Number without the checksum or V separator.)</td>
<td>DFN (The IEN of the patient in the Patient (#2) file that currently has this ICN as the active ICN (stored in field 991.01). ICN is not found -1^error message is returned.)</td>
<td>2702</td>
</tr>
</tbody>
</table>

## Supported APIs (IA Required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section documents all the supported APIs (IA required) belonging to the MPI/PD package for retrieving information from the MPI node in the PATIENT file (#2) , or MPI /PD related information sorted by routine name. The following information is provided for each API listed:

1.  API name (highlighted in boldface) and description.
2.  Associated IA.

<table>
<colgroup>
<col style="width: 91%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>API and Description</strong></th>
<th><strong>IA</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>^MPIF(984.9,D0,0)</strong></p>
<p>.01 REQUEST NUMBER 0;1 Read w/Fileman</p>
<p>.03 DATE REQUESTED 0;3 Read w/Fileman</p>
<p>.06 STATUS 0;6 Read w/Fileman</p>
<p>.07 SITE 0;7 Read w/Fileman</p>
<p>.08 TYPE OF MESSAGE 0;8 Read w/Fileman</p>
<p><strong>^MPIF(984.9,D0,1)</strong></p>
<p>1.03 TYPE OF REQUEST 1;3 Read w/Fileman</p>
<p><strong>^MPIF(984.9,'C',<br />
</strong> .02 PATIENT 'C' x-re Direct Global Read</p>
<p>To identify all requests for a specific patient we are looping through the 'C' cross reference on the PATIENT (#.02) field.</p>
<p><strong>^MPIF(984.9,'AC',<br />
</strong>The Registration package is requesting a DBIA with Master Patient Index (MPIF) to read with FileMan the MPIF CMOR REQUEST (#984.9) file as well as a direct global read on the "C" and "AC" cross references. This information is used to display need information need to make decision about changing the CMOR.</p></td>
<td>3298</td>
</tr>
<tr class="even">
<td><p><strong>$$CHANGE^MPIF001(DFN,VCCI)<br />
<br />
</strong>This API updates the CIRN MASTER OF RECORD (#991.03) field in the PATIENT file (#2) on the MPI node.</p>
<p>NOTE: Patch RG*1*9 changed user visible references from CIRN to MPI/PD except in file names and most field names where it appears. CIRN Master of Record is now Coordinating Master of Record.</p></td>
<td>2703</td>
</tr>
<tr class="odd">
<td><strong>$$ICNLC^MPIF001<br />
<br />
</strong>This API will return an ICN if one exists or create and return a Local ICN and will update the appropriate fields if a Local was created.</td>
<td>3072</td>
</tr>
<tr class="even">
<td><strong>$$A31^MPIFA31B(DFN,ERR)<br />
<br />
</strong>This API will create an A31 HL7 2.4 standard message for the patient specified by DFN. DFN (input) is the patient's Internal Entry Number from the Patient file (#2) . ERR (output) is the -1 ^ Error message OR the resulting HL7 message number.</td>
<td>3765</td>
</tr>
<tr class="odd">
<td><p><strong>A40^MPIFA40(DFN,DFN2)<br />
<br />
</strong>This API is being called via the special processing routine during a duplicate record merge process. It is the entry point used to tell the MPI that two records at a local site have been merged and that they both had National ICNs that should know be under one ICN. It will build an A40 Merge Patient HL7 message. DFN (input) is the Internal Entry Number from the Patient (#2) file that will remain after the merge process has completed. DFN2 (input) - Internal Entry Number from the Patient (#2) file that will no longer exist (FROM record) after the merge process has completed.</p>
<p>This API will return the message ID returned from the HL7 GENERATE^HLMA call if successful OR -1^error message if unsuccessful.</p></td>
<td>4294</td>
</tr>
<tr class="even">
<td><p><strong>MPIQ^MPIFAPI(DFN)<br />
<br />
</strong>This API provides support for the Registration package to provide real-time queries to the MPI for assignment of an ICN and CMOR. If the MPI is not available, a local ICN will be assigned instead. If the MPI does not already know of this patient, the patient will be added and assigned an ICN. The DFN is the IEN of the patient in the PATIENT file (#2) . This code is to be inserted after all of the required data has been collected on a new patient (new to the PATIENT file (#2)). If the patient is already known, this code should be inserted after the patient has been selected. Interaction will only occur with the MPI if the patient does not have an ICN assignment.</p>
<p>NOTE: The following fields will be updated in the PATIENT file (#2) when a successful interaction with the MPI has occurred: INTEGRATION CONTROL NUMBER (#991.01), ICN CHECKSUM (#991.02), and COORDINATING MASTER OF RECORD (#991.03). If the MPI is unavailable, in addition to the fields noted above, the LOCALLY ASSINGNED ICN (#991.04) will be set to yes.</p></td>
<td>2748</td>
</tr>
<tr class="odd">
<td><strong>$$MPIQQ^MPIFAPI(DFN)<br />
<br />
</strong>This API tasks off the real-time connection to the MPI for an ICN request. This process is the same as the API: MPIQ^MPIFAPI(DFN), but will task the process off to the background.</td>
<td>3300</td>
</tr>
<tr class="even">
<td><strong>$$UPDATE^MPIFAPI(DFN,ARR)<br />
<br />
</strong>This API allows the calling package to update the MPI node fields (#991.01- #991.05) in the PATIENT file (#2).</td>
<td>2706</td>
</tr>
<tr class="odd">
<td><strong>VTQ^MPISAQ(.MPIVAR)<br />
<br />
</strong>This API allows users to do a Display Only Query to the MPI through the MPI/PD Exception Handling Option.</td>
<td>2941</td>
</tr>
<tr class="even">
<td><strong>EXC^RGHLLOG(RGEXC,RGERR)<br />
<br />
</strong>This API will log the exception type of RGEXC with a textual message to include RGERR</td>
<td>2796</td>
</tr>
<tr class="odd">
<td><strong>START^RGHLLOG(RGMSG,RGDC)<br />
<br />
</strong>This API allows the exceptions to be logged for a particular HL7 message that is being processed.</td>
<td>2796</td>
</tr>
<tr class="even">
<td><strong>STOP^RGHLLOG(RGQUIT)<br />
<br />
</strong>This API stops the specified (input variable- RGQUIT) exceptions being logged for an HL7 message.</td>
<td>2796</td>
</tr>
<tr class="odd">
<td><strong>CALC^RGVCCMR2(RGDFN)<br />
<br />
</strong>This API calculates the CIRN CMOR Activity Score for an individual patient. This is being provided for the MPI developers to allow for re-calculating the CIRN CMOR activity score during the CMOR Batch comparison job.</td>
<td>2710</td>
</tr>
</tbody>
</table>

## Supported APIs (IA Required) to Which MPI/PD is a Subscriber

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section documents all the supported APIs (IA required) to which the MPI/PD package subscribes sorted by routine name. The following information is provided for each API listed:

1.  API name (highlighted in boldface) and description.
2.  Associated IA.

<table>
<colgroup>
<col style="width: 91%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>API and Description</strong></th>
<th><strong>IA</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>$$EN^VAFCPID(DFN,VAFSTR,VAFNUM)<br />
<br />
</strong>This API creates a PID segment when a patient is: admitted, discharged, and/or checked out of a clinic. This segment is part of a HL7 message used by MPI/PD to DATE LAST TREATED (#.03) and the ADT/HL7 EVENT REASON fields (#.07) in the TREATING FACILITY LIST file (#391.91). This is patient/facility specific information. The API is passed three input parameters: internal entry number of the PATIENT file (#2), string of fields requested separated by commas, and sequential number for SET ID (default=1).</td>
<td>3015</td>
</tr>
<tr class="even">
<td><p><strong>$$QUERYTF^VAFCTFU1(ICN,.ARRAY,INDX)<br />
<br />
</strong>This routine returns (given an Integration Control Number or a DFN) a list of facilities the patient was seen for care.</p>
<blockquote>
<p>Input: ICN─Patient Integration Control Number.</p>
<p>Both (Input/</p>
<p>Output: ARRAY─This variable is an array variable that the function uses to store the results of the treating facility list. It will be in the structure of x(1), x(2), etc., (e.g., X(1)=500^2960101, where the first piece is the IEN of the institution and the second piece is the current date on record for that institution.)</p>
<p>Input: INDX─The cross-reference to $O through. 'APAT' for patient information linked to treating facilities, 'AEVN' for patient info linked with an event reason. INDX will equal one if 'AEVN' is used, else 'APAT' is used.</p>
<p>Output: $$QUERYTF─Output is 0 if no error exists, or 1^error description, If error exists or no data in the array.</p>
</blockquote></td>
<td>2990</td>
</tr>
<tr class="odd">
<td><p><strong>TFL^VAFCTFU1(.LIST,DFN)<br />
<br />
</strong>This routine returns (given an Integration Control Number or a DFN) a list of facilities the patient was seen for care.</p>
<blockquote>
<p>Both (Input/</p>
<p>Output): LIST:</p>
</blockquote>
<ul>
<li><p>LIST(1)=-1^error message Example error messages: parameter missing, no treating facility, missing DFN, missing ICN, etc. The only time LIST(1) will always be defined is if there is an error; the first piece will be a -1.</p></li>
<li><p>Alternatively, this can be an array of treating facilities; they may or may not be VAMCs:</p>
<ul>
<li><blockquote>
<p>LIST(1)=500^ALBANY^3020513.092^3^VAMC</p>
</blockquote></li>
<li><blockquote>
<p>LIST(2)=662^SAN FRANCISCO^3020311.14^3^VAMC</p>
</blockquote></li>
<li><blockquote>
<p>LIST(3)=200^AUSTIN^^^DPC</p>
</blockquote></li>
</ul></li>
</ul>
<blockquote>
<p>Input: DFN─Required second input parameter equals the IEN in the PATIENT file (#2).</p>
</blockquote></td>
<td>2990</td>
</tr>
<tr class="even">
<td><strong>DELALLTF^VAFCTFU(PAT)<br />
<br />
</strong>This API is called to remove all associated treating facilities for a patient who’s ICN has been inactivated.</td>
<td>2988</td>
</tr>
<tr class="odd">
<td><strong>$$DELETETF^VAFCTFU(PAT,INST)<br />
<br />
</strong>This API is used to address the issue of duplicate treating facilities assigned to a patient; therefore the variable being passed is the IEN in TREATING FACILITY LIST file (#391.91) , not the IEN for a site that the other calls are using.</td>
<td>2988</td>
</tr>
<tr class="even">
<td><strong>$$EVN^VAFHLEVN<br />
<br />
</strong>This API creates an EVN segment when a patient is admitted, discharged, and/or checked out of a clinic. This segment is part of a HL7 message used by MPI/PD to DATE LAST TREATED (#.03) and the ADT/HL7 EVENT REASON (#.07) fields in the TREATING FACILITY LIST file (#391.91) . This is patient/facility specific information. The API is passed two input parameters: the HL7 Event Type and the HL7 Event Reason Code.</td>
<td>3016</td>
</tr>
<tr class="odd">
<td><strong>$$EN^VAFHLPV1<br />
<br />
</strong>This API is called to set a PV1 segment when a patient is checked out of a clinic.</td>
<td>3018</td>
</tr>
<tr class="even">
<td><strong>FILE^VAFCTFU(PDFN,FSTRG,TICN)<br />
<br />
</strong>This API is used to file data into the TREATING FACILITY LIST file (#391.91) (via the ADT/HL7 PIVOT file [#391.72]) under certain conditions.</td>
<td>2988</td>
</tr>
<tr class="odd">
<td><p><strong>DIRECT^XWB2HL7(RET,LOC,RPC,RPCVER,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10)<br />
</strong><br />
This API is used to make a RPC to a remote facility. Users should be prepared to modify their calls to support strong authentication when made available by Infrastructure.</p>
<p>NOTE: MPI/PD is only to call its own RPCs!</p></td>
<td>3144</td>
</tr>
<tr class="even">
<td><p><strong>RTNDATA^XWBDRPC(RET,HDL)<br />
</strong><br />
Contains APIs for deferred RPCs used by HL7 utilities.</p>
<p>NOTE: MPI/PD is only to call its own RPCs!</p></td>
<td>3149</td>
</tr>
</tbody>
</table>

## MPI Direct Connect

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Direct Connect is a real-time Transmission Control Protocol/Internet Protocol (TCP/IP) connection to the Master Patient Index to allow for an immediate request for an ICN. It is activated during the Register A Patient, Load/Edit Patient Data, and Electronic 10-10EZ Processing processes when:

1.  A new patient is added to the system, or
2.  When a patient exists but doesn't have an ICN

This event causes creation of a VQQ-Q02, which is sent to the MPI to find out if the patient is known. If the MPI returns a message stating that the patient is not known, an ADT-A28 Add Person message is then sent to the MPI. If the patient was known or added via the ADT-A28 message, the MPI will return the known information and the patient's entry is updated.

The Display Only Query option, used to view the data the MPI knows about a patient, also utilizes the TCP/IP direct connect with the MPI. A VTQ query is sent to the MPI.

# Background Jobs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## LOCAL/MISSING ICN RESOLUTION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Background job: MPIF LOC/MIS ICN RES

This option starts a background job that assigns ICNs to the following types of patient records, which have not been sent to the MPI:

- Patient records that have local ICNs
- Patient records that have been flagged as being active but do not have an ICN assignment.

It is recommended that this option be scheduled to run via TaskMan every 600 seconds (Patch MPIF\*1\*35).

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 90%" />
<col style="width: 1%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">![](mpi-pd-version-1-vista-programmer-manual/040.png)</td>
<td><p><strong>NOTE:</strong> As of Patch MPI*1*38 (MPI Austin side for the MPIF*1*43 and RG*1*43), this background job no longer automatically adds patients to the MPI.</p>
<p>Previous to the release of this patch, when the Local/Missing ICN Resolution job was processed on the MPI, if a match wasn't found, the patient was added immediately. As of Patch MPI*1*38, this functionality has been changed in that if a match for a patient isn't found on the MPI, a message is sent back to the site indicating this. On the site's side, this triggers an HL7 A28—Add Patient message, which then adds the patient to the MPI.</p></td>
<td></td>
</tr>
<tr class="even">
<td>![](mpi-pd-version-1-vista-programmer-manual/041.png)</td>
<td colspan="3"><strong>NOTE:</strong> A new field, LOCAL/MISSING DATE LAST RAN (#.04), was created in the CIRN SITE PARAMETER file (#991.8) to hold the last date the Local/Missing ICN Resolution Background job ran. The field will be populated by the routine ^MPIFRES.</td>
</tr>
</tbody>
</table>

Local ICNs

ICNs are created for new patients locally at the site when the MPI is unavailable or when the connection is lost prior to the assignment an ICN (e.g., the Direct Connect could not be established). A local ICN is also assigned as a placeholder when a patient has been sent to the MPI but not yet added. This is to ensure identification of these patients as these records await a response from the MPI. Local ICNs look like a national ICN. They contain the same number of digits as a national ICN. The only difference is that the first three digits are the VAMCs station number.

|                                                                                                                |                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/042.png) | NOTE: It is not recommended that local ICNs be sent to remote databases as they will only be known at the local facility that assigned them. |

Missing ICNs

Missing ICNs result from patient records which have been added to the PATIENT file (#2) via other means than through the Patient Information Management System (PIMS) options that establish the real-time connection with the MPI (Load/Edit Patient Data, Register a Patient, and Electronic 10-10EZ Processing). These records are flagged internally for inclusion in the Local/Missing ICN Resolution job.

Resolution of Local/Missing ICNs

The Local/Missing ICN Resolution background job should be scheduled via TaskMan to run every 600 seconds (Patch MPIF\*1\*35). The Local/Missing ICN Resolution job will find either of the following:

- All patient entries in the local PATIENT file (#2) with a local ICN
- Patient entries that have been flagged as missing an ICN

It then sends these patients to the MPI for a national ICN assignment. These patient entries are sent to the MPI requesting an ICN, in batch HL7 messages (maximum of 100 patient entries each). They are processed on the MPI in the same manner as the patient entries presented in the real-time connection, only in batch form instead of individual entries.

## UPDATE BATCH JOB FOR HL7 v2.3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VAFC BATCH UPDATE

The event of updating patient information can take place from several different options within VistA, including VA FileMan. Changes to any of the fields, listed in the table below, are recorded and an entry is created in the ADT/HL7 PIVOT file (#391.71). The entry is then marked as pending transmission. Direct sets to the globals cannot be collected. This background job will periodically collect (via a scheduled job) these marked events and broadcast an ADT-A08 Update Patient Information message. Because it is not possible to determine if the editing of the field is complete, this background job will periodically collect these marked events and broadcast an ADT A08 message (i.e., Update Patient Information). This is a PIMS-generated HL7 message.

| Field Number | Field Name                |
|------------------|-------------------------------|
| 2,.01            | NAME                          |
| 2,.02            | SEX                           |
| 2,.024           | SELF IDENTIFIED GENDER        |
| 2,.03            | DATE OF BIRTH                 |
| 2,.05            | MARITAL STATUS                |
| 2,.08            | RELIGIOUS PREFERENCE          |
| 2,.09            | SOCIAL SECURITY NUMBER        |
| 2,.0931          | PLACE OF BIRTH COUNTRY        |
| 2,.0932          | PLACE OF BIRTH PROVINCE       |
| 2,.111           | STREET ADDRESS \[LINE 1\]     |
| 2,.1112          | ZIP+4                         |
| 2,.112           | STREET ADDRESS \[LINE 2\]     |
| 2,.113           | STREET ADDRESS \[LINE 3\]     |
| 2,.114           | CITY                          |
| 2,.115           | STATE                         |
| 2,.116           | ZIP CODE                      |
| 2,.117           | COUNTY                        |
| 2,.1171          | PROVINCE                      |
| 2,.1172          | POSTAL CODE                   |
| 2,.1172          | COUNTRY                       |
| 2,.121           | BAD ADDRESS INDICATOR         |
| 2,.131           | PHONE NUMBER \[RESIDENCE\]    |
| 2,.132           | PHONE NUMBER \[WORK\]         |
| 2,.133           | EMAIL ADDRESS                 |
| 2,.134           | PHONE NUMBER \[CELLULAR\]     |
| 2,.211           | K-NAME OF PRIMARY NOK         |
| 2,.219           | K-PHONE NUMBER                |
| 2,.2403          | MOTHER'S MAIDEN NAME          |
| 2,.2405          | PREFERRED NAME                |
| 2,.301           | SERVICE CONNECTED?            |
| 2,.302           | SERVICE CONNECTED PERCENTAGE  |
| 2,.31115         | EMPLOYMENT STATUS             |
| 2,.313           | CLAIM NUMBER                  |
| 2,.323           | PERIOD OF SERVICE             |
| 2,.351           | DATE OF DEATH                 |
| 2,.352           | DEATH ENTERED BY              |
| 2,.353           | SOURCE OF NOTIFICATION        |
| 2,.354           | DATE OF DEATH LAST UPDATED    |
| 2,.355           | LAST EDITED BY                |
| 2,.357           | SUPPORTING DOCUMENT TYPE      |
| 2,.361           | PRIMARY ELIGIBILITY CODE      |
| 2,.525           | POW STATUS INDICATED?         |
| 2,2              | RACE INFORMATION              |
| 2,6              | ETHNICITY INFORMATION         |
| 2,391            | TYPE                          |
| 2,991.01         | INTEGRATION CONTROL NUMBER    |
| 2,991.02         | ICN CHECKSUM                  |
| 2,991.03         | COORDINATING MASTER OF RECORD |
| 2,991.04         | LOCALLY ASSIGNED ICN          |
| 2,991.05         | SUBSCRIPTION CONTROL NUMBER   |
| 2,991.06         | CMOR ACTIVITY SCORE           |
| 2,991.07         | SCORE CALCULATION DATE        |
| 2,991.08         | TEMPORARY ID NUMBER           |
| 2,991.09         | FOREIGN ID NUMBER             |
| 2,991.1          | FULL ICN                      |
| 2,994            | MULTIPLE BIRTH INDICATOR      |
| 2,1901           | VETERAN (Y/N)?                |
| 2.01,.01         | ALIAS                         |
| 2.01,1           | ALIAS SSN                     |
| 2.0991,.01       | FULL ICN HISTORY              |
| 2.0992,.01       | ICN HISTORY                   |

This background job also sends out Treating Facility "add me" and Treating Facility Update messages.

|                                                                                                                |                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mpi-pd-version-1-vista-programmer-manual/043.png) | REF: For more information on the ADT A08 Message- Update Patient Information, see the *Master Patient Index (MPI) VistA HL7 Interface Specifications*. |
| ![](mpi-pd-version-1-vista-programmer-manual/044.png) | NOTE: This background job was originally exported in patch DG\*5.3\*91.                                                                                |

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>.001 Field</strong></th>
<th colspan="2">A field containing the internal entry number of the record.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>.01 Field</strong></td>
<td colspan="2">The one field that must be present for every file and file entry. It is also called the NAME field. At a file's creation the .01 field is given the label NAME. This label can be changed.</td>
</tr>
<tr class="even">
<td><strong>10-10EZ</strong></td>
<td colspan="2">Form used to apply for health benefits.</td>
</tr>
<tr class="odd">
<td><strong>Abbreviated Response</strong></td>
<td colspan="2">This feature allows you to enter data by typing only the first few characters for the desired response. This feature will not work unless the information is already stored in the computer.</td>
</tr>
<tr class="even">
<td><strong>Accept Agreement</strong></td>
<td colspan="2">Part of the validation and agreement to the privacy regulations associated with Toolkit (IdM TK).</td>
</tr>
<tr class="odd">
<td><strong>Access Code</strong></td>
<td colspan="2">A code that, along with the Verify code, allows the computer to identify you as a user authorized to gain access to the computer. Your code is greater than 6 and less than 20 characters long; can be numeric, alphabetic, or a combination of both; and is usually assigned by a site manager or application coordinator. It is used by the Kernel's Sign-on/Security system to identify the user (see Verify Code).</td>
</tr>
<tr class="even">
<td><strong>Active Patients</strong></td>
<td colspan="2">Persons who have been seen at a site within the past three years.</td>
</tr>
<tr class="odd">
<td><strong>ADPAC</strong></td>
<td colspan="2">Automated Data Processing Application Coordinator.</td>
</tr>
<tr class="even">
<td><strong>ADR</strong></td>
<td colspan="2">The Administrative Data Repository is the authoritative data store within VHA for cross-cutting person administrative information. The Administrative Data Repository contains identification and cross-cutting demographics data as well as other administrative information. Patient Information Management System (PSIM) uploads the identity demographic data to the ADR. May also include subset of the Enrollment database. May also be referred to as ADR-N or ADR-L to designate a national or local instance.</td>
</tr>
<tr class="odd">
<td><strong>ADT</strong></td>
<td colspan="2">Admission Discharge and Transfer- Part of the Patient Information Management System (PIMS).</td>
</tr>
<tr class="even">
<td><strong>ADT/HL7 PIVOT File</strong></td>
<td colspan="2">Changes to any of the fields of person information will be recorded and an entry created in the ADT/HL7 PIVOT file (#391.71). When an update to a person's treating facility occurs, this event is to be added to the ADT/HL7 PIVOT file (#391.71) and marked for transmission. A background job will collect these updates and broadcast the appropriate HL7 message (ADT-A08 Patient Update).</td>
</tr>
<tr class="odd">
<td><strong>AITC</strong></td>
<td colspan="2">The Master Patient Index (MPI) is located at the Austin Information Technology Center (AITC).</td>
</tr>
<tr class="even">
<td><strong>Alerts</strong></td>
<td colspan="2">Brief online notices that are issued to users as they complete a cycle through the menu system. Alerts are designed to provide interactive notification of pending computing activities, such as the need to reorder supplies or review a patient's clinical test results. Along with the alert message is an indication that the View Alerts common option should be chosen to take further action.</td>
</tr>
<tr class="odd">
<td><strong>Ancillary Reviewer</strong></td>
<td colspan="2">This can be a single person or group of people given the responsibility to conduct reviews of potential duplicate record pairs with data in files other than the PATIENT file (#2). For example, selected personnel in Laboratory, Radiology, and Pharmacy.</td>
</tr>
<tr class="even">
<td><strong>ANSI</strong></td>
<td colspan="2">American National Standards Institute.</td>
</tr>
<tr class="odd">
<td><strong>ANSI M</strong></td>
<td colspan="2">The M (formerly known as MUMPS) programming language is a standard recognized by the American National Standard Institute (ANSI). M stands for Massachusetts Utility Multi-programming System.</td>
</tr>
<tr class="even">
<td><strong>API</strong></td>
<td colspan="2"><p>Program calls provided for use by application programmers. APIs allow programmers to carry out standard computing activities without needing to duplicate utilities in their own software. APIs also further DBA goals of system integration by channeling activities, such as adding new users, through a limited number of callable entry points. VistA APIs fall into the following three categories:</p>
<ul>
<li><p>The first category is "Supported API" These are callable routines, which are supported for general use by all VistA applications.</p></li>
<li><p>The second category is "Controlled Subscription API." These are callable routines for which you must obtain an Integration Agreement (IA - formerly referred to as a DBIA) to use.</p></li>
<li><p>The third category is "Private API," where only a single application is granted permission to use an attribute/function of another VistA package.</p></li>
</ul>
<p>These IAs are granted for special cases, transitional problems between versions, and release coordination.</p></td>
</tr>
<tr class="odd">
<td><strong>application</strong></td>
<td colspan="2">Any software that executes logic or rules which allow people to interface with the computer and programs which collect, manipulate, summarize, and report data and information. .</td>
</tr>
<tr class="even">
<td><strong>Application Coordinator</strong></td>
<td colspan="2">Designated individuals responsible for user-level management and maintenance of an application package such as IFCAP, Lab, Pharmacy, Mental Health, etc.</td>
</tr>
<tr class="odd">
<td><strong>Application Server</strong></td>
<td colspan="2">Software/hardware for handling complex interactions between users, business logic, and databases in transaction-based, multi-tier applications. Application servers, also known as app servers, provide increased availability and higher performance.</td>
</tr>
<tr class="even">
<td><strong>Array</strong></td>
<td colspan="2">An arrangement of elements in one or more dimensions. An M array is a set of nodes referenced by subscripts that share the same variable name.</td>
</tr>
<tr class="odd">
<td><strong>AT-SIGN ("@")</strong></td>
<td colspan="2">A VA FileMan security Access code that gives the user programmer-level access to files and to VA FileMan's developer features. See Programmer Access. Also, the character "@" (i.e., at-sign, Shift-2 key on most keyboards) is used at VA FileMan field prompts to delete data.</td>
</tr>
<tr class="even">
<td><strong>Attribute</strong></td>
<td colspan="2"><p>VHA Definition:</p>
<ul>
<li><p>These are Persons Traits or Meta-Data about the Primary View or the Correlation.</p></li>
</ul>
<p>Identity Hub™ Definition:</p>
<ul>
<li><p>Members have attributes, like Name, Gender, Address, Phone, Birth Date, SSN.</p></li>
<li><p>Attributes are stored in tables according to Segments. Segments are “attribute types” The MEMPHONE segment can hold Home Phone, Cell Phone, and Fax Number information.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Authentication</strong></td>
<td colspan="2">Verifying the identity of the end-user.</td>
</tr>
<tr class="even">
<td><strong>Authorization</strong></td>
<td colspan="2">Granting or denying user access or permission to perform a function.</td>
</tr>
<tr class="odd">
<td><strong>Auto Link Threshold or Threshold, Auto Link</strong></td>
<td colspan="2">The Auto Link Threshold is the level that a Comparison Score must meet or exceed in order for two or more Identity Profiles to be considered the same unique Person Identity.</td>
</tr>
<tr class="even">
<td><strong>Auto-Update</strong></td>
<td colspan="2">The term "auto-update" refers to fields that are updated from a central database (i.e., the Master Veteran Index).</td>
</tr>
<tr class="odd">
<td><strong>Bad Address Indicator (BAI)</strong></td>
<td colspan="2"><p>The Bad Address Indicator field applies to the address at which the person resides. This field should be set as follows (if applicable):</p>
<ul>
<li><p>"UNDELIVERABLE" - Bad Address based on returned mail.</p></li>
<li><p>"HOMELESS" - Patient is known to be homeless.</p></li>
<li><p>"OTHER" - Other Bad Address Reason</p></li>
</ul>
<p>Setting this field will prevent a Bad Address from being shared with HEC and other VAMC facilities. It will also be used to block Means Test Renewal Letters from being sent. Once the Bad Address Indicator is set, incoming “newer" addresses will automatically remove the Bad Address Indicator, and allow the "updated" address to be transmitted to HEC and other VAMC Facilities.</p></td>
</tr>
<tr class="even">
<td><strong>Batch Acknowledgements</strong></td>
<td colspan="2">The format of a HL7 batch acknowledgement message consists entirely of a group of ACK (acknowledgment) messages. In the case of MVI, batch acknowledgements are returned during the initialization process and during the Local/Missing ICN Resolution job. The background job files the ICN, updates the MVI, and then the associated treating facilities and systems. Data returned from this process constitute the acknowledgment of the batch message.</td>
</tr>
<tr class="odd">
<td><strong>Batch Messages</strong></td>
<td colspan="2">There are instances when it is convenient to transfer a batch of HL7 messages. Common examples related to MVI are queries sent to the MVI for an ICN during the initialization process, the resolution of Local or Missing ICNs, and. Such a batch could be sent online using a common file transfer protocol. In the case of the MVI, the HL7 Batch Protocol uses the Batch Header Segment (BHS) and Batch Trailer Segment (BTS) message segments to delineate the batch.</td>
</tr>
<tr class="even">
<td><strong>BHIE</strong></td>
<td colspan="2">Bidirectional Health Information Exchange (Bidirectional Health Information Exchange (BHIE) Web site )</td>
</tr>
<tr class="odd">
<td><strong>Bulletins</strong></td>
<td colspan="2">Electronic mail messages that are automatically delivered by VistA MailMan under certain conditions. For example, a bulletin can be set up to "fire" when database changes occur, such as adding a new Institution in the INSTITUTION file (#4). Bulletins are fired by bulletin-type cross-references.</td>
</tr>
<tr class="even">
<td><strong>Business Requirements</strong></td>
<td colspan="2"><ul>
<li><blockquote>
<p>Requirements state the customer needs the project output will satisfy. Requirements typically start with phrase “The system shall …” Business requirements refers to how the project will satisfy the business mission of the customer.</p>
</blockquote></li>
<li><blockquote>
<p>Business requirements refer to business functions of the project, such as project management, financial management, or change management.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Business Rule</strong></td>
<td colspan="2"><ul>
<li><blockquote>
<p>A policy imposed by the business, or an external entity, on the system used in the process of conducting that business.</p>
</blockquote></li>
<li><blockquote>
<p>A special category of a requirement. A business rule is directive, policy, or procedure within an organization that describes the relationship between two or more entities. Business rules may also come from outside sources such as government regulations and membership association guidelines.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Cache</strong></td>
<td colspan="2">Cache memory is a small area of very fast RAM used to speed exchange of data. Also, a file or directory included on your computer's hard drive which automatically stores the text and graphics from a web page you pull up, which, in turn, allows you to go back to that web page, without having to wait for the information to reload.</td>
</tr>
<tr class="odd">
<td><strong>CAIP</strong></td>
<td colspan="2">Cross-Application Integration Protocol. A framework which provides both applications and services with support for software procedure calls across systems and applications that rely upon infrastructure and middleware technologies, while simultaneously minimizing the direct dependencies of these same applications and services upon these enabling technologies.</td>
</tr>
<tr class="even">
<td><strong>Callable Entry Point</strong></td>
<td colspan="2">An authorized programmer call that may be used in any VistA application package. The DBA maintains the list of DBIC-approved entry points.</td>
</tr>
<tr class="odd">
<td><strong>CAPRI</strong></td>
<td colspan="2">Compensation &amp; Pension Records Interchange (CAPRI). This Graphical User Interface (GUI) software is used to access veterans’ electronic medical records throughout the VA. The Healthcare Identity Management (HC IdM) Team uses CAPRI as a resource for reviewing patient demographic and clinical data.</td>
</tr>
<tr class="even">
<td><strong>catastrophic edit</strong></td>
<td colspan="2">Changes that occur to two or more of the specified set of identity traits during an edit of a person's record.</td>
</tr>
<tr class="odd">
<td><strong>CHDR</strong></td>
<td colspan="2">Clinical Data Repository (CDR) Health Data Repository</td>
</tr>
<tr class="even">
<td><strong>Checksum</strong></td>
<td colspan="2">The result of a mathematical computation involving the individual characters of a routine or file.</td>
</tr>
<tr class="odd">
<td><strong>Client</strong></td>
<td colspan="2">A single term used interchangeably to refer to the user, the workstation, and the portion of the program that runs on the workstation. In an object-oriented environment, a client is a member of a group that uses the services of an unrelated group. If the client is on a local area network (LAN), it can share resources with another computer (server).</td>
</tr>
<tr class="even">
<td><strong>Clinical Patient Record System (CPRS)</strong></td>
<td colspan="2">Clinical Patient Record System provides a computer-based person record and organizes and presents all relevant data on a person in a way that directly supports clinical decision-making. CPRS integrates the extensive set of clinical and administrative applications available within VistA.</td>
</tr>
<tr class="odd">
<td><strong>Common Menu</strong></td>
<td colspan="2">The Common menu consists of options that are available to all users. Entering two question marks at the menus select prompt displays any secondary menu options available to the signed-on user, along with the common options available to all users.</td>
</tr>
<tr class="even">
<td><strong>Controlled Subscription Integration Agreement</strong></td>
<td colspan="2">This applies where the IA describes attributes/functions that must be controlled in their use. The decision to restrict the IA is based on the maturity of the custodian package. Typically, these IAs are created by the requesting package based on their independent examination of the custodian package's features. For the IA to be approved, the custodian grants permission to other VistA packages to use the attributes/functions of the IA; permission is granted on a one-by-one basis where each is based on a solicitation by the requesting package. An example is the extension of permission to allow a package (e.g., Spinal Cord Dysfunction) to define and update a component that is supported within the Health Summary package file structures.</td>
</tr>
<tr class="odd">
<td><strong>Correlation</strong></td>
<td colspan="2">Comparison of person identity traits for multiple records with the Primary View in the ADR and/or MVI databases.</td>
</tr>
<tr class="even">
<td><strong>COTS</strong></td>
<td colspan="2">Commercial Off The Shelf applications sold by vendors through public catalogue listings. COTS software is not intended to be customized or enhanced.</td>
</tr>
<tr class="odd">
<td><strong>Cross Reference</strong></td>
<td colspan="2">There are several types of cross-references available. Most generally, a VA FileMan cross-reference specifies that some action be performed when the field's value is entered, changed, or deleted. For several types of cross-references, the action consists of putting the value into a list; an index used when looking-up an entry or when sorting. The regular cross-reference is used for sorting and for lookup; you can limit it to sorting only.</td>
</tr>
<tr class="even">
<td><strong>Data Attribute</strong></td>
<td colspan="2">A characteristic unit of data such as length, value, or method of representation. VA FileMan field definitions specify data attributes.</td>
</tr>
<tr class="odd">
<td><strong>Data Dictionary (DD)</strong></td>
<td colspan="2"><p>The Data Dictionary is a global containing a description of the kind of data that is stored in the global corresponding to a particular file. VA FileMan uses the data internally for interpreting and processing files.</p>
<p>It contains the definitions of a file's elements (fields or data attributes), relationships to other files, and structure or design. Users generally review the definitions of a file's elements or data attributes; programmers review the definitions of a file's internal structure.</p></td>
</tr>
<tr class="even">
<td><strong>Data Dictionary Access</strong></td>
<td colspan="2">A user's authorization to write/update/edit the data definition for a computer file. Also known as DD Access.</td>
</tr>
<tr class="odd">
<td><strong>Data Integrity</strong></td>
<td colspan="2">This term refers to the condition of patient records in terms of completeness and correctness. It also refers to the process in which a particular patient’s data is synchronized at all the sites in which that person receives care.</td>
</tr>
<tr class="even">
<td><strong>Data Type</strong></td>
<td colspan="2">A specific field or type of information, such as Name, Social Security Number, etc.</td>
</tr>
<tr class="odd">
<td><strong>Database</strong></td>
<td colspan="2">A set of data, consisting of at least one file, that is sufficient for a given purpose. The VistA database is composed of a number of VA FileMan files. A collection of data about a specific subject, such as the PATIENT file (#2); a data collection has different data fields (e.g. patient name, SSN, Date of Birth, and so on). An organized collection of data about a particular topic.</td>
</tr>
<tr class="even">
<td><strong>Database Management System (DBMS)</strong></td>
<td colspan="2">A collection of software that handles the storage, retrieval, and updating of records in a database. A Database Management System (DBMS) controls redundancy of records and provides the security, integrity, and data independence of a database.</td>
</tr>
<tr class="odd">
<td><strong>Date of Death</strong></td>
<td colspan="2">A person may be entered as deceased at a treating facility. If a shared patient is flagged as deceased, an RG CIRN DEMOGRAPHIC ISSUES bulletin is sent to each treating facility telling where, when, and by whom the deceased date was entered. Each site can then review whether the patient should be marked as deceased at their site.</td>
</tr>
<tr class="even">
<td><strong>DBA</strong></td>
<td colspan="2">Database Administrator, oversees software development with respect to VistA Standards and Conventions (SAC) such as namespacing. Also, this term refers to the Database Administration function and staff.</td>
</tr>
<tr class="odd">
<td><strong>DBIA</strong></td>
<td colspan="2">Database Integration Agreement (see Integration Agreements [IA]).</td>
</tr>
<tr class="even">
<td><strong>Default</strong></td>
<td colspan="2">Response the computer considers the most probable answer to the prompt being given. It is identified by double slash marks (//) immediately following it. This allows you the option of accepting the default answer or entering your own answer. To accept the default you simply press the Enter (or Return) key. To change the default answer, type in your response.</td>
</tr>
<tr class="odd">
<td><strong>Demographic Data</strong></td>
<td colspan="2">Identifying descriptive data about a person, such as: name, sex, date of birth, marital status, religious preference, SSN, address, etc.</td>
</tr>
<tr class="even">
<td><strong>Demographics</strong></td>
<td colspan="2">Information about a person, such as name, address, service record, next of kin, and so on.</td>
</tr>
<tr class="odd">
<td><strong>Department of Veterans Affairs</strong></td>
<td colspan="2">The Department of Veterans Affairs (formerly known as the Veterans Administration.)</td>
</tr>
<tr class="even">
<td><strong>Device</strong></td>
<td colspan="2">Peripheral connected to the host computer, such as a printer, terminal, disk drive, modem, and other types of hardware and equipment associated with a computer. The host files of underlying operating systems may be treated like devices in that they may be written to (e.g., for spooling).</td>
</tr>
<tr class="odd">
<td><strong>DFN</strong></td>
<td colspan="2">Data File Number. This is the patient <a href="http://vaww.vista.med.va.gov/iss/acronyms/i-acronyms.asp#ien">IEN</a> (.001 Field) in the PATIENT file (#2). Additionally, this is a defined variable in VistA that refers to the IEN of the patient currently in memory.</td>
</tr>
<tr class="even">
<td><strong>DHCP</strong></td>
<td colspan="2">Decentralized Hospital Computer Program (now known as Veterans Health Information Systems and Technology Architecture [VistA]). VistA software, developed by VA, is used to support clinical and administrative functions at VA Medical Centers nationwide. It is written in M and, via the Kernel, runs on all major M implementations regardless of vendor. VistA is composed of packages that undergo a verification process to ensure conformity with namespacing and other VistA standards and conventions.</td>
</tr>
<tr class="odd">
<td><strong>Dictionary</strong></td>
<td colspan="2">Database of specifications of data and information processing resources. VA FileMan's database of data dictionaries is stored in the FILE of files (#1).</td>
</tr>
<tr class="even">
<td><strong>Direct Connect</strong></td>
<td colspan="2"><p>The Direct Connect is a real-time TCP/IP connection to the MPI to allow for an immediate request for an ICN. Direct Connect is activated when using any of the following PIMS options:</p>
<ul>
<li><p>Register A Patient,</p></li>
<li><p>Load/Edit Patient Data,</p></li>
<li><p>Electronic 10-10EZ Processing,</p></li>
</ul>
<p>and when using the:</p>
<ul>
<li><p>Display Only Query</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Direct Mode Utility</strong></td>
<td colspan="2">A programmer call that is made when working in direct programmer mode. A direct mode utility is entered at the MUMPS prompt (e.g., &gt;D ^XUP). Calls that are documented as direct mode utilities cannot be used in application software code.</td>
</tr>
<tr class="even">
<td><strong>DNS</strong></td>
<td colspan="2">Domain Name Server</td>
</tr>
<tr class="odd">
<td><strong>DOB</strong></td>
<td colspan="2">Date of Birth</td>
</tr>
<tr class="even">
<td><strong>DOD</strong></td>
<td colspan="2">IdM– Date of Death</td>
</tr>
<tr class="odd">
<td><strong>DoD</strong></td>
<td colspan="2">Department of Defense.</td>
</tr>
<tr class="even">
<td><strong>Domain</strong></td>
<td colspan="2">A site for sending and receiving mail.</td>
</tr>
<tr class="odd">
<td><strong>Double Quotes ("")</strong></td>
<td colspan="2">Symbol used in front of a Common option's menu text or synonym to select it from the Common menu. For example, the five-character string "TBOX" selects the User's Toolbox Common option.</td>
</tr>
<tr class="even">
<td><strong>Duplicate Record Merge</strong></td>
<td colspan="2">Patient Merge is a VistA application that provides an automated method to eliminate duplicate patient records within the VistA database (i.e., the VistA PATIENT file [#2]).</td>
</tr>
<tr class="odd">
<td><strong>DUZ</strong></td>
<td colspan="2">Locally defined variable in VistA that refers to the IEN of the logged on user (From the New Person file).</td>
</tr>
<tr class="even">
<td><strong>DUZ(0)</strong></td>
<td colspan="2">Locally defined variable that holds the File Manager Access Code of the signed-on user.</td>
</tr>
<tr class="odd">
<td><strong>Electronic Signature Code</strong></td>
<td colspan="2">Secret password that some users may need to establish in order to sign documents via the computer.</td>
</tr>
<tr class="even">
<td><strong>Eligibility Codes</strong></td>
<td colspan="2">Codes representing the basis of a person's eligibility for care.</td>
</tr>
<tr class="odd">
<td><strong>Encryption</strong></td>
<td colspan="2">Scrambling data or messages with a cipher or code so that they are unreadable without a secret key. In some cases encryption algorithms are one directional, that is, they only encode and the resulting data cannot be unscrambled (e.g. access/verify codes).</td>
</tr>
<tr class="even">
<td><strong>Entry</strong></td>
<td colspan="2">VA FileMan record. An internal entry number (IEN, the .001 field) uniquely identifies an entry in a file.</td>
</tr>
<tr class="odd">
<td><strong>Error Trap</strong></td>
<td colspan="2">A mechanism to capture system errors and record facts about the computing context such as the local symbol table, last global reference, and routine in use. Operating systems provide tools such as the %ER utility. The Kernel provides a generic error trapping mechanism with use of the ^%ZTER global and ^XTER* routines. Errors can be trapped and, when possible, the user is returned to the menu system.</td>
</tr>
<tr class="even">
<td><strong>ESR</strong></td>
<td colspan="2">Enrollment Systems Redesign is a centralized and reengineered Enrollment System.</td>
</tr>
<tr class="odd">
<td><strong>Exception</strong></td>
<td colspan="2">A task that has encountered an error in personal data. Any Data Quality issue that requires detailed documentation. HC IdM finds an Exception based on business rules.</td>
</tr>
<tr class="even">
<td><strong>Extrinsic Function</strong></td>
<td colspan="2">Extrinsic function is an expression that accepts parameters as input and returns a value as output that can be directly assigned.</td>
</tr>
<tr class="odd">
<td><strong>Facility</strong></td>
<td colspan="2">Geographic location at which VA business is performed.</td>
</tr>
<tr class="even">
<td><strong>FHIE</strong></td>
<td colspan="2"><p>Federal Health Information Exchange – A Federal IT health care initiative that facilitates the secure electronic one-way exchange of patient medical information between Government health organizations.</p>
<p>The project participants are the Department of Defense (DoD) and the Department of Veterans Affairs (VA). (<a href="http://vaww.va.gov/FHIE-BHIE/">BHIE Intranet Site</a><br />
> **NOTE:** This is an internal VA Web site and is not available to the public.)</p></td>
</tr>
<tr class="odd">
<td><strong>Field</strong></td>
<td colspan="2">HL7: An HL7 field is a string of characters defined by one of the HL7 data types.<br />
<br />
VistA: In a record, a specified area used for the value of a data attribute. The data specifications of each VA FileMan field are documented in the file's data dictionary. A field is similar to blanks on forms. It is preceded by words that tell you what information goes in that particular field. The blank, marked by the cursor on your terminal screen, is where you enter the information.</td>
</tr>
<tr class="even">
<td><strong>Field Components</strong></td>
<td colspan="2">A field entry may also have discernible parts or components. For example, the person's name is recorded as last name, first name, and middle initial, each of which is a distinct entity separated by a component delimiter (sub-subfield in ASTM e1238-94).</td>
</tr>
<tr class="odd">
<td><strong>File</strong></td>
<td colspan="2">Set of related records treated as a unit. VA FileMan files maintain a count of the number of entries or records.</td>
</tr>
<tr class="even">
<td><strong>File Manager (VA FileMan)</strong></td>
<td colspan="2">VistA's Database Management System (DBMS). The central component of Kernel that defines the way standard VistA files are structured and manipulated.</td>
</tr>
<tr class="odd">
<td><strong>FIN</strong></td>
<td colspan="2">Foreign ID Number</td>
</tr>
<tr class="even">
<td><strong>FIPS</strong></td>
<td colspan="2">Standards published by the U.S. National Institute of Standards and Technology, after approval by the Department of Commerce; used as a guideline for federal procurements.</td>
</tr>
<tr class="odd">
<td><strong>FOIA</strong></td>
<td colspan="2">Freedom of Information Act</td>
</tr>
<tr class="even">
<td><strong>FORUM</strong></td>
<td colspan="2">The central E-mail system within VistA. Developers use FORUM to communicate at a national level about programming and other issues. FORUM is located at the OI Field Office—Washington, DC (162-2).</td>
</tr>
<tr class="odd">
<td><strong>Free Text</strong></td>
<td colspan="2">A DATA TYPE that can contain any printable characters.</td>
</tr>
<tr class="even">
<td><strong>FTP</strong></td>
<td colspan="2">File Transfer Protocol</td>
</tr>
<tr class="odd">
<td><strong>Function Point Count (FPC)</strong></td>
<td colspan="2">The function point method is used to establish a meaningful unit-of-work measure and can be used to establish baseline costs and performance level monitors. Function point analysis centers on its ability to measure the size of any software deliverable in logical, user-oriented terms. Rather than counting lines of code, function point analysis measures the functionality being delivered to the end user.</td>
</tr>
<tr class="even">
<td><strong>GAL</strong></td>
<td colspan="2">Global Address List.</td>
</tr>
<tr class="odd">
<td><strong>Gender</strong></td>
<td colspan="2"><p>The following are listed in Legacy Vista as Standard Gender values:</p>
<ul>
<li><p>F – Female</p></li>
<li><p>M – Male</p></li>
</ul>
<p>SDS table Values:</p>
<ul>
<li><p>F – Female</p></li>
<li><p>M – Male</p></li>
<li><p>A – Ambiguous</p></li>
<li><p>N – Not Applicable</p></li>
<li><p>O - Other</p></li>
<li><p>U – Unknown</p></li>
<li><p>UN – Undifferentiated</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Global Variable</strong></td>
<td colspan="2">Variable that is stored on disk (M usage).</td>
</tr>
<tr class="odd">
<td><strong>GUI</strong></td>
<td colspan="2">Graphical User Interface.</td>
</tr>
<tr class="even">
<td><strong>HC IdM</strong></td>
<td colspan="2">Healthcare Identity Management</td>
</tr>
<tr class="odd">
<td><strong>HDR</strong></td>
<td colspan="2">Health Data Repository – A repository of clinical information normally residing on one or more independent platforms for use by clinicians and other personnel in support of patient-centric care. The data is retrieved from heritage, transaction-oriented systems and is organized in a format to support clinical decision-making in support of patient care. Formerly known as Clinical Data Repository.</td>
</tr>
<tr class="even">
<td><strong>Health Level 7 (HL7) Batch Protocol</strong></td>
<td colspan="2">Protocol utilized to transmit a batch of HL7 messages. The protocol generally uses FHS, BHS, BTS and FTS segments to delineate the batch. In the case of the MPI, the protocol only uses the BHS and BTS segments.</td>
</tr>
<tr class="odd">
<td><strong>Health Level Seven (HL7)</strong></td>
<td colspan="2">National standard for electronic data exchange/messaging protocol. HL7 messages are the dominant standard for peer-to-peer exchange of clinical, text-based information.</td>
</tr>
<tr class="even">
<td><strong>Health Level Seven (HL7) VistA</strong></td>
<td colspan="2">Messaging system developed as VistA software that follows the HL7 Standard for data exchange.</td>
</tr>
<tr class="odd">
<td><strong>Healthcare Identity Management (HC IdM)</strong></td>
<td colspan="2"><p>The Healthcare Identity Management team (formerly the Identity Management Data Quality team)</p>
<ul>
<li><p>Serves as business steward for person identity data for the person's electronic health record (such as name, SSN, date of birth, gender, mother’s maiden name, place of birth) as well as managing the person's longitudinal health record across the enterprise.</p></li>
<li><p>Defines business rules and processes governing healthcare identity management data collection and maintenance.</p></li>
<li><p>Monitors and resolves data integrity issues and conflicts on the MVI and local systems related to the individual’s identity data within their health record, including the resolution of duplicates, mismatches and catastrophic edits to person identity, which affect person care and safety.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>HealtheVet-VistA</strong></td>
<td colspan="2">The next generation of VistA, HealtheVet-VistA, will retain all of the capabilities of legacy VistA but will provide enhanced flexibility for future health care and compliance with the One VA Enterprise Architecture. It will allow seamless data sharing between all parts of VA to benefit veterans and their families.</td>
</tr>
<tr class="odd">
<td><strong>HEC</strong></td>
<td colspan="2">Health Eligibility Center.</td>
</tr>
<tr class="even">
<td><strong>Help Frames</strong></td>
<td colspan="2">Entries in the HELP FRAME file (#9.2) that can be distributed with application packages to provide online documentation. Frames can be linked with other related frames to form a nested structure.</td>
</tr>
<tr class="odd">
<td><strong>Help Prompt</strong></td>
<td colspan="2">The brief help that is available at the field level when entering one or more question marks.</td>
</tr>
<tr class="even">
<td><strong>HINQ</strong></td>
<td colspan="2">Hospital Inquiry- The HINQ module provides the capability to request and obtain veteran eligibility data via the VA national telecommunications network. Individual or group requests are sent from a local computer to a remote Veterans Benefits Administration (VBA) computer where veteran information is stored. The VBA network that supports HINQ is composed of four computer systems located in regional VA payment centers.</td>
</tr>
<tr class="odd">
<td><strong>HIPAA</strong></td>
<td colspan="2">Health Insurance Portability and Accountability Act – A law passed by Congress in 1996 that requires the Department of Health and Human Services to implement regulations that will require the use of specific standards related to health care claims, code sets, identifiers (individual, provider, employer, and health plan), and security. Protects the privacy of individually identifiable health information.</td>
</tr>
<tr class="even">
<td><strong>HL7</strong></td>
<td colspan="2">Health Level 7 – National standard for electronic data exchange/messaging protocol. A standards organization primarily focused on message-oriented middleware for healthcare. HL7 messages are the dominant standard for peer-to-peer exchange of clinical, text-based information.</td>
</tr>
<tr class="odd">
<td><strong>HLO</strong></td>
<td colspan="2">HL7 Optimized. VistA HL7 package routines.</td>
</tr>
<tr class="even">
<td><strong>ICN</strong></td>
<td colspan="2">Persons are assigned a unique identifier, Integration Control Number (ICN), within the process of being added to the MVI database. This number links persons to their records across VHA systems. The Integration Control Number is a unique identifier assigned to patients when they are added to the MVI. The ICN follows the ASTM-E1714-95 standard for a universal health identifier.</td>
</tr>
<tr class="odd">
<td><strong>ID State</strong></td>
<td colspan="2"><p>An attribute of the ICN, which describes the state of the record as Permanent, Temporary, or Deactivated. ID State is composed of the following two fields from the MPI VETERAN/CLIENT file (#985):</p>
<ul>
<li><p>ID STATE (#80) is a set of codes: PERMANENT, TEMPORARY, and DEACTIVATED. Auditing is enabled for this field.</p></li>
<li><p>DATE OF ID STATE (#81) identifies when the ID STATE field was last updated.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Identity Services</strong></td>
<td colspan="2">A business and data service that provides a consistent interface for access and maintenance of person identification to trusted client applications and services. It is the authoritative source for person identification in the Veterans Health Administration (VHA) domain.</td>
</tr>
<tr class="odd">
<td><strong>IdM</strong></td>
<td colspan="2">Identity Management</td>
</tr>
<tr class="even">
<td><strong>IdM Toolkit (IdM TK) Administrator</strong></td>
<td colspan="2">An IdM Toolkit Administrator is a user with additional privileges and security beyond the IdM Toolkit User's available functionality in the system.</td>
</tr>
<tr class="odd">
<td><strong>IEN</strong></td>
<td colspan="2">Internal Entry Number. The IEN number and Station Number comprise the Source ID of the person targeted for the search. The Source ID is used to uniquely identify a person.</td>
</tr>
<tr class="even">
<td><p><strong>IMDQ</strong></p>
<p><strong>New name: "Healthcare Identity Management (HC IdM)"</strong></p></td>
<td colspan="2">The Identity Management Data Quality team (renamed the Healthcare Identity Management team) is a group of Data Management Analysts committed to improving and safeguarding the quality and accessibility of person data throughout the VA enterprise. They are involved in many data quality initiatives, but their primary role is to assist VHA facilities in all matters related to the MVI.</td>
</tr>
<tr class="odd">
<td><strong>Initiate Identity Hub™</strong></td>
<td colspan="2">The Initiate Identity Hub™ is a third-party proprietary off-the-shelf software package that makes use of a Probabilistic Matching Algorithm.</td>
</tr>
<tr class="even">
<td><strong>Initiate Identity<br />
Hub</strong></td>
<td colspan="2">Initiate Systems Inc. software that provides a trusted on-demand system of record for multiple organizations or other entities by accurately identifying the relevant duplicate and fragmented records and linking them – within, as well as across, all data sources</td>
</tr>
<tr class="odd">
<td><strong>Input Template</strong></td>
<td colspan="2">A pre-defined list of fields that together comprise an editing session.</td>
</tr>
<tr class="even">
<td><strong>Institution</strong></td>
<td colspan="2">A Department of Veterans Affairs (VA) facility assigned a number by headquarters, as defined by Directive 97-058. An entry in the INSTITUTION file (#4) that represents the Veterans Health Administration (VHA).</td>
</tr>
<tr class="odd">
<td><strong>Integration Agreements (IA)</strong></td>
<td colspan="2">Integration Agreements define agreements between two or more VistA software applications to allow access to one development domain by another. VistA software developers are allowed to use internal entry points (APIs) or other software-specific features that are not available to the general programming public. Any software developed for use in the VistA environment is required to adhere to this standard; as such, it applies to vendor products developed within the boundaries of DBA assigned development domains (e.g., MUMPS AudioFax). An IA defines the attributes and functions that specify access. The DBA maintains and records all IAs in the Integration Agreement database on FORUM. Content can be viewed using the DBA menu or the Health Systems Design &amp; Development's Web page.</td>
</tr>
<tr class="even">
<td><strong>Integration Control Number (ICN)</strong></td>
<td colspan="2">Persons are assigned a unique identifier, known as an Integration Control Number (ICN), within the process of being added to the MVI database. This number links persons to their records across VHA systems. The Integration Control Number is a unique identifier assigned to persons when they are added to the MVI. The ICN follows the ASTM-E1714-95 standard for a universal health identifier.</td>
</tr>
<tr class="odd">
<td><strong>Internal Entry Number (IEN)</strong></td>
<td colspan="2">The number used to identify an entry within a file. Every record has a unique internal entry number.</td>
</tr>
<tr class="even">
<td><strong>IRM</strong></td>
<td colspan="2">Information Resource Management. A service at VA medical centers responsible for computer management and system security.</td>
</tr>
<tr class="odd">
<td><strong>ISO</strong></td>
<td colspan="2">Information Security Officer.</td>
</tr>
<tr class="even">
<td><strong>ISS</strong></td>
<td colspan="2">Infrastructure and Security Services (now known as Common Services Security Program).</td>
</tr>
<tr class="odd">
<td><strong>IV&amp;V</strong></td>
<td colspan="2"><p>IV&amp;V is the principal activity that oversees the successful implementation and execution of all internal control processes for financial and interfacing systems.</p>
<p>In order to ensure overall systems integrity, IV&amp;V is accomplished organizationally independent from the elements that acquire, design, develop or maintain the system.</p></td>
</tr>
<tr class="even">
<td><strong>KERNEL</strong></td>
<td colspan="2">VistA software that functions as an intermediary between the host operating system and other VistA software applications so that VistA software can coexist in a standard operating-system-independent computing environment. Kernel provides a standard and consistent user and programmer interface between software applications and the underlying M implementation.</td>
</tr>
<tr class="odd">
<td><strong>LAN</strong></td>
<td colspan="2">Local Area Network.</td>
</tr>
<tr class="even">
<td><strong>LAYGO Access</strong></td>
<td colspan="2">A user's authorization to create a new entry when editing a computer file. (Learn As You GO allows you the ability to create new file entries.)</td>
</tr>
<tr class="odd">
<td><strong>LDAP</strong></td>
<td colspan="2">Lightweight Directory Access Protocol.</td>
</tr>
<tr class="even">
<td><strong>Lookup</strong></td>
<td colspan="2">To find an entry in a file using a value for one of its fields.</td>
</tr>
<tr class="odd">
<td><strong>M (ANSI Standard)</strong></td>
<td colspan="2">Massachusetts General Hospital Utility Multi-Programming System (M, formerly named MUMPS). The Mumps language originated in the mid-60's at the Massachusetts General Hospital. Although most implementations are proprietary, consolidated into the hands of a small number of companies, an open source version of the language has been developed which is distributed freely under the GNU GPL and LGPL licenses.</td>
</tr>
<tr class="even">
<td><strong>Mail Message</strong></td>
<td colspan="2">An entry in the MESSAGE file (#3.9). The VistA electronic mail system (MailMan) supports local and remote networking of messages.</td>
</tr>
<tr class="odd">
<td><strong>Mailman</strong></td>
<td colspan="2">VistA software that provides a mechanism for handling electronic communication, whether it's user-oriented mail messages, automatic firing of bulletins, or initiation of server-handled data transmissions.</td>
</tr>
<tr class="even">
<td><strong>Manager Account</strong></td>
<td colspan="2">UCI that can be referenced by non-manager accounts such as production accounts. Like a library, the MGR UCI holds percent routines and globals (e.g., ^%ZOSF) for shared use by other UCIs.</td>
</tr>
<tr class="odd">
<td><strong>Mandatory Field</strong></td>
<td colspan="2">Field that requires a value. A null response is not valid.</td>
</tr>
<tr class="even">
<td><strong>Master Files</strong></td>
<td colspan="2">A set of common reference files used by one or more application systems. These common reference files need to be synchronized across the various applications at a given site. The Master Files Notification transactions provide a way of maintaining this synchronization.</td>
</tr>
<tr class="odd">
<td><strong>Master Patient Index (Austin) or MPI Austin</strong></td>
<td colspan="2">The MPI is a separate computer system located at the Austin Information Technology Center. It maintains a record for VA patients and stores data such as a unique patient identifier and Treating Facility lists (which tracks the sites where that ICN is known).</td>
</tr>
<tr class="even">
<td><strong>Master Patient Index or MPI</strong></td>
<td colspan="2">Master Patient Index is a cross-reference or index of patients that includes the patient’s related identifiers and other patient identifying information. It is used to associate a patient’s identifiers among multiple ID-assigning entities, possibly including a Health Data Repository, to support the consolidation and sharing of a patient’s health care information across VHA. The MPI is the authoritative source for patient identity.</td>
</tr>
<tr class="odd">
<td><strong>Master Patient Index/Patient Demographics (MPI/PD) VistA or MPI/PD</strong></td>
<td colspan="2">Master Patient Index/Patient Demographics (MPI/PD) software initializes entries in the PATIENT file (#2) with the Master Patient Index, itself. The initialization process assigns an Integration Control Number (ICN), Coordinating Master of Record (CMOR), and creates a Treating Facility list of all sites at which the patient has received care. This information is then updated in the PATIENT file (#2) at all sites where the patient has been treated.</td>
</tr>
<tr class="even">
<td><strong>Master Veteran Index or MVI</strong></td>
<td colspan="2">The authoritative source for person identity data. Maintains identity data for persons across VA systems. Provides a unique universal identifier for each person. Stores identity data as correlations for each system where a person is known. Provides a probabilistic matching algorithm. (Includes MPI, PSIM, and IdM TK) Maintains a “gold copy” known as a “Primary View” of the person’s identity data. Broadcasts identity trait updates to systems of interest. Maintains a record locator service.</td>
</tr>
<tr class="odd">
<td><strong>Match Threshold</strong></td>
<td colspan="2">The Match Threshold is the level at which an Identity Profile must score against a set of identity traits in order to be considered a match. For most enterprise applications the Match Threshold would be set at or near the Auto Link Threshold. Internal Identity Management Systems (MPI/PSIM) may use a lower score, perhaps the Task Threshold, as a Match Threshold for identity management decision processes.</td>
</tr>
<tr class="even">
<td><strong>Menu System</strong></td>
<td colspan="2">The overall Menu Manager logic as it functions within the Kernel framework.</td>
</tr>
<tr class="odd">
<td><strong>Menu Text</strong></td>
<td colspan="2">The descriptive words that appear when a list of option choices is displayed. Specifically, the Menu Text field of the OPTION file (#19). For example, User's Toolbox is the menu text of the XUSERTOOLS option. The option's synonym is TBOX.</td>
</tr>
<tr class="even">
<td><strong>Menu Text</strong></td>
<td colspan="2">The descriptive words that appear when a list of option choices is displayed. Specifically, the Menu Text field of the OPTION file (#19). For example, User's Toolbox is the menu text of the XUSERTOOLS option. The option's synonym is TBOX.</td>
</tr>
<tr class="odd">
<td><strong>Message Segments</strong></td>
<td colspan="2">Each HL7 message is composed of segments. Segments contain logical groupings of data. Segments may be optional or repeatable. A [ ] indicates the segment is optional, the { } indicates the segment is repeatable. For each message category, there will be a list of HL7 standard segments and/or "Z" segments used for the message.</td>
</tr>
<tr class="even">
<td><strong>Mirror Testing</strong></td>
<td colspan="2">Functional testing in a non-production VistA system that is maintained by the VA Medical Center (VAMC) and is normally a mirror (snapshot copy) of their production system as of the date the copy was created. The resultant “mirror” account is normally isolated from external VA systems, is scrambled to protect PHI and PII, and is refreshed (recopied from production) on a periodic basis. Users can modify mirror account data without the changes being transmitted to external systems or affecting the site’s live production database. These qualities enable site testers to execute high-priority test scenario scripts provided by the development team and note the success or failure of each script.</td>
</tr>
<tr class="odd">
<td><strong>MMN</strong></td>
<td colspan="2">Mother's Maiden Name: The family name under which the mother was born (i.e., before marriage). It is used to distinguish between patients with the same last name</td>
</tr>
<tr class="even">
<td><strong>MPI Initialization</strong></td>
<td colspan="2">The process of initializing a site's PATIENT file (#2) with the Master Patient Index (MPI). Initialization synchronizes PATIENT file (#2) information (for active shared patients) with the MPI and identifies facilities where the patient has been treated. This process transfers the Integration Control Number (ICN), and Treating Facility list for each patient to the patient's record in the VistA PATIENT file (#2) at all sites where the patient has been treated. It is also possible to initialize an individual patient to the MPI. This is done through menu options. The initial synchronization of PATIENT file (#2) information (for active, shared patients) with the Master Patient Index and with the patient's treating facilities is an important step in the implementation of the MPI/PD software system.</td>
</tr>
<tr class="odd">
<td><strong>Namespace</strong></td>
<td colspan="2">A convention for naming VistA package elements. The Database Administrator (DBA) assigns unique character strings for package developers to use in naming routines, options, and other package elements so that packages may coexist. The DBA also assigns a separate range of file numbers to each package.</td>
</tr>
<tr class="even">
<td><strong>Namespacing</strong></td>
<td colspan="2">Convention for naming VistA software elements. The DBA assigns unique two to four character string prefix for software developers to use in naming routines, options, and other software elements so that software can coexist. The DBA also assigns a separate range of file numbers to each software application.</td>
</tr>
<tr class="odd">
<td><strong>NDBI</strong></td>
<td colspan="2">National Database Integration</td>
</tr>
<tr class="even">
<td><strong>Node</strong></td>
<td colspan="2">In a tree structure, a point at which subordinate items of data originate. An M array element is characterized by a name and a unique subscript. Thus the terms: node, array element, and subscripted variable are synonymous. In a global array, each node might have specific fields or "pieces" reserved for data attributes such as name.</td>
</tr>
<tr class="odd">
<td><strong>NPI</strong></td>
<td colspan="2">National Provider Index</td>
</tr>
<tr class="even">
<td><strong>Null</strong></td>
<td colspan="2">Empty—A field or variable that has no value associated with it is null.</td>
</tr>
<tr class="odd">
<td><strong>Numeric Field</strong></td>
<td colspan="2">Response that is limited to a restricted number of digits. It can be dollar valued or a decimal figure of specified precision.</td>
</tr>
<tr class="even">
<td><strong>OI</strong></td>
<td colspan="2">Office of Information</td>
</tr>
<tr class="odd">
<td><strong>OI&amp;T</strong></td>
<td colspan="2">Office of Information Technology</td>
</tr>
<tr class="even">
<td><strong>OIFO</strong></td>
<td colspan="2">Office of Information Field Office.</td>
</tr>
<tr class="odd">
<td><strong>Option</strong></td>
<td colspan="2">An entry in the OPTION file (#19). As an item on a menu, an option provides an opportunity for users to select it, thereby invoking the associated computing activity. Options may also be scheduled to run in the background, non-interactively, by TaskMan.</td>
</tr>
<tr class="even">
<td><strong>Option Name</strong></td>
<td colspan="2">Name field in the OPTION file (e.g., XUMAINT for the option that has the menu text "Menu Management"). Options are namespaced according to VistA conventions monitored by the DBA.</td>
</tr>
<tr class="odd">
<td><strong>Package (Software)</strong></td>
<td colspan="2">The set of programs, files, documentation, help prompts, and installation procedures required for a given application (e.g., Laboratory, Pharmacy, and PIMS). A VistA software environment is composed of elements specified via the PACKAGE file (#9.4). Elements include files, associated templates, namespaced routines, and namespaced file entries from the OPTION, HELP FRAME, BULLETIN, and FUNCTION files. As public domain software, VistA software can be requested through the Freedom of Information Act (FOIA).</td>
</tr>
<tr class="even">
<td><strong>Person Correlation</strong></td>
<td colspan="2">A profile of an Identity that is maintained by an Associated System and is correlated to only one ICN. (Source - PIDS)</td>
</tr>
<tr class="odd">
<td><strong>Person Identification Service</strong></td>
<td colspan="2">The Person Identification Service (PIDS) is an OMG Interface Specification standard responsible for the identification, correlation, and search within and across a specified domain (A domain is a sphere of influence. For instance, a person has an identifier issued by the Social Security Administration [Social Security Number] which is different that their identifier issued by the State Department [Passport Number]. Both the Social Security Administration and State Department could be considered separate domains.) for identifiers based upon a provided set of search criteria traits. Essentially, this service provides for the assignment and reconciliation of multiple identifiers across domains and in supporting multiple implementation topologies. CORBA specification from OMG. (Source - PIDS)</td>
</tr>
<tr class="even">
<td><strong>PIMS</strong></td>
<td colspan="2">Patient Information Management System- VistA software package that includes Registration and Scheduling packages.</td>
</tr>
<tr class="odd">
<td><strong>PKI</strong></td>
<td colspan="2">Public Key Infrastructure</td>
</tr>
<tr class="even">
<td><strong>POB (Country)</strong></td>
<td>PLACE OF BIRTH COUNTRY: If the person was not born in the USA, this is the country where the individual was born.</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>POB (Province)</strong></td>
<td>PLACE OF BIRTH PROVINCE: The location within certain countries that contain additional divisions of where the individual was born.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>POB (City)</strong></td>
<td colspan="2">PLACE OF BIRTH CITY: The city in which this applicant was born (or foreign country if born outside the U.S.).</td>
</tr>
<tr class="odd">
<td><strong>POB (State)</strong></td>
<td colspan="2">PLACE OF BIRTH STATE: State in which patient was born.</td>
</tr>
<tr class="even">
<td><strong>Pointer</strong></td>
<td colspan="2">The address at which a data value is stored in computer memory. A relationship between two VA FileMan files, a pointer is a file entry that references another file (forward or backward). Pointers can be an efficient means for applications to access data by referring to the storage location at which the data exists.</td>
</tr>
<tr class="odd">
<td><strong>Potential Match Threshold</strong></td>
<td colspan="2">The level at which an Identity Profile must score against a set of identity traits in order to be considered a Potential Match for HC IdM decision processes.</td>
</tr>
<tr class="even">
<td><strong>Primary Key</strong></td>
<td colspan="2">A Data Base Management System construct, where one or more fields uniquely define a record (entry) in a file (table). The fields are required to be populated for every record on the file, and are unique, in combination, for every record on the file.</td>
</tr>
<tr class="odd">
<td><strong>Primary Menu</strong></td>
<td colspan="2">The list of options presented at sign-on. Each user must have a primary menu in order to sign-on and reach Menu Manager. Users are given primary menus by Information Resource Management (IRM). This menu should include most of the computing activities the user needs.</td>
</tr>
<tr class="even">
<td><strong>Primary Reviewer</strong></td>
<td colspan="2">This can be a single person or group of people given the overall responsibility to initiate reviews of potential duplicate record pairs. For example, selected personnel in Patient Administration or a task force or group formed to oversee and conduct the effort of reducing or eliminating the occurrence of duplicate records in the site's database.</td>
</tr>
<tr class="odd">
<td><strong>Primary View</strong></td>
<td colspan="2">Provides the most accurate, current, and complete identity information for a VA patient. The Primary View from the MVI business rules make determinations about data additions and updates to identity traits (Name, SSN, Date of Birth, Gender, Mother's Maiden Name, Place of Birth, and Multiple Birth Indicator) based on the authoritativeness of the update or edits as they are received by the MVI.</td>
</tr>
<tr class="even">
<td><strong>Private Integration Agreement</strong></td>
<td colspan="2">Where only a single application is granted permission to use an attribute/function of another VistA package. These IAs are granted for special cases, transitional problems between versions, and release coordination. A Private IA is also created by the requesting package based on their examination of the custodian package's features. Example: one package distributes a patch from another package to ensure smooth installation.</td>
</tr>
<tr class="odd">
<td><strong>Probabilistic Comparison Score</strong></td>
<td colspan="2"><p>In a Probabilistic Search, these are the points assigned to an identity to indicate the level of confidence of matching to a given set of traits.</p>
<p>If the Comparison Score is above a certain level called the Match Threshold, then the profile is considered to be a match and the profile would be returned to the calling application.</p></td>
</tr>
<tr class="even">
<td><strong>Probabilistic Matching Algorithm</strong></td>
<td colspan="2">A method to determine that a person identity profile has been matched in the PS Datastore based on the Comparison Score, which is calculated for each profile compared to the set of traits used for matching.</td>
</tr>
<tr class="odd">
<td><strong>Probabilistic Search</strong></td>
<td colspan="2">A search using a matching algorithm to determine that a person's identity profile matches a set of defined traits. The algorithm assigns a comparison score and returns results based on a defined match threshold.</td>
</tr>
<tr class="even">
<td><strong>Prompt</strong></td>
<td colspan="2">The computer interacts with the user by issuing questions called prompts, to which the user issues a response.</td>
</tr>
<tr class="odd">
<td><strong>Protocol</strong></td>
<td colspan="2">Entry in the PROTOCOL file (#101). Used by the Order Entry/Results Reporting (OE/RR) package to support the ordering of medical tests and other activities.</td>
</tr>
<tr class="even">
<td><strong>PS</strong></td>
<td colspan="2">Product Support</td>
</tr>
<tr class="odd">
<td><strong>Pseudo SSN Reason</strong></td>
<td colspan="2">The reason that a pseudo SSN has been collected for the patient. The PSEUDO SSN REASON value is a set of codes pulled from the PATIENT (#2) file.</td>
</tr>
<tr class="even">
<td><strong>Pseudo-SSNs</strong></td>
<td colspan="2">False Social Security Numbers that are calculated internally to VistA and cannot be mistaken for valid SSNs because they end in P.</td>
</tr>
<tr class="odd">
<td><strong>PSIM</strong></td>
<td colspan="2">Person Service Identity Management (PSIM) enumerates and maintains person identities.</td>
</tr>
<tr class="even">
<td><strong>Queuing</strong></td>
<td colspan="2">Requesting that a job be processed in the background rather than in the foreground within the current session. Jobs are processed sequentially (first-in, first-out). Kernel's TaskMan module handles the queuing of tasks.</td>
</tr>
<tr class="odd">
<td><strong>Queuing Required</strong></td>
<td colspan="2">Option attribute that specifies that the option must be processed by Task Manager (the option can only be queued). The option may be invoked and the job prepared for processing, but the output can only be generated during the specified times.</td>
</tr>
<tr class="even">
<td><strong>Receiving Site</strong></td>
<td colspan="2">Receiving Site- As it relates to HL7 Messages, it is the site that the message was sent to.</td>
</tr>
<tr class="odd">
<td><strong>Record</strong></td>
<td colspan="2">Set of related data treated as a unit. An entry in a VA FileMan file constitutes a record. A collection of data items that refer to a specific entity (e.g., in a name-address-phone number file, each record would contain a collection of data relating to one person).</td>
</tr>
<tr class="even">
<td><strong>REEME</strong></td>
<td colspan="2">Registration/Eligibility/Enrollment Maintenance and Enhancement</td>
</tr>
<tr class="odd">
<td><strong>Registration Process</strong></td>
<td colspan="2"><p>During a registration, the person is checked against the entries in the Master Veteran Index (MVI) to determine if the person is already established or needs to be added. As of Patch DG*5.3*915 “Enterprise Search” replaced Register Once in the registration process to include Department of Defense (DoD) patients in an “extended” patient lookup if no patients are found on the MVI.</p>
<p>Within the Register a Patient [DG REGISTER PATIENT] option, the initial patient lookup search remains unchanged. That is, if a patient lookup performed in the site’s local VistA system returns one or more <em><u>existing</u></em> patients, the Registration user is asked to confirm the patient’s identity. However, if the patient is <em><u>not</u></em> found in the site’s local VistA system, the user is prompted to perform an “Enterprise Search,” which includes searching the DoD system if none found on the MVI. If the user chooses not to do an Enterprise Search, the software returns the user to the Select PATIENT prompt.</p>
<p>As of Patch DG*5.3*915, an Enterprise Search is required to add <em><u>new</u></em> patients to the local VistA system via the Register a Patient [DG REGISTER PATIENT] option.</p>
<p><strong>Using the Enterprise Search functionality:</strong></p>
<p>Upon choosing to do an Enterprise Search, the Registration user is presented with a series of prompts to enter the search criteria. If insufficient search criteria have been entered, the system displays a message requesting the user to enter the search criteria again. Sufficient search criteria entered automatically sends a query to the MVI to attempt to find possible matches. If matches <em><u>are not</u></em> found on the MVI, the query is automatically sent to the DoD system to find matches.</p>
<p>Patient matches that are found are returned grouped as an Auto Link or Potential Match for the registration staff to review. If a patient entry is selected, their data from the MVI (or DoD) is automatically loaded into the new patient's record. If that patient is already enrolled in the VA system, a query is sent to obtain the patient's Enrollment record prior to entering the registration screens. Then the registration process continues as normal.</p>
<p>Other possible results returned from an Enterprise Search:</p>
<ul>
<li><p>If too many matches are returned from the Enterprise Search, then the user is prompted to provide updated (more specific) search criteria to return a more limited search result list from which to select.</p></li>
<li><p>If no patients are found on the MVI or if the connection to the MVI is down, the user will be prompted to add the patient based upon the data previously entered.</p></li>
<li><p>If the matches returned are above the Auto Link threshold, then the user <em>must</em> select one of the patients returned from the query (Auto Link threshold or Potential Match threshold) or hold the security key, DG MVI ADD PT, to override the selection.</p></li>
<li><p>NOTE: Records that are returned from the Enterprise Search of the MVI or DoD systems are displayed in the closest match order based upon score.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Remote Procedure Call (RPC)</strong></td>
<td colspan="2">Remote Procedure Call is a protocol that one program can use to request a service from a program located on another computer network. Essentially M code may take optional parameters to do some work and then return either a single value or an array back to the client application.</td>
</tr>
<tr class="odd">
<td><strong>Requesting Site</strong></td>
<td colspan="2">Requesting Site- As is relates to HL7 Messages, it is the site initiating a message to another site requesting some action be taken.</td>
</tr>
<tr class="even">
<td><strong>Required Field</strong></td>
<td colspan="2">A mandatory field, one that must not be left blank. The prompt for such a field will be repeated until the user enters a valid response.</td>
</tr>
<tr class="odd">
<td><strong>Resolution Journal Case Number</strong></td>
<td colspan="2">IDM – Number associated with each Resolution Journal Case. Used by the HealthCare Identity Management (HC IdM) team to document detailed information mostly for duplicate exception resolution but may also be used to denote details for resolving any type of exception.</td>
</tr>
<tr class="even">
<td><strong>RG CIRN DEMOGRAPHIC ISSUES mail group</strong></td>
<td colspan="2"><p>The RG CIRN DEMOGRAPHIC ISSUES bulletin controls the sending of the following person related bulletin:</p>
<ul>
<li><p>Person Related Bulletin—REMOTE SENSITIVITY INDICATED</p></li>
<li><p>Cause—person is marked as sensitive at the sending site but not at receiving site.</p></li>
<li><p>Action to take—No action: message is informational</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Routine</strong></td>
<td colspan="2">Program or a sequence of instructions called by a program that may have some general or frequent use. M routines are groups of program lines, which are saved, loaded, and called as a single unit via a specific name.</td>
</tr>
<tr class="even">
<td><strong>SAC</strong></td>
<td colspan="2">Standards and Conventions. Through a process of quality assurance, all VistA software is reviewed with respect to SAC guidelines as set forth by the Standards and Conventions Committee (SACC).</td>
</tr>
<tr class="odd">
<td><strong>SACC</strong></td>
<td colspan="2">VistA's Standards and Conventions Committee. This Committee is responsible for maintaining the SAC.</td>
</tr>
<tr class="even">
<td><strong>Scheduling Options</strong></td>
<td colspan="2">The technique of requesting that Task Manager run an option at a given time, perhaps with a given rescheduling frequency.</td>
</tr>
<tr class="odd">
<td><strong>Screen Editor</strong></td>
<td colspan="2">VA FileMan's Screen-oriented text editor. It can be used to enter data into any WORD-PROCESSING field using full-screen editing instead of line-by-line editing.</td>
</tr>
<tr class="even">
<td><strong>ScreenMan Forms</strong></td>
<td colspan="2">Screen-oriented display of fields, for editing or simply for reading. VA FileMan's Screen Manager is used to create forms that are stored in the FORM file (#.403) and exported with a software application. Forms are composed of blocks (stored in the BLOCK file [#.404]) and can be regular, full screen pages or smaller, "pop-up" pages.</td>
</tr>
<tr class="odd">
<td><strong>Screen-Oriented</strong></td>
<td colspan="2">A computer interface in which you see many lines of data at a time and in which you can move your cursor around the display screen using screen navigation commands. Compare to Scrolling Mode.</td>
</tr>
<tr class="even">
<td><strong>Security Key</strong></td>
<td colspan="2">The purpose of Security Keys is to set a layer of protection on the range of computing capabilities available with a particular software package. The availability of options is based on the level of system access granted to each user.</td>
</tr>
<tr class="odd">
<td><strong>Self Identified Gender</strong></td>
<td colspan="2"><p>The value of the Self Identified Gender field specifies the patient’s self-identified gender identity. This value will be displayed <em><u>only</u></em> if it is <em><u>not</u></em> null. The field displays as “SELF-IDENTIFIED GENDER IDENTITY.” This field is a SET of codes that specifies the patient's preferred gender:</p>
<ul>
<li><p>M = Male.</p></li>
<li><p>F = Female.</p></li>
<li><p>TM = Transmale/Transman/Female-to-Male.</p></li>
<li><p>TF = Transfemale/Transwoman/Male-to-Female.</p></li>
<li><p>O = Other.</p></li>
<li><p>N = individual chooses not to answer.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Sending Site</strong></td>
<td colspan="2">Sending Site—As it relates to HL7 Messages, it is the site that is transmitting the message to another site.</td>
</tr>
<tr class="odd">
<td><strong>Sensitive Patient</strong></td>
<td colspan="2">Person whose record contains certain information, which may be deemed sensitive by a facility, such as political figures, employees, patients with a particular eligibility or medical condition. If a shared patient is flagged as sensitive at one of the treating sites, a bulletin is sent to the DG SENSITIVITY mail group at each subscribing site telling where, when, and by whom the flag was set. Each site can then review whether the circumstances meet the local criteria for sensitivity flagging.</td>
</tr>
<tr class="even">
<td><strong>Server</strong></td>
<td colspan="2">The computer where the data and the Business Rules reside. It makes resources available to client workstations on the network. In VistA, it is an entry in the OPTION file (#19). An automated mail protocol that is activated by sending a message to a server at another location with the "S.server" syntax. A server's activity is specified in the OPTION file (#19) and can be the running of a routine or the placement of data into a file.</td>
</tr>
<tr class="odd">
<td><strong>Set Of Codes</strong></td>
<td colspan="2">Usually a preset code with one or two characters. The computer may require capital letters as a response (e.g., M for male and F for female). If anything other than the acceptable code is entered, the computer rejects the response.</td>
</tr>
<tr class="even">
<td><strong>Shared Patient</strong></td>
<td colspan="2">A person who has been seen at more than one VistA site. The MVI keeps the Treating Facility list updated every time a new facility is added. The MVI broadcasts out an updates to the treating facility list, including date last treated and event reason.</td>
</tr>
<tr class="odd">
<td><strong>Site Manager/IRM Chief</strong></td>
<td colspan="2">At each site, the individual who is responsible for managing computer systems, installing and maintaining new modules, and serving as a liaison to the CIO Field Offices.</td>
</tr>
<tr class="even">
<td><strong>Software (Package)</strong></td>
<td colspan="2">The set of programs, files, documentation, help prompts, and installation procedures required for a given application (e.g., Laboratory, Pharmacy, and PIMS). A VistA software environment is composed of elements specified via the PACKAGE file (#9.4). Elements include files, associated templates, namespaced routines, and namespaced file entries from the OPTION, HELP FRAME, BULLETIN, and FUNCTION files. As public domain software, VistA software can be requested through the Freedom of Information Act (FOIA).</td>
</tr>
<tr class="odd">
<td><strong>Source ID</strong></td>
<td colspan="2"><p>A Source ID is a term used to describe the components that define a unique correlation. There are 4 components of a Source ID in MVI:</p>
<ol type="1">
<li><p>Assigning Authority (ex. USVHA)</p></li>
<li><p>Assigning Location (ex. Station #)</p></li>
<li><p>IDType (e.g. NI, PI, EI)</p></li>
<li><p>Internal Identifier - A code used at the assigning location used to uniquely identify a person.</p></li>
</ol>
<p>The Initiate Identity Hub also uses the term Source ID, but with a slightly different context. The Source ID in the IDHub is the unique identifier of a correlated system.. The fourth Source ID component, IEN, would translate to the Member ID in the ID HUB. Thus, the IDHub uses 2 components to uniquely identify a member: Source ID and Member ID.</p></td>
</tr>
<tr class="even">
<td><strong>Spacebar Return</strong></td>
<td colspan="2">You can answer a VA FileMan prompt by pressing the spacebar and then the Return key. This indicates to VA FileMan that you would like the last response you were working on at that prompt recalled.</td>
</tr>
<tr class="odd">
<td><strong>Special Queuing</strong></td>
<td colspan="2">Option attribute indicating that Task Manager should automatically run the option whenever the system reboots.</td>
</tr>
<tr class="even">
<td><strong>SSA</strong></td>
<td colspan="2">Social Security Administration</td>
</tr>
<tr class="odd">
<td><strong>SSDI</strong></td>
<td colspan="2">Social Security Death Index (SSDI). The SSDI is a database used for genealogical research as well as enabling users to locate a death certificate, find an obituary, and discover cemetery records and track down probate records. The Healthcare Identity Management (HC IdM) Team uses the SSDI (<a href="http://www.genealogybank.com/gbnk/ssdi/">Social Security Death Index Web site</a> ) as a resource for verifying patients’ dates of death.</td>
</tr>
<tr class="even">
<td><strong>SSN</strong></td>
<td colspan="2">Social Security Number</td>
</tr>
<tr class="odd">
<td><strong>SSN Verification Status</strong></td>
<td colspan="2"><p>Possible values of this field used on the MVI for the Enrollment System Redesign (ESR) correlation are:</p>
<ul>
<li><p>NEW RECORD</p></li>
<li><p>IN-PROCESS</p></li>
<li><p>INVALID PER SSA</p></li>
<li><p>RESEND TO SSA</p></li>
<li><p>VERIFIED</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Station Identifier</strong></td>
<td colspan="2">The number assigned to a VAMC facility or a System Association. The station identifier may be three characters in length designating the facility as a parent organization or up to six characters in length designating the facility as a child of a parent organization.</td>
</tr>
<tr class="odd">
<td><strong>Subscriber</strong></td>
<td colspan="2">A subscriber is an entity, which receives updates to a patient's descriptive data from other sites. All treating facilities are also made subscribers as part of the MPI/PD processes.</td>
</tr>
<tr class="even">
<td><strong>Subscript</strong></td>
<td colspan="2">A symbol that is associated with the name of a set to identify a particular subset or element. In M, a numeric or string value that: is enclosed in parentheses, is appended to the name of a local or global variable, and identifies a specific node within an array.</td>
</tr>
<tr class="odd">
<td><strong>Supported Reference Integration Agreement</strong></td>
<td colspan="2">This applies where any VistA application may use the attributes/functions defined by the IA (these are also called "Public "). An example is an IA that describes a standard API such as DIE or VADPT. The package that creates/maintains the Supported Reference must ensure it is recorded as a Supported Reference in the IA database. There is no need for other VistA packages to request an IA to use these references; they are open to all by default.</td>
</tr>
<tr class="even">
<td><strong>Synchronized Patient Data</strong></td>
<td colspan="2">Key descriptive fields in the PATIENT file (#2) that are updated in all the descriptive subscriber's PATIENT files whenever the fields are edited by a subscriber.</td>
</tr>
<tr class="odd">
<td><strong>Systems of Interest</strong></td>
<td colspan="2">The term "systems of interest" refers to VA facilities that have seen patients and entered them as entries onto the MVI. This also refers to non-VistA systems that have a registered interest in a patient (e.g., Federal Health Information Exchange [FHIE], HomeTeleHealth, Person Service Identity Management [PSIM], Health Data Repository [HDR], etc.).</td>
</tr>
<tr class="even">
<td><strong>Task Manager</strong></td>
<td colspan="2">Kernel module that schedules and processes background tasks (also called TaskMan)</td>
</tr>
<tr class="odd">
<td><strong>Task Threshold or Threshold, Task</strong></td>
<td colspan="2"><p>The Task Threshold (also called the Clerical Review Threshold) is a value that is less than the Auto Link Threshold. A Comparison Score above the Task Threshold and below the Auto Link Threshold needs to be reviewed by an Identity Management expert to determine whether the Identity Profile is either a match or not a match for the traits being compared.</p>
<p>The Task Threshold is determined and tuned by Identity Management experts and may change over time as software systems and business processes improve. The ideal goal for automated identity matching is to minimize the difference between the Task Threshold and the Auto Link Threshold.</p></td>
</tr>
<tr class="even">
<td><strong>TCP/IP</strong></td>
<td colspan="2">Transaction Control Protocol/Internet Protocol. A set of protocols for Layers 3 (Network) and 4 (Transfer) of the OSI network model. TCP/IP has been developed over a period of 15 years under the auspices of the Department of Defense. It is a de facto standard, particularly as higher-level layers over Ethernet. Although it builds upon the OSI model, TCP/IP is not OSI-compliant.</td>
</tr>
<tr class="odd">
<td><strong>Template</strong></td>
<td colspan="2">Means of storing report formats, data entry formats, and sorted entry sequences. A template is a permanent place to store selected fields for use at a later time. Edit sequences are stored in the INPUT TEMPLATE file (#.402), print specifications are stored in the PRINT TEMPLATE file (#.4), and search or sort specifications are stored in the SORT TEMPLATE file (#.401).</td>
</tr>
<tr class="even">
<td><strong>TIN</strong></td>
<td colspan="2">Temporary ID Number</td>
</tr>
<tr class="odd">
<td><strong>Toolkit (IdM TK)</strong></td>
<td colspan="2">The User Interface for the HealthCare Identity Management team. The Toolkit provides functionality to allow HC IdM staff to search and view identity and exception information. This includes the ability to view the Primary View record and any associated correlations, correlation data, history, audit trails, and HC IdM Tasks captured by MVI. In addition, functionality is provided to support the re-hosting transition for a side-by-side comparison of ADR and MVI information.</td>
</tr>
<tr class="even">
<td><strong>Treating Facility</strong></td>
<td colspan="2">Any facility (VAMC) where a person has applied for care, or has been added to the local PATIENT file (#2) (regardless of VISN) and has identified this person to the MVI will be placed in the TREATING FACILITY LIST file (#391.91).</td>
</tr>
<tr class="odd">
<td><strong>Treating Facility List</strong></td>
<td colspan="2">Table of institutions at which the person has received care. This list is used to create subscriptions for the delivery of person clinical and demographic information between sites.</td>
</tr>
<tr class="even">
<td><strong>Trigger</strong></td>
<td colspan="2">A type of VA FileMan cross-reference. Often used to update values in the database given certain conditions (as specified in the trigger logic). For example, whenever an entry is made in a file, a trigger could automatically enter the current date into another field holding the creation date.</td>
</tr>
<tr class="odd">
<td><strong>Trigger Event</strong></td>
<td colspan="2">The event that initiates an exchange of messages is called a trigger event. The HL7 Standard is written from the assumption that an event in the real world of health care creates the need for data to flow among systems. The real-world event is called the trigger event. For example, the trigger event "a patient is admitted" may cause the need for data about that patient to be sent to a number of other systems. There is a one-to-many relationship between message types and trigger event codes. The same trigger event code may not be associated with more than one message type.</td>
</tr>
<tr class="even">
<td><strong>TSPR</strong></td>
<td colspan="2">Technical Services Project Repository</td>
</tr>
<tr class="odd">
<td><strong>UAT</strong></td>
<td colspan="2">User Acceptance Testing.</td>
</tr>
<tr class="even">
<td><strong><u>U</u>nique <u>P</u>atient <u>I</u>dentifier (UPI)</strong></td>
<td colspan="2"><ul>
<li><p><strong>Outward Facing UPI (Social Security Number [SSN]):</strong> Requirements that apply to what the user sees (<u>outward facing</u>) should be what is currently stated in P&amp;LMS policy; currently still the Social Security Number (SSN).</p></li>
<li><p><strong>Inward Facing UPI (Integration Control Number [ICN]):</strong> Any requirements that refer to <u>inward facing</u> functions (internal clinical applications patient lookups) should use the Integration Control Number (ICN).</p></li>
<li><p><strong>Potential replacement for SSN as Outward Facing UPI (EDIPI):</strong> DoD EDIPI may eventually become the outward facing unique patient identifier (UPI), which is why the new VHIC 4.0 cards contain the EDIPI. However, there are some Veterans for whom the DoD has not provided EDIPI’s; therefore, VA has not announced the EDIPI as the official outward facing UPI and will not do so until VA and DoD have closed that gap to ensure all Veterans can be assigned the EDIPI.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>User Access</strong></td>
<td colspan="2"><p>This term is used to refer to a limited level of access, to a computer system, which is sufficient for using/operating a package, but does not allow programming, modification to data dictionaries, or other operations that require programmer access. Any option, for example, can be locked with the key XUPROGMODE, which means that invoking that option requires programmer access.</p>
<p>The user's access level determines the degree of computer use and the types of computer programs available. The System Manager assigns the user an access level.</p></td>
</tr>
<tr class="even">
<td><strong>VA</strong></td>
<td colspan="2">Department of Veterans Affairs</td>
</tr>
<tr class="odd">
<td><strong>VA Domiciliary</strong></td>
<td colspan="2">Provides comprehensive health and social services in a VA facility for eligible veterans who are ambulatory and do not require the level of care provided in nursing homes.</td>
</tr>
<tr class="even">
<td><strong>VA FileMan</strong></td>
<td colspan="2">VistA's Database Management System (DBMS). The central component that defines the way standard VistA files are structured and manipulated.</td>
</tr>
<tr class="odd">
<td><strong>VA Hospital</strong></td>
<td colspan="2">An institution that is owned, staffed and operated by VA and whose primary function is to provide inpatient services. NOTE: Each division of an integrated medical center is counted as a separate hospital.</td>
</tr>
<tr class="even">
<td><strong>VA Medical Center (VAMC)</strong></td>
<td colspan="2"><p>A unique VA site of care providing two or more types of services that reside at a single physical site location. The services provided are the primary service as tracked in the VHA Site Tracking (VAST) (i.e., VA Hospital, Nursing Home, Domiciliary, independent outpatient clinic (IOC), hospital-based outpatient clinic (HBOC), and CBOC).</p>
<p>The definition of VA medical center does not include the Vet Centers as an identifying service. NOTE: This definition was established by the Under Secretary for Health.</p></td>
</tr>
<tr class="odd">
<td><strong>VA Nursing Home Care Units (NHCU)</strong></td>
<td colspan="2">Provide care to individuals who are not in need of hospital care, but who require nursing care and related medical or psychosocial services in an institutional setting. VA NHCUs are facilities designed to care for patients who require a comprehensive care management system coordinated by an interdisciplinary team. Services provided include nursing, medical, rehabilitative, recreational, dietetic, psychosocial, pharmaceutical, radiological, laboratory, dental and spiritual.</td>
</tr>
<tr class="even">
<td><strong>Variable</strong></td>
<td colspan="2">Character, or group of characters, that refer(s) to a value. M (previously referred to as MUMPS) recognizes 3 types of variables: local variables, global variables, and special variables. Local variables exist in a partition of main memory and disappear at sign-off. A global variable is stored on disk, potentially available to any user. Global variables usually exist as parts of global arrays. The term "global" may refer either to a global variable or a global array. A special variable is defined by systems operations (e.g., $TEST).</td>
</tr>
<tr class="odd">
<td><strong>VBA SHARE</strong></td>
<td colspan="2">This is a VBA application which is utilized by the Regional Offices to access BIRLS, C&amp;P, PIF, PHF, Corporate Database, Social Security and COVERS records. The Healthcare Identity Management (HC IdM) Team uses VBA SHARE as a resource for verifying patient identity data as well as military information.</td>
</tr>
<tr class="even">
<td><strong>Verify Code</strong></td>
<td colspan="2">The Kernel's Sign-on/Security system uses the Verify code to validate the user's identity. This is an additional security precaution used in conjunction with the Access code. Verify codes shall be at least eight characters in length and contain three of the following four kinds of characters: letters (lower- and uppercase), numbers, and, characters that are neither letters nor numbers (e.g., "#", "@" or "$"). If entered incorrectly, the system does not allow the user to access the computer. To protect the user, both codes are invisible on the terminal screen.</td>
</tr>
<tr class="odd">
<td><strong>Vet Center</strong></td>
<td colspan="2">A data source under the direct supervision of the Readjustment Counseling Service (RCS). The Vet Center provides professional readjustment counseling, community education, outreach to special populations, brokering of services with community agencies, and access to important links.</td>
</tr>
<tr class="even">
<td><strong>VHA</strong></td>
<td colspan="2">Veterans Health Administration.</td>
</tr>
<tr class="odd">
<td><strong>VIS</strong></td>
<td colspan="2">Veterans Information Solution (VIS). This intranet-based application is designed to provide a consolidated view of information about veterans and active service members. The HC IdM Team uses VIS as a resource for verifying patient identity data as well as military information.</td>
</tr>
<tr class="even">
<td><strong>VISN</strong></td>
<td colspan="2">Veterans Integrated Service Network</td>
</tr>
<tr class="odd">
<td><strong>VistA</strong></td>
<td colspan="2"><p>Veterans Health Information Systems and Technology Architecture (VistA) of the Veterans Health Administration (VHA), Department of Veterans Affairs (VA). VistA software, developed by the VA, is used to support clinical and administrative functions at VHA sites nationwide. It is both roll-and-scroll- and GUI-based software that undergoes a quality assurance process to ensure conformity with namespacing and other VistA standards and conventions (see <a href="http://vaww.oed.portal.va.gov/communities/app_dev/sac/default.aspx">SAC</a>).</p>
<p>Server-side code is written in M, and, via Kernel, runs on all major M implementations regardless of vendor. Client-side code is written in Java or Borland Delphi and runs on the Microsoft operating system.</p></td>
</tr>
<tr class="even">
<td><strong>VPID (replaced with ICN.)</strong></td>
<td colspan="2">Veterans Administration Personal Identifier – An enterprise-level identifier uniquely identifying VA „persons‟ across the entire VA domain.</td>
</tr>
<tr class="odd">
<td><strong>WAN</strong></td>
<td colspan="2">Wide Area Network.</td>
</tr>
<tr class="even">
<td><strong>Z segment</strong></td>
<td colspan="2">All message type and trigger event codes beginning with Z are reserved for locally defined messages. No such codes will be defined within the HL7 Standard.</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](mpi-pd-version-1-vista-programmer-manual/045.png)</td>
<td><p><strong>REF:</strong> For a comprehensive list of commonly used terms and definitions, please visit the Process Management OIT Master Glossary :</p>
<blockquote>
<p><a href="http://vaww.oed.wss.va.gov/process/Lists/glossary/default.aspx">OI&amp;T Master Glossary Web site</a></p>
</blockquote>
<p><em><strong>NOTE:</strong> This is an internal VA Web site and is not available to the public.</em></p></td>
</tr>
</tbody>
</table>

## # Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Additional Patient Identity Fields, 19
ALIAS multiple
Field \#1 in File \#2, 20
Field \#50 in File \#985, 20
stored on MVI and synchronized to VistA, 20
APIs (Supported)
\$\$CMOR2^MPIF001(DFN), 39
\$\$CMORNAME^MPIF001(CIEN), 39
\$\$EN2^MPIFAPI(), 40
\$\$GETDFN^MPIF001(ICN), 40
\$\$GETICN^MPIF001(DFN), 40
\$\$GETVCCI^MPIF001(DFN), 40
\$\$HL7CMOR^MPIF001(DFN,SEP), 41
\$\$IFLOCAL^MPIF001(DFN), 41
\$\$IFVCCI^MPIF001(DFN), 41
\$\$MPILINK^MPIFAPI(), 41
\$\$MPINODE^MPIFAPI(DFN), 41
\$\$SUBNUM^MPIFAPI(DFN), 41
GETADFN^MPIFAPI(ICN,DFN), 42
APIs (Supported—IA required MPI/PD subscriber)
\$\$DELETETF^VAFCTFU(PAT,INST), 47
\$\$EN^VAFCPID(DFN,VAFSTR,VAFNUM), 46
\$\$EN^VAFHLPV1, 47
\$\$EVN^VAFHLEVN, 47
\$\$QUERYTF^VAFCTFU1(ICN,.ARRAY,INDX), 46
DELALLTF^VAFCTFU(PAT), 47
DIRECT^XWB2HL7(RET,LOC,RPC,RPCVER,P1,P2,P3,P4,P5,P6,P7,P8,P9,P10), 47
FILE^VAFCTFU(PDFN,FSTRG,TICN), 47
RTNDATA^XWBDRPC(RET,HDL), 47
TFL^VAFCTFU1(.LIST,DFN), 46
APIs (Supported—IA required)
\$\$A31^MPIFA31B(DFN,ERR), 43
\$\$CHANGE^MPIF001(DFN,VCCI), 43
\$\$ICNLC^MPIF001, 43
\$\$MPIQQ^MPIFAPI(DFN), 44
\$\$UPDATE^MPIFAPI(DFN,ARR), 44
^MPIF(984.9,'AC',, 43
^MPIF(984.9,'C',, 43
^MPIF(984.9,D0,0), 43
^MPIF(984.9,D0,1), 43
A40^MPIFA40(DFN,DFN2), 44
CALC^RGVCCMR2(RGDFN), 45
EXC^RGHLLOG(RGEXC,RGERR), 44
MPIQ^MPIFAPI(DFN), 44
START^RGHLLOG(RGMSG,RGDC), 44
STOP^RGHLLOG(RGQUIT), 44
VTQ^MPISAQ(.MPIVAR), 44
Appendix D: Why Doesn't a Patient Have a National ICN?
Electronic 10-10EZ Processing, 28
HL7 ADT-A28 message, 29
Load/Edit Patient Data, 28
local ICN, 29
patient record does not have a national ICN?, 28
Register a Patient, 28
Are TCP/IP links managed differently than other links?, 35
authoritative source for ICN information?, 23
B
Background Jobs
LOCAL/MISSING ICN RESOLUTION, 49
UPDATE BATCH JOB FOR HL7 v2.3, 50
Business Processes That Update Person Identity, 8
C
Callable Routines
Direct Connect, 39, 47
Supported APIs, 39
Supported APIs (IA Required), 39, 43
Supported APIs (IA Required) to which MPI/PD is a subscriber, 39, 46
Can a
patient's ICN change?, 29
vendor use an ICN to identify a patient?, 30
Chapter 1: Introduction, 1–21
Distinguishing MPI (Austin) from MPI/PD (VistA), 2
MPI Identity Hub for the HC IdM Team, 2
Overview of Master Patient Index/Patient Demographics, 1
Overview of Master Veteran Index (MVI), 1
Primary View
How are VistA Sites Affected?, 7
Product Description―What Comprises the Master Patient Index?, 3–6
Chapter 2
MPI/PD FAQ, 22
Chapter 2: MPI/PD FAQ, 22–38
Are TCP/IP Links Managed Differently Than Other Links?, 35
Can a Patient's ICN Change?, 29
Can a Vendor Use an ICN to Identify a Patient?, 30
How Can I Retrieve a Patient's ICN as a VistA Developer/Application?, 27
How Can I Tell if an ICN has Change?, 29
How Can My VistA Application Get an ICN Assignment for a Patient?, 30
How do I
get correlation data?, 23
get Primary View data?, 22
How Do I Block Automatic Calls to a Patient if Other Treating Facilities Don’t Use the Same Characters?, 32
How Do I Correctly Shutdown the UCX Service For My Listener?, 37
How Do I Ensure Test System Data is Not Sent to the MPI?, 30
How Do I Interpret a DNS Address?, 36
How Do I Interpret the HL7 Systems Monitor?, 37
How Do I Resolve a Link in an ERROR State?, 38
How Do I Resolve Links in ERROR or SHUTDOWN State?, 37
How Do I Restart MPIVA DI if in SHUTDOWN State?, 38
How does a patient get an ICN?, 25
How/Where Do We Find the Correct Patient DFN Used in Exception Messages?, 34
Is the MPI the authoritative source for this information?, 23
Purging the HL7 Globals?, 38
Should Sensitive Patients be Shared Between Sites?, 34
Under What Conditions are Local ICNs Assigned to Patient Records?, 27
What Causes a Patient Record Not to Have a National ICN Assignment?, 28
What Causes a Patient Record to Have ONLY a Local ICN Assignment?, 29
What does an ICN look like?, 25
What is a local ICN?, 26
What is an Integration Control Number (ICN)?, 23
What is the Communication Procedure with the MPI?, 30
What is the INACTIVE State?, 38
What is the Master Patient Index (MPI)?, 22
Where is the ICN stored?, 26
Chapter 3: Callable Routines, 39–48
Chapter 4: Background Jobs, 49–52
Contents, ix
Correlation Data?, How do I Get, 23
D
DFN used in Exception Messages?, How/Where Do We find the correct patient, 34
DG\*5.3\*653, 9
DG\*5.3\*688, 9
DG\*5.3\*756, 9
Direct Connect, 24, 39, 47
Display Only Query option, 48
Distinguishing MPI (Austin) from MPI/PD (VistA), 2
DNS address?, How do I interpret a, 36
E
Edit PV Alias Values \[MPI DATA MGT EDIT PV ALIAS\], 20
Electronic 10-10EZ Processing, 4, 25, 28, 47
Enhanced MPI-to-VistA Synchronization, 19
Multiple Birth Indicator Synchronized to Systems of Interest, 19
SSN and Pseudo SSN Reason Synchronized to Systems of Interest, 19
SSN Verification Status Synchronized to Systems of Interest, 19
The ALIAS Multiple Stored on MPI and Synchronized to VistA, 20
Enterprise Search
Registration Process, 71
ERROR or SHUTDOWN state?, How Do I Resolve links in, 37
ERROR state, Link, 38
Exception Messages?, How/Where Do we find the correct patient DFN used in, 34
F
FAQs
Are TCP/IP Links Managed Differently Than Other Links?, 35
Can a
patient's ICN change?, 29
vendor use an ICN to identify a patient?, 30
find the Correct Patient DFN Used in Exception Messages?, 34
How can
I retrieve a patient's ICN as a VistA developer/application?, 27
I tell if an ICN has change?, 29
my VistA application get an ICN assignment for a patient?, 30
How do I
block automatic calls to a patient if other Treating Facilities don’t use the same characters?, 32
correctly shutdown the UCX service for my listener?, 37
ensure test system data is not sent to the MPI?, 30
get correlation data?, 23
get Primary View data?, 22
interpret a DNS address?, 36
interpret the HL7 Systems Monitor?, 37
resolve a link in an ERROR State?, 38
resolve links in ERROR or SHUTDOWN State?, 37
restart MPIVA DI if in SHUTDOWN State?, 38
How does a patient get an ICN?, 25
How/Where Do We Find the Correct Patient DFN Used in Exception Messages?, 34
Is the MPI the authoritative source for this information?, 23
Purging the HL7 Globals?, 38
re-enable MPIVA DIR Link?, 35
Re-enable MPIVA DIR Link?, 35
Should Sensitive Patients be Shared Between Sites?, 34
Under What Conditions are Local ICNs Assigned to Patient Records?, 27
What Causes a Patient Record Not to Have a National ICN Assignment?, 28
What Causes a Patient Record to Have ONLY a Local ICN Assignment?, 29
What does an ICN look like?, 25
What is a local ICN?, 26
What is an Integration Control Number (ICN)?, 23
What is the Communication Procedure with the MPI?, 30
What is the INACTIVE State?, 38
What is the Master Patient Index (MPI)?, 22
Where is the ICN stored?, 26
files
MPI VETERAN/CLIENT file (#985), 3, 9, 10
PATIENT file (#2), 9, 25, 26, 27, 28, 39, 40, 41, 43, 44, 46
TREATING FACILITY LIST file (#391.91), 46, 47
Frequently Asked Questions (FAQ), MPI/PD, 22
G
Glossary, 53–79
Glossary (Security and Common Services)
Web Address, 79
H
Healthcare Identity Management (HC IdM)
Data Steward for the MPI, 3
View/Edit Authority Values for Business Rules Criterion, 21
HL LOGICAL LINK file (#870)
How Do I interpret a DNS address?, 36
HL7
Globals?, Purging the, 38
Systems Monitor?, How do I interpret the, 37
Home Pages
Security and Common Services
Glossary Web Address, 79
How can
I retrieve a patient's ICN as a VistA developer/package?, 27
I tell if an ICN has changed?, 29
my VistA application get an ICN assignment for a patient?, 30
How do I
block automatic calls to a patient if treating facility doesn’t use the same characters?, 32
correctly shutdown the UCX Service for my Listener?, 37
ensure test system data is not sent to the MPI?, 30
find the Correct Patient DFN Used in Exception Messages?, 34
get correlation data?, 23
get Primary View data?, 22
interpret a DNS address?, 36
interpret the HL7 Systems Monitor?, 37
re-enable MPIVA DIR Link?, 35
Resolve links in ERROR or SHUTDOWN state?, 37
restart MPIVA DI if in SHUTDOWN state?, 38
How does
a patient get an ICN?, 25
How Does the Primary View Work?, 8
How/Where Do We find the correct patient DFN used in Exception Messages?, 34
I
ICN
Can a vendor use an to identify a patient?, 30
Can it change?, 29
Direct Connect becomes unavailable?, 25
How can
I retrieve a patient's ICN as a VistA developer/package?, 27
I tell if it has changed?, 29
my VistA application get an ICN assignment for a patient?, 30
How does a patient get an ICN?, 25
Integration Control Number, 25
local assignment, 25
What Causes a Patient Record Not to Have a National ICN Assignment?, 28
What does it look like?, 25
Where is it stored?, 26
ICN assignment
exact match on MPI, 3
local, 27, 49
local ICN, 29
Local/Missing ICN Resolution, 27
MPI Austin, 3
MPI VistA, 4, 22
national, 3, 4, 22, 49
patient record does not have a national ICN?, 28
requesting, 4
transmission to MPI, 27
UPDATE BATCH JOB FOR HL7 v2.3, 27
VistA can't connect, 27
What Causes a Patient Record Not to Have a National ICN Assignment?, 28
INACTIVE state, 38
Integration Control Number
local assignment, 25
Integration Control Number (ICN)?, What is an, 23
Introduction, 1–21
Patches MPIF\*1\*52, RG\*1\*54, XT\*7.3\*113, 2
Is the MPI the authoritative source for this information?, 23
L
Link is in an ERROR state?, 38
Load/Edit Patient Data, 4, 25, 28, 47
local ICNs
assignment, 25
Under What Conditions are Local ICNs Assigned to Patient Records?, 27
What is it?, 26
Local/Missing ICN Resolution, 27
national ICN assignment, 27
LOCAL/MISSING ICN RESOLUTION, 49
M
Master Patient Index?
How do I ensure test system data is not sent to the MPI?, 30
What is the communication procedure?, 30
Master Veteran Index
What is the?
Master Patient Index (Austin), 3
Master Patient Index/Patient Demographics (VistA), 4
Product Description, 3
Systems of Interest, 6
Treating Facilities, 6
Master Veteran Index (MVI), 1
menu text
Clear a Queue of all Entries, 37
Electronic 10-10EZ Processing, 4, 25, 28, 47
Inactivate Patient from MPI, 28
Load/Edit Patient Data, 4, 25, 28, 47
Local/Missing ICN Resolution, 4
Master Patient Index Menu, 28
PIMS—Electronic 10-10EZ Processing, 25
PIMS—Load/Edit Patient Data, 25
PIMS—Register a Patient, 25
Register a Patient, 4, 25, 28, 47
MPI Fields Broadcast to Systems of Interest, 9
MPI Primary View Centralized Business Rules
Primary View Identity Traits, 9
MPI VETERAN/CLIENT file (#985), 3, 9, 10
ALIAS multiple (#50), 19
MPI\*1\*40, 2, 5, 9
MPI\*1\*90, 10, 12, 13
MPI\*1\*91, 14
MPI/PD Exception Handling
Primary View Reject Type and View PV Rej Detail (PVR) Action, 21
MPI/PD Frequently Asked Questions (FAQ), 22
MPI/PD Patient Admin Coordinator Menu \[MPIF CMOR MGR\] obsolete, 5
MPIF\*1\*44, 5
MPIF\*1\*52, 2, 4
MPIVA DI SHUTDOWN state, 38
MPIVA DIR link?, Re-enable, 35
Multiple Birth Indicator Synchronized to Systems of Interest, 19
O
obsolete
CMOR, 5
MPI/PD Patient Admin Coordinator Menu \[MPIF CMOR MGR\], 5
options
DG LOAD PATIENT DATA, 4, 25, 28, 47
DG REGISTER PATIENT, 4, 25, 28, 47
Display Only Query, 48
EAS EZ 1010EZ PROCESSING, 4, 25, 28, 47
EXCLUDE PATIENT FROM CALLING, 32
MPI DATA MGT EDIT PV ALIAS, 20
MPIF LOC/MIS ICN RES, 4
MPIF PAT INACT, 28
MPIF VISTA MENU, 28
Orientation, xii–xv
P
Patch
DG\*5.3\*653, 9
DG\*5.3\*688, 9
DG\*5.3\*756, 9
MPI\*1\*40, 2, 5, 9
MPI\*1\*90, 10, 12, 13
MPI\*1\*91, 14
MPIF\*1\*44, 5
MPIF\*1\*52, 4
RG\*1\*45, 9, 19
RG\*1\*47, 9, 19
RG\*1.0\*62, iii
XT\*7.3\*113, 5
Patch History, viii
Patches MPIF\*1\*52, RG\*1\*54, XT\*7.3\*113, 2
PATIENT file (#2), 9, 25, 27, 28, 39, 40, 41, 43, 44, 46
ALIAS multiple (#1), 20
DFN, 39
FileMan Inquiry, 34
find a patient, 34
ICN Checksum, field (#991.02), 26
ICN History Multiple, 29
Integration Control Number, field (#991.01), 26
Where is the ICN Stored?, 26
PIMS—Electronic 10-10EZ Processing, 25
PIMS—Load/Edit Patient Data, 25
PIMS—Register a Patient, 25
Primary View
Additional Patient Identity Fields, 19
Business Processes That Update Person Identity, 8
data rules, 8
Enhanced MPI-to-VistA Synchronization, 19
HC IdM View/Edit Authority Values for Business Rules Criterion, 21
How are VistA Sites Affected?, 7
How Does the Primary View Work?, 8
MPI Fields Broadcast to Systems of Interest, 9
MPI/PD Exception Handling, 21
Multiple Birth Indicator Synchronized to Systems of Interest, 19
Primary View Identity Traits, 9
process for updating, 20
reject exception, 21
SSN and Pseudo SSN Reason Synchronized to Systems of Interest, 19
SSN Verification Status Synchronized to Systems of Interest, 19
The ALIAS Multiple Stored on MPI and Synchronized to VistA, 20
View PV Rej Detail (PVR) action, 21
What is the Primary View?, 7
Primary View Data Rules, 8
Primary View Data?, How do I Get, 22
Primary View Identity Traits, 9, 10
Primary View Reject Type, 21
Primary_View, 7–21
Process for updating the Primary View, 20
Product Description
HC IdM is Data Steward for the MPI, 3
ICN assignment, 3
Master Patient Index/Patient Demographics (VistA), 4
Primary View Replaces Obsolete CMOR View, 5
Requesting ICN Assignment, 4
Systems of Interest to the MPI, 6
Treating Facilities and Non-VistA Systems, 6
What Comprises the Master Patient Index Austin?, 3
Product Description―What Comprises the Master Patient Index?, 3–6
Purging the HL7 Globals?, 38
R
Re-enable MPIVA DIR link?, 35
Register a Patient, 4, 25, 28, 47
Registration Process
Enterprise Search, 71
RG\*1\*45, 9
RG\*1\*45, 19
RG\*1\*47, 9, 19
RG\*1\*54, 2
RG\*1.0\*62, iii
S
Security and Common Services
Glossary Web Address, 79
sensitive patients shared between sites, 34
Should sensitive patients be shared between sites?, 34
SHUTDOWN state, MPIVA DI, 38
SSN and Pseudo SSN Reason Synchronized to Systems of Interest, 19
SSN Verification Status Synchronized to Systems of Interest, 19
Supported APIs, 39
(IA Required), 39, 43
(IA Required) to which MPI/PD is a subscriber, 39, 46
Systems of Interest
MPI Fields Broadcast to, 9
T
Tables and Figures, xi
TCP/IP links, 35
treating facilities
Direct Connect becomes unavailable?, 25
TREATING FACILITY LIST file (#391.91)
ADT/HL7 EVENT REASON field (#.07), 47
DATE LAST TREATED (#.03), 46
duplicate treating facilities, 47
file data, 47
MPI/PD to DATE LAST TREATED (#.03), 47
TREATING FACILITY LIST file (#391.91), 46
U
UCX Service for my Listener?, How do I correctly shutdown the, 37
UPDATE BATCH JOB FOR HL7 v2.3, 50
local ICN assignment, 27
URLs
Security and Common Services
Web Address, Glossary, 79
V
View PV Rej Detail (PVR) Action, 21
W
Web Pages
Security and Common Services
Glossary Web Address, 79
What Causes a Patient Record Not to Have a National ICN Assignment?, 28
What does an ICN look like?, 25
What is a
local ICN?, 26
What is the
communication procedure with the MPI?, 30
INACTIVE state?, 38
Integration Control Number (ICN)?, 23
Master Patient Index (MPI)?, 22
What is the Master Veteran Index?
Master Patient Index (Austin), 3
Master Patient Index/Patient Demographics (VistA), 4
Product Description, 3
Treating Facilities, 6
What is the Primary View?, 7
Where is the
ICN stored?, 26
X
XT\*7.3\*113, 2, 5
