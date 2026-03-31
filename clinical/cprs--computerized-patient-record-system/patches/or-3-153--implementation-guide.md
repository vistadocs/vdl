---
title: OR*3*153 CPRS Query Hepatitis C Reports Installation/Implementation Guide
doc_type: IG-IMP
doc_label: Implementation Guide
doc_layer: patch
doc_subject: CPRS Query Hepatitis C Reports Installation/
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
description: > ![](or-3-153-cprs-query-hepatitis-c-reports-installation-implementation-guide/001.png)
audience: 
keywords: 
  - blockquote
  - strong
  - table
  - class
  - contents
  - style
  - width
  - colgroup
  - thead
  - tbody
page_count: 0
word_count: 2237
section_count: 15
table_count: 0
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: April 2003
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_30_153ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_30_153ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

> ![](or-3-153-cprs-query-hepatitis-c-reports-installation-implementation-guide/001.png)

> CPRS QUERY

> (HEPATITIS C REPORTS)

> INSTALLATION / IMPLEMENTATION GUIDE

> April 2003

> Department of Veterans Affairs VistA System Design & Development

> ii

> <u>Table of Contents</u>

# Preface 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
  - [Software and Manual Retrieval](#software-and-manual-retrieval)
- [Pre-Installation Information](#pre-installation-information)
  - [IRM Staff](#irm-staff)
  - [Hardware and Operating Systems Requirements](#hardware-and-operating-systems-requirements)
  - [Workstation Requirements](#workstation-requirements)
  - [System Performance Capacity](#system-performance-capacity)
  - [Software Installation Time](#software-installation-time)
  - [Users on the System](#users-on-the-system)
  - [Backup Routines](#backup-routines)
  - [Namespace](#namespace)
  - [Required Patches](#required-patches)
  - [File and Global Information](#file-and-global-information)
  - [Test Sites](#test-sites)
- [Installation Instructions](#installation-instructions)
- [Implementation](#implementation)
  - [Steps for setting up the CPRS QUERY GUI](#steps-for-setting-up-the-cprs-query-gui)
  - [Required Menus, Keys, and Parameters](#required-menus-keys-and-parameters)
- [Glossary](#glossary)
> Patch OR\*3\*153 implements the CPRS Query Tool (Hepatitis C Reports).
> The CPRS Query Tool provides users with the ability to build custom reports and view predefined reports containing clinical information for a select list of patients. This application is an enhancement to the Hepatitis C registry project. The CPRS Query Tool application will assist health care providers in following up on clinical interventions as well as providing an aggregate view of patient information to track health care outcomes.
> To use the CPRS Query Tool, a user can choose a predefined report (such as abnormal results) or create a custom query. A predefined report can be selected by clicking on the desired report. Once a report is selected, the user adds criteria to retrieve only the records for a specific group of patients for a selected time period. To create a custom query, the user selects the search items (such as orders/results), then selects the criteria. The query can be saved and reused.
> TIU\*1.0\*150, which was released April 8, 2003, provides a new API for patch OR\*3\*153. It introduces two new routines and should have no impact on other modules of either TIU or CPRS.
> The CPRS Query (Hepatitis C Reports) Installation Guide provides assistance for installing and implementing the CPRS Query/Hepatitis C Reports software.

## Software and Manual Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> OR\*3.0\*153 is distributed as a Packman message via Forum.

> A ZIP file that contains the GUI Executable and the documentation files is available on the following Office of Information Field Offices (OIFOs) ANONYMOUS SOFTWARE directories.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 38%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>OIFO</strong></th>
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
<td>Albany</td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td><blockquote>
<p>anonymous.software</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Hines</td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td><blockquote>
<p>anonymous.software</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Salt Lake City</td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td><blockquote>
<p>anonymous.software</p>
</blockquote></td>
</tr>
</tbody>
</table>

> OR_30_153.ZIP contains: CPRSQUERY.EXE

> OR_30_153IG.PDF Installation Guide OR_30_153UM.PDF User Manual

> <span id="VISTA_Intranet" class="anchor"></span>V*IST*A Intranet

> Documentation for this product is also available on the intranet at the following address: [<u>http://vista.med.va.gov/vdl/</u>](http://vista.med.va.gov/vdl/)

> This address takes you to the VistA Documentation Library (VDL), which has a listing of all the clinical software manuals. Click on the CPRS Query link and it will take you to the CPRS Query documentation.

> You can access the Hepatitis C Case Registry home page at the following address: <u>[http://vista.med.va.gov](http://vista.med.va.gov/)/ clinicalspecialties/.</u>

# Pre-Installation Information 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following information contains recommendations and requirements for the installation of the CPRS Query Tool.

## IRM Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Programmer access is required for installing CPRS Query Tool.

## Hardware and Operating Systems Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CPRS Query Tool software runs on the standard hardware platforms used by the Department of Veterans Affairs Healthcare facilities. These systems consist of Alpha Clusters running VMS (version 7.2-1 minimum) and DSM (version 7.2.1 VA1) or an Alpha 1000A running Windows NT (service pack 6) and Cache M operating system (version 3.2.31.1).

## Workstation Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Software Requirements*

- VistA’s Remote Procedure Call (RPC) Broker Version 1.1 or greater software must be properly installed and configured on the workstation.
- Microsoft Word (97 or higher)
- Microsoft Windows 98 SE (2<sup>nd</sup> edition, Windows 2000, or NT 4.0 (with service pack 6)

> *Workstation Hardware Requirements and Guidelines*

- Color VGA monitor (set at 24 bit)
- Video card and a software driver capable of a minimum 800x600 dpi and 16-bit color display must be installed and properly configured.
- Printer, mouse, and keyboard
- 166 mzh processor with at least, 64 mb RAM
- 10 mb free hard drive space

> For more detailed information about PC workstation and server requirements, see Appendix B of the CPRS Installation Guide (page 83): [<u>http://vista.med.va.gov/VistA_Lib/Clinical/Comp_Patient_Recrd_Sys\_(CPRS)/\_Toc4529</u>](http://vista.med.va.gov/VistA_Lib/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/_Toc452969918) [<u>69918</u>](http://vista.med.va.gov/VistA_Lib/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/_Toc452969918)

## System Performance Capacity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no significant changes in the performance capacity of the VistA operating system once the CPRS Query Tool software is installed. The software should not create any appreciable global growth or network transmission problems. There are no memory constraints.

## Software Installation Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The estimated installation time is less than 3 minutes during off peak hours.

## Users on the System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Users may remain on the system and no options need to be placed out of service.

## Backup Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A backup of the transport global before installing the software is recommended.

## Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CPRS Query Tool software namespace: OR.

## Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before the installation of Hepatitis C Reports, the following patches must be installed.

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Application Name</strong></p>
</blockquote></th>
<th><strong>Patches</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>OERR</p>
</blockquote></td>
<td><blockquote>
<p>OR*3*136</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TIU</p>
</blockquote></td>
<td>TIU*1.0*150</td>
</tr>
<tr class="odd">
<td>Hepatitis C Registry ROR</td>
<td>ROR*1.0*3.0</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 22%" />
<col style="width: 25%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Routine List</strong></p>
</blockquote></th>
<th colspan="3"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ORMGMRC</p>
</blockquote></td>
<td><blockquote>
<p>ORMLR</p>
</blockquote></td>
<td><blockquote>
<p>ORMRA</p>
</blockquote></td>
<td><blockquote>
<p>ORQRY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ORQRY01</p>
<p>ORRHCT</p>
</blockquote></td>
<td><blockquote>
<p>ORRHCO</p>
<p>ORRHCU</p>
</blockquote></td>
<td><blockquote>
<p>ORRHCQ</p>
<p>ORY153</p>
</blockquote></td>
<td><blockquote>
<p>ORRHCR</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Post-Install Routine

> POST^ORY153 does the following:

1.  Exports parameter "ORHEPC ABNORMAL START" at the Package level.
2.  Updates Abnormal Report default start date to the value of "ORHEPC ABNORMAL START."
3.  Sets Consult display group for the "Consult Status Report."
4.  Sets Imaging display group for the "Scheduled/Due Activity Report."
5.  For test sites, adds new patient IFN subscript to "ARS" xref in file \#100.

## File and Global Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> New files this patch installs:

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File #</strong></th>
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Root Global</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Global Protection</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Journaling</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Global Growth</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>102.21</td>
<td><p>CPRS Query</p>
<blockquote>
<p>Definition</p>
</blockquote></td>
<td><blockquote>
<p>^ORD(102.21,</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
</tr>
<tr class="even">
<td>102.22</td>
<td>CPRS Query Constraint</td>
<td><blockquote>
<p>^ORD(102.22,</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>102.23</td>
<td>CPRS Query Edit Control</td>
<td><blockquote>
<p>^ORD(102.23,</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
</tr>
<tr class="even">
<td>102.24</td>
<td><p>CPRS query</p>
<blockquote>
<p>display fields</p>
</blockquote></td>
<td><blockquote>
<p>^ORD(102.24,</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Test Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CPRS Query (Hepatitis C Reports) was tested at the following sites:

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 28%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Test Sites</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Alpha</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Beta</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Milwaukee, WI</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Northern California</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Palo Alto, CA</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>San Diego, CA</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

# Installation Instructions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Retrieve the Zip file (OR_30_153.ZIP) and unzip it.

> The ZIP file contains the GUI Executable and the documentation files: OR_30_153IG.PDF Installation Guide

> OR_30_153UM.PDF User Manual

2.  Use PackMan’s Install/Check Message option to load OR\*3.0\*153 into KIDS from a Forum message.
3.  Use the KIDS Installation option to install the patch. Answer NO to the following questions :

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? Want KIDS to INHIBIT LOGONs during the install?

> Want to DISABLE Scheduled Options, Menu Options, and Protocols?

> Installation Example

> Incoming Files:

> 100 ORDER (Partial Definition) Note: You already have the 'ORDER' File.

21. CPRS QUERY DEFINITION (including data)
22. CPRS QUERY CONSTRAINT (including data)
23. CPRS QUERY EDIT CONTROL (including data)
24. CPRS QUERY DISPLAY FIELDS (including data)

> 8989.51 PARAMETER DEFINITION (including data) Note: You already have the 'PARAMETER DEFINITION' File. I will REPLACE your data with mine.

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

> Want KIDS to INHIBIT LOGONs during the install? YES// NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// ANYWHERE

> OR\*3.0\*153

> ─────────────────────────────────────────────────

> Install Started for OR\*3.0\*153 :

> Apr 18, 2003@12:07:57

> Build Distribution Date: Apr 04, 2003

> Installing Routines:

> Apr 18, 2003@12:07:57

> Installing Data Dictionaries:

> Apr 18, 2003@12:07:57

> Installing Data:

> Apr 18, 2003@12:07:56

> Installing PACKAGE COMPONENTS: Installing REMOTE PROCEDURE

> Installing OPTION

> Apr 18, 2003@12:07:57

> Running Post-Install Routine: POST^ORY153

> Task \#313902 started to rebuild ^OR(100,"ARS"). Updating Routine file...

> The following Routines were created during this install: ORD2

> ORD21

# Implementation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Steps for setting up the CPRS QUERY GUI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Make sure the VistA servers are listed in the HOSTS file. If necessary, modify the HOSTS file of each client (PC) to set the appropriate mappings between names and IP addresses. The HOSTS file is located as follows:

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Version of Windows OS</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File (Location and Name)</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Windows 95</td>
<td>C:\WINDOWS\HOSTS</td>
</tr>
<tr class="even">
<td>Windows NT 3.51</td>
<td>C:\WINDOWS\SYSTEM32\DRIVERS\ETC\HOSTS</td>
</tr>
<tr class="odd">
<td><p>Windows NT 4.0,</p>
<p>Windows 2000</p></td>
<td>C:\WINNT\SYSTEM32\DRIVERS\ETC\HOSTS</td>
</tr>
</tbody>
</table>

> Example of a Windows 95 HOSTS file

1.  Move the cursor to the end of the last line displayed in the file.
2.  Press the \<Enter\> key to create a new line.
3.  On the new line, enter the desired IP address beginning in the first column, as described in the example above. As recommended, add an appropriate IP address for the DHCPSERVER host name as the next entry below 127.0.0.1.

> After typing the IP address, type at least one space, and enter the host name that corresponds to that IP address. As recommended, type in DHCPSERVER as the next entry below "loopback."

> For example, the entry for a server at your site with an IP address of 10.5.21.66 would look like this:

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>127.0.0.1</p>
</blockquote></th>
<th><blockquote>
<p>localhost</p>
</blockquote></th>
<th><blockquote>
<p># loopback <strong>&lt;---existing entry</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>10.5.21.66</p>
</blockquote></td>
<td><blockquote>
<p>DHCPSERVER</p>
</blockquote></td>
<td><blockquote>
<p># HepC <strong>&lt;---added entry</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

4.  Repeat steps a - c until you have entered all of the IP addresses and corresponding host names you wish to enter.
5.  When your entries are complete, use Notepad’s File \| Save command to save the HOSTS file.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>☞</th>
<th><blockquote>
<p>Do not save the HOSTS file with an extension; delete the .sam!</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

6.  Close the HOSTS file.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>☞</th>
<th><blockquote>
<p>The HOSTS file location on NT 4.0 Client is different from on WIN95. The Hepatitis C executable attempts  using RPC Broker  to log in to the default VistA server when Hepatitis C executes. RPC Broker cannot find the HOSTS file, so it uses the default.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> For more information, see the *RPC Broker V.1.1 Systems Manual*.

2.  Open the OR_30_153.zip file that contains the CPRSQuery.exe, OR3_0.\_153IG.PDF and OR3_0.\_153UM.PDF files.
3.  Copy the CPRSQuery.exe to the workstations or put the files in a shared directory on the network.
4.  Create desktop shortcut icons and enter the HOSTS address in the Properties S=(IP address) P=(port \# of local server)

> Example:

> ![](or-3-153-cprs-query-hepatitis-c-reports-installation-implementation-guide/002.png)

5.  <span id="_bookmark7" class="anchor"></span>Start the CPRS QUERY application by double-clicking on CPRS QUERY desktop shortcut icon you just created.
6.  Ensure that CPRS QUERY (Hepatitis C Reports) users are allocated the correct user security keys.

## Required Menus, Keys, and Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ORRCM REPORTING Required Menu Option.

> In order to use the CPRS Query Tool, the menu option ORRCM REPORTING must be assigned to the user.

> ROR VA HEPC USER Required key to see the “Registry” tab.

> To see the Registry tab when selecting patients, the ROR VA HEPC USER key must be assigned to the user.

> TIU/ASU Business Rules

> Business Rules in TIU/ASU authorize specific users or groups of users to perform specified actions on documents in particular statuses. A set of business rules is exported with TIU/ASU; sites can edit or add to these.

> When you search for documents in CPRS Query, the TIU business rules are applied. Users may not see a document on their list or the content of the document in the detailed display if the business rules do not allow access to the document.

> PARAMETER: ORHEPC ABNORMAL START Abnormal Result Enabled Date Upon installation, this parameter is set at the PACKAGE level to the date the patch was installed. It may also be set at the SYSTEM level locally. Sites can change this parameter by using the General Parameter Tools, available on the CPRS Configuration (IRM) menu, or from programmer mode: XPAR MENU TOOLS/EP (Edit Parameter Values) option.

> The Abnormal Results (field 72) field is added to the Orders file (100) with this patch. This field will be defined as YES for any order that is identified as an abnormal result as defined by the following criteria:

> Consults = Existence of Significant Findings Lab = Critical high or low value

> Radiology = Primary Diagnostic Code assigned to the exam report has 'Generate Abnormal Alert' set to YES in file \#78.3

> When a user queries the abnormal result report, the available abnormal report start date will refer to the value of this parameter. Therefore, any data prior to the date set in the ORHEPC ABNORMAL START parameter will NOT be included in the report query.

# Glossary 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Terms relevant to the Hepatitis C Registry
<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term or Acronym</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>DFN</strong></p>
</blockquote></td>
<td><blockquote>
<p>File Number—the local/facility patient record number (patient file internal entry number)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Extract Data Definition</strong></p>
</blockquote></td>
<td><blockquote>
<p>This is a set of file and field numbers that identify the data that should be extracted during the extraction process.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Extract Process</strong></p>
</blockquote></td>
<td><blockquote>
<p>This process is run after the update process. This function goes through patients on the local registry and, depending on their status, extracts all available data for the patient, since the last extract was run. The extract transmits any collected data for the patient to the national database via HL7.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>HL7</strong></p>
</blockquote></td>
<td><blockquote>
<p>Health Level 7</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Hepatitis C Rx</strong></p>
</blockquote></td>
<td><blockquote>
<p>A defined list of Hepatitis C medications, see Appendix A of the Clinical Case Registries V. 1.0, Hepatitis C User Manual.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>ICD-9</strong></p>
</blockquote></td>
<td><blockquote>
<p>International Classification of Diseases, version 9</p>
<p>A numeric code used for identifying patient diagnoses associated with inpatient and outpatient care.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>ICN</strong></p>
</blockquote></td>
<td><blockquote>
<p>Integration Control Number, or national VA patient record number</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Local Registry</strong></p>
</blockquote></td>
<td><blockquote>
<p>This is the local file of patients that have either passed the selection rules and therefore been added automatically or been added manually by a designated Hepatitis C supervisor.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Local Registry Update</strong></p>
</blockquote></td>
<td><blockquote>
<p>This process adds new patients (that have had data entered since the last update was run and pass the selection rules) to the local registry.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>National Case Registry</strong></p>
</blockquote></td>
<td><blockquote>
<p>All sites running the Hepatitis C Case registry transmit their data to this central data registry.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Selection Rules</strong></p>
</blockquote></td>
<td><blockquote>
<p>A predefined set of rules that define a Hepatitis C patient. See Appendix A of the Clinical Case Registries V. 1.0, Hepatitis C User Manual for selection rules.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>PTF</strong></p>
</blockquote></td>
<td><blockquote>
<p>Patient Treatment File—refers to the VistA Inpatient File in the Local Registry Report, under “Reason Added”</p>
</blockquote></td>
</tr>
</tbody>
</table>
