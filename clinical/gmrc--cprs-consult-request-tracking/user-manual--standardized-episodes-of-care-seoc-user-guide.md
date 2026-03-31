---
title: Standardized Episodes of Care (SEOC) User Guide
doc_type: UG
doc_label: User Guide
doc_layer: plain
doc_subject: Standardized Episodes of Care (SEOC)
app_code: GMRC
app_name: "CPRS: Consult/Request Tracking"
section: CLI
app_status: active
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
  - seoc
  - table
  - contents
  - span
  - care
  - class
  - export
  - standardized
  - guide
  - updated
page_count: 0
word_count: 5594
section_count: 14
table_count: 4
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: December 2023
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking/seoc_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking/seoc_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=62"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Care Coordination (CC)

  Standardized Episodes of Care (SEOC)

  Software Version 1.21

  Database User Guide
---

![](standardized-episodes-of-care-seoc-user-guide/001.png)

December 2023

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
<td>12/11/2023</td>
<td>18.0</td>
<td><p>Updated for v1.21.0:</p>
<ul>
<li><p>Updated version number.</p></li>
<li><p>Updated screens throughout the document to match the new UI.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>08/21/2023</td>
<td>17.0</td>
<td><p>Updated for v1.20.0:</p>
<ul>
<li><p>Updated version number.</p></li>
</ul>
<p>Updated screens throughout the document to match the new UI.</p></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>04/24/2023</td>
<td>16.0</td>
<td><p>Updated for v1.19.0:</p>
<ul>
<li><p>Updated version number.</p></li>
<li><p>Updated screens throughout the document to match the new UI.</p></li>
<li><p>Added Exporting Data section.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>01/24/2023</td>
<td>15.0</td>
<td><p>Updated for v1.18.0:</p>
<p>Updated version number.</p></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>10/24/2022</td>
<td>14.0</td>
<td><p>Updated for v1.17.0:</p>
<ul>
<li><p>Updated version number.</p></li>
<li><p>Updated screens and definitions to include the Filter by Service Line menu.</p></li>
<li><p>Updated screens and definitions to include the Filter by Billing Code field.</p></li>
</ul></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>06/29/2022</td>
<td>13.0</td>
<td><p>Updated for v1.16.0:</p>
<p>Updated version number.</p></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>01/21/2022</td>
<td>12.0</td>
<td><p>Updated for v1.14.0:</p>
<p>Updated version number.</p></td>
<td>VetsEZ</td>
</tr>
<tr class="even">
<td>08/31/2021</td>
<td>11.0</td>
<td><p>Updated for v1.12.0:</p>
<p>Updated screen captures.</p></td>
<td>VetsEZ</td>
</tr>
<tr class="odd">
<td>02/05/2021</td>
<td>10.0</td>
<td><p>Updated for v1.11.1:</p>
<p>Updated screen captures.</p></td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>10/28/2020</td>
<td>9.0</td>
<td><p>Updated for v1.11:</p>
<ul>
<li><p>Updated screen captures.</p></li>
<li><p>Updated Acronyms and Abbreviations section.</p></li>
</ul></td>
<td>AbleVets</td>
</tr>
<tr class="odd">
<td>01/13/2020</td>
<td>8.0</td>
<td><p>Updated for v1.10:</p>
<ul>
<li><p>Updated document name to <em>Care Coordination (CC) Standardized Episodes of Care (SEOC) v1.10 Database User Guide</em>.</p></li>
<li><p>Removed all Admin content. The Admin content can now be found in the new <em>Care Coordination (CC) Standardized Episodes of Care (SEOC) v1.10 Administrative User Guide</em>.</p></li>
<li><p>Updated screen captures.</p></li>
</ul></td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>9/18/2019</td>
<td>7.0</td>
<td><p>Updated for v1.9:</p>
<ul>
<li><p>Updated screen captures.</p></li>
<li><p>Added section: Export the SEOC Data to a JSON File.</p></li>
<li><p>Added section: Export the SEOC PreCert Data to a JSON File.</p></li>
<li><p>Added section: Sort SEOCs Alphabetically by Name.</p></li>
<li><p>Added section: Invalid Characters.</p></li>
<li><p>Added section: Show Invalid Characters.</p></li>
<li><p>Added section: Fix Invalid Characters.</p></li>
<li><p>Added section: Revert a Date Hold SEOC back to In-Progress.</p></li>
<li><p>Updated definitions for the Standardized Episodes of Care table fields.</p></li>
<li><p>Updated the steps in the JSON Instructions section.</p></li>
</ul></td>
<td>AbleVets</td>
</tr>
<tr class="odd">
<td>06/11/2019</td>
<td>6.0</td>
<td><p>Updated for v1.8:</p>
<ul>
<li><p>Draft New SEOC section</p></li>
<li><p>Activate an In-Progress SEOC section</p></li>
<li><p>Delete an In-Progress SEOC section</p></li>
<li><p>Revert SEOC to In-Progress section</p></li>
</ul></td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>3/05/2019</td>
<td>5.0</td>
<td>Updated for v1.7.<br />
Added Managing Billing Codes, Updated screen captures to reflect v1.7</td>
<td>AbleVets</td>
</tr>
<tr class="odd">
<td>1/02/2019</td>
<td>4.0</td>
<td>Updated for v1.6<br />
Updated screen captures, Added Exporting SEOC Data section, added Appendix A.</td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>10/04/2018</td>
<td>3.0</td>
<td>Updated for v1.5<br />
Included Manage Users features: Filter by Role, Filter by Name, Delete Selected User, Edit Selected User, and Add New User.</td>
<td>AbleVets</td>
</tr>
<tr class="odd">
<td>09/25/2018</td>
<td>2.0</td>
<td>Finalized for Software Version 1.0.04.1</td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>09/14/2018</td>
<td>1.3</td>
<td>Finalized for Build 5</td>
<td>AbleVets</td>
</tr>
<tr class="odd">
<td>08/09/2018</td>
<td>1.2</td>
<td>Updated for Build 5</td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>07/20/2018</td>
<td>1.1</td>
<td>Updated for Software Version 1.0.4<br />
Build 4</td>
<td>AbleVets</td>
</tr>
<tr class="odd">
<td>06/25/2018</td>
<td>1.0</td>
<td>Initial Draft Delivery</td>
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
  - [National Service Desk and Organizational Contacts](#national-service-desk-and-organizational-contacts)
- [System Summary](#system-summary)
  - [System Configuration](#system-configuration)
  - [Data Flows](#data-flows)
  - [User Access Levels](#user-access-levels)
  - [Continuity of Operation](#continuity-of-operation)
- [Getting Started](#getting-started)
  - [Logging On](#logging-on)
  - [System Menu](#system-menu)
  - [Changing User ID and Password](#changing-user-id-and-password)
  - [Exit System](#exit-system)
- [Using the Software](#using-the-software)
  - [View SEOCs](#view-seocs)
    - [View a Selected SEOC](#view-a-selected-seoc)
    - [View Filtered SEOCs](#view-filtered-seocs)
    - [Print a SEOC](#print-a-seoc)
    - [Track Version Changes](#track-version-changes)
  - [Exporting Data](#exporting-data)
    - [Export the SEOC Data to an Excel File](#export-the-seoc-data-to-an-excel-file)
    - [Export the SEOC Data to a JSON File](#export-the-seoc-data-to-a-json-file)
    - [Export the VA PreCert Webpage Data to a JSON File](#export-the-va-precert-webpage-data-to-a-json-file)
- [Troubleshooting](#troubleshooting)
- [Acronyms and Abbreviations](#acronyms-and-abbreviations)
- [Appendix A: JSON Instructions](#appendix-a-json-instructions)
The Care Coordination (CC) Standardized Episodes of Care (SEOC) is a reference database for managing care bundles for use by Veterans Information Systems and Technology Architecture (VistA) and other Department of Veterans Affairs (VA) systems. Services are grouped together within the SEOC system into bundles so that clinicians can add these bundles to patients consult records in a standardized fashion, reducing the amount of time spent manually entering consult instructions, and providing uniformity among the patient records and across facilities for how patient care is prescribed for similar complaints.
These bundles group together one or more services that are preselected for different specialties to be added to the consult records. In addition, the clinician is provided with information regarding prescribing rules and preauthorization requirements, so they can make the most informed decisions regarding patient care.
Additionally, SEOC data will be accessible outside of the VistA/Computerized Patient Record System (CPRS) system so that users of downstream applications will be accessing the centralized data, and SEOC descriptions, reducing the chances of disconnects.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to provide instruction for utilizing the SEOC application to standardize and streamline consult management for Community Care.

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Care Coordination (CC) Standardized Episodes of Care (SEOC) v1.21 Database User Guide* will provide explanations of each screen and of all user interface options within the context of an easy-to-understand demonstration data scenario.

This document is also designed to provide the user with screen-by-screen “how to” information on the usage of CC SEOC.

### Organization of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Section 1: Introduction

The Introduction section provides the purpose of this manual, an overview of the SEOC software, an overview of the software used, project references, contact information for the user to seek additional information, and an acronyms and abbreviations list for this manual.

Section 2: System Summary

The System Summary section provides a graphical representation of the equipment, communication, and networks used by the system, user access levels, how the software will be accessed, and contingencies and alternative modes of operation.

Section 3: Getting Started

Information for the Getting Started section provides a general walk-through of the system from initiation through exit, enabling the user to understand the sequence and flow of the system.

Section 4: Using the Software

This section gives the user the “how to” information to use SEOC, including many step-by-step procedures.

Section 5: Troubleshooting

This section provides troubleshooting for the SEOC user.

Section 6: Acronyms and Abbreviations

This section provides a list of acronyms and abbreviations found in this document.

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide was written with the following assumed experience/skills of the audience:

- The SEOC user has been assigned the user role of SEOC Analyst. The SEOC Analyst can view Active or Discontinued SEOCs on the Home Page. These users can View, Print, or Track Version Changes on selected SEOCs.
- User has Google Chrome and/or Microsoft Edge installed on their machine.
- The SEOC user has basic knowledge of the SEOC system (such as the use of commands, menu options, and navigation tools).
- The SEOC user has been provided the appropriate active roles, menus, and security keys required for the SEOC User Interface (UI).
- The SEOC user is using SEOC to perform their daily consult creation workflow and perform the required SEOC functions.
- The SEOC user has validated access to the SEOC UI.
- The SEOC user has been provided training on the SEOC UI and has reviewed the User Guide.
- SEOC Content Authors: The SEOC Content Authors are responsible for creating and update the content within the SEOC repository using the SEOC UI. These users are required to VA access rights and privileges and will sign on to the SEOC application using their Single Sign-On Integration (SSOI) credentials (typically their Personal Identification Verification (PIV) and access code).
- CPRS Clinicians that are responsible for documenting patient consult records. These clinicians utilize the SEOC content as part of their daily consult creation workflow such that they will add a SEOC bundle to the patient consult record which will provide for a standardized documentation and care plan approach across the VA for these consults.

### Coordination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One Consult - Consult Toolbox 1.9.02 and above and the HealthShare Referral Manager (HSRM) depend on the availability of the SEOC System. Consult Toolbox 1.9.02 requires active SEOCs whereas HSRM requires active and discontinued SEOCs. Coordination between the One Consult – Consult Toolbox, HSRM, and SEOC team is necessary with any updates to SEOC.

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual uses several methods to highlight different aspects of the material.

| Symbol                                                                                                                                                                                                                                 | Description                                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| ![](standardized-episodes-of-care-seoc-user-guide/002.png) | CAUTION: Used to caution the reader to take special notice of critical information. |

Table 2: SEOC Error Codes with Descriptions

1.  Notes are used to inform the reader of general information including references to additional reading material.

### References and Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Readers who wish to learn more about CPRS and CC SEOC should consult the VA Software Document Library.

## National Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For issues related to the CC SEOC that cannot be resolved by this manual or the site administrator, please contact the National Service Desk.

# System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There was an immediate need to provide clinicians the ability to quickly and consistently add care bundles to a patient’s consult record within VistA. SEOC provides this feature for a higher level of uniformity in patient care, easier access to appropriate services, based on initial diagnoses, and the ability to better control care costs. SEOC allows clinicians to enhance the coordination of care for the Veteran.

The system contains SEOCs, or care bundles, that clinicians or other designated individuals can assign to VA patients. These bundles allow for the consistent use of procedures when certain conditions are diagnosed. This consistency allows the VA to effectively manage patient care and provides easier traceability.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SEOC System is designed to be a simple reference database with a supporting SEOC Application Program Interface (API) and UI layer. The SEOC system comprises three application tiers as shown below.

<span id="_Ref500326578" class="anchor"></span>Figure 1: Overview of SEOC System

![](standardized-episodes-of-care-seoc-user-guide/003.png)

The first tier is the Data Tier. This tier contains SEOC data. SEOC uses Microsoft Structured Query Language (SQL) Server is the database. SEOC data consists of reference data, such as SEOC name, associated procedures, associated Current Procedural Terminology (CPT) codes, procedure durations, etc. Additionally, user role information is maintained within the tables, but no passwords or other credentials are stored. No Protected Health Information (PHI) or Personally Identifiable Information (PII) is stored in the database. SEOC data is associated with patient data in the VistA consult record.

The second tier is the Abstraction Tier. This tier acts as the data broker for the SEOC system. It is a Representational State Transfer (REST) API, built as a microservice hosted on container infrastructure (Docker Container). The API itself is built on the Spring Model-View-Controller (MVC) framework. The API receives web API calls that are forwarded to the database appropriately. Consuming applications are able to query the SEOC system through the SEOC REST API but will not be able to perform updated operations. The SEOC UI uses certificates to authenticate with the SEOC REST API to allow data modification within the SEOC system by authenticated users. Users are authenticated using SSOI. Additionally, a VistA/MUMPS patch is created to insert the SEOC associations into File \# 123.

The third and final tier is the Presentation Tier. This tier consists of the SEOC UI, which provides a user interface for approved, authenticated users to maintain the SEOC collection. This application is a web application built as a microservice hosted on container infrastructure (Docker Container). The UI is built using the React.js JavaScript framework for web applications.

## Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc153958502" class="anchor"></span>Figure 2: SEOC Data Flow Diagram

![](standardized-episodes-of-care-seoc-user-guide/004.png)

## User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SEOC user profiles comprise of the following “types of users”:

- SEOC Content Authors: The SEOC Content Authors are responsible for creating and update the content within the SEOC repository using the SEOC UI. These users are required to VA access rights and privileges and will sign on to the SEOC application using their SSOI credentials (typically their PIV and access code).
- CPRS Clinicians that are responsible for documenting patient consult records. These clinicians utilize the SEOC content as part of their daily consult creation workflow such that they will add a SEOC bundle to the patient consult record which will provide for a standardized documentation and care plan approach across the VA for these consults.
- SEOC data is also accessible to other external consumers in the future (in addition to CPRS users). The SEOC API is a RESTFul API that other (to be determined) users will have access to use.

## Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SEOC system is maintained by Enterprise Operations (EO). The continuity of operations is managed by EO.

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides a general walkthrough of CC SEOC from initiation through exit.

## Logging On

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CC SEOC is accessed using the VA SSOi log in.

<span id="_Toc153958503" class="anchor"></span>Figure 3: VA Single Sign-On for SEOC

![](standardized-episodes-of-care-seoc-user-guide/005.png)

2.  After 15 minutes of inactivity the system will automatically log you out. After 13 minutes of inactivity the system will prompt you to extend your session.

<span id="_Toc153958504" class="anchor"></span>Figure 4: 2 Minutes Until Session Expires Warning

![](standardized-episodes-of-care-seoc-user-guide/006.png)

## System Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Standardized Episodes of Care dashboard offers several features: Filter by Billing Code, Filter by Service Line, Filter by Status, Filter by Name, View Selected SEOCs, and Export SEOCs. The home page also displays the username and user role at the top right of the page.

<span id="_Toc153958505" class="anchor"></span>Figure 5: Standardized Episodes of Care Dashboard

![](standardized-episodes-of-care-seoc-user-guide/007.png)

| ![](standardized-episodes-of-care-seoc-user-guide/008.png) | CAUTION: To view the list of SEOCs using a keyboard interface with assistive technology, you will need to use the “Tab” key to navigate through the list. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|

Standardized Episodes of Care table fields:

- Service Line – A broad category of care for the services and procedures included which is intended to be used to group and filter SEOCs for easier accessibility. A standardized three-letter abbreviation of the service line is included at the beginning of the SEOC ID.
- SEOC Name – A unique title that categorizes a SEOC by specialty/subspecialty or area of clinical practice.
- Version – The version number of the SEOC. The version number is formatted A.B.C where the first digit will be 1, the second digit is the number of published SEOCs in the same Category of Care when a new SEOC is activated, and the third digit is a serialized revision number.
- Effective Date –The date the SEOC status was made from In-Progress to Active.
- End Date –The date the SEOC status was discontinued.
- Status –The SEOC statuses are as follows:
- Active: When a SEOC is Active, it will be available for all end users (e.g. API users, scheduling, payment, and auditing purposes).
- Date Hold: When the SEOC status is Date Hold, it is pending and set for activation on a designated future date. This status is only available for SEOC Administrative users for editing purposes.
- Discontinued: When a SEOC is Discontinued, read-only users will not have access to the discontinued SEOC in the SEOC Database or the scheduling interface. However, the discontinued version will still be available for payment and auditing purposes. Discontinued SEOCs will remain in the SEOC database for up to six (6) years in the central repository.
- In-Progress: The SEOC is available for editing purposes by the Administrators and Authors prior to activation. These SEOCs will not be available via SEOC Database API.

## Changing User ID and Password

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you need to change your user password, you will need to contact your local PIV office.

## Exit System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are finished working, log out of VA Single Sign-On and close any secure sessions that may still be open by selecting the Logout button.

# Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CC SEOC provides user functionality for the following items:

- View Selected SEOC
- View a Selected SEOC
- Search for a SEOC by Name
- Sort SEOCs Alphabetically by Name
- Filter SEOCs by Status
- Print a SEOC
- Track Version Changes
- Export SEOC
- Export the SEOC Data to an Excel File
- Export the SEOC Data to a JSON File
- Export the VA PreCert Webpage Data to a JSON File

## View SEOCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### View a Selected SEOC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To view a SEOC from the SEOC list, follow the steps listed below:

1.  From the SEOC home page, select the SEOC you would like to view.
1.  Select View Selected SEOC or tap the selected SEOC to view. The View SEOC page displays.

<span id="_Toc153958506" class="anchor"></span>Figure 6: View SEOC (1 of 2)

![](standardized-episodes-of-care-seoc-user-guide/009.png)

<span id="_Toc153958507" class="anchor"></span>Figure 7: View SEOC (2 of 2)

![](standardized-episodes-of-care-seoc-user-guide/010.png)

### View Filtered SEOCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SEOC allows you to filter SEOCs by billing code, service line, status, and name. You also have the option to sort the displayed columns by selecting the arrow to the right of the column heading name.

#### Filter SEOCs by Billing Code

To filter the list of SEOCs by billing code, follow the steps listed below:

3.  Those with a Viewer role are unable to filter SEOCs by billing code.
1.  From the SEOC Admin home page, enter the billing code in the Billing CodeFilter field.

<span id="_Toc117157090" class="anchor"></span>Figure 8: Billing Code Filter Field

![](standardized-episodes-of-care-seoc-user-guide/011.png)

1.  Select the Search button. The SEOC list refreshes to display the SEOCs list filtered by the billing code type.

<span id="_Toc117157091" class="anchor"></span>Figure 9: Billing Code Filter Search Results

![](standardized-episodes-of-care-seoc-user-guide/012.png)

#### Filter SEOCs by Service Line

To filter the list of SEOCs by Service Line, follow the steps listed below:

1.  From the SEOC Admin home page, select Filter by Service Line menu.

<span id="_Toc117157092" class="anchor"></span>Figure 10: by Service Line Filter Menu Options

![](standardized-episodes-of-care-seoc-user-guide/013.png)

2.  From the list of options, select one of the service line types to filter by. The SEOC list refreshes to display the SEOCs list filtered by the selected service line type.

#### Filter SEOCs by Status

To filter the list of SEOCs by status, follow the steps listed below:

1.  From the SEOC home page, select Filter By Status menu.

<span id="_Toc153958511" class="anchor"></span>Figure 11: Filter by Status Menu Options

![](standardized-episodes-of-care-seoc-user-guide/014.png)

2.  From the list of options select to filter by: All, Active, Date Hold, Discontinued, or In-Progress. The SEOC list refreshes to display the status filtered by.

#### Filter SEOCs by Name

To filter the SEOCs by name, follow the steps listed below:

1.  From the SEOC home page, enter the name of the SEOC in the Filter by Name (contains) field.

<span id="_Toc153958512" class="anchor"></span>Figure 12: Filter by Name Field

![](standardized-episodes-of-care-seoc-user-guide/015.png)

3.  Select the Search button. The Filter by Name Results display.

<span id="_Toc16600023" class="anchor"></span>Figure 13: Filter by Name Results

![](standardized-episodes-of-care-seoc-user-guide/016.png)

### Print a SEOC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To print a SEOC, follow the steps listed below:

1.  From the SEOC home page, select the SEOC you would like to print.
4.  Select View Selected SEOC or tap the selected SEOC to view, the View SEOC page displays.
5.  Select Print SEOC. The printed SEOC will display in another window. Print or save using local browser capabilities.

<span id="_Toc153958514" class="anchor"></span>Figure 14: Printed SEOC Window

![](standardized-episodes-of-care-seoc-user-guide/017.png)

### Track Version Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To track the version changes of a SEOC, follow the steps listed below:

1.  From the SEOC home page, select a SEOC with a previous version.
6.  Select View Selected SEOC or tap the selected SEOC to view, the View SEOC page displays.
7.  Select the Track Version Changes button when it becomes active. The Track Version Changes page will display.

<span id="_Toc153958515" class="anchor"></span>Figure 15: Track Version Changes Page

![](standardized-episodes-of-care-seoc-user-guide/018.png)

8.  Select the Previous Version button. The changes for the previous version will be shown. If the previous version is the first version of this SEOC, no changes will be displayed.
9.  Select the Next Version button. The changes for the next version will be shown.
10. Select the Print SEOC button. The Print SEOC page will display with the current changes.

<span id="_Toc16600017" class="anchor"></span>Figure 16: Print SEOC from Track Version Changes Page

![](standardized-episodes-of-care-seoc-user-guide/019.png)

4.  By default, Internet Explorer 11 will not print the red and green background colors. To print the red and green background colors, check the Print Background Colors and Images box in the Page Setup dialog from the Print menu.

## Exporting Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

5.  Those with a Viewer role are unable to export data.

### Export the SEOC Data to an Excel File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To export the SEOC Data, follow the steps listed below:

1.  As an Analyst, Coder, Publisher, or Administrator on the SEOC Admin home page, select Export. The Export SEOC window displays with the Export SEOCs tab open by default.

<span id="_Toc143114988" class="anchor"></span>Figure 17: Export SEOC Window

![](standardized-episodes-of-care-seoc-user-guide/020.png)

3.  Select Excel from the Export SEOCs section.
6.  Excel exports have a limit of 1,048,576 rows by 16,384 columns. If you think you may exceed this, select JSON instead. The steps to export to a JSON file can be found in the Export the SEOC Data to a JSON File section.
4.  Select which status options to include in the export and select Continue. The Export SEOC Data Properties display.
5.  Select which properties to include in the export and select Export. The SEOC data will be exported to an Excel file that you will need to save.
7.  If no SEOCs match the export criteria, the following message will display “No SEOCs found that match your export request, please select different options to export SEOCs.”.

### Export the SEOC Data to a JSON File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To export the SEOC Data, follow the steps listed below:

1.  As an Analyst, Coder, Publisher, or Administrator on the SEOC Admin home page, select Export. The Export SEOC window displays with the Export SEOCs tab open by default.

<span id="_Toc143114989" class="anchor"></span>Figure 18: Export SEOC Window

![](standardized-episodes-of-care-seoc-user-guide/021.png)

6.  Select JSON from the Export SEOC Data section.
7.  Select which status options to include in the export and select Continue. The SEOC data will be exported to a JSON file that you will need to save.
8.  If no SEOCs match the export criteria, the following message will display “No SEOCs found that match your export request, please select different options to export SEOCs.”.
9.  Please refer to Appendix A for additional steps on converting the JSON file into an Excel file.

### Export the VA PreCert Webpage Data to a JSON File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For all users who can Export SEOC Data, the SEOC Admin UI also allows them to export the data required for the VA PreCert Webpage.

To export the SEOC PreCert Data, follow the steps listed below:

1.  As an Analyst, Coder, Publisher, or Administrator on the SEOC Admin home page, select Export. The Export SEOC window displays with the Export SEOCs tab open by default.

<span id="_Toc143114990" class="anchor"></span>Figure 19: Export SEOC Window

![](standardized-episodes-of-care-seoc-user-guide/022.png)

8.  Select the Export VA Precert Webpage Data tab.

<span id="_Toc143114991" class="anchor"></span>Figure 20: Export VA Precert Webpage Data Tab

![](standardized-episodes-of-care-seoc-user-guide/023.png)

9.  Select Export. The SEOC data will be exported to a JSON file that you will need to save.

<span id="_Toc143114992" class="anchor"></span>Figure 21: SEOC Export Completed Confirmation Message

![](standardized-episodes-of-care-seoc-user-guide/024.png)

10. Select OK. The SEOC data will be exported to a JSON file that you will need to save.
10. Please refer to Appendix A for additional steps on converting the JSON file into an Excel file.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users may encounter the following errors while using the SEOC UI.

| Error Code | Description      |
|------------|------------------|
| 204        | No Content Found |
| 401        | Unauthorized     |
| 403        | Forbidden        |
| 404        | Not Found        |

# Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym | Definition                                                      |
|---------|-----------------------------------------------------------------|
| API     | Application Program Interface                                   |
| CC      | Care Coordination                                               |
| CCAD    | Community Care Agile Development                                |
| CPRS    | Computerized Patient Record System                              |
| CPT     | Current Procedural Terminology                                  |
| HSRM    | HealthShare Referral Manager                                    |
| EO      | Enterprise Operations                                           |
| JSON    | JavaScript Object Notification                                  |
| MVC     | Model-View-Controller                                           |
| NSD     | National Service Desk                                           |
| OIT     | Office of Information and Technology                            |
| PHI     | Protected Health Information                                    |
| PII     | Personally Identifiable Information                             |
| PIV     | Personal Identification Verification                            |
| REST    | Representational State Transfer                                 |
| SEOC    | Standardized Episode of Care                                    |
| SQL     | Structured Query Language                                       |
| SSOI    | Single Sign-On Integration                                      |
| UI      | User Interface                                                  |
| VA      | Department of Veterans Affairs                                  |
| VDL     | VA Software Document Library                                    |
| VIP     | Veteran-focused Integrated Process                              |
| VistA   | Veterans Health Information Systems and Technology Architecture |

# Appendix A: JSON Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To convert the SEOC JSON file to an Excel file, follow the steps listed below:

1.  Open a blank workbook in Excel.
11. Select the Data tab, then Get Data \> From File \> From JSON. The Import Data window displays.

<span id="_Toc133231226" class="anchor"></span>Figure 22: Import Data Window

![](standardized-episodes-of-care-seoc-user-guide/025.png)

12. Select the JSON file you downloaded and select Import. Excel will open the file in the Query Editor.

<span id="_Toc133231227" class="anchor"></span>Figure 23: Query Editor

![](standardized-episodes-of-care-seoc-user-guide/026.png)

13. Select the List header to the right of SEOCs to display a list of records.

<span id="_Toc133231228" class="anchor"></span>Figure 24: List of Records

![](standardized-episodes-of-care-seoc-user-guide/027.png)

14. From the Transform tab, select the Convert To Table icon and select OK. The To Table dialog box displays.

<span id="_Toc133231229" class="anchor"></span>Figure 25: To Table Dialog Box

![](standardized-episodes-of-care-seoc-user-guide/028.png)

15. From the To Table dialog box keep the default selections and select OK.
16. Select on the expand icon (\<-\|\|-\>) to the right of the Column1 header to display the Search Columns to Expand dialog box.

<span id="_Toc133231230" class="anchor"></span>Figure 26: Search Columns to Expand Dialog Box

![](standardized-episodes-of-care-seoc-user-guide/029.png)

17. De-select the Use original column name as prefix check box.
18. Select OK.
19. Select on the expand icon (\<-\|\|-\>) to the right of the SEOC header to display the Search Columns to Expand dialog box.

<span id="_Toc133231231" class="anchor"></span>Figure 27: Search Columns to Expand

![](standardized-episodes-of-care-seoc-user-guide/030.png)

20. Uncheck the Use original column name as prefix check box.
21. Select OK. The fields in the SEOC table will be expanded to columns as shown below.

<span id="_Toc133231232" class="anchor"></span>Figure 28: Expanded SEOC Fields

![](standardized-episodes-of-care-seoc-user-guide/031.png)

22. Scroll right to the services column, select on the expand icon, and select Expand to New Rows to display the records.

<span id="_Toc133231233" class="anchor"></span>Figure 29: Expand to New Rows Menu Option

![](standardized-episodes-of-care-seoc-user-guide/032.png)

23. Select the expand icon again and press OK to expand the Payable Services fields into columns.

<span id="_Toc133231234" class="anchor"></span>Figure 30: Payable Services Columns

![](standardized-episodes-of-care-seoc-user-guide/033.png)

24. Scroll right to the billingCodes column and repeat the last two steps to expand the Billing Code fields into columns.

<span id="_Toc133231235" class="anchor"></span>Figure 31: Billing Code Columns

![](standardized-episodes-of-care-seoc-user-guide/034.png)

25. Optional - Repeat the last two steps again for the serviceHptcs column if you want to see the cross-walked HPTCs that are sent for each Payable Service.
26. Scroll right and repeat the last two steps again for the hptcs column to expand the HPTC fields that were assigned to each SEOC.

<span id="_Toc133231236" class="anchor"></span>Figure 32: Expanded HPTC Fields

![](standardized-episodes-of-care-seoc-user-guide/035.png)

27. Select the Close & Load option at the left of the ribbon to create load the imported data into a spreadsheet tab.

<span id="_Toc133231237" class="anchor"></span>Figure 33: Imported Data

![](standardized-episodes-of-care-seoc-user-guide/036.png)