---
title: Emergency Dept Integration Software GUI (EDIS) Version 2.1.2 Server and Client Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: Server and Client
app_code: EDIS
app_name: Emergency Department Integration Software
section: CLI
app_status: archive
pkg_ns: EDIS
patch_ver: 2.1.2
patch_id: EDIS*2.1.2
group_key: "EDIS:EDIS:2.1.2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - edis
  - prompt
  - press
  - installation
  - class
  - server
  - emergency
  - span
page_count: 0
word_count: 3321
section_count: 20
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Emergency_Dept_Integration_Software_Archive/edis_2_1_2_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Emergency_Dept_Integration_Software_Archive/edis_2_1_2_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=358"
---

Department of Veterans AffairsEmergency Department Integration Software (EDIS)Server and Client Installation Guide

![](emergency-dept-integration-software-gui-edis-version-2-1-2-server-and-client-ins/001.png)

VistA EDP\*2.0\*2GUI EDIS Version 2.1.2November 2014Document Version 1.0

Office of Information and Technology (OI&T)

Product Development

Document Revision History

<table>
<caption><p><span id="_Toc403558526" class="anchor"></span>Table 1: ANONYMOUS Software Directories</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 56%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Document Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11/05/2014</td>
<td>1.0</td>
<td><p>EDIS v.2.1.2. Initial Document.</p>
<p>This document combines the former EDIS Server Guide (document version 3.3) with the former EDIS Client Installation Guide (document version 3.6) and adds updates for EDIS software version 2.1.2. In addition to revised installation instructions and document formatting changes, the following changes were also made:</p>
<ul>
<li><p>Removed Security Key EDPR PROVIDER (previously used for Provider Report) from Section 3.5 Keys for EDIS Users.</p></li>
<li><p>Updated EDIS URL.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

<span id="_Toc403558526" class="anchor"></span>Table 1: ANONYMOUS Software Directories

Table of Contents

List of Tables

List of Figures

> **NOTE:** This document combines two previously published EDIS installation guides, EDIS Server Installation Guide version 3.3 and EDIS Client Installation Guide version 3.6, into a single document; the previous documents are hereby rescinded.

# Overview


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Overview](#overview)
  - [Patch Overview](#patch-overview)
    - [Installation Sequence and Coordination](#installation-sequence-and-coordination)
  - [About this Guide](#about-this-guide)
    - [Section 508 of the Rehabilitation Act of 1973](#section-508-of-the-rehabilitation-act-of-1973)
    - [Document Conventions](#document-conventions)
  - [Recommended Audience](#recommended-audience)
- [Referenced Documents and Files](#referenced-documents-and-files)
- [PART I: VISTA SERVER INSTALLATION GUIDE](#part-i-vista-server-installation-guide)
- [Before Beginning the Update](#before-beginning-the-update)
  - [Changes to EDIS Web-based Application](#changes-to-edis-web-based-application)
  - [Retrieve patch EDP\2.0\2](#retrieve-patch-edp202)
  - [Check VistA Software Requirements](#check-vista-software-requirements)
- [Installing M Server Components](#installing-m-server-components)
  - [Install patch EDP\2.0\2](#install-patch-edp202)
  - [Updated Routines](#updated-routines)
- [EDIS Configuration](#edis-configuration)
  - [EDPF LOCATION Parameter](#edpf-location-parameter)
  - [EDPF NURSE STAFF SCREEN Parameter](#edpf-nurse-staff-screen-parameter)
  - [Creating an EDIS Proxy User for VistALink](#creating-an-edis-proxy-user-for-vistalink)
  - [Assign Options for Emergency Department Users](#assign-options-for-emergency-department-users)
  - [Keys for EDIS Users](#keys-for-edis-users)
- [Configure EDIS to work with other Applications](#configure-edis-to-work-with-other-applications)
  - [Configure EDIS to Work with Omnicell](#configure-edis-to-work-with-omnicell)
- [PART II: CLIENT INSTALLATION GUIDE](#part-ii-client-installation-guide)
- [Before Beginning the Update](#before-beginning-the-update-1)
  - [Verify Workstation Configuration](#verify-workstation-configuration)
  - [Check Server Requirements](#check-server-requirements)
  - [Install Flex Scripts on JAWS Users’ Machines](#install-flex-scripts-on-jaws-users-machines)
- [Post Installation of EDIS v.2.1.2/EDP\2.0\2 – URL Access](#post-installation-of-edis-v212edp202-url-access)
  - [Production URL – Usage](#production-url-usage)
  - [Pre-Production URL – Usage](#pre-production-url-usage)
- [Acronyms](#acronyms)
> The fundamental mission of Department of Veterans Affairs (VA), Office of Information & Technology (OI&T), Emergency Department Integration Software (EDIS) Program Services is to provide Veterans the benefits they have earned throughout their military service to the United States. OI&T accomplishes its mission by delivering high-quality, client-centered, effective and efficient Information Technology (IT) services to those responsible for providing care to the Veterans at the point-of-care as well as throughout all the points of the Veterans’ health care in an effective, timely and compassionate manner. VA depends on Information Technology (IT) systems to meet mission goals.
> The VHA Health Workflow System (HWS) Initiative is a single initiative whose mission is to expand health care access for Veterans, including women and rural populations. Multiple programs and projects have been assigned as part of the HWS Initiative, including EDIS.
> The system is an extension to Veterans Health Information Systems and Technology Architecture (VistA) Computerized Patient Record System (CPRS) for tracking and managing the delivery of care to patients in an Emergency Department (ED). The system provides:
- Recording and tracking Emergency Department patients during incidents of care.
- Display of the current state of care delivery.
- Reports and data extracts on the delivery of care.
> The system can be configured specifically for different Veterans Health Administration (VHA) Emergency Departments.

## Patch Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> EDIS patch EDP\*2.0\*2 and associated files accommodate the introduction of International Classification of Diseases, Tenth Revision (ICD-10). In addition, the patch includes the following fixes:

- EDIS will now allow a user to remove a patient without selecting a Provider for the following special classes of Disposition:
- Left without being treated
- Patient name entered in error
- Sent to primary care
- Nurses and Resident roles now correctly open the Edit Closed worksheet.
- Selecting the first bed in the list of the Visit worksheet no longer brings up a 'Missing Bed' popup when clicking on the "Save" button.
- The Provider report has been removed from EDIS.
- After a user switches from viewing an Edit Closed worksheet to editing and saving a Visit worksheet, the Visit worksheet no longer blanks out.

### Installation Sequence and Coordination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are four parts to the EDIS 2.1.2 (EDP\*2.0\*2) installation.

1.  Installation of edis-tracking-application-2.1.2.ear file on Oracle Weblogic Application Server by Enterprise Operations. This step has been completed.
2.  Installation of EDP\*2.0\*2 on the site’s VistA server.
3.  Update the URL on all the site’s client/user workstations.
4.  Update the URL for the site’s EDIS Big Board. Refer to the EDIS v.2.1.2 Big Board Installation Guide (see Section 2 below for location of Referenced Documents).

> NOTE: Step 1 above has been completed by Enterprise Operations. Step 2 should immediately be followed by Steps 3 and 4 at the site.

## About this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This Installation Guide pertains to EDIS v.2.1.2 (EDP\*2.0\*2). This guide provides instructions for installing application components that run on M servers at VAMC facilities. It also provides instructions for performing post-installation tasks, including configuration tasks, that require knowledge of the underlying VistA system.

> This document combines two previously published EDIS installation guides, EDIS Server Installation Guide version 3.3 and EDIS Client Installation Guide version 3.6, into a single document; the previous documents are hereby rescinded.

### Section 508 of the Rehabilitation Act of 1973

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Portable Document File (PDF) version of this guide supports assistive reading devices such as: Job Access with Speech (JAWS).

### Document Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Document conventions include:

- Bold type indicates application elements (e.g. views, panes, links, buttons, prompts, and text boxes) and keyboard key names.
- Keyboard key names appear in angle brackets \< \>.
- *Italicized* text indicates special emphasis or user responses.
- ALL CAPS indicate M routines, parameters, and option names.

## Recommended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This guide provides information specifically for Department of Veterans Affairs Medical Center (VAMC) information resource management (IRM) staff to facilitate the ability to install and configure their systems to run EDIS.

# Referenced Documents and Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following documents and files are available on the Anonymous software directories identified in the table below:

- EDIS v.2.1.2 Server and Client Installation Guide
- EDIS v.2.1.2 Big Board Installation Guide
- EDIS v.2.1.2 Release Notes
- EDIS v.2.1.2 Technical Manual
- EDIS v.2.1.2 User Guide
- EDIS Glossary
- EDIS Installation Package Zip File (contains Launch_EDIS.bat and edisautologon.reg)

> The documents (except the zip file) are also available on the VistA Documentation Library (VDL), which is located at <http://www.va.gov/vdl/application.asp?appid=179>.

| OIFO                | FTP Address                                                          | Directory                                                            |
|---------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| Albany              | [<span class="mark">REDACTED</span>](ftp://ftp.fo-albany.med.va.gov) | [<span class="mark">REDACTED</span>](ftp://ftp.fo-albany.med.va.gov) |
| Hines               | [<span class="mark">REDACTED</span>](ftp://ftp.fo-albany.med.va.gov) | [<span class="mark">REDACTED</span>](ftp://ftp.fo-albany.med.va.gov) |
| Salt Lake City      | [<span class="mark">REDACTED</span>](ftp://ftp.fo-albany.med.va.gov) | [<span class="mark">REDACTED</span>](ftp://ftp.fo-albany.med.va.gov) |
| VistA Download Site | [<span class="mark">REDACTED</span>](ftp://ftp.fo-albany.med.va.gov) | [<span class="mark">REDACTED</span>](ftp://ftp.fo-albany.med.va.gov) |

<span id="_Toc403558527" class="anchor"></span>Table 2: Document Files

> The documents appear on the Anonymous software directories under the file names listed in the table below.

<table style="width:100%;">
<caption><p><span id="_Toc403558528" class="anchor"></span>Table 3: Updated Routines</p></caption>
<colgroup>
<col style="width: 65%" />
<col style="width: 25%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name</th>
<th>Title</th>
<th>FTP Mode</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EDIS_2_1_2_IG.PDF</td>
<td>Emergency Department Integration Software Version 2.1.2 Server and Client Installation Guide</td>
<td>Binary</td>
</tr>
<tr class="even">
<td>EDIS_2_1_2_BigBrd_IG.PDF</td>
<td>Emergency Department Integration Software Version 2.1.2 Big Board Installation Guide</td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>EDIS_2_1_2_RN.PDF</td>
<td>Emergency Department Integration Software Version 2.1.2 Release Notes</td>
<td>Binary</td>
</tr>
<tr class="even">
<td>EDIS_2_1_2_TM.PDF</td>
<td>Emergency Department Integration Software Version 2.1.2 Technical Manual</td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>EDIS_2_1_2_UG.PDF</td>
<td>Emergency Department Integration Software Version 2.1.2 User Guide</td>
<td>Binary</td>
</tr>
<tr class="even">
<td>EDIS_2_1_2_Glossary.PDF</td>
<td>Emergency Department Integration Software Glossary</td>
<td>Binary</td>
</tr>
<tr class="odd">
<td><p>EDP2_1_1.zip</p>
<p><strong>NOTE:</strong> The zip file and its contents have NOT been updated for the EDIS v.2.1.2/EDP*2.0*2 release. The file is included with the latest release documentation for ease of reference but is still named for the release in which it was last modified (EDIS v.2.1.1/EDP*2.0*6).</p></td>
<td>Emergency Department Integration Software Installation Package Zip File</td>
<td>Binary</td>
</tr>
</tbody>
</table>

<span id="_Toc403558528" class="anchor"></span>Table 3: Updated Routines

# PART I: VISTA SERVER INSTALLATION GUIDE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Before Beginning the Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  
2.  

## Changes to EDIS Web-based Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The EDIS application is a web-based application which contains both a java/WebLogic (EDIS v.2.1.2) component and an M patch (EDP\*2.0\*2) component. EDIS v.2.1.2 java code (edis-tracking-application-2.1.2.ear) is already deployed and is managed by Enterprise Operations using Oracle WebLogic Application Server.

> NOTE: EDP\*2.0\*2 is NOT backward compatible with previous EDIS java code releases. Installation of EDP\*2.0\*2 should be immediately followed by updates to all client and Big Board URLs so that they use the EDIS v.2.1.2 Oracle WebLogic Application Server.

> EDIS v.2.1.2 Oracle WebLogic Application Server is currently available for connection at the new URL: <https://vaww.edisprod2.med.va.gov>.

## Retrieve patch EDP\*2.0\*2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> EDP\*2.0\*2 is a FORUM patch and will be pushed to the IRMs by Product Support. Once you have been notified that the patch has been pushed, you can retrieve and extract the patch from Mail Manager.

## Check VistA Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> EDIS uses the following packages, which must be installed and fully patched in your accounts:

- LEX\*2\*80
- ICD\*18\*57
- PX\*1.0\*199
- EDP\*2.0\*6

# Installing M Server Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Install patch EDP\*2.0\*2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Follow these instructions to install EDIS v.2.1.2 (EDP\*2.0\*2). This patch should be installed during a period of low system activity with EDIS users off the system. No options need to be placed out of service. Installation time is expected to be less than 5 minutes.

> NOTE: Coordination of the M server installation must be synchronized with the update of the EDIS URL; see Part II, section 2, below for client instructions. For Big Board instructions, refer to the EDIS v.2.1.2 Big Board Installation Guide (see section 2 above for location of Referenced Documents).

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation Menu. From this menu, you may elect to use the following option. When prompted for the INSTALL enter the patch \#(ex.EDP\*2.0\*2):
1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  From the Installation Menu, select the Install Package(s) option and choose the patch to install. Enter EDP\*2.0\*2.
5.  If prompted ‘Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//’, answer ‘NO’.
6.  When prompted ‘Want KIDS to INHIBIT LOGONs during the install? NO//’, answer ‘NO’.
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, answer ‘NO’.
8.  If prompted “Delay Install (Minutes): (0 – 60): 0//’, respond ‘0’.

## Updated Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The routines listed in the table below were updated in patch EDIS v.2.1.2/EDP\*2.0\*2.  The checksums listed in the “After Checksum” column are new checksums and can be checked with CHECK1^XTSUMBLD.

| Routine Name | Before Checksum | After Checksum |
|--------------|-----------------|----------------|
| EDP22PST     | N/A             | 737172         |
| EDPCONV      | 69787121        | 70928886       |
| EDPFAA       | 36904209        | 37763699       |
| EDPFLEX      | 1745474         | 10693270       |
| EDPLEX       | N/A             | 11049187       |
| EDPLOG       | 58048189        | 64279489       |
| EDPLPCE      | 32808524        | 39952113       |
| EDPQLE       | 43232281        | 55054483       |
| EDPQPCE      | 3317665         | 6816999        |
| EDPRPT1      | 50357723        | 51586751       |
| EDPRPT10     | 30220543        | 32122849       |
| EDPRPT2      | 24332800        | 26475007       |
| EDPRPT7      | 20666458        | 23000869       |
| EDPRPT7C     | 22153636        | 24197469       |
| EDPRPTBV     | 28273730        | 30889629       |
| EDPX         | 12709600        | 16354064       |

<span id="_Toc398900504" class="anchor"></span>Table 4: Browser Requirements for Flash Player

# EDIS Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTE: EDIS v.2.1.2/EDP\*2.0\*2 installation does NOT affect any of the parameters/options described in this section. Configuration information is included below for reference purposes only. Configuration may be needed if installing EDIS for the first time, but it is not necessary to perform these configuration steps if updating an existing EDIS system to v.2.1.2/EDP\*2.0\*2.

## EDPF LOCATION Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This parameter should contain the hospital location or locations that your emergency department uses. If you have a multi-division site, make an entry for each division.

1.  Log in to VistA.
2.  At the Select OPTION NAME prompt, type *xpar menu* (for XPAR MENU TOOLS) and then press the \<Enter\> key.
3.  At the Select General Parameter Tools Option prompt, type *ep* (for Edit Parameters) and then press the \<Enter\> key.
4.  At the Select PARAMETER DEFINITION NAME prompt, type *edpf l* (*EDPF L*; for EDPF LOCATION) and then press the \<Enter\> key.
5.  At the Select INSTITUTION NAME prompt, type the name or station number of your institution and then press the \<Enter\> key.
6.  At the Select Time Range (ex. 0800-1200) or Sequence prompt, type the time range during which the clinic location you are about to select functions as your site’s emergency department. Use military time. For example, if the location serves as your site’s emergency department from 8:00 AM to 5:00 PM, type *0800-1700*. Alternately, type a number that represents the location’s preference rating (the number *1* represents the most-preferred location). Press the \<Enter\> key. When users create a PCE encounter, EDIS uses time-of-day-based or preference-based criteria to determine the encounter’s location.

> NOTE: When selecting time ranges, be sure to account for all hours of emergency-department operation. EDIS does not create PCE encounters for patients whom users enter during times that you do not include in the EDPF LOCATION parameter. For example, suppose you set the parameter to use Clinic A from 0700 to 0800 hours and Clinic B from 0900 to 1200 hours. If a user then adds a patient at 0830 hours, EDIS will not create a PCE encounter for the patient. Further, take care not to overlap hours. In cases where hours overlap, EDIS always creates the patient’s PCE encounter for the first clinic.

> EDIS uses the time and preference settings you specify here to populate its Clinic list when you select the Show clinics on entry form check box in the application’s Configure view. This parameter allows users at sites that have multiple emergency-department locations to select the location EDIS will use when it creates the patient’s emergency-department visit in CPRS.

7.  VistA displays your new time range or selection as a default value. Press the \<Enter\> key to accept this default value.
8.  At the ED LOCATION prompt, type the name of the location that serves as your site’s emergency department during this time range or for this sequence and press the \<Enter\> key.
9.  Repeat steps 6 through 8 for additional emergency-department locations (if any).

## EDPF NURSE STAFF SCREEN Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The EDPF NURSE STAFF SCREEN parameter allows you to select the type of filtering EDIS uses to populate the nursing-staff selection list in its Assign Staff view. By default, the application allows all entries in the New Person (#200) file. Options for narrowing the list of possible staff selections include:

- Allow only persons who are present and active in the NURS STAFF file (#210)
- Allow only persons who hold the ORELSE key
- Allow only persons who hold the PSJ RNURSE key
- Allow selection from all entries in the New Person file (#200)
1.  Log in to VistA
2.  At the Select OPTION NAME prompt, type *xpar menu* (for XPAR MENU TOOLS) and then press the \<Enter\> key.
3.  At the Select OPTION NAME prompt, type *xpar edit parameter* and press the \<Enter\> key.
4.  At the Select PARAMETER DEFINITION NAME prompt, type *edpf nurse staff* and press the \<Enter\> key.
5.  At the Enter selection prompt, type the number *3* (for Division) and press the \<Enter\> key. If your site has only one division, you can set this parameter at the system level by typing the number *5* (for System).
6.  At the Select INSTITUTION NAME prompt, type your institution’s name and then press the \<Enter\> key. VistA displays a list of criteria that EDIS can use to filter entries in the New Person (#200) file.
7.  At the Allow Persons prompt, type one of the following numbers to select a screening criterion and then press the \<Enter\> key:
    - *0* (Active in NURS STAFF (210)
    - *1* (Hold ORELSE Key)
    - *2* (Hold PSJ RNURSE Key)
    - *3* (All Persons (No Screen))

## Creating an EDIS Proxy User for VistALink

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTE: For more information on how to configure and use VistALink, refer to VistALink documentation on the VDL: <http://www.va.gov/vdl/application.asp?appid=163>.

> The EDIS Version 1 Installation Guide included the following steps to create an EDIS proxy user called *CONNECTOR, EDIS*. This information is included here for reference purposes.

> *Create a Connector Proxy M Account*

> *If your site has not created a VistALink connector proxy, use the Kernal Tool’s Foundations Manager menu to create the Connector Proxy M Account.*

1.  *On the Foundations Manager main page, select CP Enter/Edit Connector Proxy User.*

<span id="_Toc403558531" class="anchor"></span>Figure 1: Foundations Manager Menu

![](emergency-dept-integration-software-gui-edis-version-2-1-2-server-and-client-ins/002.png)

2.  *At the Enter NPF CONNECTOR PROXY name prompt, type CONNECTOR, EDIS.*

> To verify or update your site’s VistALink Listener:

1.  Check the Status of your site’s VistALink Listener using the FOUNDATION menu option.
2.  If you need to change any of the information below, submit a Remedy ticket to the VA National Service Desk – Tuscaloosa.

> NOTE: Do not include restricted information in the Remedy ticket. It is VA Policy to send this information securely via public key infrastructure (PKI) message. Securely send this information for both the VistALink connector on your test VistA system and the VistALink connector on your production VistA system.

1.  The DNS for your site’s VistA server (i.e. ecp.vista.med.va.gov)
2.  The port number of your site’s VistALink Listener (i.e. 18123)
3.  The access code for the VistALink connector (i.e. 1234abc)
4.  The verify code for the VistALink connector (i.e. 5678abc!)

## Assign Options for Emergency Department Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You must assign to users and clinical application coordinators (CACs) at least one of the following secondary menu options.

> The EDIS project team recommends working with your site’s emergency-department administrative and IT staff to determine which users should receive which menu options.  For a complete listing of EDIS options, refer to the EDIS v.2.1.2 Technical Manual, Section 7 (see Section 2, Referenced Documents and Files, above).

1.  EDPF TRACKING MENU ALL – Provides access to all EDPF TRACKING VIEW options.
    1.  CPE
    2.  Configure
    3.  Edit Closed
    4.  Assign Staff
    5.  Reports
    6.  Display Board
2.  EDPF TRACKING MENU CLINICAN – Provides access to the CPE views; includes the ability to remove patients from the board and provides access to the following data-entry fields:
    1.  Room/Area
    2.  Status
    3.  Provider, Residents and Nurse staff-assignment lists
    4.  Comments
    5.  Disposition
    6.  Delay Reason (if the Delay reason is required…parameter is enabled)
    7.  Diagnosis

> There are additional secondary menu options that may need to be assigned to allow specific users to perform additional tasks:

1.  EDPF TRACKING VIEW CONFIGURE – Provides access to the Configure view, which includes the ability to configure rooms and areas, colors, one or multiple display boards, site-configurable parameters, and the contents of application pick lists.
2.  EDPF TRACKING VIEW EDIT CLOSED – Provides access to the Edit Closed view, which includes the ability to edit all data-entry fields for closed visits; the EDIS project team recommends limiting access to this view.
3.  EDPF TRACKING VIEW REPORTS – Provides access to the Reports view, which includes the ability to run administrative reports; separate keys control user access to export and print privileges, and to limited-access reports (see Section 3.5 below).
4.  EDPF TRACKING VIEW STAFF – Provides access to the Assign Staff view, which offers the ability to update physician-, resident-, and nursing-staff pick lists.

> To reiterate, work with your site’s IT staff and emergency-department managers to gather a list of EDIS users and determine which views each user needs. Assign to each user only views he or she needs.

> To assign options to a user:

1.  Log in to VistA.
2.  At the Select OPTION NAME prompt, type EVE and then press the \<Enter\> key.
3.  From the Choose 1-5 prompt, type the number 1 (for EVE Systems Manager Menu) and press the \<Enter\> key.
4.  From the Select Systems Manager Menu Option prompt, type User Management and press the \<Enter\> key.
5.  From the Select User Management Option prompt, types edit (for Edit an Existing User) and press the \<Enter\> key.
6.  From the Select NEW PERSON NAME prompt, type the user’s name using the following format: lastname, firstname. Press the \<Enter\> key.
7.  Press the \<Down Arrow\> key to highlight the Select SECONDARY MENU OPTIONS field. (Type a question mark (?) to see a list of the secondary options that are currently assigned to the user.)
8.  In the SECONDARY MENU OPTIONS field, type one of the options listed above and then press the \<Enter\> key.
9.  From the Are you adding …as a new SECONDARY MENU OPTIONS (the…for this NEW PERSON)? No// prompt, type Yes and press the \<Enter\> key.
10. Press the \<Enter\> key again to accept this new option.
11. In the SYNONYM field, type a synonym for the option (optional). Press the \<Enter\> key.
12. Press the \<Enter\> key to close the COMMAND field and return to the Select SECONDARY MENU OPTIONS field.
13. Repeat steps 6 through 12 to assign other options as necessary.
14. Press the \<Down Arrow\> key to move through the Edit Existing User dialog. At the end of each page, type the letter n in the COMMAND field to enter the following page.
15. Stop on page 3.
16. Check the user’s person class, which appears on page 3, to make sure the user’s person class is active.

> NOTE: The active person class is only needed for the Providers.

17. If the user’s person class is not active, select an active person class for the user.
18. When you have entered all applicable secondary menu options and verified that the user has an active person class, type the word Exit in the COMMAND field.
19. From the Save changes before leaving form (Y/N)? prompt, type the letter Y and press the \<Enter\> key.

## Keys for EDIS Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Assign keys for users who need access to additional reporting capabilities. The following keys are available:

- EDPR EXPORT enables the export option for EDIS reports
- EDPR XREF provides access to the Patient XRef (cross reference) report, which associates patients’ emergency department visit numbers with their patient IDs
1.  Log in to VistA.
2.  At the Select OPTION NAME prompt, type *eve* and then press the \<Enter\> key.
3.  At the Choose 1-5 prompt, type the number *1* (for EVE Systems Manager Menu) and then press the \<Enter\> key.
4.  At the Select Systems Manager Menu Option prompt, type *menu* (for Menu Management) and then press the \<Enter\> key.
5.  At the Select Menu Management Option prompt, type the word *key* (for Key Management) and then press the \<Enter\> key.
6.  At the Select Key Management Option prompt, type the word *allocation* (for Allocation of Security Keys). Press the \<Enter\> key.
7.  At the Allocate key prompt, type the name of the security key you want to assign—*EDPF EXPORT*, for example. Press the \<Enter\> key.
8.  At the Holder of key prompt, type the name of the first user to whom you are assigning the key and then press the \<Enter\> key.
9.  At the Another holder prompt, type the name of a second user to whom you are assigning the key and then press the \<Enter\> key. Repeat this step for all users to whom you are assigning the key.
10. At the You are allocating keys. Do you wish to proceed? YES// prompt, press the \<Enter\> key to accept the default response.

# Configure EDIS to work with other Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Configure EDIS to Work with Omnicell

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If your site wants EDIS to work with its Omnicell implementation, you must manually add the Omnicell event protocol (VEFS SDAM) to the EDIS EDP NEW PATIENT event. If you are already running EDIS, please review the below configuration to be certain nothing has changed.

1.  Open VA FileMan.
2.  At the Select OPTION prompt, type the number *1* (ENTER OR EDIT FILE ENTRIES).
3.  At the INPUT TO WHAT FILE prompt, type the word *protocol* (PROTOCOL).
4.  At the EDIT WHICH FIELD prompt, type the word *item*.
5.  At the CHOOSE 1–2 prompt, type the number *1* (ITEM (multiple)).
6.  At the EDIT WHICH ITEM SUB-FIELD prompt, press the \<Enter\> key to accept the default response (ALL).
7.  At the THEN EDIT FIELD prompt, press the \<Enter\> key without typing a response.
8.  At the Select PROTOCOL NAME prompt, type *EDP NEW PATIENT*.
9.  At the Select ITEM prompt, type *VEFS SDAM* (the Omnicell event protocol). You don’t need to respond to prompts for other fields in the ITEM multiple.

# PART II: CLIENT INSTALLATION GUIDE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Section 1 below is included for reference purposes only; this information may be needed if installing EDIS for the first time. If EDIS has already been set up on the workstation and is being updated to v.2.1.2/EDP\*2.0\*2, you may skip Section 1 and start with Section 2, Post Installation of EDIS v.2.1.2/EDP\*2.0\*2, below.

# Before Beginning the Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Verify Workstation Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> EDIS runs in Adobe Flash Player, which runs in a Web browser. EDIS has been tested with Internet Explorer 7 and 9, as well as Firefox 8 or greater for Mac OS X. Since this is an update it is likely the correct version of Flash Player is already running on many users’ workstations. If a workstation lacks the Flash Player 11 plug-in, you must install it.

> To check the version of Flash Player that is installed on a workstation, open a browser on the workstation and point it to: <http://www.adobe.com/products/flash/about/>. The browser will display the version of Flash Player (if any) that is currently installed.

> To install Flash Player on a workstation:

1.  Log into the workstation with administrative access.
2.  Point the workstation’s browser to <http://www.adobe.com/go/getflashplayer>.
3.  Click Download Now to download the installer.
4.  Close all browser windows.
5.  Double-click the installer icon (usually named something like install_flash_player.exe).
6.  Follow the onscreen prompts. The installation will complete in a few seconds. You will not need to restart the machine.

> Browser Requirements for Flash Player 10.x or greater are listed in the table below.

| Platform                       | Browser                                       |
|--------------------------------|-----------------------------------------------|
| Windows 7                      | Internet Explorer 8.0 or later                |
| Mac OS X 10.5 or Mac OS X 10.6 | Firefox 8.*x* or later, Safari 5.*x* or later |
| Mac OS 10.7                    | Firefox 8.*x* or later, Safari 5.*x* or later |

<span id="_Toc403558530" class="anchor"></span>Table 5: Acronyms

## Check Server Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTE: You may do this later for Thin Client Environments.

> If your site has a thin-client environment, make sure that Flash Player is up to date on all servers.

> If your thin-client environment includes roaming profiles, use the following URL to preselect your site and disable site-selection on the EDIS login screen: https://vaww.edisprod2.med.va.gov/main/tracking.html?kaajeeDefaultInstitution=

> *your institution number*&kaajeeDisableInstitutionComponents=true

> For example, if your institution number is 999, you would use this URL: <https://vaww.edisprod2.med.va.gov/main/tracking.html?kaajeeDefaultInstitution=999&kaajeeDisableInstitutionComponents=true>

## Install Flex Scripts on JAWS Users’ Machines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTE: You may do this later.

> While you are at users’ workstations, you may also want to download and install Adobe Flex accessibility scripts for users who rely on Job Access with Speech (JAWS). These scripts enable JAWS users to employ the standard keyboard shortcut to enter Forms mode on EDIS interface controls.

> Download JAWS scripts for Flex 3 (an executable file) at <http://www.adobe.com/accessibility/products/flex/jaws.html>

# Post Installation of EDIS v.2.1.2/EDP\*2.0\*2 – URL Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once the installation updates have been completed, new URLs need to be installed for EDIS v.2.1.2 users. There will be two URLs. One URL is to access the test/mirror account system for your site. This is connected to the preproduction environment of EDIS. The second URL is the production system URL. Follow VA and site procedures when granting user access.

## Production URL – Usage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> While at users’ workstations, create shortcuts to EDIS software. The URL for the EDIS production server is: [<u>https://vaww.edisprod2.med.va.gov/main</u>](https://vaww.edisprod2.med.va.gov/main)

> NOTE: If you want to preselect your site on the EDIS login screen and disable users’ ability to select another site, use this URL: https://vaww.edisprod2.med.va.gov/main/tracking.html?kaajeeDefaultInstitution=

> *your institution number*&kaajeeDisableInstitutionComponents=true

> For example, if your institution number is XXX, the URL you should use is: <https://vaww.edisprod2.med.va.gov/main/tracking.html?kaajeeDefaultInstitution=XXX&kaajeeDisableInstitutionComponents=true>

> To create a shortcut on users’ desktops:

1.  Right click the desktop and select New and then select Shortcut.
2.  Type the URL (<http://vaww.edisprod2.med.va.gov/main>) in the Type the location of the item box and then click Next. You will see a screen similar to the one in the figure below.

<span id="_Toc398900495" class="anchor"></span>Figure 2: The Create Shortcut dialog box

![](emergency-dept-integration-software-gui-edis-version-2-1-2-server-and-client-ins/003.png)

3.  Type a name for the shortcut in the Type a name for this shortcut box and click Finish to place the shortcut on the desktop.

<span id="_Toc398900496" class="anchor"></span>Figure 3: The Select a Title for the Program dialog box.

![](emergency-dept-integration-software-gui-edis-version-2-1-2-server-and-client-ins/004.png)

## Pre-Production URL – Usage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Access the following URL for training purposes: <https://preprod.edispreprod2.med.va.gov/main/>

> NOTE: The pre-production URL shall be used for connecting Test Account to sites.

# Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym | Definition                                                      |
|---------|-----------------------------------------------------------------|
| AMS     | Medical Automation Systems                                      |
| CAC     | Clinical Application Coordinator                                |
| CPE     | Clinical Practice Environment                                   |
| CPRS    | Computerized Patient System Records                             |
| CRDC    | Capital Region Data Center                                      |
| EARS    | Enterprise Archives                                             |
| ED      | Emergency Department                                            |
| EDIS    | Emergency Department Integration Software                       |
| EDP     | Namespace for EDIS                                              |
| EIE     | Enterprise Infrastructure Engineering                           |
| EMFAC   | Emergency Medicine Field Advisory Committee                     |
| ER      | Emergency Room                                                  |
| ESM     | Enterprise Systems Management                                   |
| EVE     | Client Server Program – Systems Manager                         |
| GUI     | Graphical User Interface                                        |
| GPO     | Group Policy Objects                                            |
| GTS     | Generic Traffic Shaping                                         |
| IAW     | In Accordance With                                              |
| IE      | Internet Explorer                                               |
| IOC     | Independent Out-Patient Clinics                                 |
| IP      | Internet Protocol                                               |
| IRM     | Information Resource Management                                 |
| ISP     | Internet Service Provider                                       |
| JAWS    | Job Access with Speech                                          |
| KIDS    | Kernel Installation and Distribution System                     |
| LCD     | Liquid Crystal Display                                          |
| NSR     | National Service Request                                        |
| OED     | Office of Enterprise Development                                |
| OI      | Office of Information                                           |
| OMB     | Office of Management and Budget                                 |
| PCE     | Patient Care Encounters                                         |
| PITC    | Philadelphia Information Technology Center                      |
| PKI     | Public Key Infrastructure                                       |
| PMAS    | Program Management Accountability System                        |
| POC     | Point-of-Care                                                   |
| PWS     | Performance Work Statement                                      |
| QA      | Quality Assurance                                               |
| RAM     | Random Access Memory                                            |
| RALS    | Point of Care IT Connectivity System                            |
| RQM     | Rational Quality Manager                                        |
| RR      | Risk Register                                                   |
| SCM     | Software Configuration Manager                                  |
| SSL     | Secure Sockets Layer                                            |
| TRRB    | Team Risk Review Board                                          |
| TWG     | Technical Working Group                                         |
| UAT     | User Acceptance Test                                            |
| VA      | Veterans Affairs                                                |
| VAMC    | Veterans Affairs Medical Center                                 |
| VDL     | VistA Documentation Library                                     |
| VHA     | Veterans Health Administration                                  |
| VISN    | Veterans Integrated Services Network                            |
| VistA   | Veterans Health Information Systems and Technology Architecture |
| VOB     | Version Object Base                                             |
| VM      | Virtual Machine                                                 |
| WBS     | Work Breakdown Structure                                        |
