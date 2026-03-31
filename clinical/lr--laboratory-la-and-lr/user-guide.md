---
consolidated_title: "laboratory user guide"
app_code: LR
doc_type: UG
master_source: "LR*5.2*425 Laboratory User Guide"
master_pub_date: September 2013
consolidated_from: 2 versions
prior_versions:
  - "LA*5.2*68 Laboratory User Guide"
---

VistA Laboratory Patch

![](lr-5-2-425-laboratory-user-guide/001.png)

Patch Supplemental: User Guide

Patch: LR\*5.2\*425

September 2013

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Development (PD)

<span id="_Toc327252270" class="anchor"></span>Revision History

<table style="width:100%;">
<caption><p><span id="_Toc366647077" class="anchor"></span>Table . Document Revision History</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 36%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>09/11/2013</td>
<td>1.0</td>
<td>Initial document. Created a Supplemental Patch: User Guide for the release of Laboratory Patch LR*5.2*425.</td>
<td><p>Project Development Team:</p>
<ul>
<li><p><mark>redacted</mark></p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc366647077" class="anchor"></span>Table . Document Revision History

Contents

[6.2.3 Determine if a Topography is a Default Specimen for an Active Collection  
Sample [45](#determine-if-a-topography-is-a-default-specimen-for-an-active-collection-sample)](#determine-if-a-topography-is-a-default-specimen-for-an-active-collection-sample)

<span id="_Toc366646999" class="anchor"></span>Figures and Tables

Figures

[Figure 22. Specimen Inactivation/Activation—Determine if a collection sample is used on an active  
test [42](#_Toc366647071)](#_Toc366647071)

Tables

<span id="_Toc276558124" class="anchor"></span>Orientation

How to Use this Manual

This manual provides step-by-step instructions for using and implementing new functionality for the legacy Veterans Health Information Systems and Technology Architecture (VistA) Laboratory Information Management System (LIMS) 5.2.

The new functionality for the legacy VistA Laboratory 5.2 software was released with the VistA Laboratory Patch LR\*5.2\*425.

![](lr-5-2-425-laboratory-user-guide/002.png) NOTE: For patch installation instructions, see the FORUM patch descriptions.

![](lr-5-2-425-laboratory-user-guide/003.png) NOTE: For technical and design information, see the *Laboratory Patch LR\*5.2\*425 System Design document (SDD)*.  
  
For additional legacy VistA Laboratory technical information, see the *Laboratory Technical Manual Version 5.2* located on the VA Software Document Library (VDL) at: <http://www4.va.gov/vdl/application.asp?appid=71>

Intended Audience

The intended audience of this manual includes the following stakeholders:

- Information Resource Management (IRM), system administrators, or other technical staff who are tasked with deploying LSRP-related software in all VistA environments.
- Operations Staff and LIMS/Configuration Staff who are responsible for maintaining and supporting the Laboratory Information Management System (LIMS).
- Laboratory Automated Data Processing Application Coordinators (ADPACS) and Laboratory Information Managers (LIM).
- Authorized Laboratory staff who use the following functions:
  - Obsolete Pending Orders
  - Hospital Location Change Monitoring System (HLCMS) Tool
  - Laboratory Test File 60 Audit Tool
  - Monitor Laboratory Test File Changes Affecting Quick Orders (File 60 Quick Order API)
  - Specimen Inactivation/Activation:
    - Collection Sample Entries
    - Topography Entries
- Product Support (PS).

Legal Requirements

There are no special legal requirements involved in the use of legacy VistA Laboratory software.

The legacy VistA Laboratory software runs within the VistA architecture on the VA's network. The following warning is issued during the log in process:

"This U.S. Government computer system is for official use only. The files on this system include Federal records that contain sensitive information. All activities on this system may be monitored to measure network performance and resource utilization; to detect unauthorized access to or misuse of the system or individual files and utilities on the system, including personal use; and to protect the operational integrity of the system. Further use of this system constitutes your consent to such monitoring. Misuse of or unauthorized access to this system may result in criminal prosecution and disciplinary, adverse, or other appropriate action."

Disclaimers

This manual provides an overall explanation of how to use and maintain the updated functionality for the VistA Laboratory Information Management System (LIMS) 5.2 software; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA websites on the Internet and VA Intranet for a general orientation to VistA. For example, go to the Office of Information and Technology (OIT) VistA Development VA Intranet website: http://vista.med.va.gov

![](lr-5-2-425-laboratory-user-guide/004.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this website or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols/terms are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols/terms:

<table>
<caption><blockquote>
<p><span id="_Toc366647078" class="anchor"></span>Table . Documentation symbol/term descriptions</p>
</blockquote></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Symbol</td>
<td>Description</td>
</tr>
<tr class="even">
<td>![](lr-5-2-425-laboratory-user-guide/005.png)</td>
<td><p><strong>NOTE/REF:</strong> Used to inform the reader of general information including references to additional reading material.</p>
<p>In most cases you will need this information, or at least it will make the installation smoother and more understandable. Please read each note <em>before</em> executing the steps that follow it!</p></td>
</tr>
<tr class="odd">
<td>![](lr-5-2-425-laboratory-user-guide/006.png)</td>
<td><strong>CAUTION, DISCLAIMER, or RECOMMENDATION:</strong> Used to inform the reader to take special notice of critical information.</td>
</tr>
</tbody>
</table>

<span id="_Toc366647078" class="anchor"></span>Table . Documentation symbol/term descriptions

- Descriptive text is presented in a proportional font (as represented by this font).
- "Snapshots" of computer commands and online displays (i.e., screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and may be enclosed within a box.
- User's responses to online prompts will be bold typeface and highlighted in yellow (e.g., <span class="mark">\<Enter\></span>).
- Some software code reserved/key words will be bold typeface with alternate color font.
- Author's comments, if any, are displayed in italics or as "callout" boxes.

![](lr-5-2-425-laboratory-user-guide/007.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- Besides established styles and conventions, the following additional text formatting will be used to further highlight or emphasize specific document content:
- Bold Typeface:
  - All computer keys when referenced with a command (e.g., "press Enter" or "click OK").
  - All references to computer dialogue tab or menu names (e.g., "go to the General tab" or "choose Properties from the Action menu").
  - All values entered or selected by the user in computer dialogues (e.g., "Enter 'xyz' in the Server Name field" or "Choose the ABCD folder entry from the list").
  - All user text (e.g., commands) typed or entered in a Command-Line prompt (e.g., "Enter the following command: CD xyz").
- Italicized Typeface:
  - Emphasis (e.g., do *not* proceed or you *must* do the following steps).
  - All reference to computer dialogue or screen titles (e.g., "in the *Add Entries* dialogue…").
  - All document or publication titles and references (e.g., "see the *ABC Installation Guide*").
- Step-by-Step Instructions—For documentation purposes, explicit step-by-step instructions for repetitive tasks (e.g., "Open a Command-Line prompt") are generally only provided once. For subsequent steps that refer to that same procedure or task, please refer back to the initial step where those instructions were first described.

<span id="navigation" class="anchor"></span>Documentation Navigation

Document Navigation—This document uses Microsoft® Word's built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to your toolbar, do the following:

1.  Right-click anywhere on the customizable Toolbar in Word 2007 (not the Ribbon section).
2.  Select Customize Quick Access Toolbar from the secondary menu.
3.  Press the dropdown arrow in the "Choose commands from:" box.
4.  Select All Commands from the displayed list.
5.  Scroll through the command list in the left column until you see the Back command (green circle with arrow pointing left).
6.  Click/Highlight the Back command and press Add to add it to your customized toolbar.
7.  Scroll through the command list in the left column until you see the Forward command (green circle with arrow pointing right).
8.  Click/Highlight the Forward command and press Add to add it to your customized toolbar.
9.  Press OK.

You can now use these Back and Forward command buttons in your Toolbar to navigate back and forth in your Word document when clicking on hyperlinks within the document.

![](lr-5-2-425-laboratory-user-guide/008.png) NOTE: This is a one-time setup and will automatically be available in any other Word document once you install it on the Toolbar.

Acronyms and Definitions

| Term      | Definition                                                                                                                                                        |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ADPAC     | Automated Data Processing Application Coordinator                                                                                                                 |
| ADT       | Admission/Discharge/Transfer                                                                                                                                      |
| AP        | Anatomic Pathology                                                                                                                                                |
| API       | Application Program Interface                                                                                                                                     |
| CAC       | Clinical Application Coordinator                                                                                                                                  |
| COTS      | Commercial-Off-The-Shelf (applications)                                                                                                                           |
| CPRS      | Computerized Patient Record System                                                                                                                                |
| FTP       | File Transfer Protocol                                                                                                                                            |
| GMTS      | Health Summary—Identified with the namespace moniker, "GMTS".                                                                                                     |
| GUI       | Graphical User Interface                                                                                                                                          |
| HLCMS     | Hospital Location Change Monitoring System (Tool)                                                                                                                 |
| IA        | Integration Agreement                                                                                                                                             |
| ICR       | Integration Control Registration                                                                                                                                  |
| iEHR      | integrated Electronic Healthcare Record                                                                                                                           |
| IEN       | Internal Entry Number                                                                                                                                             |
| IRM       | Information Resource Management                                                                                                                                   |
| KIDS      | Kernel Installation & Distribution System                                                                                                                         |
| LDSI      | Laboratory Data Sharing and Interoperability                                                                                                                      |
| LEDI      | Laboratory Electronic Data Interchange                                                                                                                            |
| LIM       | Laboratory Information Manager                                                                                                                                    |
| LOINC     | Logical Observation Identifiers, Names, and Codes                                                                                                                 |
| LR        | Laboratory—Identified with the namespace moniker, "LR".                                                                                                           |
| LSRP      | Laboratory System Re-Engineering Project                                                                                                                          |
| MT        | Medical Technologists                                                                                                                                             |
| MUMPS (M) | Massachusetts General Hospital Utility Multi-Programming System. It is the original medical system and computer language upon which VistA was based and enhanced. |
| OERR      | Order Entry Results Reporting                                                                                                                                     |
| OIFO      | Office of Information Field Office                                                                                                                                |
| OR        | Order Entry/Results Reporting—Identified with the namespace moniker, "OR".                                                                                        |
| RSD       | Requirements Specification Document                                                                                                                               |
| SDD       | System Design Document                                                                                                                                            |
| SNOMED    | Systematized Nomenclature of Medicine                                                                                                                             |
| STS       | Standards and Terminology Services                                                                                                                                |
| TRM       | Technical Reference Model                                                                                                                                         |
| VAMC      | VA Medical Center                                                                                                                                                 |
| VHA       | Veterans Health Administration                                                                                                                                    |
| VISTA     | Veterans Health Information Systems and Technology Architecture                                                                                                   |

<span id="_Ref358711337" class="anchor"></span>Table . Acronyms and Definitions

![](lr-5-2-425-laboratory-user-guide/009.png) REF: For a list of commonly used terms and definitions, see the OIT Master Glossary VA Intranet Website: http://vaww.oed.wss.va.gov/process/OIT%20Master%20Glossary/Home.aspx  
  
For a list of commonly used acronyms, see the VA Acronym Lookup Intranet Website: http://vaww1.va.gov/Acronyms/index.cfm

Assumptions

This manual is written with the assumption that the reader is experienced or familiar with the following:

- VistA computing environment:
- Laboratory—VistA M Server software
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft Windows
- M programming language

Reference Materials

Readers who wish to learn more about LSRP should consult the following:

- *Laboratory Installation Guide Version 5.2*
- *Laboratory Package Security Guide Version 5.2*
- *Laboratory Planning Implementation Guide (PIG) Version 5.2*
- *Laboratory Release Notes Version 5.2*
- *Laboratory Technical Manual Version 5.2*
- *Laboratory User Manual Version 5.2*
- *Software Design Document (SDD)*: Patch LR\*5.2\*425
- *Requirements Specification Document (RSD)*: Patch LR\*5.2\*425
- *Legacy VistA Laboratory Vision*
- *Legacy VistA Laboratory Supplementary Specification*
- *Legacy VistA Laboratory VistA Integration System Use Case Model and Use Case Specifications*
- *Legacy VistA Laboratory COTS LIMS Integration System Use Case Model and Use Case Specifications*
- Rational Unified Process
- VHA Health Information Architecture
- VHA Technical Reference Model (TRM)

VistA documentation is made available online in Microsoft Word format and Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader, which is freely distributed by Adobe Systems Incorporated at the following website: <http://www.adobe.com/>

VistA documentation can be downloaded from the VA Software Documentation Library (VDL) website: <http://www.va.gov/vdl/>

![](lr-5-2-425-laboratory-user-guide/010.png) REF: The legacy VistA Laboratory documentation is located on the VDL at: <http://www.va.gov/vdl/application.asp?appid=71>

VistA documentation and software can also be downloaded from the Product Support (PS) anonymous directories:

- Preferred Method download.vista.med.va.gov

![](lr-5-2-425-laboratory-user-guide/011.png) NOTE: This method transmits the files from the first available File Transfer Protocol (FTP) server.

- Albany Office of Information Field Office (OIFO) ftp.fo-albany.med.va.gov
- Hines OIFO ftp.fo-hines.med.va.gov
- Salt Lake City OIFO ftp.fo-slc.med.va.gov

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Scope](#scope)
- [Set the Obsolete Pending Orders Parameter](#set-the-obsolete-pending-orders-parameter)
  - [Set the Obsolete Pending Orders Parameter Overview](#set-the-obsolete-pending-orders-parameter-overview)
  - [Verify/Update Grace Period for Orders](#verifyupdate-grace-period-for-orders)
  - [Set Obsolete Pending Orders Parameter Procedure](#set-obsolete-pending-orders-parameter-procedure)
  - [Set Obsolete Pending Orders Schedule](#set-obsolete-pending-orders-schedule)
- [Monitor Hospital Location Changes](#monitor-hospital-location-changes)
  - [Monitor Hospital Location Changes Overview](#monitor-hospital-location-changes-overview)
  - [Verify/Re-schedule the Hospital Location Change Report](#verifyre-schedule-the-hospital-location-change-report)
  - [Reviewing the LRJ SYS MAP HL TASK RPT](#reviewing-the-lrj-sys-map-hl-task-rpt)
  - [Additional HLCMS Options](#additional-hlcms-options)
    - [DE—Display Extracted (Raw) Data Option](#dedisplay-extracted-raw-data-option)
    - [DM—Display Mail Message Option](#dmdisplay-mail-message-option)
    - [AQ—Hospital Location Audit Query Option](#aqhospital-location-audit-query-option)
    - [SM—Send Mail Message Option](#smsend-mail-message-option)
    - [SX—Send Extract File Option](#sxsend-extract-file-option)
    - [Accept/edit HL Config Dates Option](#acceptedit-hl-config-dates-option)
- [Laboratory Test File 60 Audit Tool](#laboratory-test-file-60-audit-tool)
  - [Laboratory Test File 60 Audit Tool Overview](#laboratory-test-file-60-audit-tool-overview)
  - [File 60 Audit Reports](#file-60-audit-reports)
    - [Schedule Audit Reports](#schedule-audit-reports)
    - [Manually Run File 60 Audit Reports](#manually-run-file-60-audit-reports)
  - [File 60 Audit Tool Options](#file-60-audit-tool-options)
  - [Set Additional File 60 Fields to be Audited](#set-additional-file-60-fields-to-be-audited)
    - [Set Auditing for Optional Fields](#set-auditing-for-optional-fields)
    - [Delete Auditing from Optional Fields](#delete-auditing-from-optional-fields)
  - [Display List of Audited Fields](#display-list-of-audited-fields)
  - [Display File 60 Changes](#display-file-60-changes)
  - [Send File 60 Changes in Mail](#send-file-60-changes-in-mail)
    - [Send Display as Mail Message Option](#send-display-as-mail-message-option)
    - [Send Extract File as Mail Message](#send-extract-file-as-mail-message)
- [Monitor Laboratory Test File Changes Affecting Quick Orders (File 60 Quick Order API)](#monitor-laboratory-test-file-changes-affecting-quick-orders-file-60-quick-order-api)
  - [Monitor Laboratory Test File Changes Affecting Quick Orders Overview](#monitor-laboratory-test-file-changes-affecting-quick-orders-overview)
  - [Monitor Laboratory Test File Changes Affecting Quick Orders Procedure](#monitor-laboratory-test-file-changes-affecting-quick-orders-procedure)
  - [Verify/Re-schedule the LRJ QUICK ORDER CHECK Option](#verifyre-schedule-the-lrj-quick-order-check-option)
    - [Schedule LRJ QUICK ORDER CHECK](#schedule-lrj-quick-order-check)
- [Specimen Inactivation/Activation](#specimen-inactivationactivation)
  - [Specimen Inactivation/Activation Overview](#specimen-inactivationactivation-overview)
  - [Collection Sample/Topography Field—Inactivation](#collection-sampletopography-fieldinactivation)
    - [Determine if a Collection Sample is Used on an Active Test](#determine-if-a-collection-sample-is-used-on-an-active-test)
    - [Determine if a Collection Sample is Assigned a Default Specimen](#determine-if-a-collection-sample-is-assigned-a-default-specimen)
    - [Determine if a Topography is a Default Specimen for an Active Collection Sample](#determine-if-a-topography-is-a-default-specimen-for-an-active-collection-sample)
    - [Inactivate Entries in the Collection Sample and Topography Field Files](#inactivate-entries-in-the-collection-sample-and-topography-field-files)
  - [Collection Sample/Topography Field—Activation](#collection-sampletopography-fieldactivation)
- [Mail Group Maintenance](#mail-group-maintenance)
  - [Mail Group Overview](#mail-group-overview)
  - [Assign New Users to Mail Groups](#assign-new-users-to-mail-groups)
This *VistA Laboratory Patch Supplemental: User Guide* describes the software functionality extracted from the Laboratory System Re-Engineering Project (LSRP) for use in the legacy Veterans Health Information Systems and Technology Architecture (VistA) Laboratory 5.2 software. Since LSRP is currently in sustainment mode at the Huntington, WV VA Medical Center (VAMC) and will *not* be released nationally, it was decided that some functionality was useful for the current legacy VistA Laboratory 5.2 software and should be released nationally.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this *VistA Laboratory Patch Supplemental: User Guide* is to describe the use and implementation of the new functionality enhancements for the legacy VistA Laboratory 5.2 Information Management System (LIMS) system.

This added functionality was originally developed to support LSRP and was subsequently identified to provide a significant benefit to the laboratories in the field as well as supporting ongoing VA projects outside the delivery of LSRP.

Supplemental stakeholders that were consulted in the elaboration of the original LSRP software design included:

- Legacy VistA Laboratory LIMS support staff
- LSRP Alpha-site support staff
- Computerized Patient Record System (CPRS) project team
- VA Standards and Terminology Services (STS) project team
- Lab Electronic Data Interchange (LEDI IV) – Lab Data Sharing and Interoperability (LDSI) project team

This section describes the software functionality extracted from LSRP as part of a national release of enhancements (upgrade) to the legacy VistA Laboratory 5.2 software. It describes the components of Patch LR\*5.2\*425.

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LSRP primarily focused on development work to provide a foundation for the integration of a new Commercial-off-the-Shelf (COTS) LIMS product into the VistA architecture. Much of the original scoped LSRP work was identified by VA field personnel due to the short-comings of the current, aging VistA LIMS. The LSRP software was only tested and installed in production at the Huntington, WV VAMC (i.e., Alpha site) before the project scope of deploying the COTS LIMS to the field was shifted to a sustainment of the Alpha site only while the VA re-evaluates the delivery model.

With nearly a decade of software development on the legacy VistA LIMS and a necessity to better equip Huntington VAMC for self-support, legacy VistA Laboratory recognized the need to nationally deploy a select set of Laboratory software functionality that is *not* dependent on the presence of the COTS LIMS.

Laboratory Patch LR\*5.2\*425 adds/enhances the following functionality in the legacy VistA Laboratory 5.2 software:

- <u>Set the Obsolete Pending Orders Parameter</u>
- <u>Monitor Hospital Location Changes</u>
- <u>Laboratory Test File 60 Audit Tool</u>
- <u>Monitor Laboratory Test File Changes Affecting Quick Orders (File 60 Quick Order API)</u>
- <u>Specimen Inactivation/Activation</u>

The legacy VistA Laboratory application will serve as the database/repository for all lab information. VistA applications will continue to access laboratory information from the legacy VistA Laboratory application via existing Integration Agreements (IAs). This document details all of the new functionality changes added to the legacy VistA Laboratory application to support the LIMS.

# Set the Obsolete Pending Orders Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Set the Obsolete Pending Orders Parameter Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Laboratories currently establish business rules that define how long a pending order is valid. For example, a lab might decide that an order scheduled for collection more than 90 days in the past is no longer valid. Laboratory Patch LR\*5.2\*425 automates those business rules by introducing a new LRJ OBSOLETE PENDING ORDERS parameter. This allows the site to define how many days in the past an order is considered valid.

Sites set the LRJ OBSOLETE PENDING ORDERS parameter in the PARAMETER DEFINITION file (#8989.51) to define the period of time before orders are cancelled. If that date passes:

1.  A TaskMan job cancels the order in the LAB ORDER ENTRY file (#69).
2.  TaskMan sends a status update to the Order Entry/Results Reporting (OERR) 3.0 system
3.  The Order Entry/Results Reporting (OERR) 3.0 system changes the order to "Lapsed" in the ORDER file (#100).

The value of the parameter is compared to the GRACE PERIOD FOR ORDERS field (#15) in the LABORATORY SITE file (#69.9). To allow the purging of pending orders, the site needs to verify the following:

- GRACE PERIOD FOR ORDERS field (#15) in the LABORATORY SITE file (#69.9)—*Cannot* be null; it *must* have a value.
- LRJ OBSOLETE PENDING ORDERS parameter—*Cannot* be null and it *must* be *smaller* than the value in the GRACE PERIOD FOR ORDERS field (#15) in the LABORATORY SITE file (#69.9).

Once these two field values are set properly, when the Purge old orders & accessions option \[LROC\] is run by an authorized user that is when the order is purged from the file. If either or both of these values are *not* set properly, the LROC option displays a message and does *not* run, and a MailMan message is sent to the G.LMI mail group.

![](lr-5-2-425-laboratory-user-guide/012.png) CAUTION: Sites should schedule the Obsolete Pending Order job to run daily at a non-peak hour. It cancels pending lab orders in the LAB ORDER ENTRY file (#69) and lapses them in the ORDER file (#100) based on the value set in the parameter.

## Verify/Update Grace Period for Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify the Grace Period setting and update if necessary, perform the following procedure:

1.  From the VA FileMan option \[DIUSER\], select the Enter or Edit File Entries option \[DIEDIT\].
2.  At the "Input to What File: New Person" prompt, enter 69.9 (LABORATORY SITE file).
3.  At the "Edit which field" prompt, enter Grace Period for Orders (or enter 15; the GRACE PERIOD FOR ORDERS field number).
4.  At the "Then Edit Field" prompt, press Enter.
5.  At the "Select Laboratory Site Name" prompt, enter ?? to display the *single* site name, and then enter that name at the prompt.

![](lr-5-2-425-laboratory-user-guide/013.png) NOTE: There can be only one entry in the LABORATORY SITE file (#69.9). If the site has changed the pre-populated entry (i.e., Hospital), enter that name (e.g., HUNTINGTON VAMC).

6.  At the "GRACE PERIOD FOR ORDERS: *730*//" prompt, press Enter to accept the default or enter the site-determined number of days.
- This field *must* have a value, it *cannot* be null.
- For maximum data retention when generating reports, a retention period of 2 years (730 days) is recommended.
- The *Laboratory Planning and Implementation Guide* recommends a retention period of 120 days.
- The *maximum* retention period is 999 days.

> <span id="_Ref356289876" class="anchor"></span>Figure . Set the Obsolete Pending Orders Parameter—Verify Grace Period: VA FileMan

Select Supervisor menu Option: <span class="mark">^VA FILEMAN</span>

          VA FileMan Version 22.0

          Enter or Edit File Entries

          Print File Entries

          Search File Entries

          Modify File Attributes

          Inquire to File Entries

          Utility Functions ...

          Data Dictionary Utilities ...

          Transfer Entries

          Other Options ...

Select VA FileMan Option: <span class="mark">ENTER\<Enter\></span> or Edit File Entries

INPUT TO WHAT FILE: NEW PERSON// <span class="mark">69.9 \<Enter\></span> LABORATORY SITE

                                          (1 entry)

EDIT WHICH FIELD: ALL// <span class="mark">GRACE PERIOD FOR ORDERS</span>

THEN EDIT FIELD: <span class="mark">\<Enter\></span>

Select LABORATORY SITE SITE NAME: <span class="mark">??</span>

VAMC

        You may enter a new LABORATORY SITE, if you wish

        <span class="mark">There can be only one entry in this file.</span>

Select LABORATORY SITE SITE NAME: <span class="mark">VAMC</span>

GRACE PERIOD FOR ORDERS: 730// <span class="mark">\<Enter\></span>

Select LABORATORY SITE SITE NAME:

## Set Obsolete Pending Orders Parameter Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LRJ OBSOLETE PENDING ORDERS parameter helps control the number of orders that are available for accessioning.

To set the LRJ OBSOLETE PENDING ORDERS parameter, perform the following procedure:

![](lr-5-2-425-laboratory-user-guide/014.png) NOTE: In order to access the CPRS Configuration (IRM) menu \[OR PARAM IRM MENU\], the user *must* hold the XUPROG security key.

1.  From the CPRS Configuration (IRM) menu \[OR PARAM IRM MENU\], select the General Parameter Tools option \[XPAR MENU TOOLS\].
2.  At the "Select General Parameter Tools Option:" prompt, select the EP—Edit Parameter Values option \[XPAR EDIT PARAMETER\].
3.  At the "Select PARAMETER DEFINITION NAME:" prompt, enter LRJ OBSOLETE PENDING ORDERS.
4.  At the "Enter Number of Days" prompt, enter the site-specific value for lapsed orders. The value entered *must be smaller* than the GRACE PERIOD FOR ORDERS value (see Section <u>2.1</u>).

> <span id="_Toc351646957" class="anchor"></span>Figure . Set the Obsolete Pending Orders Parameter—Sample user entries

Select Systems Manager Menu Option: <span class="mark">^CPRS \<Enter\></span> CPRS Configuration (IRM)

OC Order Check Expert System Main Menu ...

TI ORMTIME Main Menu ...

UT CPRS Clean-up Utilities ...

HD HealtheVet Desktop Configuration ...

RD Remote Data Order Checking Parameters

General Parameter Tools ...

Select CPRS Configuration (IRM) Option: <span class="mark">GENERAL \<Enter\></span> Parameter Tools

LV List Values for a Selected Parameter

LE List Values for a Selected Entity

LP List Values for a Selected Package

LT List Values for a Selected Template

EP Edit Parameter Values

ET Edit Parameter Values with Template

EK Edit Parameter Definition Keyword

Select General Parameter Tools Option: <span class="mark">EP \<Enter\></span> Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: <span class="mark">LRJ OBSOLETE PENDING ORDERS \<Enter\></span> OBSOLETE PENDING ORDERS DEFAULT

Setting LRJ OBSOLETE PENDING ORDERS for System: HUNT2.FO-BAYPINES.MED.VA.GOV

NUMBER OF DAYS: *<span class="mark">nnn</span>*

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Select PARAMETER DEFINITION NAME:

## Set Obsolete Pending Orders Schedule

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](lr-5-2-425-laboratory-user-guide/015.png) CAUTION: Sites should schedule the Obsolete Pending Order job to run daily at a non-peak hour.

To verify the Obsolete Pending Orders job is scheduled to run, perform the following procedures

1.  From the Systems Manager Menu \[EVE\], select the Taskman Management menu \[XUTM MGR\].
2.  At the "Select Taskman Management Option" prompt, select the Schedule/Unschedule option \[XUTM SCHEDULE\].
3.  At the "Select Option to schedule or reschedule:" prompt, enter LRJ OBSOLETE PENDING ORDERS.
4.  At the "OK? Yes//" prompt, press Enter. The Edit Option Schedule screen displays.
5.  The LRJ OBSOLETE PENDING ORDERS option should be queued to run in TASKMAN nightly.
6.  If no schedule is showing, at a minimum Edit and Save the QUEUED TO RUN AT WHAT TIME and the RESCHEDULING FREQUENCY fields. The option should be scheduled to run at a non-peak hour.

> <span id="_Toc351646959" class="anchor"></span>Figure . Set the Obsolete Pending Orders Parameter—Schedule Obsolete Parameter Job: Sample user dialogue and reports

Select Systems Manager Menu Option: <span class="mark">TASKMAN \<Enter\></span> Management

Schedule/Unschedule Options

One-time Option Queue

Taskman Management Utilities ...

List Tasks

Dequeue Tasks

Requeue Tasks

Delete Tasks

Print Options that are Scheduled to run

Cleanup Task List

Print Options Recommended for Queueing

Select Taskman Management Option: <span class="mark">SCHEDULE \<Enter\></span> /Unschedule Options

Select OPTION to schedule or reschedule: <span class="mark">LRJ OBSOLETE PENDING ORDERS \<Enter\></span> Obsolete Pending Lab Orders

...OK? Yes// <span class="mark">\<Enter\></span> (Yes)

\(R\)

Edit Option Schedule

Option Name: <span class="mark">LRJ OBSOLETE PENDING ORDERS</span>

Menu Text: <span class="mark">Obsolete Pending Lab Orders</span> TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: <span class="mark">FEB 2,2012@21:00</span>

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: <span class="mark">1D</span>

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

# Monitor Hospital Location Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Monitor Hospital Location Changes Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Hospital Location Change Monitoring System (HLCMS) Tool monitors changes to hospital location data made in VistA. Hospital locations include clinics, wards, and operating rooms. The HLCMS Tool is the mechanism for notifying staff that configuration changes may be needed within Vista applications that subscribe to hospital location files. Hospital location changes made in the legacy VistA Admission/Discharge/Transfer (ADT) system can be significant to the Laboratory software when locating inpatients for specimen collection.

The following functionality is introduced with the HLCMS Tool:

- Hospital Location Initial Extract—This is a predefined report that will pull the required information from VistA ADT in an extract to verify lab-related locations, beds & rooms. ("Lab-related" locations are Clinic, Ward, or Operating Room type locations.)
- Supports scheduled notifications to designated staff and alerts them of changes to the VistA hospital locations so lab configurations can be adjusted, as necessary.
- Contains tools to define the Lab sub-system that controls monitoring of hospital location changes affecting Lab. The toolset contains viewers for extracted raw data and mail messages.

Verify that the LRJ SYS MAP HL TASKMAN RPT has been scheduled to run periodically to alert laboratory support staff of additional hospital location changes (Section <u>3.2</u>).

![](lr-5-2-425-laboratory-user-guide/016.png) CAUTION: Currently, the HLCMS Tool only monitors changes to the inactivation date field on the day the change is made, after the LRJ SYS MAP HL TASKMAN RPT task has run. Note any inactivation changes planned for a future date and make necessary configuration changes on that day.

## Verify/Re-schedule the Hospital Location Change Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The frequency for running the LRJ SYS MAP HL TASKMAN RPT may vary from site-to-site and should be based on the frequency of the local hospital location changes. If hospital location changes are made daily, the report frequency should be at least daily or even multiple times during the day. If hospital location changes are not made daily, the frequency of the report should be changed to reflect a longer period. Sites should err on the side of scheduling the report to run too often and then adjust the schedule as the frequency of hospital changes is noted.

The frequency of running this report can be changed as needed. For example, when making large changes like adding a new ward/building or re-arranging beds, you might want to run the report more often until all the changes are made.

![](lr-5-2-425-laboratory-user-guide/017.png) NOTE: To schedule LRJ SYS MAP HL TASKMAN RPT using the Hospital Location Change Monitoring System (HLCMS) Tool, the user *must* hold the LRJ HL TOOLS MGR security key.

To verify/schedule how often the LRJ SYS MAP HL TASKMAN RPT is run, perform the following procedure:

1.  From the Lab liaison menu \[LRLIAISON\], select the Hospital Location Monitor Tool option \[LRJ HOSPITAL LOCATION MONITOR\].
4.  Select the DS—Show LRJ SYS MAP HL TASKMAN RPT sch option \[LRJ SYS MAP HL SCHED AUDIT RPT DISP\] to display the current TaskMan schedule for running the LRJ SYS MAP HL TASKMAN RPT.
5.  Review the time/frequency the report is scheduled to run.
6.  To make changes in the time/frequency: At the "Select Action: Quit//" prompt, select the ST—Sched LRJ SYS MAP HL TASKMAN RPT option \[LRJ SYS MAP HL SCHED AUDIT RPT TASK\] to schedule LRJ SYS MAP HL TASKMAN RPT.

    The user can change the run date/time and the frequency of the option.
7.  Upon completion of the schedule entry, the Hospital Location Audit task schedule screen displays with the user applied changes.

> <span id="_Ref356296294" class="anchor"></span>Figure . Monitor Hospital Location Changes—Show LRJ SYS MAP HL TASKMAN RPT sch and DS—Sched LRJ SYS MAP HL TASKMAN RPT options

Select Laboratory DHCP Menu Option: <span class="mark">^LAB LIAISON MENU</span>

ANT Add a new internal name for an antibiotic

ANTE Edit an Antibiotic

BCF Lab Bar Code Label Formatter

BCZ Lab Zebra Label Utility

DATA Add a new data name

HDR Recover/Transmit Lab HDR Result Messages

LNC LOINC Main Menu ...

MOD Modify an existing data name

SMGR Lab Shipping Management Menu ...

Add a new WKLD code to file

AP Microfiche Archive

Archiving Menu ...

Check files for inconsistencies

Check patient and lab data cross pointers

Download Format for Intermec Printer

Edit atomic tests

Edit cosmic tests

Edit Inactive Date - COLLECTION SAMPLE

Edit Inactive Date - TOPOGRAPHY FIELD

File 60 Audit Manager

File list for lab

<span class="mark">Hospital Location Monitor Tool</span>

LAB ROUTINE INTEGRITY MENU ...

Lab Tests and CPT Report

LIM workload menu ...

Manually compile WKLD and workload counts

OE/RR interface parameters ...

Outline for one or more files

Print AMA CPT Panel Pending List

Re-index Antimicrobial Suscept File (62.06)

Restart processing of instrument data

Turn on site workload statistics

Turn on workload stats for accession area

User selected lab test/patient list edits ...

Select Lab liaison menu Option: <span class="mark">HOSPITAL \<Enter\></span> Location Monitor Tool

\[Extract Locations... - \]

<u><span class="mark">Lab Hospital Location Tools</span> May 06, 2013@14:56:52 Page: 1 of 252</u>

<span class="mark">Lab Hospital Location Definition Extract</span>

Version: 5.2 Build: 16

<u>Hospital Locations currently defined in legacy VistA:</u>

1 : NEW^LOCATION^2^CARDIOLOGY \#6/SPEC^CLINIC^HUNTINGTON VAMC^HUNTINGTON VAMC^MAY

\+ 05, 1992^MAY 24, 2000^ADT ADMINISTRATOR \<UNKNOWN\>^3130506.14565

2 : NEW^LOCATION^17^PULMONARY-CHEST/SPEC^CLINIC^HUNTINGTON VAMC^HUNTINGTON VAMC^

+^^ADT ADMINISTRATOR \<UNKNOWN\>^3130506.14565

3 : NEW^LOCATION^19^SURG-UROLOGY \#5^CLINIC^HUNTINGTON VAMC^HUNTINGTON VAMC^MAY 0

+6, 1988^MAR 12, 2001^ADT ADMINISTRATOR \<UNKNOWN\>^3130506.14565

4 : NEW^LOCATION^30^NURSING/SPEC^CLINIC^HUNTINGTON VAMC^HUNTINGTON VAMC^^^ADT AD

+MINISTRATOR \<UNKNOWN\>^3130506.14565

5 : NEW^LOCATION^42^ONCOLOGY-TUMOR/SPEC^CLINIC^HUNTINGTON VAMC^HUNTINGTON VAMC^^

+^ADT ADMINISTRATOR \<UNKNOWN\>^3130506.14565

6 : NEW^LOCATION^43^LABORATORY^CLINIC^HUNTINGTON VAMC^HUNTINGTON VAMC^^^ADT ADMI

+NISTRATOR \<UNKNOWN\>^3130506.14565

\+ Task Rpt May 05, 2013@11:35 - May 06, 2013@11:35

DE Display Extracted (Raw) Data SX Send Extract File

DM Display Mail Message SM Send Mail Message

AQ Hospital Location Audit Query DS Show LRJ SYS MAP HL TASKMAN RPT sch

AE Accept/edit HL config dates ST Sched LRJ SYS MAP HL TASKMAN RPT

Select Action:Next Screen// <span class="mark">DS \<Enter\></span> Show LRJ SYS MAP HL TASKMAN RPT sch

<u><span class="mark">Lab Hospital Location Tools</span> May 06, 2013@14:56:56 Page: 1 of 1</u>

<span class="mark">LAB Hospital Location Change Audit Task Option Schedule</span>

Version: 5.2 Build: 16

<u>Hospital Location Audit task schedule</u>

OPTION: LRJ SYS MAP HL TASKMAN RPT

TASK ID: 278412

QUEUED TO RUN AT WHAT TIME: MAY 07, 2013@11:35

RESCHEDULING FREQUENCY: 1D

Hospital Location Audit Automated Reporting begin Date: May 06, 2013@11:35

Task Rpt May 05, 2013@11:35 - May 06, 2013@11:35

DE Display Extracted (Raw) Data SX Send Extract File

DM Display Mail Message SM Send Mail Message

AQ Hospital Location Audit Query DS Show LRJ SYS MAP HL TASKMAN RPT sch

AE Accept/edit HL config dates ST Sched LRJ SYS MAP HL TASKMAN RPT

Select Action:Quit// <span class="mark">ST \<Enter\></span> Sched LRJ SYS MAP HL TASKMAN RPT

This action will schedule the 'LRJ SYS MAP HL Change Management TaskMan Report' option \[LRJ SYS MAP HL TASKMAN RPT\] as a background task.

Do you want to do this? NO// <span class="mark">Y \<Enter\></span> YES

This is the date/time you want this option to be started by TaskMan.

QUEUED TO RUN AT WHAT TIME: May 07, 2013@11:35// <span class="mark">T@2030 \<Enter\></span> (MAY 06, 2013@20:30)

RESCHEDULING FREQUENCY: 1D// <span class="mark">2D \<Enter\></span> (MAY 06, 2013@20:30)

<u><span class="mark">Lab Hospital Location Tools</span> May 06, 2013@14:58:31 Page: 1 of 1</u>

<span class="mark">LAB Hospital Location Change Audit Task Option Schedule</span>

Version: 5.2 Build: 16

<u>Hospital Location Audit task schedule</u>

OPTION: LRJ SYS MAP HL TASKMAN RPT

TASK ID: 278429

QUEUED TO RUN AT WHAT TIME: MAY 06, 2013@20:30

RESCHEDULING FREQUENCY: 2D

Hospital Location Audit Automated Reporting begin Date: May 06, 2013@11:35

Task Rpt May 05, 2013@11:35 - May 06, 2013@11:35

DE Display Extracted (Raw) Data SX Send Extract File

DM Display Mail Message SM Send Mail Message

AQ Hospital Location Audit Query DS Show LRJ SYS MAP HL TASKMAN RPT sch

AE Accept/edit HL config dates ST Sched LRJ SYS MAP HL TASKMAN RPT

Select Action:Quit// <span class="mark">\<Enter\></span> QUIT

## Reviewing the LRJ SYS MAP HL TASK RPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When hospital location changes occur, two messages are sent to the LRJ SYS MAP HL TASK REPORT mail group. Review the messages for accuracy. If the report is not accurate, make the appropriate changes in VistA and re-run the report.

![](lr-5-2-425-laboratory-user-guide/018.png) NOTE: Add any users that need to receive messages created by the LRJ SYS MAP HL TASKMAN RPT option to the LRJ SYS MAP HL TASK REPORT mail group (see <u>Table 8</u>).

- The first message contains text file attachments of a caret ("^") delimited *new* and *modified* hospital location data. An example of the message text follows:

> <span id="_Toc282676821" class="anchor"></span>Figure . Monitor Hospital Location Changes—Sample new and edited hospital location (HL) data

> ![](lr-5-2-425-laboratory-user-guide/019.png)

The HLCSM_EXT_NEW_3100224_100553.TXT file contains data such as the following:

> <span id="_Toc282676822" class="anchor"></span>Figure . Monitor Hospital Location Changes—Sample HL change extract data—New locations

NEW^LOCATION^435^GTS TEST WARD 2-A^WARD^DEVVLD^TROY^JAN 11, 2010^JAN 14, 2010^LABUSER,ONE^3100115.101104

NEW^ROOM^435^GTS TEST WARD 2-A^WARD^DEVVLD^TROY^GS^

NEW^BED^435^GTS TEST WARD 2-A^WARD^DEVVLD^TROY^GS^2

NEW^BED^435^GTS TEST WARD 2-A^WARD^DEVVLD^TROY^GS^A-3

NEW^ROOM^435^GTS TEST WARD 2-A^WARD^DEVVLD^TROY^GTS^

NEW^BED^435^GTS TEST WARD 2-A^WARD^DEVVLD^TROY^GTS^3

NEW^BED^435^GTS TEST WARD 2-A^WARD^DEVVLD^TROY^GTS^A-3

NEW^BED^435^GTS TEST WARD 2-A^WARD^DEVVLD^TROY^GTS^A1

NEW^BED^435^GTS TEST WARD 2-A^WARD^DEVVLD^TROY^GTS^A2

NEW^BED^435^GTS TEST WARD 2-A^WARD^DEVVLD^TROY^GTS^A3

NEW^LOCATION^436^TESTER'S ZZ LOCATION^WARD^TROY^TROY^^^LABUSER,ONE^3091006.143329

NEW^LOCATION^437^ZZ GTS TEST TYPE HL^OPERATING ROOM^1 AD^TROY^^^LABUSER,ONE^3091006.144346

The HLCSM_EXT_MOD_3100224_100553.TXT file contains data such as the following:

> <span id="_Toc282676823" class="anchor"></span>Figure . Monitor Hospital Location Changes—Sample HL change extract data—Modified locations

CURRENT^LOCATION^426^ONE'S HL TEST WARD^WARD^TROY^DEVVLD^^^ LABUSER,ONE ^3091006.143848

PREVIOUS^LOCATION^426^^^^^^

CURRENT^ROOM^426^ ONE'S HL TEST WARD^WARD^TROY^DEVVLD^GTS^

PREVIOUS^ROOM^426^^^^^GTS^

CURRENT^BED^426^ ONE'S HL TEST WARD^WARD^TROY^DEVVLD^GTS^3

PREVIOUS^BED^426^^^^^^

CURRENT^BED^426^ ONE'S HL TEST WARD^WARD^TROY^DEVVLD^GTS^A2

PREVIOUS^BED^426^^^^^GS^A-4

- The second message contains *new* and *modified* hospital location (HL) data in a *user readable format*. An example of the message text follows:

> <span id="_Toc282676824" class="anchor"></span>Figure . Monitor Hospital Location Changes—Sample Hospital Location (HL) change message

> ![](lr-5-2-425-laboratory-user-guide/020.png)

## Additional HLCMS Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Ref356296447" class="anchor"></span>Figure . Monitor Hospital Location Changes—Hospital Location Tools option

<u><span class="mark">Lab Hospital Location Tools</span> May 06, 2013@14:56:52 Page: 1 of 252</u>

<span class="mark">Lab Hospital Location Definition Extract</span>

Version: 5.2 Build: 16

<u>Hospital Locations currently defined in legacy VistA:</u>

1 : NEW^LOCATION^2^CARDIOLOGY \#6/SPEC^CLINIC^HUNTINGTON VAMC^HUNTINGTON VAMC^MAY

\+ 05, 1992^MAY 24, 2000^ADT ADMINISTRATOR \<UNKNOWN\>^3130506.14565

2 : NEW^LOCATION^17^PULMONARY-CHEST/SPEC^CLINIC^HUNTINGTON VAMC^HUNTINGTON VAMC^

+^^ADT ADMINISTRATOR \<UNKNOWN\>^3130506.14565

3 : NEW^LOCATION^19^SURG-UROLOGY \#5^CLINIC^HUNTINGTON VAMC^HUNTINGTON VAMC^MAY 0

+6, 1988^MAR 12, 2001^ADT ADMINISTRATOR \<UNKNOWN\>^3130506.14565

4 : NEW^LOCATION^30^NURSING/SPEC^CLINIC^HUNTINGTON VAMC^HUNTINGTON VAMC^^^ADT AD

+MINISTRATOR \<UNKNOWN\>^3130506.14565

5 : NEW^LOCATION^42^ONCOLOGY-TUMOR/SPEC^CLINIC^HUNTINGTON VAMC^HUNTINGTON VAMC^^

+^ADT ADMINISTRATOR \<UNKNOWN\>^3130506.14565

6 : NEW^LOCATION^43^LABORATORY^CLINIC^HUNTINGTON VAMC^HUNTINGTON VAMC^^^ADT ADMI

+NISTRATOR \<UNKNOWN\>^3130506.14565

\+ Task Rpt May 05, 2013@11:35 - May 06, 2013@11:35

DE Display Extracted (Raw) Data SX Send Extract File

DM Display Mail Message SM Send Mail Message

AQ Hospital Location Audit Query DS Show LRJ SYS MAP HL TASKMAN RPT sch

AE Accept/edit HL config dates ST Sched LRJ SYS MAP HL TASKMAN RPT

Select Action:Next Screen//

### DE—Display Extracted (Raw) Data Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the DE—Display Extracted (Raw) Data option \[LRJ SYS MAP HL DISP EXT\] to redisplay a user-readable formatted extract (currently displayed) to its' "raw" extracted format.

### DM—Display Mail Message Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the DM—Display Mail Message option \[LRJ SYS MAP HL DISPLAY MESSAGE\] to format the currently displayed extract in a user-readable format.

### AQ—Hospital Location Audit Query Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the AQ—Hospital Location Audit Query option \[LRJ SYS MAP HL AUDIT QUERY\] to report hospital location changes for a user-entered date range or to re-generate the original Initialization Extract after an Audit Extract report is generated.

### SM—Send Mail Message Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the SM—Send Mail Message option \[LRJ SYS MAP HL SEND MSG\] to email the extract to a specified mail group notifying staff that configuration changes may be needed within Vista applications that subscribe to hospital location files. The email message is in a user-readable format and supports configuration and verification of lab-related hospital locations.

### SX—Send Extract File Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the SX—Send Extract File option \[LRJ SYS MAP HL SEND EXT\] to send the currently defined extract in an email message to a specified mail group. The email message contains two attachment files, which are named in the following scheme:

- HLCMS_EXT_NEW\_*\<date\>*\_*\<time\>*.TXT: Caret-delimited file containing all of the *new* hospital locations added to VistA during the defined report date range.
- HLCMS_EXT_MOD\_*\<date\>*\_*\<time\>*.TXT: Caret-delimited file containing all of the *modified* hospital locations on VistA during the defined report date range.

#### Extract Emails and Outlook

In order to review the text file attachments of the message, perform the following procedure:

1.  Make sure that the FLAGS field (#1) in the DOMAIN file (#4.2) is set to S=Send (IRM assistance may be required).
2.  If allowed, forward the VistA message to Microsoft<sup>®</sup> Outlook.

![](lr-5-2-425-laboratory-user-guide/021.png) NOTE: Some possible restrictions or limitations related to forwarding messages from VistA MailMan to Microsoft<sup>®</sup> Outlook may include:

- Many sites *do not allow* messages to be forwarded to Microsoft<sup>®</sup> Outlook from Test accounts. Sites may only be able to perform this action from Production accounts.
- Some sites *do allow* messages to be forwarded from the Test account to the Production account. If so, then the message can be forwarded to Production and then to Microsoft<sup>®</sup> Outlook.
- In addition, if the message is not received in Microsoft<sup>®</sup> Outlook, the number of lines may need to be increased.
3.  Import the extract files into a review tool (e.g., Microsoft<sup>®</sup> Excel).

### Accept/edit HL Config Dates Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the dates became corrupted or needed to be reset, use the AE—Accept/edit HL config dates option \[LRJ SYS MAP HL ACCEPT CONFIG\] to define the following parameters (user *must* hold the LRJ HL TOOLS MGR key):

- LRJ LSRP HL LAST START DATE
- LRJ LSRP HL LAST END DATE

The AE—Accept/edit HL config dates option \[LRJ SYS MAP HL ACCEPT CONFIG\] is run prior to scheduling the LRJ SYS MAP HL Change Management TaskMan Report option \[LRJ SYS MAP HL TASKMAN RPT\].

The LRJ SYS MAP HL Change Management TaskMan Report option \[LRJ SYS MAP HL TASKMAN RPT\] generates the automated audit report based upon the date defined in the LRJ LSRP HL LAST END DATE parameter. The user defines these dates after verifying that the lab-related hospital locations on VistA match those defined. This serves as the baseline for future changes.

# Laboratory Test File 60 Audit Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Laboratory Test File 60 Audit Tool Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Laboratory Test File 60 Audit Tool \[LRJ SYS MAP AUF60 MANAGER\] monitors changes made to the VistA LABORATORY TEST file (#60). If any item is not working the user can identify changes recently made to this file for the purpose of troubleshooting. This benefits the sites for any future lab capability solution and it leverages VistA Lab Test Order Catalog and Computerized Patient Record System (CPRS).

The Laboratory Test File 60 Audit Tool has pre-defined (mandatory) audit fields and is designed to notify authorized users when a change is made to an audited field in the LABORATORY TEST file (#60). Sites can add and remove *non-mandatory* fields for auditing.

![](lr-5-2-425-laboratory-user-guide/022.png) CAUTION: Auditing for *mandatory* fields *cannot* be turned off using the Laboratory Test File 60 Audit Tool. You can only remove auditing for these mandatory audit fields by direct edits to those entries in the LABORATORY TEST file (#60).

This audit tool has options to automatically (see Section <u>4.2.1</u>) or manually (see Section <u>4.2.2</u>) produce reports that display changes that have occurred in the LABORATORY TEST file (#60) for the specified timeframe. These reports are sent to individual users or mail groups.

To access the Laboratory Test File 60 Audit Tool:

1.  From the Lab liaison menu \[LRLIAISON\], at the "Select Lab liaison menu Option:" prompt, select the File 60 Audit Manager option \[LRJ SYS MAP AUD MANAGER\].
2.  The following screen displays:

> <span id="_Ref356551009" class="anchor"></span>Figure . Laboratory Test File 60 Audit Tool—File 60 Audit Manager option

Select Laboratory DHCP Menu Option: <span class="mark">^LAB LIAISON MENU</span>

ANT Add a new internal name for an antibiotic

ANTE Edit an Antibiotic

BCF Lab Bar Code Label Formatter

BCZ Lab Zebra Label Utility

DATA Add a new data name

HDR Recover/Transmit Lab HDR Result Messages

LNC LOINC Main Menu ...

MOD Modify an existing data name

SMGR Lab Shipping Management Menu ...

Add a new WKLD code to file

AP Microfiche Archive

Archiving Menu ...

Check files for inconsistencies

Check patient and lab data cross pointers

Download Format for Intermec Printer

Edit atomic tests

Edit cosmic tests

Edit Inactive Date - COLLECTION SAMPLE

Edit Inactive Date - TOPOGRAPHY FIELD

File 60 Audit Manager

File list for lab

Hospital Location Monitor Tool

LAB ROUTINE INTEGRITY MENU ...

Lab Tests and CPT Report

LIM workload menu ...

Manually compile WKLD and workload counts

OE/RR interface parameters ...

Outline for one or more files

Print AMA CPT Panel Pending List

Re-index Antimicrobial Suscept File (62.06)

Restart processing of instrument data

Turn on site workload statistics

Turn on workload stats for accession area

User selected lab test/patient list edits ...

Select Lab liaison menu Option: <span class="mark">FILE 60 \<Enter\></span> Audit Manager

<u><span class="mark">Lab File 60 Audit Menu</span> May 09, 2013@08:00:40 Page: 0 of 0</u>

<span class="mark">Lab File 60 Audit Manager</span>

Version: 5.2 Build: 22

Last Task Rpt May 08, 2013@07:30 - May 09, 2013@07

SF Set Audited Flag for Fields SM Send Display in Mail

LF List Audited Fields SX Send Extract File in Mail

DF Display File 60 Changes

## File 60 Audit Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To receive audit file change reports, use the following options:

- Set up reports to *run automatically* using TaskMan (see Section <u>4.2.1</u>).
- Run reports *manually* as needed using the DF—Display File 60 Changes \[LRJ SYS MAP AUD DISPLAY FILE 60 CHANGES\] (see Section <u>4.6</u>).

### Schedule Audit Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use TaskMan to automatically run audit change reports and send the reports in mail messages to designated users (see Section <u>7</u>, "<u>Mail Group Maintenance</u>"). Set the frequency of the following tasked options to meet site needs:

| Tasked options              | Produces Report                                  |
|-----------------------------|--------------------------------------------------|
| LRJ BACKGROUND F60 AUD FILE | File 60 Audit in delimited file (extract) format |
| LRJ BACKGROUND F60 AUDIT    | File 60 Audit in display format                  |

<span id="_Toc309210935" class="anchor"></span>Table . Laboratory Test File 60 Audit Tool—Schedule Audit Reports

To schedule audit reports to run automatically using TaskMan, perform the following procedure:

1.  At the "Select Systems Manager Menu Option:" prompt, select the Taskman Management menu \[XUTM MGR\].
2.  At the "Select Taskman Management Option:" prompt, select the Schedule/Unschedule Options option \[XUTM SCHEDULE\].
3.  At the "Select OPTION to schedule or reschedule:" prompt, enter LRJ BACK.
4.  At the "CHOOSE 1-3:" prompt, select the appropriate option number:
- 1—LRJ BACKGROUND F60 AUD FILE \[TaskMan file format file 60 audits\].
- 2—LRJ BACKGROUND F60 AUDIT \[TaskMan File 60 Audit in Display Format\].
5.  At the "Are you adding 'LRJ BACKGROUND F60 AUD FILE' as a new OPTION SCHEDULING (the *nnXX*)? No//" prompt, enter YES.
6.  The Edit Option Schedule screen displays. Complete the following fields:
1.  At the "QUEUED TO RUN AT WHAT TIME:" field, enter the date/time you want the option to start.
2.  At the "DEVICE FOR QUEUED JOB OUTPUT:" field, press Enter.
3.  At the "QUEUED TO RUN ON VOLUME SET:" field, press Enter.
4.  At the "RESCHEDULING FREQUENCY:" field, enter how often you want the report to run.
5.  Tab to the "COMMAND" field, enter Save, and then Exit.
7.  Repeat Steps 3-6 for the remaining tasked options \[LRJ BACKGROUND F60 AUDIT\]  
    > (choice number 2).

> <span id="_Toc309210810" class="anchor"></span>Figure . Laboratory Test File 60 Audit Tool—Using TASKMAN to schedule audit reports to run

Select Systems Manager Menu Option: <span class="mark">TASK \<Enter\></span> man Management

<span class="mark">Schedule/Unschedule Options</span>

One-time Option Queue

Taskman Management Utilities ...

List Tasks

Dequeue Tasks

Requeue Tasks

Delete Tasks

Print Options that are Scheduled to run

Cleanup Task List

Print Options Recommended for Queueing

Select Taskman Management Option: <span class="mark">SCHEDULE \<Enter\></span> /Unschedule Options

Select OPTION to schedule or reschedule: <span class="mark">LRJ BACK</span>

<span class="mark">1 LRJ BACKGROUND F60 AUD FILE</span> TaskMan file format file 60 audits

2 LRJ BACKGROUND F60 AUDIT TaskMan File 60 Audit in Display Format

CHOOSE 1-2: <span class="mark">1 \<Enter\></span> LRJ BACKGROUND F60 AUD FILE TaskMan file format file 60 audits

Are you adding 'LRJ BACKGROUND F60 AUD FILE' as

a new OPTION SCHEDULING (the *nnnXX*)? No// <span class="mark">YES \<Enter\></span> (Yes)

Edit Option Schedule

<u>Option Name</u>: LRJ BACKGROUND F60 AUD FILE

Menu Text: TaskMan file format file 60 audit TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME:

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY:

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

8.  Assign users who need to receive the File 60 audit change reports to the appropriate mail groups (see Section <u>7</u>, "<u>Mail Group Maintenance</u>"):

<table>
<caption><p><span id="_Toc309210936" class="anchor"></span>Table . Laboratory Test File 60 Audit Tool—Mail Groups</p></caption>
<colgroup>
<col style="width: 57%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th>Report Name</th>
<th>Mail Group</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>File 60 Audit in list format (AUF60)</td>
<td>LRJ AUF60 AUDIT TASK REPORT<br />
(see <u>Table 8</u>)</td>
</tr>
<tr class="even">
<td>File 60 Audit in delimited file (extract) format (AUF60XT)</td>
<td>LRJ AUF60XT AUDIT TASK REPORT<br />
(see <u>Table 8</u>)</td>
</tr>
</tbody>
</table>

<span id="_Toc309210936" class="anchor"></span>Table . Laboratory Test File 60 Audit Tool—Mail Groups

![](lr-5-2-425-laboratory-user-guide/023.png) NOTE: If "Tasked Report has not run!" displays on an Audit tool screen, it means one of the following:

- The site has not scheduled the report to run.
- The site scheduled the report, but it has not run yet.
- There may be a problem with how the site defined the task in TaskMan—see TaskMan documentation for troubleshooting (e.g., a date/time that the report should run was not specified).
- It may mean that the report was scheduled correctly in TaskMan, but TaskMan is not running.

### Manually Run File 60 Audit Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run reports manually, use the following Audit tools options:

<table>
<caption><p><span id="_Ref330969500" class="anchor"></span>Table . Laboratory Test File 60 Audit Tool—Options and reports</p></caption>
<colgroup>
<col style="width: 55%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th>Report</th>
<th>Option</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>File 60 Audit in list format (AUF60)</td>
<td><strong>SM—Send Display in Mail<br />
</strong>(Section <u>4.7.1</u>)</td>
</tr>
<tr class="even">
<td>File 60 Audit in delimited file (extract) format (AUF60XT)</td>
<td><strong>SX—Send Extract File Message<br />
</strong>(Section <u>4.7.2</u>)</td>
</tr>
</tbody>
</table>

<span id="_Ref330969500" class="anchor"></span>Table . Laboratory Test File 60 Audit Tool—Options and reports

![](lr-5-2-425-laboratory-user-guide/024.png) REF: Each section reference (Section xyz) in <u>Table 6</u> links to the detailed procedure content. Use Microsoft<sup>®</sup> Word's built-in [navigation](#navigation) capabilities to navigate back and forth between the table and detailed information.

## File 60 Audit Tool Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](lr-5-2-425-laboratory-user-guide/025.png) REF: Each section reference in the following list links to the detailed procedure content. Use Microsoft<sup>®</sup> Word's built-in [navigation](#navigation) capabilities to navigate back and forth between the list and detailed step.

The Laboratory Test File 60 Audit Tool sets up fields in the LABORATORY TEST file (#60) that are audited for changes (see the LF—List Audited Fields option in Section <u>4.5</u>). This audit tool allows the user to do the following:

- SF—Set Audited Flag for Fields \[LRJ SYS MAP AUD SET FILE 60 AUDITED FLAG\]: Add or turn off auditing for *non-mandatory* fields (Section <u>4.4</u>).

> ![](lr-5-2-425-laboratory-user-guide/026.png) CAUTION: Auditing for *mandatory* fields *cannot* be turned off using the Laboratory Test File 60 Audit Tool.

- LF—List Audited Fields \[LRJ SYS MAP AUD LIST AUDITED FIELDS\]: Display a list of audited fields (Section <u>4.5</u>).
- DF—Display File 60 Changes \[LRJ SYS MAP AUD DISPLAY FILE 60 CHANGES\]: Display file 60 changes for specific tests, all tests, and date range (Section <u>4.6</u>).
- SM—Send Display in Mail \[LRJ SYS MAP AUF60 SEND DISPLAY MESSAGE\]: Send the file 60 changes (displayed in the DF option) as a VistA mail message (Section <u>4.7.1</u>).
- SX—Send File 60 Audit Delimited File option \[LRJ SYS MAP AUF60 SEND FILE MESSAGE\]: Send the audits (displayed in the DF option) as a delimited file (Section <u>4.7.2</u>).

## Set Additional File 60 Fields to be Audited

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the SF—Set Audited Flag for Fields option \[LRJ SYS MAP AUD SET FILE 60 AUDITED FLAG\] to toggle auditing on or off for non-mandatory (optional) fields in the LABORATORY TEST file (#60).

### Set Auditing for Optional Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To set additional fields to be audited, perform the following procedure:

1.  From the Lab liaison menu \[LRLIAISON\], at the "Select Lab liaison menu Option:" prompt, select the File 60 Audit Manager option \[LRJ SYS MAP AUD MANAGER\].
8.  At the "Select Action: Quit//" prompt, select the SF—Set Audited Flag for Fields option \[LRJ SYS MAP AUD SET FILE 60 AUDITED FLAG\].
9.  At the "Field" prompt, enter the name or number of the field you want to audit.
10. (Optional) The "Sub-File field" prompt is only displayed if the field entered in Step 3 is a Multiple.  
      
    If you entered a Multiple field in Step 3, at the "Sub-File field" prompt, enter the name or number of the sub-field you want to audit.
11. At the "Do you wish to turn auditing ON for this field?? No" prompt, enter YES.

> <span id="_Ref356552898" class="anchor"></span>Figure . Laboratory Test File 60 Audit Tool—Set Audited Flag option using field number (1 of 2)

Select Supervisor menu Option: <span class="mark">^LAB LIAISON MENU</span>

ANT Add a new internal name for an antibiotic

ANTE Edit an Antibiotic

BCF Lab Bar Code Label Formatter

BCZ Lab Zebra Label Utility

DATA Add a new data name

HDR Recover/Transmit Lab HDR Result Messages

LNC LOINC Main Menu ...

MOD Modify an existing data name

SMGR Lab Shipping Management Menu ...

Add a new WKLD code to file

AP Microfiche Archive

Archiving Menu ...

Check files for inconsistencies

Check patient and lab data cross pointers

Download Format for Intermec Printer

Edit atomic tests

Edit cosmic tests

Edit Inactive Date - COLLECTION SAMPLE

Edit Inactive Date - TOPOGRAPHY FIELD

<span class="mark">File 60 Audit Manager</span>

File list for lab

Hospital Location Monitor Tool

LAB ROUTINE INTEGRITY MENU ...

Lab Tests and CPT Report

LIM workload menu ...

Manually compile WKLD and workload counts

OE/RR interface parameters ...

Outline for one or more files

Print AMA CPT Panel Pending List

Re-index Antimicrobial Suscept File (62.06)

Restart processing of instrument data

Turn on site workload statistics

Turn on workload stats for accession area

User selected lab test/patient list edits ...

Select Lab liaison menu Option: <span class="mark">FILE 60 \<Enter\></span> Audit Manager

<u><span class="mark">Lab File 60 Audit Menu</span> May 07, 2013@08:55:01 Page: 0 of 0</u>

<span class="mark">Lab File 60 Audit Manager</span>

Version: 5.2 Build: 16

Last Task Rpt May 06, 2013@07:30 - May 07, 2013@07

SF Set Audited Flag for Fields SM Send Display in Mail

LF List Audited Fields SX Send Extract File in Mail

DF Display File 60 Changes

Select Action:Quit// <span class="mark">SF \<Enter\></span> Set Audited Flag for Fields

Field: <span class="mark">100 \<Enter\></span> SITE/SPECIMEN

Sub-File SITE/SPECIMEN Field: <span class="mark">??</span>

Choose from:

.01 SITE/SPECIMEN

1 REFERENCE LOW

2 REFERENCE HIGH

<span class="mark">3 CRITICAL LOW</span>

4 CRITICAL HIGH

5.5 INTERPRETATION

6 UNITS

7 TYPE OF DELTA CHECK

8 DELTA VALUE

9 DEFAULT VALUE

9.2 THERAPEUTIC LOW

9.3 THERAPEUTIC HIGH

10 \*AMIS/RCS 14-4

13 USE FOR REFERENCE TESTING

20 FOREIGN COMPUTER SYSTEM

95.3 LOINC CODE

96 SPECIMEN CPT

Sub-File SITE/SPECIMEN Field: <span class="mark">3 \<Enter\></span> CRITICAL LOW

File 60.01 - Field 3 is not currently audited.

Do you wish to turn auditing ON for this field?? No// <span class="mark">Y \<Enter\></span> YES

<span class="mark">CHANGE MADE: File 60.01 - Field 3 is now audited</span>

The following screen shows how to use the SF—Set Audited Flag for Fields option \[LRJ SYS MAP AUD SET FILE 60 AUDITED FLAG\] using the field name:

> <span id="_Ref356552908" class="anchor"></span>Figure . Laboratory Test File 60 Audit Tool—Set Audited Flag option using field name  
> (2 of 2)

<u><span class="mark">Lab File 60 Audit Menu</span> May 07, 2013@09:05:47 Page: 0 of 0</u>

<span class="mark">Lab File 60 Audit Manager</span>

Version: 5.2 Build: 16

Enter ?? for more actions

SF Set Audited Flag for Fields SM Send Display in Mail

LF List Audited Fields SX Send Extract File in Mail

DF Display File 60 Changes

Select Action:Quit// <span class="mark">SF \<Enter\></span> Set Audited Flag for Fields

Field: <span class="mark">SITE</span>

1 SITE NOTES DATE

2 SITE/SPECIMEN

CHOOSE 1-2: <span class="mark">2 \<Enter\></span> SITE/SPECIMEN

Sub-File SITE/SPECIMEN Field: <span class="mark">?</span>

Answer with SITE/SPECIMEN SUB-FIELD NUMBER, or LABEL, or INDEX, or

GROUP

Do you want the entire 17-Entry SITE/SPECIMEN SUB-FIELD List? <span class="mark">Y \<Enter\></span> (Yes)

Choose from:

.01 SITE/SPECIMEN

1 REFERENCE LOW

2 REFERENCE HIGH

3 CRITICAL LOW

<span class="mark">4 CRITICAL HIGH</span>

5.5 INTERPRETATION

6 UNITS

7 TYPE OF DELTA CHECK

8 DELTA VALUE

9 DEFAULT VALUE

9.2 THERAPEUTIC LOW

9.3 THERAPEUTIC HIGH

10 \*AMIS/RCS 14-4

13 USE FOR REFERENCE TESTING

20 FOREIGN COMPUTER SYSTEM

95.3 LOINC CODE

96 SPECIMEN CPT

Sub-File SITE/SPECIMEN Field: <span class="mark">CRITICAL HIGH</span>

<span class="mark">File 60.01 - Field 4 is not currently audited.</span>

Do you wish to turn auditing <span class="mark">ON</span> for this field?? No// <span class="mark">Y \<Enter\></span> YES

<span class="mark">CHANGE MADE: File 60.01 - Field 4 is now audited</span>

### Delete Auditing from Optional Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the SF—Set Audited Flag for Fields option \[LRJ SYS MAP AUD SET FILE 60 AUDITED FLAG\] to turn off auditing for non-mandatory fields in the LABORATORY TEST file (#60).

To turn off the audit flag for *non-mandatory* fields, perform the following procedure from the File 60 Audit screen:

1.  From the File 60 Audit screen \[LRJ SYS MAP AUF60 MENU\], select the SF—Set Audited Flag for Fields option \[LRJ SYS MAP AUD SET FILE 60 AUDITED FLAG\].
12. At the "Field" prompt, enter the name or number of the field you want to stop auditing.
13. (Optional) The "Sub-File field" prompt is only displayed if the field entered in Step 2 is a Multiple.  
      
    If you entered a Multiple field in Step 2, at the "Sub-File field" prompt, enter the name or number of the sub-field you want to stop auditing.
14. At the "Do you wish to turn auditing OFF for this field?? No" prompt, enter YES.

> <span id="_Ref356553420" class="anchor"></span>Figure . Laboratory Test File 60 Audit Tool—Turning off the audit flag for optional fields

<u><span class="mark">Lab File 60 Audit Menu</span> May 07, 2013@10:19:12 Page: 0 of 0</u>

<span class="mark">Lab File 60 Audit Manager</span>

Version: 5.2 Build: 16

Last Task Rpt May 06, 2013@07:30 - May 07, 2013@07

SF Set Audited Flag for Fields SM Send Display in Mail

LF List Audited Fields SX Send Extract File in Mail

DF Display File 60 Changes

Select Action:Quit// <span class="mark">SF \<Enter\></span> Set Audited Flag for Fields

Field: <span class="mark">100 \<Enter\></span> SITE/SPECIMEN

Sub-File SITE/SPECIMEN Field: <span class="mark">3 \<Enter\></span> CRITICAL LOW

<span class="mark">File 60.01 - Field 3 is already audited.</span>

Do you wish to turn auditing <span class="mark">OFF</span> for this field?? No// <span class="mark">Y \<Enter\></span> YES

<span class="mark">CHANGE MADE: File 60.01 - Field 3 is now NOT audited</span>

![](lr-5-2-425-laboratory-user-guide/027.png) CAUTION: Auditing for *mandatory* fields *cannot* be turned off using the Laboratory Test File 60 Audit Tool.

If you try to turn off the audit flag for a required audit field, the following screen displays:

> <span id="_Ref356553386" class="anchor"></span>Figure . Laboratory Test File 60 Audit Tool—Turning off the audit flag for required audit fields

<u><span class="mark">Lab File 60 Audit Menu</span> May 07, 2013@10:21:27 Page: 0 of 0</u>

<span class="mark">Lab File 60 Audit Manager</span>

Version: 5.2 Build: 16

Enter ?? for more actions

SF Set Audited Flag for Fields SM Send Display in Mail

LF List Audited Fields SX Send Extract File in Mail

DF Display File 60 Changes

Select Action:Quit// <span class="mark">SF \<Enter\></span> Set Audited Flag for Fields

Field: <span class="mark">100 \<Enter\></span> SITE/SPECIMEN

Sub-File SITE/SPECIMEN Field: ref

1 REFERENCE HIGH

2 REFERENCE LOW

CHOOSE 1-2: <span class="mark">1 \<Enter\></span> REFERENCE HIGH

<span class="mark">'SF' cannot be used to turn auditing off for any required audit field.</span>

Sub-File SITE/SPECIMEN Field:

## Display List of Audited Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the LF—List Audited Fields option \[LRJ SYS MAP AUD LIST AUDITED FIELDS\] to display the fields that are being audited—mandatory audit fields and optional fields that have been added. Mandatory audit fields are indicated by an asterisk (\*) after the field name.

To display fields that are being audited, perform the following procedure:

1.  Navigate to the File 60 Audit Menu screen.
15. At the "Select Action: Quit//" prompt, select the LF—List Audited Fields option \[LRJ SYS MAP AUD LIST AUDITED FIELDS\].
16. At the "Select Action:Next Screen//" prompt, press Enter to display additional audited fields.
17. Review the Audit column. If any mandatory fields (indicated by \*) are listed as NOT AUDITED, turn the auditing back on using VA FileMan.

> <span id="_Ref356553597" class="anchor"></span>Figure . Laboratory Test File 60 Audit Tool—Display List of Audit Fields option

<span class="mark">Lab File 60 Audit Menu</span> May 07, 2013@13:54:16 Page: 1 of 2

<span class="mark">List of Audited Fields</span>

Asterisk (\*) beside field name denotes required field for audit

Field File Name Field Name Audit

60.01 LABORATORY TEST NAME\* YES, ALWAYS

60.3 LABORATORY TEST TYPE\* YES, ALWAYS

<span class="mark">60.4 LABORATORY TEST SUBSCRIPT\* NO</span>

60.8 LABORATORY TEST UNIQUE COLLECTION SAMPLE\* YES, ALWAYS

60.17 LABORATORY TEST HIGHEST URGENCY ALLOWED\* YES, ALWAYS

60.18 LABORATORY TEST FORCED URGENCY\* YES, ALWAYS

60.64.1 LABORATORY TEST RESULT NLT CODE\* YES, ALWAYS

60.60.01.01 SITE/SPECIMEN SITE/SPECIMEN\* YES, ALWAYS

60.60.01.1 SITE/SPECIMEN REFERENCE LOW\* YES, ALWAYS

60.60.01.2 SITE/SPECIMEN REFERENCE HIGH\* YES, ALWAYS

60.60.01.95.3 SITE/SPECIMEN LOINC CODE\* YES, ALWAYS

60.60.02.01 LAB TEST INCLUDED I LAB TEST\* YES, ALWAYS

60.60.03.01 COLLECTION SAMPLE COLLECTION SAMPLE\* YES, ALWAYS

60.60.1.01 SYNONYM SYNONYM\* YES, ALWAYS

60.60.11.01 ACCESSION AREA INSTITUTION\* YES, ALWAYS

\+ Enter ?? for more actions

SF Set Audited Flag for Fields SM Send Display in Mail

LF List Audited Fields SX Send Extract File in Mail

DF Display File 60 Changes

Select Action:Next Screen//

## Display File 60 Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the DF—Display File 60 Changes option \[LRJ SYS MAP AUD DISPLAY FILE 60 CHANGES\] to display changes made to LABORATORY TEST file (#60). The user can specify certain tests or all tests and the date range to be displayed.

To display changes to the LABORATORY TEST file (#60), perform the following procedure from the File \#60 Audit Menu screen:

1.  From the File \#60 Audit Menu screen \[LRJ SYS MAP AUF60 MENU\], select the DF—Display File 60 Changes option \[LRJ SYS MAP AUD DISPLAY FILE 60 CHANGES\].
18. At the "Select LABORATORY TEST NAME:" prompt, enter a specific test name or press Enter to display changes to all tests.
19. At the "Select Start date: TODAY//" prompt, enter the appropriate start date (e.g., T-30).
20. At the "Select End date: NOW//" prompt, press Enter for the report to end today. New and modified entries display.

> <span id="_Ref356553820" class="anchor"></span>Figure . Laboratory Test File 60 Audit Tool—Display File 60 Changes option

<span class="mark">Lab File 60 Audit Menu</span> May 08, 2013@08:34:31 Page: 0 of 0

<span class="mark">Lab File 60 Audit Manager</span>

Version: 5.2 Build: 22

Last Task Rpt May 07, 2013@07:30 - May 08, 2013@07

SF Set Audited Flag for Fields SM Send Display in Mail

LF List Audited Fields SX Send Extract File in Mail

DF Display File 60 Changes

Select Action:Quit// <span class="mark">DF \<Enter\></span> Display File 60 Changes

Select LABORATORY TEST NAME: <span class="mark">\<Enter\></span>

ALL TESTS

Select Start date: TODAY//<span class="mark">T-90 \<Enter\></span> (FEB 07, 2013)

Select End date: NOW// <span class="mark">\<Enter\></span> (MAY 08, 2013@08:35:16)

...HMMM, LET ME THINK ABOUT THAT A MOMENT...

<span class="mark">Lab File 60 Audit Menu</span> May 08, 2013@08:35:16 Page: 1 of 4

<span class="mark">Laboratory Test File (#60) Changes</span>

Date Range: Feb 07, 2013 to May 08, 2013@08:35:16

DT RECORDED USER IEN(s)

File 60 Audit - From Feb 07, 2013 to May 08, 2013@08:35:16

New Entries

Feb 25, 2013@12:47:34 LABUSER,ONE 6276

FIELD NAME: NAME

TEST NAME: ZZCULTURE,FEB

NEW VALUE: ZZCULTURE,FEB

OLD VALUE: \<no previous value\>

Feb 25, 2013@12:47:36 LABUSER,ONE 6276

FIELD NAME: SUBSCRIPT

TEST NAME: ZZCULTURE,FEB

NEW VALUE: MICROBIOLOGY

OLD VALUE: \<no previous value\>

Feb 25, 2013@12:47:41 LABUSER,ONE 6276

\+ Last Task Rpt May 07, 2013@07:30 - May 08, 2013@07

SF Set Audited Flag for Fields SM Send Display in Mail

LF List Audited Fields SX Send Extract File in Mail

DF Display File 60 Changes

Select Action:Next Screen//

## Send File 60 Changes in Mail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following report options are available:

- SM—Send Display as Mail Message option \[LRJ SYS MAP AUF60 SEND DISPLAY MESSAGE\]: Send audit information in "display" format as a VistA mail message.
- SX—Send File 60 Audit Delimited File option \[LRJ SYS MAP AUF60 SEND FILE MESSAGE\]: Send audit information in attachments (new entries and modified entries) containing delimited files to an Outlook email account.

### Send Display as Mail Message Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the SM—Send Display as Mail Message option \[LRJ SYS MAP AUF60 SEND DISPLAY MESSAGE\] to send new and modified audit information in "display" format as a mail message.

To send the Display File 60 Changes list in display format in a mail message, perform the following procedure:

1.  From the File \#60 Audit screen \[LRJ SYS MAP AUF60 MENU\], at the "Select Action: Next Screen//" prompt, select the SM—Send Display as Mail Message option \[LRJ SYS MAP AUF60 SEND DISPLAY MESSAGE\].
21. At the "Send mail to: *firstname.lastname*//" prompt, press Enter.
22. At the "Select basket to send to: IN//" prompt, press Enter.
23. At the "And Send to:" prompt, enter LRJ AUF60 AUDIT TASK REPORT mail group and any additional recipients.

> <span id="_Ref356556133" class="anchor"></span>Figure . Laboratory Test File 60 Audit Tool—Send Display in Mail option

<span class="mark">File 60 Audit Audit Message</span> May 08, 2013@08:37:22 Page: 1 of 4

<span class="mark">Laboratory Test File (#60) Changes</span>

Date Range: Feb 07, 2013 to May 08, 2013@08:35:16

DT RECORDED USER IEN(s)

File 60 Audit - From Feb 07, 2013 to May 08, 2013@08:35:16

New Entries

Feb 25, 2013@12:47:34 LABUSER,ONE 6276

FIELD NAME: NAME

TEST NAME: ZZCULTURE,FEB

NEW VALUE: ZZCULTURE,FEB

OLD VALUE: \<no previous value\>

Feb 25, 2013@12:47:36 LABUSER,ONE 6276

FIELD NAME: SUBSCRIPT

TEST NAME: ZZCULTURE,FEB

NEW VALUE: MICROBIOLOGY

OLD VALUE: \<no previous value\>

Feb 25, 2013@12:47:41 LABUSER,ONE 6276

\+ Enter ?? for more actions

LF List Audited Fields SX Send Extract File in Mail

DF Display File 60 Changes

Select Action:Next Screen// <span class="mark">SM \<Enter\></span> Send Display in Mail

Send mail to: LABUSER,ONE// <span class="mark">\<Enter\></span> LABUSER,ONE

Select basket to send to: IN// <span class="mark">\<Enter\></span>

And Send to: <span class="mark">\<Enter\></span>

### Send Extract File as Mail Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the SX—Send File 60 Audit Delimited File option \[LRJ SYS MAP AUF60 SEND FILE MESSAGE\] to send audit information in attachments to an Outlook email account. One attachment contains *new* entries; the other attachment contains *modified* entries.

To send the Display File 60 Changes list in delimited file attachments in a mail message, perform the following procedure:

1.  At the "Select Action: Next Screen//" prompt, select the SX—Send File 60 Audit Delimited File option \[LRJ SYS MAP AUF60 SEND FILE MESSAGE\].
24. At the "Send mail to: *firstname.lastname*//" (VistA mailman account) prompt, press Enter.
25. At the "Select basket to send to: IN//" prompt, press Enter.
26. At the "And Send to:" prompt, enter a VA MailMan mail group (e.g., G.LRJ AUF60XT AUDIT TASK REPORT) or user, and any additional recipients. If allowed, sites can also forward the message to Outlook by entering their Outlook account information (e.g., firstname.lastname@va.gov).

![](lr-5-2-425-laboratory-user-guide/028.png) NOTE: Some sites do *not* allow messages to be sent from the Test account to Outlook. If allowed, sites can forward the message from VistA MailMan to Outlook to view the extract in a readable format (see Section <u>3.4.5.1</u>). In addition, if the message is *not* received in Outlook, the number of lines may need to be increased.

> <span id="_Ref356556585" class="anchor"></span>Figure . Laboratory Test File 60 Audit Tool—Send Extract File in Mail option

<span class="mark">Lab File 60 Audit Menu</span> May 08, 2013@08:52:37 Page: 1 of 4

<span class="mark">Laboratory Test File (#60) Changes</span>

Date Range: Feb 07, 2013 to May 08, 2013@08:52:37

DT RECORDED USER IEN(s)

File 60 Audit - From Feb 07, 2013 to May 08, 2013@08:52:37

New Entries

Feb 25, 2013@12:47:34 LABUSER,ONE 6276

FIELD NAME: NAME

TEST NAME: ZZCULTURE,FEB

NEW VALUE: ZZCULTURE,FEB

OLD VALUE: \<no previous value\>

Feb 25, 2013@12:47:36 LABUSER,ONE 6276

FIELD NAME: SUBSCRIPT

TEST NAME: ZZCULTURE,FEB

NEW VALUE: MICROBIOLOGY

OLD VALUE: \<no previous value\>

Feb 25, 2013@12:47:41 LABUSER,ONE 6276

\+ Last Task Rpt May 07, 2013@07:30 - May 08, 2013@07

DF Display File 60 Changes

Select Action:Next Screen// <span class="mark">SX \<Enter\></span> Send Extract File in Mail

Send mail to: LABUSER,ONE// <span class="mark">one.labuser@va.gov \<Enter\></span> GK.VA.GOV via FO-BAYPINES.MV

And Send to:

> <span id="_Ref321489262" class="anchor"></span>Figure . Laboratory Test File 60 Audit Tool—Send Extract File in Mail: Sample Outlook Email

Extract Generated......: May 08, 2013@08:52:37

Extract Requested......: File 60 Audit - From Feb 07, 2013 to May 08, 2013@08:52:37

Attached LMOF NEW File 60 Audit Entries: <span class="mark">AUF60_EXT_NEW\_*\<date\>*\_*\<time\>*.csv</span>

Attached LMOF MODIFIED File 60 Audit Entries: <span class="mark">AUF60_EXT_MOD\_*\<date\>*\_*\<time\>*.csv</span>

# Monitor Laboratory Test File Changes Affecting Quick Orders (File 60 Quick Order API)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Monitor Laboratory Test File Changes Affecting Quick Orders Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Laboratory users requested that when certain fields are updated in the LABORATORY TEST (#60) file, it triggers a CPRS call (Application Program Interface \[API\]) to search for quick orders that contain the test that was updated. If any are found, the appropriate personnel are notified. The trigger fields in the LABORATORY TEST file (#60) are:

- NAME (#.01)
- TYPE (#3)
- HIGHEST URGENCY ALLOWED (#17)
- FORCED URGENCY (#18)
- COLLECTION SAMPLE (#300)

Laboratory Patch LR\*5.2\*425 supplies the following components:

- LRJ QUICK ORDER CHECK option—Scheduled to search (audit) the LABORATORY TEST file (#60) to see if these fields have been edited.

![](lr-5-2-425-laboratory-user-guide/029.png) NOTE: This option was primarily intended to notify the Clinical Application Coordinators (CACs) that a laboratory test contained in a quick order was changed. Unless the laboratory staff is added to the OR CACS mail group, they will not get the notifications.

- LRJSAUO routine—Searches for the specified test and notifies the members of the OR CACS mail group. Recipients are notified of the quick order name and whether it is active or inactive.

## Monitor Laboratory Test File Changes Affecting Quick Orders Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The automatic notification process is as follows:

1.  User changes one or more of the monitored fields in the LABORATORY TEST file (#60).
2.  Software automatically triggers a search through CPRS orderables looking for quick orders that contain the test that was updated.

![](lr-5-2-425-laboratory-user-guide/030.png) NOTE: If the site performed audits on the LABORATORY TEST file (#60) *prior* to the installation of the Laboratory Test File Changes Affecting Quick Orders Monitoring option, these audits shall *not* be included in the CPRS orderable items search.

3.  If any quick orders are found, the system sends a notification to the OR CACS mail group, which contains clinicians and Clinical Application Coordinators (CACs). The notification includes:
- Name—Quick order name.
- Status—Whether it is active or inactive.

![](lr-5-2-425-laboratory-user-guide/031.png) NOTE: Laboratory staff members are not notified of quick order changes, since they do not order in CPRS.  
  
In the future, owners of *personal* quick orders that are affected by changes to the LABORATORY TEST file (#60) will be identified in the VistA MailMan message sent to the OR CACS mail group.

| Options                   | Activities                                                                                                                                                                                                                                               |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Option Name           | LRJ QUICK ORDER CHECK                                                                                                                                                                                                                                |
| Menu Text Description | LRJ QUICK ORDER SEARCH                                                                                                                                                                                                                                   |
| Option Definition     | This option should be scheduled. It searches the Lab 60 audit for tests where certain fields have been edited. If a test is found where those fields have been changed, the routine calls a CPRS API to determine if they are included in a quick order. |

<span id="_Toc366647083" class="anchor"></span>Table . Monitor Laboratory Test File Changes Affecting Quick Orders—LRJ QUICK ORDER CHECK option

## Verify/Re-schedule the LRJ QUICK ORDER CHECK Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The frequency for running the LRJ QUICK ORDER CHECK option may vary from site-to-site and should be based on the frequency of the local LABORATORY TEST file (#60) changes. If laboratory test changes are made daily, the quick order check frequency should be at least daily or even multiple times during the day. If laboratory test changes are not made daily, the frequency of the quick order check should be changed to reflect a longer period. Sites should err on the side of scheduling the quick order check to run too often and then adjust the schedule to accommodate the frequency of changes made to laboratory tests.

The frequency of running the quick order check can be changed as needed. For example, when making large changes like adding an order catalog for a new reference lab, you might want to run the quick order check more often until all the changes are made.

### Schedule LRJ QUICK ORDER CHECK

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use TaskMan to automatically run the LRJ QUICK ORDER CHECK option and send the reports in mail messages to designated users (see Section <u>7</u>). Set the frequency of the following tasked options to meet site needs:

To schedule LRJ QUICK ORDER CHECK to run automatically using TaskMan, perform the following procedure:

1.  At the "Select Systems Manager Menu Option:" prompt, select the Taskman Management menu \[XUTM MGR\].
2.  At the "Select Taskman Management Option:" prompt, select the Schedule/Unschedule Options option \[XUTM SCHEDULE\].
3.  At the "Select OPTION to schedule or reschedule:" prompt, enter LRJ QUICK ORDER CHECK.
4.  At the "Are you adding 'LRJ QUICK ORDER CHECK' as a new OPTION SCHEDULING (the *nnXX*)? No//" prompt, enter YES.
5.  The Edit Option Schedule screen displays. Complete the following fields:
1.  At the "QUEUED TO RUN AT WHAT TIME:" field, enter the date/time you want the option to start.
6.  At the "DEVICE FOR QUEUED JOB OUTPUT:" field, press Enter.
7.  At the "QUEUED TO RUN ON VOLUME SET:" field, press Enter.
8.  At the "RESCHEDULING FREQUENCY:" field, enter how often you want the report to run.
9.  Tab to the "COMMAND" field, enter Save and Exit.

> <span id="_Ref356557615" class="anchor"></span>Figure . Monitor Laboratory Test File Changes Affecting Quick Orders—Using TASKMAN to schedule CPRS Quick Order Check option to run

Select Systems Manager Menu Option: <span class="mark">TASK \<Enter\></span> man Management

Schedule/Unschedule Options

One-time Option Queue

Taskman Management Utilities ...

List Tasks

Dequeue Tasks

Requeue Tasks

Delete Tasks

Print Options that are Scheduled to run

Cleanup Task List

Print Options Recommended for Queueing

Select Taskman Management Option: <span class="mark">SCHEDULE \<Enter\></span> /Unschedule Options

Select OPTION to schedule or reschedule: <span class="mark">LRJ QUICK ORDER CHECK</span>

Are you adding 'LRJ QUICK ORDER CHECK' as

a new OPTION SCHEDULING (the 226TH)? No// <span class="mark">YES \<Enter\></span> (Yes)

<span class="mark">Edit Option Schedule</span>

<u>Option Name</u>: LRJ QUICK ORDER CHECK

Menu Text: TaskMan file format file 60 audit TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME:

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY:

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

6.  Assign users who need to receive the CPRS Quick Order Check notification to the OR CACS mail group.

# Specimen Inactivation/Activation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Specimen Inactivation/Activation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To support order entry transactions in CPRS, entries in the following VistA files can be placed in an inactive state:

- COLLECTION SAMPLE file (#62)—INACTIVE DATE field (#64.9101)
- TOPOGRAPHY FIELD file (#61) —INACTIVE DATE field (#64.9103)

VistA entries for collection samples and topographies can be inactivated/activated using the following options:

- Edit Inactive Date - COLLECTION SAMPLE option \[LRJ MAINT INACTIVE DT FILE 62\]
- Edit Inactive Date - TOPOGRAPHY FIELD option \[LRJ MAINT INACTIVE DT FILE 61\]

![](lr-5-2-425-laboratory-user-guide/032.png) NOTE: These options use VA FileMan to edit the INACTIVATION DATE field in Files \#61 and \#62.

Only active VistA entries can be used for:

- Physician order entry.
- CPRS Quick Orders.
- New test configurations in the LABORATORY TEST file (#60).

![](lr-5-2-425-laboratory-user-guide/033.png) NOTE: Orders containing an inactive entry placed *prior* to the file entry inactivation can be processed by the lab.  
  
Inactive file entries can still be used when orders are placed by legacy lab order options. This includes Anatomic Pathology (AP) and clinical lab orders.

The following conditions *must* apply to any collection sample that is to be inactivated:

- Inactivated collection samples *must* manually be removed from both the LAB COLLECTION SAMPLE (#9) and COLLECTION SAMPLE (#300) fields for all active tests in the LABORATORY TEST file (#60) that use that collection sample.
- Inactivated collection samples assigned a default specimen from the TOPOGRAPHY FIELD file (#61) need to have the default specimen removed.

The following conditions *must* be met for any topography that is to be inactivated and is a default specimen for an active collection sample:

- Either remove the default specimen from the active collection sample
- Or, replace the default specimen with an active Topography Field file (#61) entry.

## Collection Sample/Topography Field—Inactivation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Determine if a Collection Sample is Used on an Active Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To determine if a collection sample is used on an active test, perform the following VA FileMan search:

1.  From the VA FileMan Option \[DIUSER\], at the "Select VA FileMan Option:" prompt, select the Search File Entries option \[DISEARCH\].
27. At the "OUTPUT FROM WHAT FILE: COLLECTION SAMPLE//" prompt, enter LABORATORY TEST.
28. At the "-A- SEARCH FOR LABORATORY TEST FIELD:" prompt, enter LAB.
29. At the "CHOOSE 1-2:" prompt, enter 1 to select LAB COLLECTION SAMPLE.
30. At the "-A- CONDITION:" prompt, enter EQUALS.
31. At the "-A- EQUALS COLLECTION SAMPLE:" prompt, select the entry in the COLLECTION SAMPLE file (#62) to be inactivated.
32. At the "-B- SEARCH FOR LABORATORY TEST FIELD:" prompt, enter COLLECTION SAMPLE.
33. At the "-B- SEARCH FOR LABORATORY TEST COLLECTION SAMPLE SUB-FIELD:" prompt, enter COLLECTION SAMPLE.
34. At the "-B- CONDITION:" prompt, enter EQUALS.
35. At the "-B- EQUALS COLLECTION SAMPLE:" prompt, select the same entry from Step 7 for the collection sample to be inactivated.
36. At the "-C- SEARCH FOR LABORATORY TEST COLLECTION SAMPLE SUB-FIELD:" prompt, press Enter.
37. At the "-C- SEARCH FOR LABORATORY TEST FIELD:" prompt, press Enter.
38. At the "IF:" prompt, enter A.
39. At the "OR:" prompt, Enter B.
40. At the "DO YOU WANT THIS SEARCH SPECIFICATION TO BE CONSIDERED TRUE FOR CONDITION -B-  
    1) WHEN AT LEAST ONE OF THE 'COLLECTION SAMPLE' MULTIPLES SATISFIES IT  
    2) WHEN ALL OF THE 'COLLECTION SAMPLE' MULTIPLES SATISFY IT  
    CHOOSE 1-2: 1//" prompt, press Enter to accept the default.
4.  At the "OR:" prompt, press Enter.
5.  At the "STORE RESULTS OF SEARCH IN TEMPLATE:" prompt, press Enter.
6.  At the "SORT BY: NAME//" prompt, press Enter to accept the default.
7.  At the "START WITH NAME: FIRST//" prompt, press Enter to accept the default.
8.  At the "FIRST PRINT FIELD:" prompt, enter NAME.
9.  At the "THEN PRINT FIELD:" prompt, enter LAB COLLECTION SAMPLE.
10. At the "THEN PRINT FIELD:" prompt, enter COLLECTION SAMPLE.
11. At the "THEN PRINT COLLECTION SAMPLE SUB-FIELD:" prompt, enter COLLECTION SAMPLE.
12. At the "THEN PRINT COLLECTION SAMPLE SUB-FIELD:" prompt, press Enter.
13. At the "THEN PRINT FIELD:" prompt, press Enter.
14. At the "Heading (S/C): LABORATORY TEST SEARCH Replace" prompt, press Enter.
15. At the "STORE PRINT LOGIC IN TEMPLATE:" prompt, press Enter.

![](lr-5-2-425-laboratory-user-guide/034.png) CAUTION: At the following device-related prompts, make sure your terminal emulator software (e.g., Attachmate<sup>®</sup> Reflections) display has enough log memory blocks to capture all the data displayed to the screen.

16. At the "DEVICE:" prompt enter ;;999999.
17. At the "Right Margin: 80//" prompt, press Enter.

> <span id="_Toc366647071" class="anchor"></span>Figure . Specimen Inactivation/Activation—Determine if a collection sample is used on an active test

Enter or Edit File Entries

Print File Entries

<span class="mark">Search File Entries</span>

Modify File Attributes

Inquire to File Entries

Utility Functions ...

Data Dictionary Utilities ...

Transfer Entries

Other Options ...

Select VA FileMan Option: <span class="mark">SEARCH \<Enter\></span> File Entries

OUTPUT FROM WHAT FILE: COLLECTION SAMPLE// <span class="mark">LABORATORY TEST</span> (2485 entries)

-A- SEARCH FOR LABORATORY TEST FIELD: <span class="mark">LAB COLLECTION SAMPLE</span>

-A- CONDITION: <span class="mark">EQUALS</span>

-A- EQUALS COLLECTION SAMPLE: <span class="mark">BLOOD</span>

1 BLOOD BLOOD GENERAL

2 BLOOD PLASMA GRAY

3 BLOOD BLOOD LAVENDER

4 BLOOD PLASMA BLACK TOP

5 BLOOD SERUM SPC BLUE2ML

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: <span class="mark">2 \<Enter\></span> BLOOD PLASMA GRAY

-B- SEARCH FOR LABORATORY TEST FIELD: <span class="mark">COLLECTION SAMPLE \<Enter\></span> (multiple)

-B- SEARCH FOR LABORATORY TEST COLLECTION SAMPLE SUB-FIELD: <span class="mark">COLLECTION SAMPLE</span>

-B- CONDITION: <span class="mark">EQUALS</span>

-B- EQUALS COLLECTION SAMPLE: <span class="mark">BLOOD</span>

1 BLOOD BLOOD GENERAL

2 BLOOD PLASMA GRAY

3 BLOOD BLOOD LAVENDER

4 BLOOD PLASMA BLACK TOP

5 BLOOD SERUM SPC BLUE2ML

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: <span class="mark">2 \<Enter\></span> BLOOD PLASMA GRAY

-C- SEARCH FOR LABORATORY TEST COLLECTION SAMPLE SUB-FIELD: <span class="mark">\<Enter\></span>

-C- SEARCH FOR LABORATORY TEST FIELD: <span class="mark">\<Enter\></span>

IF: <span class="mark">A \<Enter\></span> LAB COLLECTION SAMPLE EQUALS 2 (BLOOD)

OR: <span class="mark">B \<Enter\></span> Or LABORATORY TEST COLLECTION SAMPLE EQUALS 2 (BLOOD)

DO YOU WANT THIS SEARCH SPECIFICATION TO BE CONSIDERED TRUE FOR CONDITION -B-

1\) WHEN AT LEAST ONE OF THE 'COLLECTION SAMPLE' MULTIPLES SATISFIES IT

2\) WHEN ALL OF THE 'COLLECTION SAMPLE' MULTIPLES SATISFY IT

CHOOSE 1-2: 1// <span class="mark">\<Enter\></span>

OR: <span class="mark">\<Enter\></span>

STORE RESULTS OF SEARCH IN TEMPLATE: <span class="mark">\<Enter\></span>

SORT BY: NAME// <span class="mark">\<Enter\></span>

START WITH NAME: FIRST// <span class="mark">\<Enter\></span>

FIRST PRINT FIELD: <span class="mark">NAME</span>

THEN PRINT FIELD: <span class="mark">LAB COLLECTION SAMPLE</span>

THEN PRINT FIELD: <span class="mark">COLLECTION SAMPLE \<Enter\></span> (multiple)

THEN PRINT COLLECTION SAMPLE SUB-FIELD: <span class="mark">COLLECTION SAMPLE</span>

THEN PRINT COLLECTION SAMPLE SUB-FIELD: <span class="mark">\<Enter\></span>

THEN PRINT FIELD: <span class="mark">\<Enter\></span>

Heading (S/C): LABORATORY TEST SEARCH Replace <span class="mark">\<Enter\></span>

STORE PRINT LOGIC IN TEMPLATE: <span class="mark">\<Enter\></span>

DEVICE: <span class="mark">;;999999 \<Enter\></span> SSH VIRTUAL TERMINAL Right Margin: 80// <span class="mark">\<Enter\></span>

<span class="mark">LABORATORY TEST SEARCH</span> JUN 10,2013 13:33 PAGE 1

NAME LAB COLLECTION SAMPLE

COLLECTION SAMPLE

----------------------------------------------------------------------------

ZZAPTT

BLOOD

COMPLEMENT C6

BLOOD

ESTRONE

BLOOD

FATTY ACIDS, FREE

BLOOD

BLOOD

FREE HGB

BLOOD

BLOOD

HEPATITIS E ANTIBODY BLOOD

BLOOD

BLOOD

HEPATITIS E ANTIGEN BLOOD

BLOOD

BLOOD

Hgb Solubility BLOOD

BLOOD

METHANOL BLOOD

BLOOD

PLASMA FREE HGB

BLOOD

BLOOD

VITAMIN C

BLOOD

ZZDHEA THRU 11/4/11 PLASMA

BLOOD

zzC-1Q COMPLEMENT COMPONENT 11/7/11

BLOOD

zzCATECHOLAMINES, FRACT. 11/7/11/

BLOOD

14 MATCHES FOUND.

### Determine if a Collection Sample is Assigned a Default Specimen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To determine if a collection sample is assigned a default specimen, perform the following procedure:

1.  From the VA FileMan Option \[DIUSER\], at the "Select VA FileMan Option:" prompt, select the Inquire to File Entries option \[DIINQUIRE\].
41. At the "OUTPUT FROM WHAT FILE: TOPOGRAPHY FIELD//" prompt, enter COLLECTION SAMPLE.
42. At the "Select COLLECTION SAMPLE NAME:" prompt, enter a collection sample.
43. At the "ANOTHER ONE:" prompt, press Enter.
44. At the "STANDARD CAPTIONED OUTPUT? Yes//" prompt, press Enter.
45. At the "Include COMPUTED fields: (N/Y/R/B): NO//" prompt, press Enter.

> <span id="_Toc366647072" class="anchor"></span>Figure . Specimen Inactivation/Activation—Determine if a collection sample is assigned a default specimen

Enter or Edit File Entries

Print File Entries

Search File Entries

Modify File Attributes

<span class="mark">Inquire to File Entries</span>

Utility Functions ...

Data Dictionary Utilities ...

Transfer Entries

Other Options ...

Select VA FileMan Option: <span class="mark">INQUIRE \<Enter\></span> to File Entries

OUTPUT FROM WHAT FILE: LABORATORY TEST// <span class="mark">COLLECTION SAMPLE \<Enter\></span> (207 entries)

Select COLLECTION SAMPLE NAME: <span class="mark">BLOOD</span>

1 BLOOD BLOOD GENERAL

2 BLOOD PLASMA GRAY

3 BLOOD BLOOD LAVENDER

4 BLOOD PLASMA BLACK TOP

5 BLOOD SERUM SPC BLUE2ML

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: <span class="mark">2 \<Enter\></span> BLOOD PLASMA GRAY

ANOTHER ONE: <span class="mark">\<Enter\></span>

STANDARD CAPTIONED OUTPUT? Yes// <span class="mark">\<Enter\></span> (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// <span class="mark">\<Enter\></span> - No record number (IEN), no Computed Fields

NAME: BLOOD DEFAULT SPECIMEN: PLASMA

TUBE TOP COLOR: GRAY VOLUME LARGE: 5

VOLUME SMALL: 5 LAB SECTION: CHEMISTRY

CAN LAB COLLECT: YES

SYNONYM: PLASMA

SYNONYM: BLUE TOP

SYNONYM: GRAY TOP

SNOMED CT ID: 119297000 SCT CODE STATUS: LOCAL

SCT TOP CONCEPT: SCT Specimen

SCT STATUS DATE: JAN 09, 2012@11:02:40 SCT STATUS CHANGED TO: LOCAL

SCT STATUS USER: LABUSER,ONE

SCT COMMENT TEXT:

File used to apply mapping and/or disposition: HUNTINGTON_SCT_12-14-10.TXT;2

### Determine if a Topography is a Default Specimen for an Active Collection Sample

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To determine if a topography is a default specimen for an active collection sample, perform the following procedure:

1.  From the VA FileMan Option \[DIUSER\], at the "Select VA FileMan Option:" prompt, select the Search File Entries option \[DISEARCH\].
46. At the "OUTPUT FROM WHAT FILE: COLLECTION SAMPLE//" prompt, enter COLLECTION SAMPLE.
47. At the "-A- SEARCH FOR COLLECTION SAMPLE FIELD:" prompt, enter DEFAULT SPECIMEN.
48. At the "-A- CONDITION:" prompt, enter EQUALS.
49. At the "-A- EQUALS TOPOGRAPHY FIELD:" prompt, enter the name of the TOPOGRAPHY FIELD file (#61) entry.
50. At the "-B- SEARCH FOR COLLECTION SAMPLE FIELD:" prompt, press Enter.
51. At the "IF: A//" prompt, press Enter.
52. At the "STORE RESULTS OF SEARCH IN TEMPLATE:" prompt, enter a name or press Enter.
53. At the "SORT BY: NAME//" prompt, press Enter.
54. At the "START WITH NAME: FIRST//" prompt, press Enter.
55. At the "FIRST PRINT FIELD:" prompt, enter NUMBER;C2

![](lr-5-2-425-laboratory-user-guide/035.png) CAUTION: "NUMBER" *must be capitalized* or it will not be returned in the report. Number is the IEN of the file entry.

56. At the "THEN PRINT FIELD:" prompt, enter NAME;C10;L30
57. At the "THEN PRINT FIELD:" DEFAULT SPECIMEN;C42
58. At the "THEN PRINT FIELD:" prompt, press Enter.
59. At the "Heading (S/C): COLLECTION SAMPLE SEARCH Replace" prompt, press Enter.
60. At the "STORE PRINT LOGIC IN TEMPLATE:" prompt, press Enter.
61. At the "DEVICE:" prompt, enter ;;999999.
62. At the "Right Margin: 80//" prompt, press Enter.

> <span id="_Toc366647073" class="anchor"></span>Figure . Specimen Inactivation/Activation—Determine if a topography is a default specimen for an active collection sample

Enter or Edit File Entries

Print File Entries

<span class="mark">Search File Entries</span>

Modify File Attributes

Inquire to File Entries

Utility Functions ...

Data Dictionary Utilities ...

Transfer Entries

Other Options ...

Select VA FileMan Option: <span class="mark">SEARCH \<Enter\></span> File Entries

OUTPUT FROM WHAT FILE: TOPOGRAPHY FIELD// <span class="mark">COLLECTION SAMPLE \<Enter\></span> (207 entries)

-A- SEARCH FOR COLLECTION SAMPLE FIELD: <span class="mark">DEFAULT SPECIMEN</span>

-A- CONDITION: <span class="mark">EQUALS</span>

-A- EQUALS TOPOGRAPHY FIELD: <span class="mark">URINE</span>

-B- SEARCH FOR COLLECTION SAMPLE FIELD: <span class="mark">\<Enter\></span>

IF: A// <span class="mark">\<Enter\></span> DEFAULT SPECIMEN EQUALS 71 (URINE)

STORE RESULTS OF SEARCH IN TEMPLATE: <span class="mark">\<Enter\></span>

SORT BY: NAME// <span class="mark">\<Enter\></span>

START WITH NAME: FIRST// <span class="mark">\<Enter\></span>

FIRST PRINT FIELD: <span class="mark">NUMBER;C2</span>

THEN PRINT FIELD: <span class="mark">NAME;C10;L30</span>

THEN PRINT FIELD: <span class="mark">DEFAULT SPECIMEN;C42</span>

THEN PRINT FIELD: <span class="mark">\<Enter\></span>

Heading (S/C): COLLECTION SAMPLE SEARCH Replace <span class="mark">\<Enter\></span>

STORE PRINT LOGIC IN TEMPLATE: <span class="mark">\<Enter\></span>

DEVICE: <span class="mark">;;999999 \<Enter\></span> SSH VIRTUAL TERMINAL Right Margin: 80// <span class="mark">\<Enter\></span>

<span class="mark">COLLECTION SAMPLE SEARCH</span> JUN 11,2013 09:15 PAGE 1

NUMBER

NAME

DEFAULT SPECIMEN

----------------------------------------------------------------------------

75 CATHETER URINE

URINE

135 CONDOM CATHETER

URINE

81 CYSTOSCOPY

URINE

112 FOLEY CATH URINE

URINE

15 URINE

URINE

198 URINE CLEAN CATCH

URINE

197 URINE INDWELLING CATHETER

URINE

199 URINE SUPRAPUBIC

URINE

69 URINE,RANDOM

URINE

70 URINE,TIME

URINE

211 ZZFEB

URINE

11 MATCHES FOUND.

### *Inactivate* Entries in the Collection Sample and Topography Field Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To individually *inactivate* entries in the COLLECTION SAMPLE file (#62) and the TOPOGRAPHY FIELD file (#61), perform the following procedure:

1.  From the Lab liaison menu \[LRLIAISON\], enter EDIT INACTIVE.
2.  At the "CHOOSE 1-2:" prompt, select the appropriate option:
- 1—Edit Inactive Date - COLLECTION SAMPLE option \[LRJ MAINT INACTIVE DT FILE 62\] to edit the inactivation date to the INACTIVATION DATE field (#64.9101) in the COLLECTION SAMPLE file (#62).
- 2—Edit Inactive Date - TOPOGRAPHY FIELD option \[LRJ MAINT INACTIVE DT FILE 61\] to edit the inactivation date to the INACTIVATION DATE field (#64.9103) in the TOPOGRAPHY FIELD file (#61).
3.  At the "Select COLLECTION SAMPLE:" or "Select TOPOGRAPHY FIELD:" prompt, enter the name of the appropriate file entry to be *inactivated*.
63. At the "INACTIVE DATE:" prompt, enter the appropriate inactivate date.
64. Repeat Steps 3-4 for all file entries that need to be *inactivated*.

> <span id="_Toc366647074" class="anchor"></span>Figure . Specimen Inactivation/Activation—COLLECTION SAMPLE file entry: *Inactivate*

Select Laboratory DHCP Menu Option: <span class="mark">^LAB \<Enter\></span> liaison menu

ANT Add a new internal name for an antibiotic

ANTE Edit an Antibiotic

BCF Lab Bar Code Label Formatter

BCZ Lab Zebra Label Utility

DATA Add a new data name

HDR Recover/Transmit Lab HDR Result Messages

LNC LOINC Main Menu ...

MOD Modify an existing data name

SMGR Lab Shipping Management Menu ...

Add a new WKLD code to file

AP Microfiche Archive

Archiving Menu ...

Check files for inconsistencies

Check patient and lab data cross pointers

Download Format for Intermec Printer

Edit atomic tests

Edit cosmic tests

<span class="mark">Edit Inactive Date - COLLECTION SAMPLE</span>

<span class="mark">Edit Inactive Date - TOPOGRAPHY FIELD</span>

File 60 Audit Manager

File list for lab

Hospital Location Monitor Tool

LAB ROUTINE INTEGRITY MENU ...

Lab Tests and CPT Report

LIM workload menu ...

Manually compile WKLD and workload counts

OE/RR interface parameters ...

Outline for one or more files

Print AMA CPT Panel Pending List

Re-index Antimicrobial Suscept File (62.06)

Restart processing of instrument data

Turn on site workload statistics

Turn on workload stats for accession area

User selected lab test/patient list edits ...

Select Lab liaison menu Option: <span class="mark">EDIT INACTIVE</span>

<span class="mark">1 Edit Inactive Date - COLLECTION SAMPLE</span>

2 Edit Inactive Date - TOPOGRAPHY FIELD

CHOOSE 1-2: <span class="mark">1 \<Enter\></span> Edit Inactive Date - COLLECTION SAMPLE

Select COLLECTION SAMPLE: <span class="mark">URINE \<Enter\></span> URINE

INACTIVE DATE: <span class="mark">T \<Enter\></span> (FEB 22, 2012)

Select COLLECTION SAMPLE: <span class="mark">\<Enter\></span>

Select Lab liaison menu Option: <span class="mark">EDIT INACTIVE</span>

1 Edit Inactive Date - COLLECTION SAMPLE

<span class="mark">2 Edit Inactive Date - TOPOGRAPHY FIELD</span>

CHOOSE 1-2: <span class="mark">2 \<Enter\></span> Edit Inactive Date - TOPOGRAPHY FIELD

Select TOPOGRAPHY FIELD: <span class="mark">ARM, ANTERIOR SURFACE</span>

INACTIVE DATE: <span class="mark">T \<Enter\></span> (FEB 22, 2012)

## Collection Sample/Topography Field—Activation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To individually *activate* inactive entries in the COLLECTION SAMPLE file (#62) and the TOPOGRAPHY FIELD file (#61), perform the following procedure:

1.  From the Lab liaison menu \[LRLIAISON\], enter EDIT INACTIVE.
4.  At the "CHOOSE 1-2:" prompt, select the appropriate option:
- 1—Edit Inactive Date - COLLECTION SAMPLE option \[LRJ MAINT INACTIVE DT FILE 62\] to edit the inactivation date to the INACTIVATION DATE field (#64.9101) in the COLLECTION SAMPLE file (#62).
- 2—Edit Inactive Date - TOPOGRAPHY FIELD option \[LRJ MAINT INACTIVE DT FILE 61\] to edit the inactivation date to the INACTIVATION DATE field (#64.9103) in the TOPOGRAPHY FIELD file (#61).
5.  At the "Select COLLECTION SAMPLE:" or "Select TOPOGRAPHY FIELD:" prompt, enter the name of the appropriate file entry to be *activated*.
6.  At the "INACTIVE DATE: *Month DD, YYYY*" prompt, enter an at-sign ("@") to delete the INACTIVE DATE value.
7.  At the "SURE YOU WANT TO DELETE?" prompt", enter YES to *activate* the entry.
8.  Repeat Steps 3-5 for all file entries that need to be *activated*.

> <span id="_Toc366647075" class="anchor"></span>Figure . Specimen Inactivation/Activation—COLLECTION SAMPLE file entry: *Activated*

Select Laboratory DHCP Menu Option: ^<span class="mark">LAB \<Enter\></span> liaison menu

ANT Add a new internal name for an antibiotic

ANTE Edit an Antibiotic

BCF Lab Bar Code Label Formatter

BCZ Lab Zebra Label Utility

DATA Add a new data name

HDR Recover/Transmit Lab HDR Result Messages

LNC LOINC Main Menu ...

MOD Modify an existing data name

SMGR Lab Shipping Management Menu ...

Add a new WKLD code to file

AP Microfiche Archive

Archiving Menu ...

Check files for inconsistencies

Check patient and lab data cross pointers

Download Format for Intermec Printer

Edit atomic tests

Edit cosmic tests

<span class="mark">Edit Inactive Date - COLLECTION SAMPLE</span>

<span class="mark">Edit Inactive Date - TOPOGRAPHY FIELD</span>

File 60 Audit Manager

File list for lab

Hospital Location Monitor Tool

LAB ROUTINE INTEGRITY MENU ...

Lab Tests and CPT Report

LIM workload menu ...

Manually compile WKLD and workload counts

OE/RR interface parameters ...

Outline for one or more files

Print AMA CPT Panel Pending List

Re-index Antimicrobial Suscept File (62.06)

Restart processing of instrument data

Turn on site workload statistics

Turn on workload stats for accession area

User selected lab test/patient list edits ...

Select Lab liaison menu Option: <span class="mark">EDIT INACTIVE</span>

<span class="mark">1 Edit Inactive Date - COLLECTION SAMPLE</span>

2 Edit Inactive Date - TOPOGRAPHY FIELD

CHOOSE 1-2: <span class="mark">1 \<Enter\></span> Edit Inactive Date - COLLECTION SAMPLE

Select COLLECTION SAMPLE: <span class="mark">URINE \<Enter\></span> URINE

INACTIVE DATE: FEB 22, 2012// <span class="mark">@</span>

SURE YOU WANT TO DELETE? <span class="mark">Y \<Enter\></span> (Yes)

Select COLLECTION SAMPLE:

# Mail Group Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Mail Group Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the installation of Laboratory Patch LR\*5.2\*425, the mail groups in <u>Table 8</u> were created and coordinators assigned.

<table>
<caption><p><span id="_Ref351463734" class="anchor"></span>Table . Mail Group Maintenance—Mail groups released with LR*5.2*425</p></caption>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th>Mail Group</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>LRJ SYS MAP HL TASK REPORT</td>
<td><p>This mail group receives the Hospital Location System Change Management extract report generated by the TaskMan option: LRJ SYS MAP HL TASKMAN RPT.</p>
<p><strong>Membership:</strong> Should include Laboratory Information Management System (LIMS) and Commercial-off-the-Shelf (COTS) Configuration Managers (where applicable) responsible for keeping Hospital Location Rooms and Beds on Vista in synchronization with those defined on a remote Lab configuration run by the VA Medical Center.</p>
<p>It should also contain a Microsoft<sup>®</sup> Outlook mail group or users. Outlook mail groups/users can be entered as Remote Users.</p></td>
</tr>
<tr class="even">
<td>LRJ AUF60 AUDIT TASK REPORT</td>
<td><p>This mail group receives the VistA LABORATORY TEST file (#60) audit reports generated by TaskMan.</p>
<p>![](lr-5-2-425-laboratory-user-guide/036.png) <strong>REF:</strong> For detailed information on auditing, see the "<u>Laboratory Test File 60 Audit Tool</u>" section.</p></td>
</tr>
<tr class="odd">
<td>LRJ AUF60XT AUDIT TASK REPORT</td>
<td><p>This mail group receives delimited file extracts from the VistA LABORATORY TEST file (#60) audits.</p>
<p>![](lr-5-2-425-laboratory-user-guide/037.png) <strong>NOTE:</strong> Not all messages will contain file extracts. In addition, messages <em>cannot</em> be viewed in VistA. Therefore, the messages <em>must</em> be forwarded to a Microsoft<sup>®</sup> Outlook email group or users. Outlook mail groups/users can be entered as Remote Users.</p>
<p>![](lr-5-2-425-laboratory-user-guide/038.png) <strong>REF:</strong> For detailed information on auditing, see the "<u>Laboratory Test File 60 Audit Tool</u>" section.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref351463734" class="anchor"></span>Table . Mail Group Maintenance—Mail groups released with LR\*5.2\*425

![](lr-5-2-425-laboratory-user-guide/039.png) REF: For more information on mail groups and membership enrollment, see Chapter 8 in the *MailMan User Guide*, which is located on the VA Software Document Library (VDL): <http://www4.va.gov/vdl/application.asp?appid=15>

## Assign New Users to Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To enroll new members in a mail group, perform the following procedure:

1.  From the Manage Mailman menu \[XMMGR\], select the Group/Distribution Management option \[XMMGR-GROUP-MAINTENANCE\].
65. At the "Select Group/Distribution Management Option:" prompt, enter Mail Group Coordinator.
66. At the "CHOOSE 1-2:" prompt, select 1—Mail Group Coordinator's Edit option \[XMMGR-MAIL-GRP-COORDINATOR\].
67. At the " Select MAIL GROUP NAME:" prompt, enter LRJ to get a list of all mail groups that begin with "LRJ."
68. From the displayed list of mail groups, select the LRJ mail group to which you wish to add members (e.g., LRJ AUF60 AUDIT TASK REPORT).
69. At the "Select MEMBER:" prompt, enter the name of the member you wish to add to the mail group.
70. At the "Are you adding ' *Labuser,One* ' as a new MEMBER (the *nXX* for this MAIL GROUP)? No//" prompt, enter YES.
71. At the "TYPE:" prompt, enter the appropriate TYPE code for the member added, choose from:
- NULL—Indicates that this recipient is a primary recipient, and may reply.
- CC—Indicates that the recipient is being sent a copy, but is not the primary recipient. The recipient may reply.
- INFO—Indicates that the recipient may not reply to the message; the message is being transmitted to the recipient for information purposes only.
72. Repeat Steps 6-8 until all members have been added. When all entries are complete, at the "Select MEMBER:" prompt, press Enter.
73. At the "Select MEMBER GROUP NAME:" prompt, press Enter.
74. If you wish to send previous messages to the newly added members, at the "Do you wish to forward past mail group messages to the user(s) you just added to the mail group(s)? No//" prompt, enter YES.
75. If you answered YES in Step 11, at the "Message sent on or after: (MM/DD/YYYY - MM/DD/YYYY): MM/DD/YYYY//" prompt, enter the "from" date range.
76. If you answered YES in Step 11, at the "Message sent on or before: (MM/DD/YYYY - MM/DD/YYYY): MM/DD/YYYY//" prompt, enter the "to" date range.
77. Repeat Steps 4 – 13 until all LRJ mail group member enrollments are complete.

> <span id="_Ref356978323" class="anchor"></span>Figure . Mail Group Maintenance—Enrolling in a mail group

Select Manage Mailman Option: <span class="mark">GROUP \<Enter\></span> /Distribution Management

Bulletin edit

Edit Distribution List

Enroll in (or Disenroll from) a Mail Group

Mail Group Coordinator's Edit

Mail Group Coordinator's Edit W/Remotes

Mail Group Edit

Select Group/Distribution Management Option: <span class="mark">MAIL GROUP COORD</span>

1 Mail Group Coordinator's Edit

2 Mail Group Coordinator's Edit W/Remotes

CHOOSE 1-2: <span class="mark">1 \<Enter\></span> Mail Group Coordinator's Edit

Select MAIL GROUP NAME: <span class="mark">LRJ</span>

1 LRJ AUF60 AUDIT TASK REPORT

2 LRJ AUF60XT AUDIT TASK REPORT

3 LRJ SYS MAP HL TASK REPORT

CHOOSE 1-5: <span class="mark">1 \<Enter\></span> LRJ AUF60 AUDIT TASK REPORT

Select MEMBER: <span class="mark">LABUSER,ONE \<Enter\></span> OL OIT STAFF

Are you adding ' Labuser,One ' as a new MEMBER (the 1ST for this MAIL GROUP)? No// <span class="mark">Y \<Enter\></span> (Yes)

TYPE: <span class="mark">\<Enter\></span>

Select MEMBER: <span class="mark">LABUSER,TWO \<Enter\></span> TL OIT STAFF

Are you adding ' Labuser,Two ' as a new MEMBER (the 2ND for this MAIL GROUP)? No// <span class="mark">Y \<Enter\></span> (Yes)

TYPE: <span class="mark">\<Enter\></span>

Select MEMBER: <span class="mark">\<Enter\></span>

Select MEMBER GROUP NAME: <span class="mark">\<Enter\></span>

Do you wish to forward past mail group messages

to the user(s) you just added to the mail group(s)? No// <span class="mark">YES</span>

You will now choose a date range for the messages to be searched

and forwarded. The oldest message is from 4/13/2010.

Message sent on or after: (4/13/2010 - 8/8/2011): 8/8/2010// <span class="mark">\<Enter\></span> (AUG 08, 2010)

Message sent on or before: (8/8/2010 - 8/8/2011): 8/8/2011// <span class="mark">\<Enter\></span> (AUG 08, 2011)

Task \#231784 will find and forward past messages.

Select MAIL GROUP NAME:

![](lr-5-2-425-laboratory-user-guide/040.png) REF: For more information on mail groups and membership enrollment, see Chapter 8 in the *MailMan User Guide*, which is located on the VA Software Document Library (VDL): <http://www.va.gov/vdl/application.asp?appid=15>

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: LA*5.2*68 Laboratory User Guide

## Health Data Repository

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LA\*5.2\*68 allows the HL7 ORU message containing patient laboratory results to be transmitted to the subscriber, LA7 LAB RESULTS TO HDR (SUB). This subscriber protocol is used to transmit laboratory results to the VA HDR.

- After you activate sending messages to the HDR, extracting existing laboratory data (HDR historical) will follow, so that there will be an overlap with no gaps of laboratory data within the HDR.
- Once you activate sending messages to the HDR, do not inactivate, as this can cause gaps of laboratory data within the HDR.
- If you must inactivate sending messages to the HDR, contact the HDR program office, so that the laboratory data can be tracked and recovered.

## ## Blood Bank Clearance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VISTA Laboratory Package patch LA\*5.2\*68 contains changes to software controlled by VHA DIRECTIVE 99-053, titled VISTA BLOOD BANK SOFTWARE. Changes include:

New style indexes have been created for the following sub-files

of the LAB DATA file (#63):

ELECTRON MICROSCOPY (#63.02)

SURGICAL PATHOLOGY (#63.08)

CYTOPATHOLOGY (#63.09)

All of the above changes have been reviewed by the VISTA Blood Bank Developer and found to have no impact on the VISTA BLOOD BANK SOFTWARE control functions.

RISK ANALYSIS: Changes made by patch LA\*5.2\*68 have no effect on Blood Bank software functionality, therefore RISK is none.

EFFECT ON BLOOD BANK FUNCTIONAL REQUIREMENTS: Patch LA\*5.2\*68 does not alter or modify any software design safeguards or safety critical elements functions.

POTENTIAL IMPACT ON SITES: This patch contains changes to 0 routines and 1 file identified in Veterans Health Administration (VHA) Directive 99-053, group B listing. The changes have no effect on Blood Bank functionality or medical device control functions. There is no adverse potential to sites.

## About This Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This user guide provides instructions for installing the Veterans Health Information Systems and Technology Architecture (VistA) Patch LA\*5.2\*68 for the Laboratory package, as well as pertinent technical, implementation, and security information.

## HL7 Event Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 event protocol LA7 LAB RESULTS AVAILABLE (EVN) supports subscripts: CH, MI, SP, CY, and EM.

## Activate Message Generation and Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the following steps only when activating the transmission of laboratory data to the VA HDR and/or interfacing to a Commercial Off the Shelf System (COTS) or other VistA subscriber.

No further action is required, if there is no requirement to activate this interface.

- To activate messaging to the VA HDR perform steps 1, 2, and 3.
- To activate messaging to COTS and other VistA subscribers perform steps 1 and 4.
1.  Generate and transmit HL7 Lab ORU result messages
1.  Enable the configuration LA7HDR in LA7 MESSAGE PARAMETER file (#62.48), and use VA File Manager to set the field Status (#2) to Active.
2.  When this field is set to Inactive, the generation of the Lab HL7 ORU message is turned off.

Select VA FileMan Option: Enter or Edit File Entries

INPUT TO WHAT FILE: LA7 MESSAGE PARAMETER// 62.48 LA7 MESSAGE PARAMETER

EDIT WHICH FIELD: ALL// STATUS

THEN EDIT FIELD:

Select LA7 MESSAGE PARAMETER CONFIGURATION: LA7HDR

STATUS: INACTIVE// ACTIVE ACTIVE

7.  Set up the VDEFVIE4 link for Laboratory data transmission
1.  Use the HL7 Main Menu: Select Filer and Link Management Options option to edit logical link VDEFVIE4.
3.  Enable Auto Startup and add the IP address and port number.  
    IP address: 10.224.67.234  
    Port number: 5021
4.  Use the HL7 Main Menu, Start/Stop Links option to start the VDEFVIE4 link.
5.  Use the HL7 Main Menu, Site Parameters Edit option to select VDEF view and add VDEFVIE4 to the view.
8.  Activate the interface to the VA HDR
1.  On the HL package, Interface Developer Options \[HL MENU INTERFACE TK\], use the Protocol Edit \[HL EDIT INTERFACE\] menu option to edit the protocol LA7 LAB RESULTS TO HDR (SUB).
5.  On the second ScreenMan screen, remove the leading (;) character from the Routing Logic field.
6.  Enter the Save command to retain the changes to the protocol.

  
Example: Editing the Routing Logic field

HL7 SUBSCRIBER PAGE 2 OF 2

LA7 LAB RESULTS TO HDR (SUB)

---------------------------------------------------------------------------

RECEIVING APPLICATION: LA7HDR

RESPONSE MESSAGE TYPE: ACK EVENT TYPE: R01

SENDING FACILITY REQUIRED?: YES RECEIVING FACILITY REQUIRED?: YES

SECURITY REQUIRED?:

LOGICAL LINK: VDEFVIE4

PROCESSING RTN:

ROUTING LOGIC: ;D RTR^LA7HDR("CH;") \<-- remove leading ";" character

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

After the change, the field looks like:

ROUTING LOGIC: D RTR^LA7HDR("CH;")

9.  Transmit Lab HL7 ORU result messages to another system, such as a Commercial Off the Shelf System (COTS)
1.  Create an HL7 subscriber protocol, as documented in the *HL7 Site Manager & Developer Manual* version 1.6\*56.
6.  Attach the HL7 subscriber protocol as a subscriber to HL7 event protocol, LA7 LAB RESULTS AVAILABLE (EVN).
10. On the HL package, Interface Developer Options \[HL MENU INTERFACE TK\] menu option, use the Protocol Edit \[HL EDIT INTERFACE\] option to add the HL7 subscriber.

## Inactivate Message Generation and Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](la-5-2-68-laboratory-user-guide/002.png) Notify the HDR Project Office in the event that this interface is deactivated and the interface to the HDR was previously activated

To control Lab HL7 ORU message generation and transmission after the interface is activated or to inactivate message generation and/or transmission, perform the following steps.

Use step 1 to inactivate all message generation to all subscribers.

Use step 2 to inactivate message generation/transmission to a specific subscriber.

1.  Inactivate Lab HL7 ORU message generation and transmission to all subscribers of event protocol, LA7 LAB RESULTS AVAILABLE (EVN)
1.  Disable the configuration LA7HDR in the LA7 MESSAGE PARAMETER file (#62.48), and set the field Status (#2) to Inactive using VA File Manager Enter or Edit File Entries \[DIEDIT\].
7.  When this field is set to Inactive, the generation of the Lab HL7 ORU message is turned off.
11. Inactivate message transmission to a specific subscriber
1.  On the HL package, Interface Developer Options \[HL MENU INTERFACE TK\] menu option, use the Protocol Edit \[HL EDIT INTERFACE\] option to remove the related subscriber protocol from the event protocol LA7 LAB RESULTS AVAILABLE (EVN).
7.  For the VA HDR, remove subscriber protocol LA7 LAB RESULTS TO HDR (SUB).

## Routines 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The checksums below are new checksums, and can be checked with CHECK1^XTSUMBLD.

 

Routine Name: LA68

    Before:       n/a   After: B17816218  \*\*68\*\*

Routine Name: LA7HDR

    Before:       n/a   After: B39353571  \*\*68\*\*

Routine Name: LA7HDR1

    Before:       n/a   After: B37911850  \*\*68\*\*

Routine Name: LA7QRY

    Before:  B5873978   After:  B8496816  \*\*46,69,68\*\*

Routine Name: LA7QRY1

    Before: B12341981   After: B34477085  \*\*46,61,68\*\*

Routine Name: LA7QRY2

    Before: B24752999   After: B38475048  \*\*46,69,68\*\*

Routine Name: LA7VHLU

    Before: B42350744   After: B44857108  \*\*46,62,64,68\*\*

Routine Name: LA7VHLU2

    Before: B19775199   After: B28776777  \*\*46,61,64,68\*\*

Routine Name: LA7VHLU3

    Before: B15291257   After: B55573792  \*\*46,64,68\*\*

Routine Name: LA7VHLU4

    Before: B25336667   After: B25782007  \*\*46,64,68\*\*

Routine Name: LA7VHLU5

    Before: B40473983   After: B49053645  \*\*46,64,68\*\*

Routine Name: LA7VHLU9

    Before:       n/a   After: B16600197  \*\*68\*\*

Routine Name: LA7VIN5

    Before: B52231590   After: B62438539  \*\*46,64,68\*\*

Routine Name: LA7VMSG1

    Before: B51506932   After: B52098570  \*\*56,46,61,64,68\*\*

Routine Name: LA7VOBR

    Before: B23749256   After: B25844567  \*\*46,64,68\*\*

Routine Name: LA7VOBRA

    Before: B37451712   After: B39455733  \*\*46,64,68\*\*

Routine Name: LA7VOBRB

    Before:       n/a   After: B12807459  \*\*68\*\*

Routine Name: LA7VOBX

    Before: B25091305   After: B30185961  \*\*46,64,68\*\*

Routine Name: LA7VOBX1

    Before: B15262892   After: B28786998  \*\*46,61,63,64,71,68\*\*

Routine Name: LA7VOBX2

    Before: B15453740   After: B21393582  \*\*46,64,68\*\*

Routine Name: LA7VOBX3

    Before: B33632644   After: B83540167  \*\*46,64,68\*\*

Routine Name: LA7VOBXA

    Before: B31676928   After: B53603815  \*\*46,70,64,68\*\*

Routine Name: LA7VORC

    Before:  B8007778   After: B18625097  \*\*46,64,68\*\*

Routine Name: LA7VORM1

    Before: B52156055   After: B57485485  \*\*27,51,46,61,64,68\*\*

Routine Name: LA7VORU

    Before: B58855542   After: B24122155  \*\*27,46,61,64,71,68\*\*

Routine Name: LA7VORU1

    Before: B35283793   After: B61414246  \*\*46,64,68\*\*

Routine Name: LA7VORU2

    Before:  B6677596   After:  B5334202  \*\*46,64,68\*\*

Routine Name: LA7VORUA

    Before:  B8112587   After: B11624236  \*\*61,64,68\*\*

Routine Name: LA7VORUB

    Before:       n/a   After: B37430566  \*\*68\*\*

 

Routine list of preceding patches: 69, 71

## Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LA7 HDR Recover is a new option added to the OPTION file (#19).

NAME: LA7 HDR RECOVER MENU TEXT: Recover/Transmit Lab

HDR Result Messages

TYPE: run routine CREATOR: LDSICREATOR,ONE  
PACKAGE: AUTOMATED LAB INSTRUMENTS

DESCRIPTION: Option to recover from failed Lab HDR ORU Result message generation and/or transmission failure. This option allows the user to select those VistA Laboratory accessions that need to be transmitted to the VA HDR and other subscribers of the VistA Laboratory Result Available HL7 message capability via the protocol Lab Results Available Event \[LA7 LAB RESULTS AVAILABLE (EVN)\].

If the original message generation/transmission failed due to system or communication problems then using this option will allow the generation of new HL7 messages with the results associated with the selected accessions. Accessions can be selected using the human-readable accession designation (area abbreviation modified date accession number - "CH 1225 100") or the accession's associated 10 character unique identifier (UID)

ROUTINE: RECOVER^LA7HDR

UPPERCASE MENU TEXT: RECOVER/TRANSMIT LAB HDR RESUL

This option is assigned to the Lab liaison menu option \[LRLIAISON\] and can be assigned as needed to support/monitor message transmission to the VA HDR and other subscribers.

## Purging Capabilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Purging of LA7 MESSAGE QUEUE file (#62.49) is handled along with other Lab HL7 interfaces via the scheduled task.

NAME: LA7TASK NIGHTY MENU TEXT: Lab Messaging Nightly Cleanup

TYPE: run routine CREATOR: LDSICREATOR,ONE PACKAGE: AUTOMATED LAB INSTRUMENTS

DESCRIPTION: This is a tasked option to check integrity of LA7 MESSAGE QUEUE file (#62.49) and purge messages that are eligible for purging. It also purges the following files related to LEDI - SHIPPING MANIFEST (#62.8), LAB SHIPPING EVENT (#62.85) and LAB PENDING ORDERS ENTRY (#69.6)

This option should be tasked daily, preferably during period when activity in the Lab Messaging (i.e. Universal Interface, LEDI) package is at a minimum.

Prior to the purge of LA7 MESSAGE QUEUE file (#62.49), an integrity check is performed. The integrity check can be run with a couple of switches.

LA7FIX = 0 - do not fix errors

1 - do fix errors

LA7LOG = 0 - do not log errors in XTMP global.

1 - do log errors in XTMP global

LA7ION = name of device to print error report if set to

log errors (LA7LOG=1).

These parameters can be setup by TaskMan if the site defines them when scheduling the task.

An example is given below:

Edit Option Schedule

Option Name: LA7TASK NIGHTY

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

VARIABLE NAME: LA7FIX VALUE: 0

VARIABLE NAME: LA7ION VALUE: "IRM DEVELOP LASER1"

VARIABLE NAME: LA7LOG VALUE: 1

If errors are found, an alert is sent to members of the mail group "LAB MESSAGING" notifying them that errors were detected. If

logging of errors occurred then alert recipients will be able to print/view error log from the alert system. Alternatively the

error report can be printed using option Print Lab Messaging Integrity Check \[LA7 PRINT INTEGRITY CHECK\].

The integrity report can be run alone using option Lab Messaging File Integrity Checker \[LA7 CHECK FILES\].

INDEPENDENTLY INVOCABLE: YES ROUTINE: EN^LA7PURG SCHEDULING RECOMMENDED: YES

UPPERCASE MENU TEXT: LAB MESSAGING NIGHTLY CLEANUP

## Callable Entry Points

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ICR \#3556 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

INTEGRATION REFERENCE INQUIRY \#3556            MAR 31, 2009  12:04    PAGE 1

--------------------------------------------------------------------------------

  

      3556     NAME: GET LAB RESULTS

  CUSTODIAL PACKAGE: AUTOMATED LAB INSTRUMENTS           Dallas

SUBSCRIBING PACKAGE: CLINICAL CASE REGISTRIES            Hines

                     Clinical Registries system requires access to the API

                     GCPR^LA7QRY to analyze lab tests and results.  This

                     API is required during the registry update process

                     and the data extract process.

                     HEALTH DATA SYSTEMS

                     CLINICAL PROCEDURES

              USAGE: Controlled Subscri  ENTERED: APR 11,2002

             STATUS: Active              EXPIRES:

           DURATION: Till Otherwise Agr  VERSION:

        DESCRIPTION:                     TYPE: Routine

   Clinical Registries system requires access to the API GCPR^LA7QRY to

   analyze lab tests and results.  This API is required during the registry

   update process and the data extract process.

 

     ROUTINE: LA7QRY

   COMPONENT: GCPR

              This component is passed a patient identifier, start and end

              dates (for when specimens were taken) and NLT and/or LOINC

              codes and specimen types.  The component passes back an array

              with details of any lab tests with results that occurred

              within the start and end dates that were for the LOINC or NLT

              codes and specimen types that were passed in.

             The structure of the returned values is as described in the

             VistA Laboratory VA HDR HL7 Interface Specification. This document

             Is  available from the VA VistA Documentation Library

             <http://www.va.gov/vdl/>

   VARIABLES: Input   LA7PTID

                          

          Patient identifier, either SSN or MPI/ICN or medical record number.

if MPI/ICN then should be full ICN (10 digit number followed by "V" and six digit checksum)

                           Pass in the 2nd piece of this variable the type of identifier:

                           SS = Social Security number

                           PI = VA MPI Integration Control Number

                           MR = medical record number of patient in file PATIENT/IHS (#9000001)

                           Example: 1000720100V271387^PI

                                    123456789^SS

                                    123456789^MR

   VARIABLES: Input LA7SDT

                           Start date of query (FileMan D/T, time optional).

   VARIABLES:Input     LA7EDT

                           End date of query (FileMan D/T, time optional)

                           (FileMan D/T^type of date ("CD" or "RAD") Both

                           start and end date values can pass a parameter in

                           the second piece to indicate that the date values

                           are for specimen collection date/time (CD) or

                           results available date (RAD).

 

                          Example: LA7SDT="2991001.1239^CD"

                                   LA7EDT="2991002.0331^CD"

                                   LA7SDT="3010201^RAD"

                                   LA7EDT="3010201^RAD"

   VARIABLES: Input     LA7SC

                           Array of search codes, either NLT or LOINC

                           (code^coding system ("NLT" or "LN");

                          

Example:  LA7SC(1)="89628.0000^NLT"

                           LA7SC(2)="84330.0000^NLT"

                           LA7SC(3)="84295.0000^NLT"

                           LA7SC(4)="14749-6^LN"

                           or

 

                           The "\*" (wildcard) for any code;

                           Example: LA7SC="\*" 

                           or

 

                           A list of subscripts (separated by commas) from

                           where the results will be extracted ("CH", "MI" or "SP").

                           Example: LA7SC="CH,MI" (CH and MI results only).

                           Pass in the 2nd piece of LA7SC the indicator (1) to return VUID when available.

                           Example: LA7SC="\*^1" or LA7SC="CH,MI^1"

   VARIABLES: Input     LA7SPEC

                           Array of specimen types using HL7 source table

                           0070 or "\*" (wildcard) for any code. Currently

                           specimen type only supported for CH and MI

                           subscripted tests.

 

                          Example: LA7SPEC="\*"

                           or

                                    LA7SPEC(1)="UR"

                                    LA7SPEC(2)="SER"

                                    LA7SPEC(3)="PLAS"

   VARIABLES: Both      LA7QERR

                           Array (by reference) containing any errors.

                           LA7QERR(error number) = text of error message

                           The following error codes and text are returned:

                           1  Invalid patient identifier passed

                           2  No patient found with requested identifier

                           3  No laboratory record for requested patient

4  Database error - missing laboratory record for requested patient

5  If ICN passed and MPI returns error then the error  
message for a given ICN

6  Unknown search code "\_\<code\>\_" passed, where \<code\> is a LOINC or NLT code passed in input parameter LA7SC.

7  Invalid list of subscripts: '\_\<subscript\>, where \<subscript\> is the value passed in input parameter LA7SC.

                           99 No results found for requested parameters

   VARIABLES: Both      LA7DEST

                           Closed root global reference to return search

                           results (optional).  If this parameter is omitted

                           or equals an empty string, then node

                           ^TMP("HLS",\$J) is used.

 

                           Example: LA7DEST=\$NA(^TMP("ZZTMP",\$J)).

 

                           The information returned in this global reference

                           uses the structure of an HL7 message to format the

                           results of the query.

   VARIABLES: Input     LA7HL7

                           HL7 field separator and encoding characters (4) to

                           use to encode results (optional). If undefined or

                           incomplete (length\<5) then field separator "\|"\|

                           and encoding characters "^\\&" are used. See HL7

                           standard for further information of use and

                           purpose of field separator and encoding

                           characters.

                Example call:

                          S LA7PTID="0000000000v000000^PI"

                           S LA7SDT="3000101"

                           S LA7EDT=\$\$NOW^XLFDT

                           S LA7SC="\*"

                           S LA7SPEC="\*"

                         S LA7DEST=\$NA(^TMP("ZZTMP",\$J))

                         S X=\$\$GCPR^LA7QRY(LA7PTID,LA7SDT,LA7EDT,.LA7SC,.  
LA7SPEC,.LA7ERR,LA7DEST,"\|^~\\")

           KEYWORDS: Clinical Registries

                     Hepatitis C

                              \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## External Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Versions of VA FileMan, Kernel, and other software (VistA or other) required to run this software.

- VA FileMan v22
- VA MailMan v8.0
- Health Level Seven v1.6
- Kernel v 8.0

### Integration Agreement 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Integration Agreement (IA): ICR \#3556     NAME: GET LAB RESULTS

## Laboratory Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each user must be assigned appropriate keys in order to access the Laboratory system. SECURITY KEY file (#19.1) contains the key names, a short description, and a list of the holders. Under each of the appropriate key names, you need to enter the names of the users.

## Archiving Capabilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently there are no archiving capabilities required for this patch release.
