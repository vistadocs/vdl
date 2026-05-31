---
title: IVM*2*174 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: null
app_code: IVM
app_name: Income Verification Match
section: FIN
app_status: active
pkg_ns: IVM
patch_ver: 2
patch_id: IVM*2*174
group_key: IVM:IVM:2
file_numbers:
- '2'
- '408.13'
security_keys: []
menu_options: 0
description: '''[Table 1: Defects and Fixes in IVM_20_P174.KID'''
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 2079
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: January 2019
revision_count: 0
revision_newest: ''
revision_oldest: ''
docx_url: https://www.va.gov/vdl/documents/Financial_Admin/Income_Verif_Match_(IVM)/ivm_2_p174_rn.docx
pdf_url: https://www.va.gov/vdl/documents/Financial_Admin/Income_Verif_Match_(IVM)/ivm_2_p174_rn.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=44
audit_applied: '2026-05-31'
master_source: IVM*2*174 Release Notes
master_pub_date: January 2019
consolidated_from: 3 versions
prior_versions:
- IVM*2*172 Release Notes
- IVM*2*177 Release Notes
consolidated_title: release notes
---

![](ivm-2-174-release-notes/001.png)

January 2019

Office of Information and Technology (OIT)

Table of Contents

List of Tables

[Table 1: Defects and Fixes in IVM_20_P174.KID [5](#_Toc522886001)](#_Toc522886001)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Purpose](#purpose)
- [Audience](#audience)
- [This Release](#this-release)
  - [Defects and Fixes](#defects-and-fixes)
- [Known Issues](#known-issues)
- [Product Documentation](#product-documentation)
The emergency release of Veterans Health Information System and Technology Architecture (VistA) Registration, Eligibility & Enrollment (REE) Host File IVM_20_P174.KID, which includes Income Verification Match (IVM) patch IVM\*2.0\*174 and Enrollment Application System (EAS) patch EAS\*1.0\*172, supports a defect fix to the Enrollment System (ES) 5.3 release. This release supports the modifications for the Enterprise Health Benefits Determination (EHBD) program that focuses on updates for the Enrollment System Modernization (ESM) Phase 2 project, which supports Enrollment System Community Care (ESCC) and ES Sustainment.

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These Release Notes cover the changes to VistA REE IVM and EAS systems for this release.

# Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of VistA REE, the IVM and EAS systems and applies to the changes made between this release and any previous release for this software.

# This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This multi-package build is distributed as a Host File. The Host File IVM_20_P174.KID can be obtained from one of the anonymous Secure File Transfer Protocol (SFTP) directories listed in the Software and Documentation Retrieval Instructions section of the patch descriptions.

Host File IVM_20_P174.KID, which includes patches IVM\*2.0\*174 and EAS\*1.0\*172, addresses Your IT Services incident INC1928289 to fix a critical defect introduced by ES 5.3 and corrected by 5.3.0.07001, and where the dependent Social Security Number (SSN) data at the Veterans Health Information System and Technology Architecture (VistA) facilities was corrupted and requires a VistA patch to clean up the database corruption.

Patch IVM\*2.0\*174 is a follow-up patch to DG\*5.3\*970 and it is required to install this patch. Patch DG\*5.3\*970 created global ^XTMP("DG53970P") which lists the dependent records' Internal Entry Numbers (IENs) in the INCOME PERSON file (#408.13) that need to have the SOCIAL SECURITY NUMBER (#.09) field updated. It also lists the record number (DFN) in PATIENT (#2) file for the patient associated with the dependent record.

Patch IVM\*2.0\*174 uses this global when processing the Health Level 7 (HL7) ORU-Z10 message from ES to update the SOCIAL SECURITY NUMBER (#.09) field of dependent records in the INCOME PERSON file (#408.13) and to clean them out of the ^XTMP("DG53970P") global. Additionally, a post-install routine extends the expiration date of the ^XTMP("DG53970P") global by an additional 120 days from the patch install date and submits a background job to send a MailMan message every 2 days to report the status of IENs and DFNs remaining in the ^XTMP global. The message is sent to FORUM MailMan group REDACTED. The members of the mail group consist of developers, Software Quality Assurance (SQA), and Health Product Support. A copy of the mail message will be sent to the installer of patch IVM\*2.0\*174.

Once all dependent records identified in the ^XTMP("DG53970P") global have had the SOCIAL SECURITY NUMBER (#.09) field of the INCOME PERSON file (#408.13) successfully updated, the background job will no longer be automatically queued to check the global and send a status message.

Patch EAS\*1.0\*172 was created for a modified routine ^EASCM that uses a new variable to flag the ORU-Z10 as not needing further processing after a SSN fix.

List of Updates

Patch IVM\*2.0\*174 modifies the processing of the HL7 ORU-Z10 message from ES as follows:

1.  If the Patient record from the ORU-Z10 PID segment is found in the ^XTMP("DG53970P") global, only the ZDP segments in the message are processed as follows:
    1.  The dependent record (Internal Entry Number) from the INCOME PERSON file (#408.13) is derived from the ZDP segment. If that record is found in the ^XTMP("DG53970P") global, the SSN from the ZDP segment is filed into the INCOME PERSON file (#408.13) for that dependent.
    2.  The SSN will be validated prior to filing and will not be filed if it is invalid. The SSN must be 9 numbers.
    3.  If the ZDP segment includes a PSEUDO SSN REASON and it is a valid value of "S", "N", or "R", it is stored in the INCOME PERSON file (#408.13) in the PSEUDO SSN REASON field (#.1) and a "P" is appended to the SSN prior to being filed.
    4.  Prior to the SSN being updated, the SSN field in the INCOME PERSON file (#408.13) is checked and will be corrected if the field is corrupted.
    5.  If the filing of the SSN fails, the error message is placed in the ^XTMP("DG53970P") global.
    6.  If the filing of the SSN is successful, the associated ^XTMP("DG53970P") entry is removed.
2.  If the DFN in the PID segment is not found in ^XTMP("DG53970P") global, the ORU-Z10 message is processed normally.
3.  A post-install routine is run that submits the background task IVM\*2.0\*174 STATUS UPDATE JOB that produces a MailMan message that lists the patient records and associated dependent records from the ^XTMP("DG53970P") global. If there are entries in the ^XTMP("DG53970P") global, this job is submitted to run again in 2 days. The MailMan message lists the following information:
    1.  The total number of patient records and associated dependent records that need to have the SSN field updated.
    2.  Each DFN and the associated dependent IENs in the ^XTMP("DG53970P") that need to have the SSN updated. If an ORU-Z10 message failed to update an SSN for a dependent record, the error is shown with the record.

An example of the MailMan message is shown below.

Example: Post-Install MailMan Message

-------------------------------------------------------------------------

Subj: IVM\*2.0\*174-#500-VHA/ES CLEANUP OF SSNs IN (#408.13) FILE

From: \<POSTMASTER\> In 'IN' basket. Page 1

-------------------------------------------------------------------------

The job completed to check if patient records still exist in the ^XTMP("DG53970P" global and require a push of corrected SSN data from ES via an HL7(ORU-Z10) message.

<u>Job Results:</u>

Facility Name: REDACTED

Station Number: 500

Total patients (ICN/DFN) with dependents not updated: 6

Total dependent (IENs) not updated: 7

Patient ICN/DFN: 5000000001V324625/7171998

Dependent IENs: 2

Patient ICN/DFN: 5000000105V037465/7171999

Dependent IENs: 1

Patient ICN/DFN: 5000000040V317188/7171864

Dependent IENs: 3

> 4

Patient ICN/DFN: 5000000077V373245/7171902

Dependent IENs: 5

Patient ICN/DFN: 5000000101V983844/7171926

Dependent IENs: 14

Patient ICN/DFN: 5000000111V198302/7171934

Dependent IENs: 13

Patch EAS\*1.0\*172 modifies routine ^EASCM, in the subroutine PROC, for the processing of the HL7 ORU-Z10 message from ES to initialize a variable IVMSSNFLAG before calling the code that parses the message. Upon returning from that routine, if the variable is set to "1", the code quits and does not process the message further; otherwise the message is processed normally.

Code block before installation of EAS\*1.0\*172:  
; - check HL7 msg structure for errors  
K HLERR,^TMP(\$J,"IVMCM")  
D ^IVMCMC I \$D(HLERR) K:HLERR="" HLERR Q  
;

Code block after installation of EAS\*1.0\*172:  
; - check HL7 msg structure for errors  
K HLERR,^TMP(\$J,"IVMCM")  
; jam; EAS\*1.0\*172 - set IVMSSNFLAG=0 and quit processing if the flag is set upon return from ^IVMCMC  
; (see ^IVMCMC for what sets this flag)  
N IVMSSNFLAG  
S IVMSSNFLAG=0  
D ^IVMCMC I \$D(HLERR) K:HLERR="" HLERR Q  
I IVMSSNFLAG Q

The following sections provide a summary of the defects and fixes to the existing software for VistA REE with the release of Host File IVM_20_P174.KID, which includes patches IVM\*2.0\*174 and EAS\*1.0\*172.

## Defects and Fixes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Defect: Critical defect \#810016 was logged against the ES 5.3 build. A new build was created to address the defect. Emergency Release ES 5.3.0.07001 implemented code changes to remove a method and method calls that were removing the SSN from the ZDP segment and setting it to an empty string. Dependent Social Security Number (SSN) data at the VistA facilities was corrupted and requires a VistA patch to clean up the database corruption. Upon follow-up with the facilities who reported the original error, additional instances of a slightly different error were being seen after the deployment of the code fix. The expected outcome is that no errors would be seen after the deployment of ES 5.3.0.07001. The error logged in the VistA instances is as follows:

> \$ZE= \<SUBSCRIPT\>IX^DIE1 ^DGPR(408.13,"BS","")

> K ^DGPR(408.13,"BS",\$E(X,6,9),DA)

The error is occurring on the second instance of an inbound financial HL7 transmission (ORU-Z10) for a patient. The root cause was determined to be the data (in this case an empty space) which was filed into the SOCIAL SECURITY NUMBER field (#.09) of the INCOME PERSON file (#408.13). The SSN data in that file was potentially degraded by the initial issue. ES was remediated, the second transmission files the correct data; however, still errors due to the previous value. A third or higher transmission should file without error.

Fix: The processing of the ORU-Z10 message is modified:

1.  If the DFN is found in the global ^XTMP("DG53970P"), which was created by patch DG\*5.3\*970 to capture the records that need to be corrected, then process only the ZDP segments to retrieve and store the dependent SSNs. No other segments or data are processed.
2.  If the SSN update was successful, remove the associated entries from the ^XTMP("DG53970P") global.
3.  If the SSN update was not successful, store the error in the ^XTMP ("DG53970P") global.

Once all facilities have installed this emergency patch IVM\*2.0\*174 by the Compliance date, ES will be sending ORU-Z10 HL7 messages for all veterans that have dependents that needed the SSN updated during non-peak hours.

The post-install routine EP^IVM2174P queues the background task IVM\*2.0\*174 STATUS UPDATE JOB that gathers the DFNs and IENs that are in the ^XTMP("DG53970P") global. These values are listed in an email sent to FORUM MailMan group REDACTED. Members of this mail group will monitor messages received from facilities and coordinate with ES about retransmission of corrected SSN data from ES via an HL7 (ORU-Z10) message. The members of the mail group consist of developers, Software Quality Assurance (SQA), and Health Product Support. A copy of the mail message will be sent to the installer of patch IVM\*2.0\*174. If there are still entries in the global, this task will automatically be resubmitted to run in the background in 2 days.

Once all dependent records identified in the ^XTMP("DG53970P") global have had the SOCIAL SECURITY NUMBER (#.09) field of the INCOME PERSON file (#408.13) successfully updated, the background job will no longer be automatically queued to check the global and send a status message.

Table 1 lists the defects and fixes and corresponding Rational Team Concert (RTC) Change and Configuration Management (CM) numbers included in IVM\*2.0\*174.

<table>
<caption><p><span id="_Toc522886001" class="anchor"></span>Table : Defects and Fixes in IVM_20_P174.KID</p></caption>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th>RTC<br />
CM #</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>832574</td>
<td><p><strong>Defect:</strong> Correct the SSNs that got corrupted by ES transmission of SSN data with spaces.</p>
<p><strong>Fix:</strong> Issue an emergency VistA patch to update the SSNs that were inadvertently updated to spaces.</p></td>
</tr>
<tr class="even">
<td>875690</td>
<td><p><strong>Defect</strong>: Patch IVM*2.0*174 defect - A different variable than HLERR as a flag to quit ORU-Z10 processing is needed.</p>
<p><strong>Fix</strong>: Patch EAS*1.0*172 was created for the modified routine ^EASCM that uses a new variable to flag the ORU-Z10 as not needing further processing after a SSN fix.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc522886001" class="anchor"></span>Table : Defects and Fixes in IVM_20_P174.KID

# Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No known or open issues were identified in this release.

# Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents apply to this release:

<u>Title File Name FTP Mode</u>

Release Notes IVM_2_P174_RN.PDF (binary)

The preferred method is to retrieve files from REDACTED This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI Field Offices:

Hines: REDACTED  
Salt Lake City: REDACTED

Documentation can also be found on the VA Software Documentation Library at:

<http://www.va.gov/vdl/>

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: IVM*2*177 Release Notes

## New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no new features or functions added to VistA REE for IVM\*2.0\*177.

## Enhancements and Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As part of the HL7 messaging from the Enrollment System (ES) to VistA REE, patient demographic information is sent to VistA sites where the patient is known.

Since October 2018, over fifty-one thousand (51,000) Veterans had their addresses updated in ES more than four times. Based on spot checks, most of those updates were due to VistA rejecting valid address updates and sending the old address back to ES as a new address update.

Background Information

Currently, for patients with an active prescription, the Permanent Mailing Address is uploaded to a temporary location for display and manual verification in the DEMOGRAPHICS UPLOAD \[IVM UPLOAD DEM\] option. The demographic data is retained for 14 days. If not reviewed and accepted by a user within that timeframe, the address update is rejected if the patient still has an active prescription on file at the VistA site. The IVM BACKGROUND JOB \[IVM BACKGROUND JOB\] handles the review process. If the address is rejected by a user or if it is not reviewed within 14 days and the patient still has an active prescription, the Permanent Mailing Address on file at the VistA site is sent back to ES with a date/time stamp of the current day. ES processes the Z07 message as a new address update for the patient. As a result, old address updates (instead of the most current addresses) are propagated across the VA enterprise.

New Functionality

With installation of patch IVM\*2.0\*177, the processing of the HL7 ORU-Z05 message from ES is modified to eliminate the check for an active prescription. If an incoming Permanent Mailing Address change is determined to be the most current, the update(s) will be directly uploaded to the PATIENT file (#2). The BAD ADDRESS INDICATOR (#.121) field is no longer considered in determining whether to upload the address.

The IVM UPLOAD DEMOGRAPHIC TOOL should not be used to accept or reject Permanent Mailing Address Updates.

For those records still pending in the IVM UPLOAD DEMOGRAPHIC TOOL at the time the patch is installed, if an address change is rejected via the IVM BACKGROUND JOB, no HL7 message acknowledgment or HL7 ORU-Z07 address update is sent to ES. The existing functionality is retained, which removes the pending address update record from the IVM PATIENT file (#301.5) 14 days after the update was received. Therefore, 14 days after patch IVM\*2.0\*177 is installed, the IVM UPLOAD DEMOGRAPHIC TOOL will no longer display any Permanent Mailing Addresses.

Table 1 shows the enhancements and modifications included in the IVM\*2.0\*177 release as tracked in Rational Team Concert (RTC) Requirements Management (RM).

<table>
<caption><p>Table 1: IVM*2.0*177 Enhancements and Modifications</p></caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>RTC<br />
RM #</strong></th>
<th><strong>Summary</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>958593</td>
<td>CR 636583: Modify Vista REE to automatically commit Permanent Address</td>
</tr>
<tr class="even">
<td>958596</td>
<td>CR 636583: No Permanent Addresses on the IVM Demographic Tool</td>
</tr>
</tbody>
</table>

Table 1: IVM\*2.0\*177 Enhancements and Modifications

List of Updates

Patch IVM\*2.0\*177 makes the following changes to VistA REE:

1.  The processing of the HL7 ORU-Z05 message from ES is modified to eliminate the check for an active prescription and BAD ADDRESS INDICATOR (#.121) so that Permanent Mailing Address fields are automatically uploaded to the PATIENT file (#2) if the change date/time is more recent than what is in the PATIENT file (#2). The Permanent Mailing Address fields that are loaded are as follows:
    1.  ADDRESS CHANGE DT/TM (#.118)
    2.  ADDRESS CHANGE SITE (#.12)
    3.  ADDRESS CHANGE SOURCE (#.119)
    4.  CITY (#.114)
    5.  COUNTY (#.117)
    6.  COUNTRY (#.1173)
    7.  POSTAL CODE (#.1172) (zip code)
    8.  PROVINCE (#.1171)
    9.  STATE (#.115)
    10. STREET ADDRESS \[LINE 1\] (#.111)
    11. STREET ADDRESS \[LINE 2\] (#.112)
    12. STREET ADDRESS \[LINE 3\] (#.113)
    13. STREET ADDRESS CASS INDICATOR (#.1118)
    14. BAD ADDRESS INDICATOR (#.121)
2.  The IVM Background Job \[IVM BACKGROUND JOB\] option is modified to no longer trigger an ORU-Z07 message to ES after a pending address update is rejected due to the 14-day expiration. Per existing functionality, the pending address update is removed from the IVM PATIENT file (#301.5) after the 14-day expiration. Therefore, 14 days after Patch IVM\*2.0\*177 is installed, the IVM UPLOAD DEMOGRAPHIC TOOL will no longer display any Permanent Mailing Addresses.
