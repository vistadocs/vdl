---
title: VES Version 5.1 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: null
app_code: VES
app_name: VA Enrollment System
section: GUI
app_status: archive
pkg_ns: VES
patch_ver: 5.1
patch_id: VES*5.1
group_key: VES:VES:5.1
file_numbers: []
security_keys: []
menu_options: 0
description: '- Introduction - Purpose - Audience - This Release - Enhancements and Modifications - Defects and Fixes - Known Issues - [Product...'
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 8485
section_count: 4
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: March 2018
revision_count: 0
revision_newest: ''
revision_oldest: ''
docx_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VA_Enrollment_System_Archive/es_5_1_release_notes.docx
pdf_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VA_Enrollment_System_Archive/es_5_1_release_notes.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=293
audit_applied: '2026-05-31'
master_source: VES Version 5.1 Release Notes
master_pub_date: March 2018
consolidated_from: 33 versions
prior_versions:
- VES Version 5.10.1 Release Notes
- VES Version 5.10 Release Notes
- VES Version 5.12 Release Notes
- VES Version 5.13 Release Notes
- VES Version 5.14.1 Release Notes
- VES Version 5.14.2 Release Notes
- VES Version 5.14 Release Notes
- VES Version 5.15.1 Release Notes
- VES Version 5.15.2 Release Notes
- VES Version 5.15 Release Notes
- VES Version 5.16 Release Notes
- VES Version 5.17 Release Notes
- VES Version 5.18 Release Notes
- VES Version 5.19.1 Release Notes
- VES Version 5.19.2 Release Notes
- VES Version 5.19 Release Notes
- VES Version 5.2.1 Release Notes
- VES Version 5.2.3 Release Notes
- VES Version 5.2.4 Release Notes
- VES Version 5.2 Release Notes
- VES Version 5.3.1 Release Notes
- VES Version 5.3 Release Notes
- VES Version 5.4.1 Release Notes
- VES Version 5.4 Release Notes
- VES Version 5.5.1 Release Notes
- VES Version 5.5 Release Notes
- VES Version 5.6.1 Release Notes
- VES Version 5.6 Release Notes
- VES Version 5.7 Release Notes
- VES Version 5.8 Release Notes
- VES Version 5.9.1 Release Notes
- VES Version 5.9 Release Notes
consolidated_title: ves release notes
---

![](ves-version-5-1-release-notes/001.png)

March 2018

Office of Information and Technology (OIT)

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Purpose](#purpose)
- [Audience](#audience)
- [This Release](#this-release)
  - [Enhancements and Modifications](#enhancements-and-modifications)
  - [Defects and Fixes](#defects-and-fixes)
  - [Known Issues](#known-issues)
- [Product Documentation](#product-documentation)
The mission of the Department of Veterans Affairs (VA) Office of Information and Technology (OIT), Enterprise Program Management Office (EPMO) is to provide benefits to Veterans and their families. In order to meet this overarching goal, OIT is charged with providing high quality, effective, and efficient IT services and Operations and Maintenance (O&M) to persons and organizations that provide point-of-care services to our Veterans.
The VA's goals for its Veterans and families include:
- Make it easier for Veterans and their families to receive the right benefits, and meeting their expectations for quality, timeliness, and responsiveness.
- Improve the quality and accessibility of health care, benefits, and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing state of the art disease management.
- Ensure awareness and understanding of the personalized, proactive, and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice, and ongoing support needed to make informed health decisions and successfully implement the Veteran's personal health plans.
- Receive timely, high quality, personalized, safe, effective, and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates, and other service organizations.
In order to assist in meeting these goals, the Enterprise Health Benefits Determination (EHBD) program will provide enterprise wide enhancements and sustainment for the following systems/applications:
- The Enrollment System (ES) assists Veterans to enroll for VA healthcare benefits and is the core application that feeds other VA systems with Enrollment and Eligibility (E&E) data.
- Income Verification Match (IVM) assists in determining priority grouping for healthcare eligibility.
- Veterans Information Systems and Technology Architecture (VistA) Registration, Eligibility & Enrollment (REE) shares information with other VistA applications and enables registration and eligibility determinations and enrollment at VA Medical Centers (VAMC).
- Veteran's On-Line Application (VOA) is re-purposed for the online Veterans Health Benefits Handbook (VHB). VHB provides each enrolled Veteran on-demand online access to a personalized and dynamic health benefits-related Handbook.
Enrollment System Modernization (ESM) defines Health Benefit Plans (HBP) for which a client (Veteran, Service Member, or beneficiary) is eligible and ties them to the authority for care. Key enhancements to be completed include Pending Eligibility Determination, fixes to the Enrollment System, Date of Death, Internal Controls, Workflow, Veterans Financial Assessment, converting of Military Service Data Sharing (MSDS) to Enterprise Military Information Service (eMIS), Manage Relationships, Veteran Contact Service, and support for Enrollment System Community Care (ESCC).

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Release Notes document is to support the release of ES 5.1. The EHBD Program provides enhancements to the ES. This ES 5.1 release, developed in Java technology, contains ESM development efforts, including enhancements to support Community Care (CC) and ES Sustainment.

# Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of ES 5.1 and applies to the changes made between this release and any previous release for this software.

# This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ES will be upgraded from Version 5.0.1 to Version 5.1 and hosted at the Austin Information Technology Center (AITC). This upgrade will improve the user experience and the performance of ES.

The following sections provide a summary of the enhancements and modifications to the existing software and any known issues for ES 5.1.

## Enhancements and Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1 lists the enhancements and modifications included in the ES 5.1 release. Enhancements and modifications are tracked in Rational Team Concert (RTC) Requirements Management (RM).

<table>
<caption><p>Table : Enhancements and Modifications in the 5.1 Release</p></caption>
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th>RTC<br />
RM #</th>
<th>Title</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>869421</td>
<td>Query Enterprise Military Information Service (eMIS) - changes to Complete Add A Person</td>
<td>The military service information authoritative source Enterprise Military Information Service (eMIS) is queried, when a new Veteran is added to ES.</td>
</tr>
<tr class="even">
<td>869423</td>
<td>Receive from eMIS - Changes to Process Send Receive Military Service Data Sharing (MSDS) Service</td>
<td>Capability is implemented to receive zero, one or many sets of Service Period information, Guard/Reserves Activations, Deployment and Combat Pay from the eMIS Process Send Receive MSDS service.</td>
</tr>
<tr class="odd">
<td>869425</td>
<td>Capture Broker Military Episode - Changes to Military Information (MI) Process Person Military Service Data</td>
<td><p>The following military service information received from eMIS is saved:</p>
<ol type="1">
<li><p>Purple Heart Indicator</p></li>
<li><p>Medal of Honor Indicator</p></li>
<li><p>Active Duty Indicator (NEW)</p></li>
<li><p>Future Discharge Date (NEW)</p></li>
<li><p>Service Periods (Military Service Episode) Information</p></li>
<li><p>Activations Information (Military Service Episode)</p></li>
<li><p>Combat (Military) Pay Information</p></li>
</ol></td>
</tr>
<tr class="even">
<td>869427</td>
<td>Changes to MI Process Person Military Service Data</td>
<td>The Military Information (MI) Process Person Military Service Data is updated with Veteran Indicator rules.</td>
</tr>
<tr class="odd">
<td>869429</td>
<td>Edit the eMIS Current Military Service Information</td>
<td>The current Military Service Information is edited from the authoritative source.</td>
</tr>
<tr class="even">
<td>869431</td>
<td>View Current eMIS Information</td>
<td>The current Military Service Information is viewed from the authoritative source.</td>
</tr>
<tr class="odd">
<td>869439</td>
<td>Creation of eMIS Query Statuses</td>
<td>An eMIS query status of "Service Data Received but not Uploaded" is created.</td>
</tr>
<tr class="even">
<td>869441</td>
<td>Receive Business Event Notification System (BENS) Notification for Military History Changes</td>
<td><p>The subscribed event notification is received from Business Event Notification System (BENS) for the following Military History changes:</p>
<ol type="1">
<li><p>VA Department of Defense Identity Repository (VADIR) generated transaction ID<br />
(This is an internal transaction identifier)</p></li>
</ol>
<ol start="8" type="1">
<li><p>Transaction Date/Time</p></li>
<li><p>Department of Defense Electronic Data Interchange Personal Identifier (DoD EDI PI) for the transaction<br />
(In VADIR, it's called VA_ID, for the person with whom the event is associated)</p></li>
<li><p>Event Name<br />
(example: MIL_HIST_CHNG)</p></li>
<li><p>Component<br />
(A = Regular Active, V = Reserve, N = Guard, Q = Reserve)</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>869443</td>
<td>Retrieve Military Service Information (Receive BENS Notification)</td>
<td><p>Retrieval of the following Military Service information is executed under the following conditions:</p>
<ol type="1">
<li><p>A search of the database to locate the person record for the individual identified in the BENS notification.</p></li>
</ol>
<ol type="a">
<li><p>If the individual is not identified, the ES discontinues processing.</p></li>
<li><p>If the individual is identified, the ES continues processing.</p></li>
</ol>
<ol start="12" type="1">
<li><p>A check of the ES record to determine if the Service Member/Veteran is locked with the reason of "No Enrollment Determination".</p></li>
</ol>
<ol type="a">
<li><p>If the ES record is locked for "No Enrollment Determination", the ES discontinues processing.</p></li>
</ol>
<ol start="3" type="a">
<li><p>If the ES record is not locked for "No Enrollment Determination", the ES continues processing by querying the authoritative military information service (eMIS).</p></li>
</ol></td>
</tr>
<tr class="even">
<td>869445</td>
<td>View Raw, Parsed Data from eMIS</td>
<td>The raw, parsed data is viewed from eMIS.</td>
</tr>
<tr class="odd">
<td>869451</td>
<td>Capture Audit History from eMIS</td>
<td>The Audit History is captured from eMIS.</td>
</tr>
<tr class="even">
<td>869453</td>
<td>Changes to MI Process Person Military Service Data</td>
<td><p>Upon determination of matching service episodes, ES generates an exception and sets the eMIS Query Status to "Service Data Rcvd but not Uploaded" for the following condition:</p>
<p>Character of Discharge in the repository Administrative Data Repository (ADR) IS NOT BLANK or NULL AND Character of Discharge in the message IS NOT BLANK or NULL AND Character of Discharge in the repository (ADR) IS NOT EQUAL TO Character of Discharge in the message.</p></td>
</tr>
<tr class="odd">
<td>879449</td>
<td>New Application Received after the Application is closed</td>
<td>ES accepts new application from the applicants who have a record with current enrollment status of "Closed Application" and the reason is set to "Abandoned Application". ES ignores the enrollment history of the application prior to the enrollment status of Closed Application.</td>
</tr>
<tr class="even">
<td>880610</td>
<td>Query eMIS - Changes to Manage Person Military Service Information</td>
<td>An ES user is allowed to query the military service information authoritative source (eMIS) upon demand.</td>
</tr>
<tr class="odd">
<td>880614</td>
<td>Query eMIS - Changes to Process Send Receive MSDS Service</td>
<td><p>The following payloads (full set) of military service information are used when querying eMIS:</p>
<ol type="1">
<li><p>Operation Enduring Freedom/Operation Iraqi Freedom Indicator</p></li>
</ol>
<ol start="13" type="1">
<li><p>Purple Heart Indicator</p></li>
<li><p>Medal of Honor Indicator</p></li>
<li><p>Active Duty</p></li>
<li><p>Future Discharge Date</p></li>
<li><p>Future Discharge Date Certainty Code</p></li>
<li><p>Service Periods (Military Service Episode) Information</p></li>
<li><p>Activations Information (Military Service Episode)</p></li>
<li><p>Combat (Military) Pay Information</p></li>
<li><p>Deployment Information</p></li>
</ol></td>
</tr>
<tr class="even">
<td>880615</td>
<td>Receive from eMIS - Changes to MI Process Person Military Service Data</td>
<td>New logic is for Active Duty Indicator used to set the "Discharge Due to Disability".</td>
</tr>
<tr class="odd">
<td>880640</td>
<td>Save from eMIS - ADR updates</td>
<td>Alternative Dispute Resolution (ADR) updates are saved from eMIS.</td>
</tr>
<tr class="even">
<td>882166</td>
<td>Display FDD From Broker - Changes to Manage Person Military Service Information</td>
<td>The Future Discharge Date (FDD) is displayed when received from eMIS.</td>
</tr>
<tr class="odd">
<td>882171</td>
<td>Display FDD from Broker - changes to Search for Person</td>
<td>The Future Discharge Date (FDD) is displayed on the banner and Overview Tab – FDD section when received from eMIS.</td>
</tr>
<tr class="even">
<td>882174</td>
<td>View FDD from Broker - updates to MI Process Person Military Service Data</td>
<td>The Future Discharge Date is updated when received from eMIS and the eMIS System Job Name is the "Source of Change".</td>
</tr>
<tr class="odd">
<td>882222</td>
<td>View FDD from Broker - changes to ES Supplementary Specification for Clocks</td>
<td>The "Query DoD Every 7 Days" processes are run when the Future Discharge Date is the same as the current date.</td>
</tr>
<tr class="even">
<td>882223</td>
<td>View FDD from Broker - changes to MI Process Person Military Service Data</td>
<td>The Future Discharge Date Maturity clock is set/reset when a Future Discharge Date is received from eMIS.</td>
</tr>
<tr class="odd">
<td>882224</td>
<td>View FDD from Broker and share FDD with VistA</td>
<td>The Future Discharge Date is shared with VistA sites.</td>
</tr>
<tr class="even">
<td>882227</td>
<td>Capture Broker Military Episode - changes to MI Process Person Military Service Data</td>
<td><p>The following information is captured for Military Episode:</p>
<ol type="1">
<li><p>Actual discharge date.</p></li>
</ol>
<ol start="22" type="1">
<li><p>Creates a new military episode record with the new military service date.</p></li>
<li><p>Captures the combat episode information.</p></li>
<li><p>Records the date.</p></li>
<li><p>Records the discharge dates.</p></li>
<li><p>Records the character of service.</p></li>
<li><p>Transmits the Future Discharge Date to VistA sites of record.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>882307</td>
<td>View FDD from Broker - Process FDD - changes to MI Process Person Military Service Data</td>
<td>The Future Discharge Date is only processed when received from eMIS if the Active Duty Indicator = True or Yes for the service episode.</td>
</tr>
<tr class="even">
<td>886182</td>
<td>Changes to Process Send Receive Military Service Data Sharing (MSDS) Service for Person Not Found</td>
<td>The creation of "Person Not Found in VADIR and Beneficiary Identity Record Locator System (BIRLS)" is no longer needed and deprecated as part of the MSDS service response.</td>
</tr>
<tr class="odd">
<td>886183</td>
<td>Changes to Process Send Receive MSDS Service</td>
<td>The creation of "Null Identify Trait Values" is no longer needed and deprecated for "In step Prepare Request", if Last Name, First Name, SSN, Date of Birth, or Gender are null and the request is not sent to the eMIS Service.</td>
</tr>
<tr class="even">
<td>886196</td>
<td>Changes to Process Send Receive MSDS Service</td>
<td>The creation of "Person Found but No MS Data" for "In step Service Response Received" is no longer needed and deprecated.</td>
</tr>
<tr class="odd">
<td>886197</td>
<td>Changes to Process Send Receive MSDS Service</td>
<td>The creation of Multiple Persons Found in VADIR or BIRLS" is no longer needed and deprecated.</td>
</tr>
<tr class="even">
<td>886198</td>
<td>Changes to Process Send Receive MSDS Service</td>
<td>The creation of "Success from One Data Source but Not Found in Other" is no longer needed and it is removed.</td>
</tr>
<tr class="odd">
<td>886199</td>
<td>Changes to Process Send Receive MSDS Service</td>
<td><p>The creation of a "Null Values Validation" is no longer needed and deprecated for the following:</p>
<ol type="1">
<li><p>Service Period Start Date</p></li>
</ol>
<ol start="28" type="1">
<li><p>Activation Begin Date</p></li>
<li><p>Deployment Begin Date</p></li>
<li><p>Combat Pay Start Date</p></li>
<li><p>Release From Active Duty Date</p></li>
<li><p>Branch of Service</p></li>
<li><p>Combat Pay Type</p></li>
</ol></td>
</tr>
<tr class="even">
<td>886200</td>
<td>Changes to Process Send Receive MSDS Service for Date Range Validation</td>
<td><p>The creation of a "Date Range Validation" if any of the following date range validations is true as part of the MSDS service processing, is no longer needed and deprecated:</p>
<ol type="1">
<li><p>Activation Begin Date is greater than Activation End Date.</p></li>
</ol>
<ol start="34" type="1">
<li><p>Deployment Begin Date is greater than Deployment End Date.</p></li>
<li><p>Combat Payment Begin Date is greater than Combat Pay End Date.</p></li>
<li><p>Beginning Date of Service is greater than Ending Date of Service.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>896585</td>
<td>Select and Display Supporting Document Short Name on the Demographics--&gt;Personal screen (Manage Person Demographics)</td>
<td><p>The following changes to the Manage Person Demographics are implemented:</p>
<p>Select and display supporting document Short Name on the Demographics--&gt;Personal screen (Manage Person Demographics).</p></td>
</tr>
<tr class="even">
<td>896586</td>
<td>When Supporting Document Short Name is sent from MVI (Process Update Persons Date of Death)</td>
<td><p>The following changes for Supporting Document Short Name from MVI (Process Update Persons Date of Death) are implemented:</p>
<ol type="1">
<li><p>The Enrollment System retrieves the Supporting Document Short Name via the Retrieve Primary View traits from MVI.</p></li>
</ol>
<ol start="37" type="1">
<li><p>When the Date of Death information comes from MVI, the Enrollment System populates the Supporting Document Short Name field with the retrieved value.</p></li>
</ol>
<p><strong>Note:</strong> When the Date of Death information comes from MVI, there will be no popup of the Supporting Document Short Name Description.</p></td>
</tr>
<tr class="odd">
<td>896587</td>
<td>Supporting Document Short Name and VistA</td>
<td><p>The following changes for Supporting Document Short Name and VistA are implemented:</p>
<ol type="1">
<li><p>ES does not send Supporting Document Short Name information to VistA.</p></li>
</ol>
<ol start="38" type="1">
<li><p>ES ignores the Supporting Document Short Name information sent by VistA in a Z07 message.</p></li>
</ol>
<p><strong>Note:</strong> In a future release, the requirement will probably change to "When Supporting Document Short Name information is updated in VistA, a Z07 message shall not get updated and sent to ES."</p></td>
</tr>
<tr class="even">
<td>896588</td>
<td>Display Supporting Document Short Name on the Demographics --&gt; History screen (Manage Person Demographics)</td>
<td><p>The following changes for supporting documentation are implemented:</p>
<ol type="1">
<li><p>Display Supporting Document Short Name on the Demographics --&gt; History screen (Manage Person Demographics)</p></li>
</ol>
<ol start="39" type="1">
<li><p>ES displays the Supporting Document Short Name under the Death Source Notification field on the Demographics--&gt;History screen.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>902884</td>
<td>Implementation of the eMIS Phase 2</td>
<td><p>The following eMIS Phase 2 changes are implemented:</p>
<ol type="1">
<li><p>eMIS Rule for retrying MVI when no EDIPI received:</p></li>
</ol>
<ol type="a">
<li><p>ESM to retry within (x minutes) when no response from MVI.</p></li>
</ol>
<ol start="4" type="a">
<li><p>(x = amount of time estimated to allow MVI to process response from DoD Manpower Data Center (DMDC)</p></li>
</ol>
<ol start="40" type="1">
<li><p>eMIS Notification when MVI does not return EDIPI:<br />
Need Veteran applications to be put in "Queried – No Data Received" when the MVI search does not return an EDIPI and a call to eMIS is not possible.</p></li>
<li><p>Combined Requirement: (Process Send Receive MSDS Service)</p></li>
</ol>
<ol type="a">
<li><p>Create a new eMIS Query Status – "No Member ID/eMIS Not Queried".</p></li>
</ol>
<ol start="5" type="a">
<li><p>If the Person record does not have a Member ID (EDIPI) and if a call to MVI has not returned a Member ID, the ES retries the call to the MVI Web Service for 2 tries within 24 hours. If after 2 tries, the record still does not have an EDIPI, the Military Service Data (eMIS) request status is set to "No Member ID/eMIS Not Queried" and creates an HEC Member Service Episode (MSE) record out of the site data.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>919103</td>
<td>View eMIS Raw Data</td>
<td><p>The eMIS raw data displays when an ES User clicks on the 'View' Raw Data hyperlink in the eMIS Message Log for the following categories:</p>
<ol type="1">
<li><p>DEPLOYMENTS</p></li>
</ol>
<ol start="42" type="1">
<li><p>DISABILITIES</p></li>
<li><p>MILITARY SERVICE ELIGIBILITY INFORMATION</p></li>
<li><p>RETIREMENTS</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>919104</td>
<td>View Parsed eMIS Data</td>
<td>An option is provided on the eMIS Parsed Message screen for the ES User to return to the eMIS Message Log screen.</td>
</tr>
<tr class="even">
<td>919105</td>
<td>View eMIS Message Response Details</td>
<td><p>The following eMIS Message Response Details display:</p>
<ol type="1">
<li><p>The eMIS message response details for the message when a user clicks on the 'View' Response Details hyperlink in the eMIS Message Log.</p></li>
</ol>
<ol start="45" type="1">
<li><p>A hyperlink on the eMIS Message Response Details screen to allow the ES User to return to the eMIS Message Log.</p></li>
<li><p>A hyperlink on the eMIS Message Response Details screen to allow the ES User to view the message in parsed data format.</p></li>
<li><p>A hyperlink on the eMIS Message Response Details screen to allow the ES User to view the message in raw data format.</p></li>
<li><p>The following information on the eMIS Message Response Details screen:</p></li>
</ol>
<ol type="a">
<li><p>Member ID</p></li>
</ol>
<ol start="6" type="a">
<li><p>Message Type (Deployments, Disabilities, Military Service Eligibility Information, Retirements)</p></li>
<li><p>Source System Name</p></li>
<li><p>Transaction ID</p></li>
<li><p>Response Date</p></li>
<li><p>Response Code</p></li>
<li><p>Error Code</p></li>
<li><p>Error Description</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>919106</td>
<td>View eMIS Message Log</td>
<td><p>The following displays on the eMIS Message Log screen:</p>
<ol type="1">
<li><p>Response Date/Time</p></li>
</ol>
<ol start="49" type="1">
<li><p>Status</p></li>
<li><p>Member ID</p></li>
<li><p>A hyperlink to view the message as raw data</p></li>
<li><p>A hyperlink to view the message response details</p></li>
</ol></td>
</tr>
<tr class="even">
<td>922141</td>
<td>Send CC Eligibility to CCN Contractor On-demand From Community Care Determination Screen</td>
<td>The Community Care (CC) Eligibility to CCN Contractor On-demand is sent from the Community Care Determination Screen.</td>
</tr>
<tr class="odd">
<td>922176</td>
<td>Triggering the Sending of Veterans Information to CCN Contractor</td>
<td><p>Sending of Veterans Information to Community Care Network (CCN) Contractor is triggered for the following:</p>
<ol type="1">
<li><p>When the Enrollment System determines a new Veteran's Choice Eligibility (VCE) mileage eligibility for a Veteran within the Veterans Choice and Enrollment Determination process.</p></li>
</ol>
<ol start="53" type="1">
<li><p>When a record to the CCN Contractors is triggered from CC Eligibility and Enrollment Determination via a process update or from the CC Override Changes under the following conditions:</p></li>
</ol>
<ol type="a">
<li><p>The Veteran becomes no longer eligible.</p></li>
</ol>
<ol start="13" type="a">
<li><p>The Veteran becomes eligible for Community Care/Veterans Choice program.</p></li>
<li><p>The Veteran becomes eligible for Community Care/Veterans Choice services based on mileage eligibility.</p></li>
<li><p>The Veteran becomes eligible for Community Care/Veterans Choice services based on hardship eligibility.</p></li>
<li><p>The Veteran was mileage eligible for Community Care/Veterans Choice services and becomes mileage ineligible.</p></li>
</ol>
<ol start="54" type="1">
<li><p>When a Veteran's Permanent Mailing Address/Temporary Mailing Address or Residential Address changes via the Enrollment System UI or from receipt from HL7 or a Web Service, ES sends the record containing both the active mailing address and Residential Address to the CCN Contractors.</p></li>
<li><p>Upon changes to demographic information, by an Enrollment System user, or changes from the HL7 or Web Services, the Enrollment System sends the Veteran record to the CCN Contractors.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>935058</td>
<td>System Parameters and System Administrator Functions (Manage System Parameters)</td>
<td><p>The following changes are implemented for the System Parameters and System Administrator functions:</p>
<ol type="1">
<li><p>The System Administrator is able to set a system parameter that lists the date when the Supporting Document Short Date functionality was implemented. This system parameter is called 'Date of Death Supporting Document Start Date'.</p></li>
</ol>
<ol start="56" type="1">
<li><p>The 'Date of Death Supporting Document Start Date' parameter displays on the Admin --&gt; System Parameters page.</p></li>
<li><p>The 'Date of Death Supporting Document Start Date' parameter is set to the following values:</p></li>
</ol>
<ol type="a">
<li><p>Data Type is set to Alphanumeric.</p></li>
</ol>
<ol start="17" type="a">
<li><p>Data Length is set to 10.</p></li>
<li><p>Data Unit is set to Date.</p></li>
</ol>
<ol start="58" type="1">
<li><p>The default value for the Date of Death Supporting Document Start Date is changed to the system date.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>940177</td>
<td>Access the SDS Lookup Tables Page through the ES Login page</td>
<td>The Standard Data Service (SDS) Lookup Tables Page is accessed through the ES Login page.</td>
</tr>
<tr class="even">
<td>940178</td>
<td>View the SDS Lookup Tables Page after clicking the SDS Table Lookup Icon</td>
<td>The SDS Lookup Tables Page is viewed after clicking the SDS Table Lookup Icon.</td>
</tr>
<tr class="odd">
<td>940179</td>
<td>Look Up and View an SDS Table on the SDS Lookup Tables Page</td>
<td>The SDS Table is viewed on the SDS Lookup Tables Page.</td>
</tr>
<tr class="even">
<td>941907</td>
<td>Display CCN Contractor Change History Screen</td>
<td><p>The Community Care Network (CCN) Contractor Change History screen is displayed under the following conditions:</p>
<ol type="1">
<li><p>When the user selects the "VIEW HISTORICAL CONTRACTOR INFO" link from the Edit CCN Contractor screen.</p></li>
</ol>
<ol start="59" type="1">
<li><p>When the CCN Contractor Change History screen conforms to the standard History screen functionality.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>941908</td>
<td>Display CCN State Region Assignment Change History Screen</td>
<td><p>The CCN State Region Assignment Change History screen is displayed under the following conditions:</p>
<ol type="1">
<li><p>When the user selects the "VIEW HISTORICAL ASSIGNMENTS" hyperlink from the Manage State Region Assignment screen.</p></li>
</ol>
<ol start="60" type="1">
<li><p>The CCN State Region Assignments Change History conforms to the standard History screen functionality.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>942779</td>
<td>Reflect Correct Name of Health Benefit Plan – ES</td>
<td>The 'Name' of one of the Veteran Health Benefit Plan with Coverage Code (VC01004) is corrected from "Veteran Plan – VC – Unusual and Excessive Burden" to "Veteran Plan - VC - Unusual or Excessive Burden" in ES.</td>
</tr>
<tr class="odd">
<td>945340</td>
<td>Enrollment Application Date Validation when Changing Cancelled/Declined or Closed Indicators in ES</td>
<td>The Enrollment Application Date is validated when changing Cancelled/Declined or Closed Indicators in ES.</td>
</tr>
<tr class="even">
<td>945343</td>
<td>Restart the Manage Pending Clocks after Receiving a New Application.</td>
<td>The Manage Pending Clocks restart after receiving a new application.</td>
</tr>
<tr class="odd">
<td>945344</td>
<td>Triggering Initial Incomplete Application Letter After Receiving New Application</td>
<td>The Initial Incomplete Application Letter is triggered after receiving a new application.</td>
</tr>
<tr class="even">
<td>945345</td>
<td>View Prior Enrollment After New Application</td>
<td>Verified status after the Veteran has "re-applied" displays in the Initial Enrollment and Most Recent Enrollment sections.</td>
</tr>
<tr class="odd">
<td>945346</td>
<td>Check Exclusion Conditions After New Application</td>
<td>The Exclusion Conditions is checked after a new application.</td>
</tr>
<tr class="even">
<td>945356</td>
<td>eMIS Future Discharge Date Edit</td>
<td>An ES user or the eMIS system is only permitted to update the Future Discharge Date and Source of Information that were last updated by eMIS.</td>
</tr>
<tr class="odd">
<td>945357</td>
<td>Service Separation Date Received from eMIS</td>
<td><p>The following changes are implemented for Service Separation Date received from eMIS:</p>
<ol type="1">
<li><p>The Future Discharge Date Maturity Clock is terminated when there is an existing Future Discharge Date and a Service Separation Date is received from eMIS.</p></li>
</ol>
<ol start="61" type="1">
<li><p>The Future Discharge Date, Source of Information, and Other Explanation are moved to history when there is an existing Future Discharge Date and a Service Separation Date is received from eMIS.</p></li>
<li><p>The Future Discharge Date, Source of Information, and Other Explanation are set to NULL when there is an existing Future Discharge Date and a Service Separation Date is received from eMIS.</p></li>
<li><p>The Source of Change is set to the eMIS system job name when a Service Separation Date is received from the Broker and there is an existing Future Discharge Date.</p></li>
<li><p>The Determine Eligibility is triggered when there is an existing Future Discharge Date and a Service Separation Date is received from eMIS.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>945379</td>
<td>Trigger Reminder Incomplete Application Letters</td>
<td>Reminder Incomplete Application Letters are automatically triggered 326 days after an IPN (Initial Pending Notification) letter is mailed (40 days prior to the 366th day).</td>
</tr>
<tr class="odd">
<td>945380</td>
<td>Send Reminder Incomplete Application Letters to Print Vendor</td>
<td><p>The Reminder Incomplete Application Letters are sent to Print Vendor for the following conditions:</p>
<ol type="1">
<li><p>All letters successfully triggered (Without a status of "Reject at HEC") are added to the Communications Log with a status of "Send to Print Vendor".</p></li>
</ol>
<ol start="65" type="1">
<li><p>Upon creating the letter batch file to the print vendor, ES checks to ensure the enrollment status is still applicable to the letter being sent.</p></li>
<li><p>ES records each sent letter in the "Previously Mailed" (Communications Log) tab.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>945381</td>
<td>Historical Pending Application Cleanup</td>
<td>ES automatically executes a Clean Up process of the Historical Pending Application.</td>
</tr>
<tr class="odd">
<td>945382</td>
<td>Reminder Incomplete Application Email Bulletin</td>
<td>The email bulletin/notification is triggered when the Reminder Incomplete Application Letters are sent and ready to be processed by the print vendor.</td>
</tr>
<tr class="even">
<td>947075</td>
<td>Implement local solution to replace PSIM</td>
<td>Implement local solution to replace PSIM to support reports and Community Care.</td>
</tr>
<tr class="odd">
<td>947825</td>
<td>Maintain the Enrollment System Application by providing defect fixes for prior ES enhancements.</td>
<td>Maintain the Enrollment System application by providing defect fixes for prior ES enhancements.</td>
</tr>
<tr class="even">
<td>947826</td>
<td>Maintain the Enrollment System Application by providing defect fixes for prior ESCC enhancements.</td>
<td>Maintain the Enrollment System application by providing defect fixes for prior ESCC enhancements.</td>
</tr>
<tr class="odd">
<td>947834</td>
<td>Maintain the Enrollment system application by providing minor enhancements, defect fixes, and routine maintenance.</td>
<td>Maintain the Enrollment System application by providing minor enhancements, defect fixes, and routine maintenance.</td>
</tr>
<tr class="even">
<td>954378</td>
<td>Configurable Use of VET360</td>
<td>The Enrollment System is configured to use either eCIS or VET360 Web Service.</td>
</tr>
<tr class="odd">
<td>959032</td>
<td>Receive Residential Address from VistA and Perform Coding Accuracy Support System (CASS) Validation</td>
<td>The Residential Address is received from VistA and CASS Validation is performed.</td>
</tr>
<tr class="even">
<td>959034</td>
<td>Send Residential Address Changes to VistA</td>
<td>The Residential Address changes are sent to VistA.</td>
</tr>
<tr class="odd">
<td>960513</td>
<td>Compare the "Current PG" column to each "New PG" for expected system behavior.</td>
<td>Compare the "Current Priority Group (PG)" column to each "New PG" column for expected system behavior.</td>
</tr>
<tr class="even">
<td>965432</td>
<td>TPA Positive File To Include Demographic Changes</td>
<td>The Third Party Administrator (TPA) Positive File includes demographic changes.</td>
</tr>
<tr class="odd">
<td>972132</td>
<td>Configurable Parameter for CCN Activation</td>
<td>A new system parameter "CCN Enabled =N" is created to control the sending of records to the CCN Contractors.</td>
</tr>
</tbody>
</table>

Table : Enhancements and Modifications in the 5.1 Release

## Defects and Fixes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 2 lists the defects and fixes and corresponding RTC Change and Configuration Management (CM) numbers included in ES 5.1.

<table>
<caption><p>Table : Defects and Fixes in ES 5.1</p></caption>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th>RTC<br />
CM #</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>191490</td>
<td><p><strong>Defect:</strong> Remove "Placeholder" verbiage from Combat Service Location header on MS screen.</p>
<p><strong>Fix:</strong> Change code to remove "Placeholder" text.</p></td>
</tr>
<tr class="even">
<td>437471</td>
<td><p><strong>Defect:</strong> eMIS: Military Service Data Sharing (MSDS) Query Status stays in 'Queried - Pending Response' if record has no Electronic Data Interchange Personal Identifier (EDIPI).</p>
<p><strong>Fix:</strong> The Clock process batch job that runs 72 hours after the processing of the query cleans up this error.</p></td>
</tr>
<tr class="odd">
<td>497690</td>
<td><p><strong>Defect:</strong> ES should not upload Member Service Episode (MSE) from eMIS if all periods are guard/reserve with ADT.</p>
<p><strong>Fix:</strong> Code change to add a check in the episodes loop to only store the episode data if at least one non ADT Guard Reserve Service Period is found.</p></td>
</tr>
<tr class="even">
<td>509411</td>
<td><p><strong>Defect:</strong> Section 508: Informative Message windows are generated but do not receive focus and are not voiced instantaneously.</p>
<p><strong>Fix:</strong> Updated the "informationMessage.jsp" file to get focus when success message displayed.</p></td>
</tr>
<tr class="odd">
<td>514005</td>
<td><p><strong>Defect:</strong> Health Benefit Plan description needs to display full description on Active HBP.</p>
<p><strong>Fix:</strong> Updated JSP file to display the full content of description when you click on the plan name.</p></td>
</tr>
<tr class="even">
<td>516020</td>
<td><p><strong>Defect:</strong> Address with Address Line 1 and Address Line 2 information is being changed after Coding Accuracy Support System (CASS) validation.</p>
<p><strong>Fix:</strong> SQA re-tested this defect and it was working properly. No code changes were needed.</p></td>
</tr>
<tr class="odd">
<td>516036</td>
<td><p><strong>Defect:</strong> P.O. Box is entered on Address Line 1 (After the valid street address information) is getting changed after Coding Accuracy Support System (CASS) validation.</p>
<p><strong>Fix:</strong> This was an issue with Electronic Contact Information Service (eCIS), which has since been fixed, once ES points to the new eCIS version.</p></td>
</tr>
<tr class="even">
<td>516076</td>
<td><p><strong>Defect:</strong> Edit/Add Residential Address in ES is triggering an ORU Z05.</p>
<p><strong>Fix:</strong> Code changes to enable Z05 to be generated when a residential address is processed.</p></td>
</tr>
<tr class="odd">
<td>521866</td>
<td><p><strong>Defect:</strong> User has to refresh/reopen the record in order to see the CASS certified status updated.</p>
<p><strong>Fix:</strong> Moved the logic in the code to reload the person once an address is updated.</p></td>
</tr>
<tr class="even">
<td>533303</td>
<td><p><strong>Defect:</strong> Pending Applications Scheduled Report displays an Application Error when entering an invalid Day value.</p>
<p><strong>Fix:</strong> Updated Validation code to validate day of month.</p></td>
</tr>
<tr class="odd">
<td>541162</td>
<td><p><strong>Defect:</strong> If eCIS does not send back the result to ES after the retry, CASS Status should set to Not Checked.</p>
<p><strong>Fix:</strong> This was an issue with eCIS, which has since been fixed, once ES points to the new eCIS version.</p></td>
</tr>
<tr class="even">
<td>544575</td>
<td><p><strong>Defect:</strong> ES should not allow to Save Source of Change as "VADIR" or "WebHINQ" from UI.</p>
<p><strong>Fix:</strong> Updated JavaScript parameter to display message if user selects VADIR or WEBHINQ as source of change.</p></td>
</tr>
<tr class="odd">
<td>555414</td>
<td><p><strong>Defect:</strong> 508_Comminity Care Override Confirmation messages do not receive focus and are not voiced instantaneously.</p>
<p><strong>Fix:</strong> Updated the "informationMessage.jsp" file to get focus when success message displays.</p></td>
</tr>
<tr class="even">
<td>556053</td>
<td><p><strong>Defect:</strong> Use Station Name provided by Planning System Support Group (PSSG).</p>
<p><strong>Fix:</strong> ES and Extract, Transform and Load (ETL) code were changed to show the actual Station name from PSSG.</p></td>
</tr>
<tr class="odd">
<td>556256</td>
<td><p><strong>Defect:</strong> Station Name from CDW is different than in SDS table.</p>
<p><strong>Fix:</strong> Implemented Data Base changes to add CDW_STATION_NAME column to WQAITTIME table.</p></td>
</tr>
<tr class="even">
<td>560831</td>
<td><p><strong>Defect:</strong> Missing 'Total Dependents' field in Financials for IY2014 and older.</p>
<p><strong>Fix:</strong> Updated JSP file to display total dependents in current financial assessment.</p></td>
</tr>
<tr class="odd">
<td>567215</td>
<td><p><strong>Defect:</strong> ES Future Discharge Date (FDD) is not cleared in ES after the broker is queried and did not return the FDD.</p>
<p><strong>Fix:</strong> Code changes to include checks on FDD overlaps.</p></td>
</tr>
<tr class="even">
<td>570280</td>
<td><p><strong>Defect:</strong> UI Esoteric Issue -CC Determination Page - Nearest VACAA Facility needs a blue box.</p>
<p><strong>Fix:</strong> Updated the "vcDetermination.jsp" to fix display Blue box in front of VACAA Facility, Fix borders and change blue asterisks.</p></td>
</tr>
<tr class="odd">
<td>570284</td>
<td><p><strong>Defect:</strong> UI Esoteric Issue - CC Determination Page, boxes and borders need to be cleaned up.</p>
<p><strong>Fix:</strong> Updated the "vcDetermination.jsp" to fix display Blue box in front of VACAA Facility, Fix borders and change blue asterisks.</p></td>
</tr>
<tr class="even">
<td>570608</td>
<td><p><strong>Defect:</strong> UI Esoteric Issue: CC Determination Screen: Need blue asterisks for Required Fields.</p>
<p><strong>Fix:</strong> Updated the "vcDetermination.jsp" to fix display Blue box in front of VACAA Facility, Fix borders and change blue asterisks.</p></td>
</tr>
<tr class="odd">
<td>574493</td>
<td><p><strong>Defect:</strong> Strip out special characters from CITY field on addresses.</p>
<p><strong>Fix:</strong> Updated the "addressform.java" class to replace special characters.</p></td>
</tr>
<tr class="even">
<td>574518</td>
<td><p><strong>Defect:</strong> DOD_ES should not allow to "add or modify" Date of Death prior to Application Date.</p>
<p><strong>Fix:</strong> Update the "demographicValidation.irl" to validate Date of Death cannot be before Enrollment Application Date.</p></td>
</tr>
<tr class="odd">
<td>587735</td>
<td><p><strong>Defect:</strong> Missing Label of the Health Benefit Plan in HBP historical Page.</p>
<p><strong>Fix:</strong> Changed the "label.planName" to show "Health Benefit Plan".</p></td>
</tr>
<tr class="even">
<td>598870</td>
<td><p><strong>Defect:</strong> On the CCN_Daily file the temporary phone number shows up when Active Permanent Mailing Address is on the file.</p>
<p><strong>Fix:</strong> Code changes to add a conditional to the query in "batchprocess.hbm.xml" to check and only insert temp phone number in file when temp address is active. This prevents the temporary phone number from showing up when the active permanent mailing address on the file.</p></td>
</tr>
<tr class="odd">
<td>598873</td>
<td><p><strong>Defect:</strong> When user add/update Temporary Mailing Address from VistA, ES does not trigger message to (Community Care Network (CCN).</p>
<p><strong>Fix:</strong> The External Events (in this case Z07 / VOA) are captured and the Person is marked to be sent to CCN.</p></td>
</tr>
<tr class="even">
<td>600705</td>
<td><p><strong>Defect:</strong> CCN 4.0 SQA Edit CCN Contractors capability permission - When permission is not selected, all users should be able to view Manage CCN Contractors screen.</p>
<p><strong>Fix:</strong> Enabled functionality that was previously dormant and this issue was successfully validated.</p></td>
</tr>
<tr class="odd">
<td>603768</td>
<td><p><strong>Defect:</strong> When processing the record for geocoded data from Planning System Support Group (PSSG), the time is one hour behind.</p>
<p><strong>Fix:</strong> Code changed to replace DATEADD with just the GETDATE.</p></td>
</tr>
<tr class="even">
<td>604296</td>
<td><p><strong>Defect:</strong> Community Care (CC) history page needs to show those changes were associated with a new determination that was made on the same history page.</p>
<p><strong>Fix:</strong> Code changed to load history from VCELIGIBILITY_H instead of PERSON_H table.</p></td>
</tr>
<tr class="odd">
<td>605308</td>
<td><p><strong>Defect:</strong> Letter 901 triggered twice when VCE change close to the 900/901 batch process scheduled time.</p>
<p><strong>Fix:</strong> Updated the code logic to pick up the records preventing it from triggering of the Letter 901 twice.</p></td>
</tr>
<tr class="even">
<td>607215</td>
<td><p><strong>Defect:</strong> Application Error on Demographics page when Temporary Address has imprecise date.</p>
<p><strong>Fix:</strong> Code changes to handle the year and year/month variations on start and end dates on Confidential and Temporary Address entries which were causing the errors reported.</p></td>
</tr>
<tr class="odd">
<td>631000</td>
<td><p><strong>Defect:</strong> Updating Temporary Mailing Address start/end date does not trigger ORUZ05.</p>
<p><strong>Fix:</strong> Updated the "ContactInformationInputParameter.java" to check Temporary Address change for start and end date.</p></td>
</tr>
<tr class="even">
<td>632112</td>
<td><p><strong>Defect:</strong> When temporary mailing address has an imprecise date then user cannot open demographics tab.</p>
<p><strong>Fix:</strong> Code changes to handle the year and year/month variations on start and end dates on confidential and temporary address entries which were causing the errors reported.</p></td>
</tr>
<tr class="odd">
<td>636210</td>
<td><p><strong>Defect:</strong> When users change the name, birthdate or gender on the CC record, the record should send to Third Party Administrator (TPA).</p>
<p><strong>Fix:</strong> Updated the Person Traits event to mark the Veteran to be sent to TPA</p></td>
</tr>
<tr class="even">
<td>636923</td>
<td><p><strong>Defect:</strong> PSSG ignore the record for geocoding if there is duplicate record.</p>
<p><strong>Fix:</strong> The Extract, Transform and Load (ETL) code is changed to check for duplicates and updates instead of insert for the existing Person.</p></td>
</tr>
<tr class="odd">
<td>637181</td>
<td><p><strong>Defect:</strong> Manage CCN Contractor/Manage States/Regions - error message displayed after Update button is clicked.</p>
<p><strong>Fix:</strong> Implemented code changes so the update happens only in one session.</p></td>
</tr>
<tr class="even">
<td>637447</td>
<td><p><strong>Defect:</strong> ES is not processing the re-enrollment action coming from VistA REE when a Veteran has Cancel/Decline status.</p>
<p><strong>Fix:</strong> Code changes to include processing the incoming reason and received enrollment data from VistA REE when a Veteran has Cancel/Decline status.</p></td>
</tr>
<tr class="odd">
<td>637830</td>
<td><p><strong>Defect:</strong> Pending Application CSV Report does not display the leading zeros.</p>
<p><strong>Fix:</strong> Added single quotes to the Social Security Number (SSN) for both Total Closed Application and Pending Application report to display leading zeros.</p></td>
</tr>
<tr class="even">
<td>638492</td>
<td><p><strong>Defect:</strong> Manage CCN Contractor/CCN Contractor detail screen - User without Edit CCN Contractor permission - changes needed for the current screen.</p>
<p><strong>Fix:</strong> Made the fields read only if the permission is not available, created a link to say "Return to CCN Contractors" in place of the "Cancel" button and changed the tile of the screen to say "View CCN Contractors" if the "Edit Contractors" permission is not available.</p></td>
</tr>
<tr class="odd">
<td>643062</td>
<td><p><strong>Defect:</strong> Small % of eCIS requests failing for illegal escape.</p>
<p><strong>Fix:</strong> Added handling of illegal escape char in eCIS request JSON, so that an "Invalid" ("F") type of eCIS response is sent back as if it was failed address validation and will be handled by the Inbound process properly.</p></td>
</tr>
<tr class="even">
<td>652772</td>
<td><p><strong>Defect:</strong> ES sending address validation request to eCIS with changes only in audit fields.</p>
<p><strong>Fix:</strong> Code Updates to change the object comparison method to use "SimpleAddress.compareTo" so that only required fields are checked.</p></td>
</tr>
<tr class="odd">
<td>661826</td>
<td><p><strong>Defect:</strong> Clocks not always starting after being scheduled.</p>
<p><strong>Fix:</strong> Code changed of the API call to" this.scheduler.scheduleJob(jobDetail, trigger )" to start the clock after being scheduled.</p></td>
</tr>
<tr class="even">
<td>670947</td>
<td><p><strong>Defect:</strong> Merge Fortify Fixes of ES Mars Dev code version to ES Pluto Dev version build 6 stream.</p>
<p><strong>Fix:</strong> Encode by using the "ESAPI" encode method as per the Fortify scan findings. Resolve the "Unreleased Resource Database finding", the "Null Dereference" finding. Code changes to not log SQL with the confidential info and validate file name before using it to resolve the "Fortify Path Manipulation finding".</p></td>
</tr>
<tr class="odd">
<td>679314</td>
<td><p><strong>Defect:</strong> Throwing Application error while scheduling a report.</p>
<p><strong>Fix:</strong> Code changes for the durable parameter which is set to true for the quartz scheduler to add a new job.</p></td>
</tr>
<tr class="even">
<td>679409</td>
<td><p><strong>Defect:</strong> IRS ACA corrections for income year 2017 are failing due to IRS change in annual indicator.</p>
<p><strong>Fix:</strong> Removed unnecessary checks for coverage annual indicator that was removed previously from the bulk submission original payload data.</p></td>
</tr>
<tr class="odd">
<td>680709</td>
<td><p><strong>Defect:</strong> Manage CCN Contractor/Add CCN Contractor date fields do not follow format with 'mm/dd/yyyy' listed.</p>
<p><strong>Fix:</strong> Added hint label "(mm/dd/yyyy)", on both start date and end date fields.</p></td>
</tr>
<tr class="even">
<td>684233</td>
<td><p><strong>Defect:</strong> ES is uploading data from Enterprise Military Information Service (eMIS), but displaying a "No response" in eMIS Messages search screen.</p>
<p><strong>Fix:</strong> This issue was resolved with the fix to the eMIS client interface to display the "Successful" status.</p></td>
</tr>
<tr class="odd">
<td>691230</td>
<td><p><strong>Defect:</strong> Fix SSN issue with ZDP in Z10 message.</p>
<p><strong>Fix:</strong> Updated the "ECMS_framework/src/gov/va/med/fw/hl7/segment/ZDP.java" file to prevent the Z10 message from failing when processed by VistA.</p></td>
</tr>
</tbody>
</table>

Table : Defects and Fixes in ES 5.1

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 3 lists identified defects that remain open in this release.

<table>
<caption><p>Table : Open Defects in the ES 5.1 Release</p></caption>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th>RTC<br />
CM #</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>544339</td>
<td>ES_508_Screen reader does not announce that the highlighted fields in red have errors.</td>
</tr>
<tr class="even">
<td>662726</td>
<td>SSN and/or Pseudo SSN does not have blue asterisk/star for required field for Adding Dependent</td>
</tr>
<tr class="odd">
<td>668402</td>
<td>The NEW eMIS query status "No Member ID/eMIS Not Queried" is NOT being displayed on Eligibility screen.</td>
</tr>
<tr class="even">
<td>672305</td>
<td>ES 6.0_MP: Total Closed Application Report shows IPN DATE with a value of NULL when a DATE is expected.</td>
</tr>
<tr class="odd">
<td>680709</td>
<td>508 - TS 164873 Manage CCN Contractor/Add CCN Contractor date fields do not follow format with 'mm/dd/yyyy' listed.</td>
</tr>
<tr class="even">
<td>681161</td>
<td>508: Some fields that generate an error are neither read with error nor marked as error.</td>
</tr>
<tr class="odd">
<td>681220</td>
<td>508: When fields become dynamically required and generate an error; screen reader does not announce error in fields.</td>
</tr>
<tr class="even">
<td>682338</td>
<td>Manage CCN Contractors - Application error displayed when a field (any field) for an existing contractor is updated and 1 or more regions are removed.</td>
</tr>
<tr class="odd">
<td>682557</td>
<td>eMIS 24 hour clock is not attempting to send a retry call when an initial attempt is failed due to system issues.</td>
</tr>
<tr class="even">
<td>684543</td>
<td>ES 6.0_MP: A second entry for 742 - 654 Reminder Letter was automatically triggered with an address update.</td>
</tr>
<tr class="odd">
<td>684579</td>
<td>ES should be displaying an error on the UPDATE if future date entered in Language Entry date field.</td>
</tr>
<tr class="even">
<td>687568</td>
<td>ES 6.0_MP: Incorrect error message displayed upon re-application of a Cancel Declined record with previous Enrollment Status of Pending; Purple Heart Unconfirmed.</td>
</tr>
<tr class="odd">
<td>690211</td>
<td>Reason For Early Separation is NOT getting updated when the "Narrative Reason For Separation Txt " received from eMIS is different from the text displayed in ES.</td>
</tr>
<tr class="even">
<td>693942</td>
<td>SDS Reference tables - Period missing from the last sentence of the body section in ES.</td>
</tr>
<tr class="odd">
<td>695065</td>
<td>ESM B6- HCA Overwrote eMIS FDD</td>
</tr>
<tr class="even">
<td>695539</td>
<td>eMIS Message Log screen is reflecting an incorrect Member ID info when searching with a Combination of "Response Status" and "Member Id".</td>
</tr>
<tr class="odd">
<td>695869</td>
<td>ES 6.0_MP: View Prior Enrollment - Initial Enrollment and Most Recent Enrollment values switched.</td>
</tr>
<tr class="even">
<td>696041</td>
<td>ES 6.0_MP: Error message for Enrollment status is missing the word " Status".</td>
</tr>
<tr class="odd">
<td>696532</td>
<td>eMIS Error Message for not entering a Report Range From Date and End Date in incorrect.</td>
</tr>
<tr class="even">
<td>696660</td>
<td>PSIM Decoupling - Hibernate Configuration Issue - Link and Move Events not included.</td>
</tr>
<tr class="odd">
<td>696990</td>
<td>ESM_5.1_ eMIS Query Status is not set to Military Service Data Rejected</td>
</tr>
</tbody>
</table>

Table : Open Defects in the ES 5.1 Release

# Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents apply to this release:

- ES 5.1 Release Notes are uploaded to the [VA Software Document Library](http://www.va.gov/vdl/) (VDL).
- Additional reference documentation related to this release is stored in RTC.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: VES Version 5.14 Release Notes

## ES Production Defects and Fixes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 3 lists the production defects and fixes and corresponding Jira issue numbers included in ES 5.14.

<table>
<caption><p><span id="_Toc55895629" class="anchor"></span>Table 3: Production Defects and Fixes in ES 5.14</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Jira Issue #</strong></th>
<th><strong>Summary</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VES-603</td>
<td><p><strong>Defect</strong>: Deleting the Mobile (Cell) Phone in VistA does not delete the Mobile (Cell) phone in VA Profile.</p>
<p><strong>Fix</strong>: Updated code so that when a Cell Phone is deleted in VistA, the Cell Phone is also deleted in VA Profile.</p></td>
</tr>
<tr class="even">
<td>VES-1358</td>
<td><p><strong>Defect</strong>: Duplicates are sent in the Community Care Network (CCN) daily file.</p>
<p><strong>Fix</strong>: Modified the CCN batch process to send current data so that duplicate entries are no longer created.</p></td>
</tr>
<tr class="odd">
<td>VES-1534</td>
<td><p><strong>Defect</strong>: The count of VHA Profiles under the "New Value" column on the View Historical Eligibility Screen is incorrect after the Veteran indicator was changed to "No" and an Ineligible Date was entered.</p>
<p><strong>Fix</strong>: Updated the screen to no longer display VHA Profiles and the count.</p></td>
</tr>
<tr class="even">
<td>VES-2298</td>
<td><p><strong>Defect</strong>: Section 508: Associate Foreign Address.</p>
<p><strong>Fix</strong>: Analysis found that the Section 508 issues reported were only occurring with the Automatic Reader in Job Access With Speech (JAWS); no coding changes needed.</p></td>
</tr>
<tr class="odd">
<td>VES-6116</td>
<td><p><strong>Defect</strong>: Deleting the Home Phone in VistA does not also delete the Home Phone in ES (if ES has multiple phones).</p>
<p><strong>Fix</strong>: Analysis found that ES works as expected based on when the delete phone number comes from VistA; ES will not delete the phone number but will send the update to VA Profile. Upon receiving back the delete response from VA Profile, ES will delete the phone number.</p></td>
</tr>
<tr class="even">
<td>VES-6704</td>
<td><p><strong>Defect</strong>: A JavaScript Error is occurring on the Agreement modal load in Staging.</p>
<p><strong>Fix</strong>: Updated JavaScript to correct the error.</p></td>
</tr>
<tr class="odd">
<td>VES-6974</td>
<td><p><strong>Defect</strong>: ES is displaying both Code and Description for "Site of Change".</p>
<p><strong>Fix</strong>: Updated code so that when the Code and Description are the same for "Site of Change", only the Code is returned.</p></td>
</tr>
<tr class="even">
<td>VES-8166</td>
<td><p><strong>Defect</strong>: Notification was not sent to VA Profile when there was an update in SW Asia condition.</p>
<p><strong>Fix</strong>: Added comparison code to check for updates in SW Asia condition so that the proper notification will be sent to VA Profile.</p></td>
</tr>
<tr class="odd">
<td>VES-8167</td>
<td><p><strong>Defect</strong>: Open work items were created in ES for a Newborn Non-Veteran record with the message "Military Service Data (MSDS Query Blocked - Identity Traits Missing)".</p>
<p><strong>Fix</strong>: Removed the MSDS validation query for Social Security Number (SSN) required records.</p></td>
</tr>
<tr class="even">
<td>VES-9141</td>
<td><p><strong>Defect</strong>: New VCEs for Collaterals and Covered Veterans need to be added to the VCE counts section of the ESCC Email Report.</p>
<p><strong>Fix</strong>: Added the new VCEs to the ESCC Email Report.</p></td>
</tr>
<tr class="odd">
<td>VES-9169</td>
<td><p><strong>Defect</strong>: Database/User Interface displays "VIET NAM" instead of "VIETNAM" in the Country dropdown.</p>
<p><strong>Fix</strong>: Updated Country dropdown to correctly display "VIETNAM".</p></td>
</tr>
<tr class="even">
<td>VES-9361</td>
<td><p><strong>Defect</strong>: Removing and adding the same Community Care Plan (CCP) with the same Effective Date in VistA is causing the ZCE segments to be out of sync with ES.</p>
<p><strong>Fix</strong>: Updated code so that the latest dates match and are in sync between ES and VistA.</p></td>
</tr>
<tr class="odd">
<td>VES-9399</td>
<td><p><strong>Defect</strong>: The CCN Daily count reported in the ESCC Email Report is incorrect when the CCN batch process is still in process.</p>
<p><strong>Fix</strong>: Modified the stored procedure code so that if a count is not present, a text "CCN batch process not complete yet" is reported.</p></td>
</tr>
<tr class="even">
<td>VES-9413</td>
<td><p><strong>Defect</strong>: Updating the Mobile (Cell) Phone in VistA is displaying a date/time related error in VA Profile.</p>
<p><strong>Fix</strong>: Analysis found that this was a time zone issue between test accounts; no code change needed.</p></td>
</tr>
<tr class="odd">
<td>VES-9859</td>
<td><p><strong>Defect</strong>: IVD Document Management: No validation error message is being displayed when a user performs an invalid date search.</p>
<p><strong>Fix</strong>: Updated code to display an error message when the user performs an invalid date search.</p></td>
</tr>
<tr class="even">
<td>VES-9949</td>
<td><p><strong>Defect</strong>: ESCC Quality Email Report: "VMBP" needs to be updated to "VHAP".</p>
<p><strong>Fix</strong>: Changed all instances of "VMBP" in the ESCC Quality Email Report to "VHAP".</p></td>
</tr>
</tbody>
</table>

<span id="_Toc55895629" class="anchor"></span>Table 3: Production Defects and Fixes in ES 5.14

## ES Sustainment Defects and Fixes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 4 lists the sustainment defects and fixes and corresponding Jira issue numbers included in ES 5.14.

<table>
<caption><p><span id="_Ref23319755" class="anchor"></span>Table 4: Sustainment Defects and Fixes in ES 5.14</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Jira Issue #</strong></th>
<th><strong>Summary</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VES-546</td>
<td><p><strong>Defect</strong>: Browser Compatibility – Chrome and Edge – Truncated text on various buttons in ES screens.</p>
<p><strong>Fix</strong>: Updated code and formatting so that the button text no longer truncates.</p></td>
</tr>
<tr class="even">
<td>VES-588</td>
<td><p><strong>Defect</strong>: A null pointer exception was found in ES version 5.8.</p>
<p><strong>Fix</strong>: Updated messaging code to correct the null value.</p></td>
</tr>
<tr class="odd">
<td>VES-590</td>
<td><p><strong>Defect</strong>: ES did not trigger IVM migration upon change from Priority Group 8G to 8D.</p>
<p><strong>Fix</strong>: Updated code to trigger IVM migration if a record moves from Priority Group 8G to any Enrolled Group.</p></td>
</tr>
<tr class="even">
<td>VES-598</td>
<td><p><strong>Defect</strong>: VBA push to ES updates new eligibility date even though the eligibility status is not changed.</p>
<p><strong>Fix</strong>: Updated rules to check current eligibility status.</p></td>
</tr>
<tr class="odd">
<td>VES-601</td>
<td><p><strong>Defect</strong>: Net Income is not calculating for Copay Tests received from VistA.</p>
<p><strong>Fix</strong>: Updated code so that Net Income and Threshold data displays in ES.</p></td>
</tr>
<tr class="even">
<td>VES-618</td>
<td><p><strong>Defect</strong>: ES does not deactivate the temporary address when "No" is answered to the VistA prompt to delete.</p>
<p><strong>Fix</strong>: Added rules for Temporary Address to the Operational Decision Manager (ODM) deploy list so that Temporary Addresses are synchronized.</p></td>
</tr>
<tr class="odd">
<td>VES-622</td>
<td><p><strong>Defect</strong>: ES is transmitting two outbound messages to the same site for the same Veteran (using a deprecated data file number (DFN)).</p>
<p><strong>Fix</strong>: Updated code so that ES properly filters out deprecated DFNs from MVI correlation profiles.</p></td>
</tr>
<tr class="even">
<td>VES-647</td>
<td><p><strong>Defect</strong>: Person Merge fails if the Veteran has Camp Lejeune eligibility.</p>
<p><strong>Fix</strong>: Updated code and comments on Camp Lejeune so that the merge no longer fails and the user interface displays the merge page if there are comments.</p></td>
</tr>
<tr class="odd">
<td>VES-1366</td>
<td><p><strong>Defect</strong>: State Codes AA, AE, AP do not allow Box number for a Residential Address.</p>
<p><strong>Fix</strong>: Updated code to exclude State Codes AA, AE, and AP from the rule blocking entry of Box numbers in Residential Address.</p></td>
</tr>
<tr class="even">
<td>VES-1394</td>
<td><p><strong>Defect</strong>: Inbound addresses pushed from VA Profile are being added to empty/locked enrollment records.</p>
<p><strong>Fix</strong>: Updated code to discard address updates for any record with no enrollment determination.</p></td>
</tr>
<tr class="odd">
<td>VES-4126</td>
<td><p><strong>Defect</strong>: Browser Compatibility: VHIC button is not greyed out in Chrome.</p>
<p><strong>Fix</strong>: Updated style sheet so that the VHIC button is greyed out in Chrome and Edge browsers.</p></td>
</tr>
<tr class="even">
<td>VES-6698</td>
<td><p><strong>Defect</strong>: 5.13.0 Fortify: Null Dereference.</p>
<p><strong>Fix</strong>: Modified rules and code to no longer dereference a null pointer.</p></td>
</tr>
<tr class="odd">
<td>VES-6699</td>
<td><p><strong>Defect</strong>: 5.13.0 Fortify: Log Forging.</p>
<p><strong>Fix</strong>: Updated code to correct the log forging issue.</p></td>
</tr>
<tr class="even">
<td>VES-6700</td>
<td><p><strong>Defect</strong>: 5.13.0 Fortify: Unreleased Resource: Streams.</p>
<p><strong>Fix</strong>: Updated code to release the resource.</p></td>
</tr>
<tr class="odd">
<td>VES-7055</td>
<td><p><strong>Defect</strong>: ES is producing outbound Health Level 7 (HL7) messages to 200CRNR because that station was added as a type of VAMC; the messages are piling up in HealthConnect.</p>
<p><strong>Fix</strong>: Updated ES to filter out 200CRNR from the outbound builder since there is no VistA station to receive these messages.</p></td>
</tr>
<tr class="even">
<td>VES-7081</td>
<td><p><strong>Defect</strong>: 5.13.0 Fortify: Password Management - 16 issues.</p>
<p><strong>Fix</strong>: Analysis found that the affected configuration file is no longer used in Production. No code changes were necessary.</p></td>
</tr>
<tr class="odd">
<td>VES-7144</td>
<td><p><strong>Defect</strong>: When the VCE recalculation job updates a record that has both a traits change and a VCE change, it intermittently creates two separate entries to send to the CCN with different VCE statuses for the same person in the same file.</p>
<p><strong>Fix</strong>: Modified the CCN batch process to send current data so that duplicate entries are no longer created.</p></td>
</tr>
<tr class="even">
<td>VES-7155</td>
<td><p><strong>Defect</strong>: Veteran Medical Benefit Plan (VMBP)/VCE jobs are creating brand new enrollment records in an invalid status for the surviving side of a duplicate/linked/merged record when the deprecated person is the one flagged for recalculation.</p>
<p><strong>Fix</strong>: Modified code so that ES will abandon the update if the record has no enrollment record yet.</p></td>
</tr>
<tr class="odd">
<td>VES-8259</td>
<td><p><strong>Defect</strong>: Phone fields are being intermittently populated as false in the contact information adapter outbound to VA Profile. ES does not store these fields and always should be setting them as null instead of any Boolean value.</p>
<p><strong>Fix</strong>: Investigation found that there are not any phone entries with a value that directly came from ES. MPI identity transactions are updating the ES phone fields in the VA Profile phone table. No code changes were necessary.</p></td>
</tr>
<tr class="even">
<td>VES-9197</td>
<td><p><strong>Defect</strong>: 5.14.0 Fortify: JSON Injection - 1 Issue - Unvalidated input is being written into JavaScript Object Notation (JSON). This call could allow an attacker to inject arbitrary elements or attributes into the JSON entity.</p>
<p><strong>Fix</strong>: Investigation found that the JSON attributes are generated from the Java classes within ES, not derived from user input. No code changes were necessary.</p></td>
</tr>
<tr class="odd">
<td>VES-9199</td>
<td><p><strong>Defect</strong>: 5.14.0 Fortify: Privacy Violation – 3 issues.</p>
<p><strong>Fix</strong>: Investigation found that the server hosting the application is configured and operated securely according to VA hosting facility policy and that the log files in question are protected from unauthorized read and/or write access. No code changes were necessary.</p></td>
</tr>
<tr class="even">
<td>VES-9202</td>
<td><p><strong>Defect</strong>: 5.14.0 Fortify: Privacy Violation - 8 issues.</p>
<p><strong>Fix</strong>: Investigation found that the classes reported (CleanUpPendingAdjudicationProcess.java and CCNServiceLogServiceImpl.java) are not using the CCNFileData as reported. No code changes were necessary.</p></td>
</tr>
<tr class="odd">
<td>VES-9204</td>
<td><p><strong>Defect</strong>: 5.14.0 Fortify: Race Condition: Singleton Member Field - 7 issues</p>
<p><strong>Fix</strong>: Analysis found that the reported class is not a Singleton class so the rule does not apply to its members being shared between users. No code changes were necessary.</p></td>
</tr>
<tr class="even">
<td>VES-9273</td>
<td><p><strong>Defect</strong>: 5.14.0 Fortify: Weak Extensible Markup Language (XML) Schema: Unbounded Occurrences - 50 issues.</p>
<p><strong>Fix</strong>: Analysis found that ES inherits the schema and is not allowed to change it. In addition, any affected messages first pass through HealthConnect, which has validation rules that it follows before submitting to ES; therefore, the messages would fail in HealthConnect before reaching ES.</p></td>
</tr>
<tr class="odd">
<td>VES-9379</td>
<td><p><strong>Defect</strong>: Section 508: Focusable components in the content do not receive focus in an order that preserves meaning and operability.</p>
<p><strong>Fix</strong>: Updated code so that JAWS reads the fields correctly.</p></td>
</tr>
<tr class="even">
<td>VES-9496</td>
<td><p><strong>Defect</strong>: E&amp;E Service: Schema validation is failing for an Income Verification Match (IVM) request.</p>
<p><strong>Fix</strong>: Fixed the XML tags so that the IVM retrieve request is successful.</p></td>
</tr>
<tr class="odd">
<td>VES-9578</td>
<td><p><strong>Defect</strong>: The "Send IVMUpdates" request in the E&amp;E Service is throwing a Jakarta XML Binding (JAXB) unmarshalling exception error.</p>
<p><strong>Fix</strong>: Fixed an incorrect annotation in the "SendIVMUpdatesRequest.java" code that was causing the error.</p></td>
</tr>
<tr class="even">
<td>VES-9581</td>
<td><p><strong>Defect</strong>: E&amp;E Service time stamp is different in new schema than in old schema.</p>
<p><strong>Fix</strong>: Updated the format of the new schema to match the old service.</p></td>
</tr>
<tr class="odd">
<td>VES-9715</td>
<td><p><strong>Defect</strong>: E&amp;E Service missing policy effective date tag in new schema.</p>
<p><strong>Fix</strong>: Updated the format of the new schema to match the old service.</p></td>
</tr>
<tr class="even">
<td>VES-9932</td>
<td><p><strong>Defect</strong>: Bidirectional Text (BIDI): Priority Group is not updated in ES on IVM conversion; Income Effective Date is removed in ES.</p>
<p><strong>Fix</strong>: Added logic to parse incoming XML dates using alternate date formats.</p></td>
</tr>
<tr class="odd">
<td>VES-9959</td>
<td><p><strong>Defect</strong>: E&amp;E Service: "SendIVMUpdates" tag name in new service response is not matching the old service.</p>
<p><strong>Fix</strong>: Analysis found that IVM Bidirectional will work with either the old or the new tag name as long as the "&lt;acknowledgement&gt;" and "&lt;invocationDate&gt;" child elements match; no code changes needed.</p></td>
</tr>
<tr class="even">
<td>VES-9962</td>
<td><p><strong>Defect</strong>: E&amp;E Service: Extra tag is displaying in the "retrieveIVMCandidates" response in the new service.</p>
<p><strong>Fix</strong>: Analysis found that the extra tag will not break the IVM Bidirectional; no code change needed.</p></td>
</tr>
<tr class="odd">
<td>VES-10175</td>
<td><p><strong>Defect</strong>: Military service changes are being sent to VA Profile when the record is not actually changed; this causes unnecessary messaging and creation of duplicate work items in Cerner Millennium.</p>
<p><strong>Fix</strong>: Modified logic to compare only the military service eligibility object for changes and not the entire collection.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref23319755" class="anchor"></span>Table 4: Sustainment Defects and Fixes in ES 5.14

### From: VES Version 5.13 Release Notes

## Sustainment Defects and Fixes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 3 lists the sustainment defects and fixes and corresponding Jira bug numbers included in ES 5.13.

<table>
<caption><p><span id="_Ref23319755" class="anchor"></span>Table 3: Sustainment Defects and Fixes in ES 5.13</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Jira Bug #</strong></th>
<th><strong>Summary</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VES-529</td>
<td><p><strong>Defect</strong>: Browser Compatibility: Chrome and Edge - Military Service Tab - When a Veteran record with a military episode and Camp Lejeune Eligibility is pulled up in ES, it does not show the expanded view of the Camp Lejeune Eligibility section.</p>
<p><strong>Fix</strong>: Updated code to show the expanded view including all the fields on the Camp Lejeune Eligibility section of the Military Service tab.</p></td>
</tr>
<tr class="even">
<td>VES-541</td>
<td><p><strong>Defect</strong>: Browser Compatibility - Chrome only - On the Person Search screen, Military Service Number and Claim Folder Number fields under the Additional Search Criteria section are misaligned.</p>
<p><strong>Fix</strong>: Updated code to properly align the Military Service Number and Claim Folder fields under the Additional Search Criteria section.</p></td>
</tr>
<tr class="odd">
<td>VES-544</td>
<td><p><strong>Defect</strong>: Browser Compatibility: Chrome and Edge - On the "Edit Current Eligibility" screen for AAP scenario, the description does not populate for the code added under Rated SC Disabilities.</p>
<p><strong>Fix</strong>: Updated code to display all descriptions in AAP.</p></td>
</tr>
<tr class="even">
<td>VES-545</td>
<td><p><strong>Defect</strong>: Browser Compatibility: Chrome and Edge - Eligibility Tab - When a Veteran record with military episode and Camp Lejeune Eligibility is pulled up in ES, it does not show the expanded view of the Camp Lejeune Eligibility section.</p>
<p><strong>Fix</strong>: Updated code to show the expanded view including all the fields on the Camp Lejeune Eligibility section of the Eligibility tab.</p></td>
</tr>
<tr class="odd">
<td>VES-553</td>
<td><p><strong>Defect</strong>: Browser Compatibility: Report Filter by Status feature does not work on Chrome but works on IE.</p>
<p><strong>Fix</strong>: Updated code to enable the Report Filter by Status feature on both browsers.</p></td>
</tr>
<tr class="even">
<td>VES-554</td>
<td><p><strong>Defect</strong>: Browser Compatibility: Chrome - Military Service Screen: Military Service Episodes – HEC section: fields are misaligned.</p>
<p><strong>Fix</strong>: Updated code to properly align the Military Service Screen: Military Service Episodes – HEC section fields.</p></td>
</tr>
<tr class="odd">
<td>VES-555</td>
<td><p><strong>Defect</strong>: Entry of future date of birth is being allowed during Add A Person (AAP).</p>
<p><strong>Fix</strong>: Implemented validation rule to AAP: "Date of Birth Cannot Be in the Future".</p></td>
</tr>
<tr class="even">
<td>VES-580</td>
<td><p><strong>Defect</strong>: Section 508: Field label is not included in incorrect format error messages on the Completed Reports screen.</p>
<p><strong>Fix</strong>: Updated code to include field label on the incorrect format error message on the Completed Reports screen.</p></td>
</tr>
<tr class="odd">
<td>VES-586</td>
<td><p><strong>Defect</strong>: The Z05 message is failing for long city names from HCA.</p>
<p><strong>Fix</strong>: Added logic to the HCA inbound message to validate the city if the name has more than 15 characters.</p></td>
</tr>
<tr class="even">
<td>VES-600</td>
<td><p><strong>Defect</strong>: Section 508: Some active controls that generate an error are neither read with error nor marked as error (Demographics/ Personal).</p>
<p><strong>Fix</strong>: Updated code so that if Preferred Facility is not selected, an error is displayed and the field is highlighted.</p></td>
</tr>
<tr class="odd">
<td>VES-604</td>
<td><p><strong>Defect</strong>: The Programmable Logic Controller (PLC) letter response file fails to complete.</p>
<p><strong>Fix</strong>: Updated batch process to rename the file to .DONE so that the process completes.</p></td>
</tr>
<tr class="even">
<td>VES-606</td>
<td><p><strong>Defect</strong>: Errors occur when saving and opening VOA file attachments from Edit Eligibility.</p>
<p><strong>Fix</strong>: Updated code to enable VOA file attachments to be saved directly as PDFs and opened.</p></td>
</tr>
<tr class="odd">
<td>VES-632</td>
<td><p><strong>Defect</strong>: The date of birth validation message for Purple Heart is displayed when it is not expected to be displayed.</p>
<p><strong>Fix</strong>: Modified Check Birth Date / Received Date code for Purple Heart so that the validation message is not displayed when the Document Received Date field is updated with the current date.</p></td>
</tr>
<tr class="even">
<td>VES-906</td>
<td><p><strong>Defect</strong>: Browser Compatibility: Chrome and Edge - When Member ID with a trailing space is pasted in the Member ID field or a 29-character ICN is pasted in the ICN field on the Person Search page, the focus jumps to a blank field adjacent to the respective fields.</p>
<p><strong>Fix</strong>: Updated code to prevent focus from jumping to the blank fields when a Member ID with a trailing space or a 29-character ICN is entered.</p></td>
</tr>
<tr class="odd">
<td>VES-907</td>
<td><p><strong>Defect</strong>: The 10-10EZ PDF from either the Financials tab or the VOA version on the Enrollment tab is failing to generate.</p>
<p><strong>Fix</strong>: Updated code to properly load the 10-10EZ PDF from all instances.</p></td>
</tr>
<tr class="even">
<td>VES-915</td>
<td><p><strong>Defect</strong>: Browser Compatibility: Chrome Only - The row and the page counters at the top of the table on the Facilities header are displayed to the left, when they should be displayed in the middle.</p>
<p><strong>Fix</strong>: Updated code to properly display the row and page counters at the top of the table on the Facilities header.</p></td>
</tr>
<tr class="odd">
<td>VES-916</td>
<td><p><strong>Defect</strong>: Browser Compatibility: Chrome Only - Worklist Tab – The "Search Criteria" and "Search Value" fields above the "My Items" tab are displayed on the left side of the screen (no impact to functionality).</p>
<p><strong>Fix</strong>: Updated code to display the "Search Criteria" and "Search Value" fields above the "My Items" tab on the Worklist Tab on the right side of the screen.</p></td>
</tr>
<tr class="even">
<td>VES-917</td>
<td><p><strong>Defect</strong>: Browser Compatibility - Chrome and Edge – On the "My Items" subtab of the "Worklist" tab, the "Assign" button is placed away from the "Assign Selected Items to" dropdown.</p>
<p><strong>Fix</strong>: Updated code to place the "Assign" button next to the "Assign Selected Items to" dropdown menu on the "My Items" subtab of the "Worklist" tab.</p></td>
</tr>
<tr class="odd">
<td>VES-1297</td>
<td><p><strong>Defect</strong>: If a user attempts to retransmit an ORU-Z11 message, the retransmit attempt fails with the following error message: "Unable to retransmit message due to error: Failed to resend a message: Failed to build outbound ORUZ11-S message due to an exception".</p>
<p><strong>Fix</strong>: Updated code to enable retransmission of the ORU-Z11 message.</p></td>
</tr>
<tr class="even">
<td>VES-1304</td>
<td><p><strong>Defect</strong>: The "623A Notify Applicant Priority Below EGT Letter" is not being sent.</p>
<p><strong>Fix</strong>: Changed the "order-by" in the COM_MAILING_STATUS_DETAIL table.</p></td>
</tr>
<tr class="odd">
<td>VES-1849</td>
<td><p><strong>Defect</strong>: Fortify: Resolve all 1214 code warnings.</p>
<p><strong>Fix</strong>: Executed separate scan to resolve all files with the same filename in different folders.</p></td>
</tr>
<tr class="even">
<td>VES-1850</td>
<td><p><strong>Defect</strong>: A user is unable to update the "State" on the Personal screen as the field is not visible after initially adding the address.</p>
<p><strong>Fix</strong>: Updated "updateCountryFields" code so that the "State" field is visible on the Personal screen.</p></td>
</tr>
<tr class="odd">
<td>VES-1891</td>
<td><p><strong>Defect</strong>: Fortify: Unreleased Resource: Streams - 14 issues<br />
Some allocated system resources fail to be released.</p>
<p><strong>Fix</strong>: Analysis found that the allocated resources will be released even if an exception occurs.</p></td>
</tr>
<tr class="even">
<td>VES-1892</td>
<td><p><strong>Defect</strong>: Fortify: Log Forging – 1 issue<br />
Unvalidated user input could allow forging or injection of malicious content into the log.</p>
<p><strong>Fix</strong>: Created a set of legitimate log entries that correspond to different events that must be logged, and only allow logging of entries from this set (always use server-controlled values rather than user-supplied data).</p></td>
</tr>
<tr class="odd">
<td>VES-1893</td>
<td><p><strong>Defect</strong>: Fortify: Key Management: Empty Encryption Key - 1 issue<br />
Empty encryption keys can compromise security.</p>
<p><strong>Fix</strong>: Updated code so that encryption keys are never empty and are obfuscated and managed in an external source.</p></td>
</tr>
<tr class="even">
<td>VES-1894</td>
<td><p><strong>Defect</strong>: Fortify: Dynamic Code Evaluation: Unsafe Deserialization - 1 issue<br />
Deserializing user-controlled object streams at runtime can allow attackers to execute arbitrary code on the server, abuse application logic, and/or lead to denial of service.</p>
<p><strong>Fix</strong>: Analysis found that the identified class is performing deserializing file input stream on given class that is available from application classpath; the current class file is retrieved from the secured and trusted ES server classpath.</p></td>
</tr>
<tr class="odd">
<td>VES-1895</td>
<td><p><strong>Defect</strong>: Fortify: SQL Injection: Hibernate - 10 issues<br />
An SQL query build using input potentially coming from an untrusted source is being invoked.</p>
<p><strong>Fix</strong>: Updated code to mitigate SQA injection risk.</p></td>
</tr>
<tr class="even">
<td>VES-1936</td>
<td><p><strong>Defect</strong>: Fortify: Null Dereference - 1 issue<br />
Dereferencing a null pointer can crash the program.</p>
<p><strong>Fix</strong>: The local variable that could be null was checked not null.</p></td>
</tr>
<tr class="odd">
<td>VES-1937</td>
<td><p><strong>Defect</strong>: Fortify: Dynamic Code Evaluation: Unsafe XStream Deserialization – 1 issue<br />
The XStream library provides the developer with an easy way to transmit objects, serializing them to XML documents. However, XStream deserialization might enable an attacker to run arbitrary Java code on the server.</p>
<p><strong>Fix</strong>: Use whitelist rather than blacklist approach so that any class allowed in the whitelist is audited to make sure it is safe to deserialize.</p></td>
</tr>
<tr class="even">
<td>VES-1960</td>
<td><p><strong>Defect</strong>: WASA: A2 - Broken Authentication and Session Management</p>
<p><strong>Fix</strong>: Updated the Cross-Site Scripting (XSS) filter.</p></td>
</tr>
<tr class="odd">
<td>VES-1961</td>
<td><p><strong>Defect</strong>: WASA: A5 - Security Misconfiguration</p>
<p><strong>Fix</strong>: Enabled Cross Site Request Forgery (CSRF) Guard, updated build files and fixed Java Server Pages (JSPs).</p></td>
</tr>
<tr class="even">
<td>VES-4603</td>
<td><p><strong>Defect</strong>: Fortify: Path Manipulation - 2 issues<br />
Attackers are able to control a file system path argument, which allows them to access or modify otherwise protected files.</p>
<p><strong>Fix</strong>: Updated code to ensure that the user has no control over the path that is provided to the input stream.</p></td>
</tr>
<tr class="odd">
<td>VES-4604</td>
<td><p><strong>Defect</strong>: Fortify: Server-Side Request Forgery - 6 issues<br />
If data is retrieved from an external system, then it must be validated.</p>
<p><strong>Fix</strong>: Updated code to check if provided IDs are in the expected format and match that of one of the documents associated with the current record.</p></td>
</tr>
<tr class="even">
<td>VES-4605</td>
<td><p><strong>Defect</strong>: Fortify: Log Forging - 10 issues<br />
Unvalidated user input to the log could enable forging of log entries or injection of malicious content into the log.</p>
<p><strong>Fix</strong>: Updated code to prevent unvalidated user input to the log.</p></td>
</tr>
<tr class="odd">
<td>VES-4606</td>
<td><p><strong>Defect</strong>: Fortify: Null Dereference - 4 issues<br />
Dereferencing a null pointer can crash the system.</p>
<p><strong>Fix</strong>: Updated code to remove null dereferences.</p></td>
</tr>
<tr class="even">
<td>VES-4607</td>
<td><p><strong>Defect</strong>: Fortify: Unreleased Resource: Streams - 6 issues<br />
Some allocated system resources are failing to be released.</p>
<p><strong>Fix</strong>: Updated code to allow release of the allocated system resources.</p></td>
</tr>
<tr class="odd">
<td>VES-4608</td>
<td><p><strong>Defect</strong>: Fortify: Unreleased Resource: Files<br />
Allowed files are sometimes failing to be released.</p>
<p><strong>Fix</strong>: Updated code to release the allowed files.</p></td>
</tr>
<tr class="even">
<td>VES-4609</td>
<td><p><strong>Defect</strong>: Fortify: Portability Flaw: Locale Dependent Comparison</p>
<p><strong>Fix</strong>: Analysis found that there is no longer a flaw in ContactInformationInputParameter.java.</p></td>
</tr>
<tr class="odd">
<td>VES-4610</td>
<td><p><strong>Defect</strong>: Fortify: Dynamic Code Evaluation: Unsafe Deserialization</p>
<p><strong>Fix</strong>: Removed "Sys" statement to enable safe deserialization.</p></td>
</tr>
<tr class="even">
<td>VES-4611</td>
<td><p><strong>Defect</strong>: Fortify: Unresolved Scan Issues: ES_HECMS_ui_web_admin</p>
<p><strong>Fix</strong>: Resolved all scan issues in file ES_HECMS_ui_web_admin.</p></td>
</tr>
<tr class="odd">
<td>VES-4612</td>
<td><p><strong>Defect</strong>: Fortify: Unreleased Resource: Sockets: ES_WS_Webserv</p>
<p><strong>Fix</strong>: Updated code to release the Sockets: ES_WS_Webserv resource.</p></td>
</tr>
<tr class="even">
<td>VES-4613</td>
<td><p><strong>Defect</strong>: Fortify: Unresolved Scan Issues: ES_WS_Webserv</p>
<p><strong>Fix</strong>: Resolved all scan issues in file ES_WS_Webserv.</p></td>
</tr>
<tr class="odd">
<td>VES-5553</td>
<td><p><strong>Defect</strong>: Access Controls - Elevated Privileges<br />
The ability to edit a user profile is currently requiring administrator capability instead of just the single "edit user profile" capability.</p>
<p><strong>Fix</strong>: Implementation corrected so that the ability to edit a user profile requires only the existing "edit user profile" capability.</p></td>
</tr>
<tr class="even">
<td>VES-5752</td>
<td><p><strong>Defect</strong>: Section 508: Some fields on Schedule Reports screens are not read as "Required" by Job Access With Speech (JAWS).</p>
<p><strong>Fix</strong>: Fixed the Generate Report, Day to Generate Report, and Time to Generate Report fields to be read as "Required" by JAWS.</p></td>
</tr>
<tr class="odd">
<td>VES-5897</td>
<td><p><strong>Defect</strong>: Fortify: Privacy Violation - 52 issues<br />
Confidential information is being mishandled.</p>
<p><strong>Fix</strong>: Analysis found that the confidential information is being handled properly; the reported class is using a Business Entity class and not the "CCNFileData" class as reported.</p></td>
</tr>
<tr class="even">
<td>VES-5898</td>
<td><p><strong>Defect</strong>: Fortify: Privacy Violation: Heap Inspection – 30 issues<br />
Sensitive data is being stored in such a way that it cannot be reliably purged from memory.</p>
<p><strong>Fix</strong>: Analysis found that the instances identified are sensitive data. They are Enum values which are set to private variables.</p></td>
</tr>
<tr class="odd">
<td>VES-5899</td>
<td><p><strong>Defect</strong>: Fortify: Race Condition: Singleton Member Field – 3 issues<br />
Certain classes are singletons, so the member fields are shared between users; the result is that one user could see another user's data.</p>
<p><strong>Fix</strong>: Analysis found that the reported classes are not singleton classes; this rule does not apply to its members being shared between users.</p></td>
</tr>
<tr class="even">
<td>VES-6767</td>
<td><p><strong>Defect</strong>: Changing a preferred facility to a new station that has never been assigned before does not create a new assignment date; it is inheriting the facility assignment date from the previously assigned record.</p>
<p><strong>Fix</strong>: Updated code to set the assignment date to the system date when a new preferred facility is added.</p></td>
</tr>
<tr class="odd">
<td>VES-6912</td>
<td><p><strong>Defect</strong>: Fortify: Unvalidated input into JavaScript Object Notation (JSON) could allow an attacker to inject arbitrary elements or attributes into the JSON entity.</p>
<p><strong>Fix</strong>: Analysis found that JSON is created by ES; attributes are generated from the Java classes within ES, not from user input.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref23319755" class="anchor"></span>Table 3: Sustainment Defects and Fixes in ES 5.13

### From: VES Version 5.2.3 Release Notes

## Sustainment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error! Reference source not found. lists the sustainment updates included in the ES 5.2.3 release. Modifications are tracked in Rational Team Concert (RTC) Requirements Management (RM).

<table>
<caption><p>Table 1: Sustainment Updates in the 5.2.3 Release</p></caption>
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th>RTC<br />
RM #</th>
<th>Title</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>999149</td>
<td>ES 5.2.3 Maintain the Enrollment System</td>
<td>Maintain the Enrollment System application by providing minor enhancements, defect fixes, and routine maintenance.</td>
</tr>
</tbody>
</table>

Table 1: Sustainment Updates in the 5.2.3 Release
