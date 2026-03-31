---
title: Decision Support Tool (DST) User Guide
doc_type: UG
doc_label: User Guide
doc_layer: plain
doc_subject: Decision Support Tool (DST)
app_code: GMRC
app_name: "CPRS: Consult/Request Tracking"
section: CLI
app_status: archive
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - consult
  - care
  - time
  - span
  - community
  - table
  - service
  - veteran
  - contents
  - decision
page_count: 0
word_count: 8825
section_count: 19
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2020
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking_Archive/dst_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking_Archive/dst_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=343"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Decision Support Tool (DST)

  Software Version 1.1.1262

  User Guide
---

![](decision-support-tool-dst-user-guide/001.png)

August 2020

Office of Information and Technology (OIT)

Revision History

> **NOTE:** The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

<table>
<caption><p>Table 1. Documentation Symbols and Descriptions</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 12%" />
<col style="width: 45%" />
<col style="width: 24%" />
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
<td>08/17/2020</td>
<td>10.0</td>
<td><p>Software Version 1.1.1262a:</p>
<p>Added section 5.6: Previously Sent to HSRM Message.</p></td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>06/23/2020</td>
<td>9.0</td>
<td><p>Software Version 1.1.1065:</p>
<ul>
<li><p>Updated screen captures to reflect CC Average Wait Time column added to VA Facilities.</p></li>
<li><p>Updated DST Help screen.</p></li>
</ul></td>
<td>AbleVets</td>
</tr>
<tr class="odd">
<td>05/18/2020</td>
<td>8.0</td>
<td><p>Software Version 1.1.1033:</p>
<ul>
<li><p>Added information to Residential Address definition regarding No Address Available.</p></li>
<li><p>Added Clinical Service synonym information to Clinical Service definition.</p></li>
<li><p>Added No Address Available Error section.</p></li>
</ul></td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>03/12/2020</td>
<td>7.0</td>
<td><p>Software Version 1.1.921:</p>
<ul>
<li><p>Updated screen captures.</p></li>
<li><p>Updated Best Medical Interest of Veteran menu options.</p></li>
<li><p>Added Explanation field for Best Medical Interest of Veteran options.</p></li>
<li><p>Added a note and screen capture for No Basic Eligibility Found in Enrollment System.</p></li>
<li><p>Updated the Urgency section.</p></li>
<li><p>Removed No Later Than Date from Provider workflow.</p></li>
<li><p>Removed Special Instructions.</p></li>
<li><p>No Later Than Date was renamed to Wait Time Eligibility Date in the VCCPE-Admin workflow.</p></li>
<li><p>Added note that VCCPE Wait Time Eligibility is not applicable when CID is greater than Wait Time Eligibility Date.</p></li>
</ul></td>
<td>AbleVets</td>
</tr>
<tr class="odd">
<td>11/25/2019</td>
<td>6.0</td>
<td><p>Software Version 1.1:</p>
<ul>
<li><p>Updated screen captures.</p></li>
<li><p>Updated acronym list.</p></li>
<li><p>Added character limit note to the Explanation field under the Best Medical Interest of Veteran section.</p></li>
<li><p>Added What’s New? Screen to DST login.</p></li>
<li><p>Added Best Medical Interest of Veteran note for signed consult.</p></li>
<li><p>Updated Best Medical Interest of Veteran menu options.</p></li>
<li><p>Added Capturing Scheduling Information in the VCCPE-Admin Workflow section.</p></li>
<li><p>Added Auto-Forward Consult to Community Care features</p></li>
<li><p>Removed the Link DST Data Dialog Box</p></li>
</ul></td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>08/06/2019</td>
<td>5.0</td>
<td><p>Software Version 1.0.12:</p>
<ul>
<li><p>Updated screen captures.</p></li>
<li><p>Added What’s New? feature information.</p></li>
</ul></td>
<td>AbleVets</td>
</tr>
<tr class="odd">
<td>07/16/2019</td>
<td>4.0</td>
<td><p>Software Version 1.0.09:</p>
<p>Added note regarding the Average Drive Time and Average Wait Time not showing up for Clinical Services that require a manual entry.</p></td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>05/30/2019</td>
<td>3.0</td>
<td><p>Software Version 1.0.04:</p>
<ul>
<li><p>Updated name from National Service Desk to Enterprise Service Desk.</p></li>
<li><p>Updated the Facility Name description to include the radius for Specialty Care and Primary Care.</p></li>
</ul></td>
<td>AbleVets</td>
</tr>
<tr class="odd">
<td>05/21/2019</td>
<td>2.0</td>
<td><p>GMRC*3*129:</p>
<ul>
<li><p>Updated VA Facility search radius to 100 miles.</p></li>
<li><p>Updated DST dashboard screens.</p></li>
</ul></td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>04/10/2019</td>
<td>1.0</td>
<td>Initial Documentation Release for DST v1.0.03.</td>
<td>AbleVets</td>
</tr>
</tbody>
</table>

Table 1. Documentation Symbols and Descriptions

Artifact Rationale

Per the Veteran-focused Integrated Process (VIP) Guide, the User’s Guide is required to be completed prior to Critical Decision Point \#2 (CD2), with the expectation that it will be updated as needed. A User Guide is a technical communication document intended to give assistance to people using a particular system, such as VistA end users. It is usually written by a technical writer, although it can also be written by programmers, product or project managers, or other technical staff. Most user guides contain both a written guide and the associated images. In the case of computer applications, it is usual to include screenshots of the human-machine interfaces, and hardware manuals often include clear, simplified diagrams. The language used is matched to the intended audience, with jargon kept to a minimum or explained thoroughly. The User Guide is a mandatory, build-level document, and should be updated to reflect the contents of the most recently deployed build. The sections documented herein are required if applicable to your product.

Table of Contents

List of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Document Orientation](#document-orientation)
    - [Organization of the Manual](#organization-of-the-manual)
    - [Assumptions](#assumptions)
    - [Coordination](#coordination)
    - [Disclaimers](#disclaimers)
    - [Documentation Conventions](#documentation-conventions)
    - [References and Resources](#references-and-resources)
  - [Enterprise Service Desk and Organizational Contacts](#enterprise-service-desk-and-organizational-contacts)
- [System Summary](#system-summary)
  - [System Configuration](#system-configuration)
  - [Data Flows](#data-flows)
  - [User Access Levels](#user-access-levels)
  - [Continuity of Operation](#continuity-of-operation)
- [Getting Started](#getting-started)
  - [Logging On](#logging-on)
  - [System Menu](#system-menu)
    - [Provider DST Dashboard Screen Example](#provider-dst-dashboard-screen-example)
    - [Admin VCCPE DST Dashboard Screen Example](#admin-vccpe-dst-dashboard-screen-example)
    - [DST Dashboard Controls](#dst-dashboard-controls)
  - [Exit System](#exit-system)
- [Using the Software](#using-the-software)
  - [Launching DST](#launching-dst)
    - [Launching DST from an Unsigned Consult or When Ordering a New Consult](#launching-dst-from-an-unsigned-consult-or-when-ordering-a-new-consult)
    - [Launching DST from Add Comments to Consult](#launching-dst-from-add-comments-to-consult)
  - [Capturing Information in DST](#capturing-information-in-dst)
    - [Capturing Provider and Veteran Decision Data](#capturing-provider-and-veteran-decision-data)
    - [Capturing Scheduling Information in the VCCPE-Admin Workflow](#capturing-scheduling-information-in-the-vccpe-admin-workflow)
- [Troubleshooting](#troubleshooting)
  - [Unable to Lookup Clinical Service](#unable-to-lookup-clinical-service)
  - [MVI Error Handling](#mvi-error-handling)
  - [Enrollment System (ES) Error Handling](#enrollment-system-es-error-handling)
  - [PPMS Error Handling](#ppms-error-handling)
  - [No Address Available Error](#no-address-available-error)
  - [Previously Sent to HSRM Message](#previously-sent-to-hsrm-message)
- [Acronyms and Abbreviations](#acronyms-and-abbreviations)
The Veterans Health Administration (VHA) Office of Community Care has a need for a real-time decision support tool to help Department of Veterans Affairs (VA) Providers and Veterans quickly review the criteria proscribed in the VA MISSION Act of 2018, determine whether a given Veteran is eligible and would be best served utilizing the Veterans Community Care Program, and document the decision rationale in the Veteran’s health record.
The Decision Support Tool (DST) software will:
- Allow the user to view relevant data within the existing Computerized Patient Record System (CPRS) consult order workflow, that helps the Veteran and VA provider decide if a consult service should be referred to the local VA facility, a near-by VA facility via Inter-Facility Consults (IFC), or to a community provider by providing information about the following:
- Drive time standards associated with the requested consult service.
- Average wait times for the requested clinical service at VA facilities near the Veteran’s place of residence. Note, the average wait times may not be used to determine wait time eligibility.
- Veteran’s eligibility for accessing care in the community and their stated preferences (opt-in/out)
- Allow the provider to select the consult decision and enter additional justification text when indicated.
- Based on the decision outcome, provide required information to the Electronic Medical Record (EMR) in order to initiate either an in-house, IFC, or Veteran Community Care Program (VCCP) consult order.
- Document the rationale for the referral decision in the consult record.
- Generate structured text based on the displayed results that can be used for downstream report generation.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to provide instruction for utilizing the DST to standardize and streamline consult management for Community Care.

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Decision Support Tool User Guide* will provide explanations of each screen and of all user interface options within the context of an easy to understand demonstration data scenario.

This document is also designed to provide the user with screen-by-screen “how to” information on the usage of Consult Toolbox.

### Organization of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Section 1: Introduction

The Introduction section provides the purpose of this manual, an overview of the DST software, an overview of the software used, project references, contact information for the user to seek additional information, and an acronyms and abbreviations list for this manual.

Section 2: System Summary

The System Summary section provides a graphical representation of the equipment, communication, and networks used by the system, user access levels, how the software will be accessed, and contingencies and alternative modes of operation.

Section 3: Getting Started

Information for the Getting Started section provides a general walk-through of the system from initiation through exit, enabling the user to understand the sequence and flow of the system.

Section 4: Using the Software

This section gives the user the “how to” information to use DST, including many step-by-step procedures.

Section 5: Troubleshooting

This section provides troubleshooting for the DST user.

Section 6: Acronyms and Abbreviations

This section provides a list of acronyms and abbreviations found in this document.

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide was written with the following assumed experience/skills of the audience:

- User has login credentials for CPRS.
- User has basic knowledge of the CPRS operating system (such as the use of commands, menu options, and navigation tools).
- User has Consult Toolbox v1.9.0054 or later installed on their machine.
- User has Google Chrome installed on their machine.

### Coordination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual uses several methods to highlight different aspects of the material.

| Symbol                                                                                                                                                                                                                                     | Description                                                                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| ![](decision-support-tool-dst-user-guide/002.png) | CAUTION: Used to caution the reader to take special notice of critical information. |

Table 2. Acronyms and Abbreviations

1.  Notes are used to inform the reader of general information including references to additional reading material.

### References and Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Readers who wish to learn more about DST, Consult Toolbox, and CPRS should consult the following:

- CPRS: Consult/Request Tracking in the VDL: <https://www.va.gov/vdl/application.asp?appid=62>
- Office of Community Care Field Guidebook: <span class="mark">REDACTED</span>
- Office of Community Care Field Guidebook- Tools-HSRM section

## Enterprise Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For issues related to the Community Care DST that cannot be resolved by this manual or the site administrator, please contact the Enterprise Service Desk at 855-NSD-HELP (673-4357).

# System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Within the current CPRS order consult workflow, VA providers utilize the DST system to support the decision and election for consult services for a given consult.

<span id="_Toc1555615" class="anchor"></span>Figure 1: DST Business Process Workflow – Unsigned Order Consult

![](decision-support-tool-dst-user-guide/003.png)

<span id="_Toc1555616" class="anchor"></span>Figure 2: DST Business Process Workflow – Signed Order Consult

![](decision-support-tool-dst-user-guide/004.png)

## Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc1555617" class="anchor"></span>Figure 3: CCAD DST Data Flow Diagram

![](decision-support-tool-dst-user-guide/005.png)

## User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All VA providers will serve as the main user base for this system. The user must have access to CPRS and Consult Toolbox must be enabled to access DST.

## Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DST falls under the Veterans Health Information Systems and Technology Architecture (VistA) Continuity of Operations Plan.

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides a general walkthrough of DST from initiation through exit.

## Logging On

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DST is accessed through CPRS.

2.  If you have Consult Toolbox v1.9.0054 installed, you will no longer see the standard VA-provided Single Sign-On Integration (SSOi) page when launching DST from CPRS.

## System Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DST Dashboard features three sections: Consult, VA Facilities, and Community Care. The fields

### Provider DST Dashboard Screen Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc39837315" class="anchor"></span>Figure 4: Provider DST Dashboard Screen Example

![](decision-support-tool-dst-user-guide/006.png)

Following are descriptions of the features on the DST Dashboard.

Consult section:

- Name – Veteran name. This is a read only field supplied by CPRS.
- Residential Address – Veterans residential address. This is a read only field supplied by the Master Veteran Index (MVI) data interface. Provided by Eligibility & Enrollment System. If any part of the address is not available, then it is displayed as “No address available”.
- Date of Birth – Veterans date of birth. This is a read only field supplied by CPRS.
- SSN – Veterans Social Security Number (SSN). This is a read only field supplied by CPRS.
- Clinical Service – Consult Clinical Service. Automatically assigned when the user launches DST from CPRS or this field can be manually entered, it depends if you are using an unsigned or signed consult. When you are selecting the Clinical Service, you can start typing the value you are looking for. Common synonyms are searchable and will appear in the drop-down menu along with the official service name. When you select a Clinical Service synonym from the drop-down list, the official clinical service name will be displayed. Only official Clinical Service names will be saved with the DST information and written to the consult when signed.
- Urgency – This is a read only field supplied by CPRS.
- Routine – A Routine consult indicates the patient should be seen in accordance with the clinically indicated date.
- Stat – Stat consults will be defined as an “immediate” need. The sender of a stat consult is required to:
- Contact the intended receiver of the consult request to discuss the patients’ situation.
- A stat consult must be completed within 24 hours.
- Drive Time Std – This is a read only field supplied by local DST datastore, based on whether the selected clinical service is considered Primary Care/Mental Health or Specialty Care.
- Wait Time Std – This is a read only field supplied by local DST datastore, based on whether the selected clinical service is considered Primary Care/Mental Health or Specialty Care.
- CID/No Earlier Than Date – This is a read only field auto-populated from CPRS.

VA Facilities section: VHA facilities that MAY provide clinical related to this consult are listed in this section. DST searches an internal table (updated weekly from Corporate Data Warehouse (CDW)) to filter the returned list to facilities within a 100-mile radius for Specialty Care consults (40-mile radius for Primary Care/Mental Health) that offer services associated with consult Clinical Service (based on the National IFC Dashboard).

3.  Average Drive Time and Average Wait Time will not show up until a Clinical Service has been selected, whether by default or via manual entry. The DST application attempts to map consult names to Clinical Services for all Nationwide sites. However, due to the distributed and dynamic nature of consult name addition by the local VA site, DST is not able to keep a real time list of these Consult to Clinical Service mappings. When DST application cannot find a Consult to Clinical Service mapping, the application requires that the user enter the Clinical Service manually on the DST dashboard. When this clinical service is entered, the DST application will continue to request and populate the facility drive time and average wait time based on Residential Address and the entered clinical service.
4.  DST may display facilities that are outside the drive time standard so that the Veteran is aware of VA facility options. Facilities displayed that are outside the drive time standard, are not used in the drive time eligibility calculation and will appear in gray text.
- Facility Name – List of VHA facilities that offer a related consult service within a 100-mile radius for Specialty Care and a 40-mile radius for Primary Care of the Veteran residential address (sorted by Average Drive Time low-to-high).
- Average Drive Time – This refers to the average time it takes to drive from the Veteran’s residential address as noted in the Enrollment System to each identified VA facility that may offer the requested service. This measurement uses VA’s Provider Profile Management System (PPMS) which is a Microsoft-based product that utilizes Bing maps and a proprietary algorithm to determine the time to drive between the two addresses. If PPMS returns 10 facilities or fewer, the drive time calculation takes into account distance, route, speed limits and historical traffic pattern data. If PPMS returns more than 10 facilities, historical traffic data will be excluded from the drive time calculation.
- VA Average Wait Time – This is measured as the average time from the date an appointment is created to the date of the appointment itself. DST displays the average wait times of all new patient appointments completed in the stop code of the requested clinical service, based on new patient appointments in a rolling 30-day assessment. It is possible a facility offers the service requested but has not had any new patients in the last 30 days. In this case, the Average Wait Time field will state Data Not Available. This calculation is similar to the method used for the VA Access to Care public facing website.

  It is important to note that average wait time in DST should be used only for reference. It will not be used to establish Community Care eligibility. Wait time eligibility is determined at the time of scheduling the appointment, not at the time of requesting it.
- CC Average Wait Time – The Facilities list in DST shows the average wait time for Community Care appointments so that Veterans and providers can compare the average wait times between VHA and the community for the selected clinical service.

  Community care wait time is calculated by determining the average time from the date a community care appointment is made to the date of the appointment itself, as recorded in Health Share Referral Manager (HSRM). DST displays the average wait times of all appointments booked or completed under Standard Episodes of Care (SEOCs) related to the requested clinical service, based on a rolling 90-day assessment. The Community Care data displayed is for community care appointments associated with the facility and SEOCs associated with the selected clinical service. This information is provided to inform providers, schedulers and Veterans of the comparable wait time in the community so they can make an informed decision when considering community care.

  Adding the community care wait time to DST will assist with guiding the conversation between the VA Care Team and the Veteran, regarding their VA and community care options to include average community care wait time.

  Important - community care eligibility based on wait time is still to be determined at the time of scheduling into the specific VA clinic where the Veteran is to be seen.

Community Care section: If DST receives a unique Veteran Integration Control Number (ICN) back from MVI, it sends the ICN to the Enrollment System (ES) Application Program Interface (API) to retrieve the Veteran’s residential address and a Veterans eligibility identifying string containing one or more of the following eligibility codes applicable to DST: “U” – Urgent care eligible, “G” – Grandfathered, “H” – Hardship, or “N” – No full-service VHA facility.

- Community Care Eligible based on -
- Enrollment System Basic Eligibility Factor - If a Veteran is designated in the Enrollment System as ineligible for Community Care, DST will now display a message indicating that the Veteran is ineligible for Community Care because they lack Basic eligibility. If the Veteran lacks Basic eligibility, you will not be able to edit any information on the DST dashboard and you will not be able to establish Community Care eligibility for this Veteran. When you have reviewed the Veteran information in DST, save the DST record to document the Community Care ineligible status for the Veteran. This affects patients eligible for VA care but not otherwise eligible for Community Care, such as Civilian Health and Medical Program of the Department of Veterans Affairs (CHAMPVA) patients being seen at the VAMC under the CHAMPVA In-house Treatment Initiative (CITI) program.

<span id="_Toc48311199" class="anchor"></span>Figure 5: No Basic Eligibility Found in Enrollment System Message

![](decision-support-tool-dst-user-guide/007.png)

- Enrollment System Eligibility Factors – Hardship, Grandfathered, or No Full Service VHA. If any of the indicators are received from the enrollment system, the Veteran will be identified as eligible for Community Care.
- Drive Time – If there are no facilities listed within the drive time standard for the selected clinical service, then the Veteran will be identified as eligible for Community Care based on drive time.
- Best Medical Interest of Veteran – Drop-down menu. There is a Community Care policy and procedure that allows a VA provider to request the ability for a Veteran to receive care in the community based on that Veterans best medical interest. Congress requests that VA providers consider: Nature or simplicity of service, Frequency of service, Need for an attendant, Potential for improved continuity of care, or Difficulty in traveling.
5.  The Best Medical Interest of Veteran drop-down menu will only display when DST is launched from an unsigned consult if the Veteran is not otherwise eligible.

<span id="_Toc48311200" class="anchor"></span>Figure 6: Best Medical Interest of Veteran Menu Options

![](decision-support-tool-dst-user-guide/008.png)

- Nature or simplicity of service
- Frequency of service
- Need for an attendant
- Potential for improved continuity of care
- Difficulty in traveling
- Explanation (required) field – This field displays once a selection has been made from the Best Medical Interest of Veteran drop-down menu. This information will be saved to the consult and is captured for reporting purposes. (This field has a maximum 200-character limit.)
- Veteran Community Care Option (required) –
- TBD/Deferred – When this radio button is selected it will require a Standardized Episodes of Care (SEOC) to be selected if the Veteran ultimately opts in to Community Care. Because a SEOC is required on every consult that goes to Community Care, this allows the ordering provider to select the appropriate SEOC to match the consult/order that is being ordered at the time it is placed. Additionally, it allows the creator of the consult and thus user of the DST to use information even if the Veteran is a) Not ready to decide or b) Not present. This button then enables the provider to ask a team member to finish the opt in/out decision later while maintaining the integrity of the initial DST dashboard information.
- Opt-In for CC – Veteran elects care in the community.
- Opt-out of CC – Veteran elects to remain within the VA for care.
- Standardized Episode of Care (required) – Relates to Clinical Service. A service or group of services the VA authorizes a community provider to perform to complete the consult order including the duration and number of visits that might be necessary. Some or all of the authorized services may need to be performed during any particular episode of care.
- Forward Consult to Community Care? – Option to automatically forward consult to Community Care when order is signed.
- Yes
- No

### Admin VCCPE DST Dashboard Screen Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc39837318" class="anchor"></span>Figure 7: Admin VCCPE DST Dashboard Screen Example

![](decision-support-tool-dst-user-guide/009.png)

Following are descriptions of the features on the DST Dashboard.

Consult section:

- Name – Veteran name. This is a read only field supplied by CPRS.
- Residential Address – Veterans residential address. This is a read only field supplied by the MVI data interface. Provided by Eligibility & Enrollment System. If any part of the address is not available, then it is displayed as “No address available”.
- Date of Birth – Veterans date of birth. This is a read only field supplied by CPRS.
- SSN – Veterans Social Security Number (SSN). This is a read only field supplied by CPRS.
- Clinical Service – Consult Clinical Service. Automatically assigned when the user launches DST from CPRS or this field can be manually entered, it depends if you are using an unsigned or signed consult. When you are selecting the Clinical Service, you can start typing the value you are looking for. Common synonyms are searchable and will appear in the drop-down menu along with the official service name. When you select a Clinical Service synonym from the drop-down list, the official clinical service name will be displayed. Only official Clinical Service names will be saved with the DST information and written to the consult when signed.
- Urgency – This is a read only field supplied by CPRS.
- Routine – A Routine consult indicates the patient should be seen in accordance with the clinically indicated date.
- Stat – Stat consults will be defined as an “immediate” need. The sender of a stat consult is required to:
- Contact the intended receiver of the consult request to discuss the patients’ situation.
- A stat consult must be completed within 24 hours.
- Drive Time Std – This is a read only field supplied by local DST datastore, based on whether the selected clinical service is considered Primary Care/Mental Health or Specialty Care.
- Wait Time Std – This is a read only field supplied by local DST datastore, based on the urgency and whether the selected clinical service is considered Primary Care/Mental Health or Specialty Care.

| Urgency | Type                                         | Wait Time Standard |
|---------|----------------------------------------------|--------------------|
| Routine | Primary Care/Mental Health                   | 28 days            |
| Routine | Specialty Care                               | 20 days            |
| Stat    | Primary Care/Mental Health or Specialty Care | 1 day              |

- CID/No Earlier Than Date – This is a read only field auto-populated from CPRS.
- Wait Time Eligibility Date – This date is calculated as Today + wait time standard. See additional wait time eligibility details in the *Office of Community Care Field Guidebook*.

VA Facilities section: VHA facilities that MAY provide clinical related to this consult are listed in this section. DST searches an internal table (updated weekly from Corporate Data Warehouse (CDW)) to filter the returned list to facilities within a 100-mile radius for Specialty Care consults (40-mile radius for Primary Care/Mental Health) that offer services associated with consult Clinical Service (based on the National IFC Dashboard).

6.  Average Drive Time and Average Wait Time will not show up until a Clinical Service has been selected, whether by default or via manual entry. The DST application attempts to map consult names to Clinical Services for all Nationwide sites. However, due to the distributed and dynamic nature of consult name addition by the local VA site, DST is not able to keep a real time list of these Consult to Clinical Service mappings. When DST application cannot find a Consult to Clinical Service mapping, the application requires that the user enter the Clinical Service manually on the DST dashboard. When this clinical service is entered, the DST application will continue to request and populate the facility drive time and average wait time based on Residential Address and the entered clinical service.
7.  DST may display facilities that are outside the drive time standard so that the Veteran is aware of VA facility options. Facilities displayed that are outside the drive time standard, are not used in the drive time eligibility calculation and will appear in gray text.
- Facility Name – List of VHA facilities that offer a related consult service within a 100-mile radius for Specialty Care and a 40-mile radius for Primary Care of the Veteran residential address (sorted by Average Drive Time low-to-high).
- Average Drive Time – This refers to the average time it takes to drive from the Veteran’s residential address as noted in the Enrollment System to each identified VA facility that may offer the requested service. This measurement uses VA’s Provider Profile Management System (PPMS) which is a Microsoft-based product that utilizes Bing maps and a proprietary algorithm to determine the time to drive between the two addresses. If PPMS returns 10 facilities or fewer, the drive time calculation takes into account distance, route, speed limits and historical traffic pattern data. If PPMS returns more than 10 facilities, historical traffic data will be excluded from the drive time calculation.
- VA Average Wait Time – This is measured as the average time from the date an appointment is created to the date of the appointment itself. DST displays the average wait times of all new patient appointments completed in the stop code of the requested clinical service, based on new patient appointments in a rolling 30-day assessment. It is possible a facility offers the service requested but has not had any new patients in the last 30 days. In this case, the Average Wait Time field will state Data Not Available. This calculation is similar to the method used for the VA Access to Care public facing website.

  It is important to note that average wait time in DST should be used only for reference. It will not be used to establish Community Care eligibility. Wait time eligibility is determined at the time of scheduling the appointment, not at the time of requesting it.
- CC Average Wait Time – The Facilities list in DST shows the average wait time for community care appointments so that Veterans and providers can compare the average wait times between VHA and the community for the selected clinical service.

  Community care wait time is calculated by determining the average time from the date a community care appointment is made to the date of the appointment itself, as recorded in Health Share Referral Manager (HSRM). DST displays the average wait times of all appointments booked or completed under Standard Episodes of Care (SEOCs) related to the requested clinical service, based on a rolling 90-day assessment. The Community Care data displayed is for community care appointments associated with the facility and SEOCs associated with the selected clinical service. This information is provided to inform providers, schedulers and Veterans of the comparable wait time in the community so they can make an informed decision when considering community care.

  Adding the community care wait time to DST will assist with guiding the conversation between the VA Care Team and the Veteran, regarding their VA and community care options to include average community care wait time.

  Important - community care eligibility based on wait time is still to be determined at the time of scheduling into the specific VA clinic where the Veteran is to be seen.

Community Care section: If DST receives a unique Veteran ICN back from MVI, it sends the ICN to the Enrollment System (ES) API to retrieve the Veteran’s residential address and a Veterans eligibility identifying string containing one or more of the following eligibility codes applicable to DST: “U” – Urgent care eligible, “G” – Grandfathered, “H” – Hardship, or “N” – No full-service VHA facility.

- Community Care Eligible based on –
- Enrollment System Basic Eligibility Factor - If a Veteran is designated in the Enrollment System as ineligible for Community Care, DST will now display a message indicating that the Veteran is ineligible for Community Care because they lack Basic eligibility. If the Veteran lacks Basic eligibility, you will not be able to edit any information on the DST dashboard and you will not be able to establish Community Care eligibility for this Veteran. When you have reviewed the Veteran information in DST, save the DST record to document the Community Care ineligible status for the Veteran. This affects patients eligible for VA care but not otherwise eligible for Community Care, such as Civilian Health and Medical Program of the Department of Veterans Affairs (CHAMPVA) patients being seen at the VAMC under the CHAMPVA In-house Treatment Initiative (CITI) program.

<span id="_Toc48311202" class="anchor"></span>Figure 8: No Basic Eligibility Found in Enrollment System Message

![](decision-support-tool-dst-user-guide/010.png)

- Wait Time Eligibility Not Applicable – If the CID is further in the future than the Wait Time Eligibility Date, then Wait Time Eligibility is not applicable for the consult and the following warning will display.

<span id="_Toc48311203" class="anchor"></span>Figure 9: Wait Time Eligibility Not Applicable Message

![](decision-support-tool-dst-user-guide/011.png)

- Enrollment System Eligibility Factors – Hardship, Grandfathered, No Full Service VHA. If any of the indicators are received from the enrollment system, the Veteran will be identified as eligible for Community Care.
- Drive Time – If there are no facilities listed within the drive time standard for the selected clinical service, then the Veteran will be identified as eligible for Community Care based on drive time.
- Wait Time (No Clinic Appointments Available) – If the date entered in the Next Available Appointment field is greater than the Wait Time Eligibility Date, then the Veteran will be identified as eligible for Community Care based on wait time.
- Veteran Community Care Option (required) –
- TBD/Deferred – When this radio button is selected it will require a Standardized Episodes of Care (SEOC) to be selected if the Veteran ultimately opts-in to Community Care. Because a SEOC is required on every consult that goes to Community Care, this allows the ordering provider to select the appropriate SEOC to match the consult/order that is being ordered at the time it is placed. Additionally, it allows the creator of the consult and thus user of the DST to use information even if the Veteran is a) Not ready to decide or b) Not present. This button then enables the provider to ask a team member to finish the opt in/out decision later while maintaining the integrity of the initial DST dashboard information.
- Opt-In for CC – Veteran elects care in the community.
- Opt-out of CC – Veteran elects to remain within the VA for care.

### DST Dashboard Controls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DST Dashboard Controls are located at the top right of the DST Dashboard screen.

<span id="_Toc16002409" class="anchor"></span>Figure 10: DST Dashboard Controls

![](decision-support-tool-dst-user-guide/012.png)

- What’s New? – Click What’s New? to open the DST: What’s New? window. This window lists the new features for each release/build.

<span id="_Toc48311205" class="anchor"></span>Figure 11: DST: What’s New? Window Example

![](decision-support-tool-dst-user-guide/013.png)

- Help – Click Help to open a window offering resources for answering questions.

<span id="_Toc16002411" class="anchor"></span>Figure 12: DST Help Window Example

![](decision-support-tool-dst-user-guide/014.png)

- Logout – Click Logout to exit out of DST.

## Exit System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To exit DST, click Logout at the upper right corner of your screen. To end your DST session without saving changes and return to CPRS, close the browser window.

# Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Launching DST

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DST can be accessed the following ways:

- Accessing the Decision Support Tool via an Unsigned Consult
- Accessing the Decision Support Tool when Ordering a New Consult
- Accessing the Decision Support Tool via Adding a Comment in a Signed Consult
8.  When launched, DST will determine if the consult should be opened in the Provider workflow or the Veteran Community Care Program Eligibility (VCCPE)-Admin workflow.

The sections below provide additional information regarding how to launch DST.

9.  All examples in this document are representative of test data, no patient Personally Identifiable Information (PII) was used.

### Launching DST from an Unsigned Consult or When Ordering a New Consult

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DST can be launched from the Order a Consult dialog box from an unsigned consult and when ordering a new consult. When the CPRS window titled Order a Consult is active and populated as an outpatient consult without a DST ID already in the Reason for Request, Consult Toolbox displays a message over the Accept Consult button while it sends the Consult to Service/Specialty name to DST to determine if the consult is applicable to the MISSION Act.

DST searches an internal table (updated nightly from CDW) to determine whether the Clinical Service associated with the consult requires DST and returns the result to Consult Toolbox.

If DST returns FALSE, no action is initiated by Consult Toolbox and the consult order workflow continues uninterrupted. If DST returns TRUE or a previous DST ID is found in the Reason for Request field, Consult Toolbox displays a movable, non-modal window to inform the user that the consult should be reviewed for eligibility under the MISSION Act and allows them to open the DST prior to accepting the consult.

<span id="_Toc48311207" class="anchor"></span>Figure 13: Order a Consult

![](decision-support-tool-dst-user-guide/015.png)

To launch DST from Order a Consult, follow the steps listed below:

1.  From the Order a Consult window, select an option from the Consult to Service/Specialty. If Outpatient is selected, then a message stating that it is checking to see if the consult requires MISSION Act support displays.

<span id="_Toc48311208" class="anchor"></span>Figure 14: MISSION Act Support Message

![](decision-support-tool-dst-user-guide/016.png)

If MISSION Act requires the use of the DST, a message will display.

<span id="_Toc48311209" class="anchor"></span>Figure 15: MISSION Act Requires DST Message

![](decision-support-tool-dst-user-guide/017.png)

2.  Click Launch DST. The DST: What’s New? Screen displays.

<span id="_Toc48311210" class="anchor"></span>Figure 16: DST: What’s New? Screen

![](decision-support-tool-dst-user-guide/018.png)

10. If you do not want the DST: What’s New? window to display each time you launch DST, select the Do not show me this again until the next update checkbox and the window will only display where there are new DST updates.
3.  Click Close. The DST Dashboard displays.

<span id="_Toc48311211" class="anchor"></span>Figure 17: Unsigned Consult/Ordering a New Consult: DST Dashboard Example

![](decision-support-tool-dst-user-guide/019.png)

### Launching DST from Add Comments to Consult

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DST can be accessed from the Consult Toolbox menu that is displayed when you right-click inside the Add Comment to Consult window in CPRS. When DST is launched this way, the user input data is carried-forward from the most recent DST data set if present.

DST Data is kept in the local database for a period of 30 days after the last update. The data is used to populate the consult comment when the order is signed and to restore the user entries when DST is reopened. If someone opens DST from a consult after the DST data has been deleted, they will see the same as if DST was being opened for the first time on the consult. Eligibility and facility information is always updated in real-time, while the Best Medical Interest of the Veteran, Veteran Community Care Option, SEOC, and Consult Decision will be blank.

To launch DST from Consult Toolbox Add Comment to Consult, follow the steps listed below:

1.  From the Action menu, select Consult Tracking… \> Add Comment. The Add Comment to Consult window displays the Consult Toolbox menu.

<span id="_Toc48311212" class="anchor"></span>Figure 18: Consult Toolbox Menu

![](decision-support-tool-dst-user-guide/020.png)

4.  From the Consult Toolbox menu, select Launch DST. The DST: What’s New? Screen displays.

<span id="_Toc48311213" class="anchor"></span>Figure 19: DST: What’s New? Screen

![](decision-support-tool-dst-user-guide/021.png)

11. If you do not want the DST: What’s New? window to display each time you launch DST, select the Do not show me this again until the next update checkbox and the window will only display where there are new DST updates.
5.  Click Close. The DST Dashboard displays.

<span id="_Toc39837331" class="anchor"></span>Figure 20: DST Dashboard for a Signed Consult

![](decision-support-tool-dst-user-guide/022.png)

## Capturing Information in DST

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Capturing Provider and Veteran Decision Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DST allows you to enter additional information required to fully document the decision to order a VA consult or create a Community Care referral. To enter additional information, follow the steps listed below:

1.  Under the Consult section, verify if the Clinical Services (Specialty Care) field has been auto populated. If the consult is mapped to a clinical service, this field will be populated with the mapped value. If this field is not populated, enter/select the appropriate clinical service. The VA Facilities section will populate.
6.  If there are no other Community Care eligibility factors found and the provider and Veteran have agreed that it is in the Veteran’s best medical interest to be seen in the community during this specific episode of care, under the Community Care section, select an option from the Best Medical Interest of Veteran drop-down menu to establish eligibility. Once an option is selected, you must provide additional clinical information to support Best Medical Interest (BMI) selection in the Explanation field.
12. The Best Medical Interest of Veteran option will be read-only when the consult has been signed if the value was previously entered otherwise it is not displayed.
7.  If the Veteran is eligible for Community Care, from the Veteran Community Care Choice area, select the Veteran’s choice to TBD/Deferred, Opt-in for CC, or Opt-out of CC. If you select the Veteran Community Care Choice of TBD/Deferred or Opt-in for CC, the Standardized Episode of Care section becomes visible.

<span id="_Toc48311215" class="anchor"></span>Figure 21: Standardized Episode of Care Section

![](decision-support-tool-dst-user-guide/023.png)

8.  If the Veteran is eligible for Community Care and opts-in, from the Standardized Episode of Care drop-down menu, select a SEOC to define the authorized care should the consult be forwarded to Community Care. The list of SEOCs is filtered based on the selected Clinical Service (based on government-furnished mapping) to eliminate unrelated SEOCs from the selection list. The SEOC content can be previewed after selection. Once you select the SEOC, the Forward Consult to Community Care section becomes visible.

<span id="_Toc22570936" class="anchor"></span>Figure 22: Auto-Forward Consult to Community Care Section

![](decision-support-tool-dst-user-guide/024.png)

Note, if the selected SEOC is not available for consult forwarding a message will display. Please refer to the DST-Clinical Service Mapping file on the [SharePoint site](https://vaww.vha.vaco.portal.va.gov/DUSHCC/DC/DO/CI/S/Decision%20Support%20Tool/Forms/AllItems.aspx).

<span id="_Toc48311217" class="anchor"></span>Figure 23: Auto-Forward Consult to Community Care Not Available Message

![](decision-support-tool-dst-user-guide/025.png)

13. DST generates a standard Community Care Consult Name based on the SEOC selected.
1.  From the Forward Consult to Community Care section, select Yes or No if you want to automatically forward the consult when the order is signed. If you try to save the DST info before selecting an option, an error message displays prompting you to make the correction before saving.

<span id="_Toc22570937" class="anchor"></span>Figure 24: Populated DST

![](decision-support-tool-dst-user-guide/026.png)

9.  Once the required DST information is populated the save button will enabled. Click Save DST Info, the DST Save Success Message displays. The information captured on the DST dashboard will now be saved to the consult.

<span id="_Toc16002425" class="anchor"></span>Figure 25: DST Save Success Message

![](decision-support-tool-dst-user-guide/027.png)

If DST is unable to save due to content missing, the Unable to Save Message displays. Update the missing fields and save again.

<span id="_Toc16002426" class="anchor"></span>Figure 26: Missing Required Fields Message

![](decision-support-tool-dst-user-guide/028.png)

If something went wrong while trying to save, the DST Save Failed Error Message displays.

<span id="_Toc16002427" class="anchor"></span>Figure 27: DST Save Failed Error Message

![](decision-support-tool-dst-user-guide/029.png)

10. To link the DST data to the consult, close the DST Chrome browser tab or close the Chrome browser completely by clicking the X in the top right corner. The linked DST data displays in the Reason for Request section in the Order a Consult window.

<span id="_Toc48311222" class="anchor"></span>Figure 28: CPRS Order a Consult Window: DST Data Displayed in Reason for Request Field

![](decision-support-tool-dst-user-guide/030.png)

11. Click Accept Order. The consult is signed and actual DST information is displayed in the form of a comment. Any changes to DST after a consult is signed will result in a new comment.

<span id="_Toc48311223" class="anchor"></span>Figure 29: DST Data Displayed in Consult Details

![](decision-support-tool-dst-user-guide/031.png)

### Capturing Scheduling Information in the VCCPE-Admin Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DST allows you to capture scheduling information in the VCCPE-Admin workflow. To capture the scheduling information, follow the steps listed below:

<span id="_Toc48311224" class="anchor"></span>Figure 30: Admin: DST Dashboard

![](decision-support-tool-dst-user-guide/032.png)

1.  Under the Consult section, enter/select the Clinical Services (Specialty Care) name in the field. The VA Facilities section will populate.

<span id="_Toc39837342" class="anchor"></span>Figure 31: Clinical Service Selected

![](decision-support-tool-dst-user-guide/033.png)

12. Under the Community Care section, enter/update the NextAvailable Appointment field. If the NextAvailable Appointment is updated and is after the No Later Than Date, then the patient will be Wait Time (No Clinic Appointments Available) eligible for Community Care.

<span id="_Toc39837343" class="anchor"></span>Figure 32: Wait Time Eligible

![](decision-support-tool-dst-user-guide/034.png)

13. If the Veteran is eligible for Community Care, from the Veteran Community Care Choice area, select the Veteran’s choice to TBD/Deferred, Opt-in for CC, or Opt-out of CC.
14. Once the required DST information is populated the save button will enabled. Click Save, the DST Save Success Message displays. The information captured on the DST dashboard will now be saved to the consult.

<span id="_Toc48311227" class="anchor"></span>Figure 33: DST Save Success Message

![](decision-support-tool-dst-user-guide/035.png)

If DST is unable to save due to content missing, the Unable to Save Message displays. Update the missing fields and save again.

<span id="_Toc48311228" class="anchor"></span>Figure 34: Missing Required Fields Message

![](decision-support-tool-dst-user-guide/036.png)

If something went wrong while trying to save, the DST Save Failed Error Message displays.

<span id="_Toc48311229" class="anchor"></span>Figure 35: DST Save Failed Error Message

![](decision-support-tool-dst-user-guide/037.png)

15. To link the DST data to the consult, close the DST Chrome browser tab or close the Chrome browser completely by clicking the X in the top right corner. The linked DST data displays in the Reason for Request section in the Order a Consult window.

<span id="_Toc48311230" class="anchor"></span>Figure 36: CPRS Order a Consult Window: DST Data Displayed in Reason for Request Field

![](decision-support-tool-dst-user-guide/038.png)

16. Click Accept Order. The consult is signed and actual DST information is displayed in the form of a comment. Any changes to DST after a consult is signed will result in a new comment.

<span id="_Toc48311231" class="anchor"></span>Figure 37: Admin: DST Data Displayed in Consult Details

![](decision-support-tool-dst-user-guide/039.png)

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Unable to Lookup Clinical Service 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Concurrent to the remote data calls, DST searches an internal table (updated nightly from CDW) to get the Clinical Service for the selected consult and sets the consult type to Primary Care/Mental Health (PC/MH) or Specialty Care based on government-provided mapping data. If the Clinical Service cannot be identified from the CDW tables, a message will be displayed in the VA facilities area to prompt the user to select the Clinical Service manually.

<span id="_Toc48311232" class="anchor"></span>Figure 38: Manual Selection of Clinical Service

![](decision-support-tool-dst-user-guide/040.png)

## MVI Error Handling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If MVI does not respond within 10 seconds or a single exact match ICN is not returned, an error message is displayed to the user, the error code is logged in the DST database, the rest of the remote data calls are skipped, and the user can continue with the DST workflow. The specific error code will be stored in the DST database and added to comments after consult is signed to support analytics/reporting.

<span id="_Toc48311233" class="anchor"></span>Figure 39: Veteran Identity Error Handling

![](decision-support-tool-dst-user-guide/041.png)

## Enrollment System (ES) Error Handling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If ES does not respond within 10 seconds or the Veteran ICN is not found, an error message is displayed to the user, the error code is logged in the DST database, the rest of the remote data calls are skipped, and the user can continue with the DST workflow. The specific error code will be stored in the DST database and added to comments after consult is signed to support analytics/reporting.

<span id="_Toc48311234" class="anchor"></span>Figure 40: Veteran Eligibility Error Handling

![](decision-support-tool-dst-user-guide/042.png)

## PPMS Error Handling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If PPMS does not respond within 10 seconds an error message is displayed to the user in the VA Facilities section, the error code is logged in the DST database, Drive Time and Wait Time VCEs displayed with error icons, and the user can continue with the DST workflow. The specific error code will be stored in the DST database and added to comments after consult is signed to support analytics/reporting.

<span id="_Toc48311235" class="anchor"></span>Figure 41: VA Facilities Error Handling

![](decision-support-tool-dst-user-guide/043.png)

## No Address Available Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event that critical address information is not available from the enrollment system DST will display “No address available” in the patient demographics section. DST will not be able to determine VA facilities in the drive time area and DST will also display an error message in the Community Care section indicating that eligibility information cannot be determined. Please contact the Enterprise Service Desk at 855-NSD-HELP (673-4357) to enter a ticket to contact the enrollment system to update the address information.

<span id="_Toc48311236" class="anchor"></span>Figure 42: No Address Available Error

![](decision-support-tool-dst-user-guide/044.png)

## Previously Sent to HSRM Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the Consult has been released to HSRM an ICR consult factor is inserted in the Consult comments. When this consult factor is present, DST will notify you that the consult has been sent to HSRM. The consult will no longer be editable from DST so all DST controls will be read-only.

<span id="_Toc48311237" class="anchor"></span>Figure 43: Provider: Previously Sent to HSRM Message

![](decision-support-tool-dst-user-guide/045.png)

<span id="_Toc48311238" class="anchor"></span>Figure 44: Admin VCCPE: Previously Sent to HSRM Message

![](decision-support-tool-dst-user-guide/046.png)

# Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym | Definition                                                                |
|---------|---------------------------------------------------------------------------|
| API     | Application Program Interface                                             |
| BMI     | Best Medical Interest                                                     |
| CC      | Community Care                                                            |
| CD2     | Critical Decision Point \#2                                               |
| CDW     | Corporate Data Warehouse                                                  |
| CHAMPVA | Civilian Health and Medical Program of the Department of Veterans Affairs |
| CID     | Clinically Indicated Date                                                 |
| CITI    | CHAMPVA In-house Treatment Initiative                                     |
| CPRS    | Computerized Patient Record System                                        |
| DST     | Decision Support Tool                                                     |
| EMR     | Electronic Medical Record                                                 |
| ES      | Enrollment System                                                         |
| ICN     | Integration Control Number                                                |
| ID      | Identification                                                            |
| IFC     | Inter-Facility Consults                                                   |
| MH      | Mental Health                                                             |
| MVI     | Master Veteran Index                                                      |
| OIT     | Office of Information and Technology                                      |
| PC      | Primary Care                                                              |
| PII     | Personally Identifiable Information                                       |
| PPMS    | Provider Profile Management System                                        |
| SEOC    | Standardized Episodes of Care                                             |
| SSN     | Social Security Number                                                    |
| SSOi    | Single Sign On Integration                                                |
| TBD     | To Be Determined                                                          |
| VA      | Department of Veterans Affairs                                            |
| VCCP    | Veteran Community Care Program                                            |
| VCCPE   | Veteran Community Care Program Eligibility                                |
| VDL     | VA Software Document Library                                              |
| VHA     | Veterans Health Administration                                            |
| VIP     | Veteran-focused Integrated Process                                        |
| VistA   | Veterans Health Information Systems and Technology Architecture           |

Table used for formatting, only.Revision History, including date of changes, version number, description of change, and author of change.