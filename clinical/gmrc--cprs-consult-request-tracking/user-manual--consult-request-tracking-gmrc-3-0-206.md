---
title: Consult/Request Tracking User Manual (GMRC*3.0*206)
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: GMRC
app_name: "CPRS: Consult/Request Tracking"
section: CLI
app_status: active
pkg_ns: GMRC
patch_ver: 3.0
patch_id: GMRC*3.0
group_key: "GMRC:GMRC:3.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - consult
  - request
  - consults
  - action
  - service
  - tracking
  - patient
  - contents
  - table
  - results
page_count: 0
word_count: 28312
section_count: 18
table_count: 7
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking/consum.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking/consum.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=62"
---

---
title: |
  <span id="_Toc497992714" class="anchor"></span>Consult/Request Tracking

  <span id="_Toc497992715" class="anchor"></span>User Manual
---

![](consult-request-tracking-user-manual-gmrc-3-0-206/001.png)

August 2024

Department of Veterans Affairs (VA)

Office of Information & Technology (OIT)

Revision History

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 17%" />
<col style="width: 49%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Patch</th>
<th>Description</th>
<th>Authors</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/2024</td>
<td>GMRC*3.0*206</td>
<td><ul>
<li><p>Updated for 508 compliance</p></li>
</ul></td>
<td>CPRS Development Team</td>
</tr>
<tr class="even">
<td>09/2021</td>
<td>GMRC*3.0*181</td>
<td><ul>
<li><p>Redaction of screen captures to remove IP addresses and then remove arrows and call outs. Various places throughout manual.</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>03/2021</td>
<td>GMRC*3.0*84</td>
<td><ul>
<li><p>NSR 20110210 – Added the <a href="#Prosthetics_Consult_Updated_column">Prosthetics Consult Updated</a> entry to the notifications table, added the <a href="#Prosthetics_Consult_Updated_section">Prosthetics Consult Updated</a> section.</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>03/2021</td>
<td>GMRC*3.0*170</td>
<td><ul>
<li><p>Replaced sentence in the Cancelled to Discontinued Consults section with, “<strong><u>Each consult fitting the parameter criteria is evaluated as to whether the consult was resubmitted and then cancelled again on a later date. If there is no later cancellation date, the consult is discontinued by calling the $$DC^GMRCGUIA API.</u></strong>”</p></li>
<li><p>Updated Title page, Revision History, Table of Contents, Index, and Footers</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>11/2020</td>
<td>GMRC*3.0*145</td>
<td><p>Under Enhancements since Version 2.5, added paragraph describing <a href="#gmrc3.0145">GMRC*3.0*145</a>.</p>
<p>Under <a href="#_Consult/Request_Resolution_1">Consult/Request Resolution</a>, updated text for notification trigger</p>
<p>Revised dates on Title page and footers</p></td>
<td><strong>REDACTED</strong></td>
</tr>
<tr class="even">
<td>11/2019</td>
<td>GMRC*3.0*139</td>
<td>Added Auto-forwarding to DST Consult handling. See page <a href="#p2_139">2</a>, <a href="#gmrc3.0145">4</a></td>
<td><strong>REDACTED</strong></td>
</tr>
<tr class="odd">
<td>4/2019</td>
<td>GMRC*3.0*124</td>
<td>Added reference to changes in Package Operation Workflow for users of Care Coordination (CC) Decision Support Tool (DST). See Page <a href="\l">12</a></td>
<td><strong>REDACTED</strong></td>
</tr>
<tr class="even">
<td>3/2019</td>
<td>GMRC*3.0*119</td>
<td><p>Added Help Text that displays when entering ??? at the "Select Consult Tracking Reports Option:" prompt. See Page <a href="#Option_Help_119">159</a></p>
<p>Added the Administratively Released Consults by Group Local Report example. The report was changed to include in the counts those services that were made in a consult name including -DS or -ADMIN but then forwarded to a different service. See <a href="#GR_fwd">Page 162</a>.</p></td>
<td><strong>REDACTED</strong></td>
</tr>
<tr class="odd">
<td>2/2019</td>
<td>GMRC*3.0*113</td>
<td>Added the Cancelled to Discontinued Consults section. Added the option GMRC CX TO DC PARAMETER EDIT, where user is able to update parameters that drive the overnight job GMRC CHANGE STATUS X TO DC. Page <a href="#cancelled-to-discontinued-consults">161</a> – <a href="#GMRC_113_CancelledtoDiscontinuepg2">162</a>.</td>
<td><strong>REDACTED</strong></td>
</tr>
<tr class="even">
<td>1/2019</td>
<td>GMRC*3*110</td>
<td>When a user clicks on the Consults tab, then highlights a Consult, the details of the consult appear in the right-hand panel. This display was changed to display the Unique Consult ID (UCID) at the top. See Page <a href="#ucid-display">161</a>.</td>
<td><strong>REDACTED</strong></td>
</tr>
<tr class="odd">
<td>12/2018</td>
<td>GMRC*3.0*107</td>
<td>Added details for new GMRC Reports to support the ADMIN KEY consults for consults that are Administratively released by Policy. See pages <a href="#admin-key-reports">158</a> – <a href="#GMRC_3_107">161</a>.</td>
<td><strong>REDACTED</strong></td>
</tr>
<tr class="even">
<td>08/2018</td>
<td>XU*8.0*679</td>
<td>Added note regarding electronic Signature Block restrictions. See Page <a href="#SignatureBlockNote">19</a>.</td>
<td><strong>REDACTED</strong></td>
</tr>
<tr class="odd">
<td>03/3018</td>
<td>GMRC*3*91</td>
<td>Added information about additional recipients receiving an alert. See Page <a href="#Additional_Recipients_to_Receive_Alert1">139</a> and Page <a href="#Additional_Recipients_to_Receive_Alert2">150</a>.</td>
<td><strong>REDACTED</strong></td>
</tr>
<tr class="even">
<td>03/2018</td>
<td>GMRC*3*92</td>
<td><p><a href="\l">Update the VistA last name criteria.</a></p>
<p>Applied up-to-date 508 standards and VA compliance to title page, Revision History table, headings, and footers.</p></td>
<td><strong>REDACTED</strong></td>
</tr>
<tr class="odd">
<td>03/2018</td>
<td>GMRC*3*89</td>
<td>Modified SF 513 images (<a href="#GMRC_89_1">Image 1</a> and <a href="#GMRC_89_2">Image 2)</a> to reflect addition of Age and Cell Phone fields. Added info re: set up of a secondary printer for SF 513. <a href="#GMRC_89_ClosToolNote">Added info on new Consult Closure Tool.</a></td>
<td><strong>REDACTED</strong></td>
</tr>
<tr class="even">
<td>02/2016</td>
<td>GRMC*3*81</td>
<td>Changed the Earliest Appropriate Date to Clinically Indicated Date. Pages: <a href="#CID_new_order_consult">16</a>, <a href="#CID_working_copy">22</a>, <a href="#CID_SF513">32</a>, <a href="#CID_Order_a_Consult_dialog"><strong>Error! Bookmark not defined.</strong></a></td>
<td><strong>REDACTED</strong></td>
</tr>
<tr class="odd">
<td>08/2014</td>
<td>GMRC*3*75</td>
<td>Modified description to <a href="#GMRC_75_CONSULT_REQUEST_UPDATED">CONSULT/REQUEST UPDATED</a>; added description of <a href="#GMRC_75_HCPS">HCPS</a> and <a href="#GMRC_75_RAS">RAS</a> to Glossary</td>
<td><strong>REDACTED</strong></td>
</tr>
<tr class="even">
<td>01/2015</td>
<td>GMRC*3*82</td>
<td><a href="\l">Modified SF 513 Images to reflect SSN format change</a>.</td>
<td><strong>REDACTED</strong></td>
</tr>
<tr class="odd">
<td>02/2014</td>
<td><a href="#gmrc3.0145">GMRC*3*73</a></td>
<td><a href="#gmrc73display">ICD-10 Remediation</a></td>
<td><strong>REDACTED</strong></td>
</tr>
<tr class="even">
<td>02/2014</td>
<td>GMRC*3*73</td>
<td>Added info to description for <a href="#consultrequest-updated">CONSULT/REQUEST UPDATED</a> and <a href="#ConsultADDEDCOMMENT">Consult/Request Has an Added Comment</a>.</td>
<td><strong>REDACTED</strong></td>
</tr>
<tr class="odd">
<td>08/2011</td>
<td>GMRC*3*71</td>
<td><a href="#consultrequest-updated">Modified description for CONSULT/REQUEST UPDATED</a></td>
<td><strong>REDACTED</strong></td>
</tr>
<tr class="even">
<td>02/2011</td>
<td></td>
<td>Earliest Appropriate Date Patch 66</td>
<td><strong>REDACTED</strong></td>
</tr>
<tr class="odd">
<td>08/2009</td>
<td></td>
<td>Combat Veteran (CV) status added to SF 513</td>
<td><strong>REDACTED</strong></td>
</tr>
<tr class="even">
<td>04/2006</td>
<td></td>
<td>Updates/corrections to patient and provider names to comply with SOP 192-352</td>
<td><strong>REDACTED</strong></td>
</tr>
<tr class="odd">
<td>12/2004</td>
<td></td>
<td>SOP 192-352 applied (scrubbed)</td>
<td><strong>REDACTED</strong></td>
</tr>
<tr class="even">
<td>06/2002</td>
<td></td>
<td>Include Patch 25</td>
<td></td>
</tr>
<tr class="odd">
<td>04/2002</td>
<td></td>
<td>Include Patch 22 &amp; 25</td>
<td></td>
</tr>
<tr class="even">
<td>11/2001</td>
<td></td>
<td>Include Patch 17</td>
<td></td>
</tr>
<tr class="odd">
<td>06/2001</td>
<td></td>
<td>Include Patch 21</td>
<td></td>
</tr>
<tr class="even">
<td>02/2001</td>
<td></td>
<td>Include Patch 15, 19, &amp; 20</td>
<td></td>
</tr>
<tr class="odd">
<td>10/2000</td>
<td></td>
<td>Include Patches 13, 14, 16, &amp; 18</td>
<td></td>
</tr>
<tr class="even">
<td>07/2000</td>
<td></td>
<td>Add Patches 6 thru 8, 11, &amp; 12</td>
<td></td>
</tr>
<tr class="odd">
<td>09/1998</td>
<td></td>
<td>Include Patches 1 thru 5</td>
<td></td>
</tr>
<tr class="even">
<td>12/1997</td>
<td></td>
<td>Initial Release</td>
<td></td>
</tr>
</tbody>
</table>

# # # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# # Introduction](#introduction)
  - [Overview](#overview)
    - [Purpose](#purpose)
    - [Relationship to Other Packages](#relationship-to-other-packages)
  - [Enhancements since Version 2.5](#enhancements-since-version-25)
    - [GMRC\3.0\145](#gmrc30145)
    - [GMRC\3.0\139](#gmrc30139)
  - [Relations with other VistA Components](#relations-with-other-vista-components)
  - [Related Manuals and Other References](#related-manuals-and-other-references)
- [# Package Management](#package-management)
  - [Service Update and Tracking Security](#service-update-and-tracking-security)
    - [Consult Service Tracking](#consult-service-tracking)
- [# Package Operation](#package-operation)
  - [Workflow](#workflow)
    - [The Clinician Orders a Consult](#the-clinician-orders-a-consult)
    - [The Consult Service Gets a Written Copy](#the-consult-service-gets-a-written-copy)
    - [If Accepted, an Appointment is Held](#if-accepted-an-appointment-is-held)
    - [Results are Entered and Signed](#results-are-entered-and-signed)
    - [The Originating Clinician Receives an Alert that the Consult is Complete](#the-originating-clinician-receives-an-alert-that-the-consult-is-complete)
    - [The SF 513 Report Becomes Part of the Patient’s Medical Record](#the-sf-513-report-becomes-part-of-the-patients-medical-record)
  - [Quick Orders](#quick-orders)
  - [Using the Consults Package with TIU](#using-the-consults-package-with-tiu)
    - [Direct TIU Input](#direct-tiu-input)
    - [Correcting Misdirected Results](#correcting-misdirected-results)
  - [Using the Consults Package with Medicine](#using-the-consults-package-with-medicine)
  - [Using the Consults Package with Clinical Procedures](#using-the-consults-package-with-clinical-procedures)
  - [Windows Quick Start](#windows-quick-start)
  - [Introduction 57](#introduction-57)
    - [Windows Flow of Information 58](#windows-flow-of-information-58)
    - [Other Windows Topics 77](#other-windows-topics-77)
    - [Windows Flow of Information](#windows-flow-of-information)
    - [Other Windows Topics](#other-windows-topics)
    - [Changes made by Patch 73 for ICD-10 Remediation](#changes-made-by-patch-73-for-icd-10-remediation)
- [Package Reference](#package-reference)
  - [General Service User Menu](#general-service-user-menu)
    - [Consult Service Tracking Option](#consult-service-tracking-option)
    - [Completion Time Statistics](#completion-time-statistics)
    - [Service Consults Pending Resolution](#service-consults-pending-resolution)
  - [Consult Status](#consult-status)
  - [Actions](#actions)
    - [Brief Action Descriptions](#brief-action-descriptions)
    - [Add Comment (CM) Action](#add-comment-cm-action)
    - [Cancel (or Deny) Consult](#cancel-or-deny-consult)
    - [Change View (CV) Action](#change-view-cv-action)
    - [Complete Request (CT) Action](#complete-request-ct-action)
    - [Deny Request (DY) Action](#deny-request-dy-action)
    - [Detailed Order Display (DD) Action](#detailed-order-display-dd-action)
    - [Discontinue Order (DC) Action](#discontinue-order-dc-action)
    - [Edit/Resubmit (ER) Action](#editresubmit-er-action)
    - [Forward Request (FR) Action](#forward-request-fr-action)
    - [Make Addendum (MA) Action](#make-addendum-ma-action)
    - [Print Form (PF) Action](#print-form-pf-action)
    - [Print Screen Contents (PS) Action](#print-screen-contents-ps-action)
    - [Quit (Q) Action](#quit-q-action)
    - [Receive Request (RC) Action](#receive-request-rc-action)
    - [Remove Medicine Results (RM)](#remove-medicine-results-rm)
    - [Results Display (RT) Action](#results-display-rt-action)
    - [Schedule (SC) Action](#schedule-sc-action)
    - [Select New Patient (SP) Action](#select-new-patient-sp-action)
    - [Significant Findings (SF) Action](#significant-findings-sf-action)
  - [Notifications about Consults and Requests](#notifications-about-consults-and-requests)
    - [Enabling Notifications](#enabling-notifications)
    - [New Service Consult/Request](#new-service-consultrequest)
    - [Consult/Request Resolution](#consultrequest-resolution)
    - [Consult/Request Updated](#consultrequest-updated)
    - [Consult/Request Cancel/Hold](#consultrequest-cancelhold)
    - [Consult/Request Has an Added Comment](#consultrequest-has-an-added-comment)
    - [Order(s) Require Electronic Signature](#orders-require-electronic-signature)
    - [Significant Findings for a Consult](#significant-findings-for-a-consult)
    - [Prosthetics Consult Updated](#prosthetics-consult-updated)
  - [ADMIN KEY Reports](#admin-key-reports)
    - [UCID Display](#ucid-display)
    - [Cancelled to Discontinued Consults](#cancelled-to-discontinued-consults)
- [Glossary](#glossary)
- [# # Index](#index)
The *Consult/Request Tracking User Manual* provides descriptions of Consults’ options and other information required to effectively use the Consult/Request Tracking package (or Consults).
This manual is for people who use the Consults package in the course of their hospital duties, including:
- Care providers: doctors, nurses, pharmacists, and therapists who make or service requests for consultations on patients.
- Clerical staff, who assist the above-mentioned people.
- Quality Assurance and management, who have an interest in seeing that VA patients receive the best possible care.
- Consults functionality is available from a Windows interface (GUI—Graphical User Interface) on a PC workstation or from a roll-and-scroll List Manager (LM) interface on a traditional CRT (Cathode Ray Tube) terminal or terminal emulation software on a PC workstation.
You can pull out parts of this manual, such as the User Introduction to GUI section or the Package Operation section, to use for unit training or reference. General parts of this manual, such as the Package Orientation section, have been written with examples from Consults to make the general information more meaningful to this application.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Consult/Request Tracking package V. 3.0 improves the quality of patient care by:

- Interfacing with CPRS to provide an efficient mechanism for clinicians to order consults and procedure requests.
- Providing consulting services with the ability to update and track the progress of a consult/procedure request from the point of receipt through its final resolution.
- Providing results reporting that includes doctor's notes and comments entered during the tracking process.

### Relationship to Other Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Consults package works with the following packages:

- Computerized Patient Record System (CPRS)
- Text Integration Utilities (TIU)

#### Relationship of Consults to CPRS

#### From CPRS Actions to Consults:

- Ordering
- Order checking
- Order updates via HL7 messages
- Inter-Facility Consults via HL7 messages
- Tracking Consults activity
- Resulting TIU and Consults
- Notifications

#### From Consults actions to CPRS:

- Consult status changes update the CPRS order
- Forwarded and edit/resubmitted consults get a new service/correction order from CPRS
- Sends alerts based on consult activity
- <span id="p2_139" class="anchor"></span>Auto-forwarding of Consult Orders to new Consult text

#### Relationship of Consults to TIU

#### From TIU Actions to Consults:

- Select a consult to associate with a note
- One consult link per consult note
- Sends TIU updates to consult package for:
- New consult note entered
- Consult note completed
- New addendum completed
- Disassociate a note
- Extract notes for SF 513 and displays

#### From Consult Actions to TIU:

- A consult may have multiple notes associated with it.
- Lists the notes associated with a consult.
- Uses TIU to act on a note.
- Updates consult status and activity log from TIU updates.

## Enhancements since Version 2.5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### GMRC\*3.0\*145

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch, part of the larger CPRS GUI v31 Mission Act release, assists with implementing the Decision Support Tool (DST) and Consult Toolbox (CTB) directly into CPRS GUI. Please consult the DST and CTB user manuals on the VistA Document Library for detailed information regarding use of these features.

### GMRC\*3.0\*139

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch adds Auto-forwarding functionality. When the Decision Support Tool (DST) transmits the Auto-forward information to CPRS, the existing CPRS RPC process will detect the Auto-forward request and forward the Order to a new Consult location, which is referenced in the REQUEST SERVICE file (#123.5).

#### General Overview of Consults/Request Tracking

- Consults can be accessed through Windows NT, Windows 95, or a later Microsoft Windows version with the CPRS GUI Interface or through the List Manager (LM) interface.
- Consult ordering is managed by CPRS Order Entry from within the CPRS Order tab. This includes Quick Orders.
- Consult resulting is based on TIU Consult Notes, Medicine package results, and provider comments.
- Services must be defined within the ALL SERVICES hierarchy in order to access their consults and requests.
- Tracking services are not orderable unless the user is an update user for the service or its parent service.
- The ordering provider may edit and resubmit a consult after it has been canceled.

#### Alert Actions

- Users can process consult service update actions from the alert.
- The recipient of an alert for a cancelled request can edit and resubmit the request from the alert .

#### Reporting

- The Standard Form 513 is based on a hard-coded consults routine instead of the OE/RR Print Formats. This facilitates results printing when the consult reaches final resolution.
- A report with completion time statistics has been added.
- A report with pending consults has been added.
- Lists of consults can be viewed by order status, service, and/or date range.

#### Communications

- HL7 messages and protocols are the communications medium between CPRS and Consults.

#### Setup

Consult services have a related entry in the CPRS Orderable Items file (#101.43).

Management of procedures and services must be done through Consult options.

## Relations with other VistA Components 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Consults package communicates with CPRS through HL7 messages. Order Checking receives information from the Consults package through CPRS. Notifications is the only major package that Consults communicates with directly. When the requesting clinician signs the order, Consults sends a notification to the consulting physician and when the consulting physician signs the final report, Consults sends a notification to the requesting physician.

![](consult-request-tracking-user-manual-gmrc-3-0-206/002.png)

Inter-Facility Consults (IFC) are requested, acted upon, and viewed the same way as regular Consults. Typically consults that are handled at a different facility have the remote facility indicated in their title, such as “Eye Exam—Salt Lake.” The software uses HL7 messaging in the background to communicate inter-facility consults and actions between cooperating facilities. Results are filed at the resulting facility, but since CPRS uses Remote Data Views in the background to access the results, users do not need to treat Inter-Facility Consults any differently.

## Related Manuals and Other References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are an ADPAC or IRM personnel, the *Consult/Request Tracking Technical Manual* would probably aid in your understanding of Consults setup and operation.

Consults is installed with CPRS, so the *CPRS Installation Guide* is the appropriate manual to refer to on installation issues that aren’t covered in the *Consult/Request Tracking Technical Manual*.

TIU provides boilerplate text and other text-oriented services. The *TIU Clinical Coordinator & User Manual* would assist you in using these features.

Consults package is highly integrated with CPRS. As such, any Consults package user should be familiar with the *CPRS Clinician’s Getting Started Guide* and the *CPRS Clinical Coordinator & User Manual.*

See our web pages at: REDACTED

# # Package Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Service Update and Tracking Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your ADPAC can use the Consult Service User Management option, in conjunction with availability to various menus and options, to control access to Consults functionality. The menus that can be provided to you are:

### Consult Service Tracking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Consult Service Tracking menu provides access to basic consult tracking functions and reports but can also provide complete update capabilities if you have been granted update privileges by your ADPAC.

Individual options in the Consults package that may be useful to you, and what access they provide, are detailed in the following table:

| Option                              | Services                                                                        |
|-------------------------------------|---------------------------------------------------------------------------------|
| Consult Service Tracking            | Tracking and/or update functionality depending upon your individual privileges. |
| Completion Time Statistics          | Reporting.                                                                      |
| Service Consults Pending Resolution | Reporting.                                                                      |

With the GMRC Service User Management option, your ADPAC can set you up to be an update user for one or more services at your hospital. In addition, the ADPAC can grant the ability to receive consult notifications according to criteria outlined in the following table:

<table>
<colgroup>
<col style="width: 60%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th>Category</th>
<th>Notifications Received</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>UPDATE USERS W/O NOTIFICATIONS</td>
<td>Unless otherwise set up, will not receive notifications.</td>
</tr>
<tr class="even">
<td>UPDATE TEAMS W/O NOTIFICATIONS</td>
<td>Unless otherwise set up, will not receive notifications.</td>
</tr>
<tr class="odd">
<td>UPDATE USER CLASS W/O NOTIFS</td>
<td>Unless otherwise set up, will not receive notifications.</td>
</tr>
<tr class="even">
<td>SERVICE INDIVIDUAL TO NOTIFY</td>
<td>Receive consult notifications for your service.</td>
</tr>
<tr class="odd">
<td>SERVICE TEAM TO NOTIFY</td>
<td>Receive consult notifications for patients assigned to your team.*</td>
</tr>
<tr class="even">
<td><p>NOTIFICATION BY PT LOCATION</p>
<p>INDIVIDUAL TO NOTIFY</p></td>
<td>Receive all consult notifications for your service for patients in a specified ward.</td>
</tr>
<tr class="odd">
<td><p>NOTIFICATION BY PT LOCATION</p>
<p>TEAM TO NOTIFY</p></td>
<td>Receive consult notifications for patients assigned to your team and in a specified ward</td>
</tr>
<tr class="even">
<td>SPECIAL UPDATES INDIVIDUAL</td>
<td>An individual who has privileges to perform group status updates.</td>
</tr>
</tbody>
</table>

These categories are not mutually exclusive, meaning you may receive notifications based on being present on one or more of the lists detailed in the foregoing table.

\* NOTE: The service team does not receive the CONSULT/REQUEST UPDATED notification if another member of that team or an update user is the user adding the comment

| Privilege               | Granted                       |
|-------------------------|-------------------------------|
| Originate a consult     | Anyone with access to CPRS    |
| Sign a consult          | Anyone who can sign an order  |
| Change a consult status | Anyone with update privileges |
| View or print a consult | Anyone with access to CPRS    |

In summary, update user capabilities vary depending on

The option(s) that you are assigned.

Privileges granted in the Consults Service User Management option.

# # Package Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The operation of the Consults package involves multiple people, at various skill levels, in various parts of the hospital. A consult request may be entered by a clinician or a clerk under a clinician’s direction. This request acts as a depository of information about itself.

It collects notes and keeps records on everything that happens to it. When complete it becomes part of the patient’s medical record.

In the pages that follow, we present this flow of information, and show the actions that must be taken at each step in the process. Many of these actions must be taken by persons other than those originating the consult.

Also, Consults uses CPRS during the initiation process and TIU during the completion process. In this section, we give some information about each of these packages that may help you in using Consults.

## Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1. The clinician orders a consult. While in a patient's CPRS medical record, a clinician enters an order for a consultation or procedure.
2. The consult service gets a written copy. An alert and a hard-copy of the SF 513 are sent to the consult service.
3. If accepted, an appointment is held. To accept the consult, the service uses the receive action. The service can also discontinue or cancel the consult. Cancelled consults can be edited and re-submitted by the ordering clinician.
4. Results are entered and signed. The consult service enters results and comments. Resulting is primarily done using TIU.
5. The originating clinician receives an alert that the consult is complete. The results can now be examined and further action taken on behalf of the patient.
6. The SF 513 report becomes part of the patient’s medical record. A hard copy can be filed, and the electronic copy is online for paperless access.

\*NOTE: Under the Care Coordination (CC) Decision Support Tool (DST) project, the release of Patch GMRC\*3.0\*124 modifies the above workflow. The workflow changes effective with the installation of this patch will only impact users of DST. For further information regarding the workflow process for DST users, please refer to the DST User Guide, which can be found in the VA Software Document Library (VDL) under [CPRS: Consult/Request Tracking](https://www.va.gov/vdl/application.asp?appid=62).

![](consult-request-tracking-user-manual-gmrc-3-0-206/003.png)

### The Clinician Orders a Consult 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Consult orders can be entered:

From the CPRS medical record screen, Consults tab

CPRS GUI interface program, Consults tab

#### Ordering Within the CPRS Package

Primarily, Consult orders should be placed through the CPRS Add New Orders action.

In this manual we provide a step-by-step display of the process for ordering consult or procedures requests through the CPRS package. We first go through a brief list of steps, then we discuss each step in detail.

#### To Order a Consult:

A. Select CPRS Clinician Menu (OE) from the Clinician Menu.
B. Select the patient.
C. Select Chart Contents, and then Consults.
D. Select Order New Consult.
E. Answer questions on the particulars of the request.

To go over in detail how to order a consult:

#### A. Select CPRS Clinician Menu (OE) from the Clinician Menu

Exactly how you do this option depends on how IRM or your ADPAC set up your menu. This example shows one way of performing step A.

Select Clinician Menu Option: ?

OE CPRS Clinician Menu

RR Results Reporting Menu

AD Add New Orders

RO Act On Existing Orders

PP Personal Preferences ...

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Clinician Menu Option: OE

The screen now looks like this:

Patient Selection Apr 07, 1999 14:51:30 Page: 1 of 1

Current patient: \*\* No patient selected \*\*

Patient Name ID DOB Room-Bed

No patients found.

Enter the number of the patient chart to be opened \>\>\>

\+ Next Screen CV Change View ... FD Find Patient

\- Previous Screen SV (Save as Default List)Q Close

Select Patient: Change View //

#### B. Select the Patient

Select the patient as you would in any other package. Type a patient ID such as the patient's name, social security number, or the patient's last initial followed by the last 4 digits of the social security number. If more than one patient matches the key you entered, select the patient from the list presented on the screen.

Select Patient: Change View // C2342

1 C2342 CPRSPATIENT,TWO 03-04-32 666902342 MILITARY RETIREE

2 C2342 CPRSPATIENT,TWELVE 02-03-23 666242342 MILITARY RETIREE

CHOOSE 1-2: 2 CPRSPATIENT,TWELVE 02-03-23 666242342 MILITARY RETIREE

Searching for the patient's chart ...

(Continued on the next page.)

The screen now looks something like this:

Cover Sheet Feb 13, 1999 12:53:14 Page: 1 of 2

CPRSPATIENT,TWELVE 666-24-2342 1A/B-1 FEB 3,1923 (74) \<CA\>

PrimCare: CPRSProvider, Three PCTeam: GOLD

Item Entered

Allergies/Adverse Reactions \|

1 BEESWAX (hives, itching, watering eyes, \| 03/28/97

anxiety) \|

\|

Patient Postings \|

2 CRISIS NOTE \| 02/25/97 12:18

\|

Recent Vitals \|

No data available \|

\|

Immunizations \|

No immunizations found. \|

\|

Eligibility \|

Not Service Connected \|

\+ Enter the numbers of the items you wish to act on. \>\>\>

NW Enter New Allergy/ADR CV (Change View ...) SP Select New Patient

AD Add New Orders CC Chart Contents ... Q Close Patient Chart

Select: Next Screen//

#### C. Select Chart Contents, then Consults

To get to the menu containing Order New Consults, you must go through the Chart Contents menu, then select the Consults screen. This can be done in one step by typing:

CC;CON

All Consults Feb 13, 1998 12:56:32 Page: 1 of 1

CPRSPATIENT,TWELVE 666-24-2342 1A/B-1 FEB 3,1923 (74) \<CA\>

PrimCare: CPRSProvider, Three PCTeam: GOLD

Consult/Procedure Requested Status

1 CARDIOLOGY Consult \| 02/25/97 11:02 complete

Enter the numbers of the items you wish to act on. \>\>\>

NW Enter New Allergy/ADR CV (Change View ...) SP Select New Patient

AD Add New Orders CC Chart Contents ... Q Close Patient Chart

Select: Chart Contents//

#### D. Select Order New Consult

Type NW and press the \<Enter\> key.

#### Answer Questions on the Particulars of the Request

Select: Chart Contents// NW Order New Consult

Consult Procedure

Order new: C Consult

Delay release of these orders? NO// \<Enter\>

Consult to Service/Specialty: POD FOOT CLINIC FOOT CLINIC

Reason for Request:

1\>PERSISTENT SMALL FISSURES AND SCALING ON BOTH FEET.

2\>

EDIT Option:

Category: INPATIENT// \<Enter\>

Urgency: ROUTINE// ??

Select from:

1 STAT

2 ROUTINE

3 WITHIN 48 HOURS

4 WITHIN 72 HOURS

5 EMERGENCY

Select the urgency indicating how quickly results from this consult are needed.

Urgency: ROUTINE// \<Enter\>

<span id="CID_new_order_consult" class="anchor"></span>Clinically indicated date:TODAY// \<Enter\>

Place of Consultation: Bedside// ?

Select from:

1 Bedside

2 Consultant's Choice

Select the preferred place to see the patient for this consult.

Place of Consultation: Bedside// \<Enter\>

Attention: CPRSPROVIDER,THREE CT PHYSICIAN

Provisional Diagnosis: TINEA PEDIS

-------------------------------------------------------------------------------

Consult to Service/Specialty: Podiatry

Reason for Request: PERSISTENT SMALL FISSURES AND SCALING ON ...

Category: INPATIENT

Urgency: ROUTINE

Place of Consultation: Bedside

Attention: CPRSPROVIDER,THREE

Provisional Diagnosis: TINEA PEDIS

-------------------------------------------------------------------------------

(P)lace, (E)dit, or (C)ancel this order? PLACE// \<Enter\>

... order placed.

Add another Consult order? NO//

(Continued on the next page.)

The screen now looks something like this:

All Consults Feb 13, 1998 12:58:32 Page: 1 of 1

CPRSPATIENT,TWELVE 666-24-2342 1A/B-1 FEB 3,1923 (74) \<CA\>

PrimCare: CPRSProvider, Three PCTeam: GOLD

Consult/Procedure Requested Status

1 CARDIOLOGY Consult \| 02/25/97 11:02 complete

Enter the numbers of the items you wish to act on. \>\>\>

NW Enter New Allergy/ADR CV (Change View ...) SP Select New Patient

AD Add New Orders CC Chart Contents ... Q Close Patient Chart

Select: Chart Contents//

Notice that the consult just entered is not yet displayed. It is not displayed until after you have signed the order.

#### Sign the Consult

\+ Next Screen \$ Sign All Orders

\- Previous Screen Q Close

Select: Sign All Orders// \$ Sign All Orders

Enter your Current Signature Code: SIGNATURE VERIFIED

Processing orders ...

When applied to an approved medical record, an electronic signature has the same legal weight as a signature made with a pen on paper. For this reason, electronic signatures are part of the overall security system maintained by IRMS.

When the computer prints a document that has been signed and/or cosigned, an electronic signature block is included. What appears in this block is user configurable through the User’s Toolbox option.

In this example we change a title and electronic signature:

Select Consult Service Tracking Option: ??

CS Consult Service Tracking \[GMRC SERVICE TRACKING\]

PC Service Consults Pending Resolution \[GMRC RPT PENDING CONSULTS\]

ST Completion Time Statistics \[GMRC COMPLETION STATISTICS\]

Or a Common Option:

CWA Patient Warning (CWAD) Display \[GMRPNCW\]

MA MailMan Menu ... \[XMUSER\]

TBOX User's Toolbox ... \[XUSERTOOLS\]

VA View Alerts \[XQALERT\]

Continue \[XUCONTINUE\]

\*\*\> Reverse lock ZZLUKE

Halt \[XUHALT\]

Restart Session \[XURELOG\]

Time \[XUTIME\]

Where am I? \[XUSERWHERE\]

You have PENDING ALERTS

Enter "VA VIEW ALERTS to review alerts

Select Consult Service Tracking Option: TBOX User's Toolbox

Select User's Toolbox Option: ?

Display User Characteristics

Edit User Characteristics

Electronic Signature code Edit

Menu Templates ...

Spooler Menu ...

Switch UCI

TaskMan User

User Help

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select User's Toolbox Option: ELectronic Signature code Edit

This option is designed to permit you to enter or change your Initials,

Signature Block Information, Office Phone number, and Voice and

Digital Pagers numbers.

In addition, you are permitted to enter a new Electronic Signature Code

or to change an existing code.

INITIAL: CRS// \<Enter\>

SIGNATURE BLOCK PRINTED NAME: CPRSPROVIDER,SEVEN// \<Enter\>

SIGNATURE BLOCK TITLE: DOCTOR// MD

OFFICE PHONE: 555-588-5000

ANALOG PAGER: 4038

DIGITAL PAGER: \<Enter\>

Enter your Current Signature Code: SIGNATURE VERIFIED

Your typing will not show.

ENTER NEW SIGNATURE CODE:

RE-ENTER SIGNATURE CODE FOR VERIFICATION:

DONE

Select User's Toolbox Option:

\*NOTE: CONCERNING SPACES IN LAST NAMES OF PROVIDERS SIGNING CONSULTS

Providers with last names in VistA containing spaces who sign Consults – especially Inter-Facility Consults – should have spaces removed from their VistA last name. In certain situations, spaces in the provider’s VistA last name may cause IFC Consults to fail to complete. Removing spaces from the VistA last will prevent this problem. Space removal can be accomplished two ways: by combining the parts of the last name or including a hyphen. For example, the name "DE LUCA" should be changed to "DELUCA". Another example: the unhyphenated last name "JONES SMITH" should be changed to "JONES-SMITH". Please contact your facility system access coordinator with your request to edit your VistA last name. Space removal is also recommended as part of VA name standardization; more details are described by Kernel patches XU\*8\*134 and XU\*8\*343.

\*NOTE: If t<span id="SignatureBlockNote" class="anchor"></span>he SIGNATURE BLOCK PRINTED NAME and SIGNATURE BLOCK TITLE fields are disabled at your site, contact your supervisor to request entry of your name and title.

The signature block, as changed in the example above, looks like this:

/es/CPRSPROVIDER,SEVEN

MD

The /es/ annotation indicates that the medical document was electronically signed

If for some reason you do not sign an order at the time you write it, then the system enters the order into your list of alerts. Signing the order is then simply a matter of responding to the alert as in the following example:

You have PENDING ALERTS

Enter "VA VIEW ALERTS to review alerts

Select OE/RR Manager Menu Option: VA View Alerts

1\. CPRSPATIE (C0999): Order requires electronic signature.

2\. TIUPATIEN (T3456): New Consult/Request (Stat)

Select from 1 to 2

or enter ?, A I, F, P, M, R, or ^ to exit: 1

Searching for the patient's chart ...

Unsigned Orders Feb 13, 1999 13:01:58 Page: 1 of 1

CPRSPATIENT,TWELVE 666-24-3456 1A/B-1 FEB 3,1923 (74) \<CA\>

PrimCare: CPRSProvider, Three PCTeam: GOLD

Item Ordered Requestor Start Stop Sts

1 CT ABDOMEN W&W/O CONT \*UNSIGNED\* \| CPRSPROVIDER,THREE unr

2 Discontinue CBC BLOOD WC LB# 269 \| CPRSPROVIDER,TEN unr

\*UNSIGNED\* \|

3 Change SODIUM SERUM SERUM WC to GLUCOSE \| pend

SERUM SERUM SP LB# 242 \*UNSIGNED\* \|

4 Change GLUCOSE SERUM SERUM SP to \| pend

POTASSIUM SERUM SERUM SP LB# 242 \|

\*UNSIGNED\* \|

Enter the numbers of the items you wish to act on. \>\>\>

\+ Next Screen - Previous Screen Q Quit

Select:Quit// 1

Unsigned Orders Feb 13, 1998 13:02:58 Page: 1 of 1

CPRSPATIENT,TWELVE 666-24-2342 1A/B-1 FEB 3,1923 (74) \<CA\>

PrimCare: CPRSProvider, Three PCTeam: GOLD

Item Ordered Requestor Start Stop Sts

1 CT ABDOMEN W&W/O CONT \*UNSIGNED\* \| CPRSPROVIDER,THREE unr

2 Discontinue CBC BLOOD WC LB# 269 \| CPRSPROVIDER,TEN unr

\*UNSIGNED\* \|

3 Change SODIUM SERUM SERUM WC to GLUCOSE \| pend

SERUM SERUM SP LB# 242 \*UNSIGNED\* \|

4 Change GLUCOSE SERUM SERUM SP to \| pend

POTASSIUM SERUM SERUM SP LB# 242 \|

\*UNSIGNED\* \|

Enter the numbers of the items you wish to act on. \>\>\>

Change Sign

Discontinue Detailed Display

Select action: S Sign

-- CT ABDOMEN W&W/O CONT --

Enter your Current Signature Code: SIGNATURE VERIFIED

CT ABDOMEN W&W/O CONT signed.

Print CHART COPY for the orders: YES// \<Enter\> YES

DEVICE: LTA35// \<Enter\> C-ITOH 300 LINE PRINTER

DO YOU WANT YOUR OUTPUT QUEUED? NO// \<Enter\> (NO)

Unsigned Orders Feb 13, 1998 13:03:58 Page: 1 of 1

CPRSPATIENT,TWELVE 666-24-2342 1A/B-1 FEB 3,1923 (74) \<CA\>

PrimCare: CPRSProvider, Three PCTeam: GOLD

Item Ordered Requestor Start Stop Sts

1 CT ABDOMEN W&W/O CONT \*UNSIGNED\* \| CPRSPROVIDER,ONE unr

2 Discontinue CBC BLOOD WC LB# 269 \| CPRSPROVIDER,TWO unr

\*UNSIGNED\* \|

3 Change SODIUM SERUM SERUM WC to GLUCOSE \| pend

SERUM SERUM SP LB# 242 \*UNSIGNED\* \|

4 Change GLUCOSE SERUM SERUM SP to \| pend

POTASSIUM SERUM SERUM SP LB# 242 \|

\*UNSIGNED\* \|

Enter the numbers of the items you wish to act on. \>\>\>

\+ Next Screen - Previous Screen Q Quit

Select:Quit// \<Enter\> Quit

### The Consult Service Gets a Written Copy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The consult service receives an alert and a printed SF 513. The Consultation Form is automatically generated in the receiving clinic when the requesting physician signs the order. (In the case of Inter-Facility Consults, the request in routed to the resulting facility and printed there.) A Secondary Printer can be configured in VistA (see the *Consult/Request Tracking Technical Manual* for instructions). When configured, this automatically prints the SF 513 to both services whenever printing is requested.

> **CAUTION:** The Consultation Form (SF 513) generated by this package for use by the receiving services is highly confidential and should be treated with the same security precautions as other patient medical record documents.

The computerized consultation form created and printed by this package may only be placed in a patient’s medical record, as a valid medical form, *if* it has been authorized for medical record use by the Medical Records Committee at your facility.

--------------------------------------------------------------------------------

MEDICAL RECORD \| CONSULTATION SHEET

--------------------------------------------------------------------------------

CPRSPATIENT,NINETY

XXX-XX-9200 02/03/1904 <span id="GMRC_89_1" class="anchor"></span>(Age 113) NSC VETERAN

CV ELIGIBLE

Cell: (000) 555-1919

--------------------------------------------------------------------------------

Consult Request: Consult \|Consult No.: 10943

--------------------------------------------------------------------------------

To: CARDIOLOGY

From: 2B MED \|Requested: 08/24/2009 11:00 am

--------------------------------------------------------------------------------

Requesting Facility: BOISE \|ATTENTION: CPRSPROVIDER,SEVEN

================================================================================

REASON FOR REQUEST: (Complaints and findings)

Patient has a Hx of hypertrophic cardiomyopathy Dx'ed 3 years ago and

seems to be somewhat stable. Lung fields appear slightly edematious on

Chest X-Ray and we need an assessment of cardiac function prior to

increasing Digitalis dosages.

--------------------------------------------------------------------------------

PROVISIONAL DIAG: Cardiomyopathy, Hypertrophic (425.1)

--------------------------------------------------------------------------------

REQUESTED BY: \|PLACE: \|URGENCY:

CPRSPROVIDER,TEN \|Bedside \|Routine

PHYSICIAN \| \|

(Pager: ) \|SERVICE RENDERED AS: \| <span id="CID_working_copy" class="anchor"></span>Clinically Indicated

date:

(Phone: ) \|Inpatient \| Jan 31, 2011

--------------------------------------------------------------------------------

W O R K I N G C O P Y

No Consultation Results available.

================================================================================

AUTHOR & TITLE: \|

\|DATE:

--------------------------------------------------------------------------------

ID \#:\_\_\_\_\_\_\_\|ORGANIZATION: BOISE \|REG \#:\_\_\_\_ \|LOC: 2B MED

--------------------------------------------------------------------------------

Standard Form 513 (Rev 9-77)

### If Accepted, an Appointment is Held 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is fairly common for a consult to be sent to the wrong clinic. For this reason, it is very easy to forward a consult to another clinic. Simply use the FR (Forward Request) action to specify the new receiving clinic.

In this example, a Neurology consult is forwarded to Psychiatry at the discretion of the consulting physician:

Select OPTION NAME: ORMGR OE/RR Manager Menu menu

You have PENDING ALERTS

Enter "VA VIEW ALERTS to review alerts

Select OE/RR Manager Menu Option: VA View Alerts

1.I CPRSPATIE (C3779): Critical High Lab: LITHIUM 5 02/06 10:51

2\. ARTPATIEN (A9600): New Consult/Request (Today)

Select from 1 to 12

or enter ?, A I, F, P, M, R, or ^ to exit: 2

Consult/Request Alerts Feb 13, 1999 13:06 Page: 1 of 1

CPRSPATIENT,TWELVE 666-24-3779 1A/B-1 FEB 3,1923 (74) \<CA\>

Ward: 2B MED

Requested St No. Consult/Procedure Request

185 02/12/97 p 1636 NEUROLOGY Consult

Enter ?? for more actions

RC Receive CM Add Comment DD Detailed Display

FR Forward CT Complete/Update RT Results Display

CX Cancel (Deny) MA Make Addendum PF Print Form 513

DC Discontinue SC Schedule

Select Action: Quit// FR Forward Consult

Forward Request To Another Service For Action.

Select the service to send the consult to.

Forward Consult to which Service/Specialty: PSYCHIATRY

Who is responsible for Forwarding the Consult: CPRSPROVIDER,SEVEN CS HYN

Actual Date/Time of Activity: NOW// (Feb 13, 1999@14:24)

Urgency: Today// \<Enter\> Today

Enter COMMENT:

1\> List of symptoms indicates Psychiatry would give better work up.

2\> \<Enter\>

EDIT Option: \<Enter\>

(Continued on the next page.)

Consult/Request Alerts Feb 13, 1998 13:07 Page: 1 of 1

CPRSPATIENT,TWELVE 666-24-3779 1A/B-1 FEB 3,1923 (74) \<CA\>

Number Date Stat Service Procedure

185 02/12/97 p PSYCHIATRY Consult

Enter ?? for more actions

RC Receive CM Add Comment DD Detailed Display

FR Forward CT Complete/Update RT Results Display

CX Cancel (Deny) MA Make Addendum PF Print Form 513

DC Discontinue SC Schedule

Select Action: Quit//

#### Receive the Consult

Performing the Receive action on a consult changes its status from Pending to Active. This puts your clinic on record as accepting responsibility for completing the consult.

There are two ways to receive a consult:

From a consult tracking screen.

From a notification alert of a new consult. See page 128 for an example of this method.

In the following example, we receive a consult from a consult tracking screen:

CONSULT TRACKING Oct 05, 2000 09:18:22 Page: 1 of 1

CPRSPATIENT,TWELVE 666-24-3779 1A/B-1 FEB 3,1923 (74) \<CA\>

Wt.(lb): No Entry

Requested St No. Consult/Procedure Request

1 05/06/97 p 226 PSYCHIATRY Cons

Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Select: Quit// RC Receive Request

Who received it?: CPRSPROVIDER,SEVEN CS

Date/Time Actually Received: NOW// \<Enter\> (NOV 01, 1997@09:05)

Enter COMMENT...

1\>Pt will be seen ASAP

2\> \<Enter\>

EDIT Option: \<Enter\>

CONSULT TRACKING Oct 05, 2000 09:18:22 Page: 1 of 1

CPRSPATIENT,TWELVE 666-24-3779 1A/B-1 FEB 3,1923 (74) \<CA\>

Wt.(lb): No Entry

Requested St No. Consult/Procedure Request

1 05/06/97 a 226 PSYCHIATRY Cons

Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Select: Quit//

### Results are Entered and Signed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The consult service enters results and comments. When you request the Complete (CT) action from the Consults service tracking or CPRS Consults screen, V*IST*A shifts you into TIU.

In the following example, we complete a consult and enter findings through Consult’s link to TIU:

Select Consult Service Tracking Option: CS Consult Service Tracking

Select Patient: CPRSPATIENT,TWELVE 05-05-55 666553779 YES SC

VETERAN

Select Service/Specialty: ALL SERVICES// PULMONARY

List From Starting Date: ALL DATES // \<Enter\> ALL DATES

CONSULT TRACKING Oct 05, 2000 09:22:45 Page: 1 of 1

CPRSPATIENT,TWELVE 666-24-3779 1A/B-1 FEB 3,1923 (74) \<CA\>

Wt.(lb): 180

Requested St No. Consult/Procedure Request

1 09/04/97 p 319 PULMONARY Cons

Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Select: Quit// CT Complete

CHOOSE No. 1-2: 1

Creating new progress note...

Patient Location: 2B

Date/time of Admission: 10/05/00 09:22

Date/time of Note: NOW

Author of Note: CPRSPROVIDER,SEVEN

...OK? YES// \<Enter\>

Calling text editor, please wait...

==\[ WRAP \]==\[ INSERT \]===\< Patient: CPRSPATIENT,TWELVE \>===\[ \<PF1\>H=Help \]===

Mr. CPRSPatient’s regimen is lacking in inhaled corticosteroids. Recognizing

that asthma is an inflammatory process, inhaled steroids are important

in controlling the inflammatory response. My practice for severely

out-of-control asthmatics is to use high-dose inhaled steroids,

typically vanceril, 16 puffs qid, with a spacing device such as the

Aerochamber. I would institute such a regimen while he is here.

Mr. CPRSPatient has an in-house pet dog and an outside pet cat. I have

told him that the cat should go, even if it is outdoors. Cat saliva

contains a glycoprotein that leaves residue on their coats and flakes

into the air; it is problematic for many asthmatics.

The purulent phlegm asthmatics have during exacerbations is usually

due to the eosinophils, not from infection. Antibiotics are usually

not necessary.

If you like, you may refer Mr. CPRSPatient to my clinic after discharge.

\<======T=======T=======T=======T=======T=======T=======T=======T=======T=\>=====T

(Continued on next page.)

Saving MEDICINE CONSULT with changes...

Enter your Current Signature Code: SIGNATURE VERIFIED..

Print this note? No// Y YES

Do you want WORK copies or CHART copies? CHART// \<Enter\>

DEVICE: HOME// WORK OTC

DO YOU WANT YOUR OUTPUT QUEUED? NO// Y (YES)

Requested Start Time: NOW// \<Enter\> (Oct 05, 2000 09:23:05)

Request Queued!

CONSULT TRACKING Oct 05, 2000 09:23:45 Page: 1 of 1

CPRSPATIENT,TWELVE 666-24-3779 1A/B-1 FEB 3,1923 (74) \<CA\>

Wt.(lb): 180

Requested St No. Consult/Procedure Request

1 09/04/97 c 319 PULMONARY Cons

Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Select: Quit//

> **NOTE:** <span id="GMRC_89_ClosToolNote" class="anchor"></span>The Consult Closure Tool in VistA can be used to generate a team list of consults with a pending status that potentially need to be closed. The tool can be configured to search for consults by Clinic, Procedure, Service, and Order Item. The resulting list can be reviewed in CPRS, and consults can be closed using the tool within VistA. The *Consult/Request Tracking Technical Manual* provides instructions on using the tool.

### The Originating Clinician Receives an Alert that the Consult is Complete

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the consult is complete, Notifications sends an alert (via FileMan Alerts) of the completion. This is done while you are in the menu terminal mode, as such:

CPRSPATIE (C8829): Completed Consult CAR

TIUPATIEN (T2342): Cancelled consult PLM

ARTPATIEN (A9898): Completed Consult GASTROENTEROLOGY

CPRSPATIE (C8831): Completed Consult PLM with Sig Findings

Enter "VA VIEW ALERTS to review alerts

Select Consult Service Tracking Option:

To receive an on-screen report of the results, respond as in the following example:

Select Consult Service Tracking Option: VA View Alerts

1\. CPRSPATIE (C8829): Completed Consult CAR

2\. TIUPATIEN (T2342): Cancelled consult PLM

3\. ARTPATIEN (A9898): Completed Consult GASTROENTEROLOGY

4\. CPRSPATIE (C8831): Completed Consult PLM with Sig Findings

Select from 1 to 4

or enter ?, A I, F, P, M, R, or ^ to exit

or RETURN to continue: 3

Processing alert: TIUPATIEN (T8829): Completed Consult PLM

Consult/Request Alerts Feb 26, 1999 14:56:57 Page: 1 of 1

TIUPATIENT,TWELVE 666-24-2342 1A/B-1 FEB 3,1923 (74) \<CA\>

Wt.(lb): No Entry

Requested St No. Consult/Procedure Request

1 01/08/99 c 1337 PULMONARY Cons

Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Compiling Result Display...

(Continued on next page.)

Here we select the Results Display (RT) action:

Results Display Feb 26, 1999 14:59:10 Page: 1 of 1\_

TIUPATIENT,TWELVE 666-24-2342 1A/B-1 FEB 3,1923 (74) \<CA\>

Consult No.: 1337 Wt.(lb): No Entry

------------------------------MEDICINE CS CONSULT------------------------------

Pt should stay away from Oyster Crackers.

Signature: /es/CPRSPROVIDER,SEVEN Date: FEB 12, 1999@11:35:14

Source Information

Document Status: COMPLETED

Entry Date: FEB 12, 1999@11:32 Author: CPRSPROVIDER,S

Expected Signer: CPRSPROVIDER,SEVEN Expected Cosigner: None

Entered By: CRS TIU Document \#: 5365

Urgency: None

================================================================================

Enter ?? for more actions

Select Action: Quit//

### The SF 513 Report Becomes Part of the Patient’s Medical Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the consult is complete, Consults sends an alert to the requesting physician. The requesting physician can use the Print Report action to obtain a copy of the final Consults report. In the following example, the consult we want to print has already been selected:

CONSULT TRACKING Feb 13, 1998 13:20:44 Page: 1 of 1

CPRSPATIENT,TWELVE 666-24-3779 1A/B-1 FEB 3,1923 (74) \<CA\>

Wt.(lb): 178

Requested St No. Consult/Procedure Request

1 11/01/97 c 675 PULMONARY Consult

2 10/28/97 a 506 \<MEDICINE EAST\> Consult

3 07/21/97 c 285 PULMONARY Pulmonary Function Test

Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Select: Quit// PT Print Form

Chart Copy (Y/N) Y// \<Enter\>

DEVICE: HOME// ;;9999 HOME

(Continued on next page)

MEDICAL RECORD \| CONSULTATION SHEET

--------------------------------------------------------------------------------

CPRSPATIENT,FOUR SERVICE CONNECTED 50% to 100%

XXX-XX-4442 03/03/1960 <span id="GMRC_89_2" class="anchor"></span>Age: 57 SC VETERAN

123 SESAME ST.

APT. 4

SALT LAKE CITY UTAH 84101 Phone: 000-555-1289 Cell: 000 -555-1010

--------------------------------------------------------------------------------

Consult Request: Consult \|Consult No.: 675

--------------------------------------------------------------------------------

To: PULMONARY

From: NOT 2B \|Requested: 11/01/1997 10:13 am

--------------------------------------------------------------------------------

Requesting Facility: ELY \|ATTENTION: CPRSPROVIDER,TWO ================================================================================

Current Primary Care Provider: CPRSPROVIDER,SEVEN

Current Primary Care Team: GOLD TEAM

REASON FOR REQUEST: (Complaints and findings)

Pt experiences shortness of breath when out of bed.

--------------------------------------------------------------------------------

PROVISIONAL DIAG: CHEESE HANDLER’S LUNG

--------------------------------------------------------------------------------

REQUESTED BY: \|PLACE: \|URGENCY:

CPRSPROVIDER,SEVEN \|Bedside \|Routine

Chief of Surgery \| \|

(Pager: 9999) \|SERVICE RENDERED AS: \|

(Phone: 1234) \|Inpatient \|

--------------------------------------------------------------------------------

W O R K I N G C O P Y

CONSULTATION NOTE \#2330

TITLE: PULMONARY CS CONSULT

DATE OF NOTE: NOV 01, 1997@10:15:35 ENTRY DATE: NOV 01, 1997@10:15:35

AUTHOR: CPRSPROVIDER,SEVEN EXP COSIGNER:

URGENCY: STATUS: COMPLETED

At the time I went to examine the pt, he was acutely broncho-

spastic and in moderately severe respiratory distress. I had him

deliver a puff of albuterol with an Aerochamber; his technique was

poor. I then instructed him and delivered an additional four puffs,

which he did with good technique. He was improved and with a clear

lung exam within a few seconds (though wheezes were still present

on forced expiration).

The pt regimen is lacking in inhaled corticosteroids. Recognizing

that asthma is an inflammatory process, inhaled steroids are important

in controlling the inflammatory response. My practice for severely

out-of-control asthmatics is to use high-dose inhaled steroids,

typically vanceril, 16 puffs qid, with a spacing device such as the

Aerochamber. I would institute such a regimen while he is here.

/es/ CPRSPROVIDER,SEVEN

Signed: 11/01/1997 10:17

--------------------------------------------------------------------------------

PROVISIONAL DIAG: Arrhythmia (427.9)

--------------------------------------------------------------------------------

REQUESTED BY: \|PLACE: \|URGENCY:

CASEY,BEN \|Bedside \|Routine

CHIEF OF SURGERY \| \|

(Pager: ) \|SERVICE RENDERED AS: \|<span id="CID_SF513" class="anchor"></span>CLINICALLY INDICATED DATE:

(Phone: ) \|Inpatient \|Jan 31, 2011

-------------------------------------------------------------------------------

See page 126 for details on the Print Report (PR) action.

## Quick Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Quick Orders are a feature of CPRS that allow certain prompts to be automatically filled in by the computer. Your ADPAC can set them up (a subject that is discussed in the *CPRS Setup Guide*.)

CPRS is shipped with a number of quick orders. Number 91, EKG, Portable on the screen pictured below is one of them. These quick orders do not have any of the fields filled in. They are only provided as place-holders and limited examples of what is possible.

Add New Orders Feb 13, 1998 13:21:08 Page: 1 of 1

CPRSPATIENT,TWELVE 666-24-3779 1A/B-1 FEB 3,1923 (74) \<CA\>

0 ORDER SETS... 30 PATIENT CARE... 70 LABORATORY...

1 Patient Movement 31 Condom Catheter 71 Chem 7

2 Diagnosis 32 Guaiac Stools 72 T&S

3 Condition 33 Incentive Spirometer 73 Glucose

4 Allergies 34 Dressing Change 74 CBC w/Diff

75 PT

10 PARAMETERS... 40 DIETETICS... 76 PTT

11 TPR B/P 41 Regular Diet 77 CPK

12 Weight 42 Tubefeeding 78 CPK

13 I & O 43 NPO at Midnight 79 LDH

14 Call HO on 80 Urinalysis

50 IV FLUIDS... 81 Culture & Suscept

20 ACTIVITY... 51 OUTPATIENT MEDS...

21 Ad Lib 55 INPATIENT MEDS... 90 OTHER ORDERS...

23 Bed Rest / BRP 91 EKG: Portable

24 Ambulate TID 60 IMAGING ...

25 Up in Chair TID 61 Chest 2 views PA&LAT 99 Text Only Order

Enter the number of each item you wish to order. \>\>\>

\+ Next Screen TD Set Delay ... Q Done

Select Item(s): Done//

Basically, quick orders supply stock answers to some of the prompts required to make an order. For example, if we filled in the values for the placeholder EKG, Portable, we might answer the following questions in the quick order template:

Consult to Service/Specialty: Cardiology

Category: Inpatient

Place of Consult: Bedside

These three prompts are then excluded when you select EKG from the orders screen—relieving you of the necessity of filling in answering several prompts.

The other four prompts, Reason for the Request, Urgency, Attention, and Provisional Diagnosis, are all left blank in the quick order template. The answer to these questions change every time we place an order for a portable EKG. These four questions are the only ones asked when you place an order for “EKG, Portable.”

## Using the Consults Package with TIU 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Direct TIU Input

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On page 26 are the directions for entering results from the Consult/ Result Tracking screen. You can also enter results directly from TIU. This may be preferable if you are doing large volumes of consults or it fits your office work flow.

The basic steps to entering findings through TIU given here are. The interested user should look at the *TIU Clinical Coordinator & User Manual* for further information.

#### From TIU, choose Integrated Document Management.

As with almost everything in V*IST*A, exactly how you do this depends on how your system is set up. If you cannot find this option on your menu, consult your ADPAC.

Example:

Select Progress Notes/Discharge Summary \[TIU\] Option: ?

1 Progress Notes User Menu ...

2 Discharge Summary User Menu ...

3 Integrated Document Management ...

4 Personal Preferences ...

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Progress Notes/Discharge Summary \[TIU\] Option: 3 Integrated Document

Management

--- Clinician's Menu ---

Select Integrated Document Management Option:

#### Select Enter/edit Document.

Example:

Select Integrated Document Management Option: ?

1 Individual Patient Document

2 All MY UNSIGNED Documents

3 Multiple Patient Documents

4 Enter/edit Document

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Integrated Document Management Option: Enter/edit Document

#### Enter the patient’s name.

Follow the usual V*IST*A conventions for selecting a patient.

Example:

Select PATIENT NAME: CPRSPATIENT,FIV 03-05-33 666332432 YES SC VETERAN

A: Known allergies

Select TITLE:

#### Select a document title.

Using the standard help functions (? or ??), you can see a list of titles that are available to you. Consult your supervisor or ADPAC about which one is appropriate to your situation.

Example:

Select TITLE: ?

Answer with TIU DOCUMENT DEFINITION NAME, or ABBREVIATION, or

PRINT NAME

Do you want the entire TIU DOCUMENT DEFINITION List? Y (Yes)

Choose from:

ADVANCE DIRECTIVE TITLE

ADVERSE REACTION/ALLERGY TITLE

ASI-ADDICTION SEVERITY INDEX TITLE

BP TEST NOTE TITLE

CLINICAL WARNING TITLE

CRISIS NOTE TITLE

DISCHARGE SUMMARY TITLE

MEDICINE CONSULT TITLE

Select TITLE: MEDICINE CONSULT TITLE

Creating new progress note...

Patient Location: 2B

Date/time of Admission: 05/10/96 10:17

Date/time of Note: NOW

Author of Note: CPRSPROVIDER,SEVEN

...OK? YES//

You must link your Result to a Consult Request...

The following CONSULT REQUEST is available:

1\. JUL 16, 1997@06:08 278 PULMONARY

CHOOSE 1-1:

#### Choose the consult to enter findings.

TIU lists one or more active consults for the patient. Select the one you have findings for.

Example:

The following CONSULT REQUEST is available:

1\. JUL 16, 1997@06:08 278 PULMONARY

CHOOSE 1-1: 1 278

Calling text editor, please wait...

1\>

#### Enter and edit findings.

TIU enters the editor specified in your V*IST*A personal preferences. There are a number of alternate ways to enter findings in TIU. Consult the *TIU Clinical Coordinator & User Manual* for details.

Example:

Calling text editor, please wait...

1\> No significant findings. Suggest respiratory therapy.

2\>

EDIT Option:

Saving MEDICINE CONSULT with changes...

Enter your Current Signature Code:

#### Sign the findings.

At the prompt, enter your signature code. If you do not sign the document at this time, VISTA generates an alert to remind you to sign it at a later time.

There is a detailed discussion of electronic signatures under step 2, *Sign the Consult*.

#### Repeat for other patients.

After TIU accepts your signature, it prompts you for another patient name.

Example:

Enter your Current Signature Code: SIGNATURE VERIFIED..

You may enter another CLINICAL DOCUMENT. Press RETURN to exit.

Select PATIENT NAME:

> **NOTE:** If your site supports the dictation and transcription of Consult results, you may also use the batch upload facility of TIU to support single-point transfer of Consult results in mixed batches (with Discharge Summaries, Progress Notes, etc.) for either in-house or contract transcription services.

### Correcting Misdirected Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Occasionally a consult result is linked to the wrong consult. If this is detected prior to signature, it is possible for the author of a consult result to re-direct the record to a different consult request by any of several methods, as illustrated in the examples below:

- Through the Link to Request action, when processing the alert for the unsigned consult result:
- Through the Individual Patient Document option (which is identical to the Browse action, accessible by a number of familiar paths from TIU Clinician's options, or through the CPRS LM Chart).
- You may choose the Link action from the All My Unsigned Documents Option.
- From the CPRS Chart.

Following signature, such corrections can only be made by those persons who are granted permission to do so under the Authorization/ Subscription Utility (ASU). Information on how to make this kind of correction is contained in the Consult/Request Tracking Technical Manual.

Examples:

You may redirect a consult result through the Link to Request action, when processing the alert for the unsigned consult result:

--- Clinician's Menu ---

1 Progress Notes User Menu ...

2 Discharge Summary User Menu ...

3 Integrated Document Management ...

4 Personal Preferences ...

Select Progress Notes/Discharge Summary \[TIU\] Option: VA View Alerts

1\. CPRSPATIE (C0167P): PULMONARY CONSULT available for signature.

2\. ARTPATIEN (A1414): New order(s) placed.

3\. ARTPATIEN (A1414): New consult PLM (Routine)

4\. CPRSPATIE (C2432): New consult CAR (Routine)

Select from 1 to 4

or enter ?, A I, F, P, M, R, or ^ to exit: 1

Opening PULMONARY CONSULT record for review...

(Continued on the next page.)

Browse Document Jan 26, 1998 16:49:32 Page: 1 of 1

PULMONARY CONSULT

CPRSPATIENT,T 666-01-0167P PULMONARY CLINIC Visit Date: 01/26/98@16:37

DATE OF NOTE: JAN 26, 1998@16:37:34 ENTRY DATE: JAN 26, 1998@16:37:34

AUTHOR: TIUPROVIDER,THREE EXP COSIGNER:

URGENCY: STATUS: UNSIGNED

DEMOGRAPHICS: CPRSPATIENT,TWO

666-01-0167P

31

JAN 1,1967

His disposition is good.

\+ Next Screen - Prev Screen ?? More actions \>\>\>

Find Make Addendum Identify Signers

Print Sign/Cosign Delete

Edit Copy Link ...

Quit

Select Action: Quit// L Link ...

Problem(s) Patient/Visit Link with Request

Specify Linkage: L Link with Request

You must link your Result to a Consult Request...

The following CONSULT REQUEST(S) are available:

1\> JAN 23, 1998@11:14 759 PULMONARY

2\> JAN 23, 1998@11:14 760 PULMONARY

CHOOSE 1-2: 2 760

Opening PULMONARY CONSULT record for review...

Browse Document Jan 26, 1998 16:49:32 Page: 1 of 1

PULMONARY CONSULT

CPRSPATIENT,T 666-01-0167P PULMONARY CLINIC Visit Date: 01/26/98@16:37

DATE OF NOTE: JAN 26, 1998@16:37:34 ENTRY DATE: JAN 26, 1998@16:37:34

AUTHOR: TIUPROVIDER,THREE EXP COSIGNER:

URGENCY: STATUS: UNSIGNED

DEMOGRAPHICS: CPRSPATIENT,TWO

666-01-0167P

31

JAN 1,1967

His disposition is good.

\+ Next Screen - Prev Screen ?? More actions \>\>\>

Find Make Addendum Identify Signers

Print Sign/Cosign Delete

Edit Copy Link ...

Quit

Select Action: Quit// \<Enter\> Quit

(Continued on the next page.)

1\. CPRSPATIE (C2342): New order(s) placed.

2\. TIUPATIEN (T0167P): PULMONARY CONSULT available for signature.

3\. ARTPATIEN (A1414): New order(s) placed.

4\. ARTPATIEN (A1414): New consult PLM (Routine)

5\. CPRSPATIE (C2432): New consult CAR (Routine)

Select from 1 to 5

or enter ?, A I, F, P, M, R, or ^ to exit: \<Enter\>

2\. Through the Individual Patient Document option as shown here (which is identical to the Browse action, accessible by a number of familiar paths from TIU Clinician's options, or through the CPRS LM Chart):

--- Clinician's Menu ---

1 Progress Notes User Menu ...

2 Discharge Summary User Menu ...

3 Integrated Document Management ...

4 Personal Preferences ...

Select Progress Notes/Discharge Summary \[TIU\] Option: INtegrated Document Management

--- Clinician's Menu ---

1 Individual Patient Document

2 All MY UNSIGNED Documents

3 Multiple Patient Documents

4 Enter/edit Document

Select Integrated Document Management Option: INdividual Patient Document

Select PATIENT NAME: CPRSPATIENT,TWO 01-01-67 666010167P ACTIVE DUTY

A: Known allergies

Available documents: 06/13/91 thru 01/26/98 (7)

Please specify a date range from which to select documents:

List documents Beginning: 06/13/91// T-1 (JAN 25, 1998)

Thru: 01/26/98// \<Enter\> (JAN 26, 1998)

1 01/26/98 16:37 PULMONARY CONSULT CPRSPROVIDER,TWO

Visit: 01/26/98

One document found within date range...

Opening PULMONARY CONSULT record for review...

(Continued on the next page.)

Browse Document Jan 26, 1998 16:49:32 Page: 1 of 1

PULMONARY CONSULT

CPRSPATIENT,T 666-01-0167P PULMONARY CLINIC Visit Date: 01/26/98@16:37

DATE OF NOTE: JAN 26, 1998@16:37:34 ENTRY DATE: JAN 26, 1998@16:37:34

AUTHOR: TIUPROVIDER,THREE EXP COSIGNER:

URGENCY: STATUS: UNSIGNED

DEMOGRAPHICS: CPRSPATIENT,TWO

666-01-0167P

31

JAN 1,1967

His disposition is good.

\+ Next Screen - Prev Screen ?? More actions \>\>\>

Find Make Addendum Identify Signers

Print Sign/Cosign Delete

Edit Copy Link ...

Quit

Select Action: Quit// L Link ...

Problem(s) Patient/Visit Link with Request

Specify Linkage: L Link with Request

You must link your Result to a Consult Request...

The following CONSULT REQUEST(S) are available:

1\> JAN 23, 1998@11:14 759 PULMONARY

2\> JAN 23, 1998@11:14 760 PULMONARY

CHOOSE 1-2: 2 760

Opening PULMONARY CONSULT record for review...

(Continued on the next page.)

Browse Document Jan 26, 1998 16:49:32 Page: 1 of 1

PULMONARY CONSULT

CPRSPATIENT,T 666-01-0167P PULMONARY CLINIC Visit Date: 01/26/98@16:37

DATE OF NOTE: JAN 26, 1998@16:37:34 ENTRY DATE: JAN 26, 1998@16:37:34

AUTHOR: TIUPROVIDER,THREE EXP COSIGNER:

URGENCY: STATUS: UNSIGNED

DEMOGRAPHICS: CPRSPATIENT,THREE

666-01-0167P

31

JAN 1,1967

His disposition is good.

\+ Next Screen - Prev Screen ?? More actions \>\>\>

Find Make Addendum Identify Signers

Print Sign/Cosign Delete

Edit Copy Link ...

Quit

Select Action: Quit// \<Enter\> Quit

Select PATIENT NAME: \<Enter\>

Nothing selected.

3\. You may choose the Link action from the All My Unsigned Documents Option, as shown below:

--- Clinician's Menu ---

1 Individual Patient Document

2 All MY UNSIGNED Documents

3 Multiple Patient Documents

4 Enter/edit Document

Select Integrated Document Management Option: All MY UNSIGNED Documents

Searching for the documents.....

MY UNSIGNED Documents Jan 26, 1998 16:51:18 Page: 1 of 3

by AUTHOR (TIUPROVIDER,THREE) or EXPECTED COSIGNER 40 documents

Patient Document Ref Date Status

1 CPRSPATIENT,T (C0167) PULMONARY CONSULT 01/26/98 unsigned

2 ARTPATIENT,TW (A4321) Adverse React/Allergy 01/22/98 unsigned

3 CPRSPATIENT,O (C8796) Reparatory Therapy Note 01/20/98 uncosigned

4 CPRSPATIENT,F (R1350) Reparatory Therapy Note 01/16/98 uncosigned

5 CPRSPATIENT,T (C9999) Reparatory Therapy Note 01/16/98 uncosigned

6 CPRSPATIENT,T (C1350) Reparatory Therapy Note 01/15/98 uncosigned

7 TIUPATIENT,EI (T1239) Reparatory Therapy Note 01/15/98 uncosigned

8 CPRSPATIENT,T (C1563) Reparatory Therapy Note 01/14/98 uncosigned

9 CPRSPATIENT,T (C1563) Reparatory Therapy Note 01/14/98 uncosigned

10 PNPATIENT,FIV (P1350) Reparatory Therapy Note 01/14/98 uncosigned

11 DSPATIENT,TEN (D6572) Reparatory Therapy Note 01/14/98 uncosigned

12 HSPATIENT,ONE (H2591) Reparatory Therapy Note 01/14/98 uncosigned

13 TIUPATIENT,EI (T1239) Reparatory Therapy Note 01/14/98 uncosigned

14 TIUPATIENT,EI (T1239) Reparatory Therapy Note 01/14/98 uncosigned

\+ + Next Screen - Prev Screen ?? More Actions \>\>\>

Find Sign/Cosign Change View

Add Document Detailed Display Copy

Edit Browse Delete Document

Make Addendum Print Quit

Link ... Identify Signers

Select Action: Next Screen// L Link ...

Problems Patient/Visit Link with Request

Specify Linkage: L Link with Request

Select Document(s): (1-14): 1

You must link your Result to a Consult Request...

The following CONSULT REQUEST(S) are available:

1\> JAN 23, 1998@11:14 759 PULMONARY

2\> JAN 23, 1998@11:14 760 PULMONARY

CHOOSE 1-2: 2 760

(Continued on next page.)

MY UNSIGNED Documents Jan 26, 1998 16:51:32 Page: 1 of 3

by AUTHOR (TIUPATIENT,THREE) or EXPECTED COSIGNER 40 documents

Patient Document Ref Date Status

1 CPRSPATIENT,T (C0167) PULMONARY CONSULT 01/26/98 unsigned

2 ARTPATIENT,TW (A4321) Adverse React/Allergy 01/22/98 unsigned

3 CPRSPATIENT,O (C8796) Reparatory Therapy Note 01/20/98 uncosigned

4 CPRSPATIENT,F (R1350) Reparatory Therapy Note 01/16/98 uncosigned

5 CPRSPATIENT,T (C9999) Reparatory Therapy Note 01/16/98 uncosigned

6 CPRSPATIENT,T (C1350) Reparatory Therapy Note 01/15/98 uncosigned

7 TIUPATIENT,EI (T1239) Reparatory Therapy Note 01/15/98 uncosigned

8 CPRSPATIENT,T (C1563) Reparatory Therapy Note 01/14/98 uncosigned

9 CPRSPATIENT,T (C1563) Reparatory Therapy Note 01/14/98 uncosigned

10 PNPATIENT,FIV (P1350) Reparatory Therapy Note 01/14/98 uncosigned

11 DSPATIENT,TEN (D6572) Reparatory Therapy Note 01/14/98 uncosigned

12 HSPATIENT,ONE (H2591) Reparatory Therapy Note 01/14/98 uncosigned

13 TIUPATIENT,EI (T1239) Reparatory Therapy Note 01/14/98 uncosigned

14 TIUPATIENT,EI (T1239) Reparatory Therapy Note 01/14/98 uncosigned

\+ \*\* Item 1 Reassigned. \*\* \>\>\>

Find Sign/Cosign Change View

Add Document Detailed Display Copy

Edit Browse Delete Document

Make Addendum Print Quit

Link ... Identify Signers

Select Action: Next Screen// Q Quit

--- Clinician's Menu ---

1 Individual Patient Document

2 All MY UNSIGNED Documents

3 Multiple Patient Documents

4 Enter/edit Document

Select Integrated Document Management Option:

4\. From the CPRS Chart, the dialog looks like this (NOTE: If CONSULTS is defined as a CLASS under CLINICAL DOCUMENTS, this approach is not yet available):

OE CPRS Clinician Menu

RR Results Reporting Menu

AD Add New Orders

RO Act On Existing Orders

PP Personal Preferences ...

Select Clinician Menu Option: OE CPRS Clinician Menu

Clinic PULMONARY CLINIC Jan 27, 1998 15:20:32 Page: 1 of 1

Current patient: \*\* No patient selected \*\*

Patient Name ID DOB Appointment Date

No patients found.

Enter the number of the patient chart to be opened

\+ Next Screen CV Change View ... FD Find Patient

\- Previous Screen SV Save as Default List Q Close

Select Patient: Change View// CPRSPATIENT, FIFTYTHREE 01-01-67

107010167P ACTIVE DUTY

A: Known allergies

Searching the patient's chart ...

(Continued on the next page.)

Cover Sheet Jan 27, 1998 15:20:40 Page: 1 of 1

CPRSPATIENT,TWO 666-01-0167P1A JAN 1,1967 (31) \<A\>

Item Entered

Allergies/Adverse Reactions \|

1 DUST \| 10/07/97

\|

Patient Postings \|

\<None\> \|

\|

Recent Vitals \|

No data available \|

\|

Immunizations \|

No immunizations found. \|

\|

Eligibility \|

Not Service Connected \|

\|

Enter the numbers of the items you wish to act on. \>\>\>

NW Enter New Allergy/ADR CV (Change View ...) SP Select New Patient

AD Add New Orders CC Chart Contents ... Q Close Patient Chart

Select: Chart Contents// CC;N Chart Contents ...

Searching the patient's chart ...

Signed Notes Jan 27, 1998 15:20:46 Page: 1 of 1

CPRSPATIENT,TWO 666-01-0167P1A JAN 1,1967 (31) \<A\>

Currently viewing 17 notes

Title Written Author SigSt

1 PULMONARY CONSULT \| 01/26 16:37 CPRSPROVI compl

2 Respiratory Therapy Note \| 12/11 16:59 CPRSPROVI uncos

3 General Note \| 10/16 /91 CPRSPROVI compl

4 General Note \| 06/17 /91 CPRSPROVI compl

5 General Note \| 06/13 /91 CPRSPROVI compl

Enter the numbers of the items you wish to act on. \>\>\>

NW Write New Note CV Change View ... SP Select New Patient

AD Add New Orders CC Chart Contents ... Q Close Patient Chart

Select: Chart Contents// CV Change View ...

(Continued on the next page.)

Signed Notes Jan 27, 1998 15:20:46 Page: 1 of 1

CPRSPATIENT,TWO 666-01-0167P1A JAN 1,1967 (31) \<A\>

Currently viewing 17 notes

Title Written Author SigSt

1 PULMONARY CONSULT \| 01/26 16:37 CPRSPROVI compl

2 Cardiology Note \| 12/11 16:59 CPRSPROVI uncos

3 General Note \| 10/16 /91 CPRSPROVI compl

4 General Note \| 06/17 /91 CPRSPROVI compl

5 General Note \| 06/13 /91 CPRSPROVI compl

Enter the numbers of the items you wish to act on. \>\>\>

1 all signed 4 signed/author Save as Preferred View

2 my unsigned 5 signed/dates Remove Preferred View

3 my uncosigned

Select context: 2 my unsigned

Searching the patient's chart ...

Unsigned Notes Jan 27, 1998 15:20:55 Page: 1 of 1

CPRSPATIENT,TWO 666-01-0167P1A JAN 1,1967 (31) \<A\>

Currently viewing all unsigned notes

Title Written Author SigSt

1 PULMONARY CONSULT \| 01/27 15:19 CPRSPROVI unsig

Enter the numbers of the items you wish to act on. \>\>\>

NW Write New Note CV Change View ... SP Select New Patient

AD Add New Orders CC Chart Contents ... Q Close Patient Chart

Select: Chart Contents// 1

(Continued on the next page.)

Unsigned Notes Jan 27, 1998 15:20:55 Page: 1 of 1

CPRSPATIENT,TWO 666-01-0167P1A JAN 1,1967 (31) \<A\>

Currently viewing all unsigned notes

Title Written Author SigSt

1 PULMONARY CONSULT \| 01/26 16:37 CPRSPROVI unsig

Enter the numbers of the items you wish to act on. \>\>\>

Edit Detailed Display Identify signers

Make Addendum Browse Copy

Sign Print Delete

Select Action: BR Browse

Browse Document Jan 26, 1998 16:49:32 Page: 1 of 1

PULMONARY CONSULT

CPRSPATIENT,T 666-01-0167P PULMONARY CLINIC Visit Date: 01/26/98@16:37

DATE OF NOTE: JAN 26, 1998@16:37:34 ENTRY DATE: JAN 26, 1998@16:37:34

AUTHOR: TIUPROVIDER,THREE EXP COSIGNER:

URGENCY: STATUS: UNSIGNED

DEMOGRAPHICS: CPRSPATIENT,TWO

666-01-0167P

31

JAN 1,1967

His disposition is good.

\+ Next Screen - Prev Screen ?? More actions \>\>\>

Find Make Addendum Identify Signers

Print Sign/Cosign Delete

Edit Copy Link ...

Quit

Select Action: Quit// L Link ...

Problem(s) Patient/Visit Link with Request

Specify Linkage: L Link with Request

You must link your Result to a Consult Request...

The following CONSULT REQUEST(S) are available:

1\> JAN 23, 1998@11:14 759 PULMONARY

2\> JAN 23, 1998@11:14 760 PULMONARY

CHOOSE 1-2: 2 760

Opening PULMONARY CONSULT record for review...

(Continued on next page.)

Browse Document Jan 26, 1998 16:49:32 Page: 1 of 1

PULMONARY CONSULT

CPRSPATIENT,T 666-01-0167P PULMONARY CLINIC Visit Date: 01/26/98@16:37

DATE OF NOTE: JAN 26, 1998@16:37:34 ENTRY DATE: JAN 26, 1998@16:37:34

AUTHOR: TIUPROVIDER,THREE EXP COSIGNER:

URGENCY: STATUS: UNSIGNED

DEMOGRAPHICS: CPRSPATIENT,TWO

666-01-0167P

31

JAN 1,1967

His disposition is good.

\+ Next Screen - Prev Screen ?? More actions \>\>\>

Find Make Addendum Identify Signers

Print Sign/Cosign Delete

Edit Copy Link ...

Quit

Select Action: Quit// \<Enter\> Quit

Unsigned Notes Jan 27, 1998 15:20:55 Page: 1 of 1

CPRSPATIENT,TWO 666-01-0167P1A JAN 1,1967 (31) \<A\>

Currently viewing all unsigned notes

Title Written Author SigSt

1 PULMONARY CONSULT \| 01/27 15:19 CPRSPROVI unsig

Enter the numbers of the items you wish to act on. \>\>\>

NW Write New Note CV Change View ... SP Select New Patient

AD Add New Orders CC Chart Contents ... Q Close Patient Chart

Select: Chart Contents// Q Close Patient Chart

## Using the Consults Package with Medicine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your site is set up for attaching Medicine results to consults, and there are results available, then Consults prompts you to attach relevant results during the Complete/Update action.

In this example, we attach medicine results to a consult we are completing:

CONSULT TRACKING Jun 21, 2000 14:23:01 Page: 1 of 3

CPRSPATIENT,FOUR 666-43-8796 2B M DEC 4,1949 (50) \<CAD\>

Wt.(lb): No Entry

Requested St No. Consult/Procedure Request

1 05/16/00 a 1719 ELECTROCARDIOGRAM CARDIOLOGY Proc

2 05/15/00 c 1718 ELECTROCARDIOGRAM CARDIOLOGY Proc

3 02/09/00 p 1679 Holter Monitoring CARDIOLOGY Cons

4 06/18/99 a 1538 PACEMAKER SURVEILLANCE CARDIOLOGY Proc

5 04/07/99 c 1433 Holter Monitoring CARDIOLOGY Cons

6 06/11/98 pr 1047 CARDIOLOGY Cons

7 09/24/97 c 341 \*CARDIOLOGY Cons

8 02/03/97 dc 209 CARDIOLOGY Cons

9 07/28/95 c 94 ECHO CARDIOLOGY Proc

10 07/20/95 c 88 ELECTROCARDIOGRAM CARDIOLOGY Proc

11 07/20/95 c 87 ELECTROCARDIOGRAM CARDIOLOGY Proc

12 04/23/92 c 64 \*ELECTROCARDIOGRAM CARDIOLOGY Proc

\+ Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit  
Select: Next Screen// CT Complete/Update

CHOOSE No. 1-32: 1

Attach Medicine Results? Y// \<Enter\> ES

Procedure/Medicine Resulting Jun 21, 2000 14:29:50 Page: 1 of 1

CPRSPATIENT,FOUR 666-43-8796 2B M DEC 4,1949 (50) \<CAD\>

Available Medicine Results

Type of Proc. Procedure Date Summary

1 ELECTROCARDIOGRAM AUG 13,1997 ABNORMAL

2 ELECTROCARDIOGRAM JUL 31,1995@08:04 NORMAL

Select action or item number

AR Associate Result DR Display selected medicine result

Select action: Quit//

Notice that when we tried to complete a consult with available Medicine results, Consults prompted us, “Attach Medicine Results?” By responding affirmatively, we are presented a screen with a list of the qualifying Medicine results and the ability to both explore these results and attach one or more of them to the consult.

For this to happen, two things must have taken place:

1\. Your CAC or IRM must have defined certain procedures as qualifying to provide results to your service.

2\. Those procedures must have been performed on your patient and the results entered into VistA.

In the following example, a medicine result is associated with the current consult and the complete action is finished:

Procedure/Medicine Resulting Jun 21, 2000 14:29:50 Page: 1 of 1

CPRSPATIENT,FOUR 666-43-8796 2B M DEC 4,1949 (50) \<CAD\>

Available Medicine Results

Type of Proc. Procedure Date Summary

1 ELECTROCARDIOGRAM AUG 13,1997 ABNORMAL

2 ELECTROCARDIOGRAM JUL 31,1995@08:04 NORMAL

Select action or item number

AR Associate Result DR Display selected medicine result

Select action: Quit// AR Associate Result

Select item: (1-2): 1

ELECTROCARDIOGRAM AUG 13,1997 ABNORMAL

Are you sure you want to associate this result? NO// Y YES

Procedure/Medicine Resulting Jun 21, 2000 14:41:16 Page: 1 of 1

CPRSPATIENT,FOUR 666-43-8796 2B M DEC 4,1949 (50) \<CAD\>

Available Medicine Results

Type of Proc. Procedure Date Summary

1 ELECTROCARDIOGRAM JUL 31,1995@08:04 NORMAL

Select action or item number

AR Associate Result DR Display selected medicine result

Select action: Quit// \<Enter\> QUIT

Continue with Note Entry? Y// N NO

CONSULT TRACKING Jun 21, 2000 14:41:35 Page: 1 of 3

CPRSPATIENT,FOUR 666-43-8796 2B M DEC 4,1949 (50) \<CAD\>

Wt.(lb): No Entry

Requested St No. Consult/Procedure Request

1 05/16/00 c 1719 ELECTROCARDIOGRAM CARDIOLOGY Proc

2 05/15/00 c 1718 ELECTROCARDIOGRAM CARDIOLOGY Proc

3 02/09/00 p 1679 Holter Monitoring CARDIOLOGY Cons

4 06/18/99 a 1538 PACEMAKER SURVEILLANCE CARDIOLOGY Proc

5 04/07/99 c 1433 Holter Monitoring CARDIOLOGY Cons

6 06/11/98 pr 1047 CARDIOLOGY Cons

7 09/24/97 c 341 \*CARDIOLOGY Cons

8 02/03/97 dc 209 CARDIOLOGY Cons

9 07/28/95 c 94 ECHO CARDIOLOGY Proc

10 07/20/95 c 88 ELECTROCARDIOGRAM CARDIOLOGY Proc

11 07/20/95 c 87 ELECTROCARDIOGRAM CARDIOLOGY Proc

12 04/23/92 c 64 \*ELECTROCARDIOGRAM CARDIOLOGY Proc

\+ Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Select: Next Screen//

Notice that after we exited the Procedure/Medicine Resulting screen, we were prompted about entering a note. If we had responded with a Yes, we would have been able to attach a TIU note to the consult we were closing in addition to the Medicine results.

## Using the Consults Package with Clinical Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Individual consult types can be designated to be resulted with the Clinical Procedures package. If this is the case, then Consults expects clinical procedures results to be attached to the consult. This attachment is usually accomplished with the CPUser program.

If the instrument in question has not yet been connected to Clinical Procedures, then the consult may be completed in the usual way by an authorized provider. (Authorized providers being clinicians whom the CAC has set up as an interpreter for the appropriate service.) In this case Consults will filter the note titles available and only allow you to use Clinical Procedures titles.

When the clinical procedure results are present, Consults changes the status to PR (partial results). This means that, at least, at stub of a TIU document has been attached to the consult. It could also mean that one or more images and/or instrument reports created by a clinical device are also attached to the consult. Additionally, the interpretation of the clinical device image(s) or text may have been uploaded and is ready for signature.

The minimum required by the consults package to complete a clinical procedures consult is the interpretation of the clinical device output. If this is not supplied via upload, then it must be entered by the consulting clinician. When this interpretation is entered, the following fields are required and are prompted for (if not already present):

![](consult-request-tracking-user-manual-gmrc-3-0-206/004.png)

Selecting a button with an arrow pointing down displays a drop-down list of choices. A button with three dots brings up a calendar control to select a date and time.

## Windows Quick Start

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction 57

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Windows Flow of Information 58

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Starting Consults in Windows 58

#### Order New Consult 60

#### Print Form 62

#### Forward Request 63

#### Receive Request 64

#### Comment 66 

#### Complete a Consult (From the Consults Tab) 68

#### Complete a Consult (From the Notes Tab) 70

#### Complete a Consult (From Medicine Results) 74

### Other Windows Topics 77

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Cancel Request 77

#### Detailed Display 80

#### Discontinue Order 79

#### Make Addendum 86

#### New Date Range 89

#### Results Display 92

#### Select Consult 93

#### Select New Patient 94

#### Select Service 95

#### View by Status 96

#### ### Introduction

#### Before each process, select the consult. 

#### Most processes assume that you have already selected a Consult already. If you hover over a Consult, the full line displays.

![](consult-request-tracking-user-manual-gmrc-3-0-206/005.png)

### Windows Flow of Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Starting Consults in Windows

#### Start CPRS for Windows by locating the appropriate icon (usually in your Star folder if using VACS or a share folder, or on your desktop).

#### Log-on to your system using your PIV card or your user name and access code.

![](consult-request-tracking-user-manual-gmrc-3-0-206/006.png)

#### Select a patient. You can user the Patient List area to select a smaller list of patients, if one is defined for you. Type in part of the patient’s name or many sites user the first letter of the last name and the last 4 of the social security number. When you identify the correct patient name, double-click on it, or highlight it and select OK.

![](consult-request-tracking-user-manual-gmrc-3-0-206/007.png)

#### Select the Consults Tab:

![](consult-request-tracking-user-manual-gmrc-3-0-206/008.png)

#### Order New Consult 

#### Select New Consult by selecting Action \| New Consult or selecting the New Consult button.

![](consult-request-tracking-user-manual-gmrc-3-0-206/009.png)

#### Fill out the Order a Consult dialog:

![](consult-request-tracking-user-manual-gmrc-3-0-206/010.png)

1.  Select the Specialty or Service to which the Consult request will be sent. You can also use the button at the end of the field to see a tree view.
2.  If needed, change the Urgency, Place, Attention, and Provisional Diagnosis boxes.
3.  Select if the patient will be an inpatient or outpatient.
4.  Enter a Clinically Indicated Date.
5.  If needed, type the reason for request or add to boilerplate text.
6.  If the Provisional Diagnosis field is active, you must enter a diagnosis. If the field is yellow, you must use the Lexicon button to select the provisional diagnosis.
7.  Review the information in the box at the bottom of the dialog.
8.  When the information is complete and correct, select Accept Order.

#### Print Form 513

#### Select Print from the File Menu:

1.  Select File \| Print or follow the underlined letters from the keyboard by pressing Alt+F (together) then P.

![](consult-request-tracking-user-manual-gmrc-3-0-206/011.png)

#### Select the Printer Device:

1.  Select Chart Copy or Work Copy.
2.  If needed, start typing the device name, CPRS finds the closest match. Or use the scroll bar and then click on the printer you want.
3.  Then select OK or press the Enter key.

![](consult-request-tracking-user-manual-gmrc-3-0-206/012.png)

#### Forward Request

#### Select Forward:

1.  Select the appropriate Consult.
2.  Click on Action \| Consult Tracking \| Forward or follow the underlined character on the keyboard by pressing Alt+A (together), then C, and then F.

![](consult-request-tracking-user-manual-gmrc-3-0-206/013.png)

#### Fill in the Forward Consult dialog:

1.  Select the correct service.
2.  Type in the reason for forwarding this Consult.
3.  If necessary, change the Urgency, Attention, and date and time of the action.
4.  Enter comments or reason for forwarding as needed.
5.  When finished, select OK.

![](consult-request-tracking-user-manual-gmrc-3-0-206/014.png)

#### Receive Request

#### Select Receive:

1.  Select Action \| Consult Tracking \| Receive or use the keyboard by pressing the underlined characters: First Alt and A (together), then C, and then R.

![](consult-request-tracking-user-manual-gmrc-3-0-206/015.png)

#### Select OK.

1.  If you need some other time, change it using the Date/time of this action field.
2.  If the action should be by some other person, change the name in the Action by field.

![](consult-request-tracking-user-manual-gmrc-3-0-206/016.png)

#### Comment  

#### Select Add Comment:

1.  Select Action \| Consult Tracking \| Add Comment or use the keyboard following the underlined letters: First Alt+A (together), then C, then A.

![](consult-request-tracking-user-manual-gmrc-3-0-206/017.png)

#### Fill in the Add Comment to Consult Dialog:

1.  Type your comment in the text area.
2.  Then select the Send Alert check box.

![](consult-request-tracking-user-manual-gmrc-3-0-206/018.png)

#### Select the People to Receive the Alert:

1.  Selecting the names in the right list adds them to the Currently selected recipient list to receive the alert.
2.  If you need to remove someone from the list, select their name in the right pane.
3.  When the list has all the people that you want to receive the alert, select OK.

![](consult-request-tracking-user-manual-gmrc-3-0-206/019.png)

> **NOTE:** If this were an Inter-Facility Consult, individuals from the other facility involved would not be on this list. In this case, the Notification System decides who to notify at the other facility by referring to Consults files.

#### Select OK:

1.  When finished, select OK.

![](consult-request-tracking-user-manual-gmrc-3-0-206/020.png)

#### Complete a Consult (From the Consults Tab)

#### Select Complete/Update Results:

1.  Select Action \| Consult Results \| Complete/ Update Results or use the keyboard following the underlined letters: First Alt+A (together) then R and then C.

![](consult-request-tracking-user-manual-gmrc-3-0-206/021.png)

#### Select the Title of the Note:

1.  Start typing the Title, then press Enter when the correct Title is highlighted.
2.  If the Expected Cosigner box appears, you also need to fill in the Expected Cosigner.

![](consult-request-tracking-user-manual-gmrc-3-0-206/022.png)

#### Type in the text of the results:

As with any TIU document, part of it can be boiler-plate. And part of it may be entered by you. This can be typed directly or cut and pasted from a word.

![](consult-request-tracking-user-manual-gmrc-3-0-206/023.png)

#### Save the note:

You can save the note to finish and sign later by selecting Save Without Signature. This changes the status to Partial Results (pr).

Or you can sign it now using Sign Note Now. This changes the status to Complete (c).

![](consult-request-tracking-user-manual-gmrc-3-0-206/024.png)

#### Complete a Consults (From the Notes Tab)

Before starting, from the CPRS Windows program, select the correct patient and click the Notes tab.

#### Select New Note.

![](consult-request-tracking-user-manual-gmrc-3-0-206/025.png)

#### Select the Title of the Note:

1.  Type the beginning of the note title, locate the correct title and highlight it.
2.  When finished, select OK.

![](consult-request-tracking-user-manual-gmrc-3-0-206/026.png)

#### Select the consult to complete.

#### ![](consult-request-tracking-user-manual-gmrc-3-0-206/027.png) 4. Type in the text of the results.

As with any TIU document, part of it can be boiler-plate, and part of it may be entered by you.

![](consult-request-tracking-user-manual-gmrc-3-0-206/028.png)

#### Save the note.

You can save it to finish and sign later by using the Save Without Signature menu item. This changes the status to Partial Results (pr).

Or you can sign it now by using the Sign Note Now menu item. This changes the status to Complete (c).

![](consult-request-tracking-user-manual-gmrc-3-0-206/029.png)

#### Complete a Consult (From the Medicine Results)

#### Select Attach Medicine Results:

Procedures are indicated by the medical icon (caduceus).

If medicine results are available for this patient, the menu command Attach Medicine Results is turned on (not grayed out).

1.  To attach Medicine results, select Action \| Consults Results \| Attach Medicine Results.

> ![](consult-request-tracking-user-manual-gmrc-3-0-206/030.png)

#### Select the medicine result:

1.  Select the medicine result you want.
2.  Select OK.

![](consult-request-tracking-user-manual-gmrc-3-0-206/031.png)

#### No signature is necessary at this time. 

#### Undo Medicine Results

#### Select Remove Medicine Results

Windows activates this menu command when a result *you can* remove is present in the selected consult.

1.  Select Action \| Consult Results \| Remove Medicine Results.

![](consult-request-tracking-user-manual-gmrc-3-0-206/032.png)

#### Select the medicine result to be removed.

1.  If more medicine results are present, they will be listed in the Remove Medicine Result dialog.

![](consult-request-tracking-user-manual-gmrc-3-0-206/033.png)

Consults keeps and displays a complete audit trail as shown below.

![](consult-request-tracking-user-manual-gmrc-3-0-206/034.png)

### Other Windows Topics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Cancel (Deny) Request

> Note: This is a consult receiver’s action. If you are the consult originator, use the Discontinue Order action.

#### Select Cancel:

1.  Select Action \| Consult Tracking \| Cancel, or follow the underlined letters by typing Alt and A together (Alt+A), then C, and then C again.

![](consult-request-tracking-user-manual-gmrc-3-0-206/035.png)

#### Consult dialog:

1.  Type the reason for the denial. Be specific enough so that the originating provider can correct and resubmit the consult.
2.  When finished, select OK.

A notification is automatically sent to the consult originator so that the consult can be edited and resubmitted.

![](consult-request-tracking-user-manual-gmrc-3-0-206/036.png)

#### Discontinue Order

> Note: This is a consult originator’s action. If you are the consult receiver, use the Cancel (Deny) action.

#### Select Discontinue:

1.  Click on Action, then Consult Tracking, then Discontinue, or follow the underlined characters on the keyboard by pressing Alt+A (together), then C, and then D.

![](consult-request-tracking-user-manual-gmrc-3-0-206/037.png)

#### Fill out the Discontinue Consult dialog:

1.  Type in the reason in the Comments box.
2.  When finished, select OK.

A notification is automatically sent to the originator of the consult with information about the discontinuation of the order.

![](consult-request-tracking-user-manual-gmrc-3-0-206/038.png)

#### Detailed Display

Consults in Windows always show the detailed display of whatever consult is selected.

1.  Select the consult you want to see![](consult-request-tracking-user-manual-gmrc-3-0-206/039.png).

The consult number can be used to quickly access a specific consult in a variety of situations.

The Detailed Display includes:

- Current Primary Care information
- Current Eligibility information
- Order information
- Last action information
- A record of activity

All signed notes.

- Information about unsigned notes.
- Notes, Results, and Addenda
- All other text fields associated with the consult.

<span id="gmrc73display" class="anchor"></span>

### Changes made by Patch 73 for ICD-10 Remediation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ICD Diagnosis Code Display

ICD Diagnoses will be displayed on the user-selected Consults or Procedures.

If an existing consult (for which ICD-10 diagnosis was entered) is selected for display or the action Display Details is used, the ICD-10-CM diagnosis code and full description/definition will be displayed.

![](consult-request-tracking-user-manual-gmrc-3-0-206/040.png)

If the user selects an existing consult to display or uses the action Display Details and the Provisional Diagnosis was entered using free text data entry, the Consults package will not designate the diagnosis as ICD-9 or ICD-10.

![](consult-request-tracking-user-manual-gmrc-3-0-206/041.png)

The Consults package will display ICD Diagnosis on the display details of Consults/Procedures orders.

- If the user selects an order to display details and the Provisional Diagnosis was entered as an ICD-9 diagnosis using the Lexicon, the ICD-9 diagnosis code and description/definition will be displayed.
- If the user selects an order to display details and the Provisional Diagnosis was entered as an ICD-10 diagnosis using the Lexicon, the ICD-10-CM diagnosis code and full description/definition will be displayed.
- If the user selects an order to display and the Provisional Diagnosis was entered using free text data entry, then Consults will not designate the diagnosis as ICD-9 or ICD-10.
- If the user selects an existing consult to display and the Provisional Diagnosis was entered using the Lexicon, then Consults will designate the particular diagnosis as ICD-9 or ICD-10.

![](consult-request-tracking-user-manual-gmrc-3-0-206/042.png)

- ICD Diagnosis on the Display SF 513 action will be displayed for a particular Consults or Procedure.
  - If the user performs the action Display SF 513 for a consult or procedure for which ICD-10 diagnosis was entered, Consults will display the ICD-10-CM diagnosis code and full description/definition.
  - If the user performs the action Display SF 513 for a consult or procedure and the Provisional Diagnosis was entered using free text data entry, then Consults will not designate the diagnosis as ICD-9 or ICD-10.
  - If the user performs the action Display SF 513 for a consult or procedure and the Provisional Diagnosis was entered using the Lexicon, then Consults will designate the particular diagnosis as ICD-9 or ICD-10.

ICD Diagnosis Search

Consults will provide the ability to search on ICD-10-CM diagnosis full (expanded) text descriptions and codes.

![](consult-request-tracking-user-manual-gmrc-3-0-206/043.png)

- Consults will display ICD Diagnosis on the Display SF 513 action for a particular Consults or Procedure.
  - If the user performs the action Display SF 513 for a consult or procedure for which ICD-10 diagnosis was entered, Consults will display the ICD-10-CM diagnosis code and full description/definition.
  - If the user performs the action Display SF 513 for a consult or procedure and the Provisional Diagnosis was entered using free text data entry, Consults will not designate the diagnosis as ICD-9 or ICD-10.
  - If the user performs the action Display SF 513 for a consult or procedure and the Provisional Diagnosis was entered using the Lexicon, then Consults will designate the particular diagnosis as ICD-9 or ICD-10.

#### Make Addendum

An Addendum is a *medical* statement by a patient care professional about a specific Note. It differs from a Comment in that it is about medical matters, where Comments, which can be written by anyone, should contain information needed to *administer* the consult.

#### Select the Consult and the Note:

1.  First select the correct consult under All Consults.
2.  Then, in the box below the New Procedure box to select the note.

![](consult-request-tracking-user-manual-gmrc-3-0-206/044.png)

#### Select Make Addendum

1.  Select Action \| Consult Results \| Make Addendum, Or follow the underlined character on the keyboard by pressing Alt+A (together), then C, and then F.

![](consult-request-tracking-user-manual-gmrc-3-0-206/045.png)

#### Type the addendum.

An addendum supplies supplementary information on the patient’s condition.

As with other TIU objects, addendum may include boilerplate text.

![](consult-request-tracking-user-manual-gmrc-3-0-206/046.png)

#### Save the note:

You can save it to finish and sign later by using the Save Without Signature menu item. This changes the status to Partial Results (pr).

Or you can sign it now by using the Sign Note Now menu item. This changes the status to Complete (c).

![](consult-request-tracking-user-manual-gmrc-3-0-206/047.png)

#### New Date Range

#### Select Consults by Date Range:

1.  Select View \| Consults by Date Range, or use the keyboard to follow the underlined letters: Alt+V (together) then R.

![](consult-request-tracking-user-manual-gmrc-3-0-206/048.png)

#### Fill in the List Consults by Date Range Dialog:

1.  For the Beginning date, in the List Consults by Date Range dialog, enter the date or select the Calendar control by selecting the button with three dots.
2.  If using the calendar control, Initially, the current date is highlighted. Select the month, day, and time you want. These arrow buttons next to the date enables the user to go up or down the months.
3.  When you have the correct date and time, select OK.
4.  Select an Ending Date using the same method described above.
5.  In the List Consults by Date Range dialog, select the sort order oldest to newest or vice versa.

![](consult-request-tracking-user-manual-gmrc-3-0-206/049.png)

![](consult-request-tracking-user-manual-gmrc-3-0-206/050.png)

#### In the List Consults by Date Range dialog, select OK.

Below is an example of dates entered and the sort order in the List Consults by Date Range dialog.

![](consult-request-tracking-user-manual-gmrc-3-0-206/051.png)

After you click OK only consults within the date range are displayed. The date range is displayed above the Consults box.

![](consult-request-tracking-user-manual-gmrc-3-0-206/052.png)

#### Quit

There are two ways to Exit CPRS.

The simplest way to quit is to click on the X in the upper right-hand corner of the window.

![](consult-request-tracking-user-manual-gmrc-3-0-206/053.png)

Or you can select Exit from the File menu, or you can press the Alt and F4 keys at the same time (Alt+F4).

![](consult-request-tracking-user-manual-gmrc-3-0-206/054.png)

#### Results Display

1.  Highlight the correct Consult.
2.  Get the results for the current consult by selecting Action \| Consult Tracking \| Display Results.

The results display gives only the signed results and addendum making it easier to focus in on the information you need.

It also gives author information on unsigned and/or unreleased notes.

![](consult-request-tracking-user-manual-gmrc-3-0-206/055.png)

> **NOTE:** If this were an Inter-Facility Consult, CPRS’s Remote Data Views would retrieve the results over the VA Intranet. This may take slightly longer.

#### Select Consult

1.  Select the consult you want to view or perform an action on.
2.  If the consult has more than one note associated with it, that is indicated.

![](consult-request-tracking-user-manual-gmrc-3-0-206/056.png)

#### Select New Patient

#### Choose Select New Patient from the File Menu, or follow the underlined letter from the keyboard by pressing Alt+F (together) then N.

![](consult-request-tracking-user-manual-gmrc-3-0-206/057.png)

#### Use the Patient Selection Dialog:

1.  If a list has been created that narrows the patient list, select the radio button to change the appropriate list of patients, such as a Clinic perhaps.
2.  Under Patients, type anything here that is allowed in V*IST*A patient prompts (many frequently use the first letter of the last name and last 4 of the social security number) and a list of matches appear directly below.
3.  Select the patient by double-clicking a name or highlight the name and press OK.

![](consult-request-tracking-user-manual-gmrc-3-0-206/058.png)

#### Select Service

#### Select Consults by Service from the View Menu:

1.  Select View \| Consults by Service, or follow the underlined letters from the keyboard by pressing Alt+V (together) then S.
2.  In the List Consults by Service dialog that displays, you can expand hierarchies by clicking the plus sign, contract them by clicking the minus sign. You can also change the sort order of this list if you want to.
3.  Locate the service, highlight it, and select OK.

![](consult-request-tracking-user-manual-gmrc-3-0-206/059.png)

![](consult-request-tracking-user-manual-gmrc-3-0-206/060.png)

#### View by Status

#### Select Consults by Status from the View Menu, follow the underlined letters from the keyboard by pressing Alt+V (together) then U.

![](consult-request-tracking-user-manual-gmrc-3-0-206/061.png)

#### Select the status you want from the list:

1.  Click on the status or statuses you want to see. Hold down the Ctrl key when selecting to select more than one status.
2.  Change the sort order if needed.
3.  When finished, click the OK button, or press the Enter key.

![](consult-request-tracking-user-manual-gmrc-3-0-206/062.png)

Now the list of consults only has ones with the status you selected.

![](consult-request-tracking-user-manual-gmrc-3-0-206/063.png)

#### Custom List

Custom List enables the user to select the service or services, statuses, and the beginning and ending date rages. Users can also group the items by Consults/ Procedures, Service, or Status and set the sort order.

#### Select Custom View from the View Menu by selecting View \| Custom View

![](consult-request-tracking-user-manual-gmrc-3-0-206/064.png)

#### Select the view you want.

Do one or more of the following:

1.  Select one or more services from the tree view. Use the shift and Ctrl keys to select multiple statuses (or services).
2.  Enter a beginning date and ending date. You can either type it in or select the button to use the calendar control.
3.  If you want to group them, select the Group method: You can group by Consults/ Procedures, Service, or Status.

![](consult-request-tracking-user-manual-gmrc-3-0-206/065.png)

#### 3.Click OK.

# Package Reference

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three menus, six notifications, and 18 actions that make up the package that is Consults. In the preceding section, Package Operation, we discussed a number of these in order to explain how the Consult/Request Tracking package works. In this section, we give each of a description of each of these in turn to provide reference information for you.

## General Service User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are a Consults user from a service other than Medicine or Pharmacy services, you probably have the GMRC General Service User menu. This menu gives you access to all the basic functionality you need to track Consults for your service.

As a General Service User, you have access to three basic options as shown in this example:

Select Consult Service Tracking Option: ?

CS Consult Service Tracking

PC Service Consults Pending Resolution

ST Completion Time Statistics

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Consult Service Tracking Option:

### Consult Service Tracking Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Consult/Request Service Tracking option may be used to:

Review the latest activity related to a patient's consult/procedure request orders.

Update or track activities related to a patient's consults.

The menu of actions available to you depends on whether you are a Review Only user or an Update user. The names and the synonyms for each menu action is listed below:

#### Review Only and Update Actions

| ACTION NAME       | SYNONYM | GUI Menu Action                            |
|-------------------|---------|--------------------------------------------|
| Next Screen       | \+      |                                            |
| Previous Screen   | \-      |                                            |
| Add Comment       | CM      | Action\|Consult Tracking\|Add Comment      |
| Change Date Range | CV;DT   | View\|Consults by Date Range               |
| Detailed Display  | DD      | Action\|Consult Tracking\|Detailed Display |
| Edit/Resubmit     | ER      | Action\|Consult Tracking\|Edit Resubmit\*  |
| Redisplay Screen  | RD      |                                            |
| Select Patient    | SP      | File\|Select New Patient                   |
| Select Service    | CV;SS   | View\|Consults by Service                  |
| Print Form 513    | PF      | File\|Print                                |
| Quit              | Q       | File\|Exit                                 |
| Results Display   | RT      | Action\|Consult Tracking\|Display Results  |
| View By Status    | CV;ST   | View\|Consults by Status                   |

\* ER (Edit/Resubmit) may be used only by the originating provider or an update user. It is available on this menu in case the originating provider is not an update user.

#### Update Only Actions

| ACTION NAME          | SYNONYM | GUI Menu Command                                   |
|----------------------|---------|----------------------------------------------------|
| Complete (Update)    | CT      | Action\|Consult Results\|Complete/Update Results   |
| Cancel (Deny)        | DY      | Action\|Consult Tracking \|Deny                    |
| Discontinue          | DC      | Action\|Consult Tracking \|Discontinue             |
| Forward              | FR      | Action\|Consult Tracking \|Forward                 |
| Receive              | RC      | Action\|Consult Tracking \|Receive                 |
| Remove Med Rslt      | RM      | Action\| Consult Tracking\|Remove Medicine Results |
| Schedule             | SC      | Action\|Consult Tracking\|Schedule                 |
| Significant Findings | SF      | Action\|Consult Tracking\|Significant Findings     |
| Make Addendum        | MA      | Action\|Consult Results\|Make Addendum             |

Each review screen displayed has a prompt at the bottom of the display screen. This prompt varies according to what Consults thinks you are going to do next. Thus, it is either “Select Consult:” or “Select Action:” depending on various system variables. If the prompt is “Select Consult:” you may either select a consult or an action. If the prompt is “Select Action:” you may only select an action. In either case a ? at this prompt provides you with a menu of actions.

Before you use this option, you need to know:

- The patient's name or identification.

You may identify a patient by entering information other than the patient's name. Some possibilities are: Social Security Number (SSN), Ward Location, or Room-Bed, at the Select Patient prompt.

- The service or specialty.

The default answer at the Select Service/Specialty Tracking prompt is always ALL SERVICES//. The response you make at the prompt determines what action you are able to select. If you accept the ALL SERVICES default, the Review Only actions are the only ones available. Alternatively, a service/specialty could be specified to restrict the number of consults to review. If you are an Update user for the service/specialty you selected, then you have all actions available to you at the action prompt.

An example of the Consult/Request Service Tracking option and default Review Only actions available for use with the option are shown in the following sample dialogue. User responses are in bold.

Select Consult Service Tracking Option: ?

CS Consult Service Tracking

PC Service Consults Pending Resolution

ST Completion Time Statistics

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Consult Service Tracking Option: CS Consult/Request Service Tracking

Select Patient: CPRSPATIENT,FOUR 01-01-51 666123456 YES SC VET

ERAN

Select Service/Specialty: ALL SERVICES// \<Enter\> ALL SERVICES

List From Starting Date: ALL DATES// \<Enter\> ALL

Select the Consult/Request Service Tracking option from your menu and enter the name of the patient whose consults/requests you want to review.

At the Select Service/Specialty prompt enter the name of the Service or hierarchy of services the consult was referred to. If consults are available in the service or hierarchy for the patient specified, they are listed as shown in the following display.

CONSULT TRACKING Oct 06, 2000 08:24:24 Page: 1 of 1

CPRSPATIENT,FOUR 666-44-2222 8E/3E101-1 MAR 3,1960 (40) \<AD\>

Wt.(lb): 184

Requested St No. Consult/Procedure Request

1 10/06/00 p 1766 EYE CLINIC Cons

Enter ?? for more actions

SP Select Patient RT Results Display ER Edit/Resubmit

CV Change View ... PF Print Form 513

DD Detailed Display CM Add Comment

Select: Quit//

#### Review Only Actions

Enter ?? at the Select Item(s) prompt to see the complete list of options available to you.

Select Consult: Quit// ??

Enter the display number of the item you wish to act on, or select an action.

If you'd like another view of the consults, enter CV.

Status key:

'a' - active 'c' - complete 'dc' - discontinued

'p' - pending 'x' - cancelled 'pr' - partial results

's' - scheduled 'e' - expired

Enter ?? to see a list of actions available for navigating the list.

Press \<return\> to continue ...

The following actions are also available:

\+ Next Screen RD Redisplay Screen

\- Previous Screen UP Up a Line CWAD Display CWAD Info

FS First Screen DN Down a Line

LS Last Screen SL Search List

PS Print Screen EX Exit

GO Go to Page PT Print List

Enter RETURN to continue or '^' to exit:

If you are an update user, the menu of actions includes additional actions such as received, completed, and discontinued.

The help display also includes a key to abbreviations used in consult screens, including the Consult Tracking screen currently under discussion.

#### Update Select Actions

If you are an Update user, then the Consult Tracking display looks like this:

CONSULT TRACKING Oct 06, 2000 08:26:04 Page: 1 of 2

CPRSPATIENT,FOUR 666-44-2222 8E/3E101-1 MAR 3,1960 (40) \<AD\>

Wt.(lb): 184

Requested St No. Consult/Procedure Request

1 11/17/98 x 1211 BRONCHOSCOPY PULMONARY Proc

2 07/13/98 c 1112 \*PULMONARY Cons

3 06/18/98 c 1062 \*PULMONARY Cons

4 06/12/98 c 1050 PULMONARY Cons

5 06/08/98 c 1028 PULMONARY Cons

6 06/04/98 dc 1022 PULMONARY Cons

7 05/27/98 dc 940 PULMONARY Cons

8 05/20/98 dc 919 PULMONARY Cons

9 05/13/98 c 898 \*PULMONARY Cons

10 05/01/98 c 881 PULMONARY Cons

11 04/15/98 c 843 PULMONARY Cons

12 03/16/98 c 827 PULMONARY Cons

\+ Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit Select: Next Screen//

Each action is described in detail in the Actions section of Package Reference starting on page 112.

### Completion Time Statistics 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report is intended to help hospitals track overall quality of service. High numbers on this report can indicate the presence of bottlenecks in the organization that might need management attention.

In the following example, a report on completion times is printed for Pulmonary Service:

Select Consult Service Tracking Option: ?

CS Consult Service Tracking

PC Service Consults Pending Resolution

ST Completion Time Statistics

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Consult Service Tracking Option: ST Completion Time Statistics

Select Service/Specialty: ALL SERVICES// PULMONARY

List From Starting Date: ALL DATES//

...HMMM, LET ME THINK ABOUT THAT A MOMENT...........

DAYS TO COMPLETE CONSULT STATSOct 06, 2000 08:28:22 Page: 1 of 1

Number Of Days To Complete A Consult For Services Statistics.

FROM: ALL TO: OCT 6,2000

Consult/Request Completion Time Statistics

FROM: ALL TO: OCT 6,2000

SERVICE: PULMONARY

Total Number Of Consults Completed: 200

Mean Days To Complete: 46.8 Standard Deviation: 104.7

Total INPATIENT Consults: 32

Mean Days To Complete: 60.7 Standard Deviation: 125.1

Total OUTPATIENT Consults: 30

Mean Days To Complete: 93.4 Standard Deviation: 155.5

Total Unclassified Consults: 138

Mean Days To Complete: 33.4 Standard Deviation: 81.0

Enter ?? for more actions

SS Select Service PR Print Completion Statistics To A Printer.

Select Item(s): Quit//

### Service Consults Pending Resolution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of the Service Consults Pending Resolution option is to list the pending and active consults. Use it to stay informed about the overall status of consults for your service.

In the following example, the option is used to view pending and active Pulmonary consults:

Select Consult Service Tracking Option: ?

CS Consult Service Tracking

PC Service Consults Pending Resolution

ST Completion Time Statistics

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Consult Service Tracking Option: PC Service Consults Pending Resolution

Select Service/Specialty: PULMONARY

List From Starting Date: ALL DATES// \<Enter\>

...EXCUSE ME, LET ME THINK ABOUT THAT A MOMENT...

Service Consults by Status Oct 06, 2000 08:31:39 Page: 1 of 5

To Service: PULMONARY

From: ALL To: OCT 6,2000

Status Last Action Request Date Patient Name Pt Location

Consult/Request By Status

FROM: ALL TO: OCT 6,2000

SERVICE: PULMONARY

Pending CPRS RELEASED ORDER 09/20/00 CPRSATIENT,FOU (6572) 2B MED

Pending CPRS RELEASED ORDER 09/19/00 CPRSATIENT,ONE (5678) 2B MED

Pending CPRS RELEASED ORDER 09/19/00 CPRSATIENT,FIV (1111) 2B MED

Pending CPRS RELEASED ORDER 07/20/00 CPRSATIENT,TWO (3241) 2B MED

Pending PRINTED TO 06/29/99 CPRSATIENT,SIX (8829) GENERAL MEDICINE

Pending PRINTED TO 06/28/99 CPRSATIENT,FOU (3779) 1A

Pending PRINTED TO 06/15/99 CPRSATIENT,SEV (8828) 13A PSYCH

Pending PRINTED TO 06/08/99 CPRSATIENT,FIF (4111) 1A

Pending PRINTED TO 06/03/99 CPRSATIENT,EIG (2345) ONCOLOGY

Pending PRINTED TO 06/03/99 CPRSATIENT,SIX (9235) 1A

Pending PRINTED TO 06/03/99 CPRSATIENT,NIN (3242) ONCOLOGY

Pending PRINTED TO 06/03/99 CPRSATIENT,TEN (5525) ONCOLOGY

\+ Enter ?? for more actions \>\>\>

Service Status Number on/off Print List

Select Item(s): Next Screen//

> **NOTE:** Someone in your clinic or service should review this list daily to make sure that all consults are being attended to.

## Consult Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table gives the statuses that Consults uses, along with their abbreviation, name, and description:

| Abbreviation | Name            | Description                                                                              |
|--------------|-----------------|------------------------------------------------------------------------------------------|
| a            | ACTIVE          | Orders that are active or have been accepted by the service for processing.              |
| c            | COMPLETE        | Orders that require no further action by the ancillary service.                          |
| dc           | DISCONTINUE     | Orders that have been stopped prior to expiration or completion.                         |
| p            | PENDING         | Orders that have been placed but not yet accepted by the service filling the order.      |
| pr           | PARTIAL RESULTS | All or part of a consult completion report has been entered but has not yet been signed. |
| s            | SCHEDULED       | The receiving clinic has scheduled an appointment for the patient.                       |
| x            | CANCELLED       | Orders that have been rejected by the ancillary service without being acted on.          |

The following table gives the actions that Consults uses along with the status after the action is performed:

| Consult Actions     | Status after Action |
|---------------------|---------------------|
| CPRS Released Order | PENDING             |
| Discontinued        | DISCONTINUED        |
| Incomplete Report   | PARTIAL RESULTS     |
| Completed           | COMPLETE            |
| Edited/Resubmit     | PENDING             |
| Schedule            | SCHEDULED           |
| Forwarded           | PENDING             |
| Canceled            | CANCELLED           |
| Added Comment       | No change in status |
| Received            | ACTIVE              |
| Printed             | No change in status |

This table shows actions that are tracked in Consults V. 3.0. Actions that are new with 3.0 are indicated as well as which Consults menu (update or review) initiates the action. If an order status change can result from the action, the new status is shown.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 17%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><p>TRACKED</p>
<p>ACTION TYPE</p></th>
<th><p>New</p>
<p>V.3.0</p></th>
<th><p>Update</p>
<p>Actions</p></th>
<th><p>Review</p>
<p>Actions</p></th>
<th>RELATED OE/RR STATUS</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Added Comment</td>
<td></td>
<td>X</td>
<td>X</td>
<td></td>
<td>Review users can add a comment.</td>
</tr>
<tr class="even">
<td>Addendum Added To</td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
<td>Based on adding a signed and released addendum to a completed note via the Complete/Update or Make Addendum action or through TIU actions.</td>
</tr>
<tr class="odd">
<td>Cancelled</td>
<td>X</td>
<td>X</td>
<td></td>
<td>CANCELLED</td>
<td>This is used in 3.0 replacing the 2.5 Deny action.</td>
</tr>
<tr class="even">
<td><p>Complete/</p>
<p>Update</p></td>
<td></td>
<td>X</td>
<td></td>
<td>COMPLETE or PARTIAL RESULTS</td>
<td>Changed title to imply Complete can be chosen multiple times by clinicians entering results. TIU actions can also cause this tracking action. Includes the one-time Administrative Complete.</td>
</tr>
<tr class="odd">
<td>Disassociate Result</td>
<td>X</td>
<td></td>
<td></td>
<td></td>
<td>Currently done through TIU actions. In the future will be used to remove an incorrectly associated note.</td>
</tr>
<tr class="even">
<td>Discontinued</td>
<td></td>
<td>X</td>
<td></td>
<td>DISCONTINUED</td>
<td>No longer includes Denied.</td>
</tr>
<tr class="odd">
<td>Edit Before Release</td>
<td>Obso-lete</td>
<td></td>
<td></td>
<td>UNRELEASED</td>
<td>Moved unreleased consults to Order Entry in CPRS conversion.</td>
</tr>
<tr class="even">
<td>Edit/Resubmitted</td>
<td>X</td>
<td></td>
<td></td>
<td>PENDING</td>
<td>The originating provider can edit and resubmit a consult from either an alert or the Consult Tracking screen. An update user may also use this action.</td>
</tr>
<tr class="odd">
<td>CPRS Released Order</td>
<td></td>
<td></td>
<td></td>
<td>PENDING</td>
<td>Used in 3.0 to represent a signed/released Consult order from CPRS.</td>
</tr>
<tr class="even">
<td>Forwarded From</td>
<td></td>
<td>X</td>
<td></td>
<td>PENDING</td>
<td></td>
</tr>
<tr class="odd">
<td>Incomplete RPT</td>
<td></td>
<td></td>
<td></td>
<td>PARTIAL RESULTS</td>
<td>Status name has changed from Incomplete RPT. Based on Complete/Update action, and/or TIU actions, if the first consult note is not completed.</td>
</tr>
<tr class="even">
<td>New Note Added</td>
<td>X</td>
<td></td>
<td></td>
<td>PARTIAL RESULTS/ COMPLETE</td>
<td>Based on Complete/Update action and/or TIU actions.</td>
</tr>
</tbody>
</table>

Consult Action/Status Overview (Continued)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 17%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><p>TRACKED</p>
<p>ACTION TYPE</p></th>
<th><p>New</p>
<p>V.3.0</p></th>
<th><p>Update</p>
<p>Actions</p></th>
<th><p>Review</p>
<p>Actions</p></th>
<th>RELATED OE/RR STATUS</th>
<th>Comment</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Printed to</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>Based on the original order being signed and released, forwarded, and edit/resubmitted. The SF 513 printed at the Service is accomplished with the Consult package hard-coded format. (OE/RR print templates cannot include results.)</td>
</tr>
<tr class="even">
<td>Received</td>
<td></td>
<td></td>
<td></td>
<td>ACTIVE</td>
<td></td>
</tr>
<tr class="odd">
<td>Schedule</td>
<td>X</td>
<td>X</td>
<td></td>
<td>ACTIVE</td>
<td>The Schedule action does not actually schedule an appointment or link to the scheduling package. It does allow a convenient way to annotate a consult after an appointment has been scheduled by some other means.</td>
</tr>
<tr class="even">
<td>Service Entered</td>
<td></td>
<td></td>
<td></td>
<td>ACTIVE</td>
<td>Currently unavailable.</td>
</tr>
<tr class="odd">
<td>Sig Finding Update</td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
<td>May be used independently from Administrative Complete action from 2.5.</td>
</tr>
<tr class="even">
<td>Status Change</td>
<td>X</td>
<td></td>
<td></td>
<td>ACTIVE</td>
<td>Used by TIU when a note is disassociated from a consult and there are no other results associated with the it.</td>
</tr>
<tr class="odd">
<td>Unknown Action</td>
<td>X</td>
<td></td>
<td></td>
<td>NO STATUS</td>
<td>Used in displays if action is unknown.</td>
</tr>
</tbody>
</table>

## Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Brief Action Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Review Only Actions

DD The *Detailed Order Display* action displays specific order activities and details, audit/tracking trails and results.

CT The *New Date Range* allows you to change date range while in the Consult Tracking screen. This date range change does not change the patient or require you to select a new patient. It is a subordinate action to Change View (CV).

CV The *Change View* action gives you the capability to view consults by Service, Status, or Date Range. This is done by adding the modifying action to CV as such: CV;SS for Select Service. CV;ST for View by Status. CV;DT for New Date Range.

PF The Print Form action produces a copy of SF 513.

RT The *Results Display* action displays the results of the consult or procedure request order.

SP The *Select New Patient* action allows you to select a new patient’s name at any time, while using this option, rather than having to log out of the option and log back in.

SS The *Select Service* action allows you to select a different service/specialty in which to review orders. It is a subordinate action to Change View (CV).

ST The View by Status action allows you to select one or more statuses to display on the screen. It is a subordinate action to Change View (CV).

CM This action synonym may be entered at the Select prompt if the Service/Specialty wishes to add a *Comment* to an existing consult order. An example is a comment indicating that the requesting clinician wants a HOLD put on an order that has already been Received and is active in a Service/Specialty.

ER Although the *Edit/Resubmit* action shows up on the Review Only menu, it can only be executed by the originating provider or an update user. When a consult is cancelled or denied for clerical reasons (such as insufficient data), then the information on the consult can be edited and resubmitted it with this action. Alternatively, the originating provider may perform this function from the alert.

Q The *Quit* action exits all Consults options.

#### Update Actions

CT The *Complete Request* action updates the CPRS status of a consult from Active to Completed. When the patient’s consult review screen is displayed again, both the consult’s current status and the Last Activity field will be updated to indicate that the consult’s new current status is Completed.

Complete Request also links you to TIU so that you can enter findings.

CX The *Cancel (or Deny) Request *action may be used by Service personnel to deny a request for completion of a consult/procedure received by their Service. A comment concerning the reason for denial must added when using this action.

DC The *Discontinue Order* action allows Service/Specialty personnel to change an order’s current status and Last Activity field to Discontinued. In addition, a comment may be added concerning the reason for discontinuance.

FR Entering the *Forward Request* allows you to forward a consult or request to any other Service/Specialty, provided that Service/ Specialty has been set up by IRM personnel to receive consults on line. As an example, this action could be used when Cardiology Service has mistakenly received a consult that should have been sent to Hematology Service.

MA The *Make Addendum* action allows one or more people to add their comments to the results of a consult. Contrast this to Add Comment, which adds a note to the consult.

RC The *Received Request* action is used by a Service/Specialty to acknowledge receipt of a new consult/request in the Service and to update the current CPRS status of the consult/request to Active rather than Pending. The Last Activity field on the patient’s review screen will also be updated to indicate that the consult was Received.

RM The *Remove Medicine Results* action is used when a medicine result has been attached to a consult in error. Its use is restricted, but generally speaking, it can be done by anyone who can attach medicine results.

SC The *Schedule* action can be used by a Service/Specialty to annotate a consult that an appointment has been scheduled for the patient. (It does not schedule an appointment or link to the Scheduling Package.)

SF The *Significant Findings* action is used by a Service/ Specialty to mark a consult has having significant findings. When the Sig Findings flag is set to “Y” an asterisk is placed next to the consult in the review display.

> **NOTE:** Actions that require you to select an existing order can be done in one of two ways:

Select the action.

Select the order.

Or

Select the order.

Select the action.

The actions that are affected by this are:

DD Detailed Order Display

CM Comment Order

CT Complete Request

DC Discontinue Order

CY Deny Request

FR Forward Request

RC Received Request

SC Schedule

ER Edit/Resubmit

### Add Comment (CM) Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Add Comment action allows you to append a comment to a consult order when important information about the consult needs to be added to the original order or when a caregiver needs to furnish information before the consult is ready to be closed out.

The Add Comment action can be performed by any user.

To use the Comment Order action from Windows:

- From the Consults tab, highlight the consult you want to add a comment to.
- Select Action\|Consult Request\|Add Comment.

![](consult-request-tracking-user-manual-gmrc-3-0-206/066.png)

> **NOTE:** If this were an Inter-Facility Consult, individuals from the other facility involved would not be on this list. In this case, the Notification System decides who to notify at the other facility by referring to Consults files.

### Cancel (or Deny) Consult

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Cancel action is one of several options the receiving clinic or service uses to process a request (see Forward the Consult under Work Flow page 23).

The originating clinician is automatically sent an alert that the request has been canceled.

This action is provided for all update options in the Consults package.

Example:

Select Consult Management Option: CS Consult Service Tracking

Select Patient: CPRSPATIENT,FOUR 01-01-51 666123456 YES SC VET

ERAN

Select Service/Specialty: ALL SERVICES// PULMONARY

List From Starting Date: ALL DATES // \<Enter\> ALL DATES

CONSULT TRACKING Jun 19, 1997 04:21:18 Page: 1 of 1

CPRSPATIENT,FOUR 666-43-8796 2B M DEC 4,1949 (50) \<CAD\>

Wt.(lb): 184

Requested St No. Consult/Procedure Request

1 02/03/97 a 999 PULMONARY Consult

2 02/03/97 a 989 PULMONARY Consult

3 02/03/97 c 929 \*PULMONARY Consult

4 02/03/97 c 873 \*PULMONARY Consult

5 01/09/97 c 872 PULMONARY UGI

6 09/06/96 dc 500 PULMONARY ECHO

7 03/05/92 dc 444 PULMONARY Electrocardiogram

Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Select: Quit// CX Cancel (Deny)

CHOOSE No. 1-2: 2

Responsible Clinician: CPRSPROVIDER,TWO CRS PHYSICIAN

Date/Time of Actual Activity: NOW// \<Enter\> (JUN 19, 1997@04:21)

Enter COMMENT:

1\>Duplicate Consult

2\> \<Enter\>

EDIT Option: \<Enter\>

(Continued on next page.)

CONSULT TRACKING Jun 19, 1997 04:22:02 Page: 1 of 1

CPRSPATIENT,FOUR 666-43-8796 2B M DEC 4,1949 (50) \<CAD\>

Wt.(lb): 184

Requested St No. Consult/Procedure Request

1 02/03/97 x 999 PULMONARY Consult

2 02/03/97 a 989 PULMONARY Consult

3 02/03/97 c 929 \*PULMONARY Consult

4 02/03/97 c 873 \*PULMONARY Consult

5 01/09/97 c 872 PULMONARY UGI

6 09/06/96 dc 500 PULMONARY ECHO

7 03/05/92 dc 444 PULMONARY Electrocardiogram

Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Select: Quit//

The originating clinician then has the option of editing and resubmitting the request. This is done either from the view alerts function, or from the consult tracking screen with the Edit/Resubmit (ER) action. An update user for the subject service may also edit and resubmit a canceled consult.  

### Change View (CV) Action 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Change View action is really three different actions packaged into one. They are:

- View by Status (ST)
- Change Date Range (DT)
- Select Service (SS)

Enter the CV action followed by one of these three options. You can do this as two different entries, or you can put both commands on the same line separated by a semicolon, like this: CV;DT

In the following example we use the CV action to display selected statues:

With this action you can selectively display consults on the Consult Tracking screen base on the consult’s status. In the following example, the display is changed to view only consults with a status of Pending or Discontinued. For a list of consult statuses and their meanings, see page 108.

CONSULT TRACKING Jul 30, 1997 09:21:02 Page: 1 of 2

CPRSPATIENT,FOUR 666-43-8796 2B M DEC 4,1949 (50) \<CAD\>

Wt.(lb): 184

Requested St No. Consult/Procedure Request

1 10/06/00 p 1766 EYE CLINIC Cons

2 09/21/00 p 1764 Electrocardiogram CARDIOLOGY Proc

3 04/25/00 s 1713 CARDIOLOGY Cons

4 03/21/00 c 1701 CARDIOLOGY (SOUTH) Cons

5 02/22/00 pr 1687 PULMONARY (SOUTH) Cons

6 01/26/00 c 1665 CARDIOLOGY Cons

7 06/02/99 c 1483 VENTRICAL LEAD IMPLANT CARDIOLOGY Proc

8 04/29/99 a 1455 CARDIOLOGY (oex) CARDIOLOGY Cons

9 02/18/99 x 1395 CARDIOLOGY Cons

10 01/06/99 c 1322 M'S SPECIALTY SEA-M'S SPECIALTY Cons

11 01/05/99 c 1310 \*GASTROENTEROLOGY CARDIOLOGY Cons

12 01/04/99 c 1287 CARDIOLOGY Cons

\+ Enter ?? for more actions

SP Select Patient RT Results Display ER Edit/Resubmit

CV Change View ... PF Print Form 513

DD Detailed Display CM Add Comment

Select Consult: Next Screen// CV Change View ...

DT Date Range

ST Status

SS Service

Only Display Consults With Status of: All Status's// p Pending

Another Status to display: s Scheduled

Another Status to display: a Active

Another Status to display: \<Enter\>

(Continued on the next page.)

CONSULT TRACKING Jul 30, 1997 09:21:10 Page: 1 of 1

CPRSPATIENT,FOUR 666-43-8796 2B M DEC 4,1949 (50) \<CAD\>

Wt.(lb): 184

Requested St No. Consult/Procedure Request

1 10/06/00 p 1766 EYE CLINIC Cons

2 09/21/00 p 1764 Electrocardiogram CARDIOLOGY Proc

3 04/25/00 s 1713 CARDIOLOGY Cons

8 04/29/99 a 1455 CARDIOLOGY (oex) CARDIOLOGY Cons

Enter ?? for more actions

SP Select Patient RT Results Display ER Edit/Resubmit

CV Change View ... PF Print Form 513

DD Detailed Display CM Add Comment

Select Consult: Quit//

### Complete Request (CT) Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Complete Request action which updates a consult order’s CPRS status to completed (c).

Using the CT action informs the system that you are completely finished with a consult or procedure. An alert is sent to the originating provider and marks the record of the consult as complete.

Finally, the Complete action links you to TIU so that you can enter results. See page 26 for an example of this feature.

If a user is set up as either an Administrative User or on an Administrative User Team, the option exists to perform an Administrative Complete. In the GUI (Windows) interface, this is a separate command under Action \| Consult Tracking. In List Manager, if the user has Administrative privileges, then the program asks if an Administrative Complete should be performed. (An Administrative complete does not have results attached to it.)

### Deny Request (DY) Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Deny Request action has been subsumed by the Cancel action. See Cancel (CX) Action on page 116.

### Detailed Order Display (DD) Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Detailed Order Display action provides a list of all consult information contained in the computer file.

Example:

Select Consult Management Option: CS Consult Service Tracking

Select Patient: CPRSPATIENT,FOUR CPRSPATIENT,FOUR 12-04-49 666438796 SC VETERAN

Select Service/Specialty: ALL SERVICES// PULMONARY

List From Starting Date: ALL DATES // \<Enter\> ALL DATES

CONSULT TRACKING Nov 01, 1997 13:55:32 Page: 1 of 1

CPRSPATIENT,FOUR 666-43-8796 2B M DEC 4,1949 (50) \<CAD\>

Wt.(lb): 184

Requested St No. Consult/Procedure Request

1 11/01/97 c 675 PULMONARY Consult

2 10/06/00 p 566 EYE CLINIC Cons

3 09/21/00 p 464 Electrocardiogram CARDIOLOGY Proc

Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Select:Quit// DD Detail Display

Select Consult Number: 1

You can do just the opposite of the example above, i.e., you can select a consult first then type the action DD. The result is the same.

(Continued on next page.)

CONSULTS DETAILED DISPLAY Nov 01, 1997 13:55:42 Page: 1 of 5

CONSULT DETAILED DISPLAY Consult No.: 675

CPRSPATIENT,TWO 666-67-1996 DOB: MAR 5,1949 (48) Wt. (lb): No Entry

Current Inpatient/Outpatient: Inpatient

Ward: 2B

Eligibility: SC VETERAN

To Service: PULMONARY

From Service: MEDICINE

Reason For Request: Pt experiences shortness of breath when out of

bed.

Status: COMPLETE

ATTENTION: CPRSPROVIDER,TWO

Place: Bedside

Urgency: Routine

Request Activity Date/Time Ordering Clinician Entered By

11/01/97 10:13 CPRSPROVIDER,ONE CPRSPROVIDER,ONE

RECEIVED 11/01/97 10:15 CPRSPROVIDER,ONE CPRSPROVIDER,ONE

\+ Enter ?? for more actions

Select Action:Next Screen// \<Enter\>

CONSULTS DETAILED DISPLAY Nov 01, 1997 14:00:20 Page: 2 of 5

CONSULT DETAILED DISPLAY Consult No.: 675

CPRSPATIENT,TWO 666-67-1996 DOB: MAR 5,1949 (48) Wt. (lb): No Entry

\+

COMPLETED 11/01/97 10:17 CPRSPROVIDER,ONE CPRSPROVIDER,ONE

----------------------------- TIU CONSULT REPORT -------------------------------

Source Information

Reference Date: NOV 01, 1997@10:15:35 Author: CPRSPROVIDER,ONE

Entry Date: NOV 01, 1997@10:15:35 Entered By: CA

Expected Signer: CPRSPROVIDER,ONE Expected Cosigner: None

Urgency: None Document Status: COMPLETED

Line Count: 21 TIU Document \#: 2330

Subject: None

Associated Problems No linked problems.

Edit Information

Edit Date: NOV 01, 1997@10:17:23 Edited By: CPRSPROVIDER,ONE

\+ Enter ?? for more actions

Select Action:Next Screen// \<Enter\>

(Continued on next page.)

CONSULTS DETAILED DISPLAY Nov 01, 1997 14:02:13 Page: 3 of 5

CONSULT DETAILED DISPLAY Consult No.: 675

CPRSPATIENT,TWO 666-67-1996 DOB: MAR 5,1949 (48) Wt. (lb): No Entry

\+

Reassignment History Document Never Reassigned.

Signature Information

Signed Date: NOV 01, 1997@10:17:35 Signed By: CPRSPROVIDER,ONE

Signature Mode: ELECTRONIC

Cosigned Date: None Cosigned By: None

Cosignature Mode: None

Document Body

At the time I went to examine the pt, he was acutely broncho-

spastic and in moderately severe respiratory distress. I had him

deliver a puff of albuterol with an Aerochamber; his technique was

poor. I then instructed him and delivered an additional four puffs,

which he did with good technique. He was improved and with a clear

lung exam within a few seconds (though wheezes were still present

\+ Enter ?? for more actions

Select Action:Next Screen// \<Enter\>

CONSULTS DETAILED DISPLAY Nov 01, 1997 14:03:47 Page: 4 of 5

CONSULT DETAILED DISPLAY Consult No.: 675

CPRSPATIENT,TWO 666-67-1996 DOB: MAR 5,1949 (48) Wt. (lb): No Entry

\+

on forced expiration).

The pt regimen is lacking in inhaled corticosteroids. Recognizing

that asthma is an inflammatory process, inhaled steroids are important

in controlling the inflammatory response. My practice for severely

out-of-control asthmatics is to use high-dose inhaled steroids,

typically vanceril, 16 puffs qid, with a spacing device such as the

Aerochamber. I would institute such a regimen while he is here.

The pt has an in-house pet dog and an outside pet cat. I have

told him that the cat should go, even if it is outdoors. Cat saliva

contains a glycoprotein that leaves residue on their coats and flakes

into the air; it is problematic for many asthmatics.

The purulent phlegm asthmatics have during exacerbations is usually

\+ Enter ?? for more actions

Select Action:Next Screen// \<Enter\>

(Continued on the next page.)

CONSULTS DETAILED DISPLAY Nov 01, 1997 14:07:36 Page: 5 of 5

CONSULT DETAILED DISPLAY Consult No.: 675

CPRSPATIENT,TWO 666-67-1996 DOB: MAR 5,1949 (48) Wt. (lb): No Entry

\+

due to the eosinophils, not from infection. Antibiotics are usually

not necessary.

If you like, you may refer Mr. Bud to my clinic after discharge.

==================================== END =====================================

Enter ?? for more actions

Select Action:Quit//

### Discontinue Order (DC) Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Discontinue Order (DC) action is used by clinical personnel to stop a consult/procedure request after it has been signed. This differs from the cancel action in that there is not Edit/Resubmit action available on a discontinued order.

In the example below, the Discontinue Order action is used to cancel a duplicate order:

Select OPTION NAME: GMRC MGR Consult Management menu

Select Consult Management Option: cs Consult Service Tracking

Select Patient: CPRSPATIENT,FOUR CPRSPATIENT,FOUR 12-04-49 666438796 SC VETERAN

Select Service/Specialty: ALL SERVICES// PULMONARY

List From Starting Date: ALL DATES // \<Enter\> ALL DATES

CONSULT TRACKING Jun 19, 1997 09:31:19 Page: 1 of 1

CPRSPATIENT,FOUR 666-43-8796 2B M DEC 4,1949 (50) \<CAD\>

Wt.(lb): 184

Requested St No. Consult/Procedure Request

1 10/06/00 p 1766 EYE CLINIC Cons

2 09/21/00 p 1764 Electrocardiogram CARDIOLOGY Proc

3 04/25/00 c 1713 CARDIOLOGY Cons

4 03/21/00 c 1701 CARDIOLOGY (SOUTH) Cons

5 02/22/00 pr 1687 PULMONARY (SOUTH) Cons

6 01/26/00 c 1665 CARDIOLOGY Cons

7 06/02/99 c 1483 VENTRICAL LEAD IMPLANT CARDIOLOGY Proc

8 04/29/99 c 1455 CARDIOLOGY (oex) CARDIOLOGY Cons

9 02/18/99 x 1395 CARDIOLOGY Cons

10 01/06/99 c 1322 MARCIA'S SPECIALTY SEA-MARCIA'S SPECIALTY Cons

11 01/05/99 c 1310 \*GASTROENTEROLOGY CARDIOLOGY Cons

12 01/04/99 c 1287 CARDIOLOGY Cons

Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Select Consult: Quit// DC Discontinue

CHOOSE No. 1-7: 3

Responsible Clinician: CPRSPROVIDER,TWO CRS PHYSICIAN

Date/Time of Actual Activity: NOW// \<Enter\> (JUN 19, 1997@09:31)

Enter COMMENT:

1\>Duplicate

2\> \<Enter\>

EDIT Option: \<Enter\>

(Continued on next page.)

CONSULT TRACKING Jun 19, 1997 09:31:58 Page: 1 of 1

CPRSPATIENT,FOUR 666-43-8796 2B M DEC 4,1949 (50) \<CAD\>

Wt.(lb): 184

Requested St No. Consult/Procedure Request

1 10/06/00 p 1766 EYE CLINIC Cons

2 09/21/00 p 1764 Electrocardiogram CARDIOLOGY Proc

3 04/25/00 dc 1713 CARDIOLOGY Cons

4 03/21/00 c 1701 CARDIOLOGY (SOUTH) Cons

5 02/22/00 pr 1687 PULMONARY (SOUTH) Cons

6 01/26/00 c 1665 CARDIOLOGY Cons

7 06/02/99 c 1483 VENTRICAL LEAD IMPLANT CARDIOLOGY Proc

8 04/29/99 c 1455 CARDIOLOGY (oex) CARDIOLOGY Cons

9 02/18/99 x 1395 CARDIOLOGY Cons

10 01/06/99 c 1322 MARCIA'S SPECIALTY SEA-MARCIA'S SPECIALTY Cons

11 01/05/99 c 1310 \*GASTROENTEROLOGY CARDIOLOGY Cons

12 01/04/99 c 1287 CARDIOLOGY Cons

Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Select Consult: Quit//

### Edit/Resubmit (ER) Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the case where a consult is cancelled (or denied) for clerical reasons (e.g., test results that indicate that the consult is needed), then the original submitter or an update user for the relevant service has a chance to edit the consult to include the missing information and resubmit it. This may be done from either the alert screen, or from the consult tracking screen. In either case, the procedure is the same. See Consult/Request Cancel/Hold on page 150 for an example.

### Forward Request (FR) Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Entering the Forward Request allows you to forward a consult or request to any other Service/Specialty, provided that Service/Specialty has been set up by IRM personnel to receive consults online. Thus, the decision by the referring clinician regarding who should receive the consult can be modified by the receiving Service/Specialty. This action is available from both the CPRS screen and the Consult/Request Alerts screen.

If a request needs to be forwarded to a clinic that is not a sub-service of your clinic, the FR (Forward Request) action should be used. This action is discussed in the Forward the Consult section under Work Flow on page 23.

### Make Addendum (MA) Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Make Addendum action allows one or more people to add their comments to the results of a consult. Contrast this to Add Comment, which adds a note to the consult before it is resulted.

There is an example of Make Addendum in the Windows section on page 86.

### Print Form (PF) Action 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the Print Form Action, you can print either a chart or working copy of the consult form. To use this action from the Windows interface, follow these steps:

From the Consults tab, select the consult you want to print.

- Select File \| Print Form.
- Select the printer you want the form to come out on.
- Choose Chart Copy or Work Copy.
- Choose OK.

For an example of the Print Form option as used from the List Manager interface, see page 29.

![](consult-request-tracking-user-manual-gmrc-3-0-206/067.png)

### Print Screen Contents (PS) Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints the information that is on the screen. The output is not exactly a screen image, as it does not include the prompt area at the bottom of the screen. To print the entire contents of a consult request, use the Print Form (PF) action.

Example:

CONSULTS DETAILED DISPLAY Jun 20, 1997 10:40:56 Page: 1 of 2

CONSULT DETAILED DISPLAY Consult No.: 208

CPRSPATIENT,FOUR 666-43-8796 2B M DEC 4,1949 (50) \<CAD\>

Current Inpatient/Outpatient: Inpatient

Ward: 1A

Eligibility: SC VETERAN

To Service: PULMONARY

From Service:

Provisional Diagnosis: Broken interface with CPRS.

Reason For Request: Checking action of DY (denying) a consult as to

DC (discontinuing) a consult.

Status: DISCONTINUED

Urgency: SWITCH BED

Request Activity Date/Time Ordering Clinician Entered By

ENTERED IN OE/RR 03/05/97 16:09 CPRSPROVIDER,TWO CPRSPROVIDER,TWO

//

Forwarded From MEDICINE

\+ Enter ?? for more actions

Select Action:Next Screen// ps PS

DEVICE: HOME// laser PRINTER ROOM LN11 12 PITCH

DO YOU WANT YOUR OUTPUT QUEUED? NO// (NO)

### Quit (Q) Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the Quit (Q) action at the last Select prompt to quit using your Consults option.

Users may enter Q to Quit or ^ to Exit the option at any time.

### Receive Request (RC) Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Performing the Receive action on a consult changes its status from Pending to Active. This puts your clinic on record as accepting responsibility for completing the consult.

On page 25 we give an example of receiving a consult from a consult tracking screen. This is an example of receiving a consult from a notification alert:

You have PENDING ALERTS

Enter "VA VIEW ALERTS to review alerts

Select OE/RR Manager Menu Option: VA View Alerts

1\. CPRSPATIENT,FOUR (C8796): New Consult/Request ()

2\. CPRSPATIENT,TWO (C9600): New Consult/Request (Today)

4\. CPRSPATIENT,ONE (C3456): Consult/Request DENIED Consult

Select from 1 to 6

or enter ?, A I, F, P, M, R, or ^ to exit: 1

Consult/Request Alerts Feb 13, 1998 13:34:56 Page: 1 of 1

CPRSPATIENT,FOUR 666-43-8796 2B M DEC 4,1949 (50) \<CAD\>

Wt.(lb): 184

Number Date Stat Service Procedure

187 02/14/97 p NEUROLOGY Consult

Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Select: Quit// RC Receive Request

Who received it?: CPRSPROVIDER,ONE OC

Date/Time Actually Received: NOW// (FEB 13, 1998@13:36)

(Continued on the next page.)

Consult/Request Alerts Feb 13, 1998 13:36:52 Page: 1 of 1

CPRSPATIENT,FOUR 666-43-8796 2B M DEC 4,1949 (50) \<CAD\>

Wt.(lb): 184

Number Date Stat Service Procedure

187 02/14/97 a NEUROLOGY Consult

Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Select: Quit//

### Remove Medicine Results (RM) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action is used when a medicine result has been attached to a consult in error. Its use is restricted, but generally speaking, it can be done by anyone who can attach medicine results.

Attaching medicine results is done in conjunction with the Complete (CT) action in List Manager. See the section on medicine resulting on page 52 for details. In Windows, attaching and detaching medicine results are accomplished thru their own menu commands that are activated whenever medicine results are available. Fore an example of medicine results in Windows, refer to the Windows Quick Start section on page 74.

In this example, we use List Manager to remove an incorrect medicine results:

CONSULT TRACKING Mar 02, 2001@13:53:35 Page: 1 of 1

CPRSPATIENT,FOUR 666-43-8796 2B M DEC 4,1949 (50) \<CAD\>

Wt.(lb): 184

Requested St No. Consult/Procedure Request

1 03/02/01 p 599 ELECTROCARDIOGRAM CARDIOLOGY Proc

2 02/21/01 c 597 ELECTROCARDIOGRAM CARDIOLOGY Proc

3 10/10/96 a 242 ELECTROCARDIOGRAM CARDIOLOGY Proc

4 09/08/95 c 187 CARDIOLOGY CLINIC Cons

5 08/14/95 pr 183 12 LEAD STAT EKG CARDIOLOGY Proc

6 08/14/95 c 184 12 LEAD STAT EKG CARDIAC TRANSPLANT Proc

7 04/29/94 pr 53 ECHO CARDIOLOGY Proc

8 04/29/94 pr 54 ECHO CARDIOLOGY Proc

9 04/29/94 p 55 ECHO CARDIOLOGY Proc

Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Select: Quit//RM

CHOOSE No. 1-9: 1

Procedure/Medicine Resulting Mar 02, 2001@11:34:48 Page: 1 of 1

CPRSPATIENT,FOUR 666-43-8796 2B M DEC 4,1949 (50) \<CAD\>

Consult No.: 242 Associated Medicine Results

1 ELECTROCARDIOGRAM OCT 2,1995@10:00 ABNORMAL

Select action or item number

DM Disassociate result DR Display Result

Select Action:Quit// DM

Select item: (1-1): 1

ELECTROCARDIOGRAM OCT 2,1995@10:00 ABNORMAL

Are you sure you want to disassociate this result? NO// Y YES

### Results Display (RT) Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Results Display (RT) action allows you to review results of any consult/request for a patient.

The following is an example of the report displayed when you select the RT action:

C S L T R E S U L T S D I S P L A Y

CPRSPATIENT,FOUR 666-43-8796 2B M DEC 4,1949 (50) \<CAD\>

---------------------- ELECTROCARDIOGRAM SUMMARY REPORT ---------------------

DIAGNOSIS

Interpretation Code (rhythm): SINUS TACHYCARDIA

Interpretation Code (config): ABNORMAL ECG

INDICATIONS

Type OF EKG: STAT RETRIEVAL

SUMMARY

Summary: ABNORMAL

Summary procedure: Sinus rhythm has replaced atrial flutter

Press return to continue or “^” to escape \<Enter\>

### Schedule (SC) Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Schedule action is similar to the Receive (RC) action in that it changes the status of a consult. There is no interface with the Scheduling Package at this time. This action is intended only for annotation purposes.

Unlike the Receive action, this action sends an alert. You can use this alert to inform the requestor of the date and time of the appointment.

In the following example we change the status of a consult from “p” pending to “s” scheduled:

CONSULT TRACKING Jun 08, 2000 21:14:16 Page: 1 of 1

CPRSPATIENT,FOUR 666-43-8796 2B M DEC 4,1949 (50) \<CAD\>

Wt.(lb): 184

Requested St No. Consult/Procedure Request

1 07/22/99 p 1561 EXERCISE TOLERANCE TEST CARDIOLOGY Proc

2 05/20/99 p 1470 CARDIOLOGY (oex) CARDIOLOGY Cons

3 04/13/99 c 1437 CARDIOLOGY (oex) CARDIOLOGY Cons

4 04/01/99 c 1429 CARDIOLOGY (oex) CARDIOLOGY Cons

5 02/26/99 c 1406 CARDIOLOGY Cons

6 01/05/99 c 1312 CARDIOLOGY Cons

7 01/04/99 c 1290 \*CARDIOLOGY Cons

8 12/18/98 c 1252 CARDIOLOGY Cons

9 12/14/98 c 1234 CARDIOLOGY Cons

Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Select: Quit//SC Schedule

CHOOSE No. 1-9: 2

Who scheduled it?: CPRSPROVIDER,ONE CPRSPROVIDER,ONE OC PHYSICIAN

Enter COMMENT...

1\>9:30 pm Jun 23 in Bldg 4

2\> \<Enter\>

EDIT Option: \<Enter\>

Do You Wish To Send An Alert With This Comment? N// Y YES

Send Alert To Requesting Provider CPRSPROVIDER,THREE? N// Y YES

Send Alert to: \<Enter\>

Processing Alerts...

(Continued on the next page.)

CONSULT TRACKING Jun 08, 2000 21:16:45 Page: 1 of 1

CPRSPATIENT,FOUR 666-43-8796 2B M DEC 4,1949 (50) \<CAD\>

Wt.(lb): 200

Requested St No. Consult/Procedure Request

1 07/22/99 p 1561 EXERCISE TOLERANCE TEST CARDIOLOGY Proc

2 05/20/99 s 1470 CARDIOLOGY (oex) CARDIOLOGY Cons

3 04/13/99 c 1437 CARDIOLOGY (oex) CARDIOLOGY Cons

4 04/01/99 c 1429 CARDIOLOGY (oex) CARDIOLOGY Cons

5 02/26/99 c 1406 CARDIOLOGY Cons

6 01/05/99 c 1312 CARDIOLOGY Cons

7 01/04/99 c 1290 \*CARDIOLOGY Cons

8 12/18/98 c 1252 CARDIOLOGY Cons

9 12/14/98 c 1234 CARDIOLOGY Cons

Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Select: Quit//

### Select New Patient (SP) Action 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to change patients at any time.

Example:

CONSULT TRACKING Jun 20, 1997 14:44:26 Page: 1 of 1

CPRSPATIENT,FOUR 666-43-8796 2B M DEC 4,1949 (50) \<CAD\>

Wt.(lb): 184

Requested St No. Consult/Procedure Request

1 08/18/99 a 1586 PULMONARY Cons

2 08/18/99 a 1585 PULMONARY Cons

3 06/23/99 c 1545 PULMONARY Cons

Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Select: Quit// SP New Patient

Select Patient: CPRSPATIENT,THREE 01-01-51 666123456 YES SC VETERAN

Select Service/Specialty: ALL SERVICES// PULMONARY

List From Starting Date: ALL DATES // \<Enter\> ALL DATES

(Continued on the next page.)

CONSULT TRACKING Jun 20, 1997 14:44:38 Page: 1 of 1

CPRSPATIENT,THREE 666-12-3456 2B MAR 3,1960 (40) \<AD\>

Wt.(lb): 184

Requested St No. Consult/Procedure Request

1 09/14/98 c 1163 PULMONARY Cons

2 09/09/98 dc 1162 PULMONARY Cons

3 07/14/98 dc 1116 PULMONARY Cons

4 07/14/98 c 1114 \*CARDIOLOGY PULMONARY Cons

Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Select: Quit//

### Significant Findings (SF) Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Significant Findings action allows a clinic or service to append a significant findings flag onto a consult (whether completed or not). The action prompts you to enter a comment and sends an alert either at the time the SF action is taken or when the consult is complete. An asterisk is placed next to the consults that have a Significant Findings value of Y.

In this example we add a significant finding to an already completed consult:

CONSULT TRACKING May 01, 1998 14:51:35 Page: 1 of 2

CPRSPATIENT,THREE 666-12-3456 2B MAR 3,1960 (40) \<AD\>

Wt.(lb): 184

Requested St No. Consult/Procedure Request

1 09/21/00 p 1764 Electrocardiogram CARDIOLOGY Proc

2 04/25/00 c 1713 CARDIOLOGY Cons

3 01/26/00 c 1665 CARDIOLOGY Cons

4 06/02/99 c 1483 VENTRICAL LEAD IMPLANT CARDIOLOGY Proc

5 04/29/99 c 1455 CARDIOLOGY (oex) CARDIOLOGY Cons

6 02/18/99 x 1395 CARDIOLOGY Cons

7 01/05/99 c 1310 \*GASTROENTEROLOGY CARDIOLOGY Cons

8 01/04/99 c 1287 CARDIOLOGY Cons

9 12/18/98 c 1249 CARDIOLOGY Cons

10 10/09/98 c 1184 CARDIOLOGY Cons

11 08/24/98 dc 1144 CARDIOLOGY Cons

12 07/13/98 c 1113 \*CARDIOLOGY Cons

\+ Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Select: Next Screen// SF Sig Findings

CHOOSE No. 1-17: 1

Current Significant Findings = not entered yet

Are there significant findings? (Y/N/U): unknown// yes

Enter COMMENT:

1\>Pt experiencing 60% loss of breathing efficiency.

2\>

EDIT Option:

Alert will be sent to Requesting Provider: CPRSPROVIDER,TWO

Send Alert to: CPRSPROVIDER,TWO added to the list.

And Send Alert to: CPRSPROVDER,THREE already in the list.

And Send Alert to:

Processing Alerts...

(Continued on the next page.)

CONSULT TRACKING May 01, 1998 14:52:28 Page: 1 of 2

CPRSPATIENT,THREE 666-12-3456 2B MAR 3,1960 (40) \<AD\>

Wt.(lb): 184

Requested St No. Consult/Procedure Request

1 09/21/00 p 1764 \*Electrocardiogram CARDIOLOGY Proc

2 04/25/00 c 1713 CARDIOLOGY Cons

3 01/26/00 c 1665 CARDIOLOGY Cons

4 06/02/99 c 1483 VENTRICAL LEAD IMPLANT CARDIOLOGY Proc

5 04/29/99 c 1455 CARDIOLOGY (oex) CARDIOLOGY Cons

6 02/18/99 x 1395 CARDIOLOGY Cons

7 01/05/99 c 1310 \*GASTROENTEROLOGY CARDIOLOGY Cons

8 01/04/99 c 1287 CARDIOLOGY Cons

9 12/18/98 c 1249 CARDIOLOGY Cons

10 10/09/98 c 1184 CARDIOLOGY Cons

11 08/24/98 dc 1144 CARDIOLOGY Cons

12 07/13/98 c 1113 \*CARDIOLOGY Cons

\+ Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Select: Next Screen//

## Notifications about Consults and Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During your session, you may notice:

You have PENDING ALERTS

Enter "VA VIEW ALERTS to review alerts

Select Clinician Menu Option:

This appears on the screen before each prompt. You may enter VA at any menu prompt in which this message appears to view patient information related to pending notifications.

There are six notifications relating to consults:

| OE/RR Notifications                                                                             | Notification Number | Recipients                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| New Service Consult/Request                                                                     | 27                  | Service Users plus Attention                                                                                                                                         |
| Consult/Request Resolution                                                                      | 23                  | Ordering Provider on Complete                                                                                                                                        |
| Consult/Request Cancel/Hold                                                                     | 30                  | Ordering Provider and others as determined by who is taking the action. The NOTIFY ON DC field in file 123.5 affects who gets the alert on DC.                       |
| Consult/Request Update                                                                          | 63                  | Determined by the individual taking the associated action.\*                                                                                                         |
| Order(s) Require Electronic Signature                                                           | 5                   | Determined by CPRS                                                                                                                                                   |
| <span id="Prosthetics_Consult_Updated_column" class="anchor"></span>Prosthetics Consult Updated | 89                  | Determined by the individual taking the associated action. See the [Add Prosthetics Consult Updated](#Prosthetics_Consult_Updated_section) section for more details. |

The purpose of these notifications is to allow you to take appropriate follow-up action. This might involve merely reading new information, or it might involve several actions on your part such as scheduling an appointment, signing a consult, resubmission, etc.

\*NOTE:

- When a comment is added by an UPDATE USER, the alert will only go to the ordering provider (unless additional alert recipients are added).
- When a comment is added by a SERVICE TEAM member, the alert will only go to the ordering provider (unless additional alert recipients are added).
- <span id="Additional_Recipients_to_Receive_Alert1" class="anchor"></span>Any additional recipients added during the Add Comment Action will receive the alert, even if a selected recipient has the alert Disabled.

To initiate the follow-up action, enter VA at the prompt after the view alerts message. In the following example, a user follows up a notification by signing an order:

You have PENDING ALERTS

Enter "VA VIEW ALERTS to review alerts

Select CPRS Manager Menu Option: VA View Alerts

1\. CPRSPATIENT,ONE (C4723): New order(s) placed.

2\. CPRSPATIENT,THREE (C3456): Consult/Request DENIED To Service: PODIATRY

3\. CPRSPATIENT,ONE (C4723): Order requires electronic signature.

Select from 1 to 3

or enter ?, A I, F, P, M, R, or ^ to exit

or RETURN to continue: 3

Processing alert: CPRSPATIENT,ONE (C4723): Order requires electronic signature.

Searching the patient's chart ...

Unsigned Orders Sep 24, 1997 09:22:04 Page: 1 of 1

CPRSPATIENT,THREE 666-12-3456 2B MAR 3,1960 (40) \<AD\>

Selected date range: None Selected

Item Ordered Requestor Start Stop ts

1 \>\> Weight \*UNSIGNED\* \| CPRSPROVIDER,O unr

2 Consult to CARDIOLOGY Consultant's Choice \| CPRSPROVIDER,O unr

\*UNSIGNED\* \|

3 Consult to CARDIOLOGY Consultant's Choice \| CPRSPROVIDER,O unr

\*UNSIGNED\* \|

Enter the numbers of the items you wish to act on.

Enter the numbers of the items you wish to act on. \>\>\>

\+ Next Screen - Previous Screen Q Quit

Select: Quit// 2

Unsigned Orders Sep 24, 1997 09:22:04 Page: 1 of 1

CPRSPATIENT,THREE 666-12-3456 2B MAR 3,1960 (40) \<AD\>

Selected date range: None Selected

Item Ordered Requestor Start Stop Sts

1 \>\> Weight \*UNSIGNED\* \| CPRSPROVIDER,O unr

2 Consult to CARDIOLOGY Consultant's Choice \| CPRSPROVIDER,O unr

\*UNSIGNED\* \|

3 Consult to CARDIOLOGY Consultant's Choice \| CPRSPROVIDER,O unr

\*UNSIGNED\* \|

Enter the numbers of the items you wish to act on.

Enter the numbers of the items you wish to act on. \>\>\>

Change Sign

Discontinue Detailed Display

Select: Quit// S

Consult to CARDIOLOGY Consultant's Choice –

Enter your Current Signature Code: SIGNATURE VERIFIED

Consult to CARDIOLOGY Consultant's Choice signed.

Searching the patient's chart ...

(Continued on the next page.)

Unsigned Orders Sep 24, 1997 09:22:04 Page: 1 of 1

CPRSPATIENT,THREE 666-12-3456 2B MAR 3,1960 (40) \<AD\>

Selected date range: None Selected

Item Ordered Requestor Start Stop ts

1 \>\> Weight \*UNSIGNED\* \| CPRSPROVIDER,O unr

3 Consult to CARDIOLOGY Consultant's Choice \| CPRSPROVIDER,O unr

\*UNSIGNED\* \|

Enter the numbers of the items you wish to act on.

Enter the numbers of the items you wish to act on. \>\>\>

\+ Next Screen - Previous Screen Q Quit

Select: Quit//

### Enabling Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In many cases Notifications will not come to you automatically. To find out what Notifications you should be getting, you can run the Show Me the Notifications I Can Receive option from the Notifications Management Menu. If this report shows any notifications you want to receive that are disabled, you may enable them with the Enable/Disable My Notifications option.

In this example we run the Show Me the Notifications I Can Receive report and then enable Consult/Request Cancel/Hold, Consult/Request Resolution, and New Service Consult/Request (Notice that Order(s) Require Electronic Signature is already on):

Select Notification Mgmt Menu Option: ?

1 Enable/Disable My Notifications

2 Erase All of My Notifications

3 Set Notification Display Sort Method (GUI)

4 Send me a MailMan bulletin for Flagged Orders

5 Show Me the Notifications I Can Receive

6 Set Surrogate to Receive My Notifications

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Notification Mgmt Menu Option: 5 Show Me the Notifications I Can Receive

Would you like help understanding the list of notifications? No// Y (Yes)

DEVICE: HOME// \<Enter\> VAX

Notification List Help Message Page: 1

The delivery of notifications as alerts is determined from values set for:

Users, OE/RR Teams, Service/Sections, Inpatient Locations,

Hospital Divisions, Computer System and Order Entry/Results Reporting.

Possible values include 'Enabled', 'Disabled' and 'Mandatory'. These values

indicate a User's, OE/RR Team's, Service's, Location's, Division's, System's

and OERR's desire for the notification to be 'Enabled' (sent under most

conditions), 'Disabled' (not sent), or 'Mandatory' (almost always sent.)

All values, except the OERR (Order Entry) value, can be set by IRM

or Clinical Coordinators. Individual users can set 'Enabled/Disabled/Mandatory'

values for each specific notification via the 'Enable/Disable My Notifications'

option under the Personal Preferences and Notification Mgmt Menu option menus.

'ON' indicates the user will receive the notification under normal conditions.

'OFF' indicates the user normally will not receive the notification.

Notification recipient determination can also be influenced by patient

location (inpatients only.) This list does not consider patient location

when calculating the ON/OFF value for a notification.

\- End of Report -

Press RETURN to continue: \<Enter\>

This will take a moment or two, please stand by.................................

...............

DEVICE: HOME// \<Enter\> VAX

Notification List for CPRSPROVIDER,ONE Page: 1

Notification ON/OFF For This User and Why

-------------------------------- ---------------------------------------------

ABNORMAL IMAGING RESULTS ON OERR value is Mandatory

ABNORMAL LAB RESULT (INFO) ON User value is Mandatory

ABNORMAL LAB RESULTS (ACTION) OFF OERR value is Disabled

ADMISSION ON OERR value is Enabled

CONSULT/REQUEST CANCEL/HOLD ON User value is Mandatory

CONSULT/REQUEST RESOLUTION ON User value is Mandatory

CONSULT/REQUEST UPDATED OFF OERR value is Disabled

CRITICAL LAB RESULT (INFO) ON OERR value is Mandatory

CRITICAL LAB RESULTS (ACTION) ON OERR value is Mandatory

DC ORDER OFF OERR value is Disabled

DECEASED PATIENT ON OERR value is Enabled

DISCHARGE OFF OERR value is Disabled

DNR EXPIRING OFF OERR value is Disabled

ERROR MESSAGE OFF OERR value is Disabled

FLAG ORDER FOR CLARIFICATION ON OERR value is Enabled

FLAGGED OI EXPIRING - INPT OFF OERR value is Disabled

FLAGGED OI EXPIRING - OUTPT OFF OERR value is Disabled

FLAGGED OI ORDER - INPT OFF OERR value is Disabled

FLAGGED OI ORDER - OUTPT ON System value is Enabled

FLAGGED OI RESULTS - INPT OFF OERR value is Disabled

FLAGGED OI RESULTS - OUTPT OFF OERR value is Disabled

FOOD/DRUG INTERACTION OFF OERR value is Disabled

FREE TEXT OFF OERR value is Disabled

IMAGING PATIENT EXAMINED OFF User value is Disabled

IMAGING REQUEST CANCEL/HELD ON OERR value is Enabled

IMAGING RESULTS OFF User value is Disabled

IMAGING RESULTS AMENDED OFF OERR value is Disabled

LAB ORDER CANCELED OFF OERR value is Disabled

LAB RESULTS OFF OERR value is Disabled

MEDICATIONS EXPIRING OFF OERR value is Disabled

NEW ORDER OFF OERR value is Disabled

NEW SERVICE CONSULT/REQUEST ON User value is Mandatory

NPO DIET MORE THAN 72 HRS OFF OERR value is Disabled

ORDER CHECK OFF OERR value is Disabled

ORDER REQUIRES CHART SIGNATURE ON OERR value is Mandatory

ORDER REQUIRES CO-SIGNATURE OFF OERR value is Disabled

ORDER REQUIRES ELEC SIGNATURE ON OERR value is Mandatory

ORDERER-FLAGGED RESULTS OFF OERR value is Disabled

SERVICE ORDER REQ CHART SIGN ON OERR value is Mandatory

STAT IMAGING REQUEST OFF OERR value is Disabled

STAT ORDER OFF OERR value is Disabled

STAT RESULTS OFF OERR value is Disabled

TRANSFER FROM PSYCHIATRY OFF OERR value is Disabled

UNSCHEDULED VISIT ON OERR value is Enabled

UNVERIFIED MEDICATION ORDER OFF OERR value is Disabled

UNVERIFIED ORDER OFF OERR value is Disabled

URGENT IMAGING REQUEST OFF OERR value is Disabled

\- End of Report -

Select Notification Mgmt Menu Option: 1 Enable/Disable My Notifications

Enable/Disable My Notifications

-------------------------------------------------------------------------------

------------------- Setting for User: CPRSPROVIDER,ONE -------------------

Select Notification: cons

1 CONSULT/REQUEST CANCEL/HOLD

2 CONSULT/REQUEST RESOLUTION

3 CONSULT/REQUEST UPDATED

CHOOSE 1-3: 3 CONSULT/REQUEST UPDATED

Are you adding CONSULT/REQUEST UPDATED as a new Notification? Yes// \<Enter\> YES

Notification: CONSULT/REQUEST UPDATED// \<Enter\> CONSULT/REQUEST UPDATED CONSULT/REQUEST UPDATED

Value: ?

Code indicating processing flag for the entity and notification.

Select one of the following:

M Mandatory

E Enabled

D Disabled

Value: Enabled

Select Notification: \<Enter\>

Select Notification Mgmt Menu Option:

### New Service Consult/Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This notification is triggered by the Consults package when a new consult has been requested by a user.

In the following example, the system displays three notifications for new Consults:

CPRSPATIE (C5377): New consult Neuro (Stat)

CPRSPATIE (C3456): New consult CAR (Routine)

CPRSPATIE (C6572): New consult PLM (Routine)

Enter "VA VIEW ALERTS to review alerts

Select Systems Manager Menu Option:

As a follow-up action, the system displays the consult in a Consult/Tracking screen so that the recipient can take appropriate action. To initiate the follow-up action, enter VA at the prompt and select the notification you want to follow-up on. After selecting this notification from the View Alerts menu, the system deletes the notification.

In the following example, a new consult is first examined and then a receive action is performed:

1\. CPRSPATIE (C2342): NEW consult CAR (Routine)

2\. CPRSPATIE (C2432): Consult COMPLETED: CAR

Select from 1 to 3

or enter ?, A I, F, P, M, R, or ^ to exit

or RETURN to continue: A

Processing alert: CPRSPATIENT,NINE (C2342): NEW consult (Routine)

Consult/Request Alerts Feb 13, 1998 13:43:55 Page: 1 of 1

CPRSPATIENT,NINE 666-24-2342 1A MAR 3,1960 (40) \<AD\>

Wt.(lb): 184

Number Date St Service Procedure

1 12/16/97 p CARDIOLOGY EKG Portable

Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Select Action: Quit// DD Detailed Display

Compiling Report...

CONSULTS DETAILED DISPLAY Dec 19, 1997 08:12:04 Page: 1 of 5

CONSULT DETAILED DISPLAY Consult No.: 731

CPRSPATIENT,FORTY 000-00-0040 DOB: (74) Wt. (lb): No Entry

Current Inpatient/Outpatient: Inpatient

Ward: 1A

To Service: CARDIOLOGY

From Service: 1A

Consult Type: EKG Portable

Provisional Diagnosis: Cardiomyopathy

Reason For Request: Rule out alternate diagnosis

Status: PENDING

Service is to be rendered on an INPATIENT basis

ATTENTION: CPRSPROVIDER,SEVEN

Place: Bedside

Urgency: Stat

Request Activity Date/Time Ordering Clinician Entered By

CPRS RELEASED ORDER 12/16/97 15:52 CPRSPROVIDER,SEVEN CPRSPROVIDER,SEVEN

\+ Enter ?? for more actions

Select Action: Next Screen// Q Q

Consult/Request Alerts Feb 13, 1998 13:44:53 Page: 1 of 1

CPRSPATIENT,NINE 666-24-2342 1A MAR 3,1960 (40) \<AD\>

Wt.(lb): 184 Number <u>Date St Service Procedure</u>

1 12/16/97 p CARDIOLOGY EKG Portable

Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings RM Remove Med Rslt

SC Schedule CM Add Comment DD Detailed Display ER Edit/Resubmit

Select Action: Quit// RC Receive

Who received it?: CPRSPROVIDER,SEVEN SC

Date/Time Actually Received: NOW// (DEC 19, 1997 @ 08:12)

(Continued on the next page.)

Consult/Request Alerts Dec 19, 1997 08:13:01 Page: 1 of 1

CPRSPATIENT,NINE 666-24-2342 1A MAR 3,1960 (40) \<AD\>

Wt.(lb): 184 Number <u>Date St Service Procedure</u>

1 12/16/97 a CARDIOLOGY EKG Portable

Enter ?? for more actions

SP Select Patient FR Forward CT Complete/Update RT Results Display

CV Change View ... CX Cancel (Deny) MA Make Addendum PF Print Form 513

RC Receive DC Discontinue SF Sig Findings ER Edit/Resubmit

SC Schedule CM Add Comment DD Detailed Display

Select Action: Quit// \<Enter\> QUIT

Continue Processing ALERTS ? Y//

  

### Consult/Request Resolution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** This notification is typically triggered by the Consults package when it determines that a consult is complete but may also be triggered when an associated result has been amended or removed.

In the following example, the originating provider receives notifications that consults are complete:

CPRSPATIE (C3456): Completed Consult CAR HOLTER

CPRSPATIE (C1996): \*Completed Consult CAR

CPRSPATIE (C8910): Completed Consult PSURG

Enter "VA VIEW ALERTS to review alerts

Select Systems Manager Menu Option:

As a follow-up action, the system displays the Consult/Request and results/report. To initiate the follow-up action, enter VA at the prompt and select the notification you want to follow-up on. After viewing, the system deletes the notification.

Notice the asterisk on the second notification. This means that there are significant findings for that consult.

The less common usage for the Consult/Request Resolution notification applies to amending or reassigning results. In the following example, the signed result was amended, and the originating provider received notification that the consult has been reactivated, followed immediately by another notification that the consult has been completed. The two back-to-back notifications are a result of the software processing the amendment action on the document, which essentially translates into a disassociate result activity for the consult, followed immediately by the signature (completion) action for the document. In this scenario, the consult would not have any other linked documents already in a completed status.

If, during the result removal, the consult does not change status, but does have significant findings, the alert text will appear as: “\*Removed consult note for"

CPRSPATIE (C3456): Reactivated consult, removed note for VASCULAR SURGERY

CPRSPATIE (C3456): Completed Consult VASCULAR SURGERY

CPRSPATIE (C7890): \*Removed consult note for AUDIOLOGY OUTPT

CPRSPATIE (C1996): \*Completed Consult CAR

CPRSPATIE (C8910): Completed Consult PSURG

Enter "VA VIEW ALERTS to review alerts

### Consult/Request Updated

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This alert is triggered when a comment is added to consult, or the consult is scheduled. Comments may be added either with the Add Comment (CM) action or the Schedule (SC) action. The text of the alert is altered depending on which one of these actions initiated the alert as follows:

Adding a Comment\#63 "Comment Added to Consult: . . ."

Scheduling\#63 "Scheduled Consult: . . ."

As a follow-up action, the system displays the consult with comments. If appropriate, the clinician may write an additional comment or take other actions as needed.

- When a comment is added by an UPDATE USER, the alert will only go to the ordering provider (unless additional alert recipients are added).
- When a comment is added by a SERVICE TEAM member, the alert will only go to the ordering provider (unless additional alert recipients are added).
- <span id="Additional_Recipients_to_Receive_Alert2" class="anchor"></span>Any additional recipients added during the Add Comment action will receive the alert, even if a selected recipient has the alert Disabled.

<span id="GMRC_75_CONSULT_REQUEST_UPDATED" class="anchor"></span>This alert is also used by the Healthcare Claims Processing System (HCPS) to notify VA providers the status of a patient who has been referred to a Non-VA Care provider or facility. When an HCPS user enters a comment in RAS, CPRS is updated. The HCPS user might not be a user in VistA; a proxy user will display for ‘Responsible Person’ and ‘Entered By’ in the CPRS, as shown below:

Facility

Activity Date/Time/Zone Responsible Person Entered By

-------------------------------------------------------------------------------

ADDED COMMENT 08/08/14 22:31 HCPS,APPLICATION HCPS,APPLICATION

(entered) 08/08/14 22:40

Author: CPRSPROVIDER,TEN

### Consult/Request Cancel/Hold

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This notification is triggered from the Consults package when a Consult request is cancelled, discontinued, or put on hold.

In the following example, a user receives notification of a discontinued and a denied consult:

CPRSPATIE (C2342): Cancelled consult CAR

CPRSPATIE (C9876): Discontinued Consult MEDICINE

CPRSPATIE (C3456): Cancelled consult POD

Enter "VA VIEW ALERTS to review alerts

Select Systems Manager Menu Option:

As a follow-up action, the system displays consult with comments. If appropriate, the submitter may resubmit the consult based on this new information. To initiate the follow-up action, enter VA at the prompt and select the notification you want to follow-up on. After viewing, the notification is deleted by the system.

In the following example, a cancelled order is edited and resubmitted:

You have PENDING ALERTS

Enter "VA VIEW ALERTS to review alerts

Select Consult Service Tracking Option: VA View Alerts

1\. CPRSPATIE (C2342): Cancelled consult to PLM

2\. CPRSPATIE (C3456): Discontinued consult to CAR

3\. CPRSPATIE (C2432): Completed Consult CAR

Select from 1 to 3

or enter ?, A I, F, P, M, R, or ^ to exit

or RETURN to continue: 1

Processing alert: CPRSPROVIDER,EI (E8840): Cancelled consult PLM

(Continued on next page.)

Edit Consult Order Feb 26, 1999 15:58:08 Page: 1 of 2

Edit Consult for Patient CPRSPATIENT,EIGHT Consult Number: 1336

Sending Provider: CPRSPROVIDER,SEVEN

Field Name Current Field Contents

CURRENT STATUS: (Not Editable): CANCELLED

CANCELLED BY (Not Editable): CPRSPROVIDER,SEVEN

CANCELLED COMMENT (Not Editable):

Testing edit.

------------------------------------------------------------------------------

CANCELLED BY (Not Editable): CPRSPROVIDER,SEVEN

CANCELLED COMMENT (Not Editable):

Testing edit/resubmit.

------------------------------------------------------------------------------

SENDING PROVIDER (Not Editable): CPRSPROVIDER,SEVEN

REQUEST TYPE (Not Editable): Consult

-------------------------------------------------------------------------------

1 TO SERVICE: PULMONARY

2 PROCEDURE:

3 Performed as INPT OR OUTPT: Outpatient

\+ Enter ?? for more actions

ED Edit A Field RS ReSubmit Consult

Select Action: Next Screen// \<Enter\>

Edit Consult Order Feb 26, 1999 16:01:18 Page: 2 of 2

Edit Consult for Patient CPRSPATIENT,EIGHT Consult Number: 1336

Sending Provider: CPRSPROVIDER,SEVEN

\+ Field Name Current Field Contents

4 URGENCY: Routine

5 PLACE OF CONSULTATION:

6 ATTENTION (CONSULTANT):

7 PROVISIONAL DIAGNOSIS:

8 REASON FOR REQUEST:

Pt has trouble breathing.

9 COMMENT(S): (Add Only)

ADDED COMMENT (Not Editable) Entered: Jan 11, 1999 BY: CPRSPROVIDER,SEVEN

Testing, more testing.

Enter ?? for more actions

ED Edit A Field RS ReSubmit Consult

Select Item/Action:Quit// 7

(Continued on the next page.)

Edit Consult Order Feb 02, 1999 10:44:38 Page: 2 of 2

Edit Consult for Patient CPRSPATIENT,NINE Consult Number: 1366

Sending Provider: CPRSPROVIDER,SEVEN

\+ Field Name Current Field Contents

8 REASON FOR REQUEST:

Pt is having chest pains.

9 COMMENT(S): (Add Only)

Enter ?? for more actions

ED Edit A Field RS ReSubmit Consult

Select Item/Action:Quit// ED Edit A Field

Select the fields to edit: 7

Provisional Diagnosis: Angina

Edit Consult Order Feb 26, 1999 16:06:16 Page: 2 of 2

Edit Consult for Patient CPRSPATIENT,EIGHT Consult Number: 1336

Sending Provider: CPRSPROVIDER,SEVEN

\+ Field Name Current Field Contents

4 URGENCY: Routine

5 PLACE OF CONSULTATION:

6 ATTENTION (CONSULTANT):

7 PROVISIONAL DIAGNOSIS: Angina

8 REASON FOR REQUEST:

Pt has trouble breathing.

9 COMMENT(S): (Add Only)

ADDED COMMENT (Not Editable) Entered: Jan 11, 1999 BY: CPRSPROVIDER,TWO

Testing, more testing.

Enter ?? for more actions

ED Edit A Field RS ReSubmit Consult

Select Action: Quit// \<Enter\> QUIT

(Continued on the next page.)

This Consult Has Not Been Resubmitted!!

Resubmit Or All Edits Will Be Lost!!

Do you wish to resubmit now? ? YES// Y YES

Resubmitting Consult ... One moment please ...

Filing Tracking Data...

1\. CPRSPATIE (C3456): Discontinued consult to CAR

2\. CPRSPATIE (C2432): Completed Consult CAR

Select from 1 to 2

or enter ?, A I, F, P, M, R, or ^ to exit

or RETURN to continue:

#### Special Considerations for Discontinued Orders

When an order is Discontinued, who gets the notification depends on the source of the discontinuation. This is dependent on the NOTIFY ON DC field in file 123.5 for the service to which the consult was directed. This field is set by the Set up Consult Services (SS) command of the Consult Management Option.

### Consult/Request Has an Added Comment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a comment is added to a consult by someone in the receiving service, that person is prompted to send notification to the originator of the consult and to any other persons. Other recipients of this notification are controlled as a New Service Consult.

In the following example, a clinician in the Surgery service has added a comment:

SIMPSON,H (S9999): Comment Added to Consult CARDIOLOGY

Enter "VA VIEW ALERTS to review alerts

Select Consult Management Option:

The follow-up action is to display the orders containing the comments so that you can read them.

- <span id="ConsultADDEDCOMMENT" class="anchor"></span>When a comment is added by an UPDATE USER, the alert will only go to the ordering provider (unless additional alert recipients are added).
- When a comment is added by a SERVICE TEAM member, the alert will only go to the ordering provider (unless additional alert recipients are added).

### Order(s) Require Electronic Signature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you do not sign a consult at the time you initiate it, the CPRS triggers a notification reminding you of the need for an electronic signature.

In the following example, three notifications are presented for Consults that need an electronic signature:

CPRSPATIE (C3456): Order requires electronic signature.

CPRSPATIE (C4723): Order requires electronic signature.

CPRSPATIE (C3234): Order requires electronic signature.

Enter "VA VIEW ALERTS to review alerts

Select Systems Manager Menu Option:

The follow-up action is to display the orders requiring electronic signature in a CPRS screen so that you can use the Sign action. The system deletes the notification after you have signed the order.

### Significant Findings for a Consult

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the status of the Significant Findings Flag is changed in any way, an alert is sent by the Consults package. As far as the recipients and delivery, this notification is treated like a Consult/ Request Resolution.

This alert may be delayed, at the user’s option, until the consult is complete.

In the example that follows, three significant findings notifications are present. One for a completed consult, one for a pending consult, and one for the Significant Findings Flag being turned off on a completed consult:

CPRSPATIE (C3456): Sig Findings for consult CAR

CPRSPATIE (C6572): Sig Findings for consult CAR

CPRSPATIE (C1432): No Sig Findings for consult PLM

Enter "VA VIEW ALERTS to review alerts

Select Systems Manager Menu Option:

The follow-up action is to display the orders that have had a change in the Significant Findings Flag in the CPRS screen so that you can examine them.

### Prosthetics Consult Updated

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This alert is essentially a copy of the Consult/Request Updated alert and is intended to separate the update alert traffic between prosthetics consults and all other consults. Users not interested in updates to prosthetics requests may turn this alert off.

The Prosthetics Consult Updated alert is triggered by the Add Comment (CM) or Schedule action (SC) when those actions are taken on a consult request to a prosthetics service.  
  
The text of the alert is altered depending on which one of these actions initiated the alert as follows:

Adding a Comment \#89 "Comment Added to consult: . . ."

Scheduling \#89 "Scheduled Consult: . . ."

As a follow-up action, the system displays the consult with comments. If appropriate, the clinician may write an additional comment or take other actions as needed.

- When a comment is added by an UPDATE USER, the alert will only go to the ordering provider (unless additional alert recipients are added).
- When a comment is added by a SERVICE TEAM member, the alert will only go to the ordering provider (unless additional alert recipients are added).

## ADMIN KEY Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new GRMC Patch for “Admin Key Reporting” has been created to generate 3 new GRMC Reports.

- GMRC RPT ADMIN RELEASE CONSULT
- GMRC RPT ADMIN REL CONS USER
- GMRC RPT ADMIN REL CONS GROUPR

These reports allow local GMRC users to generate reports that will show the overall usage of the “Administratively Released by Policy” consults.

The user steps required to access and to display these reports are:

VISTAS1:VISTA\>D ^XUP

Select OPTION NAME: GMRC MGR Consult Management

RPT Consult Tracking Reports ...

SS Set up Consult Services

SU Service User Management

CS Consult Service Tracking

RX Pharmacy TPN Consults

GU Group update of consult/procedure requests

UA Determine users' update authority

UN Determine if user is notification recipient

NR Determine notification recipients for a service

TD Test Default Reason for Request

LH List Consult Service Hierarchy

PR Setup procedures

CP Copy Prosthetics services

CCT Menu for Closure Tools ...

DS Duplicate Sub-Service

FS Define Fee Services

IFC IFC Management Menu ...

TP Print Test Page

S<span id="Option_Help_119" class="anchor"></span>elect Consult Management \<TEST ACCOUNT\> Option: RPT Consult Tracking Reports

TI Administratively Released Consults by Title

GR Administratively Released Consults by Group

US Administratively Released Consults by User

ST Completion Time Statistics

PC Service Consults Pending Resolution

SH Service Consults Schedule-Management Report

CC Service Consults Completed

CP Service Consults Completed or Pending Resolution

IFC IFC Requests

IP IFC Requests By Patient

IR IFC Requests by Remote Ordering Provider

LCR Consults Local Completion Rate

NU Service Consults with Consults Numbers

PI Print IFC Requests

PL Print Consults by Provider, Location, or Procedure

PM Consult Performance Monitor Report

PR Print Service Consults by Status

SC Service Consults By Status

TS Print Completion Time Statistics Report

Select Consult Tracking Reports \<TEST ACCOUNT\> Option: ???

'Administratively Released Consults by Title' Option name: GMRC RPT ADMIN RE

LEASE CONSULT Synonym: TI

The ADMINISTRATIVELY RELEASED CONSULTS BY TITLE report displays counts of

the number of consults created by the OR ADMIN RBP TO CC security key

(ADMIN key) and ADMINISTRATIVELY RELEASED BY POLICY. The user will enter

a date range, and the report will be sorted by Consult Title (Request

Service name).

'Administratively Released Consults by Group' Option name: GMRC RPT ADMIN RE

L CONS GROUPR Synonym: GR

The ADMINISTRATIVELY RELEASED CONSULTS BY GROUP report displays counts of

the number of consults created by the OR ADMIN RBP TO CC security key

(ADMIN key) and ADMINISTRATIVELY RELEASED BY POLICY. The user will enter

a date range, and the report will be sorted by Consult Group (DS or

ADMIN).

'Administratively Released Consults by User' Option name: GMRC RPT ADMIN REL

CONS USER Synonym: US

The ADMINISTRATIVELY RELEASED CONSULTS BY USER report displays counts of

the number of consults created by the OR ADMIN RBP TO CC security key

(ADMIN key) and ADMINISTRATIVELY RELEASED BY POLICY. The user will enter

a date range, and the report will be sorted by User.

Select Consult Management \<TEST ACCOUNT\> Option: RPT Consult Tracking Reports

TI Administratively Released Consults by Title

GR Administratively Released Consults by Group

US Administratively Released Consults by User

ST Completion Time Statistics

PC Service Consults Pending Resolution

SH Service Consults Schedule-Management Report

CC Service Consults Completed

CP Service Consults Completed or Pending Resolution

IFC IFC Requests

IP IFC Requests By Patient

IR IFC Requests by Remote Ordering Provider

LCR Consults Local Completion Rate

NU Service Consults with Consults Numbers

PI Print IFC Requests

PL Print Consults by Provider, Location, or Procedure

PM Consult Performance Monitor Report

PR Print Service Consults by Status

SC Service Consults By Status

TS Print Completion Time Statistics Report

Select Consult Tracking Reports \<TEST ACCOUNT\> Option: TI Administratively Rele

ased Consults by Title

Enter Consult Released Starting Date: T-90

Enter Consult Released Ending Date: T

Admin Released Consults-Title Oct 12, 2018@08:17:12 Page: 1 of 1

VAMC: FACILITY VAMC

From: Jul 14, 2018 To: Oct 12, 2018

Releasing Person Number

COMMUNITY CARE-ADMIN-CARDIAC 58

CPRSADMINUSER,ONE 48

CPRSPROVIDER,ONE 10

COMMUNITY CARE-DS-CARDIAC 42

CPRSADMINUSER,ONE 34

CPRSPROVIDER,ONE 8

GRAND TOTAL 100

Enter ?? for more actions

Select Action:Quit//

TI Administratively Released Consults by Title

GR Administratively Released Consults by Group

US Administratively Released Consults by User

ST Completion Time Statistics

PC Service Consults Pending Resolution

SH Service Consults Schedule-Management Report

CC Service Consults Completed

CP Service Consults Completed or Pending Resolution

IFC IFC Requests

IP IFC Requests By Patient

IR IFC Requests by Remote Ordering Provider

LCR Consults Local Completion Rate

NU Service Consults with Consults Numbers

PI Print IFC Requests

PL Print Consults by Provider, Location, or Procedure

PM Consult Performance Monitor Report

PR Print Service Consults by Status

SC Service Consults By Status

TS Print Completion Time Statistics Report

Select Consult Tracking Reports \<TEST ACCOUNT\> Option: GR Administratively Rele

ased Consults by Group

Enter Consult Released Starting Date: T-90

Enter Consult Released Ending Date: T

Admin Released Consults-User Oct 12, 2018@08:15:21 Page: 1 of 1

VAMC: FACILITY VAMC

From: Jul 14, 2018 To: Oct 12, 2018

Admin & DS Number

ADMIN 58

COMMUNITY CARE-ADMIN-CARDIAC 58

CPRSADMINUSER,ONE 48

CPRSPROVIDER,ONE 10

DS 42

COMMUNITY CARE-DS-CARDIAC 42

CPRSADMINUSER,ONE 34

CPRSPROVIDER,ONE 8

GRAND TOTAL 100

Enter ?? for more actions

Select Action:Quit//

TI Administratively Released Consults by Title

GR Administratively Released Consults by Group

US Administratively Released Consults by User

ST Completion Time Statistics

PC Service Consults Pending Resolution

SH Service Consults Schedule-Management Report

CC Service Consults Completed

CP Service Consults Completed or Pending Resolution

IFC IFC Requests

IP IFC Requests By Patient

IR IFC Requests by Remote Ordering Provider

LCR Consults Local Completion Rate

NU Service Consults with Consults Numbers

PI Print IFC Requests

PL Print Consults by Provider, Location, or Procedure

PM Consult Performance Monitor Report

PR Print Service Consults by <span id="GMRC_3_107" class="anchor"></span>Status

SC Service Consults By Status

TS Print Completion Time Statistics Report

Select Consult Tracking Reports \<TEST ACCOUNT\> Option: US Administratively Rele

ased Consults by User

Enter Consult Released Starting Date: T-90

Enter Consult Released Ending Date: T

<span id="GR_fwd" class="anchor"></span>On the GR report above, it is possible that a consult was originally made with the Admin Key, but then forwarded to a consult service that is neither -DS or -ADMIN. In this event the consult should still show and be counted under the DS or ADMIN group heading wherever it was first created. The screen shot below is an example of that:

Admin Released Consults-Group Feb 01, 2019@09:56:59 Page: 1 of 1

VAMC: VAMC

From: Feb 01, 2019 To: Feb 01, 2019

Admin & DS Number

ADMIN 2

CARDIOLOGY DENVER 1

CPRSADMINUSER,ONE 1

COMMUNITY CARE-ADMIN-CARDIAC 1

CPRSADMINUSER,ONE 1

GRAND TOTAL 2

Enter ?? for more actions

Select Action:Quit//

Admin Released Consults-User Oct 12, 2018@08:15:21 Page: 1 of 1

VAMC: FACILITY VAMC

From: Jul 14, 2018 To: Oct 12, 2018

Orderable Item Number

CPRSADMINUSER,ONE 82

COMMUNITY CARE-ADMIN-CARDIAC 48

COMMUNITY CARE-DS-CARDIAC 34

CPRSPROVIDER,ONE 18

COMMUNITY CARE-ADMIN-CARDIAC 10

COMMUNITY CARE-DS-CARDIAC 8

GRAND TOTAL 100

Enter ?? for more actions

Select Action:Quit//

### UCID Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In patch 96 a new field was created to track Community Care Consults. The field is \#80 (UNIQUE CONSULT ID aka UCID) in file \#123 (REQUEST/CONSULTATION). Patch 110 displays the UCID in the Consult Details at the top:

![](consult-request-tracking-user-manual-gmrc-3-0-206/068.png)

### Cancelled to Discontinued Consults

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the installation of the GMRC\*3.0\*113 patch, the CSLT CANCELLED TO DISCONTINUED parameter will be set as follows:

Is the overnight cancel to discontinue job active? = NO

How many days back to start with? = 31

How many days back to end with? = 365

<span id="GMRC_113_CancelledtoDiscontinuepg2" class="anchor"></span>This parameter steers the overnight job, GMRC CHANGE STATUS X TO DC, by the date range specified in fields 2 and 3 of the multi-valued parameter. By default, upon installation, the Is the overnight cancel to discontinue job active? field is set to NO which means that it is disabled. The site is responsible for deciding if the overnight job should run and setting it to “YES” to enable it.

The overnight job then looks for consults that have been cancelled during this period. Each consult fitting the parameter criteria is evaluated as to whether the consult was resubmitted and then cancelled again on a later date. If there is no later cancellation date, the consult is discontinued by calling the \$\$DC^GMRCGUIA API. It is possible for specific users on a VistA site to change the date range prescribed by these parameters by adjusting the “How many days back to start with?” and the “How many days back to end with?” parameters with the following. However, if the Is the overnight cancelled to discontinued job active? parameter is set to NO the other two questions will not be asked.

Select OPTION NAME: GMRC CX TO DC PARAMETER EDIT GMRC CX TO DC PARAMETER EDIT

GMRC CX TO DC PARAMETER EDIT

Is the overnight cancelled to discontinued job active? YES//

How many days back to start with: (0-99999): 31// 15 09/12/2018

How many days back to end with: (15-999999): 365// 420 08/03/2017

New contents of parameter:

Is the overnight cancelled to discontinued job active? = Y

How many days back to start with? = 15 09/12/2018

How many days back to end with? = 420 08/03/2017

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Action An action in Consults can be selected throughout processing to 1) control screen movement, 2) add new consult orders, or 3) process existing orders.
Consult Referral of a patient by the primary care physician to another hospital service/ specialty, to obtain a medical opinion based on patient evaluation and completion of any procedures, modalities, or treatments the consulting specialist deems necessary to render a medical opinion.
Consulting Site In the case of Inter-Facility Consults (IFC, see below) the VA facility that originates the consult.
Discontinued Orders Orders that are discontinued or cancelled.
<span id="GMRC_75_HCPS" class="anchor"></span>HCPS The Healthcare Claims Processing System is a centralized, automated system that will support the management of purchased care referrals/authorizations.
IFC Inter-Facility Consults permits the transmitting of consults and related information between Department of Veterans Affairs facilities. Consult requests are made to remote facilities because the needed service is not locally available or for patient convenience. Although the Consult Package is utilized in the hospital settings, Consult requests between facilities have been done manually in the past.
Order A request for a consult (service/sub-specialty evaluation) or procedure (Electrocardiogram) to be completed for a patient.
Order Cancellation A request to stop performance of a consult/procedure request; the order may be edited and reactivated
Order Discontinuation A request to stop (discontinue) performance of a consult/procedure request.
Procedure Request Any procedure (EKG, Stress Test, etc.) which may be ordered from another service/ specialty without first requiring formal consultation.
<span id="GMRC_75_RAS" class="anchor"></span>RAS Referral and Authorization System; see HCPS.
Request See Procedure Request.
Requestor This is the health care provider (e. g., the physician/clinician) who requests the order to be done.
Result A consequence of an order. Refers to evaluation or status results. When you use the Complete Request (CT) action on a consult or request, you are transferred to TIU to enter the results.
Resulting Site In the case of Inter-Facility Consults (IFC, see above) the remote site that performs the consult and enters the results.
Screen Context This term refers to the particular selection of orders displayed on the screen (e. g., Medicine consults for the patient Ralph Jones).
Service A clinical or administrative specialty (or department) within a Medical Center.
Status Result A result that indicates the processing state of an order; for example, a Pharmacy TPN Consult order may be discontinued (dc) or completed (c).
Status Symbols Codes used in order entry and Consults displays to designate the status of the order.

# # # Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Action, 185

Action Descriptions, 124

Actions

Change View (CV), 130

Comment (CM), 127

Complete Request (CT), 132

Deny Request (DY), 133

Detailed Order Display (DD), 134

Discontinue Order (DC), 138

Edit/Resubmit (ER), 140

Forward Request (FR), 141

Order of, 126

Print Form (PF), 143

Print Screen Contents (PS), 144

Quit (Q), 145

Receive Request (RC), 146

Remove Medicine Results (RM), 148

Results Display (RT), 149

Review Only, 124

Schedule (SC), 150

Select New Patient (SP), 152

Significant Findings (SF), 154

Update/Tracking, 124

View by Status (ST), 130, 131

ACTIVE, 119, 146

Add New Orders, 15

Add Original Consult, 63

Alert Actions, 4

All My Unsigned Documents, 47

asterisk, 154

Auto-forwarding, 2, 4

Brief Action Descriptions, 124

Cancel (CX), 128

Cancel Request (CX), 83

CANCELLED, 119

Change Date Range (DT), 130

change signature, 20

Change View (CV), 130

Clinical Procedures, 58

Clinically Indicated Date, 18, 24, 34, 64, 84

Comment (CM), 69, 127

COMPLETE, 119

Complete a Consult (From the Consults Tab), 72

Complete a Consults (From the Notes Tab), 75

Complete Request (CT), 72, 132

Completion Time Statistics, 117

Consult, 185

Consult Service Tracking Option, 111

Consult Status, 119

Consult/Request Cancel/Hold, 169

Consult/Request Has An Added Comment, 174

Consult/Request Resolution, 167

*Consult/Request Tracking Technical Manual*, 7, 24, 30

Consult/Request Updated, 168

Consultation Form (SF 513), 24

Consulting Site, 185

Correcting Misdirected Results, 42

*CPRS Clinical Coordinator & User Manual*, 7

*CPRS Installation Guide*, 7

*CPRS Technical Manual*, 36

Custom List, 108

Deny, 128

Deny Request (DY), 133

Detailed Display (DD), 86, 124

Detailed Order Display (DD), 134

DISCONTINUE, 119

Discontinue Order (DC), 85, 125, 138, 169

Discontinued Orders, 119, 130, 173, 185

Edit/Resubmit (ER), 140

electronic signature, 20, 21, 41, 159, 174

Enabling Notifications, 161

Enhancements Since Version 2.5, 4

FilaMan Alerts, 31

Forward Request (FR), 25, 66, 125, 141

General Service User Menu, 110

Glossary, 185

Healthcare Claims Processing System, 168, 185

HL7, 2, 5

IFC, 6, 185

IFC Requests by Remote Ordering Provider, 175

Integrated Document Management, 38

Inter-Facility Consults, 6

Introduction, 1

Make Addendum (MA), 92, 142

Management, 9

Manuals, 7

Medical Records Committee, 24

Medicine Package, 54, 59

Medicine Results), 79

New Date Range, 96

New Service Consult/Request, 164

Notifications, 156

Notifications Management Menu, 161

Operation, 13

Order, 2, 185

Order Cancellation, 138, 185

Order Checking, 5

Order Discontinuation, 185

Order New Consult, 15, 63

Order of Actions, 126

Order(s) Require Electronic Signature, 174

Package Management, 9

Package Operation, 13

Package Reference, 110

PARTIAL RESULTS, 119

PENDING, 119, 146, 150

Print Form (PF) Action, 65, 143

Print Screen Contents (PS), 144

Procedure Request, 2, 111, 124, 138, 186

prompt, 41, 112, 115, 124, 144, 145, 156, 158, 164, 167, 169

Purpose, 2

Quick Orders, 36

Quit (Q) Action, 99, 145

RAS, 168, 186

Receive Request (RC) Action, 67, 146

Relations with other VISTA Components, 5

Relationship to Other Packages, 2

Remote Ordering Provider, 175

Remove Medicine Results, 80

Remove Medicine Results (RM), 148

Request, 186

Requestor, 186

Requests, 1, 2

Requests by Remote Ordering Provider, 175

Result, 42, 186

Resulting Site, 186

Results, 38, 124, 132

Results Display (RT), 100, 124, 149

Review Only Actions, 111, 115, 124

Schedule (SC), 150

SCHEDULED, 119, 150

Screen Context, 186

Security, 9, 10

Select Consult, 101

Select New Patient (SP), 102, 152

Select Service (SS), 104, 130

service, 2, 10, 24, 186

Service Consults Pending Resolution, 118

Service Update and Tracking Security, 9

Set up Consult Services, 173

Setup, 5

signature, 20, 21, 41, 159, 174

Significant Findings (SF), 154

Significant Findings for a Consult, 175

Starting Consults in Windows, 61

status, 10, 27, 132, 146

Status after Action, 119

Status Result, 186

Status Symbols, 119, 186

Text Integration Utility (TIU), 7, 28, 38, 125, 132

*TIU Clinical Coordinator & User Manual*, 7, 38, 41

TIU Correcting Misdirected Results, 42

TIU Direct Input, 38

Tracking Option, 111

Undo Medicine Results, 80

Update/Tracking, 124

Update/Tracking Actions, 112

Update/Tracking Select Actions, 116

User Menu, 110

Using the Consults Package with TIU, 38

View by Status (ST), 105, 108, 130, 131

web pages, 7

Windows, 61

Windows Quick Start, 59

Work Flow, 14