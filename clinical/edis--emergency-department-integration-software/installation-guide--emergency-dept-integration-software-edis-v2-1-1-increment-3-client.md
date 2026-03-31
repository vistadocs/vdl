---
title: Emergency Dept Integration Software (EDIS) Version 2.1.1 Increment 3 Client Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: Increment 3 Client
app_code: EDIS
app_name: Emergency Department Integration Software
section: CLI
app_status: archive
pkg_ns: EDIS
patch_ver: 2.1.1
patch_id: EDIS*2.1.1
group_key: "EDIS:EDIS:2.1.1"
file_numbers: []
security_keys: []
menu_options: 8
description: - [Department of Veterans Affairs](#department-of-veterans-affairs) - [Emergency Department Integration Software (EDIS) Version 2.1.1 Increment 3](#emergency-department-integration-software-edis-version-211-increment-3) - [Product Description](#product-description) - [Recommended Audience](#recommen
audience: 
keywords: 
  - table
  - contents
  - blockquote
  - later
  - requirements
  - class
  - strong
  - emergency
  - integration
  - software
page_count: 0
word_count: 1203
section_count: 11
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2013
revision_count: 28
revision_newest: 07/17/2013
revision_oldest: 01/10/2012
docx_url: "https://www.va.gov/vdl/documents/Clinical/Emergency_Dept_Integration_Software_Archive/edp_2_1_1_cg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Emergency_Dept_Integration_Software_Archive/edp_2_1_1_cg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=358"
---

# Department of Veterans Affairs


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Department of Veterans Affairs](#department-of-veterans-affairs)
    - [Emergency Department Integration Software (EDIS) Version 2.1.1 Increment 3](#emergency-department-integration-software-edis-version-211-increment-3)
- [Product Description](#product-description)
  - [Recommended Audience](#recommended-audience)
  - [About this Guide](#about-this-guide)
  - [Section 508 of the Rehabilitation Act of 1973](#section-508-of-the-rehabilitation-act-of-1973)
  - [Document Conventions](#document-conventions)
  - [Referenced Documents](#referenced-documents)
    - [Table 1: Documentation Description](#table-1-documentation-description)
- [Before Beginning the Update](#before-beginning-the-update)
  - [Verify Workstation Configuration](#verify-workstation-configuration)
    - [Flash Player: Minimum Requirements for Microsoft Windows](#flash-player-minimum-requirements-for-microsoft-windows)
    - [Table 2: Requirements for Microsoft Windows](#table-2-requirements-for-microsoft-windows)
    - [Table 3: Requirements for Apple MacOS](#table-3-requirements-for-apple-macos)
  - [Check Server Requirements (Thin Client Environments—You May Do This Later)](#check-server-requirements-thin-client-environmentsyou-may-do-this-later)
  - [Install Flex Scripts on JAWS Users’ Machines (You May Do This Later)](#install-flex-scripts-on-jaws-users-machines-you-may-do-this-later)
- [Post Installation – URL Access](#post-installation-url-access)
  - [Production URL – Usage](#production-url-usage)
    - [REDACTED Figure 1: The Create Shortcut dialog box](#redacted-figure-1-the-create-shortcut-dialog-box)
    - [![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-client-instal/002.png)Figure 2: The Select a Title for the Program dialog box.](#emergency-dept-integration-software-edis-version-2-1-1-increment-3-client-instal002pngfigure-2-the-select-a-title-for-the-program-dialog-box)
  - [Pre-Production URL – Usage](#pre-production-url-usage)
- [Acronyms](#acronyms)

### Emergency Department Integration Software (EDIS) Version 2.1.1 Increment 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Client Installation Guide
![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-client-instal/001.png)
> July 2013
> Document Version 3.6
| Date   | Document Version | Description                                                                   | Author                         |
|------------|----------------------|-----------------------------------------------------------------------------------|------------------------------------|
| 01/06.2012 | 1.0                  | Initial EDIS v2.0                                                                 | <span class="mark">REDACTED</span> |
| 01/10/2012 | 1.0                  | Technical Review                                                                  | <span class="mark">REDACTED</span> |
| 01/11/2012 | 2.0                  | Technical Edits                                                                   | <span class="mark">REDACTED</span> |
| 01/12/2012 | 2.0                  | Final Review prior to Submission                                                  | <span class="mark">REDACTED</span> |
| 02/29/2012 | 2.1                  | Technical Review                                                                  | <span class="mark">REDACTED</span> |
| 2/29/2012  | 2.1                  | Technical Edits and Review                                                        | <span class="mark">REDACTED</span> |
| 05/14/2012 | 2.2                  | Review document and update revision history                                       | <span class="mark">REDACTED</span> |
| 05/14/2012 | 2.2                  | Review                                                                            | <span class="mark">REDACTED</span> |
| 05/21/2012 | 2.3                  | Document revisions and figure updates                                             | <span class="mark">REDACTED</span> |
| 08/26/2012 | 2.4                  | Document review and updates                                                       | <span class="mark">REDACTED</span> |
| 09/04/2012 | 2.5                  | Document review and updates                                                       | <span class="mark">REDACTED</span> |
| 09/05/2012 | 2.5                  | Document review and updates                                                       | <span class="mark">REDACTED</span> |
| 09/18/2012 | 2.6                  | Document review and updates                                                       | <span class="mark">REDACTED</span> |
| 09/24/2012 | 2.7                  | Installation instruction additions, updated URL embedded within document          | <span class="mark">REDACTED</span> |
| 9/26/2012  | 2.7                  | Final review prior to submission                                                  | <span class="mark">REDACTED</span> |
| 10/14/2012 | 2.8                  | Updated links within document                                                     | <span class="mark">REDACTED</span> |
| 10/22/2012 | 2.9                  | Made updates (incorporated edits from \[T.S.\])                                   | <span class="mark">REDACTED</span> |
| 11/29/2012 | 3.0                  | Updated footer                                                                    | <span class="mark">REDACTED</span> |
| 11/30/2012 | 3.0                  | Final review prior to submission                                                  | <span class="mark">REDACTED</span> |
| 01/03/2013 | 3.1                  | Addressed Product Support Feedback                                                | EDIS Team                          |
| 01/04/2013 | 3.1                  | Reviewed prior to submission                                                      | <span class="mark">REDACTED</span> |
| 1/14/2013  | 3.2                  | Incorporate Product Support feedback                                              | <span class="mark">REDACTED</span> |
| 2/18/2013  | 3.3                  | URL updated                                                                       | <span class="mark">REDACTED</span> |
| 5/10/2013  | 3.4                  | Review and minor updates                                                          | <span class="mark">REDACTED</span> |
| 5/11/2013  | 3.4                  | Updated product description, changed cover page, technical and grammatical review | <span class="mark">REDACTED</span> |
| 05/12/2013 | 3.4 | Final review prior to submission                 | <span class="mark">REDACTED</span> |
|------------|-----|--------------------------------------------------|------------------------------------|
| 06/19/2013 | 3.5 | Incorporate edits from Product Support           | Prod Dev                           |
| 06/20/2013 | 3.5 | Updated footer, Technical Edits, and Review      | <span class="mark">REDACTED</span> |
| 07/17/2013 | 3.6 | Update to remove zip reference and change to HWS | ProdDev                            |
1.  [PRODUCT DESCRIPTION 1](#product-description)
    1.  [RECOMMENDED AUDIENCE 1](#recommended-audience)
    2.  [ABOUT THIS GUIDE 1](#about-this-guide)
    3.  [SECTION 508 OF THE REHABILITATION ACT OF 1973 1](#section-508-of-the-rehabilitation-act-of-1973)
    4.  [DOCUMENT CONVENTIONS 1](#document-conventions)
    5.  [REFERENCED DOCUMENTS 2](#referenced-documents)
2.  [BEFORE BEGINNING THE UPDATE 3](#before-beginning-the-update)
    1.  [VERIFY WORKSTATION CONFIGURATION 3](#verify-workstation-configuration)
    2.  [CHECK SERVER REQUIREMENTS (THIN CLIENT ENVIRONMENTS—YOU MAY DO THIS LATER) 4](#check-server-requirements-thin-client-environmentsyou-may-do-this-later)
    3.  [INSTALL FLEX SCRIPTS ON JAWS USERS’ MACHINES (YOU MAY DO THIS LATER) 4](#install-flex-scripts-on-jaws-users-machines-you-may-do-this-later)
3.  [POST INSTALLATION – URL ACCESS 4](#post-installation-url-access)
    1.  [PRODUCTION URL – USAGE 4](#production-url-usage)
    2.  [PRE-PRODUCTION URL – USAGE 6](#pre-production-url-usage)
4.  [ACRONYMS 7](#acronyms)
> FIGURES
[FIGURE 1: THE CREATE SHORTCUT DIALOG BOX 5](#redacted-figure-1-the-create-shortcut-dialog-box)
[FIGURE 2: THE SELECT A TITLE FOR THE PROGRAM DIALOG BOX. 6](#create-shortcut-screen-2.figure-2-the-select-a-title-for-the-program-dialog-box.)
TABLES

# Product Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The fundamental mission of Department of Veterans Affairs (VA), Office of Information & Technology (OI&T), Emergency Department Integration Software (EDIS) Program Services is to provide Veterans the benefits they have earned throughout their military service to the United States. OI&T accomplishes its mission by delivering high-quality, client-centered, effective and efficient Information Technology (IT) services to those responsible for providing care to the Veterans at the point-of-care as well as throughout all the points of the Veterans’ health care in an effective, timely and compassionate manner. VA depends on Information Management/Information Technology (IM/IT) systems to meet mission goals.

> The VHA Health Workflow System (HWS). (HWS) Initiative is a single initiative whose mission is to expand health care access for Veterans, including women and rural populations. Multiple programs and projects have been assigned as part of the HWS Initiative, including EDIS.

> The system is an extension to Veterans Health Information Systems and Technology Architecture / Computerized Patient Record System (VistA/CPRS) for tracking and managing the delivery of care to patients in an Emergency Department (ED). The system provides - Recording and tracking Emergency Department patients during incidents of care - Display of the current state of care delivery - Reports and data extracts on the delivery of care. The system can be configured to specifics of different Veterans Health Administration (VHA) Emergency Departments.

## Recommended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This guide provides information specifically for Department of Veterans Affairs Medical Center (VAMC) information resource management (IRM) staff.

## About this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This installation guide provides instructions for installing application components that run on M servers at VAMC facilities. It also provides instructions for performing post-installation tasks—including configuration tasks—that require knowledge of the underlying VistA system.

## Section 508 of the Rehabilitation Act of 1973

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Portable Document File (PDF) version of this guide supports assistive reading devices such as: Job Access with Speech (JAWS).

## Document Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Bold type indicates application elements (views, panes, links, buttons, prompts, and text boxes, for example) and keyboard key names.

> Keyboard key names appear in angle brackets \<\>.

> *Italicized* text indicates special emphasis or user responses. ALL CAPS indicates M routines, parameters, and option names.

> Dot-dash-dot boarders indicate excerpted text (from other documents or from applications).

## Referenced Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following documents are available on the VistA Documentation Library (VDL), which is located at [<u>http://www.va.gov/vdl/application.asp?appid=179</u>](http://www.va.gov/vdl/application.asp?appid=179) :

- EDIS Client Installation Guide
- EDIS Server Installation Guide
- IRM Big Board Installation Guide
- EDIS User Manual
- EDIS Glossary
- EDIS Technical Manual

> From the ANONYMOUS software directories:

> OIFO FTP Address Directory

- • <span class="mark">REDACTED</span>

### Table 1: Documentation Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Title</strong></th>
<th><strong>File Name</strong></th>
<th><strong>FTP Mode</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EDP_2_1_1_SrvrIG.PDF</td>
<td><p>Emergency Department Integration Software Version</p>
<p>2.1.1 Server Installation Guide</p></td>
<td>Binary</td>
</tr>
<tr class="even">
<td>EDP_2_1_1_TM.PDF</td>
<td><p>Emergency Department Integration Software Version</p>
<p>2.1.1 Technical Manual</p></td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>EDP_2_1_1_UM.PDF</td>
<td>Emergency Department Integration Software Version2.1.1 User Manual</td>
<td>Binary</td>
</tr>
<tr class="even">
<td>EDP_2_1_1_ClientIG.PDF</td>
<td>Emergency Department Integration Software Version2.1.1 Client Installation Guide</td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>EDP_2_1_1_BigBoardIG.PDF</td>
<td>Emergency Department Integration Software Version2.1.1 IRM Big Board Installation Guide</td>
<td>Binary</td>
</tr>
<tr class="even">
<td>EDP_2_1_1_Glossary.PDF</td>
<td>Emergency Department Integration Software Version2.1.1 Glossary</td>
<td>Binary</td>
</tr>
</tbody>
</table>

# Before Beginning the Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Verify Workstation Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> EDIS runs in Adobe Flash Player, which runs in a Web browser. EDIS has been tested with Internet Explorer 7 and 9, as well as Firefox 8 or greater for Mac OS X. Since this is an update it is likely the correct version of Flash Player is already running on many users’ workstations. If a workstation lacks the Flash Player 11 plug-in, you must install it.

> To check the version of Flash Player that is installed on a workstation, open a browser on the workstation and point it to: [<u>http://www.adobe.com/products/flash/about/</u>](http://www.adobe.com/products/flash/about/). The browser will display the version of Flash Player (if any) that is currently installed.

> To install Flash Player on a workstation:

- Log into the workstation with administrative access.
- Point the workstation’s browser to [<u>http://www.adobe.com/go/getflashplayer</u>](http://www.adobe.com/go/getflashplayer).
- Click Download Now to download the installer.
- Close all browser windows.
- Double-click the installer icon (usually named something like install_flash_player.exe).
- Follow the onscreen prompts. The installation will complete in a few seconds. You will not need to restart the machine.

### Flash Player: Minimum Requirements for Microsoft Windows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Browser Requirements for Flash Player 10.x or greater

### Table 2: Requirements for Microsoft Windows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Platform</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Browser</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Windows XP</p>
</blockquote></td>
<td><blockquote>
<p>Internet Explorer 7.0 or later</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Windows 7</p>
</blockquote></td>
<td><blockquote>
<p>Internet Explorer 8.0 or later</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Flash Player: Minimum Requirements for Apple Mac OS

> Browser Requirements for Flash Player 10.x or greater

### Table 3: Requirements for Apple MacOS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Platform</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Browser</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Mac OS X 10.5 or Mac OS X 10.6</p>
</blockquote></td>
<td><blockquote>
<p>Firefox 8.<em>x</em> or later, Safari 5.<em>x</em> or later</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Mac OS 10.7</p>
</blockquote></td>
<td><blockquote>
<p>Firefox 8.<em>x</em> or later, Safari 5.<em>x</em> or later</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Check Server Requirements (Thin Client Environments—You May Do This Later)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If your site has a thin-client environment, make sure that Flash Player is up to date on all servers.

> If your thin-client environment includes roaming profiles, use the following URL to preselect your site and disable site-selection on the EDIS login screen: REDACTED

> For example, if your institution number is 999, you would use this URL:

REDACTED

## Install Flex Scripts on JAWS Users’ Machines (You May Do This Later)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> While you are at users’ workstations, you may also want to download and install Adobe Flex accessibility scripts for users who rely on Job Access with Speech (JAWS). These scripts enable JAWS users to employ the standard keyboard shortcut to enter Forms mode on EDIS interface controls.

> Download JAWS scripts for Flex 3 (an executable file) at [<u>http://www.adobe.com/accessibility/products/flex/jaws.html</u>.](http://www.adobe.com/accessibility/products/flex/jaws.html)

# Post Installation – URL Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once the installation updates have been completed, new URLs need to be installed for EDIS v2 users. There will be 2 URLs. One URL is to access the test/mirror account system for your site. This is connected to the preproduction environment of EDIS. The second URL is the production system URL. Follow VA and site procedures when granting user access.

## Production URL – Usage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> While at users’ workstations, create shortcuts to EDIS software. The URL for the EDISv2 production server is: REDACTED

> *Note: If you want to preselect your site on the EDIS login screen and disable users’ ability to select another site, use this URL:*

> *https://vaww.edis2.med.va.gov/main/tracking.html?kaajeeDefaultInstitution=\[ your institution number\]&kaajeeDisableInstitutionComponents=true. (For example, if your institution number is XXX, the URL you should use is https://vaww.edis.med.va.gov/main/tracking.html?kaajeeDefaultInstitution=X XX&kaajeeDisableInstitutionComponents=true.)*

> To create a shortcut on users’ desktops:

1.  Right click the desktop and select New and then select Shortcut.
2.  Type the URL [(h](http://vaww.edis2.med.va.gov/main))t[tp://vaww.edis2.med.va.gov/main)](http://vaww.edis2.med.va.gov/main)) in the Type the location of the item

> box and then click Next. A screen similar to the one below, is what you shall see:

### REDACTED Figure 1: The Create Shortcut dialog box

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

3.  Type a name for the shortcut in the Type a name for this shortcut box and click Finish to place the shortcut on the desktop.

### ![](emergency-dept-integration-software-edis-version-2-1-1-increment-3-client-instal/002.png)Figure 2: The Select a Title for the Program dialog box.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-Production URL – Usage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Access the following URL for training purposes: [<u>https://preprod.edis2.med.va.gov/main/</u>](http://preprod.edis2.med.va.gov/main/)

> Note: that the pre-production URL shall be used for connecting Test Account to sites.

# Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym | Definition                              |
|-------------|---------------------------------------------|
| AITC        | Austin Information Technology Center        |
| CAC         | Clinical Application Coordinator            |
| CRDC        | Capital Region Data Center                  |
| CPRS        | Computerized Patient System Records         |
| EARS        | Enterprise Archives                         |
| ED          | Emergency Department                        |
| EDIS        | Emergency Department Integration Software   |
| EIE         | Enterprise Infrastructure Engineering       |
| EMFAC       | Emergency Medicine Field Advisory Committee |
| ESM         | Enterprise Systems Management               |
| iaw         | In accordance with                          |
| IOC         | Independent Out-Patient Clinics             |
| IP          | Internet Protocol                           |
| IRM         | information resource management             |
| ISP         | Internet Service Provider                   |
| KIDS        | Kernel Installation and Distribution System |
| NSR         | New Service Request                         |
| OED         | Office of Enterprise Development            |
| OI          | Office of Information                       |
| OMB         | Office of Management and Budget             |
| PITC        | Philadelphia Information Technology Center  |
| PMAS        | Program Management Accountability System    |
| PWS         | Performance Work Statement                  |
| QA          | Quality Assurance                           |
| RQM         | Rational Quality Manager                    |
| RR          | Risk Register                               |
| SCM         | Software Configuration Management           |
| TRRB        | Team Risk Review Board                      |
| TWG         | Technical Working Group                     |
| VA          | Veterans Affairs                            |
| Acronym | Definition                                                  |
|-------------|-----------------------------------------------------------------|
| UAT         | User Acceptance Test                                            |
| VHA         | Veterans Health Administration                                  |
| VISN        | Veterans Integrated Services Network                            |
| VistA       | Veterans Health Information Systems and Technology Architecture |
| VOB         | Version Object Base                                             |
| VM          | Virtual Machine                                                 |
| WBS         | Work Breakdown Structure                                        |
