---
title: PATS Installation Guide for IRM Staff
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: PATS  for IRM Staff
app_code: QAC
app_name: Patient Advocate Tracking System (PATS)
section: GUI
app_status: active
pkg_ns: QAC
patch_ver: 1.3
patch_id: QAC*1.3
group_key: "QAC:QAC:1.3"
file_numbers: []
security_keys: []
menu_options: 0
description: "<table> <colgroup> <col style=\\"width: 14%\\" /> <col style=\\"width: 14%\\" /> <col style=\\"width: 44%\\" /> <col style=\\"width: 26%\\" /> </colgroup> <tbody> <tr class=\\"odd\\"> <td><strong>Date</strong></td> <td><strong>Revision</strong></td> <td><strong>Description</strong></td> <td><strong>Author</strong></td>"
audience: 
keywords: 
  - strong
  - pats
  - class
  - blockquote
  - table
  - span
  - contents
  - migration
  - install
  - style
page_count: 0
word_count: 5251
section_count: 18
table_count: 7
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2007
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Patient_Advocate_Track/pats_1_3_installguideforirm.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Patient_Advocate_Track/pats_1_3_installguideforirm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=172"
---

![](pats-installation-guide-for-irm-staff/001.png)

PATIENT ADVOCATE TRACKING SYSTEM (PATS)INSTALLATION GUIDE FORIRM STAFF

Patch QAC\*2.0\*19

March 2007

Revised October 2011;

Office of Enterprise Development (OED)

Veterans Health Information Technology (VHIT)

Revision History

The following table displays the revision history for this document.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 44%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Revision</strong></td>
<td><strong>Description</strong></td>
<td><strong>Author</strong></td>
</tr>
<tr class="even">
<td>03/15/07</td>
<td>Initial</td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>7/12/07</td>
<td>1.1</td>
<td>Updated Sections 2.5 and 2.10. The Patient Advocate who downloads the station number list also migrates the data to PATS.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>8/09/09</td>
<td>1.2</td>
<td><ul>
<li><blockquote>
<p>Updated Section 2.4. Summarized role definitions in a table.</p>
</blockquote></li>
<li><blockquote>
<p>Changed sequence of setup sections to setup download list of station numbers and migrate data to PATS; setup pre-migration cleanup; setup SIT, SRCU, and VU users.</p>
</blockquote></li>
<li><blockquote>
<p>Updated Sections 2.5, 2.6, 2.7. Summarized security key, options, divisions, and URLs by role.</p>
</blockquote></li>
<li><blockquote>
<p>Updated Sections 2.7. Warning that individuals are assigned only one role (SIT, SRCU, VU).</p>
</blockquote></li>
<li><blockquote>
<p>Added Quick Reference Chart with security key, options, divisions, and URLs by role, Section 2.9.</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>10/10/2011</td>
<td>1.3</td>
<td><ul>
<li><blockquote>
<p>Revised the document in relation to a name change of an EIE group</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

  
Table of Contents

# # About This Document


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# About This Document](#about-this-document)
  - [Other Resources](#other-resources)
  - [<span class="mark">REDACTED</span>](#span-classmarkredactedspan)
- [# # Chapter 1 – Before You Begin to Install and Set up PATS](#chapter-1-before-you-begin-to-install-and-set-up-pats)
  - [VistALink Connector Proxy Users](#vistalink-connector-proxy-users)
  - [List of Divisions](#list-of-divisions)
- [Chapter 2 – Installation Instructions](#chapter-2-installation-instructions)
  - [Unload the PATS KIDS Distribution in VistA](#unload-the-pats-kids-distribution-in-vista)
  - [Install the PATS KIDS Distribution in VistA](#install-the-pats-kids-distribution-in-vista)
  - [Components Installed by the KIDS Build](#components-installed-by-the-kids-build)
  - [<span id="Toc174431895" class="anchor"></span>](#span-idtoc174431895-classanchorspan)
  - [Roles Defined](#roles-defined)
  - [<span id="Toc174431896" class="anchor"></span>](#span-idtoc174431896-classanchorspan)
  - [Setup for User Downloading the Station Number List and Performing Data Migration into PATS](#setup-for-user-downloading-the-station-number-list-and-performing-data-migration-into-pats)
  - [Setup for Users Performing Pre-Migration Data Cleanup](#setup-for-users-performing-pre-migration-data-cleanup)
  - [Setup for Site Information Taker Users, Site Record Control Users, and VISN-Level Patient Advocate Users](#setup-for-site-information-taker-users-site-record-control-users-and-visn-level-patient-advocate-users)
  - [Setup for National Program Office and Central Office Users](#setup-for-national-program-office-and-central-office-users)
  - [Setup Quick Reference Chart](#setup-quick-reference-chart)
  - [Download Station Number List to Temporary Global](#download-station-number-list-to-temporary-global)
  - [Assign URL Links to Users](#assign-url-links-to-users)
*Introduction*
The Patient Advocate Tracking System (PATS) provides a way of documenting and tracking patient-related issues.
*This Patient Advocate Tracking System Installation Guide* is intended for individuals on the IRM staff who are responsible for installing the PATS application and its related components at field sites. The concepts and step-by-step instructions will help field sites install and configure the PATS application.
PATS will be released by the Project Implementation Office (PIO) in a controlled manner. It is recommended that you wait until you have been notified by the PIO before you install PATS.

## *Other Resources*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## <span class="mark">REDACTED</span>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*The PATS Installation Process*

Installing PATS is seven-stage process. Steps 1 – 6 are performed at the EIE. This is intended for your information only.

The IRM staff performs Step 7.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 59%" />
<col style="width: 31%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p id="stage" class="heading">Stage</p></td>
<td><strong>Process</strong></td>
<td><strong>Role Performing Task</strong></td>
</tr>
<tr class="even">
<td><p id="section-2" class="heading">1</p></td>
<td>Download the PATS compressed file (bundle) and extract it to a temporary directory at the hosting center.</td>
<td>EIE</td>
</tr>
<tr class="odd">
<td><p id="section-3" class="heading">2</p></td>
<td>Install the PATS database at the hosting center.</td>
<td>EIE</td>
</tr>
<tr class="even">
<td><p id="section-4" class="heading">3</p></td>
<td>Install the Data Migration application at the hosting center.</td>
<td>EIE</td>
</tr>
<tr class="odd">
<td><p id="section-5" class="heading">4</p></td>
<td>Install the Download to VistA application at the hosting center.</td>
<td>EIE</td>
</tr>
<tr class="even">
<td><p id="section-6" class="heading">5</p></td>
<td>Install the PATS application at the hosting center.</td>
<td>EIE</td>
</tr>
<tr class="odd">
<td><p id="section-7" class="heading">6</p></td>
<td>Install and set up Business Objects Enterprise XI at the hosting center.</td>
<td>EIE</td>
</tr>
<tr class="even">
<td><p id="section-8" class="heading">7</p></td>
<td><strong>Install the PATS KIDS build at the field sites and assign keys, options and divisions to users.</strong></td>
<td><strong>IRM</strong></td>
</tr>
</tbody>
</table>

# # # Chapter 1 – Before You Begin to Install and Set up PATS 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before you install the KIDS build, verify that the following patches have been installed:

- VistALink XOBU 1.5
- KAAJEE patch XU\*8.0\*329
- Kernel patch XU\*8.0\*430
- Person Service Lookup patch DG\*5.3\*538
- Person Service Construct patch DG\*5.3\*557

  Verify that you have received the KIDS installation via VistA mail with the subject line *Released QAC\*2\*19*.

## VistALink Connector Proxy Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistALink Connector Proxy User is an entry on your VistA NEW PERSON file that the PATS application and other web-based applications use to connect to your VistA site. For the PATS application, there will be one data center located in <span class="mark">REDACTED</span>, VA and a second fail-over data center in <span class="mark">REDACTED</span>. A VistALink connector proxy user needs to be set up on your VistA server for the <span class="mark">REDACTED</span> data center and also for the Hines data center.

You may have already set up the VistALink connector proxy users to support the Blind Rehab or VPFS applications. In that case, you won't need to set them up. Please verify your existing VistALink connector proxy users.

To validate and/or set up VistALink connector proxy users:

1.  From the System Manager menu, select Operations Management\>User Management Menu\>Proxy User List.

    *Result: A report displays existing connector proxy users.*
2.  If you do not see any VistALink connector proxy users in the report, go to step 4.

    If there are any connector proxy users in the report, check with other ISO or IRM Specialists at your site to verify that the connection information has been given to the EIE J2EE Administrator. If you can not validate that the information has been sent, send an email to the EIE J2EE Administrator (using mail group VHA HSITES EMC HEV SUPPORT) to determine if the connectors to both the Hines and <span class="mark">REDACTED</span> data centers have been established.

    Note: Do not add new connector proxy users without consulting your EIE J2EE Administrator.
3.  Make sure that your connector proxy users are not DISUSERed or terminated.
4.  If you do not have VistALink connector proxy users already set up for both <span class="mark">REDACTED</span>, follow instructions in the *VistALink Installation Guide 1.5* (section 2.6 Post-Install: Configuring Connector Proxy User(s) for J2EE Access) to add these users to your NEW PERSON file.

    *Set up connector proxy users using the following recommended names:*
    - <span class="mark">REDACTED</span>
    - <span class="mark">REDACTED</span>

      Give the following connector information to the EIE J2EE Administrator using email group VHA HSITES EMC HEV SUPPORT:
- Your site name
- Your computing station number
- Your fully qualified domain name (FQDN)
- Port number for your VistALink connection
- Access/verify code of the connector proxy user for the Hines data center and the <span class="mark">REDACTED</span> data center (securely communicate this information using PKI, FED EX properly addressed, by phone, or using local requirements for secure communications).

## List of Divisions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to the information for connecting to your VistA account, you must also provide a list of divisions to the Project Implementation Office (PIO). The list will be used to populate the Division drop-down list for log on. This list will come from your MEDICAL CENTER DIVISION file, which is the list you currently use when entering a new Report of Contact.

You can get that list by running the following FileMan report:

Select OPTION: 2 PRINT FILE ENTRIES

OUTPUT FROM WHAT FILE: MEDICAL CENTER DIVISION// MEDICAL CENTER DIVISION

(nn entries)

SORT BY: NAME// \<Enter\>

START WITH NAME: FIRST// \<Enter\>

FIRST PRINT FIELD: .01 NAME

THEN PRINT FIELD: INSTITUTION FILE POINTER

THEN PRINT FIELD: INSTITUTION FILE POINTER:STATION NUMBER

THEN PRINT FIELD: \<Enter\>

Heading (S/C): MEDICAL CENTER DIVISION LIST Replace \<Enter\>

<span class="mark">REDACTED</span>.

# Chapter 2 – Installation Instruction*s*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes the install of the KIDS build and the setup instructions. There is a separate *Patient Advocate Tracking System (PATS) Data Migration Guide* that will lead you through the process of migrating the legacy data.

You will install a KIDS build to support PATS. The KIDS build contains both components needed for migrating the Patient Representative legacy data into PATS and components needed while running PATS.

To install and set up PATS at field sites, complete the following tasks:

1.  Unload the PATS KIDS distribution in VistA.
2.  Install the PATS KIDS distribution in VistA.
3.  Setup for user downloading the station number list and performing data migration into PATS.
4.  Setup for users performing pre-migration data cleanup.
5.  Setup for Site Information Taker (SIT) users.
6.  Setup for Site Record Control Users (SRCU).
7.  Setup for VISN-level users (VU) if a VISN-level user has access to your VistA account.
8.  Setup for National Program Office (NPO) or Central Office (CO) users (only if you maintain a VistA system used to allow logon by NPO or CO).
9.  Assign URL links for the Pre-migration Data Cleanup, Data Migration and PATS applications to users.

> **NOTE:** When your site is scheduled to begin pre-migration data cleanup, the Program Implementation Office (PIO) will instruct you to install this patch and will send you a URL link used by the data cleanup option.

When your site is scheduled to begin using the PATS application, the PIO will send you two URL links—one to the data migration application and one to the PATS application.

## Unload the PATS KIDS Distribution in VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use VistA Mail to read the message containing the KIDS build. Then use the Packman Extract KIDS option to unload the KIDS build onto your system.

Follow the instructions below to extract the KIDS build. Information in bold type indicates how you will answer questions and keys you press.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Subj: Released QAC*2*19 SEQ #18 [#411] 3 Mar 2006 12:02:06 -0500 (EST) 5327 lines</p>
<p>From: &lt;"NPM [#39264106]"@FORUM.VA.GOV&gt; In 'IN' basket. Page 1 *New*</p>
<p>---------------------------------------------------</p>
<p>$TXT Created by <mark>REDACTED</mark> at CHEY45.FO-<mark>REDACTED</mark> (KIDS) Friday, 03/03/06 at 11:56</p>
<p>===================================================</p>
<p>Run Date: MAR 03, 2006 Designation: QAC*2*19</p>
<p>Package : QAC - PATIENT REPRESENTATIVE Priority: Mandatory</p>
<p>Version : 2 Status: Released</p>
<p>===================================================</p></td>
</tr>
<tr class="even">
<td><p>Associated patches: (v)QAC*2*18 &lt;&lt;= must be installed BEFORE ‘QAC*2*19’</p>
<p>Subject: PATS Transition</p>
<p>Category:</p>
<p>- Enhancement (Mandatory)</p>
<p>- Routine</p>
<p>- Other</p>
<p>Description:</p>
<p>============</p></td>
</tr>
<tr class="odd">
<td><p>Enter RETURN to continue or '^' to exit: <strong>^ [Enter]</strong></p>
<p>Enter message action (in IN basket): Delete// <strong>x [Enter]</strong> Xtract KIDS</p>
<p>Select PackMan function: <strong>6 [Enter]</strong> INSTALL/CHECK MESSAGE</p></td>
</tr>
<tr class="even">
<td><p>Line 160 Message #29 Unloading KIDS Distribution QAC*2.0*19</p>
<p>QAC*2.0*19</p>
<p>Want to Continue with Load? YES// <strong>YES [Enter]</strong></p>
<p>Loading Distribution...</p>
<p>QAC*2.0*19</p>
<p>Will first run the Environment Check Routine, QACIENV</p></td>
</tr>
</tbody>
</table>

> Note: The environment check routine will make sure that the broker type options DGRR GUI PATIENT LOOKUP and DGRR PATIENT SERVICE QUERY exist in your VistA account.

## Install the PATS KIDS Distribution in VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After you have completed unloading the KIDS build from the mail message, you are ready to install it. Use Install Name QAC\*2.0\*19 to install this distribution.

Some tips on installing the KIDS build:

- This patch can be loaded with users on the system; however, it should be installed during a non-peak period of usage.
- From the Installation menu, you may want to Verify Checksums in Transport Global to insure the integrity of the routines in the transport global, and Print Transport Global to view the components in the KIDS build.
- There is no need to Backup a Transport Global or Compare Transport Global to Current System, because this patch brings in new routines and does not change any of the existing Patient Representative routines.
- This installation will bring new routines, options, remote procedures and keys. It does not bring in any new files or data, and does not alter any existing files or data. The patch does no data conversions.
- There is no need to inhibit logons or to disable any options or protocols while installing this patch.

The patch should run in a few seconds.

> The *Patient Advocate Tracking System (PATS) Systems Management Guide* contains detailed information about all of the components installed by this patch.

> From Installation option on the Kernel Installation and Distribution (KIDS) menu

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>1 Load a Distribution</p>
<p>2 Verify Checksums in Transport Global</p>
<p>3 Print Transport Global</p>
<p>4 Compare Transport Global to Current System</p>
<p>5 Backup a Transport Global</p>
<p>6 Install Package(s)</p>
<p>Restart Install of Package(s)</p>
<p>Unload a Distribution</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Select Installation Option: <span class="smallcaps"><strong>6 [Enter]</strong></span> Install Package(s)</td>
</tr>
<tr class="even">
<td><p>Select INSTALL NAME: <strong>QAC*2.0*19 <span class="smallcaps">[Enter] </span></strong> Loaded from Distribution 03/03/06@12:02:06</p>
<p>=&gt; Released QAC*2*19 SEQ #18</p>
<p>This Distribution was loaded on Mar 12, 2006@16:05:53 with header of</p>
<p>Released QAC*2*19 SEQ #18</p>
<p>It consisted of the following Install(s):</p>
<p>QAC*2.0*19</p>
<p>Checking Install for Package QAC*2.0*19</p>
<p>Will first run the Environment Check Routine, QACIENV</p>
<p>Install Questions for QAC*2.0*19</p></td>
</tr>
<tr class="odd">
<td>Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// <strong><span class="smallcaps">NO [Enter]</span></strong></td>
</tr>
<tr class="even">
<td>Want KIDS to INHIBIT LOGONs during the install? YES// <strong><span class="smallcaps">NO [Enter]</span></strong></td>
</tr>
<tr class="odd">
<td><p>Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// <strong><span class="smallcaps">NO [Enter]</span></strong></p>
<p>Enter the Device you want to print the Install messages.</p>
<p>You can queue the install by enter a 'Q' at the device prompt.</p>
<p>Enter a '^' to abort the install.</p></td>
</tr>
<tr class="even">
<td><p>DEVICE: HOME// <strong><span class="smallcaps">[Enter]</span></strong></p>
<p>Install Started for QAC*2.0*19 :</p>
<p>Mar 12 2006@16:05:54</p>
<p>Build Distribution Date: Jun 22 2004</p>
<p>QAC*2.0*19</p>
<p>───────────────────────────────────────────────────────</p>
<p>Installing Routines:</p>
<p>Mar 12 2006@16:05:54</p>
<p>Installing PACKAGE COMPONENTS:</p>
<p>Installing SECURITY KEY</p>
<p>Installing REMOTE PROCEDURE</p>
<p>Installing OPTION</p>
<p>Mar 12 2006@16:05:55</p></td>
</tr>
<tr class="odd">
<td><p>Updating Routine file...</p>
<p>Updating KIDS files...</p>
<p>QAC*2.0*19 Installed.</p>
<p>Mar 12 2006@16:05:56</p>
<p>NO Install Message sent</p>
<p>───────────────────────────────────────────────────────</p>
<p>┌─────────────────────────────────────────────────────┐</p>
<p>│ 25 50 75 100% │ └─────────────────────────────────────────────────────┘</p>
<p>Install Completed</p></td>
</tr>
</tbody>
</table>

## Components Installed by the KIDS Build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>Routines installed by the KIDS build</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>QACI0</p>
</blockquote></td>
<td><blockquote>
<p>QACI2E</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>QACI1</p>
</blockquote></td>
<td><blockquote>
<p>QACI3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>QACI1A</p>
</blockquote></td>
<td><blockquote>
<p>QACI4</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>QACI2</p>
</blockquote></td>
<td><blockquote>
<p>QACI5</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>QACI20</p>
</blockquote></td>
<td><blockquote>
<p>QACIENV</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>QACI2A</p>
</blockquote></td>
<td><blockquote>
<p>QACVDEM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>QACI2B</p>
</blockquote></td>
<td><blockquote>
<p>QACVEMPX</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>QACI2C</p>
</blockquote></td>
<td><blockquote>
<p>QACVKHLD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>QACI2D</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

| Options installed by the KIDS build |
|-----------------------------------------|
| QACI AUTO CLOSE ROCS                    |
| QACI INACTIVATE PAT REP                 |
| QACI KILL ROLLUP TASK                   |
| QACI MAIN DATA CLEANUP MENU             |
| QACI MAIN PATS MIGRATION MENU           |
| QACI MIGRATION DATA BUILD               |
| QACI PATS RPC ACCESS                    |
| QACI PREMIGRATION ERROR REPORT          |
| QACI REPORT AUTO-CLOSED ROCS            |
| QACI REPORT MENU                        |
| QACI REPORT MIGR COUNTS                 |
| QACI REPORT NOTIFICATIONS               |
| QACI REPORT ROC CHANGES                 |
| Options installed by the KIDS build |
| QACI REPRINT ERRORS REPORT              |
| QACI RESCHEDULE ROLLUP TASK             |
| QACI ROC MIGRATION STATUS               |
| QACI UTILITY MENU                       |
| QACV PATS RPC ACCESS                    |

| Keys installed by the KIDS build |
|--------------------------------------|
| QACV_ADUSH                           |
| QACV_DMGR                            |
| QACV_NPO                             |
| QACV_SIT                             |
| QACV_SRCU                            |
| QACV_VU                              |

| Remote Procedures installed by the KIDS build |
|---------------------------------------------------|
| QACI DELETE ALL LISTS                             |
| QACI LOAD REFERENCE TABLES                        |
| QACI LOAD ROC                                     |
| QACV KEY HOLDERS VLH                              |
| QACV PERSON LOOKUP VLH                            |
| QACI NATL INSTITUTION LIST                        |

> Pre-Init Routine QACIENV

> This routine makes sure that the Patient Service Lookup broker type option DGRR GUI PATIENT LOOKUP, and the Patient Service Construct broker type option DGRR PATIENT SERVICE QUERY exist at the site where the installation will take place.

## <span id="_Toc174431895" class="anchor"></span>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Roles Defined

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before users have access to the PATS application, you must assign them roles with associated security keys, options and divisions. Each role has specific functions the user can perform in PATS.

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Role</strong></th>
<th><strong>Tasks role performs</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Data Migration Manager</strong></td>
<td><ul>
<li><blockquote>
<p>Download national station list</p>
</blockquote></li>
<li><blockquote>
<p>Oversee data cleanup</p>
</blockquote></li>
<li><blockquote>
<p>Perform the data migration</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Users performing data cleanup</strong></td>
<td>Clean up Patient Rep data prior to migrating the data into PATS</td>
</tr>
<tr class="odd">
<td><strong>SIT – Site Information Taker</strong></td>
<td><ul>
<li><blockquote>
<p>Add an ROC (Report of Contact)</p>
</blockquote></li>
<li><blockquote>
<p>Edit an ROC entered by the person</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>SRCU – Site Record Control User (Patient Advocate)</strong></td>
<td><ul>
<li><blockquote>
<p>Add or edit their ROCs</p>
</blockquote></li>
<li><blockquote>
<p>Edit ROCs entered by others</p>
</blockquote></li>
<li><blockquote>
<p>Send notifications</p>
</blockquote></li>
<li><blockquote>
<p>Run reports (Standard and Ad hoc)</p>
</blockquote></li>
<li><blockquote>
<p>Update local reference tables: Congressional Contact, Hospital Locations, Comps, Resolution Text</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>VU – VISN User (VISN-Level Advocate)</strong></td>
<td><strong>Same as SRCU with additional task of updating Facility Service or Section reference table</strong></td>
</tr>
<tr class="even">
<td><strong>NPO – National Program Office user</strong></td>
<td><ul>
<li><blockquote>
<p>Update national tables: Method of Contact, Treatment Status, Issue Category/Issue Code, Contacting Entity, Days until an ROC expires</p>
</blockquote></li>
<li><blockquote>
<p>Run national reports</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>CO – Central Office user</strong></td>
<td><blockquote>
<p>Run some national reports</p>
</blockquote></td>
</tr>
</tbody>
</table>

## <span id="_Toc174431896" class="anchor"></span>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Setup for User Downloading the Station Number List and Performing Data Migration into PATS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following setup steps will allow any VistA user to perform the first step in data cleanup (downloading the national station number list) and to perform data migration from Patient Rep to PATS. This job (Data Migration Manager) will usually be done by an SRCU.

1.  Check with the current Patient Representative users to determine who will download the station number list and perform the migration of Patient Representative data into PATS. This person must have access to a PC and a browser.
2.  Select the *Edit an Existing User* option. Assign the new Broker Type option QACI PATS RPC ACCESS as a secondary menu to the user. This option will not need a synonym. The option will allow the PATS system to access the Patient Representative legacy data on the VistA system during the migration.
3.  From *Edit an Existing User*, assign the new option QACI MAIN PATS MIGRATION MENU as a secondary menu to the users. Give the secondary menu the synonym PRDM.
4.  In a site that has multiple divisions, the user performing data migration MUST have the default institution in their DIVISIONS list (i.e., the facility with the 3-digit station number). Data for the default institution and all divisions within the default institution will be migrated, regardless of any other divisions assigned to the user.

> a\. Select the *Edit an Existing User* option.

> b\. At the *Select DIVISION* prompt, select the default institution.

5.  In a site that has one division, the user is given access to the Institution set as the DEFAULT INSTITUTION in your KERNEL SYSTEM PARAMETERS file.

> Note: For more details on how the list of accessible Divisions is used during sign-on, see the *KAAJEE Installation Guide*.

6.  Select the *Key Management* option to assign the new security key QACV_DMGR to the user. This will be used to make a VistALink connection between the data migration application and the VistA system during the migration.

    The table summarizes the setup for the user downloading the list of station numbers and performing data migration into PATS:

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 20%" />
<col style="width: 24%" />
<col style="width: 17%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Role</strong></th>
<th><strong>Security Key</strong></th>
<th><strong>Options</strong></th>
<th><strong>Divisions</strong></th>
<th><strong>URLs</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Data Migration Manager</strong></td>
<td>QACV_DMGR</td>
<td><p>QACI MAIN PATS MIGRATION MENU (synonym PRDM)</p>
<p>QACI PATS RPC ACCESS</p></td>
<td>3-digit default institution</td>
<td><p>PATSDV application (Download national station numbers)</p>
<p>PATSDM application (Data Migration)</p></td>
</tr>
</tbody>
</table>

## Setup for Users Performing Pre-Migration Data Cleanup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following setup steps will give any VistA user access to reports used to clean up the data prior to migration from Patient Rep to PATS. This job will usually be done by SIT or SRCU users.

1.  Check with your current Patient Representative users to see which users will be performing the pre-migration data cleanup role (see the *Patient Advocate Tracking System (PATS) Data Migration Guide* if your users need help in deciding who will perform that function).
2.  Select the *Edit an Existing User* option. Assign the new option QACI MAIN DATA CLEANUP MENU as a secondary menu to the user. Give the secondary menu the synonym PRDC.The table summarizes the setup for users performing pre-migration data cleanup:

<table style="width:100%;">
<colgroup>
<col style="width: 17%" />
<col style="width: 19%" />
<col style="width: 30%" />
<col style="width: 17%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Role</strong></th>
<th><strong>Security Key</strong></th>
<th><strong>Options</strong></th>
<th><strong>Divisions</strong></th>
<th><strong>URLs</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>User(s) performing data cleanup</strong></td>
<td>None</td>
<td>QACI MAIN DATA CLEANUP MENU<br />
(synonym PRDC)</td>
<td>None</td>
<td>None</td>
</tr>
</tbody>
</table>

> Note: At least one user must be set up to download the list of national stations and perform data migration as described in Section 2.5.

## Setup for Site Information Taker Users, Site Record Control Users, and VISN-Level Patient Advocate Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section covers the steps to set up users for the following roles: Site Information taker (SIT), Site Record Control User (SRCU), VISN-level User (VU).

> Note: SIT, SRCU or VU roles should not be combined with either the CO or NPO role.

1.  Check with the current Patient Representative users to determine who will be assigned the following roles:
- SIT-level access
- SRCU-level access
- VISN-level access (VU)

| ![](pats-installation-guide-for-irm-staff/002.png) | *Only assign an individual ONE of the following roles: SIT, SRCU, VU.* |
|---------------------------------------------------|----------------------------------------------------------------------------|

1.  Select the *Edit an Existing User* option to assign the new Broker Type option QACV PATS RPC ACCESS as a secondary menu to the users. This option will not need a synonym. It allows the PATS system to access Patient and New Person data from the VistA system.
2.  Use the *Edit an Existing User* option to assign options DGRR GUI PATIENT LOOKUP and DGRR PATIENT SERVICE QUERY as secondary menus to the user. These options do not require synonyms. They are used to support the Patient Lookup service used in the PATS application.
3.  In a site that has multiple divisions, give each user access to all divisions to which they need access. PATS users need access only to divisions in your MEDICAL CENTER DIVISION file. Note you MUST enter any division they need to access in this list:
1.  Select the *Edit an Existing User* option.
2.  At the *Select DIVISION prompt,* add each Division the user is permitted to access.
1.  In a site that has one division, the user is given access to the Institution set as the DEFAULT INSTITUTION in your KERNEL SYSTEM PARAMETERS file.

> Note: For more details on how the list of accessible Divisions is used during sign-on, see the *KAAJEE Installation Guide*.

2.  Select the *Key Management* option to assign the applicable security key:

| Role                     | Security Key              |
|------------------------------|-------------------------------|
| SIT                      | QACV_SIT                  |
| SRCU                     | QACV_SRCU                 |
| VU (VISN-level Advocate) | QACV_SRCU and QACV_VU |

  
The table summarizes the setup for the SIT, SRCU, and VU roles:

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 17%" />
<col style="width: 25%" />
<col style="width: 24%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Role</strong></th>
<th><strong>Security Key</strong></th>
<th><strong>Options</strong></th>
<th><strong>Divisions</strong></th>
<th><strong>URLs</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>SIT</strong></p>
<p>![](pats-installation-guide-for-irm-staff/003.png)</p></td>
<td>QACV_SIT</td>
<td><p>QACV PATS RPC ACCESS</p>
<p>DGRR GUI PATIENT LOOKUP</p>
<p>DGRR PATIENT SERVICE QUERY</p></td>
<td><p>All divisions whose data the user should access.</p>
<p>If no divisions are assigned, the person can only access the 3-digit default institution.</p></td>
<td>PATS application</td>
</tr>
<tr class="even">
<td><p><strong>SRCU</strong></p>
<p>![](pats-installation-guide-for-irm-staff/004.png)</p></td>
<td>QACV_SRCU</td>
<td>Same as SIT</td>
<td>Same as SIT</td>
<td>PATS application</td>
</tr>
<tr class="odd">
<td><p><strong>VU<br />
(VISN-level Advocate)</strong></p>
<p>![](pats-installation-guide-for-irm-staff/005.png)</p></td>
<td>QACV_SRCU and QACV_VU</td>
<td>Same as SIT</td>
<td>Same as SIT</td>
<td>PATS application</td>
</tr>
</tbody>
</table>

## Setup for National Program Office and Central Office Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PATS system provides national reports to National Program Office (NPO) users and Central Office (CO). In addition, NPO users will maintain some national tables using PATS.

> **NOTE:** These users will probably not be users on an existing medical center’s VistA system. However, PATS logon requires that the users have a VistA access and verify code; NPO and CO users will need to be users on some VistA system.

> Note: NPO and CO roles should not be combined with the SIT, SRCU or VU role.

Setup on the VistA side is minimal, because these users access reports showing data for all divisions and don’t retrieve any data directly from VistA (only from the PATS Oracle tables).

1.  NPO and CO users should be assigned a menu only if they need to access a VistA option directly.
2.  NPO and CO users do not need to be assigned any divisions in their DIVISION multiple. They will log on to PATS using the Institution set as the DEFAULT INSTITUTION in the KERNEL SYSTEM PARAMETERS file on the VistA account to which they have access.
3.  Select the *Key Management* option to assign the applicable security key:

| Role | Security Key |
|----------|------------------|
| CO   | QACV_ADUSH   |
| NPO  | QACV_NPO     |

## Setup Quick Reference Chart

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The chart below summarizes the security key, options, divisions, and URLs that you assign to individuals by their role. Roles are defined in Section 2.4. For instructions on setting up specific roles, see Sections 2.5 – 2.8.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 16%" />
<col style="width: 22%" />
<col style="width: 24%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Role</strong></th>
<th><strong>Security Key</strong></th>
<th><strong>Options</strong></th>
<th><strong>Divisions</strong></th>
<th><strong>URLs</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Data Migration Manager</strong></td>
<td>QACV_DMGR</td>
<td><p>QACI MAIN PATS MIGRATION MENU (synonym PRDM)</p>
<p>QACI PATS RPC ACCESS</p></td>
<td>3-digit default institution</td>
<td><p>PATSDV application (Download national station numbers)</p>
<p>PATSDM application (Data Migration)</p></td>
</tr>
<tr class="even">
<td><strong>User(s) performing data cleanup</strong></td>
<td>None</td>
<td>QACI MAIN DATA CLEANUP MENU<br />
(synonym PRDC)</td>
<td>None</td>
<td>None</td>
</tr>
<tr class="odd">
<td><p><strong>SIT</strong></p>
<p>![](pats-installation-guide-for-irm-staff/006.png)</p></td>
<td>QACV_SIT</td>
<td><p>QACV PATS RPC ACCESS</p>
<p>DGRR GUI PATIENT LOOKUP</p>
<p>DGRR PATIENT SERVICE QUERY</p></td>
<td><p>All divisions whose data the user should access.</p>
<p>If no divisions are assigned, the person can only access the 3-digit default institution.</p></td>
<td>PATS application</td>
</tr>
<tr class="even">
<td><p><strong>SRCU</strong></p>
<p>![](pats-installation-guide-for-irm-staff/007.png)</p></td>
<td>QACV_SRCU</td>
<td>Same as SIT</td>
<td>Same as SIT</td>
<td>PATS application</td>
</tr>
<tr class="odd">
<td><p><strong>VU<br />
(VISN-level Advocate)</strong></p>
<p>![](pats-installation-guide-for-irm-staff/008.png)</p></td>
<td>QACV_SRCU and QACV_VU</td>
<td>Same as SIT</td>
<td>Same as SIT</td>
<td>PATS application</td>
</tr>
</tbody>
</table>

| ![](pats-installation-guide-for-irm-staff/009.png) | *Only assign an individual ONE of the following roles: SIT, SRCU, VU.* |
|---------------------------------------------------|----------------------------------------------------------------------------|

## Download Station Number List to Temporary Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When it is time for your site to begin pre-migration data cleanup, the Project Implementation Office (PIO) will notify you and send a URL link. After you install the KIDS build, share that URL link with your Point of Contact in the Patient Advocates Office—the person who will perform the data migration. That user will click on the link to log on to the application and press the Download button. A list of station numbers from the EIE master institution file will be downloaded into the temporary global ^XTMP(“QACMIGR”,”STDINSTITUTION”) on your VistA system. The list is needed to do pre-migration data error checking. This list only needs to be downloaded one time; but if it is run multiple times, it will not hurt anything.

Detailed instructions for running the application are documented in the *Patient Advocate Tracking System (PATS) Data Migration Guide.*Note: If you accidentally download the stations prior to installing the KIDS build it will not cause a problem.

## Assign URL Links to Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After your site has installed the local PATS KIDS build, your patient advocates will be given about a month to perform data cleanup in preparation for migrating the data into PATS. The Project Implementation Office (PIO) will schedule a time for your site to begin using the new PATS application. At that time, PIO will send you two URL links—one to the data migration application and the other to the PATS application.

1.  Share the link to the data migration application with the user who will migrate the legacy Patient Rep data into the new PATS database.
2.  Share the link to the PATS application with all users who need access to the application (i.e., all of the users you have set up in the preceding steps).
3.  Instruct individuals that use either the data migration application or the PATS application to save the links in their Favorites folder in the browser.
4.  You will probably also want to instruct the users to save a shortcut to the PATS application on their desktops.