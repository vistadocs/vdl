---
title: Surgery Risk Assessment Version 3 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: SRA
app_name: Surgery Risk Assessment
section: CLI
app_status: active
pkg_ns: SRA
patch_ver: 3
patch_id: SRA*3
group_key: "SRA:SRA:3"
file_numbers: []
security_keys: 
  - SR DOWNLOAD
  - SRA CLEANUP
menu_options: 0
description: 
audience: 
keywords: 
  - class
  - even
  - style
  - width
  - other
  - table
  - blockquote
  - risk
  - assessment
  - surgery
page_count: 0
word_count: 44999
section_count: 23
table_count: 3
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Surgery_Risk_Assessment_(SRA)/SRA_3_P9_TM.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Surgery_Risk_Assessment_(SRA)/SRA_3_P9_TM.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=437"
---

Surgery Risk AssessmentTechnical Manual

![](surgery-risk-assessment-version-3-technical-manual/001.png)

June 2024Version 3.0Department of Veterans AffairsOffice of Information and Technology (OIT)  
Revision History

Each time this manual is updated, the Title Page lists the new revised date, and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<table>
<caption><p><span id="_Toc181282730" class="anchor"></span>Table 1: Files Exported with the Surgery Risk Assessment Package</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 23%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Revision Date</strong></th>
<th><blockquote>
<p><strong>Sections Revised</strong></p>
</blockquote></th>
<th><strong>Revision Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>06/2024</td>
<td>All</td>
<td><blockquote>
<p>Update based on patch SRA*3*9</p>
<p>Additional updates included for patch SRA*3*10</p>
<p>For consistency and clarity, all references to Fourword, centralized Surgery Risk Assessment database and Hines have been removed and replaced with “Surgery Risk Assessment Database”. Refer to the Surgery Risk Assessment User Manual for additional details.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>7/31/21</td>
<td>All</td>
<td><blockquote>
<p>Update based on patch SRA*3*5</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>08/31/20</td>
<td>All</td>
<td><blockquote>
<p>Update based on patch SRA*3*4</p>
</blockquote></td>
</tr>
<tr class="even">
<td>06/30/20</td>
<td>All</td>
<td><blockquote>
<p>Update based on patch SRA*3*3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>05/2020</td>
<td>All</td>
<td><blockquote>
<p>Final Review (PMO Office Review)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>04/2020</td>
<td>All</td>
<td><blockquote>
<p>Updates to overview and content (PMO Office Review)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>03/2020</td>
<td>All</td>
<td><blockquote>
<p>Document updated describing the new technical elements of the Surgery Risk Assessment package. (Software Engineering Team)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc181282730" class="anchor"></span>Table 1: Files Exported with the Surgery Risk Assessment Package

Table of Contents

List of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
    - [Organization](#organization)
    - [Processing Incoming Risk Assessment Transmissions](#processing-incoming-risk-assessment-transmissions)
    - [Create Surgery Risk Assessment Download Text Files/Messages](#create-surgery-risk-assessment-download-text-filesmessages)
    - [Create SRA Monthly Workload Report Messages](#create-sra-monthly-workload-report-messages)
- [Technical Manual](#technical-manual)
  - [Implementation and Maintenance](#implementation-and-maintenance)
    - [Installation](#installation)
    - [Troubleshooting](#troubleshooting)
    - [Site Specific Parameters](#site-specific-parameters)
  - [Files](#files)
  - [File Descriptions](#file-descriptions)
  - [Routines](#routines)
  - [Exported Options](#exported-options)
    - [Options Listed by Name](#options-listed-by-name)
    - [Option Descriptions](#option-descriptions)
  - [Templates](#templates)
    - [Input Templates](#input-templates)
    - [Print Template](#print-template)
    - [Sort Template](#sort-template)
  - [Globals in the Risk Assessment Package](#globals-in-the-risk-assessment-package)
    - [Journaling Globals](#journaling-globals)
  - [Archiving and Purging](#archiving-and-purging)
    - [Archiving](#archiving)
    - [Purging](#purging)
  - [Callable Routines](#callable-routines)
  - [External Relations](#external-relations)
    - [Packages Needed to Run Surgery Risk Assessment](#packages-needed-to-run-surgery-risk-assessment)
    - [Calls Made by Surgery Risk Assessment Package](#calls-made-by-surgery-risk-assessment-package)
  - [Database Integration Control Registrations](#database-integration-control-registrations)
  - [Internal Relations](#internal-relations)
  - [Package-Wide Variables](#package-wide-variables)
- [Security Guide](#security-guide)
  - [Contingency Planning](#contingency-planning)
  - [Interfacing](#interfacing)
  - [Security Keys](#security-keys)
  - [File Security](#file-security)
- [Appendix](#appendix)
  - [Appendix A: Non-Cardiac Transmission Layout](#appendix-a-non-cardiac-transmission-layout)
  - [Appendix B: Cardiac Transmission Layout](#appendix-b-cardiac-transmission-layout)
  - [Appendix C: Workload Report Transmission Layout](#appendix-c-workload-report-transmission-layout)
  - [Appendix D: 1-Liner Transmission Layout](#appendix-d-1-liner-transmission-layout)
- [Glossary](#glossary)
- [Index](#index)
The intended audience for this Surgery Risk Assessment Technical manual is a broad base of stakeholders who include, but are not limited to, the VA National Surgery Office (NSO), the VA Office of Information and Technology (OIT), Health Product Support (HPS), the VA Project Management Team, Functional Analyst(s), and System Administrators that may work on this project.
The Surgery Risk Assessment package, Surgery Risk Assessment Database, and associated processes are designed to document, collect, organize, and transmit surgery case data. The Surgery Risk Assessment package collects non-cardiac risk assessment data from all the VA medical centers in order to process and store them in a database file at the Surgery Risk Assessment Database. Due to lower volume (about 5,000 cases annually versus 400,000 for non-cardiac), the cardiac risk assessments are sent via a separate data stream directly to the VA NSO in Denver, CO via Veterans Health Information Systems and Technology Architecture’s (VistA) MailMan messages. (MailMan is software for managing electronic mail and can run processes to route electronic mail.)
Data documented in the Surgery Risk Assessment Database is validated, formatted, analyzed, and developed into reports by the NSO using the VA Surgical Quality Improvement Program (VASQIP) system in a secure online environment. VASQIP characterizes mortality and morbidity rates, both unadjusted and risk adjusted. The VASQIP reports help show comparable and actionable surgical program data to Veterans Health Administration (VHA) facilities, Veterans Integrated Service Networks (VISNs), and VHA Leadership for surgical program assessment and quality improvement.
The published NSO Quarterly Report includes facility-level surgery-specific data for surgical outcomes, quality, staff workload, efficiency, utilization, patient satisfaction, and policy compliance. The NSO Annual Surgery Report and NSO Quarterly Report are reviewed by approximately 2,160 users each year.
This section provides an overview of the Surgery Risk Assessment package components found on the Surgery Risk Assessment Database used as an interim step in processing transmissions and also provides documentation conventions used in this *Surgery Risk Assessment Technical Manual*.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Surgery Risk Assessment package is designed to be used by NSO staff and OIT staff that support the Surgery Risk Assessment Database. The Surgery Risk Assessment package is used to collect data for patients who have had surgical procedures. Surgery Risk Assessment data is collected at VA medical centers and transmitted to the Surgery Risk Assessment Database (SURGERY RISK ASSESSMENT file (#139)) for surgical procedure analysis and reporting purposes.

The *Surgery Risk Assessment Technical Manual* acquaints the user with the various Surgery Risk Assessment options found on the Surgery Risk Assessment Database and offers specific guidance on the maintenance and use of the package. Documentation concerning the VistA Surgery Risk Assessment package, including any subsequent change pages affecting this documentation, is located on the VistA Documentation Library (VDL) on the Internet at [<u>http://www.va.gov/vdl/</u>.](http://www.va.gov/vdl/)

### Organization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Surgery Risk Assessment module on the Surgery Risk Assessment Database contains the following major components, also called modules:

- Processing Incoming Risk Assessment Transmissions
- Create Surgery Risk Assessment Download Files/Messages
- Create SRA Monthly Workload Report Messages

### Processing Incoming Risk Assessment Transmissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Non-Cardiac:

When a non-cardiac risk assessment at a VA medical center is ready for transmission to the Surgery Risk Assessment Database, it is transformed by the VistA Surgery package into a VistA MailMan message. This MailMan message is sent to the RISK ASSESSMENT mail group located on the Surgery Risk Assessment Database. The mail group location is hardcoded into the VistA Surgery Package.

When a non-cardiac risk assessment message or group of messages has been successfully transmitted to the Surgery Risk Assessment Database, an automatic server routine begins parsing the information stored in the MailMan messages into the SURGERY RISK ASSESSMENT file (#139). New non-cardiac records within file \#139 are created for new non-cardiac risk assessments and existing non-cardiac risk assessments are updated if they already exist.

Once the server has successfully parsed the non-cardiac VistA MailMan message into file \#139, validation messages are sent back to the Surgical Quality Nurse (SQN) at the VA medical center, stating that the assessment has been successfully processed, and the ASSESSMENT STATUS field (#74) of the non-cardiac risk assessment is updated from “COMPLETE” to “TRANSMITTED”.

If an error occurs as the message is loaded into file \#139, an error code is generated and a VistA MailMan message containing the error code is sent to OIT Staff via the SRA OIT SUPPORT mail group at the Surgery Risk Assessment Database. The non-cardiac risk assessment remains in the “COMPLETE” status at the VA medical center and will continue to try and transmit each time the transmission process runs until it is successful. SRA OIT staff will work with the Surgical Quality Nurse and local/regional IT support to troubleshoot recurring errors.

Non-Assessed Cases (1-Liners):

1-liner risk assessments are automatically created for all completed surgery cases. When the TIME PAT OUT OR field (#.232) in the SURGERY file (#130) is set for a surgery case at a VA medical center, the ^SRF(“AQ”, cross reference is set for that case. This cross reference is used to determine when a completed surgery case is transmitted to the Surgery Risk Assessment Database as a 1-liner risk assessment. The ^SRF(“AQ”, cross reference is set to 45 days after the end of the month for the date of operation for the completed case.

When a 1-liner risk assessment at a VA medical center is ready for transmission to the Surgery Risk Assessment Database, it is transformed by the VistA Surgery package into a VistA MailMan message. This MailMan message is sent to the RISK ASSESSMENT mail group located on the Surgery Risk Assessment Database. The mail group location is hardcoded into the VistA Surgery package.

When a 1-liner risk assessment message or group of messages has been successfully transmitted to the Surgery Risk Assessment Database, an automatic server routine begins parsing the information stored in the MailMan messages into the SURGERY RISK ASSESSMENT file (#139). New 1-liner records within file \#139 are created for new 1-liner risk assessments and existing 1-liner risk assessments are updated if they already exist.

Once the server has successfully parsed the 1-liner VistA MailMan message into file \#139, messages are sent back to the VA medical center updating the READY TO TRANSMIT field (#905) of the 1-liner case from “READY to “TRANSMITTED” and the ^SRF(“AQ”, cross reference is removed.

If an error occurs as the message is loaded into file \#139, an error code is generated and a VistA MailMan message containing the error code is sent to OIT Staff via the SRA OIT SUPPORT mail group at the Surgery Risk Assessment Database. The 1-liner risk assessment remains in the "READY" status at the VA medical center and will continue to try and transmit each time the transmission process runs until it is successful. SRA OIT staff will work with the Surgical Quality Nurse and local/regional IT support to troubleshoot recurring errors.

\*\*\*Note: Cases that are not eligible for assessment or excluded from assessment also transmit as 1-liner risk assessments. 1-liner risk assessments are also sent to the Surgery Risk Assessment Database for cases logged/completed as cardiac risk assessments - see the Cardiac section below.

Monthly Surgical Case Workload Report:

The Monthly Surgical Case Workload Report transmission message sent from VA medical centers to the Surgery Risk Assessment Database contains surgical case workload information such as the total number (count) of surgical cases performed in the prior month. It is used in later phases to keep track of facility workloads and to verify the number of records transmitted.

1.  On the 26th day of each month, VA medical centers automatically send the Monthly Surgical Case Workload Report transmission message.
2.  The Monthly Surgical Case Workload Report transmission message can be manually sent by the Surgical Quality Nurse at a VA medical center by selection of a prompt within the Monthly Surgical Case Workload Report \[SROA MONTHLY WORKLOAD REPORT\] option in the Surgery Risk Assessment Menu \[SROA RISK ASSESSMENT\] within the VistA Surgery package.
3.  The Monthly Surgical Case Workload Report transmission message is also sent when a Surgical Quality Nurse at a VA medical center executes the Queue Assessment Transmissions \[SROA TRANSMIT ASSESSMENTS\] option which manually queues the VASQIP transmission process.

Cardiac:\*\*\*Note: Cardiac risk assessments are transmitted to both the Surgery Risk Assessment Database and the VA National Surgery Office (NSO) in Denver, CO as read-only MailMan messages. Cardiac risk assessment messages are not sent through the processing routine on the Surgery Risk Assessment Database.

When a cardiac risk assessment at a VA medical center is ready for transmission to the Surgery Risk Assessment Database, it is transformed by the VistA Surgery package into a VistA MailMan message. This MailMan message is sent to the CARDIAC RISK ASSESSMENTS mail group at the VA NSO Office in Denver, CO and the SRCARDIAC mail group at the Surgery Risk Assessment Database.

National Surgery Office (NSO) staff process VistA MailMan messages in the CARDIAC RISK ASSESSMENTS Inbox sent directly to the Denver, CO National Surgery Office. Cardiac risk assessments are not processed or stored in the SURGERY RISK ASSESSMENT file (#139) on the Surgery Risk Assessment Database.

The most current transmission mapping for each of the four types of transmission messages are attached below. (These links will take you to the appropriate appendix section.)

- [Non-Cardiac Transmission Layout (A)](#appendix-a-non-cardiac-transmission-layout)
- [Cardiac Transmission Layout (B)](#appendix-b-cardiac-transmission-layout)
- [Workload Report Transmission Layout (C)](#appendix-c-workload-report-transmission-layout)
- [1-Liner Transmission Layout (D)](#appendix-d-1-liner-transmission-layout)

### Create Surgery Risk Assessment Download Text Files/Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The automated process to create text files and related Outlook messages runs based on the Risk Assessment Download Schedule in the Surgery Risk Assessment Database. The Task Risk Assessment Download Auto Process \[SRATDLTASK\] option is used to queue a recurring task on the Surgery Risk Assessment Database and is executed daily. It checks the RISK ASSESSMENT DOWNLOAD SCHEDULE file (#139.9) to determine if the process is to be executed. If a download is scheduled for this date, a message is sent to the SRA DOWNLOAD mail group on the Surgery Risk Assessment Database with the subject “VASQIP Download from NDB on xx/xx/xx notifying members of the name of the text files created by the download process”. The text files that are created by the download process are sent in separate Outlook messages to recipients of the Surgery Risk Assessment Monthly Download Outlook distribution group. Each file is attached to the message as an encrypted, password protected zip file.

The three text files are named:

- Risk Assessment Download file
- Surgical Case Workload Totals
- Workload Incomplete Assessments

The files are securely sent to the NSO staff (via the Surgery Risk Assessment Monthly Download Outlook distribution group) using tools outside the Surgery Risk Assessment software.

### Create SRA Monthly Workload Report Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The automated process to create SRA Monthly Workload Report messages by VISN runs based on the Task Monthly Surgical Case Workload Report \[SRAWTASK\] option. This option is scheduled on the Surgery Risk Assessment Database and is used to queue a recurring task that is executed on the 27<sup>th</sup> day of each month to create the SRA Monthly Workload Report. This report includes surgery workload information and incomplete assessment totals for each VISN. The report is sent as a MailMan message to the user(s) identified in the associated VISN mail group.

# Technical Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Implementation and Maintenance section contains information regarding the installation and setup of the Surgery Risk Assessment package.

### Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of the Surgery Risk Assessment software and updates on the Surgery Risk Assessment Database are done by the OIT Staff assigned to support it. This software is not installed at VA medical centers but is installed in the Virtual VistA Cluster. For questions related to the installation of the Surgery Risk Assessment software package, please contact the Enterprise Service Desk.

### Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information related to the troubleshooting of issues related to the Surgery Risk Assessment software and Surgery Risk Assessment Database is found in the Surgery Risk Assessment User Manual.

### Site Specific Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before using the Surgery Risk Assessment package, the following initial information must be set up.

1.  SRA\*3.0\*0 INSTALLATION

Whenever patch SRA\*3.0\*0 is installed, the installer should use the VA FileMan Enter or Edit File Entries \[DIEDIT\] option to update the value of the SERVER DEVICE field (#227) in the OPTION file (#19) for entry “Surgery Risk Assessment National Database Server” \[SRATSRV\] from “PALO ALTO FDA MED GUIDE” to “SRA”. This is a one-time task that only needs to be completed after the <u>initial</u> installation of SRA\*3.0\*0.

2.  NEW PERSON file (#200)

All personnel (NSO users, support staff, etc.) must be properly defined in the NEW PERSON file (#200). Instructions can be found in the Surgery Risk Assessment User Manual.

3.  SECURITY KEYS  
    Security keys have various uses in the Surgery Risk Assessment package and must be assigned as needed before using the package. The security keys used by the Surgery Risk Assessment package are described in the Security Keys section of this manual. Instructions can be found in the Surgery Risk Assessment User Manual.
4.  SURGERY ATTENDING CODES file (#139.3)

The entries of the SURGERY ATTENDING CODES file (#139.3) match what is defined in the ATTENDING CODES file (#132.9) of the Surgery package installed at VA medical centers.

5.  SURGERY CANCELLATION REASON file (#139.7)

The entries of the SURGERY CANCELLATION REASON file (#139.7) match what is defined in the SURGERY CANCELLATION REASON file (#135) of the Surgery package installed at VA medical centers.

6.  MAIL GROUPS

The following mail groups should be created with the appropriate persons added as members.

- SRA DOWNLOAD – This is the mail group that receives the VASQIP download message when the download process runs and text files are created. This is not the same as the Outlook distribution group that receives the encrypted password protected text files created by the download process.
- SRA RESOURCE MONITOR – This mail group was created on 2/15/19 to receive notifications of possible stuck resource device. The resource device is used to process surgery risk assessment transmissions.
- SRA-MGR – This mail group is made up of those who maintain the Surgery Risk Assessment Database and who receive the monthly workload report. The members of the SRA-MGR mail group who have been assigned the "SRA CLEANUP" security key also have transmission messages cleaned from their inbox daily and are alerted when there are error messages.
- SRA-VISN1 – This mail group receives the monthly workload report for VISN 1.
- SRA-VISN10 – This mail group receives the monthly workload report for VISN 10.
- SRA-VISN12 – This mail group receives the monthly workload report for VISN 12.
- SRA-VISN15 – This mail group receives the monthly workload report for VISN 15.
- SRA-VISN16 – This mail group receives the monthly workload report for VISN 16.
- SRA-VISN17 – This mail group receives the monthly workload report for VISN 17.
- SRA-VISN18 – This mail group receives the monthly workload report for VISN 18.
- SRA-VISN19 – This mail group receives the monthly workload report for VISN 19.
- SRA-VISN2 – This mail group receives the monthly workload report for VISN 2.
- SRA-VISN20 – This mail group receives the monthly workload report for VISN 20.
- SRA-VISN21 – This mail group receives the monthly workload report for VISN 21.
- SRA-VISN22 – This mail group receives the monthly workload report for VISN 22.
- SRA-VISN23 – This mail group receives the monthly workload report for VISN 23.
- SRA-VISN4 – This mail group receives the monthly workload report for VISN 4.
- SRA-VISN5 – This mail group receives the monthly workload report for VISN 5.
- SRA-VISN6 – This mail group receives the monthly workload report for VISN 6.
- SRA-VISN7 – This mail group receives the monthly workload report for VISN 7.
- SRA-VISN8 – This mail group receives the monthly workload report for VISN 8.
- SRA-VISN9 – This mail group receives the monthly workload report for VISN 9.
- SRCARDIAC – This mail group receives cardiac surgery risk assessment transmission messages.
- SRCOSERV – This mail group receives a mail message when a server request is received for Monthly Workload updates to the Surgery Risk Assessment Database. This mail group also receives processing error messages if the Monthly Workload data cannot be processed.
- SRA OIT SUPPORT – This mail group receives NSQIP transmission messages from the medical centers.

## Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following files are exported with the Surgery Risk Assessment package.

<table>
<caption><p><span id="_Toc181282731" class="anchor"></span>Table 2: List of SRA Routines from FOURWORD</p></caption>
<colgroup>
<col style="width: 10%" />
<col style="width: 41%" />
<col style="width: 12%" />
<col style="width: 22%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Update DD</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Data Comes With</strong></p>
<p><strong>File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>User</strong></p>
<p><strong>Override</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>139</td>
<td><blockquote>
<p>SURGERY RISK ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td>139.1</td>
<td><blockquote>
<p>RISK ASSESSMENT SITE</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES (MERGE)</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>139.3</td>
<td><blockquote>
<p>SURGERY ATTENDING CODES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES (MERGE)</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td>139.4</td>
<td><blockquote>
<p>TRANSMISSION LAYOUTS</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>139.7</td>
<td><blockquote>
<p>SURGERY CANCELLATION REASON</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td>139.9</td>
<td>RISK ASSESSMENT DOWNLOAD SCHEDULE</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc181282731" class="anchor"></span>Table 2: List of SRA Routines from FOURWORD

> **NOTE:** The \*SURGERY QUARTERLY DATA file (#130.99) and the \*SURGERY TRANSPLANT ASSESSMENTS file (#139.6) are no longer used. These files are not displayed with descriptions in the next section.

## File Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

View file descriptions by using the VA FileMan Print File Entries \[DIPRINT\] option. The Surgery Risk Assessment file numbers range from 139 to 139.9.

> **NOTE:** Files \*SURGERY QUARTERLY DATA (#130.99) and \*SURGERY TRANSPLANT ASSESSMENTS (#139.6) are not included in this section because they are no longer in use.

Example:

Select VA FileMan Option: Print File Entries

Output from what File: FILE

Sort by: NAME// .001 NUMBER

Start with NUMBER: FIRST// 139

Go to NUMBER: LAST// 139.9

Within NUMBER, Sort by: \<Enter\>

First Print ATTRIBUTE: 1 GLOBAL NAME

Then Print ATTRIBUTE: .01 NAME

Then Print ATTRIBUTE: 4 DESCRIPTION (word-processing)

Then Print ATTRIBUTE: \<Enter\>

Heading (S/C): FILE List// \<Enter\>

START at PAGE: 1// \<Enter\>

DEVICE: ;;1000 TCP/IP

FILE List SEP 10, 2024@10:46 PAGE 1

GLOBAL NAME NAME

DESCRIPTION

--------------------------------------------------------------------------------

NUMBER: 139

^SRA( SURGERY RISK ASSESSMENT

This file is used to store risk assessments sent to it from the sites via

MailMan. The Hines cooperative study group will periodically download these

assessments to their database.

NUMBER: 139.1

^SRAW( RISK ASSESSMENT SITE

This file contains the medical centers participating in the National Surgical

Quality Improvement Program and the monthly surgical case workload for each.

NUMBER: 139.3

^SRATT( SURGERY ATTENDING CODES

This file is pointed to by the ATTENDING CODE field in the SURGERY RISK

ASSESSMENT file (#139). It contains the codes representing the highest level

of resident supervision provided by the attending staff surgeon.

NUMBER: 139.4

^SRAM(139.4, TRANSMISSION LAYOUTS

This file contains the layouts for the transmission messages being sent to

the Surgery Risk Assessment Database. The file is released with data and

includes the field name, file and position for each data piece transmitted.

> **NOTE:** This file MUST be updated as part of any enhancement release that

changes the data being sent to the Surgery Risk Assessment Database.

NUMBER: 139.7

^SRCAN( SURGERY CANCELLATION REASON

This file stores the VA Surgical Service standard cancellation reasons.

NUMBER: 139.9

^SRAFY(139.9, RISK ASSESSMENT DOWNLOAD SCHEDULE

This file contains the Risk Assessment Data Download schedule.

The download dates included in this file are provided by the National Surgery

Office annually.

The dates identified in this file determine when the Risk Assessment Data

Download Process should be executed.

## Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is the list of routines used in the Surgery Risk Assessment package. This list excludes all initialization routines, protocol installation routines, and routines exported with patches that performed a one-time function. The first line of each routine contains a brief description of the general function of the routine. Use the Kernel First Line Routine Print \[XU FIRST LINE PRINT\] option to print a list of just the first line of each routine in the SRA\* namespace.

<table>
<caption><p><span id="_Toc181282732" class="anchor"></span>Table 3: Options in the Surgery Risk Assessment Package</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th>SRADLRPT</th>
<th>SRAENV</th>
<th>SRAFERR</th>
<th>SRAKILL</th>
<th>SRAKILL1</th>
<th><blockquote>
<p>SRAKILL2</p>
</blockquote></th>
<th><blockquote>
<p>SRAMEAS</p>
</blockquote></th>
<th><blockquote>
<p>SRANUR</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SRAPOST0</td>
<td>SRAPOST4</td>
<td>SRAPRE4</td>
<td>SRAPURGE</td>
<td>SRARMON</td>
<td><blockquote>
<p>SRASITE</p>
</blockquote></td>
<td><blockquote>
<p>SRATCHK</p>
</blockquote></td>
<td><blockquote>
<p>SRATCHK1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRATDL</td>
<td>SRATDL1</td>
<td>SRATDL2</td>
<td>SRATDL3</td>
<td>SRATDL4</td>
<td><blockquote>
<p>SRATDLNO</p>
</blockquote></td>
<td><blockquote>
<p>SRATMNO</p>
</blockquote></td>
<td><blockquote>
<p>SRATMNO7</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SRATMNO8</td>
<td>SRATMNOX</td>
<td>SRATP</td>
<td>SRATP1</td>
<td>SRATP2</td>
<td><blockquote>
<p>SRATP3</p>
</blockquote></td>
<td><blockquote>
<p>SRATP4</p>
</blockquote></td>
<td><blockquote>
<p>SRATP5</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRATP6</td>
<td>SRATP7</td>
<td>SRATPB</td>
<td>SRATPOTH</td>
<td>SRATPS</td>
<td><blockquote>
<p>SRATSRV</p>
</blockquote></td>
<td><blockquote>
<p>SRATSRV2</p>
</blockquote></td>
<td><blockquote>
<p>SRATSRV3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SRATSRV4</td>
<td>SRATSRV7</td>
<td>SRATSRV8</td>
<td>SRATSRVX</td>
<td>SRATT</td>
<td><blockquote>
<p>SRATUTL</p>
</blockquote></td>
<td><blockquote>
<p>SRATVMS</p>
</blockquote></td>
<td><blockquote>
<p>SRAVISN</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRAWDELM</td>
<td>SRAWRPT</td>
<td>SRAWRPT1</td>
<td>SRAWSERV</td>
<td>SRAWTXT</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc181282732" class="anchor"></span>Table 3: Options in the Surgery Risk Assessment Package

## Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains information about the Surgery Risk Assessment package options. The exported options are first listed by name. They are then provided alphabetically with a description of each option.

### Options Listed by Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table contains a list of all of the options in the Surgery Risk Assessment package, listed alphabetically by Option Name.

| Option Name              | Menu Text                                        |
|--------------------------|--------------------------------------------------|
| SRA DOWNLOAD             | Print Risk Assessment Download Schedule          |
| SRA DOWNLOAD EDIT        | Risk Assessment Download Schedule (Enter/Edit)   |
| SRA MAINTENANCE          | Risk Assessment Database Maintenance Menu        |
| SRA OIT UTILITIES        | OI&T Staff Utilities for Risk Assessment Menu    |
| SRA RESOURCE MONITOR     | SRA Resource Device Monitor                      |
| SRA SITE EDIT            | Risk Assessment Site (Enter/Edit)                |
| SRA TRANSMISSION LAYOUTS | Edit Transmission Layouts File (#139.4)          |
| SRA VISN DISPLAY         | Display VISN/Medical Center Alignment            |
| SRA VISN NURSE           | VISN Workload Report Recipients (Enter/Edit)     |
| SRA VISN RN LIST         | List of VISNS and Surgical Nurse Contacts        |
| SRA VISN UPDATE          | VISN Identified for Medical Center (Enter/Edit)  |
| SRAFERR                  | Check for Risk Assessment Transmission Errors    |
| SRAMLR                   | Print SRA Transmission Message Format            |
| SRAMSGP                  | Parse Risk Assessment Message                    |
| SRAPARSE                 | Decipher SRA Transmission Message                |
| SRATDL                   | \*Create Surgery Risk Assessment Download Files  |
| SRATDLEDIT               | Risk Assessment Download Schedule (Enter/Edit)   |
| SRATDLPRT                | Print Risk Assessment Download Schedule          |
| SRATDLTASK               | Task Risk Assessment Download Auto Process       |
| SRATMENU                 | Surgery Risk Assessment Manager Menu             |
| SRATSRV                  | Surgery Risk Assessment National Database Server |
| SRAWRPT                  | Surgical Case Workload Report (VISNs)            |
| SRAWSERV                 | Surgery Server for NSQIP Workload Data           |
| SRAWTASK                 | Task Monthly Surgical Case Workload Report       |
| SRAWTXT                  | \*Download Monthly Workload Reports              |

<span id="_Toc181282733" class="anchor"></span>Table 4: External Packages to Run the Surgery Risk Assessment Package

\* These options are flagged for deletion in a future release.

### Option Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides a listing of Surgery Risk Assessment options and includes a brief description of each. They are listed alphabetically by Menu Text.

*Check for Risk Assessment Transmission Errors*\[SRAFERR\]

This option is tasked nightly. It checks the IN box of the members of the SRA-MGR mail group who have been assigned the "SRA CLEANUP" security key. It identifies messages which contain "ERROR" or "PROBLEM" in the subject. It sends an email to the member and their remote email with the number of messages in the IN box, total error messages, total messages deleted and information on any error messages. After processing, it will purge non-error Risk Assessment Transmission messages.

For research purposes, the counts, Internal Entry Number (IEN) and Message Subject of deleted messages will be stored in the ^XTMP("SRAFERR") global if needed for 120 days.

Annually, on December 31st, this background task will also call PURGE^SRAPURGE and delete data greater than three full fiscal years old. A temporary backup of the purged records is kept in the ^XTMP global for sixty days. Therefore, copies of the purged records are now stored in the global ^XTMP("SRAPURGE_AUDIT "\_date. The date is in VistA format. (Example:

^XTMP("SRAPURGE_AUDIT 3231116") The global will be purged automatically after sixty days. If the purged records need to be restored with 60 days of the purge, the command RESTORE^SRAPURGE may be invoked from programmer's mode.

*\*Create Surgery Risk Assessment Download Files* \[SRATDL\]

> **NOTE:** This option has been replaced with the Task Risk Assessment Download Auto Process \[SRATDLTASK\] option which automates the risk assessment download process.

This option tasks the surgery risk assessment download process to run at the date and time selected.

*Decipher SRA Transmission Message* \[SRAPARSE\]

User can enter a message IEN or find a NC or 1-Liner from their inbox. Tool will ask to choose one case or all (if the message has multiple cases). All lines of the message will be parsed.

*Display VISN/Medical Center Alignment* \[SRA VISN DISPLAY\]

This option displays the medical center and VISN alignment stored in the RISK ASSESSMENT SITE file (#139.1).

*\*Download Monthly Workload Reports* \[SRAWTXT\]

*Note: This option has been replaced with the Task Monthly Surgical Case Workload Report \[SRAWTASK\] option.*

This option allows the downloading of monthly surgical case workload reports to a text file.

*Edit Transmission Layouts File (#139.4)* \[SRA TRANSMISSION LAYOUTS\]

This option allows modification of the TRANSMISSION LAYOUTS file (#139.4).

*List of VISNS and Surgical Nurse Contacts* \[SRA VISN RN LIST\]

This option lists the surgical nurse point of contact listed in the Remote Member field in the Risk Assessment mail group for each VISN.

*OI&T Staff Utilities for Risk Assessment Menu* \[SRA OIT UTILITIES\]

This menu contains options used by OIT Staff to management the Surgical Risk Assessment Database.

*Parse Risk Assessment Message* \[SRAMSGP\]

Server option to parse a Non-Cardiac or 1-Liner message into component parts. Used as part of option SRAPARSE.

*Print Risk Assessment Download Schedule* \[SRA DOWNLOAD\]

This option prints the download dates stored in the RISK ASSESSMENT DOWNLOAD SCHEDULE file (#139.9).

*Print Risk Assessment Download Schedule* \[SRATDLPRT\]

*Note: This option has been replaced with the option SRA DOWNLOAD.*

This option prints the download dates stored in the RISK ASSESSMENT DOWNLOAD SCHEDULE file (#139.9).

*Print SRA Transmission Message Format* \[SRAMLR\]

For either Non-Cardiac or 1-Liner messages, user may select a message line to see a map of the data that is sent in that line.

*Risk Assessment Database Maintenance Menu* \[SRA MAINTENANCE\]

This menu contains options used to maintain configurable files and mail groups used within the Surgery Risk Assessment Database. These options are used to update these items when changes in staff, VISN associations, or download schedules are made.

*Risk Assessment Download Schedule (Enter/Edit)* \[SRA DOWNLOAD EDIT\]

This option allows for the entry and editing of the RISK ASSESSMENT DOWNLOAD SCHEDULE file (#139.9). Note that if a date needs to be changed, it will need to be deleted and the new date entered.

The data in this file is used by the daily tasked job, Task Risk Assessment Download Auto Process \[SRATDLTASK\], to determine the dates for which a download text file should be created.

\*\*\*In order to add a new entry using this option, the user must have the FILE MANAGER ACCESS CODE field (#3) in the NEW PERSON file (#200) set to “@”.

*Risk Assessment Download Schedule (Enter/Edit)* \[SRATDLEDIT\]

*Note: This option has been replaced with the option SRA DOWNLOAD EDIT.*

This option allows for the entry and editing of the RISK ASSESSMENT DOWNLOAD SCHEDULE file (#139.9). Note that if a date needs to be changed, it will need to be deleted and the new date entered.

The data in this file is used by the daily tasked job, Task Risk Assessment Download Auto Process \[SRATDLTASK\], to determine the dates for which a download text file should be created.

\*\*\*In order to add a new entry using this option, the user must have the FILE MANAGER ACCESS CODE field (#3) in the NEW PERSON file (#200) set to “@”.

*Risk Assessment Site (Enter/Edit)* \[SRA SITE EDIT\]

This option is used to add, edit, or inactivate sites in the RISK ASSESSMENT SITE file (#139.1). When edits are made, a message is sent to the Surgery Risk Assessment Monthly Download distribution group in Outlook.

*SRA Resource Device Monitor*\[SRA RESOURCE MONITOR\]

This option monitors the SRA resource device and sends an email notification if a slot in use appears hung.

*Surgery Risk Assessment Manager Menu* \[SRATMENU\]

This is the main menu for Surgery Risk Assessment. It contains the options used for the maintenance and functions of the application.

*Surgery Risk Assessment National Database Server*\[SRATSRV\]

Used to process incoming surgery risk assessments sent in MailMan messages from the VAMCs moving the data into a national database.

*Surgery Server for NSQIP Workload Data*\[SRAWSERV\]

This server option processes the monthly National Surgery Quality Improvement Program case workload report mail messages moving data into the NSQIP national database.

*Surgical Case Workload Report (VISNs)*\[SRAWRPT\]

*Note: As of November 2019, this report is created and sent to VISN Nurses automatically. This option will only be used for ad hoc requests requiring manual creation.*

This option produces the VASQIP Surgical Case Workload Report which includes surgery workload information and incomplete assessment totals for the selected month. The report may be produced for a single VISN or for all VISNs. The report produced may be e-mailed to VISN Nurse Leaders or to selected individuals. The report may also be displayed on the screen or sent to a printer.

*Task Monthly Surgical Case Workload Report*\[SRAWTASK\]

This option is used to queue a recurring task which will be executed on the 27th day of each month to create the VASQIP Surgical Case Workload Report. This report includes surgery workload information and incomplete assessment totals for each VISN. The report is emailed to VISN Nurse Leaders identified in the associated VISN mail group. By tasking this report, the option Surgical Case Workload Report (VISNs) \[SRAWRPT\] will not need to be used manually each month.

*Task Risk Assessment Download Auto Process*\[SRATDLTASK\]

This option is to be used to queue a recurring task which will be executed daily. It will check the RISK ASSESSMENT DOWNLOAD SCHEDULE file (#139.9) to determine if the process is to be executed. If a download is scheduled for this date, the Surgery Risk Assessment, the Surgery Case Workload Totals, and the Surgery Case Work Incomplete Assessments Totals data will be downloaded to text files.

The text file name format will be as follows:

SRDL_mmddyy.TXT - Surgery Risk Assessment

SRTOTALS_mmddyy.TXT - Workload Totals

SRINCOMP_mmddyy.TXT - Workload Incomplete Assessments Totals

mm = 2-digit month, dd = 2-digit day, and yy = 2-digit year

It will send a MailMan message to users in the G.SRA DOWNLOAD mail group with the file names and directory name. For the Surgery Risk Assessment, it will include details on the number of records included from each site.

Routine also removes SR\* text files greater than 60 days old.

*VISN Identified for Medical Center (Enter/Edit)* \[SRA VISN UPDATE\]

This option can update the medical center and VISN alignment stored in the RISK ASSESSMENT SITE file (#139.1).

*VISN Workload Report Recipients (Enter/Edit)* \[SRA VISN NURSE\]

This option allows editing of the VISN RN who receives the Surgical Case Workload Report.

## Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the templates provided with the Surgery Risk Assessment package.

### Input Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SRA TRANSMISSION LAYOUT: This template is used to enter/edit information in the TRANSMISSION LAYOUTS file (#139.4)

### Print Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no Print Templates included.

### Sort Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no Sort Templates included.

## Globals in the Risk Assessment Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Surgery Risk Assessment package stores data in the following globals:

^SRA SURGERY RISK ASSESSMENT (#139)

^SRAFY  RISK ASSESSMENT DOWNLOAD SCHEDULE (139.9)

^SRATT SURGERY ATTENDING CODES (#139.3)

^SRAW RISK ASSESSMENT SITE (#139.1)

^SRB \*SURGERY TRANSPLANT ASSESSMENTS (#139.6)

^SRCAN SURGERY CANCELLATION REASON (#139.7)

^SRCO \*SURGERY QUARTERLY DATA (#130.99)

^SRAM TRANSMISSION LAYOUTS (#139.4)

### Journaling Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The globals SRA are recommended for journaling.

## Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the archiving and purging processes related to the Surgery Risk Assessment package.

### Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Surgery Risk Assessment package does not provide for the archiving of data.

### Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As part of the nightly tasked option Check for Risk Assessment Transmission Errors \[SRAFERR\], the software checks to determine whether it is time to purge old assessments. If the date is December 31<sup>st</sup>, the software will delete all entries in the SURGERY RISK ASSESSMENT file (#139) prior to the previous three fiscal years. For example, when run on December 31, 2023, all entries with a date prior to October 1, 2020 will be deleted.

## Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no Surgery Risk Assessment routines callable by other packages. There are no interdependencies with other systems.

## External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the packages needed to run the Surgery Risk Assessment package, and also the calls that are made by the Surgery Risk Assessment package to external routines.

### Packages Needed to Run Surgery Risk Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Surgery Risk Assessment package relies minimally on the following external packages. This software is not included in this package and must be installed before the Surgery Risk Assessment package is completely functional.

<table>
<caption><p><span id="_Toc181282734" class="anchor"></span>Table 5: External References</p></caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Package</strong></th>
<th><blockquote>
<p><strong>Minimum Version Needed</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Kernel</td>
<td><blockquote>
<p>8.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VA FileMan</td>
<td><blockquote>
<p>22.2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MailMan</td>
<td><blockquote>
<p>8.0</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc181282734" class="anchor"></span>Table 5: External References

### Calls Made by Surgery Risk Assessment Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Surgery Risk Assessment package makes calls to the following external references:

<table>
<caption><p><span id="_Toc181282735" class="anchor"></span>Table 6: Security Keys used to Restrict Access</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Routine</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Entry Points Used</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>%DT</p>
</blockquote></td>
<td>^%DT, DD</td>
</tr>
<tr class="even">
<td><blockquote>
<p>%DTC</p>
</blockquote></td>
<td>NOW</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>%RCR</p>
</blockquote></td>
<td>%XY</td>
</tr>
<tr class="even">
<td><blockquote>
<p>%ZIS</p>
</blockquote></td>
<td><blockquote>
<p>^%ZIS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>%ZISC</p>
</blockquote></td>
<td><blockquote>
<p>^%ZISC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>%ZISH</p>
</blockquote></td>
<td><blockquote>
<p>$$DEL, $$GATF, $$LIST, $$PWD, CLOSE, OPEN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>%ZTLOAD</td>
<td><blockquote>
<p>^%ZTLOAD, $$S</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DDIOL</td>
<td><blockquote>
<p>EN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DIC</td>
<td><blockquote>
<p>^DIC, $$FIND1, LIST</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DICN</td>
<td><blockquote>
<p>FILE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DID</td>
<td><blockquote>
<p>$$GET1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DIE</td>
<td><blockquote>
<p>^DIE, UPDATE^DIE, FILE^DIE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DIK</td>
<td><blockquote>
<p>^DIK</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DIQ</td>
<td><blockquote>
<p>$$GET1, D, GETS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DIR</td>
<td><blockquote>
<p>^DIR</p>
</blockquote></td>
</tr>
<tr class="even">
<td>XLFDT</td>
<td>$$DT, $$FMADD, $$FMTE, $$HDIFF, $$HTFM, $$NOW</td>
</tr>
<tr class="odd">
<td>XLFSTR</td>
<td>$$UP, $$LOW, $$REPLACE, $$TRIM</td>
</tr>
<tr class="even">
<td>XMA03</td>
<td>$$REN</td>
</tr>
<tr class="odd">
<td>XMA1C</td>
<td>REMSBMSG</td>
</tr>
<tr class="even">
<td>XMD</td>
<td>^XMD</td>
</tr>
<tr class="odd">
<td>XMXAPI</td>
<td>DELMSG, SENDMSG</td>
</tr>
<tr class="even">
<td>XMXAPIB</td>
<td>LISTMSGS, QBSKT</td>
</tr>
<tr class="odd">
<td>XPAR</td>
<td>$$GET</td>
</tr>
<tr class="even">
<td>XUSER</td>
<td>$$ACTIVE</td>
</tr>
</tbody>
</table>

<span id="_Toc181282735" class="anchor"></span>Table 6: Security Keys used to Restrict Access

## Database Integration Control Registrations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Surgery Risk Assessment package has the following Database Integration Control Registrations (ICRs) with other packages. For complete information regarding ICRs, please refer to the DBA MENU \[DBA\] option \> INTEGRATION CONTROL REGISTRATIONS \[DBA IA INTEGRATION AGREEMENTS\] option on FORUM.

2061 NAME: DBIA2061

CUSTODIAL PACKAGE: MAILMAN

SUBSCRIBING PACKAGE: SURGERY RISK ASSESSMENT

Added 6/11/20, effective with SRA\*3\*3

USAGE: Controlled Subscription ENTERED: JUL 11,1997

STATUS: Active EXPIRES:

DURATION: VERSION:

FILE: 3.8 ROOT: XMB(3.8

TYPE: File

DESCRIPTION:

This is an agreement for FileMan read/write access to subfile 3.812, (#12)

MEMBERS - REMOTE.

GLOBAL REFERENCE:

^XMB(3.8,D1,6,

.01 MEMBERS - REMOTE 0;1 Both R/W w/Fileman

KEYWORDS:

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All the Surgery Risk Assessment package options are designed to be standalone. There are no package level entry or exit actions required for any of the Surgery Risk Assessment options.

## Package-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no package-wide Surgery Risk Assessment namespaced local variables.

# Security Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Contingency Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Surgery Risk Assessment package runs on a VistA server that is backed-up daily.

## Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the interfaces to the Surgery Risk Assessment package. All interfacing between the Surgery Risk Assessment package on the Surgery Risk Assessment Database and VistA Surgery package at the VA medical centers are done using the MailMan server capabilities.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following keys are used to restrict access to menus and options. Only holders of these keys will be permitted to access the locked options or functions.

| Security Key | Description                                                                                                                                                                                                                                                                                                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SR DOWNLOAD      | This security key is used to lock the various Surgery download options.                                                                                                                                                                                                                                                                                                                                         |
| SRA CLEANUP      | This security key is used to determine if a Member of the SRA-MGR Mail Group's Mailman IN box should be cleaned up when the “SRA Task to Check for Error Messages” \[SRAFERR\] option is executed or tasked. \*\*\*Note the menu text for the SRAFERR option is actually “Check for Risk Assessment Transmission Errors”. The menu text in the Description field of the SECURITY KEY file (#19.1) is incorrect. |

<span id="_Toc181282736" class="anchor"></span>Table 7: First Time Installations of the Surgery Risk Assessment Database Software Files

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following files were distributed with limited access for first time installations of the Surgery Risk Assessment Database software. Files not listed below were sent without restrictions on VA FileMan access. Sites can add their own file access codes as needed, but it is highly recommended that they do not change the codes that are sent with this software package.

<table>
<caption><p><span id="_Toc181282737" class="anchor"></span>Table 8: Common Terms Defined</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 43%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>File</strong></p>
<p><strong>Number</strong></p></th>
<th><blockquote>
<p><strong>File Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Read</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Write</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Delete</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>LAYGO</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>139</td>
<td><blockquote>
<p>SURGERY RISK ASSESSMENT</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>139.1</td>
<td><blockquote>
<p>RISK ASSESSMENT SITE</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>139.3</td>
<td><blockquote>
<p>SURGERY ATTENDING CODES</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>139.4</td>
<td><blockquote>
<p>TRANSMISSION LAYOUTS</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>139.6</td>
<td><blockquote>
<p>*SURGERY TRANSPLANT ASSESSMENTS</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>139.7</td>
<td><blockquote>
<p>SURGERY CANCELLATION REASON</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>139.9</td>
<td><blockquote>
<p>RISK ASSESSMENT DOWNLOAD SCHEDULE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>130.99</td>
<td><blockquote>
<p>*SURGERY QUARTERLY DATA</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc181282737" class="anchor"></span>Table 8: Common Terms Defined

> **NOTE:** “\*” at the start of the file name indicates the file no longer used.

# Appendix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Appendix A: Non-Cardiac Transmission Layout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The non-cardiac transmission layout was last updated in 2024 by SR\*3.0\*205 and SRA\*3.0\*9.

Each line begins with “\$” in position 1, Station Number in positions 2-4, Assessment Number in positions 5-11, and Line Identifier in positions 12-14. The station id-assessment numbers combine on the national database to form the ID-NUMBER field (#.01) in the SURGERY RISK ASSESSMENT file (#139).

Line 1 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 1</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-21</td>
<td>7</td>
<td>RA;4 206</td>
<td>S;4 115</td>
<td>Date Transmitted</td>
<td></td>
</tr>
<tr class="even">
<td>22-24</td>
<td>3</td>
<td>Opdate – DoB</td>
<td>0;3 2</td>
<td>Age</td>
<td></td>
</tr>
<tr class="odd">
<td>25</td>
<td>1</td>
<td>VADM(5)</td>
<td>0;4 3</td>
<td>SEX</td>
<td><p>M MALE</p>
<p>F FEMALE</p></td>
</tr>
<tr class="even">
<td>26-37</td>
<td>12</td>
<td>0;9 .09</td>
<td>0;5 4</td>
<td>Date of operation</td>
<td></td>
</tr>
<tr class="odd">
<td>38-57</td>
<td>20</td>
<td>VA(“PID”)</td>
<td>SRAPID;1 309</td>
<td>PATIENT ID</td>
<td></td>
</tr>
<tr class="even">
<td>58-63</td>
<td>6</td>
<td>8;1 50</td>
<td>0;18 7</td>
<td>DIVISION</td>
<td></td>
</tr>
<tr class="odd">
<td>64-75</td>
<td>12</td>
<td>205;3 342</td>
<td>0;17 219</td>
<td>DATE/TIME OF DEATH</td>
<td></td>
</tr>
<tr class="even">
<td>76-105</td>
<td>30</td>
<td>.02 .02</td>
<td>6;1 .02</td>
<td>OP ROOM PROCEDURE PERFORMED</td>
<td>Name of OR</td>
</tr>
<tr class="odd">
<td>106-107</td>
<td>2</td>
<td>52;1 619</td>
<td>6;5 449</td>
<td>IMMED USE -CONTAMINATION</td>
<td>(0 to 99)</td>
</tr>
<tr class="even">
<td>108-109</td>
<td>2</td>
<td>52;2 620</td>
<td>6;6 450</td>
<td>IMMED USE-SPS/OR MAN ISSUE</td>
<td>(0 to 99)</td>
</tr>
<tr class="odd">
<td>110-111</td>
<td>2</td>
<td>52;3 621</td>
<td>6;7 451</td>
<td>IMMED USE-EMERGENCY CASE</td>
<td>(0 to 99)</td>
</tr>
<tr class="even">
<td>112-113</td>
<td>2</td>
<td>52;4 622</td>
<td>6;8 452</td>
<td>IMMED USE-NO BETTER OPTION</td>
<td>(0 to 99)</td>
</tr>
<tr class="odd">
<td>114-115</td>
<td>2</td>
<td>52;5 623</td>
<td>6;9 453</td>
<td>IMMED USE -LOANER</td>
<td>(0 to 99)</td>
</tr>
<tr class="even">
<td>116-117</td>
<td>2</td>
<td>52;6 624</td>
<td>6;10 454</td>
<td>IMMED USE -DECONTAMINATION</td>
<td>(0 to 99)</td>
</tr>
<tr class="odd">
<td>118-119</td>
<td>2</td>
<td>200;55 618</td>
<td>6;11 455</td>
<td>POSITIVE DRUG SCREENING</td>
<td><blockquote>
<p>1 NOT DONE</p>
<p>2 NEGATIVE RESULT</p>
<p>3 POS NOT RX</p>
<p>4 POS RX</p>
</blockquote></td>
</tr>
<tr class="even">
<td>120-121</td>
<td>2</td>
<td>200.1;9 517</td>
<td>6;12 456</td>
<td>TOBACCO USE</td>
<td><p>1 NEVER USED</p>
<p>TOBACCO</p>
<p>2 NO USE IN LAST</p>
<p>12 MOS</p>
<p>3 CIGARETTES ONLY</p>
<p>4 OTHER (NO</p>
<p>CIGARETTES)</p>
<p>5 CIGARETTES PLUS</p>
<p>OTHER</p></td>
</tr>
<tr class="odd">
<td>122-123</td>
<td>2</td>
<td>200.1;10 518</td>
<td>6;13 457</td>
<td>TOBACCO USE TIMEFRAME</td>
<td><p>1 WITHIN 2 WEEKS</p>
<p>2 2 WKS TO 3 MOS</p>
<p>3 3 TO 12 MONTHS</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="even">
<td>124-125</td>
<td>2</td>
<td>200.1;11 519</td>
<td>6;14 458</td>
<td>DIABETES MELLITUS CHRONIC</td>
<td><p>1 NO</p>
<p>2 DIET</p>
<p>3 ORAL</p>
<p>4 INSULIN</p></td>
</tr>
<tr class="odd">
<td>126-127</td>
<td>2</td>
<td>200.1;12 520</td>
<td>6;15 459</td>
<td>DIABETES MELLITUS PREOP MGMT</td>
<td><p>1 NO</p>
<p>2 DIET</p>
<p>3 ORAL</p>
<p>4 INSULIN</p></td>
</tr>
<tr class="even">
<td>128-129</td>
<td>2</td>
<td>200.1;13 521</td>
<td>6;16 460</td>
<td>CVD REPAIR/OBSTRUCTION</td>
<td><p>0 NO CVD</p>
<p>1 YES - NO</p>
<p>SURGICAL REPAIR</p>
<p>2 YES - PRIOR</p>
<p>SURGICAL REPAIR</p></td>
</tr>
<tr class="odd">
<td>130-131</td>
<td>2</td>
<td>200.1;14 522</td>
<td>6;17 461</td>
<td>HISTORY OF CVD</td>
<td><p>0 NO CVD</p>
<p>1 HISTORY OF TIA'S</p>
<p>2 CVA/STROKE NO</p>
<p>NEURO DEFICIT</p>
<p>3 CVA/STROKE W/</p>
<p>NEURO DEFICIT</p></td>
</tr>
</tbody>
</table>

Line 2 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 2</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15</td>
<td>1</td>
<td>200;2 346</td>
<td>15;1 225</td>
<td>DIABETES <em>– Discontinued use after 2012 update</em></td>
<td><p>N NO</p>
<p>O ORAL</p>
<p>I INSULIN</p></td>
</tr>
<tr class="even">
<td>16</td>
<td>1</td>
<td>200;3 202</td>
<td>2;2 19</td>
<td>CURRENT SMOKER <em>– Discontinued use after 2012 update</em></td>
<td></td>
</tr>
<tr class="odd">
<td>17</td>
<td>1</td>
<td>200;4 246</td>
<td>1;9 88</td>
<td>ETOH &gt; 2 DRINKS/DAY</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="even">
<td>18</td>
<td>1</td>
<td>200.1;2 492</td>
<td>10;9 82.5</td>
<td>PRE-OP FUNCTIONAL STATUS</td>
<td><p>1 INDEPENDENT</p>
<p>2 PARTIALLY</p>
<p>DEPENDENT</p>
<p>3 TOTALLY</p>
<p>DEPENDENT</p>
<p><del>4 UNKNOWN</del></p></td>
</tr>
<tr class="odd">
<td>19</td>
<td>1</td>
<td>200;6 325</td>
<td>10;12 197</td>
<td>DYSPNEA</td>
<td><p>1 NO</p>
<p>2 MODERATE</p>
<p>EXERTION</p>
<p>3 AT REST</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="even">
<td>20</td>
<td>1</td>
<td>200;7 238</td>
<td>5;6 79</td>
<td>DNR STATUS</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="odd">
<td>21</td>
<td>1</td>
<td></td>
<td></td>
<td><em>- blank -</em></td>
<td></td>
</tr>
<tr class="even">
<td>22</td>
<td>1</td>
<td>200;10 204</td>
<td>2;5 22</td>
<td>VENTILATOR DEPENDENT</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="odd">
<td>23</td>
<td>1</td>
<td>200;11 203</td>
<td>2;3 20</td>
<td>HISTORY OF COPD</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>24</td>
<td>1</td>
<td>200;12 326</td>
<td>10;13 198</td>
<td>CURRENT PNEUMONIA</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="odd">
<td>25</td>
<td>1</td>
<td>200.1;6 446</td>
<td>4;8 443</td>
<td>INTRAOPERATIVE ASCITES</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>26</td>
<td>1</td>
<td>200;15 212</td>
<td>4;3 35</td>
<td>PREOPERATIVE ASCITES</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="odd">
<td>27</td>
<td>1</td>
<td>200;16 213</td>
<td>4;4 36</td>
<td>ESOPHAGEAL VARICIES</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="even">
<td>28</td>
<td>1</td>
<td></td>
<td></td>
<td><em>- blank -</em></td>
<td></td>
</tr>
<tr class="odd">
<td>29</td>
<td>1</td>
<td>206;14 205</td>
<td>2;1 281</td>
<td>PRIOR MI</td>
<td><p>0 NO</p>
<p>1 YES, &lt; OR EQUAL</p>
<p>7 DAYS PREOP</p>
<p>2 YES, &gt;7 DAYS AND</p>
<p>&lt;6 MONTHS PREOP</p>
<p>3 UNKNOWN</p>
<p>4 YES, &gt;6 MONTHS</p>
<p>PREOP</p>
<p>5 UNKNOWN</p></td>
</tr>
<tr class="even">
<td>30</td>
<td>1</td>
<td>200;56 640</td>
<td>1;8 46</td>
<td>PCI</td>
<td><p>1 NONE</p>
<p>2 &lt;12 HR OF SURG</p>
<p>3 &gt;12 HR - 7 DAYS</p>
<p>4 &gt;7 DAYS</p>
<p>5 UNKNOWN</p></td>
</tr>
<tr class="odd">
<td>31</td>
<td>1</td>
<td>200;33 266</td>
<td>15;6 239</td>
<td><p>PREVIOUS CARDIAC SURGERY</p>
<p>Will not be used after SR*3*182</p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>32</td>
<td>1</td>
<td>200;34 395</td>
<td>1;3 282</td>
<td><p>ANGINA WITHIN 1 MONTH</p>
<p>Will not be used after SR*3*182</p></td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="odd">
<td>33</td>
<td>1</td>
<td>200;35 396</td>
<td>1;4 283</td>
<td><p>CHF WITHIN ONE MONTH</p>
<p>Will not be used after SR*3*182</p></td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="even">
<td>34</td>
<td>1</td>
<td>200;57 641</td>
<td>3;5 29</td>
<td>HYPERTENSION</td>
<td><p>1 NO</p>
<p>2 YES WITHOUT</p>
<p>MEDICATION</p>
<p>THERAPY</p>
<p>3 YES WITH</p>
<p>MEDICATION</p>
<p>THERAPY</p>
<p>4 UNKNOWN</p></td>
</tr>
<tr class="odd">
<td>35</td>
<td>1</td>
<td>200;38 328</td>
<td>2;8 201</td>
<td>RENAL FAILURE</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="even">
<td>36</td>
<td>1</td>
<td>200;39 211</td>
<td>4;1 33</td>
<td>CURRENTLY ON DIALYSIS</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="odd">
<td>37</td>
<td>1</td>
<td>206;16 265</td>
<td>2;9 202</td>
<td>PERIPHERAL ARTERIAL DISEASE</td>
<td><p>1 NO</p>
<p>2 YES-W/O</p>
<p>ANGI,REVASC,or</p>
<p>AMPUT</p>
<p>3 YES-W HX</p>
<p>ANGI,REVASC,or</p>
<p>AMPUT</p></td>
</tr>
<tr class="even">
<td>38</td>
<td>1</td>
<td>200;42 330</td>
<td>2;10 203</td>
<td>REST PAIN/GANGRENE</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="odd">
<td>39</td>
<td>1</td>
<td></td>
<td></td>
<td><em>- blank -</em></td>
<td></td>
</tr>
<tr class="even">
<td>40</td>
<td>1</td>
<td>200;19 332</td>
<td>2;13 206</td>
<td>IMPAIRED SENSORIUM</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="odd">
<td>41</td>
<td>1</td>
<td></td>
<td></td>
<td><em>- blank -</em></td>
<td></td>
</tr>
<tr class="even">
<td>42</td>
<td>1</td>
<td>200;21 333</td>
<td>2;14 207</td>
<td>COMA</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="odd">
<td>43</td>
<td>1</td>
<td></td>
<td></td>
<td><em>- blank -</em></td>
<td></td>
</tr>
<tr class="even">
<td>44</td>
<td>1</td>
<td></td>
<td></td>
<td><em>- blank -</em></td>
<td></td>
</tr>
<tr class="odd">
<td>45</td>
<td>1</td>
<td>200;24 400</td>
<td>1;10 287</td>
<td>HEMIPLEGIA (Y/N)</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="even">
<td>46</td>
<td>1</td>
<td>200;25 334</td>
<td>2;15 208</td>
<td>HISTORY OF TIA'S <em>– Discontinued use after 2012 update</em></td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="odd">
<td>47</td>
<td>1</td>
<td>200;26 335</td>
<td>2;16 209</td>
<td>CVA/RESIDUAL NEURO DEFICIT <em>– Discontinued use after 2012 update</em></td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="even">
<td>48</td>
<td>1</td>
<td>200;27 336</td>
<td>2;17 210</td>
<td>CVA/NO NEURO DEFICIT <em>– Discontinued use after 2012 update</em></td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="odd">
<td>49</td>
<td>1</td>
<td></td>
<td></td>
<td><em>- blank -</em></td>
<td></td>
</tr>
<tr class="even">
<td>50</td>
<td>1</td>
<td>200;29 401</td>
<td>1;11 288</td>
<td>TUMOR INVOLVING CNS (Y/N)</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="odd">
<td>51</td>
<td>1</td>
<td>200;45 338</td>
<td>2;19 212</td>
<td>DISSEMINATED CANCER (Y/N)</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="even">
<td>52</td>
<td>1</td>
<td>200;46 218</td>
<td>5;4 43</td>
<td>OPEN WOUND OR INFECTION</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="odd">
<td>53</td>
<td>1</td>
<td>200;47 339</td>
<td>2;20 213</td>
<td>CHRONIC STEROID USE (Y/N)</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="even">
<td>54</td>
<td>1</td>
<td>200;48 215</td>
<td>5;1 40</td>
<td>WEIGHT LOSS &gt; 10%</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="odd">
<td>55</td>
<td>1</td>
<td>200;49 216</td>
<td>5;2 41</td>
<td>BLEEDING (COAGULATION) DISORDER</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>56</td>
<td>1</td>
<td>200;50 217</td>
<td>5;3 42</td>
<td>TRANSFUSION &gt; 4 RBC UNITS</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="odd">
<td>57-58</td>
<td>2</td>
<td>200.1;3 269</td>
<td>4;6 430</td>
<td>PREGNANCY</td>
<td><p>N NO</p>
<p>NA NOT APPLICABLE</p>
<p>Y YES</p></td>
</tr>
<tr class="even">
<td>59-61</td>
<td>3</td>
<td>0;4 .04</td>
<td>0;2 23</td>
<td>SURGICAL SPECIALTY</td>
<td><p>48 CARDIAC</p>
<p>SURGERY</p>
<p>49 TRANSPLANTATION</p>
<p>50 GENERAL</p>
<p>SURGERY</p>
<p>51 OB/GYN</p>
<p>52 NEUROSURGERY</p>
<p>53 OPHTHALMOLOGY</p>
<p>54 ORTHOPEDICS</p>
<p>55 EAR, NOSE,</p>
<p>THROAT(ENT)</p>
<p>56 PLASTIC</p>
<p>SURGERY</p>
<p>57 PROCTOLOGY</p>
<p>58 THORACIC</p>
<p>SURGERY</p>
<p>59 UROLOGY</p>
<p>60 ORAL</p>
<p>SURGERY</p>
<p>61 PODIATRY</p>
<p>62 PERIPHERAL</p>
<p>VASCULAR</p>
<p>78 ANESTHESIOLOGY</p></td>
</tr>
<tr class="odd">
<td>62-63</td>
<td>2</td>
<td>200;52 214</td>
<td>0;19 38</td>
<td>PGY OF PRIMARY SURGEON</td>
<td><p>Number 1 to 12 or</p>
<p>0 for Staff Surgeon</p></td>
</tr>
<tr class="even">
<td>64</td>
<td>1</td>
<td>0;10 .035</td>
<td>0;6 291</td>
<td>EMERGENCY CASE (Y/N)</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>65-66</td>
<td>2</td>
<td>1.0;8 1.09</td>
<td>0;16 78</td>
<td>WOUND CLASSIFICATION</td>
<td><p>C CLEAN</p>
<p>CC CLEAN/</p>
<p>CONTAMINATED</p>
<p>D CONTAMINATED</p>
<p>I DIRTY/INFECTED</p></td>
</tr>
<tr class="even">
<td>67</td>
<td>1</td>
<td>200;53 201</td>
<td>0;11 10</td>
<td>REDO PROCEDURE</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>68</td>
<td>1</td>
<td>1.1;3 1.13</td>
<td>1;2 12</td>
<td>ASA CLASSIFICATION</td>
<td><p>1 1-NO DISTURB.</p>
<p>2 2-MILD</p>
<p>DISTURB.</p>
<p>3 3-SEVERE</p>
<p>DISTURB.</p>
<p>4 4-LIFE THREAT</p>
<p>5 5-MORIBUND</p>
<p>6 6-BRAIN-DEAD</p>
<p>1E 1E-NO</p>
<p>DISTURB-EMERG</p>
<p>2E 2E-MILD</p>
<p>DISTURB.-EMERG</p>
<p>3E 3E-SEVERE</p>
<p>DIST.-EMERG.</p>
<p>4E 4E-LIFE</p>
<p>THREAT-EMERG.</p>
<p>5E 5E-MORIBUND-</p>
<p>EMERG.</p>
<p>6E 6E-BRAIN-</p>
<p>DEAD-EMERG.</p>
<p>N N-None</p>
<p>Assigned</p></td>
</tr>
<tr class="even">
<td>69</td>
<td>1</td>
<td>6,0;1 130.06,.01</td>
<td>2;6 192</td>
<td><p>ANESTHESIA TECHNIQUE</p>
<p>OTHER option will be inactivated after 2014 update</p></td>
<td><p>G GENERAL</p>
<p>S SPINAL</p>
<p>E EPIDURAL</p>
<p>M MONITORED</p>
<p>ANESTHESIA</p>
<p>CARE</p>
<p><del>O OTHER</del></p>
<p>L LOCAL</p>
<p>R REGIONAL</p>
<p>N NO ANESTHESIA</p></td>
</tr>
<tr class="odd">
<td>70</td>
<td>1</td>
<td>1.1;3 1.13</td>
<td>1;2 12</td>
<td>ASA CLASSIFICATION SUFFIX “E”</td>
<td></td>
</tr>
<tr class="even">
<td>71</td>
<td>1</td>
<td>6,8;2 130.06,42</td>
<td>2;7 193</td>
<td>INTUBATED? (Y/N)</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>72</td>
<td>1</td>
<td>200.1;8 237.1</td>
<td>2;4 446</td>
<td>PREOPERATIVE SLEEP APNEA</td>
<td><p>1 NONE-LEVEL 1</p>
<p>2 SUSPICION OF SLEEP</p>
<p>APNEA-LEVEL 2</p>
<p>3 SLEEP APNEA-LEVEL</p>
<p>3</p></td>
</tr>
<tr class="even">
<td>73-76</td>
<td>4</td>
<td>206;1 236</td>
<td>0;14 76</td>
<td>HEIGHT</td>
<td></td>
</tr>
<tr class="odd">
<td>77-80</td>
<td>4</td>
<td>206;2 237</td>
<td>0;15 77</td>
<td>WEIGHT</td>
<td></td>
</tr>
<tr class="even">
<td>81-86</td>
<td>6</td>
<td>206;42 485</td>
<td>182;1 372</td>
<td>PRIOR HEART SURGERIES</td>
<td><p>0 None</p>
<p>1 CABG-only</p>
<p>2 Valve-only</p>
<p>3 CABG/Valve</p>
<p>4 Other</p>
<p>5 CABG/Other</p>
<p>6 Unknown</p></td>
</tr>
<tr class="odd">
<td>87</td>
<td>1</td>
<td>200;59 643</td>
<td>182;2 373</td>
<td>ANGINA TIMEFRAME</td>
<td><blockquote>
<p>1 NO ANGINA 2 W/N 14 DAY OF</p>
<p>SURGERY 3 W/N 15-30 DAYS OF</p>
<p>SURGERY 4 UNKNOWN</p>
</blockquote></td>
</tr>
<tr class="even">
<td>88</td>
<td>1</td>
<td>200;58 642</td>
<td>182;3 374</td>
<td>BLEEDING RISK DUE TO MED</td>
<td><p>N NO BLEEDING RISK</p>
<p>FROM MED</p>
<blockquote>
<p>Y BLEEDING RISK</p>
<p>MED NOT D'C</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>89-91</td>
<td>3</td>
<td>25;1 44</td>
<td>182;4 375</td>
<td>SPONGE FINAL COUNT CORRECT</td>
<td><p>Y YES</p>
<p>N NO, SEE NURSING</p>
<p>CARE COMMENTS</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="even">
<td>92-94</td>
<td>3</td>
<td>25;2 45</td>
<td>182;5 376</td>
<td>SHARPS FINAL COUNT CORRECT</td>
<td><p>Y YES</p>
<p>N NO, SEE NURSING</p>
<p>CARE COMMENTS</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="odd">
<td>95-97</td>
<td>3</td>
<td>25;3 46</td>
<td>182;6 377</td>
<td>INSTRUMENT FINAL COUNT CORRECT</td>
<td><p>Y YES</p>
<p>N NO, SEE NURSING</p>
<p>CARE COMMENTS</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="even">
<td>98</td>
<td>1</td>
<td>25;6 630</td>
<td>182;7 378</td>
<td>POSSIBLE ITEM RETENTION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>99</td>
<td>1</td>
<td>25;7 633</td>
<td>182;8 379</td>
<td>WOUND SWEEP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>100</td>
<td>1</td>
<td>25;8 636</td>
<td>182;9 463</td>
<td>INTRA-OPERATIVE X-RAY</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>101-103</td>
<td>3</td>
<td></td>
<td>182;10 464</td>
<td>NUMBER OF PROSTHESIS INSTALLED</td>
<td>(0 to 999)</td>
</tr>
<tr class="even">
<td>104-106</td>
<td>3</td>
<td></td>
<td>182;11 465</td>
<td>NUM OF READ BACK PERFORMED</td>
<td>(0 to 999)</td>
</tr>
<tr class="odd">
<td>107-109</td>
<td>3</td>
<td>206;18 267</td>
<td>1;3 282</td>
<td>ANGINA SEVERITY</td>
<td><p>N NONE</p>
<p>I CLASS I</p>
<p>II CLASS II</p>
<p>III CLASS III</p>
<p>IV CLASS IV</p>
<p>U UNKNOWN</p></td>
</tr>
<tr class="even">
<td>110-112</td>
<td>3</td>
<td>206;19 207</td>
<td>3;4 28</td>
<td><p>CONGESTIVE HEART FAILURE</p>
<p>Will no longer used after SR*3*184</p></td>
<td><p>N NONE I CARDIAC DISEASE, NO SYMPTOMS II SLIGHT LIMITATION III MARKED</p>
<p>LIMITATION IV SYMPTOMS AT REST U UNKNOWN</p></td>
</tr>
<tr class="odd">
<td>113-115</td>
<td>3</td>
<td>.4;6 .46</td>
<td>182;19 478</td>
<td>OP DISPOSITION</td>
<td><p>O OUTPATIENT/</p>
<p>DISCHARGE</p>
<p>I ICU</p>
<p>S STEPDOWN</p>
<p>W WARD</p>
<p>OBS OBSERVATION UNIT</p>
<p>M MORGUE</p></td>
</tr>
<tr class="even">
<td>116-117</td>
<td>2</td>
<td>210;1 662</td>
<td>184;4 92</td>
<td>IMPAIRED COGNITIVE FUNCTION</td>
<td><p>0 NONE-NO</p>
<p>IMPAIRMENT</p>
<p>1 YES-DOCUMENTED</p>
<p>HISTORY</p>
<p>2 YES-DOCUMENTE D</p>
<p>AND DECLINING</p>
<p>3 NO STUDY-NO</p>
<p>DOCUMENTATION</p></td>
</tr>
<tr class="odd">
<td>118-119</td>
<td>2</td>
<td>200.1;15 667</td>
<td>184;5 93</td>
<td>Sleep Apnea-Compliance</td>
<td><p>1 NIGHTLY</p>
<p>2 &gt; OR EQUAL 4 TIMES A WEEK</p>
<p>3 &lt; 4 TIMES A WEEK</p>
<p>4 NOT DOCUMENTED</p></td>
</tr>
<tr class="even">
<td>120-121</td>
<td>2</td>
<td>204;17 338.3</td>
<td>184;6 94</td>
<td>CHEMO FOR MALIG LAST 90 DAYS</td>
<td><p>1 NO CHEMO</p>
<p>2 W/IN 30 DAYS</p>
<p>3 31-90 DAYS</p></td>
</tr>
<tr class="odd">
<td>122-123</td>
<td>2</td>
<td>210;5 670</td>
<td>184;7 96</td>
<td>RESIDENCE 30 DAYS PREOP</td>
<td><p>1 HOME</p>
<p>2 ACUTE CARE</p>
<p>FACILITY</p>
<p>3 LONG TERM CARE</p>
<p>4 HOMELESS</p>
<p>5 UNKNOWN</p></td>
</tr>
<tr class="even">
<td>124-125</td>
<td>2</td>
<td>210;6 671</td>
<td>184;8 97</td>
<td>AMBULATION DEVICE PREOP</td>
<td><p>1 AMBULATES W/OUT</p>
<p>ASSISTIVE DEVICE</p>
<p>2 AMBULATES WITH</p>
<p>CANE OR WALKER</p>
<p>3 USES MANUAL</p>
<p>WHEELCHAIR</p>
<p>INDEPENDENTLY</p>
<p>4 DOES NOT AMBULATE</p>
<p>OR USE MANUAL</p>
<p>WHEELCHAIR</p>
<p>INDEPENDENTLY</p></td>
</tr>
<tr class="odd">
<td>126-127</td>
<td>2</td>
<td>210;8 673</td>
<td>184;10 101</td>
<td>HISTORY OF CANCER DIAGNOSIS</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>128-129</td>
<td>2</td>
<td>210;9 674</td>
<td>184;11 102</td>
<td>HX RAD RX PLANNED SURG FIELD</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>130-131</td>
<td>2</td>
<td>210;12 677</td>
<td>184;12 119</td>
<td>PRIOR SURG SAME OP FIELD</td>
<td><p>0 NO PREVIOUS</p>
<p>SURGERIES</p>
<p>1 1 PREVIOUS</p>
<p>SURGERY</p>
<p>2 2 PREVIOUS</p>
<p>SURGERIES</p>
<p>3 3 PREVIOUS</p>
<p>SURGERIES</p>
<p>4 4 PREVIOUS</p>
<p>SURGERIES</p>
<p>5 5 PREVIOUS</p>
<p>SURGERIES</p>
<p>6 &gt;5 PREVIOUS</p>
<p>SURGERIES</p></td>
</tr>
<tr class="even">
<td>132-133</td>
<td>2</td>
<td>207;29 423</td>
<td>184;9 100</td>
<td>CONGESTIVE HEART FAILURE PREOP</td>
<td><p>0 N CARD DX, CHF,</p>
<p>OR SX</p>
<p>1 Y CARD DX/CHF, N</p>
<p>SX</p>
<p>2 Y CARD DX/CHF, Y</p>
<p>MILD SX</p>
<p>3 Y CARD DX/CHF, Y</p>
<p>MARKED SX</p>
<p>4 Y CARD DX/CHF, Y</p>
<p>SX AT REST</p>
<p>5 N CARD DX/CHF, SX</p>
<p>UNKNOWN</p>
<p>6 Y CARD DX/CHF, SX UNKNOWN</p></td>
</tr>
<tr class="odd">
<td>134</td>
<td>1</td>
<td>.1;21 661</td>
<td>184;2 90</td>
<td>PALLIATION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>135-136</td>
<td>2</td>
<td>210;14 685</td>
<td>182;32 705</td>
<td>DISCHARGE DISPOSITION</td>
<td><p>1 HOME</p>
<p>2 ACUTE CARE</p>
<p>FACILITY TRANSFER</p>
<p>(VA OR NON</p>
<p>3 EXTENDED CARE</p>
<p>FACILITY (NON-</p>
<p>REHAB)</p>
<p>4 REHABILITATION</p>
<p>CENTER</p>
<p>5 SHELTER/</p>
<p>TRANSITIONAL</p>
<p>HOUSING</p>
<p>6 PATIENT DEATH</p>
<p>7 OTHER</p></td>
</tr>
</tbody>
</table>

Line 3 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 16%" />
<col style="width: 23%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 3</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-26</td>
<td>12</td>
<td>.2;2 .22</td>
<td>0;13 75</td>
<td>DATE/TIME OPERATION BEGAN</td>
<td></td>
</tr>
<tr class="even">
<td>27-38</td>
<td>12</td>
<td>.2;3 .23</td>
<td>0;21 182</td>
<td>DATE/TIME OPERATION ENDED</td>
<td></td>
</tr>
<tr class="odd">
<td>39-40</td>
<td>2</td>
<td>.1;10 .166</td>
<td>1;16 13.1</td>
<td>ATTENDING CODE</td>
<td><p>1 OLD0 - 0.</p>
<p>STAFF ALONE</p>
<p>2 OLD1 - 1.</p>
<p>ATTENDING IN</p>
<p>O.R.</p>
<p>3 OLD2 - 2.</p>
<p>ATTENDING IN</p>
<p>O.R.</p>
<p>SUITE</p>
<p>4 OLD3 - 3.</p>
<p>ATTENDING</p>
<p>NOT PRESENT,</p>
<p>BUT</p>
<p>AVAILABLE</p>
<p>5 LEVEL 0.</p>
<p>ATTENDING</p>
<p>DOING THE</p>
<p>OPERATION</p>
<p>6 LEVEL 1.</p>
<p>ATTENDING IN</p>
<p>O.R.</p>
<p>ASSISTING</p>
<p>THE RESIDENT</p>
<p>7 LEVEL 2.</p>
<p>ATTENDING IN</p>
<p>O.R.,</p>
<p>NOT SCRUBBED</p>
<p>8 LEVEL 3.</p>
<p>ATTENDING</p>
<p>NOT PRESENT</p>
<p>IN O.R.</p>
<p>SUITE,</p>
<p>IMMEDIATELY</p>
<p>AVAILABLE</p>
<p>9 LEVEL A:</p>
<p>ATTENDING</p>
<p>DOING</p>
<p>THE</p>
<p>OPERATION</p>
<p>10 LEVEL B:</p>
<p>ATTENDING IN</p>
<p>O.R.,</p>
<p>SCRUBBED</p>
<p>11 LEVEL C:</p>
<p>ATTENDING IN</p>
<p>O.R., NOT</p>
<p>SCRUBBED</p>
<p>12 LEVEL D:</p>
<p>ATTENDING IN</p>
<p>O.R. SUITE,</p>
<p>IMMEDIATELY</p>
<p>AVAILABLE</p>
<p>13 LEVEL E:</p>
<p>EMERGENCY</p>
<p>CARE,</p>
<p>ATTENDING</p>
<p>CONTACTED</p>
<p>ASAP</p>
<p>14 LEVEL F:</p>
<p>NON-OR</p>
<p>PROCEDURE</p>
<p>DONE IN OR,</p>
<p>ATTENDING</p>
<p>IDENTIFIED</p>
<p>99 NOT ENTERED</p></td>
</tr>
<tr class="even">
<td>41-42</td>
<td>2</td>
<td>200.1;4 443</td>
<td>4;7 431</td>
<td>INTRAOPERATIVE DISSEMINATED CANCER</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="odd">
<td>43-44</td>
<td>2</td>
<td>200;54 340</td>
<td>2;23 217</td>
<td>RBC UNITS TRANSFUSED</td>
<td></td>
</tr>
<tr class="even">
<td>45-52</td>
<td>8</td>
<td>0;3(136) .03(136)</td>
<td>0;20 99</td>
<td>POSTOPERATIVE DIAGNOSIS CODE (ICD)</td>
<td></td>
</tr>
<tr class="odd">
<td>53-56</td>
<td>4</td>
<td>205;1 247</td>
<td>6;4 98</td>
<td>LENGTH OF POST-OP STAY</td>
<td>Value or NA for Not Applicable</td>
</tr>
<tr class="even">
<td>57-62</td>
<td>6</td>
<td></td>
<td></td>
<td><em>- blank -</em></td>
<td></td>
</tr>
<tr class="odd">
<td>63</td>
<td>1</td>
<td>205;4 262</td>
<td>7;15 117</td>
<td>RETURN TO OR WITHIN 30 DAYS</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>S NO</p>
<p>STUDY</p></td>
</tr>
<tr class="even">
<td>64</td>
<td>1</td>
<td>.4;7 903</td>
<td>0;23 308</td>
<td>DEATH UNRELATED/RELATED</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>65</td>
<td>1</td>
<td>0;12 .011</td>
<td>0;24 318</td>
<td>HOSPITAL ADMISSION STATUS</td>
<td><p>1 SAME DAY</p>
<p>2 ADMISSION</p>
<p>3 HOSPITALIZED</p></td>
</tr>
<tr class="even">
<td>66</td>
<td>1</td>
<td>0;3 .03</td>
<td>0;25 319</td>
<td>MAJOR/MINOR</td>
<td><p>J MAJOR</p>
<p>N MINOR</p></td>
</tr>
<tr class="odd">
<td>67</td>
<td>1</td>
<td>0;26 .013</td>
<td>184;3 91</td>
<td>PLANNED ADMISSION STATUS</td>
<td><p>1 SAME DAY</p>
<p>2 ADMITTED</p>
<p>3 HOSPITALIZED</p></td>
</tr>
<tr class="even">
<td>68</td>
<td>1</td>
<td></td>
<td>0;27 14</td>
<td>ADMIT WI 14 DAYS OF AN OCCURRENCE</td>
<td></td>
</tr>
<tr class="odd">
<td>69-70</td>
<td>2</td>
<td></td>
<td>20;1 380</td>
<td>1 NUMBER OF SUPERFICIAL INCISIONAL SSI</td>
<td></td>
</tr>
<tr class="even">
<td>71-72</td>
<td>2</td>
<td></td>
<td>20;2 381</td>
<td>2 NUMBER OF DEEP INCISIONAL SSI</td>
<td></td>
</tr>
<tr class="odd">
<td>73-74</td>
<td>2</td>
<td></td>
<td>20;4 382</td>
<td>3 NUMBER OF SYSTEMIC SEPSIS</td>
<td></td>
</tr>
<tr class="even">
<td>75-76</td>
<td>2</td>
<td></td>
<td>20;4 383</td>
<td>4 NUMBER OF PNEUMONIA</td>
<td></td>
</tr>
<tr class="odd">
<td>77-78</td>
<td>2</td>
<td></td>
<td>20;5 384</td>
<td>5 NUMBER OF PULMONARY EMBOLISM</td>
<td></td>
</tr>
<tr class="even">
<td>79-80</td>
<td>2</td>
<td></td>
<td>20;6 385</td>
<td>6 NUMBER OF ON VENTILATOR &gt; 48 HOURS</td>
<td></td>
</tr>
<tr class="odd">
<td>81-82</td>
<td>2</td>
<td></td>
<td>20;7 386</td>
<td><p>7 NUMBER OF UNPLANNED INTUBATION</p>
<p>will not be used after SR*3*182</p></td>
<td></td>
</tr>
<tr class="even">
<td>83-84</td>
<td>2</td>
<td></td>
<td>20;8 387</td>
<td>8 NUMBER OF RENAL INSUFFICIENCY</td>
<td></td>
</tr>
<tr class="odd">
<td>85-86</td>
<td>2</td>
<td></td>
<td>20;9 388</td>
<td>9 NUMBER OF ACUTE RENAL FAILURE</td>
<td></td>
</tr>
<tr class="even">
<td>87-88</td>
<td>2</td>
<td></td>
<td>20;10 389</td>
<td><p>10 NUMBER OF URINARY TRACT INFECTION</p>
<p>will not be used after SR*3*182</p></td>
<td></td>
</tr>
<tr class="odd">
<td>89-90</td>
<td>2</td>
<td></td>
<td>20;40 437</td>
<td>37 NUMBER OF REPEAT VENT SUPPORT</td>
<td></td>
</tr>
<tr class="even">
<td>91-92</td>
<td>2</td>
<td></td>
<td>20;12 391</td>
<td>12 NUMBER OF STROKE/CVA</td>
<td></td>
</tr>
<tr class="odd">
<td>93-94</td>
<td>2</td>
<td></td>
<td>20;13 392</td>
<td>13 NUMBER OF COMA &gt; 24 HOURS</td>
<td></td>
</tr>
<tr class="even">
<td>95-96</td>
<td>2</td>
<td></td>
<td>20;14 393</td>
<td>14 NUMBER OF PERIPHERAL NERVE INJURY</td>
<td></td>
</tr>
<tr class="odd">
<td>97-98</td>
<td>2</td>
<td></td>
<td>20;15 394</td>
<td>15 NUMBER OF BLEEDING/TRANSFUSIONS</td>
<td></td>
</tr>
<tr class="even">
<td>99-100</td>
<td>2</td>
<td></td>
<td>20;16 395</td>
<td>16 NUMBER OF CARDIAC ARREST REQUIRING CPR</td>
<td></td>
</tr>
<tr class="odd">
<td>101-102</td>
<td>2</td>
<td></td>
<td>20;17 396</td>
<td>17 NUMBER OF MYOCARDIAL INFARCTION</td>
<td></td>
</tr>
<tr class="even">
<td>103-104</td>
<td>2</td>
<td></td>
<td>20;18 397</td>
<td>18 NUMBER OF ILEUS/BOWEL OBSTRUCTION</td>
<td></td>
</tr>
<tr class="odd">
<td>105-106</td>
<td>2</td>
<td></td>
<td>20;19 398</td>
<td>19 NUMBER OF GRAFT/PROSTHESIS/FLAP FAILURE</td>
<td></td>
</tr>
<tr class="even">
<td>107-108</td>
<td>2</td>
<td></td>
<td>20;20 399</td>
<td>20 NUMBER OF DVT/THROMBOPHLEBITIS</td>
<td></td>
</tr>
<tr class="odd">
<td>109-110</td>
<td>2</td>
<td></td>
<td>20;21 400</td>
<td>21 NUMBER OF OTHER OCCURRENCE</td>
<td></td>
</tr>
<tr class="even">
<td>111-112</td>
<td>2</td>
<td></td>
<td>20;22 401</td>
<td>22 NUMBER OF WOUND DISRUPTION</td>
<td></td>
</tr>
<tr class="odd">
<td>113-114</td>
<td>2</td>
<td></td>
<td>20;23 402</td>
<td>23 NUMBER OF ENDOCARDITIS</td>
<td></td>
</tr>
<tr class="even">
<td>115-116</td>
<td>2</td>
<td></td>
<td>20;24 403</td>
<td>24 NUMBER OF LOW CARDIAC OUTPUT &gt; 6 HOURS</td>
<td></td>
</tr>
<tr class="odd">
<td>117-118</td>
<td>2</td>
<td></td>
<td>20;25 404</td>
<td>25 NUMBER OF MEDIASTINITIS</td>
<td></td>
</tr>
<tr class="even">
<td>119-120</td>
<td>2</td>
<td></td>
<td>20;26 405</td>
<td>26 NUMBER OF REOPERATION FOR BLEEDING</td>
<td></td>
</tr>
<tr class="odd">
<td>121-122</td>
<td>2</td>
<td></td>
<td>20;27 406</td>
<td>27 NUMBER OF REPEAT CARDIOPULMONARY BYPASS</td>
<td></td>
</tr>
<tr class="even">
<td>123-124</td>
<td>2</td>
<td></td>
<td>20;28 407</td>
<td>28 NUMBER OF STROKE <em>(Obsolete)</em></td>
<td></td>
</tr>
<tr class="odd">
<td>125-126</td>
<td>2</td>
<td></td>
<td>20;29 408</td>
<td>29 NUMBER OF OTHER RESPIRATORY OCCURRENCE</td>
<td></td>
</tr>
<tr class="even">
<td>127-128</td>
<td>2</td>
<td></td>
<td>20;30 409</td>
<td>30 NUMBER OF OTHER CNS OCCURRENCE</td>
<td></td>
</tr>
<tr class="odd">
<td>129-130</td>
<td>2</td>
<td></td>
<td>20;31 410</td>
<td><p>31 NUMBER OF OTHER URINARY TRACT OCCURRENCE</p>
<p>will not be used after SR*3*182</p></td>
<td></td>
</tr>
<tr class="even">
<td>131-132</td>
<td>2</td>
<td></td>
<td>20;32 411</td>
<td>32 NUMBER OF OTHER CARDIAC OCCURRENCE</td>
<td></td>
</tr>
<tr class="odd">
<td>133</td>
<td>1</td>
<td></td>
<td>20;33 412</td>
<td>OCCURRENCE TYPES (“I” for Intraoperative, “P” for Postoperative, “B” for Both, or blank for none)</td>
<td><p>I INTRAOPERATIVE</p>
<p>P POSTOPERATIVE</p>
<p>B BOTH INTRA AND POST</p></td>
</tr>
<tr class="even">
<td>134-135</td>
<td>2</td>
<td></td>
<td>20;37 423</td>
<td>35 NUMBER OF ORGAN/SPACE SSI</td>
<td></td>
</tr>
<tr class="odd">
<td>136-137</td>
<td>2</td>
<td></td>
<td>20;38 424</td>
<td>36 NUMBER OF OTHER WOUND OCCURRENCE</td>
<td></td>
</tr>
<tr class="even">
<td>138-144</td>
<td>7</td>
<td>VADM(3)</td>
<td>0;26 436</td>
<td>DATE OF BIRTH</td>
<td></td>
</tr>
<tr class="odd">
<td>145-146</td>
<td>2</td>
<td></td>
<td>20;42 442</td>
<td>38 NUMBER OF C. DIFFICILE COLITIS</td>
<td></td>
</tr>
<tr class="even">
<td>147-148</td>
<td>2</td>
<td></td>
<td>20;43 447</td>
<td>39 NUMBER OF POSTOP ATRIAL FIBRILLATION</td>
<td></td>
</tr>
<tr class="odd">
<td>149-150</td>
<td>2</td>
<td></td>
<td>182;13 467</td>
<td>40 NUMBER OF SYMPTOMATIC UTI-CULTURE PLUS SIGN/SYMPTOM</td>
<td></td>
</tr>
<tr class="even">
<td>151-152</td>
<td>2</td>
<td></td>
<td>182;14 468</td>
<td><p>41 NUMBER OF MECHANICAL VENTILATION WITHIN 30 DAYS</p>
<p>will not be used after SR*3*184</p></td>
<td></td>
</tr>
<tr class="odd">
<td>153-154</td>
<td>2</td>
<td></td>
<td>20;44 641</td>
<td>42 NUM OUT-OF-OR UNPLANNED INTUB</td>
<td></td>
</tr>
</tbody>
</table>

Line 4 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 4</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-16</td>
<td>2</td>
<td></td>
<td></td>
<td># OF RELATED RETURNS (not downloaded)</td>
<td></td>
</tr>
<tr class="even">
<td>17-21</td>
<td>5</td>
<td>29,0 130.43,3</td>
<td>16,0;1 139.0294,.01</td>
<td>CPT CODE 1 – RELATED RETURN TO OR (FROM FILE 136)</td>
<td></td>
</tr>
<tr class="odd">
<td>22-26</td>
<td>5</td>
<td></td>
<td>16,0;1 139.0294,.01</td>
<td>CPT CODE 2 – RELATED RETURN TO OR (FROM FILE 136)</td>
<td></td>
</tr>
<tr class="even">
<td>27-31</td>
<td>5</td>
<td></td>
<td>16,0;1 139.0294,.01</td>
<td>CPT CODE 3 – RELATED RETURN TO OR (FROM FILE 136)</td>
<td></td>
</tr>
<tr class="odd">
<td>32-36</td>
<td>5</td>
<td></td>
<td>16,0;1 139.0294,.01</td>
<td>CPT CODE 4 – RELATED RETURN TO OR (FROM FILE 136)</td>
<td></td>
</tr>
<tr class="even">
<td>37-41</td>
<td>5</td>
<td></td>
<td>16,0;1 139.0294,.01</td>
<td>CPT CODE 5 – RELATED RETURN TO OR (FROM FILE 136)</td>
<td></td>
</tr>
<tr class="odd">
<td>42-46</td>
<td>5</td>
<td></td>
<td>16,0;1 139.0294,.01</td>
<td>CPT CODE 6 – RELATED RETURN TO OR (FROM FILE 136)</td>
<td></td>
</tr>
<tr class="even">
<td>47-48</td>
<td>2</td>
<td></td>
<td></td>
<td># OF UNRELATED RETURNS (not downloaded)</td>
<td></td>
</tr>
<tr class="odd">
<td>49-53</td>
<td>5</td>
<td></td>
<td>17,0;1 139.0295,.01</td>
<td>CPT CODE 1 – UNRELATED RETURN TO OR (FROM FILE 136)</td>
<td></td>
</tr>
<tr class="even">
<td>54-58</td>
<td>5</td>
<td></td>
<td>17,0;1 139.0295,.01</td>
<td>CPT CODE 2 – UNRELATED RETURN TO OR (FROM FILE 136)</td>
<td></td>
</tr>
<tr class="odd">
<td>59-63</td>
<td>5</td>
<td></td>
<td>17,0;1 139.0295,.01</td>
<td>CPT CODE 3 – UNRELATED RETURN TO OR (FROM FILE 136)</td>
<td></td>
</tr>
<tr class="even">
<td>64-68</td>
<td>5</td>
<td></td>
<td>17,0;1 139.0295,.01</td>
<td>CPT CODE 4 – UNRELATED RETURN TO OR (FROM FILE 136)</td>
<td></td>
</tr>
<tr class="odd">
<td>69-73</td>
<td>5</td>
<td></td>
<td>17,0;1 139.0295,.01</td>
<td>CPT CODE 5 – UNRELATED RETURN TO OR (FROM FILE 136)</td>
<td></td>
</tr>
<tr class="even">
<td>74-78</td>
<td>5</td>
<td></td>
<td>17,0;1 139.0295,.01</td>
<td>CPT CODE 6 – UNRELATED RETURN TO OR (FROM FILE 136)</td>
<td></td>
</tr>
<tr class="odd">
<td>79-85</td>
<td>7</td>
<td></td>
<td>18;1 340</td>
<td>SUPERFICIAL INCISIONAL SSI 1-7 SROC(1)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="even">
<td>86-92</td>
<td>7</td>
<td></td>
<td>18;2 341</td>
<td>DEEP INCISIONAL SSI 8-14 SROC(2)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="odd">
<td>93-99</td>
<td>7</td>
<td></td>
<td>18;3 342</td>
<td>SYSTEMIC SEPSIS 15-21 SROC(3)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="even">
<td>100-106</td>
<td>7</td>
<td></td>
<td>18;4 343</td>
<td>PNEUMONIA 22-28 SROC(4)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="odd">
<td>107-113</td>
<td>7</td>
<td></td>
<td>18;5 344</td>
<td>PULMONARY EMBOLISM 29-35 SROC(5)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="even">
<td>114-120</td>
<td>7</td>
<td></td>
<td>18;6 345</td>
<td><p>ON VENTILATOR&gt;48 HOURS</p>
<p>36-42 SROC(6)</p></td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="odd">
<td>121-127</td>
<td>7</td>
<td></td>
<td>18;7 346</td>
<td><p>UNPLANNED EDEMA 43-49 SROC(7)</p>
<p>will not be used after SR*3*182</p></td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="even">
<td>128-134</td>
<td>7</td>
<td></td>
<td>18;8 347</td>
<td>RENAL INSUFFICIENCY 50-56 SROC(8)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="odd">
<td>135-141</td>
<td>7</td>
<td></td>
<td>18;9 348</td>
<td>ACUTE RENAL FAILURE 57-63 SROC(9)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="even">
<td>142-148</td>
<td>7</td>
<td></td>
<td>18;10 349</td>
<td><p>URINARY TRACT INFECTION 64-70 SROC(10)</p>
<p>will not be used after SR*3*182</p></td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="odd">
<td>149-155</td>
<td>7</td>
<td></td>
<td>18;11 350</td>
<td>PULMONARY EDEMA 71-77 SROC(11)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="even">
<td>156-162</td>
<td>7</td>
<td></td>
<td>18;12 351</td>
<td>STROKE/CVA 78-84 SROC(12)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="odd">
<td>163-169</td>
<td>7</td>
<td></td>
<td>18;13 352</td>
<td>COMA&gt;24 HOURS 85-91 SROC(13)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="even">
<td>170-176</td>
<td>7</td>
<td></td>
<td>18;14 353</td>
<td>PERIPHERAL NERVE INJURY 92-98 SROC(14)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="odd">
<td>177-183</td>
<td>7</td>
<td></td>
<td>18;15 354</td>
<td>BLEEDING/TRANSFUSIONS 99-105 SROC(15)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="even">
<td>184-190</td>
<td>7</td>
<td></td>
<td>18;16 355</td>
<td><p>CARDIAC ARREST REQUIRING</p>
<p>CPR 106-112 SROC(16)</p></td>
<td>OCCURRENCE DATE</td>
</tr>
</tbody>
</table>

Line 5 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 23%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 5</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15</td>
<td>1</td>
<td>205;6 248</td>
<td>7;1 103</td>
<td>SUPERFICIAL INCISIONAL SSI - 1</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>16</td>
<td>1</td>
<td>205;7 249</td>
<td>7;2 104</td>
<td>DEEP INCISIONAL SSI - 2</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>17</td>
<td>1</td>
<td>205;8 404</td>
<td>7;30 299</td>
<td>WOUND DEHISCENCE - 22</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>18</td>
<td>1</td>
<td>205;10 251</td>
<td>7;4 106</td>
<td>PNEUMONIA - 4</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>19</td>
<td>1</td>
<td>205;11 412</td>
<td>7;34 296</td>
<td><p>UNPLANNED INTUBATION (Y/N) - 7</p>
<p>Will not to be used after SR*3*182</p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>20</td>
<td>1</td>
<td>205;12 252</td>
<td>7;5 107</td>
<td>PULMONARY EMBOLISM - 5</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>21</td>
<td>1</td>
<td>205;13 285</td>
<td>7;24 150</td>
<td>ON VENTILATOR &gt; 48 HOURS - 6</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>22-29</td>
<td>8</td>
<td>205;14 253</td>
<td>7;6 108</td>
<td>OTHER RESPIRATORY OCCURRENCE – 29</td>
<td>ICD Code</td>
</tr>
<tr class="odd">
<td>30</td>
<td>1</td>
<td>205;16 409</td>
<td>7;19 131</td>
<td>RENAL INSUFFICIENCY - 8</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>31</td>
<td>1</td>
<td>205;17 254</td>
<td>7;7 109</td>
<td>ACUTE RENAL FAILURE - 9</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>32</td>
<td>1</td>
<td>205;18 255</td>
<td>7;8 110</td>
<td><p>URINARY TRACT INFECTION - 10</p>
<p>Will not to be used after SR*3*182</p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>33-40</td>
<td>8</td>
<td>205;19 286</td>
<td>7;25 151</td>
<td>OTHER URINARY TRACT OCCURREN – 31</td>
<td>ICD Code</td>
</tr>
<tr class="odd">
<td>41</td>
<td>1</td>
<td>16;8 130.22,9</td>
<td>7;9 111</td>
<td>STROKE/CVA - 12</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>1 NO</p>
<p>SYMPTOMS</p>
<p>2 &lt;24</p>
<p>HOURS</p>
<p>3 24-72</p>
<p>HOURS</p>
<p>4 &gt;72</p>
<p>HOURS</p></td>
</tr>
<tr class="even">
<td>42</td>
<td>1</td>
<td>205;22 410</td>
<td>7;21 133</td>
<td>COMA &gt; 24 HOURS POSTOP - 13</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>43</td>
<td>1</td>
<td>205;23 287</td>
<td>7;26 152</td>
<td>PERIPHERAL NERVE INJURY - 14</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>44-51</td>
<td>8</td>
<td>205;24 343</td>
<td>7;29 221</td>
<td>OTHER CNS OCCURRENCE - 30</td>
<td>ICD Code</td>
</tr>
<tr class="odd">
<td>52</td>
<td>1</td>
<td>205;26 411</td>
<td>7;23 135</td>
<td>CARDIAC ARREST REQ CPR - 16</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>53</td>
<td>1</td>
<td>205;27 258</td>
<td>7;11 113</td>
<td>POSTOP MYOCARDIAL INFARCTION – 17</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>54</td>
<td>1</td>
<td>205;28 259</td>
<td>7;12 114</td>
<td>PULMONARY EDEMA - 11</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>55-62</td>
<td>8</td>
<td>205;29 344</td>
<td>7;31 223</td>
<td>OTHER CARDIAC OCCURRENCE - 32</td>
<td>ICD Code</td>
</tr>
<tr class="odd">
<td>63</td>
<td>1</td>
<td>205;31 345</td>
<td>7;32 224</td>
<td>ILEUS/BOWEL OBSTRUCTION - 18</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>64</td>
<td>1</td>
<td>205;32 257</td>
<td>7;10 112</td>
<td>POSTOP BLEEDING/TRANSFUSIONS – 15</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>65</td>
<td>1</td>
<td>205;33 261</td>
<td>7;14 116</td>
<td>GRAFT/PROSTHESIS FAILURE - 19</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>66</td>
<td>1</td>
<td>205;34 263</td>
<td>7;16 118</td>
<td>DVT/THROMBOPHLEBITIS - 20</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>67</td>
<td>1</td>
<td>205;35 250</td>
<td>7;3 105</td>
<td>SYSTEMIC SEPSIS - 3</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>68-75</td>
<td>8</td>
<td>205;36 392</td>
<td>7;33 279</td>
<td>OTHER OCCURRENCES (ICD9) - 21</td>
<td>ICD Code</td>
</tr>
<tr class="odd">
<td>76-82</td>
<td>7</td>
<td></td>
<td>18;17 356</td>
<td>MYOCARDIAL INFARCTION 113-119 SROC(17)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="even">
<td>83-89</td>
<td>7</td>
<td></td>
<td>18;18 357</td>
<td>ILEUS/BOWEL OBSTRUCTION 120-126 SROC(18)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="odd">
<td>90-96</td>
<td>7</td>
<td></td>
<td>18;19 358</td>
<td>GRAFT/PROSTHESIS/FLAP FAILURE 127-133 SROC(19)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="even">
<td>97-103</td>
<td>7</td>
<td></td>
<td>18;20 359</td>
<td>DVT/THROMBOPHLEBITIS 134-140 SROC(20)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="odd">
<td>104-110</td>
<td>7</td>
<td></td>
<td>18;21 360</td>
<td>OTHER OCCURRENCE 141-147 SROC(21)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="even">
<td>111-117</td>
<td>7</td>
<td></td>
<td>18;22 361</td>
<td>WOUND DISRUPTION 148-154 SROC(22)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="odd">
<td>118-124</td>
<td>7</td>
<td></td>
<td>18;23 362</td>
<td>OTHER RESPIRATORY OCCURRENCE 155-161 SROC(29)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="even">
<td>125-131</td>
<td>7</td>
<td></td>
<td>18;24 363</td>
<td>OTHER CNS OCCURRENCE 162-168 SROC(30)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="odd">
<td>132-138</td>
<td>7</td>
<td></td>
<td>18;25 364</td>
<td>OTHER URINARY TRACT OCCURRENC 169-175 SROC(31)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="even">
<td>139-145</td>
<td>7</td>
<td></td>
<td>18;26 365</td>
<td>OTHER CARDIAC OCCURRENCE 176-182 SROC(32)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="odd">
<td>146-152</td>
<td>7</td>
<td></td>
<td>19;7 426</td>
<td>ORGAN/SPACE SSI (DATE) 183-189 SROC(35)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="even">
<td>153-159</td>
<td>7</td>
<td></td>
<td>19;9 428</td>
<td>OTHER WOUND OCCURRENCE – DATE 190-196 SROC(36)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="odd">
<td>160</td>
<td>1</td>
<td>205;37 488</td>
<td>20;39 425</td>
<td>ORGAN/SPACE SSI (Y/N)</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>161-168</td>
<td>8</td>
<td>205;38 489</td>
<td>19;8 427</td>
<td>OTHER WOUND OCCURRENCE - ICD</td>
<td>ICD Code</td>
</tr>
<tr class="odd">
<td>169</td>
<td>1</td>
<td></td>
<td>19;10 429</td>
<td>POSTOP SEPSIS TYPE 204</td>
<td><p>2 SEPSIS</p>
<p>3 SEPTIC</p>
<p>SHOCK</p></td>
</tr>
<tr class="even">
<td>170</td>
<td>1</td>
<td>205;39 447</td>
<td>20;41 440</td>
<td>C. DIFFICILE COLITIS (Y/N)</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>171-177</td>
<td>7</td>
<td></td>
<td>19;11 441</td>
<td>C. DIFFICILE COLITIS – DATE 197-203 SROC(38)</td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="even">
<td>178</td>
<td>1</td>
<td>205;42 644</td>
<td>182;17 471</td>
<td>SYMPTOMATIC UTI – 40</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>179</td>
<td>1</td>
<td>205;43 645</td>
<td>182;18 472</td>
<td><p>MECHANICAL VENTILATION WITHIN 30 DAYS – 41</p>
<p>will not be used after SR*3*184</p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>180-186</td>
<td>7</td>
<td></td>
<td>182;15 469</td>
<td><p>SYMPTOMATIC UTI-CULTURE PLUS SIGN/SYMPTOM</p>
<p>206-212 SROC(40)</p></td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="odd">
<td>187-193</td>
<td>7</td>
<td></td>
<td>182;16 470</td>
<td><p>MECHANICAL VENTILATION WITHIN 30 DAYS</p>
<p>213-219 SROC(41)</p>
<p>will not be used after SR*3*184</p></td>
<td>OCCURRENCE DATE</td>
</tr>
<tr class="even">
<td>194</td>
<td>1</td>
<td>0;9 130.22,10</td>
<td>19;13 473</td>
<td>INDWELLING URETHRAL CATHETER</td>
<td><p>'1' YES, 1 YES, IN</p>
<p>PLACE</p>
<p>2 YES, REMOVED</p>
<p>3 NO, IN PLACE</p>
<p>4 NO, REMOVED</p>
<p>5 NO CATHETER</p></td>
</tr>
<tr class="odd">
<td>195</td>
<td>1</td>
<td>0;10 130.22,11</td>
<td>19;14 474</td>
<td>UTI SIGN/SYMPTOMS URG/FREQ/DYS</td>
<td><p>Y - HAS URGENCY,</p>
<p>FREQUENCY, OR</p>
<p>DYSURIA WITH NO</p>
<p>OTHER RECOGNIZED</p>
<p>CAUSE</p>
<p>N - DOES NOT HAVE</p>
<p>URGENCY,</p>
<p>FREQUENCY OR</p>
<p>DYSURIA</p></td>
</tr>
<tr class="even">
<td>196</td>
<td>1</td>
<td>0;11 130.22,12</td>
<td>19;15 475</td>
<td>UTI SIGNS/SYMPTOMS FEVER</td>
<td><p>Y - FEVER &gt; 38C AT</p>
<p>THE TIME OF</p>
<p>CULTURE OR ONSET</p>
<p>OF SYMPTOMS</p>
<p>N - NO FEVER &gt; 38C</p>
<p>AT THE TIME OF</p>
<p>CULTURE OR ONSET</p>
<p>OF SIGNS OR</p>
<p>SYMPTOMS</p></td>
</tr>
<tr class="odd">
<td>197</td>
<td>1</td>
<td>0;12 130.22,13</td>
<td>19;16 476</td>
<td>UTI SIGNS/SYMPTOMS TENDERNESS</td>
<td><p>Y - SUPRAPUBIC,</p>
<p>COSTOVERTEBRAL</p>
<p>ANGLE PAIN</p>
<p>N - NO SUPRAPUBIC</p>
<p>TENDERNESS,</p>
<p>COSTOVERTEBRA</p>
<p>L ANGLE PAIN</p></td>
</tr>
<tr class="even">
<td>198</td>
<td>1</td>
<td>0;13 130.22,14</td>
<td>19;17 477</td>
<td>UTI CULTURE</td>
<td><p>1 - POS CULTURE</p>
<p>&gt;10E5, 1-2</p>
<p>SPECIES</p>
<p>2 - POS CULTURE</p>
<p>10E3-10E5, 1-2</p>
<p>SPECIES</p>
<p>DIPSTICK(+),</p>
<p>PYURIA, OR GRAM</p>
<p>(+)</p></td>
</tr>
<tr class="odd">
<td>199</td>
<td>1</td>
<td>205;44 422</td>
<td>184;31 622</td>
<td>OUT-OF-OR UNPLANNED INTUBATION – 42</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>200-206</td>
<td>7</td>
<td></td>
<td>184;32 623</td>
<td><p>OUT-OF-OR UNPLANNED INTUB/DATE</p>
<p>226,232 SROC(42)</p></td>
<td>OCCURRENCE DATE</td>
</tr>
</tbody>
</table>

Line 6 of the Non-Cardiac Transmission Layout

<table style="width:100%;">
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 24%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 6</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-19</td>
<td>5</td>
<td>201;1 270</td>
<td>8;1 128</td>
<td>PREOPERATIVE SERUM SODIUM</td>
<td></td>
</tr>
<tr class="even">
<td>20-26</td>
<td>7</td>
<td>202;1 304</td>
<td>13;20 171</td>
<td>PREOP SERUM SODIUM, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>27-30</td>
<td>4</td>
<td>201;8 225</td>
<td>8;10 56</td>
<td>PREOPERATIVE SERUM ALBUMIN</td>
<td></td>
</tr>
<tr class="even">
<td>31-37</td>
<td>7</td>
<td>202;8 292</td>
<td>13;8 159</td>
<td>PREOP SERUM ALBUMIN, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>38-42</td>
<td>5</td>
<td>201;9 228</td>
<td>8;13 59</td>
<td>PREOPERATIVE TOTAL BILIRUBIN</td>
<td></td>
</tr>
<tr class="even">
<td>43-49</td>
<td>7</td>
<td>202;9 295</td>
<td>13;11 162</td>
<td>PREOP TOTAL BILIRUBIN, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>50-54</td>
<td>5</td>
<td>201;5 224</td>
<td>8;9 55</td>
<td>PREOPERATIVE BUN</td>
<td></td>
</tr>
<tr class="even">
<td>55-61</td>
<td>7</td>
<td>202;5 291</td>
<td>13;7 158</td>
<td>PREOPERATIVE BUN, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>62-65</td>
<td>4</td>
<td>201;4 223</td>
<td>8;8 54</td>
<td>PREOPERATIVE SERUM CREATININE</td>
<td></td>
</tr>
<tr class="even">
<td>66-72</td>
<td>7</td>
<td>202;4 290</td>
<td>13;6 157</td>
<td>PREOP SERUM CREATININE, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>73-77</td>
<td>5</td>
<td>201;27 487</td>
<td>9;6 66</td>
<td>PREOPERATIVE INR</td>
<td></td>
</tr>
<tr class="even">
<td>78-84</td>
<td>7</td>
<td>202;27 487.1</td>
<td>14;15 67</td>
<td>PREOPERATIVE INR, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>85-89</td>
<td>5</td>
<td>203;15 444</td>
<td>8;2 432</td>
<td>PREOPERATIVE ANION GAP (2006 update)</td>
<td></td>
</tr>
<tr class="even">
<td>90-96</td>
<td>7</td>
<td>204;15 444.1</td>
<td>13;1 433</td>
<td>PREOPERATIVE ANION GAP, DATE (2006 update)</td>
<td></td>
</tr>
</tbody>
</table>

Line 7 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 8%" />
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 23%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 7</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-26</td>
<td>12</td>
<td>208;14 418</td>
<td>8;1 320</td>
<td>HOSPITAL ADMISSION DATE</td>
<td><em>SRVADPT(7)</em></td>
</tr>
<tr class="even">
<td>27-28</td>
<td>2</td>
<td></td>
<td></td>
<td><em>- blank -</em></td>
<td></td>
</tr>
<tr class="odd">
<td>29-30</td>
<td>2</td>
<td>208;11 413</td>
<td>8;10 322</td>
<td>TRANSFER STATUS</td>
<td><p>1 NOT TRANSFERRED</p>
<p>2 NON-VAMC ACUTE</p>
<p>CARE HOSPITAL</p>
<p>3 VAMC ACUTE CARE</p>
<p>HOSPITAL</p>
<p>4 NON-VA</p>
<p>NURSING/CHRONIC CARE/SCI/INTERMEDIATE</p>
<p>CARE FACILITY</p>
<p>5 VA NURSING</p>
<p>HOME/CHRONIC CARE/SCI/INTERMEDIATE</p>
<p>CARE FACILITY</p>
<p>6 OTHER</p></td>
</tr>
<tr class="even">
<td>31-32</td>
<td>2</td>
<td>208;10 292</td>
<td>13;8 323</td>
<td>RACE</td>
<td></td>
</tr>
<tr class="odd">
<td>33-36</td>
<td>4</td>
<td>208;9 228</td>
<td>8;13 59</td>
<td><em>- blank - (PACK/YEARS removed in 2008 update)</em></td>
<td></td>
</tr>
<tr class="even">
<td>37-48</td>
<td>12</td>
<td>208;15 295</td>
<td>13;11 325</td>
<td>HOSPITAL DISCHARGE DATE</td>
<td><em>SRVADPT(8)</em></td>
</tr>
<tr class="odd">
<td>49-52</td>
<td>4</td>
<td></td>
<td></td>
<td><em>- blank -</em></td>
<td></td>
</tr>
<tr class="even">
<td>53-54</td>
<td>2</td>
<td>206;3 291</td>
<td>13;7 329</td>
<td>CHEMOTHERAPY &lt;= 30 DAYS</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="odd">
<td>55-56</td>
<td>2</td>
<td>206;4 223</td>
<td>8;8 330</td>
<td>RADIOTHERAPY &lt;= 90 DAYS</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="even">
<td>57-58</td>
<td>2</td>
<td>206;8 290</td>
<td>206;8 331</td>
<td>PREOPERATIVE SEPSIS</td>
<td><p>N NONE</p>
<p>2 SEPSIS</p>
<p>3 SEPTIC</p>
<p>SHOCK</p></td>
</tr>
<tr class="odd">
<td>59-60</td>
<td>2</td>
<td></td>
<td></td>
<td><em>- blank -</em></td>
<td></td>
</tr>
<tr class="even">
<td>61-72</td>
<td>12</td>
<td>208;16 420</td>
<td>32;2 321</td>
<td>TRANSFER DATE</td>
<td><em>SRVADPT(9)</em></td>
</tr>
<tr class="odd">
<td>73-84</td>
<td>12</td>
<td>208;17 421</td>
<td>32;5 324</td>
<td>SURGERY DISCHARGE DATE</td>
<td><em>SRVADPT(10)</em></td>
</tr>
<tr class="even">
<td>85-96</td>
<td>12</td>
<td>.2;12 .232</td>
<td>32;10 334</td>
<td>TIME PATIENT LEAVES OR</td>
<td></td>
</tr>
<tr class="odd">
<td>97-108</td>
<td>12</td>
<td>.2;1 .21</td>
<td>32;11 335</td>
<td>ANESTHESIA CARE START TIME</td>
<td></td>
</tr>
<tr class="even">
<td>109-120</td>
<td>12</td>
<td>1.1;8 1.18</td>
<td>32;12 336</td>
<td>PACU DISCHARGE TIME</td>
<td></td>
</tr>
<tr class="odd">
<td>121-132</td>
<td>12</td>
<td>208.1;1 452</td>
<td>32;13 337</td>
<td>OBSERVATION ADMISSION DATE</td>
<td><em>SRVADPT(12)</em></td>
</tr>
<tr class="even">
<td>133-144</td>
<td>12</td>
<td>208.1;2 453</td>
<td>32;14 338</td>
<td>OBSERVATION DISCHARGE DATE</td>
<td><em>SRVADPT(13)</em></td>
</tr>
<tr class="odd">
<td>145-147</td>
<td>3</td>
<td>208.1;3 454</td>
<td>32;15 339</td>
<td>OBSERVATION TREATING SPECIALTY</td>
<td><em>SRVADPT(14)</em></td>
</tr>
<tr class="even">
<td>148-157</td>
<td>10</td>
<td>CON;1 35</td>
<td>CON;5 15</td>
<td>CONCURRENT CASE</td>
<td></td>
</tr>
<tr class="odd">
<td>158-169</td>
<td>12</td>
<td>.2;4 .24</td>
<td>32;16 335.5</td>
<td>ANESTHESIA CARE END TIME</td>
<td></td>
</tr>
</tbody>
</table>

Line 8 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 24%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 8</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-19</td>
<td>5</td>
<td>201;11 227</td>
<td>8;12 58</td>
<td>PREOPERATIVE SGOT</td>
<td></td>
</tr>
<tr class="even">
<td>20-26</td>
<td>7</td>
<td>202;11 294</td>
<td>13;10 161</td>
<td>SGOT, DATE PERFORMED</td>
<td></td>
</tr>
<tr class="odd">
<td>27-31</td>
<td>5</td>
<td>201;12 229</td>
<td>8;14 60</td>
<td>PREOPERATIVE ALK PHOSPHATASE</td>
<td></td>
</tr>
<tr class="even">
<td>32-38</td>
<td>7</td>
<td>202;12 296</td>
<td>13;12 163</td>
<td>PREOP ALK PHOSPHATASE, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>39-42</td>
<td>4</td>
<td>201;13 230</td>
<td>9;1 61</td>
<td>PREOPERATIVE WBC</td>
<td></td>
</tr>
<tr class="even">
<td>43-49</td>
<td>7</td>
<td>202;13 297</td>
<td>13;13 164</td>
<td>PREOPERATIVE WBC, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>50-53</td>
<td>4</td>
<td>201;14 234</td>
<td>9;5 65</td>
<td>PREOPERATIVE HEMATOCRIT</td>
<td></td>
</tr>
<tr class="even">
<td>54-60</td>
<td>7</td>
<td>202;14 301</td>
<td>13;17 168</td>
<td>PREOP HEMATOCRIT, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>61-65</td>
<td>5</td>
<td>201;15 231</td>
<td>9;2 62</td>
<td>PREOPERATIVE PLATELET COUNT</td>
<td></td>
</tr>
<tr class="even">
<td>66-72</td>
<td>7</td>
<td>202;15 298</td>
<td>13;14 165</td>
<td>PREOP PLATELET COUNT, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>73-78</td>
<td>6</td>
<td>201;28 504</td>
<td>8;3 438</td>
<td>HEMOGLOBIN A1C</td>
<td></td>
</tr>
<tr class="even">
<td>79-85</td>
<td>7</td>
<td>202.1;1 504.1</td>
<td>13;2 439</td>
<td>HEMOGLOBIN A1C, DATE</td>
<td></td>
</tr>
</tbody>
</table>

Line 9 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 24%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 9</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-19</td>
<td>5</td>
<td>201;16 233</td>
<td>9;4 64</td>
<td>PREOPERATIVE PTT</td>
<td></td>
</tr>
<tr class="even">
<td>20-26</td>
<td>7</td>
<td>202;16 300</td>
<td>13;16 167</td>
<td>PREOPERATIVE PTT, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>27-30</td>
<td>4</td>
<td>201;17 232</td>
<td>9;3 63</td>
<td>PREOPERATIVE PT</td>
<td></td>
</tr>
<tr class="even">
<td>31-37</td>
<td>7</td>
<td>202;17 299</td>
<td>13;15 166</td>
<td>PREOPERATIVE PT, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>38-42</td>
<td>5</td>
<td>203;1 274</td>
<td>12;1 139</td>
<td>HIGHEST SERUM SODIUM</td>
<td></td>
</tr>
<tr class="even">
<td>43-49</td>
<td>7</td>
<td>204;1 305</td>
<td>14;1 172</td>
<td>HIGH SERUM SODIUM, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>50-54</td>
<td>5</td>
<td>203;2 405</td>
<td>12;11 301</td>
<td>LOW SERUM SODIUM</td>
<td></td>
</tr>
<tr class="even">
<td>55-61</td>
<td>7</td>
<td>204;2 407</td>
<td>14;11 303</td>
<td>LOW SODIUM, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>62-66</td>
<td>5</td>
<td>203;16 445</td>
<td>12;15 434</td>
<td>HIGHEST ANION GAP (2006 update)</td>
<td></td>
</tr>
<tr class="even">
<td>67-73</td>
<td>7</td>
<td>204;16 445.1</td>
<td>14;16 435</td>
<td>HIGH ANION GAP, DATE (2006 update)</td>
<td></td>
</tr>
</tbody>
</table>

Line 10 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 24%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 10</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-17</td>
<td>3</td>
<td>203;3 275</td>
<td>12;2 140</td>
<td>HIGHEST POTASSIUM</td>
<td></td>
</tr>
<tr class="even">
<td>18-24</td>
<td>7</td>
<td>204;3 306</td>
<td>14;2 173</td>
<td>HIGH POTASSIUM, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>25-27</td>
<td>3</td>
<td>203;4 406</td>
<td>12;12 302</td>
<td>LOW POTASSIUM</td>
<td></td>
</tr>
<tr class="even">
<td>28-34</td>
<td>7</td>
<td>204;4 408</td>
<td>14;12 304</td>
<td>LOW POTASSIUM, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>35-38</td>
<td>4</td>
<td>203;6 277</td>
<td>12;4 142</td>
<td>HIGHEST SERUM CREATININE</td>
<td></td>
</tr>
<tr class="even">
<td>39-45</td>
<td>7</td>
<td>204;6 308</td>
<td>14;4 175</td>
<td>HIGH SERUM CREATININE, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>46-51</td>
<td>6</td>
<td>203;7 278</td>
<td>12;5 143</td>
<td>HIGHEST CPK</td>
<td></td>
</tr>
<tr class="even">
<td>52-58</td>
<td>7</td>
<td>204;7 309</td>
<td>14;5 176</td>
<td>HIGH CPK, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>59-60</td>
<td>2</td>
<td>OP;3 2006</td>
<td>OP;4 2006</td>
<td>ROBOTIC ASSISTANCE (Y/N)</td>
<td><p>Y Yes</p>
<p>N No</p></td>
</tr>
</tbody>
</table>

Line 11 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 24%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 11</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-18</td>
<td>4</td>
<td>203;8 279</td>
<td>12;6 144</td>
<td>HIGHEST CPK-MB</td>
<td></td>
</tr>
<tr class="even">
<td>19-25</td>
<td>7</td>
<td>204;8 310</td>
<td>14;6 177</td>
<td>HIGH CPK-MB, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>26-30</td>
<td>5</td>
<td>203;9 280</td>
<td>12;7 145</td>
<td>HIGHEST TOTAL BILIRUBIN</td>
<td></td>
</tr>
<tr class="even">
<td>31-37</td>
<td>7</td>
<td>204;9 311</td>
<td>14;7 178</td>
<td>HIGH TOTAL BILIRUBIN, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>38-41</td>
<td>4</td>
<td>203;10 281</td>
<td>12;8 146</td>
<td>HIGHEST WBC</td>
<td></td>
</tr>
<tr class="even">
<td>42-48</td>
<td>7</td>
<td>204;10 312</td>
<td>14;8 179</td>
<td>HIGHEST WBC, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>49-52</td>
<td>4</td>
<td>203;12 283</td>
<td>12;10 148</td>
<td>LOWEST HEMATOCRIT</td>
<td></td>
</tr>
<tr class="even">
<td>53-59</td>
<td>7</td>
<td>204;12 314</td>
<td>14;10 181</td>
<td>LOW HEMATOCRIT, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>60-64</td>
<td>5</td>
<td>203;13 455</td>
<td>12;13 414</td>
<td>HIGHEST SERUM TROPONIN I</td>
<td></td>
</tr>
<tr class="even">
<td>65-71</td>
<td>7</td>
<td>204;13 455.1</td>
<td>14;13 416</td>
<td>HIGHEST SERUM TROPONIN I, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>72-76</td>
<td>5</td>
<td>203;14 456</td>
<td>12;14 415</td>
<td>HIGHEST SERUM TROPONIN T</td>
<td></td>
</tr>
<tr class="even">
<td>77-83</td>
<td>7</td>
<td>204;14 456.1</td>
<td>14;14 417</td>
<td>HIGHEST SERUM TROPONIN T, DATE</td>
<td></td>
</tr>
</tbody>
</table>

Line 12 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 21%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 12</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 136/130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-19</td>
<td>5</td>
<td>0;2(136) .02</td>
<td>OP;2 8</td>
<td>PRINCIPAL CPT CODE</td>
<td></td>
</tr>
<tr class="even">
<td>20-24</td>
<td>5</td>
<td>CON;1(130) 35</td>
<td>CON;2 95</td>
<td>CONCURRENT PROCEDURE CPT CODE</td>
<td></td>
</tr>
<tr class="odd">
<td>25-29</td>
<td>5</td>
<td></td>
<td>CON;4 290</td>
<td>- blank -</td>
<td></td>
</tr>
<tr class="even">
<td>30-34</td>
<td>5</td>
<td>3;1 136.03,.01</td>
<td>11;2 139.017,1</td>
<td>OTHER PROCEDURE CPT CODE #1</td>
<td></td>
</tr>
<tr class="odd">
<td>35-39</td>
<td>5</td>
<td>3;1 136.03,.01</td>
<td>11;2 139.017,1</td>
<td>OTHER PROCEDURE CPT CODE #2</td>
<td></td>
</tr>
<tr class="even">
<td>40-44</td>
<td>5</td>
<td>3;1 136.03,.01</td>
<td>11;2 139.017,1</td>
<td>OTHER PROCEDURE CPT CODE #3</td>
<td></td>
</tr>
<tr class="odd">
<td>45-49</td>
<td>5</td>
<td>3;1 136.03,.01</td>
<td>11;2 139.017,1</td>
<td>OTHER PROCEDURE CPT CODE #4</td>
<td></td>
</tr>
<tr class="even">
<td>50-54</td>
<td>5</td>
<td>3;1 136.03,.01</td>
<td>11;2 139.017,1</td>
<td>OTHER PROCEDURE CPT CODE #5</td>
<td></td>
</tr>
<tr class="odd">
<td>55-59</td>
<td>5</td>
<td>3;1 136.03,.01</td>
<td>11;2 139.017,1</td>
<td>OTHER PROCEDURE CPT CODE #6</td>
<td></td>
</tr>
<tr class="even">
<td>60-64</td>
<td>5</td>
<td>3;1 136.03,.01</td>
<td>11;2 139.017,1</td>
<td>OTHER PROCEDURE CPT CODE #7</td>
<td></td>
</tr>
<tr class="odd">
<td>65-69</td>
<td>5</td>
<td>3;1 136.03,.01</td>
<td>11;2 139.017,1</td>
<td>OTHER PROCEDURE CPT CODE #8</td>
<td></td>
</tr>
<tr class="even">
<td>70-74</td>
<td>5</td>
<td>3;1 136.03,.01</td>
<td>11;2 139.017,1</td>
<td>OTHER PROCEDURE CPT CODE #9</td>
<td></td>
</tr>
<tr class="odd">
<td>75-79</td>
<td>5</td>
<td>3;1 136.03,.01</td>
<td>11;2 139.017,1</td>
<td>OTHER PROCEDURE CPT CODE #10</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>1;1 136.01,.01</td>
<td>OP;3 8.1</td>
<td>PRIN. PROCEDURE CPT MODIFIERS</td>
<td></td>
</tr>
<tr class="odd">
<td>80-81</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="even">
<td>82-83</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="odd">
<td>84-85</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="even">
<td>86-87</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="odd">
<td>88-89</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>1;1 136.01,.01</td>
<td>CON;6 95.1</td>
<td>CONCURRENT CASE CPT MODIFIERS</td>
<td></td>
</tr>
<tr class="odd">
<td>90-91</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="even">
<td>92-93</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="odd">
<td>94-95</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="even">
<td>96-97</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="odd">
<td>98-99</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>3,1;1 136.31,.01</td>
<td>11;3 139.017,2</td>
<td><p>OTHER PROCEDURE CPT MODIFIERS</p>
<p>For OTHER PROCEDURE CPT #1</p></td>
<td></td>
</tr>
<tr class="odd">
<td>100-101</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="even">
<td>102-103</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="odd">
<td>104-105</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="even">
<td>106-107</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="odd">
<td>108-109</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>3,1;1 136.31,.01</td>
<td>11;3 139.017,2</td>
<td><p>OTHER PROCEDURE CPT MODIFIERS</p>
<p>For OTHER PROCEDURE CPT #2</p></td>
<td></td>
</tr>
<tr class="odd">
<td>110-111</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="even">
<td>112-113</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="odd">
<td>114-115</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="even">
<td>116-117</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="odd">
<td>118-119</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>3,1;1 136.31,.01</td>
<td>11;3 139.017,2</td>
<td><p>OTHER PROCEDURE CPT MODIFIERS</p>
<p>For OTHER PROCEDURE CPT #3</p></td>
<td></td>
</tr>
<tr class="odd">
<td>120-121</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="even">
<td>122-123</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="odd">
<td>124-125</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="even">
<td>126-127</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="odd">
<td>128-129</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>3,1;1 136.31,.01</td>
<td>11;3 139.017,2</td>
<td><p>OTHER PROCEDURE CPT MODIFIERS</p>
<p>For OTHER PROCEDURE CPT #4</p></td>
<td></td>
</tr>
<tr class="odd">
<td>130-131</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="even">
<td>132-133</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="odd">
<td>134-135</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="even">
<td>136-137</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="odd">
<td>138-139</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>3,1;1 136.31,.01</td>
<td>11;3 139.017,2</td>
<td><p>OTHER PROCEDURE CPT MODIFIERS</p>
<p>For OTHER PROCEDURE CPT #5</p></td>
<td></td>
</tr>
<tr class="odd">
<td>140-141</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="even">
<td>142-143</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="odd">
<td>144-145</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="even">
<td>146-147</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="odd">
<td>148-149</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>3,1;1 136.31,.01</td>
<td>11;3 139.017,2</td>
<td><p>OTHER PROCEDURE CPT MODIFIERS</p>
<p>For OTHER PROCEDURE CPT #6</p></td>
<td></td>
</tr>
<tr class="odd">
<td>150-151</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="even">
<td>152-153</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="odd">
<td>154-155</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="even">
<td>156-157</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="odd">
<td>158-159</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>3,1;1 136.31,.01</td>
<td>11;3 139.017,2</td>
<td><p>OTHER PROCEDURE CPT MODIFIERS</p>
<p>For OTHER PROCEDURE CPT #7</p></td>
<td></td>
</tr>
<tr class="odd">
<td>160-161</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="even">
<td>162-163</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="odd">
<td>164-165</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="even">
<td>166-167</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="odd">
<td>168-169</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>3,1;1 136.31,.01</td>
<td>11;3 139.017,2</td>
<td><p>OTHER PROCEDURE CPT MODIFIERS</p>
<p>For OTHER PROCEDURE CPT #8</p></td>
<td></td>
</tr>
<tr class="odd">
<td>170-171</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="even">
<td>172-173</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="odd">
<td>174-175</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="even">
<td>176-177</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="odd">
<td>178-179</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>3,1;1 136.31,.01</td>
<td>11;3 139.017,2</td>
<td><p>OTHER PROCEDURE CPT MODIFIERS</p>
<p>For OTHER PROCEDURE CPT #9</p></td>
<td></td>
</tr>
<tr class="odd">
<td>180-181</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="even">
<td>182-183</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="odd">
<td>184-185</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="even">
<td>186-187</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="odd">
<td>188-189</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>3,1;1 136.31,.01</td>
<td>11;3 139.017,2</td>
<td><p>OTHER PROCEDURE CPT MODIFIERS</p>
<p>For OTHER PROCEDURE CPT #10</p></td>
<td></td>
</tr>
<tr class="odd">
<td>190-191</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="even">
<td>192-193</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="odd">
<td>194-195</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="even">
<td>196-197</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="odd">
<td>198-199</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
</tbody>
</table>

Line 13 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 18%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 13</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15</td>
<td>1</td>
<td>VADM(11</td>
<td>20;36 420</td>
<td>ETHNICITY</td>
<td><p>D DECLINED</p>
<p>TO ANSWER</p>
<p>H HISPANIC</p>
<p>OR LATINO</p>
<p>N NOT</p>
<p>HISPANIC</p>
<p>OR LATINO</p>
<p>U UNKNOWN BY</p>
<p>PATIENT</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>21;2 139.0421,2</td>
<td>RACE CODES</td>
<td></td>
</tr>
<tr class="odd">
<td>16</td>
<td>1</td>
<td></td>
<td></td>
<td>RACE CODE #1</td>
<td><p>3 AMERICAN INDIAN</p>
<p>OR ALASKA NATIVE</p>
<p>A NATIVE HAWAIIAN</p>
<p>OR OTHER PACIFIC</p>
<p>ISLANDER</p>
<p>9 BLACK OR</p>
<p>AFRICAN AMERICAN</p>
<p>8 ASIAN</p>
<p>B WHITE</p>
<p>C DECLINED TO</p>
<p>ANSWER/UNANSWERED</p>
<p>D UNKNOWN BY</p>
<p>PATIENT</p></td>
</tr>
<tr class="even">
<td>17</td>
<td>1</td>
<td></td>
<td></td>
<td>RACE CODE #2</td>
<td><p>3 AMERICAN INDIAN</p>
<p>OR ALASKA NATIVE</p>
<p>A NATIVE HAWAIIAN</p>
<p>OR OTHER PACIFIC</p>
<p>ISLANDER</p>
<p>9 BLACK OR</p>
<p>AFRICAN AMERICAN</p>
<p>8 ASIAN</p>
<p>B WHITE</p>
<p>C DECLINED TO</p>
<p>ANSWER/UNANSWERED</p>
<p>D UNKNOWN BY</p>
<p>PATIENT</p></td>
</tr>
<tr class="odd">
<td>18</td>
<td>1</td>
<td></td>
<td></td>
<td>RACE CODE #3</td>
<td><p>3 AMERICAN INDIAN</p>
<p>OR ALASKA NATIVE</p>
<p>A NATIVE HAWAIIAN</p>
<p>OR OTHER PACIFIC</p>
<p>ISLANDER</p>
<p>9 BLACK OR</p>
<p>AFRICAN AMERICAN</p>
<p>8 ASIAN</p>
<p>B WHITE</p>
<p>C DECLINED TO</p>
<p>ANSWER/UNANSWERED</p>
<p>D UNKNOWN BY</p>
<p>PATIENT</p></td>
</tr>
<tr class="even">
<td>19</td>
<td>1</td>
<td></td>
<td></td>
<td>RACE CODE #4</td>
<td><p>3 AMERICAN INDIAN</p>
<p>OR ALASKA NATIVE</p>
<p>A NATIVE HAWAIIAN</p>
<p>OR OTHER PACIFIC</p>
<p>ISLANDER</p>
<p>9 BLACK OR</p>
<p>AFRICAN AMERICAN</p>
<p>8 ASIAN</p>
<p>B WHITE</p>
<p>C DECLINED TO</p>
<p>ANSWER/UNANSWERED</p>
<p>D UNKNOWN BY</p>
<p>PATIENT</p></td>
</tr>
<tr class="odd">
<td>20</td>
<td>1</td>
<td></td>
<td></td>
<td>RACE CODE #5</td>
<td><p>3 AMERICAN INDIAN</p>
<p>OR ALASKA NATIVE</p>
<p>A NATIVE HAWAIIAN</p>
<p>OR OTHER PACIFIC</p>
<p>ISLANDER</p>
<p>9 BLACK OR</p>
<p>AFRICAN AMERICAN</p>
<p>8 ASIAN</p>
<p>B WHITE</p>
<p>C DECLINED TO</p>
<p>ANSWER/UNANSWERED</p>
<p>D UNKNOWN BY</p>
<p>PATIENT</p></td>
</tr>
<tr class="even">
<td>21</td>
<td>1</td>
<td></td>
<td></td>
<td>RACE CODE #6</td>
<td><p>3 AMERICAN INDIAN</p>
<p>OR ALASKA NATIVE</p>
<p>A NATIVE HAWAIIAN</p>
<p>OR OTHER PACIFIC</p>
<p>ISLANDER</p>
<p>9 BLACK OR</p>
<p>AFRICAN AMERICAN</p>
<p>8 ASIAN</p>
<p>B WHITE</p>
<p>C DECLINED TO</p>
<p>ANSWER/UNANSWERED</p>
<p>D UNKNOWN BY</p>
<p>PATIENT</p></td>
</tr>
<tr class="odd">
<td>22</td>
<td>1</td>
<td></td>
<td></td>
<td>RACE CODE #7</td>
<td><p>3 AMERICAN INDIAN</p>
<p>OR ALASKA NATIVE</p>
<p>A NATIVE HAWAIIAN</p>
<p>OR OTHER PACIFIC</p>
<p>ISLANDER</p>
<p>9 BLACK OR</p>
<p>AFRICAN AMERICAN</p>
<p>8 ASIAN</p>
<p>B WHITE</p>
<p>C DECLINED TO</p>
<p>ANSWER/UNANSWERED</p>
<p>D UNKNOWN BY</p>
<p>PATIENT</p></td>
</tr>
<tr class="even">
<td>23</td>
<td>1</td>
<td></td>
<td></td>
<td>RACE CODE #8</td>
<td><p>3 AMERICAN INDIAN</p>
<p>OR ALASKA NATIVE</p>
<p>A NATIVE HAWAIIAN</p>
<p>OR OTHER PACIFIC</p>
<p>ISLANDER</p>
<p>9 BLACK OR</p>
<p>AFRICAN AMERICAN</p>
<p>8 ASIAN</p>
<p>B WHITE</p>
<p>C DECLINED TO</p>
<p>ANSWER/UNANSWERED</p>
<p>D UNKNOWN BY</p>
<p>PATIENT</p></td>
</tr>
<tr class="odd">
<td>24</td>
<td>1</td>
<td></td>
<td></td>
<td>RACE CODE #9</td>
<td><p>3 AMERICAN INDIAN</p>
<p>OR ALASKA NATIVE</p>
<p>A NATIVE HAWAIIAN</p>
<p>OR OTHER PACIFIC</p>
<p>ISLANDER</p>
<p>9 BLACK OR</p>
<p>AFRICAN AMERICAN</p>
<p>8 ASIAN</p>
<p>B WHITE</p>
<p>C DECLINED TO</p>
<p>ANSWER/UNANSWERED</p>
<p>D UNKNOWN BY</p>
<p>PATIENT</p></td>
</tr>
<tr class="even">
<td>25</td>
<td>1</td>
<td></td>
<td></td>
<td>RACE CODE #10</td>
<td><p>3 AMERICAN INDIAN</p>
<p>OR ALASKA NATIVE</p>
<p>A NATIVE HAWAIIAN</p>
<p>OR OTHER PACIFIC</p>
<p>ISLANDER</p>
<p>9 BLACK OR</p>
<p>AFRICAN AMERICAN</p>
<p>8 ASIAN</p>
<p>B WHITE</p>
<p>C DECLINED TO</p>
<p>ANSWER/UNANSWERED</p>
<p>D UNKNOWN BY</p>
<p>PATIENT</p></td>
</tr>
<tr class="odd">
<td>26-60</td>
<td>35</td>
<td>RA;9 272.1</td>
<td></td>
<td><p>ASSESSMENT</p>
<p>COMPLETED BY</p></td>
<td></td>
</tr>
<tr class="even">
<td>61-72</td>
<td>12</td>
<td>.9;1 612</td>
<td>.9;1 612</td>
<td>ORIGINAL DESIRED PROCEDURE DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>73-84</td>
<td>12</td>
<td>.9;2 613</td>
<td>.9;2 613</td>
<td>D/T OF DESIRED PROCEDURE DATE ENTRY</td>
<td></td>
</tr>
<tr class="even">
<td>85-96</td>
<td>12</td>
<td>.9;3 614</td>
<td>.9;3 614</td>
<td>ORIGINAL SCHEDULED DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>97-108</td>
<td>12</td>
<td>.9;4 615</td>
<td>.9;4 615</td>
<td>D/T OF SCHEDULED DATE ENTRY</td>
<td></td>
</tr>
<tr class="even">
<td>109-120</td>
<td>12</td>
<td>.9;5 616</td>
<td>.9;5 616</td>
<td>DESIRED PROCEDURE DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>121-132</td>
<td>12</td>
<td>.9;6 617</td>
<td>.9;6 617</td>
<td>SCHEDULED DATE</td>
<td></td>
</tr>
<tr class="even">
<td>133-134</td>
<td>2</td>
<td>VER;7 600</td>
<td>VER;7 600</td>
<td>CONFIRM PATIENT IDENTITY</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>135-136</td>
<td>2</td>
<td>VER;8 601</td>
<td>VER;8 601</td>
<td>PROCEDURE TO BE PERFORMED</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>137-138</td>
<td>2</td>
<td>VER;9 602</td>
<td>VER;9 602</td>
<td>SITE OF PROCEDURE</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>139-140</td>
<td>2</td>
<td>VER;10 603</td>
<td>VER;10 603</td>
<td>VALID CONSENT FORM</td>
<td><p>1 YES, i-MED</p>
<p>2 YES, PAPER</p>
<p>3 YES,</p>
<p>TELEPHONE</p>
<p>4 NO,</p>
<p>EMERGENCY</p>
<p>5 NO, NOT</p>
<p>EMERGENCY</p></td>
</tr>
<tr class="even">
<td>141-142</td>
<td>2</td>
<td>VER;11 604</td>
<td>VER;11 604</td>
<td>CONFIRM PATIENT POSITION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>143-144</td>
<td>2</td>
<td>VER;12 605</td>
<td>VER;12 605</td>
<td>MARKED SITE CONFIRMED</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>145-146</td>
<td>2</td>
<td>VER;13 606</td>
<td>VER;13 606</td>
<td>PREOPERATIVE IMAGES CONFIRMED</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT</p>
<p>APPLICABLE</p></td>
</tr>
<tr class="odd">
<td>147-148</td>
<td>2</td>
<td>VER;14 607</td>
<td>VER;14 607</td>
<td>CORRECT MEDICAL IMPLANTS</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT</p>
<p>APPLICABLE</p></td>
</tr>
<tr class="even">
<td>149-150</td>
<td>2</td>
<td>VER;15 608</td>
<td>VER;15 608</td>
<td>ANTIBIOTIC PROPHYLAXIS</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NI NOT</p>
<p>INDICATED</p></td>
</tr>
<tr class="odd">
<td>151-152</td>
<td>2</td>
<td>VER;16 609</td>
<td>VER;16 609</td>
<td>APPROPRIATE DVT PROPHYLAXIS</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NI NOT</p>
<p>INDICATED</p></td>
</tr>
<tr class="even">
<td>153-154</td>
<td>2</td>
<td>VER;17 610</td>
<td>VER;17 610</td>
<td>BLOOD AVAILABILITY</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NI NOT</p>
<p>INDICATED</p></td>
</tr>
<tr class="odd">
<td>155-156</td>
<td>2</td>
<td>VER;18 611</td>
<td>VER;18 611</td>
<td>AVAILABILITY OF SPECIAL EQUIP</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT</p>
<p>APPLICABLE</p></td>
</tr>
</tbody>
</table>

Line 14 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 18%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 14</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-21</td>
<td>7</td>
<td>130.0647,.01</td>
<td>184;15 134</td>
<td>ORGAN TO BE TRANSPLANTED</td>
<td><p>1 HEART, 2 LUNG, 3 KIDNEY</p>
<p>4 LIVER, 5 PANCREAS</p>
<p>6 INTESTINE, 7 OTHER</p></td>
</tr>
<tr class="even">
<td>22-31</td>
<td>10</td>
<td>VER1;2 648</td>
<td>184;16 137</td>
<td>UNOS NUMBER</td>
<td>1-10 chars</td>
</tr>
<tr class="odd">
<td>32-33</td>
<td>2</td>
<td>VER1;3 649</td>
<td>184;17 154</td>
<td>DONOR SEROLOGY HCV</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="even">
<td>34-35</td>
<td>2</td>
<td>VER1;4 650</td>
<td>184;18 186</td>
<td>DONOR SEROLOGY HBV</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="odd">
<td>36-37</td>
<td>2</td>
<td>VER1;5 651</td>
<td>184;19 199</td>
<td>DONOR SEROLOGY CMV</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="even">
<td>38-39</td>
<td>2</td>
<td>VER1;6 652</td>
<td>184;20 205</td>
<td>DONOR SEROLOGY HIV</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="odd">
<td>40</td>
<td>1</td>
<td>VER1;7 653</td>
<td>184;21 214</td>
<td>DONOR ABO TYPE</td>
<td><p>1 A RH(+)</p>
<p>2 A RH(-)</p>
<p>3 B RH(+)</p>
<p>4 B RH(-)</p>
<p>5 AB RH(+)</p>
<p>6 AB RH(-)</p>
<p>7 O RH(+)</p>
<p>8 O RH(-)</p></td>
</tr>
<tr class="even">
<td>41</td>
<td>1</td>
<td>VER1;8 654</td>
<td>184;22 215</td>
<td>RECIPIENT ABO TYPE</td>
<td><p>1 A RH(+)</p>
<p>2 A RH(-)</p>
<p>3 B RH(+)</p>
<p>4 B RH(-)</p>
<p>5 AB RH(+)</p>
<p>6 AB RH(-)</p>
<p>7 O RH(+)</p>
<p>8 O RH(-)</p></td>
</tr>
<tr class="odd">
<td>42</td>
<td>1</td>
<td>VER1;9 655</td>
<td>184;23 220</td>
<td>BLOOD BANK ABO VERIFICATION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>43-54</td>
<td>12</td>
<td>VER1;19 747</td>
<td>182;31 640</td>
<td>D/T BLOOD BANK ABO VERIF</td>
<td>Date/time</td>
</tr>
<tr class="odd">
<td>55</td>
<td>1</td>
<td>VER1;10 656</td>
<td>184;24 222</td>
<td>OR ABO VERIFICATION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>56-67</td>
<td>12</td>
<td>VER1;21 749</td>
<td>184;33 624</td>
<td>D/T OR ABO VERIF</td>
<td>Date/time</td>
</tr>
<tr class="odd">
<td>68</td>
<td>1</td>
<td>VER1;22 750</td>
<td>184;35 626</td>
<td>UNET VERIF BY SURGEON</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>69</td>
<td>1</td>
<td>VER1;12 658</td>
<td>184;36 627</td>
<td>ORGAN VER PRE-ANESTHESIA</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>70-71</td>
<td>2</td>
<td>VER1;24 752</td>
<td>182;21 630</td>
<td>DONOR ORG VER PRE-ANES</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="even">
<td>72-73</td>
<td>2</td>
<td>VER1;14 660</td>
<td>182;22 631</td>
<td>ORGAN VER PRE-TRANSPLANT</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="odd">
<td>74</td>
<td>1</td>
<td>VER1;15 663</td>
<td>184;29 233</td>
<td>DONOR VESSEL USAGE</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>75-76</td>
<td>2</td>
<td>VER1;16 665</td>
<td>184;30 234</td>
<td><p>DONOR VESSEL DISPOSITION</p>
<p>Updated with SR*3*205</p></td>
<td><p>N NO DONOR VESSELS</p>
<p>RECEIVED</p>
<p>D DISCARDED</p>
<p>R RETURNED TO OPO</p>
<p>S STORED</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="odd">
<td>77-106</td>
<td>30</td>
<td>VER1;11 657</td>
<td>184;34 625</td>
<td>SURGEON VERIFYING UNET</td>
<td>Name field</td>
</tr>
<tr class="even">
<td>107-136</td>
<td>30</td>
<td>VER1;23 751</td>
<td>184;37 628</td>
<td>SURGEON VER ORGAN PRE-ANES</td>
<td>Name field</td>
</tr>
<tr class="odd">
<td>137-166</td>
<td>30</td>
<td>VER1;13 659</td>
<td>182;20 629</td>
<td>SURGEON VER DONOR ORG PRE-ANES</td>
<td>Name field</td>
</tr>
<tr class="even">
<td>167-196</td>
<td>30</td>
<td>VER1;25 753</td>
<td>182;23 632</td>
<td>SURGEON VER ORG PRE-TRANSPLANT</td>
<td>Name field</td>
</tr>
</tbody>
</table>

Line 15 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 18%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 15</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-24</td>
<td>10</td>
<td><p>57;0 Multiple</p>
<p>#130.0664</p></td>
<td>182;24 633</td>
<td>DONOR VESSEL UNOS ID – Entry #1</td>
<td>1-10 chars Free-Text</td>
</tr>
<tr class="even">
<td>25-34</td>
<td>10</td>
<td><p>57;0 Multiple</p>
<p>#130.0664</p></td>
<td>182;25 634</td>
<td>DONOR VESSEL UNOS ID – Entry #2</td>
<td>1-10 chars Free-Text</td>
</tr>
<tr class="odd">
<td>35-44</td>
<td>10</td>
<td><p>57;0 Multiple</p>
<p>#130.0664</p></td>
<td>182;26 635</td>
<td>DONOR VESSEL UNOS ID – Entry #3</td>
<td>1-10 chars Free-Text</td>
</tr>
<tr class="even">
<td>45-54</td>
<td>10</td>
<td><p>57;0 Multiple</p>
<p>#130.0664</p></td>
<td>182;27 636</td>
<td>DONOR VESSEL UNOS ID – Entry #4</td>
<td>1-10 chars Free-Text</td>
</tr>
<tr class="odd">
<td>55-64</td>
<td>10</td>
<td><p>57;0 Multiple</p>
<p>#130.0664</p></td>
<td>182;28 637</td>
<td>DONOR VESSEL UNOS ID – Entry #5</td>
<td>1-10 chars Free-Text</td>
</tr>
<tr class="even">
<td>65-74</td>
<td>10</td>
<td><p>57;0 Multiple</p>
<p>#130.0664</p></td>
<td>182;29 638</td>
<td>DONOR VESSEL UNOS ID – Entry #6</td>
<td>1-10 chars Free-Text</td>
</tr>
<tr class="odd">
<td>75-84</td>
<td>10</td>
<td><p>57;0 Multiple</p>
<p>#130.0664</p></td>
<td>182;30 639</td>
<td>DONOR VESSEL UNOS ID – Entry #7</td>
<td>1-10 chars Free-Text</td>
</tr>
<tr class="even">
<td>85-86</td>
<td>2</td>
<td>211;1 686</td>
<td>30;1 642</td>
<td>AORTIC REGURGITATION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>87-88</td>
<td>2</td>
<td>211;2 687</td>
<td>30;2 643</td>
<td>INJURY TO ADJACENT ORGAN</td>
<td><p>0 NO;</p>
<p>1 YES, WITH</p>
<p>INTERVENTION</p>
<p>2 YES, WITH NO</p>
<p>INTERVENTION REQ</p></td>
</tr>
<tr class="even">
<td>89-90</td>
<td>2</td>
<td>211;3 688</td>
<td>30;4 644</td>
<td>STOMA COMPLICATIONS</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>91-92</td>
<td>2</td>
<td>211;4 689</td>
<td>30;3 645</td>
<td>NON-UNION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>93-94</td>
<td>2</td>
<td>211;5 690</td>
<td>30;5 646</td>
<td>IMPLANT INFECTIONS</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>95-96</td>
<td>2</td>
<td>211;6 691</td>
<td>30;6 647</td>
<td>CHYLE/LYMPH LEAK</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>97-98</td>
<td>2</td>
<td>211;7 692</td>
<td>30;7 648</td>
<td>ANASTOMOTIC LEAK</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>99-100</td>
<td>2</td>
<td>211;8 693</td>
<td>30;8 649</td>
<td>FISTULA</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>101-102</td>
<td>2</td>
<td>211;9 694</td>
<td>30;9 650</td>
<td>NECROTIZING SOFT TISS INFECT</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>103-104</td>
<td>2</td>
<td>211;10 695</td>
<td>30;10 651</td>
<td>OTHER BLOOD PRODUCT UNITS</td>
<td><p>0 NONE</p>
<p>1 PLATELETS</p>
<p>2 FRESH FROZEN</p>
<p>PLASMA</p>
<p>3 PLASMA AND</p>
<p>PLATELETS</p>
<p>4 ANY OTHER</p>
<p>COMBINATION</p>
<p>5 ANY OTHER BLOOD</p>
<p>PRODUCT</p></td>
</tr>
<tr class="even">
<td>105-106</td>
<td>2</td>
<td>211;11 696</td>
<td>30;11 652</td>
<td>PRESSORS USED INTRAOP</td>
<td><p>0 NO;</p>
<p>1 YES-BOLUS;</p>
<p>2 YES-CONTINUOUS</p>
<p>INFUSION</p></td>
</tr>
<tr class="odd">
<td>107-108</td>
<td>2</td>
<td>211;12 697</td>
<td>30;12 653</td>
<td>MITRAL STENOSIS</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>109-110</td>
<td>2</td>
<td>211;13 698</td>
<td>30;13 654</td>
<td>PCI INTERVENTION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>111-112</td>
<td>2</td>
<td>211;14 699</td>
<td>30;14 655</td>
<td>ATRIAL ARRHYTHMIAS</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>113-114</td>
<td>2</td>
<td>211;15 700</td>
<td>30;15 656</td>
<td>HEAD OR NECK CANCER</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>115-116</td>
<td>2</td>
<td>211;16 701</td>
<td>30;16 657</td>
<td>MACULAR DEGENERATION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>117-118</td>
<td>2</td>
<td>211;17 702</td>
<td>30;17 658</td>
<td>GLAUCOMA</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>119-120</td>
<td>2</td>
<td>211;19 704</td>
<td>30;18 659</td>
<td>HX RETINAL DETACHMENT</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>121-122</td>
<td>2</td>
<td>211;20 705</td>
<td>30;19 660</td>
<td>AXIAL LEN/ANTERIOR CHAM DEP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>123-124</td>
<td>2</td>
<td>211;21 706</td>
<td>30;20 661</td>
<td>CORNEAL GUTTAE/FUCHS ENDO</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>125-126</td>
<td>2</td>
<td>211;22 707</td>
<td>30;21 662</td>
<td>DIABETIC RETINOPATHY</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>127-128</td>
<td>2</td>
<td>211;23 708</td>
<td>30;22 663</td>
<td>COMPLEX CATARACT</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>129-130</td>
<td>2</td>
<td>211;24 709</td>
<td>30;23 664</td>
<td>STATIN 30 DAYS PREOP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>131-132</td>
<td>2</td>
<td>211;25 710</td>
<td>30;24 665</td>
<td>IPSILAT CORTICAL EVENT PREOP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>133-134</td>
<td>2</td>
<td>211;26 711</td>
<td>30;25 666</td>
<td>PREOP MODIFIED RANKIN SCORE</td>
<td></td>
</tr>
<tr class="odd">
<td>135-136</td>
<td>2</td>
<td>211;27 712</td>
<td>30;26 667</td>
<td>CAROTID SUR ANATOMIC HIGH RISK</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>137-138</td>
<td>2</td>
<td>211;28 713</td>
<td>30;27 668</td>
<td>BYPASS CRITICAL LIMB ISCHEMIA</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>139-144</td>
<td>6</td>
<td><p>64;0 714</p>
<p>Combine all entries in the multiple field</p></td>
<td>30;28 669</td>
<td>INDIC DESC THOR ENDOGRAFT</td>
<td><p>1 ACUTE DISSECTION</p>
<p>2 CHRONIC</p>
<p>DISSECTION</p>
<p>3 ANEURYSM</p>
<p>4 ATHEROSCLEROTIC</p>
<p>OCCLUSIVE DISEASE</p>
<p>5 OTHER</p></td>
</tr>
<tr class="even">
<td>145-146</td>
<td>2</td>
<td>211;30 715</td>
<td>30;29 670</td>
<td>ENDOLEAK AT COMPLETION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>147-151</td>
<td>5</td>
<td>211;31 716</td>
<td>30;30 671</td>
<td>HIGH HEART RATE 6HRS PREOP</td>
<td>Numeric (30-250)</td>
</tr>
<tr class="even">
<td>152-156</td>
<td>5</td>
<td>211;32 717</td>
<td>30;31 672</td>
<td>HIGH HEART RATE INTRAOP</td>
<td>Numeric (30-250)</td>
</tr>
<tr class="odd">
<td>157-161</td>
<td>5</td>
<td>211;35 722</td>
<td>30;32 673</td>
<td>LOWEST PH INTRAOP</td>
<td>from 6.80 to 7.60 with 3 significant digits</td>
</tr>
<tr class="even">
<td>162-165</td>
<td>4</td>
<td>211;34 719</td>
<td>30;33 674</td>
<td>HIGH LACTIC ACID 6HRS PREOP</td>
<td>number between 0 and 30, 1 decimal</td>
</tr>
<tr class="odd">
<td>166-169</td>
<td>4</td>
<td>211;39 727</td>
<td>30;34 675</td>
<td>LOWEST BICARBONATE INTRAOP</td>
<td>from 0 to 40 with on decimal</td>
</tr>
<tr class="even">
<td>170-172</td>
<td>3</td>
<td>211;33 718</td>
<td>30;35 676</td>
<td>LOW ARTERIAL PRESS 6HRS PREOP</td>
<td>between 0 and 200</td>
</tr>
<tr class="odd">
<td>173-175</td>
<td>3</td>
<td>211;36 723</td>
<td>30;36 677</td>
<td>LOW ARTERIAL PRESS INTRAOP</td>
<td>between 0 and 200</td>
</tr>
<tr class="even">
<td>176-178</td>
<td>3</td>
<td>211;40 728</td>
<td>30;37 678</td>
<td>UNITS TRANSFUSED 6HRS PREOP</td>
<td>from 0 to 100</td>
</tr>
<tr class="odd">
<td>179-180</td>
<td>2</td>
<td>211;37 724</td>
<td>30;38 679</td>
<td>OLIGURIA &lt;60CC/2HRS 6HRS PREOP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>181-182</td>
<td>2</td>
<td>211;38 725</td>
<td>30;39 680</td>
<td>OLIGURIA URINE OUTPUT INTRAOP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>183-184</td>
<td>2</td>
<td>211;41 729</td>
<td>30;40 681</td>
<td>VASOPRESSOR USAGE AT OR ENTRY</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>185-186</td>
<td>2</td>
<td>211;42 730</td>
<td>30;41 682</td>
<td>CARDIAC ARREST 24HRS PREOP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>187-188</td>
<td>2</td>
<td>211;43 731</td>
<td>30;42 683</td>
<td>DIC 6HRS PREOP</td>
<td><p>1 SCORE &lt;5</p>
<p>2 SCORE &gt; OR EQUAL 5</p></td>
</tr>
<tr class="even">
<td>189-192</td>
<td>4</td>
<td>VERD;6 720</td>
<td>30;43 684</td>
<td>HIGH LACTIC ACID INTRAOP</td>
<td>number between 0 and 30, 1 decimal</td>
</tr>
<tr class="odd">
<td>193-197</td>
<td>5</td>
<td>VERD;7 721</td>
<td>30;44 685</td>
<td>LOWEST PH 6HRS PREOP</td>
<td>from 6.80 to 7.60 with 3 significant digits</td>
</tr>
<tr class="even">
<td>198-201</td>
<td>4</td>
<td>VERD;8 726</td>
<td>30;45 686</td>
<td>LOWEST BICARBONATE 6HRS PREOP</td>
<td>from 0-40 with 1 decimal</td>
</tr>
</tbody>
</table>

Line 16 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 16</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-16</td>
<td>2</td>
<td>210;2 666</td>
<td>30;46 687</td>
<td>LIVER DISEASE/CIRRHOSIS</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>17-18</td>
<td>2</td>
<td>210;3 668</td>
<td>30;47 688</td>
<td>IMMUNOCOMPROMISED STATE PREOP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>19-20</td>
<td>2</td>
<td>210;4 669</td>
<td>30;48 689</td>
<td>PULMONARY HTN</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>21-22</td>
<td>2</td>
<td>210;7 672</td>
<td>30;49 690</td>
<td>NUTRITIONAL SUPPLEMENT PREOP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>23-24</td>
<td>2</td>
<td>210;10 675</td>
<td>30;50 691</td>
<td>PRIOR INFEC/INFLAM SURG FIELD</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>25-26</td>
<td>2</td>
<td>210;11 676</td>
<td>31;1 692</td>
<td>HX DEEP VEIN THROMBOSIS</td>
<td><p>1 NEITHER DVT NOR</p>
<p>PE</p>
<p>2 DVT WITHOUT PE</p>
<p>3 PE WITHOUT DVT</p>
<p>4 BOTH DVT AND PE</p></td>
</tr>
<tr class="odd">
<td>27-28</td>
<td>2</td>
<td>211;44 732</td>
<td>31;2 693</td>
<td>HYPOXEMIA W/IN 6HRS PREOP</td>
<td><p>1 NOT MEASURED</p>
<p>2 PAO2/FIO2 &lt; 200</p>
<p>3 PAO2/FIO2 200-</p>
<p>249</p>
<p>4 PAO2/FIO2 250-</p>
<p>299</p>
<p>5 PAO2/FIO2 &gt; 300</p></td>
</tr>
<tr class="even">
<td>29-30</td>
<td>2</td>
<td>211;45 733</td>
<td>31;3 694</td>
<td>ENDOLEAK AT FOLLOW-UP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>31-32</td>
<td>2</td>
<td>211;46 734</td>
<td>31;4 695</td>
<td>CARDIAC ARREST INTRAOP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>33-34</td>
<td>2</td>
<td>211;47 735</td>
<td>31;5 696</td>
<td>FLOPPY IRIS INTRAOP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>35-36</td>
<td>2</td>
<td>211;48 736</td>
<td>31;6 697</td>
<td>PREOP VISUAL ACUITY</td>
<td><p>1 20/20 OR BETTER</p>
<p>2 &gt; 20/20 - 20/50</p>
<p>3 &gt; 20/50 -</p>
<p>20/100</p>
<p>4 &gt; 20/100 -</p>
<p>20/200</p>
<p>5 &gt; 20/200</p>
<p>6 HAND MOTION</p>
<p>7 LIGHT</p>
<p>PERCEPTION</p>
<p>8 NO LIGHT</p>
<p>PERCEPTION</p></td>
</tr>
<tr class="even">
<td>37-38</td>
<td>2</td>
<td>211;49 737</td>
<td>31;7 698</td>
<td>POSTOP VISUAL ACUITY</td>
<td><p>1 20/20 OR BETTER</p>
<p>2 &gt; 20/20 - 20/50</p>
<p>3 &gt; 20/50 -</p>
<p>20/100</p>
<p>4 &gt; 20/100 -</p>
<p>20/200</p>
<p>5 &gt; 20/200</p>
<p>6 HAND MOTION</p>
<p>7 LIGHT</p>
<p>PERCEPTION</p>
<p>8 NO LIGHT</p>
<p>PERCEPTION</p></td>
</tr>
<tr class="odd">
<td>39-40</td>
<td>2</td>
<td>211;50 738</td>
<td>31;8 699</td>
<td>ENDOPHTHALMITIS TYPE</td>
<td><p>0 NO</p>
<p>ENDOPHTHALMITIS</p>
<p>1 BACTERIAL</p>
<p>2 TASS</p></td>
</tr>
<tr class="even">
<td>41-42</td>
<td>2</td>
<td>211;51 739</td>
<td>31;9 700</td>
<td>CYSTOID MACULAR EDEMA</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>43-44</td>
<td>2</td>
<td>211;52 740</td>
<td>31;10 701</td>
<td>DISLOCATION OF OPERATIVE JOINT</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>45-46</td>
<td>2</td>
<td>211;53 741</td>
<td>31;11 702</td>
<td>PERIPROSTHETIC FRACTURES</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>47-58</td>
<td>12</td>
<td>211;54 742</td>
<td>184;13 130</td>
<td>D/T PAT ARRIVES HOSP DAY SURG</td>
<td>Date/Time</td>
</tr>
<tr class="even">
<td>59-70</td>
<td>12</td>
<td>211;55 743</td>
<td>184;14 132</td>
<td>D/T PAT LEAVES HOSP DAY SURG</td>
<td>Date/Time</td>
</tr>
<tr class="odd">
<td>71-73</td>
<td>3</td>
<td>211;56 744</td>
<td>31;12 703</td>
<td>KIDNEY DONOR PROFILE INDEX</td>
<td>(0-100)</td>
</tr>
<tr class="even">
<td>74-76</td>
<td>3</td>
<td>211;57 745</td>
<td>31;13 704</td>
<td>EXPECTED POST TRANSPLANT INDEX</td>
<td>(0-100)</td>
</tr>
</tbody>
</table>

Line A1 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line A1</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td>VADM(1)</td>
<td>SRAPID;2 310</td>
<td>PATIENT NAME</td>
<td></td>
</tr>
</tbody>
</table>

Line A2 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line A2</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td>VAPA(1)</td>
<td>SRAPID;3 311</td>
<td>PATIENT STREET ADDRESS1</td>
<td></td>
</tr>
</tbody>
</table>

Line A3 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line A3</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td>VAPA(2)</td>
<td>SRAPID;4 312</td>
<td>PATIENT STREET ADDRESS2</td>
<td></td>
</tr>
</tbody>
</table>

Line A4 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line A4</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td>VAPA(3)</td>
<td>SRAPID2;1 313</td>
<td>PATIENT STREET ADDRESS3</td>
<td></td>
</tr>
</tbody>
</table>

Line A5 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line A5</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td>VAPA(4)</td>
<td>SRAPID2;2 314</td>
<td>CITY</td>
<td></td>
</tr>
</tbody>
</table>

Line A6 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line A6</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td>VAPA(5)</td>
<td>SRAPID2;3 315</td>
<td>STATE</td>
<td></td>
</tr>
</tbody>
</table>

Line A7 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line A7</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td>VAPA(6)</td>
<td>SRAPID2;4 316</td>
<td>ZIP</td>
<td></td>
</tr>
</tbody>
</table>

Line A8 of the Non-Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line A8</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td>VAPA(8)</td>
<td>SRAPID2;4 317</td>
<td>PHONE</td>
<td></td>
</tr>
</tbody>
</table>

## Appendix B: Cardiac Transmission Layout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The cardiac transmission layout was last updated in 2024 by SR\*3.0\*205 and SRA\*3.0\*9.

Each line begins with “{” in position 1, Station Number in positions 2-4, Assessment Number in positions 5-11, and Line Identifier in positions 12-14.

Line 1 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 17%" />
<col style="width: 25%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 1</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-21</td>
<td>7</td>
<td>RA;4 260</td>
<td>Date Transmitted</td>
<td></td>
</tr>
<tr class="even">
<td>22-24</td>
<td>3</td>
<td>Opdate – DoB</td>
<td>Age</td>
<td></td>
</tr>
<tr class="odd">
<td>25</td>
<td>1</td>
<td>VADM(5)</td>
<td>SEX</td>
<td><p>M MALE</p>
<p>F FEMALE</p></td>
</tr>
<tr class="even">
<td>26-37</td>
<td>12</td>
<td>0;9 .09</td>
<td>Date of operation</td>
<td></td>
</tr>
<tr class="odd">
<td>38-58</td>
<td>21</td>
<td>VA(“PID”)</td>
<td>PATIENT ID</td>
<td></td>
</tr>
<tr class="even">
<td>59-60</td>
<td>2</td>
<td>208;11 413</td>
<td><p>TRANSFER STATUS</p>
<p>Change added by SR*3*184</p></td>
<td><p>1 NOT TRANSFERRED</p>
<p>2 NON-VAMC ACUTE CARE</p>
<p>HOSPITAL</p>
<p>3 VAMC ACUTE CARE HOSPITAL</p>
<p>4 NON-VA NURSING/CHRONIC</p>
<p>CARE/SCI/INTERMEDIATE</p>
<p>CARE FACILITY</p>
<p>5 VA NURSING HOME/CHRONIC</p>
<p>CARE/SCI/INTERMEDIATE</p>
<p>CARE FACILITY</p>
<p>6 OTHER</p></td>
</tr>
<tr class="odd">
<td>61-62</td>
<td>2</td>
<td>OP;3 2006</td>
<td>ROBOTIC ASSISTANCE (Y/N)</td>
<td><p>Y Yes</p>
<p>N No</p></td>
</tr>
</tbody>
</table>

Line 2 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 17%" />
<col style="width: 26%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 2</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-17</td>
<td>3</td>
<td>206;1 236</td>
<td>HEIGHT</td>
<td></td>
</tr>
<tr class="even">
<td>18</td>
<td>1</td>
<td>206;1 236</td>
<td>HEIGHT UNITS (C)</td>
<td>“C” or null</td>
</tr>
<tr class="odd">
<td>19-21</td>
<td>3</td>
<td>206;2 237</td>
<td>WEIGHT</td>
<td></td>
</tr>
<tr class="even">
<td>22</td>
<td>1</td>
<td>206;2 237</td>
<td>WEIGHT UNITS (K)</td>
<td>“K” or null</td>
</tr>
<tr class="odd">
<td>23-24</td>
<td>2</td>
<td></td>
<td>(not used)</td>
<td></td>
</tr>
<tr class="even">
<td>25-26</td>
<td>2</td>
<td>200;11 203</td>
<td>COPD</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>27-29</td>
<td>3</td>
<td>206;5 347</td>
<td>FEV1</td>
<td>Value or NS for No Study</td>
</tr>
<tr class="even">
<td>30-31</td>
<td>2</td>
<td>206;6 209</td>
<td>CARDIOMEGALY</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>32-33</td>
<td>2</td>
<td>206;7 348</td>
<td><p>PULMONARY RALES</p>
<p>*Will not be used after SR*3*184</p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>34-35</td>
<td>2</td>
<td>200.1;5 510</td>
<td><p>CURRENT SMOKER</p>
<p>Not used after 2012 update</p></td>
<td><p>1 NEVER A SMOKER</p>
<p>2 WITHIN 2 WEEKS OF SURGERY</p>
<p>3 2 WEEKS TO 3 MONTHS PRIOR</p>
<p>4 &gt;3 MONTHS PRIOR TO</p></td>
</tr>
<tr class="odd">
<td>36-39</td>
<td>4</td>
<td>201;4 223</td>
<td>SERUM CREATININE</td>
<td></td>
</tr>
<tr class="even">
<td>40-41</td>
<td>2</td>
<td>206;10 349</td>
<td>ACTIVE ENDOCARDITIS</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>42-43</td>
<td>2</td>
<td>206;11 350</td>
<td><p>RESTING ST DEPRESSION</p>
<p>*Will not be used after SR*3*184</p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>44-45</td>
<td>2</td>
<td>200;8 240</td>
<td><p>FUNCTIONAL STATUS</p>
<p>*Will not be used after SR*3*184</p></td>
<td><p>1 INDEPENDENT</p>
<p>2 PARTIALLY DEPENDENT</p>
<p>3 TOTALLY DEPENDENT</p></td>
</tr>
<tr class="odd">
<td>46-47</td>
<td>2</td>
<td>200.1;2 492</td>
<td><p>PREOP FUNCT. HEALTH STATUS</p>
<p>Added by SR*3*184</p></td>
<td><p>1 INDEPENDENT</p>
<p>2 PARTIALLY DEPENDENT</p>
<p>3 TOTALLY DEPENDENT</p></td>
</tr>
<tr class="even">
<td>48-49</td>
<td>2</td>
<td>206;14 205</td>
<td>PRIOR MI</td>
<td><p>0 NO</p>
<p>1 YES, &lt; OR EQUAL 7 DAYS PREOP</p>
<p>2 YES, &gt;7 DAYS AND &lt;6 MONTHS PREOP</p>
<p>3 UNKNOWN</p>
<p>4 YES, &gt;6 MONTHS PREOP</p>
<p>5 UNKNOWN</p></td>
</tr>
<tr class="odd">
<td>50-51</td>
<td>2</td>
<td></td>
<td>(not used)</td>
<td></td>
</tr>
<tr class="even">
<td>52-53</td>
<td>2</td>
<td>206;16 265</td>
<td>PERIPHERAL ARTERIAL DISEASE</td>
<td>1 NO 2 YES-W/O ANGI,REVASC,or AMPUT 3 YES-W HX ANGI,REVASC,or AMPUT</td>
</tr>
<tr class="odd">
<td>54-55</td>
<td>2</td>
<td>206;17 264</td>
<td>CEREBRAL VASCULAR DISEASE Not used after 2012 update</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>56-58</td>
<td>3</td>
<td>206;18 267</td>
<td>ANGINA SEVERITY</td>
<td><p>N NONE</p>
<p>I CLASS I</p>
<p>II CLASS II</p>
<p>III CLASS III</p>
<p>IV CLASS IV</p>
<p>U UNKNOWN</p></td>
</tr>
<tr class="odd">
<td>59-61</td>
<td>3</td>
<td>206;19 207</td>
<td><p>CONGESTIVE HEART FAILURE</p>
<p>* will not be used after SR*3*184</p></td>
<td><p>N NONE</p>
<p>I CARDIAC DISEASE, NO</p>
<p>LIMITATION</p>
<p>II SLIGHT LIMITATION</p>
<p>III MARKED LIMITATION</p>
<p>IV SYMPTOMS AT REST</p>
<p>U UNKNOWN</p></td>
</tr>
<tr class="even">
<td>62-63</td>
<td>2</td>
<td>206;20 353</td>
<td>CURRENT DIURETIC USE</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>64-65</td>
<td>2</td>
<td>206;21 354</td>
<td><p>CURRENT DIGOXIN USE</p>
<p>*Will not be used after SR*3*184</p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>66-67</td>
<td>2</td>
<td>206;22 355</td>
<td>IV NTG WITHIN 48 HOURS</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>68-69</td>
<td>2</td>
<td>206;23 356</td>
<td>PREOPERATIVE USE OF IABP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>70-71</td>
<td>2</td>
<td>208;19 509</td>
<td>PREOPERATIVE ATRIAL FIBRILLATION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>72-73</td>
<td>2</td>
<td>205;8 404</td>
<td>WOUND DISRUPTION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>74-75</td>
<td>2</td>
<td>205;6 248</td>
<td>SUPERFICIAL INCISIONAL SSI</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>76</td>
<td>1</td>
<td>200;59 643</td>
<td>ANGINA TIMEFRAME</td>
<td><blockquote>
<p>1 NO ANGINA 2 W/N 14 DAY OF SURGERY 3 W/N 15-30 DAYS OF SURGERY 4 UNKNOWN</p>
</blockquote></td>
</tr>
<tr class="even">
<td>77-78</td>
<td>2</td>
<td>207;29 423</td>
<td>CONGESTIVE HEART FAILURE PREOP</td>
<td><blockquote>
<p>0 N CARD DX, CHF, OR SX</p>
<p>1 Y CARD DX/CHF, N SX</p>
<p>2 Y CARD DX/CHF, Y MILD SX</p>
<p>3 Y CARD DX/CHF, Y MARKED SX</p>
<p>4 Y CARD DX/CHF, Y SX AT REST</p>
<p>5 N CARD DX/CHF, SX UNKNOWN</p>
<p>6 Y CARD DX/CHF, SX UNKNOWN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>79</td>
<td>1</td>
<td>0;26 .013</td>
<td>PLANNED ADMISSION STATUS</td>
<td><blockquote>
<p>1 SAME DAY</p>
<p>2 ADMITTED</p>
<p>3 HOSPITALIZED</p>
</blockquote></td>
</tr>
</tbody>
</table>

Line 3 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 17%" />
<col style="width: 25%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 3</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-16</td>
<td>2</td>
<td>206;24 357</td>
<td>LVEDP</td>
<td>Value or NS for No Study</td>
</tr>
<tr class="even">
<td>17-19</td>
<td>3</td>
<td>206;25 358</td>
<td>AORTIC SYSTOLIC PRESSURE</td>
<td>Value or NS for No Study</td>
</tr>
<tr class="odd">
<td>20-22</td>
<td>3</td>
<td>206;26 359</td>
<td>PA SYSTOLIC PRESSURE</td>
<td>Value or NS for No Study</td>
</tr>
<tr class="even">
<td>23-25</td>
<td>3</td>
<td>206;27 360</td>
<td>PAW MEAN PRESSURE</td>
<td>Value or NS for No Study</td>
</tr>
<tr class="odd">
<td>26-28</td>
<td>3</td>
<td>206;28 361</td>
<td>LEFT MAIN STENOSIS</td>
<td>Value or NS for No Study</td>
</tr>
<tr class="even">
<td>29-31</td>
<td>3</td>
<td>206;33 362.1</td>
<td>LAD STENOSIS</td>
<td>Value or NS for No Study</td>
</tr>
<tr class="odd">
<td>32-34</td>
<td>3</td>
<td>206;34 362.2</td>
<td>RIGHT CORONARY STENOSIS</td>
<td>Value or NS for No Study</td>
</tr>
<tr class="even">
<td>35-37</td>
<td>3</td>
<td>206;35 362.3</td>
<td>CIRCUMFLEX STENOSIS</td>
<td>Value or NS for No Study</td>
</tr>
<tr class="odd">
<td>38-40</td>
<td>3</td>
<td>206;30 363</td>
<td>LV CONTRACTION SCORE</td>
<td><p>I &gt; OR EQUAL 0.55 NORMAL</p>
<p>II 0.45-0.54 MILD DYSFUNC.</p>
<p>IIIa 0.40-0.44 MOD. DYSFUNC. A</p>
<p>IIIb 0.35-0.39 MOD. DYSFUNC. B</p>
<p>IV 0.25-0.34 SEVERE DYSFUNC.</p>
<p>V &lt;0.25 VERY SEVERE DYSFUNC.</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="even">
<td>41-42</td>
<td>2</td>
<td>206;9 415</td>
<td>MITRAL REGURGITATION</td>
<td><p>0 NONE</p>
<p>1 MILD</p>
<p>2 MODERATE</p>
<p>3 SEVERE</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="odd">
<td>43-45</td>
<td>3</td>
<td>206;31 364</td>
<td><p>ESTIMATE OF MORTALITY</p>
<p>*Will not be used after SR*3*184</p></td>
<td>Value or NS for No Study</td>
</tr>
<tr class="even">
<td>46-57</td>
<td>12</td>
<td>206;32 364.1</td>
<td><p>ESTIMATE OF MORTALITY DATE</p>
<p>Will not be used after SR*3*184</p></td>
<td></td>
</tr>
<tr class="odd">
<td>58</td>
<td>1</td>
<td>1.1;3 1.13</td>
<td>ASA CLASSIFICATION</td>
<td><p>1 1-NO DISTURB.</p>
<p>2 2-MILD DISTURB.</p>
<p>3 3-SEVERE DISTURB.</p>
<p>4 4-LIFE THREAT</p>
<p>5 5-MORIBUND</p>
<p>6 6-BRAIN-DEAD</p></td>
</tr>
<tr class="even">
<td>59</td>
<td>1</td>
<td>208;12 414</td>
<td>SURGICAL PRIORITY</td>
<td><p>1 ELECTIVE</p>
<p>2 URGENT</p>
<p>3 EMERGENT (ONGOING ISCHEMIA)</p>
<p>4 EMERGENT (HEMODYNAMIC</p>
<p>COMPROMISE)</p>
<p>5 EMERGENT (ARREST WITH CPR)</p></td>
</tr>
<tr class="odd">
<td>60-71</td>
<td>12</td>
<td>208;13 414.1</td>
<td>ESTIMATE OF SURG. PRIOR. DATE</td>
<td></td>
</tr>
<tr class="even">
<td>72-73</td>
<td>2</td>
<td>1.0;8 1.09</td>
<td>WOUND CLASSIFICATION</td>
<td><p>C CLEAN</p>
<p>CC CLEAN/CONTAMINATED</p>
<p>D CONTAMINATED</p>
<p>I DIRTY/INFECTED</p></td>
</tr>
<tr class="odd">
<td>74-75</td>
<td>2</td>
<td>210;14 685</td>
<td>DISCHARGE DISPOSITION</td>
<td><p>1 HOME</p>
<p>2 ACUTE CARE FACILITY TRANSFER</p>
<p>(VA OR NON</p>
<p>3 EXTENDED CARE FACILITY (NON-</p>
<p>REHAB)</p>
<p>4 REHABILITATION CENTER</p>
<p>5 SHELTER/TRANSITIONAL HOUSING</p>
<p>6 PATIENT DEATH</p>
<p>7 OTHER</p></td>
</tr>
</tbody>
</table>

Line 4 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 17%" />
<col style="width: 26%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 4</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-16</td>
<td>2</td>
<td>207;1 365</td>
<td><p>NUMBER WITH VEIN</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td></td>
</tr>
<tr class="even">
<td>17-18</td>
<td>2</td>
<td>207;2 366</td>
<td><p>NUMBER WITH IMA</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td></td>
</tr>
<tr class="odd">
<td>19-20</td>
<td>2</td>
<td>207;3 367</td>
<td><p>AORTIC VALVE PROCEDURE</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td><p>N NONE</p>
<p>M MECHANICAL</p>
<p>S STENTED BIOPROSTHETIC</p>
<p>B STENTLESS BIOPROSTHETIC</p>
<p>H HOMOGRAFT</p>
<p>PR PRIMARY REPAIR</p>
<p>PA PRIMARY REPAIR&amp;ANNULO PLASTY</p>
<p>DEVICE</p>
<p>AN ANNULOPLASTY DEVICE ALOONE</p>
<p>AU AUTOGRAFT (ROSS)</p>
<p>O OTHER</p></td>
</tr>
<tr class="even">
<td>21-22</td>
<td>2</td>
<td>207;4 368</td>
<td><p>MITRAL VALVE PROCEDURE</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td><p>N NONE</p>
<p>M MECHANICAL</p>
<p>S STENTED BIOPROSTHETIC</p>
<p>B STENTLESS BIOPROSTHETIC</p>
<p>H HOMOGRAFT</p>
<p>PR PRIMARY REPAIR</p>
<p>PA PRIMARY REPAIR&amp;ANNULO PLASTY</p>
<p>DEVICE</p>
<p>AN ANNULOPLASTY DEVICE ALOONE</p>
<p>AU AUTOGRAFT (ROSS)</p>
<p>O OTHER</p></td>
</tr>
<tr class="odd">
<td>23-24</td>
<td>2</td>
<td>207;5 369</td>
<td><p>TRICUSPID VALVE PROCEDURE</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td><p>N NONE</p>
<p>M MECHANICAL</p>
<p>S STENTED BIOPROSTHETIC</p>
<p>B STENTLESS BIOPROSTHETIC</p>
<p>H HOMOGRAFT</p>
<p>PR PRIMARY REPAIR</p>
<p>PA PRIMARY REPAIR&amp;ANNULO PLASTY</p>
<p>DEVICE</p>
<p>AN ANNULOPLASTY DEVICE ALOONE</p>
<p>AU AUTOGRAFT (ROSS)</p>
<p>O OTHER</p></td>
</tr>
<tr class="even">
<td>25-26</td>
<td>2</td>
<td></td>
<td>(not used)</td>
<td></td>
</tr>
<tr class="odd">
<td>27-28</td>
<td>2</td>
<td>207;7 371</td>
<td><p>LV ANEURYSMECTOMY</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>29-30</td>
<td>2</td>
<td>207;8 372</td>
<td><p>GREAT VESSEL REPAIR</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>31-32</td>
<td>2</td>
<td>207;9 373</td>
<td><p>CARDIAC TRANSPLANT</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>33-34</td>
<td>2</td>
<td>207;10 374</td>
<td>ELECTROPHYSIOLOGIC PROCEDURE</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>35-36</td>
<td>2</td>
<td>207;12 376</td>
<td><p>ASD REPAIR</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>37-38</td>
<td>2</td>
<td>207;13 380</td>
<td><p>VSD REPAIR</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>39-40</td>
<td>2</td>
<td>207;14 377</td>
<td><p>MYXOMA RESECTION</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>41-42</td>
<td>2</td>
<td>207;15 381</td>
<td><p>FOREIGN BODY REMOVAL</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>43-44</td>
<td>2</td>
<td>207;16 378</td>
<td><p>MYECTOMY FOR IHSS</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>45-46</td>
<td>2</td>
<td>207;17 382</td>
<td><p>PERICARDIECTOMY</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>47-48</td>
<td>2</td>
<td>207;18 379</td>
<td><p>OTHER TUMOR RESECTION</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>49-50</td>
<td>2</td>
<td></td>
<td>(not used)</td>
<td></td>
</tr>
<tr class="odd">
<td>51-52</td>
<td>2</td>
<td>205;41 342.1</td>
<td>30 DAY DEATH</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>53-64</td>
<td>12</td>
<td>^DPT(DFN,.35)</td>
<td>DATE/TIME OF DEATH</td>
<td></td>
</tr>
<tr class="odd">
<td>65</td>
<td>1</td>
<td>207;20 416</td>
<td><p>NUMBER WITH OTHER CONDUIT</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td></td>
</tr>
<tr class="even">
<td>66-67</td>
<td>2</td>
<td>207;28 493</td>
<td><p>PULMONARY VALVE PROCEDURE</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td><p>N NONE</p>
<p>M MECHANICAL</p>
<p>S STENTED BIOPROSTHETIC</p>
<p>B STENTLESS BIOPROSTHETIC</p>
<p>H HOMOGRAFT</p>
<p>PR PRIMARY REPAIR</p>
<p>PA PRIMARY REPAIR&amp;ANNULO PLASTY</p>
<p>DEVICE</p>
<p>AN ANNULOPLASTY DEVICE ALOONE</p>
<p>AU AUTOGRAFT (ROSS)</p>
<p>O OTHER</p></td>
</tr>
<tr class="odd">
<td>68</td>
<td>1</td>
<td>200.1;8 237.1</td>
<td>PREOPERATIVE SLEEP APNEA</td>
<td><p>1 NONE-LEVEL 1</p>
<p>2 SUSPICI OF SLEEP APNEA-LEVEL 2</p>
<p>3 SLEEP APNEA-LEVEL 3</p></td>
</tr>
<tr class="even">
<td>69-71</td>
<td>3</td>
<td>.4;6 .46</td>
<td>OP DISPOSITION</td>
<td><p>O OUTPATIENT/DISCHARGE</p>
<p>I ICU</p>
<p>S STEPDOWN</p>
<p>W WARD</p>
<p>OBS OBSERVATION UNIT</p>
<p>M MORGUE</p></td>
</tr>
<tr class="odd">
<td>72</td>
<td>1</td>
<td>200.1;15 667</td>
<td>Sleep Apnea-Compliance</td>
<td><p>1 NIGHTLY</p>
<p>2 &gt; OR EQUAL 4 TIMES A WEEK</p>
<p>3 &lt; 4 TIMES A WEEK</p>
<p>4 NOT DOCUMENTED</p></td>
</tr>
<tr class="even">
<td>73-74</td>
<td>2</td>
<td>210;5 670</td>
<td>RESIDENCE 30 DAYS PREOP</td>
<td><p>1 HOME</p>
<p>2 ACUTE CARE FACILITY</p>
<p>3 LONG TERM CARE</p>
<p>4 HOMELESS</p>
<p>5 UNKNOWN</p></td>
</tr>
<tr class="odd">
<td>75-76</td>
<td>2</td>
<td>210;6 671</td>
<td>AMBULATION DEVICE PREOP</td>
<td><p>1 AMBULATES W/OUT ASSISTIVE</p>
<p>DEVICE</p>
<p>2 AMBULATES WITH CANE OR WALKER</p>
<p>3 USES MANUAL WHEELCHAIR</p>
<p>INDEPENDENTLY</p>
<p>4 DOES NOT AMBULATE OR USE MANUAL</p>
<p>WHEELCHAIR INDEPENDENTLY</p></td>
</tr>
<tr class="even">
<td>77-78</td>
<td>2</td>
<td>210;8 673</td>
<td>HISTORY OF CANCER DIAGNOSIS</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
</tbody>
</table>

Line 5 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 17%" />
<col style="width: 26%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 5</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-44</td>
<td>30</td>
<td>0;2 .02</td>
<td>OP ROOM PROCEDURE PERFORMED</td>
<td>(Name of OR)</td>
</tr>
<tr class="even">
<td>45-46</td>
<td>2</td>
<td>52;1 619</td>
<td>IMMED USE-CONTAMINATION</td>
<td>(0 to 99)</td>
</tr>
<tr class="odd">
<td>47-48</td>
<td>2</td>
<td>52;2 620</td>
<td>IMMED USE-SPS/OR MAN ISSUE</td>
<td>(0 to 99)</td>
</tr>
<tr class="even">
<td>49-50</td>
<td>2</td>
<td>52;3 621</td>
<td>IMMED USE-EMERGENCY CASE</td>
<td>(0 to 99)</td>
</tr>
<tr class="odd">
<td>51-52</td>
<td>2</td>
<td>52;4 622</td>
<td>IMMED USE-NO BETTER OPTION</td>
<td>(0 to 99)</td>
</tr>
<tr class="even">
<td>53-54</td>
<td>2</td>
<td>52;5 623</td>
<td>IMMED USE-LOANER</td>
<td>(0 to 99)</td>
</tr>
<tr class="odd">
<td>55-56</td>
<td>2</td>
<td>52;6 624</td>
<td>IMMED USE -DECONTAMINATION</td>
<td>(0 to 99)</td>
</tr>
<tr class="even">
<td>57-58</td>
<td>2</td>
<td>200;55 618</td>
<td>POSITIVE DRUG SCREENING</td>
<td><blockquote>
<p>1 NOT DONE 2 NEGATIVE RESULT 3 POS NOT RX 4 POS RX</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>59-60</td>
<td>2</td>
<td>200.1;9 517</td>
<td>TOBACCO USE</td>
<td><p>1 NEVER USED TOBACCO</p>
<p>2 NO USE IN LAST 12 MOS</p>
<p>3 CIGARETTES ONLY</p>
<p>4 OTHER (NO CIGARETTES)</p>
<p>5 CIGARETTES PLUS OTHER</p></td>
</tr>
<tr class="even">
<td>61-62</td>
<td>2</td>
<td>200.1;10 518</td>
<td>TOBACCO USE TIMEFRAME</td>
<td><p>1 WITHIN 2 WEEKS</p>
<p>2 2 WKS TO 3 MOS</p>
<p>3 3 TO 12 MONTHS</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="odd">
<td>63-64</td>
<td>2</td>
<td>200.1;11 519</td>
<td>DIABETES MELLITUS CHRONIC</td>
<td><p>1 NO</p>
<p>2 DIET</p>
<p>3 ORAL</p>
<p>4 INSULIN</p></td>
</tr>
<tr class="even">
<td>65-66</td>
<td>2</td>
<td>200.1;12 520</td>
<td>DIABETES MELLITUS PREOP MGMT</td>
<td><p>1 NO</p>
<p>2 DIET</p>
<p>3 ORAL</p>
<p>4 INSULIN</p></td>
</tr>
<tr class="odd">
<td>67-68</td>
<td>2</td>
<td>200.1;13 521</td>
<td>CVD REPAIR/OBSTRUCTION</td>
<td><p>0 NO CVD</p>
<p>1 YES - NO SURGICAL REPAIR</p>
<p>2 YES - PRIOR SURGICAL</p>
<p>REPAIR</p></td>
</tr>
<tr class="even">
<td>69-70</td>
<td>2</td>
<td>200.1;14 522</td>
<td>HISTORY OF CVD</td>
<td><p>0 NO CVD</p>
<p>1 HISTORY OF TIA'S</p>
<p>2 CVA/STROKE - NO NEURO</p>
<p>DEFICIT</p>
<p>3 CVA/STROKE W/ NEURO</p>
<p>DEFICIT</p></td>
</tr>
<tr class="odd">
<td>71-72</td>
<td>2</td>
<td>210;9 674</td>
<td>HX RAD RX PLANNED SURG FIELD</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>73-74</td>
<td>2</td>
<td>210;12 677</td>
<td>PRIOR SURG SAME OP FIELD</td>
<td><blockquote>
<p>0 NO PREVIOUS SURGERIES</p>
<p>1 1 PREVIOUS SURGERY</p>
<p>2 2 PREVIOUS SURGERIES</p>
<p>3 3 PREVIOUS SURGERIES</p>
<p>4 4 PREVIOUS SURGERIES</p>
<p>5 5 PREVIOUS SURGERIES</p>
<p>6 &gt;5 PREVIOUS SURGERIES</p>
</blockquote></td>
</tr>
</tbody>
</table>

Line 6 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 21%" />
<col style="width: 25%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 6</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-16</td>
<td>2</td>
<td>205;27 258</td>
<td>MYOCARDIAL INFARCTION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>17-18</td>
<td>2</td>
<td>208;3 386</td>
<td>ENDOCARDITIS</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>19-20</td>
<td>2</td>
<td>208;17 254</td>
<td>ACUTE RENAL FAILURE</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>21-22</td>
<td>2</td>
<td>208;4 387</td>
<td>LOW CARDIAC OUTPUT &gt; 6 HOURS</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>23-24</td>
<td>2</td>
<td>208;5 388</td>
<td>MEDIASTINITIS</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>25-26</td>
<td>2</td>
<td>208;28 259</td>
<td>CONGESTIVE HEART FAILURE <em>Category Inactivated</em></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>27-28</td>
<td>2</td>
<td>208;6 389</td>
<td>REOPERATION FOR BLEEDING</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>29-30</td>
<td>2</td>
<td>208;13 285</td>
<td>ON VENTILATOR&gt;48 HOURS</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>31-32</td>
<td>2</td>
<td><p>208;7 391</p>
<p>16,0;5 130.22,8</p></td>
<td>REPEAT CARDIAC SURGICAL PROCEDURE</td>
<td><p>0 None</p>
<p>1 On-bypass</p>
<p>2 Off-bypass</p>
<p>N NO</p>
<p>Y YES</p></td>
</tr>
<tr class="even">
<td>33-34</td>
<td>2</td>
<td>205;22 410</td>
<td>COMA&gt;24 HOURS</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>35-36</td>
<td>2</td>
<td>16;8 130.22,9</td>
<td>STROKE/CVA</td>
<td><p>1 NO SYMPTOMS</p>
<p>2 &lt;24 HOURS</p>
<p>3 24-72 HOURS</p>
<p>4 &gt;72 HOURS</p></td>
</tr>
<tr class="even">
<td>37-38</td>
<td>2</td>
<td><p>205;26 411</p>
<p>10,0;2 130.13,3</p>
<p>16,0;2 130.22,5</p></td>
<td>CARDIAC ARREST REQUIRING CPR</td>
<td><p>I INTRAOP</p>
<p>P POST-OP</p>
<p>N NO</p>
<p>Y YES</p></td>
</tr>
<tr class="odd">
<td>39</td>
<td>1</td>
<td>VADM(11)</td>
<td>ETHNICITY</td>
<td><p>D DECLINED TO ANSWER</p>
<p>H HISPANIC OR LATINO</p>
<p>N NOT HISPANIC OR LATINO</p>
<p>U UNKNOWN BY PATIENT</p></td>
</tr>
<tr class="even">
<td>40</td>
<td>1</td>
<td>VADM(12)</td>
<td>RACE 1</td>
<td><p>3 AMERICAN INDIAN OR ALASKA</p>
<p>NATIVE</p>
<p>A NATIVE HAWAIIAN OR OTHER</p>
<p>PACIFIC ISLANDER</p>
<p>9 BLACK OR AFRICAN AMERICAN</p>
<p>8 ASIAN</p>
<p>B WHITE</p>
<p>C DECLINED TO</p>
<p>ANSWER/UNANSWERED</p>
<p>D UNKNOWN BY PATIENT</p></td>
</tr>
<tr class="odd">
<td>41</td>
<td>1</td>
<td>VADM(12)</td>
<td>RACE 2</td>
<td><p>3 AMERICAN INDIAN OR ALASKA</p>
<p>NATIVE</p>
<p>A NATIVE HAWAIIAN OR OTHER</p>
<p>PACIFIC ISLANDER</p>
<p>9 BLACK OR AFRICAN AMERICAN</p>
<p>8 ASIAN</p>
<p>B WHITE</p>
<p>C DECLINED TO</p>
<p>ANSWER/UNANSWERED</p>
<p>D UNKNOWN BY PATIENT</p></td>
</tr>
<tr class="even">
<td>42</td>
<td>1</td>
<td>VADM(12)</td>
<td>RACE 3</td>
<td><p>3 AMERICAN INDIAN OR ALASKA</p>
<p>NATIVE</p>
<p>A NATIVE HAWAIIAN OR OTHER</p>
<p>PACIFIC ISLANDER</p>
<p>9 BLACK OR AFRICAN AMERICAN</p>
<p>8 ASIAN</p>
<p>B WHITE</p>
<p>C DECLINED TO</p>
<p>ANSWER/UNANSWERED</p>
<p>D UNKNOWN BY PATIENT</p></td>
</tr>
<tr class="odd">
<td>43</td>
<td>1</td>
<td>VADM(12)</td>
<td>RACE 4</td>
<td><p>3 AMERICAN INDIAN OR ALASKA</p>
<p>NATIVE</p>
<p>A NATIVE HAWAIIAN OR OTHER</p>
<p>PACIFIC ISLANDER</p>
<p>9 BLACK OR AFRICAN AMERICAN</p>
<p>8 ASIAN</p>
<p>B WHITE</p>
<p>C DECLINED TO</p>
<p>ANSWER/UNANSWERED</p>
<p>D UNKNOWN BY PATIENT</p></td>
</tr>
<tr class="even">
<td>44</td>
<td>1</td>
<td>VADM(12)</td>
<td>RACE 5</td>
<td><p>3 AMERICAN INDIAN OR ALASKA</p>
<p>NATIVE</p>
<p>A NATIVE HAWAIIAN OR OTHER</p>
<p>PACIFIC ISLANDER</p>
<p>9 BLACK OR AFRICAN AMERICAN</p>
<p>8 ASIAN</p>
<p>B WHITE</p>
<p>C DECLINED TO</p>
<p>ANSWER/UNANSWERED</p>
<p>D UNKNOWN BY PATIENT</p></td>
</tr>
</tbody>
</table>

Line 7 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 16%" />
<col style="width: 26%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 7</p>
<p>Position</p></th>
<th>Length</th>
<th></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-79</td>
<td>65</td>
<td>VADM(1)</td>
<td>PATIENT NAME</td>
<td></td>
</tr>
</tbody>
</table>

Line 8 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 8</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-24</td>
<td>10</td>
<td>VAPA(11/6)</td>
<td>ZIP CODE</td>
<td></td>
</tr>
<tr class="even">
<td>25</td>
<td>1</td>
<td>208;18 442</td>
<td>EMPLOYMENT STATUS</td>
<td><p>1 EMPLOYED FULL TIME</p>
<p>2 EMPLOYED PART TIME</p>
<p>3 NOT EMPLOYED</p>
<p>4 SELF EMPLOYED</p>
<p>5 RETIRED</p>
<p>6 ACTIVE MILITARY DUTY</p>
<p>9 UNKNOWN</p></td>
</tr>
<tr class="odd">
<td>26-32</td>
<td>7</td>
<td>201;20 219</td>
<td>HEMOGLOBIN</td>
<td></td>
</tr>
<tr class="even">
<td>33-39</td>
<td>7</td>
<td>202;20 239</td>
<td>HEMOGLOBIN DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>40-43</td>
<td>4</td>
<td>201;8 225</td>
<td>SERUM ALBUMIN</td>
<td>Value or NS for No Study</td>
</tr>
<tr class="even">
<td>44-50</td>
<td>7</td>
<td>202;8 292</td>
<td>SERUM ALBUMIN DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>51-57</td>
<td>7</td>
<td>202;4 290</td>
<td>SERUM CREATININE DATE</td>
<td></td>
</tr>
<tr class="even">
<td>58-61</td>
<td>4</td>
<td>206;36 450</td>
<td>TOTAL ISCHEMIC TIME</td>
<td></td>
</tr>
<tr class="odd">
<td>62</td>
<td>1</td>
<td></td>
<td>(not used)</td>
<td></td>
</tr>
<tr class="even">
<td>63-66</td>
<td>4</td>
<td>206;37 451</td>
<td>TOTAL CPB TIME</td>
<td></td>
</tr>
<tr class="odd">
<td>67-68</td>
<td>2</td>
<td></td>
<td>(not used)</td>
<td></td>
</tr>
</tbody>
</table>

Line 9 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 9</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 136</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-19</td>
<td>5</td>
<td>0;2 .02</td>
<td>PRINCIPAL CPT CODE</td>
<td></td>
</tr>
<tr class="even">
<td>20-24</td>
<td>5</td>
<td>3;136.03 .01</td>
<td>OTHER PROCEDURE CPT CODE #1</td>
<td></td>
</tr>
<tr class="odd">
<td>25-29</td>
<td>5</td>
<td>3;136.03 .01</td>
<td>OTHER PROCEDURE CPT CODE #2</td>
<td></td>
</tr>
<tr class="even">
<td>30-34</td>
<td>5</td>
<td>3;136.03 .01</td>
<td>OTHER PROCEDURE CPT CODE #3</td>
<td></td>
</tr>
<tr class="odd">
<td>35-39</td>
<td>5</td>
<td>3;136.03 .01</td>
<td>OTHER PROCEDURE CPT CODE #4</td>
<td></td>
</tr>
<tr class="even">
<td>40-44</td>
<td>5</td>
<td>3;136.03 .01</td>
<td>OTHER PROCEDURE CPT CODE #5</td>
<td></td>
</tr>
<tr class="odd">
<td>45-49</td>
<td>5</td>
<td>3;136.03 .01</td>
<td>OTHER PROCEDURE CPT CODE #6</td>
<td></td>
</tr>
<tr class="even">
<td>50-54</td>
<td>5</td>
<td>3;136.03 .01</td>
<td>OTHER PROCEDURE CPT CODE #7</td>
<td></td>
</tr>
<tr class="odd">
<td>55-59</td>
<td>5</td>
<td>3;136.03 .01</td>
<td>OTHER PROCEDURE CPT CODE #8</td>
<td></td>
</tr>
<tr class="even">
<td>60-64</td>
<td>5</td>
<td>3;136.03 .01</td>
<td>OTHER PROCEDURE CPT CODE #9</td>
<td></td>
</tr>
<tr class="odd">
<td>65-69</td>
<td>5</td>
<td>3;136.03 .01</td>
<td>OTHER PROCEDURE CPT CODE #10</td>
<td></td>
</tr>
</tbody>
</table>

Line 10 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 10</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-26</td>
<td>12</td>
<td>207;21 440</td>
<td>CARDIAC CATHETERIZATION DATE</td>
<td>Value or “NS” for No Study</td>
</tr>
<tr class="even">
<td>27-38</td>
<td>12</td>
<td>208;14 418</td>
<td>HOSPITAL ADMISSION DATE/TIME</td>
<td></td>
</tr>
<tr class="odd">
<td>39-50</td>
<td>12</td>
<td>208;15 419</td>
<td>HOSPITAL DISCHARGE DATE/TIME</td>
<td></td>
</tr>
<tr class="even">
<td>51-62</td>
<td>12</td>
<td>.2;1 .21</td>
<td>ANESTHESIA START DATE/TIME</td>
<td></td>
</tr>
<tr class="odd">
<td>63-74</td>
<td>12</td>
<td>.2;4 .24</td>
<td>ANESTHESIA END DATE/TIME</td>
<td></td>
</tr>
</tbody>
</table>

Line 11 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 11</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-26</td>
<td>12</td>
<td>.2;10 .205</td>
<td>TIME PAT IN OR</td>
<td></td>
</tr>
<tr class="even">
<td>27-38</td>
<td>12</td>
<td>.2;12 .232</td>
<td>TIME PAT OUT OR</td>
<td></td>
</tr>
<tr class="odd">
<td>39-50</td>
<td>12</td>
<td>.2;2 .22</td>
<td>DATE/TIME OPERATION BEGAN</td>
<td></td>
</tr>
<tr class="even">
<td>51-62</td>
<td>12</td>
<td>.2;3 .23</td>
<td>DATE/TIME OPERATION ENDED</td>
<td></td>
</tr>
</tbody>
</table>

Line 12 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 12</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-79</td>
<td>65</td>
<td>206.1;1 430</td>
<td><p>PREOP RISK FACTORS COMMENTS</p>
<p>*Will not be used after SR*3*184</p></td>
<td></td>
</tr>
</tbody>
</table>

Line 13 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 13</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-79</td>
<td>65</td>
<td>206.1;1 430</td>
<td><p>PREOP RISK FACTORS COMMENTS, CONTINUED</p>
<p>*Will no longer be used after SR*3*184</p></td>
<td></td>
</tr>
</tbody>
</table>

Line 14 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 14</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-79</td>
<td>65</td>
<td>206.2;1 431</td>
<td><p>RESOURCE DATA COMMENTS</p>
<p>*Will no longer be used after SR*3*184</p></td>
<td></td>
</tr>
</tbody>
</table>

Line 15 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 15</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-79</td>
<td>65</td>
<td>206.2;1 431</td>
<td><p>RESOURCE DATA COMMENTS, (CONTINUED)</p>
<p>*Will no longer be used after SR*3*184</p></td>
<td></td>
</tr>
</tbody>
</table>

Line 16 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 16</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 136</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-16</td>
<td>2</td>
<td>1;136.01 .01</td>
<td>PRIN. PROC. CPT MODIFIER #1</td>
<td></td>
</tr>
<tr class="even">
<td>17-18</td>
<td>2</td>
<td>1;136.01 .01</td>
<td>PRIN. PROC. CPT MODIFIER #2</td>
<td></td>
</tr>
<tr class="odd">
<td>19-20</td>
<td>2</td>
<td>1;136.01 .01</td>
<td>PRIN. PROC. CPT MODIFIER #3</td>
<td></td>
</tr>
<tr class="even">
<td>21-22</td>
<td>2</td>
<td>1;136.01 .01</td>
<td>PRIN. PROC. CPT MODIFIER #4</td>
<td></td>
</tr>
<tr class="odd">
<td>23-24</td>
<td>2</td>
<td>1;136.01 .01</td>
<td>PRIN. PROC. CPT MODIFIER #5</td>
<td></td>
</tr>
<tr class="even">
<td>25-26</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #1 - MODIFIER #1</td>
<td></td>
</tr>
<tr class="odd">
<td>27-28</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #1 - MODIFIER #2</td>
<td></td>
</tr>
<tr class="even">
<td>29-30</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #1 - MODIFIER #3</td>
<td></td>
</tr>
<tr class="odd">
<td>31-32</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #1 - MODIFIER #4</td>
<td></td>
</tr>
<tr class="even">
<td>33-34</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #1 - MODIFIER #5</td>
<td></td>
</tr>
<tr class="odd">
<td>35-36</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #2 - MODIFIER #1</td>
<td></td>
</tr>
<tr class="even">
<td>37-38</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #2 - MODIFIER #2</td>
<td></td>
</tr>
<tr class="odd">
<td>39-40</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #2 - MODIFIER #3</td>
<td></td>
</tr>
<tr class="even">
<td>41-42</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #2 - MODIFIER #4</td>
<td></td>
</tr>
<tr class="odd">
<td>43-44</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #2 - MODIFIER #5</td>
<td></td>
</tr>
<tr class="even">
<td>45-46</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #3 - MODIFIER #1</td>
<td></td>
</tr>
<tr class="odd">
<td>47-48</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #3 - MODIFIER #2</td>
<td></td>
</tr>
<tr class="even">
<td>49-50</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #3 - MODIFIER #3</td>
<td></td>
</tr>
<tr class="odd">
<td>51-52</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #3 - MODIFIER #4</td>
<td></td>
</tr>
<tr class="even">
<td>53-54</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #3 - MODIFIER #5</td>
<td></td>
</tr>
<tr class="odd">
<td>55-56</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #4 - MODIFIER #1</td>
<td></td>
</tr>
<tr class="even">
<td>57-58</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #4 - MODIFIER #2</td>
<td></td>
</tr>
<tr class="odd">
<td>59-60</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #4 - MODIFIER #3</td>
<td></td>
</tr>
<tr class="even">
<td>61-62</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #4 - MODIFIER #4</td>
<td></td>
</tr>
<tr class="odd">
<td>63-64</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #4 - MODIFIER #5</td>
<td></td>
</tr>
<tr class="even">
<td>65-66</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #5 - MODIFIER #1</td>
<td></td>
</tr>
<tr class="odd">
<td>67-68</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #5 - MODIFIER #2</td>
<td></td>
</tr>
<tr class="even">
<td>69-70</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #5 - MODIFIER #3</td>
<td></td>
</tr>
<tr class="odd">
<td>71-72</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #5 - MODIFIER #4</td>
<td></td>
</tr>
<tr class="even">
<td>73-74</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #5 - MODIFIER #5</td>
<td></td>
</tr>
</tbody>
</table>

Line 17 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 17</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 136</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-16</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #6 - MODIFIER #1</td>
<td></td>
</tr>
<tr class="even">
<td>17-18</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #6 - MODIFIER #2</td>
<td></td>
</tr>
<tr class="odd">
<td>19-20</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #6 - MODIFIER #3</td>
<td></td>
</tr>
<tr class="even">
<td>21-22</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #6 - MODIFIER #4</td>
<td></td>
</tr>
<tr class="odd">
<td>23-24</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #6 - MODIFIER #5</td>
<td></td>
</tr>
<tr class="even">
<td>25-26</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #7 - MODIFIER #1</td>
<td></td>
</tr>
<tr class="odd">
<td>27-28</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #7 - MODIFIER #2</td>
<td></td>
</tr>
<tr class="even">
<td>29-30</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #7 - MODIFIER #3</td>
<td></td>
</tr>
<tr class="odd">
<td>31-32</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #7 - MODIFIER #4</td>
<td></td>
</tr>
<tr class="even">
<td>33-34</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #7 - MODIFIER #5</td>
<td></td>
</tr>
<tr class="odd">
<td>35-36</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #8 - MODIFIER #1</td>
<td></td>
</tr>
<tr class="even">
<td>37-38</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #8 - MODIFIER #2</td>
<td></td>
</tr>
<tr class="odd">
<td>39-40</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #8 - MODIFIER #3</td>
<td></td>
</tr>
<tr class="even">
<td>41-42</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #8 - MODIFIER #4</td>
<td></td>
</tr>
<tr class="odd">
<td>43-44</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #8 - MODIFIER #5</td>
<td></td>
</tr>
<tr class="even">
<td>45-46</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #9 - MODIFIER #1</td>
<td></td>
</tr>
<tr class="odd">
<td>47-48</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #9 - MODIFIER #2</td>
<td></td>
</tr>
<tr class="even">
<td>49-50</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #9 - MODIFIER #3</td>
<td></td>
</tr>
<tr class="odd">
<td>51-52</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #9 - MODIFIER #4</td>
<td></td>
</tr>
<tr class="even">
<td>53-54</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #9 - MODIFIER #5</td>
<td></td>
</tr>
<tr class="odd">
<td>55-56</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #10 - MODIFIER #1</td>
<td></td>
</tr>
<tr class="even">
<td>57-58</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #10 - MODIFIER #2</td>
<td></td>
</tr>
<tr class="odd">
<td>59-60</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #10 - MODIFIER #3</td>
<td></td>
</tr>
<tr class="even">
<td>61-62</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #10 - MODIFIER #4</td>
<td></td>
</tr>
<tr class="odd">
<td>63-64</td>
<td>2</td>
<td>3,1;136.31 .01</td>
<td>OTHER PROC. CPT #10 - MODIFIER #5</td>
<td></td>
</tr>
<tr class="even">
<td>65-70</td>
<td>6</td>
<td>8;1 50</td>
<td>DIVISION</td>
<td></td>
</tr>
</tbody>
</table>

Line 18 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 16%" />
<col style="width: 26%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 18</p>
<p>Position</p></th>
<th>Length</th>
<th></th>
<th>FIELD NAMES</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-49</td>
<td>35</td>
<td>VAPA(1)</td>
<td>STREET ADRESS (LINE 1)</td>
<td></td>
</tr>
<tr class="even">
<td>50-79</td>
<td>30</td>
<td>VAPA(2)</td>
<td>STREET ADRESS (LINE 2)</td>
<td></td>
</tr>
</tbody>
</table>

Line 19 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 16%" />
<col style="width: 26%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 19</p>
<p>Position</p></th>
<th>Length</th>
<th></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-44</td>
<td>30</td>
<td>VAPA(3)</td>
<td>STREET ADRESS (LINE 2)</td>
<td></td>
</tr>
<tr class="even">
<td>45-59</td>
<td>15</td>
<td>VAPA(4)</td>
<td>CITY</td>
<td></td>
</tr>
<tr class="odd">
<td>60-64</td>
<td>5</td>
<td>VAPA(5)</td>
<td>STATE (ABBREVIATION)</td>
<td></td>
</tr>
</tbody>
</table>

Line 20 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 15%" />
<col style="width: 26%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 20</p>
<p>Position</p></th>
<th>Length</th>
<th></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-34</td>
<td>20</td>
<td>VAPA(8)</td>
<td>PHONE NUMBER</td>
<td></td>
</tr>
<tr class="even">
<td>35-64</td>
<td>30</td>
<td>Field .05, File 405</td>
<td>REFERRING FACILITY NAME</td>
<td></td>
</tr>
<tr class="odd">
<td>65-70</td>
<td>6</td>
<td>Field .05, File 405</td>
<td>REFERRING FACILITY NUMBER</td>
<td></td>
</tr>
<tr class="even">
<td>71-76</td>
<td>6</td>
<td>Field 27.02, File 2</td>
<td>PREFERRED FACILITY NUMBER</td>
<td></td>
</tr>
</tbody>
</table>

Line 21 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 22%" />
<col style="width: 20%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 21</p>
<p>Position</p></th>
<th>Length</th>
<th></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-44</td>
<td>30</td>
<td>Field .05, File 405</td>
<td>FOLLOW-UP FACILITY NAME</td>
<td></td>
</tr>
<tr class="even">
<td>45-50</td>
<td>6</td>
<td>Field .05, File 405</td>
<td>FOLLOW-UP FACILITY NUMBER</td>
<td></td>
</tr>
</tbody>
</table>

Line 22 of the Cardiac Transmission Layout

<table style="width:100%;">
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 22%" />
<col style="width: 23%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 22</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-20</td>
<td>6</td>
<td>201;21 457</td>
<td>HDL</td>
<td>Value or “NS” for No Study</td>
</tr>
<tr class="even">
<td>21-27</td>
<td>7</td>
<td>202;21 457.1</td>
<td>HDL, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>28-33</td>
<td>6</td>
<td>201;22 458</td>
<td>SERUM TRIGLYCERIDE</td>
<td>Value or “NS” for No Study</td>
</tr>
<tr class="even">
<td>34-40</td>
<td>7</td>
<td>202;22 458.1</td>
<td>SERUM TRIGLYCERIDE, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>41-46</td>
<td>6</td>
<td>201;23 459</td>
<td>SERUM POTASSIUM</td>
<td>Value or “NS” for No Study</td>
</tr>
<tr class="even">
<td>47-53</td>
<td>7</td>
<td>202;23 459.1</td>
<td>SERUM POTASSIUM, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>54-59</td>
<td>6</td>
<td>201;24 460</td>
<td>SERUM BILIRUBIN</td>
<td>Value or “NS” for No Study</td>
</tr>
<tr class="even">
<td>60-66</td>
<td>7</td>
<td>202;24 460.1</td>
<td>SERUM BILIRUBIN, DATE</td>
<td></td>
</tr>
</tbody>
</table>

Line 23 of the Cardiac Transmission Layout

<table style="width:100%;">
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 22%" />
<col style="width: 23%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 23</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-20</td>
<td>6</td>
<td>201;25 461</td>
<td>LDL</td>
<td>Value or “NS” for No Study</td>
</tr>
<tr class="even">
<td>21-27</td>
<td>7</td>
<td>202;25 461.1</td>
<td>LDL, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>28-33</td>
<td>6</td>
<td>201;26 462</td>
<td>TOTAL CHOLESTEROL</td>
<td>Value or “NS” for No Study</td>
</tr>
<tr class="even">
<td>34-40</td>
<td>7</td>
<td>202;26 462.1</td>
<td>TOTAL CHOLESTEROL, DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>41-47</td>
<td>7</td>
<td>VADM(3)</td>
<td>DATE OF BIRTH</td>
<td></td>
</tr>
<tr class="even">
<td>48-50</td>
<td>3</td>
<td>25;1 44</td>
<td>SPONGE FINAL COUNT CORRECT</td>
<td><p>Y YES</p>
<p>N NO, SEE NURSING CARE</p>
<p>COMMENTS</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="odd">
<td>51-53</td>
<td>3</td>
<td>25;2 45</td>
<td>SHARPS FINAL COUNT CORRECT</td>
<td><p>Y YES</p>
<p>N NO, SEE NURSING CARE</p>
<p>COMMENTS</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="even">
<td>54-56</td>
<td>3</td>
<td>25;3 46</td>
<td>INSTRUMENT FINAL COUNT CORRECT</td>
<td><p>Y YES</p>
<p>N NO, SEE NURSING CARE</p>
<p>COMMENTS</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="odd">
<td>57</td>
<td>1</td>
<td>25;6 630</td>
<td>POSSIBLE ITEM RETENTION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>58</td>
<td>1</td>
<td>25;7 633</td>
<td>WOUND SWEEP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>59</td>
<td>1</td>
<td>25;8 636</td>
<td>INTRA-OPERATIVE X-RAY</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>60-62</td>
<td>3</td>
<td></td>
<td>NUM OF PROSTHESIS INSTALLED ENTRIES</td>
<td>(0 to 999)</td>
</tr>
<tr class="odd">
<td>63-65</td>
<td>3</td>
<td></td>
<td>NUM OF PROVIDER READ BACK PERFORMED “YES” RESPONCES</td>
<td>(0 to 999)</td>
</tr>
</tbody>
</table>

Line 24 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 22%" />
<col style="width: 23%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 24</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-16</td>
<td>2</td>
<td></td>
<td>(not used)</td>
<td></td>
</tr>
<tr class="even">
<td>17-18</td>
<td>2</td>
<td>200;57 641</td>
<td>HYPERTENSION</td>
<td><blockquote>
<p>1 NO 2 YES WITHOUT MED</p>
<p>3 YES WITH MED</p>
<p>4 UNKNOWN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>19-20</td>
<td>2</td>
<td>207;24 464</td>
<td><p>NUMBER WITH RADIAL ARTERY</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td></td>
</tr>
<tr class="even">
<td>21-22</td>
<td>2</td>
<td>207;25 465</td>
<td><p>NUMBER WITH OTHER ARTERY</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td></td>
</tr>
<tr class="odd">
<td>23-24</td>
<td>2</td>
<td>206;39 466</td>
<td>TRACHEOSTOMY</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>25-26</td>
<td>2</td>
<td><p>206;40 467</p>
<p>10,0;2 130.13,3</p>
<p>16,0;2 130.22,5</p></td>
<td>NEW MECHANICAL CIRCULATORY</td>
<td><p>I INTRAOP</p>
<p>P POST-OP</p>
<p>N NO</p>
<p>Y YES</p></td>
</tr>
<tr class="odd">
<td>27-28</td>
<td>2</td>
<td></td>
<td>(not used)</td>
<td></td>
</tr>
<tr class="even">
<td>29-40</td>
<td>12</td>
<td>208;22 470</td>
<td>DATE/TIME PATIENT EXTUBATED</td>
<td>Value or “RI” for Remains intubated at 30 days</td>
</tr>
<tr class="odd">
<td>41-52</td>
<td>12</td>
<td>208;23 471</td>
<td>D/T PAT DISCHARGED FROM ICU</td>
<td>Value or “RI” for Remains in ICU at 30 days</td>
</tr>
<tr class="even">
<td>53-54</td>
<td>2</td>
<td>206;41 472</td>
<td><p>CARDIAC SURG CONTRACTED NON-VA FACILITY</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS UNKNOWN</p></td>
</tr>
<tr class="odd">
<td>55-57</td>
<td>3</td>
<td>207;26 468</td>
<td>INCISION TYPE</td>
<td><p>FS FULL STERNOTOMY</p>
<p>FT FULL THORACOTOMY</p>
<p>LP LIMITED PARASTERNAL APPROACH</p>
<p>LS LIMITED STERNOTOMY</p>
<p>LT LIMITED THORACOTOMY</p>
<p>OL OTHER LIMITED SURG APPROACH</p>
<p>NS NO STUDY/UNKNOWN</p></td>
</tr>
<tr class="even">
<td>58-65</td>
<td>8</td>
<td>RPC^DGPTFAPI</td>
<td>DISCHARGE ICD #1 -PRIMARY</td>
<td></td>
</tr>
<tr class="odd">
<td>66-67</td>
<td>2</td>
<td>205;40 448</td>
<td>POSTOPERATIVE ATRIAL FIBRILLATION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>68</td>
<td>1</td>
<td>130.13,5</td>
<td>INTRAOP DEVICE TYPE</td>
<td><blockquote>
<p>1 IABP</p>
<p>2 VAD</p>
<p>3 TAH</p>
<p>4 ECMO</p>
<p>5 MULTIPLE DEVICES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>69</td>
<td>1</td>
<td>130.22,15</td>
<td>POSTOP DEVICE TYPE</td>
<td><blockquote>
<p>1 IABP</p>
<p>2 VAD</p>
<p>3 TAH</p>
<p>4 ECMO</p>
<p>5 MULTIPLE DEVICES</p>
</blockquote></td>
</tr>
<tr class="even">
<td>70</td>
<td>1</td>
<td>.1;21 661</td>
<td><p>PALLIATION</p>
<p>SR*3*184 Change</p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
</tbody>
</table>

Line 25 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 14%" />
<col style="width: 27%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 25</p>
<p>Position</p></th>
<th>Length</th>
<th></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-16</td>
<td>2</td>
<td>RPC^DGPTFAPI</td>
<td>TYPE OF DISCHARGE</td>
<td><p>1 REGULAR</p>
<p>2 NBC OR WHILE ASIH</p>
<p>3 EXPIRATION 6 MONTH LIMIT</p>
<p>4 IRREGULAR</p>
<p>5 TRANSFER</p>
<p>6 DEATH WITH AUTOPSY</p>
<p>7 DEATH WITHOUT AUTOPSY</p></td>
</tr>
<tr class="even">
<td>17-24</td>
<td>8</td>
<td>RPC^DGPTFAPI</td>
<td>DISCHARGE ICD #2</td>
<td></td>
</tr>
<tr class="odd">
<td>25-32</td>
<td>8</td>
<td>RPC^DGPTFAPI</td>
<td>DISCHARGE ICD #3</td>
<td></td>
</tr>
<tr class="even">
<td>33-40</td>
<td>8</td>
<td>RPC^DGPTFAPI</td>
<td>DISCHARGE ICD #4</td>
<td></td>
</tr>
<tr class="odd">
<td>41-48</td>
<td>8</td>
<td>RPC^DGPTFAPI</td>
<td>DISCHARGE ICD #5</td>
<td></td>
</tr>
<tr class="even">
<td>49-56</td>
<td>8</td>
<td>RPC^DGPTFAPI</td>
<td>DISCHARGE ICD #6</td>
<td></td>
</tr>
<tr class="odd">
<td>57-64</td>
<td>8</td>
<td>RPC^DGPTFAPI</td>
<td>DISCHARGE ICD #7</td>
<td></td>
</tr>
<tr class="even">
<td>65-72</td>
<td>8</td>
<td>RPC^DGPTFAPI</td>
<td>DISCHARGE ICD #8</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>DISCHARGE ICD #9<em>– Moved to Node 28</em></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>DISCHARGE ICD #10<em>– Moved to Node 28</em></td>
<td></td>
</tr>
</tbody>
</table>

Line 26 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 19%" />
<col style="width: 23%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 26</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-16</td>
<td>2</td>
<td>RPC^DGPTFAPI</td>
<td>PLACE OF DISPOSITION</td>
<td><p>1 RETURN TO COMMUNITY-INDEPENDENT</p>
<p>2 VA MEDICAL CENTER</p>
<p>3 MILITARY HOSPITAL</p>
<p>4 OTHER FEDERAL HOSPITAL</p>
<p>5 OTHER GOVERNMENT HOSPITAL</p>
<p>6 COMMUNITY HOSPITAL</p>
<p>7 VA NURSING HOME CARE UNIT</p>
<p>(NHCU)</p>
<p>8 COMMUNITY NURSING HOME</p>
<p>9 NURSING CARE CONT AT SAM</p>
<p>NURSING HOME</p>
<p>10 NURSE CARE CONTD ANOTHER COMM</p>
<p>NURS HOME</p>
<p>11 STATE HOME</p>
<p>12 VA DOMICILLARY</p>
<p>13 STATE HOME</p>
<p>14 FOSTER HOME</p>
<p>15 HALFWAY HOUSE</p>
<p>16 BOARDING HOUSE</p>
<p>17 PENAL INSTITUTION</p>
<p>18 RESIDENTIAL HOTEL/RESIDENT (IE YMCA)</p>
<p>19 OTHER PLACEMENT/UNKNOWN (NOT</p>
<p>SPECIFIED)</p>
<p>20 HOME-BASED PRIMARY CARE (HBPC)</p>
<p>21 SPINAL CORD INJURY-VACO</p>
<p>APPROVED ONLY</p>
<p>22 HOSPICE CARE</p>
<p>23 RESPITE CARE</p>
<p>24 REFER VA-PD HOME/COMMUNIT</p>
<p>HEALTH</p>
<p>25 REFER MEDICARE HOME HEALTH CARE</p>
<p>26 REFER OTHER AGENCY-PD HOM</p>
<p>HEALTH CARE</p></td>
</tr>
<tr class="even">
<td>17-18</td>
<td>2</td>
<td>200;56 640</td>
<td>PCI</td>
<td><blockquote>
<p>1 NONE</p>
<p>2 &lt;12 HRS OF SURG</p>
<p>3 &gt;12 HRS - 7 DAYS</p>
<p>4 &gt;7 DAYS</p>
<p>5 UNKNOWN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>19-20</td>
<td>2</td>
<td>206;15 352</td>
<td>NUM OF PRIOR SURGERIES</td>
<td><p>0 NONE</p>
<p>1 1</p>
<p>2 2</p>
<p>3 3</p>
<p>&gt; &gt;3</p></td>
</tr>
<tr class="even">
<td>21-22</td>
<td>2</td>
<td></td>
<td>(nOT used)</td>
<td></td>
</tr>
<tr class="odd">
<td>23-24</td>
<td>2</td>
<td>207;27 469</td>
<td>CONVERT FROM OFF PUMP TO CPB</td>
<td><p>1 NO (began off-pump/stayed off-pump)</p>
<p>2 YES-PLANNED</p>
<p>3 YES-UNPLANNED</p>
<p>5 N/A (began on-pump/stayed on-pump)</p>
<p>NS NO STUDY/UNKNOWN</p></td>
</tr>
<tr class="even">
<td>25-26</td>
<td>2</td>
<td>209;1 473</td>
<td>HOMELESS</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NS NO STUDY/UNKNOWN</p></td>
</tr>
<tr class="odd">
<td>27-28</td>
<td>2</td>
<td>209;2 474</td>
<td>PREOP CIRCULATORY DEVICE</td>
<td><p>N NONE</p>
<p>I IABP</p>
<p>V VAD (includes BIVAD)</p>
<p>A ARTIFICIAL HEART</p>
<p>O OTHER</p></td>
</tr>
<tr class="even">
<td>29-30</td>
<td>2</td>
<td>209;3 475</td>
<td><p>DIABETES (CARDIAC)</p>
<p>Not used after 2012 update</p></td>
<td><p>N NO</p>
<p>D DIET</p>
<p>O ORAL</p>
<p>I INSULIN</p></td>
</tr>
<tr class="odd">
<td>31-32</td>
<td>2</td>
<td>209;4 476</td>
<td>PROCEDURE TYPE</td>
<td><p>C CATH</p>
<p>I IVUS</p>
<p>B BOTH/COMBINATION</p>
<p>NS NO STUDY/UNKNOWN</p></td>
</tr>
<tr class="even">
<td>33-34</td>
<td>2</td>
<td>209;5 477</td>
<td>AORTIC STENOSIS</td>
<td><p>0 NONE/TRIVIAL</p>
<p>1 MILD</p>
<p>2 MODERATE</p>
<p>3 SEVERE</p>
<p>NS NO STUDY</p></td>
</tr>
<tr class="odd">
<td>35-37</td>
<td>3</td>
<td>209;6 478</td>
<td>RE-DO LAD STENOSIS</td>
<td>Value or “NS” for No Study/Unknown</td>
</tr>
<tr class="even">
<td>38-40</td>
<td>3</td>
<td>209;7 479</td>
<td>RE-DO RT CORONARY STENOSIS</td>
<td>Value or “NS” for No Study/Unknown</td>
</tr>
<tr class="odd">
<td>41-43</td>
<td>3</td>
<td>209;8 480</td>
<td>RE-DO CIRCUMFLEX STENOSIS</td>
<td>Value or “NS” for No Study/Unknown</td>
</tr>
<tr class="even">
<td>44-45</td>
<td>2</td>
<td>209;9 481</td>
<td><p>BRIDGE TO TRANSPLANT/DEVICE</p>
<p><em>Re-used by SR*3*184</em></p></td>
<td><p>N NONE</p>
<p>B BRIDGE TO TRANSPLANT</p>
<p>D DESTINATION THERAPY</p></td>
</tr>
<tr class="odd">
<td>46-47</td>
<td>2</td>
<td></td>
<td><em>(No longer used)</em></td>
<td></td>
</tr>
<tr class="even">
<td>48-49</td>
<td>2</td>
<td>209;11 483</td>
<td><p>TMR</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>50-54</td>
<td>5</td>
<td>206;42 485</td>
<td><p>PRIOR HEART SURGERIES</p>
<p><em>NO LONGER USED - MOVED BY SR*3*182 TO POSITION 57-62</em></p></td>
<td><p>0 None</p>
<p>1 CABG-only</p>
<p>2 Valve-only</p>
<p>3 CABG/Valve</p>
<p>4 Other</p>
<p>5 CABG/Other</p></td>
</tr>
<tr class="even">
<td>55-56</td>
<td>2</td>
<td>209;12 490</td>
<td><p>REPEAT VENTILATOR W/IN 30 DAYS</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>57-62</td>
<td>6</td>
<td>206;42 485</td>
<td>PRIOR HEART SURGERIES</td>
<td><p>0 None</p>
<p>1 CABG-only</p>
<p>2 Valve-only</p>
<p>3 CABG/Valve</p>
<p>4 Other</p>
<p>5 CABG/Other</p>
<p>6 Unknown</p>
<p>SR*3*182 change</p></td>
</tr>
<tr class="even">
<td>63-64</td>
<td>2</td>
<td>205;43 645</td>
<td>MECHANICAL VENT W/N 30 DAYS</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>65-66</td>
<td>2</td>
<td>205;44 422</td>
<td>OUT-OF-OR UNPLANNED INTUBATION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
</tbody>
</table>

Line 27 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 19%" />
<col style="width: 22%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 27</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-79</td>
<td>65</td>
<td>209.1;1 484</td>
<td><p>OTHER CARDIAC PROCEDURES</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td></td>
</tr>
</tbody>
</table>

Line 28 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 19%" />
<col style="width: 22%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 28</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-16</td>
<td>2</td>
<td>209;13 502</td>
<td><p>OTHER CARDIAC PROCEDURES</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>17-18</td>
<td>2</td>
<td>209;14 512</td>
<td><p>MAZE PROCEDURE</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td><p>N NO MAZE PERFORMED</p>
<p>F FULL MAZE</p>
<p>M MINI MAZE</p></td>
</tr>
<tr class="odd">
<td>19-20</td>
<td>2</td>
<td>207.1;2 505</td>
<td><p>ENDOVASCULAR REPAIR</p>
<p><em>Will not be used after SR*3*182</em></p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>21-26</td>
<td>6</td>
<td>201;28 504</td>
<td>HEMOGLOBIN A1C</td>
<td>Value or “NS” for No Study</td>
</tr>
<tr class="odd">
<td>27-33</td>
<td>7</td>
<td>202.1;1 504.1</td>
<td>HEMOGLOBIN A1C, DATE</td>
<td></td>
</tr>
<tr class="even">
<td>34-38</td>
<td>5</td>
<td>201;29 507</td>
<td>B-TYPE NATRIURETIC PEPTIDE (BNP)</td>
<td>Value or “NS” for No Study</td>
</tr>
<tr class="odd">
<td>39-45</td>
<td>7</td>
<td>202.1;2 507.1</td>
<td>B-TYPE NATRIURETIC PEPTIDE (BNP) DATE</td>
<td></td>
</tr>
<tr class="even">
<td>46-53</td>
<td>8</td>
<td>RPC^DGPTFAPI</td>
<td>Discharge ICD #9</td>
<td></td>
</tr>
<tr class="odd">
<td>54-61</td>
<td>8</td>
<td>RPC^DGPTFAPI</td>
<td>Discharge ICD #10</td>
<td></td>
</tr>
<tr class="even">
<td>62</td>
<td>1</td>
<td>210;1 662</td>
<td>IMPAIRED COGNITIVE FUNCTION</td>
<td><p>0 NONE-NO IMPAIRMENT</p>
<p>1 YES-DOCUMENTED HISTORY</p>
<p>2 YES-DOCUMENTE D AND DECLINING</p>
<p>3 NO STUDY-NO DOCUMENTATION</p></td>
</tr>
</tbody>
</table>

Line 29 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 19%" />
<col style="width: 22%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 29</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-21</td>
<td>7</td>
<td>130.0647,.01</td>
<td>ORGAN TO BE TRANSPLANTED</td>
<td><p>1 HEART, 2 LUNG, 3 KIDNEY</p>
<p>4 LIVER, 5 PANCREAS</p>
<p>6 INTESTINE, 7 OTHER</p></td>
</tr>
<tr class="even">
<td>22-31</td>
<td>10</td>
<td>VER1;2 648</td>
<td>UNOS NUMBER</td>
<td>1-10 chars</td>
</tr>
<tr class="odd">
<td>32-33</td>
<td>2</td>
<td>VER1;3 649</td>
<td>DONOR SEROLOGY HCV</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="even">
<td>34-35</td>
<td>2</td>
<td>VER1;4 650</td>
<td>DONOR SEROLOGY HBV</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="odd">
<td>36-37</td>
<td>2</td>
<td>VER1;5 651</td>
<td>DONOR SEROLOGY CMV</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="even">
<td>38-39</td>
<td>2</td>
<td>VER1;6 652</td>
<td>DONOR SEROLOGY HIV</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="odd">
<td>40</td>
<td>1</td>
<td>VER1;7 653</td>
<td>DONOR ABO TYPE</td>
<td><p>1 A RH(+)</p>
<p>2 A RH(-)</p>
<p>3 B RH(+)</p>
<p>4 B RH(-)</p>
<p>5 AB RH(+)</p>
<p>6 AB RH(-)</p>
<p>7 O RH(+)</p>
<p>8 O RH(-)</p></td>
</tr>
<tr class="even">
<td>41</td>
<td>1</td>
<td>VER1;8 654</td>
<td>RECIPIENT ABO TYPE</td>
<td><p>1 A RH(+)</p>
<p>2 A RH(-)</p>
<p>3 B RH(+)</p>
<p>4 B RH(-)</p>
<p>5 AB RH(+)</p>
<p>6 AB RH(-)</p>
<p>7 O RH(+)</p>
<p>8 O RH(-)</p></td>
</tr>
<tr class="odd">
<td>42</td>
<td>1</td>
<td>VER1;9 655</td>
<td>BLOOD BANK ABO VERIFICATION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>43-54</td>
<td>12</td>
<td>VER1;19 747</td>
<td>D/T BLOOD BANK ABO VERIF</td>
<td></td>
</tr>
<tr class="odd">
<td>55</td>
<td>1</td>
<td>VER1;10 656</td>
<td>OR ABO VERIFICATION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>56-67</td>
<td>12</td>
<td>VER1;21 749</td>
<td></td>
<td>D/T OR ABO VERIF</td>
</tr>
<tr class="odd">
<td>68</td>
<td>1</td>
<td>VER1;22 750</td>
<td>UNET VERIF BY SURGEON</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>69</td>
<td>1</td>
<td>VER1;12 658</td>
<td>ORGAN VER PRE-ANESTHESIA</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>70</td>
<td>1</td>
<td>VER1;24 752</td>
<td>DONOR ORG VER PRE-ANES</td>
<td><p>1 YES</p>
<p>2 NO</p>
<p>3 NOT APPLICABLE</p></td>
</tr>
<tr class="even">
<td>71</td>
<td>1</td>
<td>VER1;14 660</td>
<td>ORGAN VER PRE-TRANSPLANT</td>
<td><p>1 YES</p>
<p>2 NO</p>
<p>3 NOT APPLICABLE</p></td>
</tr>
<tr class="odd">
<td>72</td>
<td>1</td>
<td>VER1;15 663</td>
<td>DONOR VESSEL USAGE</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>73-74</td>
<td>2</td>
<td>VER1;16 665</td>
<td><p>DONOR VESSEL DISPOSITION</p>
<p>Updated with SR*3*205</p></td>
<td><p>N NO DONOR VESSELS RECEIVED</p>
<p>D DISCARDED</p>
<p>R RETURNED TO OPO</p>
<p>S STORED</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
</tbody>
</table>

Line 30 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 19%" />
<col style="width: 22%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 30</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-44</td>
<td>30</td>
<td>VER1;11 657</td>
<td>SURGEON VERIFYING UNET</td>
<td>Name field</td>
</tr>
<tr class="even">
<td>45-74</td>
<td>30</td>
<td>VER1;23 751</td>
<td>SURGEON VER ORGAN PRE-ANES</td>
<td>Name field</td>
</tr>
</tbody>
</table>

Line 31 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 19%" />
<col style="width: 23%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 31</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-44</td>
<td>30</td>
<td>VER1;13 659</td>
<td>SURGEON VER DONOR ORG PRE-ANES</td>
<td>Name field</td>
</tr>
<tr class="even">
<td>45-74</td>
<td>30</td>
<td>VER1;25 753</td>
<td>SURGEON VER ORG PRE-TRANSPLANT</td>
<td>Name field</td>
</tr>
</tbody>
</table>

Line 32 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 21%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 32</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-24</td>
<td>10</td>
<td>57;0 Multiple #130.0664</td>
<td>DONOR VESSEL UNOS ID – Entry #1</td>
<td>1-10 chars Free-Text</td>
</tr>
<tr class="even">
<td>25-34</td>
<td>10</td>
<td>57;0 Multiple #130.0664</td>
<td>DONOR VESSEL UNOS ID – Entry #2</td>
<td>1-10 chars Free-Text</td>
</tr>
<tr class="odd">
<td>35-44</td>
<td>10</td>
<td>57;0 Multiple #130.0664</td>
<td>DONOR VESSEL UNOS ID – Entry #3</td>
<td>1-10 chars Free-Text</td>
</tr>
<tr class="even">
<td>45-54</td>
<td>10</td>
<td>57;0 Multiple #130.0664</td>
<td>DONOR VESSEL UNOS ID – Entry #4</td>
<td>1-10 chars Free-Text</td>
</tr>
<tr class="odd">
<td>55-64</td>
<td>10</td>
<td>57;0 Multiple #130.0664</td>
<td>DONOR VESSEL UNOS ID – Entry #5</td>
<td>1-10 chars Free-Text</td>
</tr>
<tr class="even">
<td>65-74</td>
<td>10</td>
<td>57;0 Multiple #130.0664</td>
<td>DONOR VESSEL UNOS ID – Entry #6</td>
<td>1-10 chars Free-Text</td>
</tr>
</tbody>
</table>

Line 33 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 21%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 33</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-24</td>
<td>10</td>
<td>57;0 Multiple #130.0664</td>
<td>DONOR VESSEL UNOS ID – Entry #7</td>
<td>1-10 chars Free-Text</td>
</tr>
<tr class="even">
<td>25-26</td>
<td>2</td>
<td>211;1 686</td>
<td>AORTIC REGURGITATION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>27-28</td>
<td>2</td>
<td>211;2 687</td>
<td>INJURY TO ADJACENT ORGAN</td>
<td><p>0 NO;</p>
<p>1 YES, WITH INTERVENTION</p>
<p>2 YES, WITH NO INTERVENTION REQ</p></td>
</tr>
<tr class="even">
<td>29-30</td>
<td>2</td>
<td>211;3 688</td>
<td>STOMA COMPLICATIONS</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>31-32</td>
<td>2</td>
<td>211;4 689</td>
<td>NON-UNION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>33-34</td>
<td>2</td>
<td>211;5 690</td>
<td>IMPLANT INFECTIONS</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>35-36</td>
<td>2</td>
<td>211;6 691</td>
<td>CHYLE/LYMPH LEAK</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>37-38</td>
<td>2</td>
<td>211;7 692</td>
<td>ANASTOMOTIC LEAK</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>39-40</td>
<td>2</td>
<td>211;8 693</td>
<td>FISTULA</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>41-42</td>
<td>2</td>
<td>211;9 694</td>
<td>NECROTIZING SOFT TISS INFECT</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>43-44</td>
<td>2</td>
<td>211;10 695</td>
<td>OTHER BLOOD PRODUCT UNITS</td>
<td><p>0 NONE</p>
<p>1 PLATELETS</p>
<p>2 FRESH FROZEN PLASMA</p>
<p>3 PLASMA AND PLATELETS</p>
<p>4 ANY OTHER COMBINATION</p>
<p>5 ANY OTHER BLOOD PRODUCT</p></td>
</tr>
<tr class="even">
<td>45-46</td>
<td>2</td>
<td>211;11 696</td>
<td>PRESSORS USED INTRAOP</td>
<td><p>0 NO</p>
<p>1 YES-BOLUS</p>
<p>2 YES-CONTINUOUS INFUSION</p></td>
</tr>
<tr class="odd">
<td>47-48</td>
<td>2</td>
<td>211;12 697</td>
<td>MITRAL STENOSIS</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>49-50</td>
<td>2</td>
<td>211;13 698</td>
<td>PCI INTERVENTION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>51-52</td>
<td>2</td>
<td>211;14 699</td>
<td>ATRIAL ARRHYTHMIAS</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>53-54</td>
<td>2</td>
<td>211;15 700</td>
<td>HEAD OR NECK CANCER</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>55-56</td>
<td>2</td>
<td>211;16 701</td>
<td>MACULAR DEGENERATION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>57-58</td>
<td>2</td>
<td>211;17 702</td>
<td>GLAUCOMA</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>59-60</td>
<td>2</td>
<td>211;20 705</td>
<td>AXIAL LEN/ANTERIOR CHAM DEP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>61-62</td>
<td>2</td>
<td>211;19 704</td>
<td>HX RETINAL DETACHMENT</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>63-64</td>
<td>2</td>
<td>211;21 706</td>
<td>CORNEAL GUTTAE/FUCHS ENDO</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>65-66</td>
<td>2</td>
<td>211;22 707</td>
<td>DIABETIC RETINOPATHY</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>67-68</td>
<td>2</td>
<td>211;23 708</td>
<td>COMPLEX CATARACT</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>69-70</td>
<td>2</td>
<td>211;24 709</td>
<td>STATIN 30 DAYS PREOP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>71-72</td>
<td>2</td>
<td>211;25 710</td>
<td>IPSILAT CORTICAL EVENT PREOP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>73-74</td>
<td>2</td>
<td>211;26 711</td>
<td>PREOP MODIFIED RANKIN SCORE</td>
<td></td>
</tr>
<tr class="odd">
<td>75-76</td>
<td>2</td>
<td>211;27 712</td>
<td>CAROTID SUR ANATOMIC HIGH RISK</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>77-78</td>
<td>2</td>
<td>211;28 713</td>
<td>BYPASS CRITICAL LIMB ISCHEMIA</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
</tbody>
</table>

Line 34 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 21%" />
<col style="width: 20%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 34</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-20</td>
<td>6</td>
<td><p>64;0 714</p>
<p>multiple field</p></td>
<td>INDIC DESC THOR ENDOGRAFT</td>
<td><p>1 ACUTE DISSECTION</p>
<p>2 CHRONIC DISSECTION</p>
<p>3 ANEURYSM</p>
<p>4 ATHEROSCLEROTIC OCCLUSIVE DISEASE</p>
<p>5 OTHER</p></td>
</tr>
<tr class="even">
<td>21-22</td>
<td>2</td>
<td>211;30 715</td>
<td>ENDOLEAK AT COMPLETION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>23-27</td>
<td>5</td>
<td>211;31 716</td>
<td>HIGH HEART RATE 6HRS PREOP</td>
<td>Numeric (30-250)</td>
</tr>
<tr class="even">
<td>28-32</td>
<td>5</td>
<td>211;32 717</td>
<td>HIGH HEART RATE INTRAOP</td>
<td>Numeric (30-250)</td>
</tr>
<tr class="odd">
<td>33-37</td>
<td>5</td>
<td>211;35 722</td>
<td>LOWEST PH INTRAOP</td>
<td>from 6.80 to 7.60 with 3 significant digits</td>
</tr>
<tr class="even">
<td>38-41</td>
<td>4</td>
<td>211;34 719</td>
<td>HIGH LACTIC ACID 6HRS PREOP</td>
<td>number between 0 and 30, 1 decimal</td>
</tr>
<tr class="odd">
<td>42-45</td>
<td>4</td>
<td>211;39 727</td>
<td>LOWEST BICARBONATE INTRAOP</td>
<td>from 0 to 40 with on decimal</td>
</tr>
<tr class="even">
<td>46-48</td>
<td>3</td>
<td>211;33 718</td>
<td>LOW ARTERIAL PRESS 6HRS PREOP</td>
<td>between 0 and 200</td>
</tr>
<tr class="odd">
<td>49-51</td>
<td>3</td>
<td>211;36 723</td>
<td>LOW ARTERIAL PRESS INTRAOP</td>
<td>between 0 and 200</td>
</tr>
<tr class="even">
<td>52-54</td>
<td>3</td>
<td>211;40 728</td>
<td>UNITS TRANSFUSED 6HRS PREOP</td>
<td>from 0 to 100</td>
</tr>
<tr class="odd">
<td>55-56</td>
<td>2</td>
<td>211;37 724</td>
<td>OLIGURIA &lt;60CC/2HRS 6HRS PREOP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>57-58</td>
<td>2</td>
<td>211;38 725</td>
<td>OLIGURIA URINE OUTPUT INTRAOP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>59-60</td>
<td>2</td>
<td>211;41 729</td>
<td>VASOPRESSOR USAGE AT OR ENTRY</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>61-62</td>
<td>2</td>
<td>211;42 730</td>
<td>CARDIAC ARREST 24HRS PREOP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>63-64</td>
<td>2</td>
<td>211;43 731</td>
<td>DIC W/IN 6HRS PREOP</td>
<td><p>1 SCORE &lt;5</p>
<p>2 SCORE &gt; OR EQUAL 5</p></td>
</tr>
<tr class="even">
<td>65-68</td>
<td>4</td>
<td>VERD;6 720</td>
<td>HIGH LACTIC ACID INTRAOP</td>
<td>number between 0 and 30, 1 decimal</td>
</tr>
<tr class="odd">
<td>69-73</td>
<td>5</td>
<td>VERD;7 721</td>
<td>LOWEST PH 6HRS PREOP</td>
<td>from 6.80 to 7.60 with 3 significant digits</td>
</tr>
<tr class="even">
<td>74-77</td>
<td>4</td>
<td>VERD;8 726</td>
<td>LOWEST BICARBONATE 6HRS PREOP</td>
<td>from 0-40 with 1 decimal</td>
</tr>
</tbody>
</table>

Line 35 of the Cardiac Transmission Layout

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 21%" />
<col style="width: 20%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 35</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-16</td>
<td>2</td>
<td>210;2 666</td>
<td>LIVER DISEASE/CIRRHOSIS</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>17-18</td>
<td>2</td>
<td>210;3 668</td>
<td>IMMUNOCOMPROMISED STATE PREOP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>19-20</td>
<td>2</td>
<td>210;4 669</td>
<td>PULMONARY HTN</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>21-22</td>
<td>2</td>
<td>210;7 672</td>
<td>NUTRITIONAL SUPPLEMENT PREOP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>23-24</td>
<td>2</td>
<td>210;10 675</td>
<td>PRIOR INFEC/INFLAM SURG FIELD</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>25-26</td>
<td>2</td>
<td>210;11 676</td>
<td>HX DEEP VEIN THROMBOSIS</td>
<td><p>1 NEITHER DVT NOR PE</p>
<p>2 DVT WITHOUT PE</p>
<p>3 PE WITHOUT DVT</p>
<p>4 BOTH DVT AND PE</p></td>
</tr>
<tr class="odd">
<td>27-28</td>
<td>2</td>
<td>211;44 732</td>
<td>HYPOXEMIA W/IN 6HRS PREOP</td>
<td><p>1 NOT MEASURED</p>
<p>2 PAO2/FIO2 &lt; 200</p>
<p>3 PAO2/FIO2 200-249</p>
<p>4 PAO2/FIO2 250-299</p>
<p>5 PAO2/FIO2 &gt; 300</p></td>
</tr>
<tr class="even">
<td>29-30</td>
<td>2</td>
<td>211;45 733</td>
<td>ENDOLEAK AT FOLLOW-UP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>31-32</td>
<td>2</td>
<td>211;46 734</td>
<td>CARDIAC ARREST INTRAOP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>33-34</td>
<td>2</td>
<td>211;47 735</td>
<td>FLOPPY IRIS INTRAOP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>35-36</td>
<td>2</td>
<td>211;48 736</td>
<td>PREOP VISUAL ACUITY</td>
<td><p>1 20/20 OR BETTER</p>
<p>2 &gt; 20/20 - 20/50</p>
<p>3 &gt; 20/50 - 20/100</p>
<p>4 &gt; 20/100 - 20/200</p>
<p>5 &gt; 20/200</p>
<p>6 HAND MOTION</p>
<p>7 LIGHT PERCEPTION</p>
<p>8 NO LIGHT PERCEPTION</p></td>
</tr>
<tr class="even">
<td>37-38</td>
<td>2</td>
<td>211;49 737</td>
<td>POSTOP VISUAL ACUITY</td>
<td><p>1 20/20 OR BETTER</p>
<p>2 &gt; 20/20 - 20/50</p>
<p>3 &gt; 20/50 - 20/100</p>
<p>4 &gt; 20/100 - 20/200</p>
<p>5 &gt; 20/200</p>
<p>6 HAND MOTION</p>
<p>7 LIGHT PERCEPTION</p>
<p>8 NO LIGHT PERCEPTION</p></td>
</tr>
<tr class="odd">
<td>39-40</td>
<td>2</td>
<td>211;50 738</td>
<td>ENDOPHTHALMITIS TYPE</td>
<td><p>0 NO ENDOPHTHALMITIS</p>
<p>1 BACTERIAL</p>
<p>2 TASS</p></td>
</tr>
<tr class="even">
<td>41-42</td>
<td>2</td>
<td>211;51 739</td>
<td>CYSTOID MACULAR EDEMA</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>43-44</td>
<td>2</td>
<td>211;52 740</td>
<td>DISLOCATION OF OPERATIVE JOINT</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>45-46</td>
<td>2</td>
<td>211;53 741</td>
<td>PERIPROSTHETIC FRACTURES</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>47-58</td>
<td>12</td>
<td>211;54 742</td>
<td>D/T PAT ARRIVES HOSP DAY SURG</td>
<td>Date/Time</td>
</tr>
<tr class="even">
<td>59-70</td>
<td>12</td>
<td>211;55 743</td>
<td>D/T PAT LEAVES HOSP DAY SURG</td>
<td>Date/Time</td>
</tr>
<tr class="odd">
<td>71-73</td>
<td>3</td>
<td>211;56 744</td>
<td>KIDNEY DONOR PROFILE INDEX</td>
<td>(0-100)</td>
</tr>
<tr class="even">
<td>74-76</td>
<td>3</td>
<td>211;57 745</td>
<td>EXPECTED POST TRANSPLANT INDEX</td>
<td>(0-100)</td>
</tr>
</tbody>
</table>

## Appendix C: Workload Report Transmission Layout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each line begins with Station Number in piece 1. Fields listed below are sub-fields within the MONTHLY WORKLOAD REPORT multiple field (#1, sub-file \#139.11) in the RISK ASSESSMENT SITE file (#139.1). D1 in the Global column represents the IEN of the Monthly Workload Report in sub-file \#139.11)

Line 1 of the Workload Report Transmission Layout

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 17%" />
<col style="width: 23%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 1</p>
<p>Piece</p></th>
<th>Global</th>
<th>Field</th>
<th>Field Name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2</td>
<td>1,D1,0;1</td>
<td>.01</td>
<td>MONTHLY WORKLOAD REPORT</td>
</tr>
<tr class="even">
<td>3</td>
<td>1,D1,0;2</td>
<td>.05</td>
<td>DATE TRANSMITTED</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1,D1,0;3</td>
<td>1</td>
<td>TOTAL CASES</td>
</tr>
<tr class="even">
<td>5</td>
<td>1,D1,0;4</td>
<td>2</td>
<td>EXCLUDED CASES</td>
</tr>
<tr class="odd">
<td>6</td>
<td>1,D1,0;5</td>
<td>3</td>
<td>ASSESSED CASES</td>
</tr>
<tr class="even">
<td>7</td>
<td>1,D1,0;6</td>
<td>4</td>
<td>NON-ASSESSED CASES (aka NOT LOGGED MAJOR CASES)</td>
</tr>
<tr class="odd">
<td>8</td>
<td>1,D1,0;7</td>
<td>5</td>
<td>CARDIAC CASES</td>
</tr>
<tr class="even">
<td>9</td>
<td>1,D1,0;8</td>
<td>6</td>
<td>NON-CARDIAC CASES</td>
</tr>
<tr class="odd">
<td>10</td>
<td>1,D1,0;9</td>
<td>7</td>
<td>ASSESSED CASE/DAY</td>
</tr>
<tr class="even">
<td>11</td>
<td>1,D1,0,10</td>
<td>8</td>
<td>MAJOR CASES</td>
</tr>
<tr class="odd">
<td>12</td>
<td>1,D1,0,11</td>
<td>9</td>
<td>MINOR CASES</td>
</tr>
<tr class="even">
<td>13</td>
<td>1,D1,0,12</td>
<td>2.1</td>
<td>EXCLUSION TYPE 1 (ANESTHESIA TYPE – No longer used))</td>
</tr>
<tr class="odd">
<td>14</td>
<td>1,D1,0,13</td>
<td>2.2</td>
<td>EXCLUSION TYPE 2 (EXCEEDS MAX ASSMNTS)</td>
</tr>
<tr class="even">
<td>15</td>
<td>1,D1,0,14</td>
<td>2.3</td>
<td>EXCLUSION TYPE 3 (EXCEEDS MAX TURPS)</td>
</tr>
<tr class="odd">
<td>16</td>
<td>1,D1,0,15</td>
<td>2.4</td>
<td>EXCLUSION TYPE 4 (STUDY CRITERIA)</td>
</tr>
<tr class="even">
<td>17</td>
<td>1,D1,0,16</td>
<td>2.6</td>
<td>EXCLUSION TYPE 6 (SCNR ON A/L)</td>
</tr>
<tr class="odd">
<td>18</td>
<td>1,D1,0,17</td>
<td>2.8</td>
<td>EXCLUSION TYPE 8 (CONCURRENT CASE)</td>
</tr>
<tr class="even">
<td>19</td>
<td>1,D1,0,18</td>
<td>2.9</td>
<td>EXCLUSION TYPE 9 (EXCEEDS MAX HERNIAS)</td>
</tr>
<tr class="odd">
<td>20</td>
<td>1,D1,0,19</td>
<td>2.11</td>
<td>EXCLUSION TYPE 0 (NON-SURGEON CASE)</td>
</tr>
</tbody>
</table>

Line 2 of the Workload Report Transmission Layout

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 16%" />
<col style="width: 22%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 2</p>
<p>Piece</p></th>
<th>Global</th>
<th>Field</th>
<th>Field Name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2</td>
<td>1,D1,1;1</td>
<td>10</td>
<td>MONTH #1</td>
</tr>
<tr class="even">
<td>3</td>
<td>1,D1,1;2</td>
<td>10.1</td>
<td>MONTH #1 CARDIAC</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1,D1,1;3</td>
<td>10.2</td>
<td>MONTH #1 NON-CARDIAC</td>
</tr>
<tr class="even">
<td>5</td>
<td>1,D1,1;4</td>
<td>11</td>
<td>MONTH #2</td>
</tr>
<tr class="odd">
<td>6</td>
<td>1,D1,1;5</td>
<td>11.1</td>
<td>MONTH #2 CARDIAC</td>
</tr>
<tr class="even">
<td>7</td>
<td>1,D1,1;6</td>
<td>11.2</td>
<td>MONTH #2 NON-CARDIAC</td>
</tr>
<tr class="odd">
<td>8</td>
<td>1,D1,1;7</td>
<td>12</td>
<td>MONTH #3</td>
</tr>
<tr class="even">
<td>9</td>
<td>1,D1,1;8</td>
<td>12.1</td>
<td>MONTH #3 CARDIAC</td>
</tr>
<tr class="odd">
<td>10</td>
<td>1,D1,1;9</td>
<td>12.2</td>
<td>MONTH #3 NON-CARDIAC</td>
</tr>
<tr class="even">
<td>11</td>
<td>1,D1,1;10</td>
<td>13</td>
<td>MONTH #4</td>
</tr>
<tr class="odd">
<td>12</td>
<td>1,D1,1;11</td>
<td>13.1</td>
<td>MONTH #4 CARDIAC</td>
</tr>
<tr class="even">
<td>13</td>
<td>1,D1,1;12</td>
<td>13.2</td>
<td>MONTH #4 NON-CARDIAC</td>
</tr>
<tr class="odd">
<td>14</td>
<td>1,D1,1;13</td>
<td>14</td>
<td>MONTH #5</td>
</tr>
<tr class="even">
<td>15</td>
<td>1,D1,1;14</td>
<td>14.1</td>
<td>MONTH #5 CARDIAC</td>
</tr>
<tr class="odd">
<td>16</td>
<td>1,D1,1;15</td>
<td>14.2</td>
<td>MONTH #5 NON-CARDIAC</td>
</tr>
<tr class="even">
<td>17</td>
<td>1,D1,1;16</td>
<td>15</td>
<td>MONTH #6</td>
</tr>
<tr class="odd">
<td>18</td>
<td>1,D1,1;17</td>
<td>15.1</td>
<td>MONTH #6 CARDIAC</td>
</tr>
<tr class="even">
<td>19</td>
<td>1,D1,1;18</td>
<td>15.2</td>
<td>MONTH #6 NON-CARDIAC</td>
</tr>
<tr class="odd">
<td>20</td>
<td>1,D1,1;19</td>
<td>16</td>
<td>MONTH #7</td>
</tr>
<tr class="even">
<td>21</td>
<td>1,D1,1;20</td>
<td>16.1</td>
<td>MONTH #7 CARDIAC</td>
</tr>
<tr class="odd">
<td>22</td>
<td>1,D1,1;21</td>
<td>16.2</td>
<td>MONTH #7 NON-CARDIAC</td>
</tr>
<tr class="even">
<td>23</td>
<td>1,D1,1;22</td>
<td>17</td>
<td>MONTH #8</td>
</tr>
<tr class="odd">
<td>24</td>
<td>1,D1,1;23</td>
<td>17.1</td>
<td>MONTH #8 CARDIAC</td>
</tr>
<tr class="even">
<td>25</td>
<td>1,D1,1;24</td>
<td>17.2</td>
<td>MONTH #8 NON-CARDIAC</td>
</tr>
<tr class="odd">
<td>26</td>
<td>1,D1,1;25</td>
<td>18</td>
<td>MONTH #9</td>
</tr>
<tr class="even">
<td>27</td>
<td>1,D1,1;26</td>
<td>18.1</td>
<td>MONTH #9 CARDIAC</td>
</tr>
<tr class="odd">
<td>28</td>
<td>1,D1,1;27</td>
<td>18.2</td>
<td>MONTH #9 NON-CARDIAC</td>
</tr>
<tr class="even">
<td>29</td>
<td>1,D1,1;28</td>
<td>19</td>
<td>MONTH #10</td>
</tr>
<tr class="odd">
<td>30</td>
<td>1,D1,1;29</td>
<td>19.1</td>
<td>MONTH #10 CARDIAC</td>
</tr>
<tr class="even">
<td>31</td>
<td>1,D1,1;30</td>
<td>19.2</td>
<td>MONTH #10 NON-CARDIAC</td>
</tr>
<tr class="odd">
<td>32</td>
<td>1,D1,1;31</td>
<td>20</td>
<td>MONTH #11</td>
</tr>
<tr class="even">
<td>33</td>
<td>1,D1,1;32</td>
<td>20.1</td>
<td>MONTH #11 CARDIAC</td>
</tr>
<tr class="odd">
<td>34</td>
<td>1,D1,1;33</td>
<td>20.2</td>
<td>MONTH #11 NON-CARDIAC</td>
</tr>
<tr class="even">
<td>35</td>
<td>1,D1,1;34</td>
<td>21</td>
<td>MONTH #12</td>
</tr>
<tr class="odd">
<td>36</td>
<td>1,D1,1;35</td>
<td>21.1</td>
<td>MONTH #12 CARDIAC</td>
</tr>
<tr class="even">
<td>37</td>
<td>1,D1,1;36</td>
<td>21.2</td>
<td>MONTH #12 NON-CARDIAC</td>
</tr>
<tr class="odd">
<td>38</td>
<td>1,D1,2;1</td>
<td>22</td>
<td>MONTH #13</td>
</tr>
<tr class="even">
<td>39</td>
<td>1,D1,2;2</td>
<td>22.1</td>
<td>MONTH #13 CARDIAC</td>
</tr>
<tr class="odd">
<td>40</td>
<td>1,D1,2;3</td>
<td>22.2</td>
<td>MONTH #13 NON-CARDIAC</td>
</tr>
<tr class="even">
<td>41</td>
<td></td>
<td></td>
<td>Field transmitted as “0”</td>
</tr>
</tbody>
</table>

Line 3 of the Workload Report Transmission Layout

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 17%" />
<col style="width: 23%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 3</p>
<p>Piece</p></th>
<th>Global</th>
<th>Field</th>
<th>Field Name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2</td>
<td></td>
<td></td>
<td>(If 0, send ACK)</td>
</tr>
<tr class="even">
<td>3</td>
<td>1,D1,0;20</td>
<td>8.5</td>
<td>ELIGIBLE CASES</td>
</tr>
<tr class="odd">
<td>4</td>
<td>1,D1,0;21</td>
<td>4.5</td>
<td>NOT LOGGED ELIGIBLE CASES</td>
</tr>
<tr class="even">
<td>5</td>
<td>1,D1,0;23</td>
<td>2006</td>
<td>ROBOTIC ASSISTED CASES</td>
</tr>
</tbody>
</table>

## Appendix D: 1-Liner Transmission Layout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 1-Liner transmission layout was last updated in 2024 by SR\*3.0\*205 and SRA\*3.0\*9.

Each line begins with ‘@’ in position 1, Station Number in positions 2-4, Case Number in positions 5-11, and Line Identifier in positions 12-14.

Line 1 of the 1-Liner Transmission Layout

<table style="width:100%;">
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 18%" />
<col style="width: 17%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line 1</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>14</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td><p>C Cardiac</p>
<p>* Excluded</p>
<p>X All others</p></td>
</tr>
<tr class="even">
<td>15-21</td>
<td>7</td>
<td>0;9 .09</td>
<td>0;5 4</td>
<td>Date of operation</td>
<td></td>
</tr>
<tr class="odd">
<td>22-24</td>
<td>3</td>
<td>6;0 .37</td>
<td>2;6 192</td>
<td>anesthesia technique</td>
<td><p>G GENERAL</p>
<p>S SPINAL</p>
<p>E EPIDURAL</p>
<p>M MONITORED ANESTHESIA CARE</p>
<p>L LOCAL</p>
<p>R REGIONAL</p>
<p>N NO ANESTHESIA</p></td>
</tr>
<tr class="even">
<td>25</td>
<td>1</td>
<td>0;10 .035</td>
<td>0;6 291</td>
<td>EMERGENCY (Y/N)</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>26-28</td>
<td>3</td>
<td>0;4 .04</td>
<td>0;2 23</td>
<td>SURGICAL SPECIALTY</td>
<td><p>48 CARDIAC SURGERY</p>
<p>49 TRANSPLANTATION</p>
<p>50 GENERAL SURGERY</p>
<p>51 OB/GYN</p>
<p>52 NEUROSURGERY</p>
<p>53 OPHTHALMOLOGY</p>
<p>54 ORTHOPEDICS</p>
<p>55 EAR, NOSE, THROAT (ENT)</p>
<p>56 PLASTIC SURGERY</p>
<p>57 PROCTOLOGY</p>
<p>58 THORACIC SURGERY</p>
<p>59 UROLOGY</p>
<p>60 ORAL SURGERY</p>
<p>61 PODIATRY</p>
<p>62 PERIPHERAL VASCULAR</p>
<p>78 ANESTHESIOLOGY</p></td>
</tr>
<tr class="even">
<td>29-33</td>
<td>5</td>
<td>0;2(136) .02(136)</td>
<td>OP;2 8</td>
<td>PRINCIPAL OPERATION (cpt)</td>
<td></td>
</tr>
<tr class="odd">
<td>34</td>
<td>1</td>
<td>RA;7 102</td>
<td>S;5 305</td>
<td>EXCLUSION REASON</td>
<td><p>0 NON-SURGEON CASE</p>
<p>2 EXCEEDS MAX ASSMNTS</p>
<p>3 EXCEEDS MAX TURPS</p>
<p>4 STUDY CRITERIA</p>
<p>6 10% RULE</p>
<p>8 CONCURRENT CASE</p>
<p>9 EXCEEDS MAX HERNIAS</p></td>
</tr>
<tr class="even">
<td>35-54</td>
<td>20</td>
<td>VA(“PID”)</td>
<td>SRAPID;1 309</td>
<td>PATIENT ID</td>
<td></td>
</tr>
<tr class="odd">
<td>55-60</td>
<td>6</td>
<td>8;1 50</td>
<td>0;18 7</td>
<td>DIVISION</td>
<td></td>
</tr>
<tr class="even">
<td>61</td>
<td>1</td>
<td>VADM(5)</td>
<td>0;4 3</td>
<td>SEX</td>
<td><p>M MALE</p>
<p>F FEMALE</p></td>
</tr>
<tr class="odd">
<td>62</td>
<td>1</td>
<td>0;3 .03</td>
<td>0;25 319</td>
<td>MAJOR/MINOR</td>
<td><p>J MAJOR</p>
<p>N MINOR</p></td>
</tr>
<tr class="even">
<td>63-69</td>
<td>7</td>
<td></td>
<td></td>
<td><em>- blank -</em></td>
<td></td>
</tr>
<tr class="odd">
<td>70</td>
<td>1</td>
<td>.4;7 903</td>
<td>0;23 308</td>
<td>DEATH UNRELATED/RELATED</td>
<td><p>U UNRELATED</p>
<p>R RELATED</p></td>
</tr>
<tr class="even">
<td>71</td>
<td>1</td>
<td>0;12 .011</td>
<td>0;24 318</td>
<td>HOSPITAL ADMISSION STATUS</td>
<td><p>O OUTPATIENT</p>
<p>I INPATIENT</p>
<p>1 SAME DAY</p>
<p>2 ADMISSION</p>
<p>3 HOSPITALIZED</p></td>
</tr>
<tr class="odd">
<td>72-74</td>
<td>3</td>
<td>Opdate – DoB</td>
<td>0;3 2</td>
<td>Age</td>
<td></td>
</tr>
<tr class="even">
<td>75-76</td>
<td>2</td>
<td>1.1;3 1.13</td>
<td>1;2 12</td>
<td>ASA CLASSIFICATION</td>
<td><p>1 1. NO DISTURBANCE</p>
<p>2 2. MILD DISTURBANCE</p>
<p>3 3. SEVERE DISTURBANCE</p>
<p>4 4. LIFE THREATENING</p>
<p>5 5. MORIBUND</p>
<p>N NONE ASSIGNED</p>
<p>1E 1-EMERG.</p>
<p>2E 2-EMERG.</p>
<p>3E 3-EMERG.</p>
<p>4E 4-EMERG.</p>
<p>5E 5-EMERG.</p>
<p>6 6. BRAIN-DEAD</p>
<p>6E 6-EMERG.</p></td>
</tr>
<tr class="odd">
<td>77</td>
<td>1</td>
<td></td>
<td>0;27 14</td>
<td>ADMIT WI 14 DAYS AFTER OUTPAT SURG</td>
<td></td>
</tr>
<tr class="even">
<td>78-79</td>
<td>2</td>
<td></td>
<td>20;1 380</td>
<td>1 NUMBER OF SUPERFICIAL INCISIONAL SSI</td>
<td></td>
</tr>
<tr class="odd">
<td>80-81</td>
<td>2</td>
<td></td>
<td>20;2 381</td>
<td>2 NUMBER OF DEEP INCISIONAL SSI</td>
<td></td>
</tr>
<tr class="even">
<td>82-83</td>
<td>2</td>
<td></td>
<td>20;4 382</td>
<td>3 NUMBER OF SYSTEMIC SEPSIS</td>
<td></td>
</tr>
<tr class="odd">
<td>84-85</td>
<td>2</td>
<td></td>
<td>20;4 383</td>
<td>4 NUMBER OF PNEUMONIA</td>
<td></td>
</tr>
<tr class="even">
<td>86-87</td>
<td>2</td>
<td></td>
<td>20;5 384</td>
<td>5 NUMBER OF PULMONARY EMBOLISM</td>
<td></td>
</tr>
<tr class="odd">
<td>88-89</td>
<td>2</td>
<td></td>
<td>20;6 385</td>
<td>6 NUMBER OF ON VENTILATOR &gt; 48 HOURS</td>
<td></td>
</tr>
<tr class="even">
<td>90-91</td>
<td>2</td>
<td></td>
<td>20;7 386</td>
<td>7 NUMBER OF UNPLANNED INTUBATION</td>
<td></td>
</tr>
<tr class="odd">
<td>92-93</td>
<td>2</td>
<td></td>
<td>20;8 387</td>
<td>8 NUMBER OF RENAL INSUFFICIENCY</td>
<td></td>
</tr>
<tr class="even">
<td>94-95</td>
<td>2</td>
<td></td>
<td>20;9 388</td>
<td>9 NUMBER OF ACUTE RENAL FAILURE</td>
<td></td>
</tr>
<tr class="odd">
<td>96-97</td>
<td>2</td>
<td></td>
<td>20;10 389</td>
<td>10 NUMBER OF URINARY TRACT INFECTION</td>
<td></td>
</tr>
<tr class="even">
<td>98-99</td>
<td>2</td>
<td></td>
<td>20;40 437</td>
<td>37 NUMBER OF REPEAT VENT SUPPORT</td>
<td></td>
</tr>
<tr class="odd">
<td>100-101</td>
<td>2</td>
<td></td>
<td>20;12 391</td>
<td>12 NUMBER OF STROKE/CVA</td>
<td></td>
</tr>
<tr class="even">
<td>102-103</td>
<td>2</td>
<td></td>
<td>20;13 392</td>
<td>13 NUMBER OF COMA &gt; 24 HOURS</td>
<td></td>
</tr>
<tr class="odd">
<td>104-105</td>
<td>2</td>
<td></td>
<td>20;14 393</td>
<td>14 NUMBER OF PERIPHERAL NERVE INJURY</td>
<td></td>
</tr>
<tr class="even">
<td>106-107</td>
<td>2</td>
<td></td>
<td>20;15 394</td>
<td>15 NUMBER OF BLEEDING/TRANSFUSIONS</td>
<td></td>
</tr>
<tr class="odd">
<td>108-109</td>
<td>2</td>
<td></td>
<td>20;16 395</td>
<td><p>16 NUMBER OF CARDIAC ARREST</p>
<p>REQUIRING CPR</p></td>
<td></td>
</tr>
<tr class="even">
<td>110-111</td>
<td>2</td>
<td></td>
<td>20;17 396</td>
<td>17 NUMBER OF MYOCARDIAL INFARCTION</td>
<td></td>
</tr>
<tr class="odd">
<td>112-113</td>
<td>2</td>
<td></td>
<td>20;18 397</td>
<td>18 NUMBER OF ILEUS/BOWEL OBSTRUCTION</td>
<td></td>
</tr>
<tr class="even">
<td>114-115</td>
<td>2</td>
<td></td>
<td>20;19 398</td>
<td>19 NUMBER OF GRAFT/PROSTHESIS/FLAP FAILURE</td>
<td></td>
</tr>
<tr class="odd">
<td>116-117</td>
<td>2</td>
<td></td>
<td>20;20 399</td>
<td>20 NUMBER OF DVT/THROMBOPHLEBITIS</td>
<td></td>
</tr>
<tr class="even">
<td>118-119</td>
<td>2</td>
<td></td>
<td>20;21 400</td>
<td>21 NUMBER OF OTHER OCCURRENCE</td>
<td></td>
</tr>
<tr class="odd">
<td>120-121</td>
<td>2</td>
<td></td>
<td>20;22 401</td>
<td>22 NUMBER OF WOUND DISRUPTION</td>
<td></td>
</tr>
<tr class="even">
<td>122-123</td>
<td>2</td>
<td></td>
<td>20;23 402</td>
<td>23 NUMBER OF ENDOCARDITIS</td>
<td></td>
</tr>
<tr class="odd">
<td>124-125</td>
<td>2</td>
<td></td>
<td>20;24 403</td>
<td>24 NUMBER OF LOW CARDIAC OUTPUT &gt; 6 HOURS</td>
<td></td>
</tr>
<tr class="even">
<td>126-127</td>
<td>2</td>
<td></td>
<td>20;25 404</td>
<td>25 NUMBER OF MEDIASTINITIS</td>
<td></td>
</tr>
<tr class="odd">
<td>128-129</td>
<td>2</td>
<td></td>
<td>20;26 405</td>
<td>26 NUMBER OF REOPERATION FOR BLEEDING</td>
<td></td>
</tr>
<tr class="even">
<td>130-131</td>
<td>2</td>
<td></td>
<td>20;27 406</td>
<td>27 NUMBER OF REPEAT CARDIO-PULMONARY BYPASS</td>
<td></td>
</tr>
<tr class="odd">
<td>132-133</td>
<td>2</td>
<td></td>
<td>20;28 407</td>
<td>28 NUMBER OF STROKE <em>(Obsolete)</em></td>
<td></td>
</tr>
<tr class="even">
<td>134-135</td>
<td>2</td>
<td></td>
<td>20;29 408</td>
<td>29 NUMBER OF OTHER RESPIRATORY OCCURRENCE</td>
<td></td>
</tr>
<tr class="odd">
<td>136-137</td>
<td>2</td>
<td></td>
<td>20;30 409</td>
<td>30 NUMBER OF OTHER CNS OCCURRENCE</td>
<td></td>
</tr>
<tr class="even">
<td>138-139</td>
<td>2</td>
<td></td>
<td>20;31 410</td>
<td>31 NUMBER OF OTHER URINARY TRACT OCCURRENCE</td>
<td></td>
</tr>
<tr class="odd">
<td>140-141</td>
<td>2</td>
<td></td>
<td>20;32 411</td>
<td>32 NUMBER OF OTHER CARDIAC OCCURRENCE</td>
<td></td>
</tr>
<tr class="even">
<td>142-146</td>
<td>5</td>
<td>3;1 136.03,.01</td>
<td>11;2 139.017,1</td>
<td>OTHER PROCEDURE CPT CODE #1</td>
<td></td>
</tr>
<tr class="odd">
<td>147-151</td>
<td>5</td>
<td>3;1 136.03,.01</td>
<td>11;2 139.017,1</td>
<td>OTHER PROCEDURE CPT CODE #2</td>
<td></td>
</tr>
<tr class="even">
<td>152-156</td>
<td>5</td>
<td>3;1 136.03,.01</td>
<td>11;2 139.017,1</td>
<td>OTHER PROCEDURE CPT CODE #3</td>
<td></td>
</tr>
<tr class="odd">
<td>157-161</td>
<td>5</td>
<td>3;1 136.03,.01</td>
<td>11;2 139.017,1</td>
<td>OTHER PROCEDURE CPT CODE #4</td>
<td></td>
</tr>
<tr class="even">
<td>162-166</td>
<td>5</td>
<td>3;1 136.03,.01</td>
<td>11;2 139.017,1</td>
<td>OTHER PROCEDURE CPT CODE #5</td>
<td></td>
</tr>
<tr class="odd">
<td>167-171</td>
<td>5</td>
<td>3;1 136.03,.01</td>
<td>11;2 139.017,1</td>
<td>OTHER PROCEDURE CPT CODE #6</td>
<td></td>
</tr>
<tr class="even">
<td>172-176</td>
<td>5</td>
<td>3;1 136.03,.01</td>
<td>11;2 139.017,1</td>
<td>OTHER PROCEDURE CPT CODE #7</td>
<td></td>
</tr>
<tr class="odd">
<td>177-181</td>
<td>5</td>
<td>3;1 136.03,.01</td>
<td>11;2 139.017,1</td>
<td>OTHER PROCEDURE CPT CODE #8</td>
<td></td>
</tr>
<tr class="even">
<td>182-186</td>
<td>5</td>
<td>3;1 136.03,.01</td>
<td>11;2 139.017,1</td>
<td>OTHER PROCEDURE CPT CODE #9</td>
<td></td>
</tr>
<tr class="odd">
<td>187-191</td>
<td>5</td>
<td>3;1 136.03,.01</td>
<td>11;2 139.017,1</td>
<td>OTHER PROCEDURE CPT CODE #10</td>
<td></td>
</tr>
<tr class="even">
<td>192-193</td>
<td>2</td>
<td>1.0;8 1.09</td>
<td>0;16 78</td>
<td>WOUND CLASSIFICATION</td>
<td><p>C CLEAN</p>
<p>CC CLEAN/ CONTAMINATED</p>
<p>D CONTAMINATED</p>
<p>I INFECTED</p></td>
</tr>
<tr class="odd">
<td>194</td>
<td>1</td>
<td></td>
<td>20;33 412</td>
<td>OCCURRENCE TYPES</td>
<td><p>I INTRAOP</p>
<p>P POSTOP</p>
<p>B BOTH</p></td>
</tr>
<tr class="even">
<td>195-196</td>
<td>2</td>
<td></td>
<td>S;12 127</td>
<td>RETRANSMISSION NUMBER</td>
<td></td>
</tr>
<tr class="odd">
<td>197</td>
<td>1</td>
<td></td>
<td></td>
<td></td>
<td>“*” REDOWNLOAD INDICATORE</td>
</tr>
<tr class="even">
<td>198-204</td>
<td>7</td>
<td></td>
<td>S;4 115</td>
<td>TRANSMISSION DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>205-214</td>
<td>10</td>
<td>CON;1 35</td>
<td>CON;5 15</td>
<td>CONCURRENT CASE</td>
<td></td>
</tr>
<tr class="even">
<td>215-226</td>
<td>12</td>
<td>VADM(6)</td>
<td>0;17 219</td>
<td>DATE/TIME OF DEATH</td>
<td></td>
</tr>
<tr class="odd">
<td>227-238</td>
<td>12</td>
<td>208;15 419</td>
<td>32;6 325</td>
<td>HOSPITAL DISCHARGE DATE</td>
<td></td>
</tr>
<tr class="even">
<td>239</td>
<td>1</td>
<td>30;6 18.5</td>
<td>184;1 89</td>
<td>CASE ABORTED</td>
<td><p>1 NO</p>
<p>2 YES-PRE ANESTHESIA</p>
<p>3 YES-POST ANESTHESIA</p></td>
</tr>
<tr class="odd">
<td>240</td>
<td>1</td>
<td>.1;21 661</td>
<td>184;2 90</td>
<td>PALLIATION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>241</td>
<td>1</td>
<td>0;26 .013</td>
<td>184;3 91</td>
<td>PLANNED ADMISSION STATUS</td>
<td><p>1 SAME DAY</p>
<p>2 ADMITTED</p>
<p>3 HOSPITALIZED</p></td>
</tr>
<tr class="odd">
<td>242-243</td>
<td>2</td>
<td>OP;3 2006</td>
<td>OP;4 2006</td>
<td>ROBOTIC ASSISTANCE (Y/N)</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
</tbody>
</table>

Line B of the 1-Liner Transmission Layout

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 18%" />
<col style="width: 17%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line B</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-26</td>
<td>12</td>
<td>.2;1 .21</td>
<td>32;11 335</td>
<td>ANESTHESIA CARE START TIME</td>
<td></td>
</tr>
<tr class="even">
<td>27-38</td>
<td>12</td>
<td>.2;4 .24</td>
<td>32;16 335.5</td>
<td>ANESTHESIA CARE END TIME</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>1;1 136.01,.01</td>
<td>OP;3 8.1</td>
<td>PRIN. PROCEDURE CPT MODIFIERS</td>
<td></td>
</tr>
<tr class="even">
<td>39-40</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="odd">
<td>41-42</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="even">
<td>43-44</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="odd">
<td>45-46</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="even">
<td>47-48</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>3,1;1 136.31,.01</td>
<td>11;3 139.017,2</td>
<td><p>OTHER PROCEDURE CPT MODIFIERS</p>
<p>For OTHER</p>
<p>PROCEDURE CPT</p>
<p>#1</p></td>
<td></td>
</tr>
<tr class="even">
<td>49-50</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="odd">
<td>51-52</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="even">
<td>53-54</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="odd">
<td>55-56</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="even">
<td>57-58</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>3,1;1 136.31,.01</td>
<td>11;3 139.017,2</td>
<td><p>OTHER PROCEDURE CPT MODIFIERS</p>
<p>For OTHER</p>
<p>PROCEDURE CPT</p>
<p>#2</p></td>
<td></td>
</tr>
<tr class="even">
<td>59-60</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="odd">
<td>61-62</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="even">
<td>63-64</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="odd">
<td>65-66</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="even">
<td>67-68</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>3,1;1 136.31,.01</td>
<td>11;3 139.017,2</td>
<td><p>OTHER PROCEDURE CPT MODIFIERS</p>
<p>For OTHER PROCEDURE CPT #3</p></td>
<td></td>
</tr>
<tr class="even">
<td>69-70</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="odd">
<td>71-72</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="even">
<td>73-74</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="odd">
<td>75-76</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="even">
<td>77-78</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>3,1;1 136.31,.01</td>
<td>11;3 139.017,2</td>
<td><p>OTHER PROCEDURE CPT MODIFIERS</p>
<p>For OTHER PROCEDURE CPT #4</p></td>
<td></td>
</tr>
<tr class="even">
<td>79-80</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="odd">
<td>81-82</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="even">
<td>83-84</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="odd">
<td>85-86</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="even">
<td>87-88</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>3,1;1 136.31,.01</td>
<td>11;3 139.017,2</td>
<td><p>OTHER PROCEDURE CPT MODIFIERS</p>
<p>For OTHER PROCEDURE CPT #5</p></td>
<td></td>
</tr>
<tr class="even">
<td>89-90</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="odd">
<td>91-92</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="even">
<td>93-94</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="odd">
<td>95-96</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="even">
<td>97-98</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>3,1;1 136.31,.01</td>
<td>11;3 139.017,2</td>
<td><p>OTHER PROCEDURE CPT MODIFIERS</p>
<p>For OTHER PROCEDURE CPT #6</p></td>
<td></td>
</tr>
<tr class="even">
<td>99-100</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="odd">
<td>101-102</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="even">
<td>103-104</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="odd">
<td>105-106</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="even">
<td>107-108</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>3,1;1 136.31,.01</td>
<td>11;3 139.017,2</td>
<td><p>OTHER PROCEDURE CPT MODIFIERS</p>
<p>For OTHER PROCEDURE CPT #7</p></td>
<td></td>
</tr>
<tr class="even">
<td>109-110</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="odd">
<td>111-112</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="even">
<td>113-114</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="odd">
<td>115-116</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="even">
<td>117-118</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>3,1;1 136.31,.01</td>
<td>11;3 139.017,2</td>
<td><p>OTHER PROCEDURE CPT MODIFIERS</p>
<p>For OTHER PROCEDURE CPT #8</p></td>
<td></td>
</tr>
<tr class="even">
<td>119-120</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="odd">
<td>121-122</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="even">
<td>123-124</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="odd">
<td>125-126</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="even">
<td>127-128</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>3,1;1 136.31,.01</td>
<td>11;3 139.017,2</td>
<td><p>OTHER PROCEDURE CPT MODIFIERS</p>
<p>For OTHER PROCEDURE CPT #9</p></td>
<td></td>
</tr>
<tr class="even">
<td>129-130</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="odd">
<td>131-132</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="even">
<td>133-134</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="odd">
<td>135-136</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="even">
<td>137-138</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>3,1;1 136.31,.01</td>
<td>11;3 139.017,2</td>
<td><p>OTHER PROCEDURE CPT MODIFIERS</p>
<p>For OTHER PROCEDURE CPT #10</p></td>
<td></td>
</tr>
<tr class="even">
<td>139-140</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #1</td>
<td></td>
</tr>
<tr class="odd">
<td>141-142</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #2</td>
<td></td>
</tr>
<tr class="even">
<td>143-144</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #3</td>
<td></td>
</tr>
<tr class="odd">
<td>145-146</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #4</td>
<td></td>
</tr>
<tr class="even">
<td>147-148</td>
<td>2</td>
<td></td>
<td></td>
<td>MODIFIER #5</td>
<td></td>
</tr>
<tr class="odd">
<td>149</td>
<td>1</td>
<td>6;8;2 130.06,42</td>
<td>2;7 193</td>
<td>INTUBATED? (Y/N)</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>150-151</td>
<td>2</td>
<td></td>
<td>20;34 418</td>
<td>NUMBER OF TRACHEOSTOMY</td>
<td></td>
</tr>
<tr class="odd">
<td>152-153</td>
<td>2</td>
<td></td>
<td>20;35 419</td>
<td>NUMBER OF NEW MECH. CIRCULATORY SUP.</td>
<td></td>
</tr>
<tr class="even">
<td>154-155</td>
<td>2</td>
<td></td>
<td>20;37 423</td>
<td>NUMBER OF ORGAN/SPACE SSI</td>
<td></td>
</tr>
<tr class="odd">
<td>156-157</td>
<td>2</td>
<td></td>
<td>20;38 424</td>
<td>NUMBER OF OTHER WOUND OCCURRENCES</td>
<td></td>
</tr>
<tr class="even">
<td>158-159</td>
<td>2</td>
<td>.1;10 .166</td>
<td>1;16 13.1</td>
<td>ATTENDING CODE</td>
<td><p>1 OLD0 - 0. STAFF ALONE</p>
<p>2 OLD1 - 1. ATTENDING IN O.R.</p>
<p>3 OLD2 - 2. ATTENDING IN O.R.</p>
<p>SUITE</p>
<p>4 OLD3 - 3. ATTENDING NOT PRESENT,</p>
<p>BUT AVAILABLE</p>
<p>5 LEVEL 0. ATTENDING DOING THE OPERATION</p>
<p>6 LEVEL 1. ATTENDING IN O.R.</p>
<p>ASSISTING THE RESIDENT</p>
<p>7 LEVEL 2. ATTENDING IN O.R., NOT</p>
<p>SCRUBBED</p>
<p>8 LEVEL 3. ATTENDING NOT PRESENT IN</p>
<p>O.R. SUITE, IMMEDIATELY AVAILABLE</p>
<p>9 LEVEL A: ATTENDING DOING THE OPERATION</p>
<p>10 LEVEL B: ATTENDING IN O.R., SCRUBBED</p>
<p>11 LEVEL C: ATTENDING IN O.R., NOT</p>
<p>SCRUBBED</p>
<p>12 LEVEL D: ATTENDING IN O.R. SUITE,</p>
<p>IMMEDIATELY AVAILABLE</p>
<p>13 LEVEL E: EMERGENCY CARE, ATTENDING</p>
<p>CONTACTED ASAP</p>
<p>14 LEVEL F: NON-OR PROCEDURE DONE IN</p>
<p>OR, ATTENDING IDENTIFIED</p>
<p>99 NOT ENTERED</p></td>
</tr>
<tr class="odd">
<td>160-166</td>
<td>7</td>
<td></td>
<td>0;26 436</td>
<td>DATE OF BIRTH</td>
<td></td>
</tr>
<tr class="even">
<td>167-174</td>
<td>8</td>
<td>0;3(136) .03(136)</td>
<td>0;20 99</td>
<td>POSTOP DIAGNOSIS ICD CODE</td>
<td></td>
</tr>
<tr class="odd">
<td>175-176</td>
<td>2</td>
<td></td>
<td>20;42 442</td>
<td>NUMBER OF C. DIFFICILE COLITIS</td>
<td></td>
</tr>
<tr class="even">
<td>177-178</td>
<td>2</td>
<td></td>
<td>20;43 447</td>
<td>NUMBER OF POSTOP ATRIAL FIBRILLATION</td>
<td></td>
</tr>
<tr class="odd">
<td>179-190</td>
<td>12</td>
<td>.2;10 .205</td>
<td>32;18 334.5</td>
<td>TIME PAT IN OR</td>
<td></td>
</tr>
<tr class="even">
<td>191-202</td>
<td>12</td>
<td>.2;12 .232</td>
<td>32;10 334</td>
<td>TIME PAT OUT OR</td>
<td></td>
</tr>
<tr class="odd">
<td>203-214</td>
<td>12</td>
<td>.2;2 .22</td>
<td>0;13 75</td>
<td>DATE/TIME OPERATION BEGAN</td>
<td></td>
</tr>
<tr class="even">
<td>215-226</td>
<td>12</td>
<td>.2;3 .23</td>
<td>0;21 182</td>
<td>DATE/TIME OPERATION ENDED</td>
<td></td>
</tr>
<tr class="odd">
<td>227</td>
<td>1</td>
<td>16;8 130.22,9</td>
<td>7;9 111</td>
<td>STROKE/CVA</td>
<td><p>1 NO SYMPTOMS</p>
<p>2 &lt;24 HOURS</p>
<p>3 24-72 HOURS</p>
<p>4 &gt;72 HOURS</p></td>
</tr>
</tbody>
</table>

Line D of the 1-Liner Transmission Layout

<table style="width:100%;">
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line D</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-26</td>
<td>12</td>
<td>.9;1 612</td>
<td>.9;1 612</td>
<td>ORIGINAL DESIRED PROCEDURE DATE</td>
<td></td>
</tr>
<tr class="even">
<td>27-38</td>
<td>12</td>
<td>.9;2 613</td>
<td>.9;2 613</td>
<td>D/T OF DESIRED PROCEDURE DATE ENTRY</td>
<td></td>
</tr>
<tr class="odd">
<td>39-50</td>
<td>12</td>
<td>.9;3 614</td>
<td>.9;3 614</td>
<td>ORIGINAL SCHEDULED DATE</td>
<td></td>
</tr>
<tr class="even">
<td>51-62</td>
<td>12</td>
<td>.9;4 615</td>
<td>.9;4 615</td>
<td>D/T OF SCHEDULED DATE ENTRY</td>
<td></td>
</tr>
<tr class="odd">
<td>63-74</td>
<td>12</td>
<td>.9;5 616</td>
<td>.9;5 616</td>
<td>DESIRED PROCEDURE DATE</td>
<td></td>
</tr>
<tr class="even">
<td>75-86</td>
<td>12</td>
<td>.9;6 617</td>
<td>.9;6 617</td>
<td>SCHEDULED DATE</td>
<td></td>
</tr>
<tr class="odd">
<td>87-98</td>
<td>12</td>
<td>30;1 17</td>
<td>22;3 619</td>
<td>CANCEL DATE</td>
<td></td>
</tr>
<tr class="even">
<td>99-102</td>
<td>4</td>
<td>31;8 18</td>
<td>22;4 620</td>
<td>CANCEL REASON</td>
<td><p>1010 PATIENT RELATED ISSUE</p>
<p>1011 ENVIRONMENTAL ISSUE</p>
<p>1012 STAFF ISSUE</p>
<p>1013 PATIENT HEALTH STATUS</p>
<p>1014 CLIN URGENT/EMERGENT CASE</p>
<p>1015 SCHED ISSUES NON EMERGENT CASE</p>
<p>1016 UNAVAILABLE BED</p>
<p>1017 UNAVAILABLE EQUIP EXCLUDE RME</p>
<p>1018 UNAVAILABLE REUSABLE EQUP-RME</p>
<p>1019 CASE MOVED TO EARLIER DATE</p></td>
</tr>
<tr class="odd">
<td>103-152</td>
<td>50</td>
<td>30;4 19</td>
<td>22;5 621</td>
<td>CANCELLATION COMMENTS</td>
<td></td>
</tr>
<tr class="even">
<td>153-154</td>
<td>2</td>
<td>VER;7 600</td>
<td>VER;7 600</td>
<td>CONFIRM PATIENT IDENTITY</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>155-156</td>
<td>2</td>
<td>VER;8 601</td>
<td>VER;8 601</td>
<td>PROCEDURE TO BE PERFORMED</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>157-158</td>
<td>2</td>
<td>VER;9 602</td>
<td>VER;9 602</td>
<td>SITE OF PROCEDURE</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>159-160</td>
<td>2</td>
<td>VER;10 603</td>
<td>VER;10 603</td>
<td>CONFIRM VALID CONSENT</td>
<td><p>1 YES, i-MED</p>
<p>2 YES, PAPER</p>
<p>3 YES, TELEPHONE</p>
<p>4 NO, EMERGENCY</p>
<p>5 NO, NOT EMERGENCY</p></td>
</tr>
<tr class="even">
<td>161-162</td>
<td>2</td>
<td>VER;11 604</td>
<td>VER;11 604</td>
<td>CONFIRM PATIENT POSITION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>163-164</td>
<td>2</td>
<td>VER;12 605</td>
<td>VER;12 605</td>
<td>MARKED SITE CONFIRMED</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>165-166</td>
<td>2</td>
<td>VER;13 606</td>
<td>VER;13 606</td>
<td>PREOPERATIVE IMAGES CONFIRMED</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="odd">
<td>167-168</td>
<td>2</td>
<td>VER;14 607</td>
<td>VER;14 607</td>
<td>CORRECT MEDICAL IMPLANTS</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="even">
<td>169-170</td>
<td>2</td>
<td>VER;15 608</td>
<td>VER;15 608</td>
<td>ANTIBIOTIC PROPHYLAXIS</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="odd">
<td>171-172</td>
<td>2</td>
<td>VER;16 609</td>
<td>VER;16 609</td>
<td>APPROPRIATE DVT PROPHYLAXIS</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT APPLICABLE</p>
<p>NI NOT INDICATED</p></td>
</tr>
<tr class="even">
<td>173-174</td>
<td>2</td>
<td>VER;17 610</td>
<td>VER;17 610</td>
<td>BLOOD AVAILABILITY</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NI NOT INDICATED</p></td>
</tr>
<tr class="odd">
<td>175-176</td>
<td>2</td>
<td>VER;18 611</td>
<td>VER;18 611</td>
<td>AVAILABILITY OF SPECIAL EQUIP</td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="even">
<td>177-206</td>
<td>30</td>
<td>0;2 .02</td>
<td>6;1 .02</td>
<td>OP ROOM PROCEDURE PERFORMED</td>
<td>(Name of OR)</td>
</tr>
<tr class="odd">
<td>207-208</td>
<td>2</td>
<td>52;1 619</td>
<td>6;5 449</td>
<td>IMMED USE -CONTAMINATION</td>
<td>(0 to 99)</td>
</tr>
<tr class="even">
<td>209-210</td>
<td>2</td>
<td>52;2 620</td>
<td>6;6 450</td>
<td>IMMED USE -SPS/OR MGT ISSUE</td>
<td>(0 to 99)</td>
</tr>
<tr class="odd">
<td>211-212</td>
<td>2</td>
<td>52;3 621</td>
<td>6;7 451</td>
<td>IMMED USE -EMERGENCY</td>
<td>(0 to 99)</td>
</tr>
<tr class="even">
<td>213-214</td>
<td>2</td>
<td>52;4 622</td>
<td>6;8 452</td>
<td>IMMED USE -NO BETTER OPTION</td>
<td>(0 to 99)</td>
</tr>
<tr class="odd">
<td>215-216</td>
<td>2</td>
<td>52;5 623</td>
<td>6;9 453</td>
<td>IMMED USE -LOANER</td>
<td>(0 to 99)</td>
</tr>
<tr class="even">
<td>217-218</td>
<td>2</td>
<td>52;6 624</td>
<td>6;10 454</td>
<td>IMMED USE -DECONTAMINATION</td>
<td>(0 to 99)</td>
</tr>
<tr class="odd">
<td>219-221</td>
<td>3</td>
<td>25;1 44</td>
<td>182;4 375</td>
<td>SPONGE FINAL COUNT CORRECT</td>
<td><p>Y YES</p>
<p>N NO, SEE NURSING CARE COMMENTS</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="even">
<td>222-224</td>
<td>3</td>
<td>25;2 45</td>
<td>182;5 376</td>
<td>SHARPS FINAL COUNT CORRECT</td>
<td><p>Y YES</p>
<p>N NO, SEE NURSING CARE COMMENTS</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="odd">
<td>225-227</td>
<td>3</td>
<td>25;3 46</td>
<td>182;6 377</td>
<td>INSTRUMENT FINAL COUNT CORRECT</td>
<td><p>Y YES</p>
<p>N NO, SEE NURSING CARE COMMENTS</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="even">
<td>228</td>
<td>1</td>
<td>25;6 630</td>
<td>182;7 378</td>
<td>POSSIBLE ITEM RETENTION</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>229</td>
<td>1</td>
<td>25;7 633</td>
<td>182;8 379</td>
<td>WOUND SWEEP</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>230</td>
<td>1</td>
<td>25;8 636</td>
<td>182;9 463</td>
<td>INTRA-OPERATIVE X-RAY</td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>231-233</td>
<td>3</td>
<td></td>
<td>182;10 464</td>
<td>NUM of PROSTHESIS INSTALLED entries</td>
<td>(0 to 999)</td>
</tr>
<tr class="even">
<td>234-236</td>
<td>3</td>
<td></td>
<td>182;11 465</td>
<td># of “Yes” answers to the PROVIDER READ BACK PERFORMED field</td>
<td>(0 to 999)</td>
</tr>
<tr class="odd">
<td>237</td>
<td>1</td>
<td>30;5 17.5</td>
<td>182;12 466</td>
<td>CANCELLATION TIMEFRAME</td>
<td><p>1 SURGERY CANCELLED &lt;48 HRS BEFORE SCHEDULED SURGERY</p>
<p>2 SURGERY CANCELLED &gt;48 HRS BEFORE SCHEDULED SURGERY</p></td>
</tr>
<tr class="even">
<td>238-240</td>
<td>3</td>
<td>.4;6 .46</td>
<td>182;19 478</td>
<td>OP DISPOSITION</td>
<td><p>O OUTPATIENT/DISCHARGE</p>
<p>I ICU</p>
<p>S STEPDOWN</p>
<p>W WARD</p>
<p>OBS OBSERVATION UNIT</p>
<p>M MORGUE</p></td>
</tr>
<tr class="odd">
<td>241-242</td>
<td>2</td>
<td></td>
<td>182;13 467</td>
<td>NUMBER OF SYMPTOMATIC UTI OCCURRENCES</td>
<td>(0 to 99)</td>
</tr>
<tr class="even">
<td>243-244</td>
<td>2</td>
<td></td>
<td>182;14 468</td>
<td><p>NUMBER OF MECHANICAL VENT W/N 30 DAYS OCCURRENCES</p>
<p>will not be used after SR*3*184</p></td>
<td>(0 to 99)</td>
</tr>
</tbody>
</table>

Line E of the 1-Liner Transmission Layout – no longer used after SR\*3.0\*184

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Line E</p>
<p>Position</p></th>
<th>Length</th>
<th><p>File 130</p>
<p>Global Field</p></th>
<th><p>File 139</p>
<p>Global Field</p></th>
<th>Field Name</th>
<th><p>Set of Codes or Other Notes</p>
<p>Code Stands for</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15-26</td>
<td>12</td>
<td>211;54 742</td>
<td>184;13 130</td>
<td><p>D/T PAT ARRIVES HOSP DAY SURG</p>
<p>Will not be used after SR*3*184</p></td>
<td></td>
</tr>
<tr class="even">
<td>27-38</td>
<td>12</td>
<td>211;55 743</td>
<td>184;14 132</td>
<td><p>D/T PAT LEAVES HOSP DAY SURG</p>
<p>Will not be used after SR*3*184</p></td>
<td></td>
</tr>
<tr class="odd">
<td>39-45</td>
<td>7</td>
<td>130.0647,.01</td>
<td>184;15 134</td>
<td><p>ORGAN TO BE TRANSPLANTED</p>
<p>Will not be used after SR*3*184</p></td>
<td><p>1 HEART, 2 LUNG, 3 KIDNEY</p>
<p>4 LIVER, 5 PANCREAS</p>
<p>6 INTESTINE, 7 OTHER</p></td>
</tr>
<tr class="even">
<td>46-55</td>
<td>10</td>
<td>VER1;2 648</td>
<td>184;16 137</td>
<td><p>UNOS NUMBER</p>
<p>Will not be used after SR*3*184</p></td>
<td>1-10 chars</td>
</tr>
<tr class="odd">
<td>56-57</td>
<td>2</td>
<td>VER1;3 649</td>
<td>184;17 154</td>
<td><p>DONOR SEROLOGY HCV</p>
<p>Will not be used after SR*3*184</p></td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="even">
<td>58-59</td>
<td>2</td>
<td>VER1;4 650</td>
<td>184;18 186</td>
<td><p>DONOR SEROLOGY HBV</p>
<p>Will not be used after SR*3*184</p></td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="odd">
<td>60-61</td>
<td>2</td>
<td>VER1;5 651</td>
<td>184;19 199</td>
<td><p>DONOR SEROLOGY CMV</p>
<p>Will not be used after SR*3*184</p></td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="even">
<td>62-63</td>
<td>2</td>
<td>VER1;6 652</td>
<td>184;20 205</td>
<td><p>DONOR SEROLOGY HIV</p>
<p>Will not be used after SR*3*184</p></td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="odd">
<td>64</td>
<td>1</td>
<td>VER1;7 653</td>
<td>184;21 214</td>
<td><p>DONOR ABO TYPE</p>
<p>Will not be used after SR*3*184</p></td>
<td><p>1 A RH(+)</p>
<p>2 A RH(-)</p>
<p>3 B RH(+)</p>
<p>4 B RH(-)</p>
<p>5 AB RH(+)</p>
<p>6 AB RH(-)</p>
<p>7 O RH(+)</p>
<p>8 O RH(-)</p></td>
</tr>
<tr class="even">
<td>65</td>
<td>1</td>
<td>VER1;8 654</td>
<td>184;22 215</td>
<td><p>RECIPIENT ABO TYPE</p>
<p>Will not be used after SR*3*184</p></td>
<td><p>1 A RH(+)</p>
<p>2 A RH(-)</p>
<p>3 B RH(+)</p>
<p>4 B RH(-)</p>
<p>5 AB RH(+)</p>
<p>6 AB RH(-)</p>
<p>7 O RH(+)</p>
<p>8 O RH(-)</p></td>
</tr>
<tr class="odd">
<td>66</td>
<td>1</td>
<td>VER1;9 655</td>
<td>184;23 220</td>
<td><p>BLOOD BANK ABO VERIFICATION</p>
<p>Will not be used after SR*3*184</p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>67-78</td>
<td>12</td>
<td>VER1;19 747</td>
<td>182;31 640</td>
<td><p>D/T BLOOD BANK ABO VERIF</p>
<p>Will not be used after SR*3*184</p></td>
<td></td>
</tr>
<tr class="odd">
<td>79</td>
<td>1</td>
<td>VER1;10 656</td>
<td>184;24 222</td>
<td><p>OR ABO VERIFICATION</p>
<p>Will not be used after SR*3*184</p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>80-91</td>
<td>12</td>
<td>VER1;21 749</td>
<td>184;33 624</td>
<td><p>D/T OR ABO VERIF</p>
<p>Will not be used after SR*3*184</p></td>
<td></td>
</tr>
<tr class="odd">
<td>92-121</td>
<td>30</td>
<td>VER1;11 657</td>
<td>184;34 625</td>
<td><p>SURGEON VERIFYING UNET</p>
<p>Will not be used after SR*3*184</p></td>
<td>Name field</td>
</tr>
<tr class="even">
<td>122</td>
<td>1</td>
<td>VER1;22 750</td>
<td>184;35 626</td>
<td><p>UNET VERIF BY SURGEON</p>
<p>Will not be used after SR*3*184</p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="odd">
<td>123</td>
<td>1</td>
<td>VER1;12 658</td>
<td>184;36 627</td>
<td><p>ORGAN VER PRE-ANESTHESIA</p>
<p>Will not be used after SR*3*184</p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>124-153</td>
<td>30</td>
<td>VER1;23 751</td>
<td>184;37 628</td>
<td><p>SURGEON VER ORGAN PRE-ANES</p>
<p>Will not be used after SR*3*184</p></td>
<td>Name field</td>
</tr>
<tr class="odd">
<td>154-183</td>
<td>30</td>
<td>VER1;13 659</td>
<td>182;20 629</td>
<td><p>SURGEON VER DONOR ORG PRE-ANES</p>
<p>Will not be used after SR*3*184</p></td>
<td>Name field</td>
</tr>
<tr class="even">
<td>184-185</td>
<td>2</td>
<td>VER1;24 752</td>
<td>182;21 630</td>
<td><p>DONOR ORG VER PRE-ANES</p>
<p>Will not be used after SR*3*184</p></td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="odd">
<td>186-187</td>
<td>2</td>
<td>VER1;14 660</td>
<td>182;22 631</td>
<td><p>ORGAN VER PRE-TRANSPLANT</p>
<p>Will not be used after SR*3*184</p></td>
<td><p>Y YES</p>
<p>N NO</p>
<p>NA NOT APPLICABLE</p></td>
</tr>
<tr class="even">
<td>188-217</td>
<td>30</td>
<td>VER1;25 753</td>
<td>182;23 632</td>
<td><p>SURGEON VER ORG PRE-TRANSPLANT</p>
<p>Will not be used after SR*3*184</p></td>
<td>Name field</td>
</tr>
<tr class="odd">
<td>218</td>
<td>1</td>
<td>VER1;15 663</td>
<td>184;29 233</td>
<td><p>DONOR VESSEL USAGE</p>
<p>Will not be used after SR*3*184</p></td>
<td><p>Y YES</p>
<p>N NO</p></td>
</tr>
<tr class="even">
<td>219</td>
<td>1</td>
<td>VER1;16 665</td>
<td>184;30 234</td>
<td><p>DONOR VESSEL DISPOSITION</p>
<p>Will not be used after SR*3*184</p></td>
<td><p>N NO DONOR VESSELS RECEIVED</p>
<p>D DISCARDED</p>
<p>R RETURNED TO OPO</p>
<p>S STORED</p></td>
</tr>
</tbody>
</table>

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table provides definitions for common terms used in this manual.
| Term        | Definition                                                                                                                                                                                                                                                |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Risk Assessment | A module of the Surgery software that provides medical centers a mechanism to track information related to surgical risk and operative mortality. Completed assessments are transmitted to the NSQIP or the CICSP national database for statistical analysis. |
| 1-Liner         | This term is also known as abbreviated case record.                                                                                                                                                                                                           |
| VASQIP          | VA Surgical Quality Improvement Program.                                                                                                                                                                                                                      |

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Archiving, 22
B
Background tasks, 15, 16, 17, 18, 19
C
Callable entry points, 23
Calls, 24
Configurable files, 17
Contingency plan, 29
D
Database Integration Agreements, 26
E
Exported files, 10
Exported options, 14
External packages, 24
F
File descriptions, 11
Files, 10
G
Globals, 21
I
Initialization routines, 13
Input Templates, 20
Installation, 7, 32
J
Journaling, 21
M
Mail groups, 8, 17
N
Namespaced, 28
NEW PERSON file, 7, 17, 18
O
Option Descriptions, 15
P
Package-wide variables, 28
Print Template, 20
Purging, 22
R
Routines, 13, 23
S
Security Keys, 7, 31
Site Specific Parameters, 7
Sort Template, 20
T
Templates, 20
X
XU FIRST LINE PRINT, 13
