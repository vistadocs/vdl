---
title: "Laboratory: Universal Interface AutoRelease  Version 1 Technical Manual"
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: LA
app_name: "Laboratory: Universal Interface"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 1
patch_id: 
group_key: "LA::1"
file_numbers: []
security_keys: []
menu_options: 8
description: The VistA Laboratory Enhancement (VLE), AutoVerification initiative, is a natural extension of Kansas City (KC) Veterans Affairs Medical Center (VAMC) Innovation Award. This Office of Information & Technology (OI&T) effort both insures the original code conforms to National Release requirements and
audience: 
keywords: 
  - class
  - table
  - autoverification
  - laboratory
  - span
  - results
  - interface
  - contents
  - colspan
  - auto
page_count: 0
word_count: 6985
section_count: 13
table_count: 7
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 7
revision_newest: 11/1/2016
revision_oldest: 05/25/2016
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/labautorelease1_0_technicalmanual.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/labautorelease1_0_technicalmanual.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=120"
---

Auto Verification: VistA Auto ReleaseVistA Laboratory Enhancements Project

LR\*5.2\*458 & LA\*5.2\*88 Patches &

Warranty Release: LA\*5.2\*94 & LR\*5.2\*475

Technical Manual  
and  
Security Guide

![](laboratory-universal-interface-autorelease-version-1-technical-manual/001.png)

Department of Veterans AffairsNovember 2016

Revision History

| Date       | Version | Description                                                                                                                                                          | Author                             |
|------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| 11/1/2016  | 1.4     | Added Warranty Release information for LA\*5.2\*94 & LR\*5.2\*475                                                                                                    | <span class="mark">REDACTED</span> |
| 06/30/2016 | 1.3     | Changed Checksum of routine LRVRAR due to the addition of comments.                                                                                                  | <span class="mark">REDACTED</span> |
| 06/22/2016 | 1.2     | Incorporated changes from <span class="mark">REDACTED</span> Section Documentation Updates: changes made to Lab UI HL V1.6 Upgrade documents from Patch LA\*5.2\*66. | <span class="mark">REDACTED</span> |
| 06/21/2016 | 1.1     | Incorporated changes <span class="mark">REDACTED</span>                                                                                                              | <span class="mark">REDACTED</span> |
| 06/13/2016 | 1.0     | Final peer review: minor formatting changes and footer edits.                                                                                                        | <span class="mark">REDACTED</span> |
| 6/13/2016  | 0.9     | Incorporated peer review comments from development team.                                                                                                             | <span class="mark">REDACTED</span> |
| 05/25/2016 | 0.1     | Draft initiated                                                                                                                                                      | <span class="mark">REDACTED</span> |

<span id="_Ref251310381" class="anchor"></span>Table 1 – Text Conventions

Table of Contents

# List of Tables


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [List of Tables](#list-of-tables)
- [ORIENTATION](#orientation)
  - [Text Conventions](#text-conventions)
- [INTRODUCTION](#introduction)
  - [IRM Staff](#irm-staff)
  - [Laboratory Staff](#laboratory-staff)
    - [Acceptance Criteria](#acceptance-criteria)
  - [AutoVerification Test Sites](#autoverification-test-sites)
  - [Database Integration Agreements (DBIA)](#database-integration-agreements-dbia)
  - [AutoVerification Routines](#autoverification-routines)
  - [AutoVerification Namespace](#autoverification-namespace)
  - [AutoVerification Files](#autoverification-files)
  - [AutoVerification Globals](#autoverification-globals)
    - [New Global](#new-global)
    - [Temporary Global](#temporary-global)
  - [AutoVerification Menus, Options and Templates](#autoverification-menus-options-and-templates)
  - [AutoVerification Proxy Users](#autoverification-proxy-users)
  - [AutoVerification Bulletins](#autoverification-bulletins)
    - [AutoVerification Parameters](#autoverification-parameters)
    - [AutoVerification Reports Menu](#autoverification-reports-menu)
    - [Report Tasking Options](#report-tasking-options)
    - [Documentation Updates](#documentation-updates)
- [Security Introduction](#security-introduction)
- [Security Keys](#security-keys)

# ORIENTATION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Text Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout this document, the following fonts and other text conventions are used:

| Font                       | Used for…                             | Examples:                                                                                                                                          |
|--------------------------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Blue text, underlined          | Hyperlink to another document or URL      | “For further instructions on using KIDS, please refer to the [*Kernel Version 8.0 Systems Manual*](http://www.hardhats.org/kernel/docs/KRN8_0SM.PDF).” |
| Green text, dotted underlining | Hyperlink within this document            | “MRSA-PT contains reports that will extract and consolidate required data for entry into the [Inpatient Evaluation Center](#Glos_IPEC) (IPEC).”        |
| Arial                          | Text inside tables                        | (This table)                                                                                                                                           |
| Courier New                    | Menu options                              | MRSA Tools Parameter Setup                                                                                                                             |
|                                | Screen prompts                            | Want KIDS to INHIBIT LOGONs during the install? YES//                                                                                                  |
|                                | Patch names                               | MMMS\*1.0\*1                                                                                                                                           |
|                                | VistA filenames                           | XYZ file \#798.1                                                                                                                                       |
|                                | VistA field names                         | “In the Indicator field, enter the logic that is to be used to determine if the test was positive for the selected MDRO.”                              |
| Courier New, bold              | User responses to screen prompts          | NO                                                                                                                                                 |
| Franklin Gothic Demi           | Keyboard keys                             | \< F1 \>, \< Alt \>, \< L \>, \<Tab\>, \<Enter\>                                                                                                       |
| Microsoft Sans Serif           | Software Application names                | MRSA Program Tools                                                                                                                                     |
|                                | Report names                              | Procedures report                                                                                                                                      |
| Times New Roman                | Body text (Normal text)                   | “There are no changes in the performance of the system once the installation process is complete.”                                                     |
| Times New Roman Italic         | Text emphasis                             | “It is *very* important…”                                                                                                                              |
|                                | National and International Standard names | *International Statistical Classification of Diseases and Related Health Problems*                                                                     |
|                                | Document names                            | *MRSA Program Tools Technical Manual & Security Guide*                                                                                                 |

<span id="_Ref251310415" class="anchor"></span>Table 2 – AutoVerification Test Sites

# INTRODUCTION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Laboratory Enhancement (VLE), AutoVerification initiative, is a natural extension of Kansas City (KC) Veterans Affairs Medical Center (VAMC) Innovation Award. This Office of Information & Technology (OI&T) effort both insures the original code conforms to National Release requirements and incorporates additional requested enhancements. The code patches, which give VistA the capability to automatically release verified laboratory results without human intervention, was tested at five Initial Operating Capability (IOC) test sites: KC, Tucson, Fresno, Tampa, and Iowa City. While architected to use with any third party, vendor agnostic Generic Interface Manager (GIM), the Data Innovation’s Instrument Manager was tested with this solution since it is already in production use at the majority of the Veterans Health Administration’s (VHA) medical facilities. For the AutoVerification effort, a new contract was awarded to Data Innovations (DI) to provide software and guidance for rules creation and configuration for up to four instruments or analyzers at each Initial Operating Capability (IOC) test site. In accordance with regulatory guidelines, each site tested and documented the rule sets they selected and created or customized.

KC VAMC achieved over 90% AutoVerification rate on those tests selected for AutoVerification (besting the goal of 70%). This means a reduction in STAT TAT (Turn Around Time) performance, reduction in the amount of time a Laboratory Technologist/Technician is required to release reports and print reports (both supporting Cost Containment Executive Orders), reduction in data entry errors, and a measureable increase in employee satisfaction.

<span id="_Toc454348879" class="anchor"></span>About the AutoVerification Enhancement

AutoVerification is the…

- Use of algorithms, or set of rules, to make decisions about safety and reliability of results coming off an instrument and posting them to the patient’s chart without human intervention.
- Algorithms are based on decision trees a technologist would normally use to assess a result and make a decision to post the result into the patient’s chart. The algorithm is executed by computer software and the need for human intervention decreases.
- Algorithms can incorporate instrument Quality Control (QC), moving averages, critical values, specimen characteristics (hemolysis, lipemia, icteric), reference ranges and patient history into its decision making process.
- Since the software puts every result through the same rigorous decision making process the results are evidence based, consistent and reliable.

Currently, results are all manually verified by a technologist using the VistA Legacy Laboratory system. However, more and more facilities are using class III software to implement AutoVerification systems. This Technical Manual focuses on the modifications to the VistA Legacy Laboratory system in order to support a Class I software solution to support the receiving, processing, and storing of results verified prior to coming to the VistA system.

<span id="_Toc454348880" class="anchor"></span>Intended Audience

## IRM Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRM staff is required for:

- Installation of two patches: LA\*5.2\*88 and LR\*5.2\*458
- <span class="mark">Installation of warranty patches: LA\*5.2\*94 & LR\*5.2\*475</span>
- Assigning menu and [Security Keys](#Glos_Sec_Key) (e.g. pre-existing key: LRVERIFY)

## Laboratory Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is *highly recommended* that the Laboratory Information Manager (LIM), and a representative from the Laboratory section (director, supervisor, or technologist) *jointly* participate in reviewing the parameter set-up for enabling when to use the AutoVerification system with the VistA Auto Release Capability. This group may also wish to review the same acceptance criteria that were established for the test sites to ensure a better understanding of the capabilities of the Auto/Verification enhancement.

### Acceptance Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AutoVerification uses Decision Support Algorithms or rule sets to automatically review laboratory results and directly post “normal” results to the patient’s chart. Results that are deemed “abnormal” by the rule set will be reviewed by laboratory personnel before being manually released into the patient’s electronic health record (EHR).

Specifically in VistA:

1.  *VistA Laboratory receives autoverified results from external system:* Receiving an indication of when a test has been successfully autoverified.
    - Acceptance Criteria:
      - Results received from AutoVerification system contain an indication that the result is ‘AutoVerified’.
      - VistA stores the indicator received from the AutoVerification system with the result.
      - VistA stores the original message transmission for a period of time, as per current VistA capabilities, for troubleshooting purposes.
2.  *VistA Laboratory automatically releases Autoverified Results:* Processing test results, with an indicator of successful AutoVerification, to Auto Release, making results available to appropriate clinicians and providers with privileges to view the results.
    - Acceptance Criteria:
      - Results received from AutoVerification system that are identified as ‘AutoVerified’ will be automatically released and visible to the clinicians authorized to view the results (as per current VistA/CPRS capabilities) for the patient.
      - Clinicians with appropriate authorization will immediately be able to view the patient’s AutoVerified results via CPRS.
3.  *VistA Laboratory receives verified results from external system:* Receiving an indication of when a test has been successfully verified by an authorized technologist.
    - Acceptance Criteria:
      - Results received from AutoVerification system contain unique identification of the technologist who ‘Verified’ the result.
      - VistA stores the identification of the technologist received from the AutoVerification system with the result.
      - VistA stores the original message transmission for a period of time, as per current VistA capabilities, for troubleshooting purposes.
4.  *VistA Laboratory automatically releases Tech Verified Results:* Processing test results, with an indicator of successful verification by an authorized technologist, to Auto Release, making results available to appropriate clinicians and providers with privileges to view the results.
    - Acceptance Criteria:
      - Results received from AutoVerification system, that are identified as ‘Verified’ will be automatically released and visible to the clinicians authorized to view the results (as per current VistA/CPRS capabilities) for the patient.
      - Clinicians with appropriate authorization will immediately be able to view the patient’s verified results via CPRS.
5.  *VistA Laboratory sends enhanced Order Messages with Provider Contact Information:* Sending ordering provider contact information to the instrument middleware for the purpose of making it accessible to authorized technologists who are responsible for verifying test results.
    - Acceptance Criteria:
      - VistA Laboratory system will include the provider’s pager and phone number available from New Person File \#200, prior to the technologist initiating the results verification process.
      - VistA stores the original message transmission for a period of time, as per current VistA capabilities, for troubleshooting purposes.
6.  *VistA Laboratory Auto Release Patches Operate with AutoVerification System:* The VistA Auto Release Patches work with the AutoVerification system, instrument middleware, for the purpose of implementing a full end to end AutoVerification solution.
    - Acceptance Criteria:
      - VistA patches are installed and meet acceptance criteria 1-5 above.
      - VistA patches are operating with the DI AutoVerification system.

## AutoVerification Test Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 2 displays the sites that assisted in testing AutoVerification prior to the release date.

<table>
<caption><p><span id="_Toc454348863" class="anchor"></span>Table – Approved Database Integration Agreements</p></caption>
<colgroup>
<col style="width: 69%" />
<col style="width: 13%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Test Site</strong></th>
<th><p><strong>Type of</strong></p>
<p><strong>Test Site</strong></p></th>
<th><strong>Date Installed</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td>Alpha</td>
<td>11/16/2015</td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td>Beta</td>
<td>12/8/2015</td>
</tr>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td>Beta</td>
<td>12/14/2015</td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td>Beta</td>
<td>11/30/2015</td>
</tr>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td>Beta</td>
<td>12/22/2015</td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td><mark>Warranty</mark></td>
<td></td>
</tr>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td><mark>Warranty</mark></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc454348863" class="anchor"></span>Table – Approved Database Integration Agreements

## Database Integration Agreements (DBIA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is one database integration agreement (DBIA) approved for AutoVerification. The following table lists the approved DBIA.

| File                                                             | Access | DBIA | Comment |
|------------------------------------------------------------------|--------|------|---------|
| Application proxies – LRLAB, AUTO RELEASE and LRLAB, AUTO VERIFY | N/A    | 4677 |         |

<span id="_Toc249158675" class="anchor"></span>Table 4 – AutoVerification Routines

## AutoVerification Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists the M routines included in KIDS build LAB_AUTORELEASE_1_0.KID (checksums were generated using the CHECK1^XTSUMBLD).

<table>
<caption><p><span id="_Toc249158676" class="anchor"></span>Table – AutoVerification Files</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 62%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th>Routine</th>
<th>Routine Description</th>
<th>Checksum</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>LA7UCFG</td>
<td><p>Allows configuring Lab Universal Interface entries (LA7UI*) in LA7 MESSAGE PARAMETER file (#62.48) and corresponding entries in AUTO INSTRUMENT file (#62.4) which use the Lab Universal Interface.</p>
<p><mark>Warranty Fix: modifies LA7UCFG at ENKEY+14 to add '*' to the variables being</mark></p>
<p><mark>passed to Taskman:</mark></p>
<p>S ZTSAVE("LRKEY*")="",ZTSAVE("LRUSER*")=""</p></td>
<td><p>Old_B137316017</p>
<p><mark>New_B137340339</mark></p></td>
</tr>
<tr class="even">
<td>LA7UCFG1</td>
<td>Check added to Lab UI Configuration Report to warn if the performing lab specified for the associated load list has not been assigned as a division to the LRLAB, AUTO RELEASE proxy.</td>
<td>B29526912</td>
</tr>
<tr class="odd">
<td>LA7UIO1</td>
<td>This routine builds the ORM Order message for the Laboratory Universal Interface. It was modified to include ordering provider contact information. Check added to see if Lab Universal Interface has been upgraded from HL7 V2.2 protocol to HL7 v2.5.1 protocol.</td>
<td>B75417661</td>
</tr>
<tr class="even">
<td>LA7UTILB</td>
<td>Checks for Auto Release needing to be restarted and asks user if they want the AR processes for selected enabled Load/Work lists to be queued for processing. Called by option Reprocess Lab HL7 Messages [LA7 REPROCESS HL7 MESSAGES].</td>
<td>B23365722</td>
</tr>
<tr class="odd">
<td>LA7VHL</td>
<td>Include receiving application and receiving facility to ORU message ACK. (From v6 updates)</td>
<td>B38289473</td>
</tr>
<tr class="even">
<td>LA7VHLU8</td>
<td><p>This routine does the constructing of the ordering provider contact information as an HL7 XTN data type.</p>
<p>Include error info in ERR segment of ACK.</p></td>
<td>B60447079</td>
</tr>
<tr class="odd">
<td>LA7VHLU9</td>
<td>This routine does the constructing of the ordering provider contact information as an HL7 XTN data type.</td>
<td>B33364706</td>
</tr>
<tr class="even">
<td>LA7VIN</td>
<td>Modified VistA Laboratory routine LA7VIN to support Auto Release. Added: If universal interface and auto-release turned on then task job(s) to process results in LAH.</td>
<td>B31997123</td>
</tr>
<tr class="odd">
<td>LA7VIN1</td>
<td>Triggers the building of the enhanced acknowledgement message. Builds ERR segment and includes additional information in acknowledgement for Lab Universal Interface related message – patient name, patient identifier, specimen identifier and generic error message if specific error message is not specified.</td>
<td>B65233143</td>
</tr>
<tr class="even">
<td>LA7VIN2</td>
<td>Extract MSH-15 (Accept acknowledgement type) and MSH-16 (Application acknowledgement type) from incoming HL7 message’s MSH segment.</td>
<td>B46992282</td>
</tr>
<tr class="odd">
<td>LA7VIN2A</td>
<td>Check if results are to be auto released then comments (NTE segment) are also to be stored.</td>
<td>B34119950</td>
</tr>
<tr class="even">
<td>LA7VIN4</td>
<td>Check OBR-24 for auto release indicator (AR) and use to process associated results through auto release process.</td>
<td>B81803911</td>
</tr>
<tr class="odd">
<td>LA7VIN4A</td>
<td><p>To identify inbound messages from the Universal Interface that are to be Auto Released and set flag to create new entry in LAH global and not overlay existing entry on same accession.</p>
<p>This routine is a continuation of LA7VIN4 and is only called from there.</p></td>
<td>B23154184</td>
</tr>
<tr class="even">
<td>LA7VIN5</td>
<td><p>Set flag when extracting test results to submit results to auto release process when processing message complete.</p>
<p>Any error encountered when processing ORU messages from DI will be returned in the application ack.</p></td>
<td>B85555425</td>
</tr>
<tr class="odd">
<td>LA7VIN5A</td>
<td>Store units, normals and abnormal flags associated with results when results are flagged for auto release.</td>
<td>B34608326</td>
</tr>
<tr class="even">
<td>LA7VORC</td>
<td>Modified to build ORC-14 sequence - Order Callback Phone Number with the ordering provider contact information.</td>
<td>B22779822</td>
</tr>
<tr class="odd">
<td>LA88</td>
<td><p>KIDS patch pre-install routine. Deleted by KIDS after successful patch installation.</p>
<p>Add prompts to insure site has upgraded COTS to send HL7 v2.5.1 in MSH segments.  Code added to update Lab UI protocols to HL7 v2.5.1.</p></td>
<td>B37005513</td>
</tr>
<tr class="even">
<td>LA88A</td>
<td><p>New routine;</p>
<p>The pre-install questions pertaining to updating LAB UI 1.6 to HL7 2.5.1 were moved from the pre-install routine (and defined install questions portion of the KID build) to the Environment check routine. This enables an aborted install to be restarted using the Install Package option.</p></td>
<td>B100793409</td>
</tr>
<tr class="odd">
<td>LRDIQ</td>
<td><p>Added displaying on Summary list report field</p>
<p>PERFORMED/RELEASED ON... Also changed display so multiple tests aren’t run together on the same line. (From v9 updates). Provide tracking information to LIM/supervisors when reviewing auto released results.</p></td>
<td>B6385366</td>
</tr>
<tr class="even">
<td>LRGP2</td>
<td>Check for auto release process when building test list during release.</td>
<td>B21346835</td>
</tr>
<tr class="odd">
<td>LRLISTPS</td>
<td>New routine/option Summary List (Patient) [LRLISTPS] to provide LIM/supervisors ability to review details of individual patients’ auto released testing results.</td>
<td>B17691343</td>
</tr>
<tr class="even">
<td>LRNIGHT</td>
<td>Include task to purge old instrument data from ^LAH global during Nightly Lab Cleanup.</td>
<td>B7575682</td>
</tr>
<tr class="odd">
<td>LRVER5</td>
<td><p>Logic added to always use the previously stored units/reference range of verified (unmodified) results when manually modifying data (i.e. Comments) (From v6 updates)</p>
<p>Flag indicating the units/normal/delta checks to be stored with a test not being set properly for Lab Group Verify resulting in delta checks not being executed and units/normal not being stored with results.</p></td>
<td>B148324560</td>
</tr>
<tr class="even">
<td>LRVR3</td>
<td>Entry point for task to clean up ^LAH global from Nightly Lab Cleanup.</td>
<td>B108418700</td>
</tr>
<tr class="odd">
<td>LRVRAR</td>
<td><p>New routine, main routine that performs the actual auto release of test results that have been flagged as auto verified or tech verified on the laboratory middleware.</p>
<p><mark>Warranty Fix: adds functionality to store Lab Test (#60) configuration data which doesn't come from the middleware for verified results. This will allow the user to edit previously auto-released results using the normal VistA Lab EM/EA options utilizing the configuration values used at the time of original verification.</mark></p></td>
<td><p>Old_B69815158</p>
<p><mark>New_B71328911</mark></p></td>
</tr>
<tr class="even">
<td>LRVRARU</td>
<td>New routine that provides utility functions to the auto release process routine LRVRAR. To do the auto releasing will be in the LRVRAR* namespace to keep the actual verifying in the automated results LRVR namespace, AR for Auto Release functionality.</td>
<td>B32878283</td>
</tr>
</tbody>
</table>

<span id="_Toc249158676" class="anchor"></span>Table – AutoVerification Files

## AutoVerification Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AutoVerification uses the LA and LR [namespace](#Glos_Namespace).

## AutoVerification Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists the files that are exported with the AutoVerification software.

| File Name (Number)                  | Description                         | Remarks                                                                                                                                                                                       |
|-------------------------------------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LOAD/WORK LIST (#68.2)              | PROFILE (#68.23),                   | New entry for AUTO RELEASE                                                                                                                                                                    |
|                                     | DEFAULT REFERENCE LABORATORY (#2.3) | Should be set to the Institution that should be used as the performing and releasing lab for results released via the auto release process                                                    |
|                                     | AUTORELEASE (#2.4)                  | The Auto Release field (#2.4) in the Load/Work List file (#68.2) is used to mark a profile as being used by the auto release process. There should only be one profile flagged per load list. |
| AUTO INSTRUMENT (#62.4)             | New field: AUTO RELEASE (#99)       | Enables Auto Release on an instrument basis, which allows for different levels of granularity                                                                                                 |
| LA7 MESSAGE LOG BULLETINS (#62.485) | New entries                         | See AutoVerification Bulletin section for details.                                                                                                                                            |

<span id="_Toc454348866" class="anchor"></span>Table – AutoVerification Parameters

## AutoVerification Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no new globals.

### Temporary Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AutoVerification uses the pre-existing ^TMP global during report generation to store data needed to compile the reports.

## AutoVerification Menus, Options and Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AutoVerification comes with the following:

- The new Summary List (Patient) Option \[LRLISTPS\]
- Minor changes to the Lab Universal Setup Option \[LA7 UI SETUP\]
- The modified input template \[LRLLDFT\]

## AutoVerification Proxy Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AutoVerification adds two new application proxy users:

- LRLAB, AUTO RELEASE is used to indicate that the results in VistA Lab were released by an automated Lab process without human interventions.
- LRLAB, AUTO VERIFY is used to indicate that the results were "approved" by an automated process using a rules based system.

Local site personnel should assign DIVISIONS to the new proxy users, LRLAB, AUTO RELEASE and LRLAB, AUTO VERIFY that corresponds to the performing laboratories that will utilize the auto release process.

## AutoVerification Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are new entries in the file LA7 MESSAGE LOG BULLETINS (#62.485):

CODE: 301 TEXT: Msg \#\|1\|, User \|2\| \[DUZ: \|3\|\] does not own the LRVERIFY security key. Auto Release not allowed for accession UID \|4\|. SEND ALERT: YES

CODE: 302 TEXT: Msg \#\|1\|, User \|2\| \[DUZ: \|3\|\] is not an active user on the system. Auto Release not allowed for accession UID \|4\|. SEND ALERT: YES

CODE: 303 TEXT: Msg \#\|1\|, No verifying user or application proxy found. Auto Release not allowed for accession UID \|2\|. SEND ALERT: YES

CODE: 304 TEXT: Msg \#\|1\|, User \|2\| \[DUZ: \|3\|\] is not a valid user to verify results. Auto Release not allowed for accession UID \|4\|. SEND ALERT: YES

CODE: 305 TEXT: Msg \#\|1\|, User \|2\| \[DUZ: \|3\|\] is not allowed to verify. Only auto verification enabled for this instrument. Auto Release not allowed for accession UID \|4\|. SEND ALERT: YES

CODE: 306 TEXT: Msg \#\|1\|, User \|2\| \[DUZ: \|3\|\] is not allowed to verify. Only tech verification enabled for this instrument. Auto Release not allowed for accession UID \|4\|. SEND ALERT: YES

CODE: 307 TEXT: Msg \#\|1\|, Auto Release not allowed for accession UID \|2\|. Results have previously been released. SEND ALERT: YES

### AutoVerification Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AutoVerification uses the parameters listed in the table below.

<table>
<caption><p><span id="_Toc454348867" class="anchor"></span>Table – Reports Menu Options</p></caption>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Purpose/Remarks</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Auto Release Results System Wide [LA UI AUTO RELEASE MASTER]</td>
<td><p>NAME: LA UI AUTO RELEASE MASTER</p>
<p>DISPLAY TEXT: Auto Release Results System Wide</p>
<p>MULTIPLE VALUED: No</p>
<p>VALUE TERM: AUTO RELEASE RESULTS SYSTEM WIDE</p>
<p>VALUE DATA TYPE: set of codes</p>
<p>VALUE DOMAIN: 0:NO (DISABLED);1:YES (ENABLED)</p>
<p>VALUE HELP: Do you want to Auto Release Results System Wide?</p>
<p>DESCRIPTION:</p>
<p>This parameter is used to determine whether lab results are sent to the auto release process.</p>
<p>PRECEDENCE: 1 ENTITY FILE: SYSTEM</p>
<p>PRECEDENCE: 10 ENTITY FILE: PACKAGE</p></td>
</tr>
<tr class="even">
<td>Lab Ordering Provider Contact Info [LA UI PROVIDER CONTACT INFO]</td>
<td><p>NAME: LA UI PROVIDER CONTACT INFO</p>
<p>DISPLAY TEXT: Lab Ordering Provider Contact Info</p>
<p>MULTIPLE VALUED: Yes</p>
<p>INSTANCE TERM: Sequence</p>
<p>VALUE TERM: Type of Phone Contact</p>
<p>VALUE DATA TYPE: set of codes</p>
<p>VALUE DOMAIN: 1:PHONE (HOME);2:OFFICE PHONE;3:PHONE #3;4:PHONE #4;5:COMMERICAL;6:FAX;7:VOICE PAGER;8:DIGITAL PAGER</p>
<p>VALUE HELP: Specify which method to use to contact the ordering provider.</p>
<p>INSTANCE DATA TYPE: numeric</p>
<p>INSTANCE DOMAIN: 1:8:0</p>
<p>INSTANCE HELP: Enter the sequence for the contact info.</p>
<p>DESCRIPTION: Contains the list of which contact info for the ordering provider to send in a Lab HL7 Order message from the user's corresponding entry in NEW PERSON file (#200). It can be specified at the system or the individual user level. If specified at the user level it takes precedence and overrides the setting at the system level allowing specific users to have their own specific set of contacts to send. The sequence specifies the order and info to check, maximum of 6 allowed. Only the first 2 with a value will be placed in the message as the HL7 Standard constrains the number of repetitions for this information at 2. The value specifies which field from the person's entry in NEW PERSON file (#200) to send in the message.</p>
<p>These are the fields currently available.</p>
<p>Field # Field Name Description</p>
<p>.131 PHONE (HOME) This is the telephone number for the new person.</p>
<p>.132 OFFICE PHONE This is the business/office telephone for the new person.</p>
<p>.133 PHONE #3 This is an alternate telephone number where the new person might also be reached.</p>
<p>.134 PHONE #4 This is another alternate telephone number where the new person might also be reached.</p>
<p>.135 COMMERCIAL PHONE This is a commercial phone number.</p>
<p>.136 FAX NUMBER This field holds a phone number for a FAX machine for this user. It needs to be a format that can be understood by a sending MODEM.</p>
<p>.137 VOICE PAGER This field holds a phone number for an ANALOG PAGER that this person carries with them.</p>
<p>.138 DIGITAL PAGER This field holds a phone number for a DIGITAL PAGER that this person carries with them.</p>
<p>The parameter is distributed pre-configured at the package level as follows:</p>
<p>Sequence Value</p>
<p>-------- -----</p>
<p>1 OFFICE PHONE</p>
<p>2 DIGITAL PAGER</p>
<p>3 VOICE PAGER</p>
<p>4 PHONE #3</p>
<p>5 PHONE #4</p>
<p>6 PHONE (HOME)</p>
<p>7 COMMERICAL PHONE</p>
<p>8 FAX NUMBER</p>
<p>PRECEDENCE: 1 ENTITY FILE: USER</p>
<p>PRECEDENCE: 2 ENTITY FILE: SYSTEM</p>
<p>PRECEDENCE: 3 ENTITY FILE: PACKAGE</p></td>
</tr>
<tr class="odd">
<td>Days to keep of instrument data [LR WORKLIST DATA CLEANUP]</td>
<td><p>NAME: LR WORKLIST DATA CLEANUP DISPLAY TEXT: Days to keep of instrument data</p>
<p>MULTIPLE VALUED: Yes</p>
<p>INSTANCE TERM: LOAD/WORK LIST</p>
<p>VALUE TERM: Number of days to keep in LAH global</p>
<p>PROHIBIT EDITING: No</p>
<p>VALUE DATA TYPE: numeric</p>
<p>VALUE DOMAIN: 0:365:0</p>
<p>VALUE HELP: Answer with the number of days to keep in LAH before automatic purge</p>
<p>INSTANCE DATA TYPE: pointer</p>
<p>INSTANCE DOMAIN: 68.2</p>
<p>DESCRIPTION: Allows site to specify the number of days of instrument data to keep in LAH global before it's automatically purged by nightly process.</p>
<p>PRECEDENCE: 10</p>
<p>ENTITY FILE: PACKAGE</p></td>
</tr>
<tr class="even">
<td>Lab Package Level Parameters [LR PKG]</td>
<td><p>NAME: LR PKG</p>
<p>DISPLAY TEXT: Lab Package Level Parameters</p>
<p>USE ENTITY FROM: PACKAGE</p>
<p>SEQUENCE: 1</p>
<p>PARAMETER: LR COLLECT MONDAY</p>
<p>SEQUENCE: 2</p>
<p>PARAMETER: LR COLLECT TUESDAY</p>
<p>SEQUENCE: 3</p>
<p>PARAMETER: LR COLLECT WEDNESDAY</p>
<p>SEQUENCE: 4</p>
<p>PARAMETER: LR COLLECT THURSDAY</p>
<p>SEQUENCE: 5</p>
<p>PARAMETER: LR COLLECT FRIDAY</p>
<p>SEQUENCE: 6</p>
<p>PARAMETER: LR COLLECT SATURDAY</p>
<p>SEQUENCE: 7</p>
<p>PARAMETER: LR COLLECT SUNDAY</p>
<p>SEQUENCE: 8</p>
<p>PARAMETER: LR IGNORE HOLIDAYS</p>
<p>SEQUENCE: 11</p>
<p>PARAMETER: LR EGFR METHOD</p>
<p>SEQUENCE: 12</p>
<p>PARAMETER: LR EGFR AGE CUTOFF</p>
<p>SEQUENCE: 13</p>
<p>PARAMETER: LR EGFR RESULT SUPPRESS</p>
<p>SEQUENCE: 9.2</p>
<p>PARAMETER: LR VER EA VERIFY BY UID</p>
<p>SEQUENCE: 9.1</p>
<p>PARAMETER: LR VER EM VERIFY BY UID</p>
<p>SEQUENCE: 20</p>
<p>PARAMETER: LRAPRES1 AP ALERT</p>
<p>SEQUENCE: 21</p>
<p>PARAMETER: LR AP REPORT SELECTION</p>
<p>SEQUENCE: 24</p>
<p>PARAMETER: LR AP SNOMED SYSTEM PRINT</p>
<p>SEQUENCE: 50</p>
<p>PARAMETER: LR CH GUI REPORT RIGHT MARGIN</p>
<p>SEQUENCE: 52</p>
<p>PARAMETER: LR MI GUI REPORT RIGHT MARGIN</p>
<p>SEQUENCE: 54</p>
<p>PARAMETER: LR AP GUI REPORT RIGHT MARGIN</p>
<p>SEQUENCE: 9.3</p>
<p>PARAMETER: LR MI VERIFY DISPLAY PROVIDER</p>
<p>SEQUENCE: 130.1</p>
<p>PARAMETER: LR ACCESSION DEFAULT SPECIMEN</p>
<p>SEQUENCE: 130.2</p>
<p>PARAMETER: LR ACCESSION DEFAULT COL SAMP</p>
<p>SEQUENCE: 130.3 PARAMETER: LR ACCESSION DEFAULT LAB TEST</p>
<p>SEQUENCE: 25 PARAMETER: LR AP SURGERY REFERENCE</p>
<p>SEQUENCE: 9.35 PARAMETER: LR MI VERIFY CPRS ALERT</p>
<p>SEQUENCE: 9.36</p>
<p>PARAMETER: LR CH VERIFY CPRS ALERT</p>
<p>SEQUENCE: 8.1</p>
<p>PARAMETER: LR LAB COLLECT FUTURE</p>
<p>SEQUENCE: 8.11</p>
<p>PARAMETER: LR MAX DAYS CONTINUOUS</p>
<p>SEQUENCE: 200</p>
<p>PARAMETER: LR REPORTS FACILITY PRINT</p>
<p>SEQUENCE: 900</p>
<p>PARAMETER: LR MAPPING DEFAULT DIRECTORY</p>
<p>SEQUENCE: 900.1</p>
<p>PARAMETER: LR MAPPING DEFAULT FILESPEC</p>
<p>SEQUENCE: 22</p>
<p>PARAMETER: LR ASK PERFORMING LAB AP</p>
<p>SEQUENCE: 23</p>
<p>PARAMETER: LR ASK PERFORMING LAB MICRO</p>
<p>SEQUENCE: 150.1</p>
<p>PARAMETER: LR MANIFEST EXC PREV TEST</p>
<p>SEQUENCE: 150.2</p>
<p>PARAMETER: LR MANIFEST DEFLT ACCESSION</p>
<p>SEQUENCE: 120</p>
<p>PARAMETER: LR AP DEFAULT ACCESSION NUMBER</p>
<p>SEQUENCE: 210</p>
<p>PARAMETER: LR WORKLIST DATA CLEANUP</p></td>
</tr>
</tbody>
</table>

<span id="_Toc454348867" class="anchor"></span>Table – Reports Menu Options

### AutoVerification Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table listed the new option.

| Option                                                                   |                                     | Purpose/Remarks                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| New option was added to the Supervisor reports \[LRSUPER REPORTS\] menu. | Summary List (Patient) \[LRLISTPS\] | Description: All results for a given patient for a given area for a given date. This report can serve as an 'audit trail' for a patient. Includes information on person placing order, person performing test, verifying person, and dates and times of specimen collection and test completion. The report can be printed in an "extended" form, which includes the above mentioned information plus the test results and associated units/normals/LOINC coding and performing lab. |

<span id="_Toc454348868" class="anchor"></span>Table – Report Tasking Options

### Report Tasking Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no options used to task reports.

| Option |     | Used To… |
|--------|-----|----------|
| none   |     |          |

### Documentation Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents have been updated as a result of the enhancements made for AutoVerification. These are available at SOFTWARE.DIR and the VistA Documentation Library (VDL) website as a secondary source.

- Lab UI HL V1.6 Upgrade Interface Specifications Document
- LR\*5.2\*458 and LA\*5.2\*88-Universal Interface-Release Notes
- LR\*5.2\*458 and LA\*5.2\*88(Lab AutoRelease 1.0) User Guide
- LR\*5.2\*458 and LA\*5.2\*88(Lab AutoRelease 1.0) Technical Manual/Security  Guide

Reference material for Lab Universal Interface 1.6, also available on SOFTWARE.DIR and VDL as a secondary source:

- Lab UI HL V1.6 Upgrade Instal<span id="_Toc454348899" class="anchor"></span>lation and User Guide LA\*5.2\*66

SECURITY GUIDE

# Security Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Security Guide aids in controlling the release of sensitive information related to national software. AutoVerification does not contain highly sensitive information, so this component of the manual may be included in Freedom of Information Act (FOIA) request releases. There are no unique/atypical features or other information that would be of interest to security personnel or other support groups.

# Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AutoVerification utilizes one pre-existing [security key](#Glos_Sec_Key), listed in the table below.

| Key      | Purpose/Remarks                                                                                                                                 |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| LRVERIFY | If auto release process is to release results that have been tech verified on the GIM middleware then the user needs to hold this key on VistA. |

<span id="_Toc232405454" class="anchor"></span>GLOSSARY

![](laboratory-universal-interface-autorelease-version-1-technical-manual/002.png) ![](laboratory-universal-interface-autorelease-version-1-technical-manual/003.png) ![](laboratory-universal-interface-autorelease-version-1-technical-manual/004.png) ![](laboratory-universal-interface-autorelease-version-1-technical-manual/005.png) ![](laboratory-universal-interface-autorelease-version-1-technical-manual/006.png) ![](laboratory-universal-interface-autorelease-version-1-technical-manual/007.png) ![](laboratory-universal-interface-autorelease-version-1-technical-manual/008.png) ![](laboratory-universal-interface-autorelease-version-1-technical-manual/009.png) ![](laboratory-universal-interface-autorelease-version-1-technical-manual/010.png) ![](laboratory-universal-interface-autorelease-version-1-technical-manual/011.png) ![](laboratory-universal-interface-autorelease-version-1-technical-manual/012.png) ![](laboratory-universal-interface-autorelease-version-1-technical-manual/013.png) ![](laboratory-universal-interface-autorelease-version-1-technical-manual/014.png) ![](laboratory-universal-interface-autorelease-version-1-technical-manual/015.png) ![](laboratory-universal-interface-autorelease-version-1-technical-manual/016.png) ![](laboratory-universal-interface-autorelease-version-1-technical-manual/017.png) ![](laboratory-universal-interface-autorelease-version-1-technical-manual/018.png)

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Term or Acronym</th>
<th colspan="3">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"></td>
<td><strong>A</strong></td>
<td>![](laboratory-universal-interface-autorelease-version-1-technical-manual/019.png)</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><strong>B</strong></td>
<td>![](laboratory-universal-interface-autorelease-version-1-technical-manual/020.png)</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><strong>C</strong></td>
<td>![](laboratory-universal-interface-autorelease-version-1-technical-manual/021.png)</td>
</tr>
<tr class="even">
<td><span id="Glos_CPRS" class="anchor"></span>Computerized Patient Record System (CPRS)</td>
<td colspan="3">A Computerized Patient Record (CPR) is a comprehensive database system used to store and access patients’ healthcare information. CPRS is the Department of Veteran’s Affairs electronic health record software. The CPRS organizes and presents all relevant data on a patient in a way that directly supports clinical decision making. This data includes medical history and conditions, problems and diagnoses, diagnostic and therapeutic procedures and interventions. Both a graphic user interface version and a character-based interface version are available. CPRS provides a single interface for health care providers to review and update a patient’s medical record, and to place orders, including medications, special procedures, x-rays, patient care nursing orders, diets, and laboratory tests. CPRS is flexible enough to be implemented in a wide variety of settings for a broad spectrum of health care workers, and provides a consistent, event-driven, Windows-style interface.</td>
</tr>
<tr class="odd">
<td>CPRS</td>
<td colspan="3"><em>See</em> <a href="#Glos_CPRS">Computerized Patient Record System</a></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><strong>D</strong></td>
<td>![](laboratory-universal-interface-autorelease-version-1-technical-manual/022.png)</td>
</tr>
<tr class="odd">
<td><span id="Glos_DBIA" class="anchor"></span>Database Integration Agreement (DBIA)</td>
<td colspan="3">A formal understanding between two or more application packages which describes how data is shared or how packages interact. This agreement maintains information between package Developers, allowing the use of internal entry points or other package-specific features.</td>
</tr>
<tr class="even">
<td>DBIA</td>
<td colspan="3">See <a href="#Glos_DBIA">Database Integration Agreement</a></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><strong>E</strong></td>
<td>![](laboratory-universal-interface-autorelease-version-1-technical-manual/023.png)</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><strong>F</strong></td>
<td>![](laboratory-universal-interface-autorelease-version-1-technical-manual/024.png)</td>
</tr>
<tr class="odd">
<td><span id="Glos_FileMan" class="anchor"></span>FileMan</td>
<td colspan="3"><p>FileMan is a set of <a href="#Glos_M">M</a> utilities written in the late 1970s and early 1980s which allow the definition of data structures, menus and security, reports, and forms.</p>
<p>Its first use was in the development of medical applications for the Veterans Administration (now the Department of Veterans Affairs). Since it was a work created by the government, the source code cannot be copyrighted, placing that code in the public domain. For this reason, it has been used for rapid development of applications across a number of organizations, including commercial products.</p></td>
</tr>
<tr class="even">
<td><span id="Glos_FTP" class="anchor"></span>File Transfer Protocol (FTP)</td>
<td colspan="3">A <a href="#Glos_ClientServer">client-server</a> protocol which allows a user on one computer to transfer files to and from another computer over a TCP/IP network. Also the client program the user executes to transfer files. It is defined in <a href="http://www.ietf.org/rfc/rfc959.txt">Internet Standard 9, Request for Comments 959</a>.</td>
</tr>
<tr class="odd">
<td>FTP</td>
<td colspan="3"><em>See</em> <a href="#Glos_FTP">File Transfer Protocol</a></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><strong>G</strong></td>
<td>![](laboratory-universal-interface-autorelease-version-1-technical-manual/025.png)</td>
</tr>
<tr class="odd">
<td><span id="Glos_Global" class="anchor"></span>Global</td>
<td colspan="3"><p><a href="#Glos_M">M</a> uses <em>globals</em>: variables which are intrinsically stored in files and which persist beyond the program or process completion. Globals appear as normal variables with the caret character in front of the name. For example, the M statement…</p>
<p><strong>SET ^A(“first_name”)=”Bob”</strong></p>
<p>…will result in a new record being created and inserted in the persistent just as a file persists in an operating system. Globals are stored, naturally, in highly structured data files by the language and accessed only as M globals. Huge databases grow randomly rather than in a forced serial order, and the strength and efficiency of M is based on its ability to handle all this flawlessly and invisibly to the programmer.</p>
<p>For all of these reasons, one of the most common M programs is a database management system. <a href="#Glos_FileMan">FileMan</a> is one such example. M allows the programmer much wider control of the data; there is no requirement to fit the data into square boxes of rows and columns.</p></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><strong>I</strong></td>
<td>![](laboratory-universal-interface-autorelease-version-1-technical-manual/026.png)</td>
</tr>
<tr class="odd">
<td>Indicated Value</td>
<td colspan="3">Code to determine how to compare data (<em>e.g.</em>, “<strong>R</strong>” equals “resistant”).</td>
</tr>
<tr class="even">
<td>Indicator</td>
<td colspan="3">Code to determine how to match results/interpretations.</td>
</tr>
<tr class="odd">
<td><span id="Glos_IRM" class="anchor"></span>Information Resources Management (IRM)</td>
<td colspan="3">The service which is involved in planning, budgeting, procurement and management-in-use of VA's information technology investments.</td>
</tr>
<tr class="even">
<td>IRM</td>
<td colspan="3"><em>See</em> <a href="#Glos_IRM">Information Resources Management</a></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><strong>K</strong></td>
<td>![](laboratory-universal-interface-autorelease-version-1-technical-manual/027.png)</td>
</tr>
<tr class="even">
<td><span id="Glos_KIDS" class="anchor"></span>Kernel Installation and Distribution System (KIDS)</td>
<td colspan="3">The Kernel system permits any <a href="#Glos_VistA">VistA</a> software application to run without modification to its base structure no matter what hardware or software vendor the application was built on. The Kernel contains a number of building management supplies which provide its foundation, including device, menu, programming, operations, security/auditing, task, user, and system management. Its framework provides a structurally sound computing environment that permits controlled user access, menus for choosing various computing activities, the ability to schedule tasks, application development tools, and numerous other management and operation tools.</td>
</tr>
<tr class="odd">
<td>Keys</td>
<td colspan="3"><em>See</em> <a href="#Glos_Sec_Key">Security Keys</a></td>
</tr>
<tr class="even">
<td>KIDS</td>
<td colspan="3"><em>See</em> <a href="#Glos_KIDS">Kernel Installation and Distribution System</a></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><strong>L</strong></td>
<td>![](laboratory-universal-interface-autorelease-version-1-technical-manual/028.png)</td>
</tr>
<tr class="even">
<td><span id="Glos_LIM" class="anchor"></span>Laboratory Information Manager</td>
<td colspan="3">The LIM manages the laboratory files in VistA. Additional duties include creation of new tests, interface set-up and maintenance of instruments, coordination with staff outside of lab to create quick orders, order sets and other <a href="#Glos_CPRS">Computerized Patient Record System</a> (CPRS) functions.</td>
</tr>
<tr class="odd">
<td>LIM</td>
<td colspan="3"><em>See</em> <a href="#Glos_LIM">Laboratory Information Manager</a></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><strong>M</strong></td>
<td>![](laboratory-universal-interface-autorelease-version-1-technical-manual/029.png)</td>
</tr>
<tr class="odd">
<td><span id="Glos_M" class="anchor"></span>M</td>
<td colspan="3"><p>M is a procedural, interpreted, multi-user, general-purpose programming language designed to build and control massive databases. It provides a simple abstraction that all data values are strings of characters, and that all data can be structured as multiple dimensional arrays. MUMPS data structures are sparse, using strings of characters as subscripts.</p>
<p>M was formerly (and is still commonly) called MUMPS, for Massachusetts General Hospital Utility Multiprogramming System.</p></td>
</tr>
<tr class="even">
<td>Massachusetts General Hospital Utility Multi-Programming System (MUMPS)</td>
<td colspan="3">See <a href="#Glos_M">M</a></td>
</tr>
<tr class="odd">
<td><span id="Glos_MailMan" class="anchor"></span>MailMan</td>
<td colspan="3">MailMan is an electronic messaging system that transmits messages, computer programs, data dictionaries, and data between users and applications located at the same or at different facilities. Network MailMan disseminates information across any communications medium.</td>
</tr>
<tr class="even">
<td>MUMPS</td>
<td colspan="3">See <a href="#Glos_M">M</a></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><strong>N</strong></td>
<td>![](laboratory-universal-interface-autorelease-version-1-technical-manual/030.png)</td>
</tr>
<tr class="even">
<td><span id="Glos_Namespace" class="anchor"></span>Namespace</td>
<td colspan="3">A logical partition on a physical device that contains all the artifacts for a complete <a href="#Glos_M">M</a> system, including <a href="#Glos_Global">globals</a>, routines, and libraries. Each namespace is unique, but data can be shared between namespaces with proper addressing within the routines. In <a href="#Glos_VistA">VistA</a>, namespaces are usually dedicated to a particular function. The MMMS namespace, for example, is designed for use by MRSA-PT.</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><strong>P</strong></td>
<td>![](laboratory-universal-interface-autorelease-version-1-technical-manual/031.png)</td>
</tr>
<tr class="even">
<td>PackMan</td>
<td colspan="3">A specific type of <a href="#Glos_MailMan">MailMan</a> message used to distribute <a href="#Glos_KIDS">KIDS</a> builds.</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><strong>S</strong></td>
<td>![](laboratory-universal-interface-autorelease-version-1-technical-manual/032.png)</td>
</tr>
<tr class="even">
<td><span id="Glos_Sec_Key" class="anchor"></span>Security Keys</td>
<td colspan="3">Codes which define the characteristic(s), authorization(s), or privilege(s) of a specific user or a defined group of users. The <a href="#Glos_VistA">VistA</a> option file refers to the security key as a “lock.” Only those individuals assigned that “lock” can use a particular VistA option or perform a specific task that is associated with that security key/lock. In MRSA-PT, keys are used to access specific options that are otherwise “locked” without the security key. Only users designated as “Holders” may access these options.</td>
</tr>
<tr class="odd">
<td>Selected Etiology</td>
<td colspan="3">Organism or final microbial diagnosis/<a href="#Glos_isolate">isolate</a>.</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td><strong>T</strong></td>
<td>![](laboratory-universal-interface-autorelease-version-1-technical-manual/033.png)</td>
</tr>
<tr class="odd">
<td>Tasked Report</td>
<td colspan="3">Reports that can be scheduled via <a href="#Glos_TaskMan">TaskMan</a>.</td>
</tr>
<tr class="even">
<td><span id="Glos_TaskMan" class="anchor"></span>TaskMan</td>
<td colspan="3">The Kernel module that schedule and processes background tasks (aka Task Manager)</td>
</tr>
<tr class="odd">
<td>TCP/IP</td>
<td colspan="3"><em>See</em> <a href="#Glos_TCPIP">Transmission Control Protocol over Internet Protocol</a></td>
</tr>
<tr class="even">
<td><span id="Glos_TCPIP" class="anchor"></span>Transmission Control Protocol over Internet Protocol (TCP/IP)</td>
<td colspan="3">The <em>de facto</em> standard Ethernet protocols, TCP/IP was developed for internetworking and encompasses both network layer and transport layer protocols. While TCP and IP specify two protocols at specific protocol layers, TCP/IP is often used to refer to the entire Department of Defense protocol suite based upon these, including telnet, File Transfer Protocol (FTP), User Datagram Protocol (UDP), and Reliable Data Protocol (RDP).</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><strong>V</strong></td>
<td>![](laboratory-universal-interface-autorelease-version-1-technical-manual/034.png)</td>
</tr>
<tr class="even">
<td>Value</td>
<td colspan="3">Code used to determine how to compare results.</td>
</tr>
<tr class="odd">
<td><span id="Glos_VistA" class="anchor"></span>Veterans Health Information Systems and Technology Architecture (VistA)</td>
<td colspan="3">VistA is a comprehensive, integrated health care information system composed of numerous software modules. <em>See</em> <a href="http://www.va.gov/vista_monograph/docs/2008VistAHealtheVet_Monograph.pdf">http://www.va.gov/VistA_monograph/docs/2008VistAHealtheVet_Monograph.pdf</a> and <a href="http://www.virec.research.va.gov/DataSourcesName/VISTA/VISTA.htm">http://www.virec.research.va.gov/DataSourcesName/VISTA/VISTA.htm</a>.</td>
</tr>
<tr class="even">
<td>VistA</td>
<td colspan="3"><em>See</em> <a href="#Glos_VistA">Veterans Health Information Systems and Technology Architecture</a></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td><strong>W</strong></td>
<td>![](laboratory-universal-interface-autorelease-version-1-technical-manual/035.png)</td>
</tr>
</tbody>
</table>