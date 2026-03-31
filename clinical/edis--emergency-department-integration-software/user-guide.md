---
consolidated_title: "emergency department integration software user guide"
app_code: EDIS
doc_type: UG
master_source: "Emergency Department Integration Software User Guide (file name contains _r)"
master_pub_date: April 2025
consolidated_from: 2 versions
prior_versions:
  - "Emergency Department Integration Software User Guide"
---

---
title: |
  <span id="_Toc495855387" class="anchor"></span>Emergency Department Integration Software (EDIS)

  User Guide
---

![](emergency-department-integration-software-user-guide-file-name-contains-r/001.png)

April 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

<table style="width:100%;">
<caption><p><span id="_Ref52792508" class="anchor"></span>Table 1: Reports with Possible Errors</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 13%" />
<col style="width: 47%" />
<col style="width: 22%" />
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
<td>4/2/2025</td>
<td>4.7</td>
<td><p>EDP*2.0*33</p>
<ul>
<li><blockquote>
<p>Section 9, Updated Waiting Room Display Board with new image and updated metrics described.</p>
</blockquote></li>
</ul></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>2/3/2025</td>
<td>4.6</td>
<td><p>EDP*2.0*31</p>
<ul>
<li><p>Replaced graphic for 7.3.4 Delay Summary Report.</p></li>
</ul></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>12/21/2023</td>
<td>4.5</td>
<td><p>EDP*2.0*28</p>
<ul>
<li><p>Updated version used in section <strong><u>2.2 Log In</u></strong></p></li>
</ul>
<p>Updated the Title page, Revision History, Table of Contents, List of Tables, List of Figures, and Footers</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>07/13/2023</td>
<td>4.4</td>
<td><p>EDP*2.0*24:</p>
<ul>
<li><p>Section 2.3 new EDIS Home Page image added</p></li>
<li><p>Added sub-section 2.3.2 “Restore”</p></li>
<li><p>Section 2.3.7.4 parameters added for Metrics Text, Footer Text, Updates Text</p></li>
<li><p>Section 4 Text removed "This view also allows a user to restore a patient to the board who was removed in error"</p></li>
<li><p>Section 8.2.2 added Admittance Delay</p></li>
<li><p>Section 8.4 Updated image of Parameters screen and added three new bulleted parameters</p></li>
<li><p>Added sub-sections for 8.4.10, 8.4.11, 8.4.12</p></li>
<li><blockquote>
<p>Section 9, added for Waiting Room Display Board with new image and text.</p>
</blockquote></li>
<li><blockquote>
<p>Updated the Title page, Revision History, Table of Contents, List of Tables, List of Figures, and Footers</p>
</blockquote></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>03/09/2023</td>
<td>4.3</td>
<td><p>EDP*2.0*20</p>
<p>Added to Section 2.2 Note referencing Log In</p>
<p>Added to Section 2.5.3.1 2<sup>nd</sup> Bullet "Check in Ms. Jones"</p>
<p>Added to Section 2.4 1<sup>st</sup> Bullet "when the patient is checked in"</p>
<p>Removed Note referencing parameter “EDPF SCHEDULING TRIGGER” in Section 2.4.</p>
<p>Removed the first paragraph reference to parameter “EDPF SCHEDULING TRIGGER” in Section 2.5.3.1.</p>
<ul>
<li><p>Updated the Title page, Revision History, Table of Contents, List of Tables, List of Figures, and Footers</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>07/25/2022</td>
<td>4.2</td>
<td><p>EDP*2.0*22:</p>
<p>Patient Demographics is now read-only.</p>
<ul>
<li><p>Removed “or update” from, <em>view or update patient demographic information</em> in section <strong><u>2.3.1.1</u></strong></p></li>
<li><p>Removed “or update” from, <em>view or update patient demographic information</em> in section <strong>3.3</strong></p></li>
<li><p>Removed “or update” and “or edited” from the title and body of section <strong><u>3.3.2</u></strong></p></li>
</ul>
<ul>
<li><p>Updated the Title page, Revision History, Table of Contents, List of Tables, List of Figures, and Footers</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>06/23/2021</td>
<td>4.1</td>
<td><p>EDP*2.0*15:</p>
<ul>
<li><p>Added Knowledge Base Numbers for PIV reference material in section <strong><u>0</u></strong>, <strong><u>Note: As of EDIS v2.2.47, the user</u> will no longer be able to</strong> routinely log in with their Access and Verify codes. The user will need to link their PIV card to their VistA instance.</p></li>
<li><p>PIV Reference Material from the Knowledge Bases</p></li>
<li><p>Added the <u>Note</u> in section 2.2</p></li>
<li><p>Removed the Access and Verify Codes Log In section</p></li>
<li><p>Updated the use of PIV credentials when logging in for section <strong><u>2.2</u></strong>, <strong><u>Log In</u></strong></p></li>
<li><p>Added the Display When and Inactive <strong><u>Note</u></strong> in section 8.1</p></li>
<li><p>Added the room and area single additional display <strong><u>Note</u></strong> in section 8.1</p></li>
<li><p>Added the Display When and Inactive <strong><u>Note</u></strong> in section 8.1.1</p></li>
<li><p>Added the room and area single additional display <strong><u>Note</u></strong> in section 8.1.1</p></li>
<li><p>Added the resizing column <strong><u>Note</u></strong> in section 8.2.2.5</p></li>
</ul>
<ul>
<li><p>Updated Title page, Revision History, Table of Contents, List of Tables, List of Figures, and Footers</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>12/21/2020</td>
<td>4.0</td>
<td><p>EDP*2.0*13:</p>
<ul>
<li><p>Document updated for EDIS GUI 2.2.41</p></li>
<li><p>Providers must assign themselves to patients</p></li>
<li><p>Document styles updated to current VA standards</p></li>
<li><p>Updated altering in the Active Patient Table on the CPE view</p></li>
<li><p>Removed ED Mental Health Patients report</p></li>
<li><p>Removed the Preventing Accidental Application Sign-outs section, since the preferred browser is Chrome</p></li>
</ul>
<ul>
<li><p>Updated Title Page, Revision History, Table of Contents, List of Tables, List of Figures, and Footers</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>November 2014</td>
<td>3.9</td>
<td><p>Patch EDP*2.0*2, EDIS GUI v2.1.2:</p>
<ul>
<li><p>Updated title page, headers, footers, and Index.</p></li>
<li><p>Deleted two paragraphs from Section 1.5 Application Timeouts as ORWOR TIMEOUT CHART and ORWOR TIMEOUT COUNTDOWN are no longer used.</p></li>
<li><p>Deleted Provider Report: Deleted mention of EDPR PROVIDER security key in Section 7, Reports View; Revised the Cross Reference Report paragraph in Section 7.1.2 to remove references to the Provider Report; Deleted Provider Report summary from p. 67; Deleted Figure 46 from Table of Figures and from p.68; Deleted reference to Provider Report from notation in Section 7.2.</p></li>
</ul>
<ul>
<li><p>Made formatting changes (added automatic Table of Contents, corrected all page numbers in Table of Figures, made section 3.3.1 label Heading 3, deleted extra section break in section 7.2, linked last 3 section footers to previous footers to correct page numbers 95-97).</p></li>
</ul></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>August 2014</td>
<td>3.8</td>
<td><p>Patch EDP*2*2, GUI 2.1.1-ICD-10</p>
<ul>
<li><p>Updated Document Version</p></li>
<li><p>Updated TOC</p></li>
<li><p>Updated to reference ICD-10 diagnosis entries (pp. 10, 43, 92)</p></li>
<li><p>Added information on new ICD-10 search function (p. 43)</p></li>
<li><p>Updated column headings for Standard Reports (p. 54)</p></li>
<li><p>Updated column headings for the Activity Report (p. 55)</p></li>
<li><p>New Activity Report screenshot (p. 56)</p></li>
<li><p>Updated column headings for the Delay Report (p. 57)</p></li>
<li><p>New screenshot for Delay Report (p. 58)</p></li>
<li><p>Updated column headings for ED Mental Health Patients Report (p. 59)</p></li>
<li><p>New screenshot for ED Mental Health Report (p. 60)</p></li>
<li><p>Updated ICD reference in Exposure Report (p. 60)</p></li>
<li><p>New screenshot for Exposure Report (p. 61)</p></li>
<li><p>Updated column headings for the VA Admissions Report (p. 65)</p></li>
</ul>
<p>New screenshot for VA Admissions Report (p. 66 )</p></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>07/17/2013</td>
<td>3.7</td>
<td>Update to change to HWS</td>
<td>ProdDev</td>
</tr>
<tr class="even">
<td>06/20/2013</td>
<td>3.6</td>
<td>Incorporate edits from Product Support</td>
<td>Product Development</td>
</tr>
<tr class="odd">
<td>06/20/2013</td>
<td>3.6</td>
<td>Technical and Grammatical Review. Update of Index and TOC</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>06/17/2013</td>
<td>3.5</td>
<td>Document review and addition of delay definitions</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>05/13/2013</td>
<td>3.4</td>
<td>Final edits prior to submission</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>05/09/2013</td>
<td>3.4</td>
<td>Review and edits</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>05/06/2013</td>
<td>3.4</td>
<td>Document review, add content and update screen shots for EDIS v2.1.1</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>02/19/2013</td>
<td>3.3</td>
<td>Updated URLs</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>01/03/2013</td>
<td>3.1</td>
<td>Addressed Product Support Feedback</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>12/19/2012</td>
<td>3.0</td>
<td>Added verbiage for 1.7</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>12/19/2012</td>
<td>3.0</td>
<td>Final review prior to submission</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>11/30/2012</td>
<td>2.9</td>
<td>Final review prior to submission</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>11/29/2012</td>
<td>2.9</td>
<td>Updated footer</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>10/22/2012</td>
<td>2.8</td>
<td>Made updates (incorporated edits from [T.S.])</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>10/14/2012</td>
<td>2.7</td>
<td>Updated links within document</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>09/25/12</td>
<td>2.6</td>
<td>Final review prior to submission</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>09/24/12</td>
<td>2.6</td>
<td>Review and edits</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>09/21/12</td>
<td>2.6</td>
<td>Document review and revision updates</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>09/06/12</td>
<td>2.5</td>
<td>Final review prior to submission</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>09/04/12</td>
<td>2.5</td>
<td>Document review and revision updates</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>09/04/12</td>
<td>2.5</td>
<td>Review &amp; Edits</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>08/22/12</td>
<td>2.4</td>
<td>Document review, content and screenshot updates</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>08/06/12</td>
<td>2.3</td>
<td>Peer review</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>06/28/12</td>
<td>2.2</td>
<td>Document review, content and screenshot updates</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>06/10/12</td>
<td>2.1</td>
<td>Document review and screenshot updates</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>05/17/12</td>
<td>2.0</td>
<td>Final Review prior to submission</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>05/15/12</td>
<td>2.0</td>
<td>Document revisions and Table of Contents updates</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>05/15/12</td>
<td>2.0</td>
<td>Review</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>05/08/12</td>
<td>0.9</td>
<td>Document revisions and history updates</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>02/29/12</td>
<td>0.8</td>
<td>Document content and figure updates</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>01/12/12</td>
<td>0.7</td>
<td>Final Review prior to submission</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>01/11/12</td>
<td>0.7</td>
<td>Technical Edits</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>01/07/12</td>
<td>0.6</td>
<td>Technical Review</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>01/06/12</td>
<td>0.6</td>
<td>Document review and edits</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>12/07/11</td>
<td>0.5</td>
<td>Document revisions</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>12/06/11</td>
<td>0.4</td>
<td>New content added to the document</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>12/02/11</td>
<td>0.3</td>
<td>Table updates and additional content added to the document</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>11/25/11</td>
<td>0.2</td>
<td>Reference place holders added to the document</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>11/07/11</td>
<td>0.1</td>
<td>Initial document review</td>
<td><mark>Redacted</mark></td>
</tr>
</tbody>
</table>

<span id="_Ref52792508" class="anchor"></span>Table 1: Reports with Possible Errors

Table of Contents

List of Tables

[Table 1: Reports with Possible Errors [38](#_Ref52792508)](#_Ref52792508)

List of Figures

# Product Description


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Product Description](#product-description)
  - [About this Guide](#about-this-guide)
  - [Accessibility](#accessibility)
  - [Role-based Access to Views](#role-based-access-to-views)
  - [Document Conventions](#document-conventions)
  - [Application Timeouts](#application-timeouts)
  - [Reporting EDIS Issues/Problems](#reporting-edis-issuesproblems)
  - [National Definitions](#national-definitions)
    - [Statuses](#statuses)
    - [Dispositions](#dispositions)
    - [Delay Reasons](#delay-reasons)
    - [Sources](#sources)
- [Getting Started](#getting-started)
  - [Launch EDIS](#launch-edis)
    - [Creating Desktop Shortcuts to EDIS](#creating-desktop-shortcuts-to-edis)
  - [Log In](#log-in)
    - [PIV Reference Material from the Knowledge Bases](#piv-reference-material-from-the-knowledge-bases)
    - [Changing User Verify Code](#changing-user-verify-code)
  - [EDIS Views](#edis-views)
    - [Clinical Practice Environment (CPE)](#clinical-practice-environment-cpe)
    - [Restore](#restore)
    - [Edit Closed](#edit-closed)
    - [Display Board](#display-board)
    - [Assign Staff](#assign-staff)
    - [Reports](#reports)
    - [Configure](#configure)
  - [Understanding EDIS and CPRS Interactions](#understanding-edis-and-cprs-interactions)
  - [Using EDIS with Appointment Manager](#using-edis-with-appointment-manager)
    - [Benefits of this Method](#benefits-of-this-method)
    - [Drawbacks of this Method](#drawbacks-of-this-method)
    - [Best Practice for Using EDIS with Appointment Manager](#best-practice-for-using-edis-with-appointment-manager)
    - [Unscheduled Appointments that cause Errors (in Appointment Manager)](#unscheduled-appointments-that-cause-errors-in-appointment-manager)
  - [Using EDIS with PCE](#using-edis-with-pce)
    - [Benefits of this Method](#benefits-of-this-method-1)
    - [Drawbacks of this Method](#drawbacks-of-this-method-1)
    - [PCE is Best Used with EDIS](#pce-is-best-used-with-edis)
    - [Why This is a Best Practice](#why-this-is-a-best-practice)
    - [Processes with PCE that Lead to Errors](#processes-with-pce-that-lead-to-errors)
  - [Notifications](#notifications)
    - [Patient-Selection Messages](#patient-selection-messages)
- [CPE View](#cpe-view)
  - [Create a PCE encounter in CPRS](#create-a-pce-encounter-in-cprs)
  - [Add Patients to EDIS from the CPE View](#add-patients-to-edis-from-the-cpe-view)
    - [Search for Patient in VistA](#search-for-patient-in-vista)
    - [Enter Name, Patient Is Not In VistA](#enter-name-patient-is-not-in-vista)
    - [Ambulance is Arriving, Patient Name Is Unknown](#ambulance-is-arriving-patient-name-is-unknown)
  - [Update Information in the Active Patients Table](#update-information-in-the-active-patients-table)
    - [Updating a Room or Bed](#updating-a-room-or-bed)
    - [View Patient Demographic Information](#view-patient-demographic-information)
    - [Change the Patient Status](#change-the-patient-status)
    - [Change the Acuity Level](#change-the-acuity-level)
    - [Assign or Remove a Provider](#assign-or-remove-a-provider)
    - [Add or Change a Nurse](#add-or-change-a-nurse)
    - [Entering Patient Complaint](#entering-patient-complaint)
    - [Entering Comments](#entering-comments)
    - [Entering Disposition](#entering-disposition)
    - [Add or Remove a Resident](#add-or-remove-a-resident)
  - [Visit Sub View](#visit-sub-view)
    - [Complaint](#complaint)
    - [Vitals](#vitals)
    - [Updated Vitals](#updated-vitals)
    - [Status/Responsibility](#statusresponsibility)
    - [Disposition](#disposition)
  - [Assess Sub View](#assess-sub-view)
    - [Labs](#labs)
    - [Active Problems](#active-problems)
    - [Active Medications](#active-medications)
  - [Remove Patients](#remove-patients)
    - [Remove Patients Entered in Error](#remove-patients-entered-in-error)
- [Edit Closed View](#edit-closed-view)
  - [Edit Patients](#edit-patients)
- [Display Board View](#display-board-view)
  - [Arrange Columns](#arrange-columns)
  - [Resize Columns](#resize-columns)
  - [Sort Columns](#sort-columns)
- [Assign Staff View](#assign-staff-view)
  - [Add Providers, Residents, and Nurses](#add-providers-residents-and-nurses)
  - [Remove Providers, Residents, and Nurses](#remove-providers-residents-and-nurses)
  - [Configure Colors for Providers, Residents, and Nurses](#configure-colors-for-providers-residents-and-nurses)
- [Reports View](#reports-view)
  - [Report Columns](#report-columns)
  - [Disposition Abbreviations](#disposition-abbreviations)
  - [Standard Reports](#standard-reports)
    - [Activity Report](#activity-report)
    - [Acuity Report](#acuity-report)
    - [Delay Report](#delay-report)
    - [Delay Summary Report](#delay-summary-report)
    - [Exposure Report](#exposure-report)
    - [Missed Opportunities Report](#missed-opportunities-report)
    - [Orders by Acuity](#orders-by-acuity)
    - [Patient Intake Report](#patient-intake-report)
    - [Shift Report](#shift-report)
    - [VA Admissions Report](#va-admissions-report)
  - [Non-Standard Report](#non-standard-report)
    - [Patient xRef Report](#patient-xref-report)
  - [Run and View Reports](#run-and-view-reports)
  - [Print Reports](#print-reports)
  - [Export Reports](#export-reports)
- [Configure View](#configure-view)
  - [Room / Areas Sub View](#room-areas-sub-view)
    - [Add Room/Bed](#add-roombed)
    - [Edit Room/Bed](#edit-roombed)
  - [Display Board Sub View](#display-board-sub-view)
    - [Add a New Display Board](#add-a-new-display-board)
    - [Columns](#columns)
    - [Save Display Board Configuration Changes](#save-display-board-configuration-changes)
  - [Colors Sub View](#colors-sub-view)
    - [Configure Colors for Status/Acuity, Status, Acuity, Urgency Lab, and Urgency Radiology](#configure-colors-for-statusacuity-status-acuity-urgency-lab-and-urgency-radiology)
    - [Configure Colors for Total Elapsed Minutes, Minutes at Location, Minutes for Lab Order, Minutes for Imaging Order, Minutes for Unverified Order](#configure-colors-for-total-elapsed-minutes-minutes-at-location-minutes-for-lab-order-minutes-for-imaging-order-minutes-for-unverified-order)
  - [Parameters Sub View](#parameters-sub-view)
    - [Show Residents on Entry Form](#show-residents-on-entry-form)
    - [Show Clinics on Entry Form](#show-clinics-on-entry-form)
    - [Diagnosis Is Required Before Removing a Patient](#diagnosis-is-required-before-removing-a-patient)
    - [Diagnosis Must be Coded as ICD](#diagnosis-must-be-coded-as-icd)
    - [Disposition is Required Before Removing Patient](#disposition-is-required-before-removing-patient)
    - [Require a Delay Reason](#require-a-delay-reason)
    - [Shift Parameters](#shift-parameters)
    - [Arriving Ambulance Room/Area is](#arriving-ambulance-roomarea-is)
    - [Default Room/Area is](#default-roomarea-is)
    - [Metrics Text for Waiting Room Display Board](#metrics-text-for-waiting-room-display-board)
    - [Footer Text for Waiting Room Display Board](#footer-text-for-waiting-room-display-board)
    - [Updates Text for Waiting Room Display Board](#updates-text-for-waiting-room-display-board)
    - [Save Parameters Selection](#save-parameters-selection)
  - [Selections Sub View](#selections-sub-view)
    - [Adding Status, Disposition, Delay Reason, and Source Selections](#adding-status-disposition-delay-reason-and-source-selections)
- [Waiting Room Display Board](#waiting-room-display-board)
The fundamental mission of Department of Veterans Affairs (VA), Office of Information & Technology (OIT), Emergency Department Integration Software (EDIS) Program Services is to provide Veterans the benefits they have earned throughout their military service to the United States. OIT accomplishes its mission by delivering high-quality, client-centered, effective and efficient Information Technology (IT) services to those responsible for providing care to the Veterans at the point-of-care as well as throughout all the points of the Veterans’ health care in an effective, timely and compassionate manner. VA depends on Information Management/Information Technology (IM/IT) systems to meet mission goals.
The Veterans Health Administration (VHA) Health Workflow System (HWS) initiative is a single initiative whose mission is to expand health care access for Veterans, including women and rural populations. Multiple programs and projects have been assigned as part of the HWS Initiative, including EDIS.
The system is an extension to Veterans Health Information Systems and Technology Architecture / Computerized Patient Record System (VistA/CPRS) for tracking and managing the delivery of care to patients in an Emergency Department (ED). Capabilities of the system include the recording and tracking of ED patients during incidents of care, displaying the current state of care delivery, and reports and data extracts on the delivery of care. The system can be configured to the specifics of different VHA emergency departments.

## About this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide walks through the process of performing the following tasks:

1.  Launch Emergency Department Integration Software (EDIS).
2.  Sign in patients using the VistA Scheduling package (also known as Appointment Manager) to make appointments for or check patients into the emergency department. EDIS will automatically add the patients to the Active Patients table.
3.  Enter Emergency Severity Index (ESI) values for triaged patients.
4.  Create emergency department encounters in the Computerized Patient Record System (CPRS) Patient Care Encounters (PCE) package (if not using Appointment Manager).
5.  Update patient information as patients progress through the emergency-care process
6.  View the display board.
7.  Enter patients’ dispositions in EDIS.
8.  Enter patients’ discharge diagnoses in EDIS and CPRS.
9.  Remove patients from the display board (this task incorporates disposing patients, which supports discharge and admit processes).
10. Make site and shift relevant staff assignments.
11. Edit visit-related information, including vital signs.
12. Create reports.
13. Configure the application using its graphical user interface (GUI) tools. All patient and provider information is fabricated information for testing purposes.

## Accessibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide supports the use of assistive reading devices. EDIS uses a graphical user interface (GUI) and this guide will include steps for accessing application functionality.

## Role-based Access to Views

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS provides role-based access to the specific functionality sets that are available through its views. If the application does not display in its main navigation page, one or more of the views this guide describes, a user’s current role may not be compatible with functionality that the views include. Please contact the information resource management (IRM) or clinical application coordinator (CAC) staff with questions about roles. Please see *Emergency Department Integration Software Technical Manual* for information about configuring role-based access to application functionality.

## Document Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Bold type indicates application elements such as views, panes, links, buttons, fields, text boxes, notes, column names, and key names. Key names appear in all CAPITAL LETTERS and within the confines of this user guide, the terms visit and encounter are synonymous.

## Application Timeouts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS uses parameter settings, EDP APP TIMEOUT and EDP APP COUNTDOWN, for application timeouts and timeout countdowns. IRM personnel enter values for these parameters at the site level. Emergency department managers usually do not determine them. For many sites, EDIS is set to time out after 15 minutes of inactivity.

EDIS displays its timeout message and countdown within the browser, at the bottom of the current EDIS view. Because screen readers cannot read this message, EDIS also sounds a chime as it begins its timeout countdown.

> **NOTE:** If users are simultaneously running CPRS and EDIS, an active CPRS window can obscure the EDIS timeout warning and countdown. Facilities may want to consider using separate screens for each application. This solution helps ensure that both applications are fully visible.

## Reporting EDIS Issues/Problems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All Emergency Department Integrated Software (EDIS) problems should be reported to the Enterprise Service Desk according to local policies.

The Enterprise Service Desk can be contacted by phone at 855-673-4357, teletype at 1-844-224-6186 or navigating to <https://yourit.va.gov/va> to submit a Service Now (SNOW) ticket.

> **NOTE:** The site can also enter its own SNOW ticket through the YourIT application. The ESD will forward the SNOW ticket to the appropriate EDIS support team for resolution. If the problem involves a Server issue, local or national, the ticket will be referred to the Austin Information Technology Center/Austin Automation Center (AITC) Service Desk. Once the AITC has resolved the issue/ticket, the SNOW ticket will be updated with the resolution information

## National Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDIS technical working group (TWG) offers the following definitions for the nationally released status, disposition, delay reason, and source selections that are provided with EDIS

### Statuses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Admitted: The patient is admitted but is still in the emergency department.
- ED Boarding \[Hold\]: The patient is admitted and is designated as a holder (extended time in the emergency department).
- Discharged: The patient is discharged but is still in the emergency department.
- ED Observation Unit: The patient is an observation patient under the emergency department's care.
- ED Patient: The patient is an emergency department patient (after triage).
- En Route/Prearrival: The patient is en route to the emergency department.
- Awaiting Triage: The patient is at the emergency department and is awaiting triage.

> **NOTE:** Statuses are site configurable.

### Dispositions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Admitted to VA Ward: The patient was admitted to an inpatient location, not including an ICU, telemetry, or psychiatric unit.
- AMA: The self-discharge of a patient from the ED against the advice of a Licensed Independent Provider (LIP) (signing a form is not required to be AMA).
- Sent to Urgent Care Clinic: The patient was discharged from the emergency department and referred to another evaluation clinic at the same site; some degree of triage is necessary to make this judgment.
- Deceased: The patient is dead.
- Eloped: A patient who arrives in the ED and has had, or is in the process of having, a medical screening evaluation by a LIP and leaves before treatment is completed without having a discussion with the LIP about the risks of leaving.
- Patient Name Entered in Error: The patient's name was entered in error; this disposition removes the patient from the board.
- Home: The patient was discharged to his or her previous living arrangement.
- Admitted to ICU: The patient was admitted to an inpatient critical care unit.
- Left Without Being Treated/Seen: A patient that is checked into the ED but leaves before being seen by a LIP (i.e. before having a medical screening evaluation by a LIP initiated).
- Sent to Nurse Eval / Drop-in Clinic: the patient was discharged from the emergency department and referred to another on-campus same-day evaluation clinic; some degree of triage is necessary to make this judgment.
- Admitted to Psychiatry: the patient was admitted to an inpatient psychiatric unit.
- Admitted to Telemetry: the patient was admitted to an inpatient telemetry unit.
- Transferred to a Non-VA Facility: the patient was discharged from the emergency department and sent to another, non-VA, facility.
- Transferred to VA Facility: the patient was discharged from the emergency department and sent to another VA facility.

> **NOTE:** Dispositions are site configurable.

### Delay Reasons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Obtain Accepting Physician: The delay was caused by the inability to find an accepting physician to admit the patient. This selection includes the elapsed time between determining the patient's need for admission and obtaining an accepting physician.
- Admit Physician Writing Dispo: The delay resulted from the physician's failure to write the patient’s admit or discharge order. This selection includes the elapsed time between when the patient was ready for his or her disposition and when the physician wrote the order to admit or discharge the patient.
- Admitting Physician Evaluation: The delay was related to the admitting physician's evaluation and confirmation of the patient's disposition. For this selection, delay time begins when the physician sees the patient and ends when:
  - H&P is done
  - Ancillary studies that are necessary for disposing the patient are done and resulted
  - The patient is ready to be disposed
- Patient Admitted to Observation: The delay resulted from the patient's admission to observation. This selection includes the elapsed time between when the patient was ready to be disposed and the time the physician wrote an order to admit the patient to 23 hours of emergency department or floor observation.
- Obtain Ambulance Services: The delay resulted from the time it took to obtain ambulance services. This selection includes the elapsed time between when emergency department staff requested ambulance services and the time the ambulance service arrived.
- Obtain Consultant: The delay resulted from an ordered consultation's lack of completion. This selection includes the elapsed time from when a physician ordered a consultation to the time the physician obtained the consultation.
- ED to Hospital Bed: The delay represents the difference between the time the patient was assigned a hospital bed and the time the patient was transported from the emergency department. For example, this delay could represent the time emergency department staff spent waiting for an escort, for a bed to be cleaned, for a nursing report, or for staffing.
- Obtain Escort: The delay resulted from the time it took to obtain an escort for the purpose of transporting the patient (not including transport to a hospital bed, use ED to Hospital Bed for this reason). This selection includes the time that elapsed between when the emergency department called an escort and the time the escort arrived to transport the patient to a clinic, radiology, or another ancillary department.
- Patient Transport Home: The delay resulted from an inability to find transportation for a discharged patient or from the time it took the identified source of transportation to arrive at the emergency department. This selection includes the elapsed time between when the patient was ready for discharge and the time the patient left the emergency department.
- Obtain Imaging Results: The delay resulted from time spent waiting to obtain imaging results. This selection includes the elapsed time between when the imaging study was completed and the time the study was resulted.
- Obtain Imaging Studies: The delay resulted from time spent waiting for imaging studies. This selection includes the elapsed time between when the physician ordered the imaging study and the time the study was done and ready for interpretation.
- Obtain Inpatient Bed: The delay resulted from the time spent waiting for an impatient bed assignment. This selection includes the elapsed time between when the physician wrote the admission order and the time bed control or the house supervisor assigned the patient to a bed. For example, the time an ICU patient waited for an ICU bed to become open.
- Interfacility Transfer: The delay was caused by an inability to transfer the patient to another facility in a timely manner.
- Obtain Lab Results: The delay was caused by the lack of a timely turnaround for laboratory tests. This selection includes the elapsed time between when labs were drawn or obtained and the time the labs were resulted.
- Obtain Lab Studies: The delay was caused by an inability to get labs drawn in a timely fashion. This selection includes the elapsed time between when the physician wrote the lab order and the time the lab test was drawn.
- On-call Staff: The delay was caused by an inability to contact on-call staff.
- Overcrowding of ED: The delay resulted from waiting for an emergency department bed to become available (includes hallway beds and beds that were unavailable because of staffing issues); no beds were available for inbound ambulances, including hallway beds.
- Obtain Drugs/Pharmacology: The delay was caused by an inability to get ordered drugs from the pharmacy. This selection includes the elapsed time between when the physician ordered the medications and the time the emergency department received the medications.
- ED Physician Limits: The delay resulted from time the physician spent seeing patients. This selection includes the elapsed time between when the patient was placed in a bed and when the physician saw the patient. For example, this reason for delay might apply if five patients presented with chest pains, all within 10 minutes.
- ED Staff Limits: The delay resulted from a failure to process the patient (see the patient or accomplish orders, for example) in a timely manner because of insufficient staffing. This selection includes the elapsed time between when the physician wrote an order (splint a broken ankle, for example) and the time the order was accomplished.
- Obtain Medical Supplies: The delay resulted from an inability to obtain medical supplies (splints, crutches, and c-line kits, for example) in a timely manner. This selection includes elapsed time from when emergency department personnel ordered the supplies (or identified the need for them) and the time the emergency department received the supplies.
- Arrange Emergency Surgery: The delay resulted from the time it took to get the patient (who needed surgery) to the operating room.
- Patient Transport Other: The delay resulted from the time it took to find transportation for the patient to a location other than home. This selection includes the elapsed time between when the patient was ready for transport to the time the patient left the emergency department.

### Sources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Non-referred
- On-site Clinic
- On-site Nursing Home
- VA Clinic, Off-site
- VA Nursing Home, Off-site
- Non-VA Clinic/Office
- Non-VA Nursing Home
- Transfer, Other

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Launch EDIS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS v2.2 should be accessible through a shortcut on the user’s desktop, a shared network folder, or on the CPRS Tools menu. Contact the IRM or CAC staff for assistance with shortcuts.

A Pre-Production version of EDIS is also available. Please contact IRM or CAC staff for assistance.

### Creating Desktop Shortcuts to EDIS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create desktop shortcuts to EDIS:

1.  Navigate to EDIS v2.2.
2.  Select the 3 vertical dots icon to the right of the Address bar.
3.  Go to the More tools menu.
4.  Select the Create shortcut… option.

<span id="_Toc196383164" class="anchor"></span>Figure 1: Internet Options in Google Chrome

![](emergency-department-integration-software-user-guide-file-name-contains-r/002.png)

5.  Enter a display name for the shortcut.
6.  Select Create.

## Log In

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When logging into EDIS, the application will prompt the user to use their PIV credentials. If a user’s PIV is associated with more than one site, a list of institutions will be displayed. Select the correct institution to proceed.

> **NOTE:** As of EDIS v2.2.47, the user will no longer be able to routinely log in with their Access and Verify codes. The user will need to link their PIV card to their VistA instance.

### PIV Reference Material from the Knowledge Bases

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For PIV assistance, refer to the following 2 Knowledge Base numbers:

KB0013359 - VistA: Link PIV Card to Vista/CPRS/CAPRI

[KB0013706](https://yourit.va.gov/kb_view.do?sysparm_article=KB0013706) - SSOi: Accessing Applications Using Windows Authentication

### Changing User Verify Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event that SSOi is down, EDIS may require Access and Verify codes to log in. If the user has an expired VistA verify code, it can be changed in CPRS or another VistA application. EDIS will then accept the change.

## EDIS Views

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Upon successfully logging in, the user will be presented with the EDIS Home Page.

<span id="_Toc196383165" class="anchor"></span>Figure 2: EDIS Home Page

![](emergency-department-integration-software-user-guide-file-name-contains-r/003.png)

> **NOTE:** In the event that a Default Waiting Room has not been assigned to EDIS, users will receive a warning popup message, indicating that new patients will be added to an area called EDIS_DEFAULT.

While users still will be able to log in and use EDIS normally, this situation should be resolved by asking the CAC or EDIS Coordinator to assign a default room in the Parameters sub view of the Configure view within EDIS (see section 8.4.9 Default Room/Area is).

> **NOTE:** Not all views are available to all users. EDIS offers site-configurable, role-based access to views. If a user does not have access to a view that they need, speak with the IRM or CAC staff responsible for role-based access at the site.

### Clinical Practice Environment (CPE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPE view allows users to add patients to the application but will need the provider to assign themselves to the patient to create a visit in CPRS. The CPE view contains the following sub views:

- Active Patients
- Visit
- Assess

#### Active Patients Sub View

The Active Patients sub view is a table that enables users to update or add a room or bed, view patient demographic information, enter a complaint in free-form text, change the acuity of a patient, assign or remove a provider, assign or remove a resident, assign or change a nurse, assign or change the status, assign or change the disposition, and enter comments in free-form text.

> **NOTE:** Only providers and residents can assign or remove themselves

#### Visit Sub View

The Visit sub view enables users to view, add, or change Complaints, Vitals, Status/Responsibilities or Dispositions.

> **NOTE:** Only providers and residents can assign or remove themselves

#### Assess Sub View

The Assess sub view enables users to view and print lab results, active problems, and active medications.

### Restore

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Restore view enables users to restore a patient to the board that was previously removed in error. This view allows users to search by patient name or date of visit.

### Edit Closed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit Closed view enables users to edit patients’ information after their emergency department visits have ended.

This view enables users to change a patient’s complaint, status/responsibility elements, and the patients’ dispositions and diagnoses. Diagnoses shall be entered in the form of International Classification of Diseases, Tenth Revision, Clinical Modifications (ICD-10-CM) or free-text, if the EDIS parameter is set to allow free-text entries for diagnosis. If patients’ stays have exceeded the national emergency department visit limit (currently six hours), the application may require users to select a reason for delay. If it does, this view will include a list of reasons from which can be chosen.

### Display Board

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Display Board view is a PC-based version of the site’s main electronic whiteboard (big-board) display. Multiple big-board displays can be configured for the site. However, only the site’s main display board can be viewed using the PC-based Display Board view.

### Assign Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Assign Staff view enables users to create site-specific staff-selection lists. This view can also be used to assign color indicators for individual staff members.

### Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Reports view enables users to run, view, and print EDIS reports. The PatientxRef report contains personal information and requires security-key access.

### Configure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Configure view lets authorized users configure the application to include locally meaningful pick lists and create customized electronic whiteboard displays. It contains the following sub views:

- Room / Areas
- Display Board
- Colors
- Parameters
- Selections

#### Room / Areas Sub View

The Room / Areas sub view enables users to add a room or bed, edit a room or bed, or assign a color to a room or bed.

#### Display Board Sub View

The Display Board sub view enables users to add a new display board and edit display boards.

#### Colors Sub View

The Colors sub view enables users to configure colors for status and acuity values, urgency lab values, urgency radiology values, total elapsed minutes, minutes at location, minutes for lab order, minutes for imaging order, and minutes for unverified orders.

#### Parameters Sub View

The Parameters sub view enables users to set the following parameters:

- Include residents on entry form.
- Require a diagnosis.
- Require ICD-10-CM or free-text diagnoses.
- Require disposition to remove patient.
- Require a reason for delay.
- Configure shift parameters.
- Set a default room or area for patients arriving by ambulance.
- Set a default room or area.
- Metrics Text for Waiting Room Display Board
- Footer Text for Waiting Room Display Board
- Updates Text for Waiting Room Display Board

#### Selections Sub View

The Selections sub view enables users to add locally meaningful selections to the preset lists within EDIS. Selections can be adding to statuses, dispositions, delay reasons, and sources.

## Understanding EDIS and CPRS Interactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users can successfully integrate CPRS with EDIS in one of two ways:

- Create an unscheduled appointment in Appointment Manager; when the patient is checked in to a clinic location the site has specified in the EDPF LOCATION parameter, EDIS adds the patient to the EDIS Active Patients list.
- Add a patient to the application then have the provider assign themselves to the patient for an encounter to be created through EDIS, using Patient Care Encounter (PCE).

Each method has strengths and weaknesses. As is the case for any patient-scheduling system, less-than-optimal practices can lead to duplicated encounters. Sections 2.5 Using EDIS with Appointment Manager and 2.6 Using EDIS with PCE provide information that may help users choose the method that’s best for the user’s location. Please read these two sections carefully.

## Using EDIS with Appointment Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Benefits of this Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The site maintains the advantage of having a selectable list of triaged emergency department patients available on the CPRS Patient Selection view.

This list of scheduled (that is, Appointment Manager-created) appointments is not available via the PCE method.

### Drawbacks of this Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Successful CPRS and EDIS integration using this method requires intensive (recommended twenty-four-hours a day, seven days a week) secretarial and administrative support. For this method to work, the site must create an appointment for each emergency department patient before doing anything else, which requires round-the-clock support of administrative staff who have access to Appointment Management.

### Best Practice for Using EDIS with Appointment Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Add Patients to Appointment Management First:

When a patient presents to the emergency department for evaluation, a member of the site’s administrative staff immediately creates an appointment for the patient in Appointment Manager. A patient is added to the board at CHECK IN. This creates a selectable visit in CPRS and adds the patient to EDIS. The triage nurse must subsequently add additional data to EDIS.

Example:

- Ms. Jones arrives at 11:30.
- At 11:32, a member of the ED staff uses Appointment Manager to create an appointment and check in Ms. Jones.
- EDIS automatically displays Ms. Jones in the Active Patients table.
- The triage nurse sees Ms. Jones at 11:35 and completes her EDIS triage information; the nurse then opens CPRS and writes a triage note under the visit in CPRS that corresponds to Ms. Jones’s emergency department appointment.
- The emergency department provider selects this same encounter in CPRS when he or she writes notes or orders related to Ms. Jones’s emergency department care.

#### Why This Is a Best Practice

CPRS was created long before EDIS. It has not been changed to recognize that EDIS exists.

### Unscheduled Appointments that cause Errors (in Appointment Manager)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following list contains things users should not do. This section was included to help users troubleshoot problems that can occur when the site uses EDIS with unscheduled appointments in Appointment Manager.

#### Creating unscheduled appoints just before the midnight hour

Appointments will disappear at midnight for patients who have unscheduled appointments for times that precede the midnight hour and for whom emergency department personnel have completed neither documentation nor orders before midnight. When this occurs, the site must reenter the vanished appointments, thus creating both second appointments and duplicate PCE encounters. This problem is the result of CPRS business logic which exists outside of EDIS.

#### Failing to select the proper appointment when writing notes or ordering tests

Providers and nurses create duplicate PCE encounters if they fail to select the proper appointment in CPRS when writing notes or ordering tests.

#### Writing notes or orders before creating unscheduled appointments

Providers and nurses create duplicate PCE encounters when they write orders or notes before ED staff have created unscheduled appointments for their patients.

## Using EDIS with PCE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Benefits of this Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Integrating EDIS with CPRS via the Patient Care Encounter (PCE) does not require intensive (recommended round-the-clock) support from personnel who have access to Appointment Manager.

### Drawbacks of this Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites that switch from using Appointment Manager to PCE, will impact their users, because they no longer have a list on their Patient Selection (initial) view of CPRS from which they can select patients who have emergency department appointments. This list of scheduled (that is, Appointment Manager-created) appointments only appears when sites use the Appointment Manager method. As a result of not having this list, looking up patients who were discharged in the past (days or weeks ago) is a little more difficult in CPRS. However, authorized users can easily look up these patients in the EDIS Edit Closed view.

### PCE is Best Used with EDIS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Place Patient on EDIS First with Provider Name:

When a patient is sent to the emergency department for evaluation, someone notifies the triage nurse and adds the patient to EDIS. The attending provider must assign himself or herself to the patient in EDIS. Assigning a provider in EDIS creates an unscheduled encounter in CPRS. Providers and nurses can subsequently write notes and orders under this encounter.

Although assigning a nurse in EDIS can also generate an encounter in CPRS, it doesn’t always. Nurse assignments generate selectable encounters in CPRS only if the hospital configures nurses with an active person class in the VistA New Person file. Some sites do not allow this practice. In addition, using nursing assignments to create PCE encounters makes nurses primary providers in EDIS-generated encounters. Primary providers must change these placeholder assignments for encounters other than nursing-only encounters. To do this, primary providers should select Yes when CPRS prompts them to identify themselves as primary providers for encounters they are signing.

Example 1:

- At 11:31, a member of the administrative staff or a triage nurse adds Mr. Jones to EDIS and Dr. Smith assigns himself or herself as Mr. Jones’s provider.
- This creates an 11:31 encounter for Mr. Jones in CPRS.
- The triage nurse opens CPRS, enters Mr. Jones’s chart, starts note, and selects the emergency department encounter that already appears in CPRS.
- The triage nurse writes and signs the note.
- Mr. Jones’s provider writes a note or orders, also selecting the encounter that EDIS already created in CPRS.

In this example, if the initially assigned provider is not the primary provider for the encounter, the primary provider must select himself or herself when he or she signs the note. The primary provider must also assign himself or herself in EDIS.

Example 2:

- At 11:31, an LPN adds Mr. Jones to EDIS.
- Mr. Jones’s triage nurse has an active person class in the VistA New Person file and opens a PCE encounter for Mr. Jones’s visit in CPRS as a provider.
- A provider sees Mr. Jones; the provider adds his or her name in EDIS.
- When the provider is signing the encounter in CPRS, the provider identifies himself or herself as the primary provider for the encounter.

If no primary provider had seen Mr. Jones (if he had left without being seen, for example) the triage nurse would close the encounter in CPRS with a disposition of Nurse-only visit.

### Why This is a Best Practice

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS was created long before EDIS and has not been updated to recognize EDIS. The PCE system is limited and cannot create encounters unless a primary provider enters himself or herself as a provider or enters diagnoses for the encounters. If users add patients to EDIS without having the primary provider assign himself or herself as the primary provider or set a diagnoses, EDIS cannot give to CPRS the information that CPRS must supply to the PCE application, and PCE cannot create the encounters. This is a limitation of the PCE application, not a limitation of EDIS. The best practice is to have the primary provider assign himself or herself immediately after the user adds a patient to EDIS because diagnoses are rarely available early in the patient-care process.

> **NOTE:** When patients present before midnight, but providers do not treat them until after midnight, the providers must be certain to select the EDIS-created visit from the preceding day, as opposed to opening new (duplicate) visits.

### Processes with PCE that Lead to Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following list contains things users should not do. We have included this section to help users troubleshoot problems that can occur when the site uses EDIS with the PCE system.

#### Failing to select a provider when adding a patient to EDIS

When a provider fails to assign himself or herself, EDIS cannot create an encounter in CPRS.

#### Failing to add a patient upon his or her arrival

Duplicate encounters will result if users fail to add patients to EDIS and have the provider assign himself or herself before clinicians have started writing notes or orders.

#### Failing to select the EDIS-created visit when starting notes or writing orders

Duplicate encounters will result if nurses and providers fail to select the encounter EDIS creates when they start notes or create orders.

#### Continuing to use Appointment Manager for some patients

Implementing two separate process flows can confuse staff and lead to errors.

## Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Patient-Selection Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When users select patients, who are already registered in the local VistA system, EDIS may display one or more of the following messages:

#### Restricted Record Warning

This message appears when users select a patient whose records contain sensitive information. Only authorized users may view these records.

#### Patient Record Flags 

EDIS displays advisory messages when users add patients whose records are flagged in VistA. Users can view patient record flags after users have added patients by selecting the Flag option. Flag icons appear on the Patient Information bar, the green panel containing patient information, when users select patients.

When users select the Flag option, EDIS displays important information to help users and other clinical staff better care for patients whose behavior or medical conditions warrant special attention. The application displays patient-record flags in the Active Flag window.

<span id="_bookmark42" class="anchor"></span>Figure 3: Flag Icon on the Patient Information Bar

![](emergency-department-integration-software-user-guide-file-name-contains-r/004.png)

<span id="_Toc196383167" class="anchor"></span>Figure 4: Active Flag Window

![](emergency-department-integration-software-user-guide-file-name-contains-r/005.png)

#### Duplicate Selection

EDIS displays an advisory when users attempt to add patients who are already active in the application.

<span id="_Toc196383168" class="anchor"></span>Figure 5: Duplicate Selection Notification

![](emergency-department-integration-software-user-guide-file-name-contains-r/006.png)

#### Multiple Patient Icon

The application alerts users to the possibility of confusing patients’ identities by displaying an icon when two or more patients share the same last name or at least two consecutive ending digits of their social security numbers.

<span id="_Toc196383169" class="anchor"></span>Figure 6: Duplicate Selection Icon on Board

![](emergency-department-integration-software-user-guide-file-name-contains-r/007.png)

# CPE View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS automatically adds patients when users use the VistA Scheduling (Appointment Manager) package to create an emergency department appointment for patients. Utilizing Appointment Manager is the preferred way to enter new patients into EDIS.

The EDPF LOCATION parameter, which holds the site’s emergency department location or locations, controls this functionality. Parameter settings ensure that only emergency department check-ins and appointments add patients to EDIS.

From the CPE view, users can create an encounter in CPRS and add patients to the application after the provider assigns himself or herself.

## Create a PCE encounter in CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a provider (or a nurse who has an active person class in the New Person file) assigns himself or herself to a patient, EDIS automatically creates a PCE encounter in CPRS. This will happen unless EDIS has already created an encounter for this particular emergency department episode of care (through Appointment Manager, for example) or the provider does not have an active person class in the VistA New Person file. To reduce the possibility of creating duplicate PCE encounters in CPRS, EDIS checks back one hour for PCE encounter entries associated with the emergency department location the site’s IT staff has specified.

> **NOTE:** EDPF LOCATION parameter settings and, if applicable, Clinic list selections determine the location EDIS uses to create encounters.

The application creates only one PCE encounter in CPRS for each emergency department episode of care (or encounter). Users can avoid creating duplicate encounters for the same episode of care by selecting the encounter that EDIS creates when users’ complete patients’ emergency department encounters in CPRS.

## Add Patients to EDIS from the CPE View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Navigate to the CPE view. The Active Patients table will be displayed.

<span id="_Toc196383170" class="anchor"></span>Figure 7: New Patient Option

![](emergency-department-integration-software-user-guide-file-name-contains-r/008.png)

Select + New Patient in the upper right corner above the table. The application displays the New Patient pane, which offers the following three selections:

1.  Search for Patient in VistA: Enables a user to add patients who are already in the local VistA system.
2.  Enter Name, Patient Is Not in VistA: Enables a user to add patients who are not in the local VistA system (EDIS does not create PCE visits for these patients until someone adds them via a VistA search).
3.  Ambulance Is Arriving, Patient Name Is Unknown: Enables a user to add information for patients whose identities are unknown (EDIS does not create PCE visits for these patients until someone adds them via a VistA search).

### Search for Patient in VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To search for a patient in VistA:

1.  If necessary, then select the Search for Patient in VistA option (this is the application's default selection; in most cases, a user won’t need to manually select this option).
2.  Search for a patient in the Patient Name field using the following formats:

> **NOTE:** Use an underscore to denote spaces in names. For example, if the patient’s name is O Hara, enter O_Hara.

1.  Last name,First name (no spaces)
2.  Last name
3.  Last name and the beginning letter of the first name
4.  Last four digits of a Social Security number (SSN)
5.  Beginning letter of a last name followed by the last four digits of their SSN (X9999)
6.  Entire SSN (999999999)
3.  Select Search. The application lists possible matches.
4.  Choose a patient and select Continue. If the patient isn't already on the board, then the application displays the Visit sub view.

### Enter Name, Patient Is Not In VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add a patient that is not in VistA:

1.  From the New Patient pane, select Enter Name, Patient Is Not in VistA (If the Search for Patient in VistA option was used first, then EDIS automatically populates the Patient Name field with the name entered to initiate the VistA search).
2.  Enter the patient's full name, if applicable, in the Patient Name field using the format, Last name,First name (no spaces).
3.  Select Continue. The application displays the Visit sub view.

#### Adding Unidentified Patients

When a user must add unresponsive patients whose identities the user does not know, use the Enter Name, Patient Is Not in VistA selection and follow the naming protocol defined in section 3, NONTYPICAL PERSONS, of Appendix A, of the VHA Directive 1906, Data Quality Requirements for Health Care Identity Management and Master Person Index Functions.

Use the name UU-UNRESPONSIVE, PATIENT for the first such patient, UU-UNRESPONSIVE, PATIENT A for the second, UU-UNRESPONSIVE, PATIENT B for the third, and so forth. Users can navigate to [VHA Directive 1906](https://www.va.gov/vhapublications/ViewPublication.asp?pub_ID=8787) to find the full text of this directive.

### Ambulance is Arriving, Patient Name Is Unknown

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS enables a user to add unknown patients who are arriving by ambulance or other types of emergency transportation, thereby allowing the user to make room, provider (which must be performed by the provider), and nurse assignments before these patients arrive.

> **NOTE:** EDIS reports do not reflect the number of patients that users add to the application via this method. EDIS creates its Time In timestamps when users identify patients in VistA or create unscheduled appointments for them in Appointment Management. As a result, sites must correct EDIS's Time In values to reflect actual arrival times.

To add a patient that is arriving by emergency transportation:

1.  From the New Patient pane, select Ambulance Is Arriving, Patient Name Is Unknown. The name will display as ambulance en route.

> **NOTE:** Use the Identify Patient option in the Visit sub view to provide patient details later.

2.  Select Continue. The application displays the Visit sub view.

## Update Information in the Active Patients Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Navigate to the CPE view. The Active Patients table will be displayed.

Information can be updated in a few ways:

- Selecting a patient in the Patient column of the table, then selecting the icon to the left of the Patient option above the top left corner of the table. This will split the screen to include the Active Patients table and the Visit sub view

> **NOTE:** Double selecting a patient in the Patient column will also trigger the split-screen.

<span id="_Toc196383171" class="anchor"></span>Figure 8: Split-Screen Icon

![](emergency-department-integration-software-user-guide-file-name-contains-r/009.png)

- Selecting a patient in the Patient column of the table, then selecting the Patient option above the top left corner of the table. This will direct the user to the full-screen Visit sub view.
- Selecting individual cells within the Active Patients table. A description for updating cells directly from the table is outlined below.

From the Active Patients table, select a cell under one of the column headers to perform the following functions:

> **NOTE:** The header text is configurable and may be different for certain sites and selections may take a moment or two.

- Room: to update or add a room or bed
- Patient (exclamation icon): to view patient demographic information
- Complaint: to enter a complaint in free-form text
- Acuity: to change the Acuity of a patient
- Prv: to assign or change a provider (only providers can update this cell)
- Res: to assign or change a resident (only residents can update this cell)
- RN: to assign or change a nurse (If the selection doesn't have initials in their \#200 file entry, then the cell will appear blank)
- Status: to assign or change the status
- Disposition: to assign or change the disposition
- Comment: to enter comments in free-form text

> **NOTE:** A check mark in the Visit column lets the user know that a visit has been created in PCE.

### Updating a Room or Bed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To update a room or bed:

1.  In the Room column, select the patient cell to be viewed or edited. The application displays the Bed for pop-up.
2.  Select a room.

### View Patient Demographic Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To view patient demographic information:

1.  In the Patient column, go to the cell to be viewed (the user may need to resize the column to select the Exclamation icon).

<span id="_Toc196383172" class="anchor"></span>Figure 9: CPE Patient Demographics Icon

![](emergency-department-integration-software-user-guide-file-name-contains-r/010.png)

2.  Select the gray Exclamation icon next to the patient's name. The application displays the Patient Demographics pop-up.
3.  View the patient’s information.

### Change the Patient Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To change a patient’s status:

1.  In the Status column, select the cell to be viewed or edited. The application displays the Status for pop-up.
2.  Select a status (see section 1.7.1 Statuses for national status descriptions).

### Change the Acuity Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To change an acuity:

1.  In the Acuity column, select the cell to be viewed or edited. The application displays the Acuity for EDIS pop-up.
2.  Select an acuity level.

> **NOTE:** EDIS supports the Emergency Severity Index (ESI) triage algorithm, which ranks a patient's acuity using the numbers 1 (most urgent) through 5 (least urgent). Visit the [Agency for Healthcare Research and Quality](https://www.ahrq.gov/professionals/systems/hospital/esi/index.html) web site for more information.

### Assign or Remove a Provider

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To assign or remove a provider:

> **NOTE:** Only providers can assign or remove themselves

In the Prv column, select the cell to be viewed or edited.

Two options could be presented, currently assigned as provider or not.

1.  If currently assigned as provider, select Remove to no longer be assigned or Cancel to close without saving.
2.  If not currently assigned as provider, select Assign to become the assigned provider or Cancel to close without saving.

> **NOTE:** Providers in this list, are defined in the Provider Configuration in Section, 6, Assign Staff View.

### Add or Change a Nurse

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add or change a nurse:

1.  In the RN column, select the cell to be viewed or edited. The application displays the Nurse for EDIS pop-up.
2.  Select a nurse.

> **NOTE:** the nurse selection is defined by the Nurse Configuration in Section, 6, Assign Staff View.

### Entering Patient Complaint

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To enter or update a complaint:

1.  In the Complaint column, select the cell to be viewed or edited. The application displays the Complaint for pop-up.
2.  Enter a complaint.
3.  Select Ok to accept the changes or select Cancel to return to the active patients table without saving.

### Entering Comments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To enter a comment:

1.  In the Comment column, select the cell to be viewed or edited. The application displays the Comment for pop-up.
2.  Enter a comment.
3.  Select Ok to accept the changes or select Cancel to close the window without saving.

### Entering Disposition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To enter a disposition:

1.  In the Disposition column, select the cell to be viewed or edited. The application displays the Disposition for pop-up.
2.  Select a disposition (see section 1.7.2Dispositions for national disposition descriptions).

### Add or Remove a Resident

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To assign or remove a resident:

> **NOTE:** Only residents can assign or remove themselves

In the Res column, select the cell to be viewed or edited.

Two options could be presented, currently assigned as resident or not.

1.  If currently assigned as resident, select Remove to no longer be assigned or Cancel to close without saving.
2.  If not currently assigned as resident, select Assign to become the assigned resident or Cancel to close without saving.

> **NOTE:** the resident selection is defined by the Resident Configuration in Section, 6, Assign Staff View.

## Visit Sub View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Navigate to the CPE view by selecting CPE. The Active Patients table will be displayed.

To enter and edit the Visit sub view:

1.  Select a patient from the Patient column in the Active Patients table (or add a patient with the + New Patient option above the top right corner of the table).
2.  Select the Patient option in the top left corner above the table. The Visit sub view will be displayed.

<span id="_Toc196383173" class="anchor"></span>Figure 10: Patient Option

![](emergency-department-integration-software-user-guide-file-name-contains-r/011.png)

3.  View or update the available information for the following sections (select each section to collapse or expand the drop-down menus):
    1.  Complaint
    2.  Vitals
    3.  Update Vitals
    4.  Status/Responsibility
    5.  DispositionNote: Details for section contents will be in the subsequent subheadings.
4.  Select Save to save the changes or select Cancel to close the Visit sub view without saving the changes.
    1.  Users can also select Save & Remove from board to remove a patient from the display board (see Section 3.6, Remove Patients, for more details).
5.  Return to the Active Patients table by selecting Board icon at the top left.

<span id="_Toc196383174" class="anchor"></span>Figure 11: Board Icon

![](emergency-department-integration-software-user-guide-file-name-contains-r/012.png)

### Complaint

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Complaint drop-down menu enables users to:

- Select a source (see section 1.7.4 Sources for national source descriptions).
- Enter a Long Complaint (optional), to provide supplementary information about the patient's display-board complaint.
- Enter a Complaint for Display Board.

### Vitals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vitals drop-down menu enables users to load and print information for vitals that have been saved using the Updated Vitals section.

### Updated Vitals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Updated Vitals drop-down menu enables users to save the following information for vitals:

- BP: Blood pressure
- T(f): Temperature in Fahrenheit
- P: Pulse
- RR: Respiratory Rate
- Ht (in): Height in inches
- Wt (lbs): Weight in pounds
- Pain Severity

### Status/Responsibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Status/Responsibility drop-down menu enables users to:

Select a Room / Area assignment (This information is mandatory; the waiting room is the application's default selection).

Select an Acuity value (This information is mandatory).

> **NOTE:** EDIS supports the Emergency Severity Index (ESI) triage algorithm, which ranks a patient's acuity using the numbers 1 (most urgent) through 5 (least urgent). Visit the [Agency for Healthcare Research and Quality](https://www.ahrq.gov/professionals/systems/hospital/esi/index.html) web site for more information.

Select a Status (see Section 1.7.1, Statuses, for national status descriptions), Provider, Resident, Clinic, and Nurse.

> **NOTE:** When a provider is assigned in EDIS, the application automatically creates a Patient Care Encounter (PCE) visit in CPRS, if it hasn't already done so. EDIS does not create visits when the assigned provider does not have an active person class in VistA. EDIS does not create visits for patients the user added using the Enter Name, Patient Is Not in VistA, Ambulance Is Arriving, and Patient Name Is Unknown selections. EDIS does not create visits when the user only enters resident or nurse assignments; However, EDIS does create visits in CPRS for nurse assignments if the nurses in question are listed in the VistA Provider file.

> **NOTE:** EDIS does not register patients.

### Disposition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Disposition drop-down menu enables users to:

- Enter Comments.
- Select a disposition (see Section 1.7.2, Dispositions, for national disposition descriptions).

> **NOTE:** Depending upon the site's configuration, the application may require a disposition before allowing users to remove a patient from the display board.

> **NOTE:** Sites can activate and inactivate these dispositions. The application allows the site to configure additional, site-specific dispositions.

- Select a Delay Reason. This list is only available under the following concurrent conditions:
  - A site requires a delay reason (see Section 1.7.3, Delay Reasons, for national delay reason descriptions).
  - The patient's stay has exceeded the site-determined limit.
  - The patient is not in an observation ward.

> **NOTE:** If the site requires a reason for delay and the patient’s stay has exceeded the site's maximum number of minutes, then the application will require a user to enter a delay reason before it allows the user to remove the patient from the display board.

- Select a Diagnosis Code (or enter a free-text diagnosis if the site allows it).

> **NOTE:** For the ability to use a free-text diagnosis make sure that the parameter option, Diagnosis must be coded as ICD, is unchecked when configuring the parameters for Section 8.4 Parameters Sub View.

Enter the direct code, key words, abbreviations, or partial spellings into the search box.

- Select Search.
- Select a diagnosis from the list
- Select the Add option to the right of the list. The diagnosis should populate into the Selected Diagnosis table to the right.
- Select the Set as Primary Diagnosis option, if applicable.

> **NOTE:** Saving an ICD-10-CM diagnosis in EDIS adds the diagnosis to the patient's emergency department visit in CPRS. If EDIS hasn't already created a PCE visit for this patient, then it will also create a visit at this time. The application does not add free-text diagnoses to the patient's visit in CPRS.

- To remove a diagnosis from the Selected Diagnosis table
  - Select a diagnosis to be removed from the Selected Diagnosis table.
  - Select the Remove option to the left.

> **NOTE:** To capture admission-delay times for reporting, a user must change a patient's status to Admitted and then immediately select Admitted to VA Ward as their disposition. Unless the intention is to remove the patient from the board, select Save. Do not select Save & Remove from Board, which will prematurely remove the patient from the EDIS tracking application.

## Assess Sub View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Assess sub view enables users to Load and Print patient information from the Labs, Active Problems, and Active Medications drop-down menus.

Navigate to the CPE view by selecting CPE. The Active Patients table will be displayed.

To enter the Assess sub view:

1.  Select a patient from the Active Patients table.
2.  Select the Patient option in the top left corner above the table. The Visit sub view is displayed.
3.  Select the Assess option underneath the list of views at the top.

<span id="_Toc196383175" class="anchor"></span>Figure 12: Assess Sub View Option

![](emergency-department-integration-software-user-guide-file-name-contains-r/013.png)

4.  From here users can Load and Print patient information from the Labs, Active Problems, and Active Medications drop-down menus. Select each section to collapse or expand the menus.

### Labs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To load and print the Labs section:

1.  If necessary, expand the Labs section.
2.  Select the Load option to view patient lab data.

> **NOTE:** The labs will be returned up to 6 weeks prior to the current date.

3.  Select the Print option to print the information in the table.

### Active Problems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To load and print the Active Problems section:

1.  If necessary, expand the Active Problems section.
2.  Select the Load option to view patient data.
3.  Select the Print to print the information in the table.

### Active Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To load and print the Active Medications section:

1.  If necessary, expand the Active Medications section.
2.  Select the Load option to view patient data.
3.  Select the Print option to print the information in the table.

## Remove Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To remove patients:

Use the Save & Remove from Board option to save changes and remove patients from the display board.

This option is available only after users have entered a clinic and all disposition information required by the user's site. If a user hasn't entered a provider, a complaint, and acuity, the application alerts them to do so before it allows them to save the changes and remove the patient from the board. This happens unless the patient’s disposition is one of the following:

- Patient Name Entered in Error
- Left Without Being Treated / Seen
- Sent to Nurse Eval / Drop In Clinic

Selecting the Save & Remove from Board option removes patients from the display board and saves previously unsaved changes. While the application retains information about the visits of patients that have been removed from the display board, only users who have access to the Edit Closed view will have direct access to this information. Users who have access to the Reports view will have indirect access to this information.

### Remove Patients Entered in Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To remove patients entered in error:

1.  Open the Disposition list in the Visit sub view.
2.  Select Patient Name Entered in Error.

Select Save & Remove from Board.

# Edit Closed View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This view enables authorized users to edit the EDIS records of patients who are no longer on the display board. EDIS logs all changes for subsequent reference (as it does with changes users make while patients are still signed into the emergency department).

Navigate to the Edit Closed view by selecting Edit Closed. The Patient Name orDate search field is displayed.

> **NOTE:** To access the Edit Closed view, the \[EDPF TRACKING VIEW EDIT CLOSED\] Option is needed.

<span id="_Toc196383176" class="anchor"></span>Figure 13: Edit Closed View

![](emergency-department-integration-software-user-guide-file-name-contains-r/014.png)

## Edit Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To edit patients:

1.  In the Patient Name or Date field, enter one of the following
    1.  Last name,First name (no spaces)
    2.  Last name
    3.  Last name and the beginning letter of the first name
    4.  Beginning letter of a last name followed by the last four digits of their SSN (X9999)
    5.  Entire SSN (999999999)
    6.  A date (mm/dd/yy)
    7.  The word today (for a list of today’s visits)
    8.  t-n (where t represents today, and n represents the number of days prior to today)
2.  Select Search. EDIS lists matches in the table.
3.  Select a patient. The Edit Closed pane displays on the right side of the screen. Select Complaint, EC Status/Responsibility, or EC Disposition to collapse or expand each drop-down menu respectively.

> **NOTE:** Use Identify Patient... if the patient has yet to be identified.

4.  Add or update data-entry fields in the Edit Closed pane as necessary. A user can add information to or update the following fields:
    1.  Complaint drop-down menu:
        1.  Complaint for Display Board
        2.  Long Complaint (optional)
        3.  Source (see Section 1.7.4, Sources, for national source descriptions)
    2.  EC Status/Responsibility drop-down menu:
        1.  Room / Area
        2.  Acuity
        3.  Status (see Section 1.7.1, Statuses, for national status descriptions)
        4.  Provider
        5.  Resident
        6.  Clinic
        7.  Nurse
    3.  EC Disposition drop-down menu:
        1.  Comments
        2.  Disposition (see Section 1.7.2, Dispositions, for national disposition descriptions)
        3.  Delay Reason
        4.  Time In
        5.  Time Out
        6.  Diagnosis CodeNote: Use the Time In or Time Out calendar icons to adjust the date and time.

<span id="_Toc196383177" class="anchor"></span>Figure 14: Calendar icons

![](emergency-department-integration-software-user-guide-file-name-contains-r/015.png)

5.  Select Save to save the changes or Cancel to close the Edit Closed pane without saving.

# Display Board View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Navigate to the Display Board view by selecting Display Board. The workstation-based preview of the site's main electronic whiteboard will be displayed.

<span id="_Toc196383178" class="anchor"></span>Figure 15: Display Board View

![](emergency-department-integration-software-user-guide-file-name-contains-r/016.png)

> **NOTE:** To access the Display Board view, the \[EDPF TRACKING VIEW BOARD\] Option is needed.

A site can configure one or more display boards. The Display Board view offers a PC or workstation-based preview of the site's main electronic whiteboard display configuration. If a user has access to this view, then they can customize it or disable the auto refresh capability.

Layout changes made within this view cannot be saved. Further, the changes a user makes appear only on their local machine (as opposed to the large display). To request permanent changes in the Display Board view, please contact the person who configures EDIS for the site (usually an IRM, CAC, or EDIS Coordinator).

The PC-based Display Board view contains only the columns a site has selected for its main display board. Refer to section 8.2Display Board Sub View for a list of these columns.

> **NOTE:** EDIS only displays information for laboratory, imaging, and new orders that are associated with patients' current emergency department visits.

## Arrange Columns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To arrange columns in the Display Board view, use a drag-and-drop operation.

## Resize Columns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To resize columns in the Display Board view:

- Use a drag-and-drop operation.
  - Go to a column boarder in the header row of the table. EDIS displays a slider in place of the pointer.
  - Select and drag the boarder to a new location.
  - Deselect.

## Sort Columns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To sort columns in the Display Board view:

- Select a column header to sort the column's contents in descending order.
- Select the column header again to sort the column’s contents in ascending order.

> **NOTE:** Sorting information within columns in the PC-based Display Board view does not cause EDIS to similarly sort information in the large electronic (LCD) whiteboard display columns. EDIS first sorts large display columns by the order of the rooms and areas listed in the Room / Areas sub view, then secondly by the order of patients' acuities.

# Assign Staff View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Navigate to the Assign Staff view by selecting Assign Staff.

This view enables authorized users to:

- Add staff
- Remove staff
- Configure text and background colors for staff assignments

Changes in this view will affect the pick lists that are available in the CPE and Edit Closed views.

<span id="_bookmark93" class="anchor"></span>Figure 16: Assign Staff View

![](emergency-department-integration-software-user-guide-file-name-contains-r/017.png)

## Add Providers, Residents, and Nurses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add providers, residents, and nurses:

1.  Enter the name of a physician, resident, or nurse in the view's respective Providers, Residents, or Nurses search field. EDIS displays a list of possible matches from the local VistA system (nurse search lists are based on the site's EDPF NURSE STAFF SCREEN parameter setting).
2.  Select the name of the physician, resident, or nurse to be added and select the Add \>\> option. EDIS adds the name to the respective Provider, Resident, or Nurse table.
3.  Select Save Staff Changes to save the changes.

> **NOTE:** A user can only belong to one table. After selecting Save Staff Changes, the user will be a part of the table they were last added to and promptly removed from all other tables.

## Remove Providers, Residents, and Nurses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To remove providers, residents, and nurses:

1.  In the Provider, Resident, or Nurse table, select the physician, resident, or nurse to be removed.
2.  Select Remove.
3.  Select Save Staff Changes to save the changes.

## Configure Colors for Providers, Residents, and Nurses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To configure text and background colors for providers, residents, and nurses:

1.  Select a physician, resident, or nurse in the Provider, Resident, or Nurse table. EDIS displays the Use Custom Color check box to the right of the respective table.
2.  Select the Use Custom Color check box. If the color selection menu does not appear, then select the Color icon to the right to expand or collapse the color menu. The bottom right corner of each color scheme indicates the text color, and the remaining space around the corner indicates the background color.

<span id="_Toc196383180" class="anchor"></span>Figure 17: Color Icon

![](emergency-department-integration-software-user-guide-file-name-contains-r/018.png)

3.  Select a color scheme. The Color icon to the right will change according to this selection.

> **NOTE:** Colors configured for staff assignments will not appear on the display board unless colors (in general) are enabled for staff selections in section 8.2 Display Board Sub View.

# Reports View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Navigate to the Reports view by selecting Reports. A Report drop-down menu, Start Date and Stop Date fields, along with a Run Report option is displayed.

EDIS allows the site to control access to the Reports view in several ways. For example, the site can deny access (in which case users don't see the Reports view from the view options). Users can run and view, print, and export the EDIS reports.

<span id="_Toc196383181" class="anchor"></span>Figure 18: Reports View

![](emergency-department-integration-software-user-guide-file-name-contains-r/019.png)

> **NOTE:** Sites control user access to the export feature via the EDPR EXPORT security key. Sites also control access to the Patient xRef report via the EDPR XREF security key.

> **NOTE:** The reports in Table 1: Reports with Possible Errors may, under certain circumstances, give erroneous results. These reports should be used with caution.

| Report              | Possible Error                                                                             |
|---------------------|--------------------------------------------------------------------------------------------|
| Activity            | May display negative values for Wait, Triage, Admission Delay, Admission Decision columns. |
| Acuity              | May display negative values.                                                               |
| Delay               | May display negative values for Admission Delay, Admission Decision columns.               |
| Missed Opportunity  | May display negative values for Wait, Triage, Admission Delay, Admission Decision columns. |
| Shift               | Does not display correct values.                                                           |
| VA Admission Report | May display negative values for Wait, Triage, Admission Delay, Admission Decision columns. |

Reports with Possible ErrorsThis table shows the reports that may experience errors and provides a short discription of those errors

## Report Columns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS reports are data tables that include one or more of the following columns:

- IEN: The EDIS internal entry number (IEN-a number recorded in the .001 field of VistA VA FileMan files)
- Patient: The EDIS patient name
- Time In: The time at which an EDIS user identified and added the patient, or the time at which an Appointment Management user created an emergency department appointment for the patient
- Time Out: The time at which the facility closed the patient's emergency department visit
- Complaint: The patient's display-board complaint
- MD: The initials of the patient's physician
- Acuity: The patient's acuity level
- Elapsed: Total elapsed time (from the patient's time in to his or her time out, in minutes; asterisks indicate stays that have exceeded the current nationally recognized stay limit of 360 minutes)
- Triage: The elapsed time between the patient's time in and his or her initial acuity assessment
- Wait: The elapsed time between the patient's time in and his or her first assignment to a location other than the waiting room
- Disposition (Dispo): The patient's disposition
- Admission Decision (Adm Dec): The elapsed time between the patient's time in and the decision to admit the patient
- Admission Delay (Adm Delay): The elapsed time between the patient's time out and the decision to admit the patient
- Diagnosis: The patient's diagnosis
- ICD: The patient's International Classification of Diseases 10, Clinical Modifications (ICD-10-CM) diagnosis
- ICD Type: Contains ICD-10-CM to indicate the type of ICD diagnosis

## Disposition Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS reports use these abbreviations for the national list of dispositions when space is limited (see section 1.7.2Dispositions for national disposition descriptions):

- VA: Admitted to VA Ward
- AMA: Left against medical advice
- CL: Sent to Urgent Care Clinic
- D: Deceased
- E: Eloped
- ERR: Patient Name Entered in Error
- H: Home
- ICU: Admitted to ICU
- L: Left Without Being Treated/Seen
- NEC: Sent to Nurse Eval / Drop-In Clinic
- PSY: Admitted to Psychiatry
- T: Admitted to Telemetry
- NVA: Transferred to Non-VA Facility
- O: Transferred to VA Facility

## Standard Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The standard reports are:

- Activity Report
- Acuity Report
- Delay Report
- Delay Summary Report
- Exposure Report
- Missed Opportunities Report
- Orders by Acuity Report
- Patient Intake Report
- Shift Report
- VA Admissions Report

### Activity Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc196383182" class="anchor"></span>Figure 19: Activity Report

![](emergency-department-integration-software-user-guide-file-name-contains-r/020.png)

This report displays patient’s activity from the timeframe specified from the date range. The Activity report lists the following information below:

- IEN
- Time In
- Time Out
- Complaint
- MD
- Acuity
- Elapsed
- Triage
- Wait
- Disposition (Dispo)
- Admission Decision (Adm Dec)
- Admission Delay (Adm Delay)
- Diagnosis
- ICD
- ICD Type

In addition, this report provides averages for several important time-based measurements (Admission Decision, Admission Delay, Elapsed, Wait, and Triage) in several patient categories:

- All patients
- All patients who were admitted
- All patients who were not admitted
- All patients in each of the following disposition categories: Deceased (D), Eloped (E), Patient Name Entered in Error (ERR), Home (H), Admittedto ICU (ICU), Left Without Being Treated/Seen (L), Sent to Nurse Eval / Drop In Clinic (NEC), Transferred to non-VA Facility (NVA), Admitted to Psychiatry (PSY), Admitted to Telemetry (T), and Admitted to VA Ward (VA).

### Acuity Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc196383183" class="anchor"></span>Figure 20: Acuity Report

![](emergency-department-integration-software-user-guide-file-name-contains-r/021.png)

This report displays statistics that measure patient workload for each acuity level. For the date-and-time range selected, statistics show the number of patients who fell into each acuity category, the number of patients in each category who were admitted, and the number of patients in each category who were admitted to a VA facility. The Acuity report also provides the following average times for patients in each acuity category:

- Admission Decision (all facilities)
- Admission Decision (VA facilities)
- Admission Delay (VA facilities)

Also, if the site’s process results in a number of patients who have been removed from the board using the Patient Name Entered in Error selection, then correct the report’s total number of patients by subtracting the number of patients who were entered in error.

### Delay Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc196383184" class="anchor"></span>Figure 21: Delay Report

![](emergency-department-integration-software-user-guide-file-name-contains-r/022.png)

This report presents information about patients whose emergency department stays exceeded the nationally recognized limit (six hours or 360 minutes). For each patient whose stay exceeded this limit, the Delay report displays available information in the following columns:

- IEN
- Patient
- Time In
- Elapsed
- Disposition
- Delay Reason
- MD
- Admission Decision (Adm Dec)
- Admission Delay (Adm Delay)
- Acuity
- Diagnosis
- ICD
- ICD TypeNote: EDIS does not include, in its Delay and Delay Summary reports, patients whose emergency department visits are not yet closed regardless of the number of hours their visits have consumed.

### Delay Summary Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc196383185" class="anchor"></span>Figure 22: Delay Summary Report

![](emergency-department-integration-software-user-guide-file-name-contains-r/023.png)

This report presents average visit and decision-to-admit times (and other important information) for the following three visit categories:

- All emergency department visits
- All visits that resulted in VA-facility admissions
- All visits that did not result in VA-facility admissions

This report also presents acuity-based tallies for each applicable reason for delay. Again, if the site’s process results in a number of patients who have been removed from the board using the Patient Name Entered in Error selection, then subtract this number from the report’s total number of visits and from visits that didn’t result in VA-facility admissions.

> **NOTE:** EDIS does not include, in its Delay and Delay Summary reports, patients whose emergency department visits are not yet closed regardless of the number of hours their visits have consumed.

### Exposure Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc196383186" class="anchor"></span>Figure 23: Exposure Report

![](emergency-department-integration-software-user-guide-file-name-contains-r/024.png)

This report identifies patients and staff who may have been in the emergency department when a contagious patient was present for treatment. To run the report, users enter the internal entry number (IEN) from the contagious patient’s Visit file (ED LOG file (#230)). EDIS then uses information in this file to compile lists of all patients and staff that were in the emergency department during the time of the contagious patient’s visit. ICD and ICD Type column headings have been added to this report.

### Missed Opportunities Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc196383187" class="anchor"></span>Figure 24: Missed Opportunities Report

![](emergency-department-integration-software-user-guide-file-name-contains-r/025.png)

This report displays the following information about patients whose dispositions are AMA (left against medical advice), L (left without being treated or seen), or E (eloped):

- IEN
- Time In
- Complaint
- MD
- Acuity
- Elapsed
- Triage
- Wait
- Disposition
- Admission Decision (Adm Dec)

If the site assigns a nurse to left-without-being-seen (LWBS) callbacks, the nurse must either have access to the xRef report or the application’s Edit Closed view (to search for LWBS patients by Time In values).

### Orders by Acuity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc196383188" class="anchor"></span>Figure 25: Orders by Acuity Report

![](emergency-department-integration-software-user-guide-file-name-contains-r/026.png)

For each acuity, this report tallies the number of medication, laboratory, imaging, consultation, and other orders emergency department personnel placed during the date-and-time range specified.

### Patient Intake Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc196383189" class="anchor"></span>Figure 26: Patient Intake Report

![](emergency-department-integration-software-user-guide-file-name-contains-r/027.png)

The Patient Intake report provides time-of-day and day-of-week statistics about the number of patients who visited the emergency department during the date and time range selected.

Columns that report day-of-week tallies cover the entire time and date range against which the user runs the report.

- For example, if the date range entered includes two Tuesdays, the intersection of the Tue column and the 0700-0800 row will display the total number of patients who visited the emergency department on both Tuesdays between the hours of 7:00 a.m. and 8:00 a.m. The Total column contains a sum of all daily totals across each time-based row.
- For example, in the 0700-0800 row, the Total column contains a sum of daily totals from the Sun through Sat columns.

For each time-based row, the Avg/Day column presents an average that is based on the figure in the Total column and the total number of days in the date range selected.

- For example, if the date range is January 1, 2009 through January 31, 2009, the total number of days (the denominator) will be 31.

The report's Avg/Hour row contains an average that is based on the total number of visits in each day's column divided by the total number of hours for each day in the search range selected.

- For example, in the Sun column, the application calculates the following average: the total number of Sunday visits (the value in the Total row, Sun column) divided by 24 (the number of hours in a day) multiplied by the number of Sundays in the date range selected.

> **NOTE:** The Patient Intake report does not include maximum, minimum, or mean calculations.

### Shift Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc196383190" class="anchor"></span>Figure 27: Shift Report

![](emergency-department-integration-software-user-guide-file-name-contains-r/028.png)

This report is limited to one day of reporting and presents a shift-based calculation of the following data categories:

- Carried over at Report Start
- Number of New Patients
- Number of Patients Discharged
- Number Dec (Decision) to Admit to VA
- Number Dec (Decision) to Admit to Other
- Number over Six Hours
- Number Waiting for Triage
- Number of Occupied Beds
- Number of Missed Opportunities
- Number Deceased
- Number With No Disposition
- Carry over to Next Shift

### VA Admissions Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc196383191" class="anchor"></span>Figure 28: VA Admissions Report

![](emergency-department-integration-software-user-guide-file-name-contains-r/029.png)

This report uses Disposition selections to identify patients who were admitted to VA facilities (VA wards, intensive care units \[ICUs\], telemetry, and observation wards, for example) during the time-and-date range specified.

The report contains available information in the following columns:

- IEN
- Time Out
- Complaint
- MD
- Acuity
- Disposition
- Adm Dec (Admission Decision)
- Adm (Admission) Delay
- Diagnoses
- ICD
- ICD Type

The report also provides averages for patients who fall into each applicable VA-admission category.

## Non-Standard Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient xRef report is a non-standard report that contains personally identifying information, which requires special security keys (in VistA) to access and run the report.

### Patient xRef Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc196383192" class="anchor"></span>Figure 29: Patient xRef Report

![](emergency-department-integration-software-user-guide-file-name-contains-r/030.png)

The key for the Patient xRef report is EDPR XREF.

This report provides a cross reference between the EDIS IEN and patient identifiers (including patients' surname initials concatenated with the last four digits of their SSN. The report also includes patient's DFNs, which are the IENs in the VistA Patient file (#2).

## Run and View Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To run and view a report:

1.  From the Reports view select a report from the Report list.

> **NOTE:** If a user is running the Exposure report, enter the contagious patient's IEN in the visit IEN field. The Exposure report does not require a date range.

2.  For the Start Date: field select the Calendar icon to the right of the field to choose a date or enter a date in the box using the format, mm/dd/yyyy. The application automatically formats shorter dates. For example, if 8/8/09 is entered, then the application will reformat the date as 08/08/2009.

<span id="_Toc196383193" class="anchor"></span>Figure 30: Calendar Icon for Reports

![](emergency-department-integration-software-user-guide-file-name-contains-r/031.png)

3.  Select a starting time, which is found at the bottom of the Calendar icon drop-down menu.
4.  For the Stop Date: field select the Calendar icon to the right of the field to choose a date or enter a date in the box using the format, mm/dd/yyyy.
5.  Select a stopping time, which is found at the bottom of the Calendar icon drop-down menu
6.  Select Run Report.

> **NOTE:** If the reports contain negative numbers, then the problem could lie within the logic that EDIS's reporting functionality inherited from the class-three Syracuse application. Syracuse reporting logic assumes that users will enter information in a certain sequence. For example, the application assumes that a provider assigns himself or herself before entering a patient's disposition. To calculate the time that elapsed between a patient's provider assignment and disposition, the application subtracts provider entry time from disposition entry time. If a provider assigns himself or herself after they've entered dispositions, then reports will contain negative numbers. Negative numbers can also be a result of incorrect data entry, so be sure to double check that the correct information has been entered.

## Print Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To print a report:

1.  Select the Reports view.
2.  Run a report (see steps 1 through 6 in section 7.5 Run and View Reports).
3.  Select Print in the upper right corner above the report.

## Export Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Exporting reports requires the EDPR EXPORT key.

To export a report:

1.  Select the Reports view.
2.  Run a report (see steps 1 through 6 in section 7.5 Run and View Reports).
3.  If the user is authorized to export reports, then they can select Export in the upper right corner above the report.
4.  Open, Save, or Cancel the export.
    1.  Opening the report will open the report in an Excel spreadsheet, which then can be saved.
    2.  Saving the report will provide additional options to Open, Open folder, or Viewdownloads. Unless the Save As option was selected, then the user will be prompted to choose a file location and enter a name for the Excel spreadsheet.
    3.  Canceling the export cancels the Export operation.

# Configure View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Navigate to the Configure view by selecting Configure. By default, the Room / Areas sub view is displayed.

<span id="_Toc196383194" class="anchor"></span>Figure 31: Configure View

![](emergency-department-integration-software-user-guide-file-name-contains-r/032.png)

The Configure view lets authorized users configure the application to include locally meaningful pick lists and create customized electronic whiteboard displays. It houses the sub views:

- Room / Areas
- Display Board
- Colors
- Parameters
- SelectionsNote: \[EDPF TRACKING MENU ALL\] or \[EDPF TRACKING VIEW CONFIGURE\] Options are required.

## Room / Areas Sub View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc196383195" class="anchor"></span>Figure 32: Room / Areas Sub View

![](emergency-department-integration-software-user-guide-file-name-contains-r/033.png)

The Room / Area sub view enables users to:

- Add or configure rooms and areas
- Specify display names for rooms and areas
- Determine when the display board displays rooms and areas
- Select a default status for patients who occupy specific rooms or areas
- Mark rooms or areas inactive
- Select the occupancy category into which rooms and areas fall (multiple patient, single patient, and so forth)
- Indicate areas that contain two or more beds (for exposure reports)
- Specify the electronic whiteboard display on which rooms and areas appear

> Note: A room can be displayed on the default board and one additional board.

- Configure background and text colors for rooms and areas

### Add Room/Bed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add Room/Bed:

1.  Select Add Room/Bed at the top left of the Rooms/Areas table. The application will display the Room/Bed Details pane to the right of the table and add a new row to the bottom of the table (these additions cannot be removed).

<span id="_Toc196383196" class="anchor"></span>Figure 33: Room/Bed Details

![](emergency-department-integration-software-user-guide-file-name-contains-r/034.png)

2.  Replace New with the name of the room in the Name field of the Room/Bed Details pane (the application does not support duplicate room or area names).
3.  Replace New with the name EDIS will display in the Display Name field.
4.  Select the option Occupied, Always, or Never from the Display When list. This selection determines when EDIS includes the room or area on the electronic whiteboard display.

> Note: If Never is selected, then be sure to select the Inactive checkbox as well. Additionally, any patient in that room will no longer be visible on the display board.

5.  Select a status from the Default Status list (sites can configure their own selections for this list).
6.  If the new room or area is currently inactive, then select the Inactive? check box.
7.  Select the occupancy category from the Category list.
8.  If a room or area contains two or more beds, then enter a name that associates both of the beds into the Shared Name field.
9.  If the site uses more than one electronic whiteboard display, then enter the name of the display board that shows this room or area in the Use Board field. All patients appear on the application's main electronic whiteboard display.

> Note: A room can be displayed on the default board and one additional board.

10. Choose a text and background color scheme for the room or area in the Use Custom Color field (optional).
    1.  Select the Use Custom Color check box. If the color selection menu does not appear, then select the Color icon to the right. The color selection menu will expand below. The bottom right corner of each color scheme indicates the text color, and the remaining space around the corner indicates the background color.
    2.  Select a color scheme from the menu. The Color icon will change according to this selection. To collapse the menu, select the Color icon.

> **NOTE:** Colors for room and area assignments will not appear on the display board unless colors are enabled for room and area selections in the Configure view's Display Board sub view (see section 8.2 Display Board Sub View).

11. Select Move Up or Move Down to arrange the order of the row in the table or use a drag-and-drop operation.
12. Select Save Room/Bed Changes to save the changes. The application will display the alert message, "New room/bed configuration saved." Select the x in the upper right corner of the dialog box to dismiss this message.

> **NOTE:** If there are duplicated Name fields in the table, then the application displays the alert message, "The following duplicate names must be corrected before saving:" Select the x in the upper right corner of the dialog box to dismiss this message.

<span id="_Toc196383197" class="anchor"></span>Figure 34: Duplicate Name Alert Message

![](emergency-department-integration-software-user-guide-file-name-contains-r/035.png)

13. To dismiss the Room/Bed Details pane and view all the columns in the Rooms/Areas table, select All Columns \>\> located above the Name field in the Room/Bed Details pane.

### Edit Room/Bed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To edit Room/Bed:

1.  Select an existing row in the Rooms / Areas table. The application will display the Room /Bed Details pane to the right of the table.
2.  Edit any of necessary fields. See steps 2 through 11 in section 8.1.1 Add Room/Bed for instructions on the specific fields.
3.  Select Save Room / Bed Changes to save the changes. The application will display the alert message, "New room/bed configuration saved." Select the x in the upper right corner of the dialog box to dismiss this message.

> **NOTE:** If there are duplicated Name fields in the table, then the application displays the alert message, "The following duplicate names must be corrected before saving:" Select the x in the upper right corner of the dialog box to dismiss this message. Find and correct the duplicates before continuing.

4.  To dismiss the Room/Bed Details pane and view all the columns in the Rooms/Areas table, select All Columns \>\> located above the Name field in the Room/Bed Details pane.

## Display Board Sub View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS enables users to configure each display board separately. Simply select the board to be configured in the Board Name list. The application displays editable information about the board in the Board Properties pane.

<span id="_Toc196383198" class="anchor"></span>Figure 35: Display Board Sub View

![](emergency-department-integration-software-user-guide-file-name-contains-r/036.png)

Editable information includes:

- Add a new large electronic whiteboard display
- Add or remove display-board columns
- Edit column headers
- Identify information upon which users want to base cell colors in display-board columns
- Identify information upon which users want to base colors in display-board rows
- Reposition and resize display-board columns
- Select optimal display sizes
- Configure the display’s font size and scroll-delay time
- Compress (squish) all data rows into a single, no-scroll view (if possible)

### Add a New Display Board

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS enables the user to create multiple display boards. Display boards cannot be deleted once saved. When a new display board is added, the application associates all possible columns to it by default.

To add a new display board, select Add Board, by default all columns are populated for the added board.

### Columns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The columns that are populated in the new board:

- Room/Bed: The rooms, beds, and areas associated with the display board
- Complaint: Patients' display-board complaints
- Provider Initials: The initials of providers whom users have selected via the CPE view
- Resident Initials: The initials of residents whom users have selected via the CPE view
- Nurse Initials: The initials of nurses whom users have selected via the CPE view
- Total Minutes: The number of minutes from patients' time-in values (the times users added patients to or identified them in EDIS) to the present
- Lab Active/Complete: The number of active laboratory orders associated with patients' emergency department visits over the number of completed laboratory orders
- Clinic: No longer utilized, but still in the application for historical data
- Comments: Comments that users have entered via the CPE view
- Patient Name: Patients' surnames
- Acuity: Acuities users have entered via the CPE view
- New (Unverified) Orders: The number of unverified orders associated with patients' emergency department visits.
- Imaging Active/Complete: The number of active imaging orders associated with patients' emergency department visits over the number of completed imaging orders
- Status: Statuses users have entered via the CPE view
- Disposition: Dispositions users have entered via the CPE view
- Visit Created: Checkmarks that indicate EDIS has created visits for patients in CPRS or blank spaces that indicate EDIS has not created visits
- Minutes at Location: The number of minutes patients have been assigned to their present locations
- Admittance Delay: The elapsed time in minutes between the patient’s time-out value (the time user removed patient from EDIS) and the time the patient’s first admitting disposition (a disposition flagged "VA") is assigned

#### Remove Columns

To remove a column:

1.  Select a column in the list of columns below the Add Column option. The Column Properties pane will display underneath the Board Properties pane.
2.  Select the Remove Column option at the bottom of the Column Properties pane. The Preview Display Board pane at the bottom of the screen dynamically displays columns as they are removed.
3.  Repeat steps as necessary.

#### Add Columns 

To add columns:

1.  Select the Add Column option, the list of available columns will be displayed in a drop-down menu. If the Add Column option is gray and cannot be selected, then all existing columns are present in the board.
2.  Select a column name. The Preview Display Board pane at the bottom of the screen dynamically displays columns as they are added.
3.  Repeat steps as necessary.

#### Arrange Columns

To arrange columns:

1.  There are three ways to arrange the ordering of columns.
    1.  In the list of columns use a drag-and-drop operation.
    2.  In the Preview Display Board pane use a drag-and-drop operation.
    3.  Select a row in the list of columns and use the Move Up or Move Down options located at the bottom of the Columns Properties pane.

#### Update Column Properties

To update column properties:

1.  In the list of columns, select the column to be edited. The Column Properties pane will display underneath the Board Properties pane.
2.  Enter the new header in the Header box (optional).
3.  Select an item in the Color Based On list (optional). This selection determines the criteria the application uses to display color configurations in electronic whiteboard display columns. The application gives preference to the colors configured for columns over the colors configured for rows.

> **NOTE:** The Configure view determines the colors that are displayed for the columns on the display board. For example, select the Status column, then select Acuity from the Color Based On list. In this case, the board will display, in its Status column, the colors configured for Acuity.

#### Resize Columns 

Columns in the Preview Display Board pane can be resized in 2 ways:

1.  A drag-and-drop operation:
    1.  Go to the border of the column header to be resized in the Preview Display Board pane.
    2.  The pointer will become a slider, select and drag the border to resize the column.
    3.  Deselect.
    4.  Repeat as necessary.
2.  The Width field in the Column Properties pane:

> Note: Resize all the columns from left to right. Before an initial value is set, updating the field for a specific column out of order will readjust all the columns incorrectly. Start with a reasonable pixel value (e.g. 30) for each column. Then to resize further begin adjusting the field values from left to right.

1.  Enter the pixel width in the Width field to specify the size of the column.
2.  Repeat as necessary.

#### Edit Board Properties

To edit board properties:

1.  In the Board Name field, replace New-# with the name of the new display board.
2.  Select an item in the Row Color Based On list (optional).
3.  Select the screen size for the display board in the Display Size list. Display sizes are site configurable. If the Display Size list does not contain the new board's screen size, then check with the site's CAC or IRM staff.
4.  Enter or select a font size in the Font Size field. The Preview Display Board pane dynamically displays the font choices.
5.  Select the optional Squish Rows To Fit (if possible) check box. This selection allows EDIS to compress all data rows to completely fit within the site's display screen, if it is possible. To ensure readability, the application compresses data only down to a row size of 18 points and a font size of 11 points. If the site's data will still not fit within a single display view after applying the maximum compression, then the application applies scrolling functionality and restores the display board's font size to the value specified in the Font Size field.
6.  Enter or select a scroll-delay time (in seconds) in the Scroll Delay field. The application automatically activates scrolling when the screen cannot display all of the patients who are currently on the list of active patients. The delay-time setting determines how long screen contents remain stationary.

> **NOTE:** EDIS refreshes the display board every 30 seconds. Each refresh resets the display board. Set scroll-delay intervals that allow the application to display all patients within the span of a single refresh cycle. Screen reader users can disable automatic refresh functionality and manually refresh the display board by pressing the F7 key; however, the automatic refresh feature is disabled only when the screen reader is running.

### Save Display Board Configuration Changes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To save the configuration changes, select Save Display Board Changes underneath the Column Properties pane. EDIS displays the alert message, "Display Board configuration saved." Select the x in the upper right corner of the dialog box to dismiss this message.

## Colors Sub View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_bookmark135" class="anchor"></span>Figure 36: Colors Sub View

![](emergency-department-integration-software-user-guide-file-name-contains-r/037.png)

The Colors sub view enables users to configure colors for the following items:

- Status/Acuity
- Status
- Acuity
- Urgency Lab
- Urgency Radiology
- Total Elapsed Minutes
- Minutes at Location
- Minutes for Lab Order
- Minutes for Imaging Order
- Minutes for Unverified Order

Users can configure colors for rooms and areas in the Room / Area sub view. Colors can also be configured for emergency department staff in the Assign Staff view.

### Configure Colors for Status/Acuity, Status, Acuity, Urgency Lab, and Urgency Radiology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the Status/Acuity selection enables users to configure colors for the combined set of status and acuity values.

> **NOTE:** Color schemes in the Colors sub view must match at least one-color selection in the Display Board sub view. For example, if configuring colors using the Status/Acuity selection in the Colors sub view, then select Status / Acuity in the Colors Based On column or Row Color list in the Display Board sub view. If configuring colors for the Status/Acuity selection and also for the Acuity and/or Status selections, then the application will display the colors that are configured for Status/Acuity.

To configure colors for these selections:

1.  In the Available Color Maps list, select Status, Acuity, or Status/Acuity, Urgency Lab, or Urgency Radiology. EDIS displays the Colors for Status, Colors for Acuity, Colors for Status/Acuity, Colors for Urgency Lab, or Colors for Urgency Radiology list, respectively.
2.  To configure colors for a value listed, select the value.
3.  Select the Use Custom Color check box. If the color selection menu does not appear, then select the Color icon to the right. The color selection menu will expand below. The bottom right corner of each color scheme indicates the text color, and the remaining space around the corner indicates the background color.
4.  Select a color scheme from the menu. The Color icon will change according to this selection. To collapse the menu, select the Color icon.
5.  Repeat steps 1 through 4 to configure colors for additional values.
6.  Select Save Color Changes to save the color configurations. The application displays the alert message, "New board colors saved." Select the x in the upper right corner of the dialog box to dismiss this message.

### Configure Colors for Total Elapsed Minutes, Minutes at Location, Minutes for Lab Order, Minutes for Imaging Order, Minutes for Unverified Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To configure colors for these selections:

1.  Select Total Elapsed Minutes, Minutes at Location, Minutes for Lab Order, Minutes for Imaging Order, or Minutes for Unverified Order in the Available Color Maps list. The application displays the Colors for Total Elapsed Minutes, Colors for Minutes at Location, Colors for Minutes for Lab Orders, Colors for Minutes for Imaging Order, Colors for Minutes for Unverified Order list, respectively.
2.  To add or edit a time value in the Starting at Elapsed Minute column, select Add or a specific row. The application adds the new row to the bottom of the list with a default value of zero or highlights the selected row.
3.  Enter a starting value in the Starting at Elapsed Minute field. EDIS uses this value to determine when to display the color configuration.
4.  Select the Use Custom Color check box. If the color selection menu does not appear, then select the Color icon to the right. The color selection menu will expand below. The bottom right corner of each color scheme indicates the text color, and the remaining space around the corner indicates the background color.
5.  Select a color scheme from the menu. The Color icon will change according to this selection. To collapse the menu, select the Color icon.
6.  Repeat steps 2 through 5 to configure colors for additional values.
7.  Select Save Color Changes to save the color configurations. The application displays the alert message, "New board colors saved." Select the x in the upper right corner of the dialog box to dismiss this message.

## Parameters Sub View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc196383200" class="anchor"></span>Figure 37: Parameters Sub View

![](emergency-department-integration-software-user-guide-file-name-contains-r/038.png)

The Parameters sub view enables users to set the following parameters:

- Show residents on entry form
- Show clinics on entry form
- Diagnosis is required before removing a patient
- Diagnosis must be coded as ICD
- Disposition is required before removing patient
- Delay reason is required for visits exceeding (site specified) minutes
- Shift Parameters
- Arriving Ambulance Room/Area is
- Default Room/Area is
- Metrics Text for Waiting Room Display Board
- Footer Text for Waiting Room Display Board
- Updates Text for Waiting Room Display Board

### Show Residents on Entry Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter enables sites to include residents on the application's data-entry views. Resident-selection lists appear on the CPE and Edit Closed views.

To activate this parameter, select the Show residents on entry form checkbox. To deactivate this parameter, clear the Show residents on entry form checkbox.

### Show Clinics on Entry Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter enables sites to include clinics on the application's data-entry views.

To activate this parameter, select the Show clinics on entry form checkbox. To deactivate this parameter, clear the Show clinics on entry form checkbox.

### Diagnosis Is Required Before Removing a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter requires emergency department personnel to enter diagnoses as a precondition to removing patients from the display board. The exception is if the patient's disposition is one of the following:

- Patient Name Entered in Error
- Left Without Being Treated/Seen
- Sent to Nurse Eval/Drop In Clinic

To activate this parameter, select the Diagnosis is required before removing patient checkbox. To deactivate this parameter, clear the Diagnosis is required before removing patient checkbox.

### Diagnosis Must be Coded as ICD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter requires the use of the VistA ICD-10-CM search for all diagnosis entries. When sites do not select this parameter, the application provides a free-text field for recording diagnoses.

> **NOTE:** A free-text diagnosis does not pass to the PCE Encounter.

To activate this parameter, select the Diagnosis must be coded as ICD checkbox. To deactivate this parameter and allow free-text diagnoses, clear the Diagnosis must be coded as ICD checkbox.

### Disposition is Required Before Removing Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter requires emergency department personnel to enter dispositions before removing patients from the display board.

To activate this parameter, select the Disposition is required before removing patient checkbox. To deactivate this parameter, clear the Disposition is required before removing patient checkbox.

### Require a Delay Reason

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter does not allow users to remove patients whose stays have exceeded a specific number of minutes without first entering a reason for delay. The exception is if the patient's disposition indicates that he or she has been assigned to an observation ward.

To activate this parameter, select the Delay reason is required for visits exceeding … minutes checkbox. In the Minutes field, enter or select a number of minutes (up to a maximum of 360) to be exceeded for a reason for delay. To deactivate this parameter, clear the Delay reason is required for visits exceeding … minutes checkbox.

### Shift Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The application uses this information to pull data for shift reports.

In the First shift begins at field, enter the time (in hours and minutes hh:mm) the site's first shift begins.

In the Shift duration is… hours and minutes fields, enter or select the hours and minutes that mark the duration of the site's shifts.

### Arriving Ambulance Room/Area is

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter enables sites to select a default room or area for patients who are arriving by ambulance or other emergency-transport vehicles.

Select a room or area from the Arriving Ambulance Room/Area is drop-down menu.

### Default Room/Area is

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter enables sites to select a default room or area.

Select a room or area from the Default Room/Area is drop-down menu.

> **NOTE:** If a default room is not selected, EDIS will warn users upon login that a default room needs to be set. Until a default room is selected, EDIS will place new patients in an area designated as EDIS_DEFAULT. This will ensure that new patients will function correctly within the EDIS application.

### Metrics Text for Waiting Room Display Board

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter allows users the ability to provide Veterans up-to-date information on the metrics shown on the Waiting Room Display Board. The text can be customized to meet the needs of the local site. This text field has a 240-character limit.

Example of Metrics Text: Please note that patients with more severe illness or injury may be seen ahead of more stable patients and not necessarily in order of arrival to the ED.

### Footer Text for Waiting Room Display Board

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter allows users the ability to customize the local Waiting Room Display Board with the Facility Name. This text field has a 240-character limit.

### Updates Text for Waiting Room Display Board

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter allows users the ability to provide Veterans relevant patient-focused updates to be displayed on the Waiting Room Display Board. This text field has a 240-character limit.

### Save Parameters Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Save Parameter Changes. The application displays the alert message, "New parameter configuration saved." Select the x in the upper right corner of the dialog box to dismiss this message.

If a user wishes to change the parameter settings after saving, for whatever reason, they may receive the alert message, "Only one person should edit the configuration at a time. The configuration has been modified since beginning. The user will need to re-enter the changes they have made." The application will revert back to the selections that were just saved. Log out and log back in to make additional changes and save the new parameter selections.

> **NOTE:** Some parameter settings require the user to log out of the application and log back in. For example, if a user selects the Diagnosis must be coded as ICD or the Show residents on entry form check box, then the user must log out and log back in to see the changes in the CPE view.

## Selections Sub View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc196383201" class="anchor"></span>Figure 38: Selections Sub View

![](emergency-department-integration-software-user-guide-file-name-contains-r/039.png)

The Selections sub view enables users to add locally meaningful selections to the preset lists within EDIS. Selections can be added to the following lists:

- Statuses
- Dispositions
- Delay Reasons
- Sources

The EDIS technical working group (TWG) and technical advisory group (TAG) have vetted these default lists. When sites add selections, the application denotes local adaptations of the national status, disposition, delay reason, and source list values described in Section 1.7, National Definitions, by displaying (local) in the sub view's National Name column.

### Adding Status, Disposition, Delay Reason, and Source Selections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add selections to these lists:

1.  Select Status, Disposition, Delay Reason, or Source in the Selection List. The application displays the Selections for Status, Selections for Disposition, Selections for Delay Reason, or Selections for Source lists, respectively.
2.  Select Add, the application displays the Edit Selection Item pane to the right.
3.  Enter a name into the Name field.
4.  Enter an abbreviation into the Abbreviation field. EDIS uses this abbreviation for its electronic whiteboard display.
5.  Enter the applicable flags into the Flags field. EDIS uses these flags for reporting and to determine whether or not it should require a reason for delay when emergency department visits exceed site-specified time limits.
    1.  Status selection flags include A (for admitted), O (for observation), or AO (for both).
    2.  Disposition select flags include VA (for VA admission, A (for admitted), or M (for missed opportunity).

> **NOTE:** Status and Disposition flags cannot be edited. Editing flags would affect historical data. If a flag is incorrect a user can deactivate an old term and create a new term (with the same name) and correct flag.

6.  Select the check box for the Inactive field to deactivate the new item (optional). The application does not include inactive items on its selection lists.
7.  Arrange the order of the list by using a drag-and-drop operation or selecting the Move Up or Move Down options in the Edit Selection Item pane (optional).
8.  Select Save Selection List Changes to save the additions or edits. EDIS displays the alert message, "New selection configuration saved." Select the x in the upper right corner of the dialog box to dismiss this message.

# Waiting Room Display Board

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Waiting Room Display Board is a Veteran facing Big Board (monitor on the wall) that was deployed with EDIS v.2.2.46/EDP\*2.0\*24. The Waiting Room Display Board displays the following metrics:

- The average wait time "Door to Doc" for the last 5 patients assigned a provider in EDIS. "Door to Doc" is the time in minutes between patient arrival (Time In) and the first assignment of a provider. The clock will restart at 0 when there are zero patients on the EDIS board.

The Display Board has 3 configurable text fields: a Footer message, a Metrics message, and an Updates message. The text in these fields can be modified locally from the EDIS Parameters Configuration screen.

Please see *Emergency Department Integration Software Technical Manual* for information about the technical set-up of the Waiting Room Display Board by IRM staff.

<span id="_Toc196383202" class="anchor"></span>Figure 39: Waiting Room Board

![](emergency-department-integration-software-user-guide-file-name-contains-r/040.png)