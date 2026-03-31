---
title: Emergency Department Integration Software Server Installation Guide with Client Configuration
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: Emergency Department Integration Software Server  with Client Configuration
app_code: EDIS
app_name: Emergency Department Integration Software
section: CLI
app_status: active
pkg_ns: EDIS
patch_ver: 2.2
patch_id: EDIS*2.2
group_key: "EDIS:EDIS:2.2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - edis
  - table
  - contents
  - prompt
  - press
  - edpf
  - site
  - board
  - department
  - application
page_count: 0
word_count: 3934
section_count: 16
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Emergency_Dept_Integration_Software/edis_2_2_ig_r.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Emergency_Dept_Integration_Software/edis_2_2_ig_r.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=179"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Emergency Department Integration Software (EDIS)

  Server Installation Guide with Client Configuration
---

![](emergency-department-integration-software-server-installation-guide-with-client-/001.png)

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 53%" />
<col style="width: 18%" />
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
<td>06/29/2021</td>
<td>2.1</td>
<td><p>EDP*2.0*15:</p>
<ul>
<li><p>Added section Creating a Desktop Shortcut</p></li>
<li><p>Added the VA Folder Shortcut Note in section 4.1.1</p></li>
<li><p>Added section Create/Update EDIS Link on CPRS Tools Menu</p></li>
<li><p>Patch specific installation sections and procedures have been altered or removed within this document and integrated into the accompanying <em>Deployment, Installation, Back-out, and Rollback Guide</em> and will be released in this fashion by Product Support for nationally released FORUM patches moving forward</p></li>
<li><p>Added section EDIS Big Board</p></li>
<li><p>Added section Big Board Configuration</p></li>
<li><p>Updated Title page, Revision History, Table of Contents, and Footers</p></li>
<li><p>See the non-redacted EDIS_2_2_IG on the SOFTWARE library for viewing <mark>REDACTED</mark> information</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>12/21/2020</td>
<td>2.0</td>
<td><p>EDP*2.0*13:</p>
<ul>
<li><p>Updated document for GUI version 2.2.41</p></li>
<li><p>Updated files in XXXX</p></li>
<li><p>Added new EDIS URL</p></li>
<li><p>Updated section XXXXX VistA Server Installation Guide and its subsections for the release</p></li>
<li><p>Updated section XXXXX Client Installation Guide and its subsections for the release</p></li>
<li><p>Updated XXXX</p></li>
<li><p>Updated XXXX</p></li>
<li><p>Removed the Accronyms and Abbreviation section and included any missing terms into the Glossary document</p></li>
<li><p>Added institution N</p></li>
<li><p>Updated formatting, Title page, Revision History, Table of Contents, List of Tables, List of Figures, and Footers</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>11/05/2014</td>
<td>1.0</td>
<td><p>EDIS v.2.1.2. Initial Document.</p>
<p>This document combines the former EDIS Server Guide (document version 3.3) with the former EDIS Client Installation Guide (document version 3.6) and adds updates for EDIS software version 2.1.2. In addition to revised installation instructions and document formatting changes, the following changes were also made:</p>
<ul>
<li><p>Removed Security Key EDPR PROVIDER (previously used for Provider Report) from Section 3.5 Keys for EDIS Users.</p></li>
<li><p>Updated EDIS URL.</p></li>
</ul></td>
<td><mark>REDACTED</mark> <mark>REDACTED</mark></td>
</tr>
</tbody>
</table>
# Overview


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Overview](#overview)
  - [About this Guide](#about-this-guide)
  - [Section 508 of the Rehabilitation Act of 1973](#section-508-of-the-rehabilitation-act-of-1973)
    - [Document Conventions](#document-conventions)
  - [Recommended Audience](#recommended-audience)
  - [Referenced Documents and Files](#referenced-documents-and-files)
- [EDIS Web-based Application](#edis-web-based-application)
  - [M Server Components](#m-server-components)
- [EDIS Configuration](#edis-configuration)
  - [EDPF LOCATION Parameter](#edpf-location-parameter)
  - [EDPF NURSE STAFF SCREEN Parameter](#edpf-nurse-staff-screen-parameter)
  - [Creating an EDIS Proxy User for VistALink](#creating-an-edis-proxy-user-for-vistalink)
  - [Assign Options for Emergency Department Users](#assign-options-for-emergency-department-users)
  - [Keys for EDIS Users](#keys-for-edis-users)
  - [Configure EDIS to work with other Applications](#configure-edis-to-work-with-other-applications)
    - [Configure EDIS to Work with Omnicell](#configure-edis-to-work-with-omnicell)
  - [EDIS Big Boards](#edis-big-boards)
  - [Big Board Configuration](#big-board-configuration)
- [Client Configuration](#client-configuration)
  - [Production URL – Usage](#production-url-usage)
    - [Creating a Desktop Shortcut](#creating-a-desktop-shortcut)
    - [Create/Update EDIS Link on the CPRS Tools Menu](#createupdate-edis-link-on-the-cprs-tools-menu)
  - [Pre-Production URL – Usage](#pre-production-url-usage)
The fundamental mission of Department of Veterans Affairs (VA), Office of Information & Technology (OIT), Emergency Department Integration Software (EDIS) Program Services is to provide Veterans the benefits they have earned throughout their military service to the United States. OI&T accomplishes its mission by delivering high-quality, client-centered, effective and efficient Information Technology (IT) services to those responsible for providing care to the Veterans at the point-of-care as well as throughout all the points of the Veterans’ health care in an effective, timely and compassionate manner. VA depends on IT systems to meet mission goals.
The VHA Health Workflow System (HWS) Initiative is a single initiative whose mission is to expand health care access for Veterans, including women and rural populations. Multiple programs and projects have been assigned as part of the HWS Initiative, including EDIS.
The system is an extension to Veterans Health Information Systems and Technology Architecture (VistA) Computerized Patient Record System (CPRS) for tracking and managing the delivery of care to patients in an Emergency Department (ED). The system provides:
- Recording and tracking ED patients during incidents of care.
- Display of the current state of care delivery.
- Reports and data extracts on the delivery of care.
The system can be configured specifically for different Veterans Health Administration (VHA) Emergency Departments.

## About this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide provides instructions for installing application components that run on M servers at VAMC facilities. It also provides post-installation tasks and application configuration tasks within VistA.

## Section 508 of the Rehabilitation Act of 1973

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Portable Document File (PDF) version of this guide supports assistive reading devices.

### Document Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Document conventions include:

- Bold type indicates application elements (e.g. views, panes, links, buttons, prompts, and text boxes) and keyboard key names.
- Keyboard key names appear in angle brackets \< \>.
- *Italicized* text indicates special emphasis or user responses.
- ALL CAPS indicate M routines, parameters, and option names.

## Recommended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide provides information specifically for Department of Veterans Affairs Medical Center (VAMC) information resource management (IRM) staff to facilitate the ability to install and configure their systems to run EDIS.

## Referenced Documents and Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents and files are available on the software directory

- EDIS Server Installation Guide with Client Configuration
- EDIS Technical Manual
- EDIS User Guide
- EDIS Glossary
- Deployment, Installation, Back-out, and Rollback Guides (DIBR)

The documents are also available on the Veterans Document Library (VDL), which is located at <http://www.va.gov/vdl/application.asp?appid=179>.

# EDIS Web-based Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDIS application is a web-based application which contains both a java/WebLogic component and an M patch component. EDIS v.2.2 java code is already deployed and is managed by Enterprise Operations using Oracle WebLogic Application Server.

Oracle WebLogic Application Server is currently available for connection at the new URL:

<span class="mark">REDACTED</span>

## M Server Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Product Support nationally releases FORUM patches, to update the EDIS application, using a DIBR to convey the installation instructions.

# EDIS Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Configurations outlined in this section may be needed if EDIS is being installed for the first time. If an existing EDIS system is being updated with a nationally released FORUM patch, it is not necessary to perform these configuration steps.

## EDPF LOCATION Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter should contain the hospital location or locations that your emergency department uses. If you have a multi-division site, make an entry for each division.

1.  Log in to VistA.
2.  At the Select OPTION NAME prompt, type *xpar menu* (for XPAR MENU TOOLS) and then press the \<Enter\> key.
3.  At the Select General Parameter Tools Option prompt, type *ep* (for Edit Parameters) and then press the \<Enter\> key.
4.  At the Select PARAMETER DEFINITION NAME prompt, type *edpf l* (EDPF L; for EDPF LOCATION) and then press the \<Enter\> key.
5.  At the Select INSTITUTION NAME prompt, type the name or station number of your institution and then press the \<Enter\> key.
6.  At the Select Time Range (ex. 0800-1200) or Sequence prompt, type the time range during which the clinic location you are about to select functions as your site’s emergency department. Use military time. For example, if the location serves as your site’s emergency department from 8:00 AM to 5:00 PM, type *0800-1700*. Alternately, type a number that represents the location’s preference rating (the number *1* represents the most-preferred location). Press the \<Enter\> key. When users create a PCE encounter, EDIS uses time-of-day-based or preference-based criteria to determine the encounter’s location.

> Note: When selecting time ranges, be sure to account for all hours of emergency-department operation. EDIS does not create PCE encounters for patients whom users enter during times that you do not include in the EDPF LOCATION parameter. For example, suppose you set the parameter to use Clinic A from 0700 to 0800 hours and Clinic B from 0900 to 1200 hours. If a user then adds a patient at 0830 hours, EDIS will not create a PCE encounter for the patient. Further, take care not to overlap hours. In cases where hours overlap, EDIS always creates the patient’s PCE encounter for the first clinic.

> EDIS uses the time and preference settings you specify here to populate its Clinic list when you select the Show clinics on entry form check box in the application’s Configure view. This parameter allows users at sites that have multiple emergency-department locations to select the location EDIS will use when it creates the patient’s emergency department visit in CPRS.

7.  VistA displays your new time range or selection as a default value. Press the \<Enter\> key to accept this default value.
8.  At the ED LOCATION prompt, type the name of the location that serves as your site’s emergency department during this time range or for this sequence and press the \<Enter\> key.
9.  Repeat steps 6 through 8 for additional emergency-department locations (if any).

## EDPF NURSE STAFF SCREEN Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDPF NURSE STAFF SCREEN parameter allows you to select the type of filtering EDIS uses to populate the nursing-staff selection list in its Assign Staff view. By default, the application allows all entries in the New Person (#200) file. Options for narrowing the list of possible staff selections include:

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

> **NOTE:** For more information on how to configure and use VistALink, refer to VistALink documentation on the VDL: <http://www.va.gov/vdl/application.asp?appid=163>.

The EDIS Version 1 Installation Guide included the following steps to create an EDIS proxy user called *CONNECTOR, EDIS*. This information is included here for reference purposes.

Create a Connector Proxy M Account

*If your site has not created a VistALink connector proxy, use the Kernal Tool’s Foundations Manager menu to create the Connector Proxy M Account.*

1.  On the Foundations Manager main page, select CP Enter/Edit Connector Proxy User.

> Figure 1: Foundations Manager Menu

> ![](emergency-department-integration-software-server-installation-guide-with-client-/002.png)

2.  At the Enter NPF CONNECTOR PROXY name prompt, type CONNECTOR, EDIS.

To verify or update your site’s VistALink Listener:

1.  Check the Status of your site’s VistALink Listener using the FOUNDATION menu option.
2.  If you need to change any of the information below, submit a Service Now (SNOW) ticket to the VA Enterprise Service Desk.

> **NOTE:** Do not include restricted information in the SNOW ticket. It is VA Policy to send this information securely via public key infrastructure (PKI) message. Securely send this information for both the VistALink connector on your test VistA system and the VistALink connector on your production VistA system.

1.  The DNS for your site’s VistA server
2.  The port number of your site’s VistALink Listener
3.  The access code for the VistALink connector
4.  The verify code for the VistALink connector

## Assign Options for Emergency Department Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to gain access to EDIS, users and clinical application coordinators (CACs) must be assigned at least one of the following secondary menu options.

The EDIS project team recommends working with your site’s emergency-department administrative and IT staff to determine which users should receive which menu options. For a complete listing of EDIS options, refer to the *EDIS Technical Manual*, Section 7

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

There are additional secondary menu options that may need to be assigned to allow specific users to perform additional tasks:

1.  EDPF TRACKING VIEW CONFIGURE – Provides access to the Configure view, which includes the ability to configure rooms and areas, colors, one or multiple display boards, site-configurable parameters, and the contents of application pick lists.
2.  EDPF TRACKING VIEW EDIT CLOSED – Provides access to the Edit Closed view, which includes the ability to edit all data-entry fields for closed visits; the EDIS project team recommends limiting access to this view.
3.  EDPF TRACKING VIEW REPORTS – Provides access to the Reports view, which includes the ability to run administrative reports; separate keys control user access to export and print privileges, and to limited-access reports (see Section 3.5 below).
4.  EDPF TRACKING VIEW STAFF – Provides access to the Assign Staff view, which offers the ability to update physician-, resident-, and nursing-staff pick lists.

To reiterate, work with your site’s IT staff and emergency-department managers to gather a list of EDIS users and determine which views each user needs. Assign to each user only views he or she needs.

To assign options to a user:

1.  Log in to VistA.
2.  At the Select OPTION NAME prompt, type EVE and then press the \<Enter\> key.
3.  From the Choose 1-5 prompt, type the number 1 (for EVE Systems Manager Menu) and press the \<Enter\> key.
4.  From the Select Systems Manager Menu Option prompt, type User Management and press the \<Enter\> key.
5.  From the Select User Management Option prompt, type edit (for Edit an Existing User) and press the \<Enter\> key.
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
    1.  Note: The active person class is only needed for the Providers.
17. If the user’s person class is not active, select an active person class for the user.
18. When you have entered all applicable secondary menu options and verified that the user has an active person class, type the word Exit in the COMMAND field.
19. From the Save changes before leaving form (Y/N)? prompt, type the letter Y and press the \<Enter\> key.

## Keys for EDIS Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Assign keys for users who need access to additional reporting capabilities. The following keys are available:

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

## Configure EDIS to work with other Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Configure EDIS to Work with Omnicell

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your site wants EDIS to work with its Omnicell implementation, you must manually add the Omnicell event protocol (VEFS SDAM) to the EDIS EDP NEW PATIENT event. If you are already running EDIS, please review the below configuration to be certain nothing has changed.

1.  Open VA FileMan.
2.  At the Select OPTION prompt, type the number *1* (ENTER OR EDIT FILE ENTRIES).
3.  At the INPUT TO WHAT FILE prompt, type the word *protocol* (PROTOCOL).
4.  At the EDIT WHICH FIELD prompt, type the word *item*.
5.  At the CHOOSE 1–2 prompt, type the number *1* (ITEM (multiple)).
6.  At the EDIT WHICH ITEM SUB-FIELD prompt, press the \<Enter\> key to accept the default response (ALL).
7.  At the THEN EDIT FIELD prompt, press the \<Enter\> key without typing a response.
8.  At the Select PROTOCOL NAME prompt, type *EDP NEW PATIENT*.

At the Select ITEM prompt, type *VEFS SDAM* (the Omnicell event protocol). You don’t need to respond to prompts for other fields in the ITEM multiple.

## EDIS Big Boards

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites can configure one or more electronic whiteboard (also known as big board) displays. Display boards run in their own browser-based instances.

Use the following address as the main big board display. Replace the sitecode parameter 442 with the local institution number of the current site.

REDACTED

Secondary big board displays can be accessed by appending the above address. For example, if the 442 site has a secondary display board named Lab it would have the following address:

REDACTED

Appending the following arguments in the address will change the site and/or secondary display board:

- Replace sitecode=442 with the respective sitecode=current_site_code.
- Replace board=Lab with the respective board=secondary_board_name.

For assistance setting up the Big Board, refer to local operating system deployment (OSD) processes to properly image the device using the approved EDIS baseline. For imaging assistance, contact the Client Technologies team.

<span class="mark">REDACTED</span>

## Big Board Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Configure view in the EDIS desktop application allows users to select the optimal screen size for their site’s electronic whiteboard displays. Verify the Big Board display size is available in EDIS’s Configure view. If the site’s optimal display size is not on this list, it can be added by taking the following steps.

1.  Log in to VistA.
2.  At the Select OPTION NAME prompt, type xpar menu (for XPAR MENU TOOLS) and then press the \<Enter\> key.
3.  At the Select General Parameter Tools Option prompt, type ep (for Edit Parameter Values) and then press the \<Enter\> key.
4.  At the Select PARAMETER DEFINITION NAME prompt, type edpf screen (for EDPF SCREEN SIZES) and then press the \<Enter\> key.
5.  At the Enter selection prompt, type 5 (for Division) and then press the \<Enter\> key.
6.  At the Select INSTITUTION NAME prompt, type the name of your institution or its station number and then press the \<Enter\> key.
7.  At the Select Sequence prompt, type a number that represents the selection-list sequence in which you want the display size to appear and press the \<Enter\> key.
8.  If you are adding this sequence as a new sequence, respond to the Are you adding…as a new Sequence? Yes// prompt by pressing the \<Enter\> key to accept the default.
9.  At the Screen Size (WIDTHxHEIGHT) prompt, type the screen size you want EDIS to list and press the \<Enter\> key.
10. Repeat steps 7 through 9 to add additional selections to the screen-size list (as needed).

Refer to section 8.2 Display Board Sub View in the *EDIS User Guide* for further Big Board Configuration instructions.

# Client Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Production URL – Usage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS v2.2 should be accessible through a shortcut on the user’s desktop, in a shared network folder, or on the CPRS Tools menu. Follow VA and site procedures when granting user access, see Section 3.4

The URL for the EDIS production server is:

<span class="mark">REDACTED</span>

> **NOTE:** The institution is based on the user’s PIV. Users with 1 associated PIV location will never see a site drop down list. Users with multiple associated PIV locations will only see those corresponding sites in their site drop down list.

> **NOTE:** Chrome is the preferred browser.

### Creating a Desktop Shortcut

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow the instructions outlined below to create a shortcut on a user’s desktop.

1.  Right click the desktop and select New and then select Shortcut.
2.  Enter the following location into the Type the location of the item box then select Next.
    1.  "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" <span class="mark">REDACTED</span>
    2.  Note: Verify that the chrome.exe is located in the folder shown above. If not, adjust the string above before creating the shortcut.
3.  Enter EDIS v2.2 for the name of the shortcut in the Type a name for this shortcut box.
4.  Select Finish to place the shortcut on the desktop.

> **NOTE:** Updating the shortcut on a shared network folder is also an option; however, local sites only have access to edit shortcuts in their site specific folder (XXX_Shortcuts). To update the shortcut in the main network folder, a ticket would need to be entered for Regional support.

### Create/Update EDIS Link on the CPRS Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the VistA option GUI Tool Menu Items to create/update the EDIS link on the CPRS Tools Menu.

An example entry for EDIS is:

EDIS="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" <span class="mark">REDACTED</span>

> **NOTE:** Verify that the chrome.exe is located in the folder shown above. If not, adjust the string above before creating the link.

Select GUI Parameters \<TEST ACCOUNT\> Option: GUI Tool Menu Items

---------- Setting CPRS GUI Tools Menu for Division: BEDFORD VAMC ----------

Select Sequence: ?

Enter the sequence in which this menu item should appear.Select Sequence: 1

Are you adding 1 as a new Sequence? Yes// YES

Sequence: 1// \<Enter\>

Name=Command: EDIS="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" REDACTED

## Pre-Production URL – Usage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS v2.2 should be accessible through a shortcut on the user’s desktop, a shared network folder or on the CPRS Tools menu, see Section 4.1.1.1 above.

Access the following URL for training purposes in the test environment:

<span class="mark">REDACTED</span>